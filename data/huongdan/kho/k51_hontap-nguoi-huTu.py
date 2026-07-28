# -*- coding: utf-8 -*-
"""k51 — hontap-nguoi-huTu: LÔ SỬA, không phải lô soạn mới.

Giữ nguyên phần đang tốt của nội dung cũ; chỉ làm ba việc:
  (1) thêm mục "Họ hàng" cho thẻ nào thiếu,
  (2) cắt xuống tối đa 2 ô đỏ,
  (3) cắt cho vừa một màn hình iPhone (<700px).

🔴 KHÔNG có khối dùng chung. Hai khối cũ ("Hai dạng -ский / по-…-ски" lặp ở 5 thẻ
và "Tính từ → trạng từ" lặp ở 4 thẻ) đã BỎ HẲN — phần nào thật sự cần cho CHÍNH
từ đó thì hoà một câu vào "Cách nhớ" của riêng thẻ ấy.
"""

S = {}
V = {}

# ─────────────────────────────────────────────────────────── quốc tịch / ngôn ngữ

S["англичанин"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">Англи-</span>'
    '<span class="hd-gloss">А́нглия — nước Anh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-чан-</span>'
    '<span class="hd-gloss">biến thể của <b>-ан-</b> sau <b>и</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ин</span>'
    '<span class="hd-gloss">hậu tố NGƯỜI NAM — lớp cổ hơn <b>-ец</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ <b>phá luật</b>: người Anh KHÔNG phải <i>*англиец</i> mà là '
    '<b>англича́нин</b>. Hậu tố <b>-анин / -янин</b> là lớp cổ, chỉ dành cho vài dân tộc '
    'quen thuộc lâu đời với người Nga.</div>'
    '<div class="hd-warn"><b>Bẫy số nhiều:</b> lớp <b>-анин</b> RỤNG mất <b>-ин</b> khi sang '
    'số nhiều — англича́н<b>ин</b> → англича́н<b>е</b>, không phải <i>*англичанины</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>А́нглия</b> nước Anh · <b>англича́нка</b> người Anh (nữ) · '
    '<b>англи́йский</b> thuộc Anh · <b>по-англи́йски</b> bằng tiếng Anh · cùng lớp '
    '<b>-анин</b>: <b>славяни́н</b>, <b>россия́нин</b></div>'
)

S["английский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">Англи-</span>'
    '<span class="hd-gloss">А́нглия — nước Anh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-йск-</span>'
    '<span class="hd-gloss">hậu tố tính từ, biến thể sau <b>и</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span>'
    '<span class="hd-gloss">đuôi tính từ, giống đực số ít</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tên nước tận cùng <b>-ия</b> thì hậu tố mọc thêm chữ <b>й</b> cho trôi '
    'miệng: Англ<b>и</b>я → англ<b>и́й</b>ский. Cùng luật: <b>Росси́я</b> → <b>росси́йский</b>, '
    '<b>И́ндия</b> → <b>инди́йский</b>.</div>'
    '<div class="hd-warn"><b>Bẫy:</b> tính từ dựng từ TÊN NƯỚC, còn danh từ chỉ người lại dựng '
    'khác hẳn — <b>англича́нин</b>. Hai nhánh này không suy ra được nhau.</div>'
    '<div class="hd-warn"><b>Đi với DANH TỪ:</b> <b>англи́йский язы́к</b> = tiếng Anh. Còn "nói/đọc '
    'BẰNG tiếng Anh" thì phải đổi sang trạng từ <b>по-англи́йски</b> — bỏ chữ <b>й</b>, thêm '
    '<b>по-</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>А́нглия</b> nước Anh · <b>англича́нин</b> người Anh (nam) · '
    '<b>англича́нка</b> (nữ) · <b>по-англи́йски</b> bằng tiếng Anh</div>'
)

