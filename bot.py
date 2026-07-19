# ==============================================================================
# --- BOT TELEGRAM: thêm từ + sửa thẻ Anki từ xa (chạy 24/7 trên VPS) ---
# File này CHỈ là điểm vào (systemd trên VPS chạy `python bot.py` — giữ nguyên).
# Toàn bộ ruột bot nằm trong gói tgbot/ (tách 19/07/2026 khi file 1 cục chạm
# ~1.400 dòng): core (phiên/menu), commands (lệnh 1 phát), flow_add (thêm từ),
# flow_edit (/sua + /suadeck), flow_scan (📷 quét ảnh), dispatch (chia text/nút),
# app (lắp handler + khởi động). Muốn sửa luồng nào mở đúng file đó.
# ==============================================================================
from tgbot.app import main

if __name__ == "__main__":
    main()
