# -*- coding: utf-8 -*-
"""Chuẩn hoá CHỮ NGA + hằng dùng chung của họ grammar — tách từ grammar.py
(03/08/2026, QD-19). Mảnh LÁ: không import mảnh grammar nào khác."""
import re

from .utils import convert_stress_to_combining_accent

ACUTE = "́"
VOWELS = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"

# 6 cách. Nhãn phải NGẮN: bảng nằm trong ô rộng 368px trên iPhone, ba cột.
CASES = [("nom", "1 · chủ ngữ"), ("gen", "2 · sở hữu"), ("dat", "3 · tặng"),
         ("acc", "4 · đối"), ("inst", "5 · công cụ"), ("prep", "6 · giới")]
PERSONS = ["я", "ты", "он / она́", "мы", "вы", "они́"]
PASTS = ["он", "она́", "оно́", "они́"]
GIONG_TT = [("m", "он (đực)"), ("f", "она́ (cái)"), ("n", "оно́ (trung)"), ("pl", "они́ (số nhiều)")]


def acc(word):
    """Dạng OpenRussian (`сто'л`) -> dấu trọng âm ghép (`стол`).

    Từ MỘT nguyên âm thì BỎ dấu: OpenRussian vẫn đánh dấu (`сто'л`, `го'д`) nhưng
    trên thẻ nó chỉ gây nhiễu — một nguyên âm thì không có chỗ nào khác để nhấn.
    Bộ soát `congcu.py soat` cũng dùng đúng luật này (chỉ đòi dấu khi >= 2 nguyên âm).
    """
    if not word:
        return ""
    out = convert_stress_to_combining_accent(word.strip())
    # 🔴 `ё` LUÔN mang trọng âm sẵn, nên `ё` + dấu là SAI CHÍNH TẢ, không phải một
    # cách viết. Nguồn vẫn ghi thế ở vài từ (`шофё́р` 12 ô, `зачё́там`, `неё́`).
    # Vá ở ĐÂY chứ không vá dữ liệu đã cào: 30/07 tôi sửa thẳng bản ghi cache cũ
    # rồi `--nangcap` cào lại là dấu thừa quay về đủ 15 chỗ, và một thẻ đã nạp
    # bản sai. Sửa dữ liệu thì lần cào sau mất; sửa phép biến đổi thì vĩnh viễn.
    out = out.replace("ё" + ACUTE, "ё").replace("Ё" + ACUTE, "Ё")
    # Ô có nhiều biến thể: "лю'ди, челове'ки" -> xử lý từng biến thể một
    parts = [p.strip() for p in out.split(",")]
    fixed = []
    for p in parts:
        toks = []
        for t in p.split():
            if len(re.findall(f"[{VOWELS}]", t)) <= 1:
                t = t.replace(ACUTE, "")
            toks.append(t)
        fixed.append(" ".join(toks))
    return ", ".join(x for x in fixed if x)


def bare(word):
    """Bỏ dấu trọng âm, giữ nguyên ё (ё ≠ е — xem congcu.khoa_note)."""
    return (word or "").replace(ACUTE, "").replace("'", "").strip().lower()


def stress_pos(form):
    """Vị trí trọng âm tính theo THỨ TỰ NGUYÊN ÂM (1 = nguyên âm đầu).

    Đếm theo nguyên âm chứ không theo ký tự vì thân từ dài ngắn khác nhau giữa
    các ô; 0 = không xác định được (từ một nguyên âm, hoặc ô có nhiều biến thể).
    """
    form = (form or "").split(",")[0].strip()
    if "ё" in form.lower():
        form = re.sub("ё", "е" + ACUTE, form, count=1, flags=re.I)
    n = 0
    for ch in form:
        if ch in VOWELS:
            n += 1
        elif ch == ACUTE:
            return n
    # Một nguyên âm thì chính nó mang trọng âm — `acc()` đã bỏ dấu cho đỡ rối
    # mắt, nhưng ở đây phải trả lại, nếu không `стол → стола́` (trọng âm chạy từ
    # thân ra đuôi, đúng thứ cần bắt) sẽ lọt vì hai đầu cùng ra 0.
    return 1 if n == 1 else 0
