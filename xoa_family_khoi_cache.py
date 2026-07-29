# -*- coding: utf-8 -*-
"""Gỡ khoá `family` khỏi mọi bản ghi trong `data/grammar_cache.json` (v2 -> v3).

    python xoa_family_khoi_cache.py            # CHẠY KHAN
    python xoa_family_khoi_cache.py --apply    # ghi thật

## Vì sao KHÔNG phải cào lại mạng

`BAN_GHI_V` tăng thường có nghĩa "phải `cao_nguphap.py --nangcap` 950 lượt". Lần
này thì không: v3 chỉ **BỚT** một khoá, dữ liệu mới là **tập con** của dữ liệu cũ
nên gỡ ngay trên file là đủ và đúng. Chỉ lần THÊM khoá mới bắt buộc gọi mạng.

Sau khi chạy file này, chạy tiếp `backfill_grammar_json.py --apply` để field
`GrammarJSON` trên thẻ cũng sạch theo (không phải schema mod, không full sync).

Lý do bỏ `family`: xem khối comment trong `anki_tools/grammar.py` (chỗ
`_adj_declension`) và mục 29/07 trong CHANGELOG.
"""
import io
import json
import os
import sys

from anki_tools import grammar

CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "data", "grammar_cache.json")


def main():
    apply = "--apply" in sys.argv
    d = json.load(io.open(CACHE, encoding="utf-8"))

    co_fam = [k for k, v in d.items() if isinstance(v, dict) and "family" in v]
    cu_v = {}
    for v in d.values():
        if isinstance(v, dict):
            cu_v[v.get("v")] = cu_v.get(v.get("v"), 0) + 1

    # đo hai đầu bằng CÙNG một cách tuần tự hoá, nếu không thì phần "giảm" chỉ là
    # khác nhau ở dấu cách chứ không phải dữ liệu bớt đi
    gon = dict(ensure_ascii=False, separators=(",", ":"))
    truoc = len(json.dumps(d, **gon))
    for v in d.values():
        if isinstance(v, dict):
            v.pop("family", None)
            v["v"] = grammar.BAN_GHI_V
    sau = len(json.dumps(d, **gon))

    print(f"{len(d)} ban ghi | co khoa 'family': {len(co_fam)}")
    print(f"  so hieu truoc: {cu_v}  ->  tat ca ve v{grammar.BAN_GHI_V}")
    print(f"  cache: {truoc/1024/1024:.2f} MB -> {sau/1024/1024:.2f} MB")
    if not apply:
        print("\n(CHAY KHAN — them --apply de ghi that)")
        return
    # ghi qua file tạm rồi đổi tên: đứt điện giữa chừng thì cache cũ còn nguyên,
    # chứ không thành file JSON cụt mà mọi luồng khác đọc vào là nổ.
    tam = CACHE + ".tmp"
    with io.open(tam, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, sort_keys=True, indent=0)
    os.replace(tam, CACHE)
    print(f"\n✅ Da ghi {CACHE}")
    print("   Chay tiep: python backfill_grammar_json.py --apply")


if __name__ == "__main__":
    main()
