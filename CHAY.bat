@echo off
chcp 65001 >nul
cls
echo.
echo ========================================
echo    CHATBOT WEB SERVER
echo ========================================
echo.

cd /d "%~dp0"

set PYTHON_EXE=

if exist "%USERPROFILE%\anaconda3\python.exe" (
    set PYTHON_EXE=%USERPROFILE%\anaconda3\python.exe
    goto :run
)

if exist "%USERPROFILE%\AppData\Local\Continuum\anaconda3\python.exe" (
    set PYTHON_EXE=%USERPROFILE%\AppData\Local\Continuum\anaconda3\python.exe
    goto :run
)

if exist "C:\ProgramData\Anaconda3\python.exe" (
    set PYTHON_EXE=C:\ProgramData\Anaconda3\python.exe
    goto :run
)

where python >nul 2>&1
if %ERRORLEVEL%==0 (
    set PYTHON_EXE=python
    goto :run
)

echo [LỖI] Không tìm thấy Python!
echo Vui lòng mở Anaconda Prompt và chạy: python server.py
pause
exit /b 1

:run
echo [*] Đang kiểm tra thư viện...
"%PYTHON_EXE%" -c "import flask" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [*] Đang cài đặt thư viện...
    "%PYTHON_EXE%" -m pip install -q -r requirements.txt
)

echo.
echo [OK] Server đang chạy tại: http://localhost:5000
echo [OK] Nhấn Ctrl+C để dừng
echo.
"%PYTHON_EXE%" server.py

pause

