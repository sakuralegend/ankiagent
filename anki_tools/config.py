# ==============================================================================
# --- CẤU HÌNH HỆ THỐNG ---
# Đây là nơi DUY NHẤT chứa các hằng số cấu hình.
# ⚠️ Từ phiên bản VPS: mọi giá trị BÍ MẬT (API key, bot token...) KHÔNG còn
# nằm trong file này nữa mà đọc từ file .env ở thư mục gốc project
# (xem .env.example). Nhờ vậy code có thể đưa lên GitHub an toàn.
#
# Các placeholder __CLAUDE_API_URL__, __CLAUDE_MODEL__, __CLAUDE_API_KEY__,
# __ANKI_MOBILE_URL__, __ANKI_LOCAL_URL__ trong templates/back_template.html
# vẫn được thay tự động khi setup_anki_environment() chạy như trước.
# ==============================================================================
import os
from pathlib import Path

from dotenv import load_dotenv

# .env nằm ở thư mục gốc project (cạnh main.py / bot.py), load 1 lần khi import
_PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(_PROJECT_ROOT / ".env")

ANKI_CONNECT_URL = os.environ.get("ANKI_CONNECT_URL", "http://127.0.0.1:8765")

# --- Cấu hình AI (Gemini qua endpoint OpenAI-compatible) ---
# ⚠️ API key sẽ được NHÚNG vào JS của thẻ Anki (nút AI Refine trong webview).
# Ai được share thẻ sẽ xem được key. Rủi ro đã được chấp nhận từ trước.
CLAUDE_API_URL = os.environ.get(
    "CLAUDE_API_URL",
    "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions",
)
CLAUDE_API_KEY = os.environ.get("CLAUDE_API_KEY", "")
CLAUDE_MODEL = os.environ.get("CLAUDE_MODEL", "gemini-3.5-flash")

# --- Telegram Bot ---
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_USER_ID = int(os.environ.get("TELEGRAM_USER_ID", "0"))
DEFAULT_DECK = os.environ.get("DEFAULT_DECK", "Russian")

OPENRUSSIAN_AUDIO_TEMPLATE = "https://api.openrussian.org/read/ru/{word}"
MODEL_NAME = "Russian_Premium_OLED_Type_v25"

# Dùng riêng cho JavaScript nhúng trong thẻ Anki (back_template.html).
# Từ khi chuyển sang sửa thẻ qua bot Telegram, phần lưu-qua-AnkiConnect của nút
# AI Refine chỉ còn hoạt động khi học trên chính máy đang chạy Anki (localhost).
ANKI_CONNECT_LOCAL_URL = os.environ.get("ANKI_CONNECT_LOCAL_URL", "http://127.0.0.1:8765/")
ANKI_CONNECT_MOBILE_URL = os.environ.get("ANKI_CONNECT_MOBILE_URL", "http://127.0.0.1:8765/")
