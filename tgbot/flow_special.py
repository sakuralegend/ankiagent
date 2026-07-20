# ==============================================================================
# --- ⭐ MỤC ĐẶC BIỆT: các deck NGỮ PHÁP (biến cách), tách khỏi luồng từ vựng ---
# Hiện có 1 loại: số nhiều bất quy tắc. Sau này thêm loại mới (genitive số nhiều,
# chia động từ...) thì chỉ cần: viết pipeline trong grammar_forms/, rồi thêm 1
# nút vào _special_keyboard() + 1 nhánh trong on_special_callback().
#
# Mọi nghiệp vụ nằm ở grammar_forms/ — file này CHỈ lo giao diện Telegram.
# ==============================================================================
import asyncio

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from anki_tools.anki_client import trigger_sync
from anki_tools.utils import hl_to_bracket, strip_accents_perfectly

from grammar_forms import cards as gcards
from grammar_forms.config import PLURAL_DECK
from grammar_forms.pipeline import load_word_list, process_word, redo_note, redo_word

from .core import SYNC_FAIL_TEXT, SYNC_OK_TEXT, _reset_idle_timer
from .flow_edit import SUADECK_DELAY_SECONDS

SPECIAL_TEXT = (
    "⭐ MỤC ĐẶC BIỆT — thẻ ngữ pháp (biến cách)\n"
    "───────────────────\n"
    f"Thẻ loại này nằm riêng ở {PLURAL_DECK}, KHÔNG lẫn vào deck từ vựng RUSSIAN.\n"
    "Mặt trước: từ số ít + nghĩa + audio → bạn gõ dạng số nhiều.\n"
    "Mặt sau: dạng số nhiều + audio + 3 ví dụ dùng đúng dạng đó.\n\n"
    "Chọn việc muốn làm:"
)


def _special_keyboard():
    """Menu mục đặc biệt. Thêm loại biến cách mới -> thêm 1 hàng nút ở đây."""
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Thêm 1 từ số nhiều bất quy tắc", callback_data="sp:pl:one")],
        [InlineKeyboardButton("📋 Thêm loạt từ danh sách có sẵn", callback_data="sp:pl:batch")],
        [InlineKeyboardButton("🔄 Làm lại 1 thẻ (giữ tiến trình học)", callback_data="sp:pl:sua")],
        [InlineKeyboardButton("🩹 Vá thẻ cũ (thiếu ví dụ/audio)", callback_data="sp:pl:fix")],
    ])


async def cmd_dacbiet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _reset_idle_timer(context, update.effective_chat.id)
    await update.message.reply_text(SPECIAL_TEXT, reply_markup=_special_keyboard())


def _format_summary(info):
    """Tóm tắt 1 thẻ số nhiều vừa tạo/làm lại, dạng text thuần cho Telegram."""
    lines = [
        f"✅ THẺ SỐ NHIỀU: {info['word']} → {info['plural']}",
    ]
    if info.get("kind"):
        lines.append(f"🔤 Kiểu: {info['kind']}")
    if info.get("en"):
        lines.append(f"🇬🇧 {', '.join(info['en'])}")
    lines.append(f"🇻🇳 {info['vi']}")

    for i, ex in enumerate(info.get("examples", [])[:3]):
        lines.append(f"💡 {i + 1}. {hl_to_bracket(ex['ru'])}")
        lines.append(f"     🇬🇧 {hl_to_bracket(ex['en'])}")
        lines.append(f"     🇻🇳 {hl_to_bracket(ex['vi'])}")

    if info.get("missing_audio"):
        lines.append("⚠️ Thiếu audio một trong hai dạng (cả OpenRussian lẫn TTS đều hụt).")
    lines.append(f"📦 {info.get('deck', PLURAL_DECK)}")
    if info.get("synced") is False:
        lines.append(SYNC_FAIL_TEXT)
    else:
        lines.append(SYNC_OK_TEXT)
    return "\n".join(lines)


async def do_add_plural(msg, word, context):
    """Thêm 1 thẻ số nhiều (gọi từ dispatch khi đang chờ từ)."""
    await msg.edit_text(f"⏳ Đang dựng thẻ số nhiều cho '{word}' (cào + AI + audio)...")
    success, info, error = await asyncio.to_thread(process_word, word, PLURAL_DECK, True)
    if not success:
        await msg.edit_text(f"❌ {error}")
        return
    await msg.edit_text(_format_summary(info))


