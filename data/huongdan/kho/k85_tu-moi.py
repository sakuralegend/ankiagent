# -*- coding: utf-8 -*-
"""k85 — tu-moi: 20 từ user vừa thêm, phần lớn là động từ chưa hoàn thành.

Mỗi thẻ soạn độc lập, không khối hệ thống. Chỗ cần nhất quán:
(1) ba động từ "pha" начина́ть / конча́ть / продолжа́ть cùng một luật: nguyên thể theo
    sau luôn ở thể CHƯA hoàn thành — trải ở начина́ть, hai thẻ kia dẫn chiếu một câu;
(2) luật -мн- → -мина- của cặp thể nằm ở вспомина́ть, запомина́ть dẫn chiếu;
(3) khớp khuôn chẻ đã có: -да- CHO (уда́ча, сда́ча), -мог-/-мощ- SỨC (по́мощь),
    -прос- XIN/HỎI (спроси́ть), вс- + -помн- (вспо́мнить), стро- XÂY (строи́тель),
    -кры- CHE (откры́тка), важ- SỨC NẶNG (ва́жно), -сед-/-сид- NGỒI (сосе́д).
"""

S = {}

# -------------------------------------------------------- начинать
S["начинать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">tiền tố, ở đây KHÔNG mang nghĩa riêng tách ra được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-чин-</span>'
    '<span class="hd-gloss">gốc BẮT ĐẦU — cùng gốc với <b>нача́ло</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp thể là <b>нача́ть</b> (bắt đầu xong một lần; <b>я начну́</b>). '
    'Đi với cách 4 (<i>начина́ть рабо́ту</i>) hoặc với một động từ nguyên thể.</div>'
    '<div class="hd-warn">Nguyên thể đứng sau luôn ở thể CHƯA hoàn thành: <b>начина́ть чита́ть</b>, '
    'không bao giờ <i>начинать прочитать</i>. Luật này đúng cho cả <b>конча́ть</b> và '
    '<b>продолжа́ть</b>.</div>'
    '<div class="hd-warn">Ai bắt đầu cái gì → <b>начина́ть</b>. Bản thân sự việc bắt đầu → thêm '
    '<b>-ся</b>: <b>Уро́к начина́ется в де́вять.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нача́ть</b> bắt đầu (HT) · <b>нача́ло</b> sự bắt đầu · '
    '<b>снача́ла</b> lúc đầu, từ đầu · <b>нача́льник</b> thủ trưởng</div>'
)

# -------------------------------------------------------- кончать
S["кончать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">конч-</span>'
    '<span class="hd-gloss">gốc KẾT THÚC — chính là <b>коне́ц</b>, <b>ц</b> hoá <b>ч</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đưa việc tới <b>коне́ц</b> ⇒ làm xong. Cặp thể: <b>ко́нчить</b>. '
    'Nguyên thể theo sau ở thể chưa hoàn thành, y như <b>начина́ть</b>.</div>'
    '<div class="hd-warn">Dùng trống không, không có tân ngữ, nói về người thì mang nghĩa tục '
    '(lên đỉnh). Nói "làm xong việc" người ta chuộng <b>зака́нчивать</b> / <b>зако́нчить</b>.</div>'
    '<div class="hd-warn">Thêm <b>-ся</b> = tự hết, cạn: <b>Де́ньги ко́нчились.</b> Hết tiền rồi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>коне́ц</b> phần cuối · <b>наконе́ц</b> cuối cùng thì · '
    '<b>коне́чно</b> tất nhiên · <b>зако́нчить</b> làm xong (HT)</div>'
)

# -------------------------------------------------------- конец
S["конец"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кон-</span>'
    '<span class="hd-gloss">gốc TẬN CÙNG, KẾT THÚC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ц</span>'
    '<span class="hd-gloss">đuôi danh từ giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng khuôn với <b>оте́ц → отца́</b>: chữ <b>е</b> trong <b>-ец</b> rơi mất khi '
    'thêm đuôi, trọng âm dồn về cuối — <b>конца́, концу́, концо́м</b>, số nhiều <b>концы́</b>.</div>'
    '<div class="hd-warn">Hai cụm phải thuộc: <b>в конце́</b> + cách 2 = vào cuối '
    '(<i>в конце́ ме́сяца</i>) · <b>в конце́ концо́в</b> = rốt cuộc, sau cùng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>конча́ть</b> kết thúc · <b>коне́чно</b> tất nhiên · '
    '<b>наконе́ц</b> cuối cùng thì · <b>бесконе́чный</b> vô tận</div>'
)

