# -*- coding: utf-8 -*-
"""S1–S8 — các cửa soi CẤU TRÚC CODE (và một cửa soi tài liệu tự khai: S8).
Mỗi hàm trả về danh sách `PhatHien`; riêng S8 trả `None` nghĩa là "chưa bật".
"""
import ast
import json
import re

from . import khung
from .khung import PhatHien

# Điểm vào sống ở gốc (L2) — ĐÚNG BA FILE (QD-02). Script vận hành: `scripts/`.
# 🔴 Thêm tên vào đây là NỚI LUẬT — phải có lý do trong QUYETDINH.md trước.
GOC_HOP_LE = {"bot.py", "main.py", "soatkientruc.py"}

HTML_DAC_TRUNG = ("example-toggle", "meaning-list")


# ---------------------------------------------------------------------------
# S1 — cửa lậu tới AnkiConnect
# ---------------------------------------------------------------------------
def s1_cong_anki():
    """L1: AnkiConnect đi qua MỘT cửa — `anki_tools/config.py` định nghĩa
    `ANKI_CONNECT_URL` là cửa thật; nợ cũ nằm trong baseline."""
    ra = []
    for p in khung.cac_file_py(ke_ca_minh=False):
        src, cay = khung.doc_cay(p)
        if cay is None:
            continue
        for chuoi, dong in khung.chuoi_trong_cay(cay):
            if "8765" in chuoi:
                ra.append(PhatHien(khung.duong_dan(p), dong,
                                   f"tro thang toi cong AnkiConnect: {chuoi!r}"))
                break
    return ra


# ---------------------------------------------------------------------------
# S2 — gọi tên private XUYÊN GÓI
# ---------------------------------------------------------------------------
def s2_private_xuyen_goi():
    """Private trong CÙNG gói là chuyện nội bộ, hợp lệ. Chỉ bắt khi một gói thò
    tay vào ruột gói khác — đó là chỗ sẽ gãy khi gói kia được dọn."""
    ra = []
    for p in khung.cac_file_py():
        # `tests/` được phép thò tay vào ruột — kiểm nội bộ chính là VIỆC của test.
        if khung.duong_dan(p).startswith("tests/"):
            continue
        src, cay = khung.doc_cay(p)
        if cay is None:
            continue
        goi = khung.goi_cua(p)
        # tên đang dùng -> gói của module đó. `import congcu` (chèn sys.path) không
        # thuộc gói nào -> "" ⇒ KHÁC mọi gói, vẫn bị soi — đúng chủ đích.
        goi_cua_ten = {}

        for node in ast.walk(cay):
            # `import anki_tools.grammar as grammar` / `from anki_tools import grammar`
            if isinstance(node, ast.Import):
                for a in node.names:
                    ten = (a.asname or a.name).split(".")[0]
                    goi_cua_ten[ten] = a.name.split(".")[0] if a.asname else ten
            elif isinstance(node, ast.ImportFrom):
                if node.level > 0:                 # import tương đối = cùng gói
                    for a in node.names:
                        goi_cua_ten[a.asname or a.name] = goi
                elif node.module:
                    for a in node.names:
                        goi_cua_ten[a.asname or a.name] = node.module.split(".")[0]

        for node in ast.walk(cay):
            # dạng 1: from <goi khac>.<mod> import _ten
            if isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
                if node.module.split(".")[0] == goi:
                    continue                      # cùng gói -> bỏ qua
                for a in node.names:
                    if a.name.startswith("_"):
                        ra.append(PhatHien(
                            f"{khung.duong_dan(p)}|{a.name}", node.lineno,
                            f"import ten private xuyen goi: {node.module}.{a.name}"))
            # dạng 2: <module>._ten  (vd grammar._cache)
            elif isinstance(node, ast.Attribute) and node.attr.startswith("_"):
                val = node.value
                if isinstance(val, ast.Name) and val.id in goi_cua_ten:
                    if goi_cua_ten[val.id] == goi:
                        continue                   # cùng gói -> nội bộ, hợp lệ
                    ra.append(PhatHien(
                        f"{khung.duong_dan(p)}|{val.id}.{node.attr}", node.lineno,
                        f"goi ten private xuyen goi: {val.id}.{node.attr}"))
    return ra


# ---------------------------------------------------------------------------
# S3 — tgbot: flow import ngang flow
# ---------------------------------------------------------------------------
def s3_tgbot_tang():
    """Mô hình tầng: core <- flows <- dispatch <- app. Flow gọi flow là bắc cầu
    ngang, làm hai màn hình dính nhau — sửa một cái là cái kia đổi theo âm thầm."""
    ra = []
    for p in khung.cac_file_py():
        if khung.goi_cua(p) != "tgbot" or not p.name.startswith("flow_"):
            continue
        src, cay = khung.doc_cay(p)
        if cay is None:
            continue
        for node in ast.walk(cay):
            if isinstance(node, ast.ImportFrom) and node.module:
                if node.module.startswith("flow_") and node.module != p.stem:
                    ra.append(PhatHien(
                        f"{khung.duong_dan(p)}|{node.module}", node.lineno,
                        f"flow import ngang flow: {p.stem} -> {node.module}"))
    return ra


