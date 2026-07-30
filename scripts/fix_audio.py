# ==============================================================================
# --- VÁ ÂM THANH CHO THẺ ĐANG THIẾU MP3 ---
# Tìm mọi thẻ model RU_Word có ô Audio TRỐNG (thường do OpenRussian trả 500 lúc
# tạo thẻ) rồi tải lại: OpenRussian trước, hụt thì Google Cloud TTS (cần
# GOOGLE_TTS_API_KEY trong .env — xem README). KHÔNG đụng gì tới thẻ đã có tiếng.
#
# Chạy trên máy có Anki + AnkiConnect đang mở:
#   python fix_audio.py            -> DRY-RUN: chỉ liệt kê thẻ thiếu tiếng
#   python fix_audio.py --apply    -> tải + lưu audio, sync AnkiWeb
# ==============================================================================
import argparse
import re
import sys
import time

import requests

# Chay duoc tu bat cu dau: file nay khong con nam o goc repo nen phai tu tro
# duong dan goc vao sys.path truoc khi import anki_tools (G3, 31/07/2026).
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from anki_tools.config import ANKI_CONNECT_URL, GOOGLE_TTS_API_KEY, MODEL_NAME
from anki_tools.anki_client import store_word_audio, update_note_fields, trigger_sync
from anki_tools.utils import strip_accents_perfectly

DELAY_SECONDS = 1  # nghỉ nhẹ giữa 2 từ khi phải gọi Google TTS (tránh dồn dập)


def call(action, **params):
    r = requests.post(ANKI_CONNECT_URL, json={"action": action, "version": 6, "params": params}, timeout=60)
    j = r.json()
    if j.get("error"):
        raise SystemExit(f"AnkiConnect lỗi ({action}): {j['error']}")
    return j["result"]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Vá audio cho thẻ thiếu mp3")
    ap.add_argument("--apply", action="store_true", help="làm thật (mặc định: dry-run)")
    args = ap.parse_args()

    note_ids = call("findNotes", query=f'note:"{MODEL_NAME}"')
    notes = call("notesInfo", notes=note_ids)

    # "Thiếu tiếng" = ô Audio KHÔNG có tag [sound:...] hợp lệ. Gồm cả thẻ trống
    # LẪN thẻ mà AnkiConnect ghi câu lỗi "...download failed with return code 500"
    # vào ô Audio (bug cũ: tải hụt nhưng vẫn tạo thẻ với ô Audio = text lỗi).
    missing = []  # (note_id, clean_word)
    for n in notes:
        fields = n.get("fields", {})
        audio = fields.get("Audio", {}).get("value") or ""
        if re.search(r"\[sound:[^\]]+\]", audio):
            continue
        clean = (fields.get("WordClean", {}).get("value") or "").strip()
        if not clean:
            clean = strip_accents_perfectly(fields.get("Word", {}).get("value", ""))
        if clean:
            missing.append((n["noteId"], clean))

    print(f"Tổng thẻ {MODEL_NAME}: {len(notes)} | thẻ THIẾU audio: {len(missing)}")
    if missing:
        print("  " + ", ".join(w for _, w in missing[:40]) + (" ..." if len(missing) > 40 else ""))
    if not GOOGLE_TTS_API_KEY:
        print("⚠️ Chưa có GOOGLE_TTS_API_KEY: chỉ vá được từ nào OpenRussian tải LẠI được, "
              "từ lỗi 500 vẫn trống. Điền key vào .env để vá triệt để.")

    if not args.apply:
        print("\n(DRY-RUN — chưa tải gì. Chạy lại với --apply để vá thật.)")
        return

    fixed, still_missing = [], []
    for i, (note_id, clean) in enumerate(missing, 1):
        audio_field, source = store_word_audio(clean)
        # Luôn ghi đè ô Audio: có tiếng -> tag [sound:]; hụt -> "" để XÓA câu lỗi rác.
        update_note_fields(note_id, {"Audio": audio_field})
        if audio_field:
            fixed.append((clean, source))
            print(f"  [{i}/{len(missing)}] ✅ {clean} ({source})")
        else:
            still_missing.append(clean)
            print(f"  [{i}/{len(missing)}] ❌ {clean} (cả 2 nguồn hụt — đã xóa text lỗi)")
        if source == "google_tts" and i < len(missing):
            time.sleep(DELAY_SECONDS)

    print(f"\n✅ Vá được {len(fixed)} thẻ | ❌ còn thiếu {len(still_missing)}")
    if still_missing:
        print("   Còn thiếu: " + ", ".join(still_missing[:40]))
    if fixed:
        print("⏳ Sync AnkiWeb...")
        print("☁️ Xong." if trigger_sync() else "⚠️ Sync thất bại — thử /sync trong bot.")


if __name__ == "__main__":
    main()
