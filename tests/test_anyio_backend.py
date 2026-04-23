"""Tests that verify the AnyIO pytest plugin is set up correctly.

These helpers exercise the fixtures defined in ``tests/conftest.py`` and
provide a simple sanity check that the backend is configured as expected.
"""

from . import conftest as tests_conftest
from .utils import GlobPatternParser

"""Public API of the anyio backend tests."""
__all__ = ()


def test_anyio_backend_name(anyio_backend_name: str):
    """The backend name fixture should always be ``"asyncio"``."""
    assert anyio_backend_name == "asyncio"


def test_anyio_backend_options(anyio_backend_options: dict[str, object]):
    """The options fixture should enable uvloop."""
    assert anyio_backend_options.get("use_uvloop") is True


def test_anyio_backend_fixture_shape(
    anyio_backend: tuple[str, dict[str, object]],
) -> None:
    """The backend fixture should be a ``(name, options)`` tuple."""
    backend_name, backend_options = anyio_backend
    assert backend_name == "asyncio"
    assert isinstance(backend_options, dict)
    assert backend_options.get("use_uvloop") is True


def test_pytest_plugins_wires_shared_test_utils_module() -> None:
    """The test suite should load shared fixtures from ``tests.utils``."""
    assert tests_conftest.pytest_plugins == ("tests.utils",)


def test_policy_glob_parsers_are_available_through_conftest(
    policy_glob_parsers: tuple[GlobPatternParser, ...],
    policy_glob_parser_names: tuple[str, ...],
) -> None:
    """Conftest should expose typed parser fixtures from the shared utils module."""
    assert len(policy_glob_parsers) == 3
    assert all(
        name.endswith("._iter_glob_patterns") for name in policy_glob_parser_names
    )
