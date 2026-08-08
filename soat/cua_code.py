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
# S22 — CHIỀU IMPORT MỘT CHIỀU giữa các mảng
# ---------------------------------------------------------------------------
# Các mảng (`tgbot`, `grammar_forms`, `data/huongdan`) được phép import
# `anki_tools`; chiều ngược lại thì KHÔNG. Lý do user chốt 20/07/2026, và nó là
# ưu tiên tuyệt đối của cả repo: *"ít ảnh hưởng đến deck RUSSIAN đang chạy ngon"*
# — thứ đang chạy được thì không được để việc mới làm hỏng. Import ngược là
# đường để một thay đổi bên thẻ ngữ pháp giết chết dây chuyền kho đang chạy.
#
# 🔴 Gộp luôn ca `anki_tools/soat_nguphap.py` KHÔNG được import `grammar` (chốt
# 02/08/2026): cửa canh dữ liệu ngữ pháp phải đứng riêng để không đẻ vòng import
# với chính thứ nó đi soi. Cùng một họ bệnh nên cùng một cửa.
MANG_TREN = ("anki_tools",)
MANG_DUOI = ("tgbot", "grammar_forms")
CAM_RIENG = {"anki_tools/soat_nguphap.py": ("grammar",)}


def _ten_import(cay):
    """(tên module, dòng) cho mọi `import x` / `from x import ...`, kể cả
    import-trong-hàm — chỗ người ta hay lách khi muốn bẻ vòng."""
    for node in ast.walk(cay):
        if isinstance(node, ast.Import):
            for a in node.names:
                yield a.name, node.lineno
        elif isinstance(node, ast.ImportFrom):
            # 🔴 Phải sinh CẢ `module` LẪN `module.tên` — `from anki_tools import
            # grammar` mang tên thật ở `names`, không ở `module`. Bản đầu chỉ đọc
            # `module` nên đúng ca này lọt, test S22 bắt được ngay.
            for a in node.names:
                yield f"{node.module or ''}.{a.name}".strip("."), node.lineno
            yield (node.module or ""), node.lineno


def s22_chieu_import_mot_chieu():
    ra = []
    for p in khung.cac_file_py():
        src, cay = khung.doc_cay(p)
        if cay is None:
            continue
        dd = khung.duong_dan(p)
        for ten, dong in _ten_import(cay):
            goc = (ten or "").split(".")[0]
            if khung.goi_cua(p) in MANG_TREN and goc in MANG_DUOI:
                ra.append(PhatHien(dd, dong,
                                   f"IMPORT NGUOC: {khung.goi_cua(p)} khong duoc import "
                                   f"`{goc}` — mang duoi hong thi mang tren chet theo"))
            for file_cam, cam in CAM_RIENG.items():
                if dd == file_cam and any(x in cam for x in ten.split(".")):
                    ra.append(PhatHien(dd, dong,
                                       f"`{dd}` khong duoc import `{ten}` — cua soi du lieu "
                                       f"phai dung RIENG, khong deo vong import voi thu no soi"))
    return ra


# ---------------------------------------------------------------------------
# S23 — AnkiConnect KHÔNG được tự tải media hộ
# ---------------------------------------------------------------------------
def s23_media_phai_tu_tai():
    """Bot **tự tải bytes** rồi `storeMediaFile`, CẤM đưa `url` cho AnkiConnect.

    Vì sao (chốt 20/07/2026): nguồn audio trả 500 thì AnkiConnect ghi **nguyên
    câu lỗi** vào ô Audio. Thẻ hỏng khi đó nhận ra bằng *thiếu `[sound:]`* chứ
    KHÔNG phải bằng ô rỗng — tức hỏng im lặng, đúng loại user không tự thấy.
    Tự tải thì lỗi mạng nổ ngay tại chỗ, có `log_fail`.
    """
    ra = []
    for p in khung.cac_file_py(ke_ca_minh=False):
        src, cay = khung.doc_cay(p)
        if cay is None:
            continue
        for node in ast.walk(cay):
            # Lời gọi AnkiConnect là dict LỒNG: `action` ở ngoài, `url` nằm trong
            # `params` ⇒ phải soi từ dict NGOÀI CÙNG rồi lặn vào, chứ đòi cả hai
            # nằm chung một dict thì không ca thật nào khớp (test S23 bắt được).
            if not isinstance(node, ast.Dict) or not _co_chuoi(node, "storeMediaFile"):
                continue
            if any(isinstance(k, ast.Constant) and k.value == "url"
                   for con in ast.walk(node) if isinstance(con, ast.Dict)
                   for k in con.keys):
                ra.append(PhatHien(khung.duong_dan(p), node.lineno,
                                   "dua `url` cho storeMediaFile — AnkiConnect tai ho thi "
                                   "nguon loi 500 se bi GHI THANG vao o Audio"))
                break
    return ra


