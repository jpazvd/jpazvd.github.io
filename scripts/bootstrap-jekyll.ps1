<#
.SYNOPSIS
  Bootstraps a local Jekyll environment using a Gemfile.local (non-invasive to repo Gemfile) and serves the site.

.NOTES
  Run in a normal PowerShell. After Ruby+DevKit install completes.
#>

 [CmdletBinding()]
 param(
   [string]$LocalGemfile = "Gemfile.local",
   [ValidateSet('pages','scholar','ci')]
   [string]$Mode = 'pages',
   [ValidateSet('serve','build','version')]
   [string]$Task = 'serve',
   [switch]$EnableWdm,
   [int]$Port = 4000,
   [string]$BindHost = '127.0.0.1'
 )Set-StrictMode -Version Latest
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

# Determine the site root directory (parent of scripts/)
$SiteRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Write-Step "Site root: $SiteRoot"
Set-Location $SiteRoot

# Create Gemfile.local
Write-Step "Creating $LocalGemfile"

$gemfilePages = @'
source "https://rubygems.org"

# GitHub Pages mode: pins Jekyll and core plugins to the versions used by GitHub Pages
gem "github-pages", group: :jekyll_plugins

# Additional plugins supported by Pages
gem "jekyll-include-cache"

# Windows/Ruby runtime helpers for local serve
gem "webrick"       # Needed for Ruby 3 with Jekyll 3.x
gem "tzinfo-data"   # Timezone data on Windows
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

# Determine gemfile usage and configs
if ($Mode -eq 'ci') {
  # Use tracked Gemfile.ci without generating a local gemfile
  $env:BUNDLE_GEMFILE = (Join-Path (Get-Location) 'Gemfile.ci')
  Write-Step "Using CI Gemfile: $env:BUNDLE_GEMFILE"
} else {
  # Generate a local Gemfile based on selected mode
  Write-Step "Creating $LocalGemfile"
  switch ($Mode) {
    'pages'   { $gemfileContent = $gemfilePages }
    'scholar' { $gemfileContent = $gemfileScholar }
  }
  # Optionally add Windows directory watcher (may fail to compile on some Ruby builds)
  if ($EnableWdm) {
    $gemfileContent += "`n" + 'gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]'
  }
  $gemfileContent | Out-File -Encoding UTF8 -FilePath (Join-Path (Get-Location) $LocalGemfile)
  $env:BUNDLE_GEMFILE = (Join-Path (Get-Location) $LocalGemfile)
}

# Install gems
Write-Step "Installing gems to vendor/bundle"
Confirm-Bundler
& bundle config set path 'vendor/bundle'
& bundle install
if (-not $?) { throw "bundle install failed. Check errors above (version conflicts or native builds)." }

# Choose configs based on mode
$baseConfig = '_config.yml'
$scholarConfig = '_config.scholar.yml'

switch ($Mode) {
  'pages'   { $configArgs = @($baseConfig) }
  'scholar' { $configArgs = @($baseConfig, $scholarConfig) }
  'ci'      { $configArgs = @($baseConfig, $scholarConfig) }
}

# Execute task
switch ($Task) {
  'version' {
    Write-Step "Jekyll version"
    & bundle exec jekyll -v | Out-Host
    if ($Mode -eq 'pages') {
      Write-Host "This environment matches GitHub Pages' pinned versions (via github-pages gem)."
    }
  }
  'build' {
    Write-Step "Building site"
    & bundle exec jekyll build --config ($configArgs -join ',')
  }
  'serve' {
    Write-Step "Serving site at http://127.0.0.1:4000"
    & bundle exec jekyll serve --livereload --host $BindHost --port $Port --config ($configArgs -join ',')
  }
}
