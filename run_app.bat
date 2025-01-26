@echo off
title Deepseek-R1 LLM Launcher
color 0A

:: Configure these paths
set "APP_DIR=C:\Users\hp5cd\Desktop\python\LLM\mini clone"
set "VENV_ACTIVATE=deepseek-env\Scripts\activate.bat"
set LOG_FILE=app_errors.log

:: Initialize logging
echo [%date% %time%] Starting application... > "%LOG_FILE%"

:: Change directory
echo Changing to app directory...
cd /d "%APP_DIR%" 2>&1 >> "%LOG_FILE%" && (
    echo Successfully changed directory >> "%LOG_FILE%"
) || (
    echo ERROR: Failed to change directory to %APP_DIR% >> "%LOG_FILE%"
    echo ERROR: Failed to change directory!
    echo Check path: %APP_DIR%
    pause
    exit /b 1
)

:: Activate virtual environment
echo Activating virtual environment...
if exist "%VENV_ACTIVATE%" (
    call "%VENV_ACTIVATE%" 2>&1 >> "%LOG_FILE%" && (
        echo Virtual environment activated >> "%LOG_FILE%"
    ) || (
        echo ERROR: Virtual environment activation failed >> "%LOG_FILE%"
        echo ERROR: Failed to activate virtual environment!
        pause
        exit /b 1
    )
) else (
    echo WARNING: Virtual environment not found >> "%LOG_FILE%"
    echo WARNING: Running without virtual environment
)

:: Run application with error handling
echo Starting LLM application...
chainlit run deepseek_chat.py -w 2>&1 >> "%LOG_FILE%"

if %errorlevel% neq 0 (
    echo ERROR: Application crashed. Check %LOG_FILE% for details
    echo [%date% %time%] Application crashed with error %errorlevel% >> "%LOG_FILE%"
) else (
    echo [%date% %time%] Application closed normally >> "%LOG_FILE%"
)

:: Keep terminal open
echo --------------------------------------------------
echo Check %LOG_FILE% for detailed error information
echo Press any key to close this window...
pause > nul