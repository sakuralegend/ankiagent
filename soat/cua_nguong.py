# -*- coding: utf-8 -*-
"""S10 · S12–S14 — các cửa canh CON SỐ TRẦN, tất cả đọc chung `soat_nguong.json`
(QD-21: một nguồn duy nhất, tài liệu chỉ trỏ).

Quy ước chung của file này: cửa nào cần số mà config hỏng/mất thì **im lặng**,
vì S12 đã kêu ĐỎ rồi — kêu ba lần cho một lỗi thì người đọc bắt đầu bỏ qua.
"""
import json
import re
import subprocess
from datetime import date
from fnmatch import fnmatchcase

from . import khung
from .khung import PhatHien


def nguong():
    """Đọc `soat_nguong.json`. Parse CHẶT: khoá trùng (một đích hai trần) là
    ValueError — JSON chuẩn sẽ lặng lẽ lấy giá trị sau, và trần bị nuốt như thế
    là trần không tồn tại."""
    def _ghep(cap):
        d = {}
        for k, v in cap:
            if k in d:
                raise ValueError(f"khoa trung (mot dich hai tran): {k}")
            d[k] = v
        return d
    return json.loads((khung.GOC / "soat_nguong.json").read_text(encoding="utf-8"),
                      object_pairs_hook=_ghep)


# ---------------------------------------------------------------------------
# S10 — file trí nhớ phình quá trần (PHÚT ĐỌC quy ra KÝ TỰ — QD-20)
# ---------------------------------------------------------------------------
def s10_tri_nho_phinh():
    """Chạm trần KHÔNG có nghĩa "cấm viết thêm" — nghĩa là phải dừng lại CHỌN:
    cắt mục đã hết giá trị, hay nâng ngân sách trong `soat_nguong.json` kèm QD-nn.

    🔴 HAI TẦNG, ĐỪNG CỘNG CHUNG — vì sao: QD-30. `batbuoc` = tầng THẬT SỰ bị nhồi
    vào đầu mỗi phiên, có trần TỔNG chặt. Các file còn lại giữ trần riêng làm lưới
    an toàn nhưng KHÔNG cộng vào tầng bắt buộc — một file tra-cứu dài ra không
    cướp chỗ của file bắt-đọc, và ngược lại.
    """
    try:
        ng = nguong()
        toc_do, tran_phut = ng["ky_tu_moi_phut"]["so"], ng["phut_doc"]["tran"]
    except (OSError, ValueError, KeyError):
        return []                              # soat_nguong.json hỏng: S12 kêu ĐỎ
    ra = []

    batbuoc = ng["phut_doc"].get("batbuoc") or []
    tran_tong = ng["phut_doc"].get("tran_tong_batbuoc")
    if batbuoc and tran_tong:
        tong = 0
        for ten in batbuoc:
            p = khung.GOC / ten
            if p.exists():
                tong += len(p.read_text(encoding="utf-8"))
        if tong > tran_tong * toc_do:
            ra.append(PhatHien(
                "LOI BAT BUOC", tong,
                f"tang bat-buoc-doc {tong} ky tu (~{tong / toc_do:.1f} phut) > tran "
                f"{tran_tong} phut — day la thu MOI phien deu phai nuot, cat that chu "
                f"khong day sang file khac ({' + '.join(batbuoc)})"))
    for ten, phut in sorted(tran_phut.items()):
        p = khung.GOC / ten
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
# S12·S13·S14 — ba cửa quanh `soat_nguong.json` (QD-21)
# ---------------------------------------------------------------------------
def s12_nguong_hop_le():
    """Nguồn duy nhất thì phải TỰ nhất quán: trần trỏ file đã xoá / trỏ QD-nn
    không có trong QUYETDINH.md / khoá trùng / file hỏng-mất ⇒ ĐỎ ngay."""
    try:
        ng = nguong()
    except (OSError, ValueError) as e:
        return [PhatHien("soat_nguong.json", 0, f"doc/parse that bai: {e}")]
    ra = []
    duong = list(ng.get("phut_doc", {}).get("tran", {})) + \
            list(ng.get("dong_py", {}).get("da_ghi_no", {}))
    for ten in duong:
        if not (khung.GOC / ten).exists():
            ra.append(PhatHien(f"nguong|{ten}", 0, f"tran tro toi file khong ton tai: {ten}"))
    qd_that = so_hieu_da_biet()
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
        ng = nguong()["dong_py"]
    except (OSError, ValueError, KeyError):
        return []
    ra = []
    for p in khung.cac_file_py():
        d = khung.duong_dan(p)
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


