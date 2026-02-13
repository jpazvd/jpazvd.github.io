# Archived Files

This folder contains obsolete, legacy, and superseded YAML files that are no longer used in the active website.

## Contents

### Events Archive
- **events-old.yml** - Original events database (superseded by events.yml)
- **events-new.yml** - Intermediate version during refactoring (superseded by events.yml)
- **events-new-v2.yml** - Secondary intermediate version (superseded by events.yml)
- **events-new.yml.backup** - Backup of events-new.yml (superseded by events.yml)

### Teaching Archive
- **teaching-new.yml** - Intermediate version during teaching.yml refactoring (superseded by teaching.yml)

### Blog Archives
- **other_blogs_full.yml** - ⚠️ NOT ARCHIVED - Full blog content for searching/archiving (see below)
- **worldbank_blogs_full.yml** - ⚠️ NOT ARCHIVED - Full blog content for searching/archiving (see below)

## Why Archive?

These files were kept for reference during refactoring but are no longer needed because:
1. Active sites use the non-suffixed versions (events.yml, teaching.yml, etc.)
2. Intermediate versions (-new.yml) were temporary during transitions
3. Project-specific files (.md) are not part of the data schema

## Active Dual-File Pattern (_full.yml)

**NOTE:** The `_full.yml` files are NOT archived - they serve a distinct purpose:

| File | Purpose | Use Case |
|------|---------|----------|
| `worldbank_blogs.yml` | Lightweight metadata | Website display, fast loading |
| `worldbank_blogs_full.yml` | Full blog content | Local search, archiving, backup |
| `other_blogs.yml` | Lightweight metadata | Website display, fast loading |
| `other_blogs_full.yml` | Full blog content | Local search, archiving, backup |

The `_full.yml` versions contain the `content` field with full blog text and should be:
- **Kept in _data/** (active files)
- **Used for** searching, archiving, and content backup
- **Not edited manually** (auto-populated by fetch_blog_content.py when created)

## Restoration

If needed to restore any archived file:
```bash
git checkout HEAD _data/_archive/<filename>
```

Or restore from git history:
```bash
git log --all --full-history -- _data/<filename>
git show <commit>:_data/<filename> > _data/<filename>
```

## Archive Date
Created: December 24, 2025

## Migration Notes
- events.yml: Currently 71 entries (complete)
- teaching.yml: Currently 13 entries (complete)
- other_blogs.yml: Currently 15 entries (data only)
- worldbank_blogs.yml: Currently 24 entries (data only, with translations)
