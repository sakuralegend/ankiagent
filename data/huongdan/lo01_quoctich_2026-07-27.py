# -*- coding: utf-8 -*-
"""LÔ 1 — nội dung field `HuongDan` cho họ QUỐC TỊCH (phần danh từ chỉ người).

Vì sao gom theo họ chứ không chia đều: 32/168 từ đang học nằm trong CÙNG MỘT hệ
thống (-ец / -ка / -ский / по-…-ски). Soạn cùng nhau thì lời giải thích nhất quán
và không tự mâu thuẫn giữa các lô. Lô này là 17 danh từ chỉ người; tính từ và
trạng từ по-…-ски để lô 2.

Cấu trúc mỗi mục (xem memory field-huong-dan): Chẻ từ -> Cách nhớ -> Họ hàng.
KHÔNG phiên âm, KHÔNG mnemonic — user đã bỏ hẳn hướng đó 27/07/2026.

Chạy: python data/huongdan/lo01_quoctich_2026-07-27.py [--apply]
Không có --apply thì chỉ đối chiếu key, không ghi gì.
"""
import json
import sys
import urllib.request

ANKI = "http://127.0.0.1:8765"

# --- Khối hệ thống dùng chung: lặp lại ở MỌI thẻ là cố ý. User chỉ nhìn thấy
# một thẻ tại một thời điểm, và gặp lại bộ bốn này 32 lần chính là spaced
# repetition cho bản thân cái hệ thống. ---
HE = (
    '<div class="hd-sec">Bộ bốn quốc tịch — thuộc bộ này là suy ra được mọi nước</div>'
    '<div class="hd-row"><span class="hd-piece">-ец</span>'
    '<span class="hd-gloss">người NAM: испа́н<b>ец</b>, коре́<b>ец</b>, не́м<b>ец</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">người NỮ: испа́н<b>ка</b>, не́м<b>ка</b>, америка́н<b>ка</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ский</span>'
    '<span class="hd-gloss">TÍNH TỪ: испа́н<b>ский</b>, неме́ц<b>кий</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">по-…-ски</span>'
    '<span class="hd-gloss">NÓI tiếng đó: <b>по-</b>испа́н<b>ски</b></span></div>'
)

S = {}

S["американка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">Америк-</span><span class="hd-gloss">Аме́рика — nước Mỹ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ан-</span><span class="hd-gloss">phần thân quốc tế, đúng chữ <i>Americ-an</i> của tiếng Anh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span><span class="hd-gloss">hậu tố NGƯỜI NỮ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiếng Anh đã cho bạn <i>American</i> — chỉ việc thay đuôi <i>-an</i> thành <b>-ец</b> (nam) hoặc <b>-ка</b> (nữ). Đây là từ dễ nhất trong cả họ vì bạn đã biết sẵn thân từ.</div>'
    '<div class="hd-sec">Họ hàng — nước Mỹ</div>'
    '<div class="hd-fam"><b>Аме́рика</b> nước Mỹ · <b>америка́нец</b> người Mỹ (nam) · <b>америка́нка</b> người Mỹ (nữ) · <b>америка́нский</b> thuộc Mỹ · <b>по-америка́нски</b> theo kiểu Mỹ</div>'
    + HE
)

S["англичанин"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">Англи-</span><span class="hd-gloss">А́нглия — nước Anh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-чан-</span><span class="hd-gloss">biến âm của <b>-ан-</b> sau <b>и</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ин</span><span class="hd-gloss">hậu tố NGƯỜI NAM — lớp cổ hơn <b>-ец</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là từ <b>phá luật</b> đầu tiên bạn gặp: người Anh KHÔNG phải <i>*англиец</i> mà là <b>англича́нин</b>. Hậu tố <b>-анин / -янин</b> là lớp cổ, dùng cho vài dân tộc quen thuộc lâu đời với người Nga.</div>'
    '<div class="hd-why">Cùng lớp đó: <b>россия́нин</b> công dân Nga · <b>славя́нин</b> người Slav · <b>христиани́н</b> tín đồ Cơ Đốc · <b>египтя́нин</b> người Ai Cập.</div>'
    '<div class="hd-warn"><b>Bẫy số nhiều:</b> lớp <b>-анин</b> RỤNG mất <b>-ин</b> khi sang số nhiều — англича́н<b>ин</b> → англича́н<b>е</b> (không phải <i>*англичанины</i>). Y hệt: славя́нин → славя́не.</div>'
    '<div class="hd-sec">Họ hàng — nước Anh</div>'
    '<div class="hd-fam"><b>А́нглия</b> nước Anh · <b>англича́нин</b> người Anh (nam) · <b>англича́нка</b> người Anh (nữ) · <b>англи́йский</b> thuộc Anh · <b>по-англи́йски</b> bằng tiếng Anh</div>'
    + HE
)

