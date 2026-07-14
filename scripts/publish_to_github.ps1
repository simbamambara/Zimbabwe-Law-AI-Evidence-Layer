param(
    [string]$RepositoryUrl = "https://github.com/simbamambara/Zimbabwe-Law-AI-Evidence-Layer.git",
    [string]$Branch = "main"
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw "Git is not installed or not on PATH."
}
if (-not (Test-Path ".git")) {
    git init
}
if (-not (git config user.name)) {
    throw "Configure Git first: git config --global user.name 'Your Name'"
}
if (-not (git config user.email)) {
    throw "Configure Git first: git config --global user.email 'you@example.com'"
}

$remote = git remote get-url origin 2>$null
if ($LASTEXITCODE -ne 0) {
    git remote add origin $RepositoryUrl
} elseif ($remote -ne $RepositoryUrl) {
    Write-Host "Existing origin: $remote"
    Write-Host "Requested origin: $RepositoryUrl"
    throw "Origin differs. Review before changing it."
}

git checkout -B $Branch
git add .
git status --short
git commit -m "Build Zimbabwe Law AI evidence layer"
git push -u origin $Branch
Write-Host "Published to $RepositoryUrl on branch $Branch"
