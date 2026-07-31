# -*- coding: utf-8 -*-
"""MỖI BUG ĐÃ TRẢ HỌC PHÍ = MỘT TEST.

Vì sao có thư mục này (SONO.md 31/07/2026): `soatkientruc.py` chỉ bắt lỗi CẤU TRÚC
(ai gọi ai, file nằm đâu). Lỗi LOGIC — thẻ sai nghĩa, badge sai giống, `ё` hỏng âm
thầm — trước nay **không có gì bắt ngoài mắt user**. Mọi bug đắt nhất của dự án
đều thuộc loại đó, và user luôn là người phát hiện. Đây là bước đầu chuyển việc
phát hiện từ mắt user sang máy.

Nguyên tắc chọn cái gì test — CỐ Ý HẸP, để bộ test không phình thành thứ không ai
chạy: **chỉ test những chỗ ĐÃ HỎNG THẬT một lần**, mỗi ca ghi rõ bug gốc. Không
test hàm chưa từng gây sự cố, không đuổi theo độ phủ.

KHÔNG cần Anki, KHÔNG cần mạng — chạy được mọi lúc, đó là điều kiện để nó hữu ích:

    python -m unittest discover -s tests -v
"""
import os
import sys
import unicodedata
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from anki_tools import grammar                                       # noqa: E402
from anki_tools.html_builder import (_build_example_block,           # noqa: E402
                                     parse_examples_html)
from anki_tools.utils import (apply_hl, hl_to_bracket,               # noqa: E402
                              convert_stress_to_combining_accent,
                              strip_accents_perfectly)

ACUTE = "́"          # dấu trọng âm tổ hợp, đứng SAU nguyên âm


class ChuanHoaTiengNga(unittest.TestCase):
    """BUG GỐC: hai hàm chuẩn hoá lệch nhau ⇒ `ё` hỏng IM LẶNG (CLAUDE.md, bẫy 1)."""

    def test_bo_dau_trong_am_to_hop(self):
        self.assertEqual(strip_accents_perfectly("сло" + ACUTE + "во"), "слово")

    def test_giu_nguyen_chu_e_kep(self):
        # `ё` là CHỮ RIÊNG, không phải `е` có dấu — bỏ nhầm là sai chính tả.
        self.assertEqual(strip_accents_perfectly("ёлка"), "ёлка")

    def test_ha_thuong(self):
        self.assertEqual(strip_accents_perfectly("МОСКВА"), "москва")

    def test_nhay_don_la_dau_trong_am_cua_tu_dien(self):
        # `nouns.csv` ghi trọng âm bằng dấu nháy SAU nguyên âm.
        self.assertEqual(strip_accents_perfectly("сло'во"), "слово")

    def test_doi_nhay_thanh_dau_to_hop(self):
        self.assertEqual(convert_stress_to_combining_accent("сло'во"), "сло" + ACUTE + "во")


class BadgeSaiTeHonBadgeTrong(unittest.TestCase):
    """BUG GỐC: `де́ньги` từng hiện `FEM ♀` — dạy user nói "э́та де́ньга".

    Luật đã chốt: KHÔNG chắc thì trả rỗng, đừng đoán bừa."""

    @staticmethod
    def _rec(nom, inst, animate=None):
        r = {"decl": {"sg": {"nom": nom, "inst": inst}}}
        if animate is not None:
            r["animate"] = animate
        return r

    def test_do_vat_duoi_a_la_giong_cai(self):
        # `дачка` — đồ vật (animate=False) nên đuôi -ой kết luận được.
        ma, ly_do = grammar.suy_giong(self._rec("да́чка", "да́чкой", animate=False))
        self.assertEqual(ma, "f")
        self.assertTrue(ly_do)                      # phải kèm bằng chứng, không phán suông

    def test_duoi_yu_la_giong_cai_bien_cach_III(self):
        self.assertEqual(grammar.suy_giong(self._rec("быль", "бы́лью"))[0], "f")

    def test_cach1_duoi_o_la_giong_trung(self):
        self.assertEqual(grammar.suy_giong(self._rec("окно́", "окно́м"))[0], "n")

    def test_phu_am_cuoi_la_giong_duc(self):
        self.assertEqual(grammar.suy_giong(self._rec("стол", "столо́м"))[0], "m")

    def test_KHONG_DOAN_BUA_voi_dya_dya(self):
        """`дя́дя` (chú) là giống ĐỰC nhưng biến cách y hệt giống cái.

        Test này BẮT ĐƯỢC BUG THẬT ngay lần chạy đầu 31/07/2026: hàm trả 'f'.
        Người/sinh vật (animate) đuôi -а/-я thì hình thái không đủ kết luận."""
        self.assertEqual(
            grammar.suy_giong(self._rec("дя́дя", "дя́дей", animate=True)), (None, None))

    def test_thieu_du_lieu_animate_thi_cung_khong_doan(self):
        # Không biết là người hay đồ vật ⇒ im lặng, đừng đoán.
        self.assertEqual(grammar.suy_giong(self._rec("па́па", "па́пой")), (None, None))

    def test_thieu_du_lieu_thi_khong_phan(self):
        self.assertEqual(grammar.suy_giong({}), (None, None))
        self.assertEqual(grammar.suy_giong(self._rec("стол", "")), (None, None))


