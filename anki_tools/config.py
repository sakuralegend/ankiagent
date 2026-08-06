# ==============================================================================
# --- CẤU HÌNH HỆ THỐNG ---
# Đây là nơi DUY NHẤT chứa các hằng số cấu hình.
# ⚠️ Từ phiên bản VPS: mọi giá trị BÍ MẬT (API key, bot token...) KHÔNG còn
# nằm trong file này nữa mà đọc từ file .env ở thư mục gốc project
# (xem .env.example). Nhờ vậy code có thể đưa lên GitHub an toàn.
# ==============================================================================
import os
from pathlib import Path

from dotenv import load_dotenv

# .env nằm ở thư mục gốc project (cạnh main.py / bot.py), load 1 lần khi import
_PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(_PROJECT_ROOT / ".env")

ANKI_CONNECT_URL = os.environ.get("ANKI_CONNECT_URL", "http://127.0.0.1:8765")

# Đường dẫn file kho Anki, dùng để ĐỌC (chỉ-đọc) ba con số xác nhận "đã gửi hết
# lên AnkiWeb chưa" — xem `anki_client.trang_thai_dong_bo()` và QD-34.
# CỐ Ý để RỖNG làm mặc định: máy nào không khai thì cửa canh trả "không biết" và
# bot nói thật là chưa kiểm được, thay vì đoán bừa là sạch. Trên VPS khai trong
# `.env`; trên laptop bỏ trống cũng không sao (chỉ mất phần kiểm chứng).
ANKI_COLLECTION = os.environ.get("ANKI_COLLECTION", "")

# --- Cấu hình AI (Gemini qua endpoint OpenAI-compatible) ---
# Key chỉ dùng phía Python (bot/CLI trên server). Từ khi gỡ nút AI Refine
# khỏi thẻ, key KHÔNG còn bị nhúng vào thẻ Anki nữa.
CLAUDE_API_URL = os.environ.get(
    "CLAUDE_API_URL",
    "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions",
)
CLAUDE_API_KEY = os.environ.get("CLAUDE_API_KEY", "")
CLAUDE_MODEL = os.environ.get("CLAUDE_MODEL", "gemini-3.5-flash")
# Model dự phòng (phân cách bằng dấu phẩy): khi model chính hết hạn mức miễn phí
# trong ngày (lỗi 429), tự động thử lần lượt các model này. Các model *-lite
# có hạn mức free/ngày cao hơn hẳn dòng flash thường.
CLAUDE_FALLBACK_MODELS = [
    m.strip() for m in os.environ.get(
        "CLAUDE_FALLBACK_MODELS", "gemini-3.1-flash-lite,gemini-flash-lite-latest"
    ).split(",") if m.strip()
]

# --- Telegram Bot ---
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_USER_ID = int(os.environ.get("TELEGRAM_USER_ID", "0"))
# (Không còn deck mặc định: bot hỏi tên deck khi bắt đầu phiên, giống CLI main.py)

OPENRUSSIAN_AUDIO_TEMPLATE = "https://api.openrussian.org/read/ru/{word}"

# --- Âm thanh dự phòng: Google Cloud Text-to-Speech ---
# OpenRussian thỉnh thoảng trả 500 -> thẻ thiếu mp3. Khi đó tự sinh audio bằng
# Google Cloud TTS giọng Standard tiếng Nga (miễn phí 4 triệu ký tự/tháng — dư
# sức cho nhu cầu học từ).
# ⚠️ Key Gemini của AI Studio KHÔNG gọi được Cloud TTS — phải là API key tạo
# trong Google Cloud Console, project đã bật "Cloud Text-to-Speech API".
# Để riêng biến GOOGLE_TTS_API_KEY trong .env; trống thì bỏ qua phao dự phòng.
GOOGLE_TTS_URL = "https://texttospeech.googleapis.com/v1/text:synthesize"
GOOGLE_TTS_API_KEY = os.environ.get("GOOGLE_TTS_API_KEY", "")
GOOGLE_TTS_LANG = os.environ.get("GOOGLE_TTS_LANG", "ru-RU")
GOOGLE_TTS_VOICE = os.environ.get("GOOGLE_TTS_VOICE", "ru-RU-Standard-A")  # giọng nữ
# Đổi tên 19/07/2026 (tên cũ Russian_Premium_OLED_Type_v25) — đổi trong Anki
# thì phải đổi cả đây, và ngược lại. Model 26 thẻ Irregular tên RU_Plural.
MODEL_NAME = "RU_Word"

# --- Deck tổng (kho) chứa các deck con theo chủ đề: <kho>::<topic slug> ---
# (Tên tiếng Anh theo yêu cầu user: dễ gõ khi tìm kiếm/gõ tên deck hơn Cyrillic.)
TOPIC_DECK_PARENT = os.environ.get("TOPIC_DECK_PARENT", "RUSSIAN")

# --- LỘ TRÌNH HỌC HAI GIAI ĐOẠN (26/07/2026) ---------------------------------
# Trước đây thẻ mới rơi thẳng vào một deck `0-inbox` và bắt GÕ tiếng Nga ngay từ
# lần gặp đầu — nhiệm vụ khó nhất có thể. Nay tách làm hai chặng, mỗi chặng đo
# ĐÚNG MỘT thứ:
#
#   GĐ1  STAGE1_DECK (0-quen) — LÀM QUEN. Mặt trước chỉ có chữ Nga, KHÔNG ô gõ.
#        Đo: nhận diện mặt chữ + âm điệu + nghĩa. Rời learning (~2 lượt Good,
#        khoảng 15 phút vì learning steps là 1m+15m) thì job dọn lật field
#        Stage sang "type", forgetCards cho thành thẻ MỚI TINH, rồi đẩy sang GĐ2.
#
#   GĐ2  STAGE2_DECK (1-go) — GÕ. Chính là deck `0-inbox` cũ, giữ nguyên preset
#        `inbox` và gợi ý chữ cái đầu. Đo: chính tả. Rời learning lần nữa thì
#        chuyển về <kho>::<topic slug> theo tag topic:: (như trước giờ vẫn làm).
#
# ⚠️ Vì sao phải là HAI DECK chứ không phải một deck với hạn mức gấp đôi: Anki
# rút thẻ mới theo thứ tự vị trí, nên một deck gộp có thể lĩnh trọn suất cho GĐ1
# và không còn suất nào cho GĐ2. Hai deck thì mỗi bên có ngân sách đảm bảo.
# ⚠️ Kèm theo: trần thẻ mới của DECK CHA phải >= tổng hai con (đã đặt 140), vì
# scheduler v3 lấy trần cha kẹp cả cây — xem git log quanh 21/07/2026.
# Tên "0-"/"1-" để Anki xếp đúng thứ tự học trong danh sách deck.
STAGE1_DECK = f"{TOPIC_DECK_PARENT}::0-quen"
STAGE2_DECK = f"{TOPIC_DECK_PARENT}::1-go"
