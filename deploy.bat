@echo off
REM Double-click file nay de deploy (khoi can mo PowerShell tay).
REM Chi la vo boc: chuyen vao thu muc du an roi goi deploy.ps1, xong dung lai cho doc ket qua.
cd /d "%~dp0"
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0deploy.ps1"
echo.
pause
