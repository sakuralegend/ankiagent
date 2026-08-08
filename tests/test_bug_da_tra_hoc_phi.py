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


class MocFsrsPhaiSoatDuMOIPRESET(unittest.TestCase):
    """04/08/2026 — `scripts/do_fsrs.py` bản đầu chỉ đọc preset của deck "RUSSIAN",
    mà deck đó KHÔNG chứa thẻ nào. User bấm Optimize xong, script báo "21 tham số
    y hệt, không đổi" trong khi bộ thật sự xếp lịch (preset "Default", 28 deck) đã
    đổi hẳn. Bảng so sánh phải kể tên ĐỦ 4 preset, kể cả preset chỉ có ở một mốc."""

    def _in(self, cu, moi):
        import contextlib, importlib.util, io as _io          # noqa: E401
        goc = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        spec = importlib.util.spec_from_file_location(        # scripts/ không phải package
            "do_fsrs", os.path.join(goc, "scripts", "do_fsrs.py"))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        buf = _io.StringIO()
        with contextlib.redirect_stdout(buf):
            mod.in_so_sanh(cu, moi)
        return buf.getvalue()

    def test_ke_du_ten_preset_ke_ca_ben_chi_co_o_MOT_moc(self):
        a, b = {"fsrsParams6": [0.1] * 21}, {"fsrsParams6": [0.2] * 21}
        ra = self._in({"ngay": "A", "preset": {"Default": a, "stage1-quen": a}},
                      {"ngay": "B", "preset": {"Default": b, "stage1-quen": a, "inbox": a}})
        for ten in ("Default", "stage1-quen", "inbox"):
            self.assertIn(ten, ra, f"preset {ten} biến mất khỏi bảng so sánh")
        self.assertIn("Y HỆT", ra, "preset không đổi phải nói rõ là không đổi")
        # Mốc 25/07 để tham số phẳng ở gốc, chưa xếp theo preset -> vẫn phải đọc được
        ra = self._in({"ngay": "A", "preset": "russian-parent-70", "fsrsParams6": [0.1] * 21},
                      {"ngay": "B", "preset": {"Default": b}})
        self.assertIn("russian-parent-70", ra)


class MotChanLyLaTheAnki(unittest.TestCase):
    """BUG GỐC 04/08/2026 (user báo qua `устать`): user sửa tay nghĩa tiếng Việt
    trong Anki, chạy lô xong thì nghĩa **bật lại bản cũ**.

    Đo ra ba đường đè, cả ba đều im lặng:
      1. `congcu.py tiep` in đề bài từ `tudien.json` — ảnh chụp đông lạnh, đo
         04/08 lệch **353/1039 từ** với thẻ thật ⇒ agent "sửa" một dòng vốn đúng.
      2. `nap --tatca` phát lại mọi dòng `V` cũ trong file lô.
      3. `/sua` của bot dựng lại field `Vietnamese` bằng một lượt dịch AI mới.
    QD-27 chốt: thẻ là chân lý, `tudien.json` bỏ hẳn cột `vi`."""

    def test_tudien_json_KHONG_con_cot_vi(self):
        """Còn cột `vi` là còn bản chép thứ hai, và bản thứ hai SẼ lệch."""
        import io as _io
        import json as _json
        goc = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        duong = os.path.join(goc, "data", "huongdan", "kho", "tudien.json")
        with _io.open(duong, encoding="utf-8") as f:
            d = _json.load(f)
        co_vi = [e["wc"] for e in d if "vi" in e]
        self.assertEqual(co_vi, [], f"{len(co_vi)} muc con cot `vi` — QD-27 da bo")

    def test_lam_lai_the_KHONG_de_len_nghia_Viet_user_da_sua(self):
        """`/sua` giữ nghĩa Việt cũ y như đã giữ ô Hướng dẫn."""
        import inspect
        from anki_tools import pipeline
        nguon = inspect.getsource(pipeline.redo_note_id)
        self.assertIn('new_fields["Vietnamese"] = fields["Vietnamese"]', nguon,
                      "redo_note_id phai GIU nghia tieng Viet user da sua (QD-27)")

    def test_nghia_Viet_chi_doc_tu_lo_CHUA_nap(self):
        """`--tatca` đẩy lại phần máy nhưng KHÔNG phát lại dòng `V` cũ."""
        import inspect
        import importlib.util
        goc = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        kho = os.path.join(goc, "data", "huongdan", "kho")
        sys.path.insert(0, kho)
        spec = importlib.util.spec_from_file_location("congcu", os.path.join(kho, "congcu.py"))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        nguon = inspect.getsource(mod.cmd_nap)
        self.assertIn('if not l.get("daNap")', nguon,
                      "cmd_nap phai loc lo CHUA nap truoc khi doc dict V (QD-27)")


