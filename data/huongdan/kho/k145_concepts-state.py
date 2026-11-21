# -*- coding: utf-8 -*-
"""k145 — concepts::state: 19 từ — từ quốc tế chính trị/xã hội + mấy CẶP THỂ đi đôi.

Không khối hệ thống. Chỗ cần nhất quán trong lô:
(1) -и́зм (chủ nghĩa) ↔ -и́ст (người theo): социализм, фашизм ↔ фашист, пессимист (khớp оптимист k105).
(2) Cặp thể: thẻ đầu cặp giải gốc, thẻ kia dẫn chiếu + nói đúng một chỗ khác
    (ошибаться/ошибиться · исполниться/исполняться · радовать/обрадовать).
(3) Gốc -полн- ĐẦY: исполниться khớp выполнить (k02) / полный (k113).
(4) радовать (cách 4, LÀM vui) đối lại радоваться (cách 3, k136).
Họ hàng: cố ý vắng ở митинг — từ mượn đứng một mình, không có phái sinh thông dụng.
"""

# 🔴 KHÔNG dựng biến khối dùng chung (HE/LUAT/THE…) rồi cộng vào mọi thẻ.

V = {
    "мужественный": "can trường",                     # RÚT «dũng cảm» — trùng смелый (k88, đã nạp)
    "исполниться": "thành hiện thực, tròn tuổi",      # bỏ «;» và ngoặc «(tuổi)»
    "исполняться": "thành hiện thực, tròn tuổi, được biểu diễn",  # «tràn đầy (cảm xúc)» gloss Anh không xác nhận; thêm «performed» gloss có
    "обрадовать": "làm vui mừng, làm mừng rỡ",        # bỏ «ai» chen giữa
    "радовать": "làm vui, làm vui lòng",              # bỏ «ai» chen giữa
}

S = {}

# ----------------------------------------------------------- митинг
S["митинг"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn tiếng Anh <i>meeting</i> — không chẻ trong tiếng Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đã hẹp lại: chỉ cuộc tụ tập ĐÔNG NGƯỜI, thường ngoài trời, vì một '
    'mục đích chính trị — đúng như «mít tinh» tiếng Việt (cũng từ chữ đó mà ra).</div>'
    '<div class="hd-warn">Cuộc họp ở công ty KHÔNG phải <b>ми́тинг</b> — đó là <b>собра́ние</b> '
    'hoặc <b>встре́ча</b>.</div>'
)

# ----------------------------------------------------------- социализм
S["социализм"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">социал-</span>'
    '<span class="hd-gloss">XÃ HỘI — như trong <b>социа́льный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́зм</span>'
    '<span class="hd-gloss">CHỦ NGHĨA (= <i>-ism</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>socialism</i>. Đuôi <b>-и́зм</b> luôn là giống đực, trọng âm '
    'gần như luôn nằm trên nó: <b>фаши́зм</b>, <b>оптими́зм</b>. Người theo thì đổi sang <b>-и́ст</b>: '
    '<b>социали́ст</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>социа́льный</b> thuộc xã hội · <b>социали́ст</b> người theo CNXH · '
    '<b>социалисти́ческий</b> xã hội chủ nghĩa</div>'
)

# ----------------------------------------------------------- фашизм
S["фашизм"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">фаш-</span>'
    '<span class="hd-gloss">Ý <i>fascio</i> — BÓ, nhóm (bó que, biểu tượng quyền lực La Mã)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́зм</span>'
    '<span class="hd-gloss">CHỦ NGHĨA</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>fascism</i>. Tiếng Nga viết <b>ш</b> theo cách đọc tiếng Ý '
    '(<i>sc</i> đọc như «sh»), không theo mặt chữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>фаши́ст</b> kẻ phát xít · <b>фаши́стский</b> thuộc phát xít · '
    '<b>антифаши́ст</b> người chống phát xít</div>'
)

# ----------------------------------------------------------- гражданство
S["гражданство"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гражда́н-</span>'
    '<span class="hd-gloss">CÔNG DÂN — <b>граждани́н</b> rụng <b>-ин</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ство</span>'
    '<span class="hd-gloss">→ danh từ chỉ TƯ CÁCH, trạng thái (như <b>де́тство</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Tư cách công dân» ⇒ quốc tịch — đúng khuôn Anh <i>citizen</i> → '
    '<i>citizenship</i>. <b>получи́ть гражда́нство</b> = được nhập quốc tịch.</div>'
    '<div class="hd-warn"><b>гражда́нство</b> là quốc tịch trên giấy tờ; <b>национа́льность</b> '
    'ở Nga là DÂN TỘC (Nga, Tatar…) — hai chuyện khác nhau.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>граждани́н</b> công dân · <b>гражда́нка</b> nữ công dân · '
    '<b>гражда́нский</b> dân sự</div>'
)

