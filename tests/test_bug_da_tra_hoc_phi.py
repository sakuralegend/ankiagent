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
import inspect
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


class JsonPhayThuaKhongDuocCoiLaAiHong(unittest.TestCase):
    """BUG GỐC (đo 12/08/2026): thêm từ qua bot chậm gấp đôi-ba, có ca 26 GIÂY
    cho MỘT từ (log VPS 07:53:18 -> 07:53:44) trong khi một lượt AI chỉ 1,8s.

    Nguyên nhân: Gemini thỉnh thoảng trả JSON kiểu JavaScript, thừa dấu phẩy
    trước `}` hoặc `]`. `json.loads` từ chối, `_parse_ai_response` trả None, và
    `build_examples_html` hiểu nhầm thành "AI hỏng" nên gọi lại freestyle thêm
    1-2 lượt nữa -> 3-4 lượt AI cho 1 từ. Hỏng IM LẶNG theo nghĩa xấu nhất: thẻ
    vẫn ra đúng nên không ai nghi, chỉ thấy "sao dạo này chậm thế".

    Đo được 1/12 từ dính. KHÔNG phải lỗi model: 3.1-flash-lite và 3.5-flash-lite
    đều 1,7-1,9s/lượt, cả hai đều thỉnh thoảng thừa phẩy."""

    def setUp(self):
        from anki_tools import ai_client
        self.parse = ai_client._parse_ai_response

    def _json_du(self, duoi_vi):
        return ('{"vietnamese_meaning": "dep", "topic": "qualities", '
                '"simplified_examples": ['
                '{"ru": "a", "en": "b", "vi": "c"},'
                '{"ru": "d", "en": "e", "vi": "f"},'
                '{"ru": "g", "en": "h", "vi": "%s"}' % duoi_vi)

    def test_phay_thua_truoc_ngoac_nhon(self):
        raw = '{"vietnamese_meaning": "dep", "topic": "qualities",}'
        self.assertEqual(self.parse(raw).get("vietnamese_meaning"), "dep")

    def test_phay_thua_truoc_ngoac_vuong_va_nhon_cung_luc(self):
        # đúng hình dạng đã bắt được thật ở từ `красивый` trên VPS 12/08
        raw = self._json_du("i") + ',\n  ]\n}'
        parsed = self.parse(raw)
        self.assertIsNotNone(parsed, "phẩy thừa vẫn bị coi là AI hỏng")
        self.assertEqual(len(parsed["simplified_examples"]), 3)

    def test_phay_trong_cau_KHONG_bi_dung(self):
        """Vá không được nuốt dấu phẩy nằm trong chính câu tiếng Việt/Nga —
        đó là lý do không dùng regex quét cả chuỗi."""
        raw = '{"vietnamese_meaning": "chao, ban", "simplified_examples": []}'
        self.assertEqual(self.parse(raw)["vietnamese_meaning"], "chao, ban")

    def test_rac_that_thi_van_tra_None(self):
        """Tha thứ phẩy thừa KHÔNG được biến thành 'nuốt mọi thứ' — câu trả lời
        hỏng thật vẫn phải trả None để caller còn biết đường chạy freestyle."""
        for rac in ("xin loi toi khong the", '{"a": ', "", "```json\n{oops```"):
            self.assertIsNone(self.parse(rac), repr(rac))


