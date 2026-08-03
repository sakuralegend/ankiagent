# -*- coding: utf-8 -*-
"""S10 · S12–S14 — các cửa canh CON SỐ TRẦN, tất cả đọc chung `soat_nguong.json`
(QD-21: một nguồn duy nhất, tài liệu chỉ trỏ).

Quy ước chung của file này: cửa nào cần số mà config hỏng/mất thì **im lặng**,
vì S12 đã kêu ĐỎ rồi — kêu ba lần cho một lỗi thì người đọc bắt đầu bỏ qua.
"""
import json
import re
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
    cắt mục đã hết giá trị, hay nâng ngân sách trong `soat_nguong.json` kèm QD-nn."""
    try:
        ng = nguong()
        toc_do, tran_phut = ng["ky_tu_moi_phut"]["so"], ng["phut_doc"]["tran"]
    except (OSError, ValueError, KeyError):
        return []                              # soat_nguong.json hỏng: S12 kêu ĐỎ
    ra = []
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
    try:
        qd_that = set(re.findall(r"QD-\d+", (khung.GOC / "QUYETDINH.md").read_text(encoding="utf-8")))
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