def _co_chuoi(node, can):
    return any(isinstance(x, ast.Constant) and x.value == can for x in ast.walk(node))


# ---------------------------------------------------------------------------
# S24 — model thẻ từ vựng chỉ được có ĐÚNG MỘT card template
# ---------------------------------------------------------------------------
def s24_mot_card_template():
    """Gợi ý (hint) dựng bằng **JS trong mặt trước thẻ**, KHÔNG thêm template.

    Vì sao (chốt 22/07/2026): chỉ card template mới nhân đôi số THẺ — thêm một
    template là tự nhân đôi cả bộ sưu tập, và Anki không hỏi lại lần nào. Bao
    nhiêu JS trên mặt thẻ cũng không đẻ ra thẻ mới.
    """
    ra = []
    for p in khung.cac_file_py(ke_ca_minh=False):
        src, cay = khung.doc_cay(p)
        if cay is None:
            continue
        for node in ast.walk(cay):
            # `createModel`: cardTemplates=[...]  ·  `updateModelTemplates`: templates={...}
            if isinstance(node, ast.keyword) and node.arg == "cardTemplates":
                n = len(node.value.elts) if isinstance(node.value, ast.List) else -1
            elif (isinstance(node, ast.Dict) and any(
                    isinstance(k, ast.Constant) and k.value in ("cardTemplates", "templates")
                    for k in node.keys)):
                v = next(v for k, v in zip(node.keys, node.values)
                         if isinstance(k, ast.Constant) and k.value in ("cardTemplates", "templates"))
                n = len(v.elts) if isinstance(v, ast.List) else (
                    len(v.keys) if isinstance(v, ast.Dict) else -1)
            else:
                continue
            if n > 1:
                ra.append(PhatHien(khung.duong_dan(p), node.lineno,
                                   f"khai {n} card template — moi template NHAN DOI so the "
                                   f"cua ca bo suu tap; goi y phai dung bang JS o mat truoc"))
    return ra


# ---------------------------------------------------------------------------
# S17 — nuốt lỗi im lặng
# ---------------------------------------------------------------------------
def s17_nuot_loi_im_lang():
    """`except ...: pass` trần trụi = lỗi biến mất không dấu vết, đúng kiểu hỏng
    mà repo này sợ nhất. Luật đã chốt 31/07: mọi `except` phải LOG, **hoặc** phải
    có comment nói vì sao được phép nuốt — nên chỗ nào có comment thì THA.

    VÀNG có ratchet (QD-24): 5 file nợ cũ im, chỗ thứ 9 mới ĐỎ. Sửa bớt rồi chạy
    `--chot` là mốc tụt xuống và không leo lại được."""
    ra = []
    for p in khung.cac_file_py():
        src, cay = khung.doc_cay(p)
        if cay is None:
            continue
        dong = src.splitlines()
        for node in ast.walk(cay):
            if not isinstance(node, ast.ExceptHandler):
                continue
            if len(node.body) != 1 or not isinstance(node.body[0], ast.Pass):
                continue
            # Có comment trong khoảng `except` → `pass` nghĩa là đã khai lý do.
            if any("#" in dong[i] for i in range(node.lineno - 1, node.body[0].lineno)
                   if i < len(dong)):
                continue
            ra.append(PhatHien(khung.duong_dan(p), node.lineno,
                               "`except ...: pass` tran trui — nuot loi im lang; "
                               "them log, hoac comment khai vi sao duoc phep nuot"))
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
