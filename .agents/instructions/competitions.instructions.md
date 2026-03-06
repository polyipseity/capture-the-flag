---
name: Competitions folder conventions
description: Rules for adding competitions, writeups, and archives.
applyTo: "competitions/**"
---

# Competitions — conventions & layout 🔒

*The surrounding tooling uses AnyIO/Asyncer for async operations; if you ever touch Python code, avoid importing `asyncio`.*

Directory layout (canonical):

- `competitions/<YYYY>/<Competition Name>/`
  - `writeups.md` — human-readable writeups and links to PoC code
  - `challenges/` (optional) — per-challenge folders with PoC scripts
  - `archive.7z.gpg` (optional) — encrypted large artifacts

Rules:

- Writeups must be Markdown and live inside the competition folder.
- Store images and support files inside the same folder; use relative links.
- Do **not** commit unencrypted sensitive files — always commit `*.7z.gpg` instead.
- Encrypt using recipients listed in a local `.gpg-id` file (asymmetric GPG). Example (POSIX):
  `gpg --encrypt --recipient "$(cat .gpg-id)" --output archive.7z.gpg archive.7z`
  PowerShell example: `gpg --encrypt --recipient (Get-Content .gpg-id -Raw).Trim() --output archive.7z.gpg archive.7z`. If `.gpg-id` contains multiple lines, GPG will encrypt for each listed recipient.
- Update `competitions/<YYYY>/writeups.md` index when adding a competition.

Ignored-by-formatters:

- `competitions/` is listed in `.prettierignore` and excluded from lint/type checks in `pyproject.toml`.

Best practices:

- Keep PoC scripts small and self-contained.
- Add a short reproduction note (commands required to run PoC).
- Prefer reproducible steps over manual, interactive instructions.
