# -*- coding: utf-8 -*-
"""k78 — động vật + đồ vật quanh nhà: từ mới user vừa thêm, các từ KHÔNG cùng họ.

Mỗi thẻ soạn độc lập, không ép một trục chung, không dựng khối hệ thống. Ba chỗ
cố ý nối nhau bằng ĐÚNG MỘT dòng chứ không lặp khối: bộ ba tên con vật
`-ица` (cái) / `-ёнок` (con) trải đủ ở đúng thẻ `тигр`, thẻ khác chỉ liệt kê dạng
của chính nó; đuôi `-ь` giống ĐỰC nói ở `медведь` rồi `олень` dẫn chiếu lại; luật
nguyên âm chạy cách 2 số nhiều của `-ка` nêu riêng trên từng thẻ `утка` /
`коробка` / `миска` bằng chính từ đó, không nêu thành bảng chung.
"""

S = {}

# -------------------------------------------------------------------- волк
S["волк"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn <b>волк-</b>, không bóc được tiền tố hay hậu tố nào.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đọc <b>волк</b> rồi đọc <i>wolf</i>: cùng một từ Ấn–Âu cổ, chỉ '
    'khác chữ cuối. Mọi từ phái sinh đều đổi <b>к → ч</b> (đúng luật <b>г/к/х → ж/ч/ш</b> '
    'đã học): <b>волчи́ца</b>, <b>волчо́нок</b>, <b>во́лчий</b>.</div>'
    '<div class="hd-warn">Số nhiều gãy làm đôi: cách 1 <b>во́лки</b> giữ trọng âm ở gốc, '
    'từ cách 2 trở đi nhảy ra đuôi — <b>волко́в</b>, <b>волка́м</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>волчи́ца</b> sói cái · <b>волчо́нок</b> sói con · '
    '<b>во́лчий</b> thuộc về sói</div>'
)

# ------------------------------------------------------------------- заяц
S["заяц"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">зай-</span>'
    '<span class="hd-gloss">gốc THỎ (lộ ra ở <b>за́йчик</b>, <b>за́йка</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-яц</span>'
    '<span class="hd-gloss">đuôi; chữ <b>я</b> chỉ ghé qua cách 1</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dạng gốc thật là <b>зай-</b>: ra khỏi cách 1 là <b>я</b> biến mất '
    'sạch — <b>за́яц → за́йца, за́йцу, за́йцем</b>, số nhiều <b>за́йцы</b>. Trọng âm đứng '
    'yên ở <b>за́-</b> suốt.</div>'
    '<div class="hd-warn"><b>Е́хать за́йцем</b> = đi tàu xe TRỐN VÉ. Hình ảnh là kẻ nhảy '
    'lên rồi ngồi im thin thít như con thỏ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>за́йчик</b> thỏ con · <b>за́йка</b> cưng, bé yêu (gọi âu yếm) · '
    '<b>за́ячий</b> thuộc về thỏ</div>'
)

# ------------------------------------------------------------------ змея
S["змея"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">зме-</span>'
    '<span class="hd-gloss">gốc, cùng nhà với <b>земля́</b> — đất</span></div>'
    '<div class="hd-row"><span class="hd-piece">-я</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Con vật BÒ SÁT MẶT ĐẤT. Người Slav cổ kiêng gọi thẳng tên nó nên '
    'gọi vòng theo chỗ nó sống, rồi cái tên vòng ấy ở lại luôn.</div>'
    '<div class="hd-warn">⚠️ Mức tin: <b>змея́</b> ↔ <b>земля́</b> là TỪ NGUYÊN (giả thuyết '
    'chuẩn của từ điển), không phải luật suy ra được — đừng lấy nó đoán từ khác.</div>'
    '<div class="hd-warn">Số ít trọng âm ở đuôi (<b>змея́</b>, <b>змеи́</b>), số nhiều lùi '
    'hết về gốc: <b>зме́и</b>, <b>зме́ям</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>змеи́ный</b> thuộc về rắn · <b>змеёныш</b> rắn con · '
    '<b>возду́шный змей</b> cái diều</div>'
)