S["немецкий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">нем-</span>'
    '<span class="hd-gloss">CÂM — cùng gốc <b>немо́й</b> (câm)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ец-</span>'
    '<span class="hd-gloss">hậu tố người, còn sót lại trong tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-кий</span>'
    '<span class="hd-gloss">đuôi tính từ, dạng rút của <b>-ский</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tính từ này dựng từ <b>TÊN NGƯỜI</b> (<b>не́мец</b>) chứ không phải tên '
    'nước — nước là <b>Герма́ния</b>, chẳng dính gì. Khi <b>ц</b> gặp <b>-ский</b> thì chữ <b>с</b> '
    'bị nuốt mất: не́мец + ский → неме́<b>цк</b>ий. Luật <b>ц + ск → цк</b> lặp khắp nơi.</div>'
    '<div class="hd-warn"><b>Bẫy trọng âm:</b> danh từ <b>не́мец</b> nhấn đầu, còn tính từ '
    '<b>неме́цкий</b> nhấn giữa. Trọng âm DỊCH khi thêm hậu tố — chuyện rất thường ở tiếng '
    'Nga.</div>'
    '<div class="hd-warn"><b>Đi với DANH TỪ:</b> <b>неме́цкий язы́к</b> = tiếng Đức. Nói BẰNG tiếng '
    'Đức thì là trạng từ <b>по-неме́цки</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>немо́й</b> câm · <b>не́мец</b> người Đức (nam) · <b>не́мка</b> (nữ) · '
    '<b>по-неме́цки</b> bằng tiếng Đức · <b>Герма́ния</b> nước Đức</div>'
)

S["по-русски"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố "theo kiểu…, bằng…"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-русс-</span>'
    '<span class="hd-gloss">Русь — gốc tên dân tộc Nga</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ски</span>'
    '<span class="hd-gloss">đuôi TRẠNG TỪ — <b>-ский</b> đã bỏ chữ <b>й</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ bạn dùng nhiều nhất cả đời học tiếng Nga: <b>Я говорю́ по-ру́сски</b> = '
    'Tôi nói tiếng Nga. Nhớ nguyên câu thay vì nhớ từ lẻ. Nó tả ĐỘNG TỪ; đi với danh từ thì phải '
    'dùng tính từ <b>ру́сский язы́к</b>.</div>'
    '<div class="hd-warn"><b>Bẫy chính tả:</b> giữ đủ <b>hai chữ с</b> (Рус + ск) và <b>KHÔNG có й</b> '
    'ở cuối. Sai một trong hai là hỏng: <i>*по-руски</i>, <i>*по-русский</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>Росси́я</b> nước Nga · <b>ру́сский</b> người Nga; tiếng Nga · '
    '<b>росси́йский</b> thuộc nhà nước Nga · <b>россия́нин</b> công dân Nga</div>'
)

S["по-французски"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố "theo kiểu…, bằng…"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-француз-</span>'
    '<span class="hd-gloss">францу́з — người Pháp</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ски</span>'
    '<span class="hd-gloss">đuôi TRẠNG TỪ — <b>-ский</b> đã bỏ chữ <b>й</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dựng đúng luật chung: lấy tính từ <b>францу́зский</b>, bỏ <b>й</b> cuối, '
    'thêm <b>по-</b> đầu. Nó tả ĐỘNG TỪ: <b>говорю́ по-францу́зски</b> = tôi nói tiếng Pháp.</div>'
    '<div class="hd-warn"><b>Bẫy chính tả:</b> chữ <b>з</b> đọc gần như mất (nghe "фран-ЦУС-ки") '
    'nhưng <b>viết vẫn phải có</b>. Đếm đủ: ф-р-а-н-ц-у-з-с-к-и.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>Фра́нция</b> nước Pháp · <b>францу́з</b> người Pháp (nam) · '
    '<b>францу́женка</b> (nữ) · <b>францу́зский</b> thuộc Pháp</div>'
)

S["русский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">Рус-</span>'
    '<span class="hd-gloss">Русь — nhà nước Nga cổ, gốc tên dân tộc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ск-</span>'
    '<span class="hd-gloss">hậu tố tạo TÍNH TỪ từ tên đất, tên người</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span>'
    '<span class="hd-gloss">đuôi tính từ, giống đực số ít</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là quốc tịch duy nhất người ta gọi bằng <b>TÍNH TỪ</b>: đàn ông là '
    '<b>ру́сский</b>, phụ nữ là <b>ру́сская</b> — nghĩa đen "người thuộc về Rus". Mọi dân tộc khác '
    'đều có danh từ riêng (<b>не́мец</b>, <b>испа́нец</b>). Hai chữ <b>с</b> là do <b>Рус</b> + '
    '<b>ск</b> ghép lại, mỗi bên góp một — nhớ vậy thì không viết thiếu.</div>'
    '<div class="hd-warn"><b>Bẫy nghĩa:</b> <b>ру́сский</b> = thuộc DÂN TỘC Nga; <b>росси́йский</b> = '
    'thuộc NHÀ NƯỚC Nga. Hộ chiếu ghi <i>российский</i>, còn ngôn ngữ thì luôn là <i>русский '
    'язык</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>Русь</b> nước Nga cổ · <b>Росси́я</b> nước Nga · <b>росси́йский</b> '
    'thuộc nhà nước Nga · <b>россия́нин</b> công dân Nga · <b>по-ру́сски</b> bằng tiếng Nga</div>'
)

