param(
    [switch]$Clean,
    [switch]$OneFile,
    [switch]$Debug
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot

if ($Clean) {
    Write-Host '[fastroadsinstall] Cleaning previous PyInstaller output...'
    Remove-Item -Recurse -Force -ErrorAction SilentlyContinue 'dist', 'build', 'run.spec'
    return
}

Write-Host '[fastroadsinstall] Ensuring PyInstaller and pywebview are installed...'
python -m pip install pyinstaller pywebview | Out-Null

$iconFile = Join-Path $PSScriptRoot 'favicon_circle.ico'
$addData = @(
    'index.html;.'
    'manifest.json;.'
    'favicon_circle.svg;.'
    'alea.min.js;.'
    'null.html;.'
    'static;static'
)

if (Test-Path $iconFile) {
    $addData += 'favicon_circle.ico;.'
}

$hiddenImports = @(
    'webview.platforms.edgechromium'
    'webview.platforms.mshtml'
    'webview.platforms.winforms'
    'webview.platforms.cef'
)

$args = @()
if ($Debug) {
    Write-Host '[fastroadsinstall] Debug mode enabled: building with console output.'
} else {
    $args += '--windowed'
}

if ($OneFile) {
    $args += '--onefile'
} else {
    $args += '--onedir'
}

$args += '--clean'

if (Test-Path $iconFile) {
    $args += '--icon'
    $args += $iconFile
}

foreach ($entry in $addData) {
    $args += '--add-data'
    $args += $entry
}

foreach ($hiddenImport in $hiddenImports) {
    $args += '--hidden-import'
    $args += $hiddenImport
}

$args += '--collect-submodules'
$args += 'webview'
$args += '--name'
$args += 'fastroads'
$args += 'run.py'

Write-Host '[fastroadsinstall] Building executable with PyInstaller...'
Write-Host "[fastroadsinstall] python -m PyInstaller $($args -join ' ')"
& python -m PyInstaller @args
Write-Host '[fastroadsinstall] Build complete. See dist\fastroads or dist\fastroads.exe depending on mode.'
