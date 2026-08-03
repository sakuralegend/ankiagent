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
import unittest.mock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from anki_tools import grammar, soat_nguphap                         # noqa: E402
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


class TheLaNguonSuThat(unittest.TestCase):
    """QD-11: thẻ Anki là nguồn DUY NHẤT của dữ liệu ngữ pháp — không còn file
    cache trên đĩa làm bộ đệm dự phòng (thay QD-08: trước đó file cache + thẻ
    là hai bản dự phòng cho nhau, và hai bản giống hệt nhau đã lệch nhau âm thầm
    89 thẻ suốt nhiều tuần — đúng bug mà việc bỏ hẳn file cache triệt tiêu)."""

    def test_dong_anki_phai_KEU_TO_khong_duoc_im_lang(self):
        """QD-11: Anki đóng/lỗi phải NÉM LỖI, KHÔNG được coi là "không có dữ
        liệu" rồi trả rỗng — im lặng ở đây từng khiến lô soạn ghi thẻ THIẾU bảng
        chia mà không ai biết."""
        goc_da_hoi, goc_cache = grammar._DA_HOI_THE, grammar._CACHE
        try:
            grammar._DA_HOI_THE = False
            grammar._CACHE = {}
            with unittest.mock.patch(
                    "anki_tools.anki_client.doc_grammar_json_tat_ca",
                    side_effect=RuntimeError("gia lap Anki dong")):
                with self.assertRaises(RuntimeError):
                    grammar.get_cached("tu_khong_bao_gio_ton_tai_xyz")
        finally:
            grammar._DA_HOI_THE = goc_da_hoi
            grammar._CACHE = goc_cache

    def test_lap_dem_KHONG_DUOC_de_ban_ghi_dang_co(self):
        """Ô `GrammarJSON` hỏng/rỗng không được xoá mất thứ đang đúng trong đệm."""
        dem = grammar._cache()
        khoa = "khoa_thu_" + "x" * 5
        dem[khoa] = {"pos": "noun", "v": 99}
        goc = grammar._DA_HOI_THE
        try:
            grammar._DA_HOI_THE = True         # chặn gọi Anki thật trong test
            grammar._lap_dem_tu_the()
            self.assertEqual(dem[khoa], {"pos": "noun", "v": 99})
        finally:
            dem.pop(khoa, None)
            grammar._DA_HOI_THE = goc


class DuLieuNguPhapBiDaoCach(unittest.TestCase):
    """BUG GỐC (02/08/2026): OpenRussian trả `ке́ды` với cách 5 và cách 6 ĐỔI CHỖ
    nhau ở cả số ít lẫn số nhiều. Bảng chia do máy nối vào lúc ghi thẻ nên
    `soat`/`dodai` mù hoàn toàn — agent bắt được bằng mắt, may.

    Bản ghi dưới đây là DỮ LIỆU THẬT, chép từ `backups/_backup_grammarjson_kedy.json`.
    """

    KEDY_HONG = {"pos": "noun", "decl": {
        "sg": {"nom": "кед", "gen": "ке́да", "dat": "ке́ду", "acc": "кед",
               "inst": "ке́де", "prep": "ке́дом"},
        "pl": {"nom": "ке́ды", "gen": "ке́дов, кед", "dat": "ке́дам", "acc": "ке́ды",
               "inst": "ке́дах", "prep": "ке́дами"}}}

    def test_bat_dung_ban_ghi_that_bi_dao(self):
        ra = soat_nguphap.dao_cach_5_6(self.KEDY_HONG)
        self.assertEqual([so for so, _, _ in ra], ["sg", "pl"])

    def test_ban_da_va_thi_im(self):
        # Đúng thứ tự cột thì cửa phải câm — cửa kêu oan là cửa rồi cũng bị bỏ qua.
        self.assertEqual(soat_nguphap.dao_cach_5_6({"pos": "noun", "decl": {
            "sg": {"inst": "ке́дом", "prep": "ке́де"},
            "pl": {"inst": "ке́дами", "prep": "ке́дах"}}}), [])

    def test_khong_keu_oan_nhom_bat_quy_tac(self):
        # `людьми́` kết thúc bằng `-и` — đuôi HỢP LỆ của cách 6. Hỏi thiếu một vế
        # là báo nhầm ngay ca này, nên nó phải nằm trong bộ test.
        self.assertEqual(soat_nguphap.dao_cach_5_6({"pos": "noun", "decl": {
            "pl": {"inst": "людьми́", "prep": "лю́дях"}}}), [])

    def test_khong_keu_oan_cach_vi_tri_va_gioi_tu_dinh_kem(self):
        # Cách 6 hay được lưu kèm giới từ (`в году́`), và `-у` là cách vị trí thật.
        self.assertEqual(soat_nguphap.dao_cach_5_6({"pos": "noun", "decl": {
            "sg": {"inst": "го́дом", "prep": "в году́"}}}), [])

    def test_khong_keu_oan_danh_tu_bien_nhu_tinh_tu(self):
        # `моро́женое`: cách 6 kết thúc `-ом` là ĐÚNG, vì nó biến như tính từ.
        self.assertEqual(soat_nguphap.dao_cach_5_6({"pos": "noun", "decl": {
            "sg": {"inst": "моро́женым", "prep": "моро́женом"}}}), [])

    def test_thieu_du_lieu_thi_im_chu_khong_no(self):
        for rec in ({}, None, {"pos": "noun"}, {"decl": {"sg": {"inst": "ке́де"}}}):
            self.assertEqual(soat_nguphap.dao_cach_5_6(rec), [])