# ----------------------------------------------------------- импорт
S["импорт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn qua châu Âu, không chẻ trong tiếng Nga. Gốc Latin: <i>im-</i> VÀO + '
    '<i>portare</i> MANG.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mang VÀO ⇒ nhập khẩu. Trọng âm ở đầu: <b>и́мпорт</b>. Cặp ngược chỉ đổi '
    'tiền tố: <b>э́кспорт</b> (<i>ex-</i> RA) = xuất khẩu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>э́кспорт</b> xuất khẩu · <b>импорти́ровать</b> nhập khẩu (động từ)</div>'
)

# ----------------------------------------------------------- фашист
S["фашист"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">фаш-</span>'
    '<span class="hd-gloss">Ý <i>fascio</i> BÓ, nhóm — xem <b>фаши́зм</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ст</span>'
    '<span class="hd-gloss">NGƯỜI theo chủ trương đó (như <b>тури́ст</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>fascist</i>. Đổi <b>-и́зм</b> → <b>-и́ст</b> là từ chủ nghĩa ra người '
    'theo nó: <b>фаши́зм → фаши́ст</b>, <b>пессими́зм → пессими́ст</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>фаши́зм</b> chủ nghĩa phát xít · <b>фаши́стский</b> thuộc phát xít</div>'
)

# ----------------------------------------------------------- делегация
S["делегация"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">делег-</span>'
    '<span class="hd-gloss">Latin <i>delegare</i> — CỬ ai đi thay mình</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ция</span>'
    '<span class="hd-gloss">= <i>-ation</i>, danh từ GIỐNG CÁI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>delegation</i>: nhóm người được cử đi. Đuôi <b>-ация</b> ứng với '
    '<i>-ation</i>, luôn giống cái, trọng âm rơi vào <b>а́</b>: <b>делега́ция</b>, '
    '<b>организа́ция</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>делега́т</b> đại biểu (một người)</div>'
)

# ----------------------------------------------------------- анализировать
S["анализировать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">анализ-</span>'
    '<span class="hd-gloss">← <b>ана́лиз</b> sự phân tích</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ровать</span>'
    '<span class="hd-gloss">khuôn biến từ mượn thành động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trọng âm rời gốc sang <b>-и́р-</b> rồi đứng yên ở đó; <b>-ова-</b> co '
    'thành <b>-у-</b>: <b>анализи́рую</b>, <b>анализи́руешь</b>. Thể hoàn thành thêm <b>про-</b>: '
    '<b>проанализи́ровать</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ана́лиз</b> sự phân tích · <b>анали́тик</b> nhà phân tích</div>'
)

# ----------------------------------------------------------- наизусть
S["наизусть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">chỉ để dựng trạng từ, không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-из-</span>'
    '<span class="hd-gloss">TỪ, ra khỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-усть</span>'
    '<span class="hd-gloss">MIỆNG, MÔI — từ cổ <b>уста́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Nói ra từ miệng», không cần nhìn sách ⇒ thuộc lòng. Hai cụm gần như '
    'luôn đi kèm: <b>учи́ть наизу́сть</b> học thuộc lòng · <b>знать наизу́сть</b> thuộc lòng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>у́стный</b> bằng miệng (<b>у́стный экза́мен</b> thi vấn đáp)</div>'
)

# ----------------------------------------------------------- ошибаться / ошибиться
S["ошибаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-ши́б-</span>'
    '<span class="hd-gloss">← <b>оши́бка</b> lỗi (gốc <b>шиб-</b> VA, ĐÁNH — cú đánh trượt)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть-ся</span>'
    '<span class="hd-gloss">khuôn chưa hoàn thành + <b>-ся</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Động từ của <b>оши́бка</b>: nhầm, sai. Nhầm VỀ ai → <b>в</b> + cách 6: '
    '<b>Я ошиба́лся в нём</b> = tôi đã nhìn lầm anh ta. Cặp hoàn thành: <b>ошиби́ться</b>.</div>'
    '<div class="hd-warn"><b>Е́сли я не ошиба́юсь…</b> = nếu tôi không nhầm… — câu rào đón rất hay '
    'dùng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оши́бка</b> lỗi · <b>ошиби́ться</b> (HT)</div>'
)

