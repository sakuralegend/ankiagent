# -*- coding: utf-8 -*-
"""k30 — numbers: SỐ THỨ TỰ. Số đếm + đuôi tính từ ⇒ một tính từ chia theo giống/cách.

Trục của lô: mỗi thẻ chỉ nói về CHÍNH từ đó — gốc lấy từ số đếm nào, chỗ nào
lệch (седьмо́й, восьмо́й, сороково́й, тре́тий), và họ hàng thật sự cùng gốc.
Không dựng khối hệ thống dùng chung (README §3).
"""

S = {}

S["первый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">перв-</span>'
    '<span class="hd-gloss">ĐẦU, TRƯỚC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Số thứ tự tiếng Nga là <b>tính từ</b>: chia theo giống và cách, '
    'hợp với danh từ đứng sau — <b>пе́рвый эта́ж</b> tầng 1, <b>пе́рвое ме́сто</b> hạng nhất. '
    'Gốc <b>перв-</b> không sinh ra từ <b>оди́н</b>, y hệt tiếng Anh <i>one → first</i>; '
    'và đúng là cùng gốc Ấn–Âu với <i>first</i> (nghĩa gốc: "ở phía trước nhất").</div>'
    '<div class="hd-warn">⚠️ <b>пе́рвая по́мощь</b> = <b>sơ cứu</b> — cụm cố định, '
    'không dịch thành "sự giúp đỡ đầu tiên".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>впервы́е</b> lần đầu tiên · <b>пе́рвенство</b> chức vô địch · '
    '<b>первонача́льный</b> ban đầu</div>'
)

S["второй"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">втор-</span>'
    '<span class="hd-gloss">THỨ HAI, LẶP LẠI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ, luôn mang trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cũng không sinh ra từ <b>два</b> (giống <i>two → second</i>). '
    'Nhận ra gốc <b>втор-</b> ở hai từ dùng hằng ngày: <b>вто́рник</b> "ngày thứ hai" '
    '— tức thứ Ba, vì tuần Nga bắt đầu từ thứ Hai — và <b>повторя́ть</b> "làm lần thứ hai" '
    'tức lặp lại. Đuôi <b>-о́й</b> giữ trọng âm ở mọi dạng: <b>втора́я</b>, <b>вторы́е</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вто́рник</b> thứ Ba · <b>повторя́ть</b> lặp lại · '
    '<b>втори́чный</b> thứ cấp, lần hai</div>'
)

S["третий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">трет-</span>'
    '<span class="hd-gloss">từ <b>три</b> BA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span>'
    '<span class="hd-gloss">đuôi mềm (không phải -ый)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trong toàn bộ số thứ tự tiếng Nga, chỉ mình từ này không chia như '
    'tính từ thường. Nó chia theo kiểu của <b>чей</b> "của ai": trừ đúng dạng gốc '
    '<b>тре́тий</b>, mọi dạng còn lại đều chèn thêm dấu mềm <b>ь</b>.</div>'
    '<div class="hd-warn">⚠️ Học thuộc bốn dạng gốc: <b>тре́тий</b> · <b>тре́тья</b> · '
    '<b>тре́тье</b> · <b>тре́тьи</b>; cách 2 giống đực là <b>тре́тьего</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>треть</b> một phần ba · <b>треуго́льник</b> hình tam giác · '
    '<b>тро́йка</b> bộ ba, điểm 3</div>'
)

S["четвёртый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">четвёрт-</span>'
    '<span class="hd-gloss">BỐN (gốc đầy đủ четвер-)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc đầy đủ là <b>четвер-</b>, thấy nguyên vẹn ở <b>четве́рг</b> '
    '"ngày thứ tư" — tức thứ Năm — và <b>че́тверть</b> một phần tư. Số đếm <b>четы́ре</b> '
    'lại không có chữ <b>в</b>, nên đừng suy số thứ tự thẳng từ nó. Chữ <b>ё</b> luôn '
    'mang trọng âm, khỏi phải nhớ thêm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>четве́рг</b> thứ Năm · <b>че́тверть</b> một phần tư · '
    '<b>четвёрка</b> số 4, điểm 4</div>'
)

