# ==============================================================================
# --- JOB NỀN — chạy ngầm 24/7, app.py bật lúc khởi động (lệnh user gõ: commands.py)
# ⚠️ QUY TẮC SỐNG CÒN của mọi job ở đây: thân vòng lặp PHẢI bọc try/except.
# Task asyncio mà ném exception thì CHẾT HẲN VÀ IM LẶNG — từ đó job không bao giờ
# chạy nữa cho tới khi restart bot, mà không có dấu hiệu nào báo ra. Bản đầu của
# _nightly_don dính đúng lỗi này: AnkiConnect lỗi một đêm là mất luôn job dọn
# inbox (phát hiện 21/07/2026 khi soi log sau deploy).
# Dùng vòng lặp asyncio tự viết thay vì JobQueue của PTB vì JobQueue đòi thêm gói
# apscheduler — không đáng cài thêm dependency lên VPS đang chạy ổn.
# ==============================================================================
import asyncio
import datetime

from anki_tools.config import TELEGRAM_USER_ID
from anki_tools.utils import log_warn
from anki_tools.soat_giaidoan import soat_va_va
from anki_tools.anki_client import sync_now
from anki_tools.backup import human_size, run_backup

from .alerts import alerter, sync_error_hint
from .commands import _don_report, run_don


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
    Lỗi thì log, CẢNH BÁO Telegram rồi nghỉ `cooldown` giây để không quay vòng
    điên cuồng.

    Job nền ném exception là luôn bất thường (khác lỗi sync có thể do mạng chớp),
    nên báo ngay từ lần đầu — after=1."""
    while True:
        try:
            await body()
        except asyncio.CancelledError:
            raise                       # tắt bot: phải để hủy task diễn ra bình thường
        except Exception as e:
            print(f"⚠️ Job '{name}' lỗi: {e!r} — bỏ qua nhịp này, job vẫn tiếp tục.")
            await alerter.problem(
                f"job:{name}",
                f"Job nền '{name}' đang lỗi:\n{e!r}\n\n"
                "Job vẫn chạy tiếp, nhưng nhịp này bị bỏ. "
                "Xem log: journalctl -u anki-bot -n 50",
                after=1,
            )
            await asyncio.sleep(cooldown)


async def _nightly_don(app):
    """3h sáng mỗi ngày tự chạy đúng cái /don gộp — LƯỚI AN TOÀN phòng khi user
    quên gõ tay. Chỉ nhắn Telegram khi CÓ thẻ được chuyển; đêm không có gì thì
    im lặng, đừng đánh thức user vì một tin nhắn rỗng."""
    async def once():
        await _sleep_until(3, 0)
        res = await asyncio.to_thread(run_don)
        # Bất thường thì báo BẤT KỂ có thẻ nào được chuyển hay không.
        # 🔴 `chua_gui` phải có trong điều kiện này: bản cũ chỉ xét sync KÉO VỀ, nên
        # đêm 06/08 việc dọn nằm lại VPS 7 tiếng mà KHÔNG một tiếng còi nào — user
        # bấm sync trên iPhone cả buổi sáng. (QD-34)
        if res["error"] or not res["sync_in"] or res["chua_gui"]:
            await alerter.problem(
                "don dem",
                "Job dọn 3h sáng chạy không trọn:\n"
                + (f"• {res['error']}\n" if res["error"] else "")
                + ("• sync kéo về thất bại → dọn trên dữ liệu cũ\n" if not res["sync_in"] else "")
                + (f"• {res['chua_gui']} thứ dọn xong VẪN NẰM TRÊN VPS, AnkiWeb chưa "
                   "nhận → iPhone kéo về không thấy gì đổi.\n"
                   "  👉 Mở Anki trên laptop bấm Sync một lần là nó đi.\n"
                   if res["chua_gui"] else ""),
                after=1,
            )
        else:
            await alerter.ok("don dem", "Job dọn 3h sáng")
        if res["promoted"] or res["total"]:
            try:
                await app.bot.send_message(TELEGRAM_USER_ID, "🌙 " + _don_report(res))
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


async def _soat_giai_doan():
    """Bám ĐUÔI nhịp sync: vừa kéo AnkiWeb về xong thì soi ngay thẻ hiện sai mặt.

    Vì sao đặt ở ĐÂY chứ không phải job riêng (QD-17): ① nhịp 30′ có sẵn, không
    đẻ job mới; ② ghi hàng loạt lên note đòi phải kéo về TRƯỚC (QD-16) — đứng
    ngay sau `sync_now()` thành công là tự thoả, khỏi sync lần hai; ③ sync HỎNG
    thì cố ý KHÔNG soát: dữ liệu đang cũ, vá trên bản cũ chính là cơ chế đã đẻ ra
    sự cố 31/07.

    Sạch thì im lặng tuyệt đối — cửa canh nói mỗi 30 phút là user tắt thông báo,
    và lần hỏng THẬT sau đó không ai thấy (nguyên tắc thiết kế của alerts.py)."""
    try:
        n, bao_cao = await asyncio.to_thread(soat_va_va, True, True)
    except Exception as e:
        # Không để cửa canh làm chết nhịp sync — sync quan trọng hơn hẳn.
        log_warn(f"Soát giai đoạn lỗi: {e!r}")
        await alerter.problem("soat giai doan",
                              f"Cửa canh thẻ sai mặt đang lỗi:\n{e!r}", after=2)
        return
    await alerter.ok("soat giai doan", "Cửa canh thẻ sai mặt")
    if n:
        await alerter.problem("the sai mat", f"🔄 {bao_cao}", after=1)


async def _periodic_sync():
    """Sync hai chiều mỗi PERIODIC_SYNC_MINUTES phút. Im lặng khi thành công.

    Hỏng thì CẢNH BÁO Telegram — nhưng chỉ sau 2 nhịp liên tiếp (~1 tiếng), vì
    một nhịp lỗi thường chỉ là mạng chớp. Đây chính là lỗ hổng đã để VPS kẹt
    "Sync status 2" suốt hai ngày mà không ai biết (25-26/07/2026)."""
    async def once():
        await asyncio.sleep(PERIODIC_SYNC_MINUTES * 60)
        ok, err = await asyncio.to_thread(sync_now)
        if ok:
            await alerter.ok("sync", "Sync AnkiWeb")
            await _soat_giai_doan()
        else:
            print("⚠️ Sync định kỳ thất bại (sẽ thử lại ở nhịp sau).")
            await alerter.problem(
                "sync",
                f"SYNC ANKIWEB ĐANG HỎNG.\n\n{err[:300]}\n\n👉 {sync_error_hint(err)}",
            )

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
            await alerter.ok("backup dem", "Backup đêm")
            return
        # Backup hỏng là LUÔN bất thường (after=1): lúc đó kho đang không có bản
        # sao lưu mới, mà backup chính là thứ cứu được khi full sync nhầm chiều.
        await alerter.problem(
            "backup dem",
            "BACKUP ĐÊM THẤT BẠI — kho Anki đang KHÔNG có bản sao lưu mới.\n"
            + "; ".join(result.get("errors", []))[:300],
            after=1,
        )

    await _guard("backup dem", once)
