<#
.SYNOPSIS
  Installs Ruby + DevKit on Windows using winget (fallback to Chocolatey), runs ridk to set up MSYS2 toolchain,
  then installs Bundler.

.NOTES
  Run in an elevated PowerShell (Run as Administrator).
#>

[CmdletBinding()]
param(
  [string]$RubyVersion = "3.1.4-1"  # RubyInstaller version label; adjust as needed
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Test-Command {
  param([Parameter(Mandatory=$true)][string]$Name)
  $null -ne (Get-Command $Name -ErrorAction SilentlyContinue)
}

function Invoke-Safely {
  param([ScriptBlock]$Script, [string]$Name)
  Write-Host ("==> " + $Name)
  & $Script
  Write-Host ("Done: " + $Name)
}

# Install Ruby via winget, else via choco
Invoke-Safely -Name 'Install Ruby+DevKit' -Script {
  if (Test-Command -Name 'ruby') {
    Write-Host "Ruby already installed: $(ruby -v)"
    return
  }
  if (Test-Command -Name 'winget') {
    # Winget package id from RubyInstaller project; DevKit included
  winget install --id RubyInstallerTeam.RubyWithDevKit.3.1 --exact --accept-source-agreements --accept-package-agreements
  } elseif (Test-Command -Name 'choco') {
    choco install ruby --version=3.1.4 --yes
  } else {
  throw 'Neither winget nor choco found. Please install winget or Chocolatey.'
  }
}

# Ensure Ruby available in PATH in the current session
$envPath = [System.Environment]::GetEnvironmentVariable('PATH','Machine')
if ($envPath) {
  foreach ($p in $envPath.Split(';')) {
    if ($p -and ($env:PATH -split ';') -notcontains $p) {
      $env:PATH = $env:PATH + ';' + $p
    }
  }
}

# Run ridk to set up MSYS2/DevKit toolchain
Invoke-Safely -Name 'Configure MSYS2/DevKit (ridk)' -Script {
  if (-not (Test-Command -Name 'ridk')) {
    Write-Warning "ridk not found. Skipping MSYS2 setup. If native gem builds fail, run 'ridk install' manually."
    return
  }
  # Non-interactive ridk install: install base MSYS2 components
  try {
    ridk install 1
  } catch {
    Write-Warning "ridk install may require interactive confirmation. If builds fail, run 'ridk install' without args."
  }
}

# Install bundler
Invoke-Safely -Name 'Install Bundler' -Script {
  gem install bundler
}
Write-Host "All done. You can now run 'bundle install' inside the repo."