S["англичанка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">Англи-</span><span class="hd-gloss">А́нглия — nước Anh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-чан-</span><span class="hd-gloss">biến âm của <b>-ан-</b> sau <b>и</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span><span class="hd-gloss">hậu tố NGƯỜI NỮ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bên nữ trở lại đúng luật: cứ <b>-ка</b>. Chỉ bên nam mới lệch (<b>англича́нин</b> chứ không phải <i>*англиец</i>) — nhớ một chỗ lệch là đủ, đừng nhớ hai.</div>'
    '<div class="hd-sec">Họ hàng — nước Anh</div>'
    '<div class="hd-fam"><b>А́нглия</b> nước Anh · <b>англича́нин</b> người Anh (nam) · <b>англича́нка</b> người Anh (nữ) · <b>англи́йский</b> thuộc Anh · <b>по-англи́йски</b> bằng tiếng Anh</div>'
    + HE
)

S["араб"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ <b>gốc trơn</b>, không chẻ được — vay mượn quốc tế, đúng chữ <i>Arab</i> của tiếng Anh. Không có tiền tố hay hậu tố nào cả.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhóm này khác quốc tịch thường: <b>ара́б</b> chỉ một DÂN TỘC chứ không gắn với một nước. Vì thế nó trần trụi, không đội hậu tố <b>-ец</b> nào.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ара́б</b> người Ả Rập (nam) · <b>ара́бка</b> người Ả Rập (nữ) · <b>ара́бский</b> thuộc Ả Rập · <b>по-ара́бски</b> bằng tiếng Ả Rập · <b>Ара́вия</b> bán đảo Ả Rập</div>'
    + HE
)

S["арабка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">араб-</span><span class="hd-gloss">ара́б — người Ả Rập (dạng nam, gốc trơn)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span><span class="hd-gloss">hậu tố NGƯỜI NỮ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trường hợp sạch nhất của cả họ: dạng nam không có hậu tố gì, nên dạng nữ chỉ việc dán thẳng <b>-ка</b> vào. Không biến âm, không rụng chữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ара́б</b> người Ả Rập (nam) · <b>ара́бка</b> người Ả Rập (nữ) · <b>ара́бский</b> thuộc Ả Rập · <b>по-ара́бски</b> bằng tiếng Ả Rập</div>'
    + HE
)

S["испанец"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">Испан-</span><span class="hd-gloss">Испа́ния — Tây Ban Nha</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ец</span><span class="hd-gloss">hậu tố NGƯỜI NAM</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là <b>mẫu chuẩn</b> của cả họ — học thuộc từ này thì suy ra được phần lớn các từ còn lại: bỏ <b>-ия</b> của tên nước, dán <b>-ец</b> vào.</div>'
    '<div class="hd-warn"><b>Bẫy chính tả:</b> chữ <b>е</b> trong <b>-ец</b> RỤNG khi biến cách — испа́н<b>ец</b> → испа́нца, испа́нцу, испа́нцы. Cả lớp <b>-ец</b> đều vậy: не́мец → не́мцы, коре́ец → коре́йцы.</div>'
    '<div class="hd-sec">Họ hàng — Tây Ban Nha</div>'
    '<div class="hd-fam"><b>Испа́ния</b> Tây Ban Nha · <b>испа́нец</b> người TBN (nam) · <b>испа́нка</b> người TBN (nữ) · <b>испа́нский</b> thuộc TBN · <b>по-испа́нски</b> bằng tiếng TBN</div>'
    + HE
)

S["испанка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">Испан-</span><span class="hd-gloss">Испа́ния — Tây Ban Nha</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span><span class="hd-gloss">hậu tố NGƯỜI NỮ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dạng nữ dựng từ THÂN TỪ (испан-), không phải từ dạng nam: <b>không</b> phải испанец + ка. Nhớ vậy thì mọi dạng nữ đều dễ — cứ lấy tên nước bỏ đuôi rồi dán <b>-ка</b>.</div>'
    '<div class="hd-sec">Họ hàng — Tây Ban Nha</div>'
    '<div class="hd-fam"><b>Испа́ния</b> Tây Ban Nha · <b>испа́нец</b> người TBN (nam) · <b>испа́нка</b> người TBN (nữ) · <b>испа́нский</b> thuộc TBN · <b>по-испа́нски</b> bằng tiếng TBN</div>'
    + HE
)

