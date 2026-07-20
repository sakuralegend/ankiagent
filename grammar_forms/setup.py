# ==============================================================================
# --- THIẾT LẬP MỘT LẦN CHO MẢNG THẺ BIẾN CÁCH ---
# Chạy:  python -m grammar_forms.setup
#
# Việc làm (đều IDEMPOTENT — chạy lại nhiều lần vô hại):
#   1. Đổi tên deck cũ "Irregular" -> "GRAMMAR::plural-irregular" (giữ lịch ôn)
#   2. Tạo/cập nhật model RU_Plural: thêm ô còn thiếu + ghi lại template & CSS
# ==============================================================================
from anki_tools.anki_client import check_anki_ready, trigger_sync

from . import cards
from .config import PLURAL_DECK, PLURAL_DECK_LEGACY


def main():
    if not check_anki_ready():
        print("❌ Không kết nối được AnkiConnect. Mở Anki trên máy rồi chạy lại.")
        return

    print("--- ⚙️  Thiết lập mảng thẻ biến cách ---")

    moved = cards.rename_legacy_deck(PLURAL_DECK_LEGACY, PLURAL_DECK)
    if moved:
        print(f"📦 Đã chuyển {moved} thẻ '{PLURAL_DECK_LEGACY}' -> '{PLURAL_DECK}' "
              "(lịch ôn giữ nguyên).")
    else:
        cards.anki("createDeck", deck=PLURAL_DECK)
        print(f"📦 Deck '{PLURAL_DECK}' đã sẵn sàng.")

    cards.setup_model()

    print("☁️  Sync AnkiWeb..." if trigger_sync() else "⚠️  Sync AnkiWeb thất bại.")
    print("--- Hoàn tất. ---")


if __name__ == "__main__":
    main()
