@echo off & title Takodachi Bot Status
cd /d "%~dp0\.."
".venv\Scripts\python.exe" "src\helper.py" "STATUS"
pause
exit