# ==============================================================================
# --- CÀO DỮ LIỆU CHO THẺ BIẾN CÁCH ---
# Cố tình KHÔNG dùng anki_tools/scraper.py: hàm bên đó dựng sẵn dict phục vụ thẻ
# từ vựng và không lấy bảng biến cách. Ở đây cần thứ khác (số nhiều, giống, ví dụ
# thô) nên cào riêng — đổi gì bên này cũng không ảnh hưởng thẻ từ vựng.
# ==============================================================================
import json
import urllib.parse

import requests
from bs4 import BeautifulSoup

from anki_tools.utils import convert_stress_to_combining_accent, log_fail

_URL = "https://en.openrussian.org/ru/{word}"
_HEADERS = {"User-Agent": "Mozilla/5.0"}


def fetch_noun(word):
    """Cào 1 danh từ từ OpenRussian, lấy đủ thứ cần cho thẻ số nhiều.

    Trả về dict hoặc None:
      word            số ít có dấu nhấn (dấu combining, hiển thị đẹp trong Anki)
      plural          số nhiều có dấu nhấn
      english         list nghĩa tiếng Anh
      gender          m / f / n
      level           A1..C2 (có thể rỗng — OpenRussian gắn không đầy đủ)
      raw_examples    list {"ru","en"} ví dụ thô của từ (mọi dạng, chưa lọc)
    """
    clean = (word or "").strip()
    if not clean:
        return None
    try:
        res = requests.get(_URL.format(word=urllib.parse.quote(clean, safe="")),
                           headers=_HEADERS, timeout=20)
        if res.status_code != 200:
            log_fail(f"OpenRussian trả về status {res.status_code} cho '{clean}'.")
            return None

        soup = BeautifulSoup(res.text, "html.parser")
        tag = soup.find("script", id="__NEXT_DATA__")
        if not tag:
            log_fail("Không tìm thấy dữ liệu (OpenRussian có thể đã đổi cấu trúc).")
            return None

        words = json.loads(tag.get_text()).get("props", {}).get("pageProps", {}) \
                    .get("info", {}).get("words", [])
        w = next((x for x in words if x.get("type") == "noun"), None)
        if not w:
            log_fail(f"'{clean}' không phải danh từ (hoặc không có trên OpenRussian).")
            return None

        noun = w.get("noun") or {}
        plural = ((noun.get("declension") or {}).get("pl") or {}).get("nom") or ""
        # "дома', домы'" -> lấy dạng chuẩn đầu tiên
        plural = plural.split(",")[0].strip()
        if not plural:
            log_fail(f"'{clean}' không có dạng số nhiều trên OpenRussian "
                     "(danh từ chỉ dùng số ít?).")
            return None

        # ⚠️ Khóa là "tls" (LIST nghĩa), không phải "tl" — dùng nhầm "tl" thì mọi
        # thẻ đều ra "N/A" (đã dính lỗi này 20/07/2026).
        english = []
        for t in w.get("translations") or []:
            if isinstance(t, dict) and isinstance(t.get("tls"), list):
                english.extend(x for x in t["tls"] if isinstance(x, str) and x.strip())
        if not english:
            english = ["N/A"]

        raw_examples = [
            {"ru": convert_stress_to_combining_accent(s.get("ru", "")), "en": s.get("tl", "")}
            for s in (w.get("sentences") or []) if isinstance(s, dict)
        ]

        return {
            "word": convert_stress_to_combining_accent(w.get("accented") or clean),
            "plural": convert_stress_to_combining_accent(plural),
            "english": english,
            "gender": noun.get("gender") or "",
            "level": w.get("level") or "",
            "raw_examples": raw_examples,
        }
    except Exception as e:
        log_fail(f"Lỗi cào '{clean}': {e}")
        return None
