# -*- coding: utf-8 -*-
"""k186 — nature::animals (lô trộn): con vật, đồ đeo, thiên nhiên, thể thao.

Chỗ cần nhất quán trong lô:
(1) Bốn con vật gốc trơn (пчела́, пау́к, бык, осёл): không chẻ, chỉ nói chỗ bảng chia lệch.
(2) -ёнок → số nhiều -я́та chỉ trải ở цыплёнок (thẻ duy nhất mang hậu tố này).
(3) Ba tính từ земно́й / областно́й / го́рный: chẻ cùng khuôn «gốc danh từ + -н- + đuôi».
(4) пояс: пояснить (giải thích) đi từ ясный, KHÔNG cùng gốc — nói ở ô đỏ.
(5) любитель: từ điển in «nhiều любителе́й» (trọng âm dịch) — SAI, đúng là люби́телей
    (trọng âm đứng yên), nên thẻ không nhắc chuyện trọng âm dịch.
Họ hàng cố ý vắng: браслет (mượn Pháp, không có phái sinh Nga thông dụng).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "украшение": "đồ trang trí, đồ trang sức, sự trang trí",               # bỏ «vật trang trí» (lặp); THIẾU decorating
    "пояс": "thắt lưng, dây lưng, cạp, vòng eo, vành đai, múi giờ",        # THIẾU waist, zone/belt of territory, time zone
    "земной": "của Trái Đất, trên mặt đất, trần thế",                       # «mặt đất» là danh từ -> «trên mặt đất»
}

# --------------------------------------------------------------------- украшение
S["украшение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">làm cho thành (tiền tố hoàn thành)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-краш-</span>'
    '<span class="hd-gloss">ĐẸP — gốc крас-, с đổi thành ш</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái làm cho đẹp» ⇒ đồ trang trí, đồ trang sức. Đi thẳng từ động từ '
    '<b>укра́сить</b> trang trí → <b>украша́ть</b> → <b>украше́ние</b>: chữ с của '
    '<b>краси́вый</b> đổi sang ш, phép biến âm <b>с→ш</b> gặp khắp nơi.</div>'
    '<div class="hd-warn"><b>кра́сный</b> «đỏ» cũng cùng gốc: xưa nó nghĩa là «đẹp» — '
    '<b>Кра́сная пло́щадь</b> vốn là «Quảng trường Đẹp».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>краси́вый</b> đẹp · <b>красота́</b> vẻ đẹp · '
    '<b>укра́сить</b>/<b>украша́ть</b> trang trí · <b>кра́сный</b> đỏ</div>'
)

# --------------------------------------------------------------------- пояс
S["пояс"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">quanh, khắp</span></div>'
    '<div class="hd-row"><span class="hd-piece">-яс</span>'
    '<span class="hd-gloss">THẮT, BUỘC — gốc cổ, không còn đứng riêng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái buộc quanh người» ⇒ thắt lưng, rồi mở rộng thành vòng eo '
    '(<b>до по́яса</b> tới ngang thắt lưng) và dải vùng quanh địa cầu: '
    '<b>часово́й по́яс</b> múi giờ. Số nhiều đuôi <b>-а́</b> nhấn: <b>пояса́</b>, '
    '<b>поясо́в</b> (như <b>дома́</b>).</div>'
    '<div class="hd-warn">⚠️ Mức tin: gốc <b>-яс</b> «thắt» là từ nguyên (cùng gốc tiếng Litva '
    '<i>juosta</i> dây lưng). Còn <b>поясни́ть</b> «giải thích» KHÔNG cùng họ — nó là '
    'по + <b>я́сный</b> rõ ràng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поясни́ца</b> thắt lưng (phần lưng dưới) · '
    '<b>опоя́сать</b> thắt quanh, bao quanh</div>'
)

# --------------------------------------------------------------------- браслет
S["браслет"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn (Pháp <i>bracelet</i>) — không chẻ được trong tiếng Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Y hệt tiếng Anh <i>bracelet</i> (cũng mượn từ Pháp; <i>bras</i> = '
    'cánh tay). Trọng âm cuối: <b>брасле́т</b>. Giống đực, biến cách đều.</div>'
)

# --------------------------------------------------------------------- любитель
S["любитель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">люб-</span>'
    '<span class="hd-gloss">YÊU, THÍCH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-тель</span>'
    '<span class="hd-gloss">→ NGƯỜI làm việc đó (như учи́тель, писа́тель)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người <b>люби́ть</b>» ⇒ người mê một thứ gì. Thứ được mê đứng ở '
    '<b>cách 2</b>: <b>люби́тель му́зыки</b> người mê nhạc, <b>люби́тель ко́фе</b>.</div>'
    '<div class="hd-warn">Nghĩa thứ hai: <b>nghiệp dư</b>, đối lập với '
    '<b>профессиона́л</b> — người làm vì thích chứ không vì nghề.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>люби́ть</b> yêu · <b>любо́вь</b> tình yêu · '
    '<b>люби́мый</b> yêu thích · <b>люби́тельский</b> nghiệp dư</div>'
)

# --------------------------------------------------------------------- рекорд
S["рекорд"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn (Anh <i>record</i>) — không chẻ được trong tiếng Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỉ giữ MỘT nghĩa của <i>record</i>: kỷ lục. Hai động từ đi kèm: '
    '<b>установи́ть реко́рд</b> lập kỷ lục · <b>поби́ть реко́рд</b> phá kỷ lục.</div>'
    '<div class="hd-warn"><i>Record</i> «bản ghi, đĩa hát» KHÔNG phải <b>реко́рд</b> — đó là '
    '<b>за́пись</b>, <b>пласти́нка</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>реко́рдный</b> kỷ lục (tính từ) · '
    '<b>рекордсме́н</b> người giữ kỷ lục</div>'
)

# --------------------------------------------------------------------- старт
S["старт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn (Anh <i>start</i>) — không chẻ được trong tiếng Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Như tiếng Anh <i>start</i>, nhưng là danh từ của thể thao và tên lửa: '
    'vạch xuất phát, lúc phóng. Động từ «bắt đầu» thường ngày vẫn là <b>начина́ть</b>.</div>'
    '<div class="hd-warn">Lệnh xuất phát phải thuộc: <b>На старт! Внима́ние! Марш!</b> — '
    'Vào vị trí! Chuẩn bị! Chạy!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стартова́ть</b> xuất phát · <b>ста́ртовый</b> thuộc về xuất phát</div>'
)

# --------------------------------------------------------------------- медаль
S["медаль"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn (Pháp <i>médaille</i>) — không chẻ được trong tiếng Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <b>-ь</b> không cho biết giống — <b>меда́ль</b> là <b>giống cái</b>, '
    'đúng như gốc Pháp <i>la médaille</i>: <b>золота́я меда́ль</b>.</div>'
    '<div class="hd-warn"><b>Оборо́тная сторона́ меда́ли</b> — «mặt sau tấm huy chương» = '
    'mặt trái của sự việc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>медали́ст</b> người đoạt huy chương</div>'
)

# --------------------------------------------------------------------- пчела
S["пчела"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn Slav cổ — không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Số ít nhấn đuôi <b>пчела́</b>; sang số nhiều trọng âm nhảy lên gốc và '
    'е thành ё: <b>пчёлы</b>, <b>пчёл</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пчели́ный</b> của ong (<b>пчели́ный мёд</b> mật ong) · '
    '<b>пчелово́д</b> người nuôi ong · <b>пчёлка</b> con ong nhỏ</div>'
)

# --------------------------------------------------------------------- цыплёнок
S["цыплёнок"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">цыпл-</span>'
    '<span class="hd-gloss">GÀ CON — gốc trơn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ёнок</span>'
    '<span class="hd-gloss">→ CON NON của loài vật (như котёнок mèo con)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hậu tố <b>-ёнок</b> có bảng riêng: số ít mất о (<b>цыплёнка</b>), số '
    'nhiều đổi hẳn sang <b>-я́та</b>: <b>цыпля́та</b>, <b>цыпля́т</b>. Cùng khuôn: '
    '<b>котёнок</b> → <b>котя́та</b>.</div>'
    '<div class="hd-warn"><b>Цыпля́т по о́сени счита́ют</b> — «gà con đến thu mới đếm» = '
    'đừng vội mừng trước khi có kết quả.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">cùng hậu tố: <b>котёнок</b> mèo con · <b>ребёнок</b> đứa trẻ · '
    '<b>медвежо́нок</b> gấu con</div>'
)

# --------------------------------------------------------------------- паук
S["паук"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn Slav cổ — không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỉ dạng gốc nhấn <b>пау́к</b>; thêm đuôi là trọng âm nhảy ra đuôi: '
    '<b>паука́</b>, <b>пауки́</b>.</div>'
    '<div class="hd-warn"><b>паути́на</b> mạng nhện cùng gốc — và Internet được gọi là '
    '<b>Всеми́рная паути́на</b>, đúng như <i>World Wide Web</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>паути́на</b> mạng nhện · <b>паучо́к</b> con nhện nhỏ</div>'
)

# --------------------------------------------------------------------- бык
S["бык"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn Slav cổ — không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Con ĐỰC; bò cái là từ khác hẳn: <b>коро́ва</b>. Thêm đuôi là trọng âm '
    'nhảy ra đuôi: <b>быка́</b>, <b>быки́</b>. Nói người thì là gã to con hung hãn.</div>'
    '<div class="hd-warn"><b>Взять быка́ за рога́</b> — nắm sừng con bò, y như tiếng Anh '
    '<i>take the bull by the horns</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бычо́к</b> bò đực non</div>'
)

# --------------------------------------------------------------------- осёл
S["осёл"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — mượn rất sớm qua tiếng Goth, gốc Latin <i>asinus</i> '
    '(cùng nguồn với tiếng Anh <i>ass</i>).</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nguyên âm ё rơi mất khi thêm đuôi, trọng âm nhảy ra đuôi: '
    '<b>осла́</b>, <b>ослу́</b>, <b>ослы́</b>.</div>'
    '<div class="hd-warn">Nói người là chửi: <b>Ты осёл!</b> — đồ ngu, đồ cứng đầu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>о́слик</b> con lừa nhỏ · <b>осли́ный</b> của lừa '
    '(<b>осли́ное упря́мство</b> cứng đầu như lừa)</div>'
)

# --------------------------------------------------------------------- гнездо
S["гнездо"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Trong tiếng Nga hiện đại là gốc trơn — không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng một từ Ấn-Âu với tiếng Anh <i>nest</i>: «chỗ ngồi xuống». '
    'Số nhiều trọng âm lên gốc, е thành ё: <b>гнёзда</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: gặp <i>nest</i> là từ nguyên học khá chắc, không phải luật '
    'suy ra được. Cụm hay gặp: <b>вить гнездо́</b> làm tổ (bện tổ).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гнезди́ться</b> làm tổ · <b>гнёздышко</b> tổ nhỏ, tổ ấm</div>'
)

# --------------------------------------------------------------------- корень
S["корень"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn Slav cổ — không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nguyên âm е rơi khi thêm đuôi: <b>ко́рня</b>, <b>ко́рнем</b>; số nhiều '
    '<b>ко́рни</b>, <b>корне́й</b>. Đây cũng là chữ của ngữ pháp: <b>ко́рень сло́ва</b> gốc từ — '
    'đúng mảnh in HOA ở mục «Chẻ từ».</div>'
    '<div class="hd-warn"><b>в ко́рне</b> = tận gốc, hoàn toàn: <b>в ко́рне неве́рно</b> sai từ '
    'gốc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>коренно́й</b> bản địa, căn bản · <b>укорени́ться</b> bén rễ · '
    '<b>корешо́к</b> rễ nhỏ, gáy sách</div>'
)

# --------------------------------------------------------------------- жара
S["жара"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">жар-</span>'
    '<span class="hd-gloss">NÓNG RỰC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">→ danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái nóng của THỜI TIẾT: <b>Сего́дня жара́</b> hôm nay nóng. Cảm thấy '
    'nóng thì dùng trạng từ: <b>Мне жа́рко</b>.</div>'
    '<div class="hd-warn">Bớt chữ а là đổi nghĩa: <b>У него́ жар</b> = anh ấy bị SỐT, '
    'không phải trời nóng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жар</b> hơi nóng, cơn sốt · <b>жа́ркий</b> nóng · '
    '<b>жа́рить</b> rán, nướng</div>'
)

# --------------------------------------------------------------------- закат
S["закат"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">ra sau, khuất đi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-кат</span>'
    '<span class="hd-gloss">LĂN (như кати́ть)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mặt trời «lăn khuất» sau chân trời: <b>со́лнце закати́лось</b>. Nghĩa '
    'bóng là lúc tàn: <b>зака́т импе́рии</b>. Cặp đối: <b>восхо́д</b> mặt trời mọc '
    '(вос- lên + ход đi).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кати́ть</b> lăn · <b>ката́ться</b> đi chơi (bằng xe, trượt) · '
    '<b>закати́ться</b> lăn vào, lặn</div>'
)

# --------------------------------------------------------------------- пламя
S["пламя"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn — không chẻ được; đuôi <b>-мя</b> là dấu hiệu nhóm từ đặc biệt.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng nhóm với <b>вре́мя</b> và <b>и́мя</b>: giống trung, thêm '
    '<b>-ен-</b> khi biến cách — <b>пла́мени</b>, <b>пла́менем</b>, như <b>вре́мени</b>.</div>'
    '<div class="hd-warn">Chỉ dùng số ít. Muốn nói từng ngọn lửa: <b>языки́ пла́мени</b> '
    '«những lưỡi lửa».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пла́менный</b> rực lửa, nồng nhiệt (<b>пла́менный приве́т</b> lời '
    'chào nồng nhiệt)</div>'
)

# --------------------------------------------------------------------- земной
S["земной"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">зем-</span>'
    '<span class="hd-gloss">ĐẤT (như земля́)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ой</span>'
    '<span class="hd-gloss">→ tính từ, đuôi -ой luôn nhấn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thuộc về <b>земля́</b>» — cả Trái Đất lẫn cõi trần, đối lập với '
    '<b>небе́сный</b> trên trời: <b>земно́й шар</b> địa cầu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>земля́</b> đất, Trái Đất · <b>подзе́мный</b> dưới đất · '
    '<b>землетрясе́ние</b> động đất · <b>земляни́ка</b> dâu rừng</div>'
)

# --------------------------------------------------------------------- областной
S["областной"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">област-</span>'
    '<span class="hd-gloss">VÙNG, TỈNH (о́бласть)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ой</span>'
    '<span class="hd-gloss">→ tính từ, đuôi -ой luôn nhấn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thuộc về <b>о́бласть</b>» — cấp tỉnh: <b>областно́й центр</b> tỉnh lỵ. '
    'Trọng âm nhảy từ đầu ra đuôi: о́бласть → областно́й.</div>'
    '<div class="hd-warn">⚠️ Mức tin: từ nguyên — <b>о́бласть</b> gốc là «vùng dưới quyền», '
    'cùng gốc <b>власть</b> quyền lực. Không suy ra được từ mặt chữ hiện nay.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>о́бласть</b> tỉnh, vùng, lĩnh vực · <b>власть</b> quyền lực</div>'
)

# --------------------------------------------------------------------- горный
S["горный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гор-</span>'
    '<span class="hd-gloss">NÚI (như гора́)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">→ tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thuộc về <b>гора́</b>»: <b>го́рные лы́жи</b> trượt tuyết đổ dốc. '
    'Mỏ khoét vào núi nên còn nghĩa ngành mỏ: <b>го́рный инжене́р</b> kỹ sư mỏ.</div>'
    '<div class="hd-warn"><b>го́род</b> thành phố KHÔNG cùng gốc — chỉ trùng mặt chữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гора́</b> núi · <b>го́рка</b> đồi nhỏ, cầu trượt · '
    '<b>горня́к</b> thợ mỏ</div>'
)

B = {
    "docbangmat": 78,
    "loitubat": 2,
    "nguonsai": 1,
    "baolen": [
        "Nguồn sai (đã bác): любитель — bảng từ điển in «nhiều любителе́й» và báo «trọng âm dịch khi sang số nhiều»; đúng là люби́тели, люби́телей (trọng âm đứng yên trên -би-). Thẻ không nhắc chuyện trọng âm dịch.",
        "Lỗi tự bắt (2): стартово́й → ста́ртовый (tính từ nhấn gốc, không nhấn đuôi); пояс: bỏ ví dụ «по по́яс» vì cụm này hay nói «по́ пояс» (trọng âm nhảy lên giới từ), thay bằng «до по́яса» an toàn.",
        "Không chắc (mức tin vừa, đã gắn ⚠️ Mức tin trên thẻ): пояс gốc -яс «thắt» (cùng Litva juosta); гнездо cùng gốc tiếng Anh nest (*ni-sd- «ngồi xuống»); о́бласть cùng gốc власть. Ba điều KHÔNG gắn cờ nhưng cũng là từ nguyên: кра́сный xưa = «đẹp» (Кра́сная пло́щадь), паути́на cùng gốc пау́к, осёл mượn qua Goth từ Latin asinus — tôi tin khá chắc, luồng chính muốn chặt hơn thì hạ thành ⚠️.",
        "Họ hàng cố ý vắng: браслет (mượn Pháp, không có phái sinh Nga thông dụng).",
        "V cần duyệt (3 thẻ): украшение (bỏ «vật trang trí» lặp «đồ trang trí», thêm «sự trang trí» = decorating); пояс (THIẾU vòng eo, vành đai, múi giờ — gloss có waist, belt of territory, time zone); земной («mặt đất» là danh từ → «trên mặt đất»). 17 thẻ còn lại giữ đề cũ. Va chạm nghĩa: không có.",
    ],
}