# --------------------------------------------------------------- зоопарк
S["зоопарк"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">зоо-</span>'
    '<span class="hd-gloss">tiếng Hy Lạp <i>zoon</i> — ĐỘNG VẬT</span></div>'
    '<div class="hd-row"><span class="hd-piece">парк</span>'
    '<span class="hd-gloss">công viên (đã học)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ghép thẳng hai khối: công viên của động vật. <b>зоо-</b> là mảnh '
    'quốc tế, gặp lại nguyên si trong <i>zoo</i>, <i>zoology</i> — thấy <b>зоо-</b> mở đầu '
    'từ nào là biết từ đó nói về con vật.</div>'
    '<div class="hd-warn">Từ ghép chỉ giữ MỘT trọng âm, và nó rơi vào khối SAU: '
    '<b>зоопа́рк</b>, không phải «зо́опарк».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>зооло́гия</b> động vật học · <b>зоомагази́н</b> cửa hàng thú '
    'cưng · <b>парк</b> công viên</div>'
)

# ---------------------------------------------------------------- корова
S["корова"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">коров-</span>'
    '<span class="hd-gloss">gốc trơn: BÒ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không có gì để bóc thêm, cũng không có gì bất thường: trọng âm '
    'cắm chặt ở <b>-ро́-</b> qua mọi cách, mọi số. Nhánh phái sinh dựng bằng <b>-к-</b> và '
    '<b>-ник</b>: <b>коро́вка</b>, <b>коро́вник</b>.</div>'
    '<div class="hd-warn"><b>Бо́жья коро́вка</b> — «con bò nhỏ của Chúa» — là con BỌ RÙA. '
    'Đây là tên gọi chính thức của nó, không phải lối nói bóng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>коро́вий</b> thuộc về bò · <b>коро́вка</b> bò nhỏ · '
    '<b>коро́вник</b> chuồng bò</div>'
)

# ------------------------------------------------------------------ лиса
S["лиса"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">лис-</span>'
    '<span class="hd-gloss">gốc CÁO; đứng trần là <b>лис</b> — cáo ĐỰC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một gốc mọc ra ba dạng: <b>лис</b> con đực, <b>лиса́</b> từ thường '
    'ngày (và cũng là con cái), <b>лиси́ца</b> dạng đầy đủ thiên về sách vở và tên gọi '
    'động vật học.</div>'
    '<div class="hd-warn">Trọng âm nhảy khi sang số nhiều: số ít ở đuôi (<b>лиса́</b>, '
    '<b>лисы́</b>), số nhiều về gốc (<b>ли́сы</b>, <b>ли́сам</b>).</div>'
    '<div class="hd-warn"><b>Лиси́чка</b> vừa là «cáo con» vừa là tên một loại NẤM vàng '
    'cam — gọi theo đúng màu lông cáo.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лис</b> cáo đực · <b>лиси́ца</b> cáo (dạng đầy đủ) · '
    '<b>ли́сий</b> thuộc về cáo</div>'
)

# --------------------------------------------------------------- медведь
S["медведь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мед-</span>'
    '<span class="hd-gloss"><b>мёд</b> — mật ong (mất trọng âm thì ё thành е)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ведь</span>'
    '<span class="hd-gloss">gốc <b>ве́дать</b> — biết, hay biết</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Kẻ BIẾT chỗ có MẬT ONG». Người Slav cổ kiêng gọi thẳng tên con '
    'gấu nên đặt cho nó biệt danh này, rồi biệt danh chiếm luôn chỗ của tên thật.</div>'
    '<div class="hd-warn">Đuôi <b>-ь</b> thường báo giống CÁI, nhưng <b>медве́дь</b> là '
    'giống ĐỰC — cùng ca với <b>оле́нь</b> trong lô này. Chia theo mẫu đực mềm: '
    '<b>медве́дя</b>, <b>медве́дю</b>, <b>медве́дем</b>.</div>'
    '<div class="hd-warn"><b>Медве́жья услу́га</b> = «sự giúp đỡ kiểu gấu» — giúp mà hoá '
    'hại. Cụm rất thông dụng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мёд</b> mật ong · <b>медве́дица</b> gấu cái · '
    '<b>медвежо́нок</b> gấu con · <b>медве́жий</b> thuộc về gấu</div>'
)

# ----------------------------------------------------------------- олень
S["олень"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn <b>олен-</b>, không có mảnh nào để bóc.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <b>-ь</b> ở đây là giống ĐỰC (đúng ca <b>медве́дь</b>), chia '
    'mềm: <b>оле́ня</b>, <b>оле́ню</b>, <b>оле́нем</b>, số nhiều <b>оле́ни</b>. Trọng âm '
    'đứng yên ở <b>-ле́-</b>. Thịt của con vật dựng bằng hậu tố <b>-ина</b>: '
    '<b>оле́нина</b>.</div>'
    '<div class="hd-warn"><b>Се́верный оле́нь</b> — «hươu phương Bắc» — là con TUẦN LỘC. '
    'Đứng một mình thì <b>оле́нь</b> là hươu, nai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оле́ний</b> thuộc về hươu · <b>оле́нина</b> thịt hươu · '
    '<b>оленёнок</b> hươu con</div>'
)

