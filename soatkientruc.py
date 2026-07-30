# -*- coding: utf-8 -*-
"""CỬA SOÁT KIẾN TRÚC — máy canh những luật mà tài liệu không tự thi hành được.

Vì sao có file này (G1 của `_fable_plan.md`): dự án không bị "code xấu", nó bị
THIẾU CỬA SOÁT CHO CODE. Chỗ nào có máy đo (dây chuyền kho, tag `chuan::N`) thì
sạch; chỗ nào luật chỉ nằm trong đầu người thì trôi. File này là cái máy đo đó
cho phần code.

    python soatkientruc.py          # kiểm — exit 1 khi có ĐỎ
    python soatkientruc.py --chot   # chốt baseline mới (CHỈ được giảm)

🔴 KHÔNG import bất cứ module nào của dự án. Import là kéo theo `telegram`, đọc
CSV 8,4 MB, tệ nhất là chạm `setup_anki_environment` — một bộ soát mà có tác dụng
phụ thì không ai dám chạy. Chỉ `pathlib` đọc text + `ast` phân tích cú pháp tĩnh
(KHÔNG thực thi) + regex. Zero phụ thuộc ngoài stdlib.

🟡 VÀNG vs 🔴 ĐỎ — nguyên tắc chống báo động giả (README huongdan:314 của user:
"bộ soát kêu oan là bộ soát chết"): toàn bộ nợ tồn đọng là VÀNG, im lặng cho tới
khi TĂNG. Chỉ ĐỎ với vi phạm MỚI, hoặc lỗi một-lần-là-hại (S4, S7). Mọi miễn trừ
phải kèm lý do ngay trong `soat_baseline.json` — học từ chính `MIEN_TRU`.

Ratchet: `soat_baseline.json` ghi số hiện tại của từng mục VÀNG; vượt là ĐỎ;
`--chot` chỉ ghi được số THẤP HƠN ⇒ nợ chỉ đi xuống, không mọc lại.
"""
import ast
import json
import re
import sys
from pathlib import Path

GOC = Path(__file__).resolve().parent
BASELINE = GOC / "soat_baseline.json"


def inn(msg=""):
    """print() không bao giờ làm chết bộ soát. Console Windows mặc định cp1252
    KHÔNG in nổi emoji lẫn tiếng Việt có dấu — `congcu.py` đã chết đúng vì lý do
    này. Một cửa canh deploy mà tự chết vì lỗi in ấn thì tệ hơn là không có cửa:
    nó chặn deploy bằng một lỗi chẳng liên quan gì tới kiến trúc."""
    try:
        print(msg)
    except UnicodeEncodeError:
        print(msg.encode("ascii", errors="replace").decode("ascii"))

# Thư mục không quét: `_daxong/` là script đã khai tử (L2 — chúng chết rồi, soi
# làm gì), còn lại là rác công cụ.
BO_QUA_THU_MUC = {".git", "__pycache__", "venv", ".venv", "_daxong", "node_modules"}

# Điểm vào sống được phép nằm ở gốc (L2) — ĐÚNG BA FILE, từ G3 (31/07/2026).
# `soatkientruc.py` là điểm vào thứ 3, ngoại lệ L2 hợp thức bằng QD-02.
# Script vận hành ở `scripts/`, script chạy-một-lần đã khai tử ở `_daxong/`.
# 🔴 Thêm tên vào đây là NỚI LUẬT — phải có lý do trong QUYETDINH.md trước.
GOC_HOP_LE = {"bot.py", "main.py", "soatkientruc.py"}

HTML_DAC_TRUNG = ("example-toggle", "meaning-list")


class PhatHien:
    """Một chỗ bị bắt. `khoa` là thứ dùng để so với baseline — CỐ Ý không chứa
    số dòng, vì số dòng đổi mỗi lần sửa file khác và sẽ làm baseline nhiễu."""

    def __init__(self, khoa, dong, mo_ta):
        self.khoa = khoa
        self.dong = dong
        self.mo_ta = mo_ta


