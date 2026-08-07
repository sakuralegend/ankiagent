# -*- coding: utf-8 -*-
"""k56 — people-family: tên dân tộc dựng bằng -ец (đàn ông) / -ка (phụ nữ), tính
từ -ский và trạng từ по-…-ски; cộng hai từ lẻ малы́ш và зачёт."""

S = {}
V = {}

S["испанец"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">испа́н-</span>'
    '<span class="hd-gloss">từ <b>Испа́ния</b> Tây Ban Nha</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ец</span>'
    '<span class="hd-gloss">ĐÀN ÔNG thuộc về nơi đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tên nước bỏ đuôi -ия rồi lắp -ец là ra người đàn ông; đổi -ец '
    'lấy -ка là ra phụ nữ (<b>испа́нка</b>).</div>'
    '<div class="hd-warn">Chữ <b>е</b> trong -ец là nguyên âm chạy: hễ thêm đuôi là nó '
    'rơi mất — <b>испа́нца</b>, <b>испа́нцу</b>, <b>испа́нцем</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>Испа́ния</b> Tây Ban Nha · <b>испа́нка</b> phụ nữ Tây Ban Nha · '
    '<b>испа́нский</b> thuộc về Tây Ban Nha</div>'
)

S["испанка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">испа́н-</span>'
    '<span class="hd-gloss">từ <b>Испа́ния</b> Tây Ban Nha</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">PHỤ NỮ thuộc về nơi đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng thân với <b>испа́нец</b>, chỉ thay đuôi đàn ông -ец bằng '
    'đuôi phụ nữ -ка. Trọng âm không nhúc nhích.</div>'
    '<div class="hd-warn">Số nhiều cách 2 bỏ hết đuôi thì còn cụm -нк khó đọc, nên tiếng '
    'Nga chèn <b>о</b> vào giữa: <b>испа́нок</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>испа́нец</b> người Tây Ban Nha · <b>испа́нский</b> thuộc về '
    'Tây Ban Nha · <b>Испа́ния</b> Tây Ban Nha</div>'
)

S["итальянец"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">италья́н-</span>'
    '<span class="hd-gloss">từ <b>Ита́лия</b> nước Ý</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ец</span>'
    '<span class="hd-gloss">ĐÀN ÔNG thuộc về nơi đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chữ и của <b>Ита́лия</b> co lại thành ь khi lắp đuôi, và trọng âm '
    'chạy theo về sau: <i>Ита́лия → италья́нец</i>.</div>'
    '<div class="hd-warn">Cũng rơi <b>е</b> như <b>испа́нец</b>: <b>италья́нца</b>, '
    '<b>италья́нцу</b>, <b>италья́нцем</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>Ита́лия</b> nước Ý · <b>италья́нка</b> phụ nữ Ý · '
    '<b>италья́нский</b> thuộc về nước Ý</div>'
)

S["итальянка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">италья́н-</span>'
    '<span class="hd-gloss">từ <b>Ита́лия</b> nước Ý</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">PHỤ NỮ thuộc về nơi đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bỏ -ец của <b>италья́нец</b>, lắp -ка vào đúng chỗ đó. Trọng âm '
    'giữ nguyên ở -я́н-.</div>'
    '<div class="hd-warn">Số nhiều cách 2 chèn <b>о</b> cho đọc được cụm -нк: '
    '<b>италья́нок</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>италья́нец</b> người Ý · <b>италья́нский</b> thuộc về nước Ý · '
    '<b>Ита́лия</b> nước Ý</div>'
)

