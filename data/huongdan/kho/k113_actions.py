# -*- coding: utf-8 -*-
"""k113 — actions: động từ B1 theo CẶP THỂ + vài danh từ trừu tượng; trục là gốc ста-/став-.

Chỗ cần nhất quán trong lô:
(1) Gốc ста- «ĐỨNG» có hai mặt: -ста- TỰ đứng (оста́ться, стать — như вста́ть k71) và -став-
    LÀM CHO đứng, đặt (оста́вить — như ста́вить, поста́вить k02/k80). оста́ться = tự đứng lại
    ⇒ ở lại; оста́вить = đặt (vật) đứng lại ⇒ để lại. Phép so trải ở оста́вить, thẻ khác dẫn chiếu.
    Dạng có н (ста́ну, станови́ться, остано́вка k49) chẻ là -стан-/-станов-.
(2) приня́ть/принима́ть: lõi -ня-/-ним- «nắm, lấy» như k03 взять, k60 поня́ть; иметь nối vào lõi
    đó CHỈ theo từ nguyên, hạ mức tin.
(3) о- trong оста́ться/оста́вить/оказа́ться: tiền tố KHÔNG mang nghĩa riêng (như остано́вка k49).
Họ hàng cố ý vắng: проце́сс (mượn Latin, không có từ phái sinh Nga đáng dạy).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa, ngăn bằng dấu phẩy.
# Cả 21 thẻ đang ngăn bằng «;» ⇒ viết lại hết bằng dấu phẩy; chỗ đổi NGHĨA thì có ghi chú.
V = {
    "действие": "hành động, việc làm",
    "развитие": "sự phát triển, diễn biến",
    "вести": "dẫn, dắt",                          # RÚT «đưa đi» — trùng води́ть (cùng v + IMPF)
    "процесс": "quá trình, vụ kiện",
    "принимать": "nhận, chấp nhận",               # RÚT «uống (thuốc)» — trùng пить, lại có ngoặc
    "принять": "nhận, chấp nhận",                 # RÚT «uống (thuốc)» — trùng вы́пить
    "спасать": "cứu, giải cứu",
    "спасти": "cứu, giải cứu",
    "иметь": "có, sở hữu",                            # RÚT «có» — trùng быть, есть (xem báo cáo)
    "пройти": "đi qua, đi ngang qua",
    "проходить": "đi ngang qua",                  # RÚT «đi qua» — trùng переходи́ть (cùng IMPF)
    "оставить": "để lại, bỏ lại",
    "оставлять": "để lại, bỏ lại",
    "оставаться": "ở lại, còn lại",               # bỏ ghi chú trong ngoặc «(chưa xong)»
    "остаться": "ở lại, còn lại",
    "оказаться": "hóa ra là, thấy mình ở",        # bỏ ngoặc «(đâu đó)»
    "становиться": "trở nên, trở thành",          # bỏ «dần» — là nhãn thể trá hình, badge đã có
    "стать": "trở thành, trở nên",
    "сила": "sức mạnh, sức, lực",                 # «quyền lực» là nghĩa của власть; gloss «force» xác nhận «lực»
    "условие": "điều kiện, điều khoản",
    "полный": "đầy, đầy đủ",                      # RÚT «toàn bộ» — trùng це́лый (cùng adj)
}

# ---------------------------------------------------------------- действие
S["действие"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">действ-</span>'
    '<span class="hd-gloss">HÀNH ĐỘNG — gốc của <b>де́йствовать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ие</span>'
    '<span class="hd-gloss">đuôi danh từ giống trung (như <i>-ение</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái đang ĐƯỢC LÀM, đang có tác động ⇒ hành động, và cả «tác dụng»: '
    '<b>де́йствие лека́рства</b> tác dụng của thuốc. Cái đang thật sự vận hành thì có thật ⇒ '
    '<b>действи́тельно</b> = thật sự.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>де́йствовать</b> hành động, có hiệu lực · <b>действи́тельно</b> thật sự · '
    '<b>действи́тельный</b> có thật, còn hiệu lực</div>'
)

# ---------------------------------------------------------------- развитие
S["развитие"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span>'
    '<span class="hd-gloss">TÁCH RA, mở bung ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ви-</span>'
    '<span class="hd-gloss">CUỘN, XOẮN — gốc của <b>вить</b> (bện)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тие</span>'
    '<span class="hd-gloss">đuôi danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tháo cuộn ra, mở dần ra ⇒ phát triển. Tiếng Anh dùng đúng hình ảnh ấy: '
    '<i>develop</i> vốn là «mở gói ra». Nghĩa thứ hai cũng từ đó: sự việc «mở ra» từng bước = '
    '<b>разви́тие собы́тий</b> diễn biến sự việc.</div>'
    '<div class="hd-warn">Động từ có hai dạng: <b>развива́ть</b> phát triển CÁI GÌ (cách 4) · '
    '<b>развива́ться</b> TỰ phát triển — <b>Го́род бы́стро развива́ется</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>развива́ть</b> phát triển (cái gì) · <b>разви́ть</b> phát triển (HT) · '
    '<b>развива́ться</b> tự phát triển · <b>вить</b> bện, xoắn</div>'
)

# ------------------------------------------------------------------- вести
S["вести"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вес- (вед-)</span>'
    '<span class="hd-gloss">DẪN — gốc thật là <i>вед-</i>, <i>д</i> hoá <i>с</i> trước <i>-ти</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ти́</span>'
    '<span class="hd-gloss">đuôi nguyên thể có trọng âm, như <b>идти́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Động từ MỘT CHIỀU: đang dẫn ai tới một nơi. Dẫn đi lại, hay dẫn là '
    '<b>води́ть</b> (<i>е → о</i>). Gốc <i>вед-</i> hiện rõ ở hiện tại: <b>веду́, ведёшь</b>; '
    'quá khứ rơi hẳn <i>д</i>: <b>вёл, вела́, вели́</b>.</div>'
    '<div class="hd-warn"><b>вести́</b> (dẫn, đi bộ) và <b>везти́</b> (chở bằng xe) đọc gần như '
    'y hệt — phân biệt bằng nghĩa: <b>веду́</b> ≠ <b>везу́</b>.</div>'
    '<div class="hd-warn"><b>вести́ себя́</b> = cư xử: <b>Веди́ себя́ хорошо́!</b> Ngoan nào!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>води́ть</b> dẫn (nhiều chiều) · <b>привести́</b> dẫn tới · '
    '<b>провести́</b> tiến hành; trải qua (thời gian) · <b>веду́щий</b> người dẫn chương trình</div>'
)

# ----------------------------------------------------------------- процесс
S["процесс"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn Latin <i>processus</i> (<i>pro-</i> tiến tới + <i>cedere</i> đi) — '
    'chính là <i>process</i> của tiếng Anh. Không chẻ theo kiểu Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhận ra chứ không phải học: giữ cả hai chữ <i>с</i> như tiếng Anh, nhấn '
    'âm hai <b>проце́сс</b>. Hai nghĩa: quá trình, và vụ kiện — <b>суде́бный проце́сс</b> phiên toà.</div>'
    '<div class="hd-warn"><b>в проце́ссе</b> + cách 2 = trong quá trình: '
    '<b>в проце́ссе рабо́ты</b> trong lúc làm việc.</div>'
)

# --------------------------------------------------------------- принимать
S["принимать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">TỚI, về phía mình</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ним-</span>'
    '<span class="hd-gloss">NẮM, LẤY — cùng lõi <i>-ня-</i> của <b>приня́ть</b>, <b>поня́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi kéo dài → thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp thể song song từng chữ: <b>принима́ть : приня́ть</b> = '
    '<b>понима́ть : поня́ть</b>. Chia đều: <b>принима́ю, принима́ешь</b>. Nghĩa và cụm dùng '
    'xem ở thẻ <b>приня́ть</b>; thể này cho việc lặp lại: <b>Врач принима́ет по вторника́м</b> '
    '— bác sĩ khám bệnh vào thứ Ba.</div>'
    '<div class="hd-warn"><b>принима́ть</b> X <b>за</b> Y (cách 4) = nhầm X là Y: '
    '<b>Меня́ ча́сто принима́ют за студе́нта</b> — người ta hay tưởng tôi là sinh viên.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>приня́ть</b> nhận (HT) · <b>понима́ть</b> hiểu · <b>приём</b> sự tiếp '
    'đón, buổi tiếp</div>'
)

# ----------------------------------------------------------------- принять
S["принять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">TỚI, về phía mình</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ня-</span>'
    '<span class="hd-gloss">NẮM, LẤY — lõi cổ chung với <b>взять</b>, <b>поня́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nắm lấy VỀ PHÍA MÌNH ⇒ nhận, chấp nhận, tiếp nhận. Bảng chia y như '
    '<b>поня́ть</b>: tương lai mọc <i>-м-</i>, mất <i>-ня-</i> — <b>приму́, при́мешь</b>; quá khứ '
    'nhấn đuôi ở giống cái — <b>при́нял, приняла́</b>.</div>'
    '<div class="hd-warn">Uống THUỐC là «nhận» thuốc, không phải «uống» thường: '
    '<b>приня́ть табле́тку</b>. Cùng kiểu: <b>приня́ть душ</b> tắm vòi sen.</div>'
    '<div class="hd-warn">Hai cụm phải thuộc: <b>приня́ть реше́ние</b> ra quyết định · '
    '<b>приня́ть уча́стие в</b> + cách 6 tham gia.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>принима́ть</b> nhận (CHT) · <b>поня́ть</b> hiểu · <b>взять</b> cầm lấy · '
    '<b>приём</b> sự tiếp đón</div>'
)

# ----------------------------------------------------------------- спасать
S["спасать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пас-</span>'
    '<span class="hd-gloss">CHE CHỞ, trông giữ — gốc của <b>пасти́</b> (chăn thả)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người chăn giữ đàn khỏi sói ⇒ cứu. Cặp thể của <b>спасти́</b> (gốc và '
    '<b>спаси́бо</b> trải ở thẻ đó). Chia đều: <b>спаса́ю, спаса́ешь</b>.</div>'
    '<div class="hd-warn">Cứu AI (cách 4) KHỎI cái gì: <b>от</b> + cách 2 — '
    '<b>спаса́ть люде́й от пожа́ра</b> cứu người khỏi đám cháy.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спасти́</b> cứu (HT) · <b>спасе́ние</b> sự cứu thoát · '
    '<b>спаса́тель</b> nhân viên cứu hộ · <b>спаси́бо</b> cảm ơn</div>'
)

# ------------------------------------------------------------------ спасти
S["спасти"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пас-</span>'
    '<span class="hd-gloss">CHE CHỞ, trông giữ — gốc của <b>пасти́</b> (chăn thả)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ти́</span>'
    '<span class="hd-gloss">đuôi nguyên thể có trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tương lai chia đều: <b>спасу́, спасёшь</b>. Quá khứ giống đực không có '
    '<i>-л</i> (như <b>вёз</b>), các dạng khác nhấn đuôi: <b>спас, спасла́, спасли́</b>. '
    'Kêu cứu: <b>Спаси́те!</b> Cứu với!</div>'
    '<div class="hd-warn"><b>спаси́бо</b> chính là <b>спаси́ Бог</b> — «Chúa cứu (bạn)», nói dính '
    'lại thành lời cảm ơn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спаса́ть</b> cứu (CHT) · <b>спасе́ние</b> sự cứu thoát · '
    '<b>спаса́тель</b> nhân viên cứu hộ · <b>спаси́бо</b> cảm ơn</div>'
)

# ------------------------------------------------------------------- иметь
S["иметь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">им-</span>'
    '<span class="hd-gloss">NẮM, GIỮ trong tay</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ть</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đang nắm trong tay ⇒ có. Chia đều: <b>име́ю, име́ешь</b>.</div>'
    '<div class="hd-warn">«Tôi có X» hằng ngày nói <b>у меня́ есть</b> X, KHÔNG nói '
    '<b>я име́ю</b>. <b>име́ть</b> đi với danh từ trừu tượng: <b>име́ть пра́во</b> có quyền · '
    '<b>име́ть смысл</b> có lý · <b>име́ть в виду́</b> ý muốn nói.</div>'
    '<div class="hd-warn">⚠️ Mức tin: <i>им-</i> nối với lõi <i>-ня-/-ним-</i> «lấy» của '
    '<b>приня́ть</b>, <b>поня́ть</b> là từ nguyên, không phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>име́ться</b> có sẵn, hiện có · <b>иму́щество</b> tài sản</div>'
)

# ------------------------------------------------------------------ пройти
S["пройти"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">XUYÊN QUA, NGANG QUA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-йти</span>'
    '<span class="hd-gloss">ĐI — chính là <b>идти́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chia như <b>идти́</b>: <b>пройду́, пройдёшь</b>; quá khứ mượn <b>шёл</b>: '
    '<b>прошёл, прошла́, прошли́</b>. Đi xuyên qua cả quãng thời gian ⇒ «trôi qua»: '
    '<b>Год прошёл</b> một năm đã qua. Hỏi han hằng ngày: <b>Как прошёл день?</b></div>'
    '<div class="hd-warn">Ngang qua CÁI GÌ: <b>ми́мо</b> + cách 2 — <b>пройти́ ми́мо до́ма</b> '
    'đi ngang qua ngôi nhà.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>проходи́ть</b> đi qua (CHT) · <b>прохо́д</b> lối đi · '
    '<b>прохо́жий</b> người qua đường · <b>идти́</b> đi</div>'
)

# --------------------------------------------------------------- проходить
S["проходить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">XUYÊN QUA, NGANG QUA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ход-</span>'
    '<span class="hd-gloss">ĐI — gốc của <b>ходи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp chia 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp thể của <b>пройти́</b>. Chia y như <b>ходи́ть</b>: <b>прохожу́</b> '
    '(<i>д→ж</i>), rồi trọng âm lùi — <b>прохо́дишь</b>. Mời khách: <b>Проходи́те!</b> = Mời vào!</div>'
    '<div class="hd-warn"><b>про-</b> đi NGANG / xuyên qua · <b>пере-</b> đi SANG bên kia: '
    '<b>проходи́ть ми́мо до́ма</b> nhưng <b>переходи́ть у́лицу</b> sang đường.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пройти́</b> đi qua (HT) · <b>прохо́д</b> lối đi · '
    '<b>прохо́жий</b> người qua đường · <b>переходи́ть</b> băng qua</div>'
)

# ---------------------------------------------------------------- оставить
S["оставить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-став-</span>'
    '<span class="hd-gloss">LÀM CHO ĐỨNG, đặt — như <b>ста́вить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đặt vật đứng lại đó rồi mình đi ⇒ để lại. Luôn cần vật bị để (cách 4). '
    'Ngôi «tôi» thêm <i>л</i> như <b>поста́вить</b>: <b>оста́влю</b>, <b>оста́вишь</b>.</div>'
    '<div class="hd-warn"><i>-став-</i> = làm cho ĐỨNG ⇒ <b>Я оста́вил ключи́ до́ма</b> (để chìa ở '
    'nhà) · <i>-ста-</i> = tự ĐỨNG ⇒ <b>Я оста́лся до́ма</b> (tôi ở nhà).</div>'
    '<div class="hd-warn"><b>Оста́вь меня́ в поко́е!</b> = Để tôi yên!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оставля́ть</b> để lại (CHT) · <b>ста́вить</b> đặt · '
    '<b>поста́вить</b> đặt đứng · <b>соста́вить</b> lập ra · <b>оста́ться</b> ở lại</div>'
)

# --------------------------------------------------------------- оставлять
S["оставлять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-став-</span>'
    '<span class="hd-gloss">LÀM CHO ĐỨNG, đặt — như <b>ста́вить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ля́ть</span>'
    '<span class="hd-gloss">đuôi kéo dài → thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Song song từng chữ với <b>соста́вить : составля́ть</b> — chữ <i>л</i> mọc '
    'đúng chỗ của <b>оста́влю</b>. Chia đều: <b>оставля́ю, оставля́ешь</b>. Phân biệt với '
    '<b>остава́ться</b> (ở lại) xem thẻ <b>оста́вить</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оста́вить</b> để lại (HT) · <b>ста́вить</b> đặt · '
    '<b>составля́ть</b> lập ra (CHT) · <b>остава́ться</b> ở lại</div>'
)

# -------------------------------------------------------------- оставаться
S["оставаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ста-</span>'
    '<span class="hd-gloss">ĐỨNG — như <b>встать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва́-ть-ся</span>'
    '<span class="hd-gloss">đuôi kéo dài → CHT · <i>-ся</i> chính mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hiện tại nuốt mất <i>-ва-</i>, y như <b>встава́ть → встаю́</b>: '
    '<b>остаю́сь, остаёшься</b>. Cặp thể của <b>оста́ться</b>.</div>'
    '<div class="hd-warn"><b>остава́ться</b> + cách 5 = VẪN LÀ: <b>Он остаётся мои́м дру́гом</b> — '
    'anh ấy vẫn là bạn tôi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оста́ться</b> ở lại (HT) · <b>встава́ть</b> đứng dậy · '
    '<b>стать</b> trở thành · <b>оставля́ть</b> để lại (vật)</div>'
)

# ---------------------------------------------------------------- остаться
S["остаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ста-</span>'
    '<span class="hd-gloss">ĐỨNG — như <b>встать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть-ся</span>'
    '<span class="hd-gloss">đuôi nguyên thể · <i>-ся</i> chính mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người khác đi, MÌNH tự đứng lại ⇒ ở lại; với đồ vật là «còn lại». '
    'Tương lai mọc <i>н</i> như <b>вста́ну</b>: <b>оста́нусь, оста́нешься</b>. Đừng lẫn với '
    '<b>оста́вить</b> (để VẬT lại) — so ở thẻ đó.</div>'
    '<div class="hd-warn">«Tôi còn X»: thứ còn lại là chủ ngữ, người ở <b>у</b> + cách 2 — '
    '<b>У меня́ оста́лось сто рубле́й</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>остава́ться</b> ở lại (CHT) · <b>встать</b> đứng dậy · '
    '<b>стать</b> trở thành · <b>оста́вить</b> để lại (vật)</div>'
)

# --------------------------------------------------------------- оказаться
S["оказаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-каз-</span>'
    '<span class="hd-gloss">ĐƯA RA CHO THẤY — như <b>показа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть-ся</span>'
    '<span class="hd-gloss">đuôi động từ · <i>-ся</i> chính mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tự cho thấy mình thật ra là gì ⇒ hoá ra. Chia như <b>сказа́ть</b>: '
    '<b>окажу́сь, ока́жешься</b>. Nghĩa thứ hai: bỗng thấy mình ở đâu — '
    '<b>Как я тут оказа́лся?</b> Sao tôi lại ở đây?</div>'
    '<div class="hd-warn">Hoá ra LÀ gì: cách 5 — <b>Он оказа́лся врачо́м</b>. Đầu câu: '
    '<b>Оказа́лось, что…</b> = Hoá ra là…</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>показа́ть</b> cho xem · <b>показа́ться</b> có vẻ · '
    '<b>доказа́ть</b> chứng minh · <b>сказа́ть</b> nói ra</div>'
)

# ------------------------------------------------------------- становиться
S["становиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">станов-</span>'
    '<span class="hd-gloss">ĐỨNG VÀO chỗ — gốc <i>ста-</i> mọc <i>н</i>, như <b>остано́вка</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть-ся</span>'
    '<span class="hd-gloss">đuôi động từ · <i>-ся</i> chính mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tự đứng vào một vị trí mới ⇒ trở nên. Cặp thể của <b>стать</b>; '
    'cũng đòi cách 5 (xem thẻ <b>стать</b>). Ngôi «tôi» thêm <i>л</i>, rồi trọng âm lùi: '
    '<b>становлю́сь, стано́вишься</b>. Rất hay gặp không chủ ngữ: <b>Стано́вится хо́лодно</b> '
    '— trời trở lạnh.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стать</b> trở thành (HT) · <b>остано́вка</b> chỗ dừng · '
    '<b>останови́ться</b> dừng lại · <b>встать</b> đứng dậy</div>'
)

# ------------------------------------------------------------------- стать
S["стать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ста-</span>'
    '<span class="hd-gloss">ĐỨNG — như <b>встать</b>, <b>стоя́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đứng vào một chỗ mới ⇒ trở thành. Tương lai mọc <i>н</i>, y như '
    '<b>вста́ну</b>: <b>ста́ну, ста́нешь</b>. Cặp thể: <b>станови́ться</b>.</div>'
    '<div class="hd-warn">Trở thành GÌ: cách 5 — <b>стать врачо́м</b>, <b>Он стал стро́же</b> '
    '(tính từ so sánh thì để nguyên).</div>'
    '<div class="hd-warn"><b>стать</b> + nguyên thể CHT = BẮT ĐẦU: <b>Он стал рабо́тать</b> — '
    'anh ấy bắt đầu làm việc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>станови́ться</b> trở nên (CHT) · <b>встать</b> đứng dậy · '
    '<b>оста́ться</b> ở lại · <b>остано́вка</b> chỗ dừng</div>'
)

# -------------------------------------------------------------------- сила
S["сила"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сил-</span>'
    '<span class="hd-gloss">SỨC — gốc trơn, không chẻ thêm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Sức của người, và «lực» trong vật lý: <b>си́ла тя́жести</b> trọng lực. '
    'Từ gốc này ra cả tính từ lẫn trạng từ hay dùng: <b>си́льный</b> mạnh, <b>си́льно</b> mạnh, rất.</div>'
    '<div class="hd-warn">Số nhiều <b>си́лы</b> = sức lực còn lại của một người: '
    '<b>У меня́ нет сил</b> — tôi hết sức rồi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>си́льный</b> mạnh · <b>си́льно</b> mạnh, rất · <b>уси́лие</b> nỗ lực · '
    '<b>наси́лие</b> bạo lực</div>'
)

# ----------------------------------------------------------------- условие
S["условие"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-слов-</span>'
    '<span class="hd-gloss">LỜI — gốc của <b>сло́во</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ие</span>'
    '<span class="hd-gloss">đuôi danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Điều đã NÓI RA cho hai bên cùng đồng ý — giao kèo bằng lời ⇒ điều kiện. '
    'Số nhiều <b>усло́вия</b> còn là hoàn cảnh: <b>в тру́дных усло́виях</b> trong điều kiện khó khăn.</div>'
    '<div class="hd-warn"><b>при усло́вии, что…</b> = với điều kiện là…</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сло́во</b> lời, từ · <b>усло́вный</b> có điều kiện, quy ước · '
    '<b>безусло́вно</b> chắc chắn (không điều kiện gì)</div>'
)

# ------------------------------------------------------------------ полный
S["полный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пол-</span>'
    '<span class="hd-gloss">ĐẦY</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Ấn–Âu với <i>full</i> (<i>p</i> ↔ <i>f</i> như <i>pater</i> ↔ '
    '<i>father</i>). Đầy CÁI GÌ: cách 2 — <b>по́лный стака́н воды́</b>. Dạng ngắn mọc <i>о</i> ở '
    'giống đực, còn lại nhấn đuôi: <b>по́лон, полна́, полны́</b>. Nói về người = đẫy đà, mập '
    '(cách nói lịch sự).</div>'
    '<div class="hd-warn">«Hoàn toàn» nói bằng <b>по́лностью</b>: '
    '<b>Я по́лностью согла́сен</b> — tôi hoàn toàn đồng ý.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́лностью</b> hoàn toàn · <b>напо́лнить</b> làm đầy · '
    '<b>испо́лнить</b> thực hiện (làm cho trọn)</div>'
)
