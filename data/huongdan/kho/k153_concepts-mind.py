# -*- coding: utf-8 -*-
"""k153 — concepts::mind: 21 từ — khái niệm trừu tượng (cách, phương án, trạng thái, nỗi sợ).

Không khối hệ thống. Chỗ cần nhất quán trong lô:
(1) Gốc -ня- NẮM, LẤY (khớp поня́ть, взять, приня́ть): понятие, понятный.
(2) Gốc -став- ĐẶT (khớp ста́вить, представи́тель): cặp thể представить/представлять —
    thẻ HT giải gốc, thẻ CHT dẫn chiếu + nói đúng chỗ khác.
(3) Gốc -стоя- ĐỨNG (khớp состоя́ть, стоя́ть): состояние.
(4) Từ quốc tế mượn đứng một mình, KHÔNG chẻ: контроль, федерация, метод, принцип, вариант.
Họ hàng: có ở mọi thẻ (kể cả từ mượn — đều có phái sinh thông dụng).
"""

# 🔴 KHÔNG dựng biến khối dùng chung (HE/LUAT/THE…) rồi cộng vào mọi thẻ.

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "король": "nhà vua, quân K",                       # «;» → «,»
    "федерация": "liên đoàn, liên bang",               # «;» → «,»
    "решение": "quyết định, lời giải",                 # «;» → «,»; «cách giải» → «lời giải» (gloss: solution / answer)
    "средство": "phương tiện, cách, tiền của, phương thuốc",  # «;» → «,»; thêm «phương thuốc» (gloss: remedy)
    "вариант": "phương án, lựa chọn, phiên bản",       # thêm «phiên bản» (gloss: version / variant) — tách khỏi вы́бор «sự lựa chọn»
    "представить": "giới thiệu, trình ra, đệ trình, hình dung, tưởng tượng",  # RÚT «giới thiệu» (trùng посове́товать) + «nộp» (trùng сдать); thêm nghĩa gloss: submit / imagine
    "представлять": "giới thiệu, trình bày, hình dung, tưởng tượng, đại diện",  # thêm nghĩa gloss: imagine / represent
    "состояние": "trạng thái, tình trạng, gia tài",    # thêm «gia tài» (gloss: fortune / wealth)
    "довольный": "hài lòng, mãn nguyện",               # RÚT «vui vẻ» — trùng весёлый (k53, đã nạp); gloss: content / pleased
}

S = {}

# ----------------------------------------------------------- король
S["король"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — từ rất cổ, theo từ nguyên phổ biến là tên '
    '<i>Karl</i> (Charlemagne) biến thành danh xưng «vua», như Ba Lan <i>król</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giống ĐỰC dù đuôi <b>-ь</b>. Trọng âm nhảy xuống đuôi ngay từ cách 2: '
    '<b>коро́ль → короля́</b>, số nhiều <b>короли́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>короле́ва</b> nữ hoàng, hoàng hậu · <b>короле́вство</b> vương quốc · '
    '<b>короле́вский</b> thuộc vua</div>'
)

# ----------------------------------------------------------- контроль
S["контроль"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn Pháp <i>contrôle</i> — không chẻ trong tiếng Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>control</i>, nhưng nghiêng về KIỂM TRA, giám sát hơn là điều khiển. '
    'Giống ĐỰC dù đuôi <b>-ь</b>.</div>'
    '<div class="hd-warn"><b>контро́льная</b> (<b>рабо́та</b>) = bài kiểm tra ở trường — '
    'tính từ dùng luôn như danh từ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>контро́льный</b> thuộc kiểm tra · <b>контроли́ровать</b> kiểm soát · '
    '<b>контролёр</b> người soát vé</div>'
)