class MoiLoiGoiAiPhaiEpKHUONJson(unittest.TestCase):
    """BUG GỐC (đo 12/08/2026, cùng gốc với lớp trên). Vá dấu phẩy thừa xong đo
    lại vẫn 4/16 từ phải gọi AI nhiều lượt — còn kiểu hỏng THỨ HAI: model QUÊN
    DẤU NHÁY MỞ ở câu tiếng Nga (`думать`: `"ru": Я сижу и <hl>думаю</hl>,...`).
    Kiểu này KHÔNG vá tay được vì không biết câu bắt đầu từ đâu.

    Cách chữa tận gốc là ép khuôn ngay lúc API sinh chữ (`response_format`) thay
    vì dặn suông trong prompt: đo 16/16 đúng, chỉ chậm thêm ~0,1s mỗi lượt.

    Test này canh cái DỄ MẤT nhất: một lời gọi AI mới được viết mà QUÊN truyền
    khuôn — lúc đó nó chạy vẫn ra kết quả, chỉ thỉnh thoảng chậm gấp ba, đúng
    kiểu hỏng im lặng đã ngốn cả buổi để tìm ra."""

    def test_khuon_duoc_gan_vao_payload(self):
        from anki_tools import ai_client
        bat = {}

        class FakeRes:
            status_code = 200
            def json(self):
                return {"choices": [{"message": {"content": '{"a": 1}'}}]}

        def fake_post(url, headers=None, json=None, timeout=None):
            bat.update(json or {})
            return FakeRes()

        with unittest.mock.patch.object(ai_client.requests, "post", fake_post):
            ai_client._call_model_once("m", "sys", "user", khuon=ai_client._KHUON_THE)
        self.assertIn("response_format", bat, "khuôn KHÔNG được gửi lên API")
        self.assertEqual(bat["response_format"]["type"], "json_schema")
        self.assertEqual(bat["response_format"]["json_schema"]["schema"], ai_client._KHUON_THE)

    def test_khong_khuon_thi_khong_gui_field(self):
        from anki_tools import ai_client
        bat = {}

        class FakeRes:
            status_code = 200
            def json(self):
                return {"choices": [{"message": {"content": '{"a": 1}'}}]}

        with unittest.mock.patch.object(ai_client.requests, "post",
                lambda url, headers=None, json=None, timeout=None: (bat.update(json or {}), FakeRes())[1]):
            ai_client._call_model_once("m", "sys", "user", khuon=None)
        self.assertNotIn("response_format", bat)

    def test_moi_ham_call_claude_deu_truyen_khuon(self):
        """Ai thêm hàm gọi AI mới mà quên khuôn thì gãy Ở ĐÂY, không phải gãy
        bằng việc bot chậm dần mà không ai hiểu vì sao."""
        import inspect
        from anki_tools import ai_client
        thieu = []
        for ten, ham in vars(ai_client).items():
            if not (ten.startswith("call_claude") and callable(ham)):
                continue
            if ten == "call_claude_ready" or ten == "check_claude_ready":
                continue
            src = inspect.getsource(ham)
            if "_send_ai_request(" in src and "khuon=" not in src:
                thieu.append(ten)
        self.assertEqual(thieu, [], "hàm gọi AI quên truyền khuôn JSON: %s" % thieu)

    def test_khuon_ngu_phap_bo_topic_nhung_giu_phan_con_lai(self):
        from anki_tools import ai_client
        kt = ai_client._KHUON_THE_KHONG_TOPIC
        self.assertNotIn("topic", kt["required"])
        self.assertNotIn("topic", kt["properties"])
        self.assertEqual(kt["properties"]["simplified_examples"],
                         ai_client._KHUON_THE["properties"]["simplified_examples"])


