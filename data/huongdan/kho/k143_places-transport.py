# -*- coding: utf-8 -*-
"""k143 — places::transport: tiền tố + gốc chuyển động (-езжа-/-ехать, -лет-, -воз-/-вез-) và vài danh từ nơi chốn."""

# 🔴 KHÔNG dựng biến khối dùng chung (HE/LUAT/THE…) rồi cộng vào mọi thẻ.

S = {}

S["стройка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">строй-</span>'
    '<span class="hd-gloss">XÂY — gốc của <b>стро́ить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">đuôi biến việc làm thành danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Chỗ đang xây» ⇒ công trường, công trình đang dựng: '
    '<b>рабо́тать на стро́йке</b> = làm ở công trường (đi với <b>на</b>). '
    'Số nhiều cách 2 chèn <b>е</b> vào chỗ <b>й</b>: <b>стро́ек</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стро́ить</b> xây · <b>постро́ить</b> xây xong · '
    '<b>строи́тель</b> thợ xây · <b>строи́тельство</b> sự xây dựng</div>'
)

S["гимназия"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn, không chẻ theo gốc Nga: qua tiếng Đức <i>Gymnasium</i> '
    '← Hy Lạp <i>gymnasion</i> «nơi luyện tập».</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Châu Âu dùng chữ «nơi luyện tập» cho trường luyện TRÍ: ở Nga '
    'là trường trung học chất lượng cao, phải thi mới vào. Đuôi <b>-ия</b> ⇒ giống cái.</div>'
    '<div class="hd-warn">Không phải phòng gym — phòng tập là <b>спортза́л</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гимна́стика</b> thể dục · <b>гимна́ст</b> vận động viên thể dục '
    '· <b>гимнази́ст</b> học sinh trường này</div>'
)

S["консерватория"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">консерв-</span>'
    '<span class="hd-gloss">GIỮ GÌN — Latin <i>conservare</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-атор-ия</span>'
    '<span class="hd-gloss">nơi chốn, danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng chữ với tiếng Anh <i>conservatory</i>: nơi «giữ gìn» và truyền '
    'nghề nhạc ⇒ nhạc viện. <b>учи́ться в консервато́рии</b> = học nhạc viện.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>консе́рвы</b> đồ hộp (thức ăn được «giữ») · '
    '<b>консервати́вный</b> bảo thủ</div>'
)

S["вверху"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">Ở TRONG, ở</span></div>'
    '<div class="hd-row"><span class="hd-piece">-верх-у́</span>'
    '<span class="hd-gloss"><b>верх</b> PHẦN TRÊN, đuôi chỉ chỗ <b>-у́</b> (như <b>в лесу́</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ở ĐÂU ⇒ ở phía trên, trên cao: <b>вверху́ страни́цы</b> = '
    'ở phía trên trang giấy. Đi lên là <b>вверх</b> (cùng mảnh, bỏ đuôi -у́).</div>'
    '<div class="hd-warn"><b>вверху́</b> ≈ <b>наверху́</b> (ở trên), nhưng chỉ '
    '<b>наверху́</b> mới hay dùng cho «trên lầu».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вверх</b> hướng lên · <b>наверху́</b> ở trên · '
    '<b>ве́рхний</b> ở trên · <b>внизу́</b> ở dưới (đối của nó)</div>'
)

S["командировка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">команд-</span>'
    '<span class="hd-gloss">LỆNH — <b>кома́нда</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-иров-</span>'
    '<span class="hd-gloss">đuôi động từ mượn: <b>командирова́ть</b> cử đi công tác</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-а</span>'
    '<span class="hd-gloss">biến thành danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Được «lệnh cử đi» ⇒ chuyến công tác. Số nhiều cách 2 '
    'chèn <b>о</b>: <b>командиро́вок</b>.</div>'
    '<div class="hd-warn"><b>Он в командиро́вке.</b> = Anh ấy đang đi công tác · '
    '<b>е́хать в командиро́вку</b> = đi công tác.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кома́нда</b> lệnh; đội · <b>команди́р</b> người chỉ huy · '
    '<b>командирова́ть</b> cử đi công tác</div>'
)

