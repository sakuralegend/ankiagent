# -*- coding: utf-8 -*-
"""k149 — actions: 9 cặp/nhóm động từ + 3 từ lẻ, trục là khuôn у- + GỐC TÍNH TỪ + -ить.

Không khối hệ thống. Chỗ phải khớp với thẻ đã có:
(1) у- «làm cho TRỞ NÊN…» + -лучш-/-меньш-/-велич- — khớp улучша́ть/улу́чшить (k137);
    vế HT kéo trọng âm về gốc so sánh hơn (улу́чшить, уме́ньшиться) như k137 đã dạy;
(2) -кры- «CHE, ĐẬY», ы → о khi chia — khớp закры́ть/закрыва́ть (k85, k87);
(3) тра́т- «TIÊU HAO», т → ч — khớp тра́тить/потра́тить (k97);
(4) цен- «GIÁ» — khớp цена́/це́нный/оцени́ть (k86, k128, k138);
(5) quá khứ + -ый ⇒ tính từ — khớp уста́лый (k117);
(6) обы́кн- «QUEN» — khớp обыкнове́нный/обы́чный (k108); обы́чай thuộc k148 (chỉ nhắc tên).
"""

V = {
    "увеличиваться": "gia tăng, to ra",     # bỏ «dần» — nhãn thể trá hình; RÚT «tăng lên» — trùng поднима́ться (CHT, -ся)
    "увеличиться": "gia tăng, to ra",       # RÚT «tăng lên» (вы́расти, подня́ться) + «lớn lên» (вы́расти — nghĩa người lớn lên, nới rộng); gloss: increase / get bigger
    "уменьшаться": "giảm đi, nhỏ lại",      # bỏ «dần» — nhãn thể; cùng dòng vế HT, badge thể tách
    "мерить": "đo, thử đồ",                 # bỏ ngoặc «(quần áo)»; «thử» trơn trùng проверя́ть (CHT) → «thử đồ» (gloss: try on)
    "померить": "đo, thử đồ",               # như ме́рить; badge thể tách
    "провожать": "tiễn",                    # RÚT «đưa» — trùng дава́ть; bỏ ngoặc «(ai đi đâu)»
    "употребить": "dùng, sử dụng, tiêu thụ",   # bỏ «(một lần)»; thêm «tiêu thụ» (gloss: consume) — vẫn trùng «dùng, sử dụng», xem baolen
    "употреблять": "dùng, sử dụng, tiêu thụ",  # thêm «tiêu thụ» (gloss: consume / ingest) — vẫn trùng по́льзоваться, xem baolen
    "беречь": "giữ gìn, tiết kiệm",         # RÚT «chăm sóc» — trùng забо́титься; thêm «tiết kiệm» (gloss: save / use sparingly) — «giữ gìn» vẫn trùng храни́ть
    "сберечь": "bảo quản, tiết kiệm",       # bỏ «giữ gìn được» — «được» là nhãn thể, «giữ gìn» trùng сохрани́ть (HT); gloss: economize on / save
    "необыкновенный": "khác thường",        # RÚT «phi thường» — trùng удиви́тельный
    "улучшаться": "khá lên, được cải thiện",  # bỏ «dần» — nhãn thể; cùng dòng vế HT, badge thể tách
}

S = {}

# ------------------------------------------------------------- меньшинство
S["меньшинство"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ме́ньш-</span>'
    '<span class="hd-gloss">ÍT HƠN — chính là <b>ме́ньше</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-инств-о́</span>'
    '<span class="hd-gloss">đuôi danh từ giống trung — y như <b>большинство́</b> đa số</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Phần ít hơn» ⇒ thiểu số. Vế đối <b>большинство́</b> «phần nhiều hơn» '
    '(<b>бо́льше</b>) ⇒ đa số — cùng khuôn, chỉ đổi gốc so sánh hơn.</div>'
    '<div class="hd-warn">Số nhiều trọng âm lùi vào thân: <b>национа́льные меньши́нства</b> = '
    'các dân tộc thiểu số.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ме́ньше</b> ít hơn · <b>ме́ньший</b> nhỏ hơn · '
    '<b>большинство́</b> đa số · <b>уме́ньшиться</b> giảm đi</div>'
)

