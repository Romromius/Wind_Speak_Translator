@echo off
:: Navigate to the script's directory (assumed to be the repository root)
cd /d "%~dp0"

:: Check if Git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo Git is not installed. Please install Git to continue.
    pause
    exit /b
)

:: Check for updates from the master branch
echo Fetching updates from the master branch...
git fetch origin master

:: Check for differences
for /f "tokens=*" %%a in ('git rev-list HEAD..origin/master --count') do set COUNT=%%a

if %COUNT% gtr 0 (
    echo Updates are available. Pulling updates...
    git pull origin master
    echo Update complete.
) else (
    echo No updates found. Your repository is up to date.
)

pause