class OMayDungRiengKhoiOHuongDan(unittest.TestCase):
    """QD-26 (04/08/2026): bảng chia + cặp thể chuyển sang field `BangMay`.

    Trước đó máy nối bảng vào đuôi `HuongDan` bằng cắt–dán khuôn mẫu, nên cửa
    soát của dây chuyền lô đo phải cả phần máy và rác trong bảng sống nhiều tuần
    (7 ca trong `SONO.md`). Hai chủ ghi chung một ô là gốc của cả loại lỗi đó."""

    def test_go_bang_giu_nguyen_phan_agent_soan(self):
        html = ('<div class="hd-sec">Chẻ từ</div>NGƯỜI SOẠN'
                '<details class="gt-bang"><summary>x</summary>BẢNG CŨ</details>')
        ra = grammar.go_bang(html)
        self.assertIn("NGƯỜI SOẠN", ra)
        self.assertNotIn("BẢNG CŨ", ra)

    def test_go_bang_goi_hai_lan_van_ra_mot_ket_qua(self):
        """Chạy `bang --apply` hai lần không được đội bảng / cụt chữ."""
        html = 'CHỮ<details class="gt-bang">B</details>'
        self.assertEqual(grammar.go_bang(grammar.go_bang(html)), grammar.go_bang(html))

    def test_cap_the_chi_lay_MOT_ban_thay_vi_liet_ke_het(self):
        """`partners` trả 1–3 mục; mục sau là từ GẦN NGHĨA, in ra là dạy sai."""
        rec = {"pos": "verb", "aspect": "perfective", "acc": "сказа́ть",
               "partners": ["говори́ть", "ска́зывать"]}
        ra = grammar.cap_the_html(rec)
        self.assertIn("говори́ть", ra)
        self.assertNotIn("ска́зывать", ra)

    def test_cap_the_im_lang_khi_khong_ro_the(self):
        """Thể `both` / thiếu thể: nói cặp là nói bừa -> không in gì."""
        self.assertEqual(grammar.cap_the_html(
            {"pos": "verb", "aspect": "both", "acc": "жени́ться",
             "partners": ["пожени́ться"]}), "")
        self.assertEqual(grammar.cap_the_html({"pos": "noun", "partners": ["x"]}), "")

    def test_dang_ou_duoc_dan_nhan_van_chuong(self):
        """139 danh từ + 170 tính từ có dạng `-ою/-ею` ở cách 5, từ điển in ngang
        hàng không nhãn ⇒ user tưởng dùng thay nhau được trong lời nói thường."""
        ra = grammar._nhan_bien_the("ма́мой, ма́мою")
        self.assertIn("văn chương", ra)
        self.assertIn("ма́мой", ra)

    def test_KHONG_dan_nham_khi_ou_nam_trong_than_tu(self):
        """`сою́зом` có `ою` nhưng đó là thân từ — dán nhãn là bịa ra biến thể."""
        self.assertEqual(grammar._nhan_bien_the("сою́зом"), "сою́зом")
        self.assertEqual(grammar._nhan_bien_the("сою́зами"), "сою́зами")

    def test_o_chi_co_moi_dang_ou_thi_dung_lai_dang_doi_nay(self):
        """13 ô (đo 08/08 trên 1041 thẻ) chỉ in MỖI dạng thơ ca `пе́рвою`, không có
        `пе́рвой` đi kèm ⇒ thẻ dạy dạng cổ như thể nó là dạng duy nhất."""
        ra = grammar._nhan_bien_the("пе́рвою")
        self.assertIn("пе́рвой", ra)
        self.assertIn("văn chương", ra)
        # từ MỘT nguyên âm: từ điển in `злой` không dấu, dựng lại phải theo đúng lệ đó
        self.assertIn("злой", grammar._nhan_bien_the("зло́ю"))

    def test_hai_dau_trong_am_tren_mot_tu_thi_tach_lam_hai_bien_the(self):
        """BUG NGUỒN: `мо́дны́` là hai biến thể `мо́дны` + `модны́` bị dính liền vì
        thiếu dấu phẩy. Một từ Nga có ĐÚNG một trọng âm nên đây là ô chắc chắn
        hỏng — 3 ô như vậy trên 1041 thẻ (`мо́дный`·`у́зкий`·`кру́пный`)."""
        self.assertEqual(grammar.tach_hai_trong_am("мо́дны́"), "мо́дны, модны́")
        self.assertEqual(grammar.tach_hai_trong_am("у́зки́"), "у́зки, узки́")
        # ô THẬT của `мо́дный` có sẵn một biến thể rồi mới dính ô hỏng -> không được đẻ trùng
        self.assertEqual(grammar.tach_hai_trong_am("мо́дны, мо́дны́"), "мо́дны, модны́")
        # ô lành thì KHÔNG được đụng vào
        self.assertEqual(grammar.tach_hai_trong_am("ма́мой, ма́мою"), "ма́мой, ма́мою")
        self.assertEqual(grammar.tach_hai_trong_am("сто́л"), "сто́л")


