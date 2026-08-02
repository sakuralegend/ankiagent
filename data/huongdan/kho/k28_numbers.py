# -*- coding: utf-8 -*-
"""k28 — numbers: số đếm 0–20, trục là LUẬT SỐ KÉO DANH TỪ THEO CÁCH NÀO.

Phân bổ luật (đừng chép lại ở mọi thẻ):
  · оди́н hợp giống + danh từ số ít    -> thẻ оди́н
  · 2·3·4 + cách 2 SỐ ÍT              -> thẻ два
  · 5–20 + cách 2 SỐ NHIỀU, biến cách như danh từ giống cái -ь -> thẻ пять
  · -на́дцать = "trên mười"            -> thẻ оди́ннадцать (thẻ teen đầu tiên)
  · ghép nhân (2 x 10)                -> thẻ два́дцать
"""

S = {}

S["ноль"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: từ mượn nguyên khối của châu Âu, gốc Latin '
    '<i>nullus</i> "không có gì". Đây là số duy nhất trong lô không phải gốc Nga cổ.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng nguồn với tiếng Anh <i>null · nil · annul</i> — nhìn chữ là nhận ra. '
    'Tồn tại song song hai dạng <b>ноль</b> và <b>нуль</b>, nghĩa y hệt; khi đọc số và trong đời '
    'thường dùng <b>ноль</b>.</div>'
    '<div class="hd-warn">⚠️ Biến cách thì trọng âm nhảy ra đuôi: <b>ноль</b> → cách 2 <b>ноля́</b>, '
    'cách 5 <b>нолём</b>. Đây là danh từ giống đực chứ không phải số từ, nên nó biến như <i>дом</i>, '
    'không biến như <b>пять</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нулево́й</b> bằng không, số không (нулево́й результа́т) · '
    '<b>обнули́ть</b> đưa về 0, xoá sạch</div>'
)

S["один"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">од-</span>'
    '<span class="hd-gloss">MỘT, DUY NHẤT — cùng gốc với <b>еди́ный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́н</span>'
    '<span class="hd-gloss">đuôi khiến từ này biến như TÍNH TỪ, không như số</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vì mang đuôi tính từ nên nó phải <b>hợp giống</b> với danh từ: '
    '<b>оди́н</b> дом · <b>одна́</b> кни́га · <b>одно́</b> окно́ · <b>одни́</b> (số nhiều).</div>'
    '<div class="hd-warn">⚠️ Đây là số DUY NHẤT không kéo danh từ sang cách 2: sau <b>оди́н</b>, '
    'danh từ đứng ở <b>số ít, nguyên cách</b> — <i>оди́н дом</i>, <i>одна́ кни́га</i>. Luật này còn '
    'áp cho mọi số tận cùng bằng 1: <i>два́дцать оди́н дом</i> = 21 cái nhà, mà <i>дом</i> vẫn ở '
    'số ít.</div>'
    '<div class="hd-warn">⚠️ Cụm phải thuộc: <b>ни одного́</b> / <b>ни одно́й</b> = "không một ai, '
    'không một cái nào" — luôn đi với phủ định <i>не</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>одина́ковый</b> giống hệt nhau · <b>одино́кий</b> cô đơn · '
    '<b>одна́жды</b> một lần nọ · <b>еди́ный</b> duy nhất, thống nhất · <b>оди́ннадцать</b> 11</div>'
)

S["два"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">два</span>'
    '<span class="hd-gloss">dùng với giống ĐỰC và giống TRUNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">две</span>'
    '<span class="hd-gloss">dùng với giống CÁI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Ấn–Âu với <i>two · duo · dual</i>. Chỉ số 2 mới tách theo giống; '
    '<b>три</b> và <b>четы́ре</b> thì một dạng dùng cho tất cả.</div>'
    '<div class="hd-warn">⚠️ <b>два</b> до́ма nhưng <b>две</b> кни́ги. Chọn sai dạng là sai giống, '
    'không phải sai số.</div>'
    '<div class="hd-warn">⚠️ LUẬT ĐẮT NHẤT: sau <b>2 · 3 · 4</b> (và mọi số tận cùng bằng 2, 3, 4) '
    'danh từ đứng ở <b>cách 2 SỐ ÍT</b>: <i>два до́ма · три го́да · четы́ре кни́ги</i>. Từ 5 trở lên '
    'đổi luật — xem thẻ <b>пять</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>второ́й</b> thứ hai · <b>дво́е</b> hai người · <b>вдвоём</b> hai người '
    'cùng nhau · <b>двена́дцать</b> 12 · <b>два́дцать</b> 20</div>'
)

