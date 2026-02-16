---
name: Core workflows (capture-the-flag)
description: Common developer workflows for adding competitions, testing, and CI.
applyTo: "**"
---

# Core workflows 🔁

Install & prepare

```bash
# preferred: pnpm (runs `prepare` automatically which syncs Python dev extras via `uv`)
pnpm install

# alternative: run Python environment sync directly with uv
uv sync --locked --all-extras --dev
```

Note: when running Python modules prefer `uv run -m <module>` (e.g. `uv run -m pytest`) instead of `python -m <module>` so the locked `uv` environment is used.

Format, check, test

```bash
pnpm run format    # formatting
pnpm run check     # linters & type checks (competitions/ excluded)
pnpm run test      # pytest
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
pnpm run format && pnpm run check && pnpm run test
git commit -m "feat(competitions): add ExampleCTF 2026 writeup"
```

CI

- `.github/workflows/ci.yml` runs the same checks as local `pnpm run check` and `pnpm run test`.
- Keep CI changes minimal and add tests for any behavioural changes.

When to write tests

- Add tests for tooling, parsers, or scripts placed under `tests/`.
- Do not add tests for static writeups; instead add small smoke-check scripts if needed.