async def do_redo_plural(msg, word, context):
    """Làm lại 1 thẻ số nhiều: cào lại + AI sinh lại ví dụ + vá audio thiếu,
    ghi đè cùng note_id nên TIẾN TRÌNH HỌC giữ nguyên (giống /sua thẻ từ vựng)."""
    await msg.edit_text(f"⏳ Đang làm lại thẻ số nhiều của '{word}'...")
    success, info, error = await asyncio.to_thread(redo_word, word, True)
    if not success:
        await msg.edit_text(f"❌ {error}")
        return
    text = _format_summary(info).replace("✅ THẺ SỐ NHIỀU:", "🔄 ĐÃ LÀM LẠI:", 1)
    await msg.edit_text(text + "\n📈 Tiến trình học giữ nguyên.")


# ------------------------------------------------------------------ thêm loạt
def _batch_preview(words):
    minutes = max(1, round(len(words) * 14 / 60))  # ~11s (AI có thể phải làm lại) + nghỉ
    lines = [f"📋 {len(words)} từ trong danh sách CHƯA có thẻ:"]
    lines += [f"{i}. {w['accented']} → {w['plural']}" for i, w in enumerate(words[:40], 1)]
    if len(words) > 40:
        lines.append(f"... và {len(words) - 40} từ nữa")
    lines.append("")
    lines.append(f"⏱ Thêm hết tốn ~{minutes} phút, ít nhất {len(words)} lượt AI.")
    lines.append("Chưa bấm ✅ thì chưa thêm gì.")
    kb = InlineKeyboardMarkup([[
        InlineKeyboardButton(f"✅ Thêm cả {len(words)} từ", callback_data="sp:pl:go"),
        InlineKeyboardButton("🚫 Hủy", callback_data="sp:cancel"),
    ]])
    return "\n".join(lines), kb


async def _run_batch(context, chat_id, msg, rows, mode):
    """Task nền chạy loạt. mode='add' thêm thẻ mới, mode='fix' làm lại thẻ cũ.
    Chạy bằng create_task để nút ⏹ Dừng vẫn được xử lý trong lúc chạy."""
    context.bot_data["sp_running"] = True
    context.bot_data["sp_stop"] = False
    total = len(rows)
    done, failed = [], []
    stop_kb = InlineKeyboardMarkup([[InlineKeyboardButton("⏹ Dừng", callback_data="sp:stop")]])
    stopped, attempted = False, 0
    word_list = load_word_list()

    try:
        for i, row in enumerate(rows):
            if context.bot_data.get("sp_stop"):
                stopped = True
                break
            _reset_idle_timer(context, chat_id)
            attempted = i + 1

            if mode == "add":
                label = row["accented"]
                success, info, error = await asyncio.to_thread(
                    process_word, row["bare"], PLURAL_DECK, False, word_list
                )
            else:
                label = row["word"]
                success, info, error = await asyncio.to_thread(
                    redo_note, row["note_id"], False, word_list
                )

            if success:
                done.append(label)
                mark = "✅"
            else:
                failed.append(f"{label} ({error[:50]})" if error else label)
                mark = "❌"

            progress = (
                f"🔄 {'Thêm thẻ số nhiều' if mode == 'add' else 'Vá thẻ cũ'}: {attempted}/{total}\n"
                f"📝 Vừa xong: {label} {mark}\n"
                f"✅ {len(done)} │ ❌ {len(failed)}"
            )
            try:
                await msg.edit_text(progress, reply_markup=stop_kb)
            except Exception:
                pass

            if attempted < total and not context.bot_data.get("sp_stop"):
                await asyncio.sleep(SUADECK_DELAY_SECONDS)
    finally:
        context.bot_data["sp_running"] = False
        context.bot_data["sp_stop"] = False

    synced = await asyncio.to_thread(trigger_sync) if done else True

    verb = "thêm thẻ số nhiều" if mode == "add" else "vá thẻ cũ"
    title = f"⏹ ĐÃ DỪNG {verb}" if stopped else f"🏁 XONG {verb}"
    lines = [f"{title}: ✅ {len(done)} │ ❌ {len(failed)} │ tổng {total}"]
    if done:
        shown = ", ".join(done[:30])
        lines.append(f"✅ {shown}{f' (+{len(done) - 30} nữa)' if len(done) > 30 else ''}")
    if failed:
        lines.append("❌ Chưa xong: " + "; ".join(failed[:10]))
    if stopped and attempted < total:
        lines.append(f"💤 Còn {total - attempted} từ chưa chạy — bấm lại /dacbiet để chạy tiếp "
                     "(từ đã thêm sẽ tự bị lọc).")
    lines.append(SYNC_OK_TEXT if synced else SYNC_FAIL_TEXT)
    try:
        await msg.edit_text("\n".join(lines))
    except Exception:
        pass


