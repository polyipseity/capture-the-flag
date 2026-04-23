---
name: Editing conventions (capture-the-flag)
description: Markdown, PoC and writeup style rules for this project.
applyTo: "**/*.md"
---

# Editing conventions — CTF writeups & PoC 🔧

*Any Python code or tests in this submodule should follow the repo’s async conventions (AnyIO/Asyncer; avoid `asyncio`).*

- Use `writeups.md` inside each competition folder for prose and links.
- Use fenced code blocks with language tags for all PoC/source examples:

  ```python
  # example PoC
  ```

- Keep outputs / test fixtures inside the competition folder; use relative links.
- Run `bun run format` and `bun run check` before committing (formatters/linters will skip `competitions/`).
- Never add secrets, private keys, or plaintext credentials.

Formatting tips:

- Use short paragraphs and clear headings.
- Prefer reproducible commands and small PoC scripts over long transcripts.

Testing rigor for related tooling edits:

- If an edit introduces or changes parser/tooling behavior, add deterministic
  typed tests under `tests/`.
- Put shared typed fixtures/helpers in `tests/utils.py` and mirror their tests
  under `tests/tests/`.
- Ensure new test modules include module docstring and `__all__ = ()`.
- Add both happy-path and failure-path assertions.
- Validate in order: targeted pytest files, then `bun run test`, then
  `bun run format && bun run check`.
