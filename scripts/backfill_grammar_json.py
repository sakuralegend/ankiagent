# -*- coding: utf-8 -*-
"""Đổ dữ liệu ngữ pháp đã cào vào field `GrammarJSON` của từng thẻ.

    python backfill_grammar_json.py            # CHẠY KHAN
    python backfill_grammar_json.py --apply    # ghi thật

## Vì sao để trong THẺ chứ không chỉ trong file cache

User chốt 29/07: *"những thứ cào được này nên đặt vào một field nào đó trong
thẻ, để sau này muốn lấy để xử lí cũng dễ"*. Trước đó dữ liệu chỉ nằm ở
`data/grammar_cache.json` **trên laptop**, nên:
  · bot Telegram chạy trên VPS không với tới được;
  · mất file cache là mất trắng, phải cào lại 950 lượt mạng;
  · thẻ không tự chứa — muốn xử lý gì cũng phải có đúng máy đó.
Để trong field thì nó tự sync đi mọi thiết bị và thẻ trở thành tự chứa.

Field ẨN, không template nào hiện — cùng khuôn với `RawExamples` vốn đã lưu JSON
câu gốc. Đo thật: **0,8 MB cho 950 thẻ** (trung bình 888 B, to nhất 6 KB).

🔴 Thêm field LÀ schema mod ⇒ Anki đòi FULL SYNC một lần nữa. Xem
[[vps-ket-sync-im-lang]]: sau khi Upload phải kiểm lại VPS.
"""
import json
import os
import sys
import urllib.request

# Chay duoc tu bat cu dau: file nay khong con nam o goc repo nen phai tu tro
# duong dan goc vao sys.path truoc khi import anki_tools (G3, 31/07/2026).
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from anki_tools import grammar
from anki_tools.anki_client import sync_truoc_khi_ghi_lo
from anki_tools.config import ANKI_CONNECT_URL, MODEL_NAME

FIELD = "GrammarJSON"


def ac(action, **params):
    req = urllib.request.Request(
        ANKI_CONNECT_URL,
        json.dumps({"action": action, "version": 6, "params": params}).encode())
    out = json.load(urllib.request.urlopen(req, timeout=180))
    if out.get("error"):
        raise RuntimeError(f"{action}: {out['error']}")
    return out["result"]


def main():
    apply = "--apply" in sys.argv

    if FIELD not in ac("modelFieldNames", modelName=MODEL_NAME):
        print(f"❌ Model {MODEL_NAME} chưa có field {FIELD}.")
        print("   Chạy setup_anki_environment() một lần để nó tự thêm, rồi chạy lại.")
        return

    notes = ac("notesInfo", notes=ac("findNotes", query=f'note:"{MODEL_NAME}"'))
    doi, giu, trong, goi_mang = [], 0, [], 0
    for n in notes:
        wc = (n["fields"].get("WordClean", {}).get("value") or "").strip()
        if not wc:
            continue
        rec = grammar.get_cached(wc)
        if not rec:
            rec = grammar.fetch_grammar(wc)
            goi_mang += 1
        if not rec:
            trong.append(wc)
        moi = json.dumps(rec, ensure_ascii=False, separators=(",", ":")) if rec else ""
        cu = n["fields"].get(FIELD, {}).get("value", "")
        if moi == cu:
            giu += 1
            continue
        doi.append((n["noteId"], wc, len(cu), len(moi)))

    tong = sum(m for _, _, _, m in doi)
    print(f"{len(notes)} thẻ | sẽ ghi {len(doi)} | giữ nguyên {giu}")
    print(f"  tổng dữ liệu ghi vào: {tong / 1024 / 1024:.2f} MB "
          f"(trung bình {tong // max(len(doi), 1)} B/thẻ)")
    if doi:
        to = sorted(doi, key=lambda x: -x[3])[:5]
        print("  to nhất: " + " · ".join(f"{w} {m}B" for _, w, _, m in to))
    if trong:
        print(f"\n⚠️ {len(trong)} thẻ KHÔNG có dữ liệu ngữ pháp -> field để trống:")
        print("   " + " · ".join(trong[:30]))
    if goi_mang:
        print(f"\n({goi_mang} từ chưa có trong cache, đã gọi mạng lấy về)")

    if not apply:
        print("\n(CHẠY KHAN — thêm --apply để ghi thật)")
        return
    if not sync_truoc_khi_ghi_lo("backfill GrammarJSON"):
        return
    for nid, wc, _, _ in doi:
        rec = grammar.get_cached(wc)
        ac("updateNoteFields", note={"id": nid, "fields": {
            FIELD: json.dumps(rec, ensure_ascii=False, separators=(",", ":")) if rec else ""}})
    print(f"\n✅ Đã ghi {len(doi)} thẻ.")


if __name__ == "__main__":
    main()