async def on_special_callback(query, context, data):
    """Xử lý mọi nút 'sp:*'. Trả về True nếu đã xử lý xong."""
    if data == "sp:menu":
        await query.edit_message_text(SPECIAL_TEXT, reply_markup=_special_keyboard())
        return True

    if data == "sp:cancel":
        context.user_data.pop("sp_rows", None)
        await query.edit_message_text("⏭️ Đã hủy.")
        return True

    if data == "sp:stop":
        if context.bot_data.get("sp_running"):
            context.bot_data["sp_stop"] = True
        return True

    if data == "sp:pl:one":
        context.user_data["awaiting"] = "plural_word"
        await query.edit_message_text(
            "➕ Gõ 1 danh từ tiếng Nga (dạng số ít, vd: дом) để tạo thẻ số nhiều:"
        )
        return True

    if data == "sp:pl:sua":
        context.user_data["awaiting"] = "plural_sua_word"
        await query.edit_message_text(
            "🔄 Gõ từ (dạng SỐ ÍT) cần làm lại thẻ số nhiều:\n"
            "Thẻ sẽ được dựng lại từ đầu nhưng GIỮ NGUYÊN tiến trình học."
        )
        return True

    if data == "sp:pl:batch":
        await query.edit_message_text("⏳ Đang đối chiếu danh sách với thẻ đã có...")
        rows = load_word_list()
        if not rows:
            await query.edit_message_text(
                "❌ Chưa có danh sách từ. Chạy trên máy: python -m grammar_forms.irregular_plurals"
            )
            return True
        known = await asyncio.to_thread(gcards.existing_words)
        if known is None:
            await query.edit_message_text("❌ Không đọc được thẻ đã có từ Anki — thử lại sau nhé.")
            return True
        todo = [r for r in rows if strip_accents_perfectly(r["bare"]) not in known]
        if not todo:
            await query.edit_message_text(
                f"✅ Cả {len(rows)} từ trong danh sách đều đã có thẻ — không còn gì để thêm."
            )
            return True
        context.user_data["sp_rows"] = todo
        text, kb = _batch_preview(todo)
        await query.edit_message_text(text, reply_markup=kb)
        return True

    if data == "sp:pl:go":
        rows = context.user_data.get("sp_rows")
        if not rows:
            await query.edit_message_text("⌛ Danh sách đã cũ, bấm lại /dacbiet nhé.")
            return True
        if context.bot_data.get("sp_running") or context.bot_data.get("sd_running") \
                or context.bot_data.get("scan_running"):
            await query.message.reply_text("⏳ Đang có một đợt chạy hàng loạt khác — chờ xong rồi bấm lại nhé.")
            return True
        context.user_data.pop("sp_rows", None)
        await query.edit_message_text(f"🔄 Bắt đầu thêm {len(rows)} thẻ số nhiều...")
        asyncio.create_task(
            _run_batch(context, query.message.chat_id, query.message, rows, "add")
        )
        return True

    if data == "sp:pl:fix":
        await query.edit_message_text("⏳ Đang tìm thẻ cũ cần vá...")
        note_ids = await asyncio.to_thread(gcards.deck_note_ids)
        if not note_ids:
            await query.edit_message_text(f"📂 Deck {PLURAL_DECK} chưa có thẻ nào.")
            return True
        # Chỉ vá thẻ THIẾU: chưa có ví dụ, hoặc chưa có audio dạng số nhiều
        rows = []
        for note_id in note_ids:
            note = await asyncio.to_thread(gcards.get_note, note_id)
            if not note:
                continue
            f = note["fields"]
            if not f.get("ExamplesHTML") or "[sound:" not in (f.get("PluralAudio") or ""):
                rows.append({"note_id": note_id, "word": f.get("Word", "?")})
        if not rows:
            await query.edit_message_text("✅ Mọi thẻ đều đã đủ ví dụ và audio — không cần vá.")
            return True
        if context.bot_data.get("sp_running"):
            await query.edit_message_text("⏳ Đang có đợt chạy khác, chờ xong rồi bấm lại nhé.")
            return True
        await query.edit_message_text(f"🩹 Bắt đầu vá {len(rows)} thẻ cũ...")
        asyncio.create_task(
            _run_batch(context, query.message.chat_id, query.message, rows, "fix")
        )
        return True

    return False
