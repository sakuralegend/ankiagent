# ==============================================================================
# --- SAO LƯU COLLECTION TRÊN VPS ---
# Vì sao cần: cái nguy hiểm nhất với Anki KHÔNG phải quên sync, mà là một lần
# full sync chọn nhầm chiều — nó ghi đè cả bản trên AnkiWeb, mất sạch không lùi
# lại được. Có file backup theo ngày thì sai kiểu gì cũng phục hồi được.
#
# Cách làm: gọi AnkiConnect exportPackage cho TỪNG deck gốc (kèm includeSched
# nên giữ nguyên lịch ôn). CỐ Ý không đụng thẳng file collection.anki2: bot chạy
# trên host còn Anki chạy trong container, đường dẫn hai bên khác nhau — đi qua
# HTTP thì không phụ thuộc bố cục thư mục, chạy được ở mọi nơi.
#
# ⚠️ exportPackage KHÔNG nhận deck rỗng để xuất cả collection (đã thử: trả False),
# nên phải liệt kê deck gốc rồi xuất từng cái. Xuất deck cha là gồm cả deck con.
# ==============================================================================
import os
import re
import shutil
from datetime import datetime

import requests

from .config import ANKI_CONNECT_URL
from .utils import log_fail, log_warn

_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Thư mục chứa backup khi Anki chạy TRỰC TIẾP trên máy (PC ở nhà).
BACKUP_DIR = os.environ.get("BACKUP_DIR", os.path.join(_PROJECT_ROOT, "backups"))

# Số bản giữ lại. 1 bản ~36MB (đã gồm audio) -> 7 bản ~250MB.
BACKUP_KEEP = int(os.environ.get("BACKUP_KEEP", "7"))

# --- ⚠️ CHUYỆN ĐƯỜNG DẪN KHI ANKI CHẠY TRONG DOCKER (trên VPS) ---------------
# exportPackage bảo ANKI tự ghi file, nên đường dẫn ta đưa được hiểu THEO GÓC
# NHÌN CỦA ANKI. Trên VPS, Anki nằm trong container nên nó KHÔNG thấy
# /root/ankiagent/backups của host -> ghi vào đó là "Permission denied"
# (đã dính đúng lỗi này 21/07/2026, phát hiện nhờ chạy thử trên VPS).
# docker-compose mount:  <project>/anki-data  (host)  ->  /data  (container)
# nên phải bảo Anki ghi vào /data/backups, còn bot đọc/dọn ở <project>/anki-data/backups.
CONTAINER_DATA_ROOT = os.environ.get("ANKI_CONTAINER_DATA", "/data")
ANKI_DATA_HOST_DIR = os.environ.get(
    "ANKI_DATA_HOST_DIR", os.path.join(_PROJECT_ROOT, "anki-data")
)


def _call(action, timeout=300, **params):
    res = requests.post(ANKI_CONNECT_URL,
                        json={"action": action, "version": 6, "params": params},
                        timeout=timeout)
    out = res.json()
    if out.get("error"):
        raise RuntimeError(f"{action}: {out['error']}")
    return out.get("result")


def _safe_name(deck_name):
    """Tên deck -> tên file an toàn (deck có thể chứa ::, dấu cách, tiếng Việt)."""
    return re.sub(r'[<>:"/\\|?*]', "_", deck_name).strip() or "deck"


def top_level_decks():
    """Danh sách deck GỐC (xuất deck cha là gồm cả deck con)."""
    return sorted({d.split("::")[0] for d in (_call("deckNames", timeout=30) or [])})


def resolve_dirs():
    """Trả về (thư mục ANKI ghi vào, thư mục BOT đọc ra) — hai cái này KHÁC nhau
    khi Anki chạy trong Docker. Tự nhận biết bằng cách hỏi Anki thư mục media của
    nó nằm đâu: nằm dưới /data nghĩa là đang ở trong container.
    Không hỏi được (Anki lỗi) thì coi như chạy trực tiếp — an toàn cho PC ở nhà."""
    try:
        media = _call("getMediaDirPath", timeout=30) or ""
    except Exception:
        media = ""
    if media.replace("\\", "/").startswith(CONTAINER_DATA_ROOT.rstrip("/") + "/"):
        return (f"{CONTAINER_DATA_ROOT.rstrip('/')}/backups",
                os.path.join(ANKI_DATA_HOST_DIR, "backups"))
    return BACKUP_DIR, BACKUP_DIR


def _makedirs_shared(path):
    """Tạo thư mục mà TIẾN TRÌNH ANKI cũng ghi được.

    ⚠️ Trên VPS, bot chạy bằng root (host) còn Anki trong container chạy bằng
    uid 1000 (anki). Thư mục root tạo mặc định là 755 root:root -> Anki KHÔNG ghi
    nổi, exportPackage trả "Permission denied" (đã dính 21/07/2026). Nên phải nới
    quyền y như cách VPS_SETUP.md bảo làm với chính anki-data (chmod 777).
    An toàn: cả thư mục nằm trong anki-data vốn đã 777, và VPS chỉ có 1 người dùng,
    mọi cổng đều bind 127.0.0.1. Trên Windows chmod không có tác dụng -> bỏ qua.
    """
    os.makedirs(path, exist_ok=True)
    try:
        os.chmod(path, 0o777)
    except OSError:
        pass


