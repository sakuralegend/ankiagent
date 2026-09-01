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
    dang_chay_hang_loat,
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
from .flow_edit import _do_redo
from .flow_scan import _run_scan_add, _scan_clear, _scan_exclude
from .flow_add import (_tumoi_clear, run_banthe_add, run_tumoi_add,
                       tumoi_exclude)
from .flow_special import do_add_plural, do_redo_plural, on_special_callback


# Bảng ba luồng thêm hàng loạt — xem khối "BA LUỒNG..." trong `on_callback` để
# biết vì sao là BẢNG chứ không phải ba khối chép tay.
_NUT_LO = {
    lo["co"]: lo for lo in (
        {"co": "scan", "don": _scan_clear, "kho": "scan_words", "chay": _run_scan_add,
         "huy": "⏭️ Đã hủy — không thêm từ nào.",
         "het_han": "⌛ Danh sách quét đã hết hạn, gửi lại ảnh nhé.",
         "bat_dau": lambda v: f"🔄 Bắt đầu thêm {len(v)} từ đã duyệt..."},
        {"co": "tumoi", "don": _tumoi_clear, "kho": "tumoi_words", "chay": run_tumoi_add,
         "huy": "⏭️ Đã hủy — không thêm từ nào.",
         "het_han": "⌛ Danh sách đã hết hạn, gõ /tumoi lại nhé.",
         "bat_dau": lambda v: f"🔄 Bắt đầu thêm {len(v)} từ đã duyệt..."},
        {"co": "banthe", "don": lambda ud: ud.pop("banthe_tu", None),
         "kho": "banthe_tu", "chay": run_banthe_add,
         "huy": "⏭️ Bỏ qua — không thêm bạn thể.",
         "het_han": "⌛ Hết hạn — gõ lại từ gốc để hiện lại gợi ý.",
         "bat_dau": lambda v: f"🔄 Đang thêm '{v}'..."},
    )
}


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
        await _do_redo(msg, text, context)
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

    # --- Đang có danh sách /tumoi chờ duyệt: 'bỏ 3 7' loại VÀ nhớ luôn ---
    if context.user_data.get("tumoi_words") and re.fullmatch(r"(bỏ|bo)[\s,.\d]+", text.lower()):
        await tumoi_exclude(update, context, text)
        return

    # --- Không chọn deck = chế độ TỰ ĐỘNG (AI tự bỏ vào deck con theo chủ đề), KHÔNG chặn nữa ---
    # --- Còn lại: text là từ cần thêm ---
    word = text
    status = await update.message.reply_text(f"🔍 Đang kiểm tra '{word}'...")
    await _add_with_dup_check(status, word, context)


# 🔴 CẤM thêm nhánh nút MỚI vào hàm này (user duyệt 03/08). File kịch trần dòng (S13 canh), cố ý KHÔNG
# tách vì tách là cắt ruột hàm mà bot là nơi lỗi chết im lặng. Nhánh mới ⇒ hàm file riêng, gọi 1 dòng.
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

    # --- BA LUỒNG THÊM HÀNG LOẠT DÙNG CHUNG BỘ BA NÚT: huỷ · dừng · xác nhận ---
    #
    # 🔴 Gom 01/09/2026 (nợ ghi 23/08, điều kiện gom đã tới khi luồng thứ 5 xuất
    # hiện). Trước đó `scan*`, `tumoi*`, `banthe*` mỗi luồng chép lại đủ 9 nhánh
    # giống hệt nhau — và ba bản chép ĐÃ trôi lệch thật: `bantheadd` **pop** dữ
    # liệu chờ TRƯỚC khi kiểm có đợt nào đang chạy, nên khi bận nó vẫn bảo "chờ
    # xong rồi bấm lại nhé" trong lúc từ cần thêm đã mất trắng. Bảng dưới đây
    # buộc cả ba đi CÙNG một đường nên lệch kiểu đó không tái phát được.
    #
    # Khác biệt giữa ba luồng là DỮ LIỆU, không phải code:
    #   don      dọn trạng thái chờ (nhận user_data)
    #   huy      lời nhắn khi bấm Huỷ
    #   kho      khoá trong user_data giữ thứ sắp thêm
    #   het_han  lời nhắn khi trạng thái đã hết hạn
    #   bat_dau  lời nhắn lúc khởi động (nhận chính thứ sắp thêm)
    #   chay     hàm async làm việc thật
    lo = _NUT_LO.get(data[:-6] if data.endswith("cancel") else
                     data[:-4] if data.endswith("stop") else
                     data[:-3] if data.endswith("add") else "")
    if lo is not None:
        co = lo["co"]
        if data == f"{co}cancel":
            lo["don"](context.user_data)
            await query.edit_message_text(lo["huy"])
            return
        if data == f"{co}stop":
            if context.bot_data.get(f"{co}_running"):
                context.bot_data[f"{co}_stop"] = True
                # Tin tiến độ tự chuyển thành tổng kết ở vòng lặp kế tiếp
            return
        if data == f"{co}add":
            gia_tri = context.user_data.get(lo["kho"])
            if not gia_tri:
                await query.edit_message_text(lo["het_han"])
                return
            ban = dang_chay_hang_loat(context)
            if ban:
                # Trả lời bằng tin MỚI để giữ danh sách + nút (bấm lại sau được)
                await query.message.reply_text(
                    f"⏳ Đang chạy đợt '{ban}' — chờ xong rồi bấm lại nhé.")
                return
            lo["don"](context.user_data)
            await query.edit_message_text(lo["bat_dau"](gia_tri))
            # Task riêng để bot vẫn nhận update (nhất là nút ⏹ Dừng) trong lúc chạy
            asyncio.create_task(
                lo["chay"](context, query.message.chat_id, query.message, gia_tri))
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
        # `che_do` quyết định chạy tiếp bằng luồng nào — hai luồng dùng chung bộ
        # nút này vì chúng dùng chung lõi cào (`pipeline.cao_mot_tu`).
        if pend.get("che_do") == "sua":
            await query.edit_message_text(f"🔍 Đang làm lại '{pend['word']}' — nghĩa "
                                          f"[{m['pos']}] {m['en'][:50]}...")
            await _do_redo(query.message, pend["word"], context, chon_id=m["id"])
            return
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
                pass   # chỉ là gỡ nút cho gọn; hụt thì nút còn đó, bấm lại vẫn đúng
            return
        await _do_redo(query.message, word, context)
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
