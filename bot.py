# ==============================================================================
# --- BOT TELEGRAM: thêm từ + sửa thẻ Anki từ xa (chạy 24/7 trên VPS) ---
# Cách dùng trong Telegram (chỉ user có TELEGRAM_USER_ID mới được dùng):
#   <gõ 1 từ tiếng Nga>       -> thêm thẻ mới vào deck hiện tại
#   /deck <tên deck>          -> đổi deck hiện tại
#   /sua <từ> <yêu cầu>       -> sửa lại thẻ đã có theo yêu cầu (AI refine)
#   /sync                     -> ép đồng bộ AnkiWeb ngay
#   /start hoặc /help         -> hướng dẫn
#
# Kiến trúc: bot dùng long-polling (không cần mở port/domain/SSL).
# Mọi thao tác nặng (cào web, gọi AI, gọi AnkiConnect) là blocking-requests
# nên được đẩy vào thread qua asyncio.to_thread để không nghẽn bot.
# Logic thêm/sửa từ nằm ở anki_tools/pipeline.py - DÙNG CHUNG với main.py (CLI).
# ==============================================================================
import asyncio
import time

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

from anki_tools.config import TELEGRAM_BOT_TOKEN, TELEGRAM_USER_ID, DEFAULT_DECK
from anki_tools.utils import strip_accents_perfectly, hl_to_bracket
from anki_tools.ai_client import check_claude_ready
from anki_tools.pipeline import process_word, refine_note
from anki_tools.anki_client import (
    check_anki_ready,
    find_duplicate_notes,
    change_note_deck,
    delete_notes,
    ensure_deck_exists,
    setup_anki_environment,
    trigger_sync,
)

HELP_TEXT = (
    "🇷🇺 Bot Anki tiếng Nga\n"
    "───────────────────\n"
    "• Gõ 1 từ tiếng Nga → thêm thẻ mới\n"
    "• /deck <tên> → đổi bộ bài hiện tại\n"
    "• /sua <từ> <yêu cầu> → sửa thẻ đã có\n"
    "   vd: /sua хороший ví dụ ngắn hơn, đời thường hơn\n"
    "• /sync → đồng bộ AnkiWeb ngay\n"
    "• /help → xem lại hướng dẫn này"
)


# ---------------------------------------------------------------------------
# Tiện ích
# ---------------------------------------------------------------------------

def _current_deck(context):
    return context.bot_data.get("deck", DEFAULT_DECK)


def format_card_summary(card_info, elapsed):
    """Bản Telegram của print_card_summary() - text thuần, không markdown."""
    w = hl_to_bracket(card_info["word"])
    forced = " ⚠️ FORCE" if card_info.get("is_forced") else ""
    lines = [
        f"✅ THẺ MỚI{forced}: {w}",
        f"🇬🇧 {', '.join(card_info['en_meanings'])}",
        f"🇻🇳 {card_info['vi_meaning']}",
    ]
    if card_info.get("gender"):
        lines.append(f"🏷️ {card_info['pos']} ({card_info['gender']})")
    else:
        lines.append(f"🏷️ {card_info['pos']}")

    for i, ex in enumerate(card_info.get("simplified_examples", [])[:3]):
        ru = hl_to_bracket(ex.get("ru", ""))
        vi = hl_to_bracket(ex.get("vi") or ex.get("vietnamese") or "")
        lines.append(f"💡 {i + 1}. {ru}")
        if vi:
            lines.append(f"     ➔ {vi}")

    lines.append(f"📦 {card_info['deck']} | ⏱ {elapsed:.1f}s")
    lines.append("☁️ Đã sync AnkiWeb — mở app Anki bấm sync để thấy thẻ.")
    return "\n".join(lines)


async def _do_add(status_msg, word, deck_name, is_forced):
    """Chạy pipeline thêm từ (trong thread) rồi cập nhật tin nhắn trạng thái."""
    t0 = time.time()
    await status_msg.edit_text(f"⏳ Đang xử lý '{word}' (cào OpenRussian → AI → Anki)...")
    success, card_info, error_msg = await asyncio.to_thread(
        process_word, word, deck_name, is_forced, True  # do_sync=True trên VPS
    )
    if success:
        await status_msg.edit_text(format_card_summary(card_info, time.time() - t0))
    else:
        await status_msg.edit_text(f"❌ {error_msg}")


