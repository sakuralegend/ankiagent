# Gói bot Telegram — tách từ bot.py 19/07/2026 khi file chạm ~1.400 dòng.
# Mỗi luồng 1 file: core (phiên/menu), commands (lệnh 1 phát), flow_add (thêm từ),
# flow_edit (/sua + /suadeck), flow_scan (quét ảnh), dispatch (bộ chia text/nút),
# app (lắp handler + khởi động). Điểm vào vẫn là bot.py ở gốc repo (systemd giữ nguyên).