S["китаянка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кита-</span>'
    '<span class="hd-gloss">từ <b>Кита́й</b> Trung Quốc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́нка</span>'
    '<span class="hd-gloss">PHỤ NỮ thuộc về nơi đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi phụ nữ ở đây là biến thể -янка chứ không phải -ка trơn như '
    '<b>испа́нка</b> — chỗ chọn đuôi nào là phải thuộc, không suy ra được. Đàn ông: <b>кита́ец</b>.</div>'
    '<div class="hd-warn">Trọng âm rời <b>Кита́й</b> mà nhảy sang -я́н-; số nhiều cách 2 '
    'chèn <b>о</b> cho đọc được cụm -нк: <b>китая́нок</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>Кита́й</b> Trung Quốc · <b>кита́ец</b> người Trung Quốc · '
    '<b>кита́йский</b> thuộc về Trung Quốc</div>'
)

S["кореец"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">коре́-</span>'
    '<span class="hd-gloss">từ <b>Коре́я</b> Hàn Quốc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ец</span>'
    '<span class="hd-gloss">ĐÀN ÔNG thuộc về nơi đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vẫn đúng công thức tên nước + -ец như <b>испа́нец</b>; phụ nữ thì '
    'lấy đuôi -я́нка (<b>корея́нка</b>).</div>'
    '<div class="hd-warn">Bảng chia trông như đổi thân, thật ra vẫn là <b>е</b> của -ец rơi '
    'đi: âm /j/ còn lại phải viết bằng <b>й</b> — <b>коре́ец → коре́йца</b>, '
    '<b>коре́йцу</b>, <b>коре́йцем</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>Коре́я</b> Hàn Quốc · <b>корея́нка</b> phụ nữ Hàn Quốc · '
    '<b>коре́йский</b> thuộc về Hàn Quốc</div>'
)

S["кореянка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">коре-</span>'
    '<span class="hd-gloss">từ <b>Коре́я</b> Hàn Quốc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́нка</span>'
    '<span class="hd-gloss">PHỤ NỮ thuộc về nơi đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng khuôn với <b>китая́нка</b>: cũng lấy biến thể -янка, không phải '
    '-ка trơn. Hai từ này đi cặp với nhau cho dễ thuộc.</div>'
    '<div class="hd-warn">Trọng âm KHÔNG ở lại chỗ của <b>Коре́я</b> mà nhảy sang -я́н-: '
    '<b>корея́нка</b>, không phải «коре́янка». Số nhiều cách 2 chèn о: <b>корея́нок</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>коре́ец</b> người Hàn Quốc · <b>коре́йский</b> thuộc về Hàn Quốc · '
    '<b>Коре́я</b> Hàn Quốc</div>'
)

S["малыш"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мал-</span>'
    '<span class="hd-gloss">NHỎ (gốc của <b>ма́ленький</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ы́ш</span>'
    '<span class="hd-gloss">kẻ nhỏ bé, nói giọng trìu mến</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là "kẻ nhỏ": lấy thẳng gốc của <b>ма́ленький</b> rồi lắp đuôi '
    '-ыш vào. Đuôi này thêm sắc trìu mến, nên từ ấm hơn <b>ребёнок</b> trung tính.</div>'
    '<div class="hd-warn">Trọng âm nhảy xuống đuôi ở mọi dạng còn lại: <b>малыша́</b>, '
    '<b>малышу́</b>, <b>малышо́м</b>, số nhiều <b>малыши́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ма́ленький</b> nhỏ · <b>ма́ло</b> ít · <b>малы́шка</b> bé gái</div>'
)

S["немец"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не́м-</span>'
    '<span class="hd-gloss">CÂM, không nói được (gốc của <b>немо́й</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ец</span>'
    '<span class="hd-gloss">ĐÀN ÔNG thuộc về nhóm đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ này là chỗ nhớ luật trọng âm dịch: <i>не́мец → неме́цкий → '
    'по-неме́цки</i>, thêm đuôi là trọng âm rời khỏi âm tiết đầu. Tên nước thì đi đường '
    'khác hẳn — <b>Герма́ния</b>, không cùng gốc.</div>'
    '<div class="hd-warn">⚠️ Mức tin: "câm" là từ nguyên (người nói thứ tiếng ta không '
    'hiểu), không phải luật suy ra được — đừng áp sang tên dân tộc khác.</div>'
    '<div class="hd-warn">Chữ <b>е</b> thứ hai là nguyên âm chạy, thêm đuôi là rơi: '
    '<b>не́мца</b>, <b>не́мцу</b>, <b>не́мцем</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>не́мка</b> phụ nữ Đức · <b>неме́цкий</b> thuộc về nước Đức · '
    '<b>немо́й</b> câm</div>'
)