S["три"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được — một trong những từ cổ nhất của tiếng Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Ấn–Âu với <i>three · tri- · trio</i>, nhận ra ngay qua chữ. '
    'Khác <b>два</b>, số 3 <b>không tách theo giống</b>: <i>три до́ма</i> và <i>три кни́ги</i> đều '
    'dùng <b>три</b>. Luật kéo danh từ thì y hệt <b>два</b> (cách 2 số ít — xem thẻ đó).</div>'
    '<div class="hd-warn">⚠️ Biến cách thì gốc đổi <i>и → ё</i>: cách 2 <b>трёх</b>, cách 3 '
    '<b>трём</b>, cách 5 <b>тремя́</b>. Nhớ <i>о трёх часа́х</i> (về ba giờ).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тре́тий</b> thứ ba · <b>тро́е</b> ba người · <b>втроём</b> ba người '
    'cùng nhau · <b>трина́дцать</b> 13 · <b>три́дцать</b> 30</div>'
)

S["четыре"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn. Nhưng nhớ kỹ hình dạng <b>четы́ре</b>: nó rụng mất chữ '
    '<i>е</i> khi vào số 14 (<b>четы́рнадцать</b>, không phải четырена́дцать).</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Ấn–Âu với <i>four · quattro · quadr-</i>. '
    'Đây là số <b>cuối cùng</b> còn theo luật "cách 2 số ít" của <b>два</b>: <i>четы́ре кни́ги</i>. '
    'Bước sang <b>пять</b> là đổi luật hoàn toàn.</div>'
    '<div class="hd-warn">⚠️ Biến cách đổi gốc <i>ы → ё</i> như <b>три</b>: <b>четырёх</b>, '
    '<b>четырём</b> — riêng cách 5 là <b>четырьмя́</b> (có dấu mềm, không phải четырёмя).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>четвёртый</b> thứ tư · <b>че́тверть</b> một phần tư, quý · '
    '<b>че́тверо</b> bốn người · <b>четы́рнадцать</b> 14</div>'
)

S["пять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, kết thúc bằng dấu mềm <i>ь</i> — và chính cái đuôi mềm đó '
    'quyết định cách nó biến (xem ô đỏ thứ hai).</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Ấn–Âu với <i>five · penta- · quinque</i>. Từ <b>пять</b> trở đi, '
    'các số 5–20 hành xử giống hệt nhau, nên học kỹ một mình từ này là xong cả nhóm.</div>'
    '<div class="hd-warn">⚠️ LUẬT ĐỔI TẠI ĐÂY: sau <b>5–20</b> danh từ đứng ở <b>cách 2 SỐ NHIỀU</b> '
    '— <i>пять домо́в · пять книг · пять лет · пять часо́в</i>. So với <i>четы́ре кни́ги</i> (số ít) '
    'ở thẻ <b>два</b>.</div>'
    '<div class="hd-warn">⚠️ Cả nhóm 5–20 biến cách y như danh từ giống cái đuôi <i>-ь</i>: '
    '<b>пять → пяти́</b> (cách 2·3·6) và <b>пятью́</b> (cách 5). Riêng ở 5–10 và 20 trọng âm nhảy '
    'ra đuôi; nhóm 11–19 thì đứng yên.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пя́тый</b> thứ năm · <b>пя́тница</b> thứ Sáu (= ngày thứ NĂM của tuần '
    'Nga, tuần bắt đầu từ thứ Hai) · <b>пятна́дцать</b> 15 · <b>пятьдеся́т</b> 50</div>'
)