# ----------------------------------------------------------- безопасность
S["безопасность"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">без-</span>'
    '<span class="hd-gloss">KHÔNG CÓ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-опа́с-н-</span>'
    '<span class="hd-gloss">E NGẠI — gốc <b>опаса́ться</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span>'
    '<span class="hd-gloss">→ danh từ trừu tượng, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tình trạng không có gì phải e ngại = an toàn. Bỏ <b>без-</b> là ra '
    'nghĩa ngược: <b>опа́сность</b> sự nguy hiểm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>безопа́сный</b> an toàn · <b>опа́сность</b> sự nguy hiểm · '
    '<b>опа́сный</b> nguy hiểm · <b>опаса́ться</b> e ngại</div>'
)

# ----------------------------------------------------------- федерация
S["федерация"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">федер-</span>'
    '<span class="hd-gloss">Latin <i>foedus</i> — HIỆP ƯỚC, liên minh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ция</span>'
    '<span class="hd-gloss">= <i>-ation</i>, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>federation</i>: nhiều bên ký kết hợp lại — liên bang (nhà nước) '
    'hoặc liên đoàn (thể thao).</div>'
    '<div class="hd-warn"><b>Росси́йская Федера́ция</b> (РФ) là tên chính thức của nước Nga.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>федера́льный</b> thuộc liên bang</div>'
)

# ----------------------------------------------------------- способ
S["способ"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">tiền tố, không mang nghĩa riêng ở đây</span></div>'
    '<div class="hd-row"><span class="hd-piece">-по-соб</span>'
    '<span class="hd-gloss">GIÚP SỨC — như <b>посо́бие</b></span></div>'
    '<div class="hd-warn">⚠️ Mức tin: đây là từ nguyên, không phải luật suy ra được. Chắc chắn '
    'chỉ có một điều: <b>спо́соб</b> và <b>спосо́бный</b> cùng gốc.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cách = cái giúp mình làm được việc. «Bằng cách nào» dùng cách 5, '
    'không giới từ: <b>таки́м спо́собом</b> bằng cách này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спосо́бный</b> có năng lực · <b>спосо́бность</b> năng lực · '
    '<b>посо́бие</b> sách hướng dẫn, trợ cấp</div>'
)

# ----------------------------------------------------------- метод
S["метод"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn Hy Lạp <i>methodos</i> «con đường đi theo» — không chẻ trong tiếng Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>method</i>, trọng âm đầu: <b>ме́тод</b>. Thêm hậu tố thì trọng âm '
    'dời đi: <b>мето́дика</b>.</div>'
    '<div class="hd-warn"><b>ме́тод</b> là phương pháp CÓ HỆ THỐNG (khoa học, giảng dạy); '
    'cách làm bất kỳ hằng ngày là <b>спо́соб</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мето́дика</b> phương pháp (giảng dạy) · <b>методи́ческий</b> thuộc phương pháp</div>'
)

# ----------------------------------------------------------- решение
S["решение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">реш-</span>'
    '<span class="hd-gloss">QUYẾT, GIẢI — <b>реши́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ние</span>'
    '<span class="hd-gloss">→ danh từ, giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Kết quả của <b>реши́ть</b>: quyết một việc → quyết định; giải một bài → '
    'lời giải.</div>'
    '<div class="hd-warn">Ra quyết định là <b>приня́ть реше́ние</b> (nhận lấy), không phải '
    '«<i>make</i>» như tiếng Anh.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>реши́ть</b> / <b>реша́ть</b> quyết định, giải · '
    '<b>реши́тельный</b> kiên quyết</div>'
)

# ----------------------------------------------------------- понятие
S["понятие"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể, không thêm nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ня-</span>'
    '<span class="hd-gloss">NẮM, LẤY — như <b>поня́ть</b>, <b>приня́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-тие</span>'
    '<span class="hd-gloss">→ danh từ, giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái đầu óc «nắm» được = khái niệm. Tiếng Anh y hệt hình ảnh: '
    '<i>concept</i> từ Latin <i>capere</i> «nắm, lấy».</div>'
    '<div class="hd-warn"><b>Поня́тия не име́ю</b> = Tôi chẳng biết gì cả (cách 2 sau phủ định).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поня́ть</b> hiểu · <b>поня́тный</b> dễ hiểu · <b>поня́тно</b> hiểu rồi · '
    '<b>приня́ть</b> nhận</div>'
)

