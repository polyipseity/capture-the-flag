"""Tests for fixtures and helpers defined in :mod:`tests.utils`."""

import sys
from os import PathLike
from typing import Literal, cast

import pytest
from anyio import Path

from ..utils import (
    AsyncFileFactory,
    GlobPatternParser,
    RunModuleHelper,
    collect_glob_patterns,
)

"""Public API of this test module (none)."""
__all__ = ()


def test_collect_glob_patterns_works_for_all_policy_parsers(
    policy_glob_parsers: tuple[GlobPatternParser, ...],
) -> None:
    """All policy parsers should produce identical include/exclude outputs."""
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


@pytest.mark.anyio
async def test_async_file_factory_disk_and_memory(
    async_file_factory: AsyncFileFactory, tmp_path: PathLike[str]
) -> None:
    """Disk-backed and memory-backed wrappers should read/write correctly."""
    file_path = Path(tmp_path) / "file.txt"
    disk = async_file_factory("disk", file_path)
    await file_path.write_text("hello")

    async with await disk.open(mode="r+t") as fh:
        assert await fh.read() == "hello"
        await fh.write("world")
        assert disk.last_written == "world"

    memory = async_file_factory("memory", "init")
    async with await memory.open() as fh:
        assert await fh.read() == "init"
        await fh.write("new")
        assert memory.last_written == "new"


@pytest.mark.anyio
async def test_async_file_factory_seek_truncate_and_context(
    async_file_factory: AsyncFileFactory, tmp_path: PathLike[str]
) -> None:
    """Seek/truncate/context-manager methods should match documented behavior."""
    file_path = Path(tmp_path) / "file2.txt"
    disk = async_file_factory("disk", file_path)
    await file_path.write_text("hello")

    async with await disk.open(mode="r+t") as fh:
        assert await fh.seek(10) == 0
        assert (await fh.truncate()) is None

    memory = async_file_factory("memory", "abc")
    async with await memory.open() as fh:
        assert await fh.seek(2) == 0
        assert (await fh.truncate()) is None


def test_async_file_factory_errors(async_file_factory: AsyncFileFactory) -> None:
    """Invalid factory arguments should raise clear errors."""
    with pytest.raises(TypeError):
        async_file_factory("disk", cast(PathLike[str], "not-a-path"))
    with pytest.raises(TypeError):
        async_file_factory("memory", cast(str, 123))
    with pytest.raises(ValueError):
        async_file_factory(cast(Literal["memory"], "unknown"), "x")


@pytest.mark.anyio
async def test_run_module_helper_runs_and_handles_close_exception(
    tmp_path: PathLike[str],
    monkeypatch: pytest.MonkeyPatch,
    run_module_helper: RunModuleHelper,
) -> None:
    """The run helper should patch ``asyncer.runnify`` and execute the module."""
    module_path = Path(tmp_path) / "mod_run_close.py"
    await module_path.write_text(
        """import asyncer
asyncer.runnify(lambda: None)()
"""
    )

    monkeypatch.syspath_prepend(tmp_path)
    ran = run_module_helper("mod_run_close", ["mod_run_close"])
    assert ran["ran"] is True


@pytest.mark.anyio
async def test_run_module_helper_sets_sys_argv_and_runs_module(
    tmp_path: PathLike[str],
    monkeypatch: pytest.MonkeyPatch,
    run_module_helper: RunModuleHelper,
) -> None:
    """The run helper should pass argv and support repeated fresh execution."""
    module_path = Path(tmp_path) / "mod_run_args.py"
    await module_path.write_text(
        """import asyncer
import pathlib
import sys

p = pathlib.Path(__file__).with_suffix('.argv')
p.write_text(' '.join(sys.argv))
asyncer.runnify(lambda: None)()
"""
    )

    monkeypatch.syspath_prepend(tmp_path)

    ran = run_module_helper("mod_run_args", ["mod_run_args", "A", "B"])
    assert ran["ran"] is True

    argv_file = Path(tmp_path) / "mod_run_args.argv"
    assert await argv_file.exists()
    assert await argv_file.read_text() == "mod_run_args A B"

    ran_again = run_module_helper("mod_run_args", ["mod_run_args", "X"])
    assert ran_again["ran"] is True
    assert await argv_file.read_text() == "mod_run_args X"


@pytest.mark.anyio
async def test_run_module_helper_restores_sys_argv_when_module_raises(
    tmp_path: PathLike[str],
    monkeypatch: pytest.MonkeyPatch,
    run_module_helper: RunModuleHelper,
) -> None:
    """Even when execution fails, helper should restore ``sys.argv``."""
    module_path = Path(tmp_path) / "mod_run_error.py"
    await module_path.write_text('raise RuntimeError("boom")\n')
    monkeypatch.syspath_prepend(tmp_path)

    original_argv = sys.argv[:]
    with pytest.raises(RuntimeError, match="boom"):
        run_module_helper("mod_run_error", ["mod_run_error", "arg"])
    assert sys.argv == original_argv


@pytest.mark.anyio
async def test_run_module_helper_reports_false_when_runnify_not_called(
    tmp_path: PathLike[str],
    monkeypatch: pytest.MonkeyPatch,
    run_module_helper: RunModuleHelper,
) -> None:
    """If a module never calls ``asyncer.runnify``, helper should report ``ran`` False."""
    module_path = Path(tmp_path) / "mod_no_runnify.py"
    await module_path.write_text("VALUE = 1\n")
    monkeypatch.syspath_prepend(tmp_path)

    result = run_module_helper("mod_no_runnify", ["mod_no_runnify"])
    assert result == {"ran": False}


@pytest.mark.anyio
async def test_run_module_helper_tolerates_non_coroutine_return_from_runnify(
    tmp_path: PathLike[str],
    monkeypatch: pytest.MonkeyPatch,
    run_module_helper: RunModuleHelper,
) -> None:
    """Wrapper should ignore non-coroutine returns while still marking the run path."""
    module_path = Path(tmp_path) / "mod_non_coro.py"
    await module_path.write_text(
        """import asyncer
asyncer.runnify(lambda: 1)()
"""
    )
    monkeypatch.syspath_prepend(tmp_path)

    result = run_module_helper("mod_non_coro", ["mod_non_coro"])
    assert result == {"ran": True}