S["шесть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, đuôi mềm <i>-ь</i> như <b>пять</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Ấn–Âu với <i>six · sex- (sextet)</i>: chữ <i>ш</i> Nga ứng với '
    '<i>s</i> Anh. Biến cách và luật kéo danh từ giống hệt <b>пять</b>: <b>шести́</b> · '
    '<b>шестью́</b>, và <i>шесть книг</i> (cách 2 số nhiều).</div>'
    '<div class="hd-warn">⚠️ Nghe và viết lệch nhau: người Nga đọc lướt cụm <i>стн</i> nên số 16 '
    'nghe như "шеснадцать", nhưng vẫn phải viết <b>шестна́дцать</b> vì gốc là <b>шесть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>шесто́й</b> thứ sáu · <b>шестна́дцать</b> 16 · '
    '<b>шестьдеся́т</b> 60</div>'
)

S["семь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, đuôi mềm <i>-ь</i> như <b>пять</b>: <b>семи́</b> · '
    '<b>семью́</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Ấn–Âu với <i>seven · septem · September</i> (tháng thứ bảy của '
    'lịch La Mã cũ).</div>'
    '<div class="hd-warn">⚠️ Ba từ trông rất giống nhưng khác hẳn nhau: <b>семь</b> bảy · '
    '<b>семья́</b> gia đình · <b>се́мя</b> hạt giống. Chỉ <b>семь</b> là số.</div>'
    '<div class="hd-warn">⚠️ Số thứ tự đổi phụ âm: <b>семь</b> → <b>седьмо́й</b> (thứ bảy) — '
    '<i>м</i> thành <i>дь</i>. Không suy ra được, phải thuộc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>седьмо́й</b> thứ bảy · <b>семна́дцать</b> 17 · '
    '<b>се́мьдесят</b> 70</div>'
)

S["восемь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn. Nhưng gốc thật của nó là <i>восьм-</i>; chữ <i>е</i> trong '
    '<b>во́семь</b> chỉ là nguyên âm chèn vào cho dễ đọc khi từ đứng trần.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Ấn–Âu với <i>eight · octo- · October</i>. Biến cách và luật kéo '
    'danh từ vẫn theo khuôn <b>пять</b>.</div>'
    '<div class="hd-warn">⚠️ NGUYÊN ÂM CHẠY: chữ <i>е</i> rơi mất khi biến cách — <b>во́семь</b> → '
    '<b>восьми́</b> (cách 2·3·6) · <b>восьмью́</b> (cách 5), trọng âm nhảy theo ra đuôi. Trong lô '
    'này chỉ <b>во́семь</b> làm vậy giữa các số 5–20.</div>'
    '<div class="hd-warn">⚠️ Nhưng số 18 thì GIỮ chữ <i>е</i>: <b>восемна́дцать</b>, không phải '
    'восьмна́дцать. Đừng mang dạng rụng <i>восьм-</i> sang đó.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>восьмо́й</b> thứ tám · <b>восемна́дцать</b> 18 · '
    '<b>во́семьдесят</b> 80</div>'
)

S["девять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, đuôi mềm <i>-ь</i> như <b>пять</b>: <b>девяти́</b> · '
    '<b>девятью́</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Ấn–Âu với <i>nine · novem · November</i>.</div>'
    '<div class="hd-warn">⚠️ Cặp dễ lẫn nhất của cả lô: <b>де́вять</b> 9 và <b>де́сять</b> 10 chỉ '
    'khác đúng MỘT chữ — <i>в</i> so với <i>с</i>. Đọc lại chữ thứ ba trước khi gõ.</div>'
    '<div class="hd-warn">⚠️ Số 90 KHÔNG theo khuôn: là <b>девяно́сто</b>, không phải '
    'девятьдесят (trong khi 50–80 đều ghép đều đặn: <b>пятьдеся́т</b>, <b>во́семьдесят</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>девя́тый</b> thứ chín · <b>девятна́дцать</b> 19 · '
    '<b>девяно́сто</b> 90</div>'
)

