---
name: Agent quickstart (capture-the-flag)
description: Minimal checklist for agents and contributors working in this workspace.
applyTo: "**"
---

# Agent quickstart — capture-the-flag ✅

_This submodule’s codebase uses AnyIO/Asyncer for async helpers; avoid importing `asyncio` directly._

Short checklist to start working safely in this project.

1. Ensure your editor is opened at the project root (the workspace is this folder).
2. Install & prepare (preferred): `bun install` — `bun install` runs the `prepare` script automatically, which calls `uv sync` to install Python dev extras. Use `uv` directly when needed: `uv sync --locked`. When running Python modules prefer `uv run -m <module>` (for example `uv run -m pytest`) instead of `python -m <module>` so the locked `uv` environment is used.
3. Format & check locally: `bun run format && bun run check`
4. Run tests: `bun run test`

For Python/test-tooling changes, run one targeted test selection first
(for quick feedback), then run the full `bun run test` suite.

Required deterministic test workflow (concrete):

- Run focused tests for touched modules first (examples):
  - `uv run -m pytest tests/tests/test_utils.py`
  - `uv run -m pytest tests/tests/test_policy_helpers.py`
  - `uv run -m pytest tests/test_anyio_backend.py`
- Run full suite: `bun run test`.
- Run repository checks: `bun run format && bun run check`.
- If policy/helper behavior changed, add at least one failure-path assertion
  per changed helper and keep strictness equivalent or stronger.

Notes:

- `competitions/` is excluded from linting/type-checking by design — treat it as curated, not as library code.
- Ask before adding large private archives or changing CI/workflows.

## For automated/codegen agents (short playbook)

- Allowed quick tasks:
  - Fix failing tests in `tests/` and adjust `pyproject.toml`/`package.json` scripts when necessary.
  - Update docs (`AGENTS.md`, `README.md`, `.github/*`) and add small helper scripts.
  - Add or adjust unit tests for tooling changes in `tests/`.
- Disallowed or require human sign-off:
  - Decrypting, editing, or re-encrypting `*.7z.gpg` archives.
  - Making CI workflow permission changes or exposing secrets.
  - Large refactors of `competitions/` content without human review.
- Required pre-commit checks (agent MUST run):
  1. `bun run format` — fixes/normalises formatting
  2. `bun run check` — type/lint checks (note: `competitions/` skipped)
  3. `bun run test` — pytest (use `uv run --locked pytest` or `uv run -m pytest` for direct runs; prefer `uv run -m` over `python -m`).
- Code-style/quality quick rules:
  - Add `__all__` tuple and module-level docstring to new Python modules (see `tests/test_module_exports.py`).
  - Every `def`/`class` must have a docstring (even nested functions) — enforced by tests.
  - Line length: 88 characters (configured in `pyproject.toml`).
  - Keep tests typed and deterministic:
    - annotate `tmp_path` as `PathLike[str]`
    - prefer `os.fspath(path_like)` for path-like to string conversion
    - include module docstring + `__all__ = ()` in new test modules
  - Follow ledger-style test architecture:
    - Keep AnyIO backend + plugin wiring in `tests/conftest.py`.
    - Place typed shared helpers/fixtures in `tests/utils.py`.
    - Add focused helper tests under `tests/tests/`.
    - Include both happy and failure-path scenarios for new behavior.
- Commit & PR behaviour for agents:
  - Use Conventional Commits. See `.agents/prompts/commit-staged.prompt.md` (automation will commit staged changes with no confirmation).
  - Include tests for behavioural changes; update `competitions/*/writeups.md` indices when adding competitions.

If anything is ambiguous, open a short issue/PR and request human review rather than making large unilateral changes.
