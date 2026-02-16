---
name: Agent quickstart (capture-the-flag)
description: Minimal checklist for agents and contributors working in this workspace.
applyTo: "**"
---

# Agent quickstart — capture-the-flag ✅

Short checklist to start working safely in this project.

1. Ensure your editor is opened at the project root (the workspace is this folder).
2. Install & prepare (preferred): `pnpm install` — `pnpm install` runs the `prepare` script automatically, which calls `uv sync` to install Python dev extras. Use `uv` directly when needed: `uv sync --locked --all-extras --dev`. When running Python modules prefer `uv run -m <module>` (for example `uv run -m pytest`) instead of `python -m <module>` so the locked `uv` environment is used.
3. Format & check locally: `pnpm run format && pnpm run check`
4. Run tests: `pnpm run test`

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
  1. `pnpm run format` — fixes/normalises formatting
  2. `pnpm run check` — type/lint checks (note: `competitions/` skipped)
  3. `pnpm run test` — pytest (use `uv run --locked pytest` or `uv run -m pytest` for direct runs; prefer `uv run -m` over `python -m`).
- Code-style/quality quick rules:
  - Add `__all__` tuple and module-level docstring to new Python modules (see `tests/test_module_exports.py`).
  - Every `def`/`class` must have a docstring (even nested functions) — enforced by tests.
  - Line length: 88 characters (configured in `pyproject.toml`).
- Commit & PR behaviour for agents:
  - Use Conventional Commits. See `.github/prompts/commit-staged.prompt.md` (automation will commit staged changes with no confirmation).
  - Include tests for behavioural changes; update `competitions/*/writeups.md` indices when adding competitions.

If anything is ambiguous, open a short issue/PR and request human review rather than making large unilateral changes.