S["десять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, đuôi mềm <i>-ь</i>: <b>десяти́</b> · <b>десятью́</b>. '
    'Nhưng đây là từ <b>đẻ ra cả nửa lô</b> — xem Cách nhớ.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Ấn–Âu với <i>ten · decem · deca-</i>. Quan trọng hơn: đuôi '
    '<i>-дцать</i> trong <b>оди́ннадцать</b> … <b>два́дцать</b> chính là <b>де́сять</b> bị đọc mòn '
    'đi. Thấy <i>-дцать</i> ở đâu là biết đang có chữ "mười" ở đó.</div>'
    '<div class="hd-warn">⚠️ <b>де́сять</b> 10 với <b>де́вять</b> 9 chỉ khác một chữ <i>с/в</i>. '
    'Và đừng lẫn <b>де́сять</b> (số 10) với <b>деся́ток</b> (một chục hàng) — trọng âm cũng dời.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>деся́тый</b> thứ mười · <b>деся́ток</b> một chục · '
    '<b>пятьдеся́т</b> 50 (năm chục) · <b>шестьдеся́т</b> 60</div>'
)

S["одиннадцать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">оди́н-</span>'
    '<span class="hd-gloss">MỘT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-на-</span>'
    '<span class="hd-gloss">TRÊN (giới từ <i>на</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дцать</span>'
    '<span class="hd-gloss">MƯỜI (<b>де́сять</b> đọc mòn)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: "một trên mười". Cả nhóm 11–19 dựng theo đúng khuôn này, nên '
    'chỉ cần đọc kỹ một lần ở đây. Biến cách theo khuôn <b>пять</b>: <b>оди́ннадцати</b> · '
    '<b>оди́ннадцатью</b>, trọng âm đứng yên.</div>'
    '<div class="hd-warn">⚠️ HAI chữ <i>н</i>: <b>оди́ннадцать</b> = оди́<u>н</u> + <u>н</u>а + дцать. '
    'Chữ <i>н</i> cuối của "một" gặp chữ <i>н</i> đầu của "trên" nên cả hai cùng được viết ra.</div>'
    '<div class="hd-warn">⚠️ Trọng âm nằm ở gốc <b>оди́н</b>, KHÔNG rơi vào <i>-надцать</i>. Trong '
    'cả nhóm 11–19 chỉ có số này và <b>четы́рнадцать</b> như vậy; 12, 13, 15–19 đều dồn trọng âm '
    'vào <i>-на́дцать</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оди́н</b> 1 · <b>оди́ннадцатый</b> thứ mười một</div>'
)

S["двенадцать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">две-</span>'
    '<span class="hd-gloss">HAI — dạng giống CÁI, không phải <b>два</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-на-</span>'
    '<span class="hd-gloss">TRÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дцать</span>'
    '<span class="hd-gloss">MƯỜI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">"Hai trên mười". Điểm đáng nhớ riêng của số này: nó đông cứng dạng '
    '<b>две</b> (giống cái) chứ không lấy <b>два</b> — viết дванадцать là sai.</div>'
    '<div class="hd-warn">⚠️ Trọng âm rơi vào <b>-на́-</b>: <b>двена́дцать</b>. Từ đây trở đi trọng '
    'âm nằm ở <i>-на́дцать</i> với mọi số, trừ <b>четы́рнадцать</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>два</b> 2 · <b>двена́дцатый</b> thứ mười hai · <b>два́дцать</b> 20</div>'
)

S["тринадцать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">три-</span>'
    '<span class="hd-gloss">BA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-на-</span>'
    '<span class="hd-gloss">TRÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дцать</span>'
    '<span class="hd-gloss">MƯỜI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">"Ba trên mười" — dễ nhất nhóm: <b>три</b> dán thẳng vào <i>-надцать</i>, '
    'không rụng chữ nào mà cũng không có dấu mềm để mất. Trọng âm ở <b>-на́-</b>: '
    '<b>трина́дцать</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>три</b> 3 · <b>тре́тий</b> thứ ba · <b>трина́дцатый</b> thứ mười ba · '
    '<b>три́дцать</b> 30</div>'
)

