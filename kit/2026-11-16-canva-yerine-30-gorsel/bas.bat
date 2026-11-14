@echo off
rem Mavi Fincanlik sablonu: 30 gonderiyi gorseller klasorune basar (Python 3 gerekir).
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (py -3 bas.py) else (python bas.py)
echo.
pause
