# ==============================================================================
# --- LẤY ÂM THANH PHÁT ÂM: CHỈ OpenRussian, và LUÔN gửi kèm dấu nhấn ---
# Endpoint api.openrussian.org/read/ru/<chữ> trả HAI loại file:
#   • bản thu NGƯỜI (dự án Shtooka, ID3 chứa "SWAC_") — chỉ khi gửi chữ TRẦN và
#     OpenRussian có bản thu cho đúng chữ đó;
#   • máy đọc Yandex (ID3 "Lavf") — mọi trường hợp còn lại. Gửi chữ TRẦN thì máy
#     TỰ ĐOÁN trọng âm; gửi `приглаша'ть` (nháy đơn sau nguyên âm nhấn) thì máy
#     đọc ĐÚNG dấu — chính cách trang OpenRussian đọc bảng chia động từ.
# 🔴 Bản cũ gửi chữ trần cho mọi từ, hụt thì rơi về Google TTS (cũng không nhận
# dấu). Đo 18/10/2026: 171/1794 thẻ RU_Word và 110/124 audio số nhiều RU_Plural
# là máy tự đoán; số nhiều còn dính bản thu người của chữ TRÙNG MẶT (дома́ ↔
# до́ма "ở nhà"). Google TTS bị BỎ hẳn: thà thẻ trống tiếng (scripts/fix_audio.py
# vá sau) còn hơn dạy sai trọng âm. Đừng thêm lại phao nào không nhận dấu nhấn.
# Chỉ TRẢ VỀ BYTES — lưu vào media Anki là việc của anki_the.store_word_audio().
# ==============================================================================
import re
import urllib.parse

import requests

from .config import OPENRUSSIAN_AUDIO_TEMPLATE
from .utils import log_warn, strip_accents_perfectly


def la_ban_nguoi(data):
    """True nếu mp3 là bản thu người Shtooka (thẻ ID3 SWAC_ nằm ở đầu file)."""
    return bool(data) and b"SWAC_" in data[:8000]


def chu_co_dau(word):
    """`приглаша́ть` -> `приглаша'ть`: dạng dấu nhấn mà endpoint /read hiểu."""
    return word.strip().replace("́", "'")


def ten_file_audio(prefix, word):
    """Tên file media. Đuôi `_<vị trí nhấn>` tách hai chữ trùng mặt (за́мок /
    замо́к) khỏi việc ghi đè chung một file, và cho thẻ vá một tên MỚI để máy
    khác chắc chắn tải lại thay vì giữ bản cũ đã lưu."""
    clean = strip_accents_perfectly(word.strip())
    m = re.search("́|'", word.strip())
    return f"{prefix}_{clean}_{m.start()}.mp3" if m else f"{prefix}_{clean}.mp3"


def _openrussian_audio_bytes(text):
    """Tải mp3 từ OpenRussian. Trả về bytes hoặc None (kể cả khi 500)."""
    url = OPENRUSSIAN_AUDIO_TEMPLATE.format(word=urllib.parse.quote(text))
    try:
        r = requests.get(url, timeout=15)
    except Exception as e:
        log_warn(f"OpenRussian audio '{text}' lỗi mạng: {e}")
        return None
    if r.status_code != 200:
        log_warn(f"OpenRussian audio '{text}': HTTP {r.status_code}")
        return None
    ctype = r.headers.get("Content-Type", "").lower()
    # 200 nhưng trả HTML/JSON lỗi thay vì audio -> coi như hụt
    if "audio" not in ctype and len(r.content) < 1024:
        log_warn(f"OpenRussian audio '{text}': nội dung không phải audio")
        return None
    return r.content


def fetch_audio_bytes(word, ban_nguoi_truoc=True):
    """Lấy mp3 cho 1 từ CÓ DẤU NHẤN (`приглаша́ть`). Trả về (bytes, "openrussian")
    hoặc (None, "").

    ban_nguoi_truoc=True: thử chữ trần, nhận NẾU là bản thu người; không thì đọc
    máy kèm dấu. Truyền False cho dạng biến cách (số nhiều…): chữ trần của chúng
    hay trùng mặt một từ khác, bản thu người khi đó là người đọc NHẦM TỪ."""
    co_dau = chu_co_dau(word)
    tran = strip_accents_perfectly(co_dau)
    if ban_nguoi_truoc and co_dau.lower() != tran:
        data = _openrussian_audio_bytes(tran)
        if la_ban_nguoi(data):
            return data, "openrussian"
    # Từ không dấu nhấn (một âm tiết, có ё) thì co_dau == chữ trần: một lượt là đủ,
    # OpenRussian tự trả bản người nếu có.
    data = _openrussian_audio_bytes(co_dau)
    return (data, "openrussian") if data else (None, "")
