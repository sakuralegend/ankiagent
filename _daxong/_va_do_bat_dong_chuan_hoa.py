# -*- coding: utf-8 -*-
"""Đo bất đồng giữa các luật chuẩn hoá tiếng Nga đang tồn tại rải rác trong repo
(SONO.md, mục "4 luật chuẩn hoá tiếng Nga khác nhau", ghi 31/07/2026).

CHỈ ĐỌC — không sửa gì, không gọi Anki ghi, chỉ AnkiConnect findNotes/notesInfo.

Hai luật CÙNG MỤC ĐÍCH (chuẩn hoá để so sánh/dedup, KHÔNG gộp ё→е) đáng lẽ phải
luôn ra cùng kết quả — đây là chỗ SONO.md nghi có bug:
  A. anki_tools/utils.py:strip_accents_perfectly — bỏ dấu trọng âm U+0301 + nháy,
     hạ thường. KHÔNG unicodedata.normalize.
  B. anki_tools/ai_client.py:_clean_scan_word (inline) — NFC-normalize trước rồi
     mới bỏ dấu. Nếu input có ё dạng TỔ HỢP (е + U+0308) mà A không NFC thì hai
     hàm cho ra chuỗi khác nhau ở byte, dù nhìn y hệt.

Hai luật kia (bare() trong congcu.py / kiemtra.py) phục vụ mục đích KHÁC (tra từ
điển nouns.csv), cố ý gộp ё→е — không kỳ vọng giống nhóm A/B. Đo riêng để xác
nhận hai bản bare() (hiện là code trùng nhau sau khi gộp MIEN_TRU ở G0) còn nhất
quán, không lệch âm thầm.

Rỗng cả hai nhóm ⇒ đóng nợ trong SONO.md. Không rỗng ⇒ lỗi thật, vá theo luật
"kiểm ngược lô cũ" ở CACHLAM.md — KHÔNG gộp hàm trước khi đo (SONO.md dặn vậy).

Chạy: python _va_do_bat_dong_chuan_hoa.py
"""
import importlib.util
import io
import json
import os
import sys
import unicodedata
import urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
from anki_tools.utils import strip_accents_perfectly  # noqa: E402  (Rule A, import công khai)

ANKI = "http://127.0.0.1:8765"


def _load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def rule_b(value):
    """Sao y hệt logic trong anki_tools/ai_client.py:_clean_scan_word — KHÔNG
    import hàm private xuyên module (L1/S2), chỉ chép lại đúng 1 dòng công thức."""
    if not isinstance(value, str):
        return None
    return unicodedata.normalize("NFC", value.strip().lower()).replace("́", "")


def ac(action, **params):
    req = urllib.request.Request(
        ANKI, json.dumps({"action": action, "version": 6, "params": params}).encode())
    out = json.load(urllib.request.urlopen(req, timeout=180))
    if out.get("error"):
        raise RuntimeError(f"{action}: {out['error']}")
    return out["result"]


def gom_tu_that():
    """Gom mọi từ Nga thật đang có trong repo/Anki — CHỈ ĐỌC."""
    words = set()

    with io.open(os.path.join(ROOT, "data", "grammar_cache.json"), encoding="utf-8") as f:
        words.update(json.load(f).keys())

    with io.open(os.path.join(ROOT, "data", "huongdan", "kho", "tudien.json"), encoding="utf-8") as f:
        for item in json.load(f):
            for key in ("w", "wc"):
                v = item.get(key)
                if v:
                    words.add(v)

    note_ids = ac("findNotes", query='note:"RU_Word"')
    for n in ac("notesInfo", notes=note_ids):
        for field in ("Word", "WordClean"):
            v = n["fields"].get(field, {}).get("value", "")
            if v:
                words.add(v)

    return words


def main():
    congcu = _load_module(os.path.join(ROOT, "data", "huongdan", "kho", "congcu.py"), "_ro_congcu")
    # kiemtra.py tự tin sys.path[0] có thư mục của nó (đúng khi `python kiemtra.py`
    # chạy trực tiếp) — nạp qua importlib thì không tự có, phải chèn tay.
    sys.path.insert(0, os.path.join(ROOT, "data", "huongdan"))
    kiemtra = _load_module(os.path.join(ROOT, "data", "huongdan", "kiemtra.py"), "_ro_kiemtra")

    words = gom_tu_that()
    print(f"Tong so tu that gom duoc: {len(words)}\n")

    bat_dong_ab = []
    bat_dong_cd = []
    for w in sorted(words):
        a = strip_accents_perfectly(w)
        b = rule_b(w)
        if a != b:
            bat_dong_ab.append((w, a, b))

        c = congcu.bare(w)
        d = kiemtra.bare(w)
        if c != d:
            bat_dong_cd.append((w, c, d))

    print("=== NHOM A/B (strip_accents_perfectly vs NFC-clean, CUNG muc dich) ===")
    if not bat_dong_ab:
        print("  (khong co bat dong)")
    for w, a, b in bat_dong_ab[:50]:
        print(f"  '{w}' -> A={a!r} B={b!r}")
    if len(bat_dong_ab) > 50:
        print(f"  ... con {len(bat_dong_ab) - 50}")

    print("\n=== NHOM C/D (bare() congcu.py vs kiemtra.py, cung muc dich tra tu dien) ===")
    if not bat_dong_cd:
        print("  (khong co bat dong)")
    for w, c, d in bat_dong_cd[:50]:
        print(f"  '{w}' -> C={c!r} D={d!r}")
    if len(bat_dong_cd) > 50:
        print(f"  ... con {len(bat_dong_cd) - 50}")


if __name__ == "__main__":
    main()