# ----------------------------------------------------------- ум
S["ум"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được — nhưng là gốc của cả họ «thông minh».</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trọng âm nhảy xuống đuôi ngay từ cách 2: <b>ум → ума́, уму́</b>.</div>'
    '<div class="hd-warn"><b>сойти́ с ума́</b> = phát điên: <b>Ты с ума́ сошёл?</b> Cậu điên à? '
    '· <b>в уме́</b> = nhẩm trong đầu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>у́мный</b> thông minh · <b>у́мница</b> người giỏi giang · '
    '<b>безу́мный</b> điên rồ · <b>разу́мный</b> hợp lý</div>'
)

# ----------------------------------------------------------- средство
S["средство"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сред-</span>'
    '<span class="hd-gloss">GIỮA — như <b>среди́</b>, <b>сре́дний</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ство</span>'
    '<span class="hd-gloss">→ danh từ, giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thứ đứng GIỮA mình và mục đích = phương tiện. Tiếng Anh cùng hình ảnh: '
    '<i>medium</i> (Latin <i>medius</i> «giữa»).</div>'
    '<div class="hd-warn">Số nhiều <b>сре́дства</b> thường là TIỀN, kinh phí · '
    '<b>сре́дство от</b> + cách 2 = thuốc trị: <b>сре́дство от ка́шля</b> thuốc ho.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сре́дний</b> trung bình · <b>среди́</b> giữa, trong số · '
    '<b>среда́</b> môi trường; thứ Tư</div>'
)

# ----------------------------------------------------------- принцип
S["принцип"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn Latin <i>principium</i> «khởi đầu» — không chẻ trong tiếng Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>principle</i>, trọng âm đầu: <b>при́нцип</b>.</div>'
    '<div class="hd-warn"><b>в при́нципе</b> = về cơ bản, nói chung là — câu đệm cực hay gặp '
    'trong khẩu ngữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>принципиа́льный</b> có nguyên tắc; thuộc nguyên tắc</div>'
)

# ----------------------------------------------------------- выбор
S["выбор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span>'
    '<span class="hd-gloss">RA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бор</span>'
    '<span class="hd-gloss">LẤY, NHẶT — gốc <b>брать</b> (бер-/бор-/бр-)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhặt ra một cái từ nhiều cái = lựa chọn. Trọng âm trên <b>вы́-</b> '
    'như động từ <b>вы́брать</b>.</div>'
    '<div class="hd-warn">Số nhiều <b>вы́боры</b> = cuộc BẦU CỬ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́брать</b> / <b>выбира́ть</b> chọn · <b>сбор</b> sự thu gom · '
    '<b>собра́ние</b> cuộc họp</div>'
)

# ----------------------------------------------------------- вариант
S["вариант"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn, gốc Latin <i>variare</i> «thay đổi» — không chẻ '
    'trong tiếng Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>variant</i>, nhưng hằng ngày rộng hơn nhiều: phương án, lựa chọn, '
    'phiên bản.</div>'
    '<div class="hd-warn"><b>Есть друго́й вариа́нт?</b> Có cách khác không? · '
    '<b>Э́то не вариа́нт</b> = Thế không được đâu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вариа́ция</b> biến thể, biến tấu</div>'
)

# ----------------------------------------------------------- представить
S["представить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пред-</span>'
    '<span class="hd-gloss">PHÍA TRƯỚC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-став-</span>'
    '<span class="hd-gloss">ĐẶT — như <b>ста́вить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть</span>'
    '<span class="hd-gloss">đuôi động từ, thể hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đặt ra trước mắt người khác → trình ra, giới thiệu; đặt ra trước mắt '
    'chính mình → hình dung. Ngôi «tôi» chêm <b>л</b>: <b>предста́влю</b>, còn lại '
    '<b>предста́вишь</b>…</div>'
    '<div class="hd-warn">«Tưởng tượng» phải có <b>себе́</b>: <b>Предста́вь себе́!</b> '
    '· Giới thiệu ai (cách 4) cho ai (cách 3).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>представля́ть</b> cặp chưa hoàn thành · <b>представи́тель</b> người '
    'đại diện · <b>представле́ние</b> buổi diễn; sự hình dung</div>'
)