# -------------------------------------------------------- продолжать
S["продолжать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">xuyên qua, kéo tiếp về phía trước</span></div>'
    '<div class="hd-row"><span class="hd-piece">-долж-</span>'
    '<span class="hd-gloss">gốc DÀI — của <b>до́лгий</b>, <b>г</b> hoá <b>ж</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Kéo cho DÀI thêm ⇒ tiếp tục. Lắp ráp y hệt tiếng Anh <i>pro-long</i>. '
    'Cặp thể: <b>продо́лжить</b>. Nguyên thể theo sau ở thể chưa hoàn thành, như '
    '<b>начина́ть</b>: <i>продолжа́ть рабо́тать</i>.</div>'
    '<div class="hd-warn">Thêm <b>-ся</b> = tự kéo dài: <b>Фильм продолжа́ется два часа́.</b> '
    'Phim dài hai tiếng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>до́лгий</b> lâu, dài · <b>до́лго</b> lâu · '
    '<b>продо́лжить</b> tiếp tục (HT) · <b>продолже́ние</b> phần tiếp theo</div>'
)

# -------------------------------------------------------- открывать
S["открывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">tách ra, rời khỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-кры-</span>'
    '<span class="hd-gloss">gốc CHE, ĐẬY — như trong <b>откры́тка</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gỡ cái che ra ⇒ mở. Y như tiếng Anh <i>dis-cover</i>: gỡ nắp là '
    '"mở", gỡ màn bí mật là "phát hiện". Cặp thể <b>откры́ть</b> đổi <b>ы</b> thành <b>о</b>: '
    '<b>я откро́ю</b>.</div>'
    '<div class="hd-warn">Cửa hàng tự mở cửa → thêm <b>-ся</b>: <b>Магази́н открыва́ется в '
    'де́вять.</b> Đang mở → <b>Магази́н откры́т.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>закрыва́ть</b> đóng · <b>откры́тка</b> bưu thiếp · '
    '<b>откры́тие</b> sự khai trương, khám phá · <b>кры́ша</b> mái nhà</div>'
)

# -------------------------------------------------------- закрывать
S["закрывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">che kín, chắn lại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-кры-</span>'
    '<span class="hd-gloss">gốc CHE, ĐẬY</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Phủ kín lại ⇒ đóng, che. Là cặp đối của <b>открыва́ть</b>: cùng '
    'gốc <b>-кры-</b>, chỉ đổi tiền tố <b>от-</b> (bỏ ra) thành <b>за-</b> (đậy vào). '
    'Cặp thể <b>закры́ть</b>: <b>я закро́ю</b>.</div>'
    '<div class="hd-warn">Biển trước cửa hàng: <b>Закры́то</b> = đang đóng cửa. Cửa hàng tự '
    'đóng cửa lúc mấy giờ → <b>закрыва́ется</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>открыва́ть</b> mở · <b>закры́тый</b> đóng, kín · '
    '<b>кры́ша</b> mái nhà (cái che)</div>'
)

# -------------------------------------------------------- ключ
S["ключ"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được. Nhưng nó là gốc của cả họ "khoá vào / '
    'khoá ra" bên dưới.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chìa khoá ⇒ thứ mở ra lời giải: <i>ключ к успе́ху</i> (chìa khoá '
    'thành công). Hễ thêm đuôi là trọng âm nhảy ra đuôi: <b>ключа́, ключо́м</b>, số nhiều '
    '<b>ключи́</b> — y như <b>стол → стола́</b>.</div>'
    '<div class="hd-warn">Chìa khoá CỦA cái gì dùng <b>от</b> + cách 2, không dùng cách 2 trơn: '
    '<b>ключ от кварти́ры</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>включа́ть</b> bật (khoá vào mạch) · <b>выключа́ть</b> tắt · '
    '<b>ключево́й</b> then chốt · <b>исключе́ние</b> ngoại lệ</div>'
)