def _duplicate_text_and_keyboard(pending):
    """Dựng nội dung tin nhắn + bàn phím nút bấm cho tình huống từ bị trùng."""
    dups = pending["dups"]
    word = pending["word"]
    lines = [f"⚠️ Từ '{word}' đã tồn tại ({len(dups)} note):"]
    for i, d in enumerate(dups):
        marker = "👉 " if i == pending["sel"] else ""
        lines.append(f"{marker}[{i + 1}] {d['word']} │ {d['deck']} │ {d['status_text']}")

    rows = []
    if len(dups) > 1:
        rows.append([
            InlineKeyboardButton(f"Chọn [{i + 1}]", callback_data=f"sel:{i}")
            for i in range(min(len(dups), 4))
        ])
    rows.append([
        InlineKeyboardButton("🚫 Hủy", callback_data="act:huy"),
        InlineKeyboardButton("📦 Chuyển deck", callback_data="act:chuyen"),
    ])
    rows.append([
        InlineKeyboardButton("🗑 Xóa cũ + thêm mới", callback_data="act:xoa"),
        InlineKeyboardButton("➕ Vẫn thêm trùng", callback_data="act:trung"),
    ])
    return "\n".join(lines), InlineKeyboardMarkup(rows)


# ---------------------------------------------------------------------------
# Handlers
# ---------------------------------------------------------------------------

async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"{HELP_TEXT}\n\n📦 Deck hiện tại: {_current_deck(context)}")


async def cmd_deck(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            f"📦 Deck hiện tại: {_current_deck(context)}\nĐổi deck: /deck <tên deck>"
        )
        return
    deck_name = " ".join(context.args).strip()
    ok = await asyncio.to_thread(ensure_deck_exists, deck_name)
    if ok:
        context.bot_data["deck"] = deck_name
        await update.message.reply_text(f"📦 Đã chuyển sang deck: {deck_name}")
    else:
        await update.message.reply_text("❌ Không tạo/kiểm tra được deck (AnkiConnect lỗi?).")