S["итальянец"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">Итал-</span><span class="hd-gloss">Ита́лия — nước Ý</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ьян-</span><span class="hd-gloss">biến âm của <b>-иан-</b>: chữ <b>и</b> co lại thành dấu mềm <b>ь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ец</span><span class="hd-gloss">hậu tố NGƯỜI NAM</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỗ dễ gõ sai duy nhất là cụm <b>-ья-</b>. Hình dung: <b>Итал-и-я</b> khi thêm hậu tố thì chữ <b>и</b> không đủ chỗ nên co lại thành dấu mềm <b>ь</b> → <b>италь-ян-ец</b>.</div>'
    '<div class="hd-warn"><b>Bẫy:</b> phải là <b>итальянец</b>, KHÔNG phải <i>*италианец</i> hay <i>*италйянец</i>. Dấu mềm <b>ь</b> đứng NGAY SAU <b>л</b>.</div>'
    '<div class="hd-sec">Họ hàng — nước Ý</div>'
    '<div class="hd-fam"><b>Ита́лия</b> nước Ý · <b>италья́нец</b> người Ý (nam) · <b>италья́нка</b> người Ý (nữ) · <b>италья́нский</b> thuộc Ý · <b>по-италья́нски</b> bằng tiếng Ý</div>'
    + HE
)

S["итальянка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">Итал-</span><span class="hd-gloss">Ита́лия — nước Ý</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ьян-</span><span class="hd-gloss">biến âm của <b>-иан-</b>: <b>и</b> co lại thành dấu mềm <b>ь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span><span class="hd-gloss">hậu tố NGƯỜI NỮ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chung y hệt dạng nam, chỉ đổi đuôi cuối: <b>италья́н</b> + <b>-ец</b> (nam) / <b>-ка</b> (nữ). Nhớ được cụm <b>-льян-</b> một lần là dùng cho cả bốn dạng.</div>'
    '<div class="hd-sec">Họ hàng — nước Ý</div>'
    '<div class="hd-fam"><b>Ита́лия</b> nước Ý · <b>италья́нец</b> người Ý (nam) · <b>италья́нка</b> người Ý (nữ) · <b>италья́нский</b> thuộc Ý · <b>по-италья́нски</b> bằng tiếng Ý</div>'
    + HE
)

S["китаянка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">Кита-</span><span class="hd-gloss">Кита́й — Trung Quốc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ян-</span><span class="hd-gloss">phần chèn, xuất hiện sau nguyên âm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span><span class="hd-gloss">hậu tố NGƯỜI NỮ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp nam–nữ ở đây <b>lệch nhau</b>, phải nhớ riêng: nam là <b>кита́ец</b> (chỉ -ец), nữ là <b>китая́нка</b> (có thêm -ян-). Không suy được cái này từ cái kia.</div>'
    '<div class="hd-warn"><b>Bẫy:</b> KHÔNG phải <i>*китайка</i>. Vì tên nước kết thúc bằng nguyên âm + <b>й</b>, phải chèn <b>-ян-</b> cho trôi. Y hệt: Коре́я → корея́нка.</div>'
    '<div class="hd-sec">Họ hàng — Trung Quốc</div>'
    '<div class="hd-fam"><b>Кита́й</b> Trung Quốc · <b>кита́ец</b> người TQ (nam) · <b>китая́нка</b> người TQ (nữ) · <b>кита́йский</b> thuộc TQ · <b>по-кита́йски</b> bằng tiếng Trung</div>'
    + HE
)

