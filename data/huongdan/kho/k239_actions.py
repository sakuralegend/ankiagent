# -*- coding: utf-8 -*-
"""k239 — actions: tính từ thời gian (thường ngày, chủ nhật, trước hạn…), khoảng/thời lượng/chỉ số; giành, tưới, làm nốt, chạy tới.

Chỗ cần nhất quán trong lô:
(1) одержа́ть / оде́рживать: -держ- GIỮ, CẦM — khớp держа́ть [k94], поддержа́ть [k176], содержа́ние [k165]; о- nói thẳng không tách nghĩa.
(2) поли́ть / полива́ть: -ли- ĐỔ, RÓT — khớp нали́ть, налива́ть [k213]; по- phủ LÊN mặt, viết y hệt ở hai thẻ.
(3) доде́лать / доде́лывать: до- TỚI TẬN + -де́л- VIỆC [k01]. прибежа́ть / пробежа́ть: khuôn убежа́ть [k131].
(4) предше́ствовать: -шеств- ĐI, BƯỚC (gốc cổ) — khớp путеше́ствовать [k107]. продолжи́тельность ↔ продолже́ние [k200].
(5) воскре́сный: вос-крес- [k45]. досро́чный ↔ сро́чный [k161]. наиме́нее ↔ наибо́лее, ме́нее [k116].
(6) разбива́ть ↔ разби́ть [k80]. препя́тствовать ↔ препя́тствие [k189]. -днев- ↔ ежедне́вный [k147].
Họ hàng không vắng ở thẻ nào.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "античный": "cổ đại, thời cổ đại, thuộc Hy Lạp La Mã cổ đại",       # bỏ «cổ điển» (va класси́ческий [k73]); classical = Hy–La
    "интервал": "khoảng cách, khoảng thời gian, khoảng nghỉ",           # «quãng ngắt» lạ tai; câu 2–3 dịch «khoảng nghỉ»
    "индекс": "chỉ số, mã bưu chính",                                   # «mục lục» là содержа́ние [k165], câu ví dụ không dùng
    "разбивать": "làm vỡ, đập vỡ, chia nhỏ",                            # «làm tan» mơ hồ; cùng dãy cặp HT разби́ть [k80]
    "одержать": "giành được, giành chiến thắng, giành phần thắng",      # bỏ «đạt được» (từ này chỉ đi với побе́ду / верх)
    "одерживать": "giành được, giành chiến thắng, giành phần thắng",    # bỏ «thắng» (va выи́грывать [k122]); cặp thể cùng dãy
    "поливать": "tưới, rưới lên, dội lên",                              # cặp thể cùng dãy (theo đề của поли́ть)
    "полить": "tưới, rưới lên, dội lên",                                # giữ nguyên, khai để cặp thể cùng dãy
    "доделать": "làm cho xong, làm nốt, hoàn thành nốt",                # «kết thúc», «làm xong» là зако́нчить
    "доделывать": "làm cho xong, làm nốt, hoàn thành nốt",              # cặp thể cùng dãy; câu 2 dịch «làm nốt»
}

# --------------------------------------------------------------------- повседневный
S["повседневный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">THEO, trải khắp</span></div>'
    '<div class="hd-row"><span class="hd-piece">-все-</span>'
    '<span class="hd-gloss">MỌI — <b>все</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-днев-</span>'
    '<span class="hd-gloss">NGÀY — <b>день</b>, như ở <b>ежедне́вный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">→ tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Trải theo mọi ngày» ⇒ thường ngày, đời thường: <b>повседне́вная жизнь</b> đời sống thường '
    'ngày. Dạng ngắn giống đực chen <b>е</b>: <b>повседне́вен</b>, còn lại thì không: <b>повседне́вна</b>.</div>'
    '<div class="hd-warn">Ba từ gần nhau: <b>ежедне́вный</b> lặp lại ngày nào cũng có (chuyến bay, báo) · '
    '<b>повседне́вный</b> bình thường, không phải dịp đặc biệt · <b>бу́дничный</b> đều đều, tẻ nhạt.</div>'
    '<div class="hd-warn"><b>повседне́вная оде́жда</b> = quần áo mặc thường ngày.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>день</b> ngày · <b>ежедне́вный</b> hằng ngày · <b>дневно́й</b> ban ngày · '
    '<b>повседне́вность</b> đời thường</div>'
)

# --------------------------------------------------------------------- воскресный
S["воскресный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вос-</span>'
    '<span class="hd-gloss">LÊN, TRỞ LẠI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-крес-</span>'
    '<span class="hd-gloss">gốc SỐNG LẠI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">→ tính từ, thế chỗ <b>-енье</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lấy <b>воскресе́нье</b> chủ nhật, bỏ <b>-енье</b>, lắp <b>-ный</b> ⇒ của ngày chủ nhật: '
    '<b>воскре́сный день</b>. Trọng âm lùi một âm: <b>воскресе́нье</b> → <b>воскре́сный</b>. Dạng ngắn trong bảng '
    'thực tế không dùng.</div>'
    '<div class="hd-warn">Từ này chỉ đứng trước danh từ. «VÀO chủ nhật» thì dùng danh từ: <b>в воскресе́нье</b>; «cứ '
    'chủ nhật» là <b>по воскресе́ньям</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>воскресе́нье</b> chủ nhật · <b>воскресе́ние</b> sự sống lại · <b>воскре́снуть</b> sống '
    'lại</div>'
)

# --------------------------------------------------------------------- античный
S["античный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">анти́ч-</span>'
    '<span class="hd-gloss">CỔ — Latin <i>antiquus</i>, к → ч</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">→ tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc với <i>antique</i> nhưng nghĩa hẹp hơn: thuộc thế giới Hy Lạp – La Mã cổ đại — '
    '<b>анти́чный теа́тр</b>, <b>анти́чные ми́фы</b>. Xưa nói chung, nền văn minh nào cũng được, là <b>дре́вний</b>: '
    '<b>Дре́вний Еги́пет</b>. Dạng ngắn hầu như không dùng.</div>'
    '<div class="hd-warn">Mảnh đầu KHÔNG phải <b>анти-</b> «chống» của <b>антиви́рус</b>, chỉ trùng mặt chữ.</div>'
    '<div class="hd-warn">Đồ cổ để bán, sưu tầm có tính từ riêng: <b>антиква́рный магази́н</b> tiệm đồ cổ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>анти́чность</b> thời cổ đại Hy – La · <b>антиква́р</b> người buôn đồ cổ · '
    '<b>антиква́рный</b> (thuộc) đồ cổ</div>'
)

# --------------------------------------------------------------------- досрочный
S["досрочный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TRƯỚC — giới từ <b>до</b> «trước, cho tới»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сроч-</span>'
    '<span class="hd-gloss">THỜI HẠN — <b>срок</b> (к → ч)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">→ tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Trước hạn» — dịch đúng từng mảnh. Đi với việc có hạn ấn định: <b>досро́чный экза́мен</b> kỳ '
    'thi trước hạn, <b>досро́чные вы́боры</b> bầu cử sớm. Trạng từ: <b>досро́чно</b>. Dạng ngắn hầu như không '
    'dùng.</div>'
    '<div class="hd-warn">«Sớm» theo giờ giấc, theo mùa thì chẳng có hạn nào ⇒ <b>ра́нний</b>: <b>ра́нний '
    'за́втрак</b> bữa sáng sớm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>срок</b> thời hạn · <b>сро́чный</b> gấp · <b>сро́чно</b> gấp (trạng từ) · '
    '<b>просро́чить</b> để quá hạn</div>'
)

# --------------------------------------------------------------------- интервал
S["интервал"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">интер-</span>'
    '<span class="hd-gloss">GIỮA — như <i>inter-</i> tiếng Anh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва́л</span>'
    '<span class="hd-gloss">bờ luỹ — Latin <i>vallum</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vốn là «khoảng giữa hai bờ luỹ» ⇒ khoảng cách giữa hai vật, hai lúc. Chính là '
    '<i>interval</i>, trọng âm dồn về cuối. Giữa những gì thì <b>ме́жду</b> + cách 5: <b>интерва́л ме́жду '
    'авто́бусами</b>.</div>'
    '<div class="hd-warn">Khuôn phải thuộc: <b>с интерва́лом в</b> + cách 4 — <b>с интерва́лом в пять мину́т</b> cứ '
    'cách năm phút.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>интерва́льный</b> ngắt quãng · <b>интерне́т</b> mạng nối GIỮA các mạng · '
    '<b>интернациона́льный</b> quốc tế (GIỮA các nước)</div>'
)

# --------------------------------------------------------------------- предшествовать
S["предшествовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пред-</span>'
    '<span class="hd-gloss">TRƯỚC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-шеств-</span>'
    '<span class="hd-gloss">ĐI, BƯỚC (gốc cổ)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ть</span>'
    '<span class="hd-gloss">đuôi động từ: <b>-ова-</b> → <b>-у-</b> khi chia</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đi phía trước» ⇒ có trước, xảy ra trước; ghép y như Anh <i>pre-cede</i>. Chia như '
    '<b>путеше́ствовать</b>: <b>предше́ствую, предше́ствует</b>. Giọng sách vở, chỉ có CHT.</div>'
    '<div class="hd-warn">Trước CÁI GÌ → cách 3, không giới từ: <b>Грозе́ предше́ствовал ве́тер.</b> Trước cơn dông '
    'là gió.</div>'
    '<div class="hd-warn">⚠️ Mức tin: <b>-шеств-</b> «đi» là từ nguyên (cùng <b>шёл</b>, quá khứ của <b>идти́</b>), '
    'dùng để nhớ. Không dính <b>шесть</b> sáu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>путеше́ствовать</b> du lịch · <b>предше́ственник</b> người đi trước · '
    '<b>происше́ствие</b> sự cố · <b>предыду́щий</b> trước đó</div>'
)

# --------------------------------------------------------------------- продолжительность
S["продолжительность"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">kéo tiếp về phía trước</span></div>'
    '<div class="hd-row"><span class="hd-piece">-долж-</span>'
    '<span class="hd-gloss">gốc DÀI — của <b>до́лгий</b>, г hoá ж</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́тельн-</span>'
    '<span class="hd-gloss">→ tính từ: <b>продолжи́тельный</b> kéo dài</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span>'
    '<span class="hd-gloss">→ danh từ giống cái «độ…»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Độ kéo dài» ⇒ thời lượng. Dựng từ <b>продолжи́тельный</b>, trọng âm giữ nguyên chỗ. Chỉ đo '
    'THỜI GIAN; chiều dài của vật là <b>длина́</b>. Dùng ở số ít.</div>'
    '<div class="hd-warn"><b>продолжи́тельность жи́зни</b> = tuổi thọ — gặp suốt trong báo chí.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>продолжа́ть</b> tiếp tục · <b>продолже́ние</b> phần tiếp theo · <b>до́лгий</b> lâu, dài · '
    '<b>до́лго</b> lâu</div>'
)

# --------------------------------------------------------------------- наименее
S["наименее"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">наи-</span>'
    '<span class="hd-gloss">tiền tố CỰC CẤP: nhất</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ме́нее</span>'
    '<span class="hd-gloss"><b>ме́нее</b> ít hơn, kém hơn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Kém hơn hết thảy» ⇒ ít nhất. Vế đối của <b>наибо́лее</b>, đặt trước tính từ như '
    '<i>least</i>: <b>наиме́нее удо́бный рейс</b> chuyến bay ít tiện nhất. Giọng sách vở.</div>'
    '<div class="hd-warn">«Ít nhất cũng phải…» (mức tối thiểu) KHÔNG dùng từ này mà nói <b>ми́нимум</b> hoặc <b>по '
    'кра́йней ме́ре</b>: <b>ми́нимум два часа́</b> ít nhất hai tiếng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ме́нее</b> ít hơn · <b>ме́ньше</b> ít hơn · <b>наибо́лее</b> nhất · <b>меньшинство́</b> '
    'thiểu số</div>'
)

# --------------------------------------------------------------------- индекс
S["индекс"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn Latin (<i>index</i>), không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng chữ <i>index</i> (Latin «cái chỉ trỏ») ⇒ con số CHỈ ra mức độ: chỉ số; con số CHỈ ra '
    'địa bàn: mã bưu chính. Trọng âm đứng yên ở <b>и́н-</b>.</div>'
    '<div class="hd-warn">Trên phong bì, <b>и́ндекс</b> nói trống là mã bưu chính (đủ chữ: <b>почто́вый и́ндекс</b>) '
    '— chỗ này tiếng Anh nói <i>postcode</i>, không nói <i>index</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>индекса́ция</b> việc điều chỉnh theo chỉ số (lương, lương hưu) · <b>индика́тор</b> cái '
    'chỉ báo, đèn báo</div>'
)

# --------------------------------------------------------------------- разбивать
S["разбивать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span>'
    '<span class="hd-gloss">TÁCH RA từng mảnh, ra các phía</span></div>'
    '<div class="hd-row"><span class="hd-piece">-би-</span>'
    '<span class="hd-gloss">gốc ĐÁNH, ĐẬP — <b>бить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>разбива́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đánh cho TÁCH RA ⇒ đập vỡ; nghĩa bóng: tách một khối thành phần. Cặp HT <b>разби́ть</b> chia '
    'lệch (<b>разобью́</b>), còn thể này thì đều.</div>'
    '<div class="hd-warn">Chia thành phần → <b>на</b> + cách 4: <b>разбива́ть класс на гру́ппы</b> chia lớp thành '
    'nhóm.</div>'
    '<div class="hd-warn">Đồ vật TỰ vỡ thì thêm <b>-ся</b>: <b>Ча́шки ча́сто разбива́ются.</b> Cốc hay bị vỡ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>разби́ть</b> (HT) · <b>бить</b> đánh, đập · <b>разби́тый</b> vỡ tan · <b>уби́ть</b> '
    'giết</div>'
)

# --------------------------------------------------------------------- одержать
S["одержать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không tách nghĩa rõ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-держ-</span>'
    '<span class="hd-gloss">GIỮ, CẦM — <b>держа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể, chia lớp THỨ HAI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nắm giữ được phần thắng ⇒ giành được. Trọng âm chạy như <b>держа́ть</b>: <b>одержу́</b> '
    'nhưng <b>оде́ржишь, оде́ржат</b>. Cặp CHT: <b>оде́рживать</b>.</div>'
    '<div class="hd-warn">Gần như chỉ sống trong hai cụm: <b>одержа́ть побе́ду</b> giành chiến thắng · <b>одержа́ть '
    'верх</b> giành phần thắng. Trước AI → <b>над</b> + cách 5: <b>одержа́ть побе́ду над Испа́нией</b>.</div>'
    '<div class="hd-warn">Thắng TRẬN, trúng GIẢI thì dùng <b>вы́играть</b>: <b>вы́играть матч</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>держа́ть</b> cầm, giữ · <b>поддержа́ть</b> ủng hộ, đỡ · <b>содержа́ние</b> nội dung · '
    '<b>одержи́мый</b> bị ám ảnh</div>'
)

# --------------------------------------------------------------------- одерживать
S["одерживать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không tách nghĩa rõ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-де́рж-</span>'
    '<span class="hd-gloss">GIỮ, CẦM — <b>держа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>оде́рживаю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>одержа́ть</b>: giành được nhiều lần, hoặc đang giành. Thêm <b>-ива-</b> thì '
    'trọng âm lùi về gốc: <b>одержа́ть</b> → <b>оде́рживать</b>, như <b>подде́рживать</b>.</div>'
    '<div class="hd-warn">Cũng chỉ đi với <b>побе́ду</b> và <b>верх</b>: <b>оде́рживать побе́ду за побе́дой</b> thắng '
    'hết trận này đến trận khác.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>одержа́ть</b> (HT) · <b>держа́ть</b> cầm, giữ · <b>подде́рживать</b> ủng hộ · '
    '<b>содержа́ние</b> nội dung</div>'
)

# --------------------------------------------------------------------- поливать
S["поливать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">phủ LÊN mặt, như ở <b>покры́ть</b> che phủ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ли-</span>'
    '<span class="hd-gloss">ĐỔ, RÓT — <b>лить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>полива́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đổ nước lên khắp mặt ⇒ tưới, rưới. Cặp HT: <b>поли́ть</b>. Danh từ: <b>поли́в</b> việc '
    'tưới.</div>'
    '<div class="hd-warn">Cách 4 là CÁI ĐƯỢC TƯỚI, chất tưới để cách 5: <b>полива́ть цветы́ водо́й</b>. Ngược với '
    '<b>налива́ть</b>, nơi cách 4 là chất lỏng: <b>налива́ть во́ду в стака́н</b>.</div>'
    '<div class="hd-warn">Không dính <b>поли́тика</b> chính trị (gốc Hy Lạp), chỉ giống mặt chữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поли́ть</b> (HT) · <b>лить</b> đổ, rót · <b>налива́ть</b> rót · <b>ли́вень</b> mưa '
    'rào</div>'
)

# --------------------------------------------------------------------- полить
S["полить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">phủ LÊN mặt, như ở <b>покры́ть</b> che phủ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ли́-ть</span>'
    '<span class="hd-gloss">ĐỔ, RÓT — <b>лить</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp HT của <b>полива́ть</b>: tưới xong, rưới lên. Cùng cách dùng: cách 4 là cái được tưới, '
    'cách 5 là chất tưới — <b>поли́ть сала́т ма́слом</b>.</div>'
    '<div class="hd-warn"><b>и</b> của gốc biến thành <b>ь</b>, y như <b>пить → пью</b>: <b>полью́, польёшь</b>; sai '
    'khiến <b>поле́й</b>. Quá khứ giống cái nhảy ra đuôi: <b>полила́</b>.</div>'
    '<div class="hd-warn">Nói về mưa, <b>по-</b> lại là BẮT ĐẦU: <b>Поли́л дождь.</b> Mưa trút xuống.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>полива́ть</b> (CHT) · <b>лить</b> đổ, rót · <b>нали́ть</b> rót · <b>проли́ть</b> làm '
    'đổ</div>'
)

# --------------------------------------------------------------------- препятствовать
S["препятствовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">препя́т-</span>'
    '<span class="hd-gloss">gốc CẢN — cổ, không nối được sang từ quen</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ств-</span>'
    '<span class="hd-gloss">như ở danh từ <b>препя́тствие</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ть</span>'
    '<span class="hd-gloss">đuôi động từ: <b>-ова-</b> → <b>-у-</b> khi chia</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Động từ của <b>препя́тствие</b> trở ngại ⇒ gây trở ngại. Chia: <b>препя́тствую, '
    'препя́тствует</b>, trọng âm đứng yên ở <b>-пя́-</b>. Cặp HT: <b>воспрепя́тствовать</b>.</div>'
    '<div class="hd-warn">Cản AI, cản CÁI GÌ → cách 3: <b>препя́тствовать рабо́те</b> cản trở công việc. Đừng để cách '
    '4.</div>'
    '<div class="hd-warn">Giọng trang trọng, giấy tờ. Nói thường ngày dùng <b>меша́ть</b>, cũng cách 3: <b>Не меша́й '
    'мне!</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>препя́тствие</b> trở ngại · <b>беспрепя́тственно</b> không trở ngại</div>'
)

# --------------------------------------------------------------------- ликвидировать
S["ликвидировать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ликвид-</span>'
    '<span class="hd-gloss">Latin <i>liquidus</i> LỎNG, như <i>liquid</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́рова-ть</span>'
    '<span class="hd-gloss">đuôi động từ mượn; khi chia <b>-ова-</b> → <b>-у-</b>: <b>ликвиди́рую</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng chữ <i>liquidate</i>: làm cho «tan thành nước» ⇒ xoá bỏ, dẹp bỏ; với công ty, phòng ban '
    'là giải thể: <b>ликвиди́ровать фи́рму</b>.</div>'
    '<div class="hd-warn">Một dạng dùng cho CẢ HAI thể: <b>ликвиди́рую</b> vừa là «tôi đang xoá bỏ» vừa là «tôi sẽ '
    'xoá bỏ», ngữ cảnh quyết định.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ликвида́ция</b> sự xoá bỏ, giải thể · <b>ликви́дный</b> dễ bán, có tính thanh khoản</div>'
)

# --------------------------------------------------------------------- функционировать
S["функционировать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">функци-</span>'
    '<span class="hd-gloss"><b>фу́нкция</b> chức năng, như <i>function</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-он-и́рова-ть</span>'
    '<span class="hd-gloss">đuôi động từ mượn; khi chia <b>-ова-</b> → <b>-у-</b>: <b>функциони́рую</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng chữ <i>to function</i>: thực hiện chức năng của mình ⇒ hoạt động, vận hành. Chủ ngữ là '
    'máy móc, hệ thống, cơ quan. Chỉ có CHT.</div>'
    '<div class="hd-warn">Giọng kỹ thuật, trang trọng. Máy móc trong nhà thì cứ nói <b>рабо́тать</b>: <b>Лифт не '
    'рабо́тает.</b> Thang máy hỏng rồi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>фу́нкция</b> chức năng · <b>функциона́льный</b> thuộc chức năng, thiết thực · '
    '<b>функциони́рование</b> sự vận hành</div>'
)

# --------------------------------------------------------------------- отремонтировать
S["отремонтировать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">tiền tố thể, chỉ đánh dấu XONG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ремонт-</span>'
    '<span class="hd-gloss">SỬA — <b>ремо́нт</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́рова-ть</span>'
    '<span class="hd-gloss">đuôi động từ mượn; khi chia <b>-ова-</b> → <b>-у-</b>: <b>отремонти́рую</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp HT của <b>ремонти́ровать</b> ⇒ sửa xong, tân trang xong. Sửa CÁI GÌ → cách 4: '
    '<b>отремонти́ровать кварти́ру</b>.</div>'
    '<div class="hd-warn"><b>почини́ть</b> là làm cho món đồ hết hỏng; <b>отремонти́ровать</b> bao cả sửa sang nhà '
    'cửa, tân trang. Người ta sửa CHO mình → cách 3: <b>Мне отремонти́ровали маши́ну.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ремо́нт</b> việc sửa chữa · <b>ремонти́ровать</b> (CHT) · <b>ремо́нтник</b> thợ sửa</div>'
)

# --------------------------------------------------------------------- доделать
S["доделать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI TẬN, cho đến hết</span></div>'
    '<div class="hd-row"><span class="hd-piece">-де́л-</span>'
    '<span class="hd-gloss">VIỆC, LÀM — <b>де́лать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho tới tận cùng ⇒ làm nốt phần còn dở. Chia y như <b>де́лать</b>, trọng âm không nhích: '
    '<b>доде́лаю, доде́лаешь</b>. Cặp CHT: <b>доде́лывать</b>.</div>'
    '<div class="hd-warn"><b>сде́лать</b> = làm xong cả việc · <b>доде́лать</b> = việc đã dở dang, nay làm NỐT: <b>Я '
    'сде́лал полови́ну, за́втра доде́лаю.</b></div>'
    '<div class="hd-warn"><b>до-</b> này ghép được với nhiều động từ: <b>дочита́ть</b> đọc nốt, <b>дописа́ть</b> viết '
    'nốt.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>де́лать</b> làm · <b>сде́лать</b> làm xong · <b>де́ло</b> việc · <b>доде́лывать</b> '
    '(CHT)</div>'
)

# --------------------------------------------------------------------- доделывать
S["доделывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI TẬN, cho đến hết</span></div>'
    '<div class="hd-row"><span class="hd-piece">-де́л-</span>'
    '<span class="hd-gloss">VIỆC, LÀM — <b>де́лать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>доде́лываю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>доде́лать</b>: đang làm nốt, hoặc lần nào cũng phải làm nốt. Trọng âm vẫn ở '
    '<b>-де́л-</b>, ngay trước <b>-ыва-</b>.</div>'
    '<div class="hd-warn">Dở tay, sắp xong: <b>Я уже́ доде́лываю.</b> = Tôi đang làm nốt đây.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>доде́лать</b> (HT) · <b>де́лать</b> làm · <b>де́ло</b> việc · <b>переде́лывать</b> làm '
    'lại</div>'
)

# --------------------------------------------------------------------- прибежать
S["прибежать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">TỚI NƠI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-беж-а́ть</span>'
    '<span class="hd-gloss">CHẠY — chính là <b>бежа́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chạy và đã TỚI ⇒ chạy đến. Chia y hệt <b>бежа́ть</b>, chỉ «tôi» và «họ» mang <b>г</b>: '
    '<b>прибегу́, прибежи́шь, прибегу́т</b>; sai khiến <b>прибеги́</b>. Cặp CHT: <b>прибега́ть</b>.</div>'
    '<div class="hd-warn">Đích là nơi chốn → <b>в / на</b> + cách 4, là người → <b>к</b> + cách 3: <b>прибежа́ть в '
    'шко́лу</b>, <b>прибежа́ть к ма́ме</b>.</div>'
    '<div class="hd-warn"><b>прибега́ть к</b> + cách 3 còn nghĩa «viện đến»: <b>прибега́ть к по́мощи</b> nhờ tới sự '
    'giúp đỡ. Nghĩa này có cặp HT khác: <b>прибе́гнуть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бежа́ть</b> chạy · <b>убежа́ть</b> chạy mất · <b>сбежа́ть</b> bỏ trốn · <b>бе́гать</b> '
    'chạy (nhiều chiều)</div>'
)

# --------------------------------------------------------------------- пробежать
S["пробежать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">XUYÊN QUA, NGANG QUA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-беж-а́ть</span>'
    '<span class="hd-gloss">CHẠY — chính là <b>бежа́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chạy qua hết một quãng, hoặc chạy ngang qua. Chia y hệt <b>бежа́ть</b>, chỉ «tôi» và «họ» '
    'mang <b>г</b>: <b>пробегу́, пробежи́шь, пробегу́т</b>. Cặp CHT: <b>пробега́ть</b>.</div>'
    '<div class="hd-warn">Quãng đường để cách 4 trần: <b>пробежа́ть киломе́тр</b>. Ngang qua cái gì: <b>ми́мо</b> + '
    'cách 2 — <b>пробежа́ть ми́мо до́ма</b>.</div>'
    '<div class="hd-warn"><b>пробежа́ть глаза́ми</b> + cách 4 = đọc lướt: «chạy mắt» qua trang chữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бежа́ть</b> chạy · <b>пробе́жка</b> buổi chạy bộ · <b>пробе́г</b> quãng đường xe đã chạy '
    '· <b>убежа́ть</b> chạy mất</div>'
)
# ---------------------------------------------------------------------
B = {
    "docbangmat": 151,
    "loitubat": 3,    # ежедневный «mỗi ngày một lần» -> «ngày nào cũng có»; «nền văn minh khác mới nói древний» (sai, Дре́вний Рим vẫn đúng) -> sửa; «giành GIẢI» ở ô đỏ выиграть lẫn với nghĩa của одержать -> «trúng GIẢI»
    "nguonsai": 3,    # dạng ngắn воскре́сен, анти́чен, досро́чен: tính từ quan hệ, thực tế không dùng -> không dạy
    "baolen": [
        "V cần duyệt (9 thẻ đổi thật): античный (BỎ cổ điển; THÊM thuộc Hy Lạp La Mã cổ đại) · интервал (quãng ngắt -> khoảng nghỉ) · индекс (BỎ mục lục) · разбивать (làm tan -> chia nhỏ, cùng dãy разбить k80) · одержать, одерживать (cùng dãy; BỎ đạt được, thắng; THÊM giành phần thắng) · поливать (theo dãy полить) · доделать, доделывать (cùng dãy; BỎ kết thúc, làm xong). полить khai nhưng không đổi.",
        "Trùng hết nghĩa trong lô chỉ có 3 cặp thể (одерж-, поли(ва)ть, доделать) — badge thể tách; va chạm классический và выигрывать gỡ được bằng V.",
        "индекс: «mã bưu chính» không nằm trong gloss Anh (chỉ có index) nhưng là nghĩa thường gặp nhất và 2/3 câu dùng — giữ. Câu 1–2 tiếng Anh sai từ: phải là postcode. Câu 1 nên: Write the <b>postcode</b> on the envelope, otherwise the letter won't arrive. Câu 2 nên: With this <b>postcode</b> I quickly found your street.",
        "полить: gloss «to start pouring» (mưa trút xuống) không đưa vào V để cặp thể cùng dãy, chỉ để ở ô đỏ.",
        "CÂU GƯỢNG предшествовать câu 1 (động từ sách vở trong lời bạn bè; «đứng trước» không có trong đề) -> «Выборам предшествовали долгие переговоры.» / Long negotiations <b>preceded</b> the election. / Những cuộc đàm phán dài <b>có trước</b> cuộc bầu cử.",
        "CÂU GƯỢNG предшествовать câu 2 («весь вечер» lệch; гроза là dông, không phải bão) -> «Грозе предшествовал сильный ветер.» / A strong wind <b>preceded</b> the thunderstorm. / Gió mạnh <b>đi trước</b> cơn dông.",
        "CÂU GƯỢNG продолжительность câu 3 (số nhiều продолжительностей không ai nói) -> «Продолжительность урока — сорок пять минут.» / The <b>duration</b> of a lesson is forty-five minutes. / <b>Thời lượng</b> một tiết học là bốn mươi lăm phút.",
        "CÂU GƯỢNG одерживать câu 3 (mệnh lệnh «Не одерживай верх») -> «Они редко одерживают победу в гостях.» / They rarely <b>win</b> a victory away from home. / Họ hiếm khi <b>giành</b> chiến thắng trên sân khách.",
        "CÂU GƯỢNG препятствовать câu 3 (động từ giấy tờ nói với trẻ con; tự nhiên là Не мешай) -> «Ничто не препятствует нашему сотрудничеству.» / Nothing <b>stands in the way of</b> our cooperation. / Không gì <b>cản trở</b> sự hợp tác của chúng ta.",
        "CÂU GƯỢNG интервал câu 3 (giữa hai tiết người Nga nói в перерыве) -> «Поезда идут с интервалом в пять минут.» / Trains run at an <b>interval</b> of five minutes. / Tàu chạy với <b>khoảng cách</b> năm phút một chuyến.",
        "CÂU GƯỢNG доделывать câu 2 («tối nào cũng» làm nốt cùng một việc) -> «Мы весь вечер доделывали ремонт на кухне.» / We <b>were finishing</b> the kitchen renovation all evening. / Cả tối chúng tôi <b>làm nốt</b> việc sửa bếp.",
        "CÂU HƠI GƯỢNG наименее câu 2 (наименее дорогой отель, bình thường nói самый дешёвый) -> «Это наименее опасный путь через горы.» / It's the <b>least</b> dangerous way through the mountains. / Đây là con đường <b>ít</b> nguy hiểm <b>nhất</b> qua núi.",
        "ликвидировать: thẻ viết HAI THỂ; предшествовать, функционировать: thẻ viết chỉ có CHT — chưa nhìn được AspectBadge, lệch thì luồng chính xem.",
        "Không chắc, KHÔNG khẳng định: nghĩa riêng của о- ở одержать (nói thẳng không tách); -шеств- ghi ô Mức tin; -пят- của препятствие giữ «gốc CẢN — cổ» như k189. по- «phủ lên mặt» ở поливать/полить là cách hiểu theo nhóm покрыть, посыпать, không phải luật.",
    ],
}