S["французский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">француз-</span>'
    '<span class="hd-gloss">францу́з — người Pháp (danh từ)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ск-</span>'
    '<span class="hd-gloss">hậu tố tạo tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span>'
    '<span class="hd-gloss">đuôi tính từ, giống đực số ít</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dựng từ <b>францу́з</b> chứ không phải từ <b>Фра́нция</b> — nên chữ <b>з</b> '
    'ở lại, thành cụm ba phụ âm <b>-зск-</b>. Trông nặng nhưng viết dễ: lấy <b>францу́з</b> nguyên '
    'vẹn rồi dán <b>-ский</b> vào.</div>'
    '<div class="hd-warn"><b>Bẫy chính tả:</b> đọc thì <b>з</b> gần như biến mất (nghe "фран-ЦУС-кий") '
    'nhưng <b>viết vẫn phải có з</b>. Đúng loại lỗi hay mắc ở ô gõ.</div>'
    '<div class="hd-warn"><b>Đi với DANH TỪ.</b> Nói BẰNG tiếng Pháp thì đổi sang trạng từ '
    '<b>по-францу́зски</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>Фра́нция</b> nước Pháp · <b>францу́з</b> người Pháp (nam) · '
    '<b>францу́женка</b> (nữ) · <b>по-францу́зски</b> bằng tiếng Pháp</div>'
)

# ─────────────────────────────────────────────────────── học hành / thuật ngữ

S["грамматика"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">граммат-</span>'
    '<span class="hd-gloss">Hy Lạp <i>gramma</i> — CHỮ VIẾT, nét vạch</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ика</span>'
    '<span class="hd-gloss">hậu tố NGÀNH HỌC</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc: <b>môn học về chữ viết</b>. Đuôi <b>-ика</b> là NGÀNH, đổi thành '
    '<b>-ик</b> là ra NGƯỜI làm ngành đó: <b>фи́зика</b> môn vật lý → <b>фи́зик</b> nhà vật lý. Gốc '
    '<i>gramma</i> còn nằm trong <i>grammar, telegram, program</i>.</div>'
    '<div class="hd-warn"><b>HAI chữ м:</b> <b>грамма́тика</b> giữ nguyên hai <b>м</b> của tiếng Hy '
    'Lạp, y như <b>програ́мма</b>. Đây là chỗ dễ gõ thiếu nhất.</div>'
    '<div class="hd-warn"><b>Nhưng cùng gốc mà MỘT chữ м:</b> <b>гра́мотный</b> = biết chữ; giỏi, '
    'thạo việc. Đừng lây hai <b>м</b> sang nó.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гра́мотный</b> biết chữ; thạo · <b>програ́мма</b> chương trình · '
    '<b>телегра́мма</b> điện tín · cùng đuôi <b>-ика</b>: <b>фи́зика</b>, <b>матема́тика</b></div>'
)

S["спортивный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">спорт-</span>'
    '<span class="hd-gloss">спорт — thể thao</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ивн-</span>'
    '<span class="hd-gloss">hậu tố tính từ quốc tế (đúng <i>-ive</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ, giống đực số ít</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hậu tố <b>-ивный</b> là anh em với <b>-альный</b> bạn đã học — cũng là cửa '
    'vào kho từ quốc tế: <i>active</i> → <b>акти́вный</b>, <i>effective</i> → <b>эффекти́вный</b>. '
    'Và như mọi từ mượn, trọng âm rơi muộn hơn tiếng Anh, vào <b>-и́в-</b>.</div>'
    '<div class="hd-warn"><b>Hai nghĩa:</b> <b>спорти́вный костю́м</b> = bộ đồ thể thao (thuộc thể '
    'thao) · <b>спорти́вный па́рень</b> = chàng trai khoẻ khoắn, có dáng vận động viên.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спорт</b> thể thao · <b>спортсме́н</b> vận động viên · '
    '<b>акти́вный</b> năng động · <b>эффекти́вный</b> hiệu quả</div>'
)

