# ==============================================================================
# --- TẦNG 2 CỦA MẢNG NGỮ PHÁP: bóc dữ liệu cho thẻ biến cách ---
#
# Vẫn KHÔNG dùng `anki_tools/scraper.py`: hàm bên đó bóc field cho thẻ TỪ VỰNG,
# cần thứ khác hẳn. Nhưng phần TẢI TRANG thì dùng chung `grammar.fetch_page()`
# — nó là tầng 1, nơi duy nhất gọi mạng và biết đường dẫn JSON.
#
# Trước 29/07 file này tự GET + tự moi `__NEXT_DATA__`. Ba nơi cùng biết đường
# dẫn `props.pageProps.info.words` nghĩa là OpenRussian đổi cấu trúc thì phải
# sửa ba chỗ — mà hai chỗ nằm trong module dễ quên. Loại lỗi này ĐÃ xảy ra ở
# chính file này (xem chú thích khoá `tls` bên dưới, dính 20/07/2026).
#
# ⚠️ LUẬT CHỌN MỤC vẫn giữ RIÊNG ở đây và cố ý khác mảng từ vựng: thẻ số nhiều
# chỉ có nghĩa với DANH TỪ, nên phải ép `type == "noun"`; mảng từ vựng thì chọn
# theo mục hợp chính tả nhất, không ép từ loại.
# ==============================================================================
from anki_tools.grammar import fetch_page
from anki_tools.utils import convert_stress_to_combining_accent, log_fail


def pick_noun(words):
    """LUẬT CHỌN MỤC của mảng ngữ pháp: lấy mục DANH TỪ.

    Cố ý khác luật của mảng từ vựng (`grammar._pick_word_object` chọn theo chính
    tả + ưu tiên mục có bảng chia, không ép từ loại). Thẻ số nhiều chỉ có nghĩa
    với danh từ, nên ở đây ép `type == "noun"` là đúng.

    ⚠️ Từ có HAI mục danh từ (đồng tự, vd `мир` hoà bình / thế giới) thì lấy mục
    có bảng số nhiều; hết thảy đều có thì lấy mục ĐẦU (thứ tự OpenRussian trả về
    ~ theo tần suất). Đây là chỗ mơ hồ đã báo user 29/07 — chưa có luật nào tách
    được hai nghĩa mà không đọc ngữ cảnh.
    """
    dt = [w for w in (words or []) if isinstance(w, dict) and w.get("type") == "noun"]
    if not dt:
        return None
    co_pl = [w for w in dt
             if ((w.get("noun") or {}).get("declension") or {}).get("pl", {}).get("nom")]
    return (co_pl or dt)[0]


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
        words = (fetch_page(clean, timeout=20) or {}).get("words") or []
        w = pick_noun(words)
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
