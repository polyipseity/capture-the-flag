# AGENTS — capture-the-flag

A focused repository for CTF writeups, challenge code, and archived artifacts.
This `AGENTS.md` and the companion `.github/instructions/` documents tell contributors and automation how
to work with the `competitions/` workspace safely and consistently.

## Quick reference ✅

- `competitions/` — per-year competition folders, `writeups.md`, challenge code, encrypted archives
- `tests/` — unit/integration tests for tooling (add tests here for new tools)
- `pyproject.toml` / `package.json` — toolchain and scripts (format, check, test)
- `.github/workflows/` — CI (runs `pnpm run test` / `pnpm run check`)

## Fast start (local)

1. Ensure your editor is opened at the project root (the workspace is this folder).
2. Install & prepare environment — prefer `pnpm` (see note):
   - Preferred (recommended): `pnpm install`  # `pnpm install` runs the `prepare` script automatically
     - The `prepare` script in `package.json` calls `uv sync` to install Python development extras.
   - Alternative (direct `uv`): `uv sync --locked --all-extras --dev`
3. Validate and run tests: `pnpm run format && pnpm run check && pnpm run test`

> Run these before opening a PR — CI runs the same checks.

### Tooling note — `pnpm` vs `uv`

- `pnpm` is the repository's primary package manager for installs and scripts. Use `pnpm` for end-to-end workflows (it will invoke `uv` for Python deps via `prepare`).
- `uv` is available for direct, reproducible Python environment operations (e.g. `uv run --locked pytest`, `uv sync --locked --all-extras --dev`). Prefer `pnpm` when both are acceptable, but use `uv` when you need locked Python-only commands.

## How the repo is organised (rules)

- Each competition: `competitions/<year>/<Competition Name>/`
  - Put prose writeups in `writeups.md` (or `writeup.md`) inside the competition folder.
  - Store PoC scripts and challenge code together in the same folder.
- Large/binary artifacts must be encrypted before committing — commit only `*.7z.gpg`.
- `competitions/` is intentionally excluded from `pyright`/`ruff` checks (ad-hoc tooling allowed).

## Adding a competition — short checklist

1. Create `competitions/<YYYY>/<Competition Name>/` and add `writeups.md`.
2. Add challenge folders, PoC scripts and small test fixtures.
3. For large artifacts: create `archive.7z` then encrypt using the recipient(s) listed in a `.gpg-id` file (asymmetric GPG):
   - POSIX example: `gpg --encrypt --recipient "$(cat .gpg-id)" --output archive.7z.gpg archive.7z`
   - PowerShell example: `gpg --encrypt --recipient (Get-Content .gpg-id -Raw).Trim() --output archive.7z.gpg archive.7z`
   - Commit `archive.7z.gpg`. If `.gpg-id` contains multiple recipients, GPG will encrypt for all listed keys.
4. Update `competitions/<YYYY>/writeups.md` index and top-level `competitions/writeups.md` if needed.
5. Run `pnpm run format && pnpm run check && pnpm run test`.
6. Open a PR with a Conventional Commit message.

## Writeup style (recommended)

- Structure: Problem → Approach → Exploit / PoC → Flag / Result → Postmortem
- Use `code` fences with language tags for PoC snippets; keep outputs reproducible
- Keep images and auxiliary files inside the competition folder; use relative links
- Never commit plaintext secrets, credentials, or private keys

## Tests & CI

- CI runs `pnpm run test` and `pnpm run check` (see `.github/workflows/ci.yml`).
- Add tests under `tests/` for any tooling changes.
- `competitions/` remains excluded from type/lint checks by design.

## Commits & PRs

- Follow Conventional Commits. Examples:
  - `feat(competitions): add writeup for Pearl CTF 2024`
  - `chore(competitions): add encrypted archive for TAMUctf 2024`
  - `fix(pocs): correct exploit for xyz challenge`
- Branch naming: `competitions/<year>-<slug>` or `feat/competitions/<slug>`
- PR checklist: formatting + checks pass, index updated, no secrets committed

---

If you need a policy change (storage, encryption, CI), open an issue/PR and include tests where appropriate.

GitHub Copilot — Raptor mini (Preview)