S["спряжение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">CÙNG, gộp lại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пряж-</span>'
    '<span class="hd-gloss">BUỘC, thắng ngựa vào xe (<b>г</b> mềm thành <b>ж</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">động từ → DANH TỪ, giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Là <b>спряга́ть</b> (chia động từ) đóng gói thành danh từ. Hình ảnh gốc: '
    '<b>thắng mấy con ngựa vào chung một cỗ xe</b> — chia động từ cũng là buộc một gốc vào cả bộ '
    'sáu đuôi. Tiếng Anh trùng khít: <i>conjugation</i> ← <i>con-</i> (cùng) + <i>iugum</i> (cái '
    'ách buộc bò).</div>'
    '<div class="hd-warn"><b>Thuật ngữ dùng ngay:</b> tiếng Nga có <b>hai lớp chia</b> — '
    '<b>пе́рвое спряже́ние</b> (lớp 1, nguyên âm <b>Е</b>) và <b>второ́е спряже́ние</b> (lớp 2, '
    'nguyên âm <b>И</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спряга́ть</b> chia động từ · <b>упражне́ние</b> bài tập · '
    '<b>предложе́ние</b> câu; lời đề nghị · <b>зада́ние</b> nhiệm vụ</div>'
)

S["близко"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">близ-</span>'
    '<span class="hd-gloss">GẦN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-о</span>'
    '<span class="hd-gloss">hậu tố + đuôi TRẠNG TỪ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Là tính từ <b>бли́зкий</b> đổi đuôi thành <b>-о</b>. Hai thẻ là một cặp: '
    'tính từ tả danh từ, trạng từ tả động từ hoặc cả câu — <b>Э́то бли́зко</b> = Chỗ đó gần '
    'thôi.</div>'
    '<div class="hd-warn"><b>Gần CÁI GÌ</b> thì phải mượn giới từ <b>от</b> + cách 2: '
    '<b>бли́зко от до́ма</b> = gần nhà.</div>'
    '<div class="hd-warn"><b>Tin tốt:</b> dạng so sánh <b>бли́же</b> dùng chung cho CẢ tính từ lẫn '
    'trạng từ — không phải nhớ hai lần.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бли́зкий</b> gần (tính từ) · <b>бли́же</b> gần hơn · <b>бли́жний</b> ở '
    'gần · <b>бли́зость</b> sự gần gũi · <b>приблизи́тельно</b> khoảng chừng</div>'
)

# ─────────────────────────────────────────────── từ chức năng: giới từ, liên từ

S["за"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Giới từ một chữ, không chẻ được — nhưng là một trong những giới từ '
    '<b>nhiều việc nhất</b> tiếng Nga. Nó đi với HAI cách, và cách quyết định nghĩa.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-row"><span class="hd-piece">за + cách 5</span>'
    '<span class="hd-gloss">Ở ĐÂU (đứng yên): <b>за столо́м</b> = ở bàn (ngồi sau bàn)</span></div>'
    '<div class="hd-row"><span class="hd-piece">за + cách 4</span>'
    '<span class="hd-gloss">ĐI ĐÂU (chuyển động) / ĐỔI LẤY: <b>за стол</b> = vào bàn · '
    '<b>спаси́бо за по́мощь</b> = cảm ơn vì sự giúp đỡ</span></div>'
    '<div class="hd-why">Đây là <b>khuôn chung</b> của giới từ chỉ vị trí: cách 5 = đứng yên, cách '
    '4 = có chuyển động. Giống hệt <b>под</b>: <b>под столо́м</b> ở dưới bàn ↔ <b>под стол</b> chui '
    'xuống dưới bàn.</div>'
    '<div class="hd-warn"><b>Nghĩa "vì, để đổi lấy" dùng mỗi ngày:</b> <b>Спаси́бо за всё</b> = Cảm '
    'ơn vì tất cả · <b>плати́ть за обе́д</b> = trả tiền bữa trưa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Làm TIỀN TỐ "để lại phía sau": <b>забы́ть</b> quên · <b>закры́ть</b> đóng · '
    '<b>зайти́</b> ghé vào · <b>за́втра</b> ngày mai (sau buổi sáng)</div>'
)

