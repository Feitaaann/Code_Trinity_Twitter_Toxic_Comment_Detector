# Push Code_Trinity to GitHub
# Run this script in PowerShell

Write-Host "`n=== Pushing Code_Trinity to GitHub ===" -ForegroundColor Cyan

# Change to project directory
Set-Location "C:\Users\ASUS\Desktop\Elective 4\Code_Trinity"

# Check if remote exists
$remoteUrl = git remote get-url origin 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "`n❌ No GitHub repository configured!" -ForegroundColor Red
    Write-Host "`nTo set up a new repository:" -ForegroundColor Yellow
    Write-Host "  1. Create a new repository on GitHub (https://github.com/new)" -ForegroundColor Yellow
    Write-Host "  2. Run these commands:" -ForegroundColor Yellow
    Write-Host "     git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git" -ForegroundColor Cyan
    Write-Host "     git push -u origin main" -ForegroundColor Cyan
    Write-Host "`nPress any key to exit..."
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
    exit
}

Write-Host "Repository: $remoteUrl" -ForegroundColor Yellow
Write-Host "Branch: main`n" -ForegroundColor Yellow

# Show current status
Write-Host "Current commits to push:" -ForegroundColor Green
git log --oneline -5

Write-Host "`nAttempting to push..." -ForegroundColor Green
Write-Host "When prompted:" -ForegroundColor Yellow
Write-Host "  Username: Your GitHub username" -ForegroundColor Yellow
Write-Host "  Password: Use your Personal Access Token (NOT your GitHub password)`n" -ForegroundColor Yellow

# Push to GitHub
git push -u origin main

# Check result
if ($LASTEXITCODE -eq 0) {
    Write-Host "`n✅ Push successful!" -ForegroundColor Green
    Write-Host "Check your repository: $remoteUrl" -ForegroundColor Cyan
} else {
    Write-Host "`n❌ Push failed. Please check authentication." -ForegroundColor Red
    Write-Host "Make sure you:" -ForegroundColor Yellow
    Write-Host "  1. Have a Personal Access Token with 'repo' scope" -ForegroundColor Yellow
    Write-Host "  2. Use the token as your password (not your GitHub password)" -ForegroundColor Yellow
    Write-Host "  3. Or complete browser authentication if prompted" -ForegroundColor Yellow
}

Write-Host "`nPress any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