S["француз"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">франц-</span>'
    '<span class="hd-gloss">PHÁP (cũng là thân của <b>Фра́нция</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-у́з</span>'
    '<span class="hd-gloss">đuôi hiếm, KHÔNG phải hậu tố -ец của Nga</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là ngoại lệ của bộ dân tộc: đàn ông không lắp -ец mà giữ '
    'nguyên đuôi -у́з lạ tai. Phải tới phía phụ nữ tiếng Nga mới lấy lại đuôi của mình '
    '(<b>францу́женка</b>).</div>'
    '<div class="hd-warn">Không có «францу́зец». Và tính từ cũng dựng thẳng từ đây: '
    '<b>францу́зский</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>Фра́нция</b> nước Pháp · <b>францу́женка</b> phụ nữ Pháp · '
    '<b>францу́зский</b> thuộc về nước Pháp</div>'
)

S["француженка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">францу́ж-</span>'
    '<span class="hd-gloss">thân của <b>францу́з</b>, з đã hoá ж</span></div>'
    '<div class="hd-row"><span class="hd-piece">-енка</span>'
    '<span class="hd-gloss">PHỤ NỮ thuộc về nhóm đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi -енка kéo theo phép biến âm <b>з → ж</b>, cùng dãy với '
    'г/к/х → ж/ч/ш đã gặp. Nhớ được chỗ đổi chữ này là viết đúng cả từ.</div>'
    '<div class="hd-warn">Số nhiều cách 2 chèn <b>о</b> cho đọc được cụm -нк: '
    '<b>францу́женок</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>францу́з</b> người Pháp · <b>францу́зский</b> thuộc về nước Pháp · '
    '<b>Фра́нция</b> nước Pháp</div>'
)

S["чех"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — <b>чех</b> là gốc trơn, một âm tiết, không có '
    'tiền tố cũng không có hậu tố. Chính nó mới là cái gốc để dựng ra từ khác.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cả họ mọc ngược ra từ đây: tên nước <b>Че́хия</b>, tính từ '
    '<b>че́шский</b>, phụ nữ <b>че́шка</b> — ngược chiều với <b>испа́нец</b> hay <b>италья́нец</b>, '
    'nơi tên nước mới là cái có trước.</div>'
    '<div class="hd-warn">Hễ lắp đuôi là <b>х hoá thành ш</b> (đúng dãy г/к/х → ж/ч/ш): '
    '<b>че́шский</b>, <b>че́шка</b> — không có «чехский».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>Че́хия</b> nước Séc · <b>че́шка</b> phụ nữ Séc · '
    '<b>че́шский</b> thuộc về nước Séc</div>'
)

S["арабский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ара́б-</span>'
    '<span class="hd-gloss">từ <b>ара́б</b> người Ả Rập</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ский</span>'
    '<span class="hd-gloss">THUỘC VỀ (đuôi tính từ nguồn gốc)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lắp -ский vào tên người/tên nơi là ra tính từ "thuộc về". Ở đây '
    'trọng âm đứng yên tại ара́-; đừng vội suy nó luôn dịch — <b>не́мец → неме́цкий</b> thì '
    'dịch, còn từ này thì không.</div>'
    '<div class="hd-warn">Tính từ loại nguồn gốc này không có dạng ngắn và không đẻ ra '
    'trạng từ đuôi -о. Muốn nói "bằng tiếng Ả Rập" phải dùng dạng có gạch nối '
    'по-ара́бски.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ара́б</b> người Ả Rập · <b>ара́бка</b> phụ nữ Ả Rập</div>'
)