S["или"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Liên từ hai âm tiết. Theo <b>từ nguyên</b> nó là <b>и</b> (và) + tiểu từ '
    '<b>ли</b> ("liệu…") dính lại — chứ ngày nay không còn chẻ ra dùng riêng được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-warn"><b>Ba từ trông giống nhau mà nối câu ba kiểu:</b><br>'
    '<b>и́ли</b> = hoặc<br><b>и</b> = và<br><b>е́сли</b> = nếu<br>'
    'Đáng đọc to cả ba cạnh nhau vài lần.</div>'
    '<div class="hd-warn"><b>Dạng nhấn mạnh:</b> <b>и́ли… и́ли…</b> = hoặc là… hoặc là… — dùng khi '
    'bắt buộc chọn một. <i>И́ли ты, и́ли я</i> = Hoặc cậu, hoặc tớ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Bộ liên từ nối câu: <b>и</b> và · <b>а</b> còn, mà · <b>но</b> nhưng · '
    '<b>е́сли</b> nếu · <b>ли</b> tiểu từ hỏi "liệu"</div>'
)

S["про"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Giới từ một âm tiết, <b>luôn đi với cách 4</b>. Nghĩa: VỀ, về chuyện…</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-warn"><b>Cặp phải phân biệt — cùng nghĩa, khác giọng:</b><br>'
    '<b>про</b> + cách 4 = KHẨU NGỮ: <i>Расскажи́ про себя́</i> = Kể về cậu đi<br>'
    '<b>о / об</b> + cách 6 = trung tính, văn viết: <i>Я ду́маю о тебе́</i><br>'
    'Bài viết và thi cử thì dùng <b>о</b>.</div>'
    '<div class="hd-warn"><b>Cụm phải thuộc:</b> <b>про себя́</b> = thầm trong bụng, không nói ra '
    '(đọc thầm, nghĩ thầm).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Làm TIỀN TỐ "xuyên suốt, từ đầu đến cuối": <b>прочита́ть</b> đọc hết · '
    '<b>проверя́ть</b> kiểm tra · <b>пройти́</b> đi qua · <b>пропусти́ть</b> để lọt, bỏ sót</div>'
)

S["себя"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Đại từ <b>PHẢN THÂN</b> — trỏ ngược về chính chủ ngữ của câu, nghĩa "bản '
    'thân mình". Không chẻ ra thành phần nhỏ hơn.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dùng chung cho mọi ngôi và mọi giống: tôi, bạn, anh ấy, chúng ta đều là '
    '<b>себя́</b>. Chỗ này dễ hơn tiếng Anh, vốn phải chọn <i>myself / yourself / himself</i>.</div>'
    '<div class="hd-warn"><b>Đặc điểm lạ nhất:</b> nó <b>KHÔNG CÓ cách 1</b> — không bao giờ làm chủ '
    'ngữ, nên từ điển đành ghi thẳng dạng cách 4 làm tên gọi.</div>'
    '<div class="hd-warn"><b>Đây chính là nguồn gốc đuôi -ся!</b> <b>учи́ть</b> + <b>-ся</b> = dạy '
    'chính mình = học. Biết vậy thì cả lớp động từ phản thân bỗng có lý.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>себя́</b> (cách 2, 4) · <b>себе́</b> (cách 3, 6) · <b>собо́й</b> (cách 5) '
    '· <b>у себя́</b> ở chỗ mình · <b>к себе́</b> KÉO / <b>от себя́</b> ĐẨY (chữ trên cửa)</div>'
)

