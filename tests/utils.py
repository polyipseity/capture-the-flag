"""Test fixtures used across the test suite.

This module provides shared helpers and fixtures for tests that need
``anyio.Path``-like async file objects or controlled module execution.

Type hints:
- The file factory accepts ``kind`` (``"disk"`` or ``"memory"``) and an
  argument that is path-like for disk-backed files or an initial ``str`` for
  in-memory files.
"""

import ast
import runpy
import sys
from abc import ABC, abstractmethod
from collections.abc import Callable, Iterable
from dataclasses import dataclass
from os import PathLike, fspath
from textwrap import dedent
from types import ModuleType
from typing import Any, Literal, Protocol, Self, cast, overload

import asyncer
import pytest
from anyio import Path

from tests import test_docstrings as docstrings_module
from tests import test_git_executable as git_executable_module
from tests import test_module_exports as exports_module

"""Public symbols exported by this module."""
__all__ = (
    "AsyncFileFactory",
    "GlobPatternParser",
    "PolicyModuleBundle",
    "RunModuleHelper",
    "async_file_factory",
    "build_ast_module",
    "collect_glob_patterns",
    "policy_glob_parsers",
    "policy_module_bundle",
    "run_module_helper",
)


def build_ast_module(source: str) -> ast.Module:
    """Parse ``source`` into an :class:`ast.Module` after de-indenting.

    This keeps helper-focused tests compact and readable while still testing
    real AST behavior.
    """
    return ast.parse(dedent(source))


class GlobPatternParser(Protocol):
    """Callable parser for gitignore-style glob specs used in policy tests."""

    __name__: str
    __module__: str

    def __call__(self, spec: str) -> Iterable[tuple[str, bool]]:
        """Parse ``spec`` and yield ``(pattern, is_exclude)`` entries."""
        ...


@dataclass(frozen=True, slots=True)
class PolicyModuleBundle:
    """Typed references to policy-test modules exposing shared helpers."""

    docstrings: ModuleType
    exports: ModuleType
    git_executable: ModuleType


def collect_glob_patterns(
    parser: GlobPatternParser, spec: str
) -> list[tuple[str, bool]]:
    """Return deterministic list output from a glob parser callable."""
    return list(parser(spec))


@pytest.fixture
def policy_module_bundle() -> PolicyModuleBundle:
    """Return typed module bundle for policy helper tests.

    Importing here keeps helper wiring centralized in ``tests.utils`` while
    avoiding unnecessary imports in modules that do not use these fixtures.
    """
    return PolicyModuleBundle(
        docstrings=docstrings_module,
        exports=exports_module,
        git_executable=git_executable_module,
    )


@pytest.fixture
def policy_glob_parsers(
    policy_module_bundle: PolicyModuleBundle,
) -> tuple[GlobPatternParser, ...]:
    """Return all policy glob parsers in a deterministic tuple order."""
    return (
        cast(GlobPatternParser, policy_module_bundle.docstrings._iter_glob_patterns),
        cast(GlobPatternParser, policy_module_bundle.exports._iter_glob_patterns),
        cast(
            GlobPatternParser,
            policy_module_bundle.git_executable._iter_glob_patterns,
        ),
    )


class AsyncFileBase(ABC):
    """Abstract async file interface used by test helpers."""

    @abstractmethod
    async def read(self) -> str:
        """Read and return the file's text content asynchronously."""
        ...

    @abstractmethod
    async def write(self, data: str) -> int:
        """Write ``data`` and return number of characters written."""
        ...

    @abstractmethod
    async def seek(self, offset: int, whence: int = 0) -> int:
        """Seek operation for tests; returns new position."""
        ...

    @abstractmethod
    async def truncate(self) -> None:
        """Truncate operation for tests."""
        ...

    @abstractmethod
    async def __aenter__(self) -> Self:
        """Enter async context and return the file object."""
        ...

    @abstractmethod
    async def __aexit__(
        self, exc_type: type | None, exc: BaseException | None, tb: object | None
    ) -> bool:
        """Exit async context; return ``False`` for default exception handling."""
        ...


class AsyncPathBase(ABC):
    """Abstract base class for async path-like wrappers used in tests."""

    last_written: str | None

    @abstractmethod
    async def open(
        self,
        mode: str = "r+t",
        encoding: str = "UTF-8",
        errors: str = "strict",
        newline: str | None = None,
    ) -> AsyncFileBase:
        """Open and return an :class:`AsyncFileBase` implementation."""
        ...


class AsyncFileFactory(Protocol):
    """Callable factory returning async path-like objects for tests."""

    @overload
    def __call__(self, kind: Literal["disk"], arg: PathLike[str]) -> AsyncPathBase:
        """Create disk-backed async file path object."""
        ...

    @overload
    def __call__(self, kind: Literal["memory"], arg: str) -> AsyncPathBase:
        """Create memory-backed async file path object."""
        ...

    def __call__(
        self, kind: Literal["disk", "memory"], arg: PathLike[str] | str
    ) -> AsyncPathBase:
        """Return an async path-like object for tests."""
        ...