S["пятый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пят-</span>'
    '<span class="hd-gloss">từ <b>пять</b> NĂM</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là khuôn chung của dãy 5–20: <b>bỏ dấu mềm ь của số đếm rồi '
    'thêm đuôi</b> — <b>пять</b> → <b>пя́тый</b>, <b>де́вять</b> → <b>девя́тый</b>; cả dãy '
    'chỉ có <b>седьмо́й</b> và <b>восьмо́й</b> lệch khuôn. Riêng chỗ đặt trọng âm thì phải '
    'nhớ từng từ: <b>пя́тый</b> nhấn đầu, còn '
    '<b>шесто́й</b> <b>седьмо́й</b> <b>восьмо́й</b> nhấn đuôi. Cùng gốc: <b>пя́тница</b> '
    '"ngày thứ năm" — tức thứ Sáu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пя́тница</b> thứ Sáu · <b>пятёрка</b> số 5, điểm 5 (điểm cao '
    'nhất ở Nga) · <b>пятьдеся́т</b> năm mươi</div>'
)

S["шестой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">шест-</span>'
    '<span class="hd-gloss">từ <b>шесть</b> SÁU</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ có trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bỏ <b>ь</b> rồi thêm <b>-о́й</b>, và trọng âm rơi hẳn xuống đuôi ở '
    'mọi dạng: <b>шеста́я</b>, <b>шесто́е</b>, <b>шесты́е</b>. Cùng nhóm nhấn-đuôi với '
    '<b>второ́й</b>, <b>седьмо́й</b>, <b>восьмо́й</b>, <b>сороково́й</b> — cả nhóm này đi '
    'chung một kiểu, học một lần là xong.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>шестёрка</b> số 6 · <b>шестна́дцать</b> mười sáu · '
    '<b>шестьдеся́т</b> sáu mươi</div>'
)

S["седьмой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">седьм-</span>'
    '<span class="hd-gloss">BẢY (gốc cổ còn giữ chữ д)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ có trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Số đếm <b>семь</b> đã đánh rơi chữ <b>д</b> của gốc cổ, nhưng số '
    'thứ tự thì giữ lại — nên không suy thẳng từ mặt chữ <b>семь</b> ra được. Cả hai cùng '
    'gốc Ấn–Âu với <i>seven</i>.</div>'
    '<div class="hd-warn">⚠️ Nhớ nguyên cặp như một khối: <b>семь</b> → <b>седьмо́й</b>. '
    'Trong dãy 5–10, đây là chỗ duy nhất không luật nào suy ra hộ được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>семёрка</b> số 7 · <b>семна́дцать</b> mười bảy · '
    '<b>се́мьдесят</b> bảy mươi</div>'
)

S["восьмой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">восьм-</span>'
    '<span class="hd-gloss">từ <b>во́семь</b> TÁM</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ có trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là <b>nguyên âm chạy</b>: chữ <b>е</b> trong <b>во́семь</b> '
    'biến mất ngay khi có đuôi theo sau, để lại gốc <b>восьм-</b> — cùng luật với '
    '<b>лёд</b> → <b>льда</b>. Trọng âm cũng dời hẳn từ đầu từ xuống đuôi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>восьмёрка</b> số 8 · <b>восемна́дцать</b> mười tám · '
    '<b>во́семьдесят</b> tám mươi</div>'
)

S["девятый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">девят-</span>'
    '<span class="hd-gloss">từ <b>де́вять</b> CHÍN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bỏ <b>ь</b>, thêm <b>-ый</b>, và trọng âm dịch một bước sang phải: '
    '<b>де́вять</b> → <b>девя́тый</b> — đúng như cặp <b>де́сять</b> → <b>деся́тый</b> ngay '
    'sau đây. Hai từ này nên học liền nhau vì lệch nhau đúng một chữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>девя́тка</b> số 9 · <b>девятна́дцать</b> mười chín · '
    '<b>девяно́сто</b> chín mươi</div>'
)

