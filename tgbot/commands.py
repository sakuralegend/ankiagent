# ==============================================================================
# --- CÁC LỆNH MỘT PHÁT: /start /help /menu /deck /thongke /don /sync
# + job nền 3h sáng tự dọn inbox. (Lệnh có luồng nhiều bước nằm ở flow_*.)
# ==============================================================================
import asyncio
import datetime
import os

from telegram import Update
from telegram.ext import ContextTypes

from anki_tools.config import TELEGRAM_USER_ID, TOPIC_DECK_PARENT
from anki_tools.backup import human_size, list_backups, run_backup
from anki_tools.topics import FALLBACK_TOPIC
from anki_tools.anki_client import (
    CARD_STATES,
    ensure_deck_exists,
    get_card_state_stats,
    get_root_decks,
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


async def _card_state_section():
    """Phần 'trạng thái học' của báo cáo — đếm RIÊNG từng deck gốc (kho), vì trộn
    kho từ vựng với kho ngữ pháp vào một cột số là mất hết ý nghĩa: hai kho khác
    nhau cả về số lượng lẫn nhịp học. Trả về list dòng text ([] nếu không đếm được).
    """
    roots = await asyncio.to_thread(get_root_decks)
    if not roots:
        return []
    # Đếm các kho song song: mỗi kho là mấy request nhỏ, chờ tuần tự thì cộng dồn lâu
    results = await asyncio.gather(
        *(asyncio.to_thread(get_card_state_stats, deck) for deck in roots)
    )

    lines = []
    for deck, (counts, total) in sorted(
        zip(roots, results), key=lambda x: -(x[1][1] or 0)
    ):
        if counts is None or not total:
            continue  # deck rỗng (vd 'Mặc định') hoặc lỗi -> không bịa số
        lines.append("")
        lines.append(f"📚 {deck} — {total} thẻ")
        for slug, label, _ in CARD_STATES:
            n = counts.get(slug, 0)
            # 0 thẻ tạm ngưng/tạm ẩn là chuyện bình thường, đừng làm rối báo cáo
            if not n and slug in ("suspended", "buried"):
                continue
            lines.append(f"   {label}: {n} ({round(n * 100 / total)}%)")
        # Số lẻ không rơi vào nhóm nào (bản Anki khác có thể phân loại khác) —
        # thà hiện ra còn hơn để tổng cộng lại không khớp mà người đọc không biết
        missing = total - sum(counts.values())
        if missing:
            lines.append(f"   ❓ Khác: {missing} ({round(missing * 100 / total)}%)")
    return lines


async def thongke_report():
    """Dựng text báo cáo thống kê. Tách riêng để cả lệnh /thongke lẫn nút
    📊 trong menu 🛠 đều dùng chung một logic."""
    stats, untagged = await asyncio.to_thread(get_topic_stats)
    if stats is None:
        return "❌ Không đếm được (AnkiConnect trên VPS lỗi?)."

    total = sum(stats.values())
    lines = ["📊 THỐNG KÊ"]
    lines += await _card_state_section()
    lines.append("")
    lines.append(f"📂 CHỦ ĐỀ (kho {TOPIC_DECK_PARENT}): {total} thẻ")
    lines.append("─" * 22)
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
    return "\n".join(lines)


async def cmd_thongke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Phân bố thẻ theo chủ đề + cảnh báo khi chạm ngưỡng cần tách deck."""
    _reset_idle_timer(context, update.effective_chat.id)
    msg = await update.message.reply_text("⏳ Đang đếm thẻ theo chủ đề...")
    await msg.edit_text(await thongke_report())


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


# ==============================================================================
# --- JOB NỀN ---
# ⚠️ QUY TẮC SỐNG CÒN của mọi job ở đây: thân vòng lặp PHẢI bọc try/except.
# Task asyncio mà ném exception thì CHẾT HẲN VÀ IM LẶNG — từ đó job không bao giờ
# chạy nữa cho tới khi restart bot, mà không có dấu hiệu nào báo ra. Bản đầu của
# _nightly_don dính đúng lỗi này: AnkiConnect lỗi một đêm là mất luôn job dọn
# inbox (phát hiện 21/07/2026 khi soi log sau deploy).
# Dùng vòng lặp asyncio tự viết thay vì JobQueue của PTB vì JobQueue đòi thêm gói
# apscheduler — không đáng cài thêm dependency lên VPS đang chạy ổn.
# ==============================================================================
async def _sleep_until(hour, minute=0):
    """Ngủ tới mốc giờ:phút gần nhất (hôm nay nếu chưa qua, không thì ngày mai).
    Giờ VPS đã đặt = giờ VN nên không phải quy đổi múi giờ."""
    now = datetime.datetime.now()
    target = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if target <= now:
        target += datetime.timedelta(days=1)
    await asyncio.sleep((target - now).total_seconds())


async def _guard(name, body, cooldown=60):
    """Chạy `body()` mãi mãi, nuốt mọi lỗi để vòng lặp KHÔNG BAO GIỜ chết.
    Lỗi thì log rồi nghỉ `cooldown` giây để không quay vòng điên cuồng."""
    while True:
        try:
            await body()
        except asyncio.CancelledError:
            raise                       # tắt bot: phải để hủy task diễn ra bình thường
        except Exception as e:
            print(f"⚠️ Job '{name}' lỗi: {e!r} — bỏ qua nhịp này, job vẫn tiếp tục.")
            await asyncio.sleep(cooldown)


async def _nightly_don(app):
    """3h sáng mỗi ngày tự dọn inbox. Chỉ nhắn Telegram khi CÓ thẻ được chuyển —
    đêm không có gì thì im lặng."""
    async def once():
        await _sleep_until(3, 0)
        moved, total = await asyncio.to_thread(move_graduated_from_inbox)
        if moved and total:
            await asyncio.to_thread(trigger_sync)
            try:
                await app.bot.send_message(TELEGRAM_USER_ID, "🌙 " + _don_report(moved, total))
            except Exception as e:
                print(f"⚠️ Không gửi được báo cáo dọn inbox: {e}")

    await _guard("don inbox", once)


# --- Sync định kỳ + backup đêm (user chốt 20/07/2026) -------------------------
# Bối cảnh: user lo "quên sync trên điện thoại là mất". Đã giải thích rằng ép VPS
# tải-về-một-chiều KHÔNG cứu được (dữ liệu ôn tập nằm trong điện thoại, AnkiWeb
# cũng chưa có) và còn nguy hiểm (Download from AnkiWeb = GHI ĐÈ collection VPS,
# xóa luôn thẻ bot vừa thêm). Hai việc AN TOÀN làm thay:
#   1. sync ĐỊNH KỲ HAI CHIỀU: không ghi đè bên nào, chỉ giữ VPS <-> AnkiWeb
#      không lệch xa, để lúc có sự cố còn dễ gỡ.
#   2. backup theo ngày: đây mới là thứ cứu được khi full sync chọn nhầm chiều.
PERIODIC_SYNC_MINUTES = 30
BACKUP_HOUR = 3          # 3h30 sáng, chạy sau job dọn inbox lúc 3h00
BACKUP_MINUTE = 30


async def _periodic_sync():
    """Sync hai chiều mỗi PERIODIC_SYNC_MINUTES phút. Im lặng khi thành công —
    chỉ log lúc lỗi để không spam Telegram."""
    async def once():
        await asyncio.sleep(PERIODIC_SYNC_MINUTES * 60)
        if not await asyncio.to_thread(trigger_sync):
            print("⚠️ Sync định kỳ thất bại (sẽ thử lại ở nhịp sau).")

    await _guard("sync dinh ky", once)


async def _nightly_backup(app):
    """Backup collection mỗi đêm + dọn bản cũ. Chỉ nhắn Telegram khi THẤT BẠI
    (backup thành công là chuyện thường ngày, không cần làm phiền)."""
    async def once():
        await _sleep_until(BACKUP_HOUR, BACKUP_MINUTE)
        try:
            result, removed = await asyncio.to_thread(run_backup)
        except Exception as e:
            result, removed = {"path": "", "errors": [str(e)]}, 0
        if result.get("path"):
            print(f"💾 Backup đêm: {human_size(result['bytes'])} -> {result['path']} "
                  f"(xóa {removed} bản cũ)")
            return
        try:
            await app.bot.send_message(
                TELEGRAM_USER_ID,
                "⚠️ BACKUP ĐÊM THẤT BẠI — kho Anki đang KHÔNG có bản sao lưu mới.\n"
                + "; ".join(result.get("errors", []))[:300]
            )
        except Exception as e:
            print(f"⚠️ Không gửi được cảnh báo backup: {e}")

    await _guard("backup dem", once)


async def cmd_backup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/backup — tạo bản sao lưu ngay (dùng trước khi làm gì mạo hiểm)."""
    _reset_idle_timer(context, update.effective_chat.id)
    msg = await update.message.reply_text("⏳ Đang sao lưu (xuất từng deck, hơi lâu)...")
    result, removed = await asyncio.to_thread(run_backup)
    if not result.get("path"):
        await msg.edit_text("❌ Backup thất bại:\n" + "; ".join(result.get("errors", []))[:300])
        return
    lines = [f"💾 Đã sao lưu {len(result['decks'])} deck — {human_size(result['bytes'])}"]
    for d in result["decks"]:
        lines.append(f"   {d['deck']}: {human_size(d['bytes'])}")
    lines.append(f"📁 {os.path.basename(result['path'])}")
    existing = await asyncio.to_thread(list_backups)
    lines.append(f"🗂 Đang giữ {len(existing)} bản "
                 f"(tổng {human_size(sum(s for _, s in existing))}).")
    if removed:
        lines.append(f"🧹 Đã xóa {removed} bản cũ nhất.")
    if result["errors"]:
        lines.append("⚠️ " + "; ".join(result["errors"])[:200])
    await msg.edit_text("\n".join(lines))


async def cmd_sync(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _reset_idle_timer(context, update.effective_chat.id)
    msg = await update.message.reply_text("⏳ Đang sync AnkiWeb...")
    ok = await asyncio.to_thread(trigger_sync)
    await msg.edit_text("☁️ Đã sync AnkiWeb." if ok else "❌ Sync thất bại (xem log trên VPS).")
