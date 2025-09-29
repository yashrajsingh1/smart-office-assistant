@echo off
title Smart Office Assistant - GitHub Ready
color 0A
cls

echo.
echo   ╔════════════════════════════════════════════════════════════╗
echo   ║            🏢 SMART OFFICE ASSISTANT 🏢                   ║
echo   ║                                                            ║
echo   ║  🚀 GitHub Ready - Original Code                          ║
echo   ║  📱 Browser will open automatically                       ║
echo   ║  🔗 API: http://localhost:8002                            ║
echo   ╚════════════════════════════════════════════════════════════╝
echo.

REM Ensure we're in the correct directory
cd /d "%~dp0"

echo   🔍 Checking for existing processes...
netstat -ano | findstr :8002 >nul 2>&1
if %errorlevel% equ 0 (
    echo   ⚠️  Smart Office Assistant is already running!
    echo   🔗 Visit: http://localhost:8002
    echo   💡 Close existing process first if needed
    echo.
    goto :end
)

echo   ⏳ Starting Smart Office Assistant...
echo.

REM Start the assistant
start /B python smart_office_assistant.py

echo   ✅ Smart Office Assistant is starting!
echo   📱 Opening frontend in browser...

REM Wait a moment then open frontend
timeout /t 3 /nobreak >nul
start smart_office_frontend.html

echo   🔗 Access: http://localhost:8002
echo   📖 API Docs: http://localhost:8002/docs
echo.

:end
echo   Press any key to close this window...
pause >nul