class AliasPublicConSong(unittest.TestCase):
    """Alias public thêm ở G4 (QD-02) là hợp đồng cho ngày tách `grammar.py`.
    Ai lỡ xoá thì phải gãy Ở ĐÂY, không phải gãy trên máy chủ lúc nửa đêm."""

    def test_grammar(self):
        self.assertIs(grammar.BANG_RE, grammar._BANG_RE)
        self.assertIs(grammar.doc_cache, grammar._cache)
        self.assertIs(grammar.lap_dem_tu_the, grammar._lap_dem_tu_the)

    def test_ai_client(self):
        from anki_tools import ai_client
        self.assertIs(ai_client.parse_ai_response, ai_client._parse_ai_response)
        self.assertIs(ai_client.send_ai_request, ai_client._send_ai_request)


class GhiLoPhaiSyncTruoc(unittest.TestCase):
    """BUG GỐC (31/07/2026, phát hiện 02/08): 23 thẻ nằm ở deck gõ `1-go` mà hiện
    mặt LÀM QUEN. Bot trên VPS thăng chúng lên GĐ2 lúc 03:00 (ghi Stage="type");
    9 tiếng sau laptop CHƯA sync về đã ghi lại 976 note cho ô GrammarJSON. Ghi
    vào note làm `mod` mới hơn, mà sync Anki xử xung đột "ai sửa sau thắng TRỌN
    note" ⇒ bản laptop Stage rỗng đè bản VPS. Đổi deck sống sót vì nó nằm trên
    THẺ. Hỏng IM LẶNG: thẻ đúng deck, sai mặt, không lỗi nào bật ra."""

    def test_sync_hong_thi_KHONG_DUOC_ghi(self):
        from anki_tools import anki_client
        with unittest.mock.patch.object(anki_client, "sync_now",
                                        return_value=(False, "Sync status 2")):
            self.assertFalse(anki_client.sync_truoc_khi_ghi_lo("thu"))

    def test_moi_script_ghi_lo_deu_phai_qua_cua_nay(self):
        """Chặn đúng cách tái diễn: ai thêm script ghi hàng loạt mà quên sync."""
        goc = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        for ten in ("scripts/backfill_grammar_json.py", "scripts/backfill_badge.py",
                    "data/huongdan/kho/congcu.py", "data/huongdan/kho/cao_nguphap.py"):
            with open(os.path.join(goc, *ten.split("/")), encoding="utf-8") as f:
                nguon = f.read()
            self.assertTrue("updateNoteFields" in nguon or "grammar.remember(" in nguon,
                            f"{ten}: test bám nhầm file, ở đây không còn chỗ ghi note")
            self.assertIn("sync_truoc_khi_ghi_lo(", nguon,
                          f"{ten} ghi hàng loạt lên note mà KHÔNG kéo sync về trước")


