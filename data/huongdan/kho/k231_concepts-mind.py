# -*- coding: utf-8 -*-
"""k231 — concepts::mind: nhận thức, tính nết (lười, ít nói, kiên trì, dí dỏm) và từ mượn chính trị – pháp luật.

Chỗ cần nhất quán trong lô:
(1) познава́ть / позна́ть: по- nghĩa mờ + зна- BIẾT; -ва- rơi ở hiện tại — khớp признава́ть [k170], узнава́ть [k128].
(2) насто́йчивый: на- LÊN TRÊN, đè lên + стой- ĐỨNG — khớp наста́ивать [k196].
(3) предрассу́док: пред- TRƯỚC + рас- TÁCH RA từng phần + суд- XÉT — khớp рассужда́ть [k210].
(4) инспе́кция: ин- VÀO TRONG + спект- NHÌN — khớp инспе́ктор [k163].
(5) бесце́нный: цен- GIÁ [k86, k138]; разноцве́тный: разн- [k63, k197] + цвет- MÀU [k109].
Họ hàng không vắng ở thẻ nào.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "разноцветный": "nhiều màu, đủ màu sắc",                         # «sặc sỡ» là пёстрый, gloss không có
    "престижный": "danh giá, uy tín",                                # «sang trọng» là luxurious, nới rộng
    "напрасно": "vô ích, uổng công, vô cớ",                          # «toi công» → «uổng công»: thôi bọc trọn зря [k161]
    "легальный": "hợp pháp, đúng luật",                              # «chính thức» là официальный, «công khai» là открытый
    "криминальный": "mang tính tội phạm, hình sự",                   # «đầy tệ nạn» nới rộng; «tội phạm» trơ là danh từ преступник
    "инспекция": "cuộc thanh tra, sự thanh tra, cuộc kiểm tra",      # «đoàn thanh tra»: gloss chỉ có inspection
    "остроумный": "dí dỏm, hóm hỉnh, nhanh trí, sắc sảo, tài tình",  # THIẾU quick-witted / ingenious
    "предрассудок": "thành kiến, định kiến, điều mê tín",            # «mê tín» trơ lẫn tính từ
    "стимул": "động lực, sự khuyến khích, sự kích thích",            # «kích thích» trơ là động từ
    "познавать": "nhận thức, tìm hiểu, hiểu rõ, trải qua, nếm trải",  # chung dãy cặp thể; «khám phá» là открывать; THIẾU experience / taste
    "познать": "nhận thức, tìm hiểu, hiểu rõ, trải qua, nếm trải",    # như trên
    "претендовать": "đòi quyền, yêu sách, nhắm tới, ứng cử, tự cho là",  # «đòi hỏi» là требовать; THIẾU be a candidate / claim to be
    "молчаливый": "ít nói, lặng lẽ, kín tiếng, ngầm",                # THIẾU tacit / unspoken
    "ленивый": "lười, lười biếng, lười nhác",                        # «uể oải» là вялый, gloss chỉ có lazy
    "настойчивый": "kiên trì, bền bỉ, dai dẳng, khăng khăng",        # «cố chấp» là упрямый; insistent = khăng khăng
}

# --------------------------------------------------------------------- разноцветный
S["разноцветный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">разн-о-</span>'
    '<span class="hd-gloss">KHÁC NHAU — <b>ра́зный</b> (<i>раз-</i> tản ra mỗi hướng) + nguyên âm nối</span></div>'
    '<div class="hd-row"><span class="hd-piece">-цве́т-</span>'
    '<span class="hd-gloss">MÀU — <b>цвет</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Những màu khác nhau» ⇒ nhiều màu: <b>разноцве́тные шары́</b> bóng bay đủ màu. '
    'Dạng ngắn giống đực chen <i>е</i>: <b>разноцве́тен</b>.</div>'
    '<div class="hd-warn"><b>цветно́й</b> = có màu (đối lập đen trắng), một màu cũng được; '
    '<b>разноцве́тный</b> phải từ hai màu trở lên.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ра́зный</b> khác nhau · <b>цвет</b> màu · <b>одноцве́тный</b> một màu, trơn màu · '
    '<b>разнообра́зный</b> đa dạng</div>'
)

# --------------------------------------------------------------------- престижный
S["престижный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">прести́ж-</span>'
    '<span class="hd-gloss">UY TÍN, thanh thế — <b>прести́ж</b>, mượn Pháp <i>prestige</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>prestigious</i>: CÓ được nó thì người ta nể — '
    '<b>прести́жный университе́т</b> đại học danh giá, <b>прести́жная рабо́та</b> công việc danh giá. '
    'Dạng ngắn giống đực chen <i>е</i>: <b>прести́жен</b>.</div>'
    '<div class="hd-warn">Tả trường, nghề, giải thưởng, khu nhà. Còn NGƯỜI có uy tín, được nể trọng thì nói '
    '<b>уважа́емый</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прести́ж</b> uy tín, thanh thế · <b>непрести́жный</b> không danh giá</div>'
)

# --------------------------------------------------------------------- бесценный
S["бесценный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бес-</span>'
    '<span class="hd-gloss">KHÔNG — <b>без</b> (<i>з → с</i> trước <i>ц</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-це́н-</span>'
    '<span class="hd-gloss">GIÁ, GIÁ TRỊ — <b>цена́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ ⇒ hai chữ <i>н</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">KHÔNG định GIÁ nổi ⇒ vô giá, đúng hình ảnh của <i>priceless</i>: '
    '<b>бесце́нный пода́рок</b> món quà vô giá. Dạng ngắn giống đực chen <i>е</i>: <b>бесце́нен</b>.</div>'
    '<div class="hd-warn">«Vô giá» = quý tột bậc, KHÔNG phải «vô giá trị». Nhưng danh từ cùng mảnh lại ngược hẳn: '
    '<b>за бесце́нок</b> = với giá rẻ mạt.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>цена́</b> giá · <b>це́нный</b> có giá trị · <b>драгоце́нный</b> quý báu · '
    '<b>обесце́нить</b> làm mất giá</div>'
)

# --------------------------------------------------------------------- напрасно
S["напрасно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">напра́сн-</span>'
    '<span class="hd-gloss"><b>напра́сный</b> vô ích, vô cớ — tiếng Nga nay không chẻ nhỏ hơn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">tính từ → trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm mà không được gì, hoặc chẳng có cớ gì: <b>Я напра́сно ждал.</b> Tôi đợi uổng công. '
    '<b>Ты напра́сно волну́ешься.</b> Cậu lo vô cớ thôi. '
    'Gần như <b>зря</b>; <b>зря</b> là lời nói hằng ngày, <b>напра́сно</b> trang trọng hơn.</div>'
    '<div class="hd-warn">Cũng dùng để trách «lẽ ra đừng»: <b>Напра́сно ты э́то сказа́л.</b> '
    'Cậu không nên nói thế.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>напра́сный</b> vô ích, vô cớ · <b>понапра́сну</b> uổng công (khẩu ngữ)</div>'
)

# --------------------------------------------------------------------- легальный
S["легальный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">лег-</span>'
    '<span class="hd-gloss">LUẬT (Latin <i>lex, leg-</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́льн-ый</span>'
    '<span class="hd-gloss">= <i>-al</i>, đuôi tính từ quốc tế, như <b>официа́льный</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>legal</i>: luật cho phép, không chui lậu — <b>лега́льный би́знес</b> kinh doanh hợp pháp, '
    '<b>лега́льный дохо́д</b> thu nhập hợp pháp. Dạng ngắn giống đực đổi <i>ь → е</i>: <b>лега́лен</b>.</div>'
    '<div class="hd-warn"><b>лег-</b> ở đây là mảnh Latin, KHÔNG dính <b>лёгкий</b> nhẹ, dễ. Từ Nga gần nghĩa là '
    '<b>зако́нный</b> (← <b>зако́н</b> luật).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лега́льно</b> một cách hợp pháp · <b>нелега́льный</b> bất hợp pháp, chui · '
    '<b>нелега́л</b> người cư trú chui · <b>легализова́ть</b> hợp pháp hoá</div>'
)

# --------------------------------------------------------------------- криминальный
S["криминальный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кримина́л-</span>'
    '<span class="hd-gloss">chuyện PHẠM PHÁP, giới TỘI PHẠM — <b>кримина́л</b> (Latin <i>crimen</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ьн-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>criminal</i>: dính tới tội phạm — <b>кримина́льный райо́н</b> khu đầy tội phạm, '
    '<b>кримина́льные но́вости</b> tin hình sự. Dạng ngắn giống đực đổi <i>ь → е</i>: <b>кримина́лен</b>.</div>'
    '<div class="hd-warn">«Hình sự» của ngành luật lại là từ khác: <b>уголо́вный ко́декс</b> bộ luật hình sự. '
    'Còn KẺ tội phạm là <b>престу́пник</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кримина́л</b> chuyện phạm pháp, giới tội phạm · '
    '<b>криминали́ст</b> chuyên gia điều tra hình sự</div>'
)

# --------------------------------------------------------------------- оппозиция
S["оппозиция"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">оп-</span>'
    '<span class="hd-gloss">ĐỐI LẠI (Latin <i>ob- → op-</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пози́ция</span>'
    '<span class="hd-gloss">chỗ ĐỨNG, lập trường — chính là <b>пози́ция</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mảnh Latin: «đứng ở phía đối lại» ⇒ sự đối lập, và phe đối lập trong chính trị. '
    'Viết HAI chữ <i>п</i> như <i>opposition</i>; <b>-ция</b> = <i>-tion</i>, luôn giống cái.</div>'
    '<div class="hd-warn">Đối lập VỚI ai: <b>к</b> + cách 3 — <b>быть в оппози́ции к вла́сти</b> '
    'đối lập với chính quyền.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пози́ция</b> vị trí, lập trường · <b>оппозицио́нный</b> thuộc phe đối lập · '
    '<b>оппозиционе́р</b> người phe đối lập · <b>оппоне́нт</b> đối thủ tranh luận</div>'
)

# --------------------------------------------------------------------- инспекция
S["инспекция"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ин-</span>'
    '<span class="hd-gloss">VÀO TRONG (Latin <i>in-</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-спек(т)-</span>'
    '<span class="hd-gloss">NHÌN (Latin <i>spect-</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ция</span>'
    '<span class="hd-gloss">= <i>-tion</i>, danh từ giống cái; <i>т</i> nhường chỗ cho <i>ц</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Nhìn vào tận trong» ⇒ thanh tra, kiểm tra — ghép như <b>инспе́ктор</b>, đọc thẳng ra '
    '<i>inspection</i>: <b>пройти́ инспе́кцию</b> qua được cuộc kiểm tra.</div>'
    '<div class="hd-warn">Còn là tên CƠ QUAN thanh tra: <b>нало́говая инспе́кция</b> = cơ quan thuế.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>инспе́ктор</b> thanh tra viên · <b>инспекти́ровать</b> thanh tra (động từ) · '
    '<b>спекта́кль</b> vở diễn («thứ để nhìn», cùng <i>spect-</i>) · <b>проспе́кт</b> đại lộ</div>'
)

# --------------------------------------------------------------------- остроумный
S["остроумный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">остр-о-</span>'
    '<span class="hd-gloss">NHỌN, sắc — <b>о́стрый</b> + nguyên âm nối</span></div>'
    '<div class="hd-row"><span class="hd-piece">-у́м-</span>'
    '<span class="hd-gloss">TRÍ ÓC — <b>ум</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Trí óc sắc nhọn» ⇒ dí dỏm, nhanh trí: <b>остроу́мная шу́тка</b> câu đùa dí dỏm; tả cách làm '
    'thì là tài tình: <b>остроу́мное реше́ние</b> lời giải tài tình. Dạng ngắn giống đực chen <i>е</i>: '
    '<b>остроу́мен</b>.</div>'
    '<div class="hd-warn"><b>у́мный</b> = thông minh nói chung; <b>остроу́мный</b> = thông minh lộ ra ở câu nói hay, '
    'ý hay — thường làm người ta cười.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>о́стрый</b> sắc, cay · <b>ум</b> trí óc · <b>у́мный</b> thông minh · '
    '<b>остроу́мие</b> tài dí dỏm · <b>остри́ть</b> pha trò</div>'
)

# --------------------------------------------------------------------- рациональный
S["рациональный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рацион-</span>'
    '<span class="hd-gloss">LÝ TRÍ, sự TÍNH TOÁN (Latin <i>ratio, ration-</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́льн-ый</span>'
    '<span class="hd-gloss">= <i>-al</i>, đuôi tính từ quốc tế, như <b>национа́льный</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>rational</i>: theo lý trí chứ không theo cảm xúc. <b>рациона́льный челове́к</b> người lý '
    'trí; <b>рациона́льное реше́ние</b> giải pháp hợp lý. Dạng ngắn giống đực đổi <i>ь → е</i>: '
    '<b>рациона́лен</b>.</div>'
    '<div class="hd-warn"><b>рацио́н</b> cùng gốc Latin nhưng là «khẩu phần ăn» (phần đã tính sẵn) — đừng suy tính từ '
    'này thành «thuộc khẩu phần».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рациона́льно</b> một cách hợp lý · <b>иррациона́льный</b> phi lý trí · '
    '<b>рационали́зм</b> chủ nghĩa duy lý</div>'
)

# --------------------------------------------------------------------- предрассудок
S["предрассудок"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пред-</span>'
    '<span class="hd-gloss">TRƯỚC — <b>пе́ред</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-рас-</span>'
    '<span class="hd-gloss">TÁCH RA từng phần</span></div>'
    '<div class="hd-row"><span class="hd-piece">-су́д-</span>'
    '<span class="hd-gloss">XÉT — <b>суд</b>, <b>суди́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ок</span>'
    '<span class="hd-gloss">đuôi danh từ giống đực, <i>о</i> chạy</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Phán TRƯỚC khi kịp tách ra mà XÉT ⇒ thành kiến — cùng hình ảnh với <i>pre-judice</i> '
    '(<i>pre-</i> trước + <i>judic-</i> xét xử). Bỏ <b>пред-</b> là ra <b>рассу́док</b> lý trí.</div>'
    '<div class="hd-warn">Chữ <i>о</i> của <b>-ок</b> rụng khi thêm đuôi: <b>предрассу́дка</b>, số nhiều '
    '<b>предрассу́дки</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рассу́док</b> lý trí · <b>рассужда́ть</b> lập luận · <b>суди́ть</b> phán xét · '
    '<b>предсказа́ть</b> tiên đoán (cùng <i>пред-</i>)</div>'
)

# --------------------------------------------------------------------- стимул
S["стимул"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn, không chẻ được trong tiếng Nga — Latin <i>stimulus</i>, bỏ đuôi <i>-us</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Latin <i>stimulus</i> vốn là cái gậy nhọn để thúc bò. «Cái thúc cho đi tới» ⇒ động lực, '
    'sự khuyến khích. Trọng âm đứng yên ở đầu: <b>сти́мулы</b>.</div>'
    '<div class="hd-warn">Động lực ĐỂ làm gì: <b>к</b> + cách 3 hoặc <b>для</b> + cách 2 — '
    '<b>сти́мул к рабо́те</b>, <b>сти́мул для рабо́ты</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стимули́ровать</b> khuyến khích, kích thích · <b>стимуля́ция</b> sự kích thích · '
    '<b>стимуля́тор</b> chất kích thích</div>'
)

# --------------------------------------------------------------------- познавать
S["познавать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, nghĩa ở đây mờ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-зна-</span>'
    '<span class="hd-gloss">BIẾT — <b>знать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва́-ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đi dần tới chỗ BIẾT sâu: <b>Де́ти познаю́т мир.</b> Trẻ em tìm hiểu thế giới. Hiện tại rơi '
    '<b>-ва-</b>, đúng khuôn <b>дава́ть → даю́</b>: <b>познаю́, познаёшь</b>; quá khứ giữ: <b>познава́л</b>.</div>'
    '<div class="hd-warn">Chỉ trọng âm tách hai thể: <b>познаю́</b> tôi đang tìm hiểu · '
    '<b>позна́ю</b> tôi sẽ hiểu rõ — <b>позна́ть</b>.</div>'
    '<div class="hd-warn">Tục ngữ: <b>Друзья́ познаю́тся в беде́.</b> Hoạn nạn mới biết bạn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>позна́ть</b> (HT) · <b>позна́ние</b> sự nhận thức · '
    '<b>познава́тельный</b> giúp mở mang hiểu biết · <b>узнава́ть</b> nhận ra</div>'
)

# --------------------------------------------------------------------- познать
S["познать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, nghĩa ở đây mờ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-зна́-</span>'
    '<span class="hd-gloss">BIẾT — <b>знать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể; thể hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">BIẾT tới nơi, biết bằng chính trải nghiệm ⇒ hiểu rõ, nếm trải: <b>позна́ть любо́вь</b> biết thế '
    'nào là yêu, <b>позна́ть го́ре</b> nếm trải đau khổ. Chia như <b>знать</b>: <b>позна́ю, позна́ешь</b>.</div>'
    '<div class="hd-warn"><b>узна́ть</b> = biết một TIN, nhận ra một người; <b>познако́миться</b> = làm quen. '
    '<b>позна́ть</b> trang trọng hơn, hiểu tới BẢN CHẤT: <b>Позна́й себя́!</b> Hãy hiểu chính mình!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>познава́ть</b> (CHT) · <b>знать</b> biết · <b>зна́ние</b> kiến thức · '
    '<b>созна́ние</b> ý thức</div>'
)

# --------------------------------------------------------------------- претендовать
S["претендовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пре-тенд-</span>'
    '<span class="hd-gloss">Latin <i>prae-</i> TRƯỚC + <i>tend-</i> GIĂNG, chìa ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова́ть</span>'
    '<span class="hd-gloss">đuôi động từ, hiện tại đổi <i>-ова- → -у-</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mảnh Latin (<b>пре-</b> này KHÔNG phải tiền tố Nga): «chìa ra trước mặt» cái quyền của mình '
    '⇒ đòi phần, nhắm giành lấy. Chia: <b>претенду́ю, претенду́ешь</b>.</div>'
    '<div class="hd-warn">Đòi, nhắm CÁI GÌ: <b>на</b> + cách 4 — <b>претендова́ть на пе́рвое ме́сто</b> nhắm ngôi '
    'đầu, <b>претендова́ть на кварти́ру</b> đòi quyền với căn hộ.</div>'
    '<div class="hd-warn">Cùng gốc <i>pretend</i> nhưng KHÔNG phải «giả vờ» — cái đó là <b>притворя́ться</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>претенде́нт</b> ứng viên, người tranh chức · <b>прете́нзия</b> yêu sách, lời khiếu nại · '
    '<b>тенде́нция</b> xu hướng (cùng Latin <i>tend-</i>)</div>'
)

# --------------------------------------------------------------------- молчаливый
S["молчаливый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">молч-а-</span>'
    '<span class="hd-gloss">IM, KHÔNG NÓI — <b>молча́ть</b>, giữ chữ <i>а</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ли́в-ый</span>'
    '<span class="hd-gloss">→ tính từ «có tính…», như <b>терпели́вый</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Có tính hay im» ⇒ ít nói: <b>молчали́вый сосе́д</b> người hàng xóm ít nói. Tả TÍNH NẾT; '
    'còn lúc này đang im thì dùng động từ: <b>Он молчи́т.</b></div>'
    '<div class="hd-warn">Còn nghĩa «ngầm, không cần nói ra»: <b>молчали́вое согла́сие</b> sự đồng ý ngầm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>молча́ть</b> im lặng · <b>молча́ние</b> sự im lặng · <b>мо́лча</b> lặng lẽ, không nói gì · '
    '<b>замолча́ть</b> im bặt</div>'
)

# --------------------------------------------------------------------- ленивый
S["ленивый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">лен-</span>'
    '<span class="hd-gloss">SỰ LƯỜI — <b>лень</b>, gốc trơn Slav</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́в-ый</span>'
    '<span class="hd-gloss">→ tính từ «có tính…», như <b>краси́вый</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Có tính lười»: <b>лени́вый кот</b> con mèo lười. Món <b>лени́вые варе́ники</b>: bột trộn '
    'luôn với phô mai tươi, khỏi gói nhân.</div>'
    '<div class="hd-warn"><b>лени́вый</b> tả tính; «tôi đang lười làm» thì dùng <b>мне лень</b> + nguyên thể: '
    '<b>Мне лень гото́вить.</b> Tôi lười nấu ăn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лень</b> sự lười · <b>лени́ться</b> lười (động từ) · <b>лентя́й</b> kẻ lười · '
    '<b>лени́во</b> uể oải</div>'
)

# --------------------------------------------------------------------- настойчивый
S["настойчивый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">LÊN TRÊN, đè lên</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сто́й-</span>'
    '<span class="hd-gloss">ĐỨNG — <b>стоя́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-чив-ый</span>'
    '<span class="hd-gloss">→ tính từ «hay làm việc đó»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Hay đứng lì trên» ý mình ⇒ kiên trì, khăng khăng — tính từ của <b>наста́ивать</b> nhất quyết '
    'đòi. <b>насто́йчивый продаве́ц</b> người bán dai dẳng, <b>насто́йчивая про́сьба</b> lời xin tha thiết.</div>'
    '<div class="hd-warn"><b>упря́мый</b> là bướng, thường là chê; <b>насто́йчивый</b> thường là khen: theo tới cùng để '
    'đạt mục đích.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>наста́ивать</b> nhất quyết đòi · <b>насто́йчиво</b> một cách kiên trì · '
    '<b>стоя́ть</b> đứng · <b>усто́йчивый</b> vững chắc</div>'
)

# --------------------------------------------------------------------- тревожный
S["тревожный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">трево́ж-</span>'
    '<span class="hd-gloss">NỖI LO, BÁO ĐỘNG — <b>трево́га</b>, <i>г → ж</i> trước <b>-н-</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tả cả thứ GÂY lo — <b>трево́жная но́вость</b> tin đáng lo — lẫn lòng ĐANG lo: '
    '<b>трево́жный взгляд</b> ánh mắt bất an. <i>г → ж</i> y như <b>доро́га → доро́жный</b>. '
    'Dạng ngắn giống đực chen <i>е</i>: <b>трево́жен</b>.</div>'
    '<div class="hd-warn"><b>трево́га</b> còn là «báo động» ⇒ <b>трево́жная кно́пка</b> nút báo động.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>трево́га</b> nỗi lo, báo động · <b>трево́жить</b> làm lo, quấy rầy · '
    '<b>трево́жно</b> lo lắng (trạng từ) · <b>встрево́женный</b> đang lo lắng</div>'
)

B = {
    "docbangmat": 118,
    "loitubat": 3,
    "nguonsai": 0,
    "baolen": [
        "🔴 THẺ ĐÃ NẠP SAI TRỌNG ÂM: настаивать [k196] ghi «насто́ять (насто́ю)» ở thân và Họ hàng — đúng là настоя́ть (настою́). nouns.csv chỉ có danh từ nên soat không bắt. Mồ côi, tôi không sửa.",
        "V duyệt — легальный: bỏ «chính thức, công khai» (gloss chỉ legal) ⇒ hết bọc официальный.",
        "V duyệt — напрасно: đổi «toi công» → «uổng công» (for nothing) ⇒ hết bọc зря {vô ích, toi công}; giữ «vô ích» + «vô cớ» (needlessly, đúng câu ví dụ «lo vô cớ»).",
        "V duyệt — bỏ nới rộng: разноцветный «sặc sỡ», престижный «sang trọng» (câu ví dụ nhà hàng vẫn in «sang trọng»), криминальный «đầy tệ nạn» (câu ví dụ vẫn in), инспекция «đoàn thanh tra», ленивый «uể oải», настойчивый «cố chấp», познавать «khám phá» (câu ví dụ vẫn in).",
        "V duyệt — thêm nghĩa thiếu theo gloss: остроумный «nhanh trí, tài tình», молчаливый «ngầm», претендовать «ứng cử, tự cho là», познать/познавать «trải qua, nếm trải».",
        "Trùng hết nghĩa chỉ có cặp thể познать/познавать — badge thể tách. Các chỗ còn lại chỉ giao một nghĩa.",
        "Không đưa lên thẻ: cặp остро́та (câu dí dỏm) / острота́ (độ sắc) — đồng tự THẬT, nhưng nouns.csv chỉ biết острота́; bỏ thay vì xin nới MIEN_TRU.",
        "Không chắc, KHÔNG đưa lên thẻ: từ nguyên напрасный (на-прас-) và тревога. предрассудок chỉ nói «cùng hình ảnh với prejudice», không khẳng định là dịch từ Pháp préjugé.",
    ],
}
