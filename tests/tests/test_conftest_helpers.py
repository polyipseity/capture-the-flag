"""Tests for shared helper fixture wiring through :mod:`tests.conftest`."""

from ..utils import GlobPatternParser, collect_glob_patterns

"""Public API of this test module (none)."""
__all__ = ()


def test_policy_glob_parser_names_are_deterministic(
    policy_glob_parser_names: tuple[str, ...],
) -> None:
    """Parser names exposed by conftest should be stable and fully qualified."""
    assert policy_glob_parser_names == (
        "tests.test_docstrings._iter_glob_patterns",
        "tests.test_module_exports._iter_glob_patterns",
        "tests.test_git_executable._iter_glob_patterns",
    )


def test_policy_glob_parsers_parse_consistently(
    policy_glob_parsers: tuple[GlobPatternParser, ...],
) -> None:
    """All shared parser fixtures should parse the same gitignore-style spec."""
    spec = "tests/**/*.py\n!tests/**/legacy_*.py\n"
    expected = [("tests/**/*.py", False), ("tests/**/legacy_*.py", True)]

    for parser in policy_glob_parsers:
        assert collect_glob_patterns(parser, spec) == expected
