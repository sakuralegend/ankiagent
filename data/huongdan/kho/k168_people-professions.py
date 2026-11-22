# -*- coding: utf-8 -*-
"""k168 — people::professions (lô trộn): người, cơ thể, tiền bạc, ăn uống.

Chỗ cần nhất quán trong lô:
(1) дохо́д / расхо́д: cùng -ход- ĐI BẰNG CHÂN như thẻ доходи́ть; до- TỚI ↔ рас- TẢN RA — một cặp đối.
(2) вы́жить / выжива́ть: вы- RA NGOÀI + жи- SỐNG như thẻ жить; bảng chia vay thân жив- của жить.
(3) оте́чественный: от(е)ч- CHA như thẻ оте́ц; máy ghép че́стный = báo oan.
(4) нали́чные: лич- MẶT như thẻ ли́чный (ц → ч). замести́тель: мест- CHỖ như thẻ ме́сто.
(5) подро́сток: рос- LỚN như thẻ рост / расти́. напи́ток: пи- UỐNG như thẻ пить.
Họ hàng cố ý vắng: ве́ко (gốc trơn, không có từ phái sinh thông dụng).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "сексуальный": "gợi cảm, về tình dục",                     # bỏ «sexy» (chữ Anh) + đổi «;»
    "подросток": "thanh thiếu niên, trẻ vị thành niên",        # «tuổi dậy thì» là nghĩa SAI (puberty ≠ teenager)
    "отечественный": "nội địa, trong nước, thuộc tổ quốc",     # of the fatherland
    "доход": "thu nhập, doanh thu, lợi nhuận",                 # revenue / profit
    "расход": "khoản chi, chi phí, mức tiêu thụ",              # costs
    "профессиональный": "chuyên nghiệp, thuộc nghề nghiệp",    # occupational / vocational
    "заместитель": "cấp phó, người phó, người thay thế",       # substitute / stand-in
    "акция": "cổ phiếu, chiến dịch, hành động, đợt khuyến mãi",  # thiếu action/campaign; đổi «;»
    "голод": "cơn đói, nạn đói, sự thiếu hụt",                 # shortage / dearth; đổi «;»
}

# --------------------------------------------------------------------- сексуальный
S["сексуальный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">секс-</span>'
    '<span class="hd-gloss">như <b>секс</b> — mượn tiếng Anh <i>sex</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-уа́льный</span>'
    '<span class="hd-gloss">đuôi tính từ quốc tế = <i>-ual</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chép thẳng <i>sexual</i>: <b>-уа́льный</b> ứng với <i>-ual</i> như '
    '<b>индивидуа́льный</b> ↔ <i>individual</i>. Dạng ngắn giống đực chèn <b>-е-</b>: '
    '<b>сексуа́лен</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>секс</b> tình dục · <b>сексуа́льность</b> sức gợi cảm</div>'
)

# --------------------------------------------------------------------- висок
S["висок"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вис-</span>'
    '<span class="hd-gloss">TREO — như <b>висе́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́к</span>'
    '<span class="hd-gloss">hậu tố danh từ giống đực</span></div>'
    '<div class="hd-warn">⚠️ Mức tin: nối với <b>висе́ть</b> là từ nguyên (chỗ tóc mai buông '
    'xuống), không phải luật suy ra được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>о</b> chạy mất khi thêm đuôi, trọng âm dồn ra cuối: '
    '<b>виска́</b>, <b>виско́м</b>, số nhiều <b>виски́</b>.</div>'
    '<div class="hd-warn"><b>виски́</b> (hai thái dương, nhấn cuối) ≠ <b>ви́ски</b> rượu whisky '
    '(nhấn đầu) — chỉ trọng âm tách hai từ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>висо́чный</b> thuộc thái dương</div>'
)

# --------------------------------------------------------------------- веко
S["веко"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc Slav trơn, nghĩa cổ «cái nắp đậy» — không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái nắp của con mắt. Giống trung mà số nhiều ra <b>-и</b>: '
    '<b>ве́ки</b>, cách 2 <b>век</b> — bộ phận đi đôi, như <b>коле́но → коле́ни</b>.</div>'
    '<div class="hd-warn"><b>во ве́ки веко́в</b> «đời đời» KHÔNG thuộc từ này — đó là số nhiều cổ '
    'của <b>век</b> thế kỷ, chỉ trùng mặt chữ với <b>ве́ки</b> mí mắt.</div>'
)

# --------------------------------------------------------------------- поколение
S["поколение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng rõ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-коле́н-</span>'
    '<span class="hd-gloss">như <b>коле́но</b> — nghĩa cổ «một đời, một chi trong dòng họ»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ие</span>'
    '<span class="hd-gloss">đuôi danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>коле́но</b> ngoài «đầu gối» còn nghĩa cổ là một đời trong phả hệ '
    '(số nhiều <b>коле́на</b>); <b>поколе́ние</b> giữ đúng nghĩa đó ⇒ thế hệ.</div>'
    '<div class="hd-warn"><b>из поколе́ния в поколе́ние</b> — từ đời này sang đời khác.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>коле́но</b> đầu gối; đời (nghĩa cổ)</div>'
)

# --------------------------------------------------------------------- подросток
S["подросток"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span>'
    '<span class="hd-gloss">thêm một chút, nhích lên — như <b>подрасти́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-рост-</span>'
    '<span class="hd-gloss">LỚN LÊN — như <b>рост</b>, <b>расти́</b> (о ↔ а)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ок</span>'
    '<span class="hd-gloss">hậu tố danh từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đứa đang lớn thêm, chưa tới <b>взро́слый</b> người lớn ⇒ tuổi mới lớn. '
    '<b>о</b> trong <b>-ок</b> chạy mất: <b>подро́стка</b>, <b>подро́стку</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>расти́</b> lớn lên · <b>подрасти́</b> lớn thêm · '
    '<b>подростко́вый</b> thuộc tuổi thiếu niên · <b>рост</b> chiều cao</div>'
)

# --------------------------------------------------------------------- выжить
S["выжить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span>'
    '<span class="hd-gloss">RA NGOÀI — hút trọng âm suốt bảng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-жи-ть</span>'
    '<span class="hd-gloss">SỐNG — như <b>жить</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Sống mà thoát RA khỏi cơn nguy ⇒ sống sót. Thể hoàn thành; cặp là '
    '<b>выжива́ть</b>. Bảng chia vay thân <b>жив-</b> của <b>жить</b>: <b>вы́живу</b>, '
    '<b>вы́живешь</b>, quá khứ <b>вы́жил</b>.</div>'
    '<div class="hd-warn">Có tân ngữ cách 4 thì nghĩa khác: <b>вы́жить кого́-то</b> = làm cho '
    'người ta sống không nổi mà phải ra đi, hất cẳng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жить</b> sống · <b>жизнь</b> cuộc sống · <b>живо́й</b> còn sống</div>'
)

# --------------------------------------------------------------------- выживать
S["выживать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">RA NGOÀI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-жи-</span>'
    '<span class="hd-gloss">SỐNG — như <b>жить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва́-ть</span>'
    '<span class="hd-gloss">hậu tố thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dạng chưa hoàn thành của <b>вы́жить</b>: đang cầm cự, xoay xở để sống. '
    'Chia đều lớp 1: <b>выжива́ю</b>, <b>выжива́ешь</b> — trọng âm đứng ở <b>-ва́-</b>, không '
    'nhảy về <b>вы́-</b> như ở cặp hoàn thành.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́жить</b> sống sót (xong) · <b>выжива́ние</b> sự sinh tồn · '
    '<b>жить</b> sống</div>'
)

# --------------------------------------------------------------------- рай
S["рай"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đi đôi với <b>ад</b> địa ngục, và cùng một thói: «ở trên thiên đường» '
    'dùng đuôi <b>-ю́</b>: <b>в раю́</b> (như <b>в аду́</b>); <b>ра́е</b> chỉ dùng sau '
    '<b>о</b>: <b>о ра́е</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: nhiều nhà từ nguyên cho là mượn tiếng Iran cổ, nghĩa '
    '«phúc lành, của cải» — không chắc chắn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ра́йский</b> như thiên đường</div>'
)

# --------------------------------------------------------------------- отечественный
S["отечественный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">оте́ч-</span>'
    '<span class="hd-gloss">CHA — như <b>оте́ц</b> (<b>ц → ч</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-еств-</span>'
    '<span class="hd-gloss">→ <b>оте́чество</b> tổ quốc, «đất của cha»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-енн-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thuộc đất của cha ⇒ của nước mình, hàng nội. Chuỗi chữ <b>-честв-</b> chỉ '
    'trông giống <b>честь</b> danh dự — không cùng gốc.</div>'
    '<div class="hd-warn"><b>Вели́кая Оте́чественная война́</b> — Chiến tranh Vệ quốc vĩ đại '
    '(1941–1945).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оте́ц</b> cha · <b>оте́чество</b> tổ quốc · <b>о́тчество</b> tên '
    'đệm theo cha</div>'
)

# --------------------------------------------------------------------- предатель
S["предатель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пре-</span>'
    '<span class="hd-gloss">QUA — dạng sách cổ của <b>пере-</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-да-</span>'
    '<span class="hd-gloss">CHO, TRAO — như <b>дать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-тель</span>'
    '<span class="hd-gloss">NGƯỜI làm việc đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Kẻ trao người mình sang tay địch. Tiếng Anh dùng đúng hình ảnh ấy: '
    '<i>traitor</i> từ Latin <i>tradere</i> «trao đi».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>преда́ть</b> phản bội · <b>преда́тельство</b> sự phản bội · '
    '<b>переда́ть</b> trao lại · <b>дать</b> cho</div>'
)

# --------------------------------------------------------------------- доход
S["доход"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI TẬN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ход</span>'
    '<span class="hd-gloss">ĐI BẰNG CHÂN — như <b>доходи́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiền «đi tới» tay mình ⇒ thu nhập. Đối với <b>расхо́д</b>: tiền «đi tản '
    'ra» khỏi tay ⇒ khoản chi.</div>'
    '<div class="hd-warn"><b>дохо́ды и расхо́ды</b> — thu và chi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>доходи́ть</b> đi tới · <b>дохо́дный</b> sinh lời · '
    '<b>расхо́д</b> khoản chi</div>'
)

# --------------------------------------------------------------------- расход
S["расход"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рас-</span>'
    '<span class="hd-gloss">TẢN RA nhiều phía</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ход</span>'
    '<span class="hd-gloss">ĐI BẰNG CHÂN — như <b>доходи́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiền, nhiên liệu «đi tản ra» khỏi tay ⇒ khoản chi, mức tiêu hao. '
    'Ngược với <b>дохо́д</b> thu nhập.</div>'
    '<div class="hd-warn">Nói chi phí thường dùng số nhiều: <b>расхо́ды на</b> + cách 4 · '
    '<b>расхо́д бензи́на</b> mức hao xăng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>расхо́довать</b> tiêu, chi · <b>расходи́ться</b> tản ra · '
    '<b>дохо́д</b> thu nhập</div>'
)

# --------------------------------------------------------------------- наличные
S["наличные"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">TRÊN, có ở đó</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лич-</span>'
    '<span class="hd-gloss">MẶT — <b>лицо́</b>, <b>ц → ч</b> như <b>ли́чный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ые</span>'
    '<span class="hd-gloss">đuôi tính từ số nhiều</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Rút gọn từ <b>нали́чные де́ньги</b> «tiền có trước mặt» — tiếng Việt '
    'cũng gọi là tiền MẶT. Tính từ làm danh từ, luôn số nhiều, chia đuôi tính từ.</div>'
    '<div class="hd-warn"><b>плати́ть нали́чными</b> (cách 5) trả tiền mặt · '
    '<b>безнали́чный</b> không dùng tiền mặt, chuyển khoản.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нали́чие</b> sự có mặt, có sẵn · <b>лицо́</b> mặt · '
    '<b>ли́чный</b> cá nhân</div>'
)

# --------------------------------------------------------------------- профессиональный
S["профессиональный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">профессион-</span>'
    '<span class="hd-gloss">NGHỀ — như <b>профе́ссия</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́льный</span>'
    '<span class="hd-gloss">đuôi tính từ quốc tế = <i>-al</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chép thẳng <i>professional</i>. Dạng ngắn giống đực chèn <b>-е-</b>: '
    '<b>Он о́чень профессиона́лен</b>.</div>'
    '<div class="hd-warn"><b>профсою́з</b> công đoàn = <b>профессиона́льный сою́з</b> viết gọn — '
    'gặp <b>проф-</b> đầu từ ghép là mảnh này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>профе́ссия</b> nghề · <b>профессиона́л</b> người chuyên nghiệp</div>'
)

# --------------------------------------------------------------------- охотник
S["охотник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">охо́т-</span>'
    '<span class="hd-gloss">như <b>охо́та</b> — <b>о-</b> mờ nghĩa + <b>-хот-</b> MUỐN, THÈM</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ник</span>'
    '<span class="hd-gloss">NGƯỜI làm việc đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người đi <b>охо́та</b> ⇒ thợ săn. Gốc «thèm» vẫn còn sống ở nghĩa thứ hai.</div>'
    '<div class="hd-warn"><b>охо́тник до</b> + cách 2 = người mê cái gì: '
    '<b>охо́тник до книг</b> người mê sách.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>охо́та</b> việc săn · <b>охо́титься</b> đi săn · '
    '<b>охо́тно</b> sẵn lòng · <b>хоте́ть</b> muốn</div>'
)

# --------------------------------------------------------------------- заместитель
S["заместитель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">VÀO thay, lấp vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мест-</span>'
    '<span class="hd-gloss">CHỖ — như <b>ме́сто</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-тель</span>'
    '<span class="hd-gloss">NGƯỜI làm việc đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người vào CHỖ của ai ⇒ người thay, cấp phó. Gốc là <b>мест-</b>, '
    'không phải <b>заме́тить</b> nhận ra (gốc <b>мет-</b> dấu).</div>'
    '<div class="hd-warn"><b>замести́тель дире́ктора</b> (+ cách 2) phó giám đốc; khẩu ngữ '
    'gọi tắt là <b>зам</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ме́сто</b> chỗ · <b>замести́ть</b>, <b>замеща́ть</b> thay thế '
    '(<b>ст → щ</b>) · <b>вме́сто</b> thay cho</div>'
)

# --------------------------------------------------------------------- должность
S["должность"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">долж-н-</span>'
    '<span class="hd-gloss">= <b>долг</b> NỢ, BỔN PHẬN (<b>г → ж</b>), như <b>до́лжен</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span>'
    '<span class="hd-gloss">→ danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Phần việc mình «phải» gánh ở một vị trí ⇒ chức vụ.</div>'
    '<div class="hd-warn"><b>занима́ть до́лжность</b> giữ chức · <b>в до́лжности</b> + cách 2: '
    '<b>в до́лжности дире́ктора</b> ở cương vị giám đốc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>долг</b> nợ, bổn phận · <b>до́лжен</b> phải · '
    '<b>должни́к</b> con nợ</div>'
)

# --------------------------------------------------------------------- акция
S["акция"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">акц-</span>'
    '<span class="hd-gloss">HÀNH ĐỘNG — Latin <i>actio</i>, tiếng Anh <i>action</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ия</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Hành động» ⇒ chiến dịch, đợt khuyến mãi — suy ra được. Nghĩa '
    '«cổ phiếu» thì phải thuộc: đi theo tiếng Đức <i>Aktie</i>.</div>'
    '<div class="hd-warn">Chữ <b>А́кция!</b> trên bảng giá siêu thị = đang khuyến mãi; '
    'trên sàn chứng khoán = cổ phiếu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>акционе́р</b> cổ đông · <b>акти́вный</b> năng động (cùng gốc Latin)</div>'
)

# --------------------------------------------------------------------- голод
S["голод"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc Slav trơn, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một chữ cho cả cơn đói của một người lẫn nạn đói của cả vùng. Trọng âm '
    'dời khi thêm đuôi: <b>го́лод</b> → <b>голо́дный</b>.</div>'
    '<div class="hd-warn"><b>умира́ть с го́лоду</b> chết đói (hay nói quá: đói muốn chết) · '
    '<b>мори́ть го́лодом</b> bỏ đói ai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>голо́дный</b> đói · <b>голода́ть</b> chịu đói · '
    '<b>проголода́ться</b> thấy đói</div>'
)

# --------------------------------------------------------------------- напиток
S["напиток"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пи-</span>'
    '<span class="hd-gloss">UỐNG — như <b>пить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ток</span>'
    '<span class="hd-gloss">hậu tố danh từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thứ để uống. <b>о</b> trong <b>-ток</b> chạy mất: <b>напи́тка</b>, '
    'số nhiều <b>напи́тки</b>.</div>'
    '<div class="hd-warn"><b>спиртны́е напи́тки</b> đồ uống có cồn · '
    '<b>безалкого́льные напи́тки</b> nước ngọt, đồ uống không cồn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пить</b> uống · <b>пи́во</b> bia · <b>пья́ный</b> say rượu</div>'
)

# --------------------------------------------------------------------- алкоголь
S["алкоголь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ — từ quốc tế, giống hệt <i>alcohol</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <b>-ь</b> không cho biết giống, phải thuộc riêng.</div>'
    '<div class="hd-warn">GIỐNG ĐỰC: <b>кре́пкий алкого́ль</b> rượu mạnh — không phải '
    '«крепкая».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>алкого́льный</b> có cồn · <b>безалкого́льный</b> không cồn · '
    '<b>алкого́лик</b> người nghiện rượu</div>'
)

B = {
    "docbangmat": 75,
    "loitubat": 2,      # напиток: chẻ «-ток» mà câu dưới viết «о trong -ок» + на- không nói rõ là mờ nghĩa · отечественный: gọi «-честв-» là «mảnh» trong khi nó không phải mảnh chẻ
    "nguonsai": 2,      # веко: CUM CO DINH gán «в/на ве́ки веко́в» cho веко — thật ra là số nhiều cổ của век · подросток: đề cũ «tuổi dậy thì» là nghĩa sai (puberty, không phải teenager)
    "baolen": [
        "MIEN_TRU đã thêm 1 mục (đồng tự thật): виски́ = số nhiều của висо́к (chính nouns.csv dòng висок ghi pl_nom виски'), máy khớp nhầm dòng ви́ски whisky. Thẻ висок cố ý dạy cặp виски́ ↔ ви́ски. File: data/huongdan/mientru.py — luồng chính duyệt.",
        "KHÔNG viết V cho 3 thẻ có ngoặc (chú thích user, §2c): висок «thái dương (bên đầu)», выживать «sống sót, cầm cự (thường xuyên)», выжить «sống sót (xong/sẽ xong)». Hai ngoặc của выжить/выживать trông như nhãn thể kiểu cũ (loại ① bị cấm) chứ không giống văn user — và cả hai đều THIẾU nghĩa «hất cẳng, đuổi ra» (gloss: drive out / force out). User xem có muốn tự sửa không.",
        "Không chắc (đã gắn ⚠️ Mức tin trên thẻ): висо́к ← висе́ть (Vasmer «вероятно»); рай ← tiếng Iran cổ. Không gắn Mức tin nhưng là từ nguyên: поколе́ние ← коле́но nghĩa cổ «một đời» (chuẩn, khớp ghi chú k162 về коле́на); преда́тель пре- = пере- dạng Slav nhà thờ; а́кция «cổ phiếu» qua tiếng Đức Aktie.",
        "V cần duyệt: сексуальный (bỏ chữ Anh «sexy»), подросток («tuổi dậy thì» → «trẻ vị thành niên»), отечественный (+thuộc tổ quốc), доход (+doanh thu, lợi nhuận), расход (+chi phí), профессиональный (+thuộc nghề nghiệp), заместитель (+người thay thế), акция (+chiến dịch, hành động), голод (+sự thiếu hụt). Có thể chạm một nghĩa với прибыль/затраты/действие — chung một nghĩa, không trùng hết.",
        "веко: cố ý bỏ mục Họ hàng (gốc trơn, không có từ phái sinh thông dụng; ве́чный/век KHÁC gốc).",
    ],
}