S["таможня"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тамож-</span>'
    '<span class="hd-gloss">từ <b>тамга́</b> «con dấu, thuế» (gốc Turk), г → ж</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-я</span>'
    '<span class="hd-gloss">nơi chốn, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nơi đóng dấu, thu thuế hàng qua biên giới ⇒ hải quan. '
    'Số nhiều cách 2 chèn <b>е</b>, không có <b>ь</b>: <b>тамо́жен</b>.</div>'
    '<div class="hd-warn"><b>проходи́ть тамо́жню</b> = làm thủ tục hải quan '
    '(nghĩa đen «đi qua hải quan»).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тамо́женник</b> nhân viên hải quan · '
    '<b>тамо́женный</b> thuộc hải quan</div>'
)

S["маршрутка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">маршру́т-</span>'
    '<span class="hd-gloss">TUYẾN — <b>маршру́т</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-а</span>'
    '<span class="hd-gloss">đuôi RÚT GỌN cụm hai chữ thành một</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nói tắt của <b>маршру́тное такси́</b> «taxi chạy tuyến». Cùng khuôn: '
    '<b>электри́чка</b> = <b>электри́ческий по́езд</b> tàu điện ngoại ô. '
    'Số nhiều cách 2 chèn <b>о</b>: <b>маршру́ток</b>.</div>'
    '<div class="hd-warn">Đi bằng nó thì <b>на</b> + cách 6: <b>е́хать на маршру́тке</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>маршру́т</b> lộ trình, tuyến · <b>маршру́тный</b> thuộc tuyến</div>'
)

S["автобусный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">авто́бус-</span>'
    '<span class="hd-gloss">XE BUÝT — <b>авто́бус</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi «thuộc về» danh từ đứng trước</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ + <b>-ный</b> = tính từ «thuộc …»: '
    '<b>авто́бусная остано́вка</b> trạm xe buýt, <b>авто́бусный биле́т</b> vé xe buýt. '
    'Tính từ kiểu «thuộc về» này không dùng dạng ngắn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>авто́бус</b> xe buýt · <b>тролле́йбус</b> xe buýt điện '
    '(cùng mảnh <b>-бус</b>)</div>'
)

S["подъезжать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span>'
    '<span class="hd-gloss">TỚI SÁT, lại gần</span></div>'
    '<div class="hd-row"><span class="hd-piece">ъ</span>'
    '<span class="hd-gloss">dấu cứng ngăn <b>д</b> với <b>е</b> — không mang nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-езжа́-ть</span>'
    '<span class="hd-gloss">gốc ĐI BẰNG XE (như <b>приезжа́ть</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đi xe tới sát một chỗ: <b>Авто́бус подъезжа́ет к остано́вке</b> = '
    'xe buýt đang vào trạm (đi với <b>к</b> + cách 3). Chia đều: <b>подъезжа́ю</b>. '
    'Cặp hoàn thành: <b>подъе́хать</b> (luật chữ <b>ъ</b> ở thẻ đó).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>подъе́хать</b> (HT) · <b>подъе́зд</b> lối vào chung cư · '
    '<b>подходи́ть</b> đi bộ tới gần · <b>приезжа́ть</b> đến bằng xe</div>'
)

