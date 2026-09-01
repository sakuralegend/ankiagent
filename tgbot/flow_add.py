# ==============================================================================
# --- LUỒNG THÊM TỪ: gõ từ -> dò trùng -> pipeline (cào OpenRussian -> AI -> Anki).
# Hai nhánh rẽ:
#  • Từ ĐÃ CÓ thẻ -> không báo "bị trùng" suông mà đọc lại nguyên nội dung thẻ đó
#    ra như một mục TỪ ĐIỂN (_duplicate_text_and_keyboard).
#  • Từ không có trên OpenRussian -> từ điển hình thái (hoặc AI) đoán từ nguyên
#    mẫu, user bấm nút xác nhận mới thêm.
# ==============================================================================
import asyncio
import json
import os
import random
import re
import time

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from anki_tools.utils import log_warn, strip_accents_perfectly
from anki_tools.ai_client import call_claude_lemma
from anki_tools.lemma import guess_lemma_offline
from anki_tools.pipeline import process_word
from anki_tools.anki_client import (find_duplicate_notes, get_known_words,
                                    note_to_card_info, update_note_fields)
from anki_tools.anki_the import nhom_dong_tu
from anki_tools.chu_nga import nfc
from anki_tools import grammar

from .core import (_current_deck, _degraded_fix_keyboard, danh_sach_cho_duyet,
                   them_loat_tu, _reset_idle_timer)
from .hienthi import format_card_summary, format_dictionary_entry

_GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


async def _do_add(status_msg, word, deck_name, is_forced, context=None, chon_id=None):
    """Chạy pipeline thêm từ (trong thread) rồi cập nhật tin nhắn trạng thái."""
    t0 = time.time()
    await status_msg.edit_text(f"⏳ Đang xử lý '{word}' (cào OpenRussian → AI → Anki)...")
    success, card_info, error_msg = await asyncio.to_thread(
        process_word, word, deck_name, is_forced, True, chon_id  # do_sync=True trên VPS
    )
    if success:
        markup = None
        if card_info.get("ai_degraded"):
            markup = _degraded_fix_keyboard(card_info.get("clean_word", ""))
        await status_msg.edit_text(
            format_card_summary(card_info, time.time() - t0), reply_markup=markup
        )
        # Động từ mới -> dựng lại nhóm cùng gốc + mời thêm bạn thể còn thiếu.
        # CHỈ ở đây (gõ tay một từ); luồng thêm loạt cố ý im lặng (QD-39).
        if context is not None and "verb" in (card_info.get("pos") or "").lower():
            await _goi_y_ban_the(status_msg, context, card_info)
    elif (card_info or {}).get("nhieu_muc") and context is not None:
        # TỪ ĐỒNG TỰ -> hỏi user, chưa bấm thì CHƯA thẻ nào được thêm.
        await _show_homonym_buttons(status_msg, context, word,
                                    card_info["nhieu_muc"], deck_name, is_forced)
    elif (card_info or {}).get("not_found") and context is not None:
        # Từ không có trên OpenRussian: có thể sai chính tả hoặc là dạng biến cách
        # -> nhờ AI đoán từ nguyên mẫu rồi hỏi user xác nhận trước khi cào lại.
        await _suggest_lemma(status_msg, word, context)
    else:
        await status_msg.edit_text(f"❌ {error_msg}")


