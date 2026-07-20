# ==============================================================================
# --- CHẠY LOẠT TRÊN MÁY (thay cho bấm nút trong bot) ---
# Cùng logic với mục ⭐ đặc biệt của bot, nhưng chạy thẳng trên PC nên nhanh hơn
# và xem được log chi tiết.
#
#   python -m grammar_forms.backfill fix         # vá thẻ cũ thiếu ví dụ/audio
#   python -m grammar_forms.backfill add         # thêm mọi từ trong danh sách
#   python -m grammar_forms.backfill add 10      # thêm 10 từ đầu (chạy thử)
# ==============================================================================
import sys
import time

from anki_tools.anki_client import check_anki_ready, trigger_sync
from anki_tools.utils import strip_accents_perfectly

from . import cards
from .config import PLURAL_DECK
from .pipeline import load_word_list, process_word, redo_note

DELAY_SECONDS = 3  # nghỉ giữa 2 thẻ, tránh chạm giới hạn request/phút của AI


def _needs_fix(fields):
    """Thẻ cần vá: thiếu ví dụ, thiếu audio số nhiều, hoặc nghĩa tiếng Anh bị
    "N/A" (dấu vết lỗi cào dùng nhầm khóa 'tl' thay vì 'tls', sửa 20/07/2026)."""
    return (not fields.get("ExamplesHTML")
            or "[sound:" not in (fields.get("PluralAudio") or "")
            or "N/A" in (fields.get("Meaning") or ""))


def run_fix(limit=None):
    note_ids = cards.deck_note_ids()
    todo = []
    for note_id in note_ids:
        note = cards.get_note(note_id)
        if note and _needs_fix(note["fields"]):
            todo.append((note_id, note["fields"].get("Word", "?")))
    if limit:
        todo = todo[:limit]
    if not todo:
        print("✅ Mọi thẻ đều đã đủ ví dụ và audio — không cần vá.")
        return

    print(f"🩹 Vá {len(todo)} thẻ thiếu ví dụ/audio...")
    word_list = load_word_list()
    ok, fail = 0, []
    for i, (note_id, word) in enumerate(todo, 1):
        success, result, error = redo_note(note_id, do_sync=False, word_list=word_list)
        if success:
            ok += 1
            print(f"  [{i}/{len(todo)}] ✅ {result['word']} → {result['plural']}")
        else:
            fail.append(word)
            print(f"  [{i}/{len(todo)}] ❌ {word}: {error}")
        if i < len(todo):
            time.sleep(DELAY_SECONDS)
    _report(ok, fail)


def run_add(limit=None):
    rows = load_word_list()
    if not rows:
        print("❌ Chưa có danh sách. Chạy: python -m grammar_forms.irregular_plurals")
        return
    known = cards.existing_words()
    if known is None:
        print("❌ Không đọc được thẻ đã có từ Anki.")
        return
    todo = [r for r in rows if strip_accents_perfectly(r["bare"]) not in known]
    if limit:
        todo = todo[:limit]
    if not todo:
        print("✅ Mọi từ trong danh sách đều đã có thẻ.")
        return

    print(f"➕ Thêm {len(todo)} thẻ số nhiều vào {PLURAL_DECK}...")
    ok, fail = 0, []
    for i, row in enumerate(todo, 1):
        success, info, error = process_word(row["bare"], PLURAL_DECK,
                                            do_sync=False, word_list=rows)
        if success:
            ok += 1
            print(f"  [{i}/{len(todo)}] ✅ {info['word']} → {info['plural']}  ({info['vi']})")
        else:
            fail.append(row["bare"])
            print(f"  [{i}/{len(todo)}] ❌ {row['bare']}: {error}")
        if i < len(todo):
            time.sleep(DELAY_SECONDS)
    _report(ok, fail)


def _report(ok, fail):
    print(f"\n🏁 Xong: ✅ {ok} │ ❌ {len(fail)}")
    if fail:
        print("   Chưa xong: " + ", ".join(fail))
    print("☁️ Đã sync AnkiWeb." if trigger_sync() else "⚠️ Sync AnkiWeb thất bại.")


def main():
    if not check_anki_ready():
        print("❌ Không kết nối được AnkiConnect. Mở Anki rồi chạy lại.")
        return
    mode = sys.argv[1] if len(sys.argv) > 1 else "fix"
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else None
    if mode == "fix":
        run_fix(limit)
    elif mode == "add":
        run_add(limit)
    else:
        print(__doc__ or "Dùng: python -m grammar_forms.backfill [fix|add] [số lượng]")


if __name__ == "__main__":
    main()