# -------------------------------------------------------- помогать
S["помогать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мог-</span>'
    '<span class="hd-gloss">gốc SỨC, CÓ THỂ — của <b>мочь</b> (<b>я могу́</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Góp cái sức mình có cho người khác. Cùng gốc với <b>по́мощь</b> — '
    'ở đó <b>г</b> đổi áo thành <b>щ</b>. Cặp thể <b>помо́чь</b> chia y như <b>мочь</b>: '
    '<b>помогу́, помо́жешь</b>.</div>'
    '<div class="hd-warn">Người được giúp ở CÁCH 3, không phải cách 4: <b>помога́ть ма́ме</b>, '
    '<b>Помоги́ мне!</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́мощь</b> sự giúp đỡ · <b>мочь</b> có thể · '
    '<b>помо́чь</b> giúp (HT) · <b>помо́щник</b> người trợ giúp</div>'
)

# -------------------------------------------------------- просить
S["просить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">прос-</span>'
    '<span class="hd-gloss">gốc XIN, THỈNH CẦU — của <b>вопро́с</b>, <b>спроси́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc với <b>спроси́ть</b> mà khác việc: <b>спроси́ть</b> là hỏi để BIẾT, '
    '<b>проси́ть</b> là xin, nhờ ai LÀM. Cặp thể: <b>попроси́ть</b>. Riêng ngôi "tôi" '
    '<b>с</b> hoá <b>ш</b>: <b>я прошу́</b>, các ngôi khác trọng âm lùi về gốc: '
    '<b>ты про́сишь</b>.</div>'
    '<div class="hd-warn">Nhờ AI làm gì: người ở cách 4 + nguyên thể — <b>проси́ть дру́га '
    'помо́чь</b>. Xin cái gì TỪ ai: <b>у</b> + cách 2 — <b>проси́ть у отца́ де́ньги</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>про́сьба</b> lời thỉnh cầu · <b>вопро́с</b> câu hỏi · '
    '<b>спроси́ть</b> hỏi · <b>попроси́ть</b> xin, nhờ (HT)</div>'
)

# -------------------------------------------------------- получать
S["получать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-луч-</span>'
    '<span class="hd-gloss">tiền tố + gốc cổ, nay không đứng riêng — học như một khối</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhận cái người khác GỬI, TRAO tới: <i>получа́ть письмо́</i>, '
    '<i>получа́ть зарпла́ту</i>. Tự tay cầm lấy thì là <b>брать</b>. '
    'Cặp thể: <b>получи́ть</b>.</div>'
    '<div class="hd-warn">Thêm <b>-ся</b> = làm ra được, thành: <b>У меня́ не получа́ется.</b> '
    'Mình làm mãi không được. · <b>Получи́лось!</b> Được rồi!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>получи́ть</b> nhận (HT) · <b>получа́ться</b> thành, ra được · '
    '<b>получа́тель</b> người nhận</div>'
)

# -------------------------------------------------------- решать
S["решать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">реш-</span>'
    '<span class="hd-gloss">gốc GỠ, CỞI (nút buộc)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gỡ một nút thắt: gỡ bài toán ⇒ GIẢI (<i>реша́ть зада́чу</i>), gỡ sự '
    'phân vân ⇒ QUYẾT ĐỊNH. Cặp thể <b>реши́ть</b> + nguyên thể = quyết làm gì: '
    '<i>Я реши́л учи́ть ру́сский.</i></div>'
    '<div class="hd-warn">⚠️ Mức tin: nghĩa "gỡ, cởi" là từ nguyên, không phải luật suy ra '
    'được. Nó khớp với <b>разреша́ть</b> "cho phép" = gỡ lệnh cấm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>реши́ть</b> giải, quyết định (HT) · <b>реше́ние</b> lời giải, '
    'quyết định · <b>разреша́ть</b> cho phép</div>'
)

# -------------------------------------------------------- задача
S["задача"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">tiền tố của <b>зада́ть</b> "giao, đặt ra"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-да-</span>'
    '<span class="hd-gloss">gốc CHO, TRAO — như <b>дать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ча</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái được đặt ra cho mình phải giải ⇒ bài toán, nhiệm vụ. Cùng khuôn '
    '<b>-да-ча</b> với <b>сда́ча</b> và <b>уда́ча</b>. Đi đôi với <b>реша́ть</b>: '
    '<i>реша́ть зада́чу</i> = giải bài toán.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>зада́ние</b>: <b>зада́ча</b> là vấn đề cần nghĩ để giải, '
    'mục tiêu; <b>зада́ние</b> là phần việc cụ thể được giao — <i>дома́шнее зада́ние</i> '
    'bài tập về nhà.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дать</b> cho · <b>зада́ть</b> giao, đặt (câu hỏi) · '
    '<b>зада́ние</b> bài được giao · <b>уда́ча</b> may mắn</div>'
)

