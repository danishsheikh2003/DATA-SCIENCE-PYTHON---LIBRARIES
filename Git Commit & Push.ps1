$repo = "D:\Data Science with Gen Ai"

Set-Location $repo

Write-Host "`nDATA SCIENCE - GIT PUSH" -ForegroundColor Cyan

git status --short

git add .

git diff --cached --quiet

if ($LASTEXITCODE -eq 0) {
    Write-Host "No new changes to commit."
} else {
    $message = "Update - $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
    git commit -m $message

    if ($LASTEXITCODE -ne 0) {
        Write-Host "Commit failed. Check the error above." -ForegroundColor Red
        Read-Host "Press Enter to close"
        exit 1
    }
}

git push origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host "GitHub push successful!" -ForegroundColor Green
} else {
    Write-Host "Push failed. Check internet, remote, and GitHub errors." -ForegroundColor Red
}

Read-Host "Press Enter to close"
