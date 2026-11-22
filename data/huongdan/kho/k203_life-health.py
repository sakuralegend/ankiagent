# -*- coding: utf-8 -*-
"""k203 — life::health (lô trộn): đồ dùng, y tế, văn học, quần áo.

Chỗ cần nhất quán trong lô:
(1) переодева́ться / переоде́ться = пере- LẠI + одева́ться / оде́ться — khớp chẻ одева́ться [k102],
    оде́ться [k102] (thân tương lai mọc -н-, y như наде́ну).
(2) стихотворе́ние = стих [k11] + твор- [тво́рчество, k132] + -е́ние.
(3) по́весть gốc ВЕСТ- «tin, cho biết» — khớp изве́стный [k86]. KHÔNG ghép với вести́/повести́ (вед- «dẫn»).
(4) рука́в ← рука́ [k32]; но́жницы ← нож [k23]; СПИД ↔ иммуните́т (chữ И = иммунодефици́т).
Họ hàng cố ý vắng: або́рт (mượn đứng một mình), о́бморок (từ nguyên không chắc — nêu trong ô Mức tin).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "переодеваться": "thay quần áo, đổi đồ, cải trang",          # gloss: to disguise oneself — khớp переодеться
    "глухой": "bị điếc, nghễnh ngãng, trầm đục, hẻo lánh, vô thanh",  # gloss: voiceless / unvoiced
}

# --------------------------------------------------------------------- ножницы
S["ножницы"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">нож-</span>'
    '<span class="hd-gloss">DAO (<b>нож</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ниц-ы</span>'
    '<span class="hd-gloss">đuôi đồ vật, ở dạng số nhiều</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Kéo là hai lưỡi dao ghép lại ⇒ chỉ có số nhiều, như <b>брю́ки</b> (quần), '
    '<b>очки́</b> (kính). Cách 2: <b>но́жниц</b>.</div>'
    '<div class="hd-warn">MỘT cái kéo = <b>одни́ но́жницы</b>; hai cái = <b>дво́е но́жниц</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нож</b> dao · <b>но́жик</b> dao nhỏ</div>'
)

# --------------------------------------------------------------------- гвоздь
S["гвоздь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được. Đuôi <b>-ь</b> nhưng là giống đực.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hễ có đuôi là trọng âm xuống đuôi: <b>гвоздя́</b>, <b>гвоздём</b>, '
    '<b>гвозде́й</b> — riêng số nhiều cách 1 và 4 quay về gốc: <b>гво́зди</b>.</div>'
    '<div class="hd-warn"><b>гвоздь програ́ммы</b> = «cái đinh» của chương trình: tiết mục '
    'đắt giá nhất.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гвозди́ка</b> đinh hương (nụ khô trông như cái đinh nhỏ); hoa cẩm chướng</div>'
)

# --------------------------------------------------------------------- фонарь
S["фонарь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn tiếng Hy Lạp <i>phanárion</i> = cái đèn.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đèn có vỏ che, cầm tay hay treo cột: <b>у́личный фона́рь</b> đèn đường. '
    'Đuôi <b>-ь</b> giống đực; thêm đuôi là trọng âm xuống đuôi: <b>фонаря́</b>, <b>фонари́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>фона́рик</b> đèn pin (<b>-ик</b> = nhỏ)</div>'
)

# --------------------------------------------------------------------- простыня
S["простыня"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">прост-</span>'
    '<span class="hd-gloss">TRƠN, ĐƠN GIẢN (<b>просто́й</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ын-я</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Tấm vải trơn, không nhuộm» ⇒ ga trải giường. Số nhiều trọng âm chạy, '
    'phải thuộc: <b>про́стыни</b>, cách 2 <b>просты́нь</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: nối với <b>просто́й</b> là từ nguyên được nhiều sách chọn, '
    'không phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>просто́й</b> đơn giản, trơn (theo từ nguyên trên)</div>'
)

# --------------------------------------------------------------------- ожог
S["ожог"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">tác động lên bề mặt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-жог</span>'
    '<span class="hd-gloss">ĐỐT — gốc <i>жг-/жег-/жог-</i> của <b>жечь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỗ bị lửa đốt lên da ⇒ vết bỏng. Gốc lộ <i>г</i> ở <b>жгу</b> '
    '(tôi đốt); trong <b>жечь</b> thì <i>г</i> đã hoá <i>ч</i>.</div>'
    '<div class="hd-warn"><b>со́лнечный ожо́г</b> = cháy nắng · <b>получи́ть ожо́г</b> = bị bỏng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обже́чься</b> bị bỏng · <b>зажига́лка</b> bật lửa · '
    '<b>изжо́га</b> chứng ợ nóng · <b>поджо́г</b> vụ phóng hoả</div>'
)

# --------------------------------------------------------------------- спид
S["спид"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">СПИД</span>'
    '<span class="hd-gloss">viết tắt: <b>синдро́м приобретённого иммунодефици́та</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là AIDS dịch từng chữ, chỉ đảo thứ tự: hội chứng (С) · mắc phải (П) · '
    'suy giảm miễn dịch (И, Д). Viết hoa, đọc liền như một từ, giống đực.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>иммуните́т</b> miễn dịch · <b>ВИЧ</b> virus HIV '
    '(<b>ви́рус иммунодефици́та челове́ка</b>)</div>'
)

# --------------------------------------------------------------------- глухой
S["глухой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">глух-</span>'
    '<span class="hd-gloss">KHÔNG VANG, không lọt tiếng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ mang trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tai không lọt tiếng ⇒ điếc; âm không vang ⇒ trầm đục; nơi không tiếng '
    'người ⇒ hẻo lánh. Dạng ngắn kéo trọng âm về gốc, trừ giống cái: <b>глух</b>, <b>глуха́</b>, '
    '<b>глу́хо</b>, <b>глу́хи</b>.</div>'
    '<div class="hd-warn"><b>глухо́й согла́сный</b> = phụ âm vô thanh (<i>п, т, к, с</i>) — '
    'đối lại là <b>зво́нкий</b> hữu thanh.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>глушь</b> chốn hẻo lánh (<i>х → ш</i>) · <b>глуши́ть</b> làm tắt, '
    'làm át tiếng · <b>оглу́хнуть</b> bị điếc</div>'
)

# --------------------------------------------------------------------- обморок
S["обморок"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ ra được mảnh nào còn dùng nghĩa ngày nay — học như một khối.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cách nói thông dụng nhất cho «ngất» là «rơi vào cơn ngất».</div>'
    '<div class="hd-warn"><b>упа́сть в о́бморок</b> (hoàn thành) / <b>па́дать в о́бморок</b> = '
    'ngất xỉu — <b>в</b> + cách 4.</div>'
    '<div class="hd-warn">⚠️ Mức tin: sách từ nguyên thường giải là <b>об-</b> + <i>морок</i> '
    '«màn tối» (gần <b>мрак</b> bóng tối) — «bị bóng tối trùm lên». Là từ nguyên, không phải luật.</div>'
)

# --------------------------------------------------------------------- иммунитет
S["иммунитет"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">иммун-</span>'
    '<span class="hd-gloss">ĐƯỢC MIỄN (Latin <i>immunis</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ите́т</span>'
    '<span class="hd-gloss">= tiếng Anh <i>-ity</i>: <b>университе́т</b>, <b>авторите́т</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiếng Anh <i>immunity</i>, đổi <i>-ity</i> thành <b>-ите́т</b>. Cơ thể «được '
    'miễn» bệnh ⇒ miễn dịch; người «được miễn» xét xử ⇒ <b>дипломати́ческий иммуните́т</b> '
    'quyền miễn trừ ngoại giao.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>имму́нный</b> (thuộc) miễn dịch · <b>иммунодефици́т</b> suy giảm miễn '
    'dịch (chữ И trong <b>СПИД</b>)</div>'
)

# --------------------------------------------------------------------- аборт
S["аборт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn Latin <i>abortus</i> — tiếng Anh <i>abortion</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Phá thai là <b>сде́лать або́рт</b>. Trong y khoa, sẩy thai tự nhiên cũng gọi '
    '<b>або́рт</b>; ngoài đời người ta nói <b>вы́кидыш</b>.</div>'
)

# --------------------------------------------------------------------- стихотворение
S["стихотворение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">стих-о-</span>'
    '<span class="hd-gloss">DÒNG THƠ (<b>стих</b>) + nguyên âm nối</span></div>'
    '<div class="hd-row"><span class="hd-piece">-твор-</span>'
    '<span class="hd-gloss">TẠO RA (<b>тво́рчество</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ние</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thứ được tạo nên từ các dòng thơ» ⇒ một bài thơ trọn vẹn.</div>'
    '<div class="hd-warn"><b>стих</b> một dòng thơ · <b>стихи́</b> thơ nói chung · '
    '<b>стихотворе́ние</b> MỘT bài thơ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стих</b> dòng thơ · <b>стихотво́рный</b> (thuộc) thơ · '
    '<b>тво́рчество</b> sáng tác</div>'
)

# --------------------------------------------------------------------- колокол
S["колокол"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Số nhiều đuôi <b>-а́</b> có trọng âm, như <b>дом</b> → <b>дома́</b>: '
    '<b>колокола́</b>, <b>колоколо́в</b> — không phải <i>-ы</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>колоко́льчик</b> chuông nhỏ; hoa chuông · <b>колоко́льня</b> tháp chuông</div>'
)

# --------------------------------------------------------------------- аплодисменты
S["аплодисменты"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn tiếng Pháp <i>applaudissements</i> — cùng gốc tiếng Anh '
    '<i>applaud</i>, <i>applause</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỉ có số nhiều, vì tiếng vỗ tay là nhiều cái vỗ: '
    '<b>бу́рные аплодисме́нты</b> tràng vỗ tay như sấm.</div>'
    '<div class="hd-warn">Động từ <b>аплоди́ровать</b> + cách 3: <b>аплоди́ровать арти́сту</b> = '
    'vỗ tay cho nghệ sĩ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>аплоди́ровать</b> vỗ tay</div>'
)

# --------------------------------------------------------------------- повесть
S["повесть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вест-ь</span>'
    '<span class="hd-gloss">TIN, CHO BIẾT — như <b>изве́стный</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Điều được kể cho biết» ⇒ truyện. Thang độ dài: <b>расска́з</b> truyện ngắn '
    '&lt; <b>по́весть</b> truyện vừa &lt; <b>рома́н</b> tiểu thuyết. Số nhiều dịch như '
    '<b>но́вость</b>: <b>по́вести</b>, <b>повесте́й</b>.</div>'
    '<div class="hd-warn">Đừng lẫn <b>по́весть</b> (truyện) với <b>повести́</b> (dẫn đi, gốc '
    '<i>вед-</i> «dẫn») — khác gốc, khác trọng âm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>изве́стие</b> tin tức · <b>изве́стный</b> nổi tiếng · '
    '<b>пове́стка</b> giấy triệu tập · <b>повествова́ние</b> lối kể chuyện</div>'
)

# --------------------------------------------------------------------- цепочка
S["цепочка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">цеп-</span>'
    '<span class="hd-gloss">XÍCH (<b>цепь</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́чк-а</span>'
    '<span class="hd-gloss">hậu tố NHỎ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Sợi xích nhỏ» ⇒ dây chuyền đeo cổ; nghĩa bóng ⇒ một chuỗi, một dãy nối '
    'nhau. Nguyên âm chạy ở cách 2 số nhiều, như <b>ру́чка</b> → <b>ру́чек</b>: '
    '<b>цепо́чек</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>цепь</b> xích, chuỗi · <b>прицепи́ть</b> móc vào · '
    '<b>сцепле́ние</b> sự móc nối; bộ ly hợp (côn xe)</div>'
)

# --------------------------------------------------------------------- рукав
S["рукав"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рук-</span>'
    '<span class="hd-gloss">TAY (<b>рука́</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́в</span>'
    '<span class="hd-gloss">đuôi danh từ giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Phần áo bọc cánh tay ⇒ tay áo; dòng tách khỏi sông chính như cánh tay ⇒ nhánh '
    'sông. Trọng âm luôn ở đuôi: <b>рукава́</b>; số nhiều đuôi <b>-а́</b>, không phải <i>-ы</i>: '
    '<b>рукава́</b>, <b>рукаво́в</b>.</div>'
    '<div class="hd-warn"><b>засучи́ть рукава́</b> = xắn tay áo (hăng hái bắt tay vào việc) · '
    '<b>спустя́ рукава́</b> = làm qua loa, ẩu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рука́</b> tay · <b>ру́чка</b> cái bút; tay nắm · '
    '<b>рукави́ца</b> găng tay bao (không chia ngón)</div>'
)

# --------------------------------------------------------------------- халат
S["халат"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: từ mượn phương Đông, theo đường tiếng Turk vào tiếng Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Áo choàng dài, mặc rộng: áo choàng ở nhà, áo choàng tắm, và cả áo blouse '
    'của bác sĩ — <b>бе́лый хала́т</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>хала́тный</b> cẩu thả · <b>хала́тность</b> sự tắc trách '
    '(hình ảnh người mặc áo choàng ngủ cả ngày)</div>'
)

# --------------------------------------------------------------------- переодеваться
S["переодеваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span>'
    '<span class="hd-gloss">LẠI, ĐỔI (làm lại lần nữa)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-одева́ться</span>'
    '<span class="hd-gloss">mặc đồ cho chính mình (<b>одева́ться</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Mặc đồ lại lần nữa» ⇒ thay đồ; mặc đồ của vai khác ⇒ cải trang. Chia đều '
    'như <b>одева́ться</b>: <b>переодева́юсь</b>, <b>переодева́ешься</b>. Cặp hoàn thành: '
    '<b>переоде́ться</b>.</div>'
    '<div class="hd-warn">Thay SANG bộ nào thì dùng <b>в</b> + cách 4: '
    '<b>переодева́ться в спорти́вную фо́рму</b> = thay sang đồ thể thao.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>одева́ться</b> mặc đồ · <b>раздева́ться</b> cởi đồ · '
    '<b>оде́жда</b> quần áo</div>'
)

# --------------------------------------------------------------------- переодеться
S["переодеться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span>'
    '<span class="hd-gloss">LẠI, ĐỔI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-оде́ться</span>'
    '<span class="hd-gloss">mặc đồ xong (<b>оде́ться</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Là <b>переодева́ться</b> bỏ <b>-ва-</b> ⇒ hoàn thành: thay đồ xong. Thân '
    'tương lai mọc thêm <b>-н-</b>, y như <b>оде́нусь</b>: <b>переоде́нусь</b>, '
    '<b>переоде́нешься</b>, <b>переоде́нутся</b>. Mệnh lệnh: <b>Переоде́нься!</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>переодева́ться</b> (chưa hoàn thành) · <b>оде́ться</b> mặc đồ · '
    '<b>оде́жда</b> quần áo</div>'
)

B = {
    "docbangmat": 67,
    "loitubat": 3,
    "nguonsai": 1,
    "baolen": [
        "Lỗi tự bắt khi đọc lại (3): о́бморок từng viết «tiếng Nga không có động từ riêng cho ngất» — sai (có потеря́ть созна́ние…), đã sửa thành «cách nói thông dụng nhất»; гвоздь từng ghi chỉ số nhiều cách 1 về gốc — thật ra cách 1 và 4 (гво́зди); рукави́ца từng dịch «găng tay hở ngón» — sai, là găng bao không chia ngón. Ngoài ra máy bắt 1 lỗi trọng âm của tôi: пове́ствование → повествова́ние (không tính vào 3).",
        "Nguồn sai đã bác (1): gloss Anh của спид có «speed / rate / tempo» — đó là một từ khác (lóng), không dùng; đề tiếng Việt giữ «AIDS, bệnh AIDS».",
        "V cần duyệt (2): переодева́ться thêm «cải trang» (gloss to disguise oneself; nay trùng hết nghĩa với переоде́ться nhưng badge THỂ tách) · глухо́й thêm «vô thanh» (gloss voiceless/unvoiced — dùng thật trong ngữ âm: глухо́й согла́сный). Grep tudien.json + mọi file lô: không thẻ nào khác có «cải trang»/«vô thanh». Chưa chạy vacham trên bộ sưu tập.",
        "Không chắc — đã hạ Mức tin trên thẻ: простыня́ ← просто́й «vải trơn» (máy khớp chuỗi; từ nguyên được nhiều sách chọn nhưng có thuyết khác ← простере́ть «trải ra»); о́бморок ← об- + мо́рок «màn tối» (gần мрак).",
        "Không chắc — viết thẳng, không ghi Mức tin: фона́рь ← Hy Lạp phanárion; хала́т mượn phương Đông qua tiếng Turk; хала́тность ← хала́т (giải thích phổ biến); гвозди́ка đặt tên theo hình cái đinh của nụ đinh hương.",
        "Họ hàng cố ý vắng: або́рт (mượn đứng một mình), о́бморок (họ chỉ có qua từ nguyên không chắc — đã nêu trong ô Mức tin thay vì mục Họ hàng).",
        "Họ hàng KHÔNG ghép по́весть với вести́/повести́ (gốc вед- «dẫn»); по́весть ghép với изве́стный [k86], изве́стие, пове́стка (gốc вест- «tin»). Ô đỏ của по́весть cảnh báo chính cặp dễ lẫn này.",
    ],
}
