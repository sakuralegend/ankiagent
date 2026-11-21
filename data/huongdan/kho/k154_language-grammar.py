# -*- coding: utf-8 -*-
"""k154 — language::grammar: hư từ, đại từ -то/кое-/ни-, danh từ trừu tượng, tính từ thời gian.

Chỗ cần nhất quán trong lô:
(1) да́нный / да́нные = một khuôn: да- CHO (gốc của дать) + -нн- «đã được…»; да́нные là да́нный
    danh từ hoá, số nhiều — y hệt Latin data «những thứ được cho».
(2) ка́к-то, кое-что́, ничто́ chung một bộ phận: đại từ hỏi + mảnh chỉ «loại» (-то, кое-, ни-),
    khớp что́-то (k111), ничего́ (k17).
(3) поско́льку dựa thẳng vào khuôn к-/т- của ско́лько (k31): поско́льку ↔ посто́льку.
(4) скор- NHANH khớp ско́ро (k86); сто- ĐỨNG khớp стоя́ть (k03), настоя́щий (k40);
    -чёт ĐẾM khớp счёт (k57), счита́ть (k112); век → ве́чный (к → ч) khớp век (k93).
Họ hàng cố ý vắng: бу́дто, гора́здо (hư từ), о́ба (số từ), па́ра (từ mượn đứng một mình).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "как-то": "bằng cách nào đó, có lần, hôm nọ",       # bỏ «có lần» (trùng одна́жды k109); «hôm nọ» = gloss «the other day»
    "кое-что": "một điều gì đó",                # bỏ ngoặc «(đó)»
    "ничто": "không cái gì, hư vô",             # «không gì cả» trùng ничего́ (k17); «hư vô» = gloss «nought»
    "пара": "đôi, cặp đôi, vài, tiết học",      # «cặp» trùng су́мка (k20); gloss «couple / a few / class (at university)»
    "гораздо": "vượt xa, hơn hẳn",            # bỏ «...» (ghi chú cách dùng) — VẪN trùng намно́го, xem B
    "данный": "này, đã cho",                    # bỏ «hiện tại» (trùng настоя́щий k40); «;» → «,»
    "постоянный": "liên tục, thường xuyên, lâu dài",   # «;» → «,»
    "вечный": "vĩnh cửu, triền miên",           # «;» → «,»
    "скорый": "nhanh, gấp, sắp tới, tốc hành",     # bỏ «nhanh» (trùng бы́стрый k42); gloss «near / forthcoming / express (train)»
}

# ----------------------------------------------------------------- как-то
S["как-то"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">как</span>'
    '<span class="hd-gloss">thế nào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-то</span>'
    '<span class="hd-gloss">«… nào đó» — có thật, chỉ là không biết hoặc không nói ra</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Theo cách nào đó» ⇒ <b>bằng cách nào đó</b>: <b>Он ка́к-то сде́лал э́то</b>. '
    'Dời sang thời gian ⇒ một lần nào đó trong quá khứ: <b>ка́к-то раз</b> = có một lần, hôm nọ. '
    'Trọng âm nằm ở <b>как</b>. So với <b>ка́к-нибудь</b>: xem thẻ <b>кто́-то</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>как</b> thế nào · <b>что́-то</b> cái gì đó · <b>кто́-то</b> ai đó · '
    '<b>когда́-то</b> từng có thời</div>'
)

# ----------------------------------------------------------------- будто
S["будто"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Hư từ, không chẻ ra mảnh mang nghĩa riêng được.</div>'
    '<div class="hd-warn">⚠️ Mức tin: theo từ nguyên nó là <b>будь</b> (mệnh lệnh của <b>быть</b>) + <b>то</b> '
    '= «cứ cho là thế» — đó là chuyện lịch sử, không phải luật suy ra được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thường đi đôi thành <b>как бу́дто</b> = như thể: '
    '<b>Он смо́трит, как бу́дто всё зна́ет</b>. '
    'Đứng sau động từ nói thì nó mang thêm nghi ngờ: <b>Он говори́т, бу́дто был там</b> = '
    'anh ta bảo là đã ở đó (người nói không tin lắm) — khác hẳn <b>что</b> trung tính.</div>'
)

# ----------------------------------------------------------------- кое-что
S["кое-что"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кое-</span>'
    '<span class="hd-gloss">người nói BIẾT là cái gì, chỉ chưa nói ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">что</span>'
    '<span class="hd-gloss">cái gì</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>Я тебе́ кое-что́ купи́л</b> = Anh mua cho em một thứ (anh biết là gì, để dành bất ngờ). '
    'Còn <b>что́-то</b> là thứ chính người nói cũng không biết: <b>Там что́-то упа́ло</b>. '
    'Chỉ phần <b>что</b> biến cách: <b>кое-чего́</b>.</div>'
    '<div class="hd-warn">Có giới từ thì nó chen vào GIỮA và gạch nối biến mất: '
    'кое <b>о чём</b>, кое <b>с чем</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>что</b> cái gì · <b>что́-то</b> cái gì đó · <b>кое-кто́</b> có người · '
    '<b>кое-где́</b> đây đó · <b>кое-ка́к</b> qua loa</div>'
)

# ----------------------------------------------------------------- ничто
S["ничто"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ни-</span>'
    '<span class="hd-gloss">phủ định: không một… nào</span></div>'
    '<div class="hd-row"><span class="hd-piece">что</span>'
    '<span class="hd-gloss">cái gì — ở cách 1</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là dạng CHỦ NGỮ: <b>Ничто́ не ве́чно</b> = Không gì là mãi mãi. '
    'Làm tân ngữ sau động từ phủ định thì dùng cách 2 <b>ничего́</b>: <b>Я ничего́ не зна́ю</b>. '
    'Vẫn phải có <b>не</b> trước động từ — phủ định hai lần là bắt buộc.</div>'
    '<div class="hd-warn">Có giới từ thì <b>ни</b> tách ra, giới từ chen giữa: '
    '<b>ни о чём</b> (không về chuyện gì), <b>ни с чем</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ничего́</b> không gì cả · <b>никто́</b> không ai · <b>никогда́</b> không bao giờ · '
    '<b>что</b> cái gì</div>'
)

# ----------------------------------------------------------------- поскольку
S["поскольку"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">theo, đến mức</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ско́льку</span>'
    '<span class="hd-gloss">dạng cũ của <b>ско́лько</b> bao nhiêu</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen «theo chừng mực bao nhiêu». Đổi к- thành т- như ở <b>ско́лько ↔ сто́лько</b> '
    'ra cặp <b>посто́льку, поско́льку</b> = trong chừng mực mà. Dùng hằng ngày thì nó là «vì» '
    'của văn viết, nêu một lý do ai cũng đã biết.</div>'
    '<div class="hd-warn"><b>поско́льку</b> đứng ĐẦU câu được: <b>Поско́льку шёл дождь, мы оста́лись до́ма</b>. '
    '<b>потому́ что</b> thì phải đứng sau mệnh đề chính.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ско́лько</b> bao nhiêu · <b>сто́лько</b> bấy nhiêu · <b>не́сколько</b> một vài</div>'
)

# ----------------------------------------------------------------- лишь
S["лишь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Hư từ, không chẻ được. Từ nguyên: cùng gốc <b>ли́шний</b> «thừa» — '
    '«chỉ thế thôi, ngoài ra là thừa».</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa như <b>то́лько</b>, nhưng giọng văn viết, trang trọng hơn: '
    '<b>Э́то лишь нача́ло</b> = Đây chỉ mới là khởi đầu. <b>всего́ лишь</b> = vẻn vẹn chỉ.</div>'
    '<div class="hd-warn"><b>лишь бы</b> = miễn là: <b>Лишь бы ты был здоро́в</b> = Miễn là con khoẻ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ли́шний</b> thừa · <b>лиши́ть</b> tước đi</div>'
)

# ----------------------------------------------------------------- данные
S["данные"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">да́нн-</span>'
    '<span class="hd-gloss">= <b>да́нный</b> «đã được cho», gốc <b>да-</b> của <b>дать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ые</span>'
    '<span class="hd-gloss">đuôi tính từ số nhiều, dùng làm danh từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Những thứ đã được cho» — y hệt <i>data</i> tiếng Anh, vốn là Latin «những cái được cho». '
    'Vì là tính từ danh từ hoá nên chia đuôi tính từ và luôn số nhiều: '
    '<b>ба́за да́нных</b> = cơ sở dữ liệu.</div>'
    '<div class="hd-warn"><b>по да́нным</b> + cách 2 = theo số liệu của: '
    '<b>по да́нным мини́стерства</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>да́нный</b> này, đã cho · <b>дать</b> cho · <b>дава́ть</b> cho · <b>зада́ча</b> bài toán</div>'
)

# ----------------------------------------------------------------- данный
S["данный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">да-</span>'
    '<span class="hd-gloss">CHO — gốc của <b>дать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-нн-ый</span>'
    '<span class="hd-gloss">«đã được …» — đuôi phân từ bị động</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đã được cho» ⇒ cái đang được đưa ra bàn ⇒ <b>này</b>: '
    '<b>в да́нном слу́чае</b> = trong trường hợp này, <b>на да́нный моме́нт</b> = lúc này. '
    'Dạng ngắn dồn trọng âm ra đuôi: <b>дан · дана́ · дано́ · даны́</b> — đầu đề toán viết <b>Дано́:</b> = Cho:.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>да́нные</b> dữ liệu · <b>дать</b> cho · <b>дава́ть</b> cho · <b>зада́ть</b> giao (bài)</div>'
)

# ----------------------------------------------------------------- список
S["список"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">từ (bản gốc) ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пис-</span>'
    '<span class="hd-gloss">VIẾT — gốc của <b>писа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ок</span>'
    '<span class="hd-gloss">đuôi danh từ giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc là bản CHÉP ra từ <b>списа́ть</b> (chép lại); thứ hay được chép ra nhất là '
    'các tên người ⇒ danh sách. Nguyên âm <b>о</b> rơi khi thêm đuôi: <b>спи́ска</b>, <b>в спи́ске</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>писа́ть</b> viết · <b>списа́ть</b> chép lại · <b>записа́ть</b> ghi lại · '
    '<b>за́пись</b> bản ghi</div>'
)

# ----------------------------------------------------------------- отчёт
S["отчёт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">trả lại, hướng về người kia</span></div>'
    '<div class="hd-row"><span class="hd-piece">-чёт</span>'
    '<span class="hd-gloss">ĐẾM — như <b>счёт</b>, <b>счита́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đếm lại từng khoản rồi trình cho người trên ⇒ bản báo cáo, sự giải trình: '
    '<b>отчёт о рабо́те</b>. Đừng lẫn với <b>о́тчество</b> tên đệm theo cha — gốc <b>оте́ц</b>, khác hẳn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>счёт</b> hóa đơn, tỉ số · <b>счита́ть</b> đếm · <b>отчита́ться</b> báo cáo lại · '
    '<b>учёт</b> sự kiểm kê</div>'
)

# ----------------------------------------------------------------- сигнал
S["сигнал"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn (Pháp <i>signal</i>, từ Latin <i>signum</i> «dấu hiệu»), không chẻ theo tiếng Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>signal</i> tiếng Anh — nhận ra chứ không phải học. Chỉ cần nhớ trọng âm ở cuối: '
    '<b>сигна́л</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сигнализа́ция</b> hệ thống báo động</div>'
)

# ----------------------------------------------------------------- секрет
S["секрет"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn (Latin <i>secretus</i> «tách riêng ra»), không chẻ theo tiếng Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>secret</i> tiếng Anh. <b>секрета́рь</b> cùng gốc: người giữ chuyện kín của sếp.</div>'
    '<div class="hd-warn">Hai cụm phải thuộc: <b>по секре́ту</b> = (nói) riêng, nói nhỏ · '
    '<b>держа́ть в секре́те</b> = giữ bí mật.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>секре́тный</b> mật · <b>секрета́рь</b> thư ký</div>'
)

# ----------------------------------------------------------------- ложь
S["ложь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn <b>лож-/лг-</b> (NÓI DỐI), không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giống cái đuôi <b>-ь</b>. Nguyên âm <b>о</b> rơi khi thêm đuôi: <b>лжи</b> (riêng cách 5 giữ: '
    '<b>ло́жью</b>); số nhiều gần như không dùng. Động từ <b>лгать</b> lộ gốc <b>г</b> — <b>ж</b> ở đây là '
    '<b>г → ж</b> quen thuộc.</div>'
    '<div class="hd-warn">Tiếng Anh <i>lie</i> có hai nghĩa, tiếng Nga thì không: nằm là <b>лежа́ть</b> — khác gốc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лгать</b> nói dối · <b>лжец</b> kẻ nói dối · <b>ло́жный</b> giả, sai</div>'
)

# ----------------------------------------------------------------- период
S["период"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn (Hy Lạp <i>periodos</i> «một vòng đi»), không chẻ theo tiếng Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>period</i> tiếng Anh, nhưng trọng âm ở giữa: <b>пери́од</b>. '
    '<b>в пери́од</b> + cách 2 = trong thời kỳ…</div>'
    '<div class="hd-warn">Dấu chấm câu (<i>period</i> kiểu Mỹ) là <b>то́чка</b>, không phải <b>пери́од</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>периоди́ческий</b> định kỳ, tuần hoàn</div>'
)

# ----------------------------------------------------------------- постоянный
S["постоянный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, không mang nghĩa riêng ở đây</span></div>'
    '<div class="hd-row"><span class="hd-piece">-стоя́-</span>'
    '<span class="hd-gloss">ĐỨNG — gốc của <b>стоя́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-нный</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cứ đứng nguyên đó, không rời đi ⇒ thường xuyên, lâu dài: <b>постоя́нный а́дрес</b> = địa chỉ thường trú. '
    'Trạng từ <b>постоя́нно</b> = suốt, lúc nào cũng: <b>Он постоя́нно опа́здывает</b>. '
    'Dạng ngắn bớt một <b>н</b>, chèn <b>е</b>: <b>постоя́нен</b>, <b>постоя́нна</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стоя́ть</b> đứng · <b>постоя́нно</b> liên tục · <b>настоя́щий</b> thật, hiện tại · '
    '<b>стоя́нка</b> bãi đỗ xe</div>'
)

# ----------------------------------------------------------------- вечный
S["вечный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">веч-</span>'
    '<span class="hd-gloss">= <b>век</b> thế kỷ, đời người, <b>к → ч</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ный</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Kéo dài hết thế kỷ này sang thế kỷ khác ⇒ vĩnh cửu: <b>Ничто́ не ве́чно</b>. '
    'Nói quá lên thì thành «triền miên»: <b>ве́чные пробле́мы</b>. '
    'Dạng ngắn chèn <b>е</b>: <b>ве́чен</b>, <b>ве́чна</b>.</div>'
    '<div class="hd-warn"><b>ве́чер</b> buổi tối trông giống mà KHÁC gốc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>век</b> thế kỷ · <b>ве́чно</b> mãi mãi · <b>веково́й</b> lâu đời</div>'
)

# ----------------------------------------------------------------- скорый
S["скорый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">скор-</span>'
    '<span class="hd-gloss">NHANH (như <b>ско́ро</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhanh về TỐC ĐỘ hằng ngày là <b>бы́стрый</b>; <b>ско́рый</b> nghiêng về «sắp tới, gấp»: '
    '<b>в ско́ром вре́мени</b> = sắp tới, <b>ско́рый по́езд</b> = tàu nhanh. '
    'Dạng ngắn giống trung <b>ско́ро</b> chính là trạng từ «sắp»; so sánh hơn <b>скоре́е</b> còn là «đúng hơn là»: '
    '<b>скоре́е всего́</b> = nhiều khả năng nhất.</div>'
    '<div class="hd-warn"><b>До ско́рого!</b> = Hẹn sớm gặp lại!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ско́ро</b> sắp · <b>ско́рость</b> tốc độ · <b>ско́рая</b> xe cấp cứu</div>'
)

# ----------------------------------------------------------------- срок
S["срок"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn với người học, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Khoảng thời gian ĐÃ ĐỊNH, nhìn từ điểm cuối của nó: hạn chót, kỳ hạn. '
    '<b>в срок</b> = đúng hạn · <b>на до́лгий срок</b> = trong thời gian dài.</div>'
    '<div class="hd-warn"><b>срок го́дности</b> = hạn sử dụng — in trên mọi bao bì thực phẩm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сро́чный</b> khẩn · <b>сро́чно</b> gấp · <b>просро́чить</b> để quá hạn</div>'
)

# ----------------------------------------------------------------- оба
S["оба"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Số từ gốc trơn, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đi y như <b>два/две</b>: tách giống, và kéo danh từ sang cách 2 số ít — '
    '<b>о́ба бра́та</b> (đực, trung) · <b>о́бе сестры́</b> (cái).</div>'
    '<div class="hd-warn">Biến cách vẫn tách giống: đực/trung <b>обо́их</b>, <b>обо́ими</b> · '
    'cái <b>обе́их</b>, <b>обе́ими</b>.</div>'
)

# ----------------------------------------------------------------- пара
S["пара"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn (Latin <i>par</i> «ngang nhau», cùng nguồn <i>pair</i> tiếng Anh), không chẻ theo tiếng Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai thứ đi với nhau: <b>па́ра ту́фель</b> = một đôi giày, <b>влюблённая па́ра</b> = cặp đôi. '
    'Nói lỏng thì «vài»: <b>па́ра мину́т</b> = vài phút — danh từ sau nó ở cách 2. '
    'Ở đại học <b>па́ра</b> là một tiết đôi (khoảng 90 phút).</div>'
    '<div class="hd-warn"><b>пар</b> hơi nước trông giống mà KHÁC gốc.</div>'
)

# ----------------------------------------------------------------- гораздо
S["гораздо"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Hư từ, không chẻ được — trông giống <b>гора́</b> núi mà không cùng gốc.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỉ đứng trước SO SÁNH HƠN, để nói «hơn nhiều»: '
    '<b>гора́здо лу́чше</b>, <b>гора́здо бо́льше</b>. Nghĩa như <b>намно́го</b>.</div>'
    '<div class="hd-warn">Với tính từ thường thì dùng <b>о́чень</b>: ❌ <b>гора́здо хоро́ший</b> → ✅ <b>о́чень хоро́ший</b>.</div>'
)

B = {
    "docbangmat": 97,
    "loitubat": 1,
    "nguonsai": 0,
    "baolen": [
        "TRÙNG KHÔNG GỠ ĐƯỢC: гора́здо ↔ намно́го (k116) — đồng nghĩa thật, cùng badge adv; rút gọn còn «hơn nhiều» hay «hơn hẳn» đều trùng. V chỉ bỏ «...» (ghi chú cách dùng). Phương án cho user chọn: «vượt xa» (gloss «by far») hoặc chấp nhận đề bài hai đáp án.",
        "CHƯA SO VA CHẠM: nghĩa MỚI trong V chưa đối chiếu với thẻ đã nạp (agent không đọc Anki) — «hôm nọ» (как-то), «không cái gì», «hư vô» (ничто), «cặp đôi», «tiết học» (пара), «sắp tới», «tốc hành» (скорый). Luồng chính chạy lại `vacham` sau khi áp V.",
        "V cần duyệt: скорый bỏ «nhanh» theo lệnh gỡ trùng бы́стрый — đề bài mất đúng nghĩa gốc; còn «gấp, chóng, sắp tới, tốc hành» (gloss «near / forthcoming / express (train)»).",
        "V cần duyệt: как-то bỏ «có lần» (trùng одна́жды) thay bằng «hôm nọ» (gloss «the other day»); ничто «không gì cả» → «không cái gì, hư vô» (gloss «nought», khớp dòng họ hàng trên thẻ ничего́); пара «cặp» → «cặp đôi», thêm «tiết học» (gloss «class (at university)»); данный bỏ «hiện tại».",
        "Không chắc (từ nguyên, chưa máy nào soát): лишь cùng gốc ли́шний/лиши́ть (viết «Từ nguyên:» trong hd-why, không dùng ô Mức tin); гора́здо KHÔNG cùng gốc гора́ (Vasmer: ← гора́зд «giỏi»); бу́дто ← будь + то đã hạ mức tin bằng ô ⚠️; поско́льку = по- + «dạng cũ của ско́лько».",
        "Gợi ý họ «о́ба / па́ра» của luồng chính KHÔNG nối thành Họ hàng: па́ра mượn Latin par, о́ба gốc Slav — chỉ cùng chủ đề. Họ hàng cố ý vắng: бу́дто, гора́здо (hư từ), о́ба (số từ), па́ра (từ mượn đứng một mình).",
        "Lỗi tự bắt (1): срок viết «на срок + thời gian: на ме́сяц» — ví dụ không chứa chính từ срок, gây hiểu sai; đổi thành «на до́лгий срок». Không thấy thẻ cũ nào khai sai (ско́лько, ско́ро, стоя́ть, век, счёт, ничего́ đều khớp khuôn).",
    ],
}
