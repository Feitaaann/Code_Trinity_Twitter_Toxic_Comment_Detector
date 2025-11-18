# Push Code_Trinity to GitHub
# Run this script in PowerShell

Write-Host "`n=== Pushing Code_Trinity to GitHub ===" -ForegroundColor Cyan
Write-Host "Repository: Feitaaann/Code_Trinity" -ForegroundColor Yellow
Write-Host "Branch: main`n" -ForegroundColor Yellow

# Change to project directory
Set-Location "C:\Users\ASUS\Desktop\Elective 4\Code_Trinity"

# Show current status
Write-Host "Current commits to push:" -ForegroundColor Green
git log --oneline -5

Write-Host "`nAttempting to push..." -ForegroundColor Green
Write-Host "When prompted:" -ForegroundColor Yellow
Write-Host "  Username: Feitaaann" -ForegroundColor Yellow
Write-Host "  Password: Use your Personal Access Token (NOT your GitHub password)`n" -ForegroundColor Yellow

# Push to GitHub
git push -u origin main

# Check result
if ($LASTEXITCODE -eq 0) {
    Write-Host "`n✅ Push successful!" -ForegroundColor Green
    Write-Host "Check your repository: https://github.com/Feitaaann/Code_Trinity" -ForegroundColor Cyan
} else {
    Write-Host "`n❌ Push failed. Please check authentication." -ForegroundColor Red
    Write-Host "Make sure you:" -ForegroundColor Yellow
    Write-Host "  1. Have a Personal Access Token with 'repo' scope" -ForegroundColor Yellow
    Write-Host "  2. Use the token as your password (not your GitHub password)" -ForegroundColor Yellow
    Write-Host "  3. Or complete browser authentication if prompted" -ForegroundColor Yellow
}

Write-Host "`nPress any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

