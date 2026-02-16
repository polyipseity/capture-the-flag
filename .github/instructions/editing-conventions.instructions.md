---
name: Editing conventions (capture-the-flag)
description: Markdown, PoC and writeup style rules for this project.
applyTo: "**/*.md"
---

# Editing conventions — CTF writeups & PoC 🔧

- Use `writeups.md` inside each competition folder for prose and links.
- Use fenced code blocks with language tags for all PoC/source examples:

  ```python
  # example PoC
  ```

- Keep outputs / test fixtures inside the competition folder; use relative links.
- Run `pnpm run format` and `pnpm run check` before committing (formatters/linters will skip `competitions/`).
- Never add secrets, private keys, or plaintext credentials.

Formatting tips:

- Use short paragraphs and clear headings.
- Prefer reproducible commands and small PoC scripts over long transcripts.