class BadgeChiSoNhieuPhaiSongKhiKhongCoNounsCsv(unittest.TestCase):
    """BUG GỐC (đo 12/08/2026): `data/nouns.csv` bị gitignore (8 MB, là dump tải
    về từ GitHub) nên CHƯA BAO GIỜ có mặt trên VPS. `grammar.chi_so_nhieu` đọc
    thẳng file đó, không thấy thì chỉ log_warn rồi bỏ qua luật — nên mọi danh từ
    CHỈ CÓ SỐ NHIỀU thêm qua bot Telegram đều đeo badge giống SAI:
        перила (lan can) -> FEM ♀      сани (xe trượt) -> MASC ♂
    Đo 6 từ trên VPS: 3 sai hẳn, 3 mất badge; cùng mã trên laptop cả 6 đúng PL.
    Badge sai tệ hơn không badge — nó dạy user nói "э́та перила".

    Nay đọc `data/chi_so_nhieu.txt` (381 từ, 3 KB) ĐI THEO REPO. Test này canh
    đúng cái đã hỏng: chạy KHI KHÔNG CÓ nouns.csv."""

    def test_bay_tu_that_van_nhan_dung_khi_khong_co_nouns_csv(self):
        from anki_tools import grammar
        with unittest.mock.patch.object(grammar, "_PL_ONLY", None):
            for tu in ("перила", "сани", "сутки", "брюки", "деньги", "шахматы"):
                self.assertTrue(grammar.chi_so_nhieu(tu), f"{tu} phải là chỉ-số-nhiều")
            for tu in ("стол", "город", "книга"):
                self.assertFalse(grammar.chi_so_nhieu(tu), f"{tu} KHÔNG phải chỉ-số-nhiều")
        # test này chỉ có nghĩa nếu nó KHÔNG dựa vào nouns.csv
        self.assertNotIn("nouns.csv", inspect.getsource(grammar.chi_so_nhieu).split('"""')[-1],
                         "chi_so_nhieu lại đọc nouns.csv — file đó không có trên VPS")

    def test_file_nho_di_theo_repo(self):
        """File 3 KB này PHẢI được git theo dõi. Nếu ai lỡ cho nó vào .gitignore
        thì bug quay lại y hệt, và lại hỏng IM LẶNG trên VPS."""
        goc = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        duong = os.path.join(goc, "data", "chi_so_nhieu.txt")
        self.assertTrue(os.path.exists(duong), "thiếu data/chi_so_nhieu.txt")
        with open(duong, encoding="utf-8") as fh:
            tu = [d.strip() for d in fh if d.strip() and not d.startswith("#")]
        self.assertGreater(len(tu), 300, "danh sách chỉ-số-nhiều ngắn bất thường")

    def test_badge_ra_dung_PL(self):
        """Đi hết đường tới badge, vì đó là thứ user NHÌN THẤY."""
        from anki_tools import grammar
        with unittest.mock.patch.object(grammar, "_PL_ONLY", None):
            html = grammar.gender_badge_html("перила", "f")
        self.assertIn("plural", html, "перила vẫn ra badge giống số ít")


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

    def test_bang_in_TEN_the_no_sua_khong_chi_in_SO(self):
        """🔴 Vá 1 ô của `видеоигра` 09/08 mà lệnh báo đổi **2 note**.

        Note thứ hai không cách nào gọi tên lại: lệnh idempotent nên chạy lại chỉ
        ra 0, và bộ sưu tập không nằm trong git. Đếm được mà không truy được thì
        con số chỉ báo có chuyện, không nói chuyện gì."""
        import inspect
        import importlib.util
        goc = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        kho = os.path.join(goc, "data", "huongdan", "kho")
        sys.path.insert(0, kho)
        spec = importlib.util.spec_from_file_location("congcu", os.path.join(kho, "congcu.py"))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        nguon = inspect.getsource(mod.cmd_bang)
        self.assertIn("for _, wc, o in doi:", nguon,
                      "cmd_bang phai duyet `doi` de IN TEN tung the no sua")
        self.assertIn("{wc}", nguon, "vong lap do phai in ra chinh tu, khong phai dem lai")

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


