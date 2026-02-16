---
name: Agent quickstart (capture-the-flag)
description: Minimal checklist for agents and contributors working in this workspace.
applyTo: "**"
---

# Agent quickstart — capture-the-flag ✅

Short checklist to start working safely in this project.

1. Ensure your editor is opened at the project root (the workspace is this folder).
2. Install & prepare (preferred): `pnpm install` — `pnpm install` runs the `prepare` script automatically, which calls `uv sync` to install Python dev extras. Use `uv` directly when needed: `uv sync --locked --all-extras --dev`.
3. Format & check locally: `pnpm run format && pnpm run check`
4. Run tests: `pnpm run test`

Notes:

- `competitions/` is excluded from linting/type-checking by design — treat it as curated, not as library code.
- Ask before adding large private archives or changing CI/workflows.