async def _suggest_lemma(status_msg, word, context):
    """Từ không tìm thấy -> đề xuất từ nguyên mẫu cho user bấm xác nhận.

    Hỏi TỪ ĐIỂN HÌNH THÁI trước (pymorphy3, offline): nếu nó nhận ra từ này thì
    đáp án chắc chắn đúng, khỏi tốn lượt AI và khỏi chờ. Chỉ khi từ điển bó tay —
    tức là gõ sai chính tả, thứ mà từ điển không xử lý được nhưng AI thì có — mới
    gọi AI đoán."""
    clean = strip_accents_perfectly(word)
    offline = await asyncio.to_thread(guess_lemma_offline, clean)
    if offline and offline != clean:
        await _show_lemma_buttons(status_msg, context, [offline], [
            f"⚠️ Không tìm thấy '{word}' trên OpenRussian.",
            f"📚 Từ điển hình thái: đây là dạng biến cách của '{offline}'.",
        ])
        return

    await status_msg.edit_text(
        f"🔍 Không thấy '{word}' trên OpenRussian — đang hỏi AI từ nguyên mẫu..."
    )
    guess = await asyncio.to_thread(call_claude_lemma, word)
    if not guess:
        await status_msg.edit_text(
            f"❌ Không tìm thấy '{word}' trên OpenRussian, và AI cũng không đoán được "
            "từ nguyên mẫu. Kiểm tra lại chính tả rồi gõ lại nhé."
        )
        return
    lines = [
        f"⚠️ Không tìm thấy '{word}' trên OpenRussian.",
        f"🤖 AI đoán từ nguyên mẫu: {guess['lemma']}",
    ]
    if guess["reason_vi"]:
        lines.append(f"💬 {guess['reason_vi']}")
    await _show_lemma_buttons(status_msg, context, [guess["lemma"]] + guess["alternatives"], lines)


async def _show_homonym_buttons(status_msg, context, word, muc, deck_name=None,
                                is_forced=False, che_do="them"):
    """Từ ĐỒNG TỰ -> hiện từng mục thành nút để user chọn nghĩa nào.

    Dùng chung cho CẢ HAI luồng (`che_do="them"` và `"sua"`) vì chúng chạy cùng
    một lõi cào (`pipeline.cao_mot_tu`). Hai bộ nút riêng thì sớm muộn một bên
    được vá còn bên kia không — mà bên không vá lại là bên GHI ĐÈ thẻ đang học.

    `мочь` là động từ *có thể* hay danh từ *sức lực*? Máy không đoán được, mà
    đoán sai thì SAI CẢ THẺ: nghĩa, badge thể/giống, và cả bảng chia. User chốt
    29/07: *"nếu tìm ra nhiều từ đồng chính tả, cho tôi chọn"*.

    Nút mang CHỈ SỐ chứ không mang tên từ — `callback_data` trần 64 byte, chữ
    Cyrillic ăn 2 byte mỗi ký tự nên tên từ dễ vượt (bẫy đã dính, xem
    `_show_lemma_buttons`).
    """
    context.user_data["homonym"] = {"word": word, "muc": muc, "deck": deck_name,
                                    "forced": is_forced, "che_do": che_do}
    rows = [[InlineKeyboardButton(f"{m['pos']} — {m['en'][:40]}",
                                  callback_data=f"dongtu:{i}")]
            for i, m in enumerate(muc)]
    rows.append([InlineKeyboardButton("🚫 Hủy", callback_data="dongtu:cancel")])
    dau = ("Chọn nghĩa bạn muốn học — thẻ sẽ lấy nghĩa, badge và bảng chia "
           "theo đúng mục đó:") if che_do == "them" else (
          "Chọn nghĩa đúng của thẻ ĐANG CÓ — chọn sai là ghi đè thẻ bằng nghĩa "
          "của từ khác. Chưa bấm thì thẻ chưa bị đụng gì:")
    await status_msg.edit_text(
        "\n".join([f"⚠️ '{word}' có {len(muc)} mục ĐỒNG CHÍNH TẢ trên OpenRussian.", dau]),
        reply_markup=InlineKeyboardMarkup(rows),
    )