class HighlightKhongBiNuot(unittest.TestCase):
    """BUG GỐC: regex bóc ngược HTML **nuốt mất `</hl>`** khi bot đọc lại thẻ
    (memory `bot-nhu-tu-dien`). Câu tiếng Việt bọc `<span class="vi-text">` lại có
    thể chứa `<span class="hl">` LỒNG bên trong — cắt sai là mất chữ."""

    def test_apply_hl_doi_dung_ca_hai_dau(self):
        self.assertEqual(apply_hl("Э́то <hl>дом</hl>."),
                         'Э́то <span class="hl">дом</span>.')

    def test_hl_to_bracket(self):
        self.assertEqual(hl_to_bracket("Э́то <hl>дом</hl>."), "Э́то [дом].")

    def test_dung_roi_boc_lai_KHONG_MAT_CHU(self):
        """Vòng tròn dựng → bóc: đây là phép thử bắt được lỗi nuốt thẻ đóng."""
        khoi = _build_example_block(1, "Э́то <hl>дом</hl>.", "This is a house.",
                                    "Đây là <hl>ngôi nhà</hl>.")
        ra = parse_examples_html(khoi)
        self.assertEqual(len(ra), 1)
        self.assertIn("дом", ra[0]["ru"])
        self.assertEqual(ra[0]["en"], "This is a house.")
        # Chữ CUỐI của câu Việt phải còn — chỗ regex tham lam từng cắt cụt.
        self.assertTrue(ra[0]["vi"].endswith("."), f"cau Viet bi cat cut: {ra[0]['vi']!r}")
        self.assertIn("ngôi nhà", ra[0]["vi"])

    def test_hai_vi_du_khong_lan_sang_nhau(self):
        hai = (_build_example_block(1, "Пе́рвый.", "First.", "Thứ <hl>nhất</hl>.")
               + _build_example_block(2, "Второ́й.", "Second.", "Thứ hai."))
        ra = parse_examples_html(hai)
        self.assertEqual(len(ra), 2)
        self.assertNotIn("hai", ra[0]["vi"])        # ví dụ 1 không được nuốt ví dụ 2


class BocKhoiBangChia(unittest.TestCase):
    """`_BANG_RE` tách khối bảng chia khỏi phần người soạn viết. Sai regex ở đây
    là `dodai`/`soat` đo nhầm cả phần máy nối vào (memory
    `cua-soat-khong-do-phan-may-noi`)."""

    def test_boc_dung_khoi_bang(self):
        html = ('Ph<b>ần</b> ngu<i>ời</i> so<u>ạn</u>'
                '<details class="gt-bang"><summary>Bảng</summary>RUỘT</details>'
                'phần đuôi')
        con_lai = grammar.BANG_RE.sub("", html)
        self.assertNotIn("RUỘT", con_lai)
        self.assertIn("phần đuôi", con_lai)

    def test_khong_co_bang_thi_giu_nguyen(self):
        html = "chỉ là chữ thường"
        self.assertEqual(grammar.BANG_RE.sub("", html), html)


class DauTrongAmPhaiLaMotKyTuDUYNHAT(unittest.TestCase):
    """BUG GỐC 31/07/2026: OpenRussian trả `U+0341 COMBINING ACUTE TONE MARK`
    (lỗi thời) thay vì `U+0301 COMBINING ACUTE ACCENT` mà cả dự án dùng.

    Hai ký tự HIỆN RA Y HỆT NHAU — mắt không bao giờ bắt được. Hậu quả im lặng:
    hàm bỏ dấu trọng âm chỉ biết `\\u0301` nên bỏ sót; Anki lại tự chuẩn hoá NFC
    lúc ghi ⇒ thẻ và cache lệch nhau vĩnh viễn. Tìm ra khi đồng bộ toàn bộ thẻ:
    975/976 khớp, đúng một thẻ `бу́ква` lệch mà nhìn thì giống hệt."""

    XAU = "\u0341"                          # tone mark, da loi thoi
    TOT = "\u0301"                          # acute accent, chuan cua du an

    def test_hai_ky_tu_nay_that_su_khac_nhau(self):
        """Chốt lại điều phản trực giác: nhìn giống nhau, byte khác nhau."""
        self.assertNotEqual(self.XAU, self.TOT)
        self.assertEqual(unicodedata.normalize("NFC", "а" + self.XAU),
                         unicodedata.normalize("NFC", "а" + self.TOT))

    def test_ham_bo_dau_KHONG_bo_noi_ky_tu_loi_thoi(self):
        """Vì sao phải chặn từ cửa ghi chứ không trông vào hàm bỏ dấu."""
        self.assertEqual(strip_accents_perfectly("бу" + self.TOT + "ква"), "буква")
        self.assertNotEqual(strip_accents_perfectly("бу" + self.XAU + "ква"), "буква")

    def test_CACHE_THAT_khong_duoc_chua_ky_tu_loi_thoi(self):
        """Bất biến trên DỮ LIỆU THẬT — bắt được cả khi lỗi tới từ nguồn."""
        duong = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                             "data", "grammar_cache.json")
        if not os.path.exists(duong):
            self.skipTest("khong co cache tren may nay")
        with open(duong, encoding="utf-8") as f:
            noi_dung = f.read()
        self.assertNotIn(self.XAU, noi_dung,
                         "cache lai chua U+0341 — kiem `_save_cache` con chuan hoa NFC khong")


class AliasPublicConSong(unittest.TestCase):
    """Alias public thêm ở G4 (QD-02) là hợp đồng cho ngày tách `grammar.py`.
    Ai lỡ xoá thì phải gãy Ở ĐÂY, không phải gãy trên máy chủ lúc nửa đêm."""

    def test_grammar(self):
        self.assertIs(grammar.BANG_RE, grammar._BANG_RE)
        self.assertIs(grammar.doc_cache, grammar._cache)
        self.assertIs(grammar.luu_cache, grammar._save_cache)

    def test_ai_client(self):
        from anki_tools import ai_client
        self.assertIs(ai_client.parse_ai_response, ai_client._parse_ai_response)
        self.assertIs(ai_client.send_ai_request, ai_client._send_ai_request)


if __name__ == "__main__":
    unittest.main()