# ------------------------------------------------------------- увеличиваться
S["увеличиваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">làm cho TRỞ NÊN…</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вели́ч-</span>'
    '<span class="hd-gloss">LỚN — <b>вели́кий</b>, <i>к → ч</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть-ся</span>'
    '<span class="hd-gloss">thể chưa hoàn thành + TỰ nó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Tự trở nên lớn hơn» ⇒ tăng, to ra, đang diễn ra: '
    '<i>Населе́ние увели́чивается</i> dân số đang tăng. Trọng âm đứng yên ở <i>ли́</i>: '
    '<b>увели́чивается</b>. Bỏ <i>-ся</i> là <b>увели́чивать</b> làm tăng cái gì.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>увели́читься</b> (HT) · <b>увели́чивать</b> làm tăng · '
    '<b>увеличе́ние</b> sự gia tăng · <b>вели́кий</b> vĩ đại</div>'
)

# ------------------------------------------------------------- увеличиться
S["увеличиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-вели́ч-</span>'
    '<span class="hd-gloss">làm cho LỚN — <b>вели́кий</b>, <i>к → ч</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить-ся</span>'
    '<span class="hd-gloss">đuôi lớp 2 + TỰ nó: <b>увели́чится</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng khuôn <i>у- + gốc tính từ + -ить</i> với <b>улу́чшить</b> '
    '«làm cho tốt hơn». Thêm <i>-ся</i> thì cái tăng là chủ ngữ: <i>Це́ны увели́чились</i> '
    'giá đã tăng.</div>'
    '<div class="hd-warn">Tăng BAO NHIÊU: <i>на</i> + cách 4 — <b>увели́читься на де́сять '
    'проце́нтов</b>; tăng mấy LẦN: <i>в</i> + cách 4 — <b>в два ра́за</b> gấp đôi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>увели́чиваться</b> (CHT) · <b>увели́чить</b> phóng to · '
    '<b>увеличе́ние</b> sự gia tăng · <b>уме́ньшиться</b> giảm đi</div>'
)

# ------------------------------------------------------------- уменьшаться
S["уменьшаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">làm cho TRỞ NÊN…</span></div>'
    '<div class="hd-row"><span class="hd-piece">-меньш-</span>'
    '<span class="hd-gloss">ÍT HƠN, NHỎ HƠN — <b>ме́ньше</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть-ся</span>'
    '<span class="hd-gloss">thể chưa hoàn thành, chia đều + TỰ nó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vế đối của <b>увели́чиваться</b>: tự nhỏ đi, đang giảm. Trọng âm ở '
    'đuôi: <b>уменьша́ется</b>; vế HT <b>уме́ньшиться</b> kéo về <i>ме́</i> như '
    '<b>ме́ньше</b> — y chỗ lệch của <b>улучша́ть</b> / <b>улу́чшить</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уме́ньшиться</b> (HT) · <b>уменьше́ние</b> sự giảm · '
    '<b>ме́ньше</b> ít hơn · <b>меньшинство́</b> thiểu số</div>'
)

# ------------------------------------------------------------- уменьшиться
S["уменьшиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">làm cho TRỞ NÊN…</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ме́ньш-</span>'
    '<span class="hd-gloss"><b>ме́ньше</b> ít hơn — trọng âm giữ nguyên</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить-ся</span>'
    '<span class="hd-gloss">đuôi lớp 2 + TỰ nó: <b>уме́ньшится</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Khuôn <i>у- + so sánh hơn + -ить</i> như <b>улу́чшить</b>; thêm '
    '<i>-ся</i> = «tự trở nên ít hơn» ⇒ giảm. Giảm bao nhiêu / mấy lần vẫn là <i>на</i> / '
    '<i>в</i> + cách 4 như <b>увели́читься</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уменьша́ться</b> (CHT) · <b>уме́ньшить</b> làm giảm · '
    '<b>ме́ньше</b> ít hơn · <b>увели́читься</b> tăng</div>'
)

