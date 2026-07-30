# -*- coding: utf-8 -*-
"""LÔ 2 — field `HuongDan`: phần TÍNH TỪ `-ский` và TRẠNG TỪ `по-…-ски`
của họ quốc tịch. Đóng nốt hệ thống đã mở ở lô 1 (17 danh từ chỉ người).

Trọng tâm sư phạm của lô này KHÔNG phải từng từ, mà là **phân biệt hai thứ
người mới hay lẫn suốt**: `ру́сский язы́к` (tính từ, bổ nghĩa cho danh từ) và
`говори́ть по-ру́сски` (trạng từ, bổ nghĩa cho động từ). Nắm được cái này là
dùng đúng cả đời; không nắm thì sai mãi.

Chạy: python data/huongdan/lo02_quoctich_tinhtu_2026-07-27.py [--apply]
"""
raise SystemExit("KHAI TU 30/07/2026: chuan v1 — chay lai se XOA BANG CHIA the that. Xem QD-03.")
import json
import sys
import urllib.request
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from anki_tools import grammar

ANKI = "http://127.0.0.1:8765"

# --- Khối hệ thống dùng chung cho cả 15 thẻ (xem lô 1 về việc vì sao lặp lại) ---
HE = (
    '<div class="hd-sec">Hai dạng — ĐỪNG LẪN, đây là lỗi phổ biến nhất</div>'
    '<div class="hd-row"><span class="hd-piece">-ский</span>'
    '<span class="hd-gloss">TÍNH TỪ, đi kèm DANH TỪ: ру́сский <b>язы́к</b> tiếng Nga · '
    'ру́сская <b>кни́га</b> quyển sách Nga</span></div>'
    '<div class="hd-row"><span class="hd-piece">по-…-ски</span>'
    '<span class="hd-gloss">TRẠNG TỪ, đi kèm ĐỘNG TỪ: говорю́ <b>по-ру́сски</b> tôi nói tiếng Nga · '
    'чита́ю <b>по-ру́сски</b> tôi đọc tiếng Nga</span></div>'
    '<div class="hd-why">Cách dựng trạng từ: lấy tính từ, <b>bỏ chữ й cuối</b> rồi thêm <b>по-</b> '
    'ở đầu. ру́сск<b>ий</b> → <b>по-</b>ру́сск<b>и</b>. Trạng từ KHÔNG BAO GIỜ biến đổi — '
    'đó là chỗ dễ hơn tính từ, vốn phải hợp giống và hợp cách với danh từ.</div>'
)

S = {}

# ============================== TÍNH TỪ =====================================

S["русский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">Рус-</span><span class="hd-gloss">Русь — nhà nước Nga cổ, gốc của cả tên dân tộc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ск-</span><span class="hd-gloss">hậu tố tạo TÍNH TỪ từ tên đất, tên người</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span><span class="hd-gloss">đuôi tính từ, giống đực số ít</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ <b>đặc biệt nhất</b> trong tiếng Nga: đây là quốc tịch duy nhất mà người ta gọi bằng <b>TÍNH TỪ</b>, không phải danh từ. Người Nga là <b>ру́сский</b> (đàn ông) / <b>ру́сская</b> (phụ nữ) — nghĩa đen là "người thuộc về Rus". Mọi dân tộc khác đều có danh từ riêng (не́мец, испа́нец…), riêng Nga thì không.</div>'
    '<div class="hd-why">Hai chữ <b>с</b> là do <b>Рус</b> + <b>ск</b> ghép lại, mỗi bên góp một chữ. Nhớ vậy thì không bao giờ viết thiếu.</div>'
    '<div class="hd-warn"><b>Bẫy nghĩa:</b> <b>ру́сский</b> = thuộc DÂN TỘC Nga; <b>росси́йский</b> = thuộc NHÀ NƯỚC Nga. Hộ chiếu ghi <i>российский</i>, ngôn ngữ thì luôn là <i>русский язык</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>Росси́я</b> nước Nga · <b>ру́сский</b> người Nga / tiếng Nga · <b>по-ру́сски</b> bằng tiếng Nga · <b>росси́йский</b> thuộc nhà nước Nga · <b>россия́нин</b> công dân Nga</div>'
    + HE
)

