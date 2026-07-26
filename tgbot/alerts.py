# ==============================================================================
# --- CẢNH BÁO BẤT THƯỜNG QUA TELEGRAM ---
# Vì sao có file này: từ 25 đến 26/07/2026 sync trên VPS hỏng liên tục ("Sync
# status 2" — AnkiWeb đòi full sync sau khi thêm field) mà KHÔNG AI BIẾT, vì
# trigger_sync chỉ log_warn ra journal rồi trả False. Bot vẫn "chạy bình thường"
# trong khi thực ra hai ngày liền không đẩy được gì lên AnkiWeb.
#
# ⚠️ NGUYÊN TẮC THIẾT KẾ: cảnh báo phải CÓ TIẾT CHẾ. Nhắn mỗi 30 phút suốt hai
# ngày thì user sẽ tắt thông báo của bot, và lần hỏng THẬT tiếp theo lại không
# ai thấy — tệ hơn cả không cảnh báo. Nên:
#   * bỏ qua lỗi thoáng qua (mạng chớp một nhịp) -> chỉ báo khi hỏng LIÊN TIẾP
#   * đang hỏng kéo dài thì nhắc lại THƯA (mặc định 6 tiếng/lần)
#   * hết hỏng thì báo MỘT tin "đã bình thường" rồi im
# ==============================================================================
import time

from anki_tools.config import TELEGRAM_USER_ID
from anki_tools.utils import log_warn


class Alerter:
    """Theo dõi trạng thái hỏng/khoẻ theo từng `key` (mỗi loại sự cố một key)."""

    def __init__(self):
        self._app = None
        self._state = {}      # key -> {"fails": int, "alerted_at": float | None}

    def bind(self, app):
        """Gắn Application của PTB. Gọi trong _post_init, trước khi job nền chạy."""
        self._app = app

    async def _send(self, text):
        if self._app is None:
            log_warn(f"Alerter chưa bind app, bỏ tin: {text[:80]}")
            return
        try:
            await self._app.bot.send_message(TELEGRAM_USER_ID, text)
        except Exception as e:
            # Không được để việc gửi cảnh báo làm chết job đang gọi nó.
            log_warn(f"Không gửi được cảnh báo Telegram: {e!r}")

    async def problem(self, key, text, after=2, repeat_hours=6):
        """Ghi nhận MỘT lần hỏng của `key`.

        after=2  -> phải hỏng 2 nhịp liên tiếp mới báo (lọc lỗi thoáng qua).
                    Đặt 1 cho loại sự cố mà một lần đã là bất thường (job crash).
        repeat_hours -> vẫn hỏng thì bao lâu nhắc lại một lần.
        """
        st = self._state.setdefault(key, {"fails": 0, "alerted_at": None})
        st["fails"] += 1
        if st["fails"] < after:
            return
        now = time.time()
        if st["alerted_at"] and now - st["alerted_at"] < repeat_hours * 3600:
            return
        first = st["alerted_at"] is None
        st["alerted_at"] = now
        prefix = "🚨" if first else "🚨 (vẫn chưa xong)"
        await self._send(f"{prefix} {text}\n\n(hỏng {st['fails']} nhịp liên tiếp)")

    async def ok(self, key, text=None):
        """Ghi nhận `key` đang bình thường. Chỉ nhắn nếu TRƯỚC ĐÓ đã báo hỏng —
        không thì mỗi nhịp khoẻ lại spam một tin."""
        st = self._state.get(key)
        if not st:
            return
        had_alerted = st["alerted_at"] is not None
        self._state.pop(key, None)
        if had_alerted:
            await self._send(f"✅ {text or key} đã bình thường trở lại.")


# Một thể hiện dùng chung cho cả bot.
alerter = Alerter()


def sync_error_hint(err):
    """Dịch lỗi sync thô của Anki thành việc CẦN LÀM. Lỗi hay gặp nhất là
    'Sync status 2' — nó không tự khỏi, phải có người vào bấm tay."""
    e = (err or "").lower()
    if "status 2" in e or "fullsync" in e or "full sync" in e:
        return ("AnkiWeb ĐÒI FULL SYNC (thường do vừa đổi schema: thêm/xoá field, "
                "đổi note type). Sync sẽ hỏng MÃI cho tới khi xử lý tay:\n"
                "1. Máy nào có bản ĐÚNG NHẤT → Anki → Sync → Upload to AnkiWeb\n"
                "2. VNC vào VPS → Anki → Sync → Download from AnkiWeb\n"
                "3. iPhone → Sync → Download from AnkiWeb\n"
                "Nhớ /backup trước.")
    if "auth" in e or "login" in e or "401" in e:
        return "Anki trên VPS mất đăng nhập AnkiWeb → VNC vào đăng nhập lại."
    if "connect" in e or "timeout" in e or "refused" in e:
        return "Không gọi được AnkiConnect → kiểm tra container: docker ps / docker logs anki"
    return "Xem log trên VPS: journalctl -u anki-bot -n 50"