def cac_file_py(ke_ca_minh=True):
    """`ke_ca_minh=False` cho các mục soi NỘI DUNG CHUỖI (S1, S5): chính file này
    phải chứa `8765` và `meaning-list` làm mẫu để đi tìm — bộ soát tự tố mình là
    kiểu kêu oan ngu ngốc nhất, và là thứ khiến người ta tắt nó ngay ngày đầu."""
    for p in sorted(GOC.rglob("*.py")):
        if any(phan in BO_QUA_THU_MUC for phan in p.relative_to(GOC).parts):
            continue
        if not ke_ca_minh and p.resolve() == Path(__file__).resolve():
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


def _goi_cua(p):
    """Gói của một file = thành phần thư mục đầu tiên. File ở gốc thì gói là ''."""
    phan = p.relative_to(GOC).parts
    return phan[0] if len(phan) > 1 else ""


def _chuoi_trong_cay(cay):
    """Mọi hằng chuỗi trong cây cú pháp, kèm số dòng. Dùng ast chứ không grep để
    chữ nằm trong COMMENT không bị tính — `congcu.py:164` nhắc `grammar._family()`
    trong một dòng chú thích, grep bắt nhầm, ast thì không thấy."""
    for node in ast.walk(cay):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            yield node.value, getattr(node, "lineno", 0)


# ---------------------------------------------------------------------------
# S1 — cửa lậu tới AnkiConnect
# ---------------------------------------------------------------------------
def s1_cong_anki():
    """L1: AnkiConnect đi qua MỘT cửa. `anki_tools/config.py` là nơi định nghĩa
    `ANKI_CONNECT_URL` (cửa thật), `data/huongdan/kho/` đóng băng theo QD-01, và
    12 file lô đã khai tử (QD-03) thì không chạy được nữa nên không tính."""
    ra = []
    for p in cac_file_py(ke_ca_minh=False):
        src, cay = doc_cay(p)
        if cay is None:
            continue
        for chuoi, dong in _chuoi_trong_cay(cay):
            if "8765" in chuoi:
                ra.append(PhatHien(duong_dan(p), dong, f"tro thang toi cong AnkiConnect: {chuoi!r}"))
                break
    return ra


# ---------------------------------------------------------------------------
# S2 — gọi tên private XUYÊN GÓI
# ---------------------------------------------------------------------------
def s2_private_xuyen_goi():
    """Private trong CÙNG gói là chuyện nội bộ, hợp lệ. Chỉ bắt khi một gói thò
    tay vào ruột gói khác — đó là chỗ sẽ gãy khi gói kia được dọn."""
    ra = []
    for p in cac_file_py():
        src, cay = doc_cay(p)
        if cay is None:
            continue
        goi = _goi_cua(p)
        # tên đang dùng trong file -> gói mà module đó thuộc về. `import congcu`
        # (kiểu chèn sys.path của dây chuyền kho) không thuộc gói nào -> "", tức
        # KHÁC mọi gói ⇒ vẫn bị soi. Đó là đúng: `dochuan.py` gọi `congcu._BANG_RE`
        # cũng là thò tay vào ruột module khác y như gọi xuyên gói.
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
                            f"{duong_dan(p)}|{a.name}", node.lineno,
                            f"import ten private xuyen goi: {node.module}.{a.name}"))
            # dạng 2: <module>._ten  (vd grammar._cache)
            elif isinstance(node, ast.Attribute) and node.attr.startswith("_"):
                val = node.value
                if isinstance(val, ast.Name) and val.id in goi_cua_ten:
                    if goi_cua_ten[val.id] == goi:
                        continue                   # cùng gói -> nội bộ, hợp lệ
                    ra.append(PhatHien(
                        f"{duong_dan(p)}|{val.id}.{node.attr}", node.lineno,
                        f"goi ten private xuyen goi: {val.id}.{node.attr}"))
    return ra


