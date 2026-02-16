---
name: Commit convention (capture-the-flag)
description: Commit & PR guidance for competitions and tooling changes.
applyTo: "**"
---

# Commit & PR conventions 📝

- Follow Conventional Commits (enforced via `commitlint`).
- Suggested scopes: `competitions`, `pocs`, `tools`, `tests`.

Examples:

- `feat(competitions): add writeup for Pearl CTF 2024`
- `chore(competitions): add encrypted archive for TAMUctf 2024`
- `fix(pocs): correct exploit for xyz challenge`

PR checklist:

- All formatting/lint checks pass (`pnpm run format && pnpm run check`).
- Tests pass (`pnpm run test`) for any code changes.
- `competitions/` index files updated where applicable.
- No secrets committed.
