#!/bin/bash
# ==============================================================================
# CÀI ĐẶT VPS LẦN ĐẦU (chạy 1 lần duy nhất, trên VPS, với quyền root)
# Cách chạy:  bash setup_vps.sh
# Sau khi xong, làm tiếp theo hướng dẫn trong VPS_SETUP.md (copy .env,
# đăng nhập AnkiWeb qua VNC, rồi start bot).
# ==============================================================================
set -e

echo "===== [1/5] Cài Docker + Git + Python ====="
apt-get update
apt-get install -y docker.io docker-compose-v2 git python3-venv python3-pip
systemctl enable --now docker

echo "===== [2/5] Tạo swap 2GB (chống hết RAM) ====="
if ! swapon --show | grep -q /swapfile; then
    fallocate -l 2G /swapfile
    chmod 600 /swapfile
    mkswap /swapfile
    swapon /swapfile
    echo '/swapfile none swap sw 0 0' >> /etc/fstab
    echo "-> Đã tạo swap 2GB."
else
    echo "-> Swap đã có sẵn, bỏ qua."
fi

echo "===== [3/5] Khởi động container Anki headless ====="
cd "$(dirname "$0")"
docker compose up -d
echo "-> Container anki đang chạy (docker ps để kiểm tra)."

echo "===== [4/5] Tạo môi trường Python cho bot ====="
if [ ! -d venv ]; then
    python3 -m venv venv
fi
venv/bin/pip install --upgrade pip -q
venv/bin/pip install -r requirements.txt -q
echo "-> Đã cài xong thư viện Python."

echo "===== [5/5] Cài service anki-bot (chưa start) ====="
cp anki-bot.service /etc/systemd/system/anki-bot.service
systemctl daemon-reload
systemctl enable anki-bot
echo "-> Service đã cài, sẽ tự chạy mỗi lần VPS khởi động."

echo ""
echo "=========================================================="
echo "✅ CÀI ĐẶT XONG. Còn 3 việc (xem VPS_SETUP.md):"
echo "  1) Copy file .env từ PC lên:  (chạy trên PC)"
echo "     scp .env root@<IP-VPS>:/root/ankiagent/.env"
echo "  2) Đăng nhập AnkiWeb 1 lần qua VNC (xem hướng dẫn)"
echo "  3) Khởi động bot:  systemctl start anki-bot"
echo "     Xem log:        journalctl -u anki-bot -f"
echo "=========================================================="
