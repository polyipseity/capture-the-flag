---
name: Commit convention (capture-the-flag)
description: Commit & PR guidance for competitions and tooling changes.
applyTo: "**"
---

# Commit & PR conventions 📝

_The codebase is async-capable and uses AnyIO/Asyncer helpers; avoid importing `asyncio` directly when touching Python code._

- Follow Conventional Commits (enforced via `commitlint`).
- Suggested scopes: `competitions`, `pocs`, `tools`, `tests`.

Examples:

- `feat(competitions): add writeup for Pearl CTF 2024`
- `chore(competitions): add encrypted archive for TAMUctf 2024`
- `fix(pocs): correct exploit for xyz challenge`

PR checklist:

- All formatting/lint checks pass (`bun run format && bun run check`).
- Tests pass (`bun run test`) for any code changes.
- For tooling/policy changes, include targeted helper tests and full-suite test results.
- New tests should cover happy paths and failure paths; do not weaken existing policy checks.
- Keep tests deterministic and typed for policy/tooling edits:
  - annotate `tmp_path` as `PathLike[str]`
  - include module docstring + `__all__ = ()` in new test modules
  - keep shared fixtures in `tests/utils.py` and wiring in `tests/conftest.py`
- `competitions/` index files updated where applicable.
- No secrets committed.

Recommended verification log in PR/commit description (for policy changes):

1. Targeted pytest files run first (list exact file paths).
2. `bun run test` pass summary.
3. `bun run format && bun run check` pass summary.