S["английский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">Англи-</span><span class="hd-gloss">А́нглия — nước Anh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-йск-</span><span class="hd-gloss">hậu tố tính từ, biến thể sau nguyên âm <b>и</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span><span class="hd-gloss">đuôi tính từ, giống đực số ít</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tên nước tận cùng bằng <b>-ия</b> thì hậu tố mọc thêm chữ <b>й</b> cho trôi miệng: Англ<b>и</b>я → англ<b>ийс</b>кий. Cùng luật: Ита́лия → италья́нский, Росси́я → росси́йский.</div>'
    '<div class="hd-warn"><b>Bẫy:</b> tính từ dựng từ TÊN NƯỚC (Англия), còn danh từ chỉ người lại dựng khác hẳn — <b>англича́нин</b>. Hai nhánh này không suy ra được nhau.</div>'
    '<div class="hd-sec">Họ hàng — nước Anh</div>'
    '<div class="hd-fam"><b>А́нглия</b> nước Anh · <b>англича́нин</b> người Anh (nam) · <b>англича́нка</b> (nữ) · <b>англи́йский</b> thuộc Anh · <b>по-англи́йски</b> bằng tiếng Anh</div>'
    + HE
)

S["немецкий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">нем-</span><span class="hd-gloss">CÂM — cùng gốc <b>немо́й</b> (câm), xem thẻ <b>не́мец</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ец-</span><span class="hd-gloss">hậu tố người, còn sót lại trong tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-кий</span><span class="hd-gloss">đuôi tính từ, dạng rút gọn của <b>-ский</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là tính từ dựng từ <b>tên người</b> (не́мец) chứ không phải tên nước — vì nước là <b>Герма́ния</b>, chẳng liên quan gì. Khi <b>ц</b> gặp <b>-ский</b> thì hai chữ <b>с</b> nuốt mất một: не́мец + ский → неме́<b>цкий</b>.</div>'
    '<div class="hd-why">Luật <b>ц + ск → цк</b> này lặp lại khắp nơi: неме́цкий, ры́бацкий (thuộc dân chài), кузне́цкий (thuộc thợ rèn).</div>'
    '<div class="hd-warn"><b>Bẫy trọng âm:</b> danh từ là <b>не́мец</b> (nhấn đầu) nhưng tính từ là <b>неме́цкий</b> (nhấn giữa). Trọng âm DỊCH khi thêm hậu tố — chuyện rất thường ở tiếng Nga.</div>'
    '<div class="hd-sec">Họ hàng — gốc нем- (câm)</div>'
    '<div class="hd-fam"><b>немо́й</b> câm · <b>не́мец</b> người Đức (nam) · <b>не́мка</b> (nữ) · <b>неме́цкий</b> thuộc Đức · <b>по-неме́цки</b> bằng tiếng Đức · <b>Герма́ния</b> nước Đức</div>'
    + HE
)

S["французский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">француз-</span><span class="hd-gloss">францу́з — người Pháp (danh từ)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ск-</span><span class="hd-gloss">hậu tố tạo tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span><span class="hd-gloss">đuôi tính từ, giống đực số ít</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dựng từ <b>францу́з</b> chứ không phải từ <b>Фра́нция</b> — nên giữ nguyên chữ <b>з</b>, thành cụm <b>-зск-</b> ba phụ âm liền. Trông nặng nhưng viết đúng thì dễ: cứ lấy <b>францу́з</b> nguyên vẹn rồi dán <b>-ский</b>.</div>'
    '<div class="hd-warn"><b>Bẫy:</b> đọc thì <b>з</b> gần như biến mất (nghe như "фран-ЦУС-кий") nhưng <b>viết vẫn phải có з</b>. Đây đúng loại lỗi bạn hay mắc ở ô gõ.</div>'
    '<div class="hd-sec">Họ hàng — nước Pháp</div>'
    '<div class="hd-fam"><b>Фра́нция</b> nước Pháp · <b>францу́з</b> người Pháp (nam) · <b>францу́женка</b> (nữ) · <b>францу́зский</b> thuộc Pháp · <b>по-францу́зски</b> bằng tiếng Pháp</div>'
    + HE
)

