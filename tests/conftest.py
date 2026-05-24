"""Shared pytest configuration for asynchronous tests.

The AnyIO plugin is configured here; tests across the repository simply
depend on the ``anyio_backend`` fixture or use ``@pytest.mark.anyio``.
"""

import asyncio
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from .utils import GlobPatternParser

"""Public API of this test configuration module (empty)."""
__all__ = ()

"""`pytest_plugins` is a special variable recognized by pytest to load fixtures from other modules."""
pytest_plugins = ("tests.utils",)


@pytest.fixture
def anyio_backend() -> tuple[str, dict[str, bool]]:
    """Return the desired backend for AnyIO-based tests.

    Using a tuple with ``use_uvloop=True`` requests uvloop explicitly.
    AnyIO still handles platform differences (winloop on Windows) automatically.
    """
    return ("asyncio", {"use_uvloop": True})


@pytest.fixture
def policy_glob_parser_names(
    policy_glob_parsers: tuple["GlobPatternParser", ...],
) -> tuple[str, ...]:
    """Return fully-qualified parser names loaded through shared test fixtures."""
    return tuple(
        f"{parser.__module__}.{parser.__name__}" for parser in policy_glob_parsers
    )


# Lock for synchronizing tests that modify the scripts/ directory
"""Async lock to serialize access to the scripts/ directory.

Tests that create files in the repository's scripts/ directory should use
this lock through the scripts_dir_lock fixture to avoid race conditions with
parallel test execution. This ensures tests like
test_get_candidate_files_applies_exclusion_patterns and
test_top_level_scripts_executable don't interfere with each other.
"""
_scripts_dir_lock = asyncio.Lock()


@pytest.fixture
async def scripts_dir_lock() -> asyncio.Lock:
    """Async lock to serialize access to the scripts/ directory.

    Tests that create files in the repository's scripts/ directory should use
    this fixture to avoid race conditions with parallel test execution. This
    ensures tests like test_get_candidate_files_applies_exclusion_patterns and
    test_top_level_scripts_executable don't interfere with each other.
    """
    return _scripts_dir_lock
