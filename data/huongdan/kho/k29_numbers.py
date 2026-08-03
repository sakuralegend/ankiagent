# -*- coding: utf-8 -*-
"""k29 — numbers 30…1000: mỗi số là ĐƠN VỊ dính với "mười" (-дцать/-десят) hoặc
với "trăm" (-сти/-ста/-сот, ba dạng cũ của сто); ba từ phá khuôn là сорок,
девяносто, тысяча."""

S = {}

S["тридцать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">три-</span>'
    '<span class="hd-gloss">ba</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дцать</span>'
    '<span class="hd-gloss">dạng dính của <b>де́сять</b> (mười)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng nghĩa đen "ba mươi": ba × mười, cùng khuôn với '
    '<b>два́дцать</b> (hai × mười) đã học.</div>'
    '<div class="hd-why">Biến cách theo <b>пять</b>: <b>тридцати́</b> '
    '(cách 2·3·6), <b>тридцатью́</b> (cách 5).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>три</b> ba · <b>де́сять</b> mười · '
    '<b>два́дцать</b> hai mươi</div>'
)

S["сорок"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không chẻ được. 40 là chỗ đứt của cả dãy: 30 là '
    '<b>три</b>+дцать, 50 là <b>пять</b>+десят, riêng 40 có một từ riêng — '
    'phải thuộc, không suy ra được.</div>'
    '<div class="hd-warn">⚠️ Cả bảng chia chỉ có MỘT dạng gián tiếp: '
    '<b>сорока́</b> dùng cho cách 2·3·5·6. Nhớ một dạng là xong.</div>'
    '<div class="hd-warn">⚠️ <b>сорока́</b> (của 40, trọng âm cuối) khác hẳn '
    '<b>соро́ка</b> (chim ác là) — cùng mặt chữ, khác chỗ nhấn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сороково́й</b> thứ 40 · <b>сороконо́жка</b> '
    'con rết (bốn mươi chân)</div>'
)

S["пятьдесят"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пять-</span>'
    '<span class="hd-gloss">năm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-десят</span>'
    '<span class="hd-gloss">cách 2 số nhiều của <b>де́сять</b> (mười)</span>'
    '</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen "năm CỦA những chục" — dựng y hệt '
    '<b>пятьсо́т</b> (năm của những trăm).</div>'
    '<div class="hd-why">Biến cách đổi CẢ HAI nửa: <b>пяти́десяти</b> — trọng âm '
    'cũng chạy từ cuối về giữa.</div>'
    '<div class="hd-warn">⚠️ Dấu mềm <b>ь</b> nằm giữa từ và KHÔNG có ở cuối: '
    '<b>пятьдеся́т</b>. Đúng cho cả 50–80 lẫn 500–900.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пять</b> năm · <b>де́сять</b> mười · '
    '<b>пятидеся́тый</b> thứ 50</div>'
)

S["шестьдесят"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">шесть-</span>'
    '<span class="hd-gloss">sáu</span></div>'
    '<div class="hd-row"><span class="hd-piece">-десят</span>'
    '<span class="hd-gloss">chục (như trong <b>пятьдеся́т</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dựng y hệt <b>пятьдеся́т</b>: trọng âm ở đuôi khi đếm, '
    'dồn về giữa khi biến cách — <b>шести́десяти</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>шесть</b> sáu · <b>шесто́й</b> thứ 6 · '
    '<b>шестидеся́тый</b> thứ 60</div>'
)

S["семьдесят"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">семь-</span>'
    '<span class="hd-gloss">bảy</span></div>'
    '<div class="hd-row"><span class="hd-piece">-десят</span>'
    '<span class="hd-gloss">chục</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng khuôn 50 và 60, nhưng trọng âm rơi vào ĐẦU: '
    '<b>се́мьдесят</b>. Biến cách: <b>семи́десяти</b>.</div>'
    '<div class="hd-warn">⚠️ Bốn từ cùng khuôn mà trọng âm chia đôi: 50·60 nhấn '
    'cuối (<b>пятьдеся́т</b>, <b>шестьдеся́т</b>), 70·80 nhấn đầu '
    '(<b>се́мьдесят</b>, <b>во́семьдесят</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>семь</b> bảy · <b>седьмо́й</b> thứ 7 · '
    '<b>семидеся́тый</b> thứ 70</div>'
)