class TheHienSaiMatCaHaiChieu(unittest.TestCase):
    """BUG GỐC (03/08/2026): 21 thẻ nằm ở deck LÀM QUEN mà hiện mặt GÕ — chiều
    NGƯỢC của bug trên. Job 3h thăng cấp 36 thẻ; 21 thẻ user học lúc 6h36-7h04
    trên thiết bị CHƯA kéo bản 3h00 về nên bản thẻ của user (mod 6h40) thắng bản
    VPS (03:00) ⇒ mất deck + mất forgetCards, còn note thì chỉ VPS sửa nên nhãn
    `Stage="type"` sống sót. Anki xử xung đột RIÊNG cho note và RIÊNG cho card,
    nên nửa thắng nửa thua. Bằng chứng khoá chặt: lượt học đầu tiên sau 03:00 của
    cả 21 thẻ ghi `type=review, lastIvl=1` — trạng thái TRƯỚC forgetCards. (QD-17)

    Bốn test dưới bám vào `tim_lech()` vì đó là phần THUẦN — chạy offline, không
    cần Anki, nên nó luôn chạy được ở `deploy.ps1` trên máy không mở Anki."""

    def _the(self, deck, stage, tuoi_giay=3600, cid=1):
        from anki_tools.config import TOPIC_DECK_PARENT
        return {"cardId": cid, "noteId": 100 + cid, "tu": "тест",
                "deck": f"{TOPIC_DECK_PARENT}::{deck}",
                "stage": stage, "note_mod": 1_000_000 - tuoi_giay}

    def _lech(self, the, tot_nghiep=()):
        from anki_tools.soat_giaidoan import tim_lech
        return tim_lech(the, set(tot_nghiep), 1_000_000)

    def test_da_tot_nghiep_ma_bi_da_nguoc_ve_GD1_thi_DAY_TIEP_sang_GD2(self):
        """Chiều 03/08. KHÔNG gỡ nhãn cho lành: `forgetCards` là MỤC ĐÍCH của GĐ2
        (GĐ1 là chặng user bấm Again nhiều nên độ khó tích lại)."""
        ra = self._lech([self._the("0-quen", "type")], tot_nghiep=[1])
        self.assertEqual(len(ra["thang_cap"]), 1)
        self.assertEqual(ra["go_nhan"], [])

    def test_CHUA_tot_nghiep_thi_go_nhan_chu_khong_thang_cap(self):
        """User chốt 03/08: "thẻ đang học mà chưa pass 2 lần thì để nguyên đấy"."""
        ra = self._lech([self._the("0-quen", "type")], tot_nghiep=[])
        self.assertEqual(len(ra["go_nhan"]), 1)
        self.assertEqual(ra["thang_cap"], [])

    def test_lech_moi_vai_giay_thi_BO_QUA(self):
        """Chặn giẫm chân `thang_cap_gd2` đang chạy dở: nó ghi nhãn TRƯỚC, đổi
        deck SAU, nên giữa hai bước thẻ lệch là BÌNH THƯỜNG. Không có chốt này
        thì cửa canh tự đẻ ra đúng bug 31/07 mà nó sinh ra để chặn."""
        ra = self._lech([self._the("0-quen", "type", tuoi_giay=5)], tot_nghiep=[1])
        self.assertEqual(sum(len(v) for v in ra.values()), 0)

    def test_o_deck_GO_ma_MAT_nhan_thi_gan_lai(self):
        """Chiều 31/07 — `/don` mù hoàn toàn với chiều này (promote chỉ đọc deck
        `0-quen`; phần dọn về kho không đụng `Stage` ở bất kỳ đâu)."""
        ra = self._lech([self._the("1-go", ""), self._the("nature::plants", "", cid=2)])
        self.assertEqual(len(ra["gan_nhan"]), 2)

    def test_the_dung_thi_IM_LANG(self):
        """0 kêu oan — đo thật 03/08 trên 976 thẻ ra đúng 0."""
        ra = self._lech([self._the("0-quen", ""), self._the("1-go", "type", cid=2),
                         self._the("nature::plants", "type", cid=3)])
        self.assertEqual(sum(len(v) for v in ra.values()), 0)

    def test_cua_canh_dung_LAI_loi_thang_cap_chu_khong_chep_ban_hai(self):
        """Hai bản sao của cùng một luật thì sớm muộn lệch nhau ÂM THẦM."""
        goc = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(goc, "anki_tools", "soat_giaidoan.py"), encoding="utf-8") as f:
            nguon = f.read()
        self.assertIn("thang_cap_gd2", nguon)
        # Bám vào LỜI GỌI thật, không bám chữ trong văn giải thích — docstring
        # có quyền nhắc tên `forgetCards` để nói vì sao nó là mục đích.
        for buoc in ("forgetCards", "changeDeck"):
            self.assertNotIn(f'_ac("{buoc}"', nguon,
                             f"chép bước {buoc} ra đây là dựng bản thứ hai của luật thăng cấp")


if __name__ == "__main__":
    unittest.main()