S["ошибиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-ши́б-</span>'
    '<span class="hd-gloss">← <b>оши́бка</b> lỗi — xem <b>ошиба́ться</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть-ся</span>'
    '<span class="hd-gloss">khuôn hoàn thành + <b>-ся</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp hoàn thành của <b>ошиба́ться</b>: nhầm MỘT lần cụ thể. Chia: '
    '<b>ошибу́сь</b>, <b>ошибёшься</b>. Chú ý quá khứ rụng <b>-и-</b>, giống đực mất luôn '
    '<b>-л</b>: <b>оши́бся</b>, <b>оши́блась</b>, <b>оши́блись</b>.</div>'
    '<div class="hd-warn">Nhầm CÁI GÌ → cách 5, không giới từ: <b>Вы оши́блись но́мером</b> = anh '
    'gọi nhầm số · <b>ошиби́ться доро́гой</b> = đi nhầm đường.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оши́бка</b> lỗi · <b>ошиба́ться</b> (CHT)</div>'
)

# ----------------------------------------------------------- исполниться / исполняться
S["исполниться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ис-</span>'
    '<span class="hd-gloss">(= <b>из-</b>) RA, cho tới hết</span></div>'
    '<div class="hd-row"><span class="hd-piece">-полн-</span>'
    '<span class="hd-gloss">ĐẦY — <b>по́лный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить-ся</span>'
    '<span class="hd-gloss">khuôn hoàn thành + <b>-ся</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đầy ra cho tới hết» ⇒ thành sự thật — cùng khuôn nghĩa với '
    '<b>вы́полнить</b> làm trọn. Điều ước là chủ ngữ: <b>Мечта́ испо́лнилась</b> = giấc mơ đã '
    'thành hiện thực.</div>'
    '<div class="hd-warn">Tròn tuổi: NGƯỜI ở cách 3, số tuổi làm chủ ngữ — <b>Мне испо́лнилось '
    'два́дцать лет</b> = tôi vừa tròn 20 tuổi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>испо́лнить</b> thực hiện · <b>исполни́тель</b> người biểu diễn · '
    '<b>вы́полнить</b> hoàn thành · <b>по́лный</b> đầy</div>'
)

S["исполняться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ис-полн-</span>'
    '<span class="hd-gloss">RA + ĐẦY — xem <b>испо́лниться</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ть-ся</span>'
    '<span class="hd-gloss">khuôn chưa hoàn thành + <b>-ся</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp chưa hoàn thành của <b>испо́лниться</b>, hay gặp khi tuổi SẮP tròn: '
    '<b>За́втра ему́ исполня́ется три́дцать</b> = mai anh ấy tròn 30. Còn là bị động của '
    '<b>исполня́ть</b> biểu diễn: <b>Пе́сня исполня́ется впервы́е</b> = bài hát được biểu diễn '
    'lần đầu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>испо́лниться</b> (HT) · <b>исполня́ть</b> thực hiện, biểu diễn · '
    '<b>исполни́тель</b> người biểu diễn</div>'
)

# ----------------------------------------------------------- трудолюбивый
S["трудолюбивый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">труд-о-</span>'
    '<span class="hd-gloss">LAO ĐỘNG — <b>труд</b> (+ <b>о</b> nối hai gốc)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-люб-</span>'
    '<span class="hd-gloss">YÊU — <b>люби́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́вый</span>'
    '<span class="hd-gloss">đuôi tính từ «có tính đó»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Yêu lao động» ⇒ chăm chỉ. Cùng khuôn ghép: <b>миролюби́вый</b> yêu hoà '
    'bình. Trạng từ: <b>трудолюби́во</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>труд</b> lao động · <b>тру́дный</b> khó · <b>люби́ть</b> yêu</div>'
)

# ----------------------------------------------------------- мужественный
S["мужественный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">му́жеств-</span>'
    '<span class="hd-gloss">← <b>му́жество</b> lòng dũng cảm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-енн-ый</span>'
    '<span class="hd-gloss">đuôi tính từ «có cái đó»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Có <b>му́жество</b>» ⇒ can trường: gan mà VỮNG, chịu đựng được — không chỉ '
    'dám liều như <b>сме́лый</b>. Còn nghĩa nam tính: <b>му́жественное лицо́</b> khuôn mặt nam '
    'tính. Dạng ngắn giống đực có hai cách: <b>му́жествен</b> hoặc <b>му́жественен</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>муж</b> chồng · <b>мужчи́на</b> đàn ông · <b>му́жество</b> lòng dũng '
    'cảm</div>'
)

