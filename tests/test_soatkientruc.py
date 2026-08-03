# -*- coding: utf-8 -*-
"""Test cho CHÍNH CỬA SOÁT `soatkientruc.py` — trả nợ SONO 31/07/2026.

Thứ đang chặn deploy mà sai thì hoặc chặn oan hoặc bỏ lọt, không ai biết.
Cách kiểm: dựng REPO GIẢ trong thư mục tạm, trỏ `khung.GOC` vào đó bằng
`khung.dat_goc()`, gọi thẳng từng hàm `s*` và kỳ vọng ĐÚNG mục nào kêu / mục nào im.

⚠️ Chuỗi mồi (cổng AnkiConnect, tên lớp HTML) phải GHÉP lúc chạy — viết trần
trong file này là chính S1/S5 quét trúng file test và kêu oan.
"""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import soatkientruc as sk
from soat import cua_code, cua_nguong, khung

CONG = "87" + "65"                     # "8765" — ghép để S1 không bắt file test
KT_MOI_PHUT = 1400                     # khớp `ky_tu_moi_phut` trong config giả


class TestSoatKienTruc(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="soat_test_"))
        self._goc_cu = khung.GOC
        khung.dat_goc(self.tmp)
        # 🔴 LƯỚI CỦA LƯỚI — chạy ở MỌI ca, đừng gỡ. Ngày các cửa dọn sang chỗ
        # khác mà `dat_goc()` không còn với tới, mọi test dưới đây quay ra soi
        # repo THẬT (sạch, nên không thấy vi phạm nào) và XANH HẾT mà không kiểm
        # gì cả — lưới an toàn hỏng IM LẶNG. Repo giả vừa tạo phải RỖNG.
        thua = [khung.duong_dan(p) for p in khung.cac_file_py()]
        if thua:
            raise AssertionError(
                f"dat_goc() KHONG doi duoc thu muc goc — test dang soi repo THAT "
                f"({len(thua)} file .py, vd {thua[:3]}). Moi ket qua XANH deu vo nghia.")

    def tearDown(self):
        khung.dat_goc(self._goc_cu)
        shutil.rmtree(self.tmp, ignore_errors=True)

    def ghi(self, duong, noi_dung):
        p = self.tmp / duong
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(noi_dung, encoding="utf-8")
        return p

    # --- S1: cửa lậu tới AnkiConnect -------------------------------------
    def test_s1_bat_file_tro_thang_cong(self):
        self.ghi("tgbot/lau.py", f'URL = "http://127.0.0.1:{CONG}"\n')
        self.ghi("tgbot/sach.py", "x = 1\n")
        khoa = [ph.khoa for ph in cua_code.s1_cong_anki()]
        self.assertIn("tgbot/lau.py", khoa)
        self.assertNotIn("tgbot/sach.py", khoa)

    # --- S2: gọi tên private xuyên gói ------------------------------------
    def test_s2_bat_xuyen_goi_va_tha_cung_goi(self):
        self.ghi("tgbot/x.py", "from anki_tools.grammar import _cache\n")
        self.ghi("anki_tools/grammar.py", "_cache = 1\n")
        self.ghi("anki_tools/noi_bo.py", "from anki_tools.grammar import _cache\n")
        khoa = [ph.khoa for ph in cua_code.s2_private_xuyen_goi()]
        self.assertIn("tgbot/x.py|_cache", khoa)
        self.assertNotIn("anki_tools/noi_bo.py|_cache", khoa)

    # --- S3: flow import ngang flow ---------------------------------------
    def test_s3_bat_flow_goi_flow(self):
        self.ghi("tgbot/flow_a.py", "from flow_b import lam\n")
        self.ghi("tgbot/flow_b.py", "from core import x\n")   # flow -> core: hợp lệ
        khoa = [ph.khoa for ph in cua_code.s3_tgbot_tang()]
        self.assertEqual(khoa, ["tgbot/flow_a.py|flow_b"])

    # --- S4: MIEN_TRU chỉ được một nơi ------------------------------------
    def test_s4_hai_noi_la_do_mot_noi_thi_im(self):
        self.ghi("data/huongdan/mientru.py", "MIEN_TRU = {'a'}\n")
        self.assertEqual(cua_code.s4_mientru_mot_noi(), [])
        self.ghi("data/huongdan/kho/khac.py", "MIEN_TRU = {'b'}\n")
        self.assertEqual(len(cua_code.s4_mientru_mot_noi()), 2)

    # --- S6: thư mục gốc chỉ có ba điểm vào -------------------------------
    def test_s6_bat_file_la_o_goc(self):
        for ten in ("bot.py", "main.py", "soatkientruc.py", "lachong.py"):
            self.ghi(ten, "x = 1\n")
        khoa = [ph.khoa for ph in cua_code.s6_goc_sach()]
        self.assertEqual(khoa, ["lachong.py"])

    # --- S7: lô thế hệ 1 phải còn ngòi KHAI TU ----------------------------
    def test_s7_lo_mat_guard_la_do(self):
        self.ghi("data/huongdan/lo01_x.py",
                 '"""lo cu."""\nraise SystemExit("KHAI TU 30/07/2026")\nS = {}\n')
        self.ghi("data/huongdan/lo02_y.py", '"""lo cu."""\nS = {}\n')
        khoa = [ph.khoa for ph in cua_code.s7_lo_da_khai_tu()]
        self.assertNotIn("data/huongdan/lo01_x.py", khoa)
        self.assertIn("data/huongdan/lo02_y.py", khoa)

    # --- S8: manifest trong KIENTRUC.md phải khớp thực tế -----------------
    def test_s8_manifest_lech_thuc_te(self):
        (self.tmp / "goi_that").mkdir()
        self.ghi("goi_that/__init__.py", "")
        self.ghi("bot.py", "x = 1\n")
        self.ghi("KIENTRUC.md",
                 "# x\n```soat-manifest\n"
                 '{"goi": ["goi_ma"], "diem_vao": ["bot.py", "thieu.py"],'
                 ' "du_lieu_chung": []}\n```\n')
        khoa = [ph.khoa for ph in cua_code.s8_manifest()]
        self.assertIn("KIENTRUC.md|goi:goi_ma", khoa)       # khai mà không có
        self.assertIn("KIENTRUC.md|goi:goi_that", khoa)     # có mà không khai
        self.assertIn("KIENTRUC.md|diem_vao:thieu.py", khoa)

    def test_s8_ngu_khi_chua_co_kientruc(self):
        self.assertIsNone(cua_code.s8_manifest())

    # --- soat_nguong.json giả cho các mục đọc ngưỡng (QD-21) --------------
    def _nguong_gia(self, phut_doc=None, dong_py=None, phienban=None, so_qd=None, tho=None):
        """Ghi `soat_nguong.json` vào repo giả — test đi qua ĐÚNG bộ đọc thật.
        `tho` = chuỗi JSON thô, cho ca kiểm khoá trùng/parse hỏng."""
        if tho is None:
            cau = {"ky_tu_moi_phut": {"so": KT_MOI_PHUT, "qd": "QD-20"}}
            if phut_doc is not None:
                cau["phut_doc"] = {"qd": "QD-20", "tran": phut_doc}
            if dong_py is not None:
                cau["dong_py"] = {"qd": "QD-21", "ghi_no": 400, "tach": 700,
                                  "bo_qua_mau": [], "da_ghi_no": {}, **dong_py}
            if phienban is not None:
                cau["phienban"] = {"qd": "QD-07", "giu_ban": 10, "muc_moi_ban": 5,
                                   **phienban}
            if so_qd is not None:
                cau["so_quyetdinh"] = {"qd": "QD-23", "tran_dong": 250, **so_qd}
            tho = json.dumps(cau)
        self.ghi("soat_nguong.json", tho)

    # --- S10: trần đọc, đếm KÝ TỰ chứ không đếm dòng (QD-20) --------------
    def test_s10_duoi_tran_thi_im(self):
        self._nguong_gia(phut_doc={"A.md": 1})
        self.ghi("A.md", "x" * (KT_MOI_PHUT - 1))
        self.assertEqual(cua_nguong.s10_tri_nho_phinh(), [])

    def test_s10_vuot_tran_thi_keu_bang_ky_tu(self):
        self._nguong_gia(phut_doc={"A.md": 1})
        self.ghi("A.md", "x" * (KT_MOI_PHUT + 1))
        ra = cua_nguong.s10_tri_nho_phinh()
        self.assertEqual([ph.khoa for ph in ra], ["A.md"])
        self.assertIn("ky tu", ra[0].mo_ta)

    def test_s10_it_dong_ma_dong_dai_van_bi_bat(self):
        """🔴 Ca bản đếm-dòng BỎ LỌT — chính nó đẻ ra QD-20: rất ít dòng, lọt
        mọi trần tính bằng dòng, mà chữ thì vượt."""
        self._nguong_gia(phut_doc={"A.md": 1})
        self.ghi("A.md", "\n".join(["y" * 900] * 3))      # 3 dòng, ~2 700 ký tự
        self.assertEqual([ph.khoa for ph in cua_nguong.s10_tri_nho_phinh()], ["A.md"])

    def test_s10_file_khong_ton_tai_thi_bo_qua(self):
        self._nguong_gia(phut_doc={"khong_co.md": 1})
        self.assertEqual(cua_nguong.s10_tri_nho_phinh(), [])

    def test_s10_thieu_config_thi_im_de_s12_keu(self):
        """Config mất thì S10 không được nổ exception — S12 mới là nơi kêu ĐỎ."""
        self.assertEqual(cua_nguong.s10_tri_nho_phinh(), [])

    # --- S12: soat_nguong.json phải TỰ nhất quán (QD-21) ------------------
    def test_s12_thieu_file_la_do(self):
        ra = cua_nguong.s12_nguong_hop_le()
        self.assertEqual([ph.khoa for ph in ra], ["soat_nguong.json"])

    def test_s12_khoa_trung_la_do(self):
        """Một đích hai trần — JSON chuẩn lặng lẽ lấy giá trị sau, bộ đọc phải bắt."""
        self._nguong_gia(tho='{"phut_doc": {"qd": "QD-20", "tran": {"A.md": 1, "A.md": 2}}}')
        ra = cua_nguong.s12_nguong_hop_le()
        self.assertEqual([ph.khoa for ph in ra], ["soat_nguong.json"])
        self.assertIn("khoa trung", ra[0].mo_ta)

    def test_s12_tro_file_ma_va_qd_ma(self):
        self.ghi("QUYETDINH.md", "## QD-20 · x\n")
        self.ghi("A.md", "x\n")
        self._nguong_gia(phut_doc={"A.md": 1, "da_xoa.md": 1},
                         dong_py={"qd": "QD-99"})
        khoa = [ph.khoa for ph in cua_nguong.s12_nguong_hop_le()]
        self.assertIn("nguong|da_xoa.md", khoa)       # trần trỏ file đã xoá
        self.assertIn("nguong|dong_py", khoa)         # trỏ QD không tồn tại
        self.assertNotIn("nguong|A.md", khoa)

    # --- S13: trần dòng file code (QD-21) ---------------------------------
    def test_s13_vuot_ghi_no_ma_chua_khai_la_do(self):
        self._nguong_gia(dong_py={})
        self.ghi("tgbot/to.py", "x = 1\n" * 401)
        self.ghi("tgbot/nho.py", "x = 1\n" * 399)
        khoa = [ph.khoa for ph in cua_nguong.s13_tran_dong_code()]
        self.assertEqual(khoa, ["tgbot/to.py"])

    def test_s13_co_moc_thi_im_phinh_qua_moc_la_do(self):
        self._nguong_gia(dong_py={"da_ghi_no": {"tgbot/no.py": 430}})
        self.ghi("tgbot/no.py", "x = 1\n" * 420)
        self.assertEqual(cua_nguong.s13_tran_dong_code(), [])
        self.ghi("tgbot/no.py", "x = 1\n" * 431)
        self.assertEqual([ph.khoa for ph in cua_nguong.s13_tran_dong_code()], ["tgbot/no.py"])

    def test_s13_vuot_tran_tach_la_do_ke_ca_co_moc(self):
        self._nguong_gia(dong_py={"da_ghi_no": {"tgbot/qua.py": 999}})
        self.ghi("tgbot/qua.py", "x = 1\n" * 701)
        ra = cua_nguong.s13_tran_dong_code()
        self.assertEqual([ph.khoa for ph in ra], ["tgbot/qua.py"])
        self.assertIn("tach", ra[0].mo_ta)

    def test_s13_lo_du_lieu_kho_duoc_bo_qua(self):
        self._nguong_gia(dong_py={"bo_qua_mau": ["data/huongdan/kho/k*.py"]})
        self.ghi("data/huongdan/kho/k99_x.py", "x = 1\n" * 800)
        self.assertEqual(cua_nguong.s13_tran_dong_code(), [])

    # --- S14: PHIENBAN.md trần bản/mục (QD-07) ----------------------------
    def _phienban(self, so_ban, muc_moi_ban):
        than = "\n".join(f"## v1.0.{i}\n\n" + "- muc\n" * muc_moi_ban
                         for i in range(so_ban))
        self.ghi("PHIENBAN.md", "# Co gi moi\n\n" + than)

    def test_s14_dung_chuan_thi_im(self):
        self._nguong_gia(phienban={})
        self._phienban(so_ban=10, muc_moi_ban=5)
        self.assertEqual(cua_nguong.s14_phienban_tran(), [])

    def test_s14_qua_so_ban_la_do(self):
        self._nguong_gia(phienban={})
        self._phienban(so_ban=11, muc_moi_ban=2)
        self.assertEqual([ph.khoa for ph in cua_nguong.s14_phienban_tran()], ["PHIENBAN.md"])

    def test_s14_mot_ban_qua_nhieu_muc_la_do(self):
        self._nguong_gia(phienban={})
        self._phienban(so_ban=2, muc_moi_ban=6)
        self.assertEqual(len(cua_nguong.s14_phienban_tran()), 2)

    # --- S15: một quyết định MỘT dòng, trần ký tự (QD-23) ------------------
    def test_s15_dong_qua_tran_la_do_ngan_thi_im(self):
        self._nguong_gia(so_qd={"tran_dong": 100})
        self.ghi("QUYETDINH.md",
                 "| QD | Ngày | Quyết định | Vì sao |\n|---|---|---|---|\n"
                 "| QD-23 | 03/08 | ngan gon | vi the |\n"
                 "| ⚰️ QD-20 | 03/08 | " + "d" * 150 + " | x |\n")
        ra = cua_nguong.s15_dong_quyetdinh_dai()
        self.assertEqual([ph.khoa for ph in ra], ["QUYETDINH.md|QD-20"])
        self.assertIn("MOT dong", ra[0].mo_ta)

    def test_s15_bang_da_do_roi_bac_khong_bi_tinh_oan(self):
        """🔴 Bảng "ĐÃ ĐO RỒI BÁC" nằm cùng file và dòng của nó DÀI là đúng thiết kế
        — ô đầu là văn xuôi chứ không phải số hiệu, nên cửa phải bỏ qua."""
        self._nguong_gia(so_qd={"tran_dong": 100})
        self.ghi("QUYETDINH.md",
                 "| Huong nghe hop ly | Phan quyet | Vi |\n|---|---|---|\n"
                 "| Dung `_family()` cua OpenRussian de dung muc ho hang | BAC | "
                 + "n" * 150 + " |\n")
        self.assertEqual(cua_nguong.s15_dong_quyetdinh_dai(), [])

    # --- S16: nợ đã trả không được nằm lại (QD-24) ------------------------
    def test_s16_bat_no_da_tra_va_tha_no_chua_tra(self):
        self.ghi("SONO.md", "# no\n\n- [ ] con no that\n- [x] da tra roi ma van nam day\n")
        ra = cua_nguong.s16_no_da_tra_con_nam_lai()
        self.assertEqual([ph.khoa for ph in ra], ["SONO.md|dong 4"])
        self.assertIn("XOA dong", ra[0].mo_ta)

    def test_s16_so_sach_thi_im(self):
        self.ghi("SONO.md", "# no\n\n- [ ] con no that\n")
        self.assertEqual(cua_nguong.s16_no_da_tra_con_nam_lai(), [])

    # --- ratchet: baseline chỉ che đúng số cũ, vượt là lộ -----------------
    def test_baseline_doc_kieu_dict_va_so_tran(self):
        self.assertEqual(sk._so_cua(3), 3)
        self.assertEqual(sk._so_cua({"so": 2, "vi_sao": "x"}), 2)
        self.assertEqual(sk._so_cua(None), 0)


if __name__ == "__main__":
    unittest.main()