S["десятый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">десят-</span>'
    '<span class="hd-gloss">từ <b>де́сять</b> MƯỜI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trọng âm cũng dịch sang phải: <b>де́сять</b> → <b>деся́тый</b>. '
    'Gốc <b>десят-</b> là viên gạch của cả hệ đếm Nga: nó nấp trong đuôi <b>-надцать</b> '
    'của 11–19 (nguyên là "на де́сять" — trên mười) và trong đuôi <b>-десят</b> của '
    '50–80.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>деся́ток</b> một chục · <b>деся́тка</b> số 10 · '
    '<b>пятьдеся́т</b> năm mươi</div>'
)

S["одиннадцатый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">оди́н-</span>'
    '<span class="hd-gloss">MỘT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-на-</span>'
    '<span class="hd-gloss">TRÊN (chính là giới từ на)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дцат-</span>'
    '<span class="hd-gloss">MƯỜI (де́сять rút gọn)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đọc ngược lại là ra nghĩa đen: "một trên mười". Hai chữ <b>н</b> '
    'liền nhau chính là chữ cuối của <b>оди́н</b> gặp chữ đầu của <b>на</b> — biết vậy thì '
    'không bao giờ viết thiếu một <b>н</b>. Cả dãy 11–19 làm số thứ tự y như nhau: bỏ '
    '<b>ь</b> cuối số đếm, thêm <b>-ый</b>, trọng âm không nhúc nhích.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оди́н</b> một · <b>оди́ннадцать</b> mười một · '
    '<b>двена́дцатый</b> thứ mười hai</div>'
)

S["двадцатый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">два-</span>'
    '<span class="hd-gloss">HAI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дцат-</span>'
    '<span class="hd-gloss">MƯỜI ⇒ "hai mươi"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng viên gạch <b>-дцат-</b> như <b>оди́ннадцатый</b>, chỉ khác là '
    'ở đây <b>два</b> nhân với mười chứ không cộng. Trọng âm nhảy chỗ: số đếm '
    '<b>два́дцать</b> nhấn đầu, số thứ tự <b>двадца́тый</b> nhấn giữa.</div>'
    '<div class="hd-warn">⚠️ Số ghép chỉ có <b>TỪ CUỐI</b> mang dạng thứ tự: 21 là '
    '<b>два́дцать пе́рвый</b>, 25 là <b>два́дцать пя́тый</b> — không phải двадца́тый '
    'пе́рвый.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>два́дцать</b> hai mươi · <b>дво́йка</b> số 2, điểm 2 · '
    '<b>тридца́тый</b> thứ ba mươi</div>'
)

S["сороковой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сорок-</span>'
    '<span class="hd-gloss">từ <b>со́рок</b> BỐN MƯƠI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ов-</span>'
    '<span class="hd-gloss">chèn thêm để nối, không mang nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ có trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>со́рок</b> là từ lạc loài của hệ đếm: 30 là <b>три́дцать</b>, '
    '50 là <b>пятьдеся́т</b>, riêng 40 không dùng khuôn nào cả mà là một từ riêng hẳn. '
    'Số thứ tự của nó cũng riêng nốt — phải chèn <b>-ов-</b> rồi mới thêm đuôi, và trọng '
    'âm chạy tuốt xuống cuối.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>со́рок</b> bốn mươi · <b>сороконо́жка</b> con rết '
    '("bốn mươi chân")</div>'
)

