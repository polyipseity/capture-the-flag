"""Tests for helper functions used by policy-enforcement tests."""

import ast
import asyncio
import stat
from os import PathLike

import pytest
from anyio import Path

from .. import test_docstrings as docstrings_module
from .. import test_git_executable as git_executable_module
from .. import test_module_exports as exports_module
from ..utils import GlobPatternParser, build_ast_module, collect_glob_patterns

"""Public API of this test module (none)."""
__all__ = ()


def test_iter_glob_patterns_handles_comments_and_negations(
    policy_glob_parsers: tuple[GlobPatternParser, ...],
) -> None:
    """All helper glob parsers should preserve include/exclude ordering."""
    spec = """
    # comment
    tests/**/*.py

    !tests/**/legacy_*.py
    scripts/*.py
    """
    expected = [
        ("tests/**/*.py", False),
        ("tests/**/legacy_*.py", True),
        ("scripts/*.py", False),
    ]

    for parser in policy_glob_parsers:
        assert collect_glob_patterns(parser, spec) == expected


def test_iter_glob_patterns_ignores_empty_negation_entries(
    policy_glob_parsers: tuple[GlobPatternParser, ...],
) -> None:
    """Parsers should skip invalid bare-negation lines and blank patterns."""
    spec = """
    !
    !!
    tests/**/*.py
    !
    """

    expected = [("!", True), ("tests/**/*.py", False)]
    for parser in policy_glob_parsers:
        assert collect_glob_patterns(parser, spec) == expected


def test_exports_helper_accepts_assign_and_annassign_tuples() -> None:
    """``_has_all_tuple`` should accept tuple-based ``__all__`` assignments."""
    plain_node = build_ast_module('__all__ = ("alpha", "beta")\n')
    annotated_node = build_ast_module('__all__: tuple[str, ...] = ("alpha",)\n')

    assert exports_module._has_all_tuple(plain_node) == (True, "OK")
    assert exports_module._has_all_tuple(annotated_node) == (True, "OK")


def test_exports_helper_rejects_list_and_non_string_members() -> None:
    """``_has_all_tuple`` should report malformed ``__all__`` definitions."""
    list_node = build_ast_module('__all__ = ["alpha"]\n')
    mixed_node = build_ast_module('__all__ = ("alpha", 1)\n')
    missing_node = build_ast_module("def x():\n    pass\n")

    assert exports_module._has_all_tuple(list_node) == (
        False,
        "__all__ must be a tuple (not a list or other type)",
    )
    assert exports_module._has_all_tuple(mixed_node) == (
        False,
        "__all__ must contain only string constants",
    )
    assert exports_module._has_all_tuple(missing_node) == (False, "__all__ not found")


def test_docstring_helpers_extract_exports_and_find_definitions() -> None:
    """Docstring helper functions should resolve exports and target nodes."""
    node = build_ast_module(
        '''
        CONST = 1

        def alpha():
            """doc"""

        class Beta:
            """doc"""

        __all__ = ("alpha", "Beta", "CONST")
        '''
    )

    assert docstrings_module._extract_all_tuple(node) == ("alpha", "Beta", "CONST")

    alpha_node = docstrings_module._find_def_node(node, "alpha")
    assert isinstance(alpha_node, ast.FunctionDef)

    beta_node = docstrings_module._find_def_node(node, "Beta")
    assert isinstance(beta_node, ast.ClassDef)

    const_node = docstrings_module._find_def_node(node, "CONST")
    assert isinstance(const_node, ast.Assign)

    assert docstrings_module._find_def_node(node, "missing") is None


def test_docstring_helper_rejects_non_tuple_exports() -> None:
    """``_extract_all_tuple`` should return ``None`` when exports are not tuples."""
    list_node = build_ast_module('__all__ = ["alpha"]\n')
    assert docstrings_module._extract_all_tuple(list_node) is None


def test_docstring_helper_rejects_non_constant_export_members() -> None:
    """``_extract_all_tuple`` should reject tuples containing non-constants."""
    dynamic_node = build_ast_module(
        """
        name = "alpha"
        __all__ = (name,)
        """
    )
    assert docstrings_module._extract_all_tuple(dynamic_node) is None