class ToBangChia(unittest.TestCase):
    """User bắt 08/08/2026: thẻ `крокоди́л` có ô đỏ dạy "cách 4 mượn hình cách 2"
    mà bảng ngay dưới **không tô ô nào**, trong khi `президе́нт` cùng hiện tượng
    thì lại được tô — kèm nhãn sai ("ô có nhiều dạng song song").

    Gốc: bộ dò chỉ biết tìm ô có MẶT CHỮ lệch chuẩn (thân đổi · đuôi lạ · nguyên
    âm chạy · trọng âm dịch). Cách 4 = cách 2 là **quan hệ giữa hai ô**, đuôi `-а`
    / `-ов` thì chuẩn không chê được ⇒ không luật nào bắt. Đo lúc sửa: 102 ô /
    64 từ vô hình."""

    @staticmethod
    def _soi(decl, dang_goc, **them):
        """`dang_goc` = ô `acc` của bản ghi (dạng nguyên thể CÓ trọng âm) — bộ dò
        suy thân từ từ đó, thiếu nó thì mọi ô đều bị coi là lệch."""
        from anki_tools.hinh_thai import analyze
        return analyze(dict({"pos": "noun", "decl": decl, "acc": dang_goc}, **them))

    KROK = {"sg": {"nom": "крокоди́л", "gen": "крокоди́ла", "dat": "крокоди́лу",
                   "acc": "крокоди́ла", "inst": "крокоди́лом", "prep": "крокоди́ле"},
            "pl": {"nom": "крокоди́лы", "gen": "крокоди́лов", "dat": "крокоди́лам",
                   "acc": "крокоди́лов", "inst": "крокоди́лами", "prep": "крокоди́лах"}}

    def test_cach4_giong_cach2_thi_PHAI_to(self):
        a = self._soi(self.KROK, "крокоди́л")
        self.assertIn(("sg", "acc"), a["nong"])
        self.assertIn(("pl", "acc"), a["nong"])

    def test_KHONG_to_lan_sang_o_khac(self):
        """Chỉ ô cách 4 sáng — `крокоди́л` đều tăm tắp ở mọi ô còn lại."""
        self.assertEqual(self._soi(self.KROK, "крокоди́л")["nong"],
                         {("sg", "acc"), ("pl", "acc")})

    def test_khong_doc_field_animate_cua_nguon(self):
        """Nguồn ghi `animate` SAI được — đo 08/08 trên 575 danh từ: `ме́неджер`,
        `о́кунь`, `коза́`, `матрёшка` đều là sinh vật mà bị ghi `False`. Tô phải
        theo điều QUAN SÁT được (hai ô viết giống nhau), không theo lời khai."""
        a = self._soi(self.KROK, "крокоди́л", animate=False)
        self.assertIn(("sg", "acc"), a["nong"])

    def test_o_acc_hai_dang_kieu_animacy_KHONG_con_bi_goi_la_biente(self):
        """`президе́нта, президе́нт`: dạng thứ hai chỉ là ô mặc định của danh từ
        chỉ ĐỒ VẬT mà nguồn in kèm, không phải hai dạng song song."""
        d = {"sg": {"nom": "президе́нт", "gen": "президе́нта", "dat": "президе́нту",
                    "acc": "президе́нта, президе́нт", "inst": "президе́нтом",
                    "prep": "президе́нте"}}
        DG = "президе́нт"
        ma = [m for m, _ in self._soi(d, DG)["flags"]]
        self.assertIn("cach4", ma)
        self.assertNotIn("biente", ma)

    def test_o_hai_dang_THAT_thi_van_giu_nhan_biente(self):
        """Ngược lại phải giữ: đo 08/08 ra 7 từ (`ребёнок` дете́й/ребя́т ·
        `сын` · `тётя` · `среда́`…) có hai dạng vì lý do THẬT. Bỏ nhãn của chúng
        là phá dữ liệu đúng để dọn một ca sai."""
        d = {"pl": {"nom": "де́ти, ребя́та", "gen": "дете́й, ребя́т",
                    "dat": "де́тям, ребя́там", "acc": "дете́й, ребя́т",
                    "inst": "детьми́, ребя́тами", "prep": "де́тях, ребя́тах"}}
        DG = "ребёнок"
        self.assertIn("biente", [m for m, _ in self._soi(d, DG)["flags"]])

    def test_cach4_KHONG_duoc_in_duoi_tieu_de_BAT_THUONG(self):
        """`CHUAN.md` §C: có khối `BAT THUONG` ⇒ BẮT BUỘC viết một câu chú ý.
        Nhưng `cach4` là luật SINH VẬT đúng quy tắc (đo 09/08: 112/605 danh từ
        dính nhãn, 100% là sinh vật) ⇒ lô đông danh từ chỉ người thì mọi thẻ
        phải mang cùng MỘT câu — đúng "khối hệ thống dùng chung" README §3 cấm.
        Đã xảy ra thật: 8/14 thẻ k69. Ô vẫn phải TÔ (QD-35), chỉ tiêu đề đổi."""
        from data.huongdan.kho import khochung
        rec = {"pos": "noun", "acc": "крокоди́л", "decl": self.KROK}
        dong = "\n".join(khochung._dong_bat_thuong(rec))
        self.assertIn("CÁCH 4", dong)              # vẫn trỏ chỗ cho agent
        self.assertIn("KHONG can cau chu y", dong)
        self.assertNotIn("BAT THUONG", dong)       # nhưng KHÔNG đội mũ bắt buộc
        self.assertIn(("sg", "acc"), self._soi(self.KROK, "крокоди́л")["nong"])

    def test_bat_thuong_THAT_van_giu_nguyen_tieu_de_bat_buoc(self):
        """Vế ngược: lọc `cach4` không được làm câm nhãn thật. `сестра́` vừa có
        cách 4 = cách 2 (sinh vật) vừa có trọng âm dịch — phải in CẢ HAI tiêu đề."""
        from data.huongdan.kho import khochung
        d = {"sg": {"nom": "сестра́", "gen": "сестры́", "dat": "сестре́",
                    "acc": "сестру́", "inst": "сестро́й", "prep": "сестре́"},
             "pl": {"nom": "сёстры", "gen": "сестёр", "dat": "сёстрам",
                    "acc": "сестёр", "inst": "сёстрами", "prep": "сёстрах"}}
        dong = "\n".join(khochung._dong_bat_thuong(
            {"pos": "noun", "acc": "сестра́", "decl": d}))
        self.assertIn("BAT THUONG", dong)
        self.assertIn("KHONG can cau chu y", dong)

    def test_danh_tu_chia_nhu_tinh_tu_KHONG_bi_to_va_KHONG_bi_gan_nhan_bia(self):
        """`живо́тное` từng sáng 10/12 ô với nhãn "NGUYÊN ÂM CHẠY" + "thân từ ĐỔI"
        — cả hai đều bịa (agent lô k68 bác 08/08). Đuôi tính từ là luật có trong
        sách ⇒ nêu tên hệ thống, không tô ô nào."""
        d = {"sg": {"nom": "живо́тное", "gen": "живо́тного", "dat": "живо́тному",
                    "acc": "живо́тное", "inst": "живо́тным", "prep": "живо́тном"},
             "pl": {"nom": "живо́тные", "gen": "живо́тных", "dat": "живо́тным",
                    "acc": "живо́тных", "inst": "живо́тными", "prep": "живо́тных"}}
        a = self._soi(d, "живо́тное")
        self.assertEqual(a["nong"], set())
        ma = [m for m, _ in a["flags"]]
        self.assertEqual(ma, ["tinhtu"])

    def test_danh_tu_THUONG_khong_bi_nham_la_chia_nhu_tinh_tu(self):
        """`ге́ний` kết thúc bằng `-ий` nhưng chia như danh từ — phép nhận dạng
        phải soi CẢ BỘ đuôi, không chỉ nhìn mặt chữ ô cách 1."""
        d = {"sg": {"nom": "ге́ний", "gen": "ге́ния", "dat": "ге́нию",
                    "acc": "ге́ния", "inst": "ге́нием", "prep": "ге́нии"}}
        DG = "ге́ний"
        self.assertNotIn("tinhtu", [m for m, _ in self._soi(d, DG)["flags"]])