S["четырнадцать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">четы́р-</span>'
    '<span class="hd-gloss">BỐN — đã rụng chữ <i>е</i> của <b>четы́ре</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-на-</span>'
    '<span class="hd-gloss">TRÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дцать</span>'
    '<span class="hd-gloss">MƯỜI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">"Bốn trên mười" — gốc bị cắt ngắn nhất nhóm: <b>четы́ре</b> mất luôn chữ '
    '<i>е</i> cuối trước khi ghép.</div>'
    '<div class="hd-warn">⚠️ Hai bẫy cùng lúc: viết <b>четы́рнадцать</b> chứ không phải '
    'четыренадцать (rụng <i>е</i>), và trọng âm vẫn nằm ở gốc chứ không rơi vào <i>-надцать</i>. '
    'Cùng với <b>оди́ннадцать</b>, đây là hai ngoại lệ trọng âm của nhóm 11–19.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>четы́ре</b> 4 · <b>четвёртый</b> thứ tư · '
    '<b>четы́рнадцатый</b> thứ mười bốn</div>'
)

S["пятнадцать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пят-</span>'
    '<span class="hd-gloss">NĂM — <b>пять</b> đã bỏ dấu mềm <i>ь</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-на-</span>'
    '<span class="hd-gloss">TRÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дцать</span>'
    '<span class="hd-gloss">MƯỜI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">"Năm trên mười". Luật chính tả bắt đầu từ số này: gốc số nào tận cùng '
    'bằng <i>-ь</i> thì <b>mất dấu mềm</b> khi ghép — đúng cho cả nhóm 15–19 '
    '(<b>шестна́дцать</b>, <b>семна́дцать</b>, <b>восемна́дцать</b>, <b>девятна́дцать</b>). '
    'Trọng âm ở <b>-на́-</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пять</b> 5 · <b>пя́тый</b> thứ năm · <b>пятна́дцатый</b> thứ mười lăm · '
    '<b>пятьдеся́т</b> 50</div>'
)

S["шестнадцать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">шест-</span>'
    '<span class="hd-gloss">SÁU — <b>шесть</b> bỏ dấu mềm <i>ь</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-на-</span>'
    '<span class="hd-gloss">TRÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дцать</span>'
    '<span class="hd-gloss">MƯỜI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">"Sáu trên mười". Trọng âm ở <b>-на́-</b>: <b>шестна́дцать</b>.</div>'
    '<div class="hd-warn">⚠️ Số dễ viết thiếu chữ nhất của lô: cụm <i>стн</i> đọc lướt mất '
    'chữ <i>т</i> (nghe như "шеснадцать"), nhưng phải viết đủ <b>шестна́дцать</b> — cứ nhớ gốc là '
    '<b>шесть</b> thì không sót.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>шесть</b> 6 · <b>шесто́й</b> thứ sáu · '
    '<b>шестна́дцатый</b> thứ mười sáu · <b>шестьдеся́т</b> 60</div>'
)

S["семнадцать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сем-</span>'
    '<span class="hd-gloss">BẢY — <b>семь</b> bỏ dấu mềm <i>ь</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-на-</span>'
    '<span class="hd-gloss">TRÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дцать</span>'
    '<span class="hd-gloss">MƯỜI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">"Bảy trên mười". Trọng âm ở <b>-на́-</b>: <b>семна́дцать</b>. Khác với số '
    'thứ tự <b>седьмо́й</b> (đổi <i>м</i> thành <i>дь</i>), số 17 giữ nguyên gốc <i>сем-</i> nên '
    'không có gì phải nhớ thêm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>семь</b> 7 · <b>седьмо́й</b> thứ bảy · '
    '<b>семна́дцатый</b> thứ mười bảy · <b>се́мьдесят</b> 70</div>'
)

