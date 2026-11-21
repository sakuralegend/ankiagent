# -*- coding: utf-8 -*-
"""k156 — qualities: tính từ chất lượng + vài danh từ trừu tượng, gom theo bốn gốc.

Chỗ cần nhất quán trong lô:
(1) -лич- MẶT, DIỆN MẠO (лицо́, ц → ч): ли́чный · разли́чный · отли́чный — khớp thẻ cũ отли́чно.
(2) -мож- CÓ THỂ (мочь, г → ж), воз- không còn nghĩa riêng: возмо́жный · возмо́жность —
    khớp возмо́жно, мо́жно, невозмо́жно.
(3) -со́б- BẢN THÂN (себя́): со́бственный · осо́бенный — khớp осо́бый (о- = giới từ «về»).
(4) осно́в- NỀN MÓNG: осно́ва — khớp основно́й, основа́ть; ба́за tách nghĩa với осно́ва.
Khớp thẻ cũ: -равн- (сравни́ть), -луч- (слу́чай), -об-ход- (необходи́мо), -вяз- (обяза́тельно).
Dạng ngắn: chỉ ра́вный (trọng âm nhảy) và обя́занный (mất một н, dùng gần như chỉ ở dạng ngắn)
được nói; các tính từ còn lại chèn -е- đúng quy tắc ⇒ bỏ. со́бственный có hai dạng ngắn giống
đực nhưng dạng ngắn của nó gần như không dùng ⇒ cố ý bỏ.
Họ hàng cố ý vắng: абсолю́тный (từ mượn, chỉ có trạng từ абсолю́тно — đã đưa vào Cách nhớ).
Bẫy họ hàng đã gạt: сла́ва ↔ славя́нский (từ nguyên tranh cãi), ли́ния ↔ поликли́ника (oan).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "абсолютный": "tuyệt đối, hoàn toàn",                              # bỏ «hoàn toàn» — trùng чи́стый (k42, đã nạp)
    "различный": "khác nhau, đa dạng, đủ loại",             # bỏ «khác nhau» — trùng ра́зный (k63, đã nạp)
    "материал": "vật liệu, chất liệu, tư liệu, vải",         # bỏ «tài liệu» — trùng докуме́нт (k89); gloss data/fabric/cloth
    "основа": "nền tảng, nền móng, điều cơ bản",            # bỏ «cơ sở» — gỡ trong lô với ба́за; gloss fundamentals/basics
    "база": "căn cứ, cơ sở, kho",                           # bỏ «nền tảng» — gỡ trong lô với осно́ва; không lấy «trạm» (trùng ста́нция)
    "повод": "lý do, cớ, duyên cớ",                         # bỏ «dịp» — trùng слу́чай (k103, đã nạp)
    "необходимый": "cần thiết, thiết yếu, không thể thiếu",   # bỏ «cần thiết» — trùng ну́жный (k05, đã nạp); gloss unavoidable
    "особенный": "đặc biệt, lạ thường, khác lạ",                      # bỏ «đặc biệt» — trùng осо́бый (k121); «khác thường» trùng необыкнове́нный
    "великолепный": "tuyệt đẹp, tráng lệ, lộng lẫy, tuyệt diệu",       # bỏ «tuyệt đẹp» — trùng прекра́сный (k42, đã nạp)
    "отличный": "tuyệt vời, xuất sắc, rất tốt, khác với",              # bỏ «tuyệt vời, xuất sắc» — trùng прекра́сный (k42); gloss different (from)
}

# ----------------------------------------------------------------- равный
S["равный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">равн-</span>'
    '<span class="hd-gloss">BẰNG NHAU</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc của <b>сравни́ть</b> «đặt cạnh nhau xem có bằng không». Dạng ngắn '
    'trừ giống đực, trọng âm nhảy xuống đuôi: <b>ра́вен</b> · <b>равна́</b> · <b>равно́</b> · <b>равны́</b> — '
    'chính <b>равно́</b> là chữ «bằng» trong toán: <b>два плюс два равно́ четырём</b>.</div>'
    '<div class="hd-warn"><b>всё равно́</b> = sao cũng được, dù sao thì cũng vậy: '
    '<b>Мне всё равно́.</b> Tôi sao cũng được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сравни́ть</b> so sánh · <b>сра́внивать</b> so sánh · '
    '<b>ра́венство</b> sự bình đẳng</div>'
)

# ----------------------------------------------------------------- случайный
S["случайный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">CÙNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-луч-ай-</span>'
    '<span class="hd-gloss">gốc cổ TRÚNG, GẶP PHẢI — chính là <b>слу́чай</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tính từ của <b>слу́чай</b> «chuyện tự dưng xảy tới» ⇒ tình cờ, ngẫu '
    'nhiên: <b>случа́йная встре́ча</b> cuộc gặp tình cờ. Trạng từ: <b>случа́йно</b>.</div>'
    '<div class="hd-warn">Hỏi lịch sự: <b>Вы случа́йно не зна́ете…?</b> = Anh có biết… không '
    '(nghĩa đen «tình cờ anh có biết»).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>слу́чай</b> trường hợp · <b>случи́ться</b> xảy ra · '
    '<b>случа́ться</b> xảy ra · <b>случа́йно</b> tình cờ</div>'
)

# ----------------------------------------------------------------- собственный
S["собственный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со́б-</span>'
    '<span class="hd-gloss">BẢN THÂN — cùng gốc <b>себя́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ств-енн-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thuộc về bản thân» ⇒ của riêng mình, nhấn mạnh hơn <b>свой</b>: '
    '<b>свой со́бственный дом</b> căn nhà của chính mình.</div>'
    '<div class="hd-warn">Thuật ngữ ngữ pháp: <b>и́мя со́бственное</b> = danh từ riêng '
    '(Москва́, Ива́н).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>себя́</b> bản thân · <b>осо́бый</b> đặc biệt · '
    '<b>со́бственность</b> quyền sở hữu, tài sản · <b>со́бственно</b> nói đúng ra</div>'
)

# ----------------------------------------------------------------- абсолютный
S["абсолютный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">абсолю́т-</span>'
    '<span class="hd-gloss">mượn Latin <i>absolutus</i> — Anh <i>absolute</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>absolute</i> gắn đuôi <b>-ный</b>. Hay gặp nhất ở trạng '
    'từ <b>абсолю́тно</b> = hoàn toàn: <b>Абсолю́тно ве́рно!</b> Hoàn toàn đúng!</div>'
)

# ----------------------------------------------------------------- личный
S["личный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">лич-</span>'
    '<span class="hd-gloss">MẶT, DIỆN MẠO — <b>лицо́</b>, trước <b>-н-</b> đổi <b>ц → ч</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thuộc về gương mặt một người» ⇒ của riêng người đó, cá nhân: '
    '<b>ли́чная жизнь</b> đời tư.</div>'
    '<div class="hd-warn"><b>ли́чно</b> = đích thân, riêng tôi: <b>Я ли́чно про́тив.</b> '
    'Cá nhân tôi thì phản đối.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лицо́</b> mặt · <b>ли́чность</b> nhân cách · '
    '<b>отли́чный</b> rất tốt · <b>разли́чный</b> đủ loại</div>'
)

# ----------------------------------------------------------------- различный
S["различный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span>'
    '<span class="hd-gloss">TẢN RA MỖI HƯỚNG (như <b>ра́зный</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лич-</span>'
    '<span class="hd-gloss">MẶT, DIỆN MẠO — <b>лицо́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Mỗi cái một diện mạo» ⇒ khác nhau, đủ loại: '
    '<b>разли́чные ви́ды спо́рта</b> đủ các môn thể thao.</div>'
    '<div class="hd-warn">Nghĩa gần trùng <b>ра́зный</b>, nhưng <b>разли́чный</b> trang trọng '
    'hơn — hay gặp trong văn viết, báo chí.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>различа́ть</b> phân biệt · <b>разли́чие</b> sự khác biệt · '
    '<b>ли́чный</b> cá nhân · <b>отли́чный</b> rất tốt</div>'
)

# ----------------------------------------------------------------- материал
S["материал"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ: mượn nguyên khối, Anh <i>material</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa trải như tiếng Anh: vật liệu xây dựng, vải may, và «tư liệu» '
    'cho một bài viết: <b>материа́лы конфере́нции</b> tư liệu hội nghị. Trọng âm ở '
    '<b>а́</b> cuối.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>материа́льный</b> vật chất, tài chính · <b>мате́рия</b> vật chất, '
    'vải</div>'
)

# ----------------------------------------------------------------- объект
S["объект"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">объ-</span>'
    '<span class="hd-gloss">Latin <i>ob-</i> «chắn trước»; <b>ъ</b> tách phụ âm khỏi <b>е</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́кт</span>'
    '<span class="hd-gloss">Latin <i>-iectum</i> «được ném ra»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>object</i>. <b>предме́т</b> là bản dịch từng mảnh của cùng '
    'chữ Latin đó. Nghĩa Nga rộng hơn: cả công trình, cơ sở: <b>строи́тельный объе́кт</b> '
    'công trường.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>объекти́вный</b> khách quan · <b>объекти́в</b> ống kính · '
    '<b>субъе́кт</b> chủ thể · <b>предме́т</b> đồ vật</div>'
)

# ----------------------------------------------------------------- линия
S["линия"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ: mượn Latin <i>linea</i>, Anh <i>line</i>. Đuôi <b>-ия</b> '
    '⇒ giống cái.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mọi «đường»: nét kẻ, tuyến xe, đường dây: <b>ли́ния метро́</b> tuyến '
    'tàu điện ngầm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лине́йка</b> thước kẻ</div>'
)

# ----------------------------------------------------------------- слава
S["слава"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">слав-</span>'
    '<span class="hd-gloss">TIẾNG TĂM, VINH QUANG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mảnh <b>-слав</b> nằm trong rất nhiều tên Nga: <b>Яросла́в</b>, '
    '<b>Вячесла́в</b>, <b>Станисла́в</b> — và <b>Сла́ва</b> chính là tên gọi tắt của họ.</div>'
    '<div class="hd-warn"><b>Сла́ва Бо́гу!</b> = Tạ ơn Chúa! May quá! — câu cửa miệng hằng '
    'ngày, không mang màu tôn giáo.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сла́вный</b> lừng lẫy, dễ mến · <b>просла́вить</b> làm nổi '
    'danh</div>'
)

# ----------------------------------------------------------------- основа
S["основа"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">осно́в-</span>'
    '<span class="hd-gloss">NỀN MÓNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái nằm dưới đỡ mọi thứ: <b>осно́вы грамма́тики</b> những điều cơ bản '
    'của ngữ pháp. Nghĩa xưa là hàng sợi dọc căng sẵn trên khung cửi — dệt gì cũng dệt lên nó.</div>'
    '<div class="hd-warn"><b>на осно́ве</b> + cách 2 = dựa trên: <b>на осно́ве фа́ктов</b> dựa '
    'trên sự thật.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>основно́й</b> cơ bản · <b>основа́ть</b> thành lập · '
    '<b>осно́вывать</b> thành lập · <b>основа́тель</b> người sáng lập</div>'
)

# ----------------------------------------------------------------- база
S["база"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ: mượn Hy Lạp <i>basis</i>, Anh <i>base</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Như <i>base</i>: nơi đóng quân, kho, trạm — và cái nền để dựng lên. '
    'Khác <b>осно́ва</b>: <b>ба́за</b> thường là một CHỖ cụ thể, <b>осно́ва</b> là nền móng '
    'trừu tượng.</div>'
    '<div class="hd-warn"><b>ба́за да́нных</b> = cơ sở dữ liệu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ба́зовый</b> cơ bản, nền</div>'
)

# ----------------------------------------------------------------- повод
S["повод"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вод</span>'
    '<span class="hd-gloss">DẪN — gốc của <b>води́ть</b>, <b>вести́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thứ «dẫn» tới một việc ⇒ cớ, lý do: <b>по́вод для ра́дости</b> lý do để '
    'vui. Khác <b>причи́на</b> (nguyên nhân thật): <b>по́вод</b> là cái cớ châm ngòi.</div>'
    '<div class="hd-warn"><b>по по́воду</b> + cách 2 = về việc, liên quan đến: <b>по по́воду '
    'рабо́ты</b> về chuyện công việc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>води́ть</b> dẫn · <b>вести́</b> dẫn · <b>перево́д</b> bản dịch</div>'
)

# ----------------------------------------------------------------- необходимый
S["необходимый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не-</span>'
    '<span class="hd-gloss">không</span></div>'
    '<div class="hd-row"><span class="hd-piece">-об-ход-</span>'
    '<span class="hd-gloss">ĐI VÒNG — <b>обходи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́м-ый</span>'
    '<span class="hd-gloss">«có thể bị …» (như <b>люби́мый</b> được yêu)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Không thể đi vòng tránh» ⇒ không thể thiếu, thiết yếu: '
    '<b>необходи́мые докуме́нты</b> giấy tờ bắt buộc phải có. Mạnh hơn <b>ну́жный</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>необходи́мо</b> cần phải · <b>необходи́мость</b> sự cần thiết · '
    '<b>обходи́ть</b> đi vòng · <b>ходи́ть</b> đi</div>'
)

# ----------------------------------------------------------------- возможный
S["возможный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">воз-</span>'
    '<span class="hd-gloss">tiền tố, ở từ này không còn nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мож-</span>'
    '<span class="hd-gloss">CÓ THỂ — gốc của <b>мочь</b> (<b>г → ж</b>: <b>мо́жешь</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Có thể xảy ra, có thể làm được»: <b>возмо́жный вариа́нт</b> một phương '
    'án khả thi. Trạng từ <b>возмо́жно</b> = có lẽ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>возмо́жность</b> khả năng · <b>мо́жно</b> được phép · '
    '<b>невозмо́жно</b> không thể · <b>мочь</b> có thể</div>'
)

# ----------------------------------------------------------------- обязанный
S["обязанный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-(в)яз-</span>'
    '<span class="hd-gloss"><b>об-</b> quanh + <b>вяз-</b> BUỘC (<b>вяза́ть</b>), <b>в</b> rụng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-нн-ый</span>'
    '<span class="hd-gloss">«bị …» (phân từ bị động)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Bị buộc vào» ⇒ có nghĩa vụ. Gần như chỉ dùng dạng ngắn, và dạng ngắn '
    'mất một <b>н</b>: <b>обя́зан · обя́зана · обя́заны</b>.</div>'
    '<div class="hd-warn"><b>Я обя́зан</b> + nguyên mẫu = tôi có nghĩa vụ phải · <b>Я вам '
    'обя́зан</b> (cách 3) = tôi mang ơn anh.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обяза́тельно</b> nhất định · <b>обя́занность</b> nghĩa vụ · '
    '<b>связь</b> mối liên hệ · <b>вяза́ть</b> buộc, đan</div>'
)

# ----------------------------------------------------------------- особенный
S["особенный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">giới từ <b>о</b> «về»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-со́б-</span>'
    '<span class="hd-gloss">BẢN THÂN — cùng gốc <b>себя́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-енн-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Anh em của <b>осо́бый</b>, nghĩa gần trùng: «riêng một mình nó» ⇒ khác '
    'hẳn số còn lại. Trạng từ <b>осо́бенно</b> = nhất là.</div>'
    '<div class="hd-warn"><b>Ничего́ осо́бенного.</b> = Không có gì đặc biệt — câu trả lời hằng '
    'ngày, luôn dùng <b>осо́бенный</b>, không dùng осо́бый.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>осо́бый</b> đặc biệt · <b>осо́бенно</b> nhất là · '
    '<b>осо́бенность</b> nét riêng · <b>со́бственный</b> của riêng mình</div>'
)

# ----------------------------------------------------------------- великолепный
S["великолепный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вели́к-о-</span>'
    '<span class="hd-gloss">LỚN — <b>вели́кий</b>, <b>-о-</b> nối</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ле́п-</span>'
    '<span class="hd-gloss">gốc cổ ĐẸP, VỪA VẶN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đẹp một cách lớn lao» ⇒ tráng lệ, lộng lẫy: <b>великоле́пный дворе́ц</b> '
    'cung điện tráng lệ. Nói chuyện thường, <b>великоле́пно!</b> = tuyệt quá!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вели́кий</b> vĩ đại · <b>неле́пый</b> vô lý, lố bịch '
    '(«không vừa vặn»)</div>'
)

# ----------------------------------------------------------------- возможность
S["возможность"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">возмо́жн-</span>'
    '<span class="hd-gloss">CÓ THỂ — <b>возмо́жный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span>'
    '<span class="hd-gloss">tính từ → danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái có thể» ⇒ khả năng, cơ hội: <b>У меня́ нет возмо́жности</b> + '
    'nguyên mẫu = tôi không có điều kiện để… Số nhiều <b>возмо́жности</b> = năng lực, tiềm năng.</div>'
    '<div class="hd-warn"><b>с ограни́ченными возмо́жностями</b> = khuyết tật (cách nói lịch '
    'sự, nghĩa đen «khả năng bị hạn chế»).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>возмо́жный</b> khả thi · <b>возмо́жно</b> có lẽ · '
    '<b>невозмо́жно</b> không thể · <b>мочь</b> có thể</div>'
)

# ----------------------------------------------------------------- отличный
S["отличный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">TÁCH RA KHỎI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лич-</span>'
    '<span class="hd-gloss">MẶT, DIỆN MẠO — <b>лицо́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Mặt mình tách hẳn khỏi đám đông» ⇒ khác biệt ⇒ nổi trội ⇒ xuất sắc: '
    '<b>отли́чная иде́я</b> ý hay tuyệt.</div>'
    '<div class="hd-warn">Nghĩa gốc vẫn dùng: <b>отли́чный от</b> + cách 2 = khác với: '
    '<b>отли́чный от други́х</b> khác với những cái khác.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отли́чно</b> xuất sắc · <b>отлича́ться</b> khác biệt · '
    '<b>отли́чник</b> học sinh giỏi · <b>ли́чный</b> cá nhân</div>'
)

B = {
    "docbangmat": 87,
    "loitubat": 1,   # равный: viết «dạng ngắn trọng âm nhảy xuống đuôi» — sai với ра́вен (giống đực đứng yên); đã sửa «trừ giống đực»
    "nguonsai": 9,   # 8 cờ BAT THUONG dạng ngắn là đúng quy tắc (chèn -е-): случайный, абсолютный, личный, различный, возможный, особенный, великолепный, отличный — không chép; CACH DUNG великолепный là chữ Gruzia (ჩინებული) — bỏ
    "baolen": [
        "V cần duyệt — rút gọn phía lô vì bên kia ĐÃ NẠP, nên mất nghĩa cốt lõi: необходимый bỏ «cần thiết» (ну́жный) · отличный bỏ «tuyệt vời, xuất sắc» (прекра́сный) · великолепный bỏ «tuyệt đẹp» (прекра́сный) · абсолютный còn đúng «tuyệt đối» (чи́стый giữ «hoàn toàn») · различный bỏ «khác nhau» (ра́зный) · материал bỏ «tài liệu» (докуме́нт) · повод bỏ «dịp» (слу́чай). Muốn giữ nghĩa gốc thì phải rút phía thẻ đã nạp — ngoài quyền lô.",
        "Trùng nghĩa gần như không gỡ được: особенный ↔ осо́бый (k121) là đồng nghĩa thật, cùng adj; «khác thường» lại trùng необыкнове́нный ⇒ đề bài còn «lạ thường, khác lạ», gượng. Đề nghị luồng chính/user quyết.",
        "Trong lô: база «căn cứ, cơ sở, kho» · основа «nền tảng, nền móng, điều cơ bản». Bỏ «trạm» khỏi база vì trùng ста́нция. Mô phỏng do_va_cham (đọc Anki, áp V lô này): 0 cụm trùng còn lại dính từ k156.",
        "Không chắc: nouns.csv khai «про́вод», tôi tin «dây điện» là прово́д (số nhiều провода́) — đã né bằng перево́д trong Họ hàng của повод; luồng chính nên soi lại mục đó trong nouns.csv.",
        "Từ nguyên viết KHÔNG gắn «Mức tin» vì tôi tin là chuẩn (Vasmer): осно́ва nghĩa xưa sợi dọc khung cửi (gloss có «warp») · великоле́пный -ле́п- ĐẸP/VỪA VẶN, cùng gốc неле́пый · объе́кт chẻ Latin ob- + iectum. Luồng chính muốn chặt hơn thì hạ mức tin.",
        "Khuôn о- của осо́бенный theo thẻ cũ осо́бый (giới từ о «về»), khớp gợi ý luồng chính. Không nhắc nghĩa «dây cương» của по́вод. абсолю́тный cố ý không có Họ hàng (từ mượn; абсолю́тно đưa vào Cách nhớ).",
    ],
}
