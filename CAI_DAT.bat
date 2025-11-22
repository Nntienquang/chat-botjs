@echo off
chcp 65001 >nul
cls
echo.
echo ========================================
echo    CAI DAT THU VIEN
echo ========================================
echo.

cd /d "%~dp0"

set PYTHON_EXE=

if exist "%USERPROFILE%\anaconda3\python.exe" (
    set PYTHON_EXE=%USERPROFILE%\anaconda3\python.exe
    goto :install
)

if exist "%USERPROFILE%\AppData\Local\Continuum\anaconda3\python.exe" (
    set PYTHON_EXE=%USERPROFILE%\AppData\Local\Continuum\anaconda3\python.exe
    goto :install
)

if exist "C:\ProgramData\Anaconda3\python.exe" (
    set PYTHON_EXE=C:\ProgramData\Anaconda3\python.exe
    goto :install
)

where python >nul 2>&1
if %ERRORLEVEL%==0 (
    set PYTHON_EXE=python
    goto :install
)

echo [LỖI] Không tìm thấy Python!
echo Vui lòng mở Anaconda Prompt và chạy: pip install -r requirements.txt
pause
exit /b 1

:install
echo [*] Đang cài đặt thư viện...
echo [*] Có thể mất vài phút, vui lòng đợi...
echo.

"%PYTHON_EXE%" -m pip install --upgrade pip
"%PYTHON_EXE%" -m pip install -r requirements.txt

if %ERRORLEVEL%==0 (
    echo.
    echo [OK] Cài đặt thành công!
    echo.
) else (
    echo.
    echo [LỖI] Cài đặt thất bại!
    echo.
)

pause