S["только"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ chức năng, không chẻ ra thành phần có nghĩa được. Nghĩa lõi: '
    '<b>CHỈ, chỉ có</b> — nhưng nó còn hai việc nữa gặp rất sớm.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-row"><span class="hd-piece">chỉ, mỗi</span>'
    '<span class="hd-gloss">У меня́ <b>то́лько</b> оди́н вопро́с = Tôi chỉ có một câu hỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">vừa mới</span>'
    '<span class="hd-gloss">Я <b>то́лько что</b> пришёл = Tôi vừa mới đến</span></div>'
    '<div class="hd-row"><span class="hd-piece">ngay khi</span>'
    '<span class="hd-gloss"><b>Как то́лько</b> он придёт… = Ngay khi anh ấy đến…</span></div>'
    '<div class="hd-warn"><b>Vị trí quyết định nghĩa:</b> nó nhấn mạnh <b>từ đứng ngay SAU</b>. '
    '<i>То́лько я чита́л</i> = chỉ MÌNH TÔI đọc · <i>Я чита́л то́лько кни́гу</i> = tôi chỉ đọc MỖI '
    'quyển sách.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лишь</b> chỉ (đồng nghĩa, văn viết hơn) · <b>еди́нственный</b> duy nhất · '
    '<b>не то́лько… но и…</b> không những… mà còn</div>'
)

S["отлично"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">RỜI RA, tách khỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лич-</span>'
    '<span class="hd-gloss">MẶT, diện mạo — cùng gốc <b>лицо́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-о</span>'
    '<span class="hd-gloss">hậu tố + đuôi TRẠNG TỪ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>khác mặt hẳn ra</b>, nổi bật khỏi đám đông — từ "khác biệt" '
    'mà thành "xuất sắc". Tiếng Anh đi đúng đường đó: <i>distinguished</i> ← <i>distinguish</i> '
    '(phân biệt).</div>'
    '<div class="hd-warn"><b>Đây là ĐIỂM SỐ cao nhất ở Nga:</b> thang điểm 5 bậc, <b>отли́чно</b> = '
    'điểm 5. Học sinh giỏi gọi là <b>отли́чник</b>; dưới nó là <b>хорошо́</b> (4).</div>'
    '<div class="hd-warn">Trong hội thoại, <b>Отли́чно!</b> = "Tuyệt vời!" — dùng như tiếng Việt '
    '"Ngon!", rất thông dụng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лицо́</b> khuôn mặt · <b>ли́чный</b> cá nhân · <b>отлича́ть</b> phân biệt '
    '· <b>разли́чие</b> sự khác biệt · <b>отли́чник</b> học sinh giỏi</div>'
)

S["правильно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">прав-</span>'
    '<span class="hd-gloss">ĐÚNG, thẳng, phải</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ил-</span>'
    '<span class="hd-gloss">qua <b>пра́вило</b> — quy tắc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ьн-о</span>'
    '<span class="hd-gloss">hậu tố tính từ + đuôi TRẠNG TỪ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>đúng theo quy tắc</b> — nó mọc thẳng ra từ <b>пра́вило</b>. '
    'Gốc <b>прав-</b> gom đúng ba ý mà tiếng Việt cũng gom vào chữ "phải": bên phải · lẽ phải · '
    'có quyền.</div>'
    '<div class="hd-warn"><b>Dùng thật mỗi ngày:</b> nghe câu này là biết trả lời trúng. Và thêm '
    '<b>не-</b> vào đầu là được ngay từ trái nghĩa "sai" — cỗ máy nhân đôi vốn từ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пра́вило</b> quy tắc · <b>пра́вда</b> sự thật · <b>пра́во</b> quyền · '
    '<b>пра́вый</b> bên phải; đúng · <b>испра́вить</b> sửa cho đúng</div>'
)

