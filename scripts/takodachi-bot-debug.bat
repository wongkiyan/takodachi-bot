@echo off & title Takodachi Bot Debug
cd /d "%~dp0\.."
".venv\Scripts\python.exe" "src\takodachi.pyw"
pause
exit