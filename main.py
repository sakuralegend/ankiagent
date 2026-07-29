# ==============================================================================
# --- MAIN LOOP: nhập từ, cào dữ liệu, đẩy lên Anki ---
# Đây là file thay thế cho nw.py gốc (952 dòng), giờ chỉ còn vòng lặp chính.
# Toàn bộ logic được chia vào package anki_tools/ theo từng cụm chức năng:
#   config.py        - hằng số cấu hình
#   utils.py         - hàm tiện ích nhỏ (log, xử lý chữ)
#   ai_client.py     - giao tiếp Claude AI qua proxy (nguồn chân lý của system prompt)
#   scraper.py       - cào dữ liệu OpenRussian
#   html_builder.py  - dựng HTML ví dụ (nhánh AI + fallback)
#   anki_client.py   - giao tiếp AnkiConnect (deck, model, note, in tóm tắt)
#   templates/       - CSS + Front/Back HTML template (back_template.html có
#                      JS được tiêm placeholder từ config.py/ai_client.py)
# ==============================================================================
import time

from anki_tools.utils import strip_accents_perfectly
from anki_tools.ai_client import check_claude_ready
from anki_tools.pipeline import process_word
from anki_tools.anki_client import (
    check_anki_ready,
    find_duplicate_notes,
    change_note_deck,
    delete_notes,
    ensure_deck_exists,
    setup_anki_environment,
    print_card_summary,
)



def log_fail(msg):
    print(f"❌ {msg}")


def main():
    print("=" * 50)
    print("🇷🇺 OpenRussian -> Anki Flashcard Builder")
    print("=" * 50)

    print("🔍 Đang kiểm tra Anki...", end=" ", flush=True)
    if check_anki_ready():
        print("✅ Sẵn sàng.")
    else:
        log_fail("AnkiConnect chưa chạy. Hãy mở Anki thủ công trước.")
        return

    print("🔍 Đang kiểm tra Claude API...", end=" ", flush=True)
    if check_claude_ready():
        from anki_tools.config import CLAUDE_MODEL
        print(f"✅ Model '{CLAUDE_MODEL}' đã sẵn sàng.")
    else:
        from anki_tools.config import CLAUDE_MODEL
        log_fail(f"Không thể kết nối Claude API hoặc model '{CLAUDE_MODEL}' không khả dụng.")
        log_fail("Hãy kiểm tra lại CLAUDE_API_URL / CLAUDE_API_KEY / CLAUDE_MODEL trong config.py.")
        return

    setup_anki_environment()
    deck_name = input("\nNhập tên bộ bài (Enter = 🤖 tự động theo chủ đề): ").strip() or None
    if deck_name:
        ensure_deck_exists(deck_name)

    while True:
        try:
            user_input = input(f"\n[{deck_name or '🤖 tự động'}] Nhập từ: ").strip()
            if user_input.lower() in ["exit", "quit", "thoát"]:
                print("👋 Tạm biệt!")
                break
            if user_input == "":
                continue
            if user_input.lower() == "c":
                deck_name = input("Nhập tên bộ bài mới (Enter = 🤖 tự động): ").strip() or None
                if deck_name:
                    ensure_deck_exists(deck_name)
                continue

            t_start = time.time()

            clean_word_check = strip_accents_perfectly(user_input)
            is_forced = False
            duplicates = find_duplicate_notes(clean_word_check)

            if duplicates:
                print(f"\n   ⚠️ Từ '{user_input}' đã tồn tại ({len(duplicates)} note):")
                for i, dup in enumerate(duplicates):
                    print(f"     [{i + 1}] Từ: {dup['word']} │ Deck: {dup['deck']} │ {dup['status_text']}")

                selected = duplicates[0]
                if len(duplicates) > 1:
                    idx_raw = input(f"   Chọn note cần xử lý (1-{len(duplicates)}): ").strip()
                    if not idx_raw.isdigit() or not (1 <= int(idx_raw) <= len(duplicates)):
                        print(f"   ⏭️ Lựa chọn không hợp lệ. Đã hủy.")
                        continue
                    selected = duplicates[int(idx_raw) - 1]

                action = input(
                    "   1 = Hủy thêm │ 2 = Chuyển note cũ sang deck hiện tại │ 3 = Xóa note cũ đi │ 4 = Vẫn thêm trùng: "
                ).strip()

                if action == "2":
                    if not deck_name:
                        print("   🤖 Đang ở chế độ tự động (không có deck hiện tại) — chọn deck bằng lệnh 'c' trước.")
                        continue
                    if change_note_deck(selected["card_ids"], deck_name):
                        print(f"   ✅ Đã chuyển note '{selected['word']}' sang deck '{deck_name}'.")
                    else:
                        print(f"   ❌ Chuyển deck thất bại.")
                    continue
                elif action == "3":
                    if delete_notes([selected["note_id"]]):
                        print(f"   🗑️ Đã xóa note cũ '{selected['word']}'. Tiếp tục thêm note mới...")
                    else:
                        print(f"   ❌ Xóa note thất bại. Đã hủy.")
                        continue
                elif action == "4":
                    is_forced = True
                    print(f"   ⚠️ Chế độ thêm trùng (FORCE).")
                else:
                    print(f"   ⏭️ Đã hủy.")
                    continue

            # --- Cào dữ liệu -> AI -> đẩy lên Anki (pipeline dùng chung với bot) ---
            print(f"\n  --- 🔍 Đang xử lý (cào OpenRussian -> AI -> Anki)...", end=" ", flush=True)
            success, card_info, error_msg = process_word(user_input, deck_name, is_forced=is_forced)

            # TỪ ĐỒNG TỰ: pipeline dừng lại và trả danh sách mục để hỏi.
            # `мочь` là động từ "có thể" hay danh từ "sức lực"? Máy không đoán
            # được, và đoán sai thì cả thẻ (nghĩa + bảng chia + badge) sai theo.
            if not success and (card_info or {}).get("nhieu_muc"):
                muc = card_info["nhieu_muc"]
                print(f"\n  ⚠️ '{user_input}' có {len(muc)} mục ĐỒNG CHÍNH TẢ:")
                for i, m in enumerate(muc, 1):
                    print(f"     {i}. [{m['pos']}] {m['acc']} — {m['en']}")
                tra_loi = input("  Chọn số (Enter = bỏ qua): ").strip()
                if not tra_loi.isdigit() or not 1 <= int(tra_loi) <= len(muc):
                    print("   ⏭️ Đã hủy.")
                    continue
                success, card_info, error_msg = process_word(
                    user_input, deck_name, is_forced=is_forced,
                    chon_id=muc[int(tra_loi) - 1]["id"])

            t_elapsed = time.time() - t_start

            if success:
                print(f"✅ Hoàn tất!")
                print_card_summary(card_info, t_elapsed)
            else:
                print(f"❌ {error_msg} ({t_elapsed:.1f}s)")

        except KeyboardInterrupt:
            print("\n👋 Đã nhận Ctrl+C. Thoát.")
            break


if __name__ == "__main__":
    main()
