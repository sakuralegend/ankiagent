# ==============================================================================
# --- BỘ CHIA TIN NHẮN: on_word (mọi text thường) + on_callback (mọi nút inline).
# Không chứa logic nghiệp vụ — chỉ đọc trạng thái phiên rồi gọi đúng flow_*.
# ==============================================================================
import asyncio
import re

from telegram import Update
from telegram.ext import ContextTypes

from anki_tools.config import TELEGRAM_USER_ID, TOPIC_DECK_PARENT
from anki_tools.anki_client import (
    change_note_deck,
    delete_notes,
    ensure_deck_exists,
    get_deck_names,
    get_deck_note_ids,
    trigger_sync,
)

from anki_tools.backup import human_size, list_backups, run_backup

from .commands import _don_report, run_don, thongke_report
from .core import (
    HELP_TEXT,
    TOOLS_TEXT,
    _current_deck,
    _deck_choose_keyboard,
    _load_last_deck,
    _menu_keyboard,
    _menu_text,
    _reset_idle_timer,
    _save_last_deck,
    _set_deck,
    _show_deck_list,
    _sync_report_line,
    _tools_keyboard,
)
from .flow_add import _add_with_dup_check, _do_add, _duplicate_text_and_keyboard
from .flow_edit import (
    _do_redo,
    _run_suadeck,
    _sd_clear,
    _sd_confirm_text_keyboard,
    _sd_deck_list_markup,
    _sd_delete_resume,
    _sd_load_resume,
)
from .flow_scan import _run_scan_add, _scan_clear, _scan_exclude
from .flow_special import do_add_plural, do_redo_plural, on_special_callback