class TrongTaiLemmaKHONGDuocDonGianHoa(unittest.TestCase):
    """`reconcile_lemma` là TRỌNG TÀI giữa AI và từ điển hình thái — 4 luật có
    thứ tự, chốt 21/07/2026. Lý do phải khoá bằng test: cả bốn luật trông thừa
    thãi với người đọc lướt, và cám dỗ "đơn giản hoá thành *từ điển luôn thắng*"
    xuất hiện mỗi lần có người mở file. Đơn giản hoá như thế thì luật 3 chết —
    chỗ DUY NHẤT ngữ cảnh câu của AI được phép thắng.

    Test mô phỏng từ điển (`possible_lemmas`) để chạy được cả khi máy KHÔNG cài
    pymorphy3: thứ đang soi là LUẬT PHÂN XỬ, không phải chất lượng từ điển."""

    def _xu(self, seen, ai, tu_dien):
        with unittest.mock.patch("anki_tools.lemma.possible_lemmas",
                                 return_value=tu_dien):
            from anki_tools.lemma import reconcile_lemma
            return reconcile_lemma(seen, ai)

    def test_luat1_tu_dien_khong_biet_thi_GIU_AI(self):
        """Typo và tên riêng: AI giỏi hơn hẳn từ điển."""
        self.assertEqual(self._xu("Мосвка", "Москва", []), ("москва", False))

    def test_luat2_chinh_seen_la_lemma_thi_CAM_AI_chia_sau_them(self):
        """Ca thật: AI đổi `это` (this is) thành `этот` (this) vì đúng luật
        "đại từ -> cách 1 giống đực" trong prompt. Cả loạt hư từ dính bẫy này."""
        lemma, sua = self._xu("это", "этот", ["это", "этот"])
        self.assertEqual(lemma, "это")
        self.assertTrue(sua, "phai bao la DA LAT cau tra loi cua AI")

    def test_luat3_dap_an_AI_hop_le_thi_GIU_du_KHONG_pho_bien_nhat(self):
        """🔴 Luật chết đầu tiên nếu ai đó "đơn giản hoá thành từ điển luôn
        thắng": `стали` trong `из стали` là `сталь` (thép), không phải `стать`
        (trở nên) — chỉ ngữ cảnh câu mới biết, mà ngữ cảnh là thứ AI có."""
        self.assertEqual(self._xu("стали", "сталь", ["стать", "сталь"]),
                         ("сталь", False))

    def test_luat4_AI_tra_ve_thu_KHONG_phai_lemma_thi_tu_dien_thang(self):
        self.assertEqual(self._xu("дети", "дети", ["ребёнок"]), ("ребёнок", True))


