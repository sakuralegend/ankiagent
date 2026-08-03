# -*- coding: utf-8 -*-
"""KHUNG dùng chung của mọi cửa soát: thư mục gốc, kiểu `PhatHien`, đọc cây AST,
liệt kê file. Không chứa cửa nào — cửa nằm ở `cua_*.py`.

🔴 KHÔNG import module nào của dự án (QD-02). Chỉ stdlib: `pathlib` + `ast`
(phân tích tĩnh, KHÔNG thực thi).

🔴 `GOC` là biến MODULE, mọi cửa phải đọc `khung.GOC` lúc CHẠY chứ đừng
`from .khung import GOC` — bản sao lúc import sẽ không đổi theo `dat_goc()`, và
test sẽ âm thầm soi repo THẬT thay vì repo giả (xanh hết mà không kiểm gì).
"""
import ast
from pathlib import Path

GOC = Path(__file__).resolve().parents[1]
BASELINE = GOC / "soat_baseline.json"

# `_daxong/` là script đã khai tử (chết rồi, soi làm gì), còn lại là rác công cụ.
BO_QUA_THU_MUC = {".git", "__pycache__", "venv", ".venv", "_daxong", "node_modules"}

# Nguồn của CHÍNH bộ soát. Nó chứa các chuỗi mồi (cổng AnkiConnect, tên lớp HTML)
# nên phải tự loại mình khỏi mục soi NỘI DUNG CHUỖI (S1, S5), kẻo tự tố.
NGUON_BO_SOAT = {"soatkientruc.py", "soat"}


def dat_goc(duong):
    """Trỏ gốc sang thư mục khác — CHỈ dùng trong test (dựng repo giả).
    Đổi luôn `BASELINE` theo: hai thứ lệch nhau thì test đọc baseline repo thật."""
    global GOC, BASELINE
    GOC = Path(duong)
    BASELINE = GOC / "soat_baseline.json"


class PhatHien:
    """Một chỗ bị bắt. `khoa` so với baseline — CỐ Ý không chứa số dòng, vì số
    dòng đổi mỗi lần sửa file khác và sẽ làm baseline nhiễu."""
    def __init__(self, khoa, dong, mo_ta):
        self.khoa = khoa
        self.dong = dong
        self.mo_ta = mo_ta


def cac_file_py(ke_ca_minh=True):
    """`ke_ca_minh=False` cho mục soi NỘI DUNG CHUỖI (S1, S5): loại nguồn của
    chính bộ soát ra khỏi vòng quét. Loại theo ĐƯỜNG DẪN TƯƠNG ĐỐI (không theo
    `__file__`) để còn đúng khi `dat_goc()` trỏ vào repo giả."""
    for p in sorted(GOC.rglob("*.py")):
        phan = p.relative_to(GOC).parts
        if any(x in BO_QUA_THU_MUC for x in phan):
            continue
        if not ke_ca_minh and phan[0] in NGUON_BO_SOAT:
            continue
        yield p


def duong_dan(p):
    return p.relative_to(GOC).as_posix()


def doc_cay(p):
    """Trả (source, ast) — None nếu file không parse được (không chết cả bộ soát)."""
    try:
        src = p.read_text(encoding="utf-8")
        return src, ast.parse(src)
    except (OSError, SyntaxError, UnicodeDecodeError):
        return None, None


def goi_cua(p):
    """Gói của một file = thành phần thư mục đầu tiên. File ở gốc thì gói là ''."""
    phan = p.relative_to(GOC).parts
    return phan[0] if len(phan) > 1 else ""


def chuoi_trong_cay(cay):
    """Mọi hằng chuỗi trong cây cú pháp, kèm số dòng. Dùng ast chứ không grep để
    chữ trong COMMENT không bị tính oan (grep từng bắt nhầm `congcu.py:164`)."""
    for node in ast.walk(cay):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            yield node.value, getattr(node, "lineno", 0)
