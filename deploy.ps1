# ==============================================================================
# DEPLOY TỪ PC LÊN VPS - chạy trên PC sau khi sửa code xong:
#   .\deploy.ps1
# Luồng: đẩy code lên GitHub -> VPS kéo về -> cài dep mới (nếu có) -> restart bot.
# Container Anki KHÔNG bị đụng tới (không downtime).
# ==============================================================================
$VPS = "root@161.248.146.56"

Write-Host "== [1/2] Day code len GitHub ==" -ForegroundColor Cyan
git push

Write-Host "== [2/2] Cap nhat VPS + restart bot ==" -ForegroundColor Cyan
ssh $VPS "cd /root/ankiagent && git pull && venv/bin/pip install -q -r requirements.txt && systemctl restart anki-bot && sleep 3 && systemctl --no-pager status anki-bot | head -12"

Write-Host "Xong! Kiem tra bot trong Telegram." -ForegroundColor Green
