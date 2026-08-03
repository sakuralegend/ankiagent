# -*- coding: utf-8 -*-
"""Test cho CHÍNH CỬA SOÁT `soatkientruc.py` — trả nợ SONO 31/07/2026.

Thứ đang chặn deploy mà sai thì hoặc chặn oan hoặc bỏ lọt, không ai biết.
Cách kiểm: dựng REPO GIẢ trong thư mục tạm, trỏ `soatkientruc.GOC` vào đó,
gọi thẳng từng hàm `s*` và kỳ vọng ĐÚNG mục nào kêu / mục nào im.

⚠️ Chuỗi mồi (cổng AnkiConnect, tên lớp HTML) phải GHÉP lúc chạy — viết trần
trong file này là chính S1/S5 quét trúng file test và kêu oan.
"""
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import soatkientruc as sk

CONG = "87" + "65"                     # "8765" — ghép để S1 không bắt file test


class TestSoatKienTruc(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="soat_test_"))
        self._goc_cu, self._baseline_cu = sk.GOC, sk.BASELINE
        sk.GOC = self.tmp
        sk.BASELINE = self.tmp / "soat_baseline.json"

    def tearDown(self):
        sk.GOC, sk.BASELINE = self._goc_cu, self._baseline_cu
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
        khoa = [ph.khoa for ph in sk.s1_cong_anki()]
        self.assertIn("tgbot/lau.py", khoa)
        self.assertNotIn("tgbot/sach.py", khoa)

    # --- S2: gọi tên private xuyên gói ------------------------------------
    def test_s2_bat_xuyen_goi_va_tha_cung_goi(self):
        self.ghi("tgbot/x.py", "from anki_tools.grammar import _cache\n")
        self.ghi("anki_tools/grammar.py", "_cache = 1\n")
        self.ghi("anki_tools/noi_bo.py", "from anki_tools.grammar import _cache\n")
        khoa = [ph.khoa for ph in sk.s2_private_xuyen_goi()]
        self.assertIn("tgbot/x.py|_cache", khoa)
        self.assertNotIn("anki_tools/noi_bo.py|_cache", khoa)

    # --- S3: flow import ngang flow ---------------------------------------
    def test_s3_bat_flow_goi_flow(self):
        self.ghi("tgbot/flow_a.py", "from flow_b import lam\n")
        self.ghi("tgbot/flow_b.py", "from core import x\n")   # flow -> core: hợp lệ
        khoa = [ph.khoa for ph in sk.s3_tgbot_tang()]
        self.assertEqual(khoa, ["tgbot/flow_a.py|flow_b"])

    # --- S4: MIEN_TRU chỉ được một nơi ------------------------------------
    def test_s4_hai_noi_la_do_mot_noi_thi_im(self):
        self.ghi("data/huongdan/mientru.py", "MIEN_TRU = {'a'}\n")
        self.assertEqual(sk.s4_mientru_mot_noi(), [])
        self.ghi("data/huongdan/kho/khac.py", "MIEN_TRU = {'b'}\n")
        self.assertEqual(len(sk.s4_mientru_mot_noi()), 2)

    # --- S6: thư mục gốc chỉ có ba điểm vào -------------------------------
    def test_s6_bat_file_la_o_goc(self):
        for ten in ("bot.py", "main.py", "soatkientruc.py", "lachong.py"):
            self.ghi(ten, "x = 1\n")
        khoa = [ph.khoa for ph in sk.s6_goc_sach()]
        self.assertEqual(khoa, ["lachong.py"])

    # --- S7: lô thế hệ 1 phải còn ngòi KHAI TU ----------------------------
    def test_s7_lo_mat_guard_la_do(self):
        self.ghi("data/huongdan/lo01_x.py",
                 '"""lo cu."""\nraise SystemExit("KHAI TU 30/07/2026")\nS = {}\n')
        self.ghi("data/huongdan/lo02_y.py", '"""lo cu."""\nS = {}\n')
        khoa = [ph.khoa for ph in sk.s7_lo_da_khai_tu()]
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
        khoa = [ph.khoa for ph in sk.s8_manifest()]
        self.assertIn("KIENTRUC.md|goi:goi_ma", khoa)       # khai mà không có
        self.assertIn("KIENTRUC.md|goi:goi_that", khoa)     # có mà không khai
        self.assertIn("KIENTRUC.md|diem_vao:thieu.py", khoa)

    def test_s8_ngu_khi_chua_co_kientruc(self):
        self.assertIsNone(sk.s8_manifest())

    # --- S10: trần đọc, đếm KÝ TỰ chứ không đếm dòng (QD-20) --------------
    def _dat_tran(self, ten, phut):
        """Trỏ PHUT_DOC vào đúng một file giả, trả lại nguyên trạng sau test."""
        cu = sk.PHUT_DOC
        sk.PHUT_DOC = {ten: phut}
        self.addCleanup(lambda: setattr(sk, "PHUT_DOC", cu))

    def test_s10_duoi_tran_thi_im(self):
        self._dat_tran("A.md", 1)
        self.ghi("A.md", "x" * (sk.KY_TU_MOI_PHUT - 1))
        self.assertEqual(sk.s10_tri_nho_phinh(), [])

    def test_s10_vuot_tran_thi_keu_bang_ky_tu(self):
        self._dat_tran("A.md", 1)
        self.ghi("A.md", "x" * (sk.KY_TU_MOI_PHUT + 1))
        ra = sk.s10_tri_nho_phinh()
        self.assertEqual([ph.khoa for ph in ra], ["A.md"])
        self.assertIn("ky tu", ra[0].mo_ta)

    def test_s10_it_dong_ma_dong_dai_van_bi_bat(self):
        """🔴 Ca mà bản đếm-dòng BỎ LỌT — chính nó đẻ ra QD-20.

        `QUYETDINH.md` từng báo 149/150 dòng "còn chỗ" trong khi nặng 30 KB,
        dòng dài nhất 1090 ký tự. Ba dòng dưới đây là bản thu nhỏ của đúng ca
        đó: rất ít dòng, thừa sức lọt mọi trần tính bằng dòng, mà chữ thì vượt.
        """
        self._dat_tran("A.md", 1)
        self.ghi("A.md", "\n".join(["y" * 900] * 3))      # 3 dòng, ~2 700 ký tự
        self.assertEqual([ph.khoa for ph in sk.s10_tri_nho_phinh()], ["A.md"])

    def test_s10_file_khong_ton_tai_thi_bo_qua(self):
        self._dat_tran("khong_co.md", 1)
        self.assertEqual(sk.s10_tri_nho_phinh(), [])

    # --- ratchet: baseline chỉ che đúng số cũ, vượt là lộ -----------------
    def test_baseline_doc_kieu_dict_va_so_tran(self):
        self.assertEqual(sk._so_cua(3), 3)
        self.assertEqual(sk._so_cua({"so": 2, "vi_sao": "x"}), 2)
        self.assertEqual(sk._so_cua(None), 0)


if __name__ == "__main__":
    unittest.main()