def s15_dong_quyetdinh_dai():
    """Mỗi quyết định đúng MỘT dòng bảng, trần ký tự ở `soat_nguong.json` (QD-23).
    Trần không có máy đếm thì trôi ngay: bản nháp 03/08 phình 199 → 418 ký tự trong
    đúng một lượt, trước khi viết được dòng thật nào.

    Chỉ đếm dòng có ô ĐẦU là số hiệu (`QD-23`, `⚰️ QD-20`, hoặc `—` cho quyết định
    trước khi có sổ). Nhờ vậy bảng "ĐÃ ĐO RỒI BÁC" — ô đầu là văn xuôi — không bị
    tính oan. 🔴 Ô đầu phải giữ nguyên chữ `QD-`: S12 tìm chuỗi đó để xác nhận con
    trỏ trong `soat_nguong.json` không trỏ vào số ma."""
    try:
        tran = nguong()["so_quyetdinh"]["tran_dong"]
    except (OSError, ValueError, KeyError):
        return []                              # config hỏng: S12 kêu ĐỎ
    p = khung.GOC / "QUYETDINH.md"
    if not p.exists():
        return []
    ra = []
    for i, dong in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        m = re.match(r"\|\s*(?:⚰️\s*)?(QD-\d+|—)\s*\|", dong)
        if not m or len(dong) <= tran:
            continue
        so = m.group(1)
        khoa = f"QUYETDINH.md|{so}" if so != "—" else f"QUYETDINH.md|dong {i}"
        ra.append(PhatHien(khoa, i, f"{len(dong)} ky tu > tran {tran} — mot quyet dinh MOT dong; "
                                    f"cat bot, hoac day chi tiet sang `git log --grep`"))
    return ra


_MOC_DADO = "📏 ĐÃ ĐO RỒI BÁC"
_MOC_SO = "🗂️ SỔ QUYẾT ĐỊNH"

def so_hieu_da_biet():
    """Mọi số hiệu `QD-nn` từng tồn tại = **sổ sống + `git log`** (QD-29).

    🔴 KHO LƯU TRỮ LÀ `git log`, KHÔNG phải một file `.md` song song. Bản dựng đầu
    ngày 04/08 có đẻ ra `QUYETDINH-LUUTRU.md` để hứng mục rời sổ — user hỏi đúng
    một câu giết nó: *"sao không dùng luôn git?"*. Đo lại thì git **che phủ 100%**:
    cả 25 số hiệu đã rời sổ đều có commit nhắc tới, thân dài **1.542–4.089 ký tự**,
    tức gấp 6–16 lần dòng bảng 250 ký tự mà nó thay thế. Quét TOÀN BỘ thân commit
    hết **0,08 giây** cho một lệnh. File kia không thêm được gì, mà lại tái phạm
    đúng lỗi QD-06 đã đóng sổ: dựng tài liệu song song rồi để nó lệch dần.

    Vẫn phải hỏi cả sổ SỐNG chứ không chỉ git: quyết định vừa viết trong cây làm
    việc mà CHƯA commit thì `git log` chưa thấy — chỉ nhìn git là cửa kêu oan đúng
    lúc người ta đang viết quyết định mới.
    """
    ra = set()
    try:
        ra |= set(re.findall(r"QD-\d+",
                             (khung.GOC / "QUYETDINH.md").read_text(encoding="utf-8")))
    except OSError:
        pass            # chưa có sổ (repo giả trong test) — git bên dưới vẫn trả lời
    try:
        than = subprocess.run(["git", "log", "--format=%B"], cwd=str(khung.GOC),
                              capture_output=True, text=True, encoding="utf-8",
                              errors="replace", timeout=30).stdout or ""
        ra |= set(re.findall(r"QD-\d+", than))
    except (OSError, subprocess.SubprocessError):
        pass            # không có git / chưa có commit nào: sổ sống ở trên là
        # nguồn duy nhất còn lại, và cửa gọi hàm này tự kêu nếu hụt số hiệu thật
    return ra