# ------------------------------------------------------------- мерить
S["мерить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ме́р-</span>'
    '<span class="hd-gloss">gốc ĐO — <b>ме́ра</b> thước đo, mức độ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp 2, trọng âm đứng yên: <b>ме́рю, ме́ришь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đo kích thước: <b>ме́рить температу́ру</b> đo nhiệt độ. Thử quần áo '
    'cũng là «đo» cái áo lên người xem có vừa không. Cặp HT: <b>поме́рить</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поме́рить</b> (HT) · <b>ме́ра</b> mức, biện pháp · '
    '<b>изме́рить</b> đo đạc · <b>приме́рочная</b> phòng thử đồ</div>'
)

# ------------------------------------------------------------- померить
S["померить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">đánh dấu XONG, không thêm nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ме́рить</span>'
    '<span class="hd-gloss">chính là <b>ме́рить</b> — đo</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đo xong, thử xong một lần. Chia như <b>ме́рить</b> nhưng là tương lai: '
    '<b>поме́рю</b> tôi sẽ thử; mệnh lệnh <b>поме́рь</b>.</div>'
    '<div class="hd-warn">Ở cửa hàng quần áo: <b>Мо́жно поме́рить?</b> = Tôi thử được không?</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ме́рить</b> (CHT) · <b>приме́рить</b> mặc thử · '
    '<b>приме́рочная</b> phòng thử đồ</div>'
)

# ------------------------------------------------------------- провожать
S["провожать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">đi QUA, dọc theo một đoạn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вож-</span>'
    '<span class="hd-gloss">DẪN — <i>вод-</i> của <b>води́ть</b>, <i>д → ж</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">thể chưa hoàn thành, chia đều: <b>провожа́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Dẫn đi một đoạn» ⇒ đưa ai về, tiễn ai đi. Người được tiễn ở cách 4: '
    '<b>провожа́ть госте́й</b> tiễn khách.</div>'
    '<div class="hd-warn">Cặp HT <b>проводи́ть</b> trùng y mặt chữ với <b>проводи́ть</b> '
    '«trải qua (thời gian)» — phải nhìn ngữ cảnh: <b>проводи́ть дру́га на вокза́л</b> = tiễn '
    'bạn ra ga.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>проводи́ть</b> tiễn (HT) · <b>про́воды</b> buổi tiễn đưa · '
    '<b>води́ть</b> dẫn · <b>проводни́к</b> người dẫn đường, tiếp viên toa tàu</div>'
)

# ------------------------------------------------------------- истратить
S["истратить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ис-</span>'
    '<span class="hd-gloss">tới HẾT, cạn sạch</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тра́т-ить</span>'
    '<span class="hd-gloss">TIÊU HAO — chính là <b>тра́тить</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiêu tới hết. Ngôi «tôi» <i>т → ч</i> y như <b>тра́тить</b>: '
    '<b>истра́чу</b>, nhưng <b>истра́тишь</b>. Khác <b>потра́тить</b>: <i>по-</i> chỉ báo xong, '
    '<i>ис-</i> nhấn «sạch, không còn gì».</div>'
    '<div class="hd-warn">Tiêu VÀO việc gì: <i>на</i> + cách 4 — <b>Он истра́тил все де́ньги '
    'на маши́ну</b> = anh ấy tiêu sạch tiền vào xe.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тра́тить</b> tiêu (CHT) · <b>потра́тить</b> tiêu (HT) · '
    '<b>тра́та</b> khoản tiêu</div>'
)

# ------------------------------------------------------------- употребить
S["употребить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố — ở từ này không tách ra được nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-потреб-</span>'
    '<span class="hd-gloss">DÙNG — như <b>потреби́тель</b> người tiêu dùng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ngôi «tôi» chèn <i>л</i> sau <i>б</i>: <b>употреблю́</b>, nhưng '
    '<b>употреби́шь</b> — chữ <i>л</i> đó chính là thân của cặp CHT <b>употребля́ть</b>. '
    'Từ hơi sách vở: dùng TỪ NGỮ, ăn uống, dùng thuốc.</div>'
    '<div class="hd-warn">In trên bao bì: <b>Употреби́ть до…</b> = Hạn sử dụng đến ngày…</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>употребля́ть</b> (CHT) · <b>употребле́ние</b> cách dùng · '
    '<b>потреби́тель</b> người tiêu dùng · <b>потре́бность</b> nhu cầu</div>'
)

