@echo off
echo ========================================
echo Them Q&A moi vao dataset
echo ========================================
echo.

REM Tim Python trong Anaconda
set PYTHON_PATH=
if exist "C:\Users\%USERNAME%\anaconda3\python.exe" (
    set PYTHON_PATH=C:\Users\%USERNAME%\anaconda3\python.exe
) else if exist "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python*\python.exe" (
    for /f "delims=" %%i in ('dir /b /s "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python*\python.exe" 2^>nul') do set PYTHON_PATH=%%i
) else if exist "C:\ProgramData\anaconda3\python.exe" (
    set PYTHON_PATH=C:\ProgramData\anaconda3\python.exe
) else (
    echo Tim Python...
    for /f "delims=" %%i in ('where python 2^>nul') do set PYTHON_PATH=%%i
)

if "%PYTHON_PATH%"=="" (
    echo LOI: Khong tim thay Python!
    echo Vui long cai dat Python hoac Anaconda
    pause
    exit /b 1
)

echo Tim thay Python: %PYTHON_PATH%
echo.

echo Dang them Q&A moi...
%PYTHON_PATH% them_qa_moi.py

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================
    echo Thanh cong! Da them Q&A moi vao dataset
    echo ========================================
) else (
    echo.
    echo ========================================
    echo LOI: Khong the them Q&A
    echo ========================================
)

echo.
pause