async def cmd_sync(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = await update.message.reply_text("⏳ Đang sync AnkiWeb...")
    ok = await asyncio.to_thread(trigger_sync)
    await msg.edit_text("☁️ Đã sync AnkiWeb." if ok else "❌ Sync thất bại (xem log trên VPS).")


async def cmd_sua(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "Cách dùng: /sua <từ> <yêu cầu>\nvd: /sua хороший ví dụ ngắn hơn, đời thường hơn"
        )
        return
    word = context.args[0]
    instruction = " ".join(context.args[1:]).strip() or "Viết lại 3 ví dụ mới tự nhiên, đời thường hơn."

    msg = await update.message.reply_text(f"⏳ Đang sửa thẻ '{word}' theo yêu cầu...")
    t0 = time.time()
    success, result, error_msg = await asyncio.to_thread(refine_note, word, instruction, True)
    if not success:
        await msg.edit_text(f"❌ {error_msg}")
        return

    lines = [f"✏️ ĐÃ SỬA THẺ: {hl_to_bracket(result['word'])}", f"🇻🇳 {result['vi']}"]
    for i, ex in enumerate(result["examples"][:3]):
        lines.append(f"💡 {i + 1}. {hl_to_bracket(ex.get('ru', ''))}")
        vi = hl_to_bracket(ex.get("vi") or ex.get("vietnamese") or "")
        if vi:
            lines.append(f"     ➔ {vi}")
    lines.append(f"⏱ {time.time() - t0:.1f}s")
    lines.append("☁️ Đã sync AnkiWeb — mở app Anki bấm sync để thấy thẻ mới.")
    await msg.edit_text("\n".join(lines))


async def on_word(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Tin nhắn text thường = 1 từ cần thêm thẻ."""
    word = update.message.text.strip()
    if not word:
        return

    deck_name = _current_deck(context)
    status = await update.message.reply_text(f"🔍 Đang kiểm tra '{word}'...")

    clean_word = strip_accents_perfectly(word)
    duplicates = await asyncio.to_thread(find_duplicate_notes, clean_word)

    if duplicates:
        context.user_data["pending"] = {"word": word, "dups": duplicates, "sel": 0}
        text, keyboard = _duplicate_text_and_keyboard(context.user_data["pending"])
        await status.edit_text(text, reply_markup=keyboard)
        return

    await _do_add(status, word, deck_name, is_forced=False)


async def on_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Xử lý nút bấm inline (luồng từ bị trùng)."""
    query = update.callback_query
    if query.from_user.id != TELEGRAM_USER_ID:
        await query.answer("Bạn không có quyền dùng bot này.")
        return
    await query.answer()

    pending = context.user_data.get("pending")
    if not pending:
        await query.edit_message_text("⌛ Phiên xử lý đã hết hạn, gõ lại từ nhé.")
        return

    data = query.data
    deck_name = _current_deck(context)

    if data.startswith("sel:"):
        pending["sel"] = int(data.split(":", 1)[1])
        text, keyboard = _duplicate_text_and_keyboard(pending)
        await query.edit_message_text(text, reply_markup=keyboard)
        return

    selected = pending["dups"][pending["sel"]]
    word = pending["word"]
    context.user_data.pop("pending", None)

    if data == "act:huy":
        await query.edit_message_text("⏭️ Đã hủy.")

    elif data == "act:chuyen":
        ok = await asyncio.to_thread(change_note_deck, selected["card_ids"], deck_name)
        if ok:
            await asyncio.to_thread(trigger_sync)
            await query.edit_message_text(
                f"✅ Đã chuyển note '{selected['word']}' sang deck '{deck_name}'.\n☁️ Đã sync AnkiWeb."
            )
        else:
            await query.edit_message_text("❌ Chuyển deck thất bại.")

    elif data == "act:xoa":
        ok = await asyncio.to_thread(delete_notes, [selected["note_id"]])
        if not ok:
            await query.edit_message_text("❌ Xóa note cũ thất bại. Đã hủy.")
            return
        await _do_add(query.message, word, deck_name, is_forced=False)

    elif data == "act:trung":
        await _do_add(query.message, word, deck_name, is_forced=True)


# ---------------------------------------------------------------------------
# Khởi động
# ---------------------------------------------------------------------------

def wait_for_anki(max_wait_seconds=180):
    """Chờ AnkiConnect sẵn sàng (container Anki có thể khởi động chậm hơn bot)."""
    waited = 0
    while waited < max_wait_seconds:
        if check_anki_ready():
            return True
        time.sleep(5)
        waited += 5
        print(f"⏳ Chờ AnkiConnect... ({waited}s)")
    return False


def main():
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_USER_ID:
        print("❌ Thiếu TELEGRAM_BOT_TOKEN hoặc TELEGRAM_USER_ID trong .env")
        return

    print("🤖 Bot Anki khởi động...")

    if not wait_for_anki():
        print("❌ AnkiConnect không phản hồi sau 3 phút. Kiểm tra container anki (docker ps).")
        return
    print("✅ AnkiConnect sẵn sàng.")

    if check_claude_ready():
        print("✅ AI (Gemini) sẵn sàng.")
    else:
        print("⚠️ AI chưa phản hồi - bot vẫn chạy, sẽ thử lại khi có yêu cầu.")

    setup_anki_environment()
    ensure_deck_exists(DEFAULT_DECK)

    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    only_me = filters.User(user_id=TELEGRAM_USER_ID)

    app.add_handler(CommandHandler(["start", "help"], cmd_start, filters=only_me))
    app.add_handler(CommandHandler("deck", cmd_deck, filters=only_me))
    app.add_handler(CommandHandler("sync", cmd_sync, filters=only_me))
    app.add_handler(CommandHandler("sua", cmd_sua, filters=only_me))
    app.add_handler(CallbackQueryHandler(on_callback))
    app.add_handler(MessageHandler(only_me & filters.TEXT & ~filters.COMMAND, on_word))

    print(f"🚀 Bot đang chạy (long polling). Deck mặc định: {DEFAULT_DECK}")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