S["испанский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">Испан-</span><span class="hd-gloss">Испа́ния — Tây Ban Nha</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ск-</span><span class="hd-gloss">hậu tố tạo tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span><span class="hd-gloss">đuôi tính từ, giống đực số ít</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mẫu <b>sạch nhất</b> của cả nhóm tính từ: thân từ + <b>-ский</b>, không biến âm, không thêm bớt chữ nào. Lấy từ này làm chuẩn rồi đối chiếu các từ khác xem chúng lệch ở đâu.</div>'
    '<div class="hd-sec">Họ hàng — Tây Ban Nha</div>'
    '<div class="hd-fam"><b>Испа́ния</b> Tây Ban Nha · <b>испа́нец</b> người TBN (nam) · <b>испа́нка</b> (nữ) · <b>испа́нский</b> thuộc TBN · <b>по-испа́нски</b> bằng tiếng TBN</div>'
    + HE
)

S["китайский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">Китай-</span><span class="hd-gloss">Кита́й — Trung Quốc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ск-</span><span class="hd-gloss">hậu tố tạo tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span><span class="hd-gloss">đuôi tính từ, giống đực số ít</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tên nước đã sẵn chữ <b>й</b> ở cuối (Кита́<b>й</b>) nên dán thẳng <b>-ский</b> vào là xong — chữ <b>й</b> trong <b>кита́йский</b> chính là chữ й của tên nước, không phải chữ mọc thêm.</div>'
    '<div class="hd-sec">Họ hàng — Trung Quốc</div>'
    '<div class="hd-fam"><b>Кита́й</b> Trung Quốc · <b>кита́ец</b> người TQ (nam) · <b>китая́нка</b> (nữ) · <b>кита́йский</b> thuộc TQ · <b>по-кита́йски</b> bằng tiếng Trung</div>'
    + HE
)

S["арабский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">араб-</span><span class="hd-gloss">ара́б — người Ả Rập (gốc trơn)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ск-</span><span class="hd-gloss">hậu tố tạo tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span><span class="hd-gloss">đuôi tính từ, giống đực số ít</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc trơn nên ghép sạch, không biến âm — y hệt <b>испа́нский</b>. Chú ý: <b>б</b> cuối gốc đọc điếc thành "p" (nghe như "а-РАП-ский") nhưng <b>viết vẫn là б</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ара́б</b> người Ả Rập (nam) · <b>ара́бка</b> (nữ) · <b>ара́бский</b> thuộc Ả Rập · <b>по-ара́бски</b> bằng tiếng Ả Rập</div>'
    + HE
)

S["американский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">Америк-</span><span class="hd-gloss">Аме́рика — nước Mỹ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ан-</span><span class="hd-gloss">phần thân quốc tế, đúng chữ <i>Americ-an</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ский</span><span class="hd-gloss">hậu tố + đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ <b>dài nhất</b> nhóm này nhưng dễ nhất, vì tiếng Anh đã cho sẵn <i>American</i> — chỉ việc nối thêm <b>-ский</b>. Đọc thầm "American + ский" là gõ đúng.</div>'
    '<div class="hd-sec">Họ hàng — nước Mỹ</div>'
    '<div class="hd-fam"><b>Аме́рика</b> nước Mỹ · <b>америка́нец</b> người Mỹ (nam) · <b>америка́нка</b> (nữ) · <b>америка́нский</b> thuộc Mỹ · <b>по-америка́нски</b> theo kiểu Mỹ</div>'
    + HE
)

