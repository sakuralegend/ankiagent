# -*- coding: utf-8 -*-
"""k195 — actions: 9 cặp thể + повести́ + реализова́ть.

Chỗ cần nhất quán trong lô:
(1) повести́ ↔ вести́ (k113): «вес- (вед-) DẪN — gốc thật là вед-, д hoá с trước -ти».
(2) сложи́ть/скла́дывать, отложи́ть/откла́дывать: HT gốc -лож- (khuôn k95/k155), CHT gốc
    -клад- (= класть) — hai gốc khác nhau y như cặp положи́ть/класть.
(3) наказа́ть, отказа́ть (+ CHT): -каз- «NÓI, chỉ ra — gốc của сказа́ть, показа́ть», з → ж
    (khuôn k117, k167 наказа́ние).
(4) напа́сть/напада́ть: -пад- RƠI (k131 па́дать), д hoá с trước -ть y như вести́.
(5) рвать/порва́ть: рв-/рыв- (khuôn k187 взорва́ть). увели́чивать/увели́чить: khuôn k149.
Họ hàng cố ý vắng: không có (mọi từ trong lô đều có họ thật).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "увеличивать": "tăng, tăng lên, nâng lên, phóng to",          # thiếu enlarge/magnify/zoom
    "увеличить": "tăng, tăng lên, nâng lên, phóng to",            # như trên
    "рвать": "xé, làm rách, làm đứt, nhổ, hái",                   # thiếu pull out / pick
    "порвать": "xé, làm rách, xé vụn, cắt đứt",                   # thiếu break off / sever
    "складывать": "xếp, xếp vào, cất vào, gói lại, gấp, cộng",    # thiếu fold / add up
    "сложить": "xếp, xếp chồng, đặt vào, gấp, cộng",              # thiếu fold / add
    "откладывать": "hoãn, trì hoãn, để sau, để dành",             # thiếu save (money)
    "отложить": "hoãn, dời lại, để sau, để dành",                 # thiếu save / set aside (money)
    "отказать": "từ chối, không cho, khước từ, ngừng hoạt động",  # thiếu fail / give out
    "отказывать": "từ chối, không cho, khước từ, ngừng hoạt động",  # như trên
}

# --------------------------------------------------------------------- повести
S["повести"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">KHỞI SỰ — với động từ chuyển động một chiều, như <b>пойти́</b>, <b>пое́хать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-вес- (вед-)</span>'
    '<span class="hd-gloss">DẪN — gốc thật là <i>вед-</i>, <i>д</i> hoá <i>с</i> trước <i>-ти</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thể HT của <b>вести́</b>: dẫn ai LÊN ĐƯỜNG — <b>Я поведу́ дете́й в парк.</b> '
    'Gốc <i>вед-</i> lộ ở tương lai: <b>поведу́, поведёшь</b>; quá khứ rơi <i>д</i>, giống cái '
    'nhấn đuôi: <b>повёл, повела́</b>.</div>'
    '<div class="hd-warn"><b>повести́ себя́</b> = cư xử (trong một tình huống): '
    '<b>Он повёл себя́ стра́нно.</b> Anh ta cư xử lạ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вести́</b> dẫn · <b>води́ть</b> dẫn (nhiều chiều) · '
    '<b>поведе́ние</b> hành vi, cách cư xử · <b>привести́</b> dẫn tới</div>'
)

# --------------------------------------------------------------------- преодолевать
S["преодолевать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пре-</span>'
    '<span class="hd-gloss">VƯỢT QUA giới hạn — như <b>преступле́ние</b> «bước qua» luật</span></div>'
    '<div class="hd-row"><span class="hd-piece">-одол-</span>'
    '<span class="hd-gloss">chính là <b>одоле́ть</b> đánh bại, khuất phục; gốc sâu hơn đã mờ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ева́-ть</span>'
    '<span class="hd-gloss">thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Khuất phục được, vượt qua hẳn» ⇒ khắc phục. Nhận thẳng cách 4: '
    '<b>преодолева́ть тру́дности</b> đang vượt qua khó khăn. Giữ nguyên <i>-ва-</i> khi chia: '
    '<b>преодолева́ю, преодолева́ешь</b>. Cặp HT: <b>преодоле́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>преодоле́ть</b> (HT) · <b>преодоле́ние</b> sự khắc phục · '
    '<b>непреодоли́мый</b> không thể vượt qua</div>'
)

# --------------------------------------------------------------------- преодолеть
S["преодолеть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пре-</span>'
    '<span class="hd-gloss">VƯỢT QUA giới hạn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-одоле́-ть</span>'
    '<span class="hd-gloss">chính là <b>одоле́ть</b> đánh bại, khuất phục</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vượt qua HẲN một trở ngại, có kết quả. Chia như <b>уме́ть</b>: '
    '<b>преодоле́ю, преодоле́ешь</b>. Dùng cả cho trở ngại tinh thần lẫn quãng đường: '
    '<b>преодоле́ть страх</b> vượt qua nỗi sợ, <b>преодоле́ть сто киломе́тров</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>преодолева́ть</b> (CHT) · <b>преодоле́ние</b> sự khắc phục · '
    '<b>непреодоли́мый</b> không thể vượt qua</div>'
)

# --------------------------------------------------------------------- увеличивать
S["увеличивать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">làm cho TRỞ NÊN…</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вели́ч-</span>'
    '<span class="hd-gloss">LỚN — <b>вели́кий</b>, <i>к → ч</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть</span>'
    '<span class="hd-gloss">thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Làm cho lớn hơn» ⇒ tăng, phóng to (cả ảnh, chữ trên màn hình). '
    'Chia đều <b>увели́чиваю</b>, trọng âm đứng yên ở <i>ли́</i>. Cặp HT: <b>увели́чить</b>.</div>'
    '<div class="hd-warn">Không <b>-ся</b> thì phải CÓ người làm tăng cái gì (cách 4): '
    '<b>увели́чивать зарпла́ту</b>. Cái gì tự tăng là <b>увели́чиваться</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>увели́чиваться</b> tự tăng lên · <b>увеличе́ние</b> sự gia tăng, độ phóng đại · '
    '<b>вели́кий</b> vĩ đại</div>'
)

# --------------------------------------------------------------------- увеличить
S["увеличить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-вели́ч-</span>'
    '<span class="hd-gloss">làm cho LỚN — <b>вели́кий</b>, <i>к → ч</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai: <b>увели́чу, увели́чишь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng khuôn <i>у- + gốc tính từ + -ить</i> với <b>улу́чшить</b> «làm cho tốt '
    'hơn». Tăng xong, có kết quả: <b>увели́чить фо́то</b> phóng to ảnh.</div>'
    '<div class="hd-warn"><b>увели́чить це́ны</b> = (ai đó) tăng giá · <b>це́ны увели́чились</b> = '
    'giá tự tăng. Chủ ngữ là cái tăng thì phải thêm <b>-ся</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>увели́читься</b> tự tăng lên · <b>увели́чивать</b> (CHT) · '
    '<b>увеличе́ние</b> sự gia tăng · <b>вели́кий</b> vĩ đại</div>'
)

# --------------------------------------------------------------------- жертвовать
S["жертвовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">же́ртв-</span>'
    '<span class="hd-gloss">VẬT DÂNG CÚNG — chính là <b>же́ртва</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ть</span>'
    '<span class="hd-gloss">đuôi động từ; khi chia <i>-ова-</i> → <i>-у-</i>: <b>же́ртвую</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Dâng đi một vật» ⇒ quyên góp, hiến tặng; dâng đi thứ quý của mình ⇒ '
    'hy sinh. Cặp HT: <b>поже́ртвовать</b>.</div>'
    '<div class="hd-warn">Hai nghĩa tách bằng CÁCH: hiến TẶNG cái gì — cách 4 '
    '(<b>же́ртвовать де́ньги на шко́лу</b>); HY SINH cái gì — cách 5 '
    '(<b>же́ртвовать вре́менем</b> hy sinh thời gian).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>же́ртва</b> nạn nhân, vật hiến tế · <b>поже́ртвование</b> khoản quyên góp</div>'
)

# --------------------------------------------------------------------- пожертвовать
S["пожертвовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể, KHÔNG mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-же́ртв-ова-ть</span>'
    '<span class="hd-gloss">chính là <b>же́ртвовать</b> — gốc <b>же́ртва</b> vật dâng cúng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Quyên góp, hiến tặng — một lần, có kết quả. Chia <i>-ова-</i> → <i>-у-</i>: '
    '<b>поже́ртвую, поже́ртвуешь</b>.</div>'
    '<div class="hd-warn">Cách 5 là HY SINH: <b>поже́ртвовать жи́знью</b> hy sinh tính mạng. '
    'Cách 4 là tặng: <b>поже́ртвовать де́ньги</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поже́ртвование</b> khoản quyên góp · <b>же́ртва</b> nạn nhân, vật hiến tế · '
    '<b>же́ртвовать</b> (CHT)</div>'
)

# --------------------------------------------------------------------- реализовать
S["реализовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">реал-</span>'
    '<span class="hd-gloss">mượn Latin, như <i>real</i> — gốc của <b>реа́льный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-изова́-ть</span>'
    '<span class="hd-gloss">≈ Anh <i>-ize</i>; khi chia <i>-ова-</i> → <i>-у-</i>: <b>реализу́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Làm cho thành thật» ⇒ thực hiện: <b>реализова́ть план, прое́кт</b>. Trong '
    'kinh doanh còn là bán ra hàng. Một dạng dùng cho CẢ HAI thể — thể nào là do ngữ cảnh.</div>'
    '<div class="hd-warn">Bẫy tiếng Anh: <i>realize</i> = «nhận ra» thì tiếng Nga là '
    '<b>поня́ть</b>, <b>осозна́ть</b> — <b>реализова́ть</b> KHÔNG có nghĩa đó.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>реа́льный</b> thật, khả thi · <b>реализа́ция</b> sự thực hiện · '
    '<b>реа́льность</b> hiện thực</div>'
)

# --------------------------------------------------------------------- рвать
S["рвать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рв-</span>'
    '<span class="hd-gloss">XÉ, GIẬT — thân dài là <i>рыв-</i> (<b>взрыв</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi động từ; <i>а</i> rơi khi chia: <b>рву, рвёшь</b> — như <b>ждать → жду</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mọi kiểu GIẬT đứt: xé giấy, nhổ răng (<b>рвать зу́бы</b>), hái hoa '
    '(<b>рвать цветы́</b>). Quá khứ giống cái nhấn đuôi: <b>рвала́</b>, còn lại <b>рвал, рва́ли</b>. '
    'Cặp HT: <b>порва́ть</b>.</div>'
    '<div class="hd-warn">Câu không chủ ngữ: <b>Его́ рвёт.</b> = Anh ta đang nôn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>взорва́ть</b> làm nổ · <b>взрыв</b> vụ nổ · <b>разорва́ть</b> xé toạc · '
    '<b>переры́в</b> giờ nghỉ</div>'
)

# --------------------------------------------------------------------- порвать
S["порвать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể, KHÔNG mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-рв-а́ть</span>'
    '<span class="hd-gloss">XÉ, GIẬT — chính là <b>рвать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Xé xong, làm rách hẳn: <b>порва́ть брю́ки</b> làm rách quần. Chia như '
    '<b>рвать</b>: <b>порву́, порвёшь</b>; quá khứ giống cái nhấn đuôi: <b>порвала́</b>.</div>'
    '<div class="hd-warn"><b>порва́ть с</b> + cách 5 = cắt đứt quan hệ: <b>Она́ порвала́ с ним.</b> '
    'Cô ấy chia tay anh ta.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рвать</b> (CHT) · <b>разорва́ть</b> xé toạc · <b>взорва́ть</b> làm nổ · '
    '<b>переры́в</b> giờ nghỉ</div>'
)

# --------------------------------------------------------------------- складывать
S["складывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">LẠI VỚI NHAU</span></div>'
    '<div class="hd-row"><span class="hd-piece">-клад-</span>'
    '<span class="hd-gloss">ĐẶT — gốc của <b>класть</b> (<i>д</i> hoá <i>с</i> trước <i>-ть</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть</span>'
    '<span class="hd-gloss">thể chưa hoàn thành, chia đều: <b>скла́дываю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đặt lại với nhau» ⇒ xếp, gấp, cộng số. Cặp HT <b>сложи́ть</b> dùng gốc '
    'KHÁC (<i>-лож-</i>) — y như cặp <b>класть / положи́ть</b>.</div>'
    '<div class="hd-warn"><b>скла́дывать ору́жие</b> = hạ vũ khí, đầu hàng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>класть</b> đặt · <b>склад</b> nhà kho (chỗ xếp đồ) · '
    '<b>откла́дывать</b> hoãn, để dành · <b>сложи́ть</b> (HT)</div>'
)

# --------------------------------------------------------------------- сложить
S["сложить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">LẠI VỚI NHAU</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лож-</span>'
    '<span class="hd-gloss">gốc NẰM — làm cho NẰM ⇒ đặt, họ với <b>лежа́ть</b>, <b>лечь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đặt nằm lại với nhau» ⇒ xếp chồng, gấp lại, cộng. Trọng âm lùi y như '
    '<b>положи́ть</b>: <b>сложу́, сло́жишь</b>. Cặp CHT <b>скла́дывать</b> mang gốc khác '
    '(<i>-клад-</i>).</div>'
    '<div class="hd-warn">Phép cộng: <b>Сложи́те два и три.</b> Cộng hai với ba.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сло́жный</b> phức tạp · <b>сложе́ние</b> phép cộng · '
    '<b>положи́ть</b> đặt · <b>отложи́ть</b> hoãn</div>'
)

# --------------------------------------------------------------------- откладывать
S["откладывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">RỜI XA, khỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-клад-</span>'
    '<span class="hd-gloss">ĐẶT — gốc của <b>класть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть</span>'
    '<span class="hd-gloss">thể chưa hoàn thành, chia đều: <b>откла́дываю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đặt ra xa» — xa trong thời gian ⇒ hoãn; ra một bên ⇒ để dành '
    '(<b>откла́дывать де́ньги</b>). Cặp HT <b>отложи́ть</b> dùng gốc <i>-лож-</i>, như '
    '<b>класть / положи́ть</b>.</div>'
    '<div class="hd-warn">Tục ngữ: <b>Не откла́дывай на за́втра то, что мо́жно сде́лать сего́дня.</b> '
    'Việc hôm nay chớ để ngày mai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отложи́ть</b> (HT) · <b>класть</b> đặt · <b>скла́дывать</b> xếp, gấp</div>'
)

# --------------------------------------------------------------------- отложить
S["отложить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">RỜI XA, khỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лож-</span>'
    '<span class="hd-gloss">gốc NẰM — làm cho NẰM ⇒ đặt, họ với <b>лежа́ть</b>, <b>лечь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đặt ra xa» ⇒ hoãn, để dành. Trọng âm lùi như <b>положи́ть</b>: '
    '<b>отложу́, отло́жишь</b>.</div>'
    '<div class="hd-warn">Hoãn SANG lúc nào: <b>на</b> + cách 4 (<b>отложи́ть на за́втра</b>); '
    'hoãn ĐẾN mốc nào: <b>до</b> + cách 2 (<b>до понеде́льника</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>откла́дывать</b> (CHT) · <b>положи́ть</b> đặt · <b>сложи́ть</b> xếp, cộng · '
    '<b>положе́ние</b> vị trí, tình hình</div>'
)

# --------------------------------------------------------------------- наказать
S["наказать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">tiền tố, ở đây KHÔNG tách ra nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-каз-</span>'
    '<span class="hd-gloss">NÓI, chỉ ra — gốc của <b>сказа́ть</b>, <b>показа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa cổ là «dặn bảo, răn dạy»; răn kẻ có lỗi ⇒ phạt. Chia y như '
    '<b>сказа́ть</b>: <i>з → ж</i> ở mọi ngôi, ngôi 1 nhấn đuôi, còn lại nhấn gốc — '
    '<b>накажу́, нака́жешь</b>.</div>'
    '<div class="hd-warn">Phạt AI (cách 4) VÌ cái gì (<b>за</b> + cách 4): '
    '<b>наказа́ть сы́на за ложь</b> phạt con trai vì nói dối.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>наказа́ние</b> hình phạt · <b>нака́зывать</b> (CHT) · '
    '<b>сказа́ть</b> nói ra · <b>прика́з</b> mệnh lệnh</div>'
)

# --------------------------------------------------------------------- наказывать
S["наказывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">tiền tố, ở đây KHÔNG tách ra nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-каз-</span>'
    '<span class="hd-gloss">NÓI, chỉ ra — gốc của <b>сказа́ть</b>, <b>показа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть</span>'
    '<span class="hd-gloss">thể chưa hoàn thành, chia đều: <b>нака́зываю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Phạt — nhiều lần, thói quen, hoặc đang diễn ra: <b>Роди́тели ча́сто '
    'нака́зывали его́.</b> Trọng âm đứng yên ở <i>ка́</i> trong mọi dạng. Cùng cách đòi: '
    'AI (cách 4) + <b>за</b> cái gì.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>наказа́ть</b> (HT) · <b>наказа́ние</b> hình phạt · '
    '<b>показа́ть</b> cho xem · <b>прика́з</b> mệnh lệnh</div>'
)

# --------------------------------------------------------------------- отказать
S["отказать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">RỜI XA, khỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-каз-</span>'
    '<span class="hd-gloss">NÓI, chỉ ra — gốc của <b>сказа́ть</b>, <b>показа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Nói để đẩy ai XA» ⇒ không cho. Chia như <b>сказа́ть</b>: '
    '<b>откажу́, отка́жешь</b>. Máy móc, cơ thể <b>отказа́ли</b> = ngừng chạy: '
    '<b>Отказа́ли тормоза́.</b> Phanh hỏng.</div>'
    '<div class="hd-warn">Không cho AI (cách 3) cái gì (<b>в</b> + cách 6): <b>Ему́ отказа́ли в '
    'ви́зе.</b> Tự mình từ chối thứ được mời là <b>отказа́ться от</b> + cách 2.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отка́з</b> sự từ chối · <b>отказа́ться</b> từ bỏ · '
    '<b>отка́зывать</b> (CHT) · <b>сказа́ть</b> nói</div>'
)

# --------------------------------------------------------------------- отказывать
S["отказывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">RỜI XA, khỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-каз-</span>'
    '<span class="hd-gloss">NÓI, chỉ ra — gốc của <b>сказа́ть</b>, <b>показа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть</span>'
    '<span class="hd-gloss">thể chưa hoàn thành, chia đều: <b>отка́зываю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không cho — lặp lại hay đang diễn ra. Cách đòi y như <b>отказа́ть</b>: '
    'AI (cách 3) + <b>в</b> cái gì (cách 6). Từ bỏ thứ được mời thì có <b>-ся</b>: '
    '<b>отка́зываться от</b> + cách 2.</div>'
    '<div class="hd-warn"><b>ни в чём себе́ не отка́зывать</b> = chẳng tiếc gì cho bản thân, '
    'muốn gì có nấy.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отказа́ть</b> (HT) · <b>отка́з</b> sự từ chối · '
    '<b>отка́зываться</b> từ bỏ · <b>заказа́ть</b> đặt (món, hàng)</div>'
)

# --------------------------------------------------------------------- нападать
S["нападать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">LÊN, VÀO trên bề mặt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пад-</span>'
    '<span class="hd-gloss">RƠI, NGÃ — gốc của <b>па́дать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">thể chưa hoàn thành, chia đều: <b>напада́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Rơi chụp LÊN ai» ⇒ tấn công. Trọng âm ra đuôi: <b>напада́ю</b> — khác '
    '<b>па́даю</b>. Cặp HT: <b>напа́сть</b>.</div>'
    '<div class="hd-warn">Tấn công AI: <b>на</b> + cách 4 — <b>Соба́ка напада́ет на люде́й.</b> '
    'Con chó hay tấn công người.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нападе́ние</b> cuộc tấn công · <b>напада́ющий</b> tiền đạo (bóng đá) · '
    '<b>па́дать</b> rơi · <b>упа́сть</b> ngã</div>'
)

# --------------------------------------------------------------------- напасть
S["напасть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">LÊN, VÀO trên bề mặt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пас- (пад-)</span>'
    '<span class="hd-gloss">RƠI — gốc thật là <i>пад-</i>, <i>д</i> hoá <i>с</i> trước <i>-ть</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Rơi chụp LÊN ai» một lần ⇒ tấn công. Chia y như <b>упа́сть</b>: '
    '<i>д</i> hiện lại ở tương lai — <b>нападу́, нападёшь</b>; quá khứ rơi <i>д</i> — '
    '<b>напа́л, напа́ла</b>.</div>'
    '<div class="hd-warn"><b>напа́сть на</b> + cách 4 còn là tình cờ bắt gặp: <b>напа́сть на след</b> '
    'lần ra dấu vết.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>напада́ть</b> (CHT) · <b>нападе́ние</b> cuộc tấn công · '
    '<b>упа́сть</b> ngã · <b>попа́сть</b> trúng, lọt vào</div>'
)

B = {
    "docbangmat": 120,
    "loitubat": 1,
    "nguonsai": 0,
    "baolen": [
        "V cần duyệt (10 thẻ, chỉ THÊM nghĩa gloss Anh xác nhận, không cắt nghĩa cũ): увели́чивать/увели́чить + «phóng to» (enlarge/magnify/zoom) · рвать + «nhổ, hái» (pull out / pick) · порва́ть + «cắt đứt» (break off / sever) · скла́дывать/сложи́ть + «gấp, cộng» (fold / add up; скла́дывать «xếp vào» → «xếp, xếp vào») · откла́дывать/отложи́ть + «để dành» (save money) · отказа́ть/отка́зывать + «ngừng hoạt động» (fail / give out). Không có ngoặc nào.",
        "Gloss của же́ртвовать/поже́ртвовать THIẾU nghĩa «hy sinh» (sacrifice, + cách 5 — поже́ртвовать жи́знью), một nghĩa chính của từ. Theo luật §2c tôi KHÔNG thêm vào V vì gloss không xác nhận; đã dạy ở ô đỏ cả hai thẻ. User muốn đề bài có «hy sinh» thì phải duyệt riêng.",
        "Chỗ KHÔNG chắc: (1) -одол- trong преодоле́ть — chỉ ghi «chính là одоле́ть, gốc sâu hơn đã mờ», không khẳng định từ nguyên. (2) пре- ghi «VƯỢT QUA giới hạn», dẫn преступле́ние — là khái quát nghĩa tiền tố, không phải luật tuyệt đối. (3) на- trong напада́ть/напа́сть ghi «LÊN, VÀO trên bề mặt» — hợp nghĩa nhưng là diễn giải.",
        "Tự sửa 1 lỗi nội dung: thẻ нака́зывать viết «trọng âm đứng yên ở ка́, khác HT наказа́ть» — sai một nửa vì HT cũng nhấn ка́ ở нака́жешь; sửa thành «đứng yên ở ка́ trong mọi dạng».",
        "Từ đồng tự напа́сть: soạn đúng theo chốt — động từ «tấn công», không nhắc danh từ «tai hoạ». Ô đỏ dạy thêm напа́сть на след (lần ra dấu vết), không đưa nghĩa này vào V.",
    ],
}