class DonXongMaAnkiWebChuaNhan(unittest.TestCase):
    """BUG GỐC (06/08/2026, user phát hiện): sáng ra bot báo "đã dọn xong", nhưng
    iPhone bấm sync bao nhiêu lần cũng thấy 4 thẻ còn ở deck gõ `1-go`. Job 3h đã
    chuyển đúng 4 thẻ lúc 03:00:01 — mà **AnkiWeb chỉ nhận lúc ~10:05**, tức nằm
    lại VPS 7 tiếng. Khoá chặt bằng usn: 4 thẻ đóng **1387**, lớn hơn **1386** của
    lượt ôn 09:51 trên iPhone ⇒ chúng lên sau lượt ôn đó.

    Nguyên nhân: `changeDeck` của AnkiConnect ghi thẳng bảng `cards` bằng SQL nên
    thẻ có dấu "chưa gửi" mà đồng hồ của KHO không nhích; sync chỉ so đồng hồ nên
    thoát ngay. 14 nhịp sync liên tiếp đều "thành công". Hỏng IM LẶNG hai lớp: bot
    nói "đã đẩy lên AnkiWeb", và job đêm không xét bước đẩy lên nên không kêu.
    (QD-34 — cơ chế đầy đủ ở `anki_client.cham_vao_kho()`)"""

    def _kho_gia(self, chua_the=0, chua_note=0, sua=1000, dong_bo=1000):
        """Dựng một file kho GIẢ đủ ba con số — không cần Anki, chạy được mọi lúc."""
        import sqlite3 as sq
        import tempfile
        d = tempfile.TemporaryDirectory()
        self.addCleanup(d.cleanup)
        p = os.path.join(d.name, "collection.anki2")
        con = sq.connect(p)
        con.executescript("create table cards (id integer primary key, usn integer);"
                          "create table notes (id integer primary key, usn integer);"
                          "create table col (mod integer, ls integer);")
        con.executemany("insert into cards values (?, -1)", [(i,) for i in range(chua_the)])
        con.executemany("insert into notes values (?, -1)", [(i,) for i in range(chua_note)])
        con.execute("insert into cards values (9999, 5)")      # thẻ đã gửi rồi
        con.execute("insert into col values (?, ?)", (sua, dong_bo))
        con.commit()
        con.close()
        return p

    def _doc(self, **kw):
        from anki_tools import anki_client
        with unittest.mock.patch.object(anki_client, "ANKI_COLLECTION", self._kho_gia(**kw)):
            return anki_client.trang_thai_dong_bo()

    def test_dem_dung_so_thu_con_nam_lai(self):
        self.assertEqual(self._doc(chua_the=4, chua_note=2)["chua_gui"], 6)
        self.assertEqual(self._doc()["chua_gui"], 0)

    def test_khong_khai_duong_dan_thi_None_chu_KHONG_phai_sach(self):
        """🔴 `None` = KHÔNG BIẾT. Đọc thành "sạch" là tái diễn đúng bug: bot nói
        đã đẩy lên trong khi chẳng ai kiểm gì."""
        from anki_tools import anki_client
        with unittest.mock.patch.object(anki_client, "ANKI_COLLECTION", ""):
            self.assertIsNone(anki_client.trang_thai_dong_bo())
        with unittest.mock.patch.object(anki_client, "ANKI_COLLECTION", "/khong/co/that.anki2"):
            self.assertIsNone(anki_client.trang_thai_dong_bo())

    def _kiem(self, truoc_dong_bo, cham_duoc=True, so_lan=1, **kw):
        from tgbot import commands
        from anki_tools import anki_client
        with unittest.mock.patch.object(anki_client, "ANKI_COLLECTION", self._kho_gia(**kw)), \
             unittest.mock.patch.object(commands.time, "sleep"), \
             unittest.mock.patch.object(commands, "cham_vao_kho") as cham, \
             unittest.mock.patch.object(commands, "trigger_sync"):
            ra = commands._kiem_da_len_ankiweb({"dong_bo": truoc_dong_bo},
                                               cham_duoc=cham_duoc, so_lan=so_lan)
        self._da_cham = cham.call_count
        return ra

    def test_sync_keo_ve_HONG_thi_KHONG_DUOC_cham_vao_kho(self):
        """Cú chạm ghi vào note. Ghi note khi CHƯA kéo AnkiWeb về đúng là cơ chế đã
        làm hỏng 23 thẻ hôm 31/07 — thà để việc dọn nằm lại rồi KÊU RA, còn hơn âm
        thầm đè mất bản mới hơn ở máy khác."""
        self.assertEqual(self._kiem(500, cham_duoc=False, so_lan=2,
                                    chua_the=4, sua=1000, dong_bo=1000), 4)
        self.assertEqual(self._da_cham, 0)
        # Ngược lại: kéo về được thì PHẢI chạm để gỡ.
        self._kiem(500, cham_duoc=True, so_lan=2, chua_the=4, sua=1000, dong_bo=1000)
        self.assertEqual(self._da_cham, 1)

    def test_chua_keo_ve_duoc_thi_KHONG_cham_luc_chuyen_deck(self):
        """Chốt cùng luật ở đường chuyển deck: `move_graduated_from_inbox(cham=...)`
        phải nhận cờ, và `run_don` phải truyền `sync_in` vào đó."""
        goc = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(goc, "anki_tools", "anki_client.py"), encoding="utf-8") as f:
            self.assertIn("def move_graduated_from_inbox(cham=True)", f.read())
        with open(os.path.join(goc, "tgbot", "commands.py"), encoding="utf-8") as f:
            nguon = f.read()
        self.assertIn('move_graduated_from_inbox(cham=out["sync_in"])', nguon)
        self.assertIn('cham_duoc=out["sync_in"]', nguon)

    def test_sach_va_dong_ho_da_nhich_thi_coi_la_DA_TOI(self):
        self.assertEqual(self._kiem(500, sua=1000, dong_bo=1000), 0)

    def test_con_dau_chua_gui_thi_bao_CHUA_TOI(self):
        self.assertEqual(self._kiem(500, chua_the=4, sua=1000, dong_bo=1000), 4)

    def test_dong_ho_DUNG_IM_thi_bao_CHUA_TOI_du_khong_con_dau_nao(self):
        """CHÍNH CA 06/08: sync thoát ngay nên "đồng bộ tới" không nhích. Nếu chỉ
        đếm dấu "chưa gửi" thì ca này lọt — nên câu hỏi 3 phải có."""
        self.assertEqual(self._kiem(1000, sua=1000, dong_bo=1000), 1)

    def test_bao_cao_KHONG_DUOC_noi_da_day_len_khi_chua_toi(self):
        """Lời nói dối chính là thứ user gặp: "đã đẩy lên AnkiWeb" mà thực ra chưa."""
        from tgbot.commands import _don_report
        goc = {"sync_in": True, "promoted": 0, "moved": {"time": 4}, "total": 4,
               "sync_out": True, "error": None}
        self.assertNotIn("ĐÃ NHẬN", _don_report({**goc, "chua_gui": 4}))
        self.assertIn("CHƯA TỚI ANKIWEB", _don_report({**goc, "chua_gui": 4}))
        self.assertIn("ĐÃ NHẬN", _don_report({**goc, "chua_gui": 0}))
        # Không kiểm được thì nói thật là không kiểm được, đừng khẳng định.
        self.assertIn("CHƯA KIỂM ĐƯỢC", _don_report({**goc, "chua_gui": None}))

    def test_job_dem_PHAI_xet_buoc_day_len(self):
        """Lỗ hổng thứ hai: đêm 06/08 việc dọn nằm lại VPS mà không tiếng còi nào,
        vì `_nightly_don` chỉ xét sync KÉO VỀ."""
        goc = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(goc, "tgbot", "jobs.py"), encoding="utf-8") as f:
            nguon = f.read()
        self.assertIn('res["chua_gui"]', nguon,
                      "_nightly_don không xét chua_gui ⇒ đẩy lên hỏng lại im lặng")

    def test_chuyen_deck_xong_PHAI_cham_vao_kho(self):
        """Chặn đúng cách tái diễn: ai sửa `move_graduated_from_inbox` mà bỏ cú
        chạm thì thẻ lại nằm lại VPS im lặng."""
        goc = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(goc, "anki_tools", "anki_client.py"), encoding="utf-8") as f:
            nguon = f.read()
        than = nguon.split("def move_graduated_from_inbox(")[1].split("\ndef ")[0]
        self.assertIn("cham_vao_kho(", than,
                      "chuyển deck mà không chạm vào kho ⇒ sync sẽ thoát ngay, "
                      "việc dọn nằm lại VPS (xem docstring cham_vao_kho)")


