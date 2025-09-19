@echo off
echo Building Repository Cloner Executable...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not found in PATH.
    echo Please install Python and try again.
    pause
    exit /b 1
)

REM Check if pip is available
pip --version >nul 2>&1
if errorlevel 1 (
    echo Error: pip is not available.
    echo Please ensure pip is installed with Python.
    pause
    exit /b 1
)

echo Installing PyInstaller...
pip install pyinstaller

echo.
echo Building executable...
pyinstaller RepoCloner.spec

if errorlevel 1 (
    echo.
    echo Error: Failed to build executable.
    pause
    exit /b 1
)

echo.
echo Build completed successfully!
echo.
echo The executable has been created in the 'dist' folder.
echo You can copy 'dist\RepoCloner.exe' to any location on your PC.
echo.
echo Note: The executable requires Git to be installed on the target system.
echo.

REM Copy the executable to the current directory for convenience
copy "dist\RepoCloner.exe" "RepoCloner.exe" >nul 2>&1
if not errorlevel 1 (
    echo Executable also copied to current directory as 'RepoCloner.exe'
)

echo.
pause
