# ==============================================================================
# --- KHỞI ĐỘNG BOT: chờ AnkiConnect, lắp handler, đăng ký menu lệnh, polling.
# Kiến trúc: long-polling (không cần mở port/domain/SSL). Mọi thao tác nặng
# (cào web, gọi AI, AnkiConnect) chạy qua asyncio.to_thread để không nghẽn bot.
# Logic thêm/sửa từ nằm ở anki_tools/pipeline.py - DÙNG CHUNG với main.py (CLI).
# ==============================================================================
import asyncio
import time

from telegram import Update, BotCommand
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
)

from anki_tools.config import TELEGRAM_BOT_TOKEN, TELEGRAM_USER_ID
from anki_tools.ai_client import check_claude_ready
from anki_tools.utils import ban_ma_dang_chay
from anki_tools.anki_client import check_anki_ready, setup_anki_environment, trigger_sync

from .commands import (
    cmd_backup,
    cmd_deck,
    cmd_don,
    cmd_menu,
    cmd_start,
    cmd_sync,
    cmd_thongke,
)
from .jobs import _nightly_backup, _nightly_don, _periodic_sync
from .alerts import alerter
from .flow_edit import cmd_sua, cmd_suadeck
from .flow_scan import on_photo
from .flow_special import cmd_dacbiet
from .dispatch import on_callback, on_word


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


# Giữ tham chiếu tới task nền: asyncio chỉ giữ weak reference, không giữ ở đây
# thì task có thể bị thu gom rác giữa chừng.
_BACKGROUND_TASKS = set()


def _spawn(coro):
    """Chạy 1 job nền. Dùng asyncio.create_task thay cho app.create_task: lúc
    _post_init chạy thì Application chưa "running" nên app.create_task in ra
    PTBUserWarning mỗi lần khởi động (3 job = 3 dòng rác trong log, dễ che lỗi
    thật). Vòng lặp job tự bọc try/except rồi (xem _guard ở jobs.py) nên
    không cần PTB theo dõi hộ."""
    task = asyncio.create_task(coro)
    _BACKGROUND_TASKS.add(task)
    task.add_done_callback(_BACKGROUND_TASKS.discard)
    return task


async def _post_init(app):
    """Đăng ký menu lệnh gốc của Telegram (nút '/' cạnh ô gõ chữ) + bật job nền."""
    # Gắn app cho bộ cảnh báo TRƯỚC khi bật job nền — job hỏng ngay nhịp đầu thì
    # vẫn phải nhắn được, chứ không rơi vào cảnh "chưa bind, bỏ tin".
    alerter.bind(app)
    _spawn(_nightly_don(app))       # 3h00 sáng: dọn inbox
    _spawn(_nightly_backup(app))    # 3h30 sáng: sao lưu + dọn bản cũ
    _spawn(_periodic_sync())        # 30 phút/lần: sync HAI CHIỀU
    # Danh sách "/" CỐ Ý chỉ 4 mục hay dùng (user chốt 20/07/2026: 9 lệnh làm
    # rối). Các lệnh còn lại (/sua /suadeck /thongke /don /sync) vẫn chạy khi gõ
    # tay, và có nút trong menu 🛠 — chỉ không chiếm chỗ trong bảng gợi ý.
    await app.bot.set_my_commands([
        BotCommand("menu", "Menu nút bấm"),
        BotCommand("dacbiet", "⭐ Thẻ ngữ pháp: số nhiều bất quy tắc"),
        BotCommand("deck", "Đổi bộ bài (bảng chọn nút)"),
        BotCommand("help", "Hướng dẫn"),
    ])


