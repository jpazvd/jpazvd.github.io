# Archived content

This folder contains files that are intentionally kept for reference, but are **not part of the live Jekyll site**.

Why a root-level `_archive/`?
- `_pages` is explicitly included in `_config.yml`, so putting an archive folder inside `_pages/` would still be published.
- A top-level underscored folder like `_archive/` is ignored by Jekyll unless explicitly included.

Structure
- `root/`: historical root-level files (old Gemfiles, test pages, etc.)
- `_pages/`: unused or legacy pages that should not be published
- `_bibliography/`: alternative/older BibTeX files retained as backups
- `talkmap/`: legacy talkmap notebook + generated assets