S["подъехать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span>'
    '<span class="hd-gloss">TỚI SÁT, lại gần</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ъе́хать</span>'
    '<span class="hd-gloss">đi xe — <b>е́хать</b>, chèn <b>ъ</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hoàn thành của <b>подъезжа́ть</b>. Chia như <b>е́хать</b>, thân đổi '
    'sang <b>-ед-</b>: <b>подъе́ду, подъе́дешь</b>. Hay gặp: <b>Я подъе́ду че́рез час</b> = '
    'một tiếng nữa tôi tới (bằng xe).</div>'
    '<div class="hd-warn">Gõ phải có <b>ъ</b>: tiền tố tận cùng bằng phụ âm đứng trước '
    '<b>е, ё, ю, я</b> thì chèn <b>ъ</b> — <b>подъе́зд</b>, <b>съесть</b>, <b>объясни́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>подъезжа́ть</b> (CHT) · <b>подъе́зд</b> lối vào chung cư · '
    '<b>подойти́</b> đi bộ tới gần · <b>прие́хать</b> đến bằng xe</div>'
)

S["выезжать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">RA NGOÀI, từ trong ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">-езжа́-ть</span>'
    '<span class="hd-gloss">gốc ĐI BẰNG XE (như <b>уезжа́ть</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đi xe RA khỏi một chỗ — gara, sân, thành phố — và vì thế cũng là '
    '«xuất phát»: <b>Мы выезжа́ем в во́семь</b> = tám giờ bọn mình xuất phát. Chia đều: '
    '<b>выезжа́ю</b>. Cặp hoàn thành: <b>вы́ехать</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́ехать</b> (HT) · <b>вы́езд</b> lối ra; sự xuất phát · '
    '<b>выходи́ть</b> đi bộ ra · <b>уезжа́ть</b> đi khỏi bằng xe</div>'
)

S["выехать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span>'
    '<span class="hd-gloss">RA NGOÀI — và luôn nhận trọng âm ở thể hoàn thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ехать</span>'
    '<span class="hd-gloss">đi xe — <b>е́хать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hoàn thành của <b>выезжа́ть</b>. Trọng âm nằm ở <b>вы́-</b> trong mọi '
    'dạng, như <b>вы́йти</b>. Thân chia lấy <b>-ед-</b>: <b>вы́еду, вы́едешь</b>.</div>'
    '<div class="hd-warn"><b>вы́ехать</b> = ra KHỎI một chỗ (nhìn từ chỗ xuất phát) · '
    '<b>уе́хать</b> = đi MẤT, không còn ở đây nữa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>выезжа́ть</b> (CHT) · <b>вы́езд</b> lối ra · '
    '<b>вы́йти</b> đi bộ ra · <b>уе́хать</b> đi khỏi bằng xe</div>'
)

S["прилетать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">TỚI NƠI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лет-а́ть</span>'
    '<span class="hd-gloss">gốc BAY — <b>лета́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bay tới nơi. Thêm tiền tố rồi thì <b>лета́ть</b> hết là «bay qua lại», '
    'chỉ còn là cặp chưa hoàn thành của <b>прилете́ть</b>: <b>Самолёт прилета́ет в шесть</b> = '
    'máy bay đến lúc sáu giờ. Chia đều: <b>прилета́ю</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прилете́ть</b> (HT) · <b>улета́ть</b> bay đi · '
    '<b>приезжа́ть</b> đến bằng xe · <b>самолёт</b> máy bay</div>'
)

S["прилететь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">TỚI NƠI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лете́ть</span>'
    '<span class="hd-gloss">bay — <b>лете́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hoàn thành của <b>прилета́ть</b>: đã bay tới nơi. Chia như '
    '<b>лете́ть</b>: <b>т → ч</b> ở ngôi «я» — <b>прилечу́</b>, nhưng <b>прилети́шь</b>.</div>'
    '<div class="hd-warn">Bảng ở sân bay: <b>Прилёт</b> = Chuyến đến · '
    '<b>Вы́лет</b> = Chuyến đi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прилета́ть</b> (CHT) · <b>прилёт</b> sự hạ cánh, chuyến đến · '
    '<b>улете́ть</b> bay mất · <b>прие́хать</b> đến bằng xe</div>'
)