async def on_word(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Tin nhắn text thường. Ưu tiên theo trạng thái đang chờ: tên deck mới /
    từ cần sửa / yêu cầu sửa tự viết; không chờ gì thì text = từ cần thêm thẻ."""
    text = update.message.text.strip()
    if not text:
        return
    _reset_idle_timer(context, update.effective_chat.id)

    # --- Đang chờ tên deck mới (sau khi bấm nút "Tạo deck mới") ---
    if context.bot_data.get("awaiting_deck"):
        deck_name = text
        ok = await asyncio.to_thread(ensure_deck_exists, deck_name)
        if ok:
            _set_deck(context, deck_name)
            sync_line = await _sync_report_line()  # deck mới tạo phải lên AnkiWeb ngay
            await update.message.reply_text(
                f"📦 Deck: {deck_name} — giờ gõ từ tiếng Nga để thêm thẻ.\n{sync_line}"
            )
        else:
            await update.message.reply_text("❌ Không tạo được deck. Nhập tên khác thử:")
        return

    # --- Đang chờ TỪ cần làm lại (sau khi bấm /sua hoặc nút ✏️ Làm lại thẻ) ---
    if context.user_data.get("awaiting") == "sua_word":
        context.user_data.pop("awaiting", None)
        msg = await update.message.reply_text("⏳ Chuẩn bị làm lại thẻ...")
        await _do_redo(msg, text)
        return

    # --- Đang chờ TỪ để tạo thẻ SỐ NHIỀU bất quy tắc (mục ⭐ đặc biệt) ---
    if context.user_data.get("awaiting") == "plural_word":
        context.user_data.pop("awaiting", None)
        msg = await update.message.reply_text("⏳ Chuẩn bị dựng thẻ số nhiều...")
        await do_add_plural(msg, text, context)
        return

    # --- Đang chờ TỪ để LÀM LẠI thẻ số nhiều (mục ⭐ đặc biệt) ---
    if context.user_data.get("awaiting") == "plural_sua_word":
        context.user_data.pop("awaiting", None)
        msg = await update.message.reply_text("⏳ Chuẩn bị làm lại thẻ số nhiều...")
        await do_redo_plural(msg, text, context)
        return

    # --- Đang có danh sách quét ảnh chờ duyệt: nhắn 'bỏ 3 7 12' để loại từ ---
    if context.user_data.get("scan_words") and re.fullmatch(r"(bỏ|bo)[\s,.\d]+", text.lower()):
        await _scan_exclude(update, context, text)
        return

    # --- Không chọn deck = chế độ TỰ ĐỘNG (AI bỏ thẻ vào deck con theo chủ đề),
    # nên KHÔNG chặn nữa; muốn deck cố định thì /deck hoặc nút 📚 trong menu ---

    # --- Còn lại: text là từ cần thêm ---
    word = text
    status = await update.message.reply_text(f"🔍 Đang kiểm tra '{word}'...")
    await _add_with_dup_check(status, word, context)


async def on_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Xử lý mọi nút bấm inline: menu:*, sua:*, và luồng từ trùng (sel:/act:)."""
    query = update.callback_query
    if query.from_user.id != TELEGRAM_USER_ID:
        await query.answer("Bạn không có quyền dùng bot này.")
        return
    await query.answer()
    _reset_idle_timer(context, query.message.chat_id)
    data = query.data

    # --- Chọn deck: tự động theo chủ đề / deck gần nhất / có sẵn / tạo mới ---
    if data == "deck:auto":
        _set_deck(context, None)
        await query.edit_message_text(
            f"🤖 Chế độ TỰ ĐỘNG: thẻ mới vào {TOPIC_DECK_PARENT}::<chủ đề> do AI chọn "
            "(vd ::food, ::animals).\nGõ từ tiếng Nga để thêm thẻ."
        )
        return
    if data == "deck:last":
        deck_name = _load_last_deck()
        if not deck_name:
            await query.edit_message_text(
                "⌛ Bot không còn nhớ deck gần nhất — chọn lại nhé:",
                reply_markup=_deck_choose_keyboard(),
            )
            return
        # Kiểm tra deck còn tồn tại (KHÔNG dùng ensure_deck_exists để khỏi
        # vô tình tạo lại deck user đã xóa/đổi tên trong Anki)
        names = await asyncio.to_thread(get_deck_names)
        if deck_name not in names:
            _save_last_deck(None)  # quên deck đã chết để nút không hiện nữa
            await query.edit_message_text(
                f"⚠️ Deck '{deck_name}' không còn trong Anki — chọn deck khác nhé:",
                reply_markup=_deck_choose_keyboard(),
            )
            return
        _set_deck(context, deck_name)
        await query.edit_message_text(f"📦 Deck: {deck_name} — gõ từ tiếng Nga để thêm thẻ.")
        return
    if data == "deck:list":
        await _show_deck_list(query, context)
        return
    if data == "deck:new":
        context.bot_data["awaiting_deck"] = True
        await query.edit_message_text("➕ Gõ tên deck mới:")
        return
    if data.startswith("deckpick:"):
        idx = int(data.split(":", 1)[1])
        choices = context.user_data.get("deck_choices") or []
        if idx >= len(choices):
            await query.edit_message_text("⌛ Danh sách đã cũ, bấm lại nút Chọn deck nhé.")
            return
        deck_name = choices[idx]
        _set_deck(context, deck_name)
        context.user_data.pop("deck_choices", None)
        # Chọn deck có sẵn không sửa đổi collection -> không cần sync
        await query.edit_message_text(f"📦 Deck: {deck_name} — gõ từ tiếng Nga để thêm thẻ.")
        return

    # --- Nút mục ⭐ đặc biệt (thẻ ngữ pháp) — toàn bộ logic ở flow_special.py ---
    if data.startswith("sp:"):
        await on_special_callback(query, context, data)
        return

    # --- Nút menu (tầng 1) + công cụ sửa chữa (tầng 2 sau nút 🛠) ---
    if data.startswith("menu:"):
        action = data.split(":", 1)[1]
        if action == "tools":
            await query.edit_message_text(TOOLS_TEXT, reply_markup=_tools_keyboard())
        elif action == "back":
            await query.edit_message_text(_menu_text(context), reply_markup=_menu_keyboard())
        elif action == "deck":
            await query.edit_message_text(
                "📚 Chọn deck:", reply_markup=_deck_choose_keyboard()
            )
        elif action == "sua":
            context.user_data["awaiting"] = "sua_word"
            await query.edit_message_text("🔄 Gõ từ cần làm lại thẻ (chỉ cần gõ từ):")
        elif action == "suadeck":
            if context.bot_data.get("sd_running"):
                await query.edit_message_text("⏳ Đang có một đợt làm lại deck chạy dở.")
                return
            text, kb = await _sd_deck_list_markup(context)
            if not text:
                await query.edit_message_text("📂 Chưa có deck nào trong Anki.")
                return
            await query.edit_message_text(text, reply_markup=kb)
        elif action == "thongke":
            await query.edit_message_text("⏳ Đang đếm thẻ theo chủ đề...")
            await query.edit_message_text(await thongke_report())
        elif action == "don":
            # Nút 🧹 phải làm ĐÚNG như lệnh /don — cùng gọi run_don(), đừng bao giờ
            # dựng lại logic dọn ở đây. Bản cũ gọi thẳng move_graduated_from_inbox()
            # nên vừa bỏ bước sync-kéo-về vừa bỏ bước GĐ1→GĐ2, rồi crash ở dòng
            # báo cáo (26/07/2026: TypeError, _don_report đã đổi sang nhận 1 dict).
            await query.edit_message_text("⏳ Đang sync về rồi dọn...")
            res = await asyncio.to_thread(run_don)
            await query.edit_message_text(_don_report(res))
        elif action == "sync":
            await query.edit_message_text("⏳ Đang sync AnkiWeb...")
            ok = await asyncio.to_thread(trigger_sync)
            await query.edit_message_text("☁️ Đã sync AnkiWeb." if ok else "❌ Sync thất bại.")
        elif action == "backup":
            await query.edit_message_text("⏳ Đang sao lưu (xuất từng deck, hơi lâu)...")
            result, removed = await asyncio.to_thread(run_backup)
            if not result.get("path"):
                await query.edit_message_text(
                    "❌ Backup thất bại:\n" + "; ".join(result.get("errors", []))[:300])
                return
            existing = await asyncio.to_thread(list_backups)
            await query.edit_message_text(
                f"💾 Đã sao lưu {len(result['decks'])} deck — {human_size(result['bytes'])}\n"
                f"🗂 Đang giữ {len(existing)} bản "
                f"(tổng {human_size(sum(s for _, s in existing))})."
                + (f"\n🧹 Đã xóa {removed} bản cũ nhất." if removed else "")
            )
        elif action == "help":
            await query.edit_message_text(HELP_TEXT)
        return

    # --- Luồng /suadeck: chọn deck -> xác nhận -> chạy/dừng ---
    if data == "sdcancel":
        _sd_clear(context.user_data)
        await query.edit_message_text("⏭️ Đã hủy làm lại deck.")
        return
    if data == "sdstop":
        if context.bot_data.get("sd_running"):
            context.bot_data["sd_stop"] = True
            # Tin tiến độ sẽ tự chuyển thành tổng kết ở vòng lặp kế tiếp
        return
    if data.startswith("sd:"):
        idx = int(data.split(":", 1)[1])
        choices = context.user_data.get("sd_deck_choices") or []
        if idx >= len(choices):
            await query.edit_message_text("⌛ Danh sách đã cũ, gọi lại /suadeck nhé.")
            return
        deck_name = choices[idx]
        note_ids = await asyncio.to_thread(get_deck_note_ids, deck_name)
        if not note_ids:
            _sd_clear(context.user_data)
            await query.edit_message_text(
                f"📂 Deck '{deck_name}' không có thẻ nào (của bot) để làm lại."
            )
            return
        context.user_data["sd_deck"] = deck_name
        context.user_data["sd_note_ids"] = note_ids
        confirm_text, kb = _sd_confirm_text_keyboard(context)
        await query.edit_message_text(confirm_text, reply_markup=kb)
        return
    if data == "sdresume":
        state = _sd_load_resume()
        if not state:
            await query.edit_message_text("⌛ Không còn đợt làm lại dở nào, gọi lại /suadeck nhé.")
            return
        context.user_data["sd_deck"] = state["deck"]
        context.user_data["sd_note_ids"] = state["note_ids"]
        confirm_text, kb = _sd_confirm_text_keyboard(context)
        await query.edit_message_text(confirm_text, reply_markup=kb)
        return
    if data == "sdfresh":
        _sd_delete_resume()
        text, kb = await _sd_deck_list_markup(context)
        if not text:
            await query.edit_message_text("📂 Chưa có deck nào trong Anki.")
            return
        await query.edit_message_text(text, reply_markup=kb)
        return
    if data == "sdgo":
        deck = context.user_data.get("sd_deck")
        note_ids = context.user_data.get("sd_note_ids")
        if not deck or not note_ids:
            await query.edit_message_text("⌛ Phiên làm lại deck đã hết hạn, gọi lại /suadeck nhé.")
            return
        if context.bot_data.get("sd_running"):
            await query.edit_message_text("⏳ Đang có một đợt làm lại deck khác chạy dở.")
            return
        _sd_clear(context.user_data)
        await query.edit_message_text(f"🔄 Bắt đầu làm lại deck '{deck}' ({len(note_ids)} thẻ)...")
        # Task riêng để bot vẫn nhận update (đặc biệt là nút ⏹ Dừng) trong lúc chạy
        asyncio.create_task(
            _run_suadeck(context, query.message.chat_id, query.message, deck, note_ids)
        )
        return

    # --- Luồng quét ảnh (scan*): hủy / dừng / xác nhận thêm loạt ---
    if data == "scancancel":
        _scan_clear(context.user_data)
        await query.edit_message_text("⏭️ Đã hủy — không thêm từ nào.")
        return
    if data == "scanstop":
        if context.bot_data.get("scan_running"):
            context.bot_data["scan_stop"] = True
            # Tin tiến độ sẽ tự chuyển thành tổng kết ở vòng lặp kế tiếp
        return
    if data == "scanadd":
        words = context.user_data.get("scan_words")
        if not words:
            await query.edit_message_text("⌛ Danh sách quét đã hết hạn, gửi lại ảnh nhé.")
            return
        if context.bot_data.get("scan_running") or context.bot_data.get("sd_running"):
            # Trả lời bằng tin mới để GIỮ danh sách + nút (bấm lại sau được)
            await query.message.reply_text("⏳ Đang có một đợt chạy hàng loạt khác — chờ xong rồi bấm lại nhé.")
            return
        _scan_clear(context.user_data)
        await query.edit_message_text(f"🔄 Bắt đầu thêm {len(words)} từ đã duyệt...")
        # Task riêng để bot vẫn nhận update (đặc biệt nút ⏹ Dừng) trong lúc chạy
        asyncio.create_task(_run_scan_add(context, query.message.chat_id, query.message, words))
        return

    # --- Nút xác nhận từ nguyên mẫu (từ gõ vào không có trên OpenRussian) ---
    if data.startswith("lemma:"):
        arg = data.split(":", 1)[1]
        if arg == "cancel":
            context.user_data.pop("lemma_choices", None)
            await query.edit_message_text("⏭️ Đã hủy.")
            return
        choices = context.user_data.get("lemma_choices") or []
        idx = int(arg)
        if idx >= len(choices):
            await query.edit_message_text("⌛ Phiên đã hết hạn, gõ lại từ nhé.")
            return
        word = choices[idx]
        context.user_data.pop("lemma_choices", None)
        # (deck None = chế độ tự động theo chủ đề -> không cần chặn chọn deck)
        await query.edit_message_text(f"🔍 Đang kiểm tra '{word}'...")
        await _add_with_dup_check(query.message, word, context)
        return

    # --- Nút chọn nghĩa khi từ ĐỒNG TỰ (`мочь` động từ / danh từ) ---
    if data.startswith("dongtu:"):
        arg = data.split(":", 1)[1]
        pend = context.user_data.pop("homonym", None)
        if arg == "cancel":
            await query.edit_message_text("⏭️ Đã hủy.")
            return
        if not pend or not arg.isdigit() or int(arg) >= len(pend["muc"]):
            await query.edit_message_text("⌛ Phiên đã hết hạn, gõ lại từ nhé.")
            return
        m = pend["muc"][int(arg)]
        await query.edit_message_text(f"🔍 Đang thêm '{pend['word']}' — nghĩa "
                                      f"[{m['pos']}] {m['en'][:50]}...")
        await _do_add(query.message, pend["word"], pend["deck"],
                      pend["forced"], context, chon_id=m["id"])
        return

    # --- Nút trên thẻ AI tạo thiếu nội dung: làm lại thẻ / bỏ qua ---
    if data.startswith("fix:"):
        word = data.split(":", 1)[1]
        if not word:  # "fix:" rỗng = Bỏ qua -> chỉ gỡ nút, giữ nguyên tin nhắn thẻ
            try:
                await query.edit_message_reply_markup(None)
            except Exception:
                pass
            return
        await _do_redo(query.message, word)
        return

    # --- Luồng từ trùng (sel:/act:) ---
    pending = context.user_data.get("pending")
    if not pending:
        await query.edit_message_text("⌛ Phiên xử lý đã hết hạn, gõ lại từ nhé.")
        return

    deck_name = _current_deck(context)

    if data.startswith("sel:"):
        pending["sel"] = int(data.split(":", 1)[1])
        dup_text, keyboard = _duplicate_text_and_keyboard(pending)
        await query.edit_message_text(dup_text, reply_markup=keyboard)
        return

    selected = pending["dups"][pending["sel"]]
    word = pending["word"]
    context.user_data.pop("pending", None)

    if data == "act:huy":
        await query.edit_message_text("⏭️ Đã hủy.")

    elif data == "act:chuyen":
        if not deck_name:
            # Chế độ tự động không có "deck hiện tại" để chuyển note cũ sang
            await query.edit_message_text(
                "🤖 Đang ở chế độ tự động (không có deck cố định). "
                "Dùng /deck chọn deck trước rồi gõ lại từ để chuyển."
            )
            return
        ok = await asyncio.to_thread(change_note_deck, selected["card_ids"], deck_name)
        if ok:
            sync_line = await _sync_report_line()
            await query.edit_message_text(
                f"✅ Đã chuyển note '{selected['word']}' sang deck '{deck_name}'.\n{sync_line}"
            )
        else:
            await query.edit_message_text("❌ Chuyển deck thất bại.")

    elif data == "act:xoa":
        ok = await asyncio.to_thread(delete_notes, [selected["note_id"]])
        if not ok:
            await query.edit_message_text("❌ Xóa note cũ thất bại. Đã hủy.")
            return
        # Sync ngay sau khi xóa (phòng trường hợp bước thêm mới bên dưới thất bại
        # thì việc xóa vẫn đã được đẩy lên AnkiWeb, không bị lệch 2 bên)
        await asyncio.to_thread(trigger_sync)
        await _do_add(query.message, word, deck_name, is_forced=False, context=context)

    elif data == "act:trung":
        await _do_add(query.message, word, deck_name, is_forced=True, context=context)