# ----------------------------------------------------------- пессимист
S["пессимист"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пессим-</span>'
    '<span class="hd-gloss">Latin <i>pessimus</i> — TỆ NHẤT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ст</span>'
    '<span class="hd-gloss">NGƯỜI theo chủ trương đó (như <b>тури́ст</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>pessimist</i>: người luôn chờ điều tệ nhất. Trái nghĩa cùng khuôn '
    '<b>оптими́ст</b> — nhưng khác gốc (<i>optimus</i> tốt nhất), không phải họ hàng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пессими́зм</b> sự bi quan · <b>пессимисти́чный</b> bi quan</div>'
)

# ----------------------------------------------------------- радовать / обрадовать
S["радовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рад-</span>'
    '<span class="hd-gloss">VUI — <b>рад</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ть</span>'
    '<span class="hd-gloss">khuôn động từ, KHÔNG có <b>-ся</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không <b>-ся</b> ⇒ LÀM CHO người khác vui; người được vui ở cách 4. '
    '<b>-ова-</b> co thành <b>-у-</b>: <b>ра́дую</b>, <b>ра́дует</b>.</div>'
    '<div class="hd-warn">Hai câu cùng nghĩa, đảo vai: <b>Э́то меня́ ра́дует</b> (điều đó LÀM tôi '
    'vui, cách 4) = <b>Я ра́дуюсь э́тому</b> (tôi vui VÌ điều đó, cách 3).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рад</b> vui · <b>ра́дость</b> niềm vui · <b>ра́доваться</b> vui mừng · '
    '<b>обра́довать</b> (HT)</div>'
)

S["обрадовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">chỉ làm thành thể hoàn thành, KHÔNG thêm nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ра́довать</span>'
    '<span class="hd-gloss">làm vui — <b>ра́довать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp hoàn thành của <b>ра́довать</b>: làm ai vui MỘT lần, bằng một tin, một '
    'món quà. Thứ mang niềm vui ở cách 5: <b>обра́довать ма́му пода́рком</b> = làm mẹ vui bằng món '
    'quà. Chia: <b>обра́дую</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рад</b> vui · <b>ра́довать</b> (CHT) · <b>обра́доваться</b> vui mừng</div>'
)

# ----------------------------------------------------------- заплакать
S["заплакать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">BẮT ĐẦU (như <b>заговори́ть</b> bắt đầu nói)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пла́кать</span>'
    '<span class="hd-gloss">khóc — <b>пла́кать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Khoảnh khắc nước mắt bắt đầu ⇒ bật khóc. Thể hoàn thành, không có cặp '
    'chưa hoàn thành riêng. Chia đổi <b>к → ч</b> ở mọi ngôi, y như <b>пла́кать</b>: '
    '<b>запла́чу</b>, <b>запла́чешь</b>, <b>запла́чут</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пла́кать</b> khóc · <b>плач</b> tiếng khóc</div>'
)

B = {
    "docbangmat": 61,
    "loitubat": 3,
    "nguonsai": 1,
    "baolen": [
        "V мужественный: RÚT còn 'can trường' để gỡ va chạm 'dũng cảm' với смелый (k88). Gloss Anh còn xác nhận 'nam tính' (manly) — KHÔNG thêm vì luật gỡ va chạm là rút, không thêm chữ; user muốn thì thêm tay. Cần duyệt.",
        "V исполняться: bỏ 'tràn đầy (cảm xúc)' (gloss Anh không có), thêm 'được biểu diễn' (gloss có 'to be performed'). исполниться/исполняться cùng 'thành hiện thực, tròn tuổi' — badge thể tách được. Cần duyệt.",
        "V обрадовать/радовать: chỉ bỏ chữ 'ai' chen giữa, cùng cách k136 làm với обижать.",
        "loitubat: (1) viết nhầm 'оши́биться' (trọng âm sai) trong ô đỏ ошибиться; (2) chẻ наизусть 'на-из- = TỪ trong' không chính xác, tách lại на- (dựng trạng từ) + из- (từ); (3) 'đuôi -изм luôn mang trọng âm' nói quá, hạ thành 'gần như luôn'.",
        "nguonsai: nghĩa Việt hiện tại của исполняться 'tràn đầy (cảm xúc)' không được gloss Anh xác nhận — đã bác.",
        "Không chắc (từ nguyên, chưa hạ mức tin trên thẻ): наизусть = на + из + уст- 'từ miệng' (Vasmer); ошибаться gốc шиб- 'đánh' giữ đúng khuôn k69; 'mít tinh' tiếng Việt vay từ cùng chữ meeting (qua tiếng Pháp).",
        "Giữ nguyên V cũ của 14 từ còn lại (митинг 'cuộc mít tinh, buổi tụ tập' có thể rộng — chưa đo va chạm vì agent không đọc Anki; luồng chính nên chạy congcu.py vacham).",
        "митинг cố ý không có Họ hàng: từ mượn đứng một mình.",
    ],
}
