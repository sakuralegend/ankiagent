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
import subprocess
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
        # `tests/` được phép thò tay vào ruột — đó chính là VIỆC của test: kiểm
        # nội bộ, và canh giúp cho alias public (`grammar.BANG_RE is _BANG_RE`)
        # không ai lỡ xoá. Bắt test vì "gọi private" là kêu oan đúng nghĩa.
        if duong_dan(p).startswith("tests/"):
            continue
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
# S9 — commit đụng code mà không khai VÌ SAO
# ---------------------------------------------------------------------------
def s9_commit_thieu_vi_sao():
    """Commit đụng code phải khai VÌ SAO, không chỉ một dòng tiêu đề.

    Bản đầu (31/07/2026 sáng) canh `CHANGELOG.md`. Đo lại chiều đó thì thấy nó ép
    làm một việc TRÙNG LẶP: cùng một chuyện viết hai lần, một vào CHANGELOG một vào
    commit message — mà không script nào đọc CHANGELOG và user nói thẳng không đọc.
    Đóng sổ CHANGELOG (QD-06) và chuyển cửa soát sang canh đúng chỗ còn giá trị:
    chất lượng commit message — thứ **gắn chặt với diff nên không nói dối được**.

    Chỉ soi commit CHƯA PUSH: code đã rời PC thì kêu cũng muộn."""
    def _git(*doi_so):
        """Goi git, tra stdout hoac None. Co y KHONG dung ky tu phan cach ky di
        de gop nhieu truong vao mot lan goi — ban thu dau lam vay va ky tu dieu
        khien lot vao source thanh byte that, gay ngay lan chay dau. Goi git nhieu
        lan cham hon vai mili-giay nhung DOC HIEU DUOC, ma day la thu chan deploy."""
        # 🔴 PHẢI khai encoding="utf-8": mặc định `text=True` dùng bảng mã hệ
        # thống (cp1252 trên Windows), mà commit message ở repo này có tiếng Việt
        # và tiếng Nga ⇒ luồng đọc của subprocess ném UnicodeDecodeError trong
        # thread nền, `r.stdout` thành **None**, và mục soát này chết bằng
        # `'NoneType' has no attribute...`. Đã dính thật 31/07/2026.
        try:
            r = subprocess.run(["git", *doi_so], cwd=str(GOC), capture_output=True,
                               text=True, encoding="utf-8", errors="replace", timeout=20)
        except (OSError, subprocess.SubprocessError):
            return None
        return r.stdout if r.returncode == 0 else None

    danh_sach = _git("log", "origin/main..HEAD", "--format=%H")
    if not danh_sach:
        return []          # khong git / chua co origin/main / khong co commit nao

    ra = []
    for sha in [d.strip() for d in danh_sach.splitlines() if d.strip()]:
        tieu_de = (_git("log", "-1", "--format=%s", sha) or "").strip()
        than = (_git("log", "-1", "--format=%b", sha) or "").strip()

        ten_file = _git("show", "--name-only", "--format=", sha)
        if ten_file is None:
            continue
        da_doi = {d.strip() for d in ten_file.splitlines() if d.strip()}

        la_code = [d for d in da_doi
                   if d.endswith((".py", ".ps1", ".sh", ".service"))
                   and not d.startswith("_daxong/")]
        if not la_code:
            continue                               # chỉ sửa tài liệu -> không bắt buộc

        # Ngưỡng cố ý THẤP: chỉ chặn commit trần trụi một dòng. Không chấm điểm văn
        # hay — bộ soát khắt khe về câu chữ sẽ bị vô hiệu hoá bằng vài từ vô nghĩa.
        if len(than.strip()) < 40:
            ra.append(PhatHien(
                f"commit {sha[:8]}", 0,
                f"dung {len(la_code)} file code ma message KHONG co phan than giai thich "
                f"vi sao (\"{tieu_de[:50]}\") — sua bang `git commit --amend`"))
    return ra


