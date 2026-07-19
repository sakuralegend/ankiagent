# ==============================================================================
# --- CÁC LỆNH MỘT PHÁT: /start /help /menu /deck /thongke /don /sync
# + job nền 3h sáng tự dọn inbox. (Lệnh có luồng nhiều bước nằm ở flow_*.)
# ==============================================================================
import asyncio
import datetime

from telegram import Update
from telegram.ext import ContextTypes

from anki_tools.config import TELEGRAM_USER_ID, TOPIC_DECK_PARENT
from anki_tools.topics import FALLBACK_TOPIC
from anki_tools.anki_client import (
    ensure_deck_exists,
    get_topic_stats,
    move_graduated_from_inbox,
    trigger_sync,
)

from .core import (
    HELP_TEXT,
    _current_deck,
    _deck_choose_keyboard,
    _menu_keyboard,
    _menu_text,
    _reset_idle_timer,
    _set_deck,
    _sync_report_line,
)


async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _reset_idle_timer(context, update.effective_chat.id)
    deck = _current_deck(context)
    if deck:
        await update.message.reply_text(f"{HELP_TEXT}\n\n📦 Deck hiện tại: {deck}")
    else:
        await update.message.reply_text(
            f"{HELP_TEXT}\n\n🤖 Đang ở chế độ tự động ({TOPIC_DECK_PARENT}::<chủ đề>) "
            "— gõ từ luôn, hoặc chọn deck cố định:",
            reply_markup=_deck_choose_keyboard(),
        )


async def cmd_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _reset_idle_timer(context, update.effective_chat.id)
    await update.message.reply_text(_menu_text(context), reply_markup=_menu_keyboard())


async def cmd_deck(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _reset_idle_timer(context, update.effective_chat.id)
    if not context.args:
        # Không có tham số -> hiện 2 tùy chọn (deck có sẵn / tạo mới) như menu khởi đầu
        deck = _current_deck(context)
        current = (f"📦 Deck hiện tại: {deck}" if deck
                   else f"📦 Deck: 🤖 tự động theo chủ đề ({TOPIC_DECK_PARENT}::<topic>).")
        await update.message.reply_text(
            f"{current}\n📚 Chọn deck:", reply_markup=_deck_choose_keyboard()
        )
        return
    deck_name = " ".join(context.args).strip()
    ok = await asyncio.to_thread(ensure_deck_exists, deck_name)
    if ok:
        _set_deck(context, deck_name)
        sync_line = await _sync_report_line()  # deck mới tạo phải lên AnkiWeb ngay
        await update.message.reply_text(f"📦 Đã chuyển sang deck: {deck_name}\n{sync_line}")
    else:
        await update.message.reply_text("❌ Không tạo/kiểm tra được deck (AnkiConnect lỗi?).")


# Ngưỡng "đèn báo" cần tách chủ đề (xem CHANGELOG 18/07/2026: quy tắc 100 thẻ / 15% other)
TOPIC_DECK_WARN = 100     # deck con vượt mức này -> nên tách chủ đề con
OTHER_WARN_PCT = 15       # other chiếm quá % này của kho -> phân loại đang "rò rỉ"


async def cmd_thongke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Phân bố thẻ theo chủ đề + cảnh báo khi chạm ngưỡng cần tách deck."""
    _reset_idle_timer(context, update.effective_chat.id)
    msg = await update.message.reply_text("⏳ Đang đếm thẻ theo chủ đề...")
    stats, untagged = await asyncio.to_thread(get_topic_stats)
    if stats is None:
        await msg.edit_text("❌ Không đếm được (AnkiConnect trên VPS lỗi?).")
        return

    total = sum(stats.values())
    lines = [f"📊 KHO {TOPIC_DECK_PARENT}: {total} thẻ", "─" * 22]
    for slug, n in sorted(stats.items(), key=lambda x: -x[1]):
        if n == 0:
            continue
        mark = " ⚠️" if n >= TOPIC_DECK_WARN else ""
        lines.append(f"{n:>4} │ {slug}{mark}")

    warns = []
    for slug, n in stats.items():
        if n >= TOPIC_DECK_WARN:
            warns.append(f"⚠️ '{slug}' đã {n} thẻ (≥{TOPIC_DECK_WARN}) — nên tách chủ đề con "
                         f"(thêm slug dạng '{slug}::nhanh-con' vào topics.py).")
    other_pct = (stats.get(FALLBACK_TOPIC, 0) * 100 // total) if total else 0
    if other_pct > OTHER_WARN_PCT:
        warns.append(f"⚠️ '{FALLBACK_TOPIC}' chiếm {other_pct}% kho (>{OTHER_WARN_PCT}%) — trong đó chắc "
                     "đã có cụm từ đủ lớn để thành chủ đề riêng.")
    if untagged:
        warns.append(f"⚠️ {untagged} thẻ CHƯA có tag chủ đề — chạy `python tag_topics.py --missing` trên PC.")

    lines.append("─" * 22)
    if warns:
        lines.extend(warns)
    else:
        lines.append(f"✅ Chưa chạm ngưỡng tách deck ({TOPIC_DECK_WARN} thẻ/chủ đề, {FALLBACK_TOPIC} ≤{OTHER_WARN_PCT}%).")
    await msg.edit_text("\n".join(lines))


def _don_report(moved, total):
    """Format kết quả move_graduated_from_inbox thành tin nhắn."""
    if moved is None:
        return "❌ Không dọn được inbox (AnkiConnect lỗi? xem log trên VPS)."
    if total == 0:
        return "📥 Inbox chưa có thẻ nào tốt nghiệp — không có gì để chuyển."
    lines = [f"📦 Đã chuyển {total} thẻ tốt nghiệp từ inbox về deck chủ đề:"]
    for slug, n in sorted(moved.items(), key=lambda x: -x[1]):
        lines.append(f"  {n:>3} → {TOPIC_DECK_PARENT}::{slug}")
    return "\n".join(lines)


async def cmd_don(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Chuyển ngay thẻ đã tốt nghiệp learning từ inbox về deck chủ đề theo tag."""
    _reset_idle_timer(context, update.effective_chat.id)
    msg = await update.message.reply_text("⏳ Đang dọn inbox...")
    moved, total = await asyncio.to_thread(move_graduated_from_inbox)
    if total:
        await asyncio.to_thread(trigger_sync)
    await msg.edit_text(_don_report(moved, total))


async def _nightly_don(app):
    """Job nền: 3h sáng mỗi ngày tự dọn inbox (giờ VPS = giờ VN). Chỉ nhắn
    Telegram khi có thẻ được chuyển — đêm không có gì thì im lặng."""
    while True:
        now = datetime.datetime.now()
        target = now.replace(hour=3, minute=0, second=0, microsecond=0)
        if target <= now:
            target += datetime.timedelta(days=1)
        await asyncio.sleep((target - now).total_seconds())
        moved, total = await asyncio.to_thread(move_graduated_from_inbox)
        if moved and total:
            await asyncio.to_thread(trigger_sync)
            try:
                await app.bot.send_message(TELEGRAM_USER_ID, "🌙 " + _don_report(moved, total))
            except Exception as e:
                print(f"⚠️ Không gửi được báo cáo dọn inbox: {e}")


async def cmd_sync(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _reset_idle_timer(context, update.effective_chat.id)
    msg = await update.message.reply_text("⏳ Đang sync AnkiWeb...")
    ok = await asyncio.to_thread(trigger_sync)
    await msg.edit_text("☁️ Đã sync AnkiWeb." if ok else "❌ Sync thất bại (xem log trên VPS).")
