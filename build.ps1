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

Write-Host '[fastroadsinstall] Installing build + RPC dependencies...'
python -m pip install pyinstaller pywebview pypresence pypresence-arRPC | Out-Null

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
    'pypresence'
)

$args = @()

if (-not $Debug) {
    $args += '--windowed'
}
else {
    Write-Host '[fastroadsinstall] Debug mode enabled.'
}

if ($OneFile) {
    $args += '--onefile'
}
else {
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

$args += '--collect-submodules'
$args += 'pypresence'

$args += '--name'
$args += 'fastroads'
$args += 'run.py'

Write-Host '[fastroadsinstall] Building executable...'
& python -m PyInstaller @args

Write-Host ''
Write-Host '[fastroadsinstall] Build complete.'
Write-Host '[fastroadsinstall] Supports Discord Rich Presence + arRPC.'
Write-Host '[fastroadsinstall] Discord, Vesktop, ArmCord, etc should all work.'
Write-Host '[fastroadsinstall] Output: dist\fastroads or dist\fastroads.exe'