def test_assignment_docstring_requires_immediately_preceding_literal() -> None:
    """Assignment docs should only count when a string literal is immediate."""
    module = build_ast_module(
        '''
        """module doc"""
        FLAG = True
        helper = 1
        """documented var"""
        DOCUMENTED = 2
        '''
    )

    assignments = list(docstrings_module._iter_top_level_assignments(module))
    assert assignments[0][0] == "FLAG"
    assert (
        docstrings_module._get_assignment_docstring(
            assignments[0][1],
            assignments[0][2],
            is_module=assignments[0][3],
        )
        is None
    )

    documented = assignments[2]
    assert documented[0] == "DOCUMENTED"
    assert (
        docstrings_module._get_assignment_docstring(
            documented[1],
            documented[2],
            is_module=documented[3],
        )
        == "documented var"
    )


def test_iter_function_and_class_nodes_finds_nested_members() -> None:
    """Recursive definition traversal should include nested defs/classes."""
    node = build_ast_module(
        '''
        class Outer:
            """doc"""

            def method(self):
                """doc"""

                def inner():
                    """doc"""

                class Nested:
                    """doc"""

        async def top_async():
            """doc"""
        '''
    )

    definitions = list(docstrings_module._iter_function_and_class_nodes(node))
    names = [getattr(definition, "name", "") for definition in definitions]
    assert names == ["Outer", "method", "inner", "Nested", "top_async"]


@pytest.mark.anyio
async def test_get_candidate_files_applies_exclusion_patterns(
    monkeypatch: pytest.MonkeyPatch,
    scripts_dir_lock: "asyncio.Lock",
) -> None:
    """Candidate file collection should respect include and exclude rules.

    Uses an async lock to serialize access to the scripts/ directory,
    preventing race conditions with test_top_level_scripts_executable.
    """
    async with scripts_dir_lock:
        root = Path(git_executable_module.__file__).parent.parent
        scripts_dir = root / "scripts"

        scripts_dir_preexisted = await scripts_dir.exists()
        if not scripts_dir_preexisted:
            await scripts_dir.mkdir(parents=True, exist_ok=True)

        keep_path = scripts_dir / "__tmp_exec_keep__.sh"
        drop_path = scripts_dir / "__tmp_exec_drop__.sh"
        await keep_path.write_text("echo keep\n")
        await drop_path.write_text("echo drop\n")

        # Set executable bit to comply with test_top_level_scripts_executable checks
        for path in (keep_path, drop_path):
            st = await path.stat()
            await path.chmod(st.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

        monkeypatch.setattr(
            git_executable_module,
            "_GLOB_SPEC",
            "scripts/__tmp_exec_*.sh\n!scripts/__tmp_exec_drop__.sh\n",
        )

        try:
            candidates = [
                path async for path in git_executable_module._get_candidate_files()
            ]
            assert keep_path in candidates
            assert drop_path not in candidates
        finally:
            for path in (keep_path, drop_path):
                try:
                    await path.unlink()
                except FileNotFoundError:
                    pass

            if not scripts_dir_preexisted:
                try:
                    await scripts_dir.rmdir()
                except OSError:
                    pass


@pytest.mark.anyio
async def test_git_mode_raises_for_path_outside_repo(tmp_path: PathLike[str]) -> None:
    """``git_mode`` should raise when given a path outside the repository root."""
    external_file = Path(tmp_path) / "outside.txt"
    await external_file.write_text("outside")

    with pytest.raises(ValueError):
        await git_executable_module.git_mode(external_file)


@pytest.mark.anyio
async def test_git_mode_returns_none_when_run_process_fails(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """`git_mode` should gracefully return ``None`` when subprocess calls fail."""

    async def _raise_run_process(*_args: object, **_kwargs: object) -> None:
        """Raise a deterministic error to exercise exception handling."""
        raise RuntimeError("simulated process failure")

    monkeypatch.setattr(git_executable_module, "run_process", _raise_run_process)
    assert await git_executable_module.git_mode(Path(__file__)) is None
