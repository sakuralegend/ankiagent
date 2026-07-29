# -*- coding: utf-8 -*-
"""Điền badge THỂ ĐỘNG TỪ (field AspectBadge) cho các thẻ ĐÃ CÓ trong Anki.

Thẻ tạo từ 29/07/2026 trở đi tự có badge (scraper lấy `verb.aspect` lúc cào).
Script này lo phần quá khứ: ~75 động từ đã nằm sẵn trong bộ sưu tập.

    python backfill_aspect.py            # CHẠY KHAN — in ra, không ghi gì
    python backfill_aspect.py --apply    # ghi thật

Nguồn dữ liệu là `data/grammar_cache.json` (đã cào sẵn cả kho). Từ nào chưa có
trong cache thì gọi mạng lấy về — nên chạy được cả với thẻ mới thêm sau này.

🔴 TRƯỚC KHI CHẠY: field `AspectBadge` phải tồn tại. Chạy `python main.py` một
lần (setup_anki_environment tự thêm field), hoặc thêm tay trong Anki. Thêm field
là schema mod ⇒ Anki đòi FULL SYNC một lần, và VPS có thể kẹt im lặng ở
"Sync status 2" — kiểm `journalctl` trên VPS sau khi sync.
"""
import json
import re
import sys
import urllib.request

from anki_tools import grammar
from anki_tools.config import ANKI_CONNECT_URL, MODEL_NAME

FIELD = "AspectBadge"


def ac(action, **params):
    req = urllib.request.Request(
        ANKI_CONNECT_URL,
        json.dumps({"action": action, "version": 6, "params": params}).encode())
    out = json.load(urllib.request.urlopen(req, timeout=120))
    if out.get("error"):
        raise RuntimeError(f"{action}: {out['error']}")
    return out["result"]


def main():
    apply = "--apply" in sys.argv

    if FIELD not in ac("modelFieldNames", modelName=MODEL_NAME):
        print(f"❌ Model {MODEL_NAME} CHƯA có field {FIELD}.")
        print("   Chạy `python main.py` một lần để nó tự thêm, rồi chạy lại.")
        return

    notes = ac("notesInfo", notes=ac("findNotes", query=f'note:"{MODEL_NAME}"'))
    print(f"{len(notes)} thẻ {MODEL_NAME}")

    doi, giu, khong_ro, goi_mang = [], 0, [], 0
    for n in notes:
        f = n["fields"]
        wc = (f.get("WordClean", {}).get("value") or "").strip()
        if not wc:
            continue
        rec = grammar.get_cached(wc)
        if not rec:                       # thẻ mới thêm, chưa nằm trong cache
            rec = grammar.fetch_grammar(wc)
            goi_mang += 1
        pos_the = (f.get("PoS", {}).get("value") or "").strip().lower()
        la_dong_tu = rec.get("pos") == "verb" or pos_the in ("v", "verb")

        moi = grammar.aspect_badge_html(rec.get("aspect")) if la_dong_tu else ""
        cu = f.get(FIELD, {}).get("value", "")
        if la_dong_tu and not moi:
            # Động từ mà từ điển không nói thể -> KHÔNG im lặng bỏ qua. Badge
            # trống ở đúng chỗ user cần nhất là lỗi đắt nhất của cả việc này.
            khong_ro.append(wc)
        if moi == cu:
            giu += 1
            continue
        doi.append((n["noteId"], wc, cu, moi))

    print(f"\n=== SẼ ĐỔI {len(doi)} thẻ (giữ nguyên {giu}) ===")
    for _, wc, cu, moi in doi:
        cu_txt = re.sub(r"<[^>]+>", "", cu) or "(trống)"
        moi_txt = re.sub(r"<[^>]+>", "", moi) or "(xoá)"
        print(f"  {wc:24s} {cu_txt:18s} -> {moi_txt}")

    if khong_ro:
        print(f"\n⚠️ {len(khong_ro)} ĐỘNG TỪ từ điển KHÔNG cho biết thể "
              f"-> badge để trống, phải xử lý tay:")
        print("   " + " · ".join(khong_ro))
    if goi_mang:
        print(f"\n({goi_mang} từ chưa có trong cache, đã gọi mạng lấy về)")

    if not apply:
        print("\n(CHẠY KHAN — thêm --apply để ghi thật)")
        return
    for nid, _, _, moi in doi:
        ac("updateNoteFields", note={"id": nid, "fields": {FIELD: moi}})
    print(f"\n✅ Đã ghi {len(doi)} thẻ.")
    print("sync: " + str(ac("sync")))


if __name__ == "__main__":
    main()