async def _show_lemma_buttons(status_msg, context, candidates, lines):
    """Hiện các từ nguyên mẫu ứng viên thành nút bấm (dùng chung cho đề xuất của
    từ điển hình thái lẫn của AI). Chưa bấm nút thì KHÔNG thẻ nào được thêm."""
    # Tên từ (Cyrillic) có thể vượt 64 byte callback_data -> nút chỉ mang chỉ số
    context.user_data["lemma_choices"] = candidates
    rows = [
        [InlineKeyboardButton(f"✅ Thêm '{c}'", callback_data=f"lemma:{i}")]
        for i, c in enumerate(candidates)
    ]
    rows.append([InlineKeyboardButton("🚫 Hủy", callback_data="lemma:cancel")])
    await status_msg.edit_text(
        "\n".join(lines + ["Bấm từ đúng để thêm thẻ, hoặc hủy:"]),
        reply_markup=InlineKeyboardMarkup(rows),
    )


async def _add_with_dup_check(status_msg, word, context):
    """Dò trùng rồi thêm từ — luồng chung cho tin nhắn gõ từ và nút xác nhận lemma."""
    clean_word = strip_accents_perfectly(word)
    duplicates = await asyncio.to_thread(find_duplicate_notes, clean_word)
    if duplicates:
        context.user_data["pending"] = {"word": word, "dups": duplicates, "sel": 0}
        dup_text, keyboard = _duplicate_text_and_keyboard(context.user_data["pending"])
        await status_msg.edit_text(dup_text, reply_markup=keyboard)
        return
    await _do_add(status_msg, word, _current_deck(context), is_forced=False, context=context)


def _duplicate_text_and_keyboard(pending):
    """Từ đã có thẻ -> TRA TỪ ĐIỂN: đọc nguyên nội dung thẻ cũ ra (nghĩa, từ loại,
    chủ đề, 3 ví dụ, audio, trạng thái học) thay vì chỉ báo 'bị trùng'. Nút bấm cũ
    (chuyển deck / xóa / thêm trùng) vẫn giữ nguyên bên dưới."""
    dups = pending["dups"]
    sel = pending["sel"]
    card_info = note_to_card_info(dups[sel])
    text = format_dictionary_entry(card_info, index=sel, total=len(dups))

    rows = []
    if len(dups) > 1:
        # Nhiều note cùng từ: bấm để xem chi tiết note khác (bảng vẽ lại tại chỗ)
        rows.append([
            InlineKeyboardButton(
                f"{'👉 ' if i == sel else ''}Note [{i + 1}] {dups[i]['deck'].split('::')[-1]}",
                callback_data=f"sel:{i}",
            )
            for i in range(min(len(dups), 4))
        ])
    # Nút làm lại thẻ (cào + AI lại, giữ tiến trình học). Hai điều kiện:
    # - chỉ khi có ĐÚNG 1 note: redo_note() làm lại note MỚI NHẤT theo từ, nên khi
    #   có nhiều note trùng thì nút sẽ sửa nhầm cái đang xem -> thà đừng hiện;
    # - từ phải nằm gọn trong trần 64 byte của callback_data (còn /sua gõ tay).
    redo_data = f"fix:{card_info.get('clean_word', '')}"
    if len(dups) == 1 and card_info.get("clean_word") and len(redo_data.encode("utf-8")) <= 64:
        rows.append([InlineKeyboardButton("🔄 Làm lại thẻ này", callback_data=redo_data)])
    rows.append([
        InlineKeyboardButton("🚫 Xong", callback_data="act:huy"),
        InlineKeyboardButton("📦 Chuyển deck", callback_data="act:chuyen"),
    ])
    rows.append([
        InlineKeyboardButton("🗑 Xóa cũ + thêm mới", callback_data="act:xoa"),
        InlineKeyboardButton("➕ Vẫn thêm trùng", callback_data="act:trung"),
    ])
    return text, InlineKeyboardMarkup(rows)