def _dem_dong_bang(p, tu, den):
    """Đếm dòng DỮ LIỆU của bảng nằm giữa hai mốc tiêu đề.

    🔴 Đếm theo RANH GIỚI MỤC, không theo hình dạng chữ trong ô. Bản nháp đầu
    tiên dò bằng regex nội dung và **đếm hụt 2/11 dòng** — hai dòng có chữ đuôi
    sau ô phán quyết (`**BÁC** (AI đã suy sai 04/08)`). Cửa đếm hụt còn tệ hơn
    không có cửa: nó báo XANH trong khi bảng đã tràn.
    """
    if not p.exists():
        return 0
    noi_dung = p.read_text(encoding="utf-8")
    i = noi_dung.find(tu)
    if i < 0:
        return 0
    j = noi_dung.find(den, i) if den else len(noi_dung)
    khuc = noi_dung[i:j if j > 0 else len(noi_dung)]
    return sum(1 for d in khuc.splitlines()
               if d.startswith("|") and not re.match(r"\|[\s:|-]+\|$", d)
               and "Vì sao (ngắn)" not in d and "Vì (số liệu thật)" not in d)


def s20_suc_chua_co_dinh():
    """🔴 SINH PHẢI BẰNG TỬ — cửa QUAN TRỌNG NHẤT của bộ này (QD-29, 04/08/2026).

    Vì sao nó tồn tại: dự án đã tự động hoá hoàn hảo vế SINH (hook nhắc mỗi lượt,
    ba playbook, luật "quyết định nào đổi code thì ghi vết NGAY"), nhưng vế CHẾT
    thì phó mặc ý chí — phải có ai đó tự nhớ ra, đọc lại, phán là dòng này chết
    rồi. Không máy nào làm. Một hệ trí nhớ phình vô hạn khi và chỉ khi
    **tốc độ sinh > tốc độ chết**, nên mọi cửa đếm KÍCH CỠ đều chỉ chữa triệu
    chứng: trần ký tự không tạo ra tỷ lệ chết, nó chỉ khiến việc sinh ra ĐAU, rồi
    thu phần chênh lệch thành thuế nén chữ mỗi phiên. Đo 04/08: để thêm 3 dòng,
    phiên đó phải nén 4 dòng + xoá 1 + gộp 2.

    🔴 Và nén thì mất phần VÌ SAO — thứ duy nhất còn dùng được khi gặp tình huống
    mới. Đúng cái bệnh QD-28 đã đặt tên: luật nào bị luật khác phạt thì luật đó
    thua. L bắt ghi quyết định · S15 phạt sổ dài ⇒ thua sẽ là luật ghi cho tử tế.

    Cửa này chữa tận gốc: **sức chứa CỐ ĐỊNH**. Muốn thêm một dòng thì phải bỏ
    một dòng, và "bỏ" nay rẻ vì `git log` đã hứng sẵn toàn văn — `git log --grep
    QD-nn` ra nguyên văn, không mất gì (xem `so_hieu_da_biet` để biết vì sao KHÔNG
    đẻ file lưu trữ song song).

    ⚠️ KHÁC S13/S17: hai cửa kia là RATCHET (chỉ cho giảm) vì chúng đếm VI PHẠM,
    mà vi phạm thì đích đến là 0. Quyết định không phải vi phạm — đích đến không
    phải 0, mà là MỘT HẰNG SỐ. Sổ được đánh chỉ số bởi *số mảng của hệ thống* và
    *số đánh đổi người còn phải tự cân*, không phải bởi số sự thật đã biết:
    một tấm bản đồ không dài ra theo số viên gạch.
    """
    try:
        ng = nguong()["so_quyetdinh"]
        tran_qd, tran_dado = ng["tran_so_quyetdinh"], ng["tran_so_dado"]
    except (OSError, ValueError, KeyError):
        return []                              # config hỏng: S12 kêu ĐỎ
    p = khung.GOC / "QUYETDINH.md"
    ra = []
    for ten, tu, den, tran in (("so quyet dinh", _MOC_SO, None, tran_qd),
                               ("bang DA DO ROI BAC", _MOC_DADO, _MOC_SO, tran_dado)):
        n = _dem_dong_bang(p, tu, den)
        if n > tran:
            ra.append(PhatHien(
                f"QUYETDINH.md|{ten}", n,
                f"{n} dong > suc chua {tran} — SINH PHAI BANG TU: muon them mot dong thi "
                f"phai bo mot dong (toan van da o `git log --grep`, khong mat gi), "
                f"KHONG duoc nen chu de nhet them"))

    # 🔴 CHỐT CHỐNG TRỎ HỤT. Cả cơ chế "cho phép chết" đứng trên một lời hứa: dời
    # một dòng sang kho lưu trữ thì `grep QD-nn` vẫn ra. Lời hứa đó mà gãy im
    # lặng thì lần dời sau là mất thật, và không ai biết cho tới khi có người đi
    # tra một số hiệu không còn tồn tại.
    da_biet = so_hieu_da_biet()
    for p in khung.cac_file_py():
        # ⚠️ MIỄN TRỪ `tests/`: test DỰNG SẴN trạng thái sai để kiểm cửa soát —
        # `test_soatkientruc.py` cố ý trỏ một số hiệu KHÔNG tồn tại để chứng minh
        # S12 bắt được số ma. Kêu ở đó là đi tố cáo chính bài test của cửa kia.
        # (Và cấm viết số giả ấy ra đây: chính cửa này sẽ bắt luôn comment này.)
        if khung.duong_dan(p).startswith("tests/"):
            continue
        try:
            src = p.read_text(encoding="utf-8")
        except OSError:
            continue
        for so in sorted(set(re.findall(r"QD-\d\d", src)) - da_biet):
            ra.append(PhatHien(khung.duong_dan(p), 0,
                               f"trich {so} nhung KHONG co trong QUYETDINH.md lan `git log` "
                               f"— con tro hut, sua trich dan hoac khoi phuc muc"))
    return ra