# ------------------------------------------------------------- употреблять
S["употреблять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-потребл-</span>'
    '<span class="hd-gloss">DÙNG — như <b>употреби́ть</b>, đã chèn <i>л</i> sau <i>б</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ть</span>'
    '<span class="hd-gloss">thể chưa hoàn thành, chia đều: <b>употребля́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dùng nói chung, thường xuyên: <i>Э́то сло́во ча́сто употребля́ется</i> '
    'từ này hay được dùng. Hay đi với đồ ăn uống: <b>употребля́ть алкого́ль</b> uống rượu bia.</div>'
    '<div class="hd-warn">Cái được dùng ở cách 4, khác <b>по́льзоваться</b> + cách 5. '
    'Nói chuyện hằng ngày thì <b>испо́льзовать</b> hay <b>по́льзоваться</b> tự nhiên hơn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>употреби́ть</b> (HT) · <b>употребле́ние</b> cách dùng · '
    '<b>потреби́тель</b> người tiêu dùng</div>'
)

# ------------------------------------------------------------- беречь
S["беречь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бере́г-</span>'
    '<span class="hd-gloss">gốc GIỮ GÌN — chữ <i>г</i> chỉ lộ ra khi chia</span></div>'
    '<div class="hd-row"><span class="hd-piece">-чь</span>'
    '<span class="hd-gloss">đuôi nguyên thể: <i>г + ть</i> chập thành <i>чь</i>, như '
    '<b>мочь</b> → <b>могу́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chia: <b>берегу́, бережёшь, берегу́т</b> — <i>г</i> ở «tôi» và «họ», '
    '<i>ж</i> ở giữa. Quá khứ trọng âm ra đuôi: <b>берегла́, берегли́</b>. Giữ cho khỏi hỏng, '
    'khỏi mất: <b>бере́чь вре́мя</b> tiết kiệm thời gian.</div>'
    '<div class="hd-warn"><b>Береги́ себя́!</b> = Giữ gìn sức khoẻ nhé! — câu chào khi chia tay.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сбере́чь</b> (HT) · <b>бе́режный</b> nâng niu, cẩn thận · '
    '<b>сбереже́ния</b> tiền tiết kiệm</div>'
)

# ------------------------------------------------------------- сберечь
S["сберечь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">đánh dấu XONG, không thêm nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бере́чь</span>'
    '<span class="hd-gloss">GIỮ GÌN — chính là <b>бере́чь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giữ được tới cùng, không để mất: <b>сбере́чь здоро́вье</b>, '
    '<b>сбере́чь де́ньги</b> để dành tiền. Chia y <b>бере́чь</b>: <b>сберегу́, сбережёшь</b>; '
    'quá khứ <b>сберёг, сберегла́</b>.</div>'
    '<div class="hd-warn"><b>Сберба́нк</b> — ngân hàng lớn nhất nước Nga — viết tắt từ '
    '«ngân hàng TIẾT KIỆM», cùng gốc này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бере́чь</b> (CHT) · <b>сбереже́ния</b> tiền tiết kiệm · '
    '<b>бе́режный</b> nâng niu</div>'
)

# ------------------------------------------------------------- закрываться
S["закрываться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">закрыва́-ть</span>'
    '<span class="hd-gloss">chính là <b>закрыва́ть</b> — đóng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">TỰ nó — không ai làm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tự đóng lại, nói về giờ giấc thường lệ: <i>Магази́н закрыва́ется в '
    'во́семь</i> cửa hàng đóng cửa lúc tám giờ. Đối của <b>открыва́ться</b>. Cặp HT: '
    '<b>закры́ться</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>закрыва́ть</b> đóng · <b>закры́ться</b> đóng lại (HT) · '
    '<b>открыва́ться</b> mở ra · <b>кры́ша</b> mái nhà (cái che)</div>'
)

