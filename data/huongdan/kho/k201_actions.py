# -*- coding: utf-8 -*-
"""k201 — actions (lô trộn): sáu cặp thể + họ хран- + vài tính từ lạc chủ đề.

Chỗ cần nhất quán trong lô:
(1) охраня́ть / телохрани́тель: о- QUANH + -хран- CẤT GIỮ — khớp chẻ охра́на [k151], охра́нник [k162].
(2) отнести́ / относи́ть: tiền tố + нести́ ⇒ HT, tiền tố + носи́ть ⇒ CHT — luật trải ở thẻ отнести́,
    thẻ относи́ть dẫn chiếu. Khớp chẻ относи́ться [k123].
(3) влия́ть: в- + -ли- (лить) — khớp chẻ влия́ние [k167].
(4) соедини́ть: со- + -еди́н- — khớp присоедини́ться [k171]; испо́лнить: ис- + -полн- — khớp испо́лниться [k145].
(5) огля́дываться / огляну́ться: -гляд- khớp гляде́ть [k157].
(6) буди́ть: gốc буд- THỨC — KHÁC gốc быть/бу́ду (ô đỏ nói rõ). разби́ть là máy báo oan.
Họ hàng: mọi thẻ đều có.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "отнести": "mang đến, đem đi, chuyển tới, xếp vào, quy cho",    # gloss: to attribute / to classify (as)
    "относить": "mang đi, đem đến, chuyển đến, xếp vào, quy cho",   # gloss: to attribute / to classify
    "исполнить": "thực hiện, thi hành, hoàn thành, biểu diễn",      # gloss: to perform / to play (a role) / to sing
    "сырой": "sống, chưa nấu chín, ẩm, thô",                        # gloss: crude / unprocessed
}

# --------------------------------------------------------------------- будить
S["будить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">буд-</span>'
    '<span class="hd-gloss">THỨC, TỈNH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho ai THỨC ⇒ đánh thức, đi thẳng với cách 4: <b>буди́ть сы́на</b>. '
    'Ngôi «tôi» д→ж, các ngôi khác trọng âm lùi về đầu: <b>бужу́</b>, <b>бу́дишь</b>, <b>бу́дит</b>. '
    'Cặp HT: <b>разбуди́ть</b>.</div>'
    '<div class="hd-warn">Luôn là đánh thức NGƯỜI KHÁC. Tự mình thức dậy là '
    '<b>просыпа́ться</b> / <b>просну́ться</b>.</div>'
    '<div class="hd-warn"><b>бу́дишь</b> (bạn đánh thức) đọc gần như y hệt <b>бу́дешь</b> '
    '(bạn sẽ — của <b>быть</b>). Hai gốc KHÁC nhau, chỉ ngữ cảnh tách được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>разбуди́ть</b> đánh thức (HT) · <b>буди́льник</b> đồng hồ báo thức</div>'
)

# --------------------------------------------------------------------- разбудить
S["разбудить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span>'
    '<span class="hd-gloss">ở đây gần như chỉ đổi sang THỂ HOÀN THÀNH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-буд-и́ть</span>'
    '<span class="hd-gloss">ĐÁNH THỨC — <b>буди́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đánh thức xong, người kia đã tỉnh. Chia y hệt <b>буди́ть</b>: '
    '<b>разбужу́</b>, <b>разбу́дишь</b> (tương lai). Nghĩa bóng: khơi dậy — '
    '<b>разбуди́ть интере́с</b> khơi dậy hứng thú.</div>'
    '<div class="hd-warn"><b>Разбуди́ меня́ в семь.</b> = Đánh thức tôi lúc 7 giờ nhé. '
    'Tự thức dậy thì là <b>просну́ться</b>, không phải từ này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>буди́ть</b> đánh thức (CHT) · <b>буди́льник</b> đồng hồ báo thức</div>'
)

# --------------------------------------------------------------------- отнести
S["отнести"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">RỜI ĐI, ra chỗ khác</span></div>'
    '<div class="hd-row"><span class="hd-piece">-нес-ти́</span>'
    '<span class="hd-gloss">MANG (cầm tay, đi bộ) — <b>нести́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mang ra chỗ khác ⇒ đem đi, mang tới: <b>отнести́ кни́гу в библиоте́ку</b>. '
    'Nghĩa bóng «mang về một nhóm» ⇒ xếp vào, quy cho: <b>отнести́ к</b> + cách 3. '
    'Quá khứ giống đực KHÔNG có -л, như <b>нёс</b>: <b>отнёс</b>, <b>отнесла́</b>; '
    'tương lai <b>отнесу́</b>, <b>отнесёшь</b>.</div>'
    '<div class="hd-warn">Tiền tố + <b>нести́</b> (một chiều) ⇒ HOÀN THÀNH <b>отнести́</b>; '
    'tiền tố + <b>носи́ть</b> (nhiều chiều) ⇒ CHƯA HT <b>относи́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>относи́ть</b> (CHT) · <b>нести́</b> mang · '
    '<b>относи́ться</b> có thái độ, thuộc về · <b>отноше́ние</b> quan hệ</div>'
)

# --------------------------------------------------------------------- относить
S["относить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">RỜI ĐI, ra chỗ khác</span></div>'
    '<div class="hd-row"><span class="hd-piece">-нос-и́ть</span>'
    '<span class="hd-gloss">MANG (nhiều chiều) — <b>носи́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chưa HT của <b>отнести́</b> (luật cặp thể ở thẻ đó). Ngôi «tôi» с→ш, '
    'các ngôi khác trọng âm lùi: <b>отношу́</b>, <b>отно́сишь</b>. Cũng có nghĩa xếp vào: '
    '<b>относи́ть к</b> + cách 3. Thêm <b>-ся</b> là ra <b>относи́ться</b> «có thái độ với».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отнести́</b> (HT) · <b>носи́ть</b> mang · '
    '<b>относи́ться</b> có thái độ · <b>отноше́ние</b> quan hệ</div>'
)

# --------------------------------------------------------------------- влиять
S["влиять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ли-</span>'
    '<span class="hd-gloss">RÓT, CHẢY — gốc của <b>лить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ть</span>'
    '<span class="hd-gloss">đuôi động từ, chia đều <b>влия́ю</b>, <b>влия́ешь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Chảy vào» người khác ⇒ ảnh hưởng — y hệt tiếng Anh <i>in-fluence</i>.</div>'
    '<div class="hd-warn">Ảnh hưởng LÊN cái gì → <b>на</b> + cách 4: <b>влия́ть на здоро́вье</b>. '
    'Không dùng cách 4 trơn như «affect something».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>повлия́ть</b> (HT) · <b>влия́ние</b> sự ảnh hưởng · '
    '<b>влия́тельный</b> có thế lực · <b>лить</b> rót</div>'
)

# --------------------------------------------------------------------- повлиять
S["повлиять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">chỉ đổi sang THỂ HOÀN THÀNH, không thêm nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-влия́ть</span>'
    '<span class="hd-gloss">ẢNH HƯỞNG — <b>влия́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đã gây ảnh hưởng, có kết quả: <b>Э́то повлия́ло на моё реше́ние</b> = '
    'Điều đó đã ảnh hưởng tới quyết định của tôi. Vẫn đòi <b>на</b> + cách 4 như <b>влия́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>влия́ть</b> (CHT) · <b>влия́ние</b> sự ảnh hưởng · '
    '<b>влия́тельный</b> có thế lực</div>'
)

# --------------------------------------------------------------------- охранять
S["охранять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">QUANH, bao lấy</span></div>'
    '<div class="hd-row"><span class="hd-piece">-хран-</span>'
    '<span class="hd-gloss">CẤT GIỮ — như <b>храни́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành, chia đều <b>охраня́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giữ vòng quanh cho khỏi mất ⇒ canh gác, bảo vệ; đi thẳng với cách 4: '
    '<b>охраня́ть грани́цу</b> canh biên giới, <b>охраня́ть приро́ду</b> bảo vệ thiên nhiên. '
    'Khác <b>защища́ть</b> (chống đỡ khi bị tấn công) như ở thẻ <b>охра́на</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>охра́на</b> sự canh gác · <b>охра́нник</b> bảo vệ · '
    '<b>телохрани́тель</b> vệ sĩ · <b>храни́ть</b> cất giữ · <b>сохрани́ть</b> lưu lại</div>'
)

# --------------------------------------------------------------------- телохранитель
S["телохранитель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тел-о-</span>'
    '<span class="hd-gloss">THÂN THỂ — <b>те́ло</b>, -о- là nguyên âm nối</span></div>'
    '<div class="hd-row"><span class="hd-piece">-хран-</span>'
    '<span class="hd-gloss">CANH GIỮ — như <b>охраня́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́тель</span>'
    '<span class="hd-gloss">NGƯỜI LÀM việc đó — như <b>учи́тель</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người canh giữ thân thể» ⇒ vệ sĩ — ghép đúng từng mảnh như tiếng Anh '
    '<i>body-guard</i>. Đuôi <b>-тель</b> là giống ĐỰC dù tận cùng bằng -ь.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>те́ло</b> thân thể · <b>охраня́ть</b> canh gác · '
    '<b>охра́нник</b> bảo vệ · <b>храни́ть</b> cất giữ</div>'
)

# --------------------------------------------------------------------- соединить
S["соединить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-еди́н-</span>'
    '<span class="hd-gloss">MỘT — dạng cổ của <b>оди́н</b>, như <b>еди́ный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đưa CÙNG nhau thành MỘT ⇒ nối, ghép: <b>соедини́ть</b> A <b>с</b> B (cách 5). '
    'Qua điện thoại là nối máy: <b>Соедини́те меня́ с дире́ктором</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>соединя́ть</b> (CHT) · <b>присоедини́ться</b> gia nhập · '
    '<b>объедини́ть</b> hợp nhất · <b>Соединённые Шта́ты</b> Hoa Kỳ</div>'
)

# --------------------------------------------------------------------- соединять
S["соединять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-еди́н-</span>'
    '<span class="hd-gloss">CÙNG + MỘT — như <b>соедини́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành (-и́ть → -я́ть)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chưa HT của <b>соедини́ть</b>, chia đều <b>соединя́ю</b>. Hay dùng cho thứ '
    'nối thường trực: <b>Мост соединя́ет два бе́рега</b> = Cây cầu nối hai bờ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>соедини́ть</b> (HT) · <b>соедине́ние</b> sự nối, mối nối · '
    '<b>еди́ный</b> thống nhất · <b>присоединя́ться</b> gia nhập</div>'
)

# --------------------------------------------------------------------- исполнить
S["исполнить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ис-</span>'
    '<span class="hd-gloss">(= <b>из-</b>) RA, cho tới hết</span></div>'
    '<div class="hd-row"><span class="hd-piece">-по́лн-</span>'
    '<span class="hd-gloss">ĐẦY — <b>по́лный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Làm đầy cho tới hết» ⇒ thực hiện trọn — y hệt tiếng Anh <i>ful-fil</i> '
    '(fill full): <b>испо́лнить обеща́ние</b> giữ lời hứa, <b>испо́лнить жела́ние</b> thực hiện điều ước. '
    'Và biểu diễn: <b>испо́лнить пе́сню</b>.</div>'
    '<div class="hd-warn"><b>вы́полнить</b> = làm xong việc, nhiệm vụ, kế hoạch; <b>испо́лнить</b> '
    'nghiêng về lời hứa, điều ước, vai diễn, bài hát.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>исполня́ть</b> (CHT) · <b>испо́лниться</b> thành hiện thực · '
    '<b>исполни́тель</b> người biểu diễn · <b>по́лный</b> đầy</div>'
)

# --------------------------------------------------------------------- исполнять
S["исполнять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ис-по́лн-</span>'
    '<span class="hd-gloss">RA + ĐẦY — như <b>испо́лнить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành (-ить → -я́ть)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chưa HT của <b>испо́лнить</b>; trọng âm dời ra đuôi: '
    '<b>испо́лнить</b> → <b>исполня́ть</b>, chia đều <b>исполня́ю</b>. Rất hay gặp ở nghĩa biểu diễn: '
    '<b>Пе́сню исполня́ет хор</b> = Bài hát do dàn hợp xướng trình bày.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>испо́лнить</b> (HT) · <b>исполня́ться</b> thành hiện thực · '
    '<b>исполни́тель</b> người biểu diễn · <b>по́лный</b> đầy</div>'
)

# --------------------------------------------------------------------- оглядываться
S["оглядываться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">QUANH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-гля́д-</span>'
    '<span class="hd-gloss">NHÌN — như <b>гляде́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть-ся</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành + <b>-ся</b> (chính mình)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Xoay mình nhìn quanh, ngoảnh lại: <b>огля́дываться наза́д</b>. '
    'Chia đều <b>огля́дываюсь</b>. Cụm hay gặp: <b>не огля́дываясь</b> = không ngoảnh lại.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>огляну́ться</b> (HT) · <b>гляде́ть</b> nhìn · '
    '<b>взгляд</b> cái nhìn · <b>вы́глядеть</b> trông có vẻ</div>'
)

# --------------------------------------------------------------------- оглянуться
S["оглянуться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-гля-</span>'
    '<span class="hd-gloss">QUANH + NHÌN (д rụng trước -ну-)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ну-</span>'
    '<span class="hd-gloss">MỘT CÁI, tức thì — như <b>гля́нуть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть-ся</span>'
    '<span class="hd-gloss">+ <b>-ся</b> (chính mình)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ngoảnh lại MỘT CÁI ⇒ HT của <b>огля́дываться</b>. '
    'Trọng âm lùi từ ngôi «bạn»: <b>огляну́сь</b>, <b>огля́нешься</b>.</div>'
    '<div class="hd-warn">Ngoảnh lại nhìn AI → <b>на</b> + cách 4: <b>Она́ огляну́лась на меня́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>огля́дываться</b> (CHT) · <b>гля́нуть</b> liếc · '
    '<b>гляде́ть</b> nhìn · <b>взгляд</b> cái nhìn</div>'
)

# --------------------------------------------------------------------- сопротивляться
S["сопротивляться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">tiền tố, nghĩa đã mờ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-проти́в-</span>'
    '<span class="hd-gloss">CHỐNG — <b>про́тив</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-л-я́ть-ся</span>'
    '<span class="hd-gloss">в→вл như <b>лови́ть → ловлю́</b>, + <b>-ся</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đứng chống lại ⇒ kháng cự, chống cự. Chia đều <b>сопротивля́юсь</b>.</div>'
    '<div class="hd-warn">Chống lại AI/CÁI GÌ → cách 3 trơn, KHÔNG cần <b>про́тив</b>: '
    '<b>сопротивля́ться врагу́</b>, <b>сопротивля́ться боле́зни</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>про́тив</b> chống lại · <b>сопротивле́ние</b> sự kháng cự · '
    '<b>проти́вник</b> đối thủ</div>'
)

# --------------------------------------------------------------------- трещина
S["трещина"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">трещ-</span>'
    '<span class="hd-gloss">NỨT — từ <b>треск</b> (ск→щ)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ина</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỗ nứt toác ra ⇒ vết nứt: <b>тре́щина в стене́</b> vết nứt trên tường. '
    'Gốc là <b>треск</b> (tiếng nứt răng rắc); thêm <b>-ина</b> thì ск→щ — phép biến âm gặp khắp nơi. '
    'Nghĩa bóng: rạn nứt trong quan hệ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>треск</b> tiếng răng rắc · <b>тре́снуть</b> nứt toác · '
    '<b>треща́ть</b> kêu răng rắc</div>'
)

# --------------------------------------------------------------------- гладкий
S["гладкий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">глад-</span>'
    '<span class="hd-gloss">NHẴN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-ий</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mặt nhẵn, mịn: <b>гла́дкая ко́жа</b> da mịn; vải trơn không hoa văn cũng là '
    '<b>гла́дкий</b>. Trạng từ <b>гла́дко</b> = suôn sẻ: <b>Всё прошло́ гла́дко</b>.</div>'
    '<div class="hd-warn">Dạng ngắn giống đực chèn -о-: <b>гла́док</b>; giống cái trọng âm ra đuôi: '
    '<b>гладка́</b>. So sánh hơn: <b>гла́же</b> (дк → ж).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гла́дить</b> là (quần áo), vuốt ve — làm cho NHẴN · '
    '<b>гла́дко</b> suôn sẻ</div>'
)

# --------------------------------------------------------------------- металлический
S["металлический"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">металл-</span>'
    '<span class="hd-gloss">KIM LOẠI — <b>мета́лл</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ческ-ий</span>'
    '<span class="hd-gloss">≈ tiếng Anh <i>-ic</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><i>metal-lic</i> ⇒ <b>металли́ческий</b>, chép thẳng, giữ hai л. '
    'Đuôi <b>-и́ческий</b> luôn mang trọng âm nên kéo nó khỏi <b>мета́лл</b> — '
    'cùng khuôn <b>электри́ческий</b>, <b>истори́ческий</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мета́лл</b> kim loại</div>'
)

# --------------------------------------------------------------------- всеобщий
S["всеобщий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">все-</span>'
    '<span class="hd-gloss">TẤT CẢ — <b>весь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́бщ-ий</span>'
    '<span class="hd-gloss">CHUNG — <b>о́бщий</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Chung của tất cả» ⇒ toàn thể: <b>всео́бщие вы́боры</b> tổng tuyển cử, '
    '<b>всео́бщее внима́ние</b> sự chú ý của mọi người. <b>о́бщий</b> có thể chỉ chung của hai người; '
    '<b>всео́бщий</b> là của TẤT CẢ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>о́бщий</b> chung · <b>весь</b> tất cả · <b>о́бщество</b> xã hội · '
    '<b>вообще́</b> nói chung</div>'
)

# --------------------------------------------------------------------- сырой
S["сырой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сыр-</span>'
    '<span class="hd-gloss">SỐNG, ẨM</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ mang trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một gốc, hai nghĩa: CHƯA NẤU (<b>сыро́е мя́со</b> thịt sống) và ẨM '
    '(<b>сыра́я пого́да</b> trời ẩm). Trạng từ: <b>На у́лице сы́ро</b> = Ngoài trời ẩm ướt.</div>'
    '<div class="hd-warn">Dạng ngắn giống đực <b>сыр</b> trùng mặt chữ với <b>сыр</b> phô mai; '
    'giống cái trọng âm ra đuôi: <b>сыра́</b>, còn lại <b>сы́ро</b>, <b>сы́ры</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: theo từ nguyên, <b>сыр</b> phô mai cũng từ gốc «sống, tươi» này — '
    'là từ nguyên, không phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сырьё</b> nguyên liệu thô · <b>сыре́ть</b> bị ẩm</div>'
)

# --------------------------------------------------------------------- густой
S["густой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">густ-</span>'
    '<span class="hd-gloss">ĐẶC, DÀY ĐẶC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ mang trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhiều thứ chen sít nhau: <b>густо́й лес</b> rừng rậm, <b>густы́е во́лосы</b> tóc dày, '
    '<b>густо́й тума́н</b> sương dày đặc; chất lỏng thì là đặc: <b>густо́й суп</b>. '
    'So sánh hơn ст→щ: <b>гу́ще</b>, như <b>просто́й → про́ще</b>.</div>'
    '<div class="hd-warn">«Dày» về BỀ DÀY (sách dày, tường dày) là <b>то́лстый</b>, không phải '
    '<b>густо́й</b>: <b>то́лстая кни́га</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гу́сто</b> dày đặc · <b>сгу́сток</b> cục đông</div>'
)

B = {
    "docbangmat": 118,
    "loitubat": 1,
    "nguonsai": 0,
    "baolen": [
        "Lỗi tự bắt (1): сопротивля́ться — ví dụ biến âm в→вл ban đầu ghi люби́ть → люблю́ (đó là б→бл); đã đổi thành лови́ть → ловлю́.",
        "Va chạm nghĩa: mô phỏng do_va_cham (chỉ đọc Anki, áp V lô này) = 0 cụm trùng đủ 4 badge dính k201. Bỏ lọc badge còn 7, đều được badge tách: cặp thể (буди́ть/разбуди́ть, влия́ть/повлия́ть, соедини́ть/соединя́ть, испо́лнить ⊇ исполня́ть), từ loại (мета́лл n / металли́ческий adj, влия́ние n), «chống lại» сопротивля́ться v ↔ боро́ться v ↔ про́тив — riêng боро́ться/сопротивля́ться cùng v: dòng đầy đủ vẫn khác nên không phải va chạm.",
        "V cần duyệt: отнести́ + относи́ть thêm «xếp vào, quy cho» (gloss attribute/classify); испо́лнить thêm «biểu diễn» (gloss perform/sing/play a role — исполня́ть vốn đã có); сыро́й thêm «thô» (gloss crude/unprocessed: сыра́я нефть dầu thô).",
        "Không chắc (đã viết, có rào): (a) сыр phô mai cùng gốc сыро́й — để ô ⚠️ Mức tin; (b) тре́щина ← треск với ск→щ — từ nguyên chuẩn nhưng là từ nguyên; (c) раз- trong разбуди́ть ghi «gần như chỉ đổi thể»; (d) со- trong сопротивля́ться ghi «nghĩa đã mờ» thay vì bịa nghĩa; (e) бу́дишь ≈ бу́дешь đọc gần như trùng (е/и không nhấn sau phụ âm mềm đều nhược hoá) — đúng với phát âm chuẩn hiện đại.",
        "Họ hàng: không thẻ nào vắng. металли́ческий chỉ có một mục (мета́лл) — cố ý, không kéo thêm từ ít gặp.",
    ],
}