S["час"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ <b>gốc trơn</b> một âm tiết, giống đực. Nghĩa: <b>giờ</b> (đơn vị 60 '
    'phút).</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ quan trọng nhất mọc ra từ đây: <b>сейча́с</b> (bây giờ) = <b>сей</b> '
    '(này — đại từ cổ) + <b>час</b> = "giờ này". Một trong những từ bạn dùng nhiều nhất, và giờ '
    'thì nó chẻ được.</div>'
    '<div class="hd-warn"><b>BẪY SỐ NHIỀU đổi nghĩa:</b> <b>час</b> = giờ, nhưng <b>часы́</b> = '
    '<b>CÁI ĐỒNG HỒ</b> — cùng nhóm chỉ-có-số-nhiều với <b>де́ньги</b>, <b>очки́</b>.</div>'
    '<div class="hd-warn"><b>Đếm giờ:</b> <b>1 час</b> · <b>2, 3, 4 часа́</b> (cách 2 số ít) · '
    '<b>5–20 часо́в</b> (cách 2 số nhiều). Con số quyết định đuôi — luật áp cho MỌI danh từ đếm '
    'được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сейча́с</b> bây giờ · <b>часы́</b> đồng hồ · <b>часово́й</b> thuộc giờ · '
    '<b>час пик</b> giờ cao điểm</div>'
)

S["часто"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">част-</span>'
    '<span class="hd-gloss">DÀY, sít nhau (<b>ча́стый</b> = dày đặc)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi TRẠNG TỪ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa lõi là <b>DÀY</b> — các lần xảy ra sít vào nhau thì gọi là "thường '
    'xuyên". Cùng một hình ảnh: <b>ча́стый лес</b> (rừng rậm, cây mọc dày) và <b>ча́сто</b> (hay xảy '
    'ra). Trạng từ tần suất đứng TRƯỚC động từ: <b>Я ча́сто чита́ю</b>.</div>'
    '<div class="hd-warn"><b>Bộ ba tần suất:</b> <b>ча́сто</b> thường xuyên ↔ <b>ре́дко</b> hiếm khi, '
    'ở giữa là <b>иногда́</b> đôi khi (<b>ино-</b> khác + <b>когда́</b> khi nào → "vào lúc '
    'khác").</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ча́стый</b> dày; thường xuyên · <b>ча́ще</b> hay hơn · '
    '<b>частота́</b> tần số · trái nghĩa <b>ре́дко</b> hiếm khi</div>'
)

# ══════════════════════════════════════════════════════════════════════════
# FIELD Vietnamese — đề bài của deck 1-go (README §2c)
#
# Ổ va chạm lớn nhất của lô này: bộ TÍNH TỪ quốc tịch (английский, немецкий,
# французский, русский) và bộ TRẠNG TỪ tương ứng (по-русски, по-французски)
# đang cùng mang chữ "tiếng Anh / tiếng Pháp / tiếng Nga" trong nghĩa Việt —
# nhìn đề bài không thể biết phải gõ tính từ hay trạng từ. Đã tách bằng cách
# ghi rõ TỪ LOẠI + chỗ nó đứng trong câu.
#
# Ổ thứ hai: bốn trạng từ близко / отлично / правильно / часто đụng chính
# tính từ gốc của chúng (близкий, отличный, правильный, частый) — cũng gắn
# nhãn "(trạng từ)".
#
# ⚠️ Cố ý KHÔNG để chữ Nga của chính đáp án vào dòng tiếng Việt (kể cả ví dụ
#    minh hoạ), vì như vậy là cho sẵn đáp án ở ô gõ.
# ══════════════════════════════════════════════════════════════════════════

V["английский"]    = "thuộc về nước Anh, kiểu Anh (TÍNH TỪ — đi kèm danh từ)"
V["немецкий"]      = "thuộc về nước Đức, kiểu Đức (TÍNH TỪ — đi kèm danh từ)"
V["французский"]   = "thuộc về nước Pháp, kiểu Pháp (TÍNH TỪ — đi kèm danh từ)"
V["русский"]       = "thuộc dân tộc Nga; người Nga (TÍNH TỪ — đi kèm danh từ)"
V["по-русски"]     = "bằng tiếng Nga (TRẠNG TỪ — nói/đọc/viết bằng tiếng Nga)"
V["по-французски"] = "bằng tiếng Pháp (TRẠNG TỪ — nói/đọc bằng tiếng Pháp)"
V["спортивный"]    = "thuộc về thể thao, có dáng vận động viên (tính từ)"
V["спряжение"]     = "sự chia động từ; lối chia (danh từ)"
V["близко"]        = "gần, ở gần (TRẠNG TỪ — không phải tính từ)"
V["за"]            = "đằng sau; vì, để đổi lấy (giới từ, đi với cách 4 hoặc cách 5)"
V["отлично"]       = "xuất sắc, tuyệt vời (TRẠNG TỪ — cũng là điểm 5 của Nga)"
V["правильно"]     = "đúng, làm đúng theo quy tắc (TRẠNG TỪ)"
V["про"]           = "về, về chuyện… (giới từ KHẨU NGỮ, đi với cách 4)"
V["себя"]          = "bản thân mình (đại từ phản thân, không có dạng chủ ngữ)"
V["только"]        = "chỉ, chỉ có mỗi"
V["час"]           = "giờ (đơn vị 60 phút)"
V["часто"]         = "thường xuyên, hay xảy ra (TRẠNG TỪ)"