@pytest.fixture
def async_file_factory() -> AsyncFileFactory:
    """Return a factory producing disk-backed and memory-backed async files."""

    class DiskAsyncFilePath(AsyncPathBase):
        """AnyIO-like path wrapper backed by a real filesystem path."""

        class AsyncFile(AsyncFileBase):
            """A minimal async file wrapper around a real file path."""

            def __init__(self, path: "DiskAsyncFilePath") -> None:
                """Store reference to the path wrapper."""
                self._path = path

            async def read(self) -> str:
                """Read and return text from disk."""
                return await self._path._path.read_text()

            async def write(self, data: str) -> int:
                """Write ``data`` to disk and record last-written text."""
                self._path.last_written = data
                await self._path._path.write_text(data)
                return len(data)

            async def seek(self, offset: int, whence: int = 0) -> int:
                """No-op seek for tests returning 0."""
                return 0

            async def truncate(self) -> None:
                """No-op truncate for tests."""
                return None

            async def __aenter__(self) -> Self:
                """Return the file object on async context entry."""
                return self

            async def __aexit__(
                self,
                exc_type: type | None,
                exc: BaseException | None,
                tb: object | None,
            ) -> bool:
                """No special cleanup on async context exit."""
                return False

        def __init__(self, path: PathLike[str]) -> None:
            """Initialize disk-backed wrapper with filesystem path."""
            self._path = Path(path)
            self.last_written: str | None = None

        async def open(
            self,
            mode: str = "r+t",
            encoding: str = "UTF-8",
            errors: str = "strict",
            newline: str | None = None,
        ) -> AsyncFileBase:
            """Return async file wrapper bound to this disk path."""
            return self.AsyncFile(self)

    class InMemoryAsyncFilePath(AsyncPathBase):
        """AnyIO-like path wrapper storing text in memory."""

        class AsyncFile(AsyncFileBase):
            """A minimal async file wrapper around in-memory text."""

            def __init__(self, path: "InMemoryAsyncFilePath") -> None:
                """Store reference to the in-memory path wrapper."""
                self._path = path

            async def read(self) -> str:
                """Return current in-memory text."""
                return self._path._text

            async def write(self, data: str) -> int:
                """Replace in-memory text and record last-written value."""
                self._path.last_written = data
                self._path._text = data
                return len(data)

            async def seek(self, offset: int, whence: int = 0) -> int:
                """No-op seek for tests returning 0."""
                return 0

            async def truncate(self) -> None:
                """No-op truncate for tests."""
                return None

            async def __aenter__(self) -> Self:
                """Return the file object on async context entry."""
                return self

            async def __aexit__(
                self,
                exc_type: type | None,
                exc: BaseException | None,
                tb: object | None,
            ) -> bool:
                """No special cleanup on async context exit."""
                return False

        def __init__(self, text: str) -> None:
            """Initialize in-memory wrapper with initial text."""
            self._text = text
            self.last_written: str | None = None

        async def open(
            self,
            mode: str = "r+t",
            encoding: str = "UTF-8",
            errors: str = "strict",
            newline: str | None = None,
        ) -> AsyncFileBase:
            """Return async file wrapper bound to this in-memory text."""
            return self.AsyncFile(self)

    @overload
    def factory(kind: Literal["disk"], arg: PathLike[str]) -> AsyncPathBase:
        """Overload for disk-backed factory calls."""
        ...

    @overload
    def factory(kind: Literal["memory"], arg: str) -> AsyncPathBase:
        """Overload for memory-backed factory calls."""
        ...

    def factory(
        kind: Literal["disk", "memory"], arg: PathLike[str] | str
    ) -> AsyncPathBase:
        """Create a test-friendly async path object.

        ``kind`` must be either ``"disk"`` or ``"memory"``.
        """
        if kind == "disk":
            if not isinstance(arg, PathLike):
                raise TypeError("disk factory requires a os.PathLike")
            return DiskAsyncFilePath(fspath(arg))
        if kind == "memory":
            if not isinstance(arg, str):
                raise TypeError("memory factory requires initial text")
            return InMemoryAsyncFilePath(arg)
        raise ValueError(kind)

    return factory


class RunModuleHelper(ABC):
    """ABC for a helper that runs a module and reports whether it ran."""

    @abstractmethod
    def __call__(self, module_name: str, argv: list[str]) -> dict[str, bool]:
        """Run ``module_name`` as ``__main__`` with ``argv`` and return status."""
        ...


@pytest.fixture
def run_module_helper(monkeypatch: pytest.MonkeyPatch) -> RunModuleHelper:
    """Return helper that runs module as script with a fake ``asyncer.runnify``."""

    class _RunModule(RunModuleHelper):
        """Helper implementation for deterministic module execution in tests."""

        def __init__(self, monkeypatch: pytest.MonkeyPatch) -> None:
            """Store monkeypatch instance for later patching."""
            self._monkeypatch = monkeypatch

        def __call__(self, module_name: str, argv: list[str]) -> dict[str, bool]:
            """Execute module and return ``{"ran": bool}`` state."""
            called: dict[str, bool] = {"ran": False}

            def fake_runnify(
                async_func: Callable[..., Any], *_args: object, **_kwargs: object
            ) -> Callable[..., Any]:
                """Mark module as run and return a wrapper closing any coroutine."""
                called["ran"] = True

                def wrapper(*args: Any, **kwargs: Any) -> None:
                    """Invoke async function and close coroutine to avoid warnings."""
                    try:
                        coro = async_func(*args, **kwargs)
                        coro.close()
                    except Exception:
                        pass

                return wrapper

            self._monkeypatch.setattr(asyncer, "runnify", fake_runnify)

            previous_argv = sys.argv[:]
            try:
                sys.argv[:] = argv

                for module in (module_name, "scripts"):
                    sys.modules.pop(module, None)

                runpy.run_module(module_name, run_name="__main__")
            finally:
                sys.argv[:] = previous_argv

            return called

    return _RunModule(monkeypatch)
