@echo off
cd /d "%~dp0\.."
start "" ".venv\Scripts\pythonw.exe" "src\takodachi.pyw"
pause
exit