# ---------------------------------------------------------------------------
# S10 — file trí nhớ phình quá trần
# ---------------------------------------------------------------------------
# Trần cho các file BỊ BẮT ĐỌC. Vì sao cần: `CHANGELOG.md` đã phình tới mức không
# ai đọc ngược nữa (phải đóng sổ, QD-06). File mà AI phải đọc MỖI PHIÊN thì phình
# = bị lướt = chết y hệt README cũ.
#
# 🔴 ĐƠN VỊ LÀ **PHÚT ĐỌC**, quy ra **KÝ TỰ** — KHÔNG phải số dòng (QD-20, 03/08).
# Bản 31/07 đếm dòng. Đo 03/08 cho thấy nó đo sai hẳn: ký tự/dòng chạy từ **49 tới
# 140** giữa các file, gấp ~3 lần. Hệ quả thật: `QUYETDINH.md` báo 149/150 "còn
# chỗ" trong khi nó nặng 30 KB, dòng dài nhất **1090 ký tự** — vượt ngân sách gấp
# ba mà cửa vẫn XANH. Ký tự thì không nói dối được; xuống dòng thì có.
#
# Tốc độ 1400 ký tự/phút KHÔNG bịa: nó là tốc độ hàm ý của đúng hai file chưa ai
# kêu là dài — KIENTRUC.md (1417) và README.md (1438). Lấy chỗ đang vừa làm mốc.
KY_TU_MOI_PHUT = 1400
#
# ⚠️ Ngân sách dưới đây đặt từ KÍCH THƯỚC THẬT ngày 03/08 (làm tròn lên phút), tức
# một ratchet chốt-từ-hiện-trạng giống `soat_baseline.json` — nó KHÔNG hợp thức hoá
# hiện trạng, nó chặn hiện trạng phình thêm. Số trong ngoặc là ký tự đo được; cột
# "(cũ N)" là ngân sách thời đếm dòng, để thấy nó đã lệch thực tế bao xa.
PHUT_DOC = {
    "CLAUDE.md": 7,                        # 8 488 kt  (cũ 3) — nạp MỖI phiên
    "KIENTRUC.md": 9,                      # 11 337 kt (cũ 8)  — đọc khi sửa xuyên mảng
    "QUYETDINH.md": 15,                    # 19 924 kt (cũ 5)  — lệch nặng nhất
    "SONO.md": 6,                          # 8 105 kt  (cũ 4)
    "CACHLAM.md": 15,                      # 20 660 kt (cũ 8)
    "README.md": 4,                        # 4 314 kt  (cũ 3)
    # File DUY NHẤT viết cho user. Ngân sách khắt khe nhất vì user không có nghĩa
    # vụ đọc tài liệu. ⚠️ QD-07 ghi "trần 2 phút" — con số đó tính bằng DÒNG, quy
    # sang ký tự là 3; ràng buộc thật của file này vẫn là "tối đa 5 mục/bản".
    "PHIENBAN.md": 3,                      # 3 652 kt  (cũ 2)
    # Phiếu việc dùng một lần (/ycau ghi đè, /nghiemthu xoá). Trần thấp là CỬA
    # chống nó biến thành CHANGELOG.md thứ hai: phình = ai đó đang NỐI THÊM
    # thay vì ghi đè, tức là quy trình đã trôi. (QD-09)
    "VIECDANGLAM.md": 2,                   # 1 230 kt  (cũ 2) — còn dư, giữ nguyên
    # 🔴 HAI FILE TO NHẤT REPO, TRƯỚC 03/08 KHÔNG BỊ CANH GÌ CẢ. S10 khớp đúng
    # đường dẫn từ gốc, nên khoá "README.md" chỉ bắt file ở gốc (4 314 kt) và bỏ
    # lọt bản trong data/huongdan/ gấp năm lần nó. Cộng lại 60 249 ký tự — 44%
    # toàn bộ tài liệu — nằm ngoài mọi cửa trong khi PHIENBAN.md 3 652 kt bị chặn.
    "data/huongdan/kho/TIEPTUC.md": 28,    # 37 846 kt (MỚI)
    "data/huongdan/README.md": 17,         # 22 403 kt (MỚI)
}


def s10_tri_nho_phinh():
    """Chạm trần KHÔNG có nghĩa "cấm viết thêm" — nghĩa là phải dừng lại CHỌN:
    cắt mục đã hết giá trị, hay nâng ngân sách phút một cách có ý thức (ghi QD)."""
    ra = []
    for ten, phut in sorted(PHUT_DOC.items()):
        p = GOC / ten
        if not p.exists():
            continue
        try:
            so_ky_tu = len(p.read_text(encoding="utf-8"))
        except OSError:
            continue
        tran = phut * KY_TU_MOI_PHUT
        if so_ky_tu > tran:
            ra.append(PhatHien(
                ten, so_ky_tu,
                f"doc het mat ~{so_ky_tu / KY_TU_MOI_PHUT:.0f} phut, ngan sach {phut} phut "
                f"({so_ky_tu} ky tu > {tran}) — cat muc het gia tri, hoac nang ngan sach kem QD-nn"))
    return ra