# ==============================================================================
# --- 🆕 LỆNH /tumoi — xin 10 từ mới DỄ NHẤT còn thiếu theo chuẩn ТРКИ ---
# User chốt 23/08/2026: lấy THEO TRÌNH ĐỘ (A1 hết mới sang A2, rồi B1), KHÔNG gom
# theo chủ đề. Bấm ✅ mới thêm — giữ nguyên luật 19/07: bot không bao giờ tự thêm.
# Từ user loại bằng "bỏ 3 7" thì GHI LẠI và không đưa ra nữa.
#
# 🔴 Chỉ đọc CỘT TỪ + CỘT MỨC của `data/rosedu_muc.json`. Cột chủ đề của nguồn cố
# ý KHÔNG dùng — nhãn từng từ của họ sai có hệ thống (QD-37), chủ đề để AI xếp
# lúc tạo thẻ như mọi từ khác.
# ==============================================================================
SO_TU_MOI = 10
_BAN_CHUP = os.path.join(_GOC, "data", "rosedu_muc.json")
# Trạng thái CHẠY, không phải dữ liệu -> gốc repo + gitignore, đi đúng nếp
# `last_deck.json`: sống trên máy chạy bot, không lên git.
BO_QUA_FILE = os.path.join(_GOC, "tumoi_bo_qua.json")
TEN_MUC = {1: "A1", 2: "A2", 3: "B1", 4: "B2"}


def _doc_bo_qua():
    try:
        with open(BO_QUA_FILE, encoding="utf-8") as f:
            return set(json.load(f))
    except (OSError, ValueError):
        return set()


def _ghi_bo_qua(tu):
    """Thêm từ vào danh sách đã loại. Hỏng thì WARN chứ không ném: mất danh sách
    loại chỉ làm từ đó hiện lại, còn ném ra là giết cả luồng."""
    try:
        with open(BO_QUA_FILE, "w", encoding="utf-8") as f:
            json.dump(sorted(_doc_bo_qua() | set(tu)), f, ensure_ascii=False)
    except OSError as e:
        log_warn(f"khong ghi duoc {BO_QUA_FILE} ({e}) — tu vua loai se hien lai lan sau")


def chon_tu_moi(da_co, bo_qua, n=SO_TU_MOI, rng=random):
    """-> list (từ, mức) gồm n từ DỄ NHẤT còn thiếu. Hàm THUẦN (không đụng mạng,
    không đụng Anki) để test được: `da_co` và `bo_qua` là hai set người gọi đưa vào.

    Vét CẠN mức thấp rồi mới lên mức trên (A1 -> A2 -> B1 -> B2) — user chốt
    23/08/2026: học hết mức dễ đã.

    🔴 TRONG CÙNG MỘT MỨC thì LẤY NGẪU NHIÊN, không theo thứ tự nguồn. Nguồn xếp
    theo bảng chữ cái, nên giữ nguyên thứ tự là 10 từ đầu ra toàn chữ А
    (`а, август, автобус, автор, адрес...`) và phải bấm hết bảng chữ cái mới thấy
    từ chữ Б. Ngẫu nhiên trong mức cho mỗi lần bấm một nhúm đa dạng, mà vẫn giữ
    đúng luật "mức thấp trước"."""
    with open(_BAN_CHUP, encoding="utf-8") as f:
        kho = json.load(f)["tu"]
    con = {}
    for w, muc, _cats in kho:
        tran = strip_accents_perfectly(w).strip().lower()
        if tran and tran not in da_co and tran not in bo_qua:
            con.setdefault(muc, []).append(tran)
    ra = []
    for muc in sorted(con):
        con_muc = con[muc]
        rng.shuffle(con_muc)
        for tran in con_muc:
            ra.append((tran, muc))
            if len(ra) >= n:
                return ra
    return ra


def _tumoi_clear(user_data):
    user_data.pop("tumoi_words", None)
    user_data.pop("tumoi_msg", None)


