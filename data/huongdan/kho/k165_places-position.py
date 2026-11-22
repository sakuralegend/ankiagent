# -*- coding: utf-8 -*-
"""k165 — places::position (lô trộn): vị trí, đi tới, xe cộ, trạng từ, giấy tờ.

Chỗ cần nhất quán trong lô:
(1) họ определи́ть / определя́ть / определе́ние: chẻ о- + преде́л «giới hạn» — vạch ranh giới
    quanh một thứ ⇒ xác định, định nghĩa; bắc cầu tiếng Anh de-FINE (Latin finis «giới hạn»).
    Máy ghép với дели́ть bằng chuỗi — không dùng: thẻ дели́ть đã cảnh báo đừng nối nghĩa theo mặt chữ.
(2) добира́ться / добра́ться: khuôn thẻ выбира́ть (-бир- gốc LẤY, бр/бир/бер; -бира́ть CHT ↔
    -бра́ть HT); до- «TỚI ĐÍCH» như thẻ договори́ться. Báo oan до́брый: chẻ до-бра-, KHÔNG phải добр-.
(3) содержа́ние: держ- «GIỮ, CẦM» đúng khuôn thẻ держа́ть («cái được giữ bên trong»).
(4) догово́р: до- + говор- đúng khuôn thẻ договори́ться. Va chạm «hợp đồng» với контра́кт — xem B.
(5) почему́-то / не́что: dẫn chiếu thẻ кто́-то (-то) và не́который (не́- không xác định, có nhấn).
Họ hàng cố ý vắng: во́зле (giới từ cổ), пози́ция, контра́кт (từ mượn đứng một mình).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "дно": "đáy, đáy biển, lòng sông",                         # bỏ ngoặc «(sông/biển)»
    "руль": "vô lăng, ghi đông, bánh lái",                     # thiếu rudder/helm
    "договор": "hợp đồng, thoả thuận, hiệp ước",               # thiếu treaty
    "содержание": "nội dung, mục lục, sự bảo dưỡng",          # thiếu table of contents, upkeep
    "повсюду": "khắp mọi nơi, rộng khắp",                      # far and wide
    "контракт": "hợp đồng, giao kèo",                          # user chốt 22/11: tách khỏi договор
    "нечто": "điều gì đó, một điều",                           # user chốt 22/11: tách khỏi что-то
}

# --------------------------------------------------------------------- возле
S["возле"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Giới từ cổ, không chẻ được bằng mắt thường.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đòi cách 2: <b>во́зле до́ма</b> cạnh nhà. Nghĩa như <b>ря́дом с</b> '
    '(+ cách 5) — sát bên. Khác <b>о́коло</b> ở chỗ <b>во́зле</b> chỉ nói chỗ đứng, không có '
    'nghĩa «khoảng» con số.</div>'
    '<div class="hd-warn"><b>друг во́зле дру́га</b> — sát cạnh nhau, vai kề vai.</div>'
)

# --------------------------------------------------------------------- наедине
S["наедине"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">Ở TRONG (một trạng thái)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-еди́н-</span>'
    '<span class="hd-gloss">MỘT — dạng cổ của <b>оди́н</b>, như trong <b>еди́ный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ở trong thế «chỉ một» với ai ⇒ riêng hai người, không có ai khác.</div>'
    '<div class="hd-warn"><b>наедине́ с</b> + cách 5: <b>оста́ться наедине́ с ним</b> ở lại riêng '
    'với anh ấy · <b>наедине́ с собо́й</b> một mình với chính mình.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>еди́ный</b> thống nhất · <b>оди́н</b> một · '
    '<b>еди́нственный</b> duy nhất · <b>одино́кий</b> cô đơn</div>'
)

# --------------------------------------------------------------------- позади
S["позади"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">ở phía</span></div>'
    '<div class="hd-row"><span class="hd-piece">-зад-</span>'
    '<span class="hd-gloss">PHÍA SAU — <b>зад</b> (từ <b>за</b> «sau»)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ở phía sau. Làm giới từ thì đòi cách 2: <b>позади́ до́ма</b> sau nhà. '
    'Đối xứng với <b>впереди́</b> phía trước.</div>'
    '<div class="hd-warn"><b>Всё позади́</b> — mọi chuyện đã qua rồi (sau lưng mình).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сза́ди</b> ở phía sau · <b>наза́д</b> lùi lại, trở lại · '
    '<b>за</b> sau, đằng sau · <b>зад</b> phía sau, mông</div>'
)

# --------------------------------------------------------------------- дно
S["дно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đáy cốc, đáy biển, lòng sông. Cách 6 nhấn đuôi: <b>на дне́</b>. Số nhiều '
    'hiếm và lệch thân: <b>до́нья</b>, <b>до́ньев</b> — gặp thì nhận ra là đủ.</div>'
    '<div class="hd-warn"><b>Пей до дна!</b> — uống cạn (cạn ly!). <b>зале́чь на дно</b> — '
    'nằm im, lẩn trốn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бездо́нный</b> không đáy (<b>без</b> + <b>дно</b>)</div>'
)

# --------------------------------------------------------------------- повсюду
S["повсюду"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">trải ra khắp — nhấn mạnh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-всю́ду</span>'
    '<span class="hd-gloss">mọi NƠI — chính là <b>всю́ду</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>всю́ду</b> + <b>по-</b> ⇒ khắp nơi khắp chốn, nhấn vào độ trải rộng. '
    'Nói hằng ngày thì <b>везде́</b> là đủ; <b>повсю́ду</b> nghe sách vở hơn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>всю́ду</b> khắp nơi · <b>везде́</b> mọi nơi · <b>весь</b> toàn bộ · '
    '<b>всегда́</b> luôn luôn</div>'
)

# --------------------------------------------------------------------- позиция
S["позиция"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — từ mượn, cùng gốc tiếng Anh '
    '<i>position</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <i>-tion</i> → <b>-ция</b>, luôn giống cái: <b>пози́ция</b> như '
    '<b>ста́нция</b> <i>station</i>. Nghĩa cũng như tiếng Anh: chỗ đứng, và lập trường của ai '
    'trong một chuyện.</div>'
)

# --------------------------------------------------------------------- добираться
S["добираться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI ĐÍCH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бир-</span>'
    '<span class="hd-gloss">gốc LẤY — cùng gốc <b>брать</b> (<b>бр/бир/бер</b>); KHÔNG phải '
    '<b>добр-</b> «tốt»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть-ся</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>добира́юсь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa «lấy» đã mờ; nhớ bằng <b>до-</b> + <b>-ся</b>: tự đưa mình tới '
    'đích, ngụ ý phải xoay xở. Đích đi với <b>до</b> + cách 2: <b>Как добира́ться до це́нтра?</b> '
    'Mẫu <b>-бира́ться</b> (CHT) ↔ <b>-бра́ться</b> (HT) như <b>выбира́ть / вы́брать</b>; cặp HT: '
    '<b>добра́ться</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>добра́ться</b> (HT) · <b>брать</b> lấy · <b>выбира́ть</b> chọn · '
    '<b>собира́ть</b> gom, thu thập</div>'
)

# --------------------------------------------------------------------- добраться
S["добраться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI ĐÍCH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бра-ть-ся</span>'
    '<span class="hd-gloss">gốc LẤY — <b>брать</b>; KHÔNG phải <b>добр-</b> «tốt»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp HT của <b>добира́ться</b>: cuối cùng cũng tới được nơi. Chia y như '
    '<b>брать → беру́</b>: <b>доберу́сь, доберёшься</b>; quá khứ giống cái nhấn đuôi '
    '<b>добрала́сь</b>.</div>'
    '<div class="hd-warn"><b>Как добра́ться до</b> + cách 2? — Đi tới … bằng cách nào? Câu hỏi '
    'đường hay dùng nhất.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>добира́ться</b> (CHT) · <b>брать</b> lấy · <b>вы́брать</b> chọn · '
    '<b>собра́ть</b> gom lại</div>'
)

# --------------------------------------------------------------------- грузовик
S["грузовик"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">груз-</span>'
    '<span class="hd-gloss">HÀNG CHỞ, vật nặng — <b>груз</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ов-</span>'
    '<span class="hd-gloss">từ tính từ <b>грузово́й</b> «chở hàng»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́к</span>'
    '<span class="hd-gloss">→ vật, cái máy</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>грузово́й автомоби́ль</b> «xe chở hàng» rút gọn thành một từ. Từ '
    'cách 2 trở đi trọng âm nhảy ra đuôi: <b>грузовика́</b>, <b>грузовики́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>груз</b> hàng hoá, vật nặng · <b>грузи́ть</b> chất hàng · '
    '<b>гру́зчик</b> người bốc vác · <b>загрузи́ть</b> chất đầy, tải xuống</div>'
)

# --------------------------------------------------------------------- руль
S["руль"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được.</div>'
    '<div class="hd-warn">⚠️ Mức tin: theo từ nguyên là từ mượn tiếng Hà Lan <i>roer</i> «bánh '
    'lái» — để biết, không suy ra được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái để LÁI: vô lăng ô tô, ghi đông xe đạp, bánh lái tàu. Trọng âm nhảy '
    'ra đuôi: <b>руля́</b>, <b>рулём</b>.</div>'
    '<div class="hd-warn"><b>за рулём</b> (cách 5) — đang cầm lái: <b>Не звони́, я за рулём</b>.'
    '</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рули́ть</b> lái, bẻ lái · <b>рулево́й</b> người lái, thuộc về lái</div>'
)

# --------------------------------------------------------------------- авария
S["авария"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — từ mượn (gốc Ý <i>avaria</i> «hư hại '
    'hàng trên tàu»).</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tai nạn của XE, MÁY MÓC: đâm xe, vỡ ống, mất điện. Người bị ngã, bị '
    'thương thì gọi là <b>несча́стный слу́чай</b>, không phải <b>ава́рия</b>.</div>'
    '<div class="hd-warn"><b>попа́сть в ава́рию</b> — gặp tai nạn (giao thông).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>авари́йный</b> khẩn cấp, sự cố — <b>авари́йный вы́ход</b> lối '
    'thoát hiểm</div>'
)

# --------------------------------------------------------------------- видимо
S["видимо"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вид-</span>'
    '<span class="hd-gloss">THẤY — <b>ви́деть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-им-</span>'
    '<span class="hd-gloss">«được …» — <b>ви́димый</b> thấy được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">→ trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Theo những gì thấy được» ⇒ hình như, có vẻ — đoán từ dấu hiệu, không '
    'chắc chắn. Đứng đầu câu, ngăn bằng phẩy: <b>Ви́димо, он забы́л.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ви́деть</b> thấy · <b>ви́димый</b> nhìn thấy được · '
    '<b>неви́димый</b> vô hình · <b>очеви́дно</b> hiển nhiên</div>'
)

# --------------------------------------------------------------------- ладно
S["ладно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">лад-</span>'
    '<span class="hd-gloss">HOÀ HỢP, đâu ra đấy — <b>лад</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-но</span>'
    '<span class="hd-gloss">→ trạng từ (từ <b>ла́дный</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Ổn thoả rồi» ⇒ thôi được, OK. Khẩu ngữ, hay mang ý chịu theo hoặc '
    'chốt để chuyển chuyện: <b>Ну ла́дно</b> — thôi được rồi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ла́дить</b> hoà thuận (<b>с</b> + cách 5) · <b>нала́дить</b> sửa cho '
    'chạy, thu xếp ổn · <b>ла́дный</b> khéo, gọn gàng</div>'
)

# --------------------------------------------------------------------- почему-то
S["почему-то"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">почему́</span>'
    '<span class="hd-gloss">TẠI SAO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-то</span>'
    '<span class="hd-gloss">«… nào đó» — có thật, chỉ là không biết</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Có lý do, nhưng không biết là gì: <b>Он почему́-то не пришёл</b> — '
    'không hiểu sao anh ấy không đến. Cùng khuôn <b>кто́-то</b>; phép so <i>-то</i> ↔ '
    '<i>-нибудь</i> nằm ở thẻ đó.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>почему́</b> tại sao · <b>кто́-то</b> ai đó · <b>что́-то</b> cái gì '
    'đó · <b>где́-то</b> ở đâu đó</div>'
)

# --------------------------------------------------------------------- нечто
S["нечто"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не́-</span>'
    '<span class="hd-gloss">KHÔNG RÕ CÁI NÀO (không phải phủ định) — có nhấn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-что</span>'
    '<span class="hd-gloss">CÁI GÌ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một cái gì đó khó gọi tên, thường lạ hoặc ấn tượng: <b>не́что стра́нное</b> '
    'một điều gì đó kỳ lạ. Sách vở, chỉ dùng ở cách 1 và 4; nói thường thì <b>что́-то</b>.</div>'
    '<div class="hd-warn">Nhấn ở <b>не́</b> = «cái gì đó»; nhấn ở cuối <b>ничто́</b> = «không '
    'gì cả» — trái nghĩa hẳn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>не́кто</b> một người nào đó · <b>не́который</b> nào đó, một số · '
    '<b>что́-то</b> cái gì đó · <b>что</b> cái gì</div>'
)

# --------------------------------------------------------------------- содержание
S["содержание"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG, gộp lại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-держ-</span>'
    '<span class="hd-gloss">gốc GIỮ, CẦM — <b>держа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ание</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái được giữ bên trong ⇒ nội dung; trang liệt kê nội dung ⇒ mục lục. '
    'Cấu tạo y hệt tiếng Anh <i>content</i> (Latin <i>con-</i> cùng + <i>tenere</i> giữ). Giữ '
    'cho ai/cái gì sống, chạy được ⇒ sự nuôi, bảo dưỡng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>держа́ть</b> giữ · <b>содержа́ть</b> chứa, nuôi · '
    '<b>содержи́мое</b> thứ đựng bên trong · <b>подде́ржка</b> sự ủng hộ</div>'
)

# --------------------------------------------------------------------- договор
S["договор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI ĐÍCH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-говор</span>'
    '<span class="hd-gloss">NÓI — <b>говори́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>договори́ться</b>: nói với nhau tới đích rồi ghi lại ⇒ '
    'hợp đồng, thoả thuận, hiệp ước giữa các nước. <b>заключи́ть догово́р</b> ký kết hợp đồng.</div>'
    '<div class="hd-warn">Nhấn <b>-во́р</b>: <b>догово́р</b>, <b>догово́ры</b>. Kiểu <i>до́говор</i> '
    'nghe đầy đường nhưng là khẩu ngữ, sai chuẩn sách.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>договори́ться</b> thoả thuận được · <b>говори́ть</b> nói · '
    '<b>разгово́р</b> cuộc trò chuyện · <b>перегово́ры</b> cuộc đàm phán</div>'
)

# --------------------------------------------------------------------- контракт
S["контракт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — từ mượn, cùng gốc tiếng Anh '
    '<i>contract</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đọc gần như tiếng Anh, nhấn âm cuối. Hẹp hơn <b>догово́р</b>: hay dùng '
    'cho hợp đồng thương mại, lao động, thể thao — <b>рабо́тать по контра́кту</b> làm việc theo '
    'hợp đồng. Hiệp ước giữa các nước luôn là <b>догово́р</b>.</div>'
)

# --------------------------------------------------------------------- копия
S["копия"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — từ mượn, cùng gốc tiếng Anh <i>copy</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <i>-y</i> → <b>-ия</b>, giống cái: <i>copy</i> → <b>ко́пия</b> như '
    '<i>history</i> → <b>исто́рия</b>. Nhấn âm đầu như tiếng Anh.</div>'
    '<div class="hd-warn"><b>Он ко́пия отца́</b> — nó giống bố như đúc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>копи́ровать</b> sao chép · <b>ксероко́пия</b> bản photocopy</div>'
)

# --------------------------------------------------------------------- определение
S["определение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-преде́л-</span>'
    '<span class="hd-gloss">XÁC ĐỊNH — chính là <b>определи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Việc vạch ranh giới cho một thứ ⇒ sự xác định; vạch ranh giới cho một '
    'khái niệm ⇒ định nghĩa. Cách nghĩ của <b>определи́ть</b> nằm ở thẻ đó.</div>'
    '<div class="hd-warn"><b>по определе́нию</b> — theo định nghĩa, tức là hiển nhiên phải thế.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>определи́ть</b> · <b>определя́ть</b> xác định · <b>определённый</b> '
    'nhất định · <b>преде́л</b> giới hạn</div>'
)

# --------------------------------------------------------------------- определить
S["определить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">QUANH, bao lấy</span></div>'
    '<div class="hd-row"><span class="hd-piece">-преде́л-</span>'
    '<span class="hd-gloss">GIỚI HẠN, ranh giới — <b>преде́л</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi HT, chia đều: <b>определю́, определи́шь</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vạch ranh giới quanh một thứ ⇒ xác định nó; y hệt tiếng Anh '
    '<i>de-<b>fine</b></i> (Latin <i>finis</i> «giới hạn»). Đi thẳng cách 4: <b>определи́ть '
    'причи́ну</b> xác định nguyên nhân. Cặp CHT: <b>определя́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>определя́ть</b> (CHT) · <b>определе́ние</b> định nghĩa · '
    '<b>определённый</b> nhất định · <b>преде́л</b> giới hạn</div>'
)

# --------------------------------------------------------------------- определять
S["определять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-преде́л-</span>'
    '<span class="hd-gloss">vạch ranh giới quanh — <b>преде́л</b> giới hạn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>определя́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>определи́ть</b>: <b>-и́ть</b> (HT) ↔ <b>-я́ть</b> (CHT), '
    'như <b>позво́лить / позволя́ть</b>. Cách nghĩ «vạch ranh giới» nằm ở thẻ '
    '<b>определи́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>определи́ть</b> (HT) · <b>определе́ние</b> định nghĩa · '
    '<b>определённый</b> nhất định</div>'
)

B = {
    "docbangmat": 88,
    "loitubat": 0,
    "nguonsai": 1,
    "baolen": [
        "VA CHẠM KHÔNG GỠ ĐƯỢC: контра́кт «hợp đồng» vẫn nằm gọn trong догово́р «hợp đồng, thoả thuận, hiệp ước» (cùng n MASC). Gloss контракт chỉ có contract/agreement — cả hai đã thuộc догово́р; nghĩa riêng thật (hợp đồng thương mại/lao động/thể thao) là sắc thái, không phải nghĩa, mà hợp đồng lao động trong luật Nga lại gọi là трудово́й догово́р. Hai lối: (a) контракт = «hợp đồng, giao kèo» — gỡ được nhưng «giao kèo» chỉ là từ đồng nghĩa tiếng Việt, user phải thuộc vẹt chữ nào đi với từ nào; (b) để nguyên «hợp đồng», chấp nhận đề có hai đáp án. Tôi chưa ghi V cho контракт, chờ luồng chính chọn.",
        "GẦN VA CHẠM máy không bắt (khác chuỗi): не́что «một cái gì đó» ↔ что́-то «cái gì đó» (cùng pron) — nhìn đề gần như không phân biệt được; gloss нечто chỉ có «something (khó tả)». Không tự sửa.",
        "Ngoài lô (đã nạp, chỉ báo): всю́ду «mọi nơi, khắp nơi <i>(trang trọng, sách vở)</i>» và везде́ «mọi nơi, khắp nơi&nbsp;<i>(dùng nhiều hàng ngày)</i>» trên Anki còn ngoặc cấm theo §2c; bỏ ngoặc là hai thẻ trùng hết nghĩa.",
        "Nguồn sai bác: BAT THUONG của договор ghi số nhiều song song «догово́ры, догово́ра» — dạng phụ thật là договора́ (khẩu ngữ, nhấn đuôi), «догово́ра» là cách 2 số ít; không dùng.",
        "Máy bắt 1 lỗi của tôi (không tính vào loitubat): viết соде́ржимое, đúng là содержи́мое — đã sửa.",
        "Không chắc: руль ← tiếng Hà Lan roer (để trong ô ⚠️ Mức tin); авария gốc Ý avaria; во́зле không chẻ (từ nguyên nối вдоль nhưng không ghi lên thẻ); câu «до́говор là khẩu ngữ, sai chuẩn» — từ điển mới có nơi ghi до́говор là khẩu ngữ chấp nhận được.",
        "Họ определи́ть: chẻ о- + преде́л, KHÔNG nối дели́ть (máy ghép chuỗi; thẻ дели́ть đã cảnh báo nối theo mặt chữ). V cần duyệt: дно, руль (+bánh lái), договор (+hiệp ước), содержание (+mục lục, sự bảo dưỡng), повсюду (+rộng khắp).",
    ],
}