S["вьетнамский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">Вьетнам-</span><span class="hd-gloss">Вьетна́м — Việt Nam</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ск-</span><span class="hd-gloss">hậu tố tạo tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span><span class="hd-gloss">đuôi tính từ, giống đực số ít</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ghép sạch, không biến âm. Chỗ duy nhất cần để mắt là cụm mở đầu <b>Вье-</b>: chữ <b>в</b> rồi <b>ь</b> rồi <b>е</b> — tiếng Nga viết tên nước bạn bằng ba ký tự đó.</div>'
    '<div class="hd-sec">Họ hàng — Việt Nam</div>'
    '<div class="hd-fam"><b>Вьетна́м</b> Việt Nam · <b>вьетна́мец</b> người Việt (nam) · <b>вьетна́мка</b> (nữ) · <b>вьетна́мский</b> thuộc Việt Nam · <b>по-вьетна́мски</b> bằng tiếng Việt</div>'
    + HE
)

# ============================== TRẠNG TỪ ====================================

def _adv(nuoc_html, ho_hang, rieng=""):
    return (
        '<div class="hd-sec">Chẻ từ</div>'
        '<div class="hd-row"><span class="hd-piece">по-</span><span class="hd-gloss">tiền tố "theo kiểu…, bằng…"</span></div>'
        + nuoc_html +
        '<div class="hd-row"><span class="hd-piece">-ски</span><span class="hd-gloss">đuôi TRẠNG TỪ — chính là <b>-ский</b> đã bỏ chữ <b>й</b></span></div>'
        + rieng +
        '<div class="hd-sec">Họ hàng</div>'
        f'<div class="hd-fam">{ho_hang}</div>'
        + HE
    )


S["по-русски"] = _adv(
    '<div class="hd-row"><span class="hd-piece">-русс-</span><span class="hd-gloss">Русь — gốc của tên dân tộc Nga</span></div>',
    '<b>Росси́я</b> nước Nga · <b>ру́сский</b> người Nga / tiếng Nga · <b>по-ру́сски</b> bằng tiếng Nga · <b>россия́нин</b> công dân Nga',
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là từ bạn sẽ dùng nhiều nhất cả đời học tiếng Nga: <b>Я говорю́ по-ру́сски</b> = Tôi nói tiếng Nga. Nhớ nguyên câu đó thay vì nhớ từ lẻ.</div>'
    '<div class="hd-warn"><b>Bẫy:</b> giữ đủ <b>hai chữ с</b> (từ Рус + ск) và <b>KHÔNG có й</b> ở cuối. Sai một trong hai là hỏng: <i>*по-руски</i>, <i>*по-русский</i> đều sai.</div>'
)

S["по-английски"] = _adv(
    '<div class="hd-row"><span class="hd-piece">-англий-</span><span class="hd-gloss">А́нглия — nước Anh</span></div>',
    '<b>А́нглия</b> nước Anh · <b>англича́нин</b> người Anh · <b>англи́йский</b> thuộc Anh · <b>по-англи́йски</b> bằng tiếng Anh',
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ tính từ <b>англи́йский</b> bỏ chữ <b>й</b> cuối là ra: англи́йск<b>ий</b> → по-англи́йск<b>и</b>. Chữ <b>й</b> ở GIỮA từ (англи́<b>й</b>ски) vẫn còn — chỉ chữ й ở CUỐI mới bỏ.</div>'
    '<div class="hd-why">Dùng ngay: <b>Я говорю́ по-англи́йски</b> = Tôi nói tiếng Anh.</div>'
)

S["по-немецки"] = _adv(
    '<div class="hd-row"><span class="hd-piece">-немец-</span><span class="hd-gloss">не́мец — người Đức, gốc <b>нем-</b> = CÂM</span></div>',
    '<b>немо́й</b> câm · <b>не́мец</b> người Đức · <b>неме́цкий</b> thuộc Đức · <b>по-неме́цки</b> bằng tiếng Đức · <b>Герма́ния</b> nước Đức',
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ tính từ <b>неме́цкий</b> bỏ <b>й</b>: → <b>по-неме́цки</b>. Vẫn giữ cụm <b>цк</b> do <b>ц + ск</b> ghép lại.</div>'
    '<div class="hd-warn"><b>Bẫy trọng âm:</b> <b>не́мец</b> nhấn đầu, nhưng <b>по-неме́цки</b> nhấn giữa — giống tính từ chứ không giống danh từ.</div>'
)

