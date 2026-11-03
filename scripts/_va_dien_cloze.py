# -*- coding: utf-8 -*-
"""ĐIỀN Ô ClozeHTML CHO THẺ ĐANG CÓ — chạy MỘT LẦN (L2), xong chuyển `_daxong/`.

    python scripts/_va_dien_cloze.py            # CHẠY KHAN — đếm + in vài mẫu, không ghi
    python scripts/_va_dien_cloze.py --apply    # ghi thật (ô phải ĐÃ có trong model)

🔴 Đây là một bước trong chuỗi ĐỔI SCHEMA (QD-48) — chạy ĐÚNG THỨ TỰ ở VIECDANGLAM.md:
kéo sync → thêm ô trên laptop → script này → user Upload laptop → user Download VPS →
MỚI deploy. Script KHÔNG tự sync: kho vừa đổi schema thì sync thường bị AnkiWeb từ
chối, chiều đẩy phải do user bấm tay (AnkiConnect không chọn được chiều).
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from anki_tools import goi_anki
from anki_tools.anki_client import doc_notes_cua_model, sync_truoc_khi_ghi_lo
from anki_tools.config import MODEL_NAME
from anki_tools.html_builder import dung_cloze
from anki_tools.utils import log_fail

O = "ClozeHTML"


def chay(apply):
    if apply and O not in goi_anki("modelFieldNames", modelName=MODEL_NAME):
        log_fail(f"Model {MODEL_NAME} chưa có ô {O} — thêm ô trước (bước 4 VIECDANGLAM.md).")
        return
    if apply and not sync_truoc_khi_ghi_lo("điền ClozeHTML"):
        log_fail("Không kéo được AnkiWeb về — DỪNG, chưa ghi gì.")
        return
    viec, rong = [], []
    for n in doc_notes_cua_model(MODEL_NAME):
        f = {k: v["value"] for k, v in n["fields"].items()}
        try:
            rec = json.loads(f.get("GrammarJSON") or "{}")
        except ValueError:
            rec = {}
        h = dung_cloze(f.get("ExamplesHTML", ""), rec, f["WordClean"])
        if not h:
            rong.append(f["WordClean"])
        elif f.get(O, "") != h:
            viec.append((n["noteId"], h))
    print(f"Sẽ ghi {len(viec)} thẻ; {len(rong)} thẻ KHÔNG có câu hợp lệ (giữ mặt trước như cũ): {rong[:15]}")
    if not apply:
        print("Chạy KHAN — chưa ghi gì. Thêm --apply để ghi thật.")
        return
    for k, (nid, h) in enumerate(viec, 1):
        goi_anki("updateNoteFields", note={"id": nid, "fields": {O: h}})
        if k % 200 == 0:
            print(f"  {k}/{len(viec)}")
    print(f"Xong {len(viec)} thẻ. Tiếp theo: USER Tools → Sync → Upload trên laptop.")


if __name__ == "__main__":
    chay("--apply" in sys.argv)
