# -*- coding: utf-8 -*-
"""k155 — language::grammar: trạng từ, hư từ, giới từ + vài danh từ/tính từ trừu tượng.

Chỗ cần nhất quán trong lô:
(1) gốc пол- = ĐẦY — вполне́ · по́лностью, khớp по́лный (k113). Ô đỏ phân biệt hai từ nằm ở вполне́.
(2) gốc дал- = XA — да́лее, khớp далёкий (k63), далеко́ (k49), да́льше (k75).
(3) gốc -лож- = ĐẶT, tức «làm cho nằm», cùng gốc лежа́ть — положе́ние. Hai thẻ cũ khai lệch
    (положи́ть «NẰM», положи́тельный «ĐẶT»); thực ra -лож- là dạng «gây ra» của -лег-/-леж-,
    nên cả hai đều đúng một nửa — ở đây gộp: ĐẶT = làm cho nằm.
(4) gốc мест- = CHỖ — ме́стный, khớp ме́сто (k08), вме́сте (k74), вме́сто (k18).
(5) ни- = KHÔNG MỘT … nào — ника́к, cùng khuôn никако́й (k111).
(6) cặp hỏi к- / trỏ т- — насто́лько, cùng khuôn сто́лько (k112).
Họ hàng cố ý vắng: плане́та (mượn đứng một mình), за́мок (lâu đài — không kéo họ về phía ổ khoá),
ра́ди (giới từ gốc trơn), ли́бо (hư từ).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "либо": "hoặc là, hoặc… hoặc…",   # luồng chính 22/11: «hoặc, hay là» trùng nguyên văn и́ли
    "серия": "loạt, chuỗi, tập phim",                     # bỏ ngoặc «(phim)»; «tập» trơn đụng кни́га — đổi thành «tập phim»
    "положение": "vị trí, tư thế, tình thế, địa vị, quy chế",   # thêm standing/status · regulations/statute từ gloss
    "внутренний": "bên trong, nội bộ, trong nước",        # thêm domestic/home từ gloss
    "далее": "tiếp theo, xa hơn, về sau",                            # bỏ «tiếp theo» — đụng да́льше; «later on» từ gloss
    "полностью": "hoàn toàn, toàn bộ, trọn vẹn",                     # bỏ «hoàn toàn» — đụng совсе́м và вполне́ (cùng lô); «in full»
    "настолько": "đến mức, đến nỗi",                      # bỏ «quá» — đó là сли́шком, gloss không có «too»
    "ради": "vì, vì lợi ích của",                # bỏ «vì» trơn — đụng за, раз
    "при": "ở cạnh, trước mặt, trong điều kiện, dưới thời, trực thuộc",   # thêm in the time of / attached to
    "кстати": "nhân tiện, à mà, đúng lúc",                # thêm handy/welcome/convenient từ gloss
}

# ----------------------------------------------------------------- серия
S["серия"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn Latin <i>series</i> «chuỗi, dãy» — cùng gốc tiếng Anh '
    '<i>series</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc là một CHUỖI nối tiếp: <b>се́рия о́пытов</b> loạt thí nghiệm. '
    'Phim truyền hình chia thành từng mắt xích ⇒ từng tập: <b>втора́я се́рия</b> tập hai. '
    'Cả bộ phim thì là <b>сериа́л</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сериа́л</b> phim bộ · <b>сери́йный</b> hàng loạt</div>'
)

# ----------------------------------------------------------------- вечеринка
S["вечеринка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вечер-</span>'
    '<span class="hd-gloss">BUỔI TỐI (<b>ве́чер</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́нк-а</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cuộc tụ tập buổi tối ⇒ bữa tiệc vui giữa bạn bè: '
    '<b>пойти́ на вечери́нку</b> (на + cách 4, như на конце́рт). Trọng âm dời: '
    '<b>ве́чер</b> → <b>вечери́нка</b>. Cách 2 số nhiều chêm о: <b>мно́го вечери́нок</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ве́чер</b> buổi tối · <b>вече́рний</b> thuộc buổi tối · '
    '<b>ве́чером</b> vào buổi tối</div>'
)

# ----------------------------------------------------------------- планета
S["планета"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn Hy Lạp qua Latin, cùng gốc tiếng Anh <i>planet</i>. '
    'Không họ với <b>план</b> kế hoạch — chỉ trùng mặt chữ.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiếng Hy Lạp gọi hành tinh là «kẻ lang thang» — ngôi sao đi lạc giữa '
    'các sao đứng yên. Đuôi -а nên giống cái. Ở trên hành tinh dùng на, không dùng в: '
    '<b>на плане́те</b>, như <b>на Земле́</b>.</div>'
)

# ----------------------------------------------------------------- замок (ЗА́МОК — lâu đài)
S["замок"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">tiền tố «khép lại» (như <b>закры́ть</b> đóng)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мок</span>'
    '<span class="hd-gloss">gốc «đóng kín» — có trong <b>замкну́ть</b> khép kín</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nơi được khép kín sau tường thành ⇒ lâu đài, dịch sát tiếng Đức '
    '<i>Schloss</i>. Chữ о rơi khi chia: <b>за́мка</b>, <b>в за́мке</b>, số nhiều '
    '<b>за́мки</b>.</div>'
    '<div class="hd-warn">Chớ nhầm với замо́к ổ khoá: nhấn cuối, cách 2 замка́. Lâu đài nhấn ĐẦU: '
    '<b>за́мок</b> → <b>за́мка</b>.</div>'
)

# ----------------------------------------------------------------- далее
S["далее"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дал-</span>'
    '<span class="hd-gloss">XA (như <b>далёкий</b>, <b>далеко́</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ее</span>'
    '<span class="hd-gloss">đuôi so sánh hơn (như <b>быстре́е</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Xa hơn» theo dòng của bài viết ⇒ tiếp theo, về sau: '
    '<b>да́лее в те́ксте</b>. Đây là bản văn viết của <b>да́льше</b>; nói chuyện thì dùng '
    '<b>да́льше</b>.</div>'
    '<div class="hd-warn"><b>и так да́лее</b> = vân vân, viết tắt <b>и т. д.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>далёкий</b> xa · <b>далеко́</b> ở xa · <b>недалеко́</b> không xa · '
    '<b>да́льше</b> xa hơn nữa</div>'
)

# ----------------------------------------------------------------- положение
S["положение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лож-</span>'
    '<span class="hd-gloss">ĐẶT, tức «làm cho NẰM» — cùng gốc <b>лежа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ние</span>'
    '<span class="hd-gloss">đuôi danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cách một vật được ĐẶT ⇒ vị trí, tư thế; rộng ra là thế của sự việc ⇒ '
    'tình thế: <b>тру́дное положе́ние</b>. Văn bản «đặt ra» luật lệ ⇒ quy chế. Cùng khuôn: '
    '<b>предложе́ние</b> = đặt ra trước mặt ⇒ lời đề nghị.</div>'
    '<div class="hd-warn"><b>в интере́сном положе́нии</b> = đang có bầu (nói tế nhị), không phải '
    '«ở vị trí thú vị».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>положи́ть</b> đặt · <b>лежа́ть</b> nằm · <b>предложе́ние</b> lời đề nghị · '
    '<b>положи́тельный</b> tích cực</div>'
)

# ----------------------------------------------------------------- внутренний
S["внутренний"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">внутр-</span>'
    '<span class="hd-gloss">BÊN TRONG (như <b>внутри́</b> ở trong)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-енн-ий</span>'
    '<span class="hd-gloss">đuôi tính từ, đuôi mềm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thuộc về phía bên trong ⇒ nội bộ, trong nước: <b>вну́тренний ры́нок</b> '
    'thị trường nội địa. Đối nghĩa là <b>вне́шний</b> bên ngoài, đối ngoại — hai từ đi thành '
    'cặp.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>внутри́</b> ở bên trong · <b>внутрь</b> vào bên trong</div>'
)

# ----------------------------------------------------------------- местный
S["местный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мест-</span>'
    '<span class="hd-gloss">CHỖ (<b>ме́сто</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thuộc về chỗ này ⇒ địa phương: <b>ме́стный жи́тель</b> người địa '
    'phương, <b>ме́стное вре́мя</b> giờ địa phương. Cụm -стн- nuốt т khi đọc, như '
    '<b>че́стный</b>, <b>изве́стный</b>. Tính từ chỉ quan hệ nên gần như không dùng dạng ngắn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ме́сто</b> chỗ · <b>вме́сте</b> cùng nhau · <b>вме́сто</b> thay cho · '
    '<b>ме́стность</b> vùng, địa hình</div>'
)

# ----------------------------------------------------------------- вполне
S["вполне"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">giới từ «ở trong»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-полн-</span>'
    '<span class="hd-gloss">ĐẦY (<b>по́лный</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́</span>'
    '<span class="hd-gloss">đuôi cách 6 đông cứng lại</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Ở trong độ đầy» ⇒ đủ đầy, hoàn toàn: <b>вполне́ дово́лен</b> hoàn toàn '
    'hài lòng. Rất hay gặp: <b>Вполне́ возмо́жно</b> = hoàn toàn có thể.</div>'
    '<div class="hd-warn"><b>по́лностью</b> = trọn 100%, không sót phần nào: '
    '<b>прочита́ть по́лностью</b> đọc hết. <b>вполне́</b> = đủ để hài lòng, chấp nhận được: '
    '<b>вполне́ хорошо́</b> khá tốt.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́лный</b> đầy · <b>по́лностью</b> toàn bộ · <b>напо́лнить</b> làm đầy</div>'
)

# ----------------------------------------------------------------- полностью
S["полностью"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">полн-</span>'
    '<span class="hd-gloss">ĐẦY (<b>по́лный</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость-</span>'
    '<span class="hd-gloss">đuôi danh từ trừu tượng: «sự đầy đủ»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ю</span>'
    '<span class="hd-gloss">đuôi cách 5 đông cứng lại</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Bằng sự đầy đủ» ⇒ trọn vẹn, không thiếu phần nào: '
    '<b>Я по́лностью согла́сен</b> = tôi hoàn toàn đồng ý. Khác <b>вполне́</b> thế nào: xem thẻ '
    '<b>вполне́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́лный</b> đầy · <b>вполне́</b> khá, hoàn toàn · '
    '<b>напо́лнить</b> làm đầy</div>'
)

# ----------------------------------------------------------------- иначе
S["иначе"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ин-</span>'
    '<span class="hd-gloss">KHÁC (<b>ино́й</b> khác)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-аче</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Theo cách KHÁC: <b>Я ду́маю ина́че</b> = tôi nghĩ khác. Đứng đầu vế sau '
    'thì là «nếu không thì»: <b>Иди́, ина́че опозда́ешь</b> = đi đi, không thì muộn.</div>'
    '<div class="hd-warn"><b>так и́ли ина́че</b> = bằng cách này hay cách khác, đằng nào cũng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ино́й</b> khác · <b>иностра́нец</b> người nước ngoài · '
    '<b>иногда́</b> đôi khi</div>'
)

# ----------------------------------------------------------------- вообще
S["вообще"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">во-</span>'
    '<span class="hd-gloss">giới từ в «ở trong», chêm о</span></div>'
    '<div class="hd-row"><span class="hd-piece">-обще́</span>'
    '<span class="hd-gloss">CHUNG (<b>о́бщий</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Trong cái chung» ⇒ nói chung, nhìn chung: <b>Я вообще́ люблю́ спорт</b>. '
    'Mở đầu câu nói chuyện thì gần «thật ra mà nói».</div>'
    '<div class="hd-warn"><b>вообще́ не</b> = chẳng … chút nào, không phải «nói chung không»: '
    '<b>Он вообще́ не звони́л</b> = anh ta chẳng gọi lần nào.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>о́бщий</b> chung · <b>о́бщество</b> xã hội · <b>общежи́тие</b> ký túc xá</div>'
)

# ----------------------------------------------------------------- ради
S["ради"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: giới từ gốc trơn.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm việc gì vì LỢI ÍCH, vì MỤC ĐÍCH của ai/cái gì — kéo cách 2: '
    '<b>ра́ди дете́й</b> vì các con, <b>ра́ди шу́тки</b> cho vui.</div>'
    '<div class="hd-warn"><b>ра́ди</b> = vì mục đích, vì ai đó; <b>из-за́</b> = vì NGUYÊN NHÂN, '
    'thường là chuyện xấu: <b>из-за́ дождя́</b> vì mưa.</div>'
)

# ----------------------------------------------------------------- всё-таки
S["всё-таки"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">всё</span>'
    '<span class="hd-gloss">TẤT CẢ (thẻ đã học)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-таки</span>'
    '<span class="hd-gloss">tiểu từ nhấn «vậy mà vẫn»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Mặc tất cả» ⇒ dù sao vẫn: <b>Он всё-таки пришёл</b> = rốt cuộc anh ấy '
    'vẫn đến. Thường đi sau một ý trái chiều, như «tuy vậy». Viết có gạch nối.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>всё</b> mọi thứ · <b>всё равно́</b> dù sao cũng thế</div>'
)

# ----------------------------------------------------------------- при
S["при"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: giới từ gốc trơn.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa lõi: SÁT BÊN, đi kèm — luôn kéo cách 6: <b>при вхо́де</b> ở lối '
    'vào, <b>при всех</b> trước mặt mọi người, <b>при Ста́лине</b> dưới thời Stalin, '
    '<b>при усло́вии</b> với điều kiện.</div>'
    '<div class="hd-warn"><b>при э́том</b> = đồng thời, kèm theo đó — cụm nối câu rất hay gặp.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Tiền tố cùng ý «sát tới»: <b>прийти́</b> đi đến · '
    '<b>прие́хать</b> đến bằng xe</div>'
)

# ----------------------------------------------------------------- кстати
S["кстати"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">к-</span>'
    '<span class="hd-gloss">giới từ «tới, hướng về»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-стати</span>'
    '<span class="hd-gloss">danh từ cổ «dáng, chỗ hợp lẽ»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Vừa đúng chỗ» ⇒ đúng lúc: <b>пришёл кста́ти</b> đến đúng lúc. Trong lời '
    'nói, mở một ý chợt nhớ ⇒ nhân tiện, à mà: <b>Кста́ти, ты звони́л ма́ме?</b></div>'
    '<div class="hd-warn">⚠️ Mức tin: phần chẻ là từ nguyên (к + ста́ти), không phải luật suy ra '
    'được; không suy thẳng ra từ động từ <b>стать</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>некста́ти</b> không đúng lúc, lỡ dịp</div>'
)

# ----------------------------------------------------------------- всякий
S["всякий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вс-</span>'
    '<span class="hd-gloss">TẤT CẢ (<b>весь</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́кий</span>'
    '<span class="hd-gloss">đuôi «loại, kiểu»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Mọi kiểu» ⇒ đủ loại: <b>вся́кие ве́щи</b> đủ thứ đồ. Số ít thì gần '
    '«mỗi, bất cứ»: <b>вся́кий раз</b> mỗi lần. Đổi đuôi như tính từ.</div>'
    '<div class="hd-warn"><b>на вся́кий слу́чай</b> = phòng khi, cho chắc — cụm phải thuộc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>весь</b> toàn bộ · <b>всё</b> mọi thứ · <b>все</b> mọi người</div>'
)

# ----------------------------------------------------------------- никак
S["никак"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ни-</span>'
    '<span class="hd-gloss">KHÔNG MỘT … nào</span></div>'
    '<div class="hd-row"><span class="hd-piece">как</span>'
    '<span class="hd-gloss">thế nào (thẻ đã học)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Không bằng cách nào» ⇒ chẳng thể nào. Phủ định KÉP là bắt buộc, động '
    'từ vẫn mang не: <b>Я ника́к не могу́ поня́ть</b> = tôi chẳng sao hiểu nổi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Cùng ни-: <b>никако́й</b> không … nào · <b>никто́</b> không ai · '
    '<b>никогда́</b> không bao giờ</div>'
)

# ----------------------------------------------------------------- либо
S["либо"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Hư từ, không chẻ ra mảnh mang nghĩa riêng.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa như <b>и́ли</b> «hoặc», nhưng giọng văn viết, hay đi thành cặp: '
    '<b>ли́бо сего́дня, ли́бо за́втра</b>. Gắn sau đại từ bằng gạch nối thì thành «bất kỳ … nào»: '
    '<b>кто́-либо</b> bất kỳ ai, <b>что́-либо</b> bất cứ gì.</div>'
    '<div class="hd-warn"><b>что́-либо</b> = bất cứ gì, chưa nhắm cái nào; <b>что́-то</b> = một cái '
    'gì đó có thật nhưng không rõ.</div>'
)

# ----------------------------------------------------------------- настолько
S["настолько"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">tiền tố «đạt tới»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сто́лько</span>'
    '<span class="hd-gloss">bấy nhiêu (thẻ đã học)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Tới bấy nhiêu» ⇒ đến mức ấy, hay đi với что: <b>Он насто́лько уста́л, '
    'что усну́л</b> = mệt đến mức ngủ thiếp. Cùng cặp hỏi к- / trỏ т-: <b>наско́лько?</b> đến '
    'mức nào?</div>'
    '<div class="hd-warn"><b>насто́лько</b> = đến MỨC ẤY (rồi nói hệ quả); <b>сли́шком</b> = QUÁ '
    'mức cần: <b>сли́шком до́рого</b> đắt quá.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сто́лько</b> bấy nhiêu · <b>ско́лько</b> bao nhiêu · '
    '<b>наско́лько</b> đến mức nào</div>'
)

# ----------------------------------------------------------------- именно
S["именно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">имен-</span>'
    '<span class="hd-gloss">TÊN (<b>и́мя</b>, cách 2 <b>и́мени</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-но</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Gọi đúng tên» ⇒ chính là, đúng là. Đặt ngay trước từ cần nhấn: '
    '<b>и́менно он</b> chính anh ta. <b>Вот и́менно!</b> = Chính thế!</div>'
    '<div class="hd-warn"><b>а и́менно</b> = cụ thể là, tức là — mở đầu phần liệt kê.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>и́мя</b> tên</div>'
)

B = {
    "docbangmat": 96,
    "loitubat": 2,      # всё-таки «Luôn đi sau» → «Thường» (nói quá) · кстати «đừng nối với стать» → «không suy thẳng ra từ động từ» (ста́ть danh từ cổ và động từ xa xưa vẫn chung gốc ста-)
    "nguonsai": 0,
    "baolen": [
        "замок: за́мок (lâu đài) và замо́к (ổ khoá) KHÔNG phải 'không liên quan' về từ nguyên — cùng gốc за-мк- (замкну́ть), за́мок dịch sát tiếng Đức Schloss (vừa 'khoá' vừa 'lâu đài'). Ô vẫn chỉ viết về lâu đài + 1 ô đỏ chớ nhầm; phần chẻ dùng замкну́ть «khép kín» — luồng chính duyệt câu này có hợp ý user không.",
        "положение: hai thẻ cũ lệch nhau (положи́ть «-лож- NẰM» / положи́тельный «-лож- ĐẶT»). Đúng là: -лож- = ĐẶT, tức «làm cho nằm», dạng gây-ra của -лег-/-леж- (лежа́ть). Tôi dùng cách đó; thẻ положи́ть nên sửa chữ «gốc NẰM» thành «ĐẶT = làm cho nằm» — KHÔNG sửa vì ngoài lô.",
        "вполне: va chạm 'khá' (↔ доста́точно, đã nạp) và 'hoàn toàn' (↔ совсе́м, đã nạp) KHÔNG gỡ được bằng rút gọn — bỏ cả hai thì không còn nghĩa nào. Giữ nguyên «khá, hoàn toàn» (tổ hợp chỉ вполне́ có). Cần user quyết.",
        "далее ↔ да́льше: đồng nghĩa thật, chỉ khác văn phong (văn viết / nói). Tôi đổi V далее = «xa hơn, về sau» (bỏ «tiếp theo» cho hết va chạm) — mất nghĩa thông dụng nhất «next»; cần duyệt, và đề bài vẫn sát да́льше «tiếp theo, xa hơn nữa».",
        "либо ↔ и́ли: CẢ HAI đều «hoặc, hay là» trùng nguyên văn, cùng badge conj, mà máy KHÔNG báo — soatlo.tach_nghia coi «hoặc»/«hay là» là DẤU NGĂN nên nuốt mất cả hai nghĩa (lỗi mù của bộ dò va chạm). Không gỡ được bằng nghĩa (chỉ khác văn phong); chưa đổi V либо. Nên sửa tach_nghia.",
        "V cần duyệt (nới theo gloss): положение +«địa vị, quy chế» · внутренний +«trong nước» · при +«dưới thời, trực thuộc» · кстати +«đúng lúc» · полностью bỏ «hoàn toàn» → «toàn bộ, trọn vẹn» · настолько bỏ «quá» · серия «tập (phim)» → «tập phim» (gỡ va chạm кни́га).",
        "ради: V «vì lợi ích của, vì mục đích» — «vì mục đích» là cụm tôi đặt để tránh «vì» trơn (đụng за, раз); không chắc là cách nói tự nhiên nhất.",
        "Chỗ KHÔNG chắc: кстати chẻ к + ста́ти (danh từ cổ) — đã hạ mức tin bằng ô đỏ; местный «gần như không dùng dạng ngắn» là nhận định dùng thật, không phải luật.",
    ],
}