def create_backup(base_dir=None):
    """Tạo 1 bản backup vào thư mục con theo thời điểm.
    Trả về dict {"path", "bytes", "decks", "errors"} — errors rỗng là trọn vẹn."""
    anki_base, host_base = resolve_dirs()
    if base_dir:                      # gọi tay với thư mục chỉ định (chạy trực tiếp)
        anki_base = host_base = base_dir
    stamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    out_dir = os.path.join(host_base, stamp)         # bot ghi/đọc phía host
    anki_dir = f"{anki_base.rstrip('/')}/{stamp}"    # Anki ghi phía nó (POSIX)
    _makedirs_shared(host_base)       # thư mục cha cũng phải mở, tạo lần đầu là root
    _makedirs_shared(out_dir)

    decks, errors, total = [], [], 0
    for deck in top_level_decks():
        filename = f"{_safe_name(deck)}.apkg"
        try:
            # Đường dẫn đưa cho Anki phải theo GÓC NHÌN CỦA ANKI, không phải của bot
            ok = _call("exportPackage", deck=deck,
                       path=f"{anki_dir}/{filename}", includeSched=True)
            host_path = os.path.join(out_dir, filename)
            if not ok or not os.path.exists(host_path):
                errors.append(f"{deck}: exportPackage trả về {ok}")
                continue
            size = os.path.getsize(host_path)
            total += size
            decks.append({"deck": deck, "bytes": size})
        except Exception as e:
            errors.append(f"{deck}: {e}")

    # Không xuất được gì -> dọn thư mục rỗng cho khỏi rác
    if not decks:
        shutil.rmtree(out_dir, ignore_errors=True)
        return {"path": "", "bytes": 0, "decks": [], "errors": errors or ["không có deck nào"]}

    return {"path": out_dir, "bytes": total, "decks": decks, "errors": errors}


def rotate(keep=BACKUP_KEEP, base_dir=None):
    """Xóa các bản backup cũ, chỉ giữ `keep` bản mới nhất. Trả về số bản đã xóa."""
    base_dir = base_dir or resolve_dirs()[1]
    try:
        entries = sorted(
            d for d in os.listdir(base_dir)
            if os.path.isdir(os.path.join(base_dir, d))
        )
    except FileNotFoundError:
        return 0
    removed = 0
    for name in entries[:-keep] if keep > 0 else []:
        shutil.rmtree(os.path.join(base_dir, name), ignore_errors=True)
        removed += 1
    return removed


def list_backups(base_dir=None):
    """Các bản backup đang có: list (tên, tổng bytes), mới nhất ở CUỐI."""
    base_dir = base_dir or resolve_dirs()[1]
    out = []
    try:
        names = sorted(d for d in os.listdir(base_dir)
                       if os.path.isdir(os.path.join(base_dir, d)))
    except FileNotFoundError:
        return out
    for name in names:
        folder = os.path.join(base_dir, name)
        size = sum(os.path.getsize(os.path.join(folder, f))
                   for f in os.listdir(folder)
                   if os.path.isfile(os.path.join(folder, f)))
        out.append((name, size))
    return out


def human_size(num_bytes):
    for unit in ("B", "KB", "MB", "GB"):
        if num_bytes < 1024 or unit == "GB":
            return f"{num_bytes:.0f} {unit}" if unit != "GB" else f"{num_bytes:.1f} GB"
        num_bytes /= 1024
    return f"{num_bytes:.1f} GB"


def run_backup(keep=BACKUP_KEEP):
    """Tạo backup + dọn bản cũ. Trả về (result_dict, số bản đã xóa)."""
    result = create_backup()
    if result["errors"]:
        log_warn(f"Backup có lỗi: {'; '.join(result['errors'][:3])}")
    if not result["path"]:
        log_fail("Backup THẤT BẠI — không xuất được deck nào.")
        return result, 0
    removed = rotate(keep)
    return result, removed


if __name__ == "__main__":
    res, removed = run_backup()
    if res["path"]:
        print(f"💾 Đã backup {len(res['decks'])} deck ({human_size(res['bytes'])}) "
              f"-> {res['path']}")
        for d in res["decks"]:
            print(f"   {d['deck']}: {human_size(d['bytes'])}")
        if removed:
            print(f"🧹 Đã xóa {removed} bản cũ (giữ {BACKUP_KEEP} bản gần nhất).")
    else:
        print("❌ Backup thất bại: " + "; ".join(res["errors"]))
