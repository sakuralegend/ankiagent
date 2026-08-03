# -*- coding: utf-8 -*-
"""CỬA SOÁT KIẾN TRÚC — máy canh những luật mà tài liệu không tự thi hành được:
chỗ có máy đo thì sạch, chỗ luật chỉ nằm trong đầu người thì trôi (G1).
    python soatkientruc.py          # kiểm — exit 1 khi có ĐỎ
    python soatkientruc.py --chot   # chốt baseline mới (CHỈ được giảm)

File này chỉ còn ĐIỂM VÀO + bảng đăng ký cửa + ratchet; ruột từng cửa ở gói
`soat/` (QD-22, tách 03/08 khi chạm trần 700 dòng).

🔴 KHÔNG import module nào của dự án — import là kéo theo tác dụng phụ (telegram,
CSV 8,4 MB, `setup_anki_environment`), mà bộ soát có tác dụng phụ thì không ai
dám chạy. `soat/` KHÔNG phải ngoại lệ của luật này: nó là ruột của chính bộ soát,
cũng chỉ dùng stdlib (`pathlib` + `ast` phân tích tĩnh + regex).

🟡 VÀNG vs 🔴 ĐỎ — "bộ soát kêu oan là bộ soát chết": nợ tồn đọng là VÀNG, im tới
khi TĂNG; chỉ ĐỎ với vi phạm MỚI hoặc lỗi một-lần-là-hại. Ratchet
`soat_baseline.json`: `--chot` chỉ ghi được số THẤP HƠN ⇒ nợ không mọc lại.
"""
import json
import sys

from soat import cua_code, cua_nguong, cua_quytrinh, khung


def inn(msg=""):
    """print() không được làm chết bộ soát: console Windows cp1252 không in nổi
    emoji/tiếng Việt (`congcu.py` từng chết vì đúng lỗi in ấn này)."""
    try:
        print(msg)
    except UnicodeEncodeError:
        print(msg.encode("ascii", errors="replace").decode("ascii"))


# `luon_do=True`: MỘT lần lọt là đã hại — vi phạm nào cũng ĐỎ, bất kể baseline.
MUC = [
    ("S1", "CUA LAU TOI ANKICONNECT (L1)", cua_code.s1_cong_anki, False),
    ("S2", "GOI TEN PRIVATE XUYEN GOI", cua_code.s2_private_xuyen_goi, False),
    ("S3", "TGBOT: FLOW IMPORT NGANG FLOW", cua_code.s3_tgbot_tang, False),
    ("S4", "MIEN_TRU DINH NGHIA NHIEU NOI", cua_code.s4_mientru_mot_noi, True),
    ("S5", "HTML THE DUNG NGOAI html_builder", cua_code.s5_html_ngoai_builder, False),
    ("S6", "FILE .PY LA O THU MUC GOC (L2)", cua_code.s6_goc_sach, True),
    ("S7", "LO THE HE 1 MAT GUARD KHAI TU (QD-03)", cua_code.s7_lo_da_khai_tu, True),
    ("S8", "KIENTRUC.md LECH THUC TE", cua_code.s8_manifest, True),
    ("S9", "COMMIT DUNG CODE MA KHONG KHAI VI SAO", cua_quytrinh.s9_commit_thieu_vi_sao, True),
    ("S10", "FILE TRI NHO PHINH QUA TRAN", cua_nguong.s10_tri_nho_phinh, True),
    ("S11", "HOOK NHAC LUAT DA CHET (QD-13)", cua_quytrinh.s11_hook_con_song, True),
    ("S12", "soat_nguong.json TU MAU THUAN (QD-21)", cua_nguong.s12_nguong_hop_le, True),
    ("S13", "FILE CODE QUA TRAN DONG (QD-21)", cua_nguong.s13_tran_dong_code, True),
    ("S14", "PHIENBAN.md QUA TRAN BAN/MUC (QD-07)", cua_nguong.s14_phienban_tran, True),
]


def doc_baseline():
    if not khung.BASELINE.exists():
        return {}
    try:
        return json.loads(khung.BASELINE.read_text(encoding="utf-8"))
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

    khung.BASELINE.write_text(json.dumps(nen, ensure_ascii=False, indent=2) + "\n",
                              encoding="utf-8")
    inn(f"\nDa ghi {khung.BASELINE.name}.")


if __name__ == "__main__":
    ma_thoat, kq = chay()
    if "--chot" in sys.argv:
        inn("--- CHOT BASELINE ---")
        chot(kq)
        sys.exit(0)
    sys.exit(ma_thoat)
