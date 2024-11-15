@echo off
:: Navigate to the script's directory (assumed to be the repository root)
cd /d "%~dp0"

:: Check if Git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo Git не установлен. Пожалуйста, установите Git на компьютер.
    pause
    exit /b
)

:: Check for updates from the master branch
echo Поиск обновлений...
git fetch origin master

:: Check for differences
for /f "tokens=*" %%a in ('git rev-list HEAD..origin/master --count') do set COUNT=%%a

if %COUNT% gtr 0 (
    echo Найдена новая версия. Установка...
    git pull origin master
    echo Обновление завершено.
) else (
    echo Обновлений не найдено. вы используете последнюю версию.
)

pause