# ---------------------------------------------------------------------------
# S3 — tgbot: flow import ngang flow
# ---------------------------------------------------------------------------
def s3_tgbot_tang():
    """Mô hình tầng: core <- flows <- dispatch <- app. Flow gọi flow là bắc cầu
    ngang, làm hai màn hình dính nhau — sửa một cái là cái kia đổi theo âm thầm."""
    ra = []
    for p in cac_file_py():
        if _goi_cua(p) != "tgbot" or not p.name.startswith("flow_"):
            continue
        src, cay = doc_cay(p)
        if cay is None:
            continue
        for node in ast.walk(cay):
            if isinstance(node, ast.ImportFrom) and node.module:
                if node.module.startswith("flow_") and node.module != p.stem:
                    ra.append(PhatHien(
                        f"{duong_dan(p)}|{node.module}", node.lineno,
                        f"flow import ngang flow: {p.stem} -> {node.module}"))
    return ra


# ---------------------------------------------------------------------------
# S4 — MIEN_TRU phải chỉ có MỘT nơi
# ---------------------------------------------------------------------------
def s4_mientru_mot_noi():
    """Hai bản `MIEN_TRU` lệch nhau (1 mục vs 5) từng làm `kiemtra.py` kêu oan 4
    từ đúng chính tả — G0 đã gộp về `data/huongdan/mientru.py`. MỘT nơi là đúng
    (đó là cửa); từ nơi thứ HAI trở đi mới là ĐỎ, không chờ baseline: một bộ soát
    kêu oan chết nhanh hơn một bộ soát bỏ sót."""
    noi = []
    for p in cac_file_py():
        if not duong_dan(p).startswith("data/huongdan/"):
            continue
        src, cay = doc_cay(p)
        if cay is None:
            continue
        for node in cay.body:
            if isinstance(node, ast.Assign):
                for t in node.targets:
                    if isinstance(t, ast.Name) and t.id == "MIEN_TRU":
                        noi.append(PhatHien(duong_dan(p), node.lineno, "dinh nghia MIEN_TRU"))
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
    for p in cac_file_py(ke_ca_minh=False):
        if p.name == "html_builder.py":
            continue
        src, cay = doc_cay(p)
        if cay is None:
            continue
        for chuoi, dong in _chuoi_trong_cay(cay):
            hit = [h for h in HTML_DAC_TRUNG if h in chuoi]
            if hit:
                ra.append(PhatHien(f"{duong_dan(p)}|{hit[0]}", dong,
                                   f"dung HTML the ngoai html_builder: {hit[0]}"))
    return ra


# ---------------------------------------------------------------------------
# S6 — thư mục gốc chỉ chứa điểm vào đang sống (L2)
# ---------------------------------------------------------------------------
def s6_goc_sach():
    ra = []
    for p in sorted(GOC.glob("*.py")):
        if p.name not in GOC_HOP_LE:
            ra.append(PhatHien(p.name, 0, "file .py moi o thu muc goc (L2)"))
    return ra


# ---------------------------------------------------------------------------
# S7 — 12 file lô thế hệ 1 phải còn nguyên ngòi đã tháo
# ---------------------------------------------------------------------------
def s7_lo_da_khai_tu():
    """QD-03: chạy lại một file lô thế hệ 1 là XOÁ bảng chia thẻ thật, im lặng.
    Đo bằng ast chứ không đếm dòng: guard phải là CÂU LỆNH THỰC THI ĐẦU TIÊN —
    đó mới là thứ bảo đảm không code nào chạy trước nó. (Guard thực tế nằm ở
    dòng 10-15 vì docstring dài, nên luật "≤5 dòng đầu" của plan là sai chỗ.)"""
    ra = []
    for p in sorted((GOC / "data" / "huongdan").glob("lo*.py")):
        src, cay = doc_cay(p)
        if cay is None:
            ra.append(PhatHien(duong_dan(p), 0, "khong doc/parse duoc de kiem guard"))
            continue
        than = list(cay.body)
        if than and isinstance(than[0], ast.Expr) and isinstance(than[0].value, ast.Constant) \
                and isinstance(than[0].value.value, str):
            than = than[1:]                        # bỏ docstring
        ok = False
        if than and isinstance(than[0], ast.Raise):
            for chuoi, _ in _chuoi_trong_cay(than[0]):
                if "KHAI TU" in chuoi:
                    ok = True
                    break
        if not ok:
            ra.append(PhatHien(duong_dan(p), 1,
                               "THIEU guard KHAI TU o cau lenh dau tien (QD-03)"))
    return ra


