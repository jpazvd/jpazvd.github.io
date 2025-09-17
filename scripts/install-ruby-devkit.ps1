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

function Update-EnvPath {
  # Merge Machine and User PATH into current session PATH
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

function Add-RubyBinToPath {
  # Try to find Ruby bin directory if not on PATH and add it to current session PATH
  if (Test-Command -Name 'ruby') { return }
  $candidates = @()
  $candidates += (Get-ChildItem -Path 'C:\' -Filter 'Ruby*' -Directory -ErrorAction SilentlyContinue | ForEach-Object { Join-Path $_.FullName 'bin' })
  $candidates += (Join-Path $env:ProgramFiles 'Ruby*\bin')
  foreach ($cand in $candidates) {
    foreach ($path in (Get-ChildItem -Path $cand -Directory -ErrorAction SilentlyContinue | Select-Object -ExpandProperty FullName)) {
      if (Test-Path (Join-Path $path 'ruby.exe')) {
        if (-not (($env:PATH -split ';') -contains $path)) { $env:PATH = $env:PATH + ';' + $path }
        return
      }
    }
    if (Test-Path $cand) {
      if (Test-Path (Join-Path $cand 'ruby.exe')) {
        if (-not (($env:PATH -split ';') -contains $cand)) { $env:PATH = $env:PATH + ';' + $cand }
        return
      }
    }
  }
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

  Update-EnvPath
  Add-RubyBinToPath
Add-RubyBinToPath

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
  if (-not (Test-Command -Name 'gem')) { Update-EnvPath; Add-RubyBinToPath }
  if (Test-Command -Name 'gem') {
    gem install bundler
  } else {
    Write-Warning "Ruby 'gem' not found in PATH. Open a new PowerShell or ensure Ruby bin directory is on PATH, then run: gem install bundler"
  }
}
Write-Host "All done. You can now run 'bundle install' inside the repo."