# ----------------------------------------------------------- представлять
S["представлять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пред-</span>'
    '<span class="hd-gloss">PHÍA TRƯỚC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ставл-</span>'
    '<span class="hd-gloss">ĐẶT — <b>в</b> chêm <b>л</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я-ть</span>'
    '<span class="hd-gloss">hậu tố chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp chưa hoàn thành của <b>предста́вить</b> — cùng nghĩa, chia đều lớp 1: '
    '<b>представля́ю</b>, <b>представля́ешь</b>.</div>'
    '<div class="hd-warn"><b>Представля́ешь?</b> Cậu tin nổi không?! · <b>представля́ть собо́й</b> '
    '= là (văn viết).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>предста́вить</b> cặp hoàn thành · <b>представи́тель</b> người đại diện</div>'
)

# ----------------------------------------------------------- состояние
S["состояние"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-стоя-</span>'
    '<span class="hd-gloss">ĐỨNG — như <b>стоя́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ние</span>'
    '<span class="hd-gloss">→ danh từ, giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỗ mình đang «đứng» = trạng thái. Tiếng Anh cùng hình ảnh: <i>state</i> '
    'từ Latin <i>stare</i> «đứng». Nghĩa phụ: gia tài.</div>'
    '<div class="hd-warn"><b>быть в состоя́нии</b> + nguyên thể = có khả năng làm (trang trọng).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>состоя́ть</b> gồm có · <b>состоя́ться</b> diễn ra · <b>стоя́ть</b> đứng</div>'
)

# ----------------------------------------------------------- осторожный
S["осторожный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">QUANH mình</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сторож-</span>'
    '<span class="hd-gloss">CANH GÁC — <b>сто́рож</b> người gác</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tự canh gác quanh mình = cẩn thận. Dạng ngắn giống đực chêm <b>е</b>: '
    '<b>осторо́жен</b>.</div>'
    '<div class="hd-warn"><b>Осторо́жно!</b> = Cẩn thận! — câu loa tàu điện ngầm: '
    '<b>Осторо́жно, две́ри закрыва́ются</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>осторо́жно</b> cẩn thận · <b>осторо́жность</b> sự thận trọng · '
    '<b>сто́рож</b> người gác · <b>сторожи́ть</b> canh gác</div>'
)

# ----------------------------------------------------------- довольный
S["довольный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI, cho đủ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-во́ль-</span>'
    '<span class="hd-gloss">Ý MUỐN — <b>во́ля</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Được tới đủ ý muốn = hài lòng. Dạng ngắn giống đực chêm <b>е</b>: '
    '<b>дово́лен</b>.</div>'
    '<div class="hd-warn">Hài lòng VỚI cái gì = cách 5, không giới từ: <b>Я дово́лен рабо́той</b>.</div>'
    '<div class="hd-warn"><b>дово́льно</b> còn là «khá»: <b>дово́льно до́лго</b> khá lâu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>удово́льствие</b> niềm vui thích · <b>недово́льный</b> bất mãn · '
    '<b>во́ля</b> ý chí</div>'
)

# ----------------------------------------------------------- виноватый
S["виноватый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вин-</span>'
    '<span class="hd-gloss">LỖI — <b>вина́</b> (không dính tới <b>вино́</b> rượu vang)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова́т-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mang <b>вина́</b> trên người = có lỗi. Nói về chuyện gì: '
    '<b>винова́т в</b> + cách 6.</div>'
    '<div class="hd-warn"><b>Винова́т!</b> (nữ: <b>Винова́та!</b>) = Lỗi tôi! — một cách xin lỗi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вина́</b> lỗi · <b>извини́ть</b> tha lỗi · <b>обвиня́ть</b> buộc tội · '
    '<b>невино́вный</b> vô tội</div>'
)

