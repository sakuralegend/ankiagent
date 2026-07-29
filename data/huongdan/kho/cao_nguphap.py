# -*- coding: utf-8 -*-
"""Cào dữ liệu ngữ pháp (thể · sống/không sống · bảng chia · họ từ) cho CẢ KHO.

Chạy MỘT lần, kết quả nằm ở `data/grammar_cache.json` rồi dùng mãi — từ điển
OpenRussian là ảnh chụp tĩnh. Ngắt giữa chừng cứ chạy lại: từ nào có trong cache
thì bỏ qua, nên nó tiếp tục đúng chỗ đang dở.

    python data/huongdan/kho/cao_nguphap.py            # cào từ còn thiếu
    python data/huongdan/kho/cao_nguphap.py --anki     # lấy danh sách từ ANKI (kể
                                                       #   cả từ mới chưa vào kho)
    python data/huongdan/kho/cao_nguphap.py --lai TU   # cào lại một từ

⚠️ `tudien.json` là ảnh chụp ĐÔNG LẠNH 912 từ, không tự lớn theo bộ sưu tập.
Từ mới user thêm hằng ngày chỉ có trong Anki ⇒ muốn cào đủ thì dùng `--anki`.
"""
import io
import json
import os
import sys
import urllib.request

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", ".."))
from anki_tools import grammar                                   # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
TUDIEN = os.path.join(HERE, "tudien.json")


def tu_tu_anki():
    """WordClean của MỌI note RU_Word đang có trong Anki."""
    def ac(action, **params):
        req = urllib.request.Request(
            "http://127.0.0.1:8765",
            json.dumps({"action": action, "version": 6, "params": params}).encode())
        out = json.load(urllib.request.urlopen(req, timeout=120))
        if out.get("error"):
            raise RuntimeError(f"{action}: {out['error']}")
        return out["result"]

    ra = []
    for n in ac("notesInfo", notes=ac("findNotes", query="note:RU_Word")):
        wc = (n["fields"].get("WordClean", {}).get("value") or "").strip()
        if wc:
            ra.append(wc)
    return ra


def main():
    if "--lai" in sys.argv:
        for w in sys.argv[sys.argv.index("--lai") + 1:]:
            rec = grammar.fetch_grammar(w, refresh=True)
            print(json.dumps(rec, ensure_ascii=False, indent=1))
        return

    if "--anki" in sys.argv:
        tu = tu_tu_anki()
        print(f"nguon: ANKI ({len(tu)} note)")
    else:
        tu = [x["wc"] for x in json.load(io.open(TUDIEN, encoding="utf-8"))]
    cache = grammar._cache()
    can = [w for w in tu if grammar.bare(w) not in cache]
    print(f"kho {len(tu)} tu | da co {len(tu) - len(can)} | can cao {len(can)}",
          flush=True)
    hong = []
    for i, w in enumerate(can, 1):
        rec = grammar.fetch_grammar(w)
        if not rec:
            hong.append(w)
        if i % 25 == 0 or i == len(can):
            print(f"  {i}/{len(can)}  ({len(hong)} hong)", flush=True)
    print(f"XONG. cache: {len(grammar._cache())} tu | khong lay duoc: {len(hong)}")
    if hong:
        print("  " + " ".join(hong))


if __name__ == "__main__":
    main()