# -------------------------------------------------------- сидеть
S["сидеть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сид-</span>'
    '<span class="hd-gloss">gốc NGỒI — biến thể <b>-сед-</b> trong <b>сосе́д</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể, lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Ấn-Âu với tiếng Anh <i>sit</i>, <i>seat</i>. Riêng ngôi "tôi" '
    '<b>д</b> hoá <b>ж</b>: <b>я сижу́</b>, còn lại giữ <b>д</b>: <b>ты сиди́шь</b>.</div>'
    '<div class="hd-warn"><b>сиде́ть</b> là ĐANG NGỒI (trạng thái). Động tác NGỒI XUỐNG là từ '
    'khác hẳn: <b>сади́ться</b> / <b>сесть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сосе́д</b> hàng xóm (người ngồi cạnh) · <b>сади́ться</b> ngồi '
    'xuống · <b>сесть</b> ngồi xuống (HT)</div>'
)

# -------------------------------------------------------- строить
S["строить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">стро-</span>'
    '<span class="hd-gloss">gốc XÂY, DỰNG, sắp đặt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dựng lên cho có hàng có lối: nhà cửa (<i>стро́ить дом</i>) lẫn '
    'thứ trừu tượng (<i>стро́ить пла́ны</i> = lập kế hoạch). Cặp thể <b>постро́ить</b> — '
    '<b>по-</b> chỉ đánh dấu xong, không thêm nghĩa. Bảng chia đều: '
    '<b>стро́ю, стро́ишь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>строи́тель</b> thợ xây · <b>строи́тельный</b> thuộc xây dựng · '
    '<b>постро́ить</b> xây xong (HT) · <b>стро́йка</b> công trường</div>'
)

# -------------------------------------------------------- опаздывать
S["опаздывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">tiền tố</span></div>'
    '<div class="hd-row"><span class="hd-piece">-позд-/-пазд-</span>'
    '<span class="hd-gloss">gốc MUỘN — của <b>по́здно</b>, <b>по́здний</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thành ra <b>по́здно</b> ⇒ đến muộn. Cặp thể là <b>опозда́ть</b>; khi '
    'thêm <b>-ыва-</b> gốc đổi <b>о</b> thành <b>а</b> — cùng kiểu <b>спроси́ть → '
    'спра́шивать</b>. <i>Я опа́здываю!</i> = mình đang trễ!</div>'
    '<div class="hd-warn">Muộn sự kiện, chuyến xe: <b>на</b> + cách 4 — <b>опа́здывать на '
    'рабо́ту</b>, <b>на по́езд</b>. Muộn hẹn với người: <b>к</b> + cách 3 — '
    '<b>к врачу́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́здно</b> muộn · <b>по́здний</b> muộn, khuya · '
    '<b>опозда́ть</b> đến muộn (HT) · <b>опозда́ние</b> sự đến trễ</div>'
)

# -------------------------------------------------------- вспоминать
S["вспоминать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вс-</span>'
    '<span class="hd-gloss">TRỒI LÊN, bật lên</span></div>'
    '<div class="hd-row"><span class="hd-piece">-помин-</span>'
    '<span class="hd-gloss">NHỚ — chính là <b>-помн-</b> của <b>по́мнить</b>, chèn thêm <b>и</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bạn cặp thể của <b>вспо́мнить</b> (sực nhớ ra): ở đây là đang lục lại '
    'trí nhớ, hoặc hay nhớ về. Đi với cách 4 hoặc <b>о</b> + cách 6: '
    '<i>вспомина́ть о де́тстве</i>.</div>'
    '<div class="hd-warn">Luật cả họ: thể chưa hoàn thành đổi <b>-мн-</b> thành <b>-мина-</b> — '
    '<b>вспо́мнить → вспомина́ть</b>, <b>запо́мнить → запомина́ть</b>, '
    '<b>напо́мнить → напомина́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́мнить</b> còn nhớ · <b>вспо́мнить</b> nhớ ra (HT) · '
    '<b>па́мять</b> trí nhớ · <b>воспомина́ние</b> hồi ức</div>'
)

