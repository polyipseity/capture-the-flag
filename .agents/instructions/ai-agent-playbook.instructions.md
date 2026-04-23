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

For test-heavy or policy changes, run a targeted pytest selection first,
then the full suite above.

Concrete test execution order (required for policy/tooling edits):

- Run targeted tests for changed scope first (for fast feedback):
  - `uv run -m pytest tests/tests/test_utils.py`
  - `uv run -m pytest tests/tests/test_policy_helpers.py`
  - `uv run -m pytest tests/test_anyio_backend.py`
- Run full regression suite: `bun run test`.
- Run formatting + lint/type checks: `bun run format && bun run check`.
- Do not stop at happy-path coverage: add failure-path assertions for helper
  and policy tests whenever behavior is touched.

Key repository rules & examples (do this exactly):

- Add `__all__` as a `tuple[str, ...]` in any new Python module and put it after top-level imports — see `tests/test_module_exports.py`.
- Every `def`/`class` (including nested functions/methods) must have a docstring — enforced by `tests/test_docstrings.py`.
- Line length is 88 characters (see `pyproject.toml` / Ruff).
- `competitions/` is excluded from ty/ruff checks — treat it as content, not library code.

Testing architecture expectations (mirror `self/ledger` quality bar):

- Keep top-level AST policy tests for exports/docstrings and extend them with
  focused regression cases when bugs are fixed.
- Keep `tests/conftest.py` as single source of truth for AnyIO backend and
  plugin wiring.
- Put reusable typed fixtures/helpers in `tests/utils.py` and validate them in
  `tests/tests/test_utils.py`.
- Mirror source/tooling layout under `tests/` where practical.
- Require `__all__ = ()` in test modules and preserve explicit docstrings.
- New behavioral tests should include both success and failure-path assertions.

Typed determinism rules:

- Keep tests deterministic (no network, no wall-clock dependence, no random
  data without fixed seed).
- Annotate `tmp_path` as `PathLike[str]`.
- Use `os.fspath(path_like)` for path-like conversion when string is needed.
- Shared fixtures belong in `tests/utils.py` and must be wired through
  `tests/conftest.py` via `pytest_plugins`.

When changing test policy, do not weaken existing checks. If policy behavior
must change, replace coverage with equally strict or stricter assertions and
document the rationale.

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
