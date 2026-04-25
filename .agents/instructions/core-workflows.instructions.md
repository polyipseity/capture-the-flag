---
name: Core workflows (capture-the-flag)
description: Common developer workflows for adding competitions, testing, and CI.
applyTo: "**"
---

# Core workflows 🔁

_When writing tools or tests, follow the project’s async convention: use AnyIO/Asyncer and do not import `asyncio` directly._

Install & prepare

```bash
# preferred: bun (runs `prepare` automatically which syncs Python dev extras via `uv`)
bun install

# alternative: run Python environment sync directly with uv
uv sync --locked
```

Note: when running Python modules prefer `uv run -m <module>` (e.g. `uv run -m pytest`) instead of `python -m <module>` so the locked `uv` environment is used.

Format, check, test

```bash
bun run format    # formatting
bun run check     # linters & type checks (competitions/ excluded)
bun run test      # pytest
```

Add a competition (example)

```bash
mkdir -p competitions/2026/ExampleCTF
cp -r template-writeup.md competitions/2026/ExampleCTF/writeups.md
# add PoC scripts under competitions/2026/ExampleCTF/
# archive + encrypt large assets
7z a archive.7z assets/
# encrypt for recipients listed in .gpg-id (asymmetric GPG)
# POSIX example:
gpg --encrypt --recipient "$(cat .gpg-id)" --output archive.7z.gpg archive.7z
# PowerShell example:
# gpg --encrypt --recipient (Get-Content .gpg-id -Raw).Trim() --output archive.7z.gpg archive.7z

# commit the encrypted archive (archive.7z.gpg)
git add competitions/2026/ExampleCTF
bun run format && bun run check && bun run test
git commit -m "feat(competitions): add ExampleCTF 2026 writeup"
```

CI

- `.github/workflows/ci.yml` runs the same checks as local `bun run check` and `bun run test`.
- Keep CI changes minimal and add tests for any behavioural changes.

When to write tests

- Add tests for tooling, parsers, or scripts placed under `tests/`.
- Do not add tests for static writeups; instead add small smoke-check scripts if needed.

Concrete test workflow for code/tooling changes

1. Add or update tests first where practical (TDD-friendly).
2. Run a focused subset for quick iteration (for example a single module under
   `tests/tests/` or one policy test file).
3. Run full suite: `bun run test`.
4. Run full checks: `bun run format && bun run check`.
5. Confirm policy tests remain strict: `test_module_exports`, `test_docstrings`,
   `test_git_executable`, and AnyIO backend/plugin wiring checks.

Deterministic rigor expectations for tests

- Prefer typed tests: annotate `tmp_path` as `PathLike[str]` and prefer
  `os.fspath(path_like)` when string conversion is required.
- Keep helper fixtures centralized in `tests/utils.py` and loaded through
  `tests/conftest.py` (`pytest_plugins = ("tests.utils",)`).
- Mirror helper verification under `tests/tests/`.
- Every new test module must include a module docstring and `__all__ = ()`.
- For each changed helper/policy function, add both success and failure-path
  assertions to prevent regression-by-silence.