# -------------------------------------------------------- запоминать
S["запоминать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">ghim lại cho chắc — như trong <b>записа́ть</b> ghi lại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-помин-</span>'
    '<span class="hd-gloss">NHỚ — <b>-помн-</b> chèn <b>и</b> (luật ở thẻ <b>вспомина́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">"Ghi" vào trí nhớ, như <b>записа́ть</b> ghi lên giấy ⇒ học thuộc: '
    '<i>запомина́ть слова́</i>. Cặp thể: <b>запо́мнить</b>.</div>'
    '<div class="hd-warn">Ba từ một gốc, ba việc khác nhau: <b>запомина́ть</b> = ĐƯA vào trí nhớ · '
    '<b>по́мнить</b> = vẫn CÒN giữ trong đó · <b>вспомина́ть</b> = LÔI ra lại.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́мнить</b> còn nhớ · <b>запо́мнить</b> ghi nhớ (HT) · '
    '<b>па́мять</b> trí nhớ · <b>напомина́ть</b> nhắc</div>'
)

# -------------------------------------------------------- чувствовать
S["чувствовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">чу́вств-</span>'
    '<span class="hd-gloss">chính là <b>чу́вство</b> — cảm giác</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ть</span>'
    '<span class="hd-gloss">đuôi biến danh từ thành động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Có <b>чу́вство</b> ⇒ cảm thấy. Đuôi <b>-ова-</b> khi chia đổi thành '
    '<b>-у-</b>: <b>я чу́вствую</b>, <b>ты чу́вствуешь</b>. Cặp thể: <b>почу́вствовать</b>.</div>'
    '<div class="hd-warn">Chữ <b>в</b> đầu tiên KHÔNG đọc: nghe như «чу́ствовать» — cùng luật '
    'với <b>здра́вствуйте</b>.</div>'
    '<div class="hd-warn">Cảm thấy trong người thế nào thì BẮT BUỘC có <b>себя́</b>: '
    '<b>Я чу́вствую себя́ хорошо́.</b> · <b>Как вы себя́ чу́вствуете?</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>чу́вство</b> cảm giác, tình cảm · <b>почу́вствовать</b> cảm thấy (HT) · '
    '<b>чувстви́тельный</b> nhạy cảm</div>'
)

# -------------------------------------------------------- готовый
S["готовый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гото́в-</span>'
    '<span class="hd-gloss">gốc SẴN SÀNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc của <b>гото́вить</b> (làm cho sẵn sàng, nấu). Dạng dài đứng trước '
    'danh từ = làm sẵn, thành phẩm: <i>гото́вая еда́</i> đồ ăn làm sẵn.</div>'
    '<div class="hd-warn">Nói "ai/cái gì ĐÃ SẴN SÀNG" thì dùng dạng ngắn: <b>Я гото́в</b> '
    '(nữ: <b>гото́ва</b>) · <b>Обе́д гото́в.</b> Sẵn sàng cho gì: <b>к</b> + cách 3 — '
    '<i>гото́в к экза́мену</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гото́вить</b> nấu, chuẩn bị · <b>пригото́вить</b> nấu xong · '
    '<b>подгото́вить</b> chuẩn bị trước · <b>подгото́вка</b> sự chuẩn bị</div>'
)

# -------------------------------------------------------- важный
S["важный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">важ-</span>'
    '<span class="hd-gloss">SỨC NẶNG, TRỌNG LƯỢNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái gì có sức nặng thì quan trọng — y như chữ "trọng" trong '
    '"quan trọng". Trạng từ là <b>ва́жно</b> đã học. Nói về người thì còn nghĩa '
    '"ra vẻ quan trọng, oai vệ".</div>'
    '<div class="hd-warn">Dạng ngắn không suy thẳng được: giống đực chèn <b>е</b> — '
    '<b>ва́жен</b>, giống cái trọng âm nhảy ra đuôi — <b>важна́</b>; còn <b>ва́жно</b>, '
    '<b>ва́жны</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ва́жно</b> quan trọng (trạng từ) · <b>ва́жность</b> tầm quan trọng · '
    '<b>уважа́ть</b> tôn trọng · <b>уваже́ние</b> sự tôn trọng</div>'
)

V = {
    # Trùng "mời" với звать (k01) và приглашать (k71) — bỏ "mời", giữ nghĩa xin/nhờ.
    "просить": "xin, nhờ, yêu cầu, cầu xin",
    # Trùng trọn "nhớ, ghi nhớ" với помнить (k48) — bỏ "nhớ" trơn.
    "запоминать": "ghi nhớ, học thuộc",
    "готовый": "sẵn sàng, đã chuẩn bị xong, làm sẵn",
}
