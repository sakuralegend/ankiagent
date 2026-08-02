# -*- coding: utf-8 -*-
"""Cào dữ liệu ngữ pháp (thể · sống/không sống · bảng chia · họ từ) cho CẢ KHO.

🔴 BẮT BUỘC MỞ ANKI (QD-11) — thẻ là nơi DUY NHẤT dữ liệu cào được tồn tại lâu
dài; không còn file `grammar_cache.json` làm bộ đệm trên đĩa. Đóng Anki thì lệnh
này KÊU TO rồi dừng ngay từ dòng đầu, không âm thầm cào xong rồi mất trắng.
Ngắt giữa chừng cứ chạy lại: từ nào thẻ đã có thì bỏ qua, nên nó tiếp tục đúng
chỗ đang dở.

    python data/huongdan/kho/cao_nguphap.py            # cào từ còn thiếu
    python data/huongdan/kho/cao_nguphap.py --anki     # lấy danh sách từ ANKI (kể
                                                       #   cả từ mới chưa vào kho)
    python data/huongdan/kho/cao_nguphap.py --sotu     # vá SỐ TỪ hụt bảng bằng
                                                       #   Wiktionary (nguồn 2)
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
from anki_tools import grammar, soat_nguphap                     # noqa: E402

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


def va_so_tu():
    """Vá SỐ TỪ mà OpenRussian chỉ lưu dạng gốc (`formType = ru_base`).

    28 số từ đếm cơ bản (`два · со́рок · сто`…) không có bảng biến cách trên
    OpenRussian — đúng nhóm user dùng hằng ngày và dễ sai nhất. Lấy bù từ
    Wiktionary tiếng Nga, ghi kèm `nguon` để bảng dựng ra ghi đúng xuất xứ.
    """
    from anki_tools import wiktionary
    cache = grammar._cache()
    can = [wc for wc, r in sorted(cache.items())
           if r and r.get("pos") == "numeral" and not r.get("numDecl")]
    print(f"{len(can)} so tu chua co bang -> hoi Wiktionary", flush=True)
    duoc, hong = 0, []
    for i, wc in enumerate(can, 1):
        them = wiktionary.fetch_numeral(wc)
        if not them:
            hong.append(wc)
        else:
            cache[wc].update(them)
            grammar.remember(wc, cache[wc])    # ghi thẳng vào thẻ — không còn file cache (QD-11)
            duoc += 1
        if i % 10 == 0 or i == len(can):
            print(f"  {i}/{len(can)}  (duoc {duoc})", flush=True)
    print(f"XONG: va duoc {duoc}/{len(can)}")
    if hong:
        print("  Wiktionary cung khong co: " + " ".join(hong))


def main():
    """Chạy việc, rồi SOI dữ liệu ngữ pháp một lượt trước khi thoát.

    Soi ở CUỐI chứ không ở đầu, và chỉ MỘT lần: lúc này bộ đệm RAM đã gồm cả dữ
    liệu sẵn có trong thẻ (lấp ở đầu `_chay`) lẫn mọi từ vừa cào về, nên một lượt
    quét phủ hết mọi nhánh (`--anki`, `--lai`, `--nangcap`, `--sotu`) mà không
    phải nhớ chèn lời gọi vào từng nhánh — thứ chắc chắn sẽ quên ở nhánh thứ năm.

    Đây là cửa cho món nợ ② ở `SONO.md`: bản vá `ке́ды` nằm trong THẺ chứ không
    trong repo, nên cào lại là nguồn sai quay về — im lặng, cho tới khi có cửa này.
    """
    try:
        _chay()
    finally:
        # `doc_cache`, KHÔNG phải `_cache`: cửa S2 chặn gọi tên private xuyên gói,
        # và alias public này (QD-02/G4) chính là hợp đồng dựng sẵn cho việc đó.
        soat_nguphap.keu_neu_dao(grammar.doc_cache(), "sau khi cao")


def _chay():
    # Lấp bộ đệm RAM từ thẻ Anki NGAY ĐẦU — mọi nhánh dưới đây đều cần biết
    # "đã có sẵn từ nào" trước khi quyết định cào thêm. Anki đóng thì KÊU TO rồi
    # dừng ở đây, không âm thầm cào cả buổi rồi mất trắng cuối lệnh (QD-11).
    grammar.lap_dem_tu_the()
    if "--nangcap" in sys.argv:
        # Cào lại bản ghi CŨ PHIÊN BẢN. Dùng khi `normalize()` bắt đầu giữ thêm
        # khoá — không thể dò bằng "thiếu khoá X" vì khoá có thể vắng chính đáng
        # (`сожале́ние` không có `usage` thật), nên dò bằng số hiệu bản ghi.
        cache = grammar._cache()
        # Dùng CHUNG cửa `grammar.ban_ghi_cu()` — trước 30/07 chỗ này tự dò
        # `r.get("v",1) < BAN_GHI_V`, tức định nghĩa "cũ" nằm ở hai nơi.
        cu = [w for w, r in sorted(cache.items()) if grammar.ban_ghi_cu(r)]
        print(f"{len(cache)} ban ghi | can nang cap {len(cu)} "
              f"(len v{grammar.BAN_GHI_V})", flush=True)
        for i, w in enumerate(cu, 1):
            grammar.fetch_grammar(w, refresh=True)
            if i % 25 == 0 or i == len(cu):
                print(f"  {i}/{len(cu)}", flush=True)
        print("XONG")
        return
    if "--sotu" in sys.argv:
        va_so_tu()
        return
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
