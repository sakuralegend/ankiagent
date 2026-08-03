# -*- coding: utf-8 -*-
"""Lõi DÙNG CHUNG của bộ công cụ soạn kho — tách từ congcu.py (03/08/2026, QD-18).

Chứa thứ mà cả lệnh soát offline (soatlo.py) lẫn lệnh đụng Anki (congcu.py) cùng
cần: khoá chữ, hàng đợi, đọc file lô, nối bảng chia, khối từ điển in cho agent,
dấu đạt chuẩn. File này KHÔNG đụng Anki — cửa AnkiConnect (`ac`) ở congcu.py.
"""
import glob
import importlib.util
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(HERE, ".."))
from anki_tools import grammar                                    # noqa: E402

HANGDOI = os.path.join(HERE, "hangdoi.json")
TUDIEN = os.path.join(HERE, "tudien.json")
NOUNS = os.path.join(HERE, "..", "..", "nouns.csv")
ACUTE = "́"
ZWSP = "​"


def bare(w):
    """Khoá TRA TỪ ĐIỂN trọng âm — gộp ё về е vì nouns.csv in ё thành е.
    ĐỪNG dùng để ghép với note Anki: xem `khoa_note`."""
    return w.replace(ACUTE, "").replace(ZWSP, "").replace("'", "").lower().replace("ё", "е")


def khoa_note(w):
    """Khoá GHÉP VỚI NOTE ANKI — GIỮ NGUYÊN ё.

    ё và е phân biệt những từ khác hẳn nhau: всё (mọi thứ) ≠ все (mọi người),
    нёбо (vòm miệng) ≠ небо (bầu trời). Dùng `bare` ở đây thì hai note gộp làm
    một khoá, và `nap` ghi nội dung của từ này đè lên thẻ của từ kia. Đã xảy ra
    thật 28/07: thẻ всё nhận nguyên ô Hướng dẫn của все.
    """
    return w.replace(ACUTE, "").replace(ZWSP, "").replace("'", "").lower()


# --------------------------------------------------- nối BẢNG CHIA vào ô Hướng dẫn
# Bảng do MÁY dựng từ từ điển, KHÔNG do agent soạn (240 dạng có trọng âm mỗi lô
# đi qua model là 240 cơ hội sai mà user không tự kiểm được — README §1).
# Vì vậy nó được nối vào lúc GHI, không nằm trong file lô.
BANG_RE = grammar.BANG_RE            # alias public (G4); dùng chung, đừng viết lại regex ở hai nơi


def gan_bang(html, word):
    """Gắn lại bảng chia — vỏ mỏng quanh `grammar.attach_table()`.

    Logic thật nằm ở `grammar.py` để luồng soạn lô, luồng tạo thẻ mới và luồng
    làm lại thẻ dùng CHUNG một hàm. Ba nơi tự nối bảng theo ba kiểu thì sớm muộn
    có nơi quên gỡ bảng cũ và thẻ mọc hai bảng chồng nhau.
    """
    return grammar.attach_table(html, grammar.get_cached(word))


def doc_hangdoi():
    return json.load(io.open(HANGDOI, encoding="utf-8"))


def ghi_hangdoi(q):
    io.open(HANGDOI, "w", encoding="utf-8").write(json.dumps(q, ensure_ascii=False, indent=1))


