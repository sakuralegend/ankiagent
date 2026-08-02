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
# Test cho cac bug DA TRA HOC PHI. Cua soat kien truc chi bat loi CAU TRUC; day
# la thu duy nhat bat loi LOGIC (badge sai giong, `ё` hong im lang, regex nuot
# chu). Chay offline, ~0,1 giay — khong co ly do gi de bo qua.
python -m unittest discover -s tests -q
if ($LASTEXITCODE -ne 0) {
    Write-Host "TEST DO - dung deploy. Loi logic se lam hong THE THAT ma khong ai bao." -ForegroundColor Red
    exit 1
}

Write-Host "== [2/3] Day code len GitHub ==" -ForegroundColor Cyan
git push
if ($LASTEXITCODE -ne 0) {
    Write-Host "GIT PUSH HONG - dung deploy." -ForegroundColor Red
    exit 1
}

# --- BUOC NAY TUNG THAT BAI TRONG IM LANG (31/07/2026) --------------------
# `git pull` tren VPS bo cuoc khi file du lieu bi bot ghi de len (vd file cache
# ngu phap cu, da bo han o QD-11), nhung script van in "Xong!" mau xanh => nguoi
# deploy tuong da xong, thuc te bot chay CODE CU. Nay bat loi that: kiem ma
# thoat cua ssh, va in ro dieu can lam. Xem muc "cache tracked" trong SONO.md.
Write-Host "== [3/3] Cap nhat VPS + restart bot ==" -ForegroundColor Cyan
ssh $VPS "set -e; cd /root/ankiagent && git pull && venv/bin/pip install -q -r requirements.txt && systemctl restart anki-bot && sleep 3 && systemctl is-active anki-bot"
if ($LASTEXITCODE -ne 0) {
    Write-Host "VPS KHONG CAP NHAT DUOC - bot van chay CODE CU." -ForegroundColor Red
    Write-Host "Hay xem: ssh $VPS 'cd /root/ankiagent && git status'" -ForegroundColor Yellow
    Write-Host "Neu ket vi file du lieu bi sua tai cho: sao luu file do ra /root/ TRUOC," -ForegroundColor Yellow
    Write-Host "doi chieu no voi ban trong git roi moi checkout - dung de git de mu." -ForegroundColor Yellow
    exit 1
}

Write-Host "Xong! Kiem tra bot trong Telegram." -ForegroundColor Green