# ----------------------------------------------------------- страх
S["страх"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được — nhưng là gốc của cả họ «sợ».</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Sợ cái gì: <b>страх</b> + cách 2 (<b>страх сме́рти</b>) hoặc '
    '<b>пе́ред</b> + cách 5.</div>'
    '<div class="hd-warn">Bảo hiểm cũng từ gốc này: <b>страхо́вка</b>, <b>страхова́ние</b> — '
    'thứ mua để khỏi phải sợ rủi ro.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стра́шный</b> đáng sợ · <b>стра́шно</b> sợ, khủng khiếp · '
    '<b>страхова́ть</b> bảo hiểm</div>'
)

# ----------------------------------------------------------- понятный
S["понятный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-ня-</span>'
    '<span class="hd-gloss">NẮM được — <b>поня́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-т-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thứ đầu óc nắm được = dễ hiểu. Dạng ngắn giống đực chêm <b>е</b>: '
    '<b>поня́тен</b>.</div>'
    '<div class="hd-warn"><b>Поня́тно!</b> = Hiểu rồi! — câu đáp quen thuộc nhất.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поня́ть</b> hiểu · <b>поня́тие</b> khái niệm · '
    '<b>непоня́тный</b> khó hiểu</div>'
)

B = {
    "docbangmat": 75,
    "loitubat": 3,
    "nguonsai": 0,
    "baolen": [
        "V представить -> 'trình ra, đệ trình, hình dung, tưởng tượng': RÚT «giới thiệu» (trùng посове́товать k97) và «nộp» (trùng сдать k98) theo luật chỉ rút phía mình; hệ quả là đề bài HT mất nghĩa «giới thiệu» (vẫn còn ở представлять CHT). Thêm «đệ trình, hình dung, tưởng tượng» theo gloss submit/imagine/picture — cần duyệt.",
        "V довольный -> 'hài lòng, mãn nguyện': RÚT «vui vẻ» (trùng весёлый k53), thêm «mãn nguyện» (gloss content) — cần duyệt.",
        "V khác: король/федерация/решение/средство đổi «;» thành «,»; thêm nghĩa có trong gloss: решение «lời giải» (thay «cách giải»), средство «phương thuốc» (remedy), вариант «phiên bản» (version), представлять «hình dung, tưởng tượng, đại diện», состояние «gia tài» (fortune) — cần duyệt.",
        "Đã tự chạy do_va_cham (đọc Anki, thay V của lô vào): trùng đủ 4 badge = 0. Không lọc badge thì còn cụm chung nghĩa nhưng badge tách: «cách» способ(đực)/средство(trung), «nguyên tắc» правило/принцип, «lựa chọn» вариант(n)/выбрать(v), «hình dung, tưởng tượng» представить/представлять (cặp thể).",
        "Không chắc: способ ← с- + по-соб (như посо́бие) là từ nguyên — đã gắn ô «⚠️ Mức tin» trên thẻ. король ← tên Karl ghi «theo từ nguyên phổ biến». средство ← сред- GIỮA viết khẳng định (khá chắc, đối chiếu Séc prostředek ← střed), luồng chính soát lại nếu muốn hạ mức tin.",
        "Thẻ cũ: состоя́ть khai «со- CÙNG» — tôi giữ y khuôn ở состояние cho nhất quán, nhưng trong состояние/состоять nghĩa «cùng» của со- đã mờ hẳn; nếu muốn chuẩn hơn thì sửa cả hai thành «tiền tố, nghĩa đã mờ».",
        "Họ hàng có ở cả 21 thẻ (kể cả từ mượn: контроль, федерация, метод, принцип, вариант đều có phái sinh thông dụng). Không nối король/роль, виноватый/вино (thẻ виноватый còn nói rõ là khác gốc), страх/страница, принцип/принять, вариант/варить.",
    ],
}
