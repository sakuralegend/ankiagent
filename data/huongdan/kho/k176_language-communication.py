# -*- coding: utf-8 -*-
"""k176 — language::communication (lô trộn): gặp nhau, nói chuyện, âm thanh, thời điểm, đưa/giữ/dựng.

Chỗ cần nhất quán trong lô:
(1) Sáu cặp thể soạn THÀNH ĐÔI, thẻ HT và CHT chẻ cùng khuôn: ви́деться/уви́деться,
    предста́виться/представля́ться, подава́ть/пода́ть, поддержа́ть/подде́рживать,
    восстанови́ть/восстана́вливать, звуча́ть/прозвуча́ть. Bảng chia lệch chỉ nói ở thẻ có nó.
(2) под- ở подава́ть/пода́ть = SÁT TỚI (đưa tới tay); ở поддержа́ть = TỪ DƯỚI (đỡ lên).
    Hai nghĩa thật của cùng một tiền tố — nói rõ ở từng thẻ, không gộp.
(3) подава́ть/пода́ть: Họ hàng KHÔNG ghi пода́рок (nó đi từ подари́ть, gốc дар-).
(4) зара́нее: gốc ран- SỚM (ра́но), KHÔNG phải ра́на vết thương / ра́неный.
Họ hàng cố ý vắng: акце́нт (từ mượn Latin, phái sinh duy nhất акценти́ровать hiếm, không đáng dạy).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "акцент": "giọng lơ lớ, giọng vùng miền, sự nhấn mạnh",            # accent (foreign/regional) / emphasis
    "болтать": "tán gẫu, trò chuyện, nói linh tinh, đung đưa, lắc",   # THIẾU dangle/swing, shake (a liquid)
    "падение": "sự rơi, cú ngã, sự sụt giảm, sự sụp đổ",              # THIẾU collapse/downfall
    "подавать": "đưa, chuyển, dọn món, nộp, cung cấp",                # bỏ «trao» (trùng nghĩa «đưa»): xem B.baolen về va chạm давать
    "подать": "đưa, chuyển, dọn món, nộp, ra hiệu, phát bóng",        # serve/bring to table, submit, give a signal, serve a ball
    "поддержать": "ủng hộ, hỗ trợ, tán thành, đỡ, duy trì",           # bỏ «cổ vũ» (không có trong gloss); THIẾU hold up, maintain
    "поддерживать": "ủng hộ, hỗ trợ, tán thành, đỡ, duy trì",         # bỏ «động viên»; THIẾU second (a motion), hold up
}

# --------------------------------------------------------------------- акцент
S["акцент"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn (Latin <i>accentus</i>) — không chẻ được trong tiếng Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Y hệt tiếng Anh <i>accent</i>, đủ cả hai nghĩa: giọng lơ lớ của người '
    'nói tiếng nước ngoài (<b>говори́ть с акце́нтом</b>), và sự nhấn mạnh '
    '(<b>сде́лать акце́нт</b> на + cách 6).</div>'
    '<div class="hd-warn">Trọng âm của một từ KHÔNG gọi là <b>акце́нт</b> — đó là '
    '<b>ударе́ние</b>.</div>'
)

# --------------------------------------------------------------------- болтать
S["болтать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">болт-</span>'
    '<span class="hd-gloss">LẮC, ĐUNG ĐƯA — gốc trơn, không chẻ thêm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">động từ chia đều: болта́ю, болта́ешь</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng một từ cho việc lắc và việc nói: <b>болта́ть нога́ми</b> đung đưa '
    'chân · <b>болта́ть по телефо́ну</b> buôn điện thoại. Cái lưỡi lắc liên hồi ⇒ tán gẫu.</div>'
    '<div class="hd-warn">Sắc thái thân mật, nói chuyện phiếm. Trò chuyện nghiêm túc là '
    '<b>разгова́ривать</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поболта́ть</b> tán gẫu một lúc · <b>болту́н</b> người lắm mồm · '
    '<b>болтовня́</b> chuyện phiếm · <b>разболта́ть</b> để lộ bí mật</div>'
)

# --------------------------------------------------------------------- поболтать
S["поболтать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">MỘT LÚC, một chút</span></div>'
    '<div class="hd-row"><span class="hd-piece">болта́ть</span>'
    '<span class="hd-gloss">tán gẫu</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>по-</b> ở đây cắt hành động thành một khoảng ngắn: tán gẫu một lúc '
    'rồi thôi — cùng kiểu <b>погуля́ть</b> đi dạo một lát, <b>посиде́ть</b> ngồi một lúc.</div>'
    '<div class="hd-warn"><b>Дава́й поболта́ем!</b> — Tán gẫu chút đi!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>болта́ть</b> tán gẫu · <b>болтовня́</b> chuyện phiếm · '
    '<b>болту́н</b> người lắm mồm</div>'
)

# --------------------------------------------------------------------- звучать
S["звучать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">звуч-</span>'
    '<span class="hd-gloss">ÂM THANH — <b>звук</b>, к → ч</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Phát ra âm thanh» ⇒ vang lên. Như tiếng Anh <i>sound</i>: '
    '<b>Звучи́т хорошо́!</b> — Nghe hay đấy! Sau ч, đuôi -ать vẫn chia kiểu -и-: '
    '<b>звучу́, звучи́шь, звуча́т</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>звук</b> âm thanh · <b>звуково́й</b> thuộc âm thanh · '
    '<b>озву́чить</b> lồng tiếng, nói ra · <b>прозвуча́ть</b> vang lên (HT)</div>'
)

# --------------------------------------------------------------------- прозвучать
S["прозвучать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">TRỌN một lần — tiền tố thể HT</span></div>'
    '<div class="hd-row"><span class="hd-piece">звуча́ть</span>'
    '<span class="hd-gloss">vang lên (<b>звук</b> âm thanh)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Âm thanh vang lên trọn một lần: <b>прозвуча́л вы́стрел</b> một phát '
    'súng vang lên. Nghĩa bóng — lời nói «nghe ra thành»: <b>Э́то прозвуча́ло как упрёк</b> '
    'câu đó nghe như lời trách.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>звуча́ть</b> vang lên (CHT) · <b>звук</b> âm thanh · '
    '<b>озву́чить</b> lồng tiếng, nói ra</div>'
)

# --------------------------------------------------------------------- видеться
S["видеться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вид-е-ть</span>'
    '<span class="hd-gloss">THẤY — <b>ви́деть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">LẪN NHAU</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thấy nhau ⇒ gặp nhau: <b>ви́деться с</b> + cách 5 '
    '(<i>ви́деться с друзья́ми</i>). Chia như <b>ви́деть</b>, д → ж chỉ ở ngôi я: '
    '<b>ви́жусь, ви́дишься</b>.</div>'
    '<div class="hd-warn"><b>до свида́ния</b> cũng gốc вид-: с- CÙNG + вид- THẤY ⇒ «cho tới '
    'lần thấy nhau».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ви́деть</b> nhìn thấy · <b>уви́деться</b> gặp nhau (HT) · '
    '<b>свида́ние</b> cuộc hẹn · <b>телеви́дение</b> truyền hình · <b>вид</b> dáng vẻ, quang cảnh</div>'
)

# --------------------------------------------------------------------- увидеться
S["увидеться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố thể HT — không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">ви́деться</span>'
    '<span class="hd-gloss">gặp nhau</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>уви́деть</b> thấy + <b>-ся</b> lẫn nhau ⇒ gặp nhau (một lần, trọn). '
    'Chia như <b>уви́деть</b>, д → ж chỉ ở ngôi я: <b>уви́жусь, уви́дишься</b>.</div>'
    '<div class="hd-warn"><b>Уви́димся!</b> — Hẹn gặp lại! (thân mật hơn <b>до свида́ния</b>)</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уви́деть</b> nhìn thấy · <b>ви́деться</b> gặp nhau (CHT) · '
    '<b>свида́ние</b> cuộc hẹn</div>'
)

# --------------------------------------------------------------------- представиться
S["представиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пред-</span>'
    '<span class="hd-gloss">TRƯỚC mặt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-став-и-ть</span>'
    '<span class="hd-gloss">ĐẶT, dựng — <b>ста́вить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">chính mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đặt chính mình ra trước mặt người khác ⇒ tự giới thiệu. Tự đặt ra trước '
    'mắt ⇒ hiện ra: <b>предста́вился слу́чай</b> có dịp. в → вл ở ngôi я: '
    '<b>предста́влюсь</b>.</div>'
    '<div class="hd-warn"><b>Разреши́те предста́виться</b> — Cho phép tôi tự giới thiệu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>предста́вить</b> giới thiệu, hình dung · <b>представи́тель</b> người '
    'đại diện · <b>представле́ние</b> buổi biểu diễn, khái niệm · <b>ста́вить</b> đặt</div>'
)

# --------------------------------------------------------------------- представляться
S["представляться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пред-</span>'
    '<span class="hd-gloss">TRƯỚC mặt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ставл-я-ть</span>'
    '<span class="hd-gloss">ĐẶT (в → вл) + -я- thể CHT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">chính mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>предста́виться</b>, вл có mặt ở mọi dạng: '
    '<b>представля́юсь, представля́ешься</b>.</div>'
    '<div class="hd-warn"><b>Мне представля́ется, что…</b> — Tôi thấy dường như… '
    '(nghĩa «có vẻ» hay gặp ở thể này)</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>представля́ть</b> giới thiệu, hình dung · <b>представи́тель</b> '
    'người đại diện · <b>ста́вить</b> đặt</div>'
)

# --------------------------------------------------------------------- заранее
S["заранее"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">giới từ <b>за</b> dính liền — không mang nghĩa rõ</span></div>'
    '<div class="hd-row"><span class="hd-piece">ран-</span>'
    '<span class="hd-gloss">SỚM — <b>ра́но</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ее</span>'
    '<span class="hd-gloss">đuôi so sánh hơn: <b>ра́нее</b> sớm hơn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Từ lúc sớm hơn» ⇒ làm sẵn từ trước: <b>зара́нее купи́ть биле́ты</b> '
    'mua vé trước. Gốc ран- là SỚM, không dính gì tới <b>ра́на</b> vết thương.</div>'
    '<div class="hd-warn"><b>Зара́нее спаси́бо!</b> — Cảm ơn trước nhé! (cuối lời nhờ vả)</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ра́но</b> sớm · <b>ра́нний</b> sớm (tính từ) · <b>ра́ньше</b> trước '
    'đây, sớm hơn · <b>ра́нее</b> trước đây</div>'
)

# --------------------------------------------------------------------- мгновение
S["мгновение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мгнов-</span>'
    '<span class="hd-gloss">CHỚP MẮT — cùng gốc <b>миг</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một cái chớp mắt ⇒ khoảnh khắc — y như tiếng Việt «trong chớp mắt». '
    'Văn hơn <b>моме́нт</b>; hay gặp <b>в одно́ мгнове́ние</b> trong nháy mắt.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>миг</b> khoảnh khắc · <b>мгнове́нно</b> ngay tức khắc · '
    '<b>мгнове́нный</b> tức thì · <b>мига́ть</b> nhấp nháy, chớp mắt</div>'
)

# --------------------------------------------------------------------- временный
S["временный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">времен-</span>'
    '<span class="hd-gloss">THỜI GIAN — thân của <b>вре́мя</b> (<b>вре́мени</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">→ tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thuộc về một thời» ⇒ chỉ tồn tại một thời ⇒ tạm thời. Trạng từ '
    '<b>вре́менно</b> tạm thời; dạng ngắn <b>вре́менен</b> (chèn -е-) hiếm dùng.</div>'
    '<div class="hd-warn">Dời trọng âm là đổi nghĩa: <b>вре́менный</b> tạm thời ≠ '
    '<b>временно́й</b> thuộc về thời gian.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вре́мя</b> thời gian · <b>совреме́нный</b> hiện đại · '
    '<b>своевре́менный</b> đúng lúc</div>'
)

# --------------------------------------------------------------------- рассвет
S["рассвет"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рас-</span>'
    '<span class="hd-gloss">TOẢ RA, lan khắp</span></div>'
    '<div class="hd-row"><span class="hd-piece">свет</span>'
    '<span class="hd-gloss">ÁNH SÁNG</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ánh sáng toả khắp bầu trời ⇒ rạng đông. Hai chữ с vì <b>рас-</b> gặp '
    '<b>свет</b>.</div>'
    '<div class="hd-warn"><b>на рассве́те</b> — lúc rạng sáng (giới từ <b>на</b>). Mặt trời '
    'nhô lên là <b>восхо́д со́лнца</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>свет</b> ánh sáng · <b>све́тлый</b> sáng · <b>свети́ть</b> chiếu '
    'sáng · <b>рассвета́ть</b> trời rạng sáng</div>'
)

# --------------------------------------------------------------------- падение
S["падение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пад-</span>'
    '<span class="hd-gloss">RƠI — <b>па́дать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Sự rơi, cả nghĩa đen lẫn bóng: <b>паде́ние цен</b> giá sụt · '
    '<b>паде́ние импе́рии</b> đế quốc sụp đổ.</div>'
    '<div class="hd-warn"><b>взлёты и паде́ния</b> — thăng trầm (cất lên và rơi xuống).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>па́дать</b> rơi, ngã · <b>упа́сть</b> rơi, ngã (HT) · '
    '<b>водопа́д</b> thác nước · <b>за́пад</b> phía tây (nơi mặt trời rơi xuống) · '
    '<b>напада́ть</b> tấn công</div>'
)

# --------------------------------------------------------------------- подавать
S["подавать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span>'
    '<span class="hd-gloss">SÁT TỚI (đưa tới tận tay)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-да-</span>'
    '<span class="hd-gloss">ĐƯA, CHO — <b>дава́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва-ть</span>'
    '<span class="hd-gloss">thể CHT</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đưa sát tới tay người ta. Chia như <b>дава́ть</b>: -ва- rụng ở hiện tại '
    '— <b>подаю́, подаёшь</b>.</div>'
    '<div class="hd-warn">Nghĩa RIÊNG mà <b>дава́ть</b> không có: <b>подава́ть на стол</b> dọn '
    'món · <b>подава́ть заявле́ние</b> nộp đơn · <b>подава́ть мяч</b> phát bóng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дава́ть</b> đưa, cho · <b>пода́ча</b> cú phát '
    'bóng, sự cung cấp · <b>преподава́ть</b> giảng dạy · <b>переда́ть</b> chuyển, truyền</div>'
)

# --------------------------------------------------------------------- подать
S["подать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span>'
    '<span class="hd-gloss">SÁT TỚI (đưa tới tận tay)</span></div>'
    '<div class="hd-row"><span class="hd-piece">дать</span>'
    '<span class="hd-gloss">ĐƯA, CHO</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp HT của <b>подава́ть</b>, chia y hệt <b>дать</b>: <b>пода́м, пода́шь, '
    'пода́ст, подади́м, подади́те, подаду́т</b>; quá khứ <b>подала́</b> dồn trọng âm về đuôi.</div>'
    '<div class="hd-warn"><b>Пода́й ру́ку!</b> Chìa tay ra! · <b>пода́л знак</b> ra hiệu · '
    '<b>подала́ в суд</b> kiện ra toà.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дать</b> đưa, cho · <b>подава́ть</b> (CHT) · <b>пода́ча</b> cú phát '
    'bóng · <b>переда́ть</b> chuyển, truyền</div>'
)

# --------------------------------------------------------------------- поддержать
S["поддержать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span>'
    '<span class="hd-gloss">TỪ DƯỚI</span></div>'
    '<div class="hd-row"><span class="hd-piece">держ-а-ть</span>'
    '<span class="hd-gloss">GIỮ — <b>держа́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giữ từ phía dưới ⇒ đỡ, rồi nghĩa bóng ủng hộ. Trọng âm chạy như '
    '<b>держа́ть</b>: <b>поддержу́</b> nhưng <b>подде́ржишь, подде́ржит</b>.</div>'
    '<div class="hd-warn"><b>поддержа́ть</b> + cách 4, không giới từ: '
    '<i>поддержа́ть дру́га</i> — ủng hộ bạn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>держа́ть</b> cầm, giữ · <b>подде́ржка</b> sự ủng hộ · '
    '<b>подде́рживать</b> (CHT) · <b>держа́ться</b> bám, giữ mình</div>'
)

# --------------------------------------------------------------------- поддерживать
S["поддерживать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span>'
    '<span class="hd-gloss">TỪ DƯỚI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-держ-</span>'
    '<span class="hd-gloss">GIỮ — <b>держа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть</span>'
    '<span class="hd-gloss">thể CHT, trọng âm đứng yên ở <b>-де́р-</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>поддержа́ть</b>. Ngoài «ủng hộ», nghĩa «giữ cho tiếp '
    'diễn» rất hay dùng ở thể này.</div>'
    '<div class="hd-warn"><b>подде́рживать связь</b> giữ liên lạc · '
    '<b>подде́рживать поря́док</b> giữ trật tự.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>подде́ржка</b> sự ủng hộ · <b>держа́ть</b> cầm, giữ · '
    '<b>поддержа́ть</b> (HT)</div>'
)

# --------------------------------------------------------------------- восстановить
S["восстановить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вос-</span>'
    '<span class="hd-gloss">LÊN — dựng lên lại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-стан-</span>'
    '<span class="hd-gloss">ĐỨNG — <b>стать</b>, <b>станови́ться</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ов-и-ть</span>'
    '<span class="hd-gloss">động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cho đứng lên trở lại ⇒ khôi phục, xây lại. в → вл ở ngôi я và trọng '
    'âm lùi: <b>восстановлю́</b> nhưng <b>восстано́вишь</b>.</div>'
    '<div class="hd-warn"><b>восстанови́ть си́лы</b> lấy lại sức · '
    '<b>восстанови́ть в па́мяти</b> nhớ lại.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>станови́ться</b> trở nên · <b>останови́ть</b> dừng lại · '
    '<b>восстановле́ние</b> sự khôi phục · <b>восста́ние</b> cuộc khởi nghĩa</div>'
)

# --------------------------------------------------------------------- восстанавливать
S["восстанавливать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вос-</span>'
    '<span class="hd-gloss">LÊN — dựng lên lại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-стан-</span>'
    '<span class="hd-gloss">ĐỨNG — <b>станови́ться</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́влива-ть</span>'
    '<span class="hd-gloss">thể CHT</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>восстанови́ть</b>: о đổi thành а, chèn вл — đúng kiểu '
    '<b>останови́ть → остана́вливать</b>. Chia đều: <b>восстана́вливаю, '
    'восстана́вливаешь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>восстанови́ть</b> (HT) · <b>восстановле́ние</b> sự khôi phục · '
    '<b>станови́ться</b> trở nên</div>'
)

B = {
    "docbangmat": 108,
    "loitubat": 1,
    "nguonsai": 0,
    "baolen": [
        "Va chạm давать↔подавать là BÁO OAN do máy, không phải đề mơ hồ thật: tach_nghia() bỏ «cho» như hư từ, nên đề давать «đưa, cho, trao» bị đọc thành {đưa, trao} rồi nằm gọn trong подавать. Chiều ngược với lời giao (давать ⊆ подавать, không phải подавать ⊆ давать). Đã gỡ bằng V: подавать/подать bỏ «trao» (trùng nghĩa «đưa», không mất nghĩa nào), thêm nghĩa riêng dọn món · nộp · ra hiệu · phát bóng; mô phỏng vacham với V áp vào: lô k176 không còn va chạm nào. Gốc rễ nên sửa ở soatlo.tach_nghia: «cho» là NGHĨA CHÍNH của давать/дать, lọc nó là mù đúng cặp này.",
        "Đồng tự THẬT (không nới MIEN_TRU, đã viết vòng): пода́ть (động từ) ↔ по́дать «thuế» (nouns.csv). Cửa TRONG AM LECH kêu ở mọi chỗ in đậm nguyên thể пода́ть ⇒ thẻ подать dùng Пода́й / пода́л / подала́ thay cho пода́ть ру́ку / знак / в суд; thẻ подавать bỏ пода́ть khỏi Họ hàng. Nếu luồng chính thêm пода́ть vào MIEN_TRU thì có thể khôi phục hai chỗ đó.",
        "Lỗi tự bắt (loitubat=1): thẻ подать viết пода́ла в суд — quá khứ giống cái đúng là подала́ (dữ liệu ngữ pháp xác nhận).",
        "Lời giao «подать↔подарок gốc -дар- khác -да-»: đúng về mặt CẤU TẠO (подарок đi từ подарить), nhưng về từ nguyên дар và дать cùng gốc Ấn-Âu *deh₃- (như Hy Lạp dōron). Thẻ không nhắc подарок, nên không có câu nào sai — chỉ ghi để lô sau đừng viết «không cùng gốc».",
        "Không chắc (mức tin vừa): временно́й «thuộc về thời gian» trong ô đỏ thẻ временный — dạng này máy không tra được (nouns.csv chỉ có danh từ), trọng âm theo hiểu biết của tôi; болта́ть: câu «cái lưỡi lắc liên hồi ⇒ tán gẫu» là móc nhớ từ hai nghĩa có thật trong gloss, KHÔNG khẳng định đó là đường từ nguyên.",
        "Họ hàng cố ý vắng: акцент (từ mượn Latin; phái sinh акцентировать hiếm, không đáng dạy).",
        "V cần duyệt (7 thẻ): акцент (thêm «giọng lơ lớ» — nghĩa chính accent nước ngoài bị thiếu; «chất giọng vùng miền»→«giọng vùng miền»), болтать (THIẾU đung đưa, lắc), падение (THIẾU sự sụp đổ), подавать + подать (xem dòng 1; «dọn ra»→«dọn món»), поддержать (bỏ «cổ vũ», thêm đỡ, duy trì), поддерживать (bỏ «động viên», thêm tán thành, đỡ). Không viết V cho 13 thẻ còn lại (đề cũ đã đúng). Cặp поддержать/поддерживать cùng một dòng nghĩa — badge thể tách sạch.",
    ],
}
