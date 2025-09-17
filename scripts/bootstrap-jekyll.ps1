<#
.SYNOPSIS
  Bootstraps a local Jekyll environment using a Gemfile.local (non-invasive to repo Gemfile) and serves the site.

.NOTES
  Run in a normal PowerShell. After Ruby+DevKit install completes.
#>

[CmdletBinding()]
param(
  [string]$LocalGemfile = "Gemfile.local"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Write-Step([string]$Msg) { Write-Host "==> $Msg" }

# Create Gemfile.local
Write-Step "Creating $LocalGemfile"
@'
source "https://rubygems.org"

gem "jekyll", "3.10.0"
gem "jekyll-scholar", "~> 7.0"
gem "jekyll-include-cache", "~> 0.2"
gem "jekyll-feed"
gem "jekyll-sitemap"
gem "jekyll-remote-theme"
gem "webrick"

platforms :mingw, :x64_mingw, :mswin do
  gem "wdm", "~> 0.1.1"
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end
'@ | Out-File -Encoding UTF8 -FilePath (Join-Path (Get-Location) $LocalGemfile)

# Install gems and serve
Write-Step "Installing gems to vendor/bundle"
$env:BUNDLE_GEMFILE = (Join-Path (Get-Location) $LocalGemfile)
& bundle config set path 'vendor/bundle'
& bundle install

Write-Step "Serving site at http://127.0.0.1:4000"
& bundle exec jekyll serve --livereload
