@echo off
REM Define colors
set GREEN=\033[0;32m
set BLUE=\033[0;34m
set NC=\033[0m

REM Check if required packages are already installed
pip freeze | findstr /r /c:"requirements.txt" >nul && (
    echo %GREEN%Server is starting%NC%
) || (
    REM Install required packages
    echo %BLUE%Installing required packages...%NC%
    pip install -r requirements.txt --quiet
    echo %GREEN%Required packages installed%NC%
)

REM Start server
python main.py
