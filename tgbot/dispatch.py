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

from .core import (
    HELP_TEXT,
    _current_deck,
    _deck_choose_keyboard,
    _load_last_deck,
    _reset_idle_timer,
    _save_last_deck,
    _set_deck,
    _show_deck_list,
    _sync_report_line,
)
from .flow_add import _add_with_dup_check, _do_add, _duplicate_text_and_keyboard
from .flow_edit import (
    _do_sua,
    _run_suadeck,
    _sd_clear,
    _sd_confirm_text_keyboard,
    _sd_deck_list_markup,
    _sd_delete_resume,
    _sd_kind_keyboard,
    _sd_load_resume,
    _sua_keyboard,
    _SD_LABELS,
)
from .flow_scan import _run_scan_add, _scan_clear, _scan_exclude


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

    # --- Đang chờ TỪ cần sửa (sau khi bấm /sua hoặc nút ✏️ Sửa thẻ) ---
    if context.user_data.get("awaiting") == "sua_word":
        context.user_data.pop("awaiting", None)
        context.user_data["sua_word"] = text
        await update.message.reply_text(
            f"✏️ Sửa thẻ '{text}' — chọn kiểu:", reply_markup=_sua_keyboard()
        )
        return

    # --- Đang chờ YÊU CẦU tự viết cho cả deck (/suadeck -> Tự viết) ---
    if context.user_data.get("awaiting") == "sdeck_custom":
        context.user_data.pop("awaiting", None)
        if not context.user_data.get("sd_deck"):
            await update.message.reply_text("⌛ Phiên sửa deck đã hết hạn, gọi lại /suadeck nhé.")
            return
        context.user_data["sd_instruction"] = text
        context.user_data["sd_label"] = f"✏️ {text[:80]}"
        confirm_text, kb = _sd_confirm_text_keyboard(context)
        await update.message.reply_text(confirm_text, reply_markup=kb)
        return

    # --- Đang chờ YÊU CẦU tự viết (sau khi bấm nút "Tự viết yêu cầu") ---
    if context.user_data.get("awaiting") == "sua_custom":
        context.user_data.pop("awaiting", None)
        word = context.user_data.pop("sua_word", None)
        if not word:
            await update.message.reply_text("⌛ Phiên sửa đã hết hạn, gọi lại /sua nhé.")
            return
        msg = await update.message.reply_text("⏳ Chuẩn bị sửa thẻ...")
        await _do_sua(msg, word, text)
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

    # --- Nút menu ---
    if data.startswith("menu:"):
        action = data.split(":", 1)[1]
        if action == "deck":
            await query.edit_message_text(
                "📚 Chọn deck:", reply_markup=_deck_choose_keyboard()
            )
        elif action == "sua":
            context.user_data["awaiting"] = "sua_word"
            await query.edit_message_text("✏️ Gõ từ cần sửa (chỉ cần gõ từ):")
        elif action == "sync":
            await query.edit_message_text("⏳ Đang sync AnkiWeb...")
            ok = await asyncio.to_thread(trigger_sync)
            await query.edit_message_text("☁️ Đã sync AnkiWeb." if ok else "❌ Sync thất bại.")
        elif action == "help":
            await query.edit_message_text(HELP_TEXT)
        return

    # --- Luồng /suadeck: chọn deck -> kiểu sửa -> xác nhận -> chạy/dừng ---
    if data == "sdcancel":
        _sd_clear(context.user_data)
        await query.edit_message_text("⏭️ Đã hủy sửa deck.")
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
                f"📂 Deck '{deck_name}' không có thẻ nào (của bot) để sửa."
            )
            return
        context.user_data["sd_deck"] = deck_name
        context.user_data["sd_note_ids"] = note_ids
        await query.edit_message_text(
            f"🛠 Deck '{deck_name}' có {len(note_ids)} thẻ.\n"
            "Chọn kiểu sửa áp dụng cho TẤT CẢ:",
            reply_markup=_sd_kind_keyboard(),
        )
        return
    if data == "sdresume":
        state = _sd_load_resume()
        if not state:
            await query.edit_message_text("⌛ Không còn đợt sửa dở nào, gọi lại /suadeck nhé.")
            return
        context.user_data["sd_deck"] = state["deck"]
        context.user_data["sd_note_ids"] = state["note_ids"]
        await query.edit_message_text(
            f"🔁 Sửa tiếp deck '{state['deck']}' — còn {len(state['note_ids'])} thẻ.\n"
            "Chọn kiểu sửa (nên chọn ĐÚNG kiểu đã dùng lần trước cho đồng bộ):",
            reply_markup=_sd_kind_keyboard(),
        )
        return
    if data == "sdfresh":
        _sd_delete_resume()
        text, kb = await _sd_deck_list_markup(context)
        if not text:
            await query.edit_message_text("📂 Chưa có deck nào trong Anki.")
            return
        await query.edit_message_text(text, reply_markup=kb)
        return
    if data.startswith("sdsua:"):
        choice = data.split(":", 1)[1]
        if not context.user_data.get("sd_deck"):
            await query.edit_message_text("⌛ Phiên sửa deck đã hết hạn, gọi lại /suadeck nhé.")
            return
        if choice == "custom":
            context.user_data["awaiting"] = "sdeck_custom"
            await query.edit_message_text(
                f"✏️ Gõ yêu cầu sửa áp dụng cho TẤT CẢ thẻ trong deck "
                f"'{context.user_data['sd_deck']}':"
            )
            return
        context.user_data["sd_instruction"] = choice
        context.user_data["sd_label"] = _SD_LABELS.get(choice, choice)
        confirm_text, kb = _sd_confirm_text_keyboard(context)
        await query.edit_message_text(confirm_text, reply_markup=kb)
        return
    if data == "sdgo":
        deck = context.user_data.get("sd_deck")
        note_ids = context.user_data.get("sd_note_ids")
        instruction = context.user_data.get("sd_instruction")
        if not deck or not note_ids or instruction is None:
            await query.edit_message_text("⌛ Phiên sửa deck đã hết hạn, gọi lại /suadeck nhé.")
            return
        if context.bot_data.get("sd_running"):
            await query.edit_message_text("⏳ Đang có một đợt sửa deck khác chạy dở.")
            return
        _sd_clear(context.user_data)
        await query.edit_message_text(f"🔄 Bắt đầu sửa deck '{deck}' ({len(note_ids)} thẻ)...")
        # Task riêng để bot vẫn nhận update (đặc biệt là nút ⏹ Dừng) trong lúc chạy
        asyncio.create_task(
            _run_suadeck(context, query.message.chat_id, query.message, deck, note_ids, instruction)
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

    # --- Nút trên thẻ AI tạo thiếu nội dung: tự sửa (preset 2) / bỏ qua ---
    if data.startswith("fix:"):
        word = data.split(":", 1)[1]
        if not word:  # "fix:" rỗng = Bỏ qua -> chỉ gỡ nút, giữ nguyên tin nhắn thẻ
            try:
                await query.edit_message_reply_markup(None)
            except Exception:
                pass
            return
        await _do_sua(query.message, word, "2")  # "2" = preset đổi ví dụ, như /sua
        return

    # --- Nút chọn kiểu sửa thẻ ---
    if data.startswith("sua:"):
        choice = data.split(":", 1)[1]
        word = context.user_data.get("sua_word")
        if not word:
            await query.edit_message_text("⌛ Phiên sửa đã hết hạn, gọi lại /sua <từ> nhé.")
            return
        if choice == "custom":
            # Giữ sua_word, chờ user gõ thẳng yêu cầu (không cần gõ lại lệnh/từ)
            context.user_data["awaiting"] = "sua_custom"
            await query.edit_message_text(
                f"✏️ Gõ yêu cầu sửa cho '{word}':\nvd: ví dụ về chủ đề công việc"
            )
            return
        context.user_data.pop("sua_word", None)
        await _do_sua(query.message, word, choice)  # choice = "1"/"2"/"3", pipeline tự resolve
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