# ---------------------------------------------------------------------------
# S11 — hook nhắc luật còn sống không
# ---------------------------------------------------------------------------
def s11_hook_con_song():
    """Hook `UserPromptSubmit` là thứ DUY NHẤT bơm lại luật vào MỖI lượt — nhưng
    nó chết thì chết IM LẶNG: không có lỗi nào hiện ra, chỉ là các lượt sau AI
    dần quên luật, đúng cơ chế đã đẻ ra 10 wrapper. Đo 01/08/2026: S1→S10 mù
    hoàn toàn với chuyện này ⇒ dựng cửa (QD-13).

    Ba cách hook chết mà mục này bắt được:
      1. File hook bị xoá / đổi tên, `settings.json` trỏ vào chỗ trống.
      2. Mục "hooks" bị gỡ khỏi `settings.json` (vô tình khi sửa cấu hình khác).
      3. 🔴 Lệnh gọi được nhưng KHÔNG chạy nổi trên máy này — hay gặp nhất là
         `python` không có trên PATH (Linux/macOS thường chỉ có `python3`).
         Đây là lý do mục này CHẠY THẬT chứ không chỉ kiểm file có tồn tại:
         cửa soát chỉ nhìn tên file sẽ báo XANH trên đúng cái máy hook đang chết.

    Cái mục này CỐ Ý không bắt: nội dung hook viết gì. Đó là việc của người, và
    một cửa soát chấm điểm câu chữ sẽ bị vô hiệu hoá bằng vài từ vô nghĩa (S9)."""
    p_cai_dat = GOC / ".claude" / "settings.json"
    if not p_cai_dat.exists():
        return [PhatHien(".claude/settings.json", 0,
                         "khong ton tai -> hook nhac luat KHONG chay, luat se mo dan trong phien dai")]
    try:
        cau_hinh = json.loads(p_cai_dat.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        return [PhatHien(".claude/settings.json", 0, f"doc/parse that bai ({e}) -> hook coi nhu chet")]

    lenh = [h.get("command", "")
            for nhom in cau_hinh.get("hooks", {}).get("UserPromptSubmit", [])
            for h in nhom.get("hooks", []) if h.get("type") == "command"]
    if not lenh:
        return [PhatHien(".claude/settings.json", 0,
                         "khong con hook UserPromptSubmit nao -> luat khong duoc bom lai moi luot (QD-09)")]

    ra = []
    for cau in lenh:
        phan = cau.split()
        # Đối số nào trông như đường dẫn trong repo thì phải tồn tại thật.
        for doi_so in phan[1:]:
            if doi_so.endswith(".py") and not (GOC / doi_so).exists():
                ra.append(PhatHien(f"hook|{doi_so}", 0,
                                   f"settings.json goi '{doi_so}' nhung file KHONG ton tai"))
        if ra:
            continue
        try:
            r = subprocess.run(phan, cwd=str(GOC), capture_output=True, text=True,
                               encoding="utf-8", errors="replace", timeout=10)
        except (OSError, subprocess.SubprocessError) as e:
            ra.append(PhatHien(f"hook|{cau[:40]}", 0,
                               f"KHONG chay duoc tren may nay ({type(e).__name__}) — "
                               f"hay gap nhat: lenh 'python' khong co tren PATH"))
            continue
        if r.returncode != 0:
            ra.append(PhatHien(f"hook|{cau[:40]}", 0,
                               f"chay xong nhung exit {r.returncode} -> Claude Code bo qua ket qua"))
        elif not (r.stdout or "").strip():
            ra.append(PhatHien(f"hook|{cau[:40]}", 0,
                               "chay duoc nhung KHONG in ra gi -> bom vao context mot chuoi rong"))
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
    ("S9", "COMMIT DUNG CODE MA KHONG KHAI VI SAO", s9_commit_thieu_vi_sao, True),
    ("S10", "FILE TRI NHO PHINH QUA TRAN", s10_tri_nho_phinh, True),
    ("S11", "HOOK NHAC LUAT DA CHET (QD-13)", s11_hook_con_song, True),
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