def main():
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_USER_ID:
        print("❌ Thiếu TELEGRAM_BOT_TOKEN hoặc TELEGRAM_USER_ID trong .env")
        return

    print(f"🤖 Bot Anki khởi động... (bản mã {ban_ma_dang_chay()})")

    if not wait_for_anki():
        print("❌ AnkiConnect không phản hồi sau 3 phút. Kiểm tra container anki (docker ps).")
        return
    print("✅ AnkiConnect sẵn sàng.")

    if check_claude_ready():
        print("✅ AI (Gemini) sẵn sàng.")
    else:
        print("⚠️ AI chưa phản hồi - bot vẫn chạy, sẽ thử lại khi có yêu cầu.")

    # ⚠️ THỨ TỰ QUAN TRỌNG: SYNC KÉO VỀ TRƯỚC, rồi mới đẩy template.
    # Bài học 27/07/2026: bản cũ làm ngược (setup rồi mới sync). Hôm đổi tên field
    # `Mnemonic` -> `HuongDan` trên laptop, VPS khởi động lại và đẩy template có
    # {{HuongDan}} vào collection CỦA NÓ vẫn còn tên cũ -> "Field 'HuongDan' not
    # found", template hỏng. Tệ hơn: lần đẩy hỏng đó vẫn chạm vào note type, làm
    # bản của VPS "mới hơn" bản laptop nên sync sau đó GIỮ BẢN CŨ — phải vào tận
    # nơi đổi tên tay mới gỡ được. Kéo về trước thì VPS luôn dựng template trên
    # đúng bộ field hiện hành.
    if trigger_sync():
        print("☁️ Sync kéo về: OK.")
    else:
        print("⚠️ Sync kéo về thất bại - template có thể dựng trên bộ field cũ.")

    setup_anki_environment()

    # Đẩy lên lần nữa để các thiết bị khác thấy template/CSS mới ngay.
    if trigger_sync():
        print("☁️ Sync đẩy lên: OK.")
    else:
        print("⚠️ Sync đẩy lên thất bại - sẽ sync lại ở thao tác đầu tiên.")

    # Trần chờ HTTP nới hẳn so với mặc định 5s: VPS (VN) tới api.telegram.org
    # ~230ms RTT, mạng chững một nhịp là dính telegram.error.TimedOut (đã gặp
    # 19/07/2026: gửi tin trạng thái quét ảnh chết ở 5s). media_write_timeout
    # cao nhất vì tải ảnh chụp trang sách là request nặng nhất.
    app = (
        Application.builder()
        .token(TELEGRAM_BOT_TOKEN)
        .connect_timeout(15)
        .read_timeout(30)
        .write_timeout(30)
        .media_write_timeout(60)
        .pool_timeout(15)
        .post_init(_post_init)
        .build()
    )
    only_me = filters.User(user_id=TELEGRAM_USER_ID)

    app.add_handler(CommandHandler(["start", "help"], cmd_start, filters=only_me))
    app.add_handler(CommandHandler("menu", cmd_menu, filters=only_me))
    app.add_handler(CommandHandler("deck", cmd_deck, filters=only_me))
    app.add_handler(CommandHandler("thongke", cmd_thongke, filters=only_me))
    app.add_handler(CommandHandler("don", cmd_don, filters=only_me))
    app.add_handler(CommandHandler("sync", cmd_sync, filters=only_me))
    app.add_handler(CommandHandler("sua", cmd_sua, filters=only_me))
    app.add_handler(CommandHandler("suadeck", cmd_suadeck, filters=only_me))
    app.add_handler(CommandHandler("dacbiet", cmd_dacbiet, filters=only_me))
    app.add_handler(CommandHandler("backup", cmd_backup, filters=only_me))
    app.add_handler(CallbackQueryHandler(on_callback))
    app.add_handler(MessageHandler(only_me & filters.PHOTO, on_photo))
    # Ảnh gửi dạng FILE (document): Telegram KHÔNG nén nên chữ nhỏ trong sách còn
    # nguyên nét -> AI đọc sót ít hơn hẳn ảnh thường (bị ép về ~1280px).
    app.add_handler(MessageHandler(only_me & filters.Document.IMAGE, on_photo))
    app.add_handler(MessageHandler(only_me & filters.TEXT & ~filters.COMMAND, on_word))

    print("🚀 Bot đang chạy (long polling). Mặc định 🤖 tự động: thẻ vào deck con theo chủ đề AI chọn.")
    app.run_polling(allowed_updates=Update.ALL_TYPES)
