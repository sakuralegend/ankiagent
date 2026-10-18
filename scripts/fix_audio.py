# ==============================================================================
# --- VÁ ÂM THANH: thẻ THIẾU tiếng + thẻ MÁY ĐỌC TỰ ĐOÁN trọng âm ---
# Soát 3 ô audio: RU_Word.Audio, RU_Plural.Audio, RU_Plural.PluralAudio.
#   • Ô trống / file mất / file KHÔNG phải bản thu người ⇒ tải lại KÈM DẤU NHẤN
#     (anki_tools/audio.py giải thích vì sao chữ trần làm máy đoán sai).
#   • PluralAudio soát CẢ bản thu người: chữ trần số nhiều hay trùng mặt từ khác
#     (дома́ ↔ до́ма) nên bản người có thể là người đọc nhầm từ.
# Bản mới GIỐNG HỆT bản đang có ⇒ bỏ qua. OpenRussian hụt ⇒ giữ nguyên bản cũ.
# Bản mới lưu dưới TÊN MỚI (ten_file_audio) ⇒ file cũ còn trong media, lùi được.
# Chỉ sửa ô Audio — không đụng model ⇒ KHÔNG kích full sync.
#
# Chạy trên máy có Anki + AnkiConnect đang mở:
#   python scripts/fix_audio.py            -> DRY-RUN: chỉ đếm, không ghi gì
#   python scripts/fix_audio.py --apply    -> backup, tải + ghi, sync AnkiWeb
# ==============================================================================
import argparse
import os
import re
import sys
import time

# Chay duoc tu bat cu dau: file nay khong con nam o goc repo nen phai tu tro
# duong dan goc vao sys.path truoc khi import anki_tools (G3, 31/07/2026).
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from anki_tools.anki_client import (doc_media_file, doc_notes_cua_model,
                                    store_media_file, trigger_sync, update_note_fields)
from anki_tools.audio import fetch_audio_bytes, la_ban_nguoi, ten_file_audio
from anki_tools.backup import run_backup
from anki_tools.config import MODEL_NAME
from grammar_forms.config import PLURAL_MODEL

# (model, ô audio, ô chứa chữ CÓ DẤU, prefix tên file, nhận bản thu người?)
O_AUDIO = [
    (MODEL_NAME, "Audio", "Word", "ru_audio", True),
    (PLURAL_MODEL, "Audio", "Word", "ru_audio", True),
    (PLURAL_MODEL, "PluralAudio", "Plural", "ru_plural", False),
]


def tim_ung_vien():
    """[(note_id, model, ô, chữ có dấu, prefix, nhận người, file cũ, bytes cũ)]."""
    out = []
    for model, o, o_chu, prefix, nguoi in O_AUDIO:
        for n in doc_notes_cua_model(model):
            f = n["fields"]
            chu = re.sub(r"<[^>]+>", "", f.get(o_chu, {}).get("value", "")).strip()
            m = re.search(r"\[sound:([^\]]+)\]", f.get(o, {}).get("value", ""))
            cu = doc_media_file(m.group(1)) if m else None
            if not chu or (nguoi and la_ban_nguoi(cu)):
                continue
            out.append((n["noteId"], model, o, chu, prefix, nguoi, m.group(1) if m else "", cu))
    return out


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Vá audio thiếu / sai trọng âm")
    ap.add_argument("--apply", action="store_true", help="làm thật (mặc định: dry-run)")
    args = ap.parse_args()

    ung_vien = tim_ung_vien()
    print(f"Cần soát {len(ung_vien)} ô audio (trống, máy đọc, hoặc số nhiều).")
    if not args.apply:
        print("(DRY-RUN — chưa tải gì. Chạy lại với --apply để vá thật.)")
        return

    res, _ = run_backup()
    if not res["path"]:
        raise SystemExit("❌ Backup thất bại — dừng, chưa ghi gì.")
    print(f"💾 Backup: {res['path']}")

    da_va, giong, hut = [], 0, []
    for k, (nid, model, o, chu, prefix, nguoi, ten_cu, cu) in enumerate(ung_vien, 1):
        moi, _ = fetch_audio_bytes(chu, nguoi)
        if not moi:
            hut.append(chu)
        elif moi == cu:
            giong += 1
        else:
            ten = ten_file_audio(prefix, chu)
            if store_media_file(ten, moi) and update_note_fields(nid, {o: f"[sound:{ten}]"}):
                da_va.append(f"{chu}({o})")
            else:
                hut.append(chu)
        if k % 25 == 0:
            print(f"  … {k}/{len(ung_vien)}")
        time.sleep(0.15)   # đừng dồn dập máy chủ OpenRussian

    print(f"\n✅ Đã thay {len(da_va)} | = giữ nguyên {giong} (đã đúng) | ❌ hụt {len(hut)}")
    if da_va:
        print("   Đã thay: " + ", ".join(da_va))
    if hut:
        print("   Hụt (giữ bản cũ / để trống): " + ", ".join(hut))
    if da_va:
        print("⏳ Sync AnkiWeb...")
        print("☁️ Xong." if trigger_sync() else "⚠️ Sync thất bại — thử /sync trong bot.")


if __name__ == "__main__":
    main()