# ----------------------------------------------------------------- птица
S["птица"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пт-</span>'
    '<span class="hd-gloss">gốc CHIM (lộ rõ ở <b>птене́ц</b> — chim non)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ица</span>'
    '<span class="hd-gloss">hậu tố danh từ, kéo theo giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>пт-</b> quá ngắn để đứng một mình nên luôn phải có hậu tố '
    'đỡ: <b>-ица</b> ra con chim, <b>-енец</b> ra chim non. Thêm hậu tố mềm thì <b>ц</b> '
    'hoá <b>ч</b>: <b>пти́ца → пти́чка, пти́чий</b>.</div>'
    '<div class="hd-warn">Đừng lẫn <b>пти́ца</b> (chim, nói chung) với <b>ку́рица</b> (con '
    'gà) — cùng đuôi <b>-ица</b>, cùng giống cái, nhìn rất giống nhau.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>птене́ц</b> chim non · <b>пти́чка</b> chim nhỏ · '
    '<b>пти́чий</b> thuộc về chim</div>'
)

# ---------------------------------------------------------------- свинья
S["свинья"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">свин-</span>'
    '<span class="hd-gloss">gốc LỢN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ья</span>'
    '<span class="hd-gloss">đuôi giống cái, thân mềm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>свин-</b> cùng một từ Ấn–Âu cổ với <i>swine</i> tiếng Anh '
    '— đọc lên là nhận ra. Thịt của con vật dựng bằng hậu tố <b>-ина</b>: <b>свини́на</b>, '
    'cùng khuôn <b>говя́дина</b>, <b>бара́нина</b>.</div>'
    '<div class="hd-warn">Ba tầng trọng âm: số ít ở đuôi (<b>свинья́</b>, <b>свиньи́</b>), '
    'số nhiều lùi về gốc (<b>сви́ньи</b>, <b>сви́ньям</b>), riêng cách 2 số nhiều vừa mất '
    'dấu mềm vừa kéo trọng âm ra đuôi: <b>свине́й</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>свини́на</b> thịt lợn · <b>свино́й</b> thuộc về lợn · '
    '<b>свина́рник</b> chuồng lợn</div>'
)

# ------------------------------------------------------------------ тигр
S["тигр"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn quốc tế, không chẻ được: vào tiếng Nga qua tiếng Hy Lạp '
    '<i>tigris</i>, y hệt <i>tiger</i> tiếng Anh — chỉ cần nhớ mặt chữ Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là chỗ gọn nhất để nhớ bộ ba tên con vật: đực trần <b>тигр</b> '
    '→ cái thêm <b>-ица</b> (<b>тигри́ца</b>) → con thêm <b>-ёнок</b> (<b>тигрёнок</b>). '
    'Cùng khuôn: <b>волк</b> · <b>волчи́ца</b> · <b>волчо́нок</b>, và <b>медве́дь</b> · '
    '<b>медве́дица</b> · <b>медвежо́нок</b>.</div>'
    '<div class="hd-warn">Hậu tố <b>-ёнок</b> luôn tự hút trọng âm, và ở số nhiều đổi hẳn '
    'sang <b>-я́та</b>: <b>тигрёнок → тигря́та</b>, <b>медвежо́нок → медвежа́та</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тигри́ца</b> hổ cái · <b>тигрёнок</b> hổ con · '
    '<b>тигри́ный</b> thuộc về hổ</div>'
)

# ------------------------------------------------------------------ утка
S["утка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ут-</span>'
    '<span class="hd-gloss">gốc VỊT (lộ ra ở <b>утёнок</b>, <b>ути́ный</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">hậu tố dựng danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>ут-</b> ngắn nên luôn cần hậu tố đỡ, y như <b>пт-</b> của '
    '<b>пти́ца</b>. Trọng âm cắm chặt ở <b>у́-</b>, không nhúc nhích ở cách nào.</div>'
    '<div class="hd-warn">Cách 2 số nhiều chèn thêm <b>-о-</b> cho khỏi dính <b>тк</b>: '
    '<b>у́тка → у́ток</b>.</div>'
    '<div class="hd-warn"><b>Газе́тная у́тка</b> = TIN VỊT, tin bịa đặt — tiếng Việt dùng '
    'đúng con vật ấy, khỏi phải nhớ gì thêm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>утёнок</b> vịt con · <b>у́точка</b> vịt nhỏ · '
    '<b>ути́ный</b> thuộc về vịt</div>'
)

