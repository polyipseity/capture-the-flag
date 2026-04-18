---
name: AI agent playbook (capture-the-flag)
description: Concrete, actionable rules for automated/codegen agents working in this repository.
applyTo: "**"
---

# AI agent playbook — focused, safe, verifiable ✅

*Async helpers in this repository use AnyIO/Asyncer; do not import `asyncio`.*

This file tells automated/code-generation agents exactly what they may change, how to verify results, and where to look for repository-specific conventions.

- Repository purpose: a curated collection of CTF writeups, PoC scripts and small tooling — not a production library.

What you may change (no human sign-off required):

- Documentation and instructions: `AGENTS.md`, `README.md`, `.github/*` (prompts, instructions).
- Tests and tooling under `tests/` (add/modify to cover behaviour changes).
- Small utilities or scripts under the repository root (run `bun run check` and add tests).

What requires human review or is disallowed:

- Decrypting or modifying `*.7z.gpg` archives or changing `.gpg-id`.
- CI permission or workflow-privilege changes.
- Large binary uploads or changes to `competitions/` that affect archived assets.

Must-follow verification steps (run before committing):

1. bun run format
2. bun run check
3. bun run test

Key repository rules & examples (do this exactly):

- Add `__all__` as a `tuple[str, ...]` in any new Python module and put it after top-level imports — see `tests/test_module_exports.py`.
- Every `def`/`class` (including nested functions/methods) must have a docstring — enforced by `tests/test_docstrings.py`.
- Line length is 88 characters (see `pyproject.toml` / Ruff).
- `competitions/` is excluded from ty/ruff checks — treat it as content, not library code.

How to add a new competition (example):

- Create `competitions/<YEAR>/<Name>/writeups.md`.
- Put PoC scripts inside that folder and include small fixtures if needed.
- For large assets create `archive.7z`, encrypt with `.gpg-id`, commit only `archive.7z.gpg`.
- Update `competitions/<YEAR>/writeups.md` index and run the verification steps above.

CI & tooling — quick facts:

- CI runs `bun run test` and `bun run check` (see `.github/workflows/ci.yml`).
- Use `bun` for repo-level tasks; `uv` is used for Python environment control. Prefer `uv run -m <module>` over `python -m <module>` when invoking Python modules so the locked `uv` environment is respected (example: `uv run -m pytest`).

If you need to change repository policy or CI behaviour, open an issue and propose a PR with tests.

Please keep edits small, covered by tests, and explicitly reference the files above when you change repository behaviour.
