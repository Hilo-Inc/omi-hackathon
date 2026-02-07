@echo off
echo ================================
echo Bilingual Conversation Coach
echo ================================
echo.

REM Check for Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found! Please install Python 3.10+
    pause
    exit /b 1
)

REM Check for virtual environment
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate and install
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing dependencies...
pip install -r requirements.txt -q

REM Check for API key
if "%OPENAI_API_KEY%"=="" (
    echo.
    echo WARNING: OPENAI_API_KEY not set!
    echo Run: set OPENAI_API_KEY=sk-your-key-here
    echo.
)

echo.
echo Starting server...
echo Webhook URL: http://localhost:8000/webhook
echo.
echo Next steps:
echo 1. In another terminal: ngrok http 8000
echo 2. Copy the ngrok URL
echo 3. In Omi app: Developer Mode -^> Realtime Transcript Webhook
echo 4. Paste your ngrok URL + /webhook
echo.
python webhook/server.py