S["по-французски"] = _adv(
    '<div class="hd-row"><span class="hd-piece">-француз-</span><span class="hd-gloss">францу́з — người Pháp</span></div>',
    '<b>Фра́нция</b> nước Pháp · <b>францу́з</b> người Pháp · <b>францу́женка</b> (nữ) · <b>францу́зский</b> thuộc Pháp · <b>по-францу́зски</b> bằng tiếng Pháp',
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ dài nhất nhóm trạng từ. Dựng đúng luật chung: <b>францу́зский</b> bỏ <b>й</b> → <b>по-францу́зски</b>.</div>'
    '<div class="hd-warn"><b>Bẫy:</b> chữ <b>з</b> đọc gần như mất (nghe "фран-ЦУС-ки") nhưng <b>viết vẫn phải có</b>. Đếm đủ: <b>ф-р-а-н-ц-у-з-с-к-и</b>.</div>'
)

S["по-испански"] = _adv(
    '<div class="hd-row"><span class="hd-piece">-испан-</span><span class="hd-gloss">Испа́ния — Tây Ban Nha</span></div>',
    '<b>Испа́ния</b> Tây Ban Nha · <b>испа́нец</b> người TBN · <b>испа́нка</b> (nữ) · <b>испа́нский</b> thuộc TBN · <b>по-испа́нски</b> bằng tiếng TBN',
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mẫu sạch nhất của nhóm trạng từ, không biến âm gì: <b>по-</b> + <b>испан</b> + <b>-ски</b>. Lấy từ này làm chuẩn để đối chiếu các từ khác.</div>'
)

S["по-китайски"] = _adv(
    '<div class="hd-row"><span class="hd-piece">-китай-</span><span class="hd-gloss">Кита́й — Trung Quốc</span></div>',
    '<b>Кита́й</b> Trung Quốc · <b>кита́ец</b> người TQ · <b>китая́нка</b> (nữ) · <b>кита́йский</b> thuộc TQ · <b>по-кита́йски</b> bằng tiếng Trung',
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chữ <b>й</b> ở giữa (кита́<b>й</b>ски) là chữ й của tên nước <b>Кита́й</b>, nên nó ở lại. Chỉ chữ <b>й</b> ở CUỐI tính từ mới bị bỏ khi thành trạng từ.</div>'
)


# ---------------------------------------------------------------------------
def ac(action, **params):
    req = urllib.request.Request(
        ANKI, json.dumps({"action": action, "version": 6, "params": params}).encode())
    out = json.load(urllib.request.urlopen(req, timeout=180))
    if out.get("error"):
        raise RuntimeError(f"{action}: {out['error']}")
    return out["result"]


def main():
    apply = "--apply" in sys.argv
    ok, miss = [], []
    for word, html in S.items():
        ids = ac("findNotes", query=f'note:RU_Word WordClean:{word}')
        if len(ids) != 1:
            miss.append((word, len(ids)))
            continue
        if apply:
            # 🔴 GIỮ BẢNG CHIA. Script này viết 27/07, trước khi ô Hướng dẫn có
            # bảng chia máy dựng ở cuối. Ghi thẳng `html` là XOÁ MẤT bảng, im
            # lặng, chỉ phát hiện khi mở thẻ ra xem. `attach_table` nối lại bảng
            # từ dữ liệu từ điển nên chạy lại script cũ cũng không phá gì.
            ac("updateNoteFields", note={"id": ids[0], "fields": {
                "HuongDan": grammar.attach_table(html, grammar.get_cached(word))}})
        ok.append(word)

    print(f"khop: {len(ok)}/{len(S)}")
    for w, n in miss:
        print(f"  !! {w}: tim thay {n} note")
    if apply:
        print("da ghi. sync:", ac("sync"))
    else:
        print("(chua ghi gi — them --apply de ghi that)")


if __name__ == "__main__":
    main()
