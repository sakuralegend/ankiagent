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
MODEL_NAME = "Russian_Premium_OLED_Type_v25"
