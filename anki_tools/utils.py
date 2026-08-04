# ==============================================================================
# --- TIỆN ÍCH XỬ LÝ CHỮ + LOG TỐI GIẢN ---
# Các hàm nhỏ, không phụ thuộc module khác, dùng chung ở khắp nơi trong project.
#
# NHẬT KÝ PHÂN MỨC (04/08/2026, trả nợ SONO.md). Vì sao KHÔNG dùng `logging` của
# thư viện chuẩn: bot chạy dưới systemd, mọi dòng `print` đã vào `journalctl` sẵn
# — thứ còn thiếu chỉ là (a) một MỨC để lọc và (b) một chỗ để tắt bớt tiếng ồn.
# Kéo `logging` vào là phải cấu hình handler/formatter ở cả bot lẫn 4 script chạy
# tay, đổi lấy đúng hai thứ trên. Bốn hàm dưới đây làm đủ, và giữ nguyên tên cũ
# nên không phải sửa một lời gọi nào đang có.
#
#     ANKI_LOG=debug|info|warn|fail   (mặc định `info`)
#
# Lọc theo mức chứ không theo module: bot này một tiến trình, cái người đọc
# `journalctl` cần là "chỉ xem cái hỏng", không phải "chỉ xem gói X".
# ==============================================================================
import os
import re

_MUC = {"debug": 10, "info": 20, "warn": 30, "fail": 40}
_NGUONG = _MUC.get((os.getenv("ANKI_LOG") or "info").strip().lower(), 20)


def _print_safe(msg):
    """print() nhưng không crash nếu console không hỗ trợ encode ký tự (vd cp1252 trên Windows)."""
    try:
        print(msg, flush=True)
    except UnicodeEncodeError:
        print(msg.encode("ascii", errors="replace").decode("ascii"), flush=True)


def _log(muc, dau, msg):
    """In một dòng nhật ký nếu mức đủ cao. Tiền tố mức đặt ĐẦU DÒNG để
    `journalctl -u anki-bot | grep FAIL` ra đúng thứ cần, không phải lọc bằng
    emoji (emoji vỡ trên nhiều terminal, mà grep emoji thì ai cũng gõ sai)."""
    if _MUC[muc] >= _NGUONG:
        _print_safe(f"[{muc.upper():<5}] {dau}{msg}")


def log_debug(msg):
    """Chi tiết chỉ cần khi đang truy lỗi — mặc định KHÔNG in."""
    _log("debug", "", msg)


def log_info(msg):
    _log("info", "", msg)


def log_warn(msg):
    _log("warn", "⚠️  ", msg)


def log_fail(msg):
    _log("fail", "❌ ", msg)


def ban_ma_dang_chay():
    """Mã commit đang chạy, dạng ngắn (`'a1b2c3d'`), hoặc `'?'` nếu không đọc được.

    Trả nợ `SONO.md` 04/08/2026: đã có lần **bot trên VPS chạy code cũ 3 ngày mà
    không gì báo** — deploy hụt thì mọi thứ vẫn "chạy bình thường", chỉ là chạy
    bản cũ. Không có cách nào phát hiện từ ngoài, vì bot không tự khai nó là bản
    nào. Khai ra thì đối chiếu với `git rev-parse --short HEAD` trên laptop là ra
    ngay trong hai giây.

    Đọc `.git/HEAD` bằng tay thay vì gọi `git`: trong container không chắc có
    `git`, và bung một tiến trình con chỉ để lấy 7 ký tự thì đắt hơn việc cần làm.
    """
    goc = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    try:
        with open(os.path.join(goc, ".git", "HEAD"), encoding="utf-8") as f:
            head = f.read().strip()
        if head.startswith("ref:"):
            with open(os.path.join(goc, ".git", head[4:].strip()), encoding="utf-8") as f:
                head = f.read().strip()
        return head[:7] or "?"
    except OSError:
        return "?"          # cây không phải repo git (bản chép tay lên VPS) — hợp lệ


def strip_accents_perfectly(text):
    return text.replace("\u0301", "").replace("'", "").lower()


def convert_stress_to_combining_accent(word):
    """Chuyển ' sau nguyên âm -> combining acute accent U+0301."""
    return re.sub(r"([а-яёА-ЯЁ])\'", lambda m: m.group(1) + "\u0301", word)


def hl_to_bracket(text):
    """Chuyển <hl>...</hl> thành [...] để hiển thị (dùng khi in ra terminal)."""
    return text.replace("<hl>", "[").replace("</hl>", "]")


def apply_hl(text):
    """Chuyển <hl>...</hl> thành <span class="hl">...</span> để hiển thị trong Anki."""
    if not text:
        return ""
    return text.replace("<hl>", '<span class="hl">').replace("</hl>", "</span>")
