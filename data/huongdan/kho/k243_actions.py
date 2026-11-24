# -*- coding: utf-8 -*-
"""k243 — actions: chín cặp thể + bốn động từ lẻ; trục là GỐC + chỗ bảng chia lệch.

Chỗ cần nhất quán với lô đã nạp:
(1) полз- BÒ: khớp ползти k232. (2) тер-/тир- CHÀ, XÁT: khớp стирать k148. (3) кус- CẮN: khớp укусить k228, кусок k79.
(4) -ключ- chìa khoá: khớp включить k94; пере- CHUYỂN SANG: khớp переключатель nhắc ở k234.
(5) -дел- PHẦN, chia phần: khớp делить k137. (6) у- RỜI KHỎI + -гн-/-гон- ĐUỔI, PHÓNG: khớp гнать, выгнать k215.
(7) об- VÒNG QUA + мен- ĐỔI: khớp обменять k219, обмен k131. (8) о- BAO QUANH + грани́ч- BIÊN, MÉP: khớp ограничить k219.
(9) про- SUỐT một quãng: khớp прожить k127; быть → буд-: khớp прибыть k191.
(10) гас-/туш-: -ить LÀM cho tắt ↔ -нуть TỰ tắt. Nợ → гасить; hầm → тушить.
Họ hàng cố ý vắng: không có (từ nào cũng có họ thật).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "ползать": "bò, bò lổm ngổm, bò qua bò lại",              # «lê» ngoài gloss crawl; + nét nhiều hướng
    "вытереть": "lau, lau sạch, lau khô",                     # dãy chung của cặp (không đổi)
    "вытирать": "lau, lau sạch, lau khô",                     # «thấm khô» không có trong gloss
    "кусать": "cắn, đốt",                                     # bỏ «ngoạm»
    "проработать": "làm việc trong một khoảng thời gian, làm kỹ, nghiên cứu kỹ",   # study in detail
    "нюхать": "ngửi, hít",
    "понюхать": "ngửi, hít",
    "переключать": "chuyển, chuyển sang, đổi kênh, sang số",
    "переключить": "chuyển, chuyển sang, đổi kênh, sang số",
    "тормозить": "phanh, giảm tốc, cản trở, kìm hãm",         # + hinder / hold back; «thắng xe» = phanh
    "гасить": "tắt, dập tắt, trả hết nợ",                     # + pay off; tách khỏi туши́ть
    "погасить": "tắt, dập tắt, trả hết nợ",
    "тушить": "dập tắt, tắt, hầm, om",                        # + stew / braise; tách khỏi гаси́ть
    "потушить": "dập tắt, tắt, hầm, om",
    "пробыть": "ở lại, lưu lại, ở một thời gian",             # «trải qua» là провести́
    "угнать": "trộm xe, cướp xe, cướp máy bay, lùa đi",       # + hijack, herd off; «lấy đi mất» mơ hồ
    "угонять": "trộm xe, cướp xe, cướp máy bay, lùa đi",
    "обмениваться": "trao đổi, đổi cho nhau, trao cho nhau",  # «chia sẻ qua lại» ngoài gloss
    "обменяться": "trao đổi, đổi cho nhau, trao cho nhau",    # gỡ ⊆ поменя́ться k184
    "ограничиваться": "tự giới hạn, chỉ dừng ở, bó hẹp",      # «bằng lòng với» ngoài gloss
    "ограничиться": "tự giới hạn, chỉ dừng ở, bó hẹp",
}

# -------------------------------------------------------------------- ползать
S["ползать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по́лз-</span>'
    '<span class="hd-gloss">BÒ — như <b>ползти́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi chia đều: <b>по́лзаю, по́лзает</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Động từ chuyển động NHIỀU HƯỚNG: bò qua bò lại, bò nói chung, biết bò — '
    '<b>Малы́ш уже́ по́лзает</b> Bé đã biết bò. Đang bò về MỘT phía là <b>ползти́</b>; hai từ này '
    'đều CHT, sánh đôi y như <b>бе́гать ↔ бежа́ть</b>.</div>'
    '<div class="hd-warn">Bò TRÊN mặt gì: <b>по</b> + cách 3 — <b>по́лзать по ковру́</b> bò trên '
    'thảm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ползти́</b> bò (một hướng) · <b>поползти́</b> bắt đầu bò (HT) · '
    '<b>ползунки́</b> quần cho bé tập bò</div>'
)

# ------------------------------------------------------------------- вытереть
S["вытереть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span>'
    '<span class="hd-gloss">RA, cho ra hết — mang trọng âm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тер-</span>'
    '<span class="hd-gloss">CHÀ, XÁT — gốc <i>тер-/тир-</i> của <b>тере́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chà cho nước, cho bụi RA hết ⇒ lau sạch, lau khô: <b>вы́тереть ру́ки</b> lau '
    'tay. Trọng âm đứng ở <b>вы́-</b> trong mọi dạng, như <b>вы́ключить</b>. Cặp CHT: '
    '<b>вытира́ть</b>.</div>'
    '<div class="hd-warn">Bảng chia lệch: tương lai rụng <i>е</i> của gốc — <b>вы́тру, вы́трешь, '
    'вы́трут</b>; quá khứ giống đực không có <i>-л</i> — <b>вы́тер, вы́терла, вы́терли</b>. Sai khiến: '
    '<b>вы́три!</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вытира́ть</b> (CHT) · <b>тере́ть</b> chà, cọ · <b>стере́ть</b> xoá · '
    '<b>стира́ть</b> giặt, xoá</div>'
)

# ------------------------------------------------------------------- вытирать
S["вытирать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">RA, cho ra hết</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тир-</span>'
    '<span class="hd-gloss">CHÀ, XÁT — gốc <i>тер-/тир-</i> của <b>тере́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>вытира́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>вы́тереть</b>. Gốc đổi <i>тер → тир</i>, trọng âm rời <i>вы-</i> '
    'ra đuôi — cùng phép với <b>умере́ть ↔ умира́ть</b>. Lau gì ở cách 4, bằng gì ở cách 5: '
    '<b>вытира́ть ру́ки полоте́нцем</b> lau tay bằng khăn.</div>'
    '<div class="hd-warn">Chùi VÀO cái gì: <b>о</b> + cách 4 — <b>вытира́ть но́ги о ко́врик</b> chùi '
    'chân vào thảm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́тереть</b> (HT) · <b>стира́ть</b> giặt, xoá · <b>стере́ть</b> xoá (HT) · '
    '<b>тере́ть</b> chà, cọ</div>'
)

# --------------------------------------------------------------------- кусать
S["кусать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кус-</span>'
    '<span class="hd-gloss">CẮN — như <b>кусо́к</b> miếng (cái cắn ra được)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>куса́ю, куса́ет</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chó cắn, muỗi đốt đều là từ này: <b>Меня́ куса́ют комары́</b> Tôi bị muỗi đốt. '
    'Cặp HT đổi sang đuôi <i>-ить</i> và thêm <i>у-</i>: <b>укуси́ть</b> cắn một phát.</div>'
    '<div class="hd-warn">Cắn ai: cách 4; cắn VÀO chỗ nào: <b>за</b> + cách 4 — <b>куса́ть за '
    'па́лец</b> cắn vào ngón tay.</div>'
    '<div class="hd-warn">Nói TÍNH hay cắn thì thêm <i>-ся</i>: <b>Соба́ка куса́ется</b> Con chó này '
    'hay cắn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>укуси́ть</b> (HT) · <b>уку́с</b> vết cắn · <b>кусо́к</b> miếng · '
    '<b>заку́ска</b> món nhắm, khai vị</div>'
)

# ---------------------------------------------------------------- проработать
S["проработать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">SUỐT, từ đầu đến cuối</span></div>'
    '<div class="hd-row"><span class="hd-piece">-рабо́тать</span>'
    '<span class="hd-gloss">LÀM VIỆC — chính là <b>рабо́тать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm SUỐT một quãng thời gian — cùng <i>про-</i> với <b>прожи́ть</b>, '
    '<b>пробы́ть</b>. Làm suốt một đề tài từ đầu đến cuối ⇒ làm kỹ, nghiên cứu kỹ: '
    '<b>прорабо́тать план</b>. Chia đều: <b>прорабо́таю</b>.</div>'
    '<div class="hd-warn">Nghĩa «làm được bao lâu» phải kèm thời gian, đặt thẳng ở cách 4, KHÔNG giới '
    'từ: <b>прорабо́тать там год</b> làm ở đó một năm.</div>'
    '<div class="hd-warn">Cặp CHT <b>прораба́тывать</b> (<i>о → а</i>) thường chỉ dùng cho nghĩa làm '
    'kỹ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рабо́та</b> công việc · <b>рабо́тник</b> người lao động · '
    '<b>зарабо́тать</b> kiếm được tiền · <b>разрабо́тать</b> xây dựng, soạn ra</div>'
)

# --------------------------------------------------------------------- нюхать
S["нюхать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ню́х-</span>'
    '<span class="hd-gloss">NGỬI — đứng riêng thành <b>нюх</b> khứu giác, mũi thính</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>ню́хаю, ню́хает</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chủ động đưa mũi vào hít. Thứ bị ngửi ở cách 4: <b>ню́хать цветы́</b> ngửi hoa. '
    'Cặp HT: <b>поню́хать</b>.</div>'
    '<div class="hd-warn">Tự nó toả mùi thì là <b>па́хнуть</b>: <b>Цветы́ па́хнут</b> Hoa toả hương ↔ '
    '<b>Я ню́хаю цветы́</b> Tôi ngửi hoa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поню́хать</b> (HT) · <b>нюх</b> khứu giác · <b>обню́хать</b> ngửi khắp, '
    'đánh hơi (HT)</div>'
)

# ------------------------------------------------------------------- понюхать
S["понюхать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">làm thành thể hoàn thành: ngửi một cái</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ню́хать</span>'
    '<span class="hd-gloss">NGỬI — chính là <b>ню́хать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ngửi một cái cho biết: <b>поню́хать молоко́</b> ngửi thử sữa xem còn tươi '
    'không. Chia đều như <b>ню́хать</b>: <b>поню́хаю, поню́хает</b>.</div>'
    '<div class="hd-warn"><b>Поню́хай!</b> — Ngửi thử mà xem! Câu nói khi đưa hoa, đưa món ăn cho người '
    'khác.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ню́хать</b> (CHT) · <b>нюх</b> khứu giác · <b>обню́хать</b> ngửi khắp, '
    'đánh hơi (HT)</div>'
)

# ---------------------------------------------------------------- переключать
S["переключать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span>'
    '<span class="hd-gloss">CHUYỂN SANG, qua chỗ khác</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ключ-</span>'
    '<span class="hd-gloss">chìa khoá (<b>ключ</b>) — như <b>включа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>переключа́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vặn khoá SANG nấc khác ⇒ chuyển. Cùng một khúc <i>-ключать</i>: '
    '<b>включа́ть</b> bật, <b>выключа́ть</b> tắt, <b>переключа́ть</b> chuyển. Cặp HT: '
    '<b>переключи́ть</b>.</div>'
    '<div class="hd-warn">Đổi cái gì: cách 4 trơn — <b>переключа́ть кана́лы</b>. Chuyển SANG cái gì: '
    '<b>на</b> + cách 4 — <b>переключа́ть на но́вости</b> chuyển sang kênh tin tức.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>переключи́ть</b> (HT) · <b>включа́ть</b> bật · <b>отключа́ть</b> ngắt · '
    '<b>переключа́тель</b> nút chuyển</div>'
)

# ---------------------------------------------------------------- переключить
S["переключить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span>'
    '<span class="hd-gloss">CHUYỂN SANG, qua chỗ khác</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ключ-</span>'
    '<span class="hd-gloss">chìa khoá (<b>ключ</b>) — như <b>включи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́-ть</span>'
    '<span class="hd-gloss">đuôi HT lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vặn khoá SANG nấc khác một lần ⇒ chuyển xong. Trọng âm ở ĐUÔI suốt bảng như '
    '<b>включи́ть</b>: <b>переключу́, переключи́шь, переключи́т</b>. Cặp CHT: <b>переключа́ть</b>.</div>'
    '<div class="hd-warn">Trên xe: <b>переключи́ть ско́рость</b> hoặc <b>переключи́ть переда́чу</b> = '
    'sang số. Người chuyển sự chú ý thì thêm <i>-ся</i>: <b>переключи́ться на рабо́ту</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>переключа́ть</b> (CHT) · <b>включи́ть</b> bật · <b>вы́ключить</b> tắt · '
    '<b>отключи́ть</b> ngắt</div>'
)

# ------------------------------------------------------------------ тормозить
S["тормозить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тормоз-</span>'
    '<span class="hd-gloss">CÁI PHANH — <b>то́рмоз</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́-ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dùng phanh ⇒ phanh, giảm tốc; «phanh» một công việc lại ⇒ cản trở, kìm hãm: '
    '<b>тормози́ть разви́тие</b> kìm hãm sự phát triển. Cặp HT: <b>затормози́ть</b>.</div>'
    '<div class="hd-warn">Chỉ ngôi «tôi» biến âm <i>з → ж</i>, trọng âm ở đuôi suốt: <b>торможу́, '
    'тормози́шь, тормозя́т</b>.</div>'
    '<div class="hd-warn"><b>Не тормози́!</b> — thân mật: Nhanh lên, đừng lề mề! Nghĩ chậm, máy tính '
    'chạy lag cũng nói <b>тормози́т</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>затормози́ть</b> (HT) · <b>то́рмоз</b> cái phanh · <b>тормозно́й</b> thuộc '
    'về phanh · <b>торможе́ние</b> sự phanh</div>'
)

# ------------------------------------------------------------------- поделить
S["поделить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">chỉ làm thành thể hoàn thành, KHÔNG thêm nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дел-</span>'
    '<span class="hd-gloss">PHẦN, chia phần</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́-ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>дели́ть</b> làm trọn một lần: chia xong. Hay dùng khi chia cho NHAU, mỗi '
    'người một phần: <b>подели́ть де́ньги</b> chia tiền. Trọng âm lùi từ ngôi «bạn»: <b>поделю́, '
    'поде́лишь, поде́лят</b>.</div>'
    '<div class="hd-warn">Chia THÀNH mấy phần: <b>на</b> + cách 4 — <b>подели́ть торт на три ча́сти</b>.'
    '</div>'
    '<div class="hd-warn">Thêm <i>-ся</i> đổi nghĩa và đổi cách: <b>подели́ться</b> + cách 5 = chia sẻ, '
    'kể cho ai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дели́ть</b> (CHT) · <b>раздели́ть</b> chia ra (HT) · <b>подели́ться</b> chia '
    'sẻ · <b>отде́л</b> phòng, ban</div>'
)

# --------------------------------------------------------------------- гасить
S["гасить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гас-</span>'
    '<span class="hd-gloss">TẮT — như <b>га́снуть</b> tự tắt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́-ть</span>'
    '<span class="hd-gloss">LÀM cho — đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">LÀM cho tắt: <b>гаси́ть свет</b> tắt đèn. Khoản nợ cũng «dập» cho tắt ⇒ trả '
    'hết nợ: <b>гаси́ть креди́т</b>. Cặp HT: <b>погаси́ть</b>.</div>'
    '<div class="hd-warn">Ngôi «tôi» <i>с → ш</i>, từ ngôi «bạn» trọng âm lùi: <b>гашу́, га́сишь, '
    'га́сят</b>.</div>'
    '<div class="hd-warn">Chung «tắt, dập tắt» với <b>туши́ть</b>; tách ở nghĩa còn lại: NỢ → '
    '<b>гаси́ть</b> · HẦM thịt → <b>туши́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>погаси́ть</b> (HT) · <b>га́снуть</b> tự tắt · <b>пога́снуть</b> tự tắt '
    '(HT) · <b>угаса́ть</b> lụi dần</div>'
)

# ------------------------------------------------------------------- погасить
S["погасить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">chỉ làm thành thể hoàn thành, KHÔNG thêm nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-гас-</span>'
    '<span class="hd-gloss">TẮT — như <b>га́снуть</b> tự tắt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́-ть</span>'
    '<span class="hd-gloss">LÀM cho — đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho tắt hẳn: <b>погаси́ть свечу́</b> tắt nến. Nợ «tắt» hẳn ⇒ trả hết: '
    '<b>погаси́ть долг</b>. Cặp CHT: <b>гаси́ть</b>. Tự nó tắt thì là <b>пога́снуть</b>: <b>Свет '
    'пога́с</b> Đèn tắt rồi.</div>'
    '<div class="hd-warn">Chia như <b>гаси́ть</b>: ngôi «tôi» <i>с → ш</i>, từ ngôi «bạn» trọng âm '
    'lùi — <b>погашу́, пога́сишь, пога́сят</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гаси́ть</b> (CHT) · <b>погаше́ние</b> sự trả hết nợ · <b>га́снуть</b> tự '
    'tắt · <b>угаса́ть</b> lụi dần</div>'
)

# ------------------------------------------------------------------- потушить
S["потушить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">chỉ làm thành thể hoàn thành, KHÔNG thêm nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-туш-</span>'
    '<span class="hd-gloss">TẮT — như <b>поту́хнуть</b> tự tắt, <i>х → ш</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́-ть</span>'
    '<span class="hd-gloss">LÀM cho — đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dập cho tắt hẳn: <b>потуши́ть пожа́р</b> dập xong đám cháy. Trong bếp: hầm, om '
    'xong — <b>потуши́ть о́вощи</b>. Cặp CHT: <b>туши́ть</b>.</div>'
    '<div class="hd-warn">Trọng âm lùi từ ngôi «bạn»: <b>потушу́, поту́шишь, поту́шат</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>туши́ть</b> (CHT) · <b>поту́хнуть</b> tự tắt · <b>тушёный</b> hầm, om · '
    '<b>огнетуши́тель</b> bình chữa cháy</div>'
)

# --------------------------------------------------------------------- тушить
S["тушить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">туш-</span>'
    '<span class="hd-gloss">TẮT — như <b>поту́хнуть</b> tự tắt, <i>х → ш</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́-ть</span>'
    '<span class="hd-gloss">LÀM cho — đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">LÀM cho tắt, nghĩ ngay tới đám cháy: <b>туши́ть пожа́р</b> dập lửa. Cặp HT: '
    '<b>потуши́ть</b>. Nghĩa trong bếp — HẦM, om — phải thuộc riêng: <b>туши́ть мя́со</b> hầm thịt.</div>'
    '<div class="hd-warn">Trọng âm lùi từ ngôi «bạn»: <b>тушу́, ту́шишь, ту́шат</b>.</div>'
    '<div class="hd-warn">Chung «tắt, dập tắt» với <b>гаси́ть</b>; tách ở nghĩa còn lại: HẦM thịt → '
    '<b>туши́ть</b> · NỢ → <b>гаси́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>потуши́ть</b> (HT) · <b>поту́хнуть</b> tự tắt · <b>тушёный</b> hầm, om · '
    '<b>огнетуши́тель</b> bình chữa cháy</div>'
)

# -------------------------------------------------------------------- пробыть
S["пробыть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">SUỐT một khoảng thời gian — như <b>прожи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-бы́-ть</span>'
    '<span class="hd-gloss">LÀ, CÓ MẶT — chính là <b>быть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Có mặt SUỐT một quãng ⇒ ở lại bao lâu đó. Thời gian đặt thẳng ở cách 4, không '
    'giới từ: <b>пробы́ть там неде́лю</b> ở đó một tuần.</div>'
    '<div class="hd-warn">Chia y như <b>быть → бу́ду</b>: <b>пробу́ду, пробу́дешь</b>. Quá khứ nói '
    '<b>про́был</b> hay <b>пробы́л</b> đều được, riêng giống cái luôn nhấn đuôi: <b>пробыла́</b>.</div>'
    '<div class="hd-warn">Lệch một chữ: <b>прибы́ть</b> TỚI nơi · <b>пробы́ть</b> Ở suốt một thời '
    'gian.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>быть</b> là, ở · <b>побы́ть</b> ở lại một lúc · <b>прибы́ть</b> tới nơi · '
    '<b>забы́ть</b> quên</div>'
)

# --------------------------------------------------------------------- угнать
S["угнать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">RỜI KHỎI, ra xa — như <b>уйти́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-гн-а́ть</span>'
    '<span class="hd-gloss">ĐUỔI, PHÓNG — chính là <b>гнать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuổi đàn bò ĐI MẤT ⇒ lùa đi; phóng xe người khác ĐI MẤT ⇒ trộm xe; với máy bay '
    'là cướp: <b>угна́ть самолёт</b>. Cặp CHT: <b>угоня́ть</b>. Đồ đạc khác bị trộm thì nói '
    '<b>укра́сть</b>.</div>'
    '<div class="hd-warn">Chia như <b>гнать</b>, lộ <i>о</i>: <b>угоню́, уго́нишь, уго́нят</b>. Quá khứ '
    'chỉ giống cái nhấn đuôi: <b>угна́л, угнала́, угна́ли</b>.</div>'
    '<div class="hd-warn">Người mất xe: <b>у</b> + cách 2 — <b>У сосе́да угна́ли маши́ну</b> Ông hàng '
    'xóm bị trộm xe.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>угоня́ть</b> (CHT) · <b>уго́н</b> vụ trộm xe · <b>вы́гнать</b> đuổi ra · '
    '<b>догна́ть</b> đuổi kịp</div>'
)

# -------------------------------------------------------------------- угонять
S["угонять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">RỜI KHỎI, ra xa — như <b>уйти́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-гон-</span>'
    '<span class="hd-gloss">ĐUỔI, PHÓNG — gốc <i>гн-/гон-</i> của <b>гнать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>угоня́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>угна́ть</b>: kẻ chuyên trộm xe, hay trộm nhiều lần — <b>Он '
    'угоня́л маши́ны</b> Hắn từng đi trộm xe. Cả họ một khuôn: <b>догна́ть ↔ догоня́ть</b>, '
    '<b>вы́гнать ↔ выгоня́ть</b>.</div>'
    '<div class="hd-warn">Nhìn giống nhau mà hai thể: <b>угоня́ю</b> đang, hay trộm (CHT) · '
    '<b>угоню́</b> sẽ trộm (HT).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>угна́ть</b> (HT) · <b>уго́н</b> vụ trộm xe · <b>уго́нщик</b> kẻ trộm xe · '
    '<b>догоня́ть</b> đuổi theo</div>'
)

# --------------------------------------------------------------- обмениваться
S["обмениваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">VÒNG QUA — như <b>обме́н</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ме́н-</span>'
    '<span class="hd-gloss">ĐỔI — gốc của <b>меня́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>обме́ниваюсь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">ở đây = CHO NHAU</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>обме́нивать</b> đổi lấy + <i>-ся</i> cho nhau ⇒ hai bên trao qua đổi lại. Cặp '
    'HT: <b>обменя́ться</b> — trọng âm dời sang đuôi.</div>'
    '<div class="hd-warn">Thứ được đổi ở cách 5, người đổi cùng <b>с</b> + cách 5: <b>обме́ниваться '
    'кни́гами с дру́гом</b> trao đổi sách với bạn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обменя́ться</b> (HT) · <b>обме́нивать</b> đổi lấy · <b>обме́н</b> sự trao '
    'đổi · <b>меня́ться</b> thay đổi, đổi cho nhau</div>'
)

# ----------------------------------------------------------------- обменяться
S["обменяться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">VÒNG QUA — như <b>обме́н</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-меня́ть</span>'
    '<span class="hd-gloss">ĐỔI — chính là <b>меня́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">ở đây = CHO NHAU</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai bên trao qua đổi lại xong một vụ. Chia đều: <b>обменя́юсь, обменя́ешься</b>. '
    'Thứ được đổi ở cách 5: <b>обменя́ться номера́ми</b> cho nhau số điện thoại, <b>обменя́ться '
    'взгля́дами</b> đưa mắt nhìn nhau. Cặp CHT: <b>обме́ниваться</b>.</div>'
    '<div class="hd-warn"><b>обменя́ться</b> luôn là hai bên trao cho nhau; nghĩa «đã thay đổi» thuộc '
    'về <b>поменя́ться</b>: <b>Всё поменя́лось</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обме́ниваться</b> (CHT) · <b>обменя́ть</b> đổi lấy · <b>обме́н</b> sự trao '
    'đổi · <b>поменя́ться</b> đổi cho nhau</div>'
)

# ------------------------------------------------------------- ограничиваться
S["ограничиваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">BAO QUANH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-грани́ч-</span>'
    '<span class="hd-gloss">BIÊN, MÉP — <b>грани́ца</b>, <i>ц → ч</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>ограни́чиваюсь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">tự mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tự vạch biên quanh mình ⇒ tự giới hạn, chỉ dừng ở đó. Cặp HT '
    '<b>ограни́читься</b>; trọng âm hai bên cùng chỗ.</div>'
    '<div class="hd-warn">Dừng ở cái gì: cách 5, KHÔNG giới từ — <b>ограни́чиваться '
    'обеща́ниями</b> chỉ dừng ở lời hứa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ограни́читься</b> (HT) · <b>ограни́чивать</b> hạn chế · '
    '<b>ограниче́ние</b> sự hạn chế · <b>грани́ца</b> biên giới</div>'
)

# --------------------------------------------------------------- ограничиться
S["ограничиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">BAO QUANH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-грани́ч-</span>'
    '<span class="hd-gloss">BIÊN, MÉP — <b>грани́ца</b>, <i>ц → ч</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai: <b>ограни́чусь, ограни́чишься</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">tự mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tự vạch biên cho xong ⇒ dừng ở mức đó, không đi tiếp. Dừng ở cái gì: cách 5 — '
    '<b>ограни́читься ча́ем</b> chỉ uống trà thôi. Cặp CHT: <b>ограни́чиваться</b>.</div>'
    '<div class="hd-warn">Không có <i>-ся</i> thì là hạn chế NGƯỜI, VẬT khác (cách 4): <b>ограни́чить '
    'ско́рость</b> ↔ tự dừng: <b>ограни́читься</b> + cách 5.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ограни́чиваться</b> (CHT) · <b>ограни́чить</b> hạn chế · '
    '<b>ограниче́ние</b> sự hạn chế · <b>безграни́чный</b> vô biên</div>'
)

B = {
    "docbangmat": 165,
    "loitubat": 3,   # понюхать: «gặp nhiều nhất» không có căn cứ -> bỏ
                     # угнать: «chỉ nói về xe cộ và gia súc» đá với cướp máy bay -> viết lại
                     # проработать: CHT «chỉ dùng» quá chắc -> «thường chỉ dùng»
    "nguonsai": 3,   # вытереть: nguồn ghi aspect both + tương lai «бу́ду вы́тереть» -> dạy HT thuần
                     # пробыть: nguồn ghi cặp пробыва́ть (không ai dùng) -> không đưa
                     # ползать: nguồn ghi cặp опо́лзать -> không đưa
    "baolen": [
        "🔴 вытереть: nguồn ghi aspect «both» nên badge chắc là BI-ASP và bảng chia có tương lai «бу́ду вы́тереть» + cột hiện tại вы́тру — SAI, từ này HT thuần. Đề nghị thêm \"вытереть\": \"perfective\" vào THE_NGUON_SAI (anki_tools/grammar.py), sửa badge + bảng (hiện tại trống, tương lai = вы́тру, вы́трешь…).",
        "V cần duyệt (20 thẻ đổi; вытереть khai cho đủ cặp, không đổi): ползать (BỎ lê; THÊM bò qua bò lại) · вытирать (BỎ thấm khô) · кусать (BỎ ngoạm) · проработать (nghiền ngẫm -> nghiên cứu kỹ) · нюхать, понюхать (cùng dãy; BỎ hít hà, ngửi thử) · переключать, переключить (cùng dãy; bật sang -> chuyển sang) · тормозить (BỎ thắng xe = phanh; THÊM cản trở, kìm hãm) · гасить, погасить (THÊM trả hết nợ) · тушить, потушить (THÊM hầm, om) · пробыть (BỎ trải qua… = провести) · угнать, угонять (cùng dãy; BỎ lấy đi mất; THÊM lùa đi) · обмениваться, обменяться (THÊM trao cho nhau; BỎ chia sẻ qua lại) · ограничиваться, ограничиться (cùng dãy; BỎ bằng lòng với).",
        "Va chạm: обменяться ↔ поменяться[k184] đã gỡ bằng «trao cho nhau» (đổi quà, trao nhẫn, đưa mắt — exchange), giữ nguyên nghĩa chính; обмениваться ↔ меняться[k184] cũng không chứa nhau. гасить ↔ тушить tách bằng trả hết nợ / hầm, om. CHƯA chạy vacham với V mới (không đụng Anki; chỉ so với V các lô + nghĩa máy) — luồng chính soát lại. Ca mỏng: кусать «cắn, đốt» nằm trong укусить[k228] «cắn, đốt, táp» nhưng badge thể tách.",
        "CÂU VÍ DỤ thiếu nghĩa tách cặp — погасить câu 3 (погасить фонарь / đèn pin hết pin: gượng) -> «Он наконец погасил кредит за машину.» / «He finally <b>paid off</b> the car loan.» / «Cuối cùng anh ấy đã <b>trả hết nợ</b> vay mua xe.»",
        "гасить câu 2 -> «Мы гасим кредит маленькими суммами.» / «We are <b>paying off</b> the loan in small amounts.» / «Bọn tôi <b>trả hết nợ</b> vay bằng từng khoản nhỏ.» (tuỳ chọn; câu cũ không sai)",
        "тушить câu 2 -> «Бабушка тушит капусту с мясом.» / «Grandma is <b>stewing</b> cabbage with meat.» / «Bà đang <b>hầm</b> bắp cải với thịt.» · потушить câu 1 -> «Потушим овощи с курицей на ужин?» / «Shall we <b>stew</b> some vegetables with chicken for dinner?» / «Tối nay mình <b>hầm</b> rau với gà nhé?» (tuỳ chọn; câu cũ không sai)",
        "поделить câu 3 «Подели конфеты с братом» GƯỢNG (chia sẻ với ai là поделись конфетами) -> «Подели конфеты поровну, не жадничай.» / «<b>Divide</b> the candy equally, don't be greedy.» / «<b>Chia</b> kẹo cho đều đi, đừng tham.»",
        "кусать câu 3 «кусать карандаш» gượng (người Nga nói грызть) -> «Летом на даче нас всё время кусают комары.» / «In summer at the dacha mosquitoes <b>bite</b> us all the time.» / «Mùa hè ở nhà vườn bọn tôi bị muỗi <b>đốt</b> suốt.»",
        "ползать câu 2 «ползала под столом за проводом» gượng -> «Я весь вечер ползала под столом, искала провод.» / «I <b>was crawling</b> under the table all evening looking for the cable.» / dịch Việt giữ nguyên.",
        "переключать câu 2 «переключали музыку» gượng, dịch «đổi» không có trong đề -> «Мы переключали песни каждые две минуты.» / «We <b>kept switching</b> the songs every two minutes.» / «Bọn tôi cứ hai phút lại <b>chuyển</b> bài một lần.»",
        "ограничиваться câu 1 (dịch «chỉ uống», thừa «Tối») -> «Thứ Sáu bọn tôi thường <b>chỉ dừng ở</b> vài chai bia.» · câu 2 (dịch «chỉ nhắn») -> «Trước đây bọn tôi <b>chỉ dừng ở</b> những tin nhắn ngắn.» · câu 3 Nga nên «смотри ещё и видео», dịch bôi «<b>bó hẹp</b>» -> «Đừng <b>bó hẹp</b> trong sách giáo trình, xem thêm video nữa.» · ограничиться câu 2 (dịch «chỉ gọi») -> «Chúng tôi <b>chỉ dừng ở</b> cà phê, chẳng muốn ăn gì cả.»",
        "обмениваться câu 3: «с кем попало» dịch «người lạ» lệch -> «Đừng <b>trao đổi</b> mật khẩu với bất cứ ai.»",
        "THẺ CŨ вкус[k152]: thẻ chẻ в- + -кус- «CẮN» và nối кусо́к/куса́ть. Theo từ nguyên (Vasmer, Shansky) вкус thuộc gốc кус- «nếm» (искуси́ть, mượn Giécman) KHÁC gốc кус- «cắn» của кусать — thẻ khẳng định không kèm mức tin. Đề nghị thêm «⚠️ Mức tin» hoặc bỏ куса́ть/кусо́к khỏi Họ hàng. Thẻ кусать của lô này không nối sang вкус.",
        "Không chắc, KHÔNG khẳng định trên thẻ: тушить «hầm» có cùng gốc với тушить «dập» không (thẻ chỉ bảo thuộc riêng). Từ điển ghi quá khứ пробыть hai trọng âm (про́был / пробы́л) — thẻ nêu cả hai.",
    ],
}