S["пятидесятый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пяти-</span>'
    '<span class="hd-gloss">NĂM, dạng nối (đuôi -и)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-десят-</span>'
    '<span class="hd-gloss">CHỤC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Số đếm <b>пятьдеся́т</b> vốn là hai từ dán lại. Muốn thành số thứ '
    'tự thì phần đầu phải đổi sang dạng nối <b>пяти-</b> (bỏ <b>ь</b>, thêm <b>и</b>) và '
    'viết liền một chữ. Ba từ còn lại của nhóm 50–80 làm y hệt: <b>шестидеся́тый</b>, '
    '<b>семидеся́тый</b>, <b>восьмидеся́тый</b>.</div>'
    '<div class="hd-warn">⚠️ Số đếm 50–80 mỗi từ nhấn một chỗ (<b>пятьдеся́т</b> nhấn cuối '
    'nhưng <b>се́мьдесят</b> nhấn đầu); số thứ tự thì cả bốn đều nhấn <b>-деся́-</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пять</b> năm · <b>пятьдеся́т</b> năm mươi · <b>пя́тый</b> '
    'thứ năm</div>'
)

S["шестидесятый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">шести-</span>'
    '<span class="hd-gloss">SÁU, dạng nối</span></div>'
    '<div class="hd-row"><span class="hd-piece">-десят-</span>'
    '<span class="hd-gloss">CHỤC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng khuôn của <b>пятидеся́тый</b>: <b>шесть</b> bỏ <b>ь</b> thành '
    'dạng nối <b>шести-</b>, dán liền vào <b>-деся́тый</b>. Chú ý cả từ chỉ có <b>một</b> '
    'trọng âm ở <b>-ся́-</b>, phần <b>шести-</b> đọc lướt hết.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>шесть</b> sáu · <b>шестьдеся́т</b> sáu mươi · <b>шесто́й</b> '
    'thứ sáu</div>'
)

S["семидесятый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">семи-</span>'
    '<span class="hd-gloss">BẢY, dạng nối</span></div>'
    '<div class="hd-row"><span class="hd-piece">-десят-</span>'
    '<span class="hd-gloss">CHỤC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Phần đầu lấy từ số đếm <b>семь</b> chứ không lấy từ số thứ tự '
    '<b>седьмо́й</b> — nên là <b>семи-</b>, không có chữ <b>д</b> nào ở đây cả. Trọng âm '
    'cũng nhảy hẳn: số đếm <b>се́мьдесят</b> nhấn đầu, số thứ tự <b>семидеся́тый</b> nhấn '
    'gần cuối.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>семь</b> bảy · <b>се́мьдесят</b> bảy mươi · <b>седьмо́й</b> '
    'thứ bảy</div>'
)

S["восьмидесятый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">восьми-</span>'
    '<span class="hd-gloss">TÁM, dạng nối</span></div>'
    '<div class="hd-row"><span class="hd-piece">-десят-</span>'
    '<span class="hd-gloss">CHỤC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vẫn là nguyên âm chạy đã gặp ở <b>восьмо́й</b>: <b>во́семь</b> rụng '
    'chữ <b>е</b> khi có đuôi, còn <b>восьми-</b>. Và lại một lần nữa trọng âm rời đầu từ '
    'chạy về <b>-ся́-</b>: <b>во́семьдесят</b> nhưng <b>восьмидеся́тый</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>во́семь</b> tám · <b>во́семьдесят</b> tám mươi · '
    '<b>восьмо́й</b> thứ tám</div>'
)

S["девяностый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">девяност-</span>'
    '<span class="hd-gloss">từ <b>девяно́сто</b> CHÍN MƯƠI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">90 là từ lạc loài thứ hai của hệ đếm, bên cạnh <b>со́рок</b>: nó '
    'không theo khuôn <b>-десят</b> nên không có dạng nào kiểu "девятьдесят". Bù lại số thứ '
    'tự của nó dễ nhất nhóm — chỉ thay <b>-о</b> cuối bằng <b>-ый</b>, trọng âm ngồi yên '
    'tại chỗ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>де́вять</b> chín · <b>девяно́сто</b> chín mươi · '
    '<b>девя́тый</b> thứ chín</div>'
)

