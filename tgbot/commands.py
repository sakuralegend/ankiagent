# ==============================================================================
# --- CÁC LỆNH MỘT PHÁT: /start /help /menu /deck /thongke /don /sync
# (Lệnh có luồng nhiều bước nằm ở flow_*; job nền chạy ngầm nằm ở jobs.py.)
# ==============================================================================
import asyncio
import os

from telegram import Update
from telegram.ext import ContextTypes

from anki_tools.config import TOPIC_DECK_PARENT
from anki_tools.backup import human_size, list_backups, run_backup
from anki_tools.utils import log_warn
from anki_tools.topics import FALLBACK_TOPIC
from anki_tools.anki_client import (
    CARD_STATES,
    ensure_deck_exists,
    get_card_state_stats,
    get_root_decks,
    get_topic_stats,
    move_graduated_from_inbox,
    promote_stage1_to_stage2,
    sync_now,
    trigger_sync,
)

from .alerts import alerter, sync_error_hint

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


# Ngưỡng "đèn báo" cần tách chủ đề (xem git log quanh 18/07/2026: quy tắc 100 thẻ / 15% other)
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
        warns.append(f"⚠️ {untagged} thẻ CHƯA có tag chủ đề — chạy `python scripts/tag_topics.py --missing` trên PC.")

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


def run_don():
    """LỆNH GỘP TẤT-CẢ-TRONG-MỘT — user học xong gõ /don một phát là xong việc.

    Bốn bước, đúng thứ tự này:
      1. sync KÉO VỀ  — lấy kết quả học từ AnkiWeb (điện thoại đã đẩy lên)
      2. GĐ1 -> GĐ2   — làm quen xong thì thành thẻ gõ mới tinh
      3. GĐ2 -> kho   — gõ xong thì về deck chủ đề theo tag
      4. sync ĐẨY LÊN — trả kết quả dọn về AnkiWeb

    ⚠️ BƯỚC 1 MỚI LÀ THỨ LÀM LỆNH NÀY ĐÁNG TIN, và nó từng THIẾU: bản cũ chỉ sync
    SAU khi dọn, tức VPS xử lý trên ảnh chụp cũ — đúng những thẻ user vừa học xong
    trên iPhone lại là thẻ bị bỏ sót. Luôn chạy bước 1, kể cả khi đoán là không có
    gì mới.

    Sync bước 1 hỏng thì VẪN dọn tiếp: thao tác idempotent và chỉ đụng thẻ đang
    thực sự is:review trên VPS, nên cùng lắm là chuyển được ít thẻ hơn, lần /don
    sau bù. Nhưng phải BÁO RA để user không tưởng xong mà thực ra chưa đẩy lên.

    Trả về dict để _don_report dựng tin nhắn (không tự format ở đây, để job đêm
    và lệnh tay dùng chung một chỗ)."""
    out = {"sync_in": False, "promoted": 0, "moved": None, "total": 0,
           "sync_out": False, "error": None}
    out["sync_in"] = trigger_sync()
    try:
        out["promoted"] = promote_stage1_to_stage2()
    except Exception as e:
        out["error"] = f"GĐ1→GĐ2: {e}"
        log_warn(f"promote_stage1_to_stage2 lỗi: {e!r}")
    moved, total = move_graduated_from_inbox()
    out["moved"], out["total"] = moved, total
    if out["promoted"] or total:
        out["sync_out"] = trigger_sync()
    return out


def _don_report(res):
    """Format kết quả run_don() thành tin nhắn. Nói rõ CẢ BỐN BƯỚC — nhất là
    bước sync nào hỏng, vì đó là lúc user dễ tưởng xong mà thực ra chưa xong."""
    lines = []
    if not res["sync_in"]:
        lines.append("⚠️ SYNC KÉO VỀ THẤT BẠI — dọn trên dữ liệu cũ, có thể sót thẻ "
                     "bạn vừa học. Xem log VPS; nếu là 'Sync status 2' thì Anki đang "
                     "đòi full sync, phải xử lý tay.")
    if res["error"]:
        lines.append(f"❌ {res['error']}")

    if res["promoted"]:
        lines.append(f"🎓 {res['promoted']} thẻ làm quen xong → chuyển sang deck GÕ "
                     "(đã reset thành thẻ mới).")
    if res["total"]:
        lines.append(f"📦 {res['total']} thẻ gõ xong → về deck chủ đề:")
        for slug, n in sorted(res["moved"].items(), key=lambda x: -x[1]):
            lines.append(f"  {n:>3} → {TOPIC_DECK_PARENT}::{slug}")
    elif res["moved"] is None:
        lines.append("❌ Không dọn được deck gõ (AnkiConnect lỗi? xem log trên VPS).")

    if not res["promoted"] and not res["total"] and not res["error"]:
        lines.append("✅ Không có thẻ nào tốt nghiệp — chưa có gì để chuyển.")

    if res["sync_out"]:
        lines.append("☁️ Đã đẩy kết quả lên AnkiWeb.")
    elif res["promoted"] or res["total"]:
        lines.append("⚠️ ĐẨY LÊN THẤT BẠI — kết quả dọn mới chỉ nằm trên VPS.")
    else:
        lines.append("☁️ Đã sync AnkiWeb." if res["sync_in"] else "")

    lines.append("📱 Mở Anki trên iPhone để kéo về.")
    return "\n".join(l for l in lines if l)


async def cmd_don(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/don — gộp tất cả: sync về, dọn hai chặng, sync lên. Xem run_don()."""
    _reset_idle_timer(context, update.effective_chat.id)
    msg = await update.message.reply_text("⏳ Đang sync về rồi dọn...")
    res = await asyncio.to_thread(run_don)
    await msg.edit_text(_don_report(res))


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
    ok, err = await asyncio.to_thread(sync_now)
    if ok:
        # Sync tay thành công thì gỡ luôn trạng thái báo động, đừng bắt user chờ
        # tới nhịp định kỳ mới thấy tin "đã bình thường".
        await alerter.ok("sync", "Sync AnkiWeb")
        await msg.edit_text("☁️ Đã sync AnkiWeb.")
    else:
        await msg.edit_text(f"❌ Sync thất bại:\n{err[:300]}\n\n👉 {sync_error_hint(err)}")
