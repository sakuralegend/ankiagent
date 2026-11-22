# -*- coding: utf-8 -*-
"""k158 — tu-moi: ba từ user tự thêm, soạn từng thẻ độc lập.

Chỗ cần nhất quán:
(1) замо́к giữ ĐÚNG cách chẻ của thẻ за́мок (k155): за- «khép lại» + -мок gốc «đóng kín»
    (замкну́ть). Hai từ cùng gốc, chỉ khác chỗ nhấn — mỗi thẻ một dòng chớ nhầm.
(2) наре́зать / нареза́ть: gốc рез- = CẮT, khớp ре́зать (k142: «на- thành nhiều miếng»).
    Hai thẻ là MỘT cặp thể, khác nhau đúng ở trọng âm. Luật «nhấn ре́ = HT, nhấn а́ = CHT»
    trải ở thẻ наре́зать; thẻ нареза́ть chỉ dẫn chiếu.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "наре́зать": "thái, thái nhỏ, cắt thành miếng",   # bỏ «cắt» trơn — nghĩa chung của ре́зать; gloss: cut (food) / chop
    "нареза́ть": "thái, thái lát, cắt thành miếng",   # bỏ «cắt, xắt» — chứa trọn đề ре́зать (k142, cùng IMPF); gloss: slice
}

# ----------------------------------------------------------------- замо́к
S["замо́к"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">tiền tố «khép lại» (như <b>закры́ть</b> đóng)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мок</span>'
    '<span class="hd-gloss">gốc «đóng kín» — có trong <b>замкну́ть</b> khép kín</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thứ giữ cho cửa khép kín ⇒ ổ khoá. Chữ о rơi và trọng âm nhảy ra đuôi: '
    '<b>замка́</b>, <b>в замке́</b>, số nhiều <b>замки́</b>.</div>'
    '<div class="hd-warn">Chớ nhầm với <b>за́мок</b> lâu đài: cùng gốc, nhưng lâu đài nhấn ĐẦU (<b>за́мка</b>), '
    'ổ khoá nhấn CUỐI (<b>замка́</b>).</div>'
    '<div class="hd-warn"><b>закры́ть дверь на замо́к</b> = khoá cửa lại (<b>на</b> + cách 4).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>замкну́ть</b> khép kín · <b>замо́чный</b> thuộc ổ khoá '
    '(<b>замо́чная сква́жина</b> lỗ khoá) · <b>за́мок</b> lâu đài</div>'
)

# ----------------------------------------------------------------- наре́зать
S["наре́зать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">thành NHIỀU miếng, ra một lượng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ре́з-</span>'
    '<span class="hd-gloss">CẮT (như <b>ре́зать</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cắt cho ra nhiều miếng ⇒ thái: <b>наре́зать хлеб</b> thái bánh mì. '
    'Giữ <b>з → ж</b> y như <b>ре́зать</b> ở mọi ngôi: <b>наре́жу</b>, <b>наре́жешь</b>, '
    '<b>наре́жут</b> (thể HT nên đây là tương lai).</div>'
    '<div class="hd-warn">Chỗ nhấn quyết định THỂ: <b>наре́зать</b> (HT, <b>наре́жу</b>) ↔ '
    '<b>нареза́ть</b> (CHT, <b>нареза́ю</b>). Cùng khuôn: <b>отре́зать</b> / <b>отреза́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ре́зать</b> cắt · <b>наре́зка</b> đồ thái lát · '
    '<b>отре́зать</b> cắt rời · <b>ре́зкий</b> gắt, đột ngột</div>'
)

# ----------------------------------------------------------------- нареза́ть
S["нареза́ть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">thành NHIỀU miếng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-рез-</span>'
    '<span class="hd-gloss">CẮT (như <b>ре́зать</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi CHT, mang trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>наре́зать</b>: cùng chữ, dời trọng âm ra đuôi là thành CHT '
    '(luật trải ở thẻ đó). Chia đều như <b>чита́ть</b>: <b>нареза́ю</b>, <b>нареза́ешь</b> — '
    'KHÔNG có з → ж.</div>'
    '<div class="hd-warn">Chớ lẫn với <b>ре́зать</b> cắt nói chung: <b>нареза́ть</b> luôn là cắt '
    'THÀNH MIẾNG — thái, thái lát.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>наре́зать</b> thái (HT) · <b>ре́зать</b> cắt · '
    '<b>наре́зка</b> đồ thái lát · <b>разреза́ть</b> cắt ra</div>'
)

B = {
    "docbangmat": 18,
    "loitubat": 1,      # замо́к: ô đỏ chớ nhầm gõ «за́mок» (chữ m LATIN) — từ không tồn tại, bộ soát không bắt vì không đối chiếu được; tự sửa
    "nguonsai": 0,
    "baolen": [
        "V нареза́ть «cắt, thái, xắt» → «thái, thái lát, cắt thành miếng» (gỡ va chạm ре́зать «cắt, xắt» theo khai của luồng chính). Đã giả lập do_va_cham trên toàn bộ thẻ với V mới (chỉ đọc Anki): 0 va chạm dính lô này.",
        "V наре́зать «cắt, thái, thái nhỏ» → «thái, thái nhỏ, cắt thành miếng»: bỏ «cắt» trơn KHÔNG do va chạm (badge PERF đã tách khỏi ре́зать IMPF) mà vì «cắt» chung chung là nghĩa của ре́зать, còn на- = cắt thành miếng — cần duyệt.",
        "Hai đề наре́зать/нареза́ть lệch nhau một cụm (thái nhỏ ← chop / thái lát ← slice) vì mỗi thẻ theo gloss riêng; thực ra cặp thể này cùng nghĩa, badge thể tách hai đề. Muốn hai dòng giống hệt thì đặt cả hai = «thái, thái lát, thái nhỏ, cắt thành miếng».",
        "Trọng âm khớp nghĩa: наре́зать = HT (наре́жу), нареза́ть = CHT (нареза́ю) — đúng với gloss từng thẻ và khuôn отре́зать/отреза́ть, разре́зать/разреза́ть.",
        "Chỗ KHÔNG chắc lắm: наре́зка «đồ thái lát» (nghĩa siêu thị: thịt nguội/phô mai thái sẵn) — từ còn nghĩa «sự thái», tôi chọn nghĩa hay gặp nhất.",
        "замо́к: giữ V «ổ khóa, cái khóa» (không trùng ai); chẻ từ chép đúng cách của thẻ за́мок (k155) để hai thẻ nhất quán.",
    ],
}
