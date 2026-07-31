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
# Tạo sẵn thư mục dữ liệu với quyền mở, nếu không Anki trong container
# (chạy bằng user thường) sẽ báo "could not create its data folder"
mkdir -p anki-data
chmod 777 anki-data
docker compose up -d

# ⚠️ Image gắn addon AnkiConnect vào /data bằng symlink lúc build, nhưng khi
# ta mount thư mục anki-data (trống) đè lên /data thì symlink bị che mất
# -> phải chép addon thật vào volume + mở webBindAddress cho docker port map.
echo "-> Chờ container khởi tạo dữ liệu lần đầu..."
sleep 20
if [ ! -e anki-data/addons21/AnkiConnectDev/config.json ]; then
    echo "-> Cài addon AnkiConnect vào volume..."
    docker exec anki cp -r /app/anki-connect/plugin /data/addons21/AnkiConnectDev
    python3 - <<'PYEOF'
import json
p = 'anki-data/addons21/AnkiConnectDev/config.json'
cfg = json.load(open(p))
cfg['webBindAddress'] = '0.0.0.0'
json.dump(cfg, open(p, 'w'), indent=2)
print('-> Da bat webBindAddress=0.0.0.0')
PYEOF
    docker restart anki
fi
echo "-> Container anki đang chạy (docker ps để kiểm tra)."

echo "===== [4/5] Tạo môi trường Python cho bot ====="
if [ ! -d venv ]; then
    python3 -m venv venv
fi
venv/bin/pip install --upgrade pip -q
venv/bin/pip install -r requirements.txt -q
echo "-> Đã cài xong thư viện Python."

echo "===== [5/6] Cài service anki-bot (chưa start) ====="
cp anki-bot.service /etc/systemd/system/anki-bot.service
systemctl daemon-reload
systemctl enable anki-bot
echo "-> Service đã cài, sẽ tự chạy mỗi lần VPS khởi động."

# ==============================================================================
# [6/6] BỐN THỨ THÊM 31/07/2026 — thiếu chúng thì hệ thống VẪN CHẠY nhưng mất
# hết lưới an toàn, và mất trong IM LẶNG. Chúng từng chỉ được cấu hình bằng tay
# trên VPS, không ghi ở đâu ⇒ dựng lại máy mới là mất sạch mà không ai biết.
# Đó đúng là lỗi "sao lưu chưa từng khôi phục thử" ở tầng cao hơn, nên tự động
# hoá luôn thay vì viết vào tài liệu và trông chờ người đọc nhớ.
# ==============================================================================
echo "===== [6/6] Lưới an toàn: chuông báo · cache ngoài repo · trần log ====="

# (a) Chuông báo khi bot chết — đường Telegram ĐỘC LẬP với bot (QD-04).
cp anki-bot-alert.service /etc/systemd/system/anki-bot-alert.service
systemctl daemon-reload
# Vòng kiểm 15 phút, bắt cả trường hợp bot bị dừng hẳn (OnFailure không bắt được).
( crontab -l 2>/dev/null | grep -v canhbao_bot_chet
  echo "*/15 * * * * /usr/bin/env bash /root/ankiagent/scripts/canhbao_bot_chet.sh >/dev/null 2>&1"
) | crontab -
echo "-> Chuông báo bot chết: đã cài (systemd OnFailure + cron 15')."

# (b) Cache ngữ pháp của bot nằm NGOÀI repo (QD-05) — để `git pull` không kẹt
#     vì bot ghi đè file mà git đang quản.
mkdir -p /root/anki-cache
if [ -f data/grammar_cache.json ] && [ ! -f /root/anki-cache/grammar_cache.json ]; then
    cp data/grammar_cache.json /root/anki-cache/grammar_cache.json
fi
echo "-> Cache ngữ pháp: /root/anki-cache/ (đường dẫn khai trong anki-bot.service)."

# (c) Trần dung lượng log, để journald không phình vô hạn rồi tự xoá mất phần cũ.
sed -i 's/^#\?SystemMaxUse=.*/SystemMaxUse=500M/; s/^#\?MaxRetentionSec=.*/MaxRetentionSec=3month/' \
    /etc/systemd/journald.conf
systemctl restart systemd-journald
echo "-> Log: giữ tối đa 500M / 3 tháng."

echo ""
echo "=========================================================="
echo "✅ CÀI ĐẶT XONG. Còn 3 việc (xem VPS_SETUP.md):"
echo "  1) Copy file .env từ PC lên:  (chạy trên PC)"
echo "     scp .env root@<IP-VPS>:/root/ankiagent/.env"
echo "  2) Đăng nhập AnkiWeb 1 lần qua VNC (xem hướng dẫn)"
echo "  3) Khởi động bot:  systemctl start anki-bot"
echo "     Xem log:        journalctl -u anki-bot -f"
echo "=========================================================="