# ---------------------------------------------------------------------------
# S8 — KIENTRUC.md có nói dối không
# ---------------------------------------------------------------------------
def s8_manifest():
    """Tài liệu nói dối thì máy chỉ mặt — đúng cơ chế đã giữ `CHUAN.md` sống.
    Chưa có `KIENTRUC.md` (G2 mới viết) thì mục này ngủ, KHÔNG kêu."""
    kt = GOC / "KIENTRUC.md"
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
    that_goi = {d.name for d in GOC.iterdir()
                if d.is_dir() and (d / "__init__.py").exists()
                and d.name not in BO_QUA_THU_MUC}
    for g in sorted(khai_goi - that_goi):
        ra.append(PhatHien(f"KIENTRUC.md|goi:{g}", 0, f"manifest khai goi '{g}' nhung khong co that"))
    for g in sorted(that_goi - khai_goi):
        ra.append(PhatHien(f"KIENTRUC.md|goi:{g}", 0, f"goi '{g}' co that nhung manifest khong khai"))

    for ten in man.get("diem_vao", []):
        if not (GOC / ten).exists():
            ra.append(PhatHien(f"KIENTRUC.md|diem_vao:{ten}", 0,
                               f"manifest khai diem vao '{ten}' nhung file khong ton tai"))
    for ten in man.get("du_lieu_chung", []):
        if not (GOC / ten).exists():
            ra.append(PhatHien(f"KIENTRUC.md|du_lieu:{ten}", 0,
                               f"manifest khai du lieu chung '{ten}' nhung khong ton tai"))
    return ra


# ---------------------------------------------------------------------------
# Khung chạy
# ---------------------------------------------------------------------------
# `luon_do=True`: mục mà MỘT lần lọt là đã hại, không có khái niệm "nợ chấp nhận
# được" — vi phạm nào cũng ĐỎ, kể cả khi baseline từng ghi nhận.
MUC = [
    ("S1", "CUA LAU TOI ANKICONNECT (L1)", s1_cong_anki, False),
    ("S2", "GOI TEN PRIVATE XUYEN GOI", s2_private_xuyen_goi, False),
    ("S3", "TGBOT: FLOW IMPORT NGANG FLOW", s3_tgbot_tang, False),
    ("S4", "MIEN_TRU DINH NGHIA NHIEU NOI", s4_mientru_mot_noi, True),
    ("S5", "HTML THE DUNG NGOAI html_builder", s5_html_ngoai_builder, False),
    ("S6", "FILE .PY LA O THU MUC GOC (L2)", s6_goc_sach, True),
    ("S7", "LO THE HE 1 MAT GUARD KHAI TU (QD-03)", s7_lo_da_khai_tu, True),
    ("S8", "KIENTRUC.md LECH THUC TE", s8_manifest, True),
]


