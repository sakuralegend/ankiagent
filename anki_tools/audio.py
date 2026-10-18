# ==============================================================================
# --- LẤY ÂM THANH: Yandex SpeechKit giọng alena, LUÔN gửi kèm dấu nhấn ---
# Vì sao Yandex (user nghe so 5 giọng Yandex 18/10/2026, chốt alena 1×):
#   • OpenRussian hỏng CẢ HAI phía: máy đọc kiểu mới (48 kHz) cụt âm đầu — đo 27/98
#     file tiếng bắt đầu ở 0,000 s; bản thu người Shtooka cũng có từ thiếu âm
#     (согласный, user nghe ngay trên app OpenRussian). Chữ trần thì máy tự đoán
#     trọng âm, số nhiều còn dính chữ trùng mặt (дома́ ↔ до́ма).
#   • Yandex có cách đánh dấu nhấn CÓ TÀI LIỆU: `+` trước nguyên âm nhấn (з+амок).
#     Azure chỉ có phiên âm IPA cả từ; Google giới hạn thẻ phát âm ở giọng tốt nhất.
# KHÔNG có phao dự phòng: phao nào không nhận dấu nhấn là dạy sai trọng âm. Hụt
# thì thẻ trống tiếng, scripts/fix_audio.py vá sau.
# Giá v1: 11 USD / 1 triệu ký tự. Cả kho (từ + câu ví dụ) ~300k ký tự.
# Chỉ TRẢ VỀ BYTES — lưu vào media Anki là việc của anki_the.
# ==============================================================================
import hashlib
import os
import re

import requests

from .config import YANDEX_TTS_API_KEY, YANDEX_TTS_URL, YANDEX_TTS_VOICE
from .utils import log_warn, strip_accents_perfectly

_NGUYEN_AM = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
# Mọi file Yandex đi qua thư mục này (git bỏ qua). User chốt 18/10: TẢI ĐỦ toàn bộ
# vào đây trước (fix_audio.py --tai), rồi mới ghi Anki — không ghi dở dang.
THU_MUC_TIENG = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                             "data", "tieng_yandex")


def lay_tieng(text, ten_file):
    """Bytes tiếng `ten_file`: có sẵn trong THU_MUC_TIENG thì đọc, chưa có thì tải
    Yandex rồi cất vào đó. Hụt -> None."""
    duong = os.path.join(THU_MUC_TIENG, ten_file)
    if os.path.exists(duong):
        with open(duong, "rb") as f:
            return f.read()
    data, _ = fetch_audio_bytes(text)
    if data:
        os.makedirs(THU_MUC_TIENG, exist_ok=True)
        with open(duong, "wb") as f:
            f.write(data)
    return data


def chu_yandex(text):
    """`за́мок` / `за'мок` -> `з+амок`: dấu nhấn kiểu Yandex (`+` ĐỨNG TRƯỚC nguyên âm)."""
    text = re.sub(f"([{_NGUYEN_AM}])́", r"+\1", text.strip())
    return re.sub(f"([{_NGUYEN_AM}])'", r"+\1", text)


def ten_file_audio(prefix, word):
    """Tên file tiếng của MỘT TỪ. Đuôi `_<vị trí nhấn>` tách hai chữ trùng mặt
    (за́мок / замо́к) khỏi việc ghi đè chung một file. Tiền tố `ya_` = bản Yandex:
    scripts/fix_audio.py dựa vào nó để biết ô nào chưa chuyển giọng."""
    clean = strip_accents_perfectly(word.strip())
    m = re.search("́|'", word.strip())
    return f"ya_{prefix}_{clean}_{m.start()}.mp3" if m else f"ya_{prefix}_{clean}.mp3"


def ten_file_cau(text):
    """Tên file tiếng của MỘT CÂU: băm nội dung ⇒ câu đổi thì tên đổi, máy khác
    chắc chắn tải bản mới thay vì giữ bản cũ đã lưu."""
    return f"ya_cau_{hashlib.md5(chu_yandex(text).encode('utf-8')).hexdigest()[:12]}.mp3"


def fetch_audio_bytes(text):
    """Đọc `text` (một từ hoặc một câu, dấu nhấn U+0301) bằng Yandex. Trả về
    (bytes, "yandex") hoặc (None, "")."""
    if not YANDEX_TTS_API_KEY:
        log_warn("Chưa có YANDEX_TTS_API_KEY trong .env — thẻ sẽ trống tiếng.")
        return None, ""
    try:
        r = requests.post(YANDEX_TTS_URL, timeout=30,
                          headers={"Authorization": f"Api-Key {YANDEX_TTS_API_KEY}"},
                          data={"text": chu_yandex(text), "lang": "ru-RU",
                                "voice": YANDEX_TTS_VOICE, "format": "mp3"})
    except Exception as e:
        log_warn(f"Yandex TTS '{text[:40]}' lỗi mạng: {e}")
        return None, ""
    if r.status_code != 200 or len(r.content) < 1024:
        log_warn(f"Yandex TTS '{text[:40]}': HTTP {r.status_code} {r.text[:120]}")
        return None, ""
    return r.content, "yandex"