S["сотый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сот-</span>'
    '<span class="hd-gloss">TRĂM (gốc của <b>сто</b> khi có đuôi)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trong các từ phái sinh, <b>сто</b> luôn đổi sang gốc <b>сот-</b>: '
    '<b>со́тый</b>, <b>со́тня</b>. Trọng âm luôn ở đầu, không đi đâu cả. Dạng giống cái '
    '<b>со́тая</b> còn là cách nói "một phần trăm".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сто</b> một trăm · <b>со́тня</b> nhóm một trăm · '
    '<b>со́тка</b> 100 m² (đơn vị đo đất)</div>'
)

S["тысячный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ты́сяч-</span>'
    '<span class="hd-gloss">từ <b>ты́сяча</b> NGHÌN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span>'
    '<span class="hd-gloss">hậu tố biến danh từ thành tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Khác hẳn 19 từ trước: <b>ты́сяча</b> chia y như một danh từ giống '
    'cái, không như các số đếm khác, nên phải mượn hậu tố <b>-н-</b> — lối chung để biến '
    'danh từ thành tính từ — rồi mới thêm đuôi. Vì thế nó còn nghĩa thứ hai "hàng nghìn, '
    'đông tới nghìn người".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ты́сяча</b> nghìn · <b>тысячеле́тие</b> thiên niên kỷ · '
    '<b>двухты́сячный</b> thứ 2000</div>'
)

S["двухтысячный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">двух-</span>'
    '<span class="hd-gloss">HAI, dạng nối (chính là cách 2 của два)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ты́сячн-</span>'
    '<span class="hd-gloss">NGHÌN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ghép thẳng "hai" vào "thứ một nghìn". Chỗ gặp nó nhiều nhất là '
    'năm 2000: <b>в двухты́сячном году́</b>. Trọng âm không nhúc nhích khỏi <b>ты́сяча</b> '
    'dù từ đã dài ra.</div>'
    '<div class="hd-warn">⚠️ Dạng ngắn (hiếm dùng) chèn thêm <b>е</b> ở giống đực cho đỡ '
    'nghẹn phụ âm: <b>двухты́сячен</b>, còn lại đều đặn — <b>двухты́сячна</b>, '
    '<b>двухты́сячно</b>, <b>двухты́сячны</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>два</b> hai · <b>ты́сячный</b> thứ một nghìn · '
    '<b>двухле́тний</b> hai năm, kéo dài hai năm</div>'
)

# ---------------------------------------------------------------------------
# Việc thứ hai (README §2c): field `Vietnamese` là ĐỀ BÀI của deck 1-go.
# Va chạm thật, đã đối chiếu tudien.json: nghĩa Việt của bảy số thứ tự đầu
# TRÙNG ĐÚNG TỪNG CHỮ với tên các ngày trong tuần đang có trong bộ sưu tập —
# понеде́льник "thứ Hai" · вто́рник "thứ ba" · среда́ "thứ Tư" · четве́рг
# "thứ Năm" · пя́тница "thứ Sáu" · суббо́та "thứ Bảy". Badge {{PoS}} không cứu
# được (num vs n thì đúng, nhưng người gõ nhìn đề bài trước, nhìn badge sau),
# nên phải chặn ngay ở dòng tiếng Việt.
V = {
    'первый': 'thứ nhất, đầu tiên',
    'второй': 'thứ hai, thứ nhì',
    'третий': 'thứ ba, thứ 3',
    'четвёртый': 'thứ tư, thứ 4',
    'пятый': 'thứ năm, thứ 5',
    'шестой': 'thứ sáu, thứ 6',
    'седьмой': 'thứ bảy, thứ 7',
    'сотый': 'thứ 100',
    'тысячный': 'thứ một nghìn, hàng nghìn',
    'двухтысячный': 'thứ hai nghìn, thuộc năm 2000',
}