def doc_baseline():
    if not BASELINE.exists():
        return {}
    try:
        return json.loads(BASELINE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def gom(phat_hien):
    d = {}
    for ph in phat_hien:
        d[ph.khoa] = d.get(ph.khoa, 0) + 1
    return d


def _so_cua(gia_tri):
    """Mục baseline viết được hai kiểu: số trần, hoặc `{"so": N, "vi_sao": "..."}`.
    Kiểu thứ hai là kiểu ĐƯỢC KHUYẾN KHÍCH — mỗi miễn trừ/mỗi nợ kèm một câu lý do,
    học đúng từ `MIEN_TRU`: nợ không ghi lý do thì đời sau không dám trả."""
    if isinstance(gia_tri, dict):
        return gia_tri.get("so", 0)
    return gia_tri or 0


def _vi_sao(gia_tri):
    return gia_tri.get("vi_sao", "") if isinstance(gia_tri, dict) else ""


def chay():
    nen = doc_baseline()
    ket_qua = {}
    tong_do = 0

    for ma, tieu_de, ham, luon_do in MUC:
        phat_hien = ham()
        muc_nen = nen.get(ma, {})
        mien_tru = muc_nen.get("mien_tru", {})
        moc = muc_nen.get("baseline", {})

        inn(f"=== {ma} — {tieu_de} ===")

        if phat_hien is None:                      # S8 khi chưa có KIENTRUC.md
            inn("  (chua bat — chua co KIENTRUC.md, se tu bat sau G2)")
            inn()
            ket_qua[ma] = {}
            continue

        con_lai = [ph for ph in phat_hien if ph.khoa not in mien_tru]
        dem = gom(con_lai)
        ket_qua[ma] = dem

        do, vang = [], []
        for khoa in sorted(dem):
            so = dem[khoa]
            cho_phep = 0 if luon_do else _so_cua(moc.get(khoa))
            if so > cho_phep:
                do.append((khoa, so, cho_phep))
            else:
                vang.append((khoa, so))

        if not con_lai:
            inn("  (khong co)")
        for khoa, so, cho_phep in do:
            for ph in [x for x in con_lai if x.khoa == khoa]:
                inn(f"  🔴 {ph.khoa.split('|')[0]}:{ph.dong} — {ph.mo_ta}")
            if cho_phep:
                inn(f"     (baseline cho {cho_phep}, nay {so})")
        # VÀNG in gọn: nợ tồn đọng phải THẤY được nhưng không được lấn át tiếng
        # kêu thật. In hết 12 dòng lô mỗi lần chạy là cách nhanh nhất để người ta
        # thôi đọc output.
        for khoa, so in vang[:3]:
            ten = khoa.split("|")[0]
            ghi_chu = _vi_sao(moc.get(khoa))
            inn(f"  🟡 {ten} ×{so}" + (f" — {ghi_chu}" if ghi_chu else ""))
        if len(vang) > 3:
            inn(f"  🟡 ... con {len(vang) - 3} cho no cu (xem soat_baseline.json)")

        # Nợ đã trả mà chưa chốt lại: nhắc, không kêu ĐỎ.
        da_het = [k for k in moc if k not in dem]
        for k in sorted(da_het):
            inn(f"  ✅ {k.split('|')[0]} — da het, chay --chot de ghi nhan")

        tong_do += len(do)
        inn()

    if tong_do:
        inn(f"🔴 SOAT DO: {tong_do} vi pham MOI — sua truoc khi di tiep.")
        return 1, ket_qua
    inn("✅ SOAT XANH — khong co vi pham moi.")
    return 0, ket_qua


def chot(ket_qua):
    """Ratchet MỘT CHIỀU: chỉ ghi được số thấp hơn hoặc bằng. Không có cửa nào
    cho phép nới baseline — nới được thì nó thành cái bảng ghi nợ, không phải cửa."""
    nen = doc_baseline()
    doi, tu_choi = [], []

    for ma, _, _, luon_do in MUC:
        if luon_do:
            continue
        muc_nen = nen.setdefault(ma, {})
        muc_nen.setdefault("mien_tru", {})
        moc = muc_nen.setdefault("baseline", {})
        nay = ket_qua.get(ma, {})

        for khoa in sorted(set(moc) | set(nay)):
            cu = _so_cua(moc.get(khoa))
            ly_do = _vi_sao(moc.get(khoa))
            moi = nay.get(khoa, 0)
            if moi < cu:
                if moi == 0:
                    moc.pop(khoa, None)
                elif ly_do:
                    moc[khoa] = {"so": moi, "vi_sao": ly_do}
                else:
                    moc[khoa] = moi
                doi.append(f"{ma} {khoa}: {cu} -> {moi}")
            elif moi > cu:
                tu_choi.append(f"{ma} {khoa}: {cu} -> {moi}")

    for d in doi:
        inn(f"  ↓ {d}")
    for t in tu_choi:
        inn(f"  ✋ TU CHOI (ratchet chi cho GIAM): {t}")
    if not doi:
        inn("  (khong co gi de chot)")

    BASELINE.write_text(json.dumps(nen, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    inn(f"\nDa ghi {BASELINE.name}.")


if __name__ == "__main__":
    ma_thoat, kq = chay()
    if "--chot" in sys.argv:
        inn("--- CHOT BASELINE ---")
        chot(kq)
        sys.exit(0)
    sys.exit(ma_thoat)