# ------------------------------------------------------------------ гриб
S["гриб"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn <b>гриб-</b>, không có mảnh nào để bóc.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cả họ mọc ra từ gốc trần này: <b>-ник</b> dựng tên NGƯỜI làm việc '
    'đó — <b>грибни́к</b> là người đi hái nấm (cùng khuôn <b>дво́рник</b>); <b>-ной</b> '
    'dựng tính từ — <b>грибно́й суп</b> là súp nấm.</div>'
    '<div class="hd-warn">Trọng âm nhảy ngay TRONG số ít: cách 1 là <b>гриб</b>, nhưng từ '
    'cách 2 trở đi ra đuôi hết — <b>гриба́</b>, <b>грибу́</b>, <b>грибо́м</b>, số nhiều '
    '<b>грибы́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>грибни́к</b> người đi hái nấm · <b>грибно́й</b> thuộc về nấm · '
    '<b>грибо́к</b> nấm nhỏ, nấm mốc</div>'
)

# ---------------------------------------------------------------- дворец
S["дворец"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">двор-</span>'
    '<span class="hd-gloss"><b>двор</b> — cái sân; và cả TRIỀU ĐÌNH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ец</span>'
    '<span class="hd-gloss">hậu tố; <b>е</b> rơi mất khi biến cách</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Sân chầu của vua gọi là <b>двор</b>; chỗ ở của cái <b>двор</b> ấy '
    'chính là cung điện. Chú ý <b>-ец</b> ở đây KHÔNG chỉ người như trong '
    '<b>иностра́нец</b> — cùng một hậu tố, hai việc khác nhau.</div>'
    '<div class="hd-warn">Nguyên âm chạy và trọng âm dời, cả hai xảy ra ngay từ cách 2: '
    '<b>дворе́ц → дворца́, дворцу́, дворцо́м</b>, số nhiều <b>дворцы́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>двор</b> sân · <b>дво́рник</b> người quét sân (và cần gạt nước '
    'ô tô) · <b>дворяни́н</b> quý tộc</div>'
)

# --------------------------------------------------------------- коробка
S["коробка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">короб-</span>'
    '<span class="hd-gloss"><b>ко́роб</b> — thùng, giỏ đan (từ cũ)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">hậu tố NHỎ, kéo theo giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái <b>ко́роб</b> to thu nhỏ lại thành <b>коро́бка</b> — và để ý '
    'trọng âm DỜI một bước khi thêm <b>-ка</b>: <b>ко́роб</b> nhấn đầu, <b>коро́бка</b> '
    'nhấn giữa.</div>'
    '<div class="hd-warn">Cách 2 số nhiều chèn <b>-о-</b> cho khỏi dính <b>бк</b>: '
    '<b>коро́бка → коро́бок</b>.</div>'
    '<div class="hd-warn"><b>Коро́бка переда́ч</b> = hộp số ô tô; nghĩa «khung» cũng có: '
    '<b>дверна́я коро́бка</b> là khung cửa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ко́роб</b> thùng đan · <b>коро́бочка</b> hộp nhỏ xíu</div>'
)

# ----------------------------------------------------------------- миска
# Không có mục Họ hàng, và đó là CHỦ Ý: gốc `мис-` đã chết trong tiếng Nga hiện
# đại, ngoài dạng nhỏ của chính nó (`ми́сочка`) thì không mọc ra từ nào khác.
S["миска"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мис-</span>'
    '<span class="hd-gloss">gốc; nay KHÔNG còn đứng một mình được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">hậu tố NHỎ, kéo theo giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ mượn đã đứng lại một mình: gốc <b>мис-</b> chết rồi, không mọc '
    'ra từ nào khác, nên coi cả <b>ми́ска</b> là một khối — chỉ cần nhớ <b>-ка</b> báo '
    'giống cái, và trọng âm đứng yên ở <b>ми́-</b>.</div>'
    '<div class="hd-warn">Ba thứ đựng dễ lẫn: <b>ми́ска</b> tô, bát SÂU (canh, salad, thức '
    'ăn cho chó) · <b>таре́лка</b> đĩa phẳng · <b>ча́шка</b> tách có quai để uống.</div>'
    '<div class="hd-warn">Cách 2 số nhiều chèn <b>-о-</b>: <b>ми́ска → ми́сок</b>.</div>'
)

