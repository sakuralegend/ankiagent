# -*- coding: utf-8 -*-
"""k220 — people::professions (lô trộn): người, nghề, hoà giải, nghỉ việc, khái niệm mượn.

Chỗ cần nhất quán trong lô:
(1) мир- ở đây là HOÀ BÌNH (như ми́рный): мири́ться/помири́ться; nghĩa «cam chịu» chỉ có ở thẻ
    мири́ться (HT của nghĩa đó là примири́ться).
(2) у-вол-: giữ lời giải của уво́лить (k183) — у- RỜI KHỎI + вол- TỰ DO.
(3) -и́зм chủ nghĩa ↔ -и́ст người: như террори́зм/террори́ст (k204, k167).
(4) со́б- BẢN THÂN (со́бственный k156); труд- LAO ĐỘNG; зв- GỌI (призва́ть k212);
    вод- DẪN (провести́ k116); а́нгел «sứ giả» (k162).
(5) беременная: cùng gốc бре́мя (gánh nặng), KHÔNG gán với бере́чь.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "лысый": "hói, trọc, trụi lông",                  # «nhẵn trọc» không phải cách nói của bald
    "патриот": "người yêu nước",                      # «người nhiệt tình ủng hộ» nghĩa phụ, kéo sang сторонник/болельщик
    "мириться": "làm hòa, hòa giải, chịu đựng, cam chịu",  # thêm resign oneself to; tách терпеть
    "помириться": "làm hòa, hòa giải",                # cùng dãy với мириться, trừ nghĩa chỉ CHT có
    "проводник": "nhân viên toa tàu, người dẫn đường, chất dẫn điện",  # THIẾU conductor; «soát vé» = контролёр
    "собственник": "chủ sở hữu tài sản, chủ nhà, chủ đất",  # sát property owner / landowner; hết nuốt trọn владелец
    "трудиться": "lao động, làm việc vất vả, nhọc công",    # «cố gắng làm» = стараться; gloss là take the trouble
    "уволиться": "nghỉ việc, thôi việc",              # cùng dãy với увольняться, badge thể tách
    "увольняться": "nghỉ việc, thôi việc",
    "командовать": "chỉ huy, hô lệnh, sai khiến",     # «điều khiển» = управлять; «ra lệnh» nuốt trọn приказывать
}

# --------------------------------------------------------------------- косметика
S["косметика"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">косме́т-</span><span class="hd-gloss">LÀM ĐẸP — '
    'Hy Lạp <i>kosmein</i> «sắp cho gọn, trang điểm»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ик-а</span><span class="hd-gloss">đuôi mượn '
    '(= Anh <i>-ics</i>), giống cái — như <b>фи́зика</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>cosmetics</i>. Chung nguồn với <b>ко́смос</b> (<i>kosmos</i> = trật '
    'tự → vũ trụ): «sửa sang cho có trật tự» ⇒ làm đẹp, mỹ phẩm.</div>'
    '<div class="hd-warn">Anh để số nhiều, Nga dùng SỐ ÍT cho cả đống mỹ phẩm: <b>вся моя́ '
    'косме́тика</b>; dùng mỹ phẩm là <b>по́льзоваться косме́тикой</b> (cách 5).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>космети́ческий</b> thuộc mỹ phẩm · <b>космето́лог</b> chuyên viên '
    'thẩm mỹ · <b>ко́смос</b> vũ trụ</div>'
)

# --------------------------------------------------------------------- лысый
S["лысый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">лыс-</span><span class="hd-gloss">HÓI, trụi — '
    'gốc trơn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span><span class="hd-gloss">đuôi tính '
    'từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đầu không còn tóc ⇒ hói, trọc; chỗ rụng lông trên con vật cũng là '
    '<b>лы́сый</b>. Đứng một mình làm danh từ «người hói», vẫn chia như tính từ. Dạng ngắn chỉ '
    'giống cái nhảy trọng âm ra đuôi: <b>лыс</b>, <b>лыса́</b>, <b>лы́со</b>, <b>лы́сы</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лы́сина</b> chỗ hói, đầu hói · <b>лысе́ть</b> hói dần · '
    '<b>облысе́ть</b> hói hẳn</div>'
)

# --------------------------------------------------------------------- современник
S["современник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span><span class="hd-gloss">CÙNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-времен-</span><span class="hd-gloss">THỜI GIAN '
    '— <b>вре́мя</b>, thân <i>времен-</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ик</span><span class="hd-gloss">NGƯỜI — như '
    '<b>сотру́дник</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bỏ <b>-ый</b> của <b>совреме́нный</b>, thêm <b>-ик</b> (nên giữ hai chữ '
    '<i>н</i>) ⇒ người CÙNG THỜI. Cùng thời với AI là cách 2: <b>совреме́нник Пу́шкина</b>.</div>'
    '<div class="hd-warn">Anh dùng một chữ <i>contemporary</i> cho cả hai: tính từ là '
    '<b>совреме́нный</b>, NGƯỜI là <b>совреме́нник</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вре́мя</b> thời gian · <b>совреме́нный</b> hiện đại · '
    '<b>вре́менный</b> tạm thời</div>'
)

# --------------------------------------------------------------------- беременная
S["беременная"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бере́мен-</span><span class="hd-gloss">GÁNH, thứ '
    'mang theo — cùng gốc <b>бре́мя</b> gánh nặng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ая</span><span class="hd-gloss">đuôi tính từ '
    'giống cái, dùng như danh từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người đang mang» ⇒ phụ nữ có thai. Gốc xa chung với Anh <i>bear</i> '
    '(mang; sinh con) và <i>burden</i>. Là tính từ hoá danh từ nên chia như tính từ: '
    '<b>у бере́менной</b>, <b>мно́го бере́менных</b>.</div>'
    '<div class="hd-warn">Nói «cô ấy đang có thai» hay dùng dạng ngắn: <b>Она́ бере́менна</b>. '
    'Tháng thứ mấy là <b>на</b> + cách 6: <b>на пя́том ме́сяце</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бере́менность</b> thai kỳ · <b>забере́менеть</b> có thai · '
    '<b>бре́мя</b> gánh nặng</div>'
)

# --------------------------------------------------------------------- евангелие
S["евангелие"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ев-</span><span class="hd-gloss">TỐT LÀNH — Hy '
    'Lạp <i>eu-</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́нгел-</span><span class="hd-gloss">TIN BÁO — '
    'cùng gốc <b>а́нгел</b> «sứ giả, người báo tin»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ие</span><span class="hd-gloss">đuôi danh từ '
    'giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Tin lành» ⇒ Phúc Âm. Tiếng Anh <i>gospel</i> là bản dịch từng mảnh y '
    'như vậy: <i>god</i> (cổ: tốt) + <i>spel</i> (tin). Trọng âm giữ đúng chỗ của '
    '<b>а́нгел</b>.</div>'
    '<div class="hd-warn">Chỉ cuốn sách thánh thì viết HOA. «Phúc Âm THEO ai» là <b>от</b> + '
    'cách 2: <b>Ева́нгелие от Матфе́я</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>а́нгел</b> thiên thần · <b>ева́нгельский</b> thuộc Phúc Âm · '
    '<b>евангели́ст</b> người chép Phúc Âm</div>'
)

# --------------------------------------------------------------------- расизм
S["расизм"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рас-</span><span class="hd-gloss">CHỦNG TỘC — '
    '<b>ра́са</b> (= Anh <i>race</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́зм</span><span class="hd-gloss">= <i>-ism</i>: '
    'chủ nghĩa</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>racism</i>. <b>-и́зм</b> luôn nhận trọng âm và là giống đực, như '
    '<b>террори́зм</b>. Đổi <b>-и́зм</b> thành <b>-и́ст</b> là ra NGƯỜI: <b>раси́ст</b>.</div>'
    '<div class="hd-warn"><i>рас-</i> ở đây là GỐC, không phải tiền tố <b>рас-</b> «tách ra» của '
    '<b>расста́ться</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ра́са</b> chủng tộc · <b>раси́ст</b> kẻ phân biệt chủng tộc · '
    '<b>ра́совый</b> thuộc chủng tộc · <b>раси́стский</b> mang tính phân biệt chủng tộc</div>'
)

# --------------------------------------------------------------------- патриот
S["патриот"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn, gốc Hy Lạp <i>patriōtēs</i> «người cùng quê cha», từ '
    '<i>patēr</i> cha; không chẻ ra mảnh Nga được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người gắn với «đất cha» ⇒ người yêu nước = <i>patriot</i>, nhưng tiếng '
    'Nga nhấn CUỐI: <b>патрио́т</b>. Yêu CÁI GÌ là cách 2: <b>патрио́т свое́й '
    'страны́</b>.</div>'
    '<div class="hd-warn">Cũng nói cho thứ nhỏ hơn tổ quốc: <b>патрио́т своего́ го́рода</b> = '
    'người hết lòng với thành phố mình.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>патриоти́зм</b> lòng yêu nước · <b>патриоти́ческий</b> yêu nước · '
    '<b>патрио́тка</b> người yêu nước (nữ)</div>'
)

# --------------------------------------------------------------------- расист
S["расист"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рас-</span><span class="hd-gloss">CHỦNG TỘC — '
    '<b>ра́са</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ст</span><span class="hd-gloss">NGƯỜI theo (= '
    '<i>-ist</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>racist</i>: người theo <b>раси́зм</b>. <b>-и́ст</b> luôn nhận trọng '
    'âm, như <b>тури́ст</b>, <b>террори́ст</b>. Phụ nữ: <b>раси́стка</b>.</div>'
    '<div class="hd-warn"><b>раси́ст</b> chỉ là NGƯỜI; «mang tính phân biệt chủng tộc» là tính từ '
    '<b>раси́стский</b>. Tiếng Anh dùng một chữ <i>racist</i> cho cả hai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>раси́зм</b> sự phân biệt chủng tộc · <b>ра́са</b> chủng tộc · '
    '<b>ра́совый</b> thuộc chủng tộc</div>'
)

# --------------------------------------------------------------------- подружиться
S["подружиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span><span class="hd-gloss">chỉ biến thành '
    'HT, không nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-друж-и́ть-</span><span class="hd-gloss">LÀM BẠN '
    '— <b>дружи́ть</b> (<b>друг</b>, <i>г → ж</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span><span class="hd-gloss">với '
    'nhau</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trở thành <b>друг</b> của nhau ⇒ kết bạn. <b>дружи́ть</b> là ĐANG là bạn '
    'của nhau, <b>подружи́ться</b> là lúc BẮT ĐẦU thành bạn. Ngôi «tôi» nhấn đuôi, các ngôi khác '
    'lùi về gốc: <b>подружу́сь</b>, <b>подру́жишься</b>, <b>подру́жатся</b>.</div>'
    '<div class="hd-warn">Với AI: <b>с</b> + cách 5 — <b>Я подружи́лась с сосе́дкой</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>друг</b> bạn · <b>дружи́ть</b> chơi thân · <b>дру́жба</b> tình bạn · '
    '<b>дру́жный</b> hoà thuận</div>'
)

# --------------------------------------------------------------------- мириться
S["мириться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мир-</span><span class="hd-gloss">HOÀ BÌNH — '
    '<b>мир</b>, như <b>ми́рный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́-ть-ся</span><span class="hd-gloss">đuôi lớp 2 '
    '+ <b>-ся</b> với nhau</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lập lại <b>мир</b> với nhau ⇒ làm hoà; «làm hoà» với một điều khó chịu '
    '⇒ đành chịu đựng. Trọng âm luôn ở đuôi: <b>мирю́сь</b>, <b>мири́шься</b>. Bỏ <b>-ся</b>: '
    '<b>мири́ть</b> là giảng hoà cho người khác.</div>'
    '<div class="hd-warn">Cả hai nghĩa đều đi <b>с</b> + cách 5: với NGƯỜI là làm hoà '
    '(<b>мири́ться с бра́том</b>), với VIỆC là cam chịu (<b>мири́ться с шу́мом</b>).</div>'
    '<div class="hd-warn">Hai nghĩa, hai vế HT: làm hoà → <b>помири́ться</b>; cam chịu → '
    '<b>примири́ться</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мир</b> hoà bình; thế giới · <b>ми́рный</b> hoà bình · '
    '<b>переми́рие</b> đình chiến</div>'
)

# --------------------------------------------------------------------- помириться
S["помириться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span><span class="hd-gloss">chỉ biến thành '
    'HT, không nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мир-и́ть-</span><span class="hd-gloss">HOÀ BÌNH '
    '— <b>мир</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span><span class="hd-gloss">với '
    'NHAU</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vế HT của <b>мири́ться</b>, và là vế ngược của <b>поссо́риться</b> (cãi '
    'nhau, giận nhau): <b>Они́ поссо́рились, но бы́стро помири́лись</b>. Trọng âm luôn ở đuôi: '
    '<b>помирю́сь</b>, <b>помири́шься</b>.</div>'
    '<div class="hd-warn">Với AI: <b>с</b> + cách 5 — <b>Помири́сь с ма́мой!</b> Chỉ là «làm '
    'hoà», không mang nghĩa «cam chịu» của <b>мири́ться</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мири́ться</b> (CHT) · <b>мир</b> hoà bình; thế giới · '
    '<b>ми́рный</b> hoà bình</div>'
)

# --------------------------------------------------------------------- нищета
S["нищета"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">нищ-</span><span class="hd-gloss">CÙNG KHỔ — '
    '<b>ни́щий</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ет-а́</span><span class="hd-gloss">tính từ → '
    'danh từ «tính chất»: chính là <b>-ота́</b> của <b>красота́</b>, sau <i>щ</i> viết '
    '<i>е</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái tình trạng <b>ни́щий</b> ⇒ cảnh bần cùng. Trọng âm bỏ gốc, dồn ra '
    'đuôi ở mọi cách: <b>ни́щий</b> → <b>нищета́</b>, <b>в нищете́</b>. Chỉ có số ít.</div>'
    '<div class="hd-warn">Nặng hơn <b>бе́дность</b> một bậc, y như <b>ни́щий</b> so với '
    '<b>бе́дный</b>: <b>жить в нищете́</b> = không có cả thứ tối thiểu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ни́щий</b> bần cùng; kẻ ăn xin · <b>ни́щенский</b> bèo bọt (lương, mức '
    'sống) · <b>обнища́ть</b> khánh kiệt</div>'
)

# --------------------------------------------------------------------- призвание
S["призвание"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span><span class="hd-gloss">TỚI, về phía '
    'mình</span></div>'
    '<div class="hd-row"><span class="hd-piece">-зва́-</span><span class="hd-gloss">GỌI — '
    '<b>звать</b>, <b>призва́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ние</span><span class="hd-gloss">→ danh từ giống '
    'trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Công việc «GỌI ta tới» ⇒ thiên hướng, sứ mệnh. Anh dựng y hệt: '
    '<i>calling</i> (call = gọi), <i>vocation</i> (Latin <i>vocare</i> gọi). <b>врач по '
    'призва́нию</b> = bác sĩ bẩm sinh, sinh ra để làm nghề này.</div>'
    '<div class="hd-warn">Lệch một chữ là khác gốc: <b>призна́ние</b> (<i>н</i> thay <i>в</i> — '
    '<b>знать</b> biết) = sự thú nhận, sự công nhận.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>призва́ть</b> kêu gọi · <b>звать</b> gọi · <b>назва́ние</b> tên gọi · '
    '<b>зва́ние</b> danh hiệu, cấp bậc</div>'
)

# --------------------------------------------------------------------- бомж
S["бомж"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Chữ viết tắt trong giấy tờ công an: <b>без определённого ме́ста '
    'жи́тельства</b> — «không có nơi cư trú nhất định».</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bốn chữ đầu dính thành một từ thường, có chia hẳn hoi. Trọng âm dồn ra '
    'đuôi ở mọi dạng có đuôi: <b>бомжа́</b>, <b>бомжо́м</b>, <b>бомжи́</b>, '
    '<b>бомже́й</b>.</div>'
    '<div class="hd-warn">Là khẩu ngữ, nghe khinh miệt. Lịch sự hơn: <b>бездо́мный</b> «không '
    'nhà».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ме́сто</b> chỗ · <b>жи́тельство</b> sự cư trú · <b>бомжи́ха</b> người '
    'vô gia cư (nữ)</div>'
)

# --------------------------------------------------------------------- проводник
S["проводник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span><span class="hd-gloss">QUA, xuyên '
    'suốt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вод-</span><span class="hd-gloss">DẪN — '
    '<b>води́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ни́к</span><span class="hd-gloss">NGƯỜI / vật '
    'làm việc đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Kẻ DẪN QUA: đi theo khách suốt chuyến ⇒ nhân viên toa tàu; dẫn qua rừng '
    'núi ⇒ người dẫn đường; dẫn dòng điện qua ⇒ chất dẫn điện. Anh <i>conductor</i> (Latin '
    '<i>ducere</i> dẫn) cũng gộp tàu và điện. Trọng âm ra đuôi: <b>проводника́</b>, '
    '<b>проводнико́м</b>, <b>проводники́</b>.</div>'
    '<div class="hd-warn">Trên tàu đường dài Nga, mỗi toa có người lo vé, giường, trà; phụ nữ là '
    '<b>проводни́ца</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>проводи́ть</b> dẫn qua, tiến hành · <b>провести́</b> (HT) · '
    '<b>про́вод</b> dây điện · <b>води́тель</b> tài xế</div>'
)

# --------------------------------------------------------------------- собственник
S["собственник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со́б-</span><span class="hd-gloss">BẢN THÂN — '
    'cùng gốc <b>себя́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ств-енн-</span><span class="hd-gloss">phần đuôi '
    'của <b>со́бственный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ик</span><span class="hd-gloss">NGƯỜI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bỏ <b>-ый</b> của <b>со́бственный</b> «của riêng mình», thêm <b>-ик</b> ⇒ '
    'người có tài sản của riêng mình. Trọng âm đứng yên ở đầu từ. Chủ của CÁI GÌ là cách 2: '
    '<b>со́бственник кварти́ры</b>.</div>'
    '<div class="hd-warn"><b>со́бственник</b> là chủ trên GIẤY TỜ, có quyền sở hữu; người đứng ra '
    'làm chủ, quán xuyến là <b>хозя́ин</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>со́бственный</b> của riêng mình · <b>со́бственность</b> tài sản, quyền '
    'sở hữu · <b>себя́</b> bản thân</div>'
)

# --------------------------------------------------------------------- парикмахер
S["парикмахер"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">парик-</span><span class="hd-gloss">TÓC GIẢ — '
    'Đức <i>Perücke</i>; Nga có <b>пари́к</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ма́хер</span><span class="hd-gloss">NGƯỜI LÀM — '
    'Đức <i>Macher</i> (= Anh <i>maker</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn tiếng Đức <i>Perückenmacher</i> «thợ làm tóc giả», nghề thời quý '
    'tộc đội tóc giả ⇒ nay là thợ cắt tóc. Trọng âm ở <b>-ма́-</b>, đứng yên cả bảng.</div>'
    '<div class="hd-warn">Nữ cũng thường gọi là <b>парикма́хер</b>. Tiệm cắt tóc là '
    '<b>парикма́херская</b>, chia như tính từ: <b>идти́ в парикма́херскую</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пари́к</b> tóc giả · <b>парикма́херская</b> tiệm cắt tóc</div>'
)

# --------------------------------------------------------------------- трудиться
S["трудиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">труд-</span><span class="hd-gloss">LAO ĐỘNG, công '
    'sức — <b>труд</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́-ть-ся</span><span class="hd-gloss">đuôi lớp 2 '
    '+ <b>-ся</b> tự mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tự bỏ <b>труд</b> ra ⇒ lao động, làm vất vả; trang trọng và nặng nhọc '
    'hơn <b>рабо́тать</b>. Ngôi «tôi» <i>д → ж</i>, các ngôi khác giữ <i>д</i> và lùi trọng âm: '
    '<b>тружу́сь</b>, <b>тру́дишься</b>, <b>тру́дятся</b>.</div>'
    '<div class="hd-warn">Miệt mài VỚI việc gì: <b>над</b> + cách 5 — <b>труди́ться над '
    'кни́гой</b>.</div>'
    '<div class="hd-warn"><b>Не труди́тесь!</b> — xin đừng bận tâm, khỏi nhọc công.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>труд</b> lao động · <b>тру́дный</b> khó · <b>сотру́дник</b> nhân viên · '
    '<b>трудолюби́вый</b> chăm chỉ</div>'
)

# --------------------------------------------------------------------- уволиться
S["уволиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span><span class="hd-gloss">RỜI '
    'KHỎI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вол-</span><span class="hd-gloss">TỰ DO, Ý MUỐN '
    '— <b>во́ля</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить-ся</span><span class="hd-gloss">đuôi động từ '
    '+ <b>-ся</b> tự mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>уво́лить</b> là sa thải («thả về tự do»); thêm <b>-ся</b> là TỰ thả '
    'mình ⇒ xin nghỉ việc. Trọng âm đứng yên: <b>уво́люсь</b>, <b>уво́лишься</b>. Nghỉ Ở ĐÂU: '
    '<b>с</b> / <b>из</b> + cách 2 — <b>уво́литься с рабо́ты</b>. Cặp CHT: '
    '<b>увольня́ться</b>.</div>'
    '<div class="hd-warn">Công thức trong đơn xin thôi việc: <b>уво́литься по со́бственному '
    'жела́нию</b> — nghỉ theo nguyện vọng cá nhân.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уво́лить</b> sa thải · <b>увольне́ние</b> sự cho thôi việc · '
    '<b>во́ля</b> ý muốn, tự do</div>'
)

# --------------------------------------------------------------------- увольняться
S["увольняться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span><span class="hd-gloss">RỜI '
    'KHỎI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вольн-</span><span class="hd-gloss">TỰ DO — '
    '<b>во́ля</b>, có thêm <i>н</i> như <b>во́льный</b> tự do</span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ть-ся</span><span class="hd-gloss">đuôi CHƯA '
    'hoàn thành + <b>-ся</b> tự mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vế CHT của <b>уво́литься</b>: đang làm thủ tục nghỉ, hoặc nghỉ nhiều '
    'lần. Chia đều: <b>увольня́юсь</b>, <b>увольня́ешься</b>. Hiện tại hay báo một việc sắp '
    'làm: <b>Я увольня́юсь</b> — tôi (sắp) nghỉ việc đây.</div>'
    '<div class="hd-warn">Có <b>-ся</b> là TỰ nghỉ, không <b>-ся</b> là bị đuổi: <b>Он '
    'увольня́ется</b> anh ấy xin nghỉ; <b>Его́ увольня́ют</b> anh ấy bị cho thôi việc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уво́литься</b> (HT) · <b>увольня́ть</b> sa thải (CHT) · '
    '<b>увольне́ние</b> sự cho thôi việc · <b>во́ля</b> ý muốn, tự do</div>'
)

# --------------------------------------------------------------------- командовать
S["командовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кома́нд-</span><span class="hd-gloss">MỆNH LỆNH; '
    'ĐỘI — <b>кома́нда</b> (= Anh <i>command</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ов-ать</span><span class="hd-gloss">đuôi biến '
    'danh từ thành động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hô <b>кома́нда</b> «khẩu lệnh», rồi nắm cả đội ⇒ chỉ huy. <b>-ова-</b> '
    'đổi thành <b>-у-</b> khi chia: <b>кома́ндую</b>, <b>кома́ндуешь</b>. Trọng âm giữ chỗ của '
    '<b>кома́нда</b>.</div>'
    '<div class="hd-warn">Chỉ huy AI là cách 5: <b>кома́ндовать полко́м</b>; còn '
    '<b>прика́зывать</b> đi cách 3.</div>'
    '<div class="hd-warn">Ngoài quân đội là «sai khiến», ý chê: <b>Не кома́ндуй мной!</b> — đừng '
    'có chỉ tay năm ngón với tôi!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кома́нда</b> đội; khẩu lệnh · <b>команди́р</b> người chỉ huy · '
    '<b>командиро́вка</b> chuyến công tác</div>'
)

B = {"docbangmat": 113, "loitubat": 4, "nguonsai": 1, "baolen": [
    "командовать: bỏ «ra lệnh» khỏi V dù gloss có give orders, thay «hô lệnh, sai khiến» để không nuốt trọn приказывать [k135]; câu ví dụ 3 của thẻ vẫn dịch «ra lệnh» — cần duyệt",
    "собственник: «chủ sở hữu» → «chủ sở hữu tài sản» (property owner), bỏ «người có tài sản», thêm «chủ đất» (landowner); владелец giữ nguyên",
    "патриот: bỏ «người nhiệt tình ủng hộ» dù gloss có supporter — nghĩa phụ (патриот своего города, đã ghi ở ô đỏ), để lại thì đề trỏ nhầm сторонник/болельщик",
    "проводник: bỏ «người soát vé trên tàu» (dễ thành контролёр), thêm «chất dẫn điện»; ví dụ không có câu nào cho nghĩa dẫn điện/dẫn đường",
    "лысый: «nhẵn trọc» → «trọc»; GIỮ «trụi lông» vì câu ví dụ con mèo in đậm đúng nghĩa đó",
    "уволиться/увольняться: cùng dãy «nghỉ việc, thôi việc», chỉ badge thể tách; помириться là dãy con của мириться, badge thể tách",
    "Ví dụ nguồn (ngoài phạm vi file này): косметика câu 3 dùng số nhiều «в косметиках» — không tự nhiên, từ này thường chỉ dùng số ít; евангелие cả ba câu viết thường, tên sách thánh nên viết hoa",
    "бомж: gloss «good catch / eligible bachelor / Prince Charming» là nghĩa đùa, đã bác, nên xoá khỏi field English",
    "Chẻ увольняться ghi -вольн- (có н như вольный); thẻ увольнять [k183] ghi -воль- + -ять, bỏ sót chữ н — thẻ ngoài lô, chưa sửa",
    "Không chắc tuyệt đối: увольнять lấy н từ вольный là suy từ hình thái, thẻ chỉ nói «như вольный»",
]}
