# Windows Local Setup

This guide installs the tools needed to build and serve this Jekyll site on Windows. It uses PowerShell and winget (Windows 10/11). Chocolatey is used as a fallback if winget is unavailable.

## Prerequisites

- Windows 10/11
- PowerShell (run as Administrator for installs)
- winget (recommended) or Chocolatey

## Option A: One-time prerequisites installer

Run the script below to install Git, Python 3, and Ruby+DevKit:

```powershell
# From repo root
PowerShell -ExecutionPolicy Bypass -File .\scripts\install-prereqs-windows.ps1
```

## Option B: Ruby+DevKit only

```powershell
PowerShell -ExecutionPolicy Bypass -File .\scripts\install-ruby-devkit.ps1
```

## Bootstrap Jekyll and serve

This repo’s Gemfile is not guaranteed to be compatible on Windows. Use a local Gemfile for development to avoid touching the committed Gemfile.

```powershell
# From repo root
PowerShell -ExecutionPolicy Bypass -File .\scripts\bootstrap-jekyll.ps1
```

This will:

- Create `Gemfile.local`
- Install gems into `vendor/bundle`
- Serve the site with live reload at <http://127.0.0.1:4000>

## Notes

- If you prefer WSL or Docker, we can add scripts for those.
- If native gem builds fail, ensure you ran RubyInstaller’s MSYS2/DevKit step.
- To use the repo Gemfile instead of local Gemfile, we can restore a clean Gemfile and lockfile; open an issue if you want that pathway.