# ---------------------------------------------------------------- туалет
S["туалет"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">туал-</span>'
    '<span class="hd-gloss">tiếng Pháp <i>toile</i> — tấm vải</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ет</span>'
    '<span class="hd-gloss">tiếng Pháp <i>-ette</i>, hậu tố NHỎ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Tấm vải nhỏ» phủ bàn trang điểm → việc trang điểm, y phục → căn '
    'phòng làm việc đó → nhà vệ sinh. Đó là lý do từ điển vẫn còn ghi cả nghĩa «y phục» '
    'cho <b>туале́т</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: đây là đường đi TỪ NGUYÊN bên tiếng Pháp, không phải '
    'luật chẻ từ Nga — <b>туал-</b> không dùng lại được ở từ nào khác.</div>'
    '<div class="hd-warn">Nhà người Nga tách <b>туале́т</b> (phòng có bồn cầu) khỏi '
    '<b>ва́нная</b> (phòng tắm) — đó là hai phòng, không phải một.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>туале́тный</b> thuộc nhà vệ sinh · <b>туале́тная бума́га</b> '
    'giấy vệ sinh</div>'
)

# ------------------------------------------------------------------ флаг
S["флаг"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn, không chẻ được: tiếng Hà Lan <i>vlag</i>, vào tiếng Nga '
    'theo đường hàng hải — nhìn mặt chữ là ra <i>flag</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bản thân <b>флаг</b> không có gì phải nhớ, nhưng dạng nhỏ của nó '
    'gói đúng hai luật đã học: hậu tố <b>-ок</b> đổi <b>г → ж</b> và tự hút trọng âm về '
    'mình — <b>флаг → флажо́к</b>.</div>'
    '<div class="hd-warn">Trọng âm của dạng nhỏ còn chạy tiếp khi biến cách: '
    '<b>флажо́к → флажка́, флажку́</b>, trong khi <b>флаг</b> gốc thì đứng yên '
    '(<b>фла́га</b>, <b>фла́гу</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>флажо́к</b> cờ nhỏ · <b>фла́гман</b> kỳ hạm, đơn vị đầu bảng</div>'
)

# ------------------------------------------------------------------ очки
S["очки"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">оч-</span>'
    '<span class="hd-gloss">gốc <b>о́ко</b> — con mắt (cổ), <b>к</b> hoá <b>ч</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ки</span>'
    '<span class="hd-gloss">hậu tố nhỏ; ở đây LUÔN số nhiều</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đôi mắt nhỏ» đeo lên mặt. Gốc <b>о́ко</b> đã nhường chỗ cho '
    '<b>глаз</b> trong lời nói hằng ngày, nhưng vẫn sống trong <b>очки́</b> và '
    '<b>очеви́дец</b> («người thấy tận mắt» = nhân chứng).</div>'
    '<div class="hd-warn"><b>Очки́</b> KHÔNG có số ít, luôn chia số nhiều như '
    '<b>но́жницы</b>, <b>брю́ки</b>: một cái là <b>одни́ очки́</b>.</div>'
    '<div class="hd-warn">Cẩn thận cùng mặt chữ: <b>очко́</b> (giống trung) là ĐIỂM SỐ, mà '
    'số nhiều của nó cũng viết <b>очки́</b> — «ghi điểm» hay «cái kính» phải đoán theo câu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>о́ко</b> mắt (văn chương) · <b>очеви́дец</b> nhân chứng · '
    '<b>очка́рик</b> người đeo kính (lóng)</div>'
)

# --------------------------------------------------------------------- V
V = {
    # gloss tiếng Anh ghi "bathroom / restroom" — đó là tiếng Anh-Mỹ chỉ phòng có
    # bồn cầu, KHÔNG phải phòng tắm. Nhà người Nga tách hẳn туалет với ванная, nên
    # "phòng tắm" đang dạy sai nghĩa ngay trên đề bài mà user phải gõ từ Nga ra.
    "туалет": "nhà vệ sinh, phòng vệ sinh",
    # "cái bát" đụng чашка "cái tách, chén": với người Việt bát = chén, mà hai
    # thẻ cùng [n/FEM ♀] nên badge không tách. Máy không bắt được vì khác mặt
    # chữ. Bỏ "cái bát" — tô/chậu vẫn tả đúng миска, chén nhường cho чашка.
    "миска": "cái tô, cái chậu nhỏ",
}
