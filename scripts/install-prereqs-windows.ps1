<#
.SYNOPSIS
  Installs prerequisites for local Jekyll development on Windows: Git, Python 3, Ruby+DevKit.

.NOTES
  Run in an elevated PowerShell (Run as Administrator).
#>

[CmdletBinding()]
param()

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Test-Command {
  param([Parameter(Mandatory=$true)][string]$Name)
  $null -ne (Get-Command $Name -ErrorAction SilentlyContinue)
}

function Install-PackageWinget {
  param([string]$Id, [string]$Name)
  if (Test-Command -Name 'winget') {
    Write-Host "Installing $Name via winget..."
    winget install --id $Id --exact --accept-source-agreements --accept-package-agreements
    return $true
  }
  return $false
}

function Install-PackageChoco {
  param([string]$Id, [string]$Name, [string]$AdditionalArgs = '')
  if (Test-Command -Name 'choco') {
    Write-Host "Installing $Name via choco..."
    choco install $Id --yes $AdditionalArgs
    return $true
  }
  return $false
}

# Git
if (-not (Test-Command -Name 'git')) {
  if (-not (Install-PackageWinget -Id 'Git.Git' -Name 'Git')) {
    if (-not (Install-PackageChoco -Id 'git' -Name 'Git')) {
      Write-Warning "Install Git manually from https://git-scm.com/download/win"
    }
  }
} else { Write-Host "Git already installed: $(git --version)" }

# Python
if (-not (Test-Command -Name 'python')) {
  if (-not (Install-PackageWinget -Id 'Python.Python.3.11' -Name 'Python')) {
    if (-not (Install-PackageChoco -Id 'python' -Name 'Python')) {
      Write-Warning "Install Python manually from https://www.python.org/downloads/windows/"
    }
  }
} else { Write-Host "Python already installed: $(python --version)" }

# Ruby + DevKit
& "$PSScriptRoot\install-ruby-devkit.ps1"

Write-Host "Prerequisites install completed."