# ------------------------------------------------------------- закрыться
S["закрыться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">закры́-ть</span>'
    '<span class="hd-gloss">chính là <b>закры́ть</b> — đóng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">TỰ nó — không ai làm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thân hiện tại đổi <i>ы → о</i> y như <b>закры́ть</b> (<b>закро́ю</b>): '
    '<b>закро́ется</b>. Tự đóng một lần: <i>Дверь закры́лась</i> cửa đã đóng lại. Lần đó có thể '
    'là lần cuối ⇒ đóng cửa hẳn: <i>Магази́н закры́лся</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>закры́ть</b> đóng · <b>закрыва́ться</b> (CHT) · '
    '<b>откры́ться</b> mở ra · <b>закры́тие</b> sự đóng cửa, bế mạc</div>'
)

# ------------------------------------------------------------- отсталый
S["отсталый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">отста́л-</span>'
    '<span class="hd-gloss">quá khứ của <b>отста́ть</b> «tụt lại phía sau»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">biến dạng quá khứ thành tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đã tụt lại» ⇒ lạc hậu: <b>отста́лая страна́</b> nước lạc hậu. '
    'Khuôn y hệt <b>уста́лый</b> (<b>уста́ть</b> → «đã mệt»).</div>'
    '<div class="hd-warn">Động từ gốc rất hay gặp ở mệnh lệnh: <b>Отста́нь!</b> = Để tôi yên! '
    '(nghĩa đen «tụt lại, đừng bám theo»).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отста́ть</b> / <b>отстава́ть</b> tụt lại, chậm · '
    '<b>отста́лость</b> sự lạc hậu · <b>уста́лый</b> mệt mỏi (cùng khuôn)</div>'
)

# ------------------------------------------------------------- необыкновенный
S["необыкновенный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не-</span>'
    '<span class="hd-gloss">KHÔNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-обыкнове́нный</span>'
    '<span class="hd-gloss">thông thường — xem thẻ <b>обыкнове́нный</b> (gốc <i>обы́кн-</i> QUEN)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Không thông thường» ⇒ khác thường, và nghiêng về KHEN: '
    '<b>необыкнове́нная красота́</b> vẻ đẹp hiếm có. Trạng từ <b>необыкнове́нно</b> = vô cùng.</div>'
    '<div class="hd-warn">Dạng ngắn giống đực chèn <i>е</i> vào giữa hai <i>н</i>: '
    '<b>необыкнове́нен</b>, còn lại giữ <i>нн</i>: <b>необыкнове́нна</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обыкнове́нный</b> thông thường · <b>обы́чный</b> thường lệ · '
    '<b>обы́чай</b> phong tục · <b>привы́кнуть</b> quen</div>'
)

# ------------------------------------------------------------- ценить
S["ценить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">цен-</span>'
    '<span class="hd-gloss">GIÁ — <b>цена́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đặt giá cao cho một thứ ⇒ quý trọng: <b>цени́ть дру́жбу</b> quý tình bạn. '
    'Trọng âm ở đuôi chỉ tại ngôi «tôi»: <b>ценю́</b>, rồi lùi về gốc — <b>це́нишь, це́нят</b> '
    '(y như <b>оцени́ть</b>).</div>'
    '<div class="hd-warn">Vế HT theo nghĩa «trân trọng» là <b>оцени́ть</b>: <b>Я оцени́л ва́шу '
    'по́мощь</b> = tôi rất quý sự giúp đỡ của anh.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>цена́</b> giá · <b>це́нный</b> có giá trị · '
    '<b>оцени́ть</b> đánh giá · <b>драгоце́нный</b> quý báu</div>'
)