def _tumoi_man_duyet(cap):
    """cap: list (từ, mức) -> (chữ, bàn phím). Hiện mức để user biết mình đang ở
    chặng nào; khung danh sách dùng chung với luồng quét ảnh."""
    dem = {}
    for _w, m in cap:
        dem[m] = dem.get(m, 0) + 1
    # Cả nhóm cùng một mức là chuyện thường (vét cạn mức thấp trước) -> nói gọn
    # "toàn A1"; chỉ liệt kê số lượng khi nhóm vắt qua hai mức.
    pho = (f"toàn {TEN_MUC.get(next(iter(dem)))}" if len(dem) == 1
           else " · ".join(f"{TEN_MUC.get(m, m)}: {k}" for m, k in sorted(dem.items())))
    return danh_sach_cho_duyet(
        [f"{w}  ({TEN_MUC.get(m, m)})" for w, m in cap],
        tieu_de=f"🆕 {len(cap)} từ mới chưa có thẻ — {pho}",
        cb_them="tumoiadd", cb_huy="tumoicancel",
        duoi=["ℹ️ Lấy từ Lexical Minimum chuẩn ТРКИ, mức thấp hết mới lên mức trên."])


async def cmd_tumoi(update, context):
    """/tumoi — xin SO_TU_MOI từ mới dễ nhất còn thiếu. KHÔNG tự thêm: user phải
    bấm ✅ (luật 19/07/2026)."""
    _reset_idle_timer(context, update.effective_chat.id)
    msg = await update.message.reply_text("⏳ Đang dò từ mới...")
    da_co = await asyncio.to_thread(get_known_words)
    if da_co is None:
        # None ≠ rỗng: AnkiConnect lỗi mà coi là "chưa có từ nào" thì đề nghị
        # thêm lại cả kho. Dừng hẳn, đừng đoán.
        await msg.edit_text("❌ Không đọc được kho thẻ (AnkiConnect lỗi?) — thử lại sau.")
        return
    cap = await asyncio.to_thread(chon_tu_moi, da_co, _doc_bo_qua())
    if not cap:
        await msg.edit_text("🎉 Hết từ trong danh sách ТРКИ — bạn đã có hết rồi.")
        return
    context.user_data["tumoi_words"] = cap
    text, kb = _tumoi_man_duyet(cap)
    await msg.edit_text(text, reply_markup=kb)
    context.user_data["tumoi_msg"] = msg


async def tumoi_exclude(update, context, text):
    """'bỏ 3 7' -> loại khỏi danh sách VÀ ghi nhớ để không đưa ra nữa."""
    idxs = {int(x) for x in re.findall(r"\d+", text)}
    cap = context.user_data["tumoi_words"]
    giu = [c for i, c in enumerate(cap, 1) if i not in idxs]
    _ghi_bo_qua([w for i, (w, _m) in enumerate(cap, 1) if i in idxs])
    if not giu:
        _tumoi_clear(context.user_data)
        await update.message.reply_text("🚫 Đã loại hết — hủy đợt này. Gõ /tumoi để xin nhóm khác.")
        return
    context.user_data["tumoi_words"] = giu
    text2, kb = _tumoi_man_duyet(giu)
    cu = context.user_data.get("tumoi_msg")
    try:
        await cu.edit_text(text2, reply_markup=kb)
        await update.message.reply_text(
            f"✂️ Đã loại {len(cap) - len(giu)} từ, sẽ KHÔNG hiện lại (danh sách ở tin trên).")
    except Exception:
        moi = await update.message.reply_text(text2, reply_markup=kb)
        context.user_data["tumoi_msg"] = moi


async def run_tumoi_add(context, chat_id, msg, cap):
    """Thêm loạt từ user đã duyệt. Việc thật ở `core.them_loat_tu`."""
    await them_loat_tu(
        context, chat_id, msg, [w for w, _m in cap],
        co="tumoi", stop_data="tumoistop", nhan="từ mới ТРКИ",
        con_lai="gõ /tumoi lần nữa để lấy nhóm mới (từ đã thêm sẽ tự bị lọc).")

