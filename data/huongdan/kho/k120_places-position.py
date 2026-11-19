# -*- coding: utf-8 -*-
"""k120 — places-position: 22 từ trộn hai cụm (trạng từ vị trí/hướng + từ học thuật) và vài hư từ.

Không khối hệ thống, không ép một trục chung. Chỗ cần nhất quán trong lô:
(1) ĐI ĐÂU / Ở ĐÂU: в/на + cách 4 = hướng (вниз, наве́рх — thẻ cũ), в/на + cách 6 đuôi -у́
    = vị trí (внизу́, наверху́). Bộ ba куда́/где/отку́да trải ở внизу́; наверху́ dẫn chiếu.
    Bẫy ngược ở снару́жи: нару́жу đuôi -у lại là HƯỚNG. впереди́ ↔ вперёд (k12).
(2) не́- vs ни-: не́чего theo đúng khuôn не́когда (k75), phép so với ничего́ (k17).
(3) -нибудь vs -то: nói cùng quy tắc với кто́-то (k110) / како́й-то (k111).
(4) chèn л sau phụ âm môi: направле́ние, заявле́ние (y như люби́ть → люблю́).
Họ hàng: cả 22 thẻ đều có (kể cả ло́дка — có подло́дка; ана́лиз — có анализи́ровать).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa, ngăn bằng dấu phẩy.
V = {
    "направление": "hướng, chiều, xu hướng, trường phái, giấy giới thiệu",
    "впереди": "ở đằng trước, đi trước, dẫn đầu",
    "снаружи": "ở bên ngoài, từ bên ngoài",
    "мимо": "ngang qua, trượt mục tiêu",
    "внизу": "ở dưới, ở tầng dưới, ở dưới cùng",
    "наверху": "ở phía trên, ở tầng trên, ở trên cùng",
    "наверх": "lên trên, lên tầng trên",
    "путешествие": "cuộc hành trình, chuyến du hành",
    "лодка": "thuyền nhỏ, xuồng",
    "нечего": "không có gì để",
    "действительно": "thật sự, quả thực, đúng là",
    "по-твоему": "theo cậu, theo ý cậu, theo cách của cậu",
    "во-первых": "thứ nhất là, trước hết",
    "какой-нибудь": "gì đó",
    "благодаря": "nhờ có, nhờ vào",
    "заявление": "lá đơn, đơn xin, đơn trình báo, lời tuyên bố",
    "практика": "thực hành, thực tế, kỳ thực tập",
    "исследование": "công trình nghiên cứu, sự khảo sát, cuộc thám hiểm",
    "знание": "kiến thức, sự hiểu biết",
    "анализ": "xét nghiệm, sự phân tích",
    "пример": "ví dụ, tấm gương",
    "опыт": "kinh nghiệm, trải nghiệm, thí nghiệm",
}

# ------------------------------------------------------------- направление
S["направление"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">LÊN, nhắm vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-прав-</span>'
    '<span class="hd-gloss">THẲNG, ĐÚNG (gốc của <b>пра́вый</b>, <b>пра́вило</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-л-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Nắn cho thẳng về một phía» ⇒ hướng. Đây là danh từ của <b>напра́вить</b> '
    '(hướng về): <b>л</b> chèn vào sau <b>в</b> y như <b>люби́ть → люблю́</b>.</div>'
    '<div class="hd-warn"><b>в направле́нии</b> + cách 2 = về hướng: <b>в направле́нии '
    'це́нтра</b>. Ở phòng khám, <b>направле́ние</b> là tờ giấy giới thiệu đi khám chỗ khác.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>напра́во</b> sang phải · <b>пра́вый</b> bên phải, đúng · '
    '<b>пра́вило</b> quy tắc · <b>напра́вить</b> hướng về</div>'
)

# ----------------------------------------------------------------- впереди
S["впереди"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">giới từ <b>в</b> dính liền</span></div>'
    '<div class="hd-row"><span class="hd-piece">-перед-и</span>'
    '<span class="hd-gloss">PHÍA TRƯỚC — cùng gốc <b>пе́ред</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bản ĐỨNG YÊN của <b>вперёд</b> (thẻ đã học): <b>Он идёт впереди́</b> = '
    'anh ấy đi đằng trước. Làm giới từ thì kéo cách 2: <b>впереди́ всех</b> = dẫn đầu tất cả. '
    'Cũng chỉ thời gian: <b>Всё ещё впереди́</b> = mọi thứ còn ở phía trước.</div>'
    '<div class="hd-warn">Khác <b>пе́ред</b> + cách 5 = trước một vật, một lúc: <b>пе́ред до́мом</b> '
    'trước nhà, <b>пе́ред обе́дом</b> trước bữa trưa. <b>впереди́</b> là phía trước trên một '
    'hướng đi, và đứng một mình được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вперёд</b> tiến lên · <b>пе́ред</b> trước · '
    '<b>пере́дний</b> ở phía trước · <b>сза́ди</b> đằng sau (đối của nó)</div>'
)

# ----------------------------------------------------------------- снаружи
S["снаружи"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">TỪ PHÍA (như <b>сза́ди</b>, <b>сни́зу</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-наруж-и</span>'
    '<span class="hd-gloss">PHÍA NGOÀI — không chẻ tiếp được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một từ lo cả «ở ngoài» lẫn «từ ngoài»: <b>Снару́жи хо́лодно</b> = ngoài '
    'trời lạnh · <b>Дверь открыва́ется снару́жи</b> = cửa mở từ bên ngoài. Đối của nó: '
    '<b>внутри́</b> ở bên trong.</div>'
    '<div class="hd-warn">Đi RA ngoài là <b>нару́жу</b> — đuôi <b>-у</b> ở đây là HƯỚNG, ngược '
    'với <b>внизу́</b> (đuôi <b>-у́</b> là vị trí). Cặp này phải thuộc riêng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нару́жу</b> ra ngoài · <b>нару́жный</b> bên ngoài, bề ngoài</div>'
)

# -------------------------------------------------------------------- мимо
S["мимо"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ gốc trơn, không chẻ ra mảnh mang nghĩa được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đi ngang qua mà không dừng», kéo cách 2: <b>Я проходи́л ми́мо '
    'шко́лы</b> = tôi đi ngang qua trường. Không có danh từ thì đứng một mình: '
    '<b>Он прошёл ми́мо</b> = anh ta đi lướt qua.</div>'
    '<div class="hd-warn">Bắn, ném, đoán mà không trúng cũng là <b>ми́мо</b>: <b>Ми́мо!</b> = '
    'Trượt rồi!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мимохо́дом</b> tiện thể, nhân tiện (<b>ми́мо</b> + <b>ход</b> bước '
    'đi) · <b>мимолётный</b> thoáng qua (<b>ми́мо</b> + <b>лете́ть</b> bay)</div>'
)

# ------------------------------------------------------------------- внизу
S["внизу"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в</span>'
    '<span class="hd-gloss">TRONG, Ở</span></div>'
    '<div class="hd-row"><span class="hd-piece">низу́</span>'
    '<span class="hd-gloss"><b>низ</b> PHẦN DƯỚI ở cách 6 đuôi <b>-у́</b> (như <b>в лесу́</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Suy thẳng ra từ luật giới từ: <b>в</b> + cách 6 = Ở ĐÂU ⇒ <b>внизу́</b> = '
    'ở dưới, ở tầng dưới. Còn <b>в</b> + cách 4 = ĐI ĐÂU ⇒ <b>вниз</b> (thẻ đã học).</div>'
    '<div class="hd-warn">Ba câu hỏi, ba từ: <b>куда́?</b> <b>вниз</b> xuống dưới · '
    '<b>где?</b> <b>внизу́</b> ở dưới · <b>отку́да?</b> <b>сни́зу</b> từ dưới lên.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>низ</b> phần dưới · <b>ни́зкий</b> thấp · <b>ни́жний</b> ở dưới · '
    '<b>наверху́</b> ở trên (đối của nó)</div>'
)

# ----------------------------------------------------------------- наверху
S["наверху"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на</span>'
    '<span class="hd-gloss">TRÊN, Ở</span></div>'
    '<div class="hd-row"><span class="hd-piece">верху́</span>'
    '<span class="hd-gloss"><b>верх</b> PHẦN TRÊN ở cách 6 đuôi <b>-у́</b> (như <b>на полу́</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>на</b> + cách 6 = Ở ĐÂU ⇒ ở trên, ở tầng trên: <b>Ма́ма наверху́</b> = '
    'mẹ ở trên lầu. Dựng y hệt <b>внизу́</b>; bộ ba của nó: <b>наве́рх</b> lên trên · '
    '<b>наверху́</b> ở trên · <b>све́рху</b> từ trên xuống.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>верх</b> phần trên, đỉnh · <b>ве́рхний</b> ở trên · '
    '<b>вверх</b> hướng lên · <b>внизу́</b> ở dưới (đối của nó)</div>'
)

# ------------------------------------------------------------------ наверх
S["наверх"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на</span>'
    '<span class="hd-gloss">LÊN, tới chỗ</span></div>'
    '<div class="hd-row"><span class="hd-piece">верх</span>'
    '<span class="hd-gloss">PHẦN TRÊN, ĐỈNH — ở cách 4, nên chỉ HƯỚNG</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>на</b> + cách 4 = ĐI ĐÂU ⇒ lên trên, lên tầng trên: <b>Подними́сь '
    'наве́рх</b> = lên lầu đi. Tới nơi rồi đứng yên thì là <b>наверху́</b> (xem thẻ đó).</div>'
    '<div class="hd-warn">Khác <b>вверх</b> (thẻ đã học): <b>вверх</b> thường là hướng lên '
    '(<b>смотре́ть вверх</b> nhìn lên), còn <b>наве́рх</b> là lên TỚI chỗ ở trên — tầng trên, '
    'đỉnh núi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>верх</b> phần trên · <b>наверху́</b> ở trên · <b>све́рху</b> từ trên '
    'xuống · <b>вниз</b> xuống dưới (đối của nó)</div>'
)

# ------------------------------------------------------------- путешествие
S["путешествие"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">путе-</span>'
    '<span class="hd-gloss">ĐƯỜNG — gốc của <b>путь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-шеств-</span>'
    '<span class="hd-gloss">ĐI, BƯỚC (gốc cổ)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ие</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>путеше́ствовать</b> (thẻ đã học): «đi trên đường xa» ⇒ '
    'cuộc hành trình. Cách chẻ <b>-шеств-</b> là từ nguyên, mức tin ghi ở thẻ động từ.</div>'
    '<div class="hd-warn">Khác <b>пое́здка</b> = một chuyến đi có việc (về quê, công tác). '
    '<b>путеше́ствие</b> là đi xa để khám phá nhiều nơi: <b>путеше́ствие по Евро́пе</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>путь</b> con đường · <b>путеше́ствовать</b> du lịch · '
    '<b>путеше́ственник</b> người du hành</div>'
)

# ------------------------------------------------------------------- лодка
S["лодка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ hữu ích cho người học — học nguyên khối.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đi bằng thuyền là <b>на</b> + cách 6: <b>ката́ться на ло́дке</b> = đi '
    'chơi thuyền. Chỗ bất thường duy nhất: số nhiều cách 2 chèn <b>о</b> — <b>мно́го ло́док</b> '
    '— cùng luật với mọi danh từ đuôi <b>-ка</b> sau phụ âm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ло́дочка</b> chiếc thuyền con · <b>подло́дка</b> tàu ngầm (rút từ '
    '<b>подво́дная ло́дка</b> «thuyền dưới nước»)</div>'
)

# ------------------------------------------------------------------ нечего
S["нечего"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не́-</span>'
    '<span class="hd-gloss">tiền tố hút trọng âm: «không có ... mà»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-чего</span>'
    '<span class="hd-gloss">cách 2 của <b>что</b> (cái gì)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng khuôn <b>не́когда</b> (thẻ đã học): «không có cái gì để mà làm». '
    'Câu không chủ ngữ, người ở cách 3, theo sau là động từ nguyên thể: <b>Мне не́чего '
    'сказа́ть</b> = tôi không có gì để nói.</div>'
    '<div class="hd-warn">Đối chiếu <b>ничего́</b>: <b>Я ничего́ не сказа́л</b> = tôi đã chẳng '
    'nói gì (cần thêm <b>не</b>, có chủ ngữ) · <b>Мне не́чего сказа́ть</b> = không có gì để nói '
    '(không có <b>не</b> nào khác). Trọng âm cũng ngược: <b>не́чего</b> / <b>ничего́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>не́когда</b> không có thì giờ · <b>не́где</b> không có chỗ · '
    '<b>не́кого</b> không có ai (để) · <b>ничего́</b> chẳng gì</div>'
)

# ----------------------------------------------------------- действительно
S["действительно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">действ-</span>'
    '<span class="hd-gloss">HÀNH ĐỘNG, tác động (<b>де́йствие</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́тельн-</span>'
    '<span class="hd-gloss">đuôi tính từ <b>-тельный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">→ trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đi đúng con đường của tiếng Anh: <i>act</i> → <i>actual</i> → '
    '<i>actually</i>. Cái đang thật sự tác động thì là thật ⇒ <b>действи́тельный</b> thật, '
    '<b>действи́тельно</b> thật sự, quả thực.</div>'
    '<div class="hd-warn">Đứng một mình là câu đáp hằng ngày: <b>Действи́тельно?</b> = Thật à? · '
    '<b>Да, действи́тельно</b> = Ừ, đúng thế thật.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>де́йствие</b> hành động, tác dụng · <b>де́йствовать</b> hành động, '
    'có hiệu lực · <b>действи́тельность</b> hiện thực</div>'
)

# --------------------------------------------------------------- по-твоему
S["по-твоему"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">THEO, kiểu</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тво́ему</span>'
    '<span class="hd-gloss">cách 3 của <b>твой</b> (của cậu)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Theo cái của cậu» ⇒ theo ý cậu, theo cách của cậu: <b>По-тво́ему, он '
    'прав?</b> = theo cậu thì anh ấy đúng không? · <b>Пусть бу́дет по-тво́ему</b> = thôi, làm '
    'theo ý cậu.</div>'
    '<div class="hd-warn">Trọng âm lùi về gốc: <b>твоему́</b> nhưng <b>по-тво́ему</b>, '
    '<b>моему́</b> nhưng <b>по-мо́ему</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>твой</b> của cậu · <b>по-мо́ему</b> theo tôi · '
    '<b>по-ва́шему</b> theo anh/chị · <b>по-сво́ему</b> theo cách riêng của mình</div>'
)

# --------------------------------------------------------------- во-первых
S["во-первых"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">во</span>'
    '<span class="hd-gloss">= giới từ <b>в</b>, dạng đông cứng</span></div>'
    '<div class="hd-row"><span class="hd-piece">пе́рвых</span>'
    '<span class="hd-gloss"><b>пе́рвый</b> thứ nhất, cách 6 số nhiều</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Trong những điều thứ nhất» ⇒ thứ nhất là, trước hết. Dùng để mở một '
    'chuỗi lý lẽ: <b>Во-пе́рвых, уже́ по́здно</b> = thứ nhất là đã muộn rồi.</div>'
    '<div class="hd-warn">Đếm tiếp: <b>во-вторы́х</b>, rồi <b>в-тре́тьих</b>, '
    '<b>в-четвёртых</b> — từ số ba chỉ còn <b>в-</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пе́рвый</b> thứ nhất · <b>впервы́е</b> lần đầu tiên · '
    '<b>во-вторы́х</b> thứ hai là</div>'
)

# ------------------------------------------------------------ какой-нибудь
S["какой-нибудь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">како́й</span>'
    '<span class="hd-gloss">nào (thẻ đã học)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-нибудь</span>'
    '<span class="hd-gloss">«… nào cũng được» — chưa chốt cái nào, có khi chưa chắc có</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Y như <b>кто́-нибудь</b>: <b>Купи́ како́й-нибудь торт</b> = mua cái bánh '
    'nào đấy (loại nào cũng được). Chỉ phần како́й đổi đuôi: <b>кака́я-нибудь</b>, '
    '<b>каки́е-нибудь</b>.</div>'
    '<div class="hd-warn"><b>Ты чита́л каку́ю-нибудь его́ кни́гу?</b> = cậu đọc cuốn nào (bất kỳ) '
    'của ông ấy chưa? — <b>Да, каку́ю-то чита́л</b> = rồi, có đọc một cuốn (có thật, không nhớ '
    'tên). Hỏi, nhờ, nói chuyện sắp tới thì <i>-нибудь</i>; kể chuyện đã xảy ra thì <i>-то</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>како́й-то</b> nào đó (có thật) · <b>кто́-нибудь</b> bất kỳ ai · '
    '<b>что́-нибудь</b> cái gì cũng được · <b>когда́-нибудь</b> một lúc nào đó</div>'
)

# --------------------------------------------------------------- благодаря
S["благодаря"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">благо-</span>'
    '<span class="hd-gloss">ĐIỀU TỐT LÀNH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дар-</span>'
    '<span class="hd-gloss">MÓN QUÀ, trao tặng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́</span>'
    '<span class="hd-gloss">đuôi «trong khi đang…» (trạng động từ)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc là «đang cảm ơn» của <b>благодари́ть</b> (thẻ đã học), đông cứng '
    'thành giới từ «nhờ có». Lý do TỐT thì dùng nó, lý do xấu dùng <b>из-за</b>: '
    '<b>благодаря́ тебе́</b> = nhờ có cậu.</div>'
    '<div class="hd-warn">Lệch cách với chính động từ gốc: <b>благодари́ть дру́га</b> (cách 4) '
    'nhưng <b>благодаря́ дру́гу</b> (cách 3).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>благодари́ть</b> cảm ơn · <b>благода́рность</b> lòng biết ơn · '
    '<b>благода́рный</b> biết ơn · <b>пода́рок</b> món quà</div>'
)

# --------------------------------------------------------------- заявление
S["заявление"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng dễ nhớ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-яв-</span>'
    '<span class="hd-gloss">LỘ RA, HIỆN RÕ (gốc của <b>я́вный</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-л-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung, <b>л</b> chèn sau <b>в</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>заяви́ть</b> (tuyên bố): «nói cho lộ rõ ra» ⇒ lời tuyên bố. '
    'Viết ra giấy để trình rõ yêu cầu ⇒ lá đơn. Chèn <b>л</b> như <b>направле́ние</b>.</div>'
    '<div class="hd-warn"><b>подава́ть заявле́ние</b> = nộp đơn · <b>заявле́ние на о́тпуск</b> = '
    'đơn xin nghỉ phép (<b>на</b> + cách 4 cho thứ mình xin).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>заяви́ть</b> tuyên bố · <b>я́вный</b> rõ ràng · '
    '<b>явле́ние</b> hiện tượng · <b>появи́ться</b> xuất hiện</div>'
)

# ---------------------------------------------------------------- практика
S["практика"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">практ-</span>'
    '<span class="hd-gloss">LÀM, thực hiện — gốc Hy Lạp, như <i>practice</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ика</span>'
    '<span class="hd-gloss">đuôi danh từ chỉ lĩnh vực, hoạt động (<b>фи́зика</b>, <b>те́хника</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>practice</i>: phần LÀM, đối với lý thuyết <b>тео́рия</b>. '
    'Với sinh viên nó còn là kỳ đi thực tập.</div>'
    '<div class="hd-warn"><b>на пра́ктике</b> = trên thực tế · <b>проходи́ть пра́ктику</b> = '
    'đi thực tập.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>практи́ческий</b> thực tế, thực hành · <b>практи́чески</b> hầu như '
    '(như <i>practically</i>) · <b>практика́нт</b> thực tập sinh</div>'
)

# ----------------------------------------------------------- исследование
S["исследование"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ис-</span>'
    '<span class="hd-gloss">= <b>из-</b>: ra, tới tận cùng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-след-</span>'
    '<span class="hd-gloss">DẤU VẾT (<b>след</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ние</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Lần theo dấu vết tới tận cùng» ⇒ nghiên cứu, khảo sát, thám hiểm. '
    'Động từ là <b>иссле́довать</b>.</div>'
    '<div class="hd-warn">Khác <b>изуча́ть</b> = học, tìm hiểu cái người khác đã biết (học tiếng '
    'Nga). <b>иссле́дование</b> là tìm ra cái chưa ai biết: <b>нау́чное иссле́дование</b> = '
    'công trình khoa học.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>след</b> dấu vết · <b>сле́довать</b> đi theo · '
    '<b>сле́дующий</b> tiếp theo · <b>иссле́дователь</b> nhà nghiên cứu</div>'
)

# ------------------------------------------------------------------ знание
S["знание"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">зна-</span>'
    '<span class="hd-gloss">BIẾT — gốc của <b>знать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ние</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>знать</b> biết → <b>зна́ние</b> cái biết, như <i>know</i> → '
    '<i>knowledge</i>. Thêm <b>со-</b> (cùng) là <b>созна́ние</b> ý thức — dựng y như '
    '<i>con-science</i>.</div>'
    '<div class="hd-warn">«Kiến thức» nói chung thường ở số nhiều: <b>глубо́кие зна́ния</b> = kiến '
    'thức sâu. Số ít hay đi với một thứ cụ thể: <b>зна́ние языка́</b> = vốn ngoại ngữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>знать</b> biết · <b>знако́мый</b> quen biết · <b>знак</b> dấu hiệu · '
    '<b>знамени́тый</b> nổi tiếng · <b>созна́ние</b> ý thức</div>'
)

# ------------------------------------------------------------------ анализ
S["анализ"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn nguyên từ Hy Lạp qua châu Âu — chính là <i>analysis</i>, không chẻ '
    'trong tiếng Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa sách vở là «sự phân tích», nhưng ngoài đời hay gặp nhất là ở bệnh '
    'viện: <b>ана́лиз кро́ви</b> = xét nghiệm máu. Trọng âm nằm giữa: <b>ана́лиз</b>.</div>'
    '<div class="hd-warn"><b>сдать ана́лизы</b> = đi xét nghiệm (thường số nhiều, nghĩa đen «nộp '
    'mẫu»).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>анализи́ровать</b> phân tích · <b>анали́тик</b> nhà phân tích</div>'
)

# ------------------------------------------------------------------ пример
S["пример"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">ÁP VÀO, sát bên</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мер</span>'
    '<span class="hd-gloss">ĐO (gốc của <b>ме́ра</b>, <b>ме́рить</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái đem áp vào để đo, để so» ⇒ ví dụ, khuôn mẫu, tấm gương. Cùng một '
    'nước đi với <b>приме́рить</b> = ướm thử (quần áo): áp lên người để đo.</div>'
    '<div class="hd-warn"><b>наприме́р</b> (viết liền) = chẳng hạn · <b>брать приме́р с</b> + '
    'cách 2 = noi gương ai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>наприме́р</b> chẳng hạn · <b>приме́рно</b> khoảng chừng · '
    '<b>приме́рить</b> ướm thử · <b>ме́ра</b> mức, biện pháp</div>'
)

# -------------------------------------------------------------------- опыт
S["опыт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">tiền tố, không mang nghĩa riêng dễ nhớ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пыт</span>'
    '<span class="hd-gloss">THỬ (gốc của <b>пыта́ться</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Kinh nghiệm là thứ có được nhờ THỬ nhiều lần — nên cùng một từ còn là '
    '«thí nghiệm»: <b>ста́вить о́пыты</b> = làm thí nghiệm. Đúng như <b>о́пытный</b> (thẻ đã '
    'học) vừa là «dày dạn» vừa là «thử nghiệm».</div>'
    '<div class="hd-warn"><b>о́пыт рабо́ты</b> = kinh nghiệm làm việc (dòng quen thuộc trong tin '
    'tuyển dụng).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>о́пытный</b> có kinh nghiệm · <b>пыта́ться</b> cố thử · '
    '<b>попы́тка</b> lần thử</div>'
)