def nap_lo_da_soan(chi=None, lay_v=False):
    """Đọc mọi file kNN_*.py trong kho, trả {word: html} gộp.

    `chi` = danh sách id để chỉ đọc vài lô — dùng khi một lô tự soát mình.
    `lay_v` = trả thêm dict `V` (bản tiếng Việt sửa lại) của các lô đó.

    File lô có thể khai báo HAI dict:
      S = {từ: html ô Hướng dẫn}      — bắt buộc
      V = {từ: "nghĩa tiếng Việt"}    — tuỳ chọn, CHỈ những từ cần sửa
    """
    gop, nguon, vi = {}, {}, {}
    for path in sorted(glob.glob(os.path.join(HERE, "k[0-9][0-9]_*.py"))):
        if chi and os.path.basename(path)[:3] not in chi:
            continue
        spec = importlib.util.spec_from_file_location("lo_" + os.path.basename(path)[:3], path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        for w, html in getattr(mod, "S", {}).items():
            if w in gop:
                print(f"  !! TRUNG '{w}': {nguon[w]} va {os.path.basename(path)}")
            gop[w] = html
            nguon[w] = os.path.basename(path)
        vi.update(getattr(mod, "V", {}))
    return (gop, nguon, vi) if lay_v else (gop, nguon)


# ------------------------------------------- DỮ LIỆU TỪ ĐIỂN in kèm cho agent
# Hai khối dưới đây KHÔNG đụng thẻ — chúng chỉ đổi thứ agent NHÌN THẤY lúc soạn.
#
# 🔴 KHÔNG in HỌ TỪ ra đây — user chốt 29/07 SAU KHI ĐO, đừng thêm lại.
#
# Ý định ban đầu đúng: agent tự nghĩ từ nguyên đã sai thật hai lần
# (`о́блако`↔`во́лос`, `целова́ть`↔`цель`, git log quanh 28/07), nên đưa danh sách họ
# từ của từ điển ra để agent CHỌN thay vì ĐOÁN. Ba phép đo giết ý định đó:
#
#  ① Làm CỬA SOÁT thì không được. Trên 2 069 cụm in đậm ở mục "Họ hàng" của 301
#    thẻ đã soạn: bắt buộc phải có trong `family` thì kêu 65%, nới hai bước 59%,
#    lọc hai tầng chặt nhất vẫn 33% — gần hết chỗ kêu là họ hàng THẬT mà từ điển
#    xếp thiếu (`идти́` không có `похо́д`/`вход`, `знать` không có `знак`).
#    `family` là nguồn KHẲNG ĐỊNH, KHÔNG phải nguồn PHỦ ĐỊNH.
#  ② Làm nguồn THAM KHẢO cũng không xong: `groups[family]` (cùng gốc) và
#    `relateds` (nghĩa gần, KHÁC GỐC HẲN) bị `grammar._family()` gộp một rổ, nên
#    `ги́бкий` kéo theo `мя́гкий`/`бога́тый`, `о́блако` kéo theo `ту́ча`/`не́бо`.
#    Đưa cái rổ đó cho agent là công cụ TỰ ĐẺ RA đúng loại lỗi nó sinh ra để chặn.
#  ③ Tách hai khoá thì sạch, nhưng phải bóc lại. User chốt BỎ HẲN:
#    *"phần family này chỉ để AI tham khảo thôi"* → *"nếu nguy hiểm vậy thì thôi
#    bỏ đi"* → *"xoá để nó hoạt động như ban đầu, không động gì vào phần họ hàng
#    từ nữa"*.
#
# ⇒ Đã gỡ TẬN GỐC (v3, 29/07), không chỉ thôi in: `grammar.normalize()` không bóc
# `family` nữa · `xoa_family_khoi_cache.py` gỡ khoá khỏi cả 951 bản ghi (0,86 ->
# 0,37 MB) · `scripts/backfill_grammar_json.py --apply` ghi lại `GrammarJSON` 950 thẻ.
# **Không còn `rec["family"]` ở bất kỳ đâu.** Mục "Họ hàng" agent tự nghĩ, và
# KHÔNG có cửa soát nào chặn chỗ đó — README §2 dặn "không chắc thì bỏ mục đó".

TRAN_EN = 46          # cắt phần nghĩa Anh cho gọn một dòng
TRAN_IDIOM = 4


def _gon(s, n):
    s = re.sub(r"\s+", " ", (s or "")).strip()
    return s if len(s) <= n else s[:n - 1].rstrip() + "…"


def _dong_bat_thuong(rec):
    """Câu mô tả chỗ BẤT THƯỜNG của bảng chia (`grammar.analyze`).

    User chốt 29/07: *"đọc câu đó là hiểu toàn bộ bảng"*. Bảng chia do máy dựng
    nằm gấp trong `<details>`, nên phần duy nhất user đọc ngay là câu chú ý phía
    trên — mà chỉ agent viết được câu đó. Máy chỉ trỏ chỗ, KHÔNG viết hộ: các
    câu dưới đây là mô tả thô, đưa thẳng lên thẻ thì khô và dài.
    """
    flags = grammar.analyze(rec).get("flags") or []
    flags = [(ma, c) for ma, c in flags if ma not in ("khongbien",)]
    if not flags:
        return []
    return ["###   BAT THUONG trong bang chia (viet 1 cau chu y, DUNG chep nguyen):"] + \
           [f"###     - {c}" for _, c in flags]


def _dong_them(rec):
    """`usage` (ghi chú cách dùng người thật viết) + `idioms` (cụm cố định).

    Cào về 29/07 nhưng tới giờ chưa ai nhìn thấy. `idioms` đúng loại nội dung ô
    đỏ user chấm là hay nhất: bản mẫu `сожале́ние` có ô `к сожале́нию`.
    """
    ra = []
    if rec.get("usage"):
        # NGUYÊN VĂN từ điển, có mục là ghi chú nội bộ của người biên tập
        # (`быть`: "This page needs fixing…"). Không lọc được bằng máy — agent
        # đọc rồi tự bỏ, đừng chép mù.
        ra.append(f"###   CACH DUNG (tu dien ghi): {_gon(rec['usage'], 150)}")
    idi = rec.get("idioms") or []
    if idi:
        ra.append("###   CUM CO DINH:")
        for m in idi[:TRAN_IDIOM]:
            ra.append(f"###     {m['w']:24s} {_gon(m.get('en'), TRAN_EN)}".rstrip())
        if len(idi) > TRAN_IDIOM:
            ra.append(f"###     ... con {len(idi) - TRAN_IDIOM} cum")
    return ra


def khoi_nguphap(wc):
    """Toàn bộ phần từ điển in kèm một từ. Rỗng nếu chưa cào được từ đó."""
    rec = grammar.get_cached(wc)
    if not rec:
        return ["###   (KHONG CO du lieu ngu phap — chay cao_nguphap.py cho tu nay)"]
    return _dong_bat_thuong(rec) + _dong_them(rec)


# ==============================================================================
# --- DẤU ĐẠT CHUẨN: `chuan::<N>` ghi thẳng lên TAG của thẻ ---
#
# 🔴 Vì sao dấu phải mang SỐ HIỆU, không phải chỉ "đạt": nhãn `dat` cũ nằm trong
# `hangdoi.json` chỉ ghi "thẻ này đạt" mà không ghi **đạt theo chuẩn nào**. Chuẩn
# đổi bên dưới nó thì nhãn HẾT HẠN MÀ KHÔNG AI BIẾT — đo lại 29/07 thì 7/75 thẻ
# mang nhãn đó đã vỡ trần. Cả một phiên bị loạn vì chuyện này. User chốt: *"phải
# có cách đánh dấu từ nào đã đạt chuẩn để không bị loạn nữa"*.
#
# Vì sao dùng TAG chứ không phải field mới: thêm field là **schema mod** ⇒ Anki
# đòi full sync, mà [[vps-ket-sync-im-lang]] ghi rõ mỗi lần như vậy VPS kẹt im
# lặng. Tag thì sync thường, lại **tra được ngay trong app Anki** (`tag:chuan::3`)
# nên user tự kiểm được, không phải tin lời tôi.
#
# 📕 ĐỊNH NGHĨA TỪNG SỐ HIỆU NẰM Ở `data/huongdan/CHUAN.md` — con số ở đây vô
# nghĩa nếu không có file đó. Tóm tắt để khỏi phải mở:
#   v1  chuẩn dài (6–10 KB, không đếm ô đỏ)          — không thẻ nào được gắn
#   v2  §2b ngắn gọn: 1 màn hình iPhone + ≤2 ô đỏ    — không thẻ nào được gắn
#   v3  (29/07) v2 + BẮT BUỘC câu chú ý cho từ mà `tiep` in khối BAT THUONG,
#       + mục "Họ hàng" được phép vắng khi từ thật sự không có
#
# 🔴 ĐỔI CHUẨN THÌ LÀM ĐỦ BA BƯỚC (xem mục "Quy trình ĐỔI CHUẨN" trong CHUAN.md):
# ① thêm mục `## v<N+1>` vào CHUAN.md, ghi ĐỦ tiêu chuẩn chứ không chỉ phần đổi
# ② tăng số dưới đây  ③ hết — không phải đụng thẻ nào, mọi thẻ cũ tự thành
# "đạt chuẩn CŨ" và `dochuan.py` xếp chúng vào diện phải soạn lại. Đó chính là
# thứ đáng lẽ đã chặn được mớ lộn xộn hôm nay.
CHUAN_V = 3
TAG_CHUAN = "chuan"


def tag_chuan(v=None):
    return f"{TAG_CHUAN}::{CHUAN_V if v is None else v}"