S["восемнадцать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">восем-</span>'
    '<span class="hd-gloss">TÁM — <b>во́семь</b> bỏ dấu mềm, GIỮ chữ <i>е</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-на-</span>'
    '<span class="hd-gloss">TRÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дцать</span>'
    '<span class="hd-gloss">MƯỜI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">"Tám trên mười" — ghép thẳng, gốc <b>во́семь</b> chỉ mất mỗi dấu mềm. '
    'Trọng âm ở <b>-на́-</b>: <b>восемна́дцать</b>.</div>'
    '<div class="hd-warn">⚠️ Đừng lấy dạng rụng nguyên âm của <b>во́семь</b> (cách 2 là '
    '<b>восьми́</b>) mang sang đây: viết восьмнадцать là sai, phải là <b>восемна́дцать</b> đủ '
    'chữ <i>е</i>. Đây là chỗ dễ sai nhất của số 18.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>во́семь</b> 8 · <b>восьмо́й</b> thứ tám · '
    '<b>восемна́дцатый</b> thứ mười tám · <b>во́семьдесят</b> 80</div>'
)

S["девятнадцать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">девят-</span>'
    '<span class="hd-gloss">CHÍN — <b>де́вять</b> bỏ dấu mềm <i>ь</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-на-</span>'
    '<span class="hd-gloss">TRÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дцать</span>'
    '<span class="hd-gloss">MƯỜI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">"Chín trên mười" — số cuối cùng của khuôn cộng; sang 20 là đổi sang khuôn '
    'nhân. Trọng âm ở <b>-на́-</b>: <b>девятна́дцать</b>.</div>'
    '<div class="hd-warn">⚠️ Ba từ đầu giống nhau, nghĩa cách xa nhau: <b>де́вять</b> 9 · '
    '<b>девятна́дцать</b> 19 · <b>девяно́сто</b> 90. Nghe câu số thì bám vào phần đuôi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>де́вять</b> 9 · <b>девя́тый</b> thứ chín · '
    '<b>девятна́дцатый</b> thứ mười chín · <b>девяно́сто</b> 90</div>'
)

S["двадцать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">два-</span>'
    '<span class="hd-gloss">HAI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дцать</span>'
    '<span class="hd-gloss">MƯỜI — và KHÔNG có <i>-на-</i> ở giữa</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mất chữ <i>-на-</i> là dấu hiệu đổi phép tính: 11–19 là phép CỘNG '
    '("hai trên mười" = 12), còn <b>два́дцать</b> là phép NHÂN — hai lần mười. <b>три́дцать</b> 30 '
    'cũng vậy. Vì gốc <b>два</b> không còn bị đẩy đi, trọng âm lùi về đầu: <b>два́дцать</b>.</div>'
    '<div class="hd-warn">⚠️ Đếm quá 20 thì luật kéo danh từ quay lại theo chữ số CUỐI: '
    '<i>два́дцать оди́н дом</i> (số ít, nguyên cách) · <i>два́дцать два до́ма</i> (cách 2 số ít) · '
    '<i>два́дцать пять домо́в</i> (cách 2 số nhiều).</div>'
    '<div class="hd-warn">⚠️ Khác nhóm 11–19 (trọng âm đứng yên: <b>двена́дцати</b>), số này dời '
    'trọng âm ra đuôi khi biến cách: <b>два́дцать</b> → cách 2 <b>двадцати́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>два</b> 2 · <b>два́дцатый</b> thứ hai mươi · <b>три́дцать</b> 30</div>'
)

# ── Field Vietnamese (README §2c) — đề bài của deck 1-go, chỉ được có MỘT đáp án đúng.
# Số đếm gần như tự phân biệt (viết đúng chữ số là xong), nên chỉ sửa 3 chỗ thật sự mơ hồ.
V = {
    # nguồn: "số không, không có gì, trắng tay" -> "trắng tay" gợi cả пусто́й/ничего́
    "ноль":  "số không (0)",
    # nguồn: "một, một mình" -> "một mình" gợi одино́кий/сам
    "один":  "một (1)",
    # nguồn: "hai" -> không cho biết chọn два hay две
    "два":   "hai (2) — dạng đi với danh từ giống đực và giống trung",
}
