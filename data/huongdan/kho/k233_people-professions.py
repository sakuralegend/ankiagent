# -*- coding: utf-8 -*-
"""k233 — people::professions (lô trộn): dáng người, tín ngưỡng, nghề, cảnh ngộ, đồ ăn uống.

Chỗ cần nhất quán trong lô:
(1) стро(й)- XẾP, DỰNG như стро́ить, стро́йка; вер- TIN; служ- PHỤC VỤ (слуга́, г→ж); полк- TRUNG ĐOÀN.
(2) Tính từ dùng như danh từ: ве́рующий, слу́жащий (đuôi -ющ-/-ащ- «ĐANG làm» như веду́щий),
    безрабо́тный — cùng chia hệt tính từ.
(3) Đuôi NGƯỜI mượn: -ант/-ент (иммигра́нт, претенде́нт), -и́ст (такси́ст), -лог (стомато́лог).
(4) -ин của блонди́н là đuôi Pháp, KHÔNG rụng ở số nhiều (khác -ин của христиани́н).
Họ hàng cố ý vắng: майоне́з, ликёр (từ mượn đứng một mình).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "стройный": "thon thả, mảnh mai, dong dỏng, cân đối, hài hoà, mạch lạc",  # THIẾU harmonious / coherent / logical; «mảnh khảnh» thiên về gầy yếu
    "верующий": "có tín ngưỡng, sùng đạo, tin đạo, tín đồ",   # THIẾU believer / the faithful
    "христианство": "Kitô giáo, Cơ đốc giáo",                 # «đạo Thiên Chúa» ở VN thường hiểu là riêng Công giáo
    "претендент": "ứng viên, người dự tuyển, người xin việc, người tranh chức, người thách đấu",  # THIẾU contender / challenger
    "голодать": "bị đói, chịu đói, nhịn ăn, tuyệt thực",      # THIẾU hunger strike; «chết đói» = умереть с голоду
}

# --------------------------------------------------------------------- стройный
S["стройный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">строй-</span><span class="hd-gloss">XẾP, DỰNG '
    'cho có hàng lối — <b>стро́ить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span><span class="hd-gloss">đuôi tính '
    'từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Xếp đâu ra đấy» ⇒ người thì dáng cân đối, thon thả '
    '(<b>стро́йная фигу́ра</b>); lời nói, hệ thống thì hài hoà, mạch lạc. Dạng ngắn: giống đực '
    'đổi <b>й</b> thành <b>е</b> — <b>стро́ен</b>; giống cái nhấn đuôi — <b>стройна́</b>.</div>'
    '<div class="hd-warn"><b>стро́йный</b> là lời KHEN dáng đẹp; <b>худо́й</b> chỉ nói gầy, '
    'nhiều khi là chê.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стро́ить</b> xây · <b>строй</b> hàng ngũ; chế độ · '
    '<b>стро́йка</b> công trường · <b>настрое́ние</b> tâm trạng</div>'
)

# --------------------------------------------------------------------- блондин
S["блондин"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">блонд-</span><span class="hd-gloss">tóc VÀNG — '
    'Pháp <b>blond</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ин</span><span class="hd-gloss">đuôi đi kèm từ '
    'chữ Pháp <b>blondin</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Là danh từ chỉ NGƯỜI đàn ông tóc vàng. Phụ nữ thêm <b>-ка</b>: '
    '<b>блонди́нка</b>. Người tóc sẫm là <b>брюне́т</b>, <b>брюне́тка</b>.</div>'
    '<div class="hd-warn">Số nhiều GIỮ <b>-ин</b>: <b>блонди́ны, блонди́нов</b> — khác '
    '<b>христиани́н → христиа́не</b>, vì đây không phải đuôi Nga «MỘT người».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>блонди́нка</b> cô gái tóc vàng</div>'
)

# --------------------------------------------------------------------- верующий
S["верующий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вер-</span><span class="hd-gloss">TIN — như '
    '<b>ве́ра</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-у-ющ-ий</span><span class="hd-gloss">«ĐANG làm», '
    'từ động từ <b>ве́ровать</b> — như <b>сле́дующий</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đang tin» ⇒ có đạo. Đứng một mình thì thành danh từ: người có đạo, '
    'tín đồ — vẫn chia hệt tính từ: <b>ве́рующего, ве́рующие</b>; phụ nữ là '
    '<b>ве́рующая</b>.</div>'
    '<div class="hd-warn"><b>ве́рующий</b> chỉ nói chuyện TÔN GIÁO. Tin một người, một lời nói '
    'thì dùng <b>ве́рить</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ве́ра</b> niềm tin · <b>ве́рить</b> tin · <b>ве́рный</b> trung thành, '
    'đúng · <b>неве́рующий</b> người không theo đạo</div>'
)

# --------------------------------------------------------------------- ислам
S["ислам"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ theo tiếng Nga: mượn Ả Rập <b>islām</b> «sự quy phục».</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <b>Islam</b>, nhấn <b>-ла́м</b>. Tên đạo trong tiếng Nga viết '
    'chữ THƯỜNG và chỉ dùng số ít. Giống đực, chia đều: <b>в исла́ме</b> trong đạo Hồi.</div>'
    '<div class="hd-warn"><b>приня́ть исла́м</b> — theo, cải sang đạo Hồi (<b>приня́ть</b> + '
    'cách 4, dùng cho mọi đạo).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>исла́мский</b> thuộc Hồi giáo · <b>мусульма́нин</b> tín đồ Hồi giáo '
    '(cùng gốc Ả Rập)</div>'
)

# --------------------------------------------------------------------- христианство
S["христианство"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">христиан-</span><span class="hd-gloss">người theo '
    'Chúa Kitô — <b>христиани́н</b> bỏ <b>-ин</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ство</span><span class="hd-gloss">danh từ trừu '
    'tượng, giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đạo của các <b>христиа́не</b>» ⇒ Kitô giáo, cùng khuôn '
    '<b>мусульма́нство</b>. Trọng âm đúng chỗ của <b>христиа́не</b>: <b>христиа́нство</b>. Tên đạo '
    'viết chữ thường, chỉ dùng số ít.</div>'
    '<div class="hd-warn">Là cả đạo Kitô nói chung. Riêng Công giáo là <b>католици́зм</b>, '
    'Chính thống giáo là <b>правосла́вие</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>христиани́н</b> tín đồ Kitô giáo · <b>христиа́нка</b> nữ tín đồ · '
    '<b>христиа́нский</b> thuộc Kitô giáo · <b>Христо́с</b> Chúa Kitô</div>'
)

# --------------------------------------------------------------------- иммигрант
S["иммигрант"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">им-</span><span class="hd-gloss">VÀO (Latin '
    '<b>in-</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мигр-</span><span class="hd-gloss">DI CƯ (Latin '
    '<b>migrare</b>, Anh <b>migrate</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́нт</span><span class="hd-gloss">NGƯỜI đang làm '
    'việc đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người dọn VÀO một nước» ⇒ người nhập cư. Tiền tố <b>им-</b> gặp gốc '
    '<b>м-</b> nên viết HAI chữ <b>м</b>. Phụ nữ: <b>иммигра́нтка</b>.</div>'
    '<div class="hd-warn"><b>иммигра́нт</b> người đi VÀO ↔ <b>эмигра́нт</b> người bỏ nước đi RA '
    '(<b>э-</b> «ra», một chữ <b>м</b>). Cùng một người, nhìn từ hai nước.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>иммигра́ция</b> sự nhập cư · <b>эмигра́нт</b> người di cư ra nước '
    'ngoài · <b>мигра́нт</b> người di cư</div>'
)

# --------------------------------------------------------------------- стоматолог
S["стоматолог"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">стомато-</span><span class="hd-gloss">MIỆNG (Hy '
    'Lạp <b>stoma</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лог</span><span class="hd-gloss">NGƯỜI NGHIÊN CỨU '
    '— như <b>био́лог</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Chuyên gia về miệng» ⇒ bác sĩ răng. Môn <b>стоматоло́гия</b> bỏ '
    '<b>-ия</b>, trọng âm lùi một âm: <b>стомато́лог</b>, cùng khuôn <b>биоло́гия → '
    'био́лог</b>.</div>'
    '<div class="hd-warn">Đi khám răng: <b>к стомато́логу</b> (к + cách 3). Nói chuyện hằng ngày '
    'hay gọi <b>зубно́й врач</b>, hoặc trống không <b>зубно́й</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стоматоло́гия</b> nha khoa · <b>стоматологи́ческий</b> thuộc nha khoa · '
    '<b>психо́лог</b> nhà tâm lý học (cùng <b>-лог</b>)</div>'
)

# --------------------------------------------------------------------- служащий
S["служащий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">служ-</span><span class="hd-gloss">PHỤC VỤ — từ '
    '<b>слуга́</b> đầy tớ, <b>г→ж</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ащ-ий</span><span class="hd-gloss">«ĐANG làm» — '
    'lớp 2 thì <b>-ащ-</b>, lớp 1 thì <b>-ущ-</b> (<b>веду́щий</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người đang phục vụ» một cơ quan ⇒ nhân viên, công chức. Trọng âm theo '
    '<b>они́ слу́жат</b>: <b>слу́жащий</b>. Là danh từ nhưng chia hệt tính từ: <b>слу́жащего, '
    'слу́жащие</b>; phụ nữ là <b>слу́жащая</b>.</div>'
    '<div class="hd-warn"><b>слу́жащий</b> ngồi bàn giấy ↔ <b>рабо́чий</b> công nhân. Công chức '
    'nhà nước: <b>госуда́рственный слу́жащий</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>служи́ть</b> phục vụ · <b>слу́жба</b> công việc, sự phục vụ · '
    '<b>слуга́</b> đầy tớ · <b>обслу́живание</b> sự phục vụ</div>'
)

# --------------------------------------------------------------------- безработный
S["безработный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">без-</span><span class="hd-gloss">KHÔNG CÓ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-работ-</span><span class="hd-gloss">VIỆC LÀM — '
    '<b>рабо́та</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span><span class="hd-gloss">đuôi tính '
    'từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không có <b>рабо́та</b> ⇒ thất nghiệp. Đứng một mình là danh từ «người '
    'thất nghiệp», chia hệt tính từ: <b>безрабо́тного, безрабо́тные</b>. Dạng ngắn '
    '<b>безрабо́тен</b> hầu như không dùng: «Tôi thất nghiệp» là <b>Я безрабо́тный</b>.</div>'
    '<div class="hd-warn">Giữ <b>без-</b> vì <b>р</b> là phụ âm hữu thanh; gặp vô thanh mới thành '
    '<b>бес-</b>: <b>беспла́тный</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>безрабо́тица</b> nạn thất nghiệp · <b>рабо́та</b> việc làm · '
    '<b>рабо́тать</b> làm việc · <b>рабо́чий</b> công nhân</div>'
)

# --------------------------------------------------------------------- подполковник
S["подполковник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span><span class="hd-gloss">DƯỚI — như '
    '<b>подва́л</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-полк-</span><span class="hd-gloss">TRUNG ĐOÀN — '
    '<b>полк</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ов-ник</span><span class="hd-gloss">NGƯỜI gắn với '
    'nó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bậc ngay DƯỚI <b>полко́вник</b> đại tá ⇒ trung tá. Thang cấp: '
    '<b>майо́р → подполко́вник → полко́вник</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>полко́вник</b> đại tá · <b>полк</b> trung đoàn</div>'
)

# --------------------------------------------------------------------- нотариус
S["нотариус"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ theo tiếng Nga: mượn Latin <b>notarius</b> «người ghi chép», từ '
    '<b>nota</b> dấu ghi. Cùng gốc tiếng Anh <b>notary</b>, <b>note</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người ghi và đóng dấu cho giấy tờ» ⇒ công chứng viên. Giữ đuôi Latin '
    '<b>-ус</b>, giống đực, trọng âm đứng yên: <b>нота́риуса, нота́риусы</b>. Nữ công chứng viên '
    'cũng gọi <b>нота́риус</b>.</div>'
    '<div class="hd-warn"><b>заве́рить у нота́риуса</b> — đem công chứng (<b>у</b> + cách '
    '2).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нотариа́льный</b> thuộc công chứng · <b>но́та</b> nốt nhạc (cũng từ '
    'Latin <b>nota</b>)</div>'
)

# --------------------------------------------------------------------- лауреат
S["лауреат"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ theo tiếng Nga: mượn Latin <b>laureatus</b> «đội vòng nguyệt '
    'quế», từ <b>laurus</b> cây nguyệt quế. = Anh <b>laureate</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người xưa thắng cuộc được đội vòng nguyệt quế ⇒ người được trao giải. '
    'Trọng âm ở đuôi và đứng yên: <b>лауреа́т, лауреа́ты</b>.</div>'
    '<div class="hd-warn">Giải gì thì cách 2: <b>лауреа́т Но́белевской пре́мии</b> người đoạt giải '
    'Nobel. Dùng với giải thưởng, cuộc thi nghệ thuật; người thắng trận nói chung là '
    '<b>победи́тель</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">cùng nguồn <b>laurus</b>: <b>лавр</b> cây nguyệt quế · <b>лавро́вый '
    'лист</b> lá nguyệt quế (nấu canh)</div>'
)

# --------------------------------------------------------------------- претендент
S["претендент"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пре-тенд-</span><span class="hd-gloss">Latin '
    '«chìa ra TRƯỚC» ⇒ ĐÒI, nhắm lấy — <b>претендова́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́нт</span><span class="hd-gloss">NGƯỜI đang làm — '
    'như <b>конкуре́нт</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người đang đòi phần» một chức, một danh hiệu ⇒ ứng viên, người thách đấu. '
    'Không có nghĩa «giả vờ» như <b>pretend</b> tiếng Anh, dù cùng gốc.</div>'
    '<div class="hd-warn">Nhắm vào cái gì: <b>на</b> + cách 4 — <b>претенде́нт на до́лжность</b> '
    'người dự tuyển một chức vụ, <b>претенде́нт на ти́тул</b> người tranh danh hiệu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>претендова́ть</b> đòi, nhắm lấy · <b>прете́нзия</b> yêu sách, lời khiếu '
    'nại</div>'
)

# --------------------------------------------------------------------- банкрот
S["банкрот"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">банк-</span><span class="hd-gloss">Ý <b>banca</b> — '
    'cái QUẦY của người đổi tiền, như <b>банк</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-рот</span><span class="hd-gloss">Ý <b>rotta</b> — '
    'GÃY; không phải <b>рот</b> cái miệng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Quầy gãy» ⇒ người vỡ nợ, cùng chữ với <b>bankrupt</b>. Chỉ người hay cả '
    'công ty đều được. Trọng âm ở <b>-ро́т</b>, đứng yên.</div>'
    '<div class="hd-warn"><b>стать банкро́том</b> phá sản · <b>объяви́ть себя́ банкро́том</b> tuyên '
    'bố phá sản — đều cách 5.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>банкро́тство</b> sự phá sản · <b>обанкро́титься</b> bị phá sản · '
    '<b>банк</b> ngân hàng</div>'
)

# --------------------------------------------------------------------- таксист
S["таксист"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">такси-</span><span class="hd-gloss">xe TAXI — '
    '<b>такси́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ст</span><span class="hd-gloss">NGƯỜI làm nghề — '
    'như <b>программи́ст</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai chữ <b>и</b> nhập làm một: <b>такси́ + -и́ст → такси́ст</b>. '
    '<b>такси́</b> bất biến, còn <b>такси́ст</b> chia đều như mọi danh từ giống đực: '
    '<b>такси́ста, такси́сты</b>.</div>'
    '<div class="hd-warn">Làm nghề lái taxi → cách 5: <b>рабо́тать такси́стом</b>. Gọi theo '
    'việc thì <b>води́тель такси́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>такси́</b> xe taxi · <b>таксо́метр</b> đồng hồ tính cước</div>'
)

# --------------------------------------------------------------------- клубника
S["клубника"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">клубн-</span><span class="hd-gloss">thứ TRÒN, CỤC — '
    '<b>клу́бень</b> củ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ика</span><span class="hd-gloss">đuôi tên quả mọng '
    '— <b>земляни́ка</b>, <b>черни́ка</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Quả mọng tròn» ⇒ dâu tây. Tên quả mọng trong tiếng Nga dùng SỐ ÍT cho cả '
    'đống: <b>килогра́мм клубни́ки</b>. Muốn đếm từng quả thì thêm <b>я́года</b>: <b>одна́ я́года '
    'клубни́ки</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: nối với <b>клу́бень</b> là từ nguyên, không phải luật. Còn '
    '<b>клуб</b> câu lạc bộ mượn Anh <b>club</b>, không liên quan.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>клубни́чный</b> vị dâu, từ dâu · <b>клу́бень</b> củ · '
    '<b>клубо́к</b> cuộn len (tròn)</div>'
)

# --------------------------------------------------------------------- майонез
S["майонез"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn nguyên chữ Pháp <b>mayonnaise</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Pháp thì giống cái, sang Nga bỏ <b>-e</b> cuối, tận cùng phụ âm ⇒ giống '
    'ĐỰC, chia đều: <b>майоне́за, майоне́зом</b>. Viết <b>йо</b> như <b>майо́р</b>, '
    '<b>райо́н</b>, và chỉ một chữ <b>н</b>.</div>'
    '<div class="hd-warn">Có sốt: <b>с майоне́зом</b> (с + cách 5) — <b>сала́т с майоне́зом</b>; '
    'trộn sốt: <b>запра́вить майоне́зом</b>.</div>'
)

# --------------------------------------------------------------------- ликёр
S["ликёр"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn Pháp <b>liqueur</b>, gốc Latin <b>liquor</b> «chất '
    'lỏng» — cùng gốc Anh <b>liquid</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi Pháp <b>-eur</b> sang Nga thành <b>-ёр</b>, luôn mang trọng âm; ở '
    'đây nó KHÔNG chỉ người như <b>шофёр</b>. Rượu ngọt, thơm vị quả: <b>вишнёвый ликёр</b> rượu '
    'mùi anh đào.</div>'
    '<div class="hd-warn">Là Anh <b>liqueur</b> (rượu mùi), không phải <b>liquor</b> (rượu mạnh nói '
    'chung).</div>'
)

# --------------------------------------------------------------------- спирт
S["спирт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: từ mượn, gốc Latin <b>spiritus</b> «hơi thở, tinh thần» — '
    'cùng gốc Anh <b>spirit</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cồn là phần «hơi, tinh» bay lên khi chưng cất. Số ít nhấn gốc, số nhiều '
    'nhấn đuôi: <b>спи́рта</b> nhưng <b>спирты́, спирто́в</b> (các loại cồn). Cách 2 còn có '
    '<b>спи́рту</b>; ngâm trong cồn: <b>на спирту́</b>.</div>'
    '<div class="hd-warn"><b>спирт</b> là CHẤT cồn (<b>медици́нский спирт</b> cồn y tế); đồ uống có '
    'cồn là <b>алкого́ль</b> hoặc <b>спиртно́е</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спиртно́й</b> có cồn (đồ uống) · <b>спиртно́е</b> đồ uống có cồn</div>'
)

# --------------------------------------------------------------------- голодать
S["голодать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">голод-</span><span class="hd-gloss">CƠN ĐÓI — '
    '<b>го́лод</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span><span class="hd-gloss">đuôi động từ, '
    'lớp chia 1</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Sống trong cơn đói: thiếu ăn kéo dài, hoặc tự nhịn ăn, tuyệt thực. Chia '
    'đều: <b>голода́ю, голода́ешь</b>. Trọng âm dời khi thêm đuôi: <b>го́лод → '
    'голода́ть</b>.</div>'
    '<div class="hd-warn">«Tôi đói bụng» KHÔNG nói bằng từ này, mà là <b>Я го́лоден</b> / '
    '<b>Я голодна́</b>; vừa thấy đói: <b>Я проголода́лся</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>го́лод</b> cơn đói, nạn đói · <b>голо́дный</b> đói · '
    '<b>проголода́ться</b> thấy đói · <b>голодо́вка</b> cuộc tuyệt thực</div>'
)

# --------------------------------------------------------------------- кипеть
S["кипеть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кип-</span><span class="hd-gloss">SÔI — gốc '
    'trơn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е-ть</span><span class="hd-gloss">đuôi động từ, '
    'lớp chia 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nước sôi, rồi người «sôi»: <b>кипе́ть от зло́сти</b> sôi lên vì tức. Ngôi '
    '«tôi» chêm л: <b>киплю́</b>; trọng âm luôn ở đuôi: <b>кипи́шь, кипи́т, кипя́т</b> — không lùi '
    'như <b>терпе́ть → те́рпишь</b>. Sôi lên (hoàn thành): <b>вскипе́ть</b>, '
    '<b>закипе́ть</b>.</div>'
    '<div class="hd-warn"><b>кипе́ть</b> là nước TỰ sôi, không có bổ ngữ: <b>вода́ кипи́т</b>. ĐUN '
    'cho sôi là <b>кипяти́ть</b> + cách 4: <b>кипяти́ть во́ду</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кипято́к</b> nước sôi · <b>кипяти́ть</b> đun sôi · <b>закипе́ть</b> bắt '
    'đầu sôi</div>'
)

B = {
    "docbangmat": 86,
    "loitubat": 4,
    "nguonsai": 1,
    "baolen": [
        "V cần duyệt (5): стройный, верующий, христианство, претендент, голодать — lý do ghi cạnh từng dòng V.",
        "NGOÀI LÔ: thẻ служить (k119, đã nạp) ghi служа́щий ở Họ hàng — SAI trọng âm, đúng là слу́жащий (từ điển và thẻ của lô này).",
        "Nguồn sai (1): OpenRussian ghi dạng ngắn giống trung của стройный là стройно́; chuẩn là стро́йно ⇒ không đưa lên thẻ.",
        "Lỗi tự bắt (4): претендент «кандидат đi với в» nói quá (кандидат на должность vẫn đúng) ⇒ bỏ; претендент «không dính gì pretend, dù cùng gốc» tự mâu thuẫn ⇒ «không có nghĩa giả vờ»; клубника «không đếm thẳng» nói cứng ⇒ viết lại; майонез «йо chứ không ё» lý do vô nghĩa vì âm đó không nhấn ⇒ bỏ.",
        "Ví dụ trên thẻ gượng (dữ liệu _opus_k233, không phải việc của lô): ислам «В разных исламах…» và христианство «В разных христианствах…» dùng số nhiều không tự nhiên; спирт «На спирте … настаивает» — thành ngữ chuẩn là на спирту́ (thẻ dạy dạng này).",
        "Không chắc: клубника ← клубень đã ghi ⚠️ Mức tin.",
        "Họ hàng cố ý vắng: майонез, ликёр. Chẻ претендент khớp претендовать (k231): пре-тенд-.",
        "Dạng ngắn безработный bảng chia có, nhưng thực tế hầu như không dùng — thẻ nói thẳng thế.",
    ],
}