S["испанский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">испа́н-</span>'
    '<span class="hd-gloss">từ <b>Испа́ния</b> Tây Ban Nha</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ский</span>'
    '<span class="hd-gloss">THUỘC VỀ (đuôi tính từ nguồn gốc)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tên nước <b>Испа́ния</b> bỏ đuôi -ия rồi lắp -ский vào chỗ đó. '
    'Trọng âm ở nguyên chỗ cũ, không dịch.</div>'
    '<div class="hd-warn">Đây là TÍNH TỪ nên phải bám vào một danh từ: <i>испа́нский '
    'язы́к</i>. Còn "nói bằng tiếng Tây Ban Nha" thì bám vào động từ, phải đổi sang trạng '
    'từ có gạch nối по-испа́нски.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>Испа́ния</b> Tây Ban Nha · <b>испа́нец</b> người Tây Ban Nha · '
    '<b>испа́нка</b> phụ nữ Tây Ban Nha</div>'
)

S["зачёт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">GHI VÀO, tính vào sổ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-чёт</span>'
    '<span class="hd-gloss">SỰ ĐẾM, sự tính (gốc чёт/счит)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là "cái được tính vào": buổi kiểm tra xong thì kiến thức '
    'của bạn được ghi vào sổ. Cùng gốc чёт với <b>счёт</b> và <b>отчёт</b>.</div>'
    '<div class="hd-warn">Chữ <b>ё</b> luôn mang trọng âm nên từ này không bao giờ cần đánh '
    'dấu, và trọng âm không rời chỗ ở bất kỳ cách nào.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>счёт</b> hoá đơn, tỉ số · <b>отчёт</b> bản báo cáo · '
    '<b>учёт</b> sự thống kê</div>'
)

S["по-английски"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">THEO LỐI, theo kiểu</span></div>'
    '<div class="hd-row"><span class="hd-piece">англи́йск-</span>'
    '<span class="hd-gloss">thân của <b>англи́йский</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и</span>'
    '<span class="hd-gloss">đuôi biến nó thành TRẠNG TỪ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Công thức cố định: lấy tính từ -ский, bỏ -ий thay bằng -и, thêm по- '
    'và một gạch nối. Vì по- là "theo lối" nên từ này vừa là "bằng tiếng Anh" vừa là "theo '
    'kiểu Anh". Trọng âm ở nguyên chỗ của tính từ.</div>'
    '<div class="hd-warn">Gạch nối là bắt buộc; viết liền hay tách rời đều sai.</div>'
    '<div class="hd-warn">Trạng từ nên bất biến — không giống, không số, không cách. Nó bám '
    'vào động từ: <i>говори́ть по-англи́йски</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>англи́йский</b> thuộc về nước Anh · <b>англича́нин</b> người Anh · '
    '<b>А́нглия</b> nước Anh</div>'
)

S["по-испански"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">THEO LỐI, theo kiểu</span></div>'
    '<div class="hd-row"><span class="hd-piece">испа́нск-</span>'
    '<span class="hd-gloss">thân của <b>испа́нский</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и</span>'
    '<span class="hd-gloss">đuôi biến nó thành TRẠNG TỪ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là câu trả lời cho câu hỏi "thế nào?" chứ không phải "cái gì?" '
    '— đó chính là chỗ nó tách khỏi tính từ <b>испа́нский</b>.</div>'
    '<div class="hd-warn">Bất biến tuyệt đối: thẻ này không có bảng chia, và trống là đúng '
    'chứ không phải thiếu dữ liệu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>испа́нский</b> thuộc về Tây Ban Nha · <b>испа́нец</b> người Tây '
    'Ban Nha · <b>Испа́ния</b> Tây Ban Nha</div>'
)