# ------------------------------------------------------------- улучшаться
S["улучшаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">улучша́-ть</span>'
    '<span class="hd-gloss">chính là <b>улучша́ть</b> — làm cho tốt hơn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">TỰ nó — không ai làm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tự trở nên tốt hơn, đang diễn ra: <i>Пого́да улучша́ется</i> thời tiết '
    'đang tốt lên. Cặp HT <b>улу́чшиться</b> kéo trọng âm về <i>лу́</i> như <b>лу́чше</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>улучша́ть</b> cải thiện · <b>улу́чшиться</b> (HT) · '
    '<b>улучше́ние</b> sự cải thiện · <b>уменьша́ться</b> giảm đi (cùng khuôn)</div>'
)

# ------------------------------------------------------------- улучшиться
S["улучшиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">улу́чши-ть</span>'
    '<span class="hd-gloss">chính là <b>улу́чшить</b> — làm cho tốt hơn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">TỰ nó — không ai làm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Khuôn <i>у- + so sánh hơn + -ить + -ся</i> = «tự trở nên … hơn»; cùng '
    'lô có <b>уме́ньшиться</b> «tự ít đi». Trọng âm đứng yên ở <i>лу́</i>: '
    '<b>улу́чшится, улу́чшатся</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>улу́чшить</b> cải thiện · <b>улучша́ться</b> (CHT) · '
    '<b>улучше́ние</b> sự cải thiện · <b>уху́дшиться</b> tệ đi</div>'
)

# Báo cáo của người soạn lô (đếm thật).
B = {
    "docbangmat": 104,
    "loitubat": 3,   # необыкнове́нен: tả sai «bỏ một н» → đúng là chèn е giữa hai н · -инство glossed bịa «phần, khối» → «đuôi danh từ giống trung» · Дверь закры́лась dịch «sập lại» (sai sắc thái) → «đã đóng lại»
    "nguonsai": 0,
    "baolen": [
        "KHÔNG GỠ ĐƯỢC: употреблять/употребить vẫn trùng «dùng, sử dụng» với по́льзоваться (k123) + испо́льзовать (hai thể). Đã THÊM «tiêu thụ» (gloss consume/ingest) để dòng khác nhau, nhưng máy vẫn báo trùng — muốn sạch hẳn phải sửa thẻ mồ côi hoặc chấp nhận.",
        "KHÔNG GỠ ĐƯỢC: бере́чь «giữ gìn, tiết kiệm» vẫn trùng «giữ gìn» với храни́ть (k125, cùng CHT). Đã RÚT «chăm sóc» (trùng забо́титься) và THÊM «tiết kiệm» (gloss save/use sparingly).",
        "V cần duyệt — THAY chữ chứ không chỉ rút: увеличи(ва)ться «tăng lên» → «gia tăng, to ra» (tăng lên trùng вы́расти/подня́ться/поднима́ться; «lớn lên» là nghĩa người lớn lên, bỏ); ме́рить/поме́рить «thử (quần áo)» → «thử đồ» (thử trơn trùng проверя́ть); сбере́чь «giữ gìn được, bảo quản» → «bảo quản, tiết kiệm» («được» là nhãn thể, «giữ gìn» trùng сохрани́ть).",
        "V rút gọn: провожа́ть → «tiễn» (bỏ «đưa», trùng дава́ть); необыкнове́нный → «khác thường» (bỏ «phi thường», trùng удиви́тельный); bỏ chữ «dần» ở увеличиваться/уменьшаться/улучшаться (nhãn thể trá hình).",
        "Cửa TRONG AM LECH báo берёг (quá khứ бере́чь) ↔ бе́рег «bờ» — từ đồng tự thật, KHÔNG nới MIEN_TRU; đã viết vòng bằng берегла́, берегли́.",
        "Không chắc: câu «употребля́ть hơi sách vở, đời thường nói испо́льзовать/по́льзоваться» là cảm nhận văn phong, chưa có nguồn máy xác nhận.",
        "Không chắc: ме́рить nghĩa «thử đồ» là khẩu ngữ; chuẩn sách vở là приме́рить — thẻ chỉ ghi приме́рить ở Họ hàng, không nói rõ điều này.",
        "Hạ tầng: scratchpad dùng chung giữa các lô song song — script dò nghĩa của tôi bị lô khác ghi đè giữa chừng (y như k138 đã báo).",
    ],
}