class MotChucNangMotLoi(unittest.TestCase):
    """Nguyên tắc user chốt 29/07/2026: **một chức năng một script**, trùng thì
    tách tầng chứ đừng đồng bộ tay. Hai ca đã trả học phí:

    · **Ba luồng chạy nền của bot** từng là ba bản sao lệch nhau ÂM THẦM — sửa
      một chỗ, hai chỗ kia vẫn chạy luật cũ. Gom về `core.chay_hang_loat()`.
    · **`/sua`** = làm lại thẻ hoàn toàn, đi chung `build_card_fields` với đường
      thêm thẻ mới. Cơ chế "preset tinh chỉnh" cũ đã xoá hẳn (20/07/2026).

    Test khoá đúng một điều: **chỉ được có MỘT định nghĩa**. Mọc thêm bản thứ hai
    là tái phạm, và đó là kiểu hỏng không ai thấy cho tới lúc hai bản lệch nhau."""

    @staticmethod
    def _dem_dinh_nghia(ten):
        goc = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        import ast as _ast
        n = []
        for thu_muc, _, files in os.walk(goc):
            if any(x in thu_muc for x in (".git", "_daxong", "__pycache__", "tests")):
                continue
            for f in files:
                if not f.endswith(".py"):
                    continue
                duong = os.path.join(thu_muc, f)
                try:
                    with open(duong, encoding="utf-8") as fh:
                        cay = _ast.parse(fh.read())
                except (OSError, SyntaxError, UnicodeDecodeError):
                    continue
                for node in _ast.walk(cay):
                    if (isinstance(node, (_ast.FunctionDef, _ast.AsyncFunctionDef))
                            and node.name == ten):
                        n.append(os.path.relpath(duong, goc))
        return n

    def test_chay_hang_loat_chi_co_MOT_ban(self):
        noi = self._dem_dinh_nghia("chay_hang_loat")
        self.assertEqual(len(noi), 1, f"co {len(noi)} ban chay_hang_loat: {noi}")

    def test_build_card_fields_chi_co_MOT_ban(self):
        noi = self._dem_dinh_nghia("build_card_fields")
        self.assertEqual(len(noi), 1, f"co {len(noi)} ban build_card_fields: {noi}")

    def test_duong_sua_the_di_chung_loi_voi_duong_them_moi(self):
        """`/sua` phải đi qua `pipeline`, chứ không dựng lối tắt riêng."""
        goc = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(goc, "tgbot", "flow_edit.py"), encoding="utf-8") as fh:
            src = fh.read()
        self.assertIn("from anki_tools.pipeline import", src)


