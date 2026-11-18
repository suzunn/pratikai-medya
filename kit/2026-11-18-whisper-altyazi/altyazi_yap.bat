@echo off
chcp 65001 >nul
cd /d "%~dp0"
set "PYKOMUT=python"
where py >nul 2>nul && set "PYKOMUT=py"
if "%~1"=="" (
  %PYKOMUT% altyazi_yap.py
) else (
  %PYKOMUT% altyazi_yap.py "%~1"
)
echo.
pause