S["восемьдесят"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">восемь-</span>'
    '<span class="hd-gloss">tám</span></div>'
    '<div class="hd-row"><span class="hd-piece">-десят</span>'
    '<span class="hd-gloss">chục</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trọng âm ở đầu như <b>се́мьдесят</b>. Khi biến cách, '
    '<b>во́семь</b> rụng mất chữ <b>е</b>: <b>восьми́десяти</b> — đúng chỗ rụng '
    'đó cho ra <b>восьмо́й</b> và <b>восьмидеся́тый</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>во́семь</b> tám · <b>восьмо́й</b> thứ 8 · '
    '<b>восьмидеся́тый</b> thứ 80</div>'
)

S["девяносто"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không chẻ được: cùng <b>со́рок</b>, đây là số thứ hai '
    'phá khuôn — tiếng Nga không nói *девятьдесят.</div>'
    '<div class="hd-why">Cả từ chỉ có hai dạng: <b>девяно́сто</b> (cách 1·4) và '
    '<b>девяно́ста</b> cho mọi cách còn lại.</div>'
    '<div class="hd-warn">⚠️ Ba số dễ nhất khi biến cách, vì mỗi từ chỉ có một '
    'dạng gián tiếp: <b>сорока́</b> · <b>девяно́ста</b> · <b>ста</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>де́вять</b> chín · <b>девяно́стый</b> thứ 90 · '
    '<b>девятьсо́т</b> chín trăm</div>'
)

S["сто"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc trơn một âm tiết, không chẻ được. Cách 2 đến cách 6 '
    'chỉ một dạng: <b>ста</b>.</div>'
    '<div class="hd-why">Đây là gốc chung của cả dãy trăm: 200–900 đều là đơn vị '
    'dính với một dạng cũ của <b>сто</b> (-сти · -ста · -сот).</div>'
    '<div class="hd-why">Cùng gốc Ấn–Âu rất xa với "cent", "century", "percent" '
    'trong tiếng Anh — cũng là "trăm".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>со́тня</b> một trăm (nhóm trăm) · <b>со́тый</b> '
    'thứ 100 · <b>столе́тие</b> thế kỷ</div>'
)

S["двести"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">две-</span>'
    '<span class="hd-gloss">hai</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сти</span>'
    '<span class="hd-gloss">dạng số ĐÔI cổ của <b>сто</b> (hai cái trăm)</span>'
    '</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiếng Nga không ghép *два ста: 200 giữ lại dạng riêng '
    'dùng cho đúng hai cái, nay chỉ còn sót ở từ này.</div>'
    '<div class="hd-warn">⚠️ Từ 200 đến 900, biến cách phải đổi CẢ HAI nửa: '
    '<b>две́сти</b> → <b>двухсо́т</b> (cách 2), <b>двумста́м</b> (cách 3), '
    '<b>двумяста́ми</b> (cách 5). Đây là chỗ khó nhất của số trăm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>два</b> hai · <b>два́дцать</b> hai mươi · '
    '<b>сто</b> một trăm</div>'
)

S["триста"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">три-</span>'
    '<span class="hd-gloss">ba</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ста</span>'
    '<span class="hd-gloss">dạng nhiều của <b>сто</b>, dùng sau 3 và 4</span>'
    '</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đếm thì trọng âm đứng yên ở <b>три́ста</b>, nhưng biến '
    'cách thì dồn ra sau và phần đầu thành трёх-: <b>трёхсо́т</b> (cách 2).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>три</b> ba · <b>три́дцать</b> ba mươi · '
    '<b>тре́тий</b> thứ ba</div>'
)

