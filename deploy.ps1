# ==============================================================================
# DEPLOY TỪ PC LÊN VPS - chạy trên PC sau khi sửa code xong:
#   .\deploy.ps1
# Luồng: đẩy code lên GitHub -> VPS kéo về -> cài dep mới (nếu có) -> restart bot.
# Container Anki KHÔNG bị đụng tới (không downtime).
# ==============================================================================
$VPS = "root@161.248.146.56"

# --- CUA CHAN TRUOC KHI DAY DI (G1, QD-02) --------------------------------
# Vi sao dat o day: day la DUONG DUY NHAT code roi khoi PC. Khong dua vao tu
# giac (da chung minh khong hieu qua: 10 wrapper ra doi SAU khi phat bieu luat),
# ma dua vao cho code bat buoc di qua. Hai bac re nhat cua thang nghiem thu.
Write-Host "== [1/3] Soat kien truc + import ==" -ForegroundColor Cyan
$env:PYTHONIOENCODING = "utf-8"
python soatkientruc.py
if ($LASTEXITCODE -ne 0) {
    Write-Host "SOAT DO - dung deploy. Sua vi pham moi roi chay lai." -ForegroundColor Red
    exit 1
}
python -c "import bot, main"
if ($LASTEXITCODE -ne 0) {
    Write-Host "IMPORT GAY - dung deploy. Loi nay se giet bot ngay khi khoi dong." -ForegroundColor Red
    exit 1
}

Write-Host "== [2/3] Day code len GitHub ==" -ForegroundColor Cyan
git push

Write-Host "== [3/3] Cap nhat VPS + restart bot ==" -ForegroundColor Cyan
ssh $VPS "cd /root/ankiagent && git pull && venv/bin/pip install -q -r requirements.txt && systemctl restart anki-bot && sleep 3 && systemctl --no-pager status anki-bot | head -12"

Write-Host "Xong! Kiem tra bot trong Telegram." -ForegroundColor Green