class TheChiPhoi(unittest.TestCase):
    """BUG THẬT 10/08/2026 — máy ghép đáp án đẻ ra tiếng Nga SAI mà vẫn báo XANH.

    Chạy thử lô đầu (17 thẻ) thì lối ghép ngây thơ `giới từ + dạng chia` nuốt mất
    luật biến thể chính tả, ra ba cụm sai: `в вто́рник` (phải `во вто́рник`),
    `в Фра́нции` (phải `во`), `с стола́` (phải `со стола́`). Không có gì kêu —
    người học chính là người duy nhất chịu hậu quả, mà lại không biết.

    Cách chữa: người soạn viết THẲNG dạng sẽ hiện vào cột 1 của
    `data/chi_phoi.tsv`; máy chỉ quy ngược về dạng gốc để xếp deck. CẤM làm chiều
    ngược lại — luật `в→во` phụ thuộc cụm phụ âm đứng sau, đoán là sai im lặng.
    """

    def setUp(self):
        from grammar_forms import chi_phoi
        self.cp = chi_phoi

    def test_bien_the_chi_quy_MOT_CHIEU_ve_dang_goc(self):
        from grammar_forms.config import BIEN_THE_GOC
        self.assertEqual(BIEN_THE_GOC["во"], "в")
        self.assertEqual(BIEN_THE_GOC["со"], "с")
        # Chiều ngược lại PHẢI không tồn tại: có nó là mời máy đoán rồi sai im lặng.
        self.assertNotIn("в", BIEN_THE_GOC)
        self.assertNotIn("с", BIEN_THE_GOC)

    def test_dang_chia_doc_duoc_ca_ba_kieu_bang(self):
        """Danh từ · đại từ · số từ lồng khác nhau trong dữ liệu OpenRussian."""
        danh_tu = {"decl": {"sg": {"acc": "шко́лу", "prep": "шко́ле"}}}
        dai_tu = {"proDecl": {"m": {"inst": "мной"}}}
        so_tu = {"numDecl": {"dat": "пяти́"}}
        self.assertEqual(self.cp.dang_chia(danh_tu, "4"), "шко́лу")
        self.assertEqual(self.cp.dang_chia(dai_tu, "5"), "мной")
        self.assertEqual(self.cp.dang_chia(so_tu, "3"), "пяти́")
        self.assertIsNone(self.cp.dang_chia({"decl": {"sg": {}}}, "2"))

    def test_soat_bat_hai_the_cung_tu_cung_cach(self):
        rows = [
            {"so_dong": 1, "lemma": "школа", "cach": "4", "viet": "đi vào trường"},
            {"so_dong": 2, "lemma": "школа", "cach": "4", "viet": "vào trường học"},
        ]
        tra = {"школа": {"decl": {"sg": {"acc": "шко́лу"}}}}
        loi = self.cp.soat(rows, tra)
        self.assertTrue(any("trùng" in l for l in loi), loi)

    def test_soat_bat_de_bai_MO_HO_hai_dap_an_dung(self):
        """Cùng danh từ, khác cách, mà dòng Việt giống hệt ⇒ gõ đúng bị chấm sai."""
        rows = [
            {"so_dong": 1, "lemma": "школа", "cach": "4", "viet": "ở trường"},
            {"so_dong": 2, "lemma": "школа", "cach": "6", "viet": "Ở TRƯỜNG"},
        ]
        tra = {"школа": {"decl": {"sg": {"acc": "шко́лу", "prep": "шко́ле"}}}}
        loi = self.cp.soat(rows, tra)
        self.assertTrue(any("GIỐNG HỆT" in l for l in loi), loi)

    def test_soat_bat_tu_chua_co_trong_deck(self):
        rows = [{"so_dong": 1, "lemma": "ктотокхонгcó", "cach": "2", "viet": "x"}]
        self.assertTrue(self.cp.soat(rows, {}))

    def test_doi_chieu_gom_theo_DANH_TU_nen_bat_cheo_duoc_gioi_tu(self):
        """`на рабо́ту` và `с рабо́ты` khác giới từ nhưng phải thấy nhau."""
        a = {"gt_hien": "на", "form": "рабо́ту", "cach": "4", "viet": "đi tới chỗ làm"}
        b = {"gt_hien": "с", "form": "рабо́ты", "cach": "2", "viet": "từ chỗ làm về"}
        html = self.cp.dung_doi_chieu(a, [a, b])
        self.assertIn("с рабо́ты", html)
        self.assertNotIn("на рабо́ту", html)   # không tự liệt kê chính mình

    def test_file_du_lieu_that_van_soat_sach(self):
        """Dữ liệu trong repo phải luôn đọc được và đúng cú pháp 4 cột."""
        rows, loi = self.cp.doc_tsv()
        self.assertEqual(loi, [], loi)
        self.assertTrue(rows)
        for r in rows:
            self.assertIn(r["cach"], list("123456"))
            self.assertTrue(r["viet"].strip(), f"dòng {r['so_dong']} thiếu tiếng Việt")