def s16_no_da_tra_con_nam_lai():
    """`SONO.md` chỉ được chứa nợ CHƯA trả — trả xong thì XOÁ DÒNG, đừng `- [x]` rồi
    để đó (QD-24). Đo 03/08: xác nợ chiếm **67%** file, và làm hỏng luôn cái ngòi
    "sổ chạm 10 mục thì dành một phiên trả nợ" vì nó đếm cả xác.

    Không dùng ngưỡng số nào — luật là NHỊ PHÂN, có `- [x]` là sai."""
    p = khung.GOC / "SONO.md"
    if not p.exists():
        return []
    ra = []
    for i, dong in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        if dong.lstrip().startswith("- [x]"):
            ra.append(PhatHien(f"SONO.md|dong {i}", i,
                               "no da tra van nam lai — XOA dong; bai hoc con song thi doi sang "
                               "noi duoc doc (vung im lang KIENTRUC.md, comment canh code)"))
    return ra


def s14_phienban_tran():
    """`PHIENBAN.md` giữ tối đa N bản, mỗi bản tối đa M gạch đầu dòng (QD-07) —
    con số từng nêu ở 4 file mà 0 cửa canh, nay máy đếm thật."""
    try:
        ng = nguong()["phienban"]
    except (OSError, ValueError, KeyError):
        return []
    p = khung.GOC / "PHIENBAN.md"
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


