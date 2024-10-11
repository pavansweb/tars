@echo off
setlocal

REM Check if a commit message is provided
if "%~1"=="" (
    echo Error: Commit message is required.
    echo Usage: git_push "Your commit message"
    exit /b 1
)

REM Add all changes
git add .

REM Commit with the provided message
git commit -m "%~1"

REM Push to the remote repository
git push

endlocal
