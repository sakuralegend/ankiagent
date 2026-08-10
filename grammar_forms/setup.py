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
from .config import CHIPHOI_DECK_GIOITU, PLURAL_DECK, PLURAL_DECK_LEGACY


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

    # --- Loại thẻ thứ hai của mảng: CHI PHỐI ---
    cards.anki("createDeck", deck=CHIPHOI_DECK_GIOITU)
    trang_thai = cards.setup_chiphoi_model()

    if trang_thai == "moi":
        # 🔴 Tạo model mới = schema mod ⇒ Anki đòi FULL SYNC. CỐ Ý không gọi
        # `trigger_sync()`: AnkiConnect không chọn được CHIỀU sync, mà chiều sai
        # là ghi đè sạch bản còn lại và không lùi được. Việc này phải có tay
        # người, và `KIENTRUC.md` ghi rõ triệu chứng khi lỡ: VPS kẹt
        # "Sync status 2" mà KHÔNG báo Telegram tiếng nào.
        print("\n" + "=" * 62)
        print("🔴 VỪA TẠO LOẠI THẺ MỚI ⇒ ANKI SẼ ĐÒI FULL SYNC.")
        print("   Đừng để máy tự sync. Làm tay đúng thứ tự này:")
        print("   1. Trên LAPTOP:  Tools → Sync  →  chọn UPLOAD (đẩy lên)")
        print("   2. Trên VPS:     vnc.bat → Sync  →  chọn DOWNLOAD (kéo về)")
        print("   Chọn sai chiều là mất dữ liệu và KHÔNG có gì kêu.")
        print("   Xong bước 2 thì kiểm:  journalctl -u anki-bot -n 50")
        print("=" * 62)
    else:
        print("☁️  Sync AnkiWeb..." if trigger_sync() else "⚠️  Sync AnkiWeb thất bại.")
    print("--- Hoàn tất. ---")


if __name__ == "__main__":
    main()