# ---------------------------------------------------------------------------
# S4 — MIEN_TRU phải chỉ có MỘT nơi
# ---------------------------------------------------------------------------
def s4_mientru_mot_noi():
    """Hai bản `MIEN_TRU` lệch nhau từng làm `kiemtra.py` kêu oan 4 từ đúng chính
    tả (G0 gộp về `data/huongdan/mientru.py`). MỘT nơi là cửa; nơi thứ HAI là ĐỎ."""
    noi = []
    for p in khung.cac_file_py():
        if not khung.duong_dan(p).startswith("data/huongdan/"):
            continue
        src, cay = khung.doc_cay(p)
        if cay is None:
            continue
        for node in cay.body:
            if isinstance(node, ast.Assign):
                for t in node.targets:
                    if isinstance(t, ast.Name) and t.id == "MIEN_TRU":
                        noi.append(PhatHien(khung.duong_dan(p), node.lineno,
                                            "dinh nghia MIEN_TRU"))
    if len(noi) <= 1:
        return []                                  # đúng thiết kế: một cửa duy nhất
    return noi


# ---------------------------------------------------------------------------
# S5 — HTML thẻ dựng ngoài html_builder.py
# ---------------------------------------------------------------------------
def s5_html_ngoai_builder():
    """`html_builder.py` đáng lẽ là nơi duy nhất biết mặt thẻ trông thế nào.
    Nợ đã ghi SONO — VÀNG, chỉ chặn không cho mọc thêm."""
    ra = []
    for p in khung.cac_file_py(ke_ca_minh=False):
        if p.name == "html_builder.py":
            continue
        src, cay = khung.doc_cay(p)
        if cay is None:
            continue
        for chuoi, dong in khung.chuoi_trong_cay(cay):
            hit = [h for h in HTML_DAC_TRUNG if h in chuoi]
            if hit:
                ra.append(PhatHien(f"{khung.duong_dan(p)}|{hit[0]}", dong,
                                   f"dung HTML the ngoai html_builder: {hit[0]}"))
    return ra


# ---------------------------------------------------------------------------
# S6 — thư mục gốc chỉ chứa điểm vào đang sống (L2)
# ---------------------------------------------------------------------------
def s6_goc_sach():
    ra = []
    for p in sorted(khung.GOC.glob("*.py")):
        if p.name not in GOC_HOP_LE:
            ra.append(PhatHien(p.name, 0, "file .py moi o thu muc goc (L2)"))
    return ra


# ---------------------------------------------------------------------------
# S7 — 12 file lô thế hệ 1 phải còn nguyên ngòi đã tháo
# ---------------------------------------------------------------------------
def s7_lo_da_khai_tu():
    """QD-03: chạy lại lô thế hệ 1 là XOÁ bảng chia thẻ thật, im lặng. Đo bằng
    ast: guard phải là CÂU LỆNH THỰC THI ĐẦU TIÊN (sau docstring), không đếm dòng."""
    ra = []
    for p in sorted((khung.GOC / "data" / "huongdan").glob("lo*.py")):
        src, cay = khung.doc_cay(p)
        if cay is None:
            ra.append(PhatHien(khung.duong_dan(p), 0, "khong doc/parse duoc de kiem guard"))
            continue
        than = list(cay.body)
        if than and isinstance(than[0], ast.Expr) and isinstance(than[0].value, ast.Constant) \
                and isinstance(than[0].value.value, str):
            than = than[1:]                        # bỏ docstring
        ok = False
        if than and isinstance(than[0], ast.Raise):
            for chuoi, _ in khung.chuoi_trong_cay(than[0]):
                if "KHAI TU" in chuoi:
                    ok = True
                    break
        if not ok:
            ra.append(PhatHien(khung.duong_dan(p), 1,
                               "THIEU guard KHAI TU o cau lenh dau tien (QD-03)"))
    return ra


# ---------------------------------------------------------------------------
# S8 — KIENTRUC.md có nói dối không
# ---------------------------------------------------------------------------
def s8_manifest():
    """Tài liệu nói dối thì máy chỉ mặt — đúng cơ chế đã giữ `CHUAN.md` sống.
    Chưa có `KIENTRUC.md` (G2 mới viết) thì mục này ngủ, KHÔNG kêu."""
    kt = khung.GOC / "KIENTRUC.md"
    if not kt.exists():
        return None                                # None = chưa bật
    try:
        noi_dung = kt.read_text(encoding="utf-8")
    except OSError:
        return [PhatHien("KIENTRUC.md", 0, "khong doc duoc")]

    khoi = re.search(r"```soat-manifest\s*\n(.*?)```", noi_dung, re.S)
    if not khoi:
        return [PhatHien("KIENTRUC.md", 0, "thieu khoi ```soat-manifest```")]
    try:
        man = json.loads(khoi.group(1))
    except json.JSONDecodeError as e:
        return [PhatHien("KIENTRUC.md", 0, f"khoi soat-manifest khong phai JSON hop le: {e}")]

    ra = []
    khai_goi = set(man.get("goi", []))
    that_goi = {d.name for d in khung.GOC.iterdir()
                if d.is_dir() and (d / "__init__.py").exists()
                and d.name not in khung.BO_QUA_THU_MUC}
    for g in sorted(khai_goi - that_goi):
        ra.append(PhatHien(f"KIENTRUC.md|goi:{g}", 0, f"manifest khai goi '{g}' nhung khong co that"))
    for g in sorted(that_goi - khai_goi):
        ra.append(PhatHien(f"KIENTRUC.md|goi:{g}", 0, f"goi '{g}' co that nhung manifest khong khai"))

    for ten in man.get("diem_vao", []):
        if not (khung.GOC / ten).exists():
            ra.append(PhatHien(f"KIENTRUC.md|diem_vao:{ten}", 0,
                               f"manifest khai diem vao '{ten}' nhung file khong ton tai"))
    for ten in man.get("du_lieu_chung", []):
        if not (khung.GOC / ten).exists():
            ra.append(PhatHien(f"KIENTRUC.md|du_lieu:{ten}", 0,
                               f"manifest khai du lieu chung '{ten}' nhung khong ton tai"))
    return ra
