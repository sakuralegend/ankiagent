# -*- coding: utf-8 -*-
"""k191 — language::documents (lô trộn): giấy tờ, đi lại, vài từ mượn.

Chỗ cần nhất quán trong lô:
(1) спуска́ться / спусти́ться: с- XUỐNG + -пуск-/-пуст- THẢ, BUÔNG — khớp пропуска́ть [k175],
    вы́пуск [k177]; lô k185 (опуска́ть, выпуска́ть) soạn song song.
(2) подвезти́ / подвози́ть: под- SÁT LẠI GẦN (подойти́ [k125]) + вез-/воз- CHỞ (везти́ [k94],
    вози́ть [k107]). Câu cảnh báo я подвожу́ ↔ подводи́ть chép khuôn thẻ вози́ть.
(3) прибыва́ть / прибы́ть: при- + -бы- (быть) — khớp при́быль [k163]; прибы́ть chia như бу́ду.
(4) опубликова́ть / публикова́ть: -публик- = public; о- chỉ đổi thể.
(5) печа́ть khớp chẻ печа́тать [k142]; кре́пость khớp кре́пкий [k63]; мастерска́я ← ма́стер [k119].
Họ hàng cố ý vắng: рюкза́к, па́пка (từ mượn đứng một mình).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "крепость": "pháo đài, thành lũy, thành trì, độ bền, độ đậm",     # thiếu nghĩa strength (độ bền; trà/rượu đậm)
    "рюкзак": "ba lô",                                              # «túi đeo vai» = сумка через плечо, gloss chỉ có backpack
    "прибывать": "đến, tới, dâng lên, tăng lên",                    # gloss: to increase / to wax
    "печать": "con dấu, dấu đóng, hình dấu, sự in ấn",     # «báo chí» rút: đề пресса nằm gọn trong nó (luồng chính 22/11)
}

# --------------------------------------------------------------------- крепость
S["крепость"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">креп-</span>'
    '<span class="hd-gloss">CHẮC, VỮNG — như <b>кре́пкий</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span>'
    '<span class="hd-gloss">→ danh từ giống cái chỉ tính chất</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Sự chắc vững» ⇒ độ bền; với trà, rượu ⇒ độ đậm: <b>кре́пость ча́я</b>. '
    'Thứ chắc vững nhất là tường thành ⇒ pháo đài, thành lũy.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кре́пкий</b> chắc, đậm · <b>кре́пко</b> chặt, say (ngủ) · '
    '<b>укрепи́ть</b> củng cố · <b>крепостно́й</b> nông nô (thời xưa)</div>'
)

# --------------------------------------------------------------------- мастерская
S["мастерская"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ма́стер-</span>'
    '<span class="hd-gloss">THỢ CẢ, người giỏi nghề (<b>ма́стер</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ск-ая</span>'
    '<span class="hd-gloss">đuôi tính từ giống cái — ngầm hiểu «(phòng) của thợ»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Phòng của thợ» ⇒ xưởng: xưởng mộc, tiệm sửa chữa, xưởng vẽ của hoạ sĩ. '
    'Là tính từ dùng làm danh từ nên biến cách như tính từ: <b>в мастерско́й</b> ở xưởng, '
    '<b>в мастерску́ю</b> tới xưởng. Trọng âm rời đầu từ: <b>ма́стер</b> → <b>мастерска́я</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ма́стер</b> thợ cả, thợ sửa · <b>мастерство́</b> tay nghề</div>'
)

# --------------------------------------------------------------------- тупик
S["тупик"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">туп-</span>'
    '<span class="hd-gloss">CÙN, TÙ — như <b>тупо́й</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́к</span>'
    '<span class="hd-gloss">đuôi danh từ giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Con đường «cùn đầu», không xuyên đi tiếp được ⇒ ngõ cụt; nghĩa bóng ⇒ '
    'bế tắc. Trọng âm nhảy ra đuôi từ cách 2: <b>тупика́</b>, <b>в тупике́</b>.</div>'
    '<div class="hd-warn"><b>зайти́ в тупи́к</b> = rơi vào bế tắc: <b>Перегово́ры зашли́ в '
    'тупи́к</b> — đàm phán bế tắc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тупо́й</b> cùn, đần · <b>тупи́ца</b> kẻ đần độn</div>'
)

# --------------------------------------------------------------------- спускаться
S["спускаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">TỪ TRÊN XUỐNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пуск-</span>'
    '<span class="hd-gloss">THẢ, BUÔNG — như <b>пропуска́ть</b>, <b>вы́пуск</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть-ся</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành; <b>-ся</b> = thả CHÍNH MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thả chính mình xuống» ⇒ đi xuống: <b>спуска́ться по ле́стнице</b> xuống '
    'cầu thang. Chia đều: <b>спуска́юсь</b>. Cặp HT: <b>спусти́ться</b>.</div>'
    '<div class="hd-warn">Bỏ <b>-ся</b> là hạ CÁI KHÁC xuống: <b>спуска́ть ло́дку</b> hạ thuyền.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спусти́ться</b> (HT) · <b>спуск</b> dốc xuống, sự đi xuống · '
    '<b>опуска́ть</b> hạ xuống · <b>пропуска́ть</b> cho qua · <b>о́тпуск</b> kỳ nghỉ phép</div>'
)

# --------------------------------------------------------------------- спуститься
S["спуститься"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">TỪ TRÊN XUỐNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пуст-</span>'
    '<span class="hd-gloss">THẢ, BUÔNG — mặt HT của <b>-пуск-</b>, như <b>пусти́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть-ся</span>'
    '<span class="hd-gloss">đuôi động từ; <b>-ся</b> = thả CHÍNH MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thể HOÀN THÀNH của <b>спуска́ться</b>. Ngôi «tôi» đổi ст → щ, ngôi khác '
    'trọng âm lùi lên thân: <b>я спущу́сь</b>, <b>ты спу́стишься</b>. Câu hay nghe: <b>Я сейча́с '
    'спущу́сь</b> = Tôi xuống ngay đây.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спуска́ться</b> (CHT) · <b>пусти́ть</b> thả cho đi · '
    '<b>опусти́ть</b> hạ xuống · <b>пропусти́ть</b> bỏ lỡ</div>'
)

# --------------------------------------------------------------------- палатка
S["палатка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пала́т-</span>'
    '<span class="hd-gloss">GIAN PHÒNG — chính là <b>пала́та</b> (cùng gốc <i>palace</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">đuôi làm nhỏ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Gian phòng nhỏ» mang theo được ⇒ cái lều. Lều thì DỰNG bằng '
    '<b>ста́вить</b> (đặt đứng): <b>ста́вить пала́тку</b> = dựng lều.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пала́та</b> phòng bệnh, viện (quốc hội)</div>'
)

# --------------------------------------------------------------------- рюкзак
S["рюкзак"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn tiếng Đức <i>Rucksack</i> (<i>Rücken</i> «lưng» + <i>Sack</i> «bao»), '
    'không chẻ trong tiếng Nga — tiếng Anh cũng mượn y vậy: <i>rucksack</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Bao đeo lưng» ⇒ ba lô. Trọng âm nhảy ra đuôi từ cách 2: '
    '<b>рюкзака́</b>, <b>в рюкзаке́</b>.</div>'
)

# --------------------------------------------------------------------- мотор
S["мотор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn Latin <i>motor</i> «cái làm chuyển động», không chẻ — chính là '
    '<i>motor</i> tiếng Anh.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Máy làm xe, thuyền chạy ⇒ động cơ, mô tơ. Từ kỹ thuật chung hơn cho «động '
    'cơ» là <b>дви́гатель</b> (← <b>дви́гать</b> làm di chuyển).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мотоци́кл</b> xe máy · <b>мото́рный</b> (thuộc) động cơ · '
    '<b>мото́рная ло́дка</b> xuồng máy</div>'
)

# --------------------------------------------------------------------- прибывать
S["прибывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">TỚI NƠI; cũng là THÊM VÀO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бы-</span>'
    '<span class="hd-gloss">LÀ, CÓ MẶT (<b>быть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành, chia đều: <b>прибыва́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Tới mà có mặt» ⇒ đến nơi: <b>По́езд прибыва́ет на пе́рвый путь</b>. '
    '«Có thêm vào» ⇒ nước dâng, tăng lên: <b>Вода́ прибыва́ет</b> — cùng hình ảnh với '
    '<b>при́быль</b> lợi nhuận. Cặp HT: <b>прибы́ть</b>.</div>'
    '<div class="hd-warn">Giọng thông báo, giấy tờ (nhà ga, sân bay). Nói thường ngày thì dùng '
    '<b>приезжа́ть</b>, <b>приходи́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прибы́ть</b> (HT) · <b>прибы́тие</b> sự đến · <b>при́быль</b> lợi '
    'nhuận · <b>быть</b> là, có</div>'
)

# --------------------------------------------------------------------- прибыть
S["прибыть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">TỚI NƠI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бы-ть</span>'
    '<span class="hd-gloss">LÀ, CÓ MẶT — chính là <b>быть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thể HOÀN THÀNH của <b>прибыва́ть</b>: đã tới nơi, giọng trang trọng — '
    '<b>Делега́ция прибыла́ в Москву́</b>. Quá khứ trọng âm nhảy: <b>при́был</b> nhưng '
    '<b>прибыла́</b>.</div>'
    '<div class="hd-warn">Chia y như <b>быть → бу́ду</b>: <b>я прибу́ду</b>, <b>ты прибу́дешь</b> '
    '— thân <i>-буд-</i> không nhìn ra từ nguyên thể.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прибыва́ть</b> (CHT) · <b>прибы́тие</b> sự đến · <b>при́быль</b> lợi '
    'nhuận</div>'
)

# --------------------------------------------------------------------- подвезти
S["подвезти"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span>'
    '<span class="hd-gloss">SÁT LẠI GẦN — như <b>подойти́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-вез-ти́</span>'
    '<span class="hd-gloss">CHỞ (bằng xe) — chính là <b>везти́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chở ai tới sát chỗ họ cần ⇒ cho đi nhờ một đoạn. Gốc một chiều <i>вез-</i> '
    '+ tiền tố ⇒ HOÀN THÀNH; cặp CHT dùng <i>воз-</i>: <b>подвози́ть</b> (như <b>привезти́</b> / '
    '<b>привози́ть</b>). Quá khứ: <b>подвёз</b>, <b>подвезла́</b>.</div>'
    '<div class="hd-warn"><b>Тебя́ подвезти́?</b> = Để mình chở cậu một đoạn nhé?</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>подвози́ть</b> (CHT) · <b>везти́</b> chở · <b>привезти́</b> chở tới · '
    '<b>отвезти́</b> chở đi</div>'
)

# --------------------------------------------------------------------- подвозить
S["подвозить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span>'
    '<span class="hd-gloss">SÁT LẠI GẦN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-воз-и́ть</span>'
    '<span class="hd-gloss">CHỞ — <i>воз-</i> của <b>вози́ть</b> (е → о của <i>вез-</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thể CHƯA HOÀN THÀNH của <b>подвезти́</b>: hay cho đi nhờ, chở dần hàng '
    'tới. Ngôi «tôi» đổi з → ж, ngôi khác trọng âm lùi lên thân: <b>я подвожу́</b>, <b>ты '
    'подво́зишь</b>.</div>'
    '<div class="hd-warn"><b>я подвожу́</b> trùng với «tôi dẫn tới» của <b>подводи́ть</b>. Ngôi '
    'khác mới tách: <b>подво́зишь</b> / <b>подво́дишь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>подвезти́</b> (HT) · <b>вози́ть</b> chở (nhiều chiều) · '
    '<b>привози́ть</b> chở tới · <b>парово́з</b> đầu máy hơi nước</div>'
)

# --------------------------------------------------------------------- кто-либо
S["кто-либо"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кто</span>'
    '<span class="hd-gloss">AI (từ hỏi)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-либо</span>'
    '<span class="hd-gloss">«bất kỳ» — chính là <b>ли́бо</b> «hoặc là»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Hoặc người này hoặc người kia, ai cũng được» ⇒ bất kỳ ai. Nghĩa gần như '
    '<b>кто́-нибудь</b>, nhưng giọng VĂN VIẾT, trang trọng: <b>Е́сли кто́-либо узна́ет…</b> Nếu bất '
    'kỳ ai biết được… Chỉ phần <b>кто</b> biến cách: <b>кого́-либо</b>.</div>'
    '<div class="hd-warn">Đã có thật một người, chỉ không biết tên ⇒ <b>кто́-то</b>, không dùng '
    '<b>кто́-либо</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кто́-нибудь</b> bất kỳ ai (văn nói) · <b>кто́-то</b> ai đó · '
    '<b>что́-либо</b> bất cứ gì · <b>ли́бо</b> hoặc là</div>'
)

# --------------------------------------------------------------------- обложка
S["обложка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">QUANH, BỌC KÍN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лож-</span>'
    '<span class="hd-gloss">ĐẶT — như <b>положи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">→ danh từ chỉ đồ vật</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái đặt bọc quanh» ⇒ bìa sách, bìa tạp chí: <b>на обло́жке</b> trên '
    'trang bìa. Chứa mặt chữ <b>ло́жка</b> (cái thìa) chỉ là tình cờ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обложи́ть</b> bọc quanh, bao vây · <b>положи́ть</b> đặt</div>'
)

# --------------------------------------------------------------------- папка
S["папка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn tiếng Đức <i>Pappe</i> «bìa cứng, các-tông» + đuôi <b>-ка</b>, không '
    'chẻ tiếp được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tấm bìa cứng gập đôi để kẹp giấy ⇒ bìa hồ sơ, cặp tài liệu; trên máy tính '
    '⇒ thư mục: <b>созда́ть но́вую па́пку</b> tạo thư mục mới.</div>'
    '<div class="hd-warn">Cùng mặt chữ, khác từ: <b>па́пка</b> thân mật = bố (<b>па́па</b> + -ка). '
    'Ngữ cảnh tách được.</div>'
)

# --------------------------------------------------------------------- завещание
S["завещание"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">завещ-</span>'
    '<span class="hd-gloss">DẶN LẠI — từ <b>завеща́ть</b>; -вещ- là -вет- «nói» (т → щ) của '
    '<b>отве́т</b>, <b>сове́т</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ние</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lời DẶN LẠI cho người ở lại ⇒ di chúc. Cùng gốc: <b>заве́т</b> lời dặn, '
    'giao ước — <b>Ве́тхий Заве́т</b> là Cựu Ước, đúng như <i>testament</i> trong tiếng Anh vừa là '
    'di chúc vừa là tên hai phần Kinh Thánh.</div>'
    '<div class="hd-warn"><b>оста́вить завеща́ние</b> = để lại di chúc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>завеща́ть</b> để lại (theo di chúc) · <b>заве́т</b> lời dặn · '
    '<b>отве́т</b> câu trả lời · <b>сове́т</b> lời khuyên</div>'
)

# --------------------------------------------------------------------- опубликовать
S["опубликовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">tiền tố đổi sang thể HT, không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-публик-</span>'
    '<span class="hd-gloss">CÔNG CHÚNG (<b>пу́блика</b>) — chính là <i>public</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова́ть</span>'
    '<span class="hd-gloss">-овать → -ую: <b>опублику́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đưa ra trước CÔNG CHÚNG ⇒ đăng, công bố — y như <i>publish</i> ← '
    '<i>public</i>. Cặp CHT: <b>публикова́ть</b>.</div>'
    '<div class="hd-warn">Bị động rất hay gặp: <b>Статья́ опублико́вана</b> = Bài báo đã được '
    'đăng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пу́блика</b> công chúng, khán giả · <b>публика́ция</b> bài đăng, ấn '
    'phẩm · <b>публи́чный</b> công khai</div>'
)

# --------------------------------------------------------------------- публиковать
S["публиковать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">публик-</span>'
    '<span class="hd-gloss">CÔNG CHÚNG (<b>пу́блика</b>) — chính là <i>public</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова́ть</span>'
    '<span class="hd-gloss">-овать → -ую: <b>публику́ю</b>, <b>публику́ешь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thể CHƯA HOÀN THÀNH: đưa ra trước công chúng ⇒ đăng, xuất bản, thường '
    'là đều đặn: <b>Журна́л публику́ет статьи́ о нау́ке</b>. Cặp HT chỉ thêm <b>о-</b>: '
    '<b>опубликова́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>опубликова́ть</b> (HT) · <b>пу́блика</b> công chúng · '
    '<b>публика́ция</b> bài đăng, ấn phẩm</div>'
)

# --------------------------------------------------------------------- печать
S["печать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">печа́т-</span>'
    '<span class="hd-gloss">IN, ĐÓNG DẤU — thân của <b>печа́тать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ь</span>'
    '<span class="hd-gloss">danh từ giống cái — đuôi <b>-ь</b> không tự báo giống</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái ấn xuống để in dấu ⇒ con dấu: <b>кру́глая печа́ть</b> con dấu tròn. '
    'Mọi thứ được IN ra ⇒ ngành in, báo chí.</div>'
    '<div class="hd-warn"><b>свобо́да печа́ти</b> = tự do báo chí.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>печа́тать</b> in · <b>впечатле́ние</b> ấn tượng · <b>опеча́тка</b> '
    'lỗi in · <b>печа́тный</b> (thuộc) in</div>'
)

# --------------------------------------------------------------------- регистрация
S["регистрация"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">регистр-</span>'
    '<span class="hd-gloss">SỔ ĐĂNG KÝ — <i>register</i> tiếng Anh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ция</span>'
    '<span class="hd-gloss">= <i>-ation</i>, đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ghi tên vào sổ ⇒ đăng ký — chính là <i>registration</i>. Ở Nga người nước '
    'ngoài còn nghe từ này cho thủ tục khai báo tạm trú.</div>'
    '<div class="hd-warn"><b>пройти́ регистра́цию</b> = làm thủ tục đăng ký, check-in (sân bay, '
    'khách sạn, tài khoản).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>регистри́ровать</b> đăng ký · <b>зарегистри́роваться</b> đăng ký '
    '(cho mình) · <b>регистрату́ра</b> quầy tiếp đón (phòng khám)</div>'
)

B = {
    "docbangmat": 91,
    "loitubat": 0,
    "nguonsai": 2,
    "baolen": [
        "VA CHẠM KHÔNG GỠ ĐƯỢC: кто́-либо {bất cứ ai, bất kỳ ai, có ai} chứa trọn đề кто́-нибудь[k112, đã nạp, mồ côi] {bất kỳ ai, có ai}; cùng badge pron, gloss Anh của кто́-либо không có nghĩa nào khác để tách. Không thêm ngoặc, không cắt nghĩa, không viết V. User quyết.",
        "THÊM 1 mục MIEN_TRU (data/huongdan/mientru.py): тупи́к — đồng tự thật, chính từ đầu thẻ; nouns.csv có dòng ту'пик (animate=1 = chim puffin, glossed nhầm dead end) thắng dòng тупи'к. Cùng lớp замо́к/мука́. Agent k172 từng đề xuất đúng mục này. Luồng chính duyệt; lùi lại = xoá mục đó và bỏ in đậm тупи́к trong ô đỏ.",
        "Nguồn sai đã bác (2): (a) BAT THUONG của мастерска́я gọi мастерско́й/мастерску́ю là «nguyên âm chạy» — thật ra là biến cách tính từ, thẻ viết đúng thế; (b) nouns.csv dòng ту́пик (xem trên).",
        "V cần duyệt: кре́пость (+độ bền, độ đậm — gloss strength), рюкза́к («ba lô, túi đeo vai» → «ba lô»: túi đeo vai là сумка через плечо, gloss chỉ có backpack), прибыва́ть (+tăng lên — gloss increase), печа́ть (+báo chí, sự in ấn — gloss the press/printing). Chưa tự chạy `vacham` cho V mới: «báo chí» có thể đụng thẻ пре́сса nếu thẻ đó có đề chỉ «báo chí».",
        "Không chắc (đã viết nhưng nên biết): пала́тка = пала́та + -ка (từ nguyên theo Vasmer như tôi nhớ, không ghi Mức tin); па́пка ← Đức Pappe; завеща́ние ← -вещ-/-вет- «nói» (отве́т, сове́т) — từ nguyên chuẩn nhưng là từ nguyên, không phải luật suy ra.",
        "Họ hàng cố ý vắng: рюкза́к, па́пка (từ mượn đứng một mình). Đồng tự па́пка «bố» nêu thành ô đỏ.",
    ],
}