class ChotYoLamBoSoatMuMotVungLon(unittest.TestCase):
    """BUG GỐC (ghi sổ nợ 05/08/2026, trả 08/08): thẻ viết `тве́рдость` trong khi
    từ đúng là `твёрдость`, mà `congcu.py soat` báo XANH.

    Hai chốt cộng lại thành một vùng mù: ô chuẩn không có dấu sắc thì bỏ so, mà
    dạng mang `ё` thì `nouns.csv` không đánh dấu sắc (ё đã là trọng âm) ⇒ **5 230
    dạng** không bao giờ được soi. Chốt thứ hai gộp `ё→е` hai phía nên kể cả có so
    cũng không thấy. Mở khoá xong đo lại toàn kho: đúng **1** chỗ kêu oan
    (`лет` ↔ `лёт`), đã vào `MIEN_TRU` kèm lý do."""

    @staticmethod
    def _soatlo():
        goc = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        sys.path.insert(0, os.path.join(goc, "data", "huongdan", "kho"))
        sys.path.insert(0, os.path.join(goc, "data", "huongdan"))
        import soatlo
        return soatlo

    def test_viet_e_o_cho_dang_le_la_yo_thi_PHAI_bao(self):
        s = self._soatlo()
        self.assertTrue(s.lech_trong_am("тве́рдость", "твёрдость"))
        self.assertFalse(s.lech_trong_am("твёрдость", "твёрдость"))

    def test_chuan_KHONG_co_yo_thi_van_gop_nhu_cu(self):
        """`nouns.csv` in `ё` thành `е` ở phần lớn dòng — bắt bẻ chỗ đó là kêu oan."""
        s = self._soatlo()
        self.assertFalse(s.lech_trong_am("силён", "силен"))

    def test_tu_dong_tu_da_mien_tru_thi_im(self):
        s = self._soatlo()
        self.assertFalse(s.lech_trong_am("лет", "лёт"))


if __name__ == "__main__":
    unittest.main()
