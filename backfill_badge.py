# -*- coding: utf-8 -*-
"""Điền lại TOÀN BỘ badge ngữ pháp cho thẻ đã có trong Anki.

    python backfill_badge.py            # CHẠY KHAN — in ra, không ghi gì
    python backfill_badge.py --apply    # ghi thật

Ba field, ba chiều ngữ pháp, không chiều nào chồng chiều nào:

  GenderBadge     danh từ   MASC ♂ · FEM ♀ · NEUT ⚧ · PL 👥
  AspectBadge     động từ   PERF · IMPF · BI-ASP
  ReflexiveBadge  động từ   REFL -ся

Thẻ tạo từ 29/07/2026 trở đi tự có đủ ba (scraper lấy `verb.aspect` +
`verb.isReflexive` lúc cào). Script này lo phần quá khứ: 950 thẻ có sẵn.

Nguồn là `data/grammar_cache.json` (đã cào sẵn cả bộ sưu tập). Từ nào chưa có
trong cache thì gọi mạng lấy về, nên chạy được cả với thẻ mới thêm sau này.

🔴 TRƯỚC KHI CHẠY: hai field mới phải tồn tại. Chạy `setup_anki_environment()`
một lần (nó tự thêm qua `modelFieldAdd`). Thêm field LÀ schema mod ⇒ Anki đòi
FULL SYNC một lần ⇒ gom hết thay đổi schema rồi Upload MỘT lần, và sau đó kiểm
`journalctl` trên VPS: VPS kẹt sync IM LẶNG, không báo Telegram.
"""
import json
import re
import sys
import urllib.request

from anki_tools import grammar
from anki_tools.config import ANKI_CONNECT_URL, MODEL_NAME

# Nhãn giống — giữ ĐỒNG BỘ với anki_client.build_card_fields(). Phải có ở hai
# nơi vì thẻ cũ chỉ còn chuỗi HTML đã dựng, không giữ lại mã giống gốc.
GIONG = {"masculine": "MASC ♂", "feminine": "FEM ♀",
         "neuter": "NEUT ⚧", "plural": "PL 👥"}
MA_GIONG = {"m": "masculine", "f": "feminine", "n": "neuter", "pl": "plural"}


def ac(action, **params):
    req = urllib.request.Request(
        ANKI_CONNECT_URL,
        json.dumps({"action": action, "version": 6, "params": params}).encode())
    out = json.load(urllib.request.urlopen(req, timeout=120))
    if out.get("error"):
        raise RuntimeError(f"{action}: {out['error']}")
    return out["result"]


def chu(html):
    return re.sub(r"<[^>]+>", "", html or "").strip()


def gender_badge(rec, badge_cu):
    """Badge giống. Ưu tiên từ điển; từ điển thiếu thì đọc lại NHÃN CŨ trên thẻ.

    Vì sao cần nhánh thứ hai: có danh từ OpenRussian không ghi `noun.gender`
    nhưng thẻ đang hiện giống đúng (lúc tạo thẻ lấy được, hoặc sửa tay). Dựng
    lại một cách máy móc từ từ điển sẽ XOÁ MẤT badge đang đúng — đổi nhãn cho
    đẹp mà làm mất thông tin thì là lỗ, không phải lãi.
    """
    ma = MA_GIONG.get((rec.get("gender") or "").strip().lower())
    if not ma:
        cu = chu(badge_cu).lower()
        ma = next((k for k in GIONG if cu.startswith(k[:4])), None)
    return f'<div class="badge {ma}">{GIONG[ma]}</div>' if ma else ""


def gender_badge_wc(wc, rec, badge_cu):
    """Như trên, nhưng luật CHỈ DÙNG SỐ NHIỀU đè lên tất cả — xem
    grammar.chi_so_nhieu(): `де́ньги` không có số ít nên badge "FEM ♀" là dạy sai."""
    if grammar.chi_so_nhieu(wc):
        return f'<div class="badge plural">{GIONG["plural"]}</div>'
    return gender_badge(rec, badge_cu)


def main():
    apply = "--apply" in sys.argv

    co = ac("modelFieldNames", modelName=MODEL_NAME)
    thieu = [f for f in ("AspectBadge", "ReflexiveBadge") if f not in co]
    if thieu:
        print(f"❌ Model {MODEL_NAME} chưa có field: {', '.join(thieu)}")
        print("   Chạy setup_anki_environment() một lần để nó tự thêm, rồi chạy lại.")
        return

    notes = ac("notesInfo", notes=ac("findNotes", query=f'note:"{MODEL_NAME}"'))
    print(f"{len(notes)} thẻ {MODEL_NAME}")

    doi, giu, ngo, goi_mang = [], 0, [], 0
    for n in notes:
        f = n["fields"]
        wc = (f.get("WordClean", {}).get("value") or "").strip()
        if not wc:
            continue
        rec = grammar.get_cached(wc)
        if not rec:
            rec = grammar.fetch_grammar(wc)
            goi_mang += 1
        pos_the = (f.get("PoS", {}).get("value") or "").strip().lower()
        la_dong_tu = rec.get("pos") == "verb" or pos_the in ("v", "verb")
        la_danh_tu = rec.get("pos") == "noun" or pos_the in ("n", "noun")

        moi = {
            "GenderBadge": (gender_badge_wc(wc, rec, f.get("GenderBadge", {}).get("value", ""))
                            if la_danh_tu else ""),
            "AspectBadge": (grammar.aspect_badge_html(rec.get("aspect"))
                            if la_dong_tu else ""),
            "ReflexiveBadge": (grammar.reflexive_badge_html(grammar.is_reflexive(wc, rec))
                               if la_dong_tu else ""),
        }
        if la_dong_tu and not moi["AspectBadge"]:
            ngo.append(f"{wc}(thể)")
        if la_danh_tu and not moi["GenderBadge"]:
            ngo.append(f"{wc}(giống)")

        khac = {k: v for k, v in moi.items() if v != f.get(k, {}).get("value", "")}
        if not khac:
            giu += 1
            continue
        cu = {k: f.get(k, {}).get("value", "") for k in khac}
        doi.append((n["noteId"], wc, cu, khac))

    print(f"\n=== SẼ ĐỔI {len(doi)} thẻ (giữ nguyên {giu}) ===")
    dem = {}
    for _, _, cu, khac in doi:
        for k, v in khac.items():
            key = f"{k:15s} {chu(cu[k]) or '(trống)':16s} -> {chu(v) or '(xoá)'}"
            dem[key] = dem.get(key, 0) + 1
    for mo_ta, sl in sorted(dem.items(), key=lambda x: (-x[1], x[0])):
        print(f"  {sl:4d}×  {mo_ta}")

    if ngo:
        print(f"\n⚠️ {len(ngo)} thẻ từ điển KHÔNG cho biết -> badge để trống:")
        print("   " + " · ".join(ngo[:40]))
    if goi_mang:
        print(f"\n({goi_mang} từ chưa có trong cache, đã gọi mạng lấy về)")

    if not apply:
        print("\n(CHẠY KHAN — thêm --apply để ghi thật)")
        return
    for nid, _, _, khac in doi:
        ac("updateNoteFields", note={"id": nid, "fields": khac})
    print(f"\n✅ Đã ghi {len(doi)} thẻ.")


if __name__ == "__main__":
    main()