S["кореец"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">Коре-</span><span class="hd-gloss">Коре́я — Triều Tiên / Hàn Quốc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ец</span><span class="hd-gloss">hậu tố NGƯỜI NAM</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng luật chuẩn: bỏ <b>-я</b> của tên nước, dán <b>-ец</b>. Chữ <b>е</b> đôi liền nhau (<b>коре-ец</b>) trông lạ mắt nhưng không có gì đặc biệt.</div>'
    '<div class="hd-warn"><b>Bẫy biến cách:</b> khi biến cách, <b>е</b> của <b>-ец</b> rụng và mọc ra <b>й</b> — коре́<b>ец</b> → коре́<b>йц</b>а, коре́<b>йц</b>ы. Dạng nữ cũng lệch: <b>корея́нка</b> chứ không phải <i>*корейка</i>.</div>'
    '<div class="hd-sec">Họ hàng — Triều Tiên</div>'
    '<div class="hd-fam"><b>Коре́я</b> Triều Tiên · <b>коре́ец</b> người Triều Tiên (nam) · <b>корея́нка</b> (nữ) · <b>коре́йский</b> thuộc Triều Tiên · <b>по-коре́йски</b> bằng tiếng Triều Tiên</div>'
    + HE
)

S["кореянка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">Коре-</span><span class="hd-gloss">Коре́я — Triều Tiên / Hàn Quốc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ян-</span><span class="hd-gloss">phần chèn, xuất hiện sau nguyên âm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span><span class="hd-gloss">hậu tố NGƯỜI NỮ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp song sinh với <b>китая́нка</b> — cùng một luật: tên nước tận cùng bằng nguyên âm thì dạng nữ chèn <b>-ян-</b> trước <b>-ка</b>. Nhớ hai từ này chung một chỗ.</div>'
    '<div class="hd-warn"><b>Bẫy:</b> KHÔNG phải <i>*корейка</i> (từ đó có nghĩa khác hẳn: thịt thăn). Dạng nam thì lại không chèn: <b>коре́ец</b>.</div>'
    '<div class="hd-sec">Họ hàng — Triều Tiên</div>'
    '<div class="hd-fam"><b>Коре́я</b> Triều Tiên · <b>коре́ец</b> người Triều Tiên (nam) · <b>корея́нка</b> (nữ) · <b>коре́йский</b> thuộc Triều Tiên · <b>по-коре́йски</b> bằng tiếng Triều Tiên</div>'
    + HE
)

S["немец"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">нем-</span><span class="hd-gloss">CÂM, không nói được — chính là gốc của <b>немо́й</b> (câm)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ец</span><span class="hd-gloss">hậu tố NGƯỜI NAM</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ có gốc đẹp nhất trong cả họ: người Slav xưa gọi người Đức là <b>"kẻ câm"</b> — kẻ không nói được thứ tiếng ta hiểu. <b>немо́й</b> (câm) và <b>не́мец</b> (người Đức) là cùng một gốc.</div>'
    '<div class="hd-warn"><b>Bẫy lớn nhất:</b> tên nước là <b>Герма́ния</b> (Germany) nhưng người thì <b>KHÔNG</b> phải <i>*германец</i> — mà là <b>не́мец</b>, tính từ <b>неме́цкий</b>. Đây là chỗ tên nước và tên dân tộc <b>không cùng gốc</b>, khác mọi từ còn lại trong lô.</div>'
    '<div class="hd-sec">Họ hàng — gốc нем- (câm)</div>'
    '<div class="hd-fam"><b>немо́й</b> câm · <b>не́мец</b> người Đức (nam) · <b>не́мка</b> (nữ) · <b>неме́цкий</b> thuộc Đức · <b>по-неме́цки</b> bằng tiếng Đức · <b>Герма́ния</b> nước Đức</div>'
    + HE
)

S["немка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">нем-</span><span class="hd-gloss">CÂM, không nói được — gốc của <b>немо́й</b> (câm)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span><span class="hd-gloss">hậu tố NGƯỜI NỮ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ NGẮN NHẤT của cả họ — thân từ chỉ có ba chữ. Người Slav xưa gọi người Đức là <b>"kẻ câm"</b>, kẻ không nói được tiếng ta hiểu; <b>немо́й</b> = câm.</div>'
    '<div class="hd-warn"><b>Bẫy:</b> nước là <b>Герма́ния</b> nhưng người là <b>не́мка / не́мец</b> — tên nước và tên dân tộc KHÔNG cùng gốc.</div>'
    '<div class="hd-sec">Họ hàng — gốc нем- (câm)</div>'
    '<div class="hd-fam"><b>немо́й</b> câm · <b>не́мец</b> người Đức (nam) · <b>не́мка</b> (nữ) · <b>неме́цкий</b> thuộc Đức · <b>по-неме́цки</b> bằng tiếng Đức · <b>Герма́ния</b> nước Đức</div>'
    + HE
)

