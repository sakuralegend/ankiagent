# -*- coding: utf-8 -*-
"""k236 — language::communication: ký tên, trích dẫn, bác bỏ, khoe; sách vở (luận điểm, bảng chữ cái…); cộng thêm, chia đều.

Chỗ cần nhất quán trong lô:
(1) в-тре́тьих: khuôn во-пе́рвых [k120], во-вторы́х [k130]; ь chêm như тре́тий [k30].
(2) расписа́ться / распи́сываться: рас- TRẢI + -пис- VIẾT — khớp расписа́ние [k126]; с→ш như подписа́ть [k135].
(3) сосла́ться / ссыла́ться: сл-/сыл- GỬI — khớp посла́ть, посыла́ть [k88].
(4) приба́вить / прибавля́ть: -бав- mảnh chung — khớp доба́вить [k133]; при- THÊM VÀO như при́быль [k163].
(5) опрове́ргнуть / опроверга́ть: верг- NÉM (KHÔNG dính прове́рить, gốc вер- TIN [k80]).
(6) итого́ ↔ ито́г [k166]; по́ровну ↔ ро́вный [k172], khuôn понемно́гу [k218]; повторе́ние ↔ повторя́ть [k54].
Họ hàng không vắng ở thẻ nào.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "справочник": "sách tra cứu, cẩm nang, sổ tay tra cứu, danh bạ",     # THIẾU directory / yellow pages
    "расписаться": "ký tên, ký nhận, đăng ký kết hôn",                   # THIẾU to get married (at a registry office)
    "расписываться": "ký tên, ký nhận, đăng ký kết hôn",                 # như trên
    "повторение": "sự lặp lại, sự nhắc lại, việc ôn tập",                # «ôn tập» trơ là động từ повторя́ть
    "анатомия": "giải phẫu học, môn giải phẫu",                          # «giải phẫu» trơ đọc ra động từ «mổ»
    "цитировать": "trích dẫn, dẫn lời",                                  # giữ nguyên, khai để cặp thể cùng dãy
    "процитировать": "trích dẫn, dẫn lời",                               # «dẫn lại» mơ hồ
    "опровергать": "bác bỏ, phản bác, chứng minh là sai",                # cặp thể cùng dãy; to disprove
    "сослаться": "viện dẫn, viện lý do, dẫn ra, trích dẫn",              # câu ví dụ 1–2 dùng nghĩa «viện lý do» mà đề không có
    "ссылаться": "viện dẫn, viện lý do, dẫn ra, trích dẫn",              # cặp thể cùng dãy
    "похвастаться": "khoe, khoe khoang",                                 # «tự hào kể» là diễn giải, không phải nghĩa
    "нулевой": "bằng không, ở mức không, thuộc về số không",             # «số không» trơ là danh từ ноль
    "поровну": "đều nhau, chia đều, thành các phần bằng nhau",           # «bằng nhau» trơ là ра́вный; in equal parts
    "прибавить": "thêm, cho thêm, tăng thêm, cộng thêm",                 # THIẾU add (numbers)
    "прибавлять": "thêm, cho thêm, tăng thêm, cộng thêm",                # cặp thể cùng dãy
}

# --------------------------------------------------------------------- парковаться
S["парковаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">парк-</span>'
    '<span class="hd-gloss">mượn thẳng <i>park</i>, như <b>парк</b> công viên</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова́ть-ся</span>'
    '<span class="hd-gloss">đuôi động từ mượn + xe của CHÍNH MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng chữ <i>to park</i> ⇒ đỗ xe. Khi chia, <i>-ова-</i> thành <i>-у-</i> và trọng âm đứng ở '
    '<b>у</b>: <b>парку́юсь, парку́ешься</b>. Cặp HT: <b>припаркова́ться</b>.</div>'
    '<div class="hd-warn">Chữ «xe» đã nằm sẵn trong <b>-ся</b>, đừng thêm nữa. Nói rõ xe nào thì bỏ <b>-ся</b>, dùng '
    'cách 4: <b>паркова́ть маши́ну</b>. Đỗ Ở ĐÂU → cách 6: <b>паркова́ться на стоя́нке</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>парко́вка</b> việc đỗ xe, bãi đỗ · <b>паркова́ть</b> đỗ (xe) · '
    '<b>парк</b> công viên; đoàn xe</div>'
)

# --------------------------------------------------------------------- в-третьих
S["в-третьих"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в</span>'
    '<span class="hd-gloss">giới từ, dạng đông cứng — không còn <b>о</b> như ở <b>во-пе́рвых</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">тре́тьих</span>'
    '<span class="hd-gloss"><b>тре́тий</b> thứ ba, cách 6 số nhiều</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng khuôn <b>во-пе́рвых</b>, <b>во-вторы́х</b>: «trong những điều thứ ba» ⇒ thứ ba là. '
    'Có gạch nối, và giữ chữ <b>ь</b> mà <b>тре́тий</b> luôn chêm khi biến đổi: <b>тре́тья, тре́тьих</b>.</div>'
    '<div class="hd-warn">Luôn tách bằng dấu phẩy: <b>В-тре́тьих, туда́ е́хать два часа́.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тре́тий</b> thứ ba · <b>треть</b> một phần ba · <b>во-вторы́х</b> thứ hai là · '
    '<b>в-четвёртых</b> thứ tư là</div>'
)

# --------------------------------------------------------------------- справочник
S["справочник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">справоч-</span>'
    '<span class="hd-gloss">THÔNG TIN TRA CỨU — <b>спра́вка</b>, chen <b>о</b>, к → ч</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ник</span>'
    '<span class="hd-gloss">cái dùng cho việc đó, như <b>уче́бник</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Quyển dùng để tìm <b>спра́вка</b>» ⇒ sách tra cứu, cẩm nang. Chữ <b>о</b> chen đã gặp ở '
    'cách 2 số nhiều <b>спра́вок</b>. Trọng âm giữ nguyên ở <b>спра́в-</b>.</div>'
    '<div class="hd-warn"><b>телефо́нный спра́вочник</b> = danh bạ điện thoại.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спра́вка</b> giấy chứng nhận, thông tin · <b>спра́вочный</b> (thuộc) tra cứu · '
    '<b>пра́вильно</b> đúng</div>'
)

# --------------------------------------------------------------------- расписаться
S["расписаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рас-</span>'
    '<span class="hd-gloss">TRẢI ra — như <b>расписа́ние</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-пис-</span>'
    '<span class="hd-gloss">VIẾT — <b>писа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть-ся</span>'
    '<span class="hd-gloss">đuôi động từ, quay về CHÍNH MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Viết trải tên của chính mình ra» ⇒ ký tên. Chia như <b>писа́ть</b>: с → ш ở mọi ngôi, '
    'trọng âm lùi từ ngôi hai — <b>распишу́сь, распи́шешься</b>. Cặp CHT: <b>распи́сываться</b>.</div>'
    '<div class="hd-warn"><b>подписа́ть</b> + cách 4 là ký CÁI GÌ (hợp đồng). <b>расписа́ться</b> không có cách 4 trần: '
    'ký VÀO đâu → <b>в</b> + cách 6, ký NHẬN gì → <b>за</b> + cách 4: <b>расписа́ться за посы́лку</b>.</div>'
    '<div class="hd-warn"><b>Они́ расписа́лись</b> = họ đã đăng ký kết hôn (cùng ký vào sổ hộ tịch).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>распи́ска</b> giấy biên nhận · <b>по́дпись</b> chữ ký · '
    '<b>расписа́ние</b> lịch, giờ tàu xe</div>'
)

# --------------------------------------------------------------------- расписываться
S["расписываться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рас-пис-</span>'
    '<span class="hd-gloss">viết TRẢI tên ra = ký (xem <b>расписа́ться</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть-ся</span>'
    '<span class="hd-gloss">hậu tố biến hoàn thành → CHƯA hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đang ký, hay phải ký: <b>Он всегда́ распи́сывается внизу́.</b> Chia đều, giữ <b>с</b>: '
    '<b>распи́сываюсь</b>. Trọng âm nhảy về trước y như <b>подписа́ть → подпи́сывать</b>.</div>'
    '<div class="hd-warn">Ký VÀO sổ: <b>в</b> + cách 6 (<b>в журна́ле</b>). Ký NHẬN món gì: <b>за</b> + cách 4 '
    '(<b>за посы́лку</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>расписа́ться</b> ký tên (HT) · <b>распи́ска</b> giấy biên nhận · '
    '<b>подпи́сывать</b> ký (văn bản) · <b>писа́ть</b> viết</div>'
)

# --------------------------------------------------------------------- повторение
S["повторение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố (làm một lượt)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-втор-</span>'
    '<span class="hd-gloss">THỨ HAI — <b>второ́й</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ние</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>повтори́ть</b>: «việc làm lần THỨ HAI» ⇒ sự lặp lại, việc ôn tập. '
    'Lặp lại CÁI GÌ → cách 2: <b>повторе́ние уро́ка</b>.</div>'
    '<div class="hd-warn">Tục ngữ ai học tiếng Nga cũng gặp: <b>Повторе́ние — мать уче́ния.</b> '
    'Ôn luyện là mẹ của việc học.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>повтори́ть</b> nhắc lại (HT) · <b>повторя́ть</b> lặp lại, ôn lại (CHT) · '
    '<b>второ́й</b> thứ hai · <b>вто́рник</b> thứ Ba</div>'
)

# --------------------------------------------------------------------- тезис
S["тезис"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn Hy Lạp <i>thesis</i> «điều được đặt ra», không chẻ trong tiếng Nga — cùng chữ với Anh '
    '<i>thesis</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Điều đặt ra để rồi chứng minh ⇒ luận điểm. <i>th</i> thành <b>т</b> như <i>theme</i> → '
    '<b>те́ма</b>. Đi với: <b>доказа́ть те́зис</b> chứng minh luận điểm.</div>'
    '<div class="hd-warn">Bẫy với tiếng Anh: <i>thesis</i> «luận văn» KHÔNG phải <b>те́зис</b> mà là '
    '<b>диссерта́ция</b> (luận án) hay <b>дипло́мная рабо́та</b>. Số nhiều <b>те́зисы</b> còn là bản tóm tắt bài '
    'báo cáo.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гипо́теза</b> giả thuyết · <b>си́нтез</b> sự tổng hợp</div>'
)

# --------------------------------------------------------------------- алфавит
S["алфавит"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">алфа-</span>'
    '<span class="hd-gloss">chữ Hy Lạp thứ nhất, <i>alpha</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-вит</span>'
    '<span class="hd-gloss">chữ thứ hai, <i>beta</i> — người Hy Lạp về sau đọc là <i>vita</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>alphabet</i>, chỉ khác <i>b</i> thành <b>в</b>. Tiếng Nga tự đặt tên y cách đó: '
    '<b>а́збука</b> = <i>аз</i> + <i>буки</i>, tên cổ của А và Б. Trọng âm ở cuối: <b>алфави́т</b>.</div>'
    '<div class="hd-warn"><b>по алфави́ту</b> (cách 3) = theo thứ tự chữ cái: <b>спи́сок по алфави́ту</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>алфави́тный</b> theo bảng chữ cái: <b>в алфави́тном поря́дке</b> theo thứ tự ABC</div>'
)

# --------------------------------------------------------------------- анатомия
S["анатомия"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ана-</span>'
    '<span class="hd-gloss">Hy Lạp <i>ana-</i>, ở đây: khắp, rời ra từng phần</span></div>'
    '<div class="hd-row"><span class="hd-piece">-том-</span>'
    '<span class="hd-gloss">Hy Lạp <i>tomē</i> NHÁT CẮT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ия</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái = Anh <i>-y</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cắt ra mà xem» ⇒ môn giải phẫu, chính là <i>anatomy</i>. Mảnh <b>-том-</b> ấy cũng nằm '
    'trong <b>а́том</b>: <i>a-</i> KHÔNG + <i>tom</i> CẮT = «không cắt nhỏ được nữa».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ана́том</b> nhà giải phẫu · <b>анатоми́ческий</b> (thuộc) giải phẫu</div>'
)

# --------------------------------------------------------------------- процитировать
S["процитировать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">trọn từ đầu tới cuối, như <b>прочита́ть</b> → hoàn thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-цити́ровать</span>'
    '<span class="hd-gloss">trích dẫn — cùng gốc <i>cite</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một lần trích trọn: <b>процити́ровать сообще́ние целико́м</b>. Chia như <b>цити́ровать</b>: '
    '<b>процити́рую, процити́руешь</b>.</div>'
    '<div class="hd-warn">Trích AI cũng đứng cách 4: <b>процити́ровать Пу́шкина</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>цити́ровать</b> trích dẫn (CHT) · <b>цита́та</b> câu trích dẫn</div>'
)

# --------------------------------------------------------------------- цитировать
S["цитировать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">цит-</span>'
    '<span class="hd-gloss">DẪN RA — Latin <i>citāre</i>, như <b>цита́та</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ровать</span>'
    '<span class="hd-gloss">đuôi động từ mượn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>to cite</i>. Khi chia, <i>-ова-</i> thành <i>-у-</i>: '
    '<b>цити́рую, цити́руешь</b>. Cặp HT: <b>процити́ровать</b>.</div>'
    '<div class="hd-warn"><b>цити́ровать</b> + cách 4 là nhắc lại NGUYÊN VĂN. Chỉ trỏ tới nguồn thì dùng '
    '<b>ссыла́ться на</b> + cách 4.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>цита́та</b> câu trích dẫn · <b>цити́рование</b> sự trích dẫn · '
    '<b>процити́ровать</b> (HT)</div>'
)

# --------------------------------------------------------------------- опровергать
S["опровергать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-про-</span>'
    '<span class="hd-gloss">hai tiền tố, không còn tách nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-верг-</span>'
    '<span class="hd-gloss">NÉM, quật — như <b>све́ргнуть</b> lật đổ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành, chia đều: <b>опроверга́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Quật đổ» một lời nói ⇒ bác bỏ, chứng minh là sai. Bác CÁI GÌ → cách 4, không giới từ: '
    '<b>опроверга́ть слу́хи</b> bác tin đồn. Cặp HT: <b>опрове́ргнуть</b>.</div>'
    '<div class="hd-warn">Khác <b>возража́ть</b>: kia chỉ là cãi lại (người nghe ở cách 3); '
    '<b>опроверга́ть</b> là cho thấy điều đó SAI.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>опрове́ргнуть</b> (HT) · <b>опроверже́ние</b> lời bác bỏ · '
    '<b>отверга́ть</b> khước từ · <b>подверга́ть</b> bắt chịu</div>'
)

# --------------------------------------------------------------------- опровергнуть
S["опровергнуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-про-верг-</span>'
    '<span class="hd-gloss">QUẬT đổ lời nói — như <b>опроверга́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ну-ть</span>'
    '<span class="hd-gloss">đuôi thể hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Quá khứ thường rơi <b>-ну-</b>, giống đực rơi luôn <b>-л</b>: <b>опрове́рг, опрове́ргла, '
    'опрове́ргли</b> — như <b>привы́кнуть → привы́к</b>; cũng gặp <b>опрове́ргнул</b>. Tương lai đều: '
    '<b>опрове́ргну</b>. Trọng âm ở <b>-ве́рг-</b>, thể CHT mới ra đuôi.</div>'
    '<div class="hd-warn">Nhìn giống <b>прове́рить</b> kiểm tra nhưng khác gốc: kia là <i>вер-</i> TIN, đây là '
    '<i>верг-</i> NÉM — để ý chữ <b>г</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>опроверга́ть</b> (CHT) · <b>опроверже́ние</b> lời bác bỏ (г → ж) · '
    '<b>отве́ргнуть</b> khước từ</div>'
)

# --------------------------------------------------------------------- сослаться
S["сослаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">chính là <b>с-</b>, chen <b>о</b> trước <b>сл</b>; không tách nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сл-</span>'
    '<span class="hd-gloss">GỬI — như <b>посла́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть-ся</span>'
    '<span class="hd-gloss">đuôi động từ + phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Gửi» người nghe tới một chỗ dựa ⇒ viện dẫn, viện lý do. Tương lai сл → шл y như '
    '<b>посла́ть → пошлю́</b>: <b>сошлю́сь, сошлёшься, сошлётся</b>. Cặp CHT: <b>ссыла́ться</b>.</div>'
    '<div class="hd-warn">Dựa VÀO gì → <b>на</b> + cách 4: <b>сосла́ться на зако́н</b> viện dẫn luật · '
    '<b>сосла́ться на за́нятость</b> lấy cớ bận.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ссы́лка</b> đường link, chỗ dẫn nguồn; sự lưu đày · <b>посла́ть</b> gửi đi · '
    '<b>присла́ть</b> gửi tới</div>'
)

# --------------------------------------------------------------------- ссылаться
S["ссылаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">như <b>со-</b> của <b>сосла́ться</b>, không tách nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сыл-</span>'
    '<span class="hd-gloss">GỬI — dạng của <b>сл-</b>, như <b>посыла́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть-ся</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành + phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Neo vào <b>ссы́лка</b> «đường link»: link GỬI bạn tới nguồn, <b>ссыла́ться</b> là trỏ tới '
    'nguồn ⇒ viện dẫn. Viết hai <b>с</b>: một của tiền tố, một của gốc. Chia đều: <b>ссыла́юсь, '
    'ссыла́ешься</b>. Cặp HT: <b>сосла́ться</b>.</div>'
    '<div class="hd-warn">Dựa VÀO gì → <b>на</b> + cách 4: <b>ссыла́ться на пра́вила</b>. Với người thì cùng cách: '
    '<b>Не ссыла́йся на меня́!</b> Đừng lôi tên tôi ra!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ссы́лка</b> đường link, chỗ dẫn nguồn · <b>посыла́ть</b> gửi · '
    '<b>посы́лка</b> bưu kiện</div>'
)

# --------------------------------------------------------------------- похвастаться
S["похвастаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">đánh dấu XONG, không thêm nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-хва́ст-</span>'
    '<span class="hd-gloss">KHOE</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать-ся</span>'
    '<span class="hd-gloss">đuôi động từ, chuyện của CHÍNH MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Khoe một lần. Chia đều lớp 1, trọng âm đứng yên: <b>похва́стаюсь, похва́стаешься</b>. '
    'Cặp CHT: <b>хва́статься</b>. Viết <b>а</b>, đừng lẫn mặt chữ với <b>хвост</b> cái đuôi.</div>'
    '<div class="hd-warn">Khoe CÁI GÌ → <b>cách 5</b>, không giới từ; khoe TRƯỚC ai → <b>пе́ред</b> + cách 5: '
    '<b>похва́статься маши́ной пе́ред друзья́ми</b>.</div>'
    '<div class="hd-warn"><b>не могу́ похва́статься</b> + cách 5 = «tôi chẳng có … mà khoe»: '
    '<b>Не могу́ похва́статься здоро́вьем.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>хва́статься</b> khoe (CHT) · <b>хвасту́н</b> kẻ khoe khoang · '
    '<b>хвастли́вый</b> hay khoe</div>'
)

# --------------------------------------------------------------------- нулевой
S["нулевой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">нул-</span>'
    '<span class="hd-gloss">SỐ KHÔNG — từ <b>нуль</b>, dạng song song của <b>ноль</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ев-о́й</span>'
    '<span class="hd-gloss">đuôi danh từ → tính từ, nhấn ở cuối</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vì dựng từ <b>нуль</b> nên viết <b>у</b>, không phải <b>о</b>. Biến như tính từ: '
    '<b>нулево́й результа́т</b> kết quả bằng không, <b>нулева́я жи́рность</b> không chất béo.</div>'
    '<div class="hd-warn"><b>нулевы́е</b> (số nhiều, hiểu ngầm «năm») = những năm 2000: <b>в нулевы́х</b>. '
    '<b>нулево́й класс</b> = lớp dự bị trước lớp 1.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ноль</b> số không · <b>обнули́ть</b> đưa về 0</div>'
)

# --------------------------------------------------------------------- итого
S["итого"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">и-</span>'
    '<span class="hd-gloss">VÀ (<b>и</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-того́</span>'
    '<span class="hd-gloss">«của cái đó» — cách 2 của <b>тот</b></span></div>'
    '<div class="hd-warn">⚠️ Mức tin: cách ghép này là từ nguyên, không phải luật suy ra được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chữ mở dòng CỘNG trên hoá đơn ⇒ tổng cộng: <b>Итого́: пятьсо́т рубле́й.</b> Viết liền, không '
    'biến đổi. <b>г</b> đọc thành <b>в</b> như ở <b>его́</b>, <b>всего́</b> — còn <b>ито́г</b> thì không.</div>'
    '<div class="hd-warn"><b>итого́</b> chỉ để đọc kết quả cộng. <b>всего́</b> cũng là «tổng cộng» nhưng còn nghĩa '
    '«vỏn vẹn, chỉ có».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ито́г</b> tổng kết, tổng số · <b>ито́говый</b> tổng kết, cuối cùng</div>'
)

# --------------------------------------------------------------------- поровну
S["поровну"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по́-</span>'
    '<span class="hd-gloss">MỖI phần</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ровн-</span>'
    '<span class="hd-gloss">BẰNG, NGANG NHAU — <b>ро́вный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-у</span>'
    '<span class="hd-gloss">đuôi cách 3 cũ mà <b>по</b> đòi, nay đông cứng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Mỗi phần bằng nhau» ⇒ chia đều. Viết LIỀN một chữ, cùng khuôn <b>понемно́гу</b> mỗi lần '
    'một ít; riêng ở đây trọng âm nhảy hẳn về <b>по́-</b>.</div>'
    '<div class="hd-warn">Hầu như luôn đi với động từ CHIA: <b>раздели́ть по́ровну</b>, '
    '<b>подели́ть де́ньги по́ровну</b> chia đều tiền.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ро́вный</b> bằng, đều · <b>ро́вно</b> đúng, tròn · <b>ра́вный</b> bằng nhau · '
    '<b>сравни́ть</b> so sánh</div>'
)

# --------------------------------------------------------------------- прибавить
S["прибавить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">THÊM VÀO — như <b>при́быль</b> lợi nhuận</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бав-</span>'
    '<span class="hd-gloss">mảnh chung của <b>доба́вить</b>, <b>уба́вить</b> — một mình không có nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thêm vào cho số lượng TĂNG ⇒ thêm, cộng thêm. Riêng ngôi «tôi» chèn <b>л</b> như '
    '<b>доба́влю</b>: <b>приба́влю</b>, rồi <b>приба́вишь</b>. Thêm «một ít» → cách 2: <b>приба́вить са́хара</b>.</div>'
    '<div class="hd-warn">Hai cụm hay gặp: <b>приба́вить ско́рость</b> tăng tốc · <b>приба́вить в ве́се</b> lên cân. '
    'Làm toán: <b>к двум приба́вить три</b> (<b>к</b> + cách 3).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прибавля́ть</b> (CHT) · <b>приба́вка</b> phần tăng thêm · '
    '<b>доба́вить</b> thêm, bổ sung · <b>уба́вить</b> bớt đi</div>'
)

# --------------------------------------------------------------------- прибавлять
S["прибавлять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-бавл-</span>'
    '<span class="hd-gloss">THÊM VÀO — như <b>приба́вить</b>, в đã thành вл</span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành, chia đều: <b>прибавля́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thêm thường xuyên, thêm dần: <b>прибавля́ть в суп укро́п</b>. Đúng khuôn '
    '<b>доба́вить → добавля́ть</b>: <b>вл</b> mà vế HT chỉ có ở ngôi «tôi» thì ở đây có '
    'mặt ở mọi ngôi.</div>'
    '<div class="hd-warn">Thêm gì đứng cách 4, thêm VÀO đâu: <b>в</b> + cách 4, hoặc <b>к</b> + cách 3 khi cộng số: '
    '<b>прибавля́ть три к двум</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>приба́вить</b> (HT) · <b>приба́вка</b> phần tăng thêm · '
    '<b>добавля́ть</b> thêm, bổ sung · <b>убавля́ть</b> bớt đi</div>'
)

B = {
    "docbangmat": 123,
    "loitubat": 3,   # ана́том: viết sai trọng âm анато́м (cửa từ điển bắt, tự sửa)
                     # прибавля́ть: câu so вл với HT rối và thừa («họ» thì không) -> viết lại
                     # анато́мия: mảnh đuôi đánh dấu -и́я sai trọng âm -> -ия
    "nguonsai": 1,   # нулевой: nguồn ghi PoS num nhưng biến cách như tính từ -> dạy theo tính từ, không chép
    "baolen": [
        "V cần duyệt (14 thẻ đổi thật): справочник (THÊM danh bạ) · расписаться, расписываться (THÊM đăng ký kết hôn) · повторение (ôn tập trơ -> việc ôn tập; THÊM sự nhắc lại) · анатомия (giải phẫu trơ -> giải phẫu học, môn giải phẫu) · процитировать (dẫn lại -> dẫn lời, khớp цитировать) · опровергать (THÊM chứng minh là sai, khớp cặp HT) · сослаться, ссылаться (THÊM viện lý do) · похвастаться (BỎ tự hào kể) · нулевой (số không trơ -> thuộc về số không) · поровну (BỎ bằng nhau trơ) · прибавить, прибавлять (cùng dãy; THÊM cộng thêm). цитировать khai trong V nhưng không đổi.",
        "сослаться / ссылаться: «viện lý do» không có mục gloss Anh riêng, nhưng 2/3 câu ví dụ của сослаться dịch đúng nghĩa này — cần user duyệt.",
        "расписаться / расписываться: «đăng ký kết hôn» có trong gloss cả hai thể nhưng cả 6 câu ví dụ không dùng; прибавить / прибавлять: «cộng thêm», «tăng thêm» (tốc độ, cân) cũng không có câu ví dụ.",
        "Trùng hết nghĩa trong lô chỉ có 5 cặp thể (распис-, цитир-, опроверг-, ссыл-/сосл-, прибав-) — badge thể tách.",
        "нулевой mang badge num (nguồn) dù là tính từ; ноль cũng num. V tách được (ноль = số không, số 0).",
        "Lời giao ghi анатомия↔атомный là báo oan: thực ra CÙNG gốc Hy Lạp tom- «cắt» (а́том = không cắt được) — thẻ dùng làm neo. прибавить↔прибыть: -бав- theo từ nguyên là dạng gây khiến của быть; KHÔNG đưa lên thẻ, giữ khuôn добавить [k133].",
        "Không chắc, KHÔNG khẳng định: хвост ↔ хвастать (thẻ chỉ nhắc đừng lẫn mặt chữ); nghĩa riêng của о-про-, со-/с- (nói thẳng không tách); рас- TRẢI ở расписаться theo khuôn расписание.",
        "Mức tin ghi ô đỏ: итого (и + того), khớp итог [k166].",
    ],
}
