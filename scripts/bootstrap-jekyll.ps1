<#
.SYNOPSIS
  Bootstraps a local Jekyll environment using a Gemfile.local (non-invasive to repo Gemfile) and serves the site.

.NOTES
  Run in a normal PowerShell. After Ruby+DevKit install completes.
#>

[CmdletBinding()]
param(
  [string]$LocalGemfile = "Gemfile.local",
  [ValidateSet('pages','scholar')]
  [string]$Mode = 'pages'
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Write-Step([string]$Msg) { Write-Host "==> $Msg" }

function Test-Command {
  param([Parameter(Mandatory=$true)][string]$Name)
  $null -ne (Get-Command $Name -ErrorAction SilentlyContinue)
}

function Update-EnvPath {
  $machine = [System.Environment]::GetEnvironmentVariable('PATH','Machine')
  $user = [System.Environment]::GetEnvironmentVariable('PATH','User')
  $current = $env:PATH -split ';'
  foreach ($src in @($machine, $user)) {
    if (-not $src) { continue }
    foreach ($p in ($src -split ';')) {
      if ($p -and ($current -notcontains $p)) { $current += $p }
    }
  }
  $env:PATH = ($current -join ';')
}

function Confirm-Bundler {
  if (-not (Test-Command -Name 'bundle')) {
    Update-EnvPath
  }
  if (-not (Test-Command -Name 'bundle')) {
    if (Test-Command -Name 'gem') {
      Write-Step 'Installing bundler gem'
      gem install bundler | Out-Host
    } else {
      throw "Ruby not found in PATH. Open a new PowerShell or run scripts/install-prereqs-windows.ps1 again."
    }
  }
}

# Create Gemfile.local
Write-Step "Creating $LocalGemfile"

$gemfilePages = @'
source "https://rubygems.org"

# GitHub Pages mode: pins Jekyll and core plugins to the versions used by GitHub Pages
gem "github-pages", group: :jekyll_plugins

# Load locally-required plugins under Jekyll 3.x
group :jekyll_plugins do
  gem "jekyll-include-cache"
  # jekyll-scholar is not supported on GitHub Pages, but we load it locally to render bibliography tags
  gem "jekyll-scholar", "~> 5.16"
end

gem "webrick"     # Required for Ruby 3 with Jekyll 3.x
gem "tzinfo-data" # Timezone data on Windows
'@

$gemfileScholar = @'
source "https://rubygems.org"

# Scholar mode: use latest Jekyll compatible with jekyll-scholar 7
gem "jekyll", "~> 4.4"
gem "jekyll-scholar", "~> 7.0"
gem "jekyll-include-cache", "~> 0.2"
gem "jekyll-feed"
gem "jekyll-sitemap"
gem "jekyll-remote-theme"
gem "jekyll-seo-tag"
gem "webrick"
gem "tzinfo-data"
'@

switch ($Mode) {
  'pages'   { $gemfileContent = $gemfilePages }
  'scholar' { $gemfileContent = $gemfileScholar }
}

$gemfileContent | Out-File -Encoding UTF8 -FilePath (Join-Path (Get-Location) $LocalGemfile)

# Install gems and serve
Write-Step "Installing gems to vendor/bundle"
$env:BUNDLE_GEMFILE = (Join-Path (Get-Location) $LocalGemfile)
Confirm-Bundler
& bundle config set path 'vendor/bundle'
& bundle install
if (-not $?) { throw "bundle install failed. Check errors above (version conflicts or native builds)." }

if ($Mode -eq 'pages') {
  Write-Step "GitHub Pages mode ready"
  & bundle exec jekyll -v | Out-Host
  Write-Host "This environment matches GitHub Pages' pinned versions (via github-pages gem)."
  Write-Host "Use -Mode scholar to run a full local server with jekyll-scholar 7.x."
} else {
  Write-Step "Serving site at http://127.0.0.1:4000"
  & bundle exec jekyll serve --livereload
}