S["по-китайски"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">THEO LỐI, theo kiểu</span></div>'
    '<div class="hd-row"><span class="hd-piece">кита́йск-</span>'
    '<span class="hd-gloss">thân của <b>кита́йский</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и</span>'
    '<span class="hd-gloss">đuôi biến nó thành TRẠNG TỪ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chữ й cuối <b>Кита́й</b> không mất đi đâu cả, nó nằm ngay trong cụm '
    '-та́йск-. Nhìn thấy й là biết từ này dựng thẳng từ tên nước.</div>'
    '<div class="hd-warn">Trọng âm bám đúng chỗ của tên nước và không nhúc nhích qua cả ba '
    'bậc: <i>Кита́й → кита́йский → по-кита́йски</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кита́йский</b> thuộc về Trung Quốc · <b>кита́ец</b> người Trung '
    'Quốc · <b>китая́нка</b> phụ nữ Trung Quốc</div>'
)

S["по-немецки"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">THEO LỐI, theo kiểu</span></div>'
    '<div class="hd-row"><span class="hd-piece">неме́цк-</span>'
    '<span class="hd-gloss">thân của <b>неме́цкий</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и</span>'
    '<span class="hd-gloss">đuôi biến nó thành TRẠNG TỪ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không phải «-сски»: chữ ц của <b>не́мец</b> gặp đuôi -ский thì cụm '
    'ц+ск rút gọn thành цк. Ra <b>неме́цкий</b>, rồi bỏ -ий thêm -и như mọi từ по-…</div>'
    '<div class="hd-warn">Trọng âm ĐÃ DỊCH ngay từ bậc tính từ và ở lại đó: <i>не́мец → '
    'неме́цкий → по-неме́цки</i>. Đọc «по-не́мецки» là sai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>неме́цкий</b> thuộc về nước Đức · <b>не́мец</b> người Đức · '
    '<b>не́мка</b> phụ nữ Đức</div>'
)

# ── Field Vietnamese (README §2c) — chỉ những từ thật sự cần sửa ─────────────
# Ba khuôn chốt cho cả họ (lô này đang giữ 5/10 từ giống cái của họ):
#   · danh từ giống cái chỉ dân tộc → "người phụ nữ X".  Khớp mốc đã xong
#     (америка́нец "người Mỹ", америка́нка/англича́нка/не́мка "người phụ nữ …").
#     Trước sửa, riêng lô này đã dùng LẪN ba khuôn khác nhau.
#   · tính từ ngôn ngữ → "thuộc về (nước) X, tiếng X" (khớp вьетна́мский, кита́йский…).
#   · trạng từ по-… → "bằng tiếng X, theo kiểu X" (khớp по-ру́сски, по-францу́зски
#     đã xong). по- nghĩa "theo lối" nên nghĩa thứ hai là của chính cấu trúc,
#     không phải nới rộng; gloss của по-неме́цки đúng là "German" (nghĩa kiểu cách).

V = {
    "испанка": "người phụ nữ Tây Ban Nha",
    "итальянка": "người phụ nữ Ý",
    "китаянка": "người phụ nữ Trung Quốc",
    "арабский": "thuộc về Ả Rập, tiếng Ả Rập",
    "испанский": "thuộc về nước Tây Ban Nha, tiếng Tây Ban Nha",
    # зачёт trùng gần trọn dòng với тест ("bài kiểm tra, bài thi, thử nghiệm").
    # Gỡ bằng RÚT GỌN: bỏ "bài thi", đưa nghĩa gloss "knowledge check" lên đầu.
    "зачёт": "bài đánh giá kiến thức, bài kiểm tra",
    "по-английски": "bằng tiếng Anh, theo kiểu Anh",
    "по-испански": "bằng tiếng Tây Ban Nha, theo kiểu Tây Ban Nha",
    "по-китайски": "bằng tiếng Trung, theo kiểu Trung Quốc",
    "по-немецки": "bằng tiếng Đức, theo kiểu Đức",
}