S["француз"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">франц-</span><span class="hd-gloss">Фра́нция — nước Pháp</span></div>'
    '<div class="hd-row"><span class="hd-piece">-уз</span><span class="hd-gloss">đuôi RIÊNG, không phải hậu tố thường gặp</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ <b>phá luật</b> thứ hai của lô: người Pháp KHÔNG phải <i>*французец</i>. Đuôi <b>-уз</b> đi thẳng từ tiếng Pháp <i>français</i> vào tiếng Nga, không qua bộ hậu tố Nga.</div>'
    '<div class="hd-warn"><b>Bẫy:</b> dạng nữ cũng lệch theo — <b>францу́женка</b> chứ không phải <i>*французка</i>. Chữ <b>з</b> biến thành <b>ж</b>. Cả cặp nam–nữ này phải nhớ riêng.</div>'
    '<div class="hd-sec">Họ hàng — nước Pháp</div>'
    '<div class="hd-fam"><b>Фра́нция</b> nước Pháp · <b>францу́з</b> người Pháp (nam) · <b>францу́женка</b> (nữ) · <b>францу́зский</b> thuộc Pháp · <b>по-францу́зски</b> bằng tiếng Pháp</div>'
    + HE
)

S["француженка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">франц-</span><span class="hd-gloss">Фра́нция — nước Pháp</span></div>'
    '<div class="hd-row"><span class="hd-piece">-уж-</span><span class="hd-gloss">từ <b>-уз</b> của <b>францу́з</b>, chữ <b>з</b> mềm thành <b>ж</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-енка</span><span class="hd-gloss">hậu tố NGƯỜI NỮ (dạng mở rộng của -ка)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ <b>dài nhất và lệch nhất</b> trong họ quốc tịch — dựng từ dạng nam <b>францу́з</b> chứ không phải từ tên nước, và trên đường đi thì <b>з → ж</b>.</div>'
    '<div class="hd-why">Phép biến <b>з → ж</b> này không hề riêng lẻ, nó chạy khắp tiếng Nga: <b>во́зить</b> chở → <b>вожу́</b> tôi chở · <b>ре́зать</b> cắt → <b>ре́жу</b> tôi cắt. Nhận ra một lần là bớt ngạc nhiên về sau.</div>'
    '<div class="hd-warn"><b>Bẫy:</b> KHÔNG phải <i>*французка</i>, cũng KHÔNG phải <i>*францужка</i> — phải đủ <b>-ужен-ка</b>.</div>'
    '<div class="hd-sec">Họ hàng — nước Pháp</div>'
    '<div class="hd-fam"><b>Фра́нция</b> nước Pháp · <b>францу́з</b> người Pháp (nam) · <b>францу́женка</b> (nữ) · <b>францу́зский</b> thuộc Pháp · <b>по-францу́зски</b> bằng tiếng Pháp</div>'
    + HE
)

S["чех"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ <b>gốc trơn</b>, không chẻ được — một âm tiết, không hậu tố. Tên dân tộc tự thân, và tên nước <b>Че́хия</b> mới là cái dựng NGƯỢC ra từ nó.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ngắn nhất lô, nhưng để ý chiều suy: bình thường <i>nước → người</i> (Испания → испанец), riêng ở đây là <i>người → nước</i> (чех → Че́хия). Cùng kiểu với <b>ара́б</b>.</div>'
    '<div class="hd-warn"><b>Bẫy dạng nữ:</b> <b>че́шка</b> — chữ <b>х</b> biến thành <b>ш</b>. Cùng phép biến với <b>ти́хий</b> lặng → <b>ти́ше</b> lặng hơn.</div>'
    '<div class="hd-sec">Họ hàng — Séc</div>'
    '<div class="hd-fam"><b>Че́хия</b> nước Séc · <b>чех</b> người Séc (nam) · <b>че́шка</b> (nữ) · <b>че́шский</b> thuộc Séc · <b>по-че́шски</b> bằng tiếng Séc</div>'
    + HE
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
        # Khớp theo WordClean. Bẫy đã dính: dấu trọng âm U+0301 và zero-width
        # U+200B nằm lẫn trong field -> phải tìm bằng dạng sạch.
        ids = ac("findNotes", query=f'note:RU_Word WordClean:{word}')
        if len(ids) != 1:
            miss.append((word, len(ids)))
            continue
        if apply:
            ac("updateNoteFields", note={"id": ids[0], "fields": {"HuongDan": html}})
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