S["перевозить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span>'
    '<span class="hd-gloss">SANG, từ chỗ này qua chỗ kia</span></div>'
    '<div class="hd-row"><span class="hd-piece">-воз-и́ть</span>'
    '<span class="hd-gloss">CHỞ — chính là <b>вози́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chở người, hàng, đồ đạc sang chỗ khác — người chuyển nhà là '
    '<b>переезжа́ть</b>, còn đồ đạc thì <b>перевози́ть</b>. Chia như <b>вози́ть</b>: '
    '«tôi» <i>з → ж</i>, trọng âm lùi — <b>перевожу́</b>, <b>перево́зишь</b>. '
    'Cặp hoàn thành: <b>перевезти́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>перевезти́</b> (HT) · <b>перево́зка</b> sự vận chuyển · '
    '<b>переезжа́ть</b> chuyển nhà · <b>вози́ть</b> chở qua lại</div>'
)

S["увезти"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">RỜI KHỎI, đi mất (như <b>уе́хать</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вез-ти́</span>'
    '<span class="hd-gloss">CHỞ bằng xe — <b>везти́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chở đi khỏi đây, mang đi mất. Quá khứ như <b>везти́</b>: '
    '<b>увёз</b> (không có -л), rồi trọng âm dồn về cuối: <b>увезла́</b>, <b>увезли́</b>. '
    'Cặp chưa hoàn thành: <b>увози́ть</b>.</div>'
    '<div class="hd-warn"><b>увезти́</b> = chở MẤT khỏi chỗ này · <b>отвезти́</b> = chở '
    'ĐẾN một chỗ (<b>отвезти́ в аэропо́рт</b> đưa ra sân bay).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>увози́ть</b> (CHT) · <b>везти́</b> chở · '
    '<b>отвезти́</b> chở đến · <b>уе́хать</b> đi khỏi bằng xe</div>'
)

S["увозить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">RỜI KHỎI, đi mất</span></div>'
    '<div class="hd-row"><span class="hd-piece">-воз-и́ть</span>'
    '<span class="hd-gloss">CHỞ — chính là <b>вози́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp chưa hoàn thành của <b>увезти́</b> (phép so <b>у-</b>/<b>от-</b> ở thẻ đó). '
    'Chia như <b>вози́ть</b>: «tôi» <i>з → ж</i>, trọng âm lùi — <b>увожу́</b>, <b>уво́зишь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>увезти́</b> (HT) · <b>вози́ть</b> chở qua lại · '
    '<b>привози́ть</b> chở đến · <b>уезжа́ть</b> đi khỏi bằng xe</div>'
)

S["ничей"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ни-</span>'
    '<span class="hd-gloss">PHỦ ĐỊNH «không … nào» (như <b>никто́</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-чей</span>'
    '<span class="hd-gloss">của ai — <b>че́й</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Không của ai» ⇒ vô chủ. Đổi giống như <b>че́й</b>: '
    '<b>ничья́ соба́ка</b>, <b>ничьё ме́сто</b>, <b>ничьи́ ве́щи</b>.</div>'
    '<div class="hd-warn"><b>ничья́</b> đứng một mình còn là danh từ: «hoà» trong thể thao, '
    'cờ — <b>сыгра́ть вничью́</b> = đá hoà.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>че́й</b> của ai · <b>никто́</b> không ai · '
    '<b>ничто́</b> không gì · <b>нигде́</b> không đâu</div>'
)

S["чей-нибудь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">чей-</span>'
    '<span class="hd-gloss">của ai — <b>че́й</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-нибудь</span>'
    '<span class="hd-gloss">«bất kỳ» — chưa có ai cụ thể, ai cũng được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỉ phần <b>че́й</b> đổi theo giống và cách, <b>-нибудь</b> giữ nguyên. '
    'Hay đứng trong câu hỏi, câu nhờ, câu tương lai: <b>Возьми́ чей-нибудь зонт</b> = lấy '
    'ô của ai cũng được.</div>'
    '<div class="hd-warn"><b>-то</b> = có thật, chỉ không rõ: <b>Тут чья́-то су́мка</b> · '
    '<b>-нибудь</b> = chưa xác định: <b>Ты ви́дел чью-нибудь су́мку?</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>чей-то</b> của ai đó · <b>кто́-нибудь</b> ai đó · '
    '<b>что́-нибудь</b> cái gì đó · <b>где́-нибудь</b> ở đâu đó</div>'
)

