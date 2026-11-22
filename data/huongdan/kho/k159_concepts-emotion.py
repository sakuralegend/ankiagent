# -*- coding: utf-8 -*-
"""k159 — concepts::emotion: tin/tin chắc, hiểu rõ, cô đơn, trách nhiệm, cảm giác.

Chỗ cần nhất quán trong lô:
(1) gốc вер- TIN (ве́рить): дове́рие · дове́рить / доверя́ть — -и́ть (HT) ↔ -я́ть (CHT) như прове́рить / проверя́ть.
(2) gốc бр/бир/бер LẤY (брать): разбира́ться / разобра́ться — khuôn -бира́ть (CHT) ↔ -бра́ть (HT) của выбира́ть.
(3) убеди́ться / убежда́ться chẻ theo убеди́ть + -ся (không chẻ lại -бед-, thẻ убеди́ть đã giữ phần từ nguyên có mức tin).
(4) gốc од- MỘT (оди́н): одино́кий → одино́чество (к→ч như челове́к → челове́чество).
(5) gốc ясн- RÕ (я́сный): вы́яснить / выясня́ть — máy không thấy, tự thêm.
Họ hàng không vắng ở thẻ nào.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "выяснить": "tìm ra, làm rõ, làm sáng tỏ",              # khớp cặp выяснять, badge thể tách
    "выяснять": "tìm ra, làm rõ, làm sáng tỏ",              # «tìm hiểu» lệch nghĩa find out
    "убедиться": "tin chắc, kiểm chứng, tự thấy rõ",        # «xác nhận» = confirm, sai nghĩa
    "убеждаться": "tin chắc, kiểm chứng, tự thấy rõ",       # bỏ «dần» — nhãn thể trá hình
    "разбираться": "am hiểu, thông thạo, hiểu thấu, xử lý",  # thiếu figure out / sort out
    "разобраться": "hiểu ra, hiểu thấu, xử lý",             # bỏ «xong» — nhãn thể trá hình
    "беда": "tai họa, chuyện bất hạnh, rắc rối",            # thiếu trouble/problem
    "ощущение": "cảm giác, cảm nhận",                       # tách khỏi чувство (sensation/perception)
    "одинокий": "cô đơn, lẻ loi, độc thân",                 # thiếu single/unattached
}

# --------------------------------------------------------------------- выяснить
S["выяснить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">RA ngoài</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ясн-</span>'
    '<span class="hd-gloss">RÕ, SÁNG — gốc của <b>я́сный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть</span>'
    '<span class="hd-gloss">đuôi lớp chia 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho RÕ RA ⇒ tìm ra, làm sáng tỏ. Như mọi động từ HT có <b>вы-</b>, '
    'trọng âm nhảy lên <b>вы́</b> ở mọi dạng: <b>вы́ясню</b>, <b>вы́яснил</b>. '
    'Cặp CHT: <b>выясня́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>я́сный</b> rõ, trong sáng · <b>я́сно</b> rõ rồi · '
    '<b>объясни́ть</b> giải thích · <b>выясня́ть</b> (CHT)</div>'
)

# --------------------------------------------------------------------- выяснять
S["выяснять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">RA ngoài</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ясн-</span>'
    '<span class="hd-gloss">RÕ — gốc của <b>я́сный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>выясня́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">CHT của <b>вы́яснить</b>: <b>-ить</b> → <b>-я́ть</b>, như '
    '<b>прове́рить</b> → <b>проверя́ть</b>. Khác bản HT, trọng âm nằm ở đuôi, không lên '
    '<b>вы-</b>.</div>'
    '<div class="hd-warn"><b>выясня́ть отноше́ния</b> — cãi cho ra nhẽ, «nói chuyện phải trái» '
    'với ai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>я́сный</b> rõ · <b>я́сно</b> rõ rồi · '
    '<b>объясня́ть</b> giải thích · <b>вы́яснить</b> (HT)</div>'
)

# --------------------------------------------------------------------- воля
S["воля"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вол-</span>'
    '<span class="hd-gloss">Ý MUỐN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-я</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Ấn–Âu với Anh <i>will</i>, <i>voluntary</i>. Ý muốn của mình ⇒ '
    'ý chí; được sống theo ý muốn ⇒ tự do.</div>'
    '<div class="hd-warn"><b>си́ла во́ли</b> — sức mạnh ý chí, nghị lực.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>позво́лить</b> cho phép (<b>по-з-вол-</b>) · <b>дово́льный</b> hài lòng · '
    '<b>доброво́льный</b> tự nguyện · <b>во́льный</b> tự do</div>'
)

# --------------------------------------------------------------------- убедиться
S["убедиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">убеди́-</span>'
    '<span class="hd-gloss">THUYẾT PHỤC — <b>убеди́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">chính mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thuyết phục được CHÍNH MÌNH ⇒ tin chắc; muốn tin chắc thì phải kiểm ⇒ '
    'kiểm chứng. Điều được kiểm: <b>в</b> + cách 6 (<b>убеди́ться в э́том</b>) hoặc mệnh đề '
    '<b>что</b>. Cặp CHT: <b>убежда́ться</b>.</div>'
    '<div class="hd-warn">Ngôi «tôi» đổi <b>д → ж</b> (<b>убежу́сь</b>) nhưng gần như không ai '
    'nói, y như <b>убеди́ть</b>. Hay dùng quá khứ: <b>Я убеди́лся, что он прав.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>убеди́ть</b> thuyết phục · <b>убежде́ние</b> niềm tin vững chắc · '
    '<b>убеди́тельный</b> có sức thuyết phục</div>'
)

# --------------------------------------------------------------------- убеждаться
S["убеждаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">убежда́-</span>'
    '<span class="hd-gloss">THUYẾT PHỤC (CHT) — <b>убежда́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">chính mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">CHT của <b>убеди́ться</b>: <b>д → жд</b> khi sang <b>-а́ть</b>, đúng như '
    '<b>победи́ть</b> → <b>побежда́ть</b>. Chia đều: <b>убежда́юсь</b>. Hay dùng cho việc thấy đi '
    'thấy lại: <b>Я не раз убежда́лся, что…</b> — tôi nhiều lần đã thấy rõ rằng…</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>убеди́ться</b> (HT) · <b>убежда́ть</b> thuyết phục · '
    '<b>убежде́ние</b> niềm tin vững chắc</div>'
)

# --------------------------------------------------------------------- разбираться
S["разбираться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span>'
    '<span class="hd-gloss">TÁCH RA nhiều phía</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бир-</span>'
    '<span class="hd-gloss">gốc LẤY — cùng gốc <b>брать</b> (<b>бр/бир/бер</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть-ся</span>'
    '<span class="hd-gloss">đuôi CHT + phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lấy tách từng mảnh ra xem ⇒ hiểu tận gốc ⇒ am hiểu. Mẫu '
    '<b>-бира́ть</b> (CHT) ↔ <b>-бра́ть</b> (HT) như <b>собира́ть / собра́ть</b>; '
    'cặp HT: <b>разобра́ться</b>.</div>'
    '<div class="hd-warn">Am hiểu VỀ cái gì: <b>в</b> + cách 6 — <b>Я не о́чень разбира́юсь '
    'в литерату́ре.</b> Tôi không rành văn học lắm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>брать</b> lấy · <b>разбира́ть</b> tháo rời, phân tích · '
    '<b>выбира́ть</b> chọn · <b>собира́ть</b> gom · <b>разбо́р</b> sự phân tích</div>'
)

# --------------------------------------------------------------------- разобраться
S["разобраться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">разо-</span>'
    '<span class="hd-gloss">TÁCH RA — <b>раз-</b> chêm <b>о</b> trước cụm <b>бр</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-бр-</span>'
    '<span class="hd-gloss">gốc LẤY — cùng gốc <b>брать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть-ся</span>'
    '<span class="hd-gloss">đuôi HT + phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">HT của <b>разбира́ться</b>: tách ra xem hết ⇒ hiểu ra, xử lý xong. '
    'Chia y như <b>брать</b> (<b>беру́</b>): <b>разберу́сь</b>, <b>разберёшься</b>. '
    'Quá khứ giống cái nhấn đuôi: <b>разобрала́сь</b>.</div>'
    '<div class="hd-warn"><b>разобра́ться с</b> + cách 5 = xử lý (việc, người): '
    '<b>Я с э́тим разберу́сь.</b> Để tôi lo chuyện này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>брать</b> lấy · <b>разобра́ть</b> tháo rời (HT) · '
    '<b>собра́ть</b> gom (HT) · <b>вы́брать</b> chọn (HT)</div>'
)

# --------------------------------------------------------------------- беда
S["беда"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бед-</span>'
    '<span class="hd-gloss">TAI ƯƠNG, khốn khổ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người gặp <b>беда́</b> là người <b>бе́дный</b> — tội nghiệp, rồi nghèo. '
    'Số ít nhấn đuôi, số nhiều nhấn gốc: <b>беда́</b> → <b>бе́ды</b>.</div>'
    '<div class="hd-warn"><b>Не беда́!</b> — Không sao đâu! · <b>на беду́</b> — không may thay.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бе́дный</b> nghèo, tội nghiệp · <b>бе́дность</b> sự nghèo khó · '
    '<b>бе́дствие</b> thảm hoạ (<b>стихи́йное бе́дствие</b> thiên tai)</div>'
)

# --------------------------------------------------------------------- поведение
S["поведение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, không mang nghĩa riêng ở đây</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вед-</span>'
    '<span class="hd-gloss">DẪN — gốc của <b>вести́</b> (<b>веду́</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cách mình «dẫn» chính mình: danh từ của <b>вести́ себя́</b> «cư xử» '
    '(đã gặp ở thẻ <b>вести́</b>) ⇒ hành vi, cách ứng xử.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вести́ себя́</b> cư xử · <b>вести́</b> dẫn · <b>води́ть</b> dẫn (nhiều '
    'chiều) · <b>веду́щий</b> người dẫn chương trình</div>'
)

# --------------------------------------------------------------------- ощущение
S["ощущение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ощущ-</span>'
    '<span class="hd-gloss">CẢM THẤY — <b>ощути́ть</b>, <b>т → щ</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>ощути́ть</b> «cảm thấy (bằng giác quan)»; <b>т</b> hoá '
    '<b>щ</b> trước <b>-ение</b>, như <b>возврати́ть</b> → <b>возвраще́ние</b>. Khác '
    '<b>чу́вство</b>: <b>ощуще́ние</b> là cái da thịt, giác quan báo về (lạnh, đau) hoặc «có cảm '
    'giác rằng…»; còn yêu, giận là <b>чу́вство</b>.</div>'
    '<div class="hd-warn"><b>по мои́м ощуще́ниям</b> — theo cảm nhận của tôi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ощути́ть</b> cảm thấy (HT) · <b>ощуща́ть</b> cảm thấy (CHT)</div>'
)

# --------------------------------------------------------------------- доверие
S["доверие"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI mức</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вер-</span>'
    '<span class="hd-gloss">TIN — gốc của <b>ве́рить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ие</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tin TỚI MỨC dám giao việc, giao bí mật cho ai ⇒ lòng tin. Danh từ của '
    '<b>дове́рить</b> / <b>доверя́ть</b>.</div>'
    '<div class="hd-warn">Lòng tin VÀO ai: <b>к</b> + cách 3 — <b>дове́рие к нему́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ве́рить</b> tin · <b>доверя́ть</b> tin cậy · <b>дове́рить</b> giao phó · '
    '<b>недове́рие</b> sự ngờ vực</div>'
)

# --------------------------------------------------------------------- одинокий
S["одинокий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">один-</span>'
    '<span class="hd-gloss">MỘT — <b>оди́н</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́к-ий</span>'
    '<span class="hd-gloss">đuôi tính từ (mang trọng âm)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỉ có MỘT mình ⇒ cô đơn, lẻ loi; nói về người còn là sống một mình, '
    'không có đôi: <b>одино́кая же́нщина</b>. Trọng âm rời <b>оди́н</b> sang <b>-о́к-</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оди́н</b> một · <b>одино́чество</b> sự cô đơn · '
    '<b>одино́чка</b> người đơn độc (<b>мать-одино́чка</b> mẹ đơn thân)</div>'
)

# --------------------------------------------------------------------- влюблённый
S["влюблённый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-любл-</span>'
    '<span class="hd-gloss">YÊU — <b>люби́ть</b>, chêm <b>л</b> như <b>люблю́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ённый</span>'
    '<span class="hd-gloss">đuôi phân từ «đã bị…»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đã rơi VÀO yêu» ⇒ đang yêu. Là phân từ của <b>влюби́ться</b> «phải '
    'lòng».</div>'
    '<div class="hd-warn">Làm vị ngữ thì dùng dạng ngắn, nhấn đuôi: <b>влюблён</b> · '
    '<b>влюблена́</b> · <b>влюблены́</b>. Yêu AI: <b>в</b> + cách 4 — <b>Он влюблён в неё.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>люби́ть</b> yêu · <b>влюби́ться</b> phải lòng · <b>любо́вь</b> tình yêu · '
    '<b>люби́мый</b> yêu thích</div>'
)

# --------------------------------------------------------------------- благодарный
S["благодарный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">благо-</span>'
    '<span class="hd-gloss">ĐIỀU TỐT LÀNH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дар-</span>'
    '<span class="hd-gloss">MÓN QUÀ — gốc của <b>дари́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tính từ của <b>благодари́ть</b> «cảm ơn» ⇒ biết ơn. Trọng âm đứng yên ở '
    '<b>-да́-</b>.</div>'
    '<div class="hd-warn">Câu dùng nhiều nhất là dạng ngắn, giống đực chêm <b>е</b>: <b>Я вам '
    'о́чень благода́рен</b> (nữ: <b>благода́рна</b>) <b>за по́мощь.</b> Người ở cách 3, lý do '
    '<b>за</b> + cách 4.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>благодари́ть</b> cảm ơn · <b>благода́рность</b> lòng biết ơn · '
    '<b>благодаря́</b> nhờ có · <b>пода́рок</b> món quà</div>'
)

# --------------------------------------------------------------------- одиночество
S["одиночество"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">одино́ч-</span>'
    '<span class="hd-gloss">CÔ ĐƠN — <b>одино́кий</b>, <b>к → ч</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ество</span>'
    '<span class="hd-gloss">→ danh từ trừu tượng, giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>одино́кий</b>: <b>к</b> hoá <b>ч</b> trước <b>-ество</b>, '
    'đúng như <b>челове́к</b> → <b>челове́чество</b> nhân loại. Gốc sâu nhất là <b>оди́н</b> '
    '«một».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>одино́кий</b> cô đơn · <b>оди́н</b> một · '
    '<b>одино́чка</b> người đơn độc</div>'
)

# --------------------------------------------------------------------- ужас
S["ужас"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Coi như gốc trơn — chính <b>у́жас</b> là gốc của cả họ '
    '<b>ужа́сный</b>, <b>ужа́сно</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trọng âm ở danh từ nằm đầu <b>у́-</b>, sang tính từ và trạng từ thì dời '
    'về <b>-жа́-</b>: <b>у́жас</b> → <b>ужа́сный</b>, <b>ужа́сно</b>.</div>'
    '<div class="hd-warn">Dùng như câu cảm thán: <b>У́жас!</b> / <b>Како́й у́жас!</b> — Kinh khủng '
    'quá! · <b>в у́жасе</b> — hoảng hồn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ужа́сный</b> kinh khủng · <b>ужа́сно</b> khủng khiếp, cực kỳ · '
    '<b>ужасну́ться</b> hoảng sợ</div>'
)

# --------------------------------------------------------------------- ответственность
S["ответственность"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ответ-</span>'
    '<span class="hd-gloss">TRẢ LỜI — <b>отве́т</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ствен-н-</span>'
    '<span class="hd-gloss">→ tính từ <b>отве́тственный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span>'
    '<span class="hd-gloss">→ danh từ trừu tượng, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Phải TRẢ LỜI cho việc mình làm ⇒ trách nhiệm. Y hệt Anh: '
    '<i>respond</i> → <i>responsible</i> → <i>responsibility</i>.</div>'
    '<div class="hd-warn">Chịu trách nhiệm VỀ: <b>за</b> + cách 4 — <b>нести́ отве́тственность '
    'за ребёнка</b>, cũng như <b>отвеча́ть за</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отве́т</b> câu trả lời · <b>отве́тить</b> trả lời · '
    '<b>отве́тственный</b> có trách nhiệm · <b>отве́тный</b> đáp lại</div>'
)

# --------------------------------------------------------------------- личность
S["личность"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">лич-</span>'
    '<span class="hd-gloss">MẶT — <b>лицо́</b>, <b>ц → ч</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span>'
    '<span class="hd-gloss">của <b>ли́чный</b> «cá nhân»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span>'
    '<span class="hd-gloss">→ danh từ trừu tượng, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái làm nên «gương mặt riêng» của một người ⇒ nhân cách, cá tính; rồi '
    'chính con người cá nhân đó.</div>'
    '<div class="hd-warn"><b>удостовере́ние ли́чности</b> — giấy tờ tuỳ thân.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лицо́</b> mặt · <b>ли́чный</b> cá nhân · <b>ли́чно</b> đích thân</div>'
)

# --------------------------------------------------------------------- доверить
S["доверить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI mức</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вер-</span>'
    '<span class="hd-gloss">TIN — gốc của <b>ве́рить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть</span>'
    '<span class="hd-gloss">đuôi lớp chia 2: <b>дове́рю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tin TỚI MỨC giao cho ⇒ giao phó; giao điều thầm kín ⇒ phó thác, tâm sự. '
    'Cặp CHT: <b>доверя́ть</b>.</div>'
    '<div class="hd-warn">Giao CHO ai (cách 3) CÁI gì (cách 4): <b>дове́рить ему́ ключи́</b> — '
    'giao chìa khoá cho anh ấy.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ве́рить</b> tin · <b>дове́рие</b> lòng tin · <b>доверя́ть</b> (CHT)</div>'
)

# --------------------------------------------------------------------- доверять
S["доверять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI mức</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вер-</span>'
    '<span class="hd-gloss">TIN — gốc của <b>ве́рить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>доверя́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">CHT của <b>дове́рить</b>: <b>-ить</b> → <b>-я́ть</b>, như '
    '<b>прове́рить</b> → <b>проверя́ть</b>. Tin ai tới mức dám giao việc ⇒ tin cậy.</div>'
    '<div class="hd-warn">Tin AI: cách 3 — <b>Я тебе́ доверя́ю.</b> Nghĩa «tin» này chỉ có ở CHT; '
    '<b>дове́рить</b> luôn cần thứ được giao: <b>дове́рить ему́ та́йну</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ве́рить</b> tin · <b>дове́рие</b> lòng tin · '
    '<b>недове́рие</b> sự ngờ vực</div>'
)

B = {
    "docbangmat": 98,
    "loitubat": 1,
    "nguonsai": 2,
    "baolen": [
        "V CHƯA đo va chạm lại: script đọc thẻ để mô phỏng do_va_cham với V mới bị chặn quyền — luồng chính cần chạy `vacham` sau khi áp V. Đã cố ý tránh «ấn tượng» cho ощущение (sợ nuốt впечатление cùng n NEUT) và chỉ thêm «cảm nhận».",
        "V cặp thể trùng nguyên văn, chỉ badge thể tách: выяснить = выяснять «tìm ra, làm rõ, làm sáng tỏ» · убедиться = убеждаться «tin chắc, kiểm chứng, tự thấy rõ». Cặp разбираться/разобраться cố ý KHÁC: chỉ разбираться có «am hiểu, thông thạo» (nghĩa riêng CHT).",
        "ответственность giữ nguyên «trách nhiệm» theo khai của luồng chính (обязанность ở k163 sẽ đổi sang «nghĩa vụ, bổn phận»).",
        "Nguồn sai bác (2): разобраться BAT THUONG ghi thân hiện tại «không suy được, phải nhớ riêng» — thật ra chia y như брать (беру́ → разберу́сь), thẻ dạy theo đó. благодарный BAT THUONG ghi «trọng âm dịch / thêm nguyên âm» — trọng âm KHÔNG dịch (благода́рен, благода́рна), chỉ chêm е đúng quy tắc; thẻ chỉ nói phần chêm е.",
        "Cố ý KHÔNG dùng: беда ← побе́да (máy ghép chuỗi). Theo từ nguyên (Vasmer) có thể cùng gốc cổ với побе́да/убеди́ть, nhưng phải tốn một ô ⚠️ Mức tin; thay bằng họ chắc chắn бе́дный/бе́дность/бе́дствие. убедиться/убеждаться chẻ theo убеди́ть + -ся, không chẻ lại -бед-.",
        "Không chắc hẳn (đã kiểm theo hiểu biết, không có từ điển trong tay): доверять — câu «nghĩa «tin ai» chỉ có ở CHT, дове́рить luôn cần thứ được giao» (HT tương ứng của «tin» là довери́ться, không nêu trên thẻ) · убедиться — ngôi «tôi» убежу́сь «gần như không ai nói», chép theo khuôn thẻ убеди́ть · воля ↔ Anh will/voluntary cùng gốc Ấn–Âu (từ nguyên phổ biến, không đặt Mức tin).",
        "Lỗi tự bắt (1): định lấy ví dụ т→щ «защити́ть → защище́ние» — danh từ thật là защи́та, đổi sang возврати́ть → возвраще́ние.",
    ],
}
