# ==============================================================================
# --- LẤY ÂM THANH PHÁT ÂM: OpenRussian trước, hụt thì Google Cloud TTS ---
# OpenRussian (api.openrussian.org/read) thỉnh thoảng trả 500 -> thẻ mất mp3.
# fetch_audio_bytes() thử OpenRussian, thất bại thì sinh giọng Standard tiếng
# Nga bằng Google Cloud TTS. Chỉ TRẢ VỀ BYTES — việc lưu vào Anki media là của
# anki_client.store_word_audio() để mọi lệnh gọi AnkiConnect gom một chỗ.
# ==============================================================================
import base64
import urllib.parse

import requests

from .config import (
    GOOGLE_TTS_API_KEY,
    GOOGLE_TTS_LANG,
    GOOGLE_TTS_URL,
    GOOGLE_TTS_VOICE,
    OPENRUSSIAN_AUDIO_TEMPLATE,
)
from .utils import log_fail, log_warn


def _openrussian_audio_bytes(clean_word):
    """Tải mp3 phát âm từ OpenRussian. Trả về bytes hoặc None (kể cả khi 500)."""
    url = OPENRUSSIAN_AUDIO_TEMPLATE.format(word=urllib.parse.quote(clean_word))
    try:
        r = requests.get(url, timeout=15)
    except Exception as e:
        log_warn(f"OpenRussian audio '{clean_word}' lỗi mạng: {e}")
        return None
    if r.status_code != 200:
        log_warn(f"OpenRussian audio '{clean_word}': HTTP {r.status_code} (sẽ thử Google TTS)")
        return None
    ctype = r.headers.get("Content-Type", "").lower()
    # 200 nhưng trả HTML/JSON lỗi thay vì audio -> coi như hụt
    if "audio" not in ctype and len(r.content) < 1024:
        log_warn(f"OpenRussian audio '{clean_word}': nội dung không phải audio (sẽ thử Google TTS)")
        return None
    return r.content


def google_tts_bytes(text):
    """Sinh mp3 giọng Standard tiếng Nga qua Google Cloud TTS. Trả về bytes hoặc None."""
    if not GOOGLE_TTS_API_KEY:
        log_warn("Chưa cấu hình GOOGLE_TTS_API_KEY trong .env — bỏ qua phao TTS dự phòng.")
        return None
    body = {
        "input": {"text": text},
        "voice": {"languageCode": GOOGLE_TTS_LANG, "name": GOOGLE_TTS_VOICE},
        "audioConfig": {"audioEncoding": "MP3"},
    }
    try:
        r = requests.post(f"{GOOGLE_TTS_URL}?key={GOOGLE_TTS_API_KEY}", json=body, timeout=20)
    except Exception as e:
        log_fail(f"Google TTS lỗi mạng: {e}")
        return None
    if r.status_code != 200:
        # 403 hay gặp: chưa bật Cloud Text-to-Speech API trên project của key
        msg = ""
        try:
            msg = r.json().get("error", {}).get("message", "")
        except ValueError:
            msg = r.text[:200]
        log_fail(f"Google TTS lỗi {r.status_code}: {msg}")
        return None
    content = r.json().get("audioContent")
    if not content:
        log_fail("Google TTS không trả về audioContent.")
        return None
    return base64.b64decode(content)


def fetch_audio_bytes(clean_word):
    """Lấy mp3 phát âm cho 1 từ. Trả về (bytes, nguồn) hoặc (None, "").
    nguồn ∈ {"openrussian", "google_tts"} — để giao diện báo đã dùng phao dự phòng."""
    data = _openrussian_audio_bytes(clean_word)
    if data:
        return data, "openrussian"
    data = google_tts_bytes(clean_word)
    if data:
        log_warn(f"Đã dùng Google TTS thay OpenRussian cho '{clean_word}'.")
        return data, "google_tts"
    return None, ""