S["четыреста"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">четыре-</span>'
    '<span class="hd-gloss">bốn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ста</span>'
    '<span class="hd-gloss">dạng nhiều của <b>сто</b>, chung với '
    '<b>три́ста</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">300 và 400 là hai số duy nhất lấy -ста. Trọng âm giữ '
    'nguyên chỗ của <b>четы́ре</b>; cách 2 là <b>четырёхсо́т</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>четы́ре</b> bốn · <b>четвёртый</b> thứ tư · '
    '<b>сто</b> một trăm</div>'
)

S["пятьсот"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пять-</span>'
    '<span class="hd-gloss">năm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сот</span>'
    '<span class="hd-gloss">cách 2 số nhiều của <b>сто</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là "năm CỦA những trăm" — cái luật lớn của số '
    'từ đã đóng băng ngay trong từ. Cách 2: <b>пятисо́т</b>.</div>'
    '<div class="hd-warn">⚠️ Luật đó: số từ 5 trở lên bắt từ đi sau về cách 2 số '
    'nhiều — <b>пятьсо́т рубле́й</b>, <b>три́дцать лет</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пять</b> năm · <b>пя́тый</b> thứ 5 · '
    '<b>пятьдеся́т</b> năm mươi</div>'
)

S["шестьсот"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">шесть-</span>'
    '<span class="hd-gloss">sáu</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сот</span>'
    '<span class="hd-gloss">cách 2 số nhiều của <b>сто</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng khuôn <b>пятьсо́т</b>: từ 500 trở lên đều là đơn vị '
    'dính với -сот, trọng âm luôn ở đuôi. Cách 2: <b>шестисо́т</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>шесть</b> sáu · <b>шесто́й</b> thứ 6 · '
    '<b>шестьдеся́т</b> sáu mươi</div>'
)

S["семьсот"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">семь-</span>'
    '<span class="hd-gloss">bảy</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сот</span>'
    '<span class="hd-gloss">cách 2 số nhiều của <b>сто</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cách 2: <b>семисо́т</b> — phần đầu về dạng семи- y như '
    'trong <b>семи́десяти</b>.</div>'
    '<div class="hd-warn">⚠️ 70 và 700 lệch nhau đúng ở trọng âm: '
    '<b>се́мьдесят</b> nhấn đầu, <b>семьсо́т</b> nhấn cuối.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>семь</b> bảy · <b>седьмо́й</b> thứ 7 · '
    '<b>се́мьдесят</b> bảy mươi</div>'
)

S["восемьсот"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">восемь-</span>'
    '<span class="hd-gloss">tám</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сот</span>'
    '<span class="hd-gloss">cách 2 số nhiều của <b>сто</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trọng âm ở đuôi <b>восемьсо́т</b>, ngược hẳn với '
    '<b>во́семьдесят</b> (80). Biến cách thì phần đầu rụng chữ <b>е</b> thành '
    'восьми- như trong <b>восьми́десяти</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>во́семь</b> tám · <b>восьмо́й</b> thứ 8 · '
    '<b>во́семьдесят</b> tám mươi</div>'
)

S["девятьсот"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">девять-</span>'
    '<span class="hd-gloss">chín</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сот</span>'
    '<span class="hd-gloss">cách 2 số nhiều của <b>сто</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Số cuối của dãy trăm và dựng đúng khuôn — khác '
    '<b>девяно́сто</b> (90) vốn phá khuôn. Cách 2: <b>девятисо́т</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>де́вять</b> chín · <b>девя́тый</b> thứ 9 · '
    '<b>девяно́сто</b> chín mươi</div>'
)

S["тысяча"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được; cùng gốc Ấn–Âu rất xa với '
    '"thousand" trong tiếng Anh.</div>'
    '<div class="hd-why">Khác mọi số ở trên, đây là một DANH TỪ: biến cách như '
    '<b>да́ча</b> (<b>ты́сячи</b>, <b>ты́сячу</b>), trọng âm đứng yên ở ты́-.</div>'
    '<div class="hd-warn">⚠️ Vì là danh từ nên nó đếm được: <b>две ты́сячи</b> '
    '(hai nghìn), và số nhiều <b>ты́сячи</b> nghĩa là "hàng nghìn".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ты́сячный</b> thứ 1000 · <b>тысячеле́тие</b> '
    'thiên niên kỷ</div>'
)
