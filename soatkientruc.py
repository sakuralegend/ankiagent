# -*- coding: utf-8 -*-
"""CỬA SOÁT KIẾN TRÚC — máy canh những luật mà tài liệu không tự thi hành được:
chỗ có máy đo thì sạch, chỗ luật chỉ nằm trong đầu người thì trôi (G1).
    python soatkientruc.py          # kiểm — exit 1 khi có ĐỎ
    python soatkientruc.py --chot   # chốt baseline mới (CHỈ được giảm)

🔴 KHÔNG import module nào của dự án — import là kéo theo tác dụng phụ (telegram,
CSV 8,4 MB, `setup_anki_environment`), mà bộ soát có tác dụng phụ thì không ai
dám chạy. Chỉ stdlib: `pathlib` + `ast` (phân tích tĩnh, KHÔNG thực thi) + regex.

🟡 VÀNG vs 🔴 ĐỎ — "bộ soát kêu oan là bộ soát chết": nợ tồn đọng là VÀNG, im tới
khi TĂNG; chỉ ĐỎ với vi phạm MỚI hoặc lỗi một-lần-là-hại. Ratchet
`soat_baseline.json`: `--chot` chỉ ghi được số THẤP HƠN ⇒ nợ không mọc lại.
"""
import ast
import json
import re
import subprocess
import sys
from fnmatch import fnmatchcase
from pathlib import Path

GOC = Path(__file__).resolve().parent
BASELINE = GOC / "soat_baseline.json"


def inn(msg=""):
    """print() không được làm chết bộ soát: console Windows cp1252 không in nổi
    emoji/tiếng Việt (`congcu.py` từng chết vì đúng lỗi in ấn này)."""
    try:
        print(msg)
    except UnicodeEncodeError:
        print(msg.encode("ascii", errors="replace").decode("ascii"))

# `_daxong/` là script đã khai tử (chết rồi, soi làm gì), còn lại là rác công cụ.
BO_QUA_THU_MUC = {".git", "__pycache__", "venv", ".venv", "_daxong", "node_modules"}

# Điểm vào sống ở gốc (L2) — ĐÚNG BA FILE (QD-02). Script vận hành: `scripts/`.
# 🔴 Thêm tên vào đây là NỚI LUẬT — phải có lý do trong QUYETDINH.md trước.
GOC_HOP_LE = {"bot.py", "main.py", "soatkientruc.py"}

HTML_DAC_TRUNG = ("example-toggle", "meaning-list")


class PhatHien:
    """Một chỗ bị bắt. `khoa` so với baseline — CỐ Ý không chứa số dòng, vì số
    dòng đổi mỗi lần sửa file khác và sẽ làm baseline nhiễu."""
    def __init__(self, khoa, dong, mo_ta):
        self.khoa = khoa
        self.dong = dong
        self.mo_ta = mo_ta


