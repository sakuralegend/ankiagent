# -*- coding: utf-8 -*-
"""k141 — language::education: từ trường đại học + vài từ chỉ hướng, chỉ suy luận.

Chỗ cần nhất quán trong lô:
(1) gốc лёт-/лет- = BAY (улетать/улететь) — khớp лётчик (k139), лететь/полететь/самолёт (cũ);
    у- = rời đi, bay MẤT; по- = BẮT ĐẦU bay.
(2) gốc ез-/езд- = ĐI BẰNG XE (проезжать/проехать) — tách khỏi пройти/переходить (đi bộ).
(3) gốc след- = DẤU VẾT (следовательно, исследовать) — khớp следующий/последний (cũ).
(4) отметка ↔ оценка (cũ) ↔ пятёрка (k142): trường nghĩa điểm số ở trường.
Họ hàng cố ý vắng: бланк, семестр (từ mượn đứng một mình).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "каков": "ra sao",                          # RÚT «thế nào» — trùng како́й (đã nạp)
    "отметка": "dấu ghi, điểm chấm bài",        # bỏ ngoặc; «điểm» trùng то́чка, «điểm số» trùng оце́нка
    "проезжать": "đi xe qua, đi quá trạm",      # bỏ ngoặc; «đi qua» trùng переходи́ть; gloss drive past / miss one's stop
    "проехать": "đi xe qua, đi quá trạm",       # bỏ ngoặc; «đi qua» trùng пройти́; gloss drive past / overshoot
    "путешественник": "nhà du hành",            # RÚT «người đi du lịch» — trùng тури́ст (đã nạp)
    "улетать": "bay đi, bay mất",               # bỏ «(lặp lại, đang diễn ra)» — nhãn thể trá hình
    "улететь": "bay mất",                       # RÚT «bay đi» — trùng полете́ть (đã nạp)
}

# ----------------------------------------------------------------- негде
S["негде"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не́-</span>'
    '<span class="hd-gloss">KHÔNG CÓ (mang trọng âm)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-где</span>'
    '<span class="hd-gloss">ở đâu</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Không có đâu» ⇒ không có chỗ nào (để làm gì). Người cần chỗ đứng '
    'cách 3, việc đứng nguyên thể: <b>Мне не́где жить.</b> Tôi không có chỗ ở.</div>'
    '<div class="hd-warn"><b>не́где</b> + nguyên thể, KHÔNG cần <b>не</b> · <b>нигде́</b> = '
    'không ở đâu cả, PHẢI có <b>не</b>: <b>Я нигде́ не был.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>не́куда</b> không có chỗ nào để đi tới · <b>не́когда</b> không có '
    'thời gian · <b>нигде́</b> không ở đâu cả</div>'
)

# ----------------------------------------------------------------- навстречу
S["навстречу"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">hướng VÀO, về phía</span></div>'
    '<div class="hd-row"><span class="hd-piece">-встре́ч-</span>'
    '<span class="hd-gloss">cuộc gặp — <b>встре́ча</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-у</span>'
    '<span class="hd-gloss">đuôi cách 4 đã đông cứng thành trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Hướng vào cuộc gặp» ⇒ đi về phía người đang tới, ra đón: '
    '<b>Она́ вы́шла навстре́чу го́стю.</b></div>'
    '<div class="hd-warn">Người được đón đứng <b>cách 3</b>: <b>навстре́чу дру́гу</b>. '
    'Cụm <b>идти́ навстре́чу</b> (кому́) còn là «chiều theo, nhượng bộ».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>встре́ча</b> cuộc gặp · <b>встреча́ть</b> gặp, đón · '
    '<b>встре́тить</b> gặp, đón</div>'
)

# ----------------------------------------------------------------- путешественник
S["путешественник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пут-</span>'
    '<span class="hd-gloss">ĐƯỜNG — <b>пу́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е-ше́ств-</span>'
    '<span class="hd-gloss">bước đi (như <b>ше́ствие</b> đoàn diễu hành)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-енник</span>'
    '<span class="hd-gloss">→ NGƯỜI làm việc đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người bước trên đường dài» ⇒ người đi <b>путеше́ствие</b>, '
    'nhà du hành.</div>'
    '<div class="hd-warn"><b>тури́ст</b> = khách du lịch đi tham quan · '
    '<b>путеше́ственник</b> = người chu du, đi xa khám phá (Marco Polo).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>путеше́ствие</b> chuyến du lịch · <b>путеше́ствовать</b> đi du lịch · '
    '<b>пу́ть</b> con đường · <b>попу́тчик</b> bạn đồng hành</div>'
)

# ----------------------------------------------------------------- проезжать
S["проезжать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">QUA — xuyên qua, lướt ngang qua</span></div>'
    '<div class="hd-row"><span class="hd-piece">-езж-</span>'
    '<span class="hd-gloss">gốc ĐI BẰNG XE (như <b>приезжа́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành, chia đều: <b>проезжа́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đi xe qua (cạnh, xuyên qua một nơi). Cặp hoàn thành: '
    '<b>прое́хать</b>.</div>'
    '<div class="hd-warn">Gốc quyết định phương tiện: <b>проезжа́ть</b> = đi XE qua · '
    '<b>проходи́ть</b> = đi BỘ qua.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>е́хать</b> đi xe · <b>приезжа́ть</b> đến nơi bằng xe · '
    '<b>переезжа́ть</b> chuyển nhà · <b>прое́зд</b> việc đi lại, lối đi · '
    '<b>по́езд</b> tàu hoả</div>'
)

# ----------------------------------------------------------------- проехать
S["проехать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">QUA — và cả «QUÁ, lố»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́хать</span>'
    '<span class="hd-gloss">đi xe — <b>е́хать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hoàn thành của <b>проезжа́ть</b>. Chia y như <b>е́хать</b>: thân đổi '
    'sang <b>-ед-</b> — <b>прое́ду, прое́дешь</b>.</div>'
    '<div class="hd-warn"><b>прое́хать остано́вку</b> = đi lố trạm (про- = QUÁ chỗ cần xuống).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>проезжа́ть</b> cặp chưa hoàn thành · <b>прое́зд</b> việc đi lại · '
    '<b>уе́хать</b> đi khỏi bằng xe · <b>прие́хать</b> đến nơi bằng xe</div>'
)

# ----------------------------------------------------------------- улетать
S["улетать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">RỜI ĐI, khỏi chỗ (như <b>уйти́</b>, <b>уе́хать</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лет-</span>'
    '<span class="hd-gloss">gốc BAY — <b>лета́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành, chia đều: <b>улета́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bay rời khỏi đây. Cặp hoàn thành: <b>улете́ть</b>. '
    'Kiểu <b>Пти́цы улета́ют на юг.</b> Chim bay về phương nam.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лета́ть</b>/<b>лете́ть</b> bay · <b>прилета́ть</b> bay đến · '
    '<b>самолёт</b> máy bay · <b>лётчик</b> phi công</div>'
)

# ----------------------------------------------------------------- улететь
S["улететь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">RỜI ĐI, khỏi chỗ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лете́ть</span>'
    '<span class="hd-gloss">bay — <b>лете́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hoàn thành của <b>улета́ть</b>: bay đi rồi, không còn ở đây. Chia y như '
    '<b>лете́ть</b>: <b>т → ч</b> ở ngôi «я» — <b>улечу́</b>, nhưng <b>улети́шь</b>.</div>'
    '<div class="hd-warn"><b>полете́ть</b> = BẮT ĐẦU bay, cất cánh · <b>улете́ть</b> = bay '
    'MẤT, đã rời khỏi chỗ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>улета́ть</b> cặp chưa hoàn thành · <b>полете́ть</b> bắt đầu bay · '
    '<b>прилете́ть</b> bay đến · <b>лётчик</b> phi công</div>'
)

# ----------------------------------------------------------------- каков
S["каков"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">как-</span>'
    '<span class="hd-gloss">thế nào — <b>ка́к</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́в</span>'
    '<span class="hd-gloss">đuôi DẠNG NGẮN của <b>како́й</b> (như <b>тако́в</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dạng ngắn của <b>како́й</b>, đổi đuôi theo giống: '
    '<b>како́в, какова́, каково́, каковы́</b>.</div>'
    '<div class="hd-warn">Chỉ đứng làm VỊ NGỮ, danh từ theo sau ở cách 1: '
    '<b>Како́в результа́т?</b> Kết quả ra sao? — không đặt trước danh từ như <b>како́й</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>како́й</b> nào, như thế nào · <b>тако́в</b> là như thế · '
    '<b>ка́к</b> thế nào</div>'
)

# ----------------------------------------------------------------- следовательно
S["следовательно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сле́д-</span>'
    '<span class="hd-gloss">DẤU VẾT — <b>сле́д</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-</span>'
    '<span class="hd-gloss">→ động từ <b>сле́довать</b> đi theo</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тельно</span>'
    '<span class="hd-gloss">→ đuôi trạng từ (như <b>обяза́тельно</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Theo sau mà ra» ⇒ do đó, vậy nên — điều tiếp theo suy ra từ điều '
    'trước. Giọng sách vở, lập luận; nói thường hay dùng <b>поэ́тому</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сле́довать</b> đi theo, nên · <b>сле́дующий</b> tiếp theo · '
    '<b>после́дний</b> cuối cùng · <b>иссле́довать</b> nghiên cứu</div>'
)

# ----------------------------------------------------------------- чей-то
S["чей-то"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">чей-</span>'
    '<span class="hd-gloss">của ai — <b>че́й</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-то</span>'
    '<span class="hd-gloss">«nào đó» — có thật nhưng không rõ là ai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỉ phần <b>че́й</b> đổi theo giống và cách, <b>-то</b> giữ nguyên: '
    '<b>чья́-то су́мка</b>, <b>чьё-то письмо́</b>, <b>чьи́-то ве́щи</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">cùng khuôn <b>-то</b>: <b>кто́-то</b> ai đó · <b>где́-то</b> ở đâu đó · '
    '<b>куда́-то</b> đi đâu đó</div>'
)

# ----------------------------------------------------------------- бланк
S["бланк"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ mượn (Pháp <i>blanc</i> «trắng»), không chẻ được. Cùng gốc tiếng Anh '
    '<i>blank form</i>: tờ in sẵn, chừa chỗ trắng để điền.</div>'
    '<div class="hd-warn"><b>запо́лнить бла́нк</b> = điền vào tờ mẫu đơn.</div>'
)

# ----------------------------------------------------------------- отметка
S["отметка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">tách ra, ghi riêng ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мет-</span>'
    '<span class="hd-gloss">DẤU — <b>ме́тка</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">→ danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái dấu ghi lại ⇒ ở trường là con điểm ghi vào sổ cho một bài. '
    'Số nhiều cách 2 chen <b>о</b>: <b>отме́ток</b>.</div>'
    '<div class="hd-warn">Cả hai đều là «điểm»: <b>отме́тка</b> nhấn con số GHI vào sổ · '
    '<b>оце́нка</b> nhấn sự ĐÁNH GIÁ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отме́тить</b> đánh dấu, ghi nhận · <b>ме́тка</b> dấu, nhãn · '
    '<b>заме́тить</b> nhận ra · <b>пятёрка</b> điểm 5</div>'
)

# ----------------------------------------------------------------- теоретический
S["теоретический"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">теорет-</span>'
    '<span class="hd-gloss">LÝ THUYẾT — <b>тео́рия</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ческий</span>'
    '<span class="hd-gloss">= tiếng Anh <i>-ical</i> → tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>theoretical</i>. Đuôi <b>-и́ческий</b> luôn mang trọng âm '
    'ở <b>и́</b>, nên trọng âm rời <b>тео́рия</b> mà dịch về sau.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тео́рия</b> lý thuyết · <b>теоре́тик</b> nhà lý thuyết · cùng đuôi: '
    '<b>практи́ческий</b> thực tiễn</div>'
)

# ----------------------------------------------------------------- атомный
S["атомный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">а́том-</span>'
    '<span class="hd-gloss">NGUYÊN TỬ — <b>а́том</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ный</span>'
    '<span class="hd-gloss">→ tính từ «thuộc về»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>atomic</i>; trọng âm giữ ở <b>а́</b> như <b>а́том</b>.</div>'
    '<div class="hd-warn"><b>а́томная ста́нция</b> = nhà máy điện hạt nhân.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>а́том</b> nguyên tử</div>'
)

# ----------------------------------------------------------------- декан
S["декан"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ mượn (Latin <i>decanus</i>), không chẻ được. Cùng gốc tiếng Anh '
    '<i>dean</i>; trọng âm ở cuối: <b>дека́н</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>декана́т</b> văn phòng khoa</div>'
)

# ----------------------------------------------------------------- семестр
S["семестр"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ mượn (Latin «sáu tháng»), không chẻ được — chính là <i>semester</i>, '
    'nhưng trọng âm ở giữa: <b>семе́стр</b>. Kỳ thứ nhất: <b>в пе́рвом семе́стре</b>.</div>'
)

# ----------------------------------------------------------------- исследовать
S["исследовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ис-</span>'
    '<span class="hd-gloss">RA (<b>из-</b> đổi thành <b>ис-</b> trước <b>с</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-след-</span>'
    '<span class="hd-gloss">DẤU VẾT — <b>сле́д</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-овать</span>'
    '<span class="hd-gloss">đuôi động từ: <b>-ова-</b> → <b>-у-</b>: <b>иссле́дую</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Lần theo dấu vết cho ra» ⇒ nghiên cứu, khảo sát. Đối tượng ở '
    'cách 4: <b>иссле́довать пробле́му</b>.</div>'
    '<div class="hd-warn">Một từ cho CẢ HAI thể — không có cặp; thể đọc theo ngữ cảnh.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>иссле́дование</b> công trình nghiên cứu · <b>иссле́дователь</b> nhà '
    'nghiên cứu · <b>сле́довать</b> đi theo · <b>сле́д</b> dấu vết</div>'
)

# ----------------------------------------------------------------- стипендия
S["стипендия"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ mượn (Latin <i>stipendium</i> «tiền lương»), không chẻ được. Cùng '
    'gốc tiếng Anh <i>stipend</i>. Ở Nga đây là khoản tiền trường trả hằng tháng cho sinh viên.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стипендиа́т</b> người nhận học bổng</div>'
)

# ----------------------------------------------------------------- консультация
S["консультация"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">консульт-</span>'
    '<span class="hd-gloss">hỏi ý kiến — <i>consult</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ция</span>'
    '<span class="hd-gloss">= tiếng Anh <i>-ation</i> → danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>consultation</i>. Ở trường đại học: buổi thầy giải đáp '
    'thắc mắc, nhất là ngay trước kỳ thi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>консульти́ровать</b> tư vấn · <b>консульта́нт</b> người tư vấn</div>'
)

# ----------------------------------------------------------------- báo cáo lô
B = {
    "docbangmat": 62,
    "loitubat": 4,   # не́где «câu không có động từ chia» (sai: Мне не́где бы́ло жить) · -тельно «từ tính từ -тельный» (không có tính từ đó) · mảnh «теоре́т-» mang dấu nhấn gây hiểu sai · че́й-то «chỉ đổi theo giống» (thiếu: cả cách)
    "nguonsai": 1,   # gloss Anh улетать «in one direction, toward a goal» là mô tả động từ chuyển động không tiền tố, không chép
    "baolen": [
        "отметка V='dấu ghi, điểm chấm bài': buộc THÊM chữ — «điểm» trùng то́чка, «điểm số» trùng оце́нка, badge không tách. Cần duyệt.",
        "проезжать/проехать V='đi xe qua, đi quá trạm': thêm «xe» để tách переходи́ть/пройти́ (rút gọn không gỡ được). Chưa soi được field переезжа́ть có trùng 'đi xe qua' không.",
        "каков V='ra sao' (rút «thế nào»): chưa biết field како́й có chứa 'ra sao' không — cache _vacham_vi.txt chỉ ghi cụm đã trùng.",
        "путешественник V='nhà du hành': chưa soi được космона́вт (nếu có thẻ) có 'nhà du hành' trơn không.",
        "улетать V giữ 'bay đi, bay mất' — trùng полете́ть ở 'bay đi' nhưng badge THỂ tách; улететь rút còn 'bay mất'.",
        "исследовать là động từ HAI THỂ — thẻ ghi 'một từ cho cả hai thể'; cần xem AspectBadge của thẻ in đúng chưa.",
        "Không chắc tuyệt đối: путеше́ственник chẻ пут- + ше́ствие (từ nguyên chuẩn theo Vasmer, nhưng là từ nguyên, không phải luật suy ra).",
    ],
}