# ---- Field Vietnamese (đề bài deck 1-go) — README §2c: thuần danh sách nghĩa.
V = {
    "автобусный": "thuộc xe buýt",
    "подъезжать": "đi xe tới gần, lái xe tới sát",
    "подъехать": "đi xe tới gần, lái xe tới sát",
    "выезжать": "đi xe ra khỏi, lái xe ra",
    "выехать": "đi xe ra khỏi, lái xe ra",
    "прилетать": "bay đến, đến bằng máy bay",
    "прилететь": "bay đến, đến bằng máy bay",
    "перевозить": "chở sang, chở qua",
    "увезти": "chở đi mất, mang đi mất",
    "увозить": "chở đi mất, mang đi mất",
    "чей-нибудь": "của bất kỳ ai",
}

# ---- Báo cáo lô (đếm thật)
B = {
    "docbangmat": 95,
    "loitubat": 2,
    "nguonsai": 2,
    "baolen": [
        "nguonsai 1: tiep in so nhieu cach 2 cua таможня la 'тамо́жень' — sai chinh ta (sau ж khong viet ь o danh tu giong cai bien cach 1); the ghi тамо́жен.",
        "nguonsai 2: tiep in DANG NGAN авто́бусен/-на/-но/-ны cho автобусный — tinh tu quan he khong dung dang ngan; khong chep, the ghi thang la khong dung.",
        "loitubat 1: luat chu ъ o подъехать ban dau chi noi 'truoc е' trong khi vi du объясни́ть dung truoc я — da sua thanh 'truoc е, ё, ю, я'.",
        "loitubat 2: V cua вверху tung bi tu them 'tren cao' (noi rong, khong nam trong danh sach va cham) — da go, giu nguyen ban cu 'o tren, phia tren'.",
        "V can duyet — чей-нибудь: 'của ai đó (bất kỳ)' bo ngoac thi trung y het чей-то, rut gon khong go duoc; doi thanh 'của bất kỳ ai' (sat gloss anyone's). Day la VIET LAI chu khong phai rut gon — user duyet.",
        "V can duyet — перевозить: bo 'vận chuyển' (trung возить) thi 'chở' con lai qua mo (trung voi везти/возить ve nghia); viet lai 'chở sang, chở qua' theo tien to пере-. Mat nghia tu dien dau tien 'to transport' — user duyet.",
        "V can duyet — выезжать/выехать: bo 'khởi hành', 'đi', 'rời đi' (trung пойти/поехать/уходить); viet lai 'đi xe ra khỏi, lái xe ra' theo вы-. Mat nghia 'xuat phat' (dung that rat nhieu) vi поехать tren the dang giu 'xuất phát' — khong go duoc ma khong dung toi lo k80.",
        "V can duyet — увезти/увозить: bo 'chở đi' (trung повезти) va 'mang đi' (увозить se trung брать cung the CHT); doi thanh 'chở đi mất, mang đi mất'.",
        "V khac chi bo ngoac/nhan the: автобусный 'thuộc xe buýt', подъезжать/подъехать 'đi xe tới gần, lái xe tới sát', прилетать/прилететь 'bay đến, đến bằng máy bay'. Cap the CHT/HT dung chung mot dong — badge The tach.",
        "Soat va cham V lam tren ban ghep _input_k*.txt + V cac lo, KHONG doc Anki — neu user da sua tay the nao sau tiep thi co the lech; luong chinh nen chay congcu.py vacham sau nap.",
        "Khong chac: tu nguyen таможня <- тамга́ (goc Turk) la thuyet chuan (Vasmer) nen khong ha muc tin; гимна́стика ~ гимна́зия cung goc Hy Lap gymnazein.",
    ],
}