class BadgeGiongDienTayKhongDuocBiXoaNguoc(unittest.TestCase):
    """BUG GỐC (12/08/2026): `backfill_badge.py` tầng 3 so NHÃN hiển thị với 4 ký
    tự đầu của KHOÁ — `"FEM ♀".startswith("femi")` là False. Hai thứ chỉ trùng
    nhau do tình cờ ở `masculine`/`neuter`, nên FEM/PL/M-F trượt hết và script
    XOÁ MẤT badge đúng mà user (hoặc lô trước) đã điền tay — trái ngược điều
    docstring của chính nó hứa. Bắt được khi vá `иностранка` thiếu `GenderBadge`:
    chạy khan báo `FEM ♀ -> (xoá)`.
    """

    def setUp(self):
        import importlib.util
        goc = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        spec = importlib.util.spec_from_file_location(
            "_bb", os.path.join(goc, "scripts", "backfill_badge.py"))
        self.bb = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.bb)

    def _giu(self, nhan):
        """Từ điển KHÔNG ghi giống ⇒ tầng 3 phải đọc lại nhãn cũ trên thẻ."""
        cu = f'<div class="badge x">{nhan}</div>'
        return self.bb.chu(self.bb.gender_badge_wc("тест", {}, cu, []))

    def test_moi_giong_deu_giu_duoc_nhan_cu(self):
        for nhan in grammar.NHAN_GIONG.values():
            with self.subTest(nhan=nhan):
                self.assertEqual(self._giu(nhan), nhan)

    def test_FEM_la_ca_da_hong_that(self):
        self.assertEqual(self._giu("FEM ♀"), "FEM ♀")

    def test_khong_co_nhan_cu_thi_van_tra_rong(self):
        """Không được vì vá mà đâm ra bịa badge cho thẻ trắng."""
        self.assertEqual(self.bb.gender_badge_wc("тест", {}, "", []), "")


if __name__ == "__main__":
    unittest.main()