def cac_file_py(ke_ca_minh=True):
    """`ke_ca_minh=False` cho mục soi NỘI DUNG CHUỖI (S1, S5): file này chứa chính
    các chuỗi mồi nên phải tự loại mình khỏi vòng quét, kẻo tự tố."""
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
    chữ trong COMMENT không bị tính oan (grep từng bắt nhầm `congcu.py:164`)."""
    for node in ast.walk(cay):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            yield node.value, getattr(node, "lineno", 0)


# ---------------------------------------------------------------------------
# S1 — cửa lậu tới AnkiConnect
# ---------------------------------------------------------------------------
def s1_cong_anki():
    """L1: AnkiConnect đi qua MỘT cửa — `anki_tools/config.py` định nghĩa
    `ANKI_CONNECT_URL` là cửa thật; nợ cũ nằm trong baseline."""
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
        # `tests/` được phép thò tay vào ruột — kiểm nội bộ chính là VIỆC của test.
        if duong_dan(p).startswith("tests/"):
            continue
        src, cay = doc_cay(p)
        if cay is None:
            continue
        goi = _goi_cua(p)
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
    """Hai bản `MIEN_TRU` lệch nhau từng làm `kiemtra.py` kêu oan 4 từ đúng chính
    tả (G0 gộp về `data/huongdan/mientru.py`). MỘT nơi là cửa; nơi thứ HAI là ĐỎ."""
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
    """QD-03: chạy lại lô thế hệ 1 là XOÁ bảng chia thẻ thật, im lặng. Đo bằng
    ast: guard phải là CÂU LỆNH THỰC THI ĐẦU TIÊN (sau docstring), không đếm dòng."""
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
    """Commit đụng code phải khai VÌ SAO trong THÂN, không chỉ tiêu đề — commit
    message gắn chặt với diff nên không nói dối được (thay cửa CHANGELOG, QD-06).
    Chỉ soi commit CHƯA PUSH: code đã rời PC thì kêu cũng muộn."""
    def _git(*doi_so):
        """Goi git, tra stdout hoac None. Goi nhieu lan thay vi gop bang ky tu
        phan cach — ban gop tung lam ky tu dieu khien lot vao source."""
        # 🔴 PHẢI khai encoding="utf-8": mặc định text=True dùng cp1252 (Windows),
        # commit message có tiếng Việt/Nga ⇒ UnicodeDecodeError trong thread nền,
        # stdout thành None và mục này chết. Đã dính thật 31/07/2026.
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
# Ngưỡng số — đọc từ `soat_nguong.json` (QD-21)
# ---------------------------------------------------------------------------
def _nguong():
    """Mọi CON SỐ TRẦN ở `soat_nguong.json` — cấu hình THẬT, tài liệu chỉ trỏ
    (QD-21). Parse CHẶT: khoá trùng (một đích hai trần) là ValueError. Hỏng thì
    S12 kêu ĐỎ; các mục dùng số im lặng để không kêu ba lần cho một lỗi."""
    def _ghep(cap):
        d = {}
        for k, v in cap:
            if k in d:
                raise ValueError(f"khoa trung (mot dich hai tran): {k}")
            d[k] = v
        return d
    return json.loads((GOC / "soat_nguong.json").read_text(encoding="utf-8"),
                      object_pairs_hook=_ghep)


# ---------------------------------------------------------------------------
# S10 — file trí nhớ phình quá trần (PHÚT ĐỌC quy ra KÝ TỰ — QD-20)
# ---------------------------------------------------------------------------
def s10_tri_nho_phinh():
    """Chạm trần KHÔNG có nghĩa "cấm viết thêm" — nghĩa là phải dừng lại CHỌN:
    cắt mục đã hết giá trị, hay nâng ngân sách trong `soat_nguong.json` kèm QD-nn."""
    try:
        ng = _nguong()
        toc_do, tran_phut = ng["ky_tu_moi_phut"]["so"], ng["phut_doc"]["tran"]
    except (OSError, ValueError, KeyError):
        return []                              # soat_nguong.json hỏng: S12 kêu ĐỎ
    ra = []
    for ten, phut in sorted(tran_phut.items()):
        p = GOC / ten
        if not p.exists():
            continue
        try:
            so_ky_tu = len(p.read_text(encoding="utf-8"))
        except OSError:
            continue
        tran = phut * toc_do
        if so_ky_tu > tran:
            ra.append(PhatHien(
                ten, so_ky_tu,
                f"doc het mat ~{so_ky_tu / toc_do:.0f} phut, ngan sach {phut} phut "
                f"({so_ky_tu} ky tu > {tran}) — cat muc het gia tri, hoac nang ngan sach kem QD-nn"))
    return ra


# ---------------------------------------------------------------------------
# S11 — hook nhắc luật còn sống không
# ---------------------------------------------------------------------------
def s11_hook_con_song():
    """Hook `UserPromptSubmit` bơm lại luật mỗi lượt — nó chết là chết IM LẶNG
    (QD-13). Phải CHẠY THẬT lệnh hook chứ không chỉ kiểm file tồn tại: kiểu chết
    hay gặp nhất là `python` không có trên PATH, nhìn tên file sẽ báo XANH oan.
    CỐ Ý không chấm nội dung hook — cửa chấm câu chữ bị vô hiệu bằng vài từ (S9)."""
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
# S12·S13·S14 — ba cửa quanh `soat_nguong.json` (QD-21)
# ---------------------------------------------------------------------------
def s12_nguong_hop_le():
    """Nguồn duy nhất thì phải TỰ nhất quán: trần trỏ file đã xoá / trỏ QD-nn
    không có trong QUYETDINH.md / khoá trùng / file hỏng-mất ⇒ ĐỎ ngay."""
    try:
        ng = _nguong()
    except (OSError, ValueError) as e:
        return [PhatHien("soat_nguong.json", 0, f"doc/parse that bai: {e}")]
    ra = []
    duong = list(ng.get("phut_doc", {}).get("tran", {})) + \
            list(ng.get("dong_py", {}).get("da_ghi_no", {}))
    for ten in duong:
        if not (GOC / ten).exists():
            ra.append(PhatHien(f"nguong|{ten}", 0, f"tran tro toi file khong ton tai: {ten}"))
    try:
        qd_that = set(re.findall(r"QD-\d+", (GOC / "QUYETDINH.md").read_text(encoding="utf-8")))
    except OSError:
        qd_that = set()
    for muc, phan in ng.items():
        qd = phan.get("qd") if isinstance(phan, dict) else None
        if qd and qd not in qd_that:
            ra.append(PhatHien(f"nguong|{muc}", 0, f"tro {qd} nhung QUYETDINH.md khong co so do"))
    return ra


def s13_tran_dong_code():
    """Trần dòng file CODE (trước 03/08 không máy nào canh): vượt `ghi_no` phải có
    trong `da_ghi_no` kèm mốc ratchet, vượt `tach` là ĐỎ thẳng. Lô kho (`k*.py`,
    `lo*.py`) là DỮ LIỆU sinh ra, không phải code — bỏ qua theo `bo_qua_mau`."""
    try:
        ng = _nguong()["dong_py"]
    except (OSError, ValueError, KeyError):
        return []
    ra = []
    for p in cac_file_py():
        d = duong_dan(p)
        if any(fnmatchcase(d, mau) for mau in ng["bo_qua_mau"]):
            continue
        try:
            so = len(p.read_text(encoding="utf-8").splitlines())
        except OSError:
            continue
        moc = ng["da_ghi_no"].get(d)
        if so > ng["tach"]:
            ra.append(PhatHien(d, 0, f"{so} dong > tran tach {ng['tach']} — tach truoc khi them"))
        elif so > ng["ghi_no"] and moc is None:
            ra.append(PhatHien(d, 0, f"{so} dong > {ng['ghi_no']} — ghi SONO.md + moc vao da_ghi_no"))
        elif moc is not None and so > moc:
            ra.append(PhatHien(d, 0, f"{so} dong, phinh qua moc da ghi no {moc} — dung them nua"))
    return ra


def s14_phienban_tran():
    """`PHIENBAN.md` giữ tối đa N bản, mỗi bản tối đa M gạch đầu dòng (QD-07) —
    con số từng nêu ở 4 file mà 0 cửa canh, nay máy đếm thật."""
    try:
        ng = _nguong()["phienban"]
    except (OSError, ValueError, KeyError):
        return []
    p = GOC / "PHIENBAN.md"
    if not p.exists():
        return []
    muc_cua_ban, ban = {}, None
    for dong in p.read_text(encoding="utf-8").splitlines():
        if re.match(r"##\s*v\d", dong):
            ban = dong.strip()
            muc_cua_ban[ban] = 0
        elif ban and dong.lstrip().startswith("- "):
            muc_cua_ban[ban] += 1
    ra = []
    if len(muc_cua_ban) > ng["giu_ban"]:
        ra.append(PhatHien("PHIENBAN.md", 0,
                           f"{len(muc_cua_ban)} ban > tran {ng['giu_ban']} — xoa ban cu nhat"))
    for ban, so in muc_cua_ban.items():
        if so > ng["muc_moi_ban"]:
            ra.append(PhatHien(f"PHIENBAN.md|{ban[:24]}", 0, f"{so} muc > tran {ng['muc_moi_ban']}/ban"))
    return ra


# ---------------------------------------------------------------------------
# Khung chạy
# ---------------------------------------------------------------------------
# `luon_do=True`: MỘT lần lọt là đã hại — vi phạm nào cũng ĐỎ, bất kể baseline.
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
    ("S12", "soat_nguong.json TU MAU THUAN (QD-21)", s12_nguong_hop_le, True),
    ("S13", "FILE CODE QUA TRAN DONG (QD-21)", s13_tran_dong_code, True),
    ("S14", "PHIENBAN.md QUA TRAN BAN/MUC (QD-07)", s14_phienban_tran, True),
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
    """Baseline viết được hai kiểu: số trần, hoặc `{"so": N, "vi_sao": "..."}` —
    kiểu sau ĐƯỢC KHUYẾN KHÍCH: nợ không ghi lý do thì đời sau không dám trả."""
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
        # VÀNG in gọn: nợ phải THẤY được nhưng không được lấn át tiếng kêu thật.
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