def s18_sono_dong_dai_hoac_qua_han():
    """`SONO.md`: MỘT NỢ = MỘT DÒNG BẢNG, và **bắt buộc có HẠN XOÁ** (QD-25).

    Vì sao cần: sổ nợ trước đây là văn xuôi tự do, nên một món nợ ghi 04/08 phình
    thành **10 dòng log** — đúng cái đã giết `CHANGELOG.md`. Trần thì `S10` đã
    canh cho cả file, nhưng trần TỔNG không chặn được một mục nuốt hết ngân sách
    của các mục khác; phải đếm TỪNG DÒNG, giống `S15` làm với `QUYETDINH.md`.

    Hạn xoá là vế thứ hai và là vế thiếu hẳn trước đây: không có hạn thì món nợ
    nằm im vĩnh viễn, sổ chỉ dài ra chứ không bao giờ ngắn lại. Quá hạn ⇒ ĐỎ,
    chặn deploy, buộc người sửa QUYẾT LẠI (trả nợ, hoặc gia hạn kèm lý do mới).
    """
    try:
        ng = nguong()["so_no"]
    except (OSError, ValueError, KeyError):
        return []                              # config hỏng: S12 kêu ĐỎ
    p = khung.GOC / "SONO.md"
    if not p.exists():
        return []
    hom_nay = date.today().isoformat()
    ra = []
    for i, dong in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        o = [x.strip() for x in dong.split("|")]
        # Dòng nợ = dòng bảng có đủ 3 ô và KHÔNG phải header/gạch ngăn.
        if len(o) < 5 or set(dong) <= set("|- :") or o[1].startswith("Nợ"):
            continue
        ten = re.sub(r"[*`🔴]", "", o[1])[:40]
        if len(dong) > ng["tran_dong"]:
            ra.append(PhatHien(f"SONO.md|{ten}", i,
                               f"{len(dong)} ky tu > tran {ng['tran_dong']} — mot no MOT dong; "
                               f"chi tiet day sang `git log --grep`"))
        han = o[3]
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", han):
            ra.append(PhatHien(f"SONO.md|{ten}", i,
                               f"thieu HAN XOA (o cuoi = {han!r}) — phai la ngay YYYY-MM-DD (QD-25)"))
        elif han < hom_nay:
            ra.append(PhatHien(f"SONO.md|{ten}", i,
                               f"QUA HAN {han} — tra no (xoa dong) hoac gia han kem ly do moi"))
    return ra


def s19_viecdanglam_con_ton():
    """`VIECDANGLAM.md` xong phiên phải TRỐNG, hoặc còn đúng **một** đầu việc.

    User chốt 04/08. Phiếu này là thứ phiên sau đọc đầu tiên; để tồn nhiều đầu việc
    thì nó thành sổ nợ thứ hai — mà nợ đã có `SONO.md`, hai sổ song song thì không
    sổ nào được tin. 🔴 Đếm `##` KHÔNG đủ, phải đếm CẢ SỐ DÒNG — vì sao: QD-32.
    """
    try:
        ng = nguong()["viecdanglam"]
        tran, tran_dong = ng["tran_muc"], ng["tran_dong"]
    except (OSError, ValueError, KeyError):
        return []                              # config hỏng: S12 kêu ĐỎ
    p = khung.GOC / "VIECDANGLAM.md"
    if not p.exists():
        return []
    dong = p.read_text(encoding="utf-8").splitlines()
    ra = []
    if len([d for d in dong if re.match(r"##\s+\S", d)]) > tran:
        ra.append(PhatHien("VIECDANGLAM.md", 0,
                           f"nhieu hon {tran} dau viec — viec chua lam day sang SONO.md kem HAN XOA"))
    if len(dong) > tran_dong:
        ra.append(PhatHien("VIECDANGLAM.md", 0,
                           f"{len(dong)} dong > tran {tran_dong} — dai the nay la dang CHUA NO trong "
                           f"doan van (du chi mot muc ##); no sang SONO.md, luat chung sang file "
                           f"nguoi ta doc luc can"))
    return ra
