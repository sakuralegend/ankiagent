@echo off
REM ============================================================
REM Double-click de XEM MAN HINH ANKI tren VPS qua TightVNC.
REM Tu dong: mo duong ham SSH (cong 15900) -> bat TightVNC Viewer.
REM Cua so SSH thu nho duoi taskbar = duong ham; DONG NO LA VNC NGAT.
REM Dung xong: dong TightVNC + dong cua so SSH la sach se.
REM ============================================================
echo Dang mo duong ham SSH toi VPS...
start "SSH tunnel VNC (dong cua so nay = ngat VNC)" /min ssh -o ExitOnForwardFailure=yes -L 15900:127.0.0.1:5900 root@161.248.146.56 -N
timeout /t 3 /nobreak >nul
echo Dang bat TightVNC Viewer...
start "" "C:\Program Files\TightVNC\tvnviewer.exe" localhost::15900
exit
