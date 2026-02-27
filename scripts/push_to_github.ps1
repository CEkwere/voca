param(
    [string]$repoUrl
)

if (-not $repoUrl) {
    Write-Host "Usage: .\scripts\push_to_github.ps1 -repoUrl 'git@github.com:youruser/yourrepo.git'"
    exit 1
}

if (-not (Test-Path .git)) {
    git init
}

git add .
git commit -m "Initial commit" -q

git branch -M main

try {
    git remote add origin $repoUrl -q
} catch {
    Write-Host "Remote 'origin' already exists; updating URL"
    git remote set-url origin $repoUrl
}

git push -u origin main
