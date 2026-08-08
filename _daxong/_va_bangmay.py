"""Dựng lại field `BangMay` cho MỌI thẻ (chạy 08/08/2026, một lần).

Vì sao phải chạy lại: `BangMay` được sinh **lúc tạo thẻ**, nên hai bản vá vừa
thêm vào `bang_chia.py` chỉ ăn vào thẻ tương lai. Hai bản vá đó:

  ① `_nhan_bien_the` nay dựng lại dạng đời nay cho ô chỉ có mỗi dạng thơ ca
     (`пе́рвою` -> `пе́рвой · пе́рвою (văn chương)`) — 13 ô, toàn số thứ tự.
  ② `tach_hai_trong_am` tách ô dính liền hai biến thể (`мо́дны́` -> `мо́дны,
     модны́`) — 3 ô, đều là dạng ngắn số nhiều.

KHÔNG bịa dữ liệu: cả hai chỉ sắp xếp lại chữ vốn đã có trong ô. Nguồn thật
vẫn là `GrammarJSON` trên chính thẻ (QD-11), không đụng tới.

Ghi `BangMay` KHÔNG phải schema mod (field có sẵn) ⇒ không kích full sync.

Chạy khan (mặc định) in ra thẻ nào đổi, `--apply` mới ghi thật.
"""
import json
import sys

sys.path.insert(0, ".")

from anki_tools import grammar                                    # noqa: E402
from anki_tools.anki_client import _ac, sync_truoc_khi_ghi_lo     # noqa: E402

APPLY = "--apply" in sys.argv


def main():
    ids = _ac("findNotes", query='note:"RU_Word"')
    notes = _ac("notesInfo", notes=ids, timeout=300)
    print(f"doc {len(notes)} the")

    doi = []
    for n in notes:
        f = n["fields"]
        word = f.get("Word", {}).get("value", "")
        cu = f.get("BangMay", {}).get("value", "")
        raw = f.get("GrammarJSON", {}).get("value", "")
        if not raw:
            continue
        try:
            rec = json.loads(raw)
        except ValueError:
            print(f"  ⚠️ {word}: GrammarJSON hong, bo qua")
            continue
        moi = grammar.khoi_may(rec)
        if moi != cu:
            doi.append((n["noteId"], word, cu, moi))

    print(f"\nSO THE DOI: {len(doi)} / {len(notes)}")
    for _, w, cu, moi in doi[:25]:
        print(f"\n  === {w}")
        for dong_cu, dong_moi in zip(cu.split("</tr>"), moi.split("</tr>")):
            if dong_cu != dong_moi:
                print(f"      CU : {dong_cu[-110:]}")
                print(f"      MOI: {dong_moi[-110:]}")

    if not APPLY:
        print("\n(chua ghi gi — them --apply de ghi that)")
        return

    if not sync_truoc_khi_ghi_lo("dung lai BangMay"):
        print("SYNC HONG — dung, khong ghi gi.")
        return
    for note_id, w, _, moi in doi:
        _ac("updateNoteFields", note={"id": note_id, "fields": {"BangMay": moi}})
    print(f"\nda ghi {len(doi)} note")


if __name__ == "__main__":
    main()