# ==============================================================================
# --- SAU KHI THÊM MỘT ĐỘNG TỪ: dựng lại nhóm + mời thêm bạn thể (QD-39) ---
# CHỈ ở luồng gõ tay MỘT từ. Quét ảnh / `/tumoi` cố ý im lặng — user chốt 27/08:
# thêm loạt 30 từ mà hỏi 30 lần thì không ai bấm hết.
# ==============================================================================
def _dung_lai_nhom(acc):
    """Dựng lại ô `BangMay` cho mọi thẻ cùng nhóm với `acc`. -> số thẻ đã ghi.

    Phải chạy sau MỖI lần thêm động từ: thẻ mới biến nhóm 2 thẻ thành 3, mà mặt
    hai thẻ CŨ đã dựng từ trước nên vẫn in dòng "Cặp thể" cũ — không dựng lại thì
    nhóm mới chỉ hiện trên thẻ vừa thêm, sai IM LẶNG. Ghi theo `noteId` (QD-40).
    """
    nhom = nhom_dong_tu(lam_moi=True)
    cum = nhom.get(acc) or []
    ghi = 0
    for m in cum:
        moi = grammar.khoi_may(m["rec"], nhom=cum)
        if moi != m["may"]:
            update_note_fields(m["noteId"], {"BangMay": moi})
            ghi += 1
    return ghi


def ban_the_con_thieu(acc):
    """`(acc bạn thể, nghĩa Anh)` nếu động từ này thiếu bạn thể PHỔ BIẾN NHẤT.

    `partners[0]` chính là từ phổ biến nhất — đo 27/08 trên 38 động từ có nhiều
    hơn một bạn thể: khớp 38/38. Ô `aspectPartner` "chính thức" của OpenRussian
    lệch 9/38 mà ở cả 9 chỗ chọn từ HIẾM hơn ⇒ đừng đổi sang nó. Gợi ý ĐÚNG MỘT
    từ (user chốt 27/08).
    """
    nhom = nhom_dong_tu()
    cum = nhom.get(acc) or []
    minh = next((m for m in cum if m["acc"] == acc), None)
    if not minh:
        return None
    ban = next((nfc(p) for p in (minh["rec"].get("partners") or []) if p), "")
    if not ban or any(m["acc"] == ban for m in cum):
        return None
    return ban


async def _goi_y_ban_the(status_msg, context, card_info):
    """Thêm động từ xong -> dựng lại nhóm, rồi mời thêm bạn thể nếu còn thiếu."""
    try:
        acc = nfc(card_info.get("word"))
        await asyncio.to_thread(_dung_lai_nhom, acc)
        ban = await asyncio.to_thread(ban_the_con_thieu, acc)
    except Exception as e:                       # gợi ý hỏng KHÔNG được giết thẻ vừa thêm
        log_warn(f"goi y ban the ('{card_info.get('word')}') hong: {e}")
        return
    if not ban:
        return
    context.user_data["banthe_tu"] = ban
    text, kb = danh_sach_cho_duyet(
        [ban], tieu_de=f"🔗 '{card_info.get('word')}' còn thiếu bạn thể",
        cb_them="bantheadd", cb_huy="banthecancel",
        duoi=["ℹ️ Đây là nửa kia của cặp thể — biết một nửa thì không đặt câu được."])
    await status_msg.reply_text(text, reply_markup=kb)


async def run_banthe_add(context, chat_id, msg, tu):
    """User bấm ✅ -> thêm bạn thể, xong thì dựng lại nhóm lần nữa."""
    await them_loat_tu(context, chat_id, msg, [tu], co="banthe_running",
                       stop_data="banthestop", nhan="bạn thể")
    try:
        await asyncio.to_thread(_dung_lai_nhom, tu)
    except Exception as e:
        log_warn(f"dung lai nhom sau khi them '{tu}' hong: {e}")
