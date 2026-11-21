# -*- coding: utf-8 -*-
"""k151 — concepts::state: luật pháp, toà án, tội phạm, nhà nước.

Chỗ cần nhất quán trong lô:
(1) gốc прав- = THẲNG, ĐÚNG — пра́во, пра́вильный, управле́ние (у-прав-, nhánh пра́вить điều khiển
    cho đúng → прави́тельство k89), khớp пра́вило (k115), пра́вильно (k51), испра́вить (k125).
(2) gốc -каз- = NÓI RA, CHỈ RA — прика́з (khớp приказа́ть k135), доказа́тельство (khớp доказа́ть k95).
(3) gốc хран- = CẤT GIỮ — охра́на, khớp храни́ть/сохрани́ть (k125).
(4) gốc вид- = THẤY — свиде́тель, khớp свида́ние (k33).
(5) gốc суд- = PHÁN XỬ — суд, судья́ (cả hai trong lô), khớp судьба́ (k119).
(6) gốc -ступ- = BƯỚC CHÂN — преступле́ние, престу́пник, khớp поступи́ть (k97).
(7) уби́йца/уби́йство: у- + бить, khớp уби́ть (k98).
Họ hàng cố ý vắng: шанс (từ mượn đứng một mình).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "правильный": "đúng, chính xác, đúng đắn, hợp quy tắc",   # bỏ «chính xác» (va то́чный); thêm «hợp quy tắc» từ gloss regular/proper
    "шанс": "cơ hội, khả năng",                    # «;» → «,»
    "жертва": "nạn nhân, vật hiến tế",             # «;» → «,»
    "охрана": "sự bảo vệ, sự canh gác, đội bảo vệ, sự bảo tồn",  # bỏ «sự bảo vệ» (va защи́та) + bỏ ngoặc «(đội)»; gloss guarding/guards/conservation
    "убийца": "kẻ sát nhân, hung thủ",             # «;» → «,»
    "суд": "toà án, phiên toà",                    # «;» → «,»
    "управление": "sự quản lý, sự điều khiển, cục",  # «;» → «,»
    "преступление": "tội ác, hành vi phạm tội",    # «tội» trơn dễ lẫn вина́; gloss crime/offence
    "обвинение": "lời buộc tội, cáo buộc",         # «;» → «,»
    "приказ": "lệnh, mệnh lệnh, chỉ thị",          # bỏ ngoặc «(hành chính)»; gloss order/command/directive
    "преступник": "tên tội phạm, kẻ phạm tội",     # «;» → «,»
    "право": "quyền, quyền hạn, luật, bằng lái xe",  # thêm «luật», «bằng lái xe» từ gloss law / driving licence
    "убийство": "vụ giết người, án mạng",          # «;» → «,»
    "доказательство": "bằng chứng, chứng cứ",      # «;» → «,»
    "свидетель": "người làm chứng, người chứng kiến",  # «;» → «,»
    "судья": "thẩm phán, trọng tài",               # «;» → «,»
}

# ----------------------------------------------------------------- право
S["право"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">прав-</span>'
    '<span class="hd-gloss">THẲNG, ĐÚNG — như <b>пра́вда</b>, <b>пра́вило</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Điều ĐÚNG mà mình được hưởng ⇒ quyền; cả hệ thống những điều đúng ⇒ luật: '
    '<b>права́ челове́ка</b> nhân quyền, <b>а́вторское пра́во</b> bản quyền. Số nhiều trọng âm '
    'nhảy xuống đuôi: <b>пра́во → права́</b>.</div>'
    '<div class="hd-warn"><b>име́ть пра́во на</b> + cách 4 = có quyền hưởng cái gì; '
    '<b>име́ть пра́во</b> + nguyên thể = có quyền làm gì.</div>'
    '<div class="hd-warn">Trong khẩu ngữ <b>права́</b> (số nhiều) = bằng lái xe: '
    '<b>У тебя́ есть права́?</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пра́вда</b> sự thật · <b>пра́вило</b> quy tắc · <b>пра́вый</b> bên phải, đúng · '
    '<b>прави́тельство</b> chính phủ</div>'
)

# ----------------------------------------------------------------- правильный
S["правильный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">прав-</span>'
    '<span class="hd-gloss">THẲNG, ĐÚNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ил-</span>'
    '<span class="hd-gloss">lấy từ <b>пра́вило</b> quy tắc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ьн-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Theo đúng quy tắc» ⇒ đúng: <b>пра́вильный отве́т</b> câu trả lời đúng, '
    '<b>пра́вильный глаго́л</b> động từ có quy tắc. Trạng từ là <b>пра́вильно</b>. Dạng ngắn giống đực '
    'chèn <b>е</b>: <b>пра́вилен</b>, còn lại theo đuôi — <b>пра́вильна, пра́вильны</b>.</div>'
    '<div class="hd-warn">«Cậu nói đúng» là <b>Ты прав</b> (dạng ngắn của <b>пра́вый</b>), không dùng '
    '<b>пра́вильный</b> cho người.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пра́вило</b> quy tắc · <b>пра́вильно</b> đúng · <b>пра́вый</b> bên phải, đúng · '
    '<b>испра́вить</b> sửa cho đúng</div>'
)

# ----------------------------------------------------------------- управление
S["управление"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố, nghĩa riêng đã mờ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-прав-</span>'
    '<span class="hd-gloss">THẲNG, ĐÚNG → <b>пра́вить</b> điều khiển cho đúng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-л-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>управля́ть</b> quản lý, lái: giữ cho mọi thứ chạy ĐÚNG hướng. '
    'Chữ <b>л</b> chèn sau <b>в</b> y như <b>испра́вить → исправля́ть</b>. Cũng là tên một cơ quan: '
    '<b>управле́ние поли́ции</b> sở cảnh sát.</div>'
    '<div class="hd-warn">Đi với cách 5, như động từ của nó: <b>управле́ние страно́й</b>, '
    '<b>управля́ть маши́ной</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>управля́ть</b> quản lý · <b>прави́тельство</b> chính phủ · '
    '<b>пра́вило</b> quy tắc · <b>пра́во</b> quyền, luật</div>'
)

# ----------------------------------------------------------------- суд
S["суд"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn <b>суд-</b> = PHÁN XỬ, không chẻ nhỏ hơn được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nơi PHÁN XỬ ⇒ toà án, và cả phiên toà. Mọi dạng khác trọng âm nằm ở đuôi, '
    'như <b>стол → стола́</b>: <b>суда́</b>, <b>в суде́</b>, <b>суды́</b>.</div>'
    '<div class="hd-warn">Kiện ai = nộp đơn VÀO toà, người bị kiện ở cách 4 sau <b>на</b>: '
    '<b>Он по́дал в суд на сосе́да.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>судья́</b> thẩm phán · <b>суди́ть</b> xét xử · <b>судьба́</b> số phận · '
    '<b>осуди́ть</b> kết án</div>'
)

# ----------------------------------------------------------------- судья
S["судья"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">суд-</span>'
    '<span class="hd-gloss">PHÁN XỬ — như <b>суд</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ья</span>'
    '<span class="hd-gloss">đuôi danh từ chỉ người</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người PHÁN XỬ ⇒ thẩm phán ở toà, trọng tài trên sân. Biến cách theo đuôi '
    '<b>-я</b> như <b>семья́</b>: số nhiều trọng âm lên đầu <b>су́дьи</b>, cách 2 số nhiều chèn '
    '<b>е</b> — <b>суде́й</b> (như <b>семе́й</b>).</div>'
    '<div class="hd-warn">Đuôi <b>-я</b> nhưng chỉ đàn ông thì tính từ theo giống đực: '
    '<b>стро́гий судья́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>суд</b> toà án · <b>суди́ть</b> xét xử · <b>судьба́</b> số phận</div>'
)

# ----------------------------------------------------------------- приказ
S["приказ"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">hướng TỚI người kia</span></div>'
    '<div class="hd-row"><span class="hd-piece">-каз</span>'
    '<span class="hd-gloss">NÓI RA, CHỈ RA — như <b>сказа́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>приказа́ть</b> ra lệnh, bỏ đuôi động từ đi là xong. '
    'Lệnh của cấp trên — quân đội, giám đốc: <b>прика́з дире́ктора</b>.</div>'
    '<div class="hd-warn"><b>по прика́зу</b> + cách 2 = theo lệnh của ai: '
    '<b>по прика́зу команди́ра</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>приказа́ть</b> ra lệnh · <b>сказа́ть</b> nói · <b>показа́ть</b> cho xem · '
    '<b>ука́з</b> sắc lệnh</div>'
)

# ----------------------------------------------------------------- доказательство
S["доказательство"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI tận đích</span></div>'
    '<div class="hd-row"><span class="hd-piece">-каз-</span>'
    '<span class="hd-gloss">ĐƯA RA CHO THẤY — như <b>показа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́тельство</span>'
    '<span class="hd-gloss">danh từ chỉ cái do việc đó tạo ra, như <b>обяза́тельство</b> nghĩa vụ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thứ đưa ra cho thấy tới tận cùng ⇒ bằng chứng; danh từ của <b>доказа́ть</b> '
    'chứng minh. Ở toà hay dùng số nhiều: <b>доказа́тельства</b> chứng cứ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>доказа́ть</b> chứng minh · <b>дока́зывать</b> chứng minh (CHT) · '
    '<b>показа́ть</b> cho xem · <b>прика́з</b> mệnh lệnh</div>'
)

# ----------------------------------------------------------------- охрана
S["охрана"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">QUANH, bao lấy</span></div>'
    '<div class="hd-row"><span class="hd-piece">-хран-</span>'
    '<span class="hd-gloss">CẤT GIỮ — như <b>храни́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giữ vòng quanh cho khỏi mất ⇒ canh gác. Cũng chỉ chính những người canh: '
    '<b>Позови́те охра́ну!</b> Gọi bảo vệ đi! Và bảo tồn: <b>охра́на приро́ды</b>.</div>'
    '<div class="hd-warn"><b>охра́на</b> = canh giữ thường trực; <b>защи́та</b> = chống đỡ khi bị '
    'tấn công.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>охраня́ть</b> canh gác · <b>охра́нник</b> nhân viên bảo vệ · '
    '<b>храни́ть</b> cất giữ · <b>сохрани́ть</b> lưu lại</div>'
)

# ----------------------------------------------------------------- свидетель
S["свидетель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">CÙNG, có mặt cùng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вид-е-</span>'
    '<span class="hd-gloss">THẤY — như <b>ви́деть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-тель</span>'
    '<span class="hd-gloss">NGƯỜI làm việc đó, như <b>учи́тель</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người có mặt và đã THẤY ⇒ nhân chứng. Cùng khuôn <b>с- + вид-</b> với '
    '<b>свида́ние</b> «cùng nhìn thấy nhau». Ở đám cưới Nga, <b>свиде́тель</b> là người đứng làm chứng '
    'bên chú rể.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ви́деть</b> thấy · <b>свида́ние</b> cuộc hẹn · '
    '<b>свиде́тельство</b> giấy chứng nhận</div>'
)

# ----------------------------------------------------------------- преступление
S["преступление"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пре-</span>'
    '<span class="hd-gloss">VƯỢT QUA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ступ-</span>'
    '<span class="hd-gloss">BƯỚC CHÂN — như <b>поступи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-л-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bước VƯỢT QUA lằn ranh của luật ⇒ tội ác: <b>преступи́ть зако́н</b> = phạm luật. '
    '<b>л</b> chèn sau <b>п</b> như <b>поступлю́</b>. Tên tiểu thuyết Dostoevsky: '
    '<b>«Преступле́ние и наказа́ние»</b> Tội ác và hình phạt.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>престу́пник</b> tội phạm · <b>престу́пность</b> tình hình tội phạm · '
    '<b>поступи́ть</b> hành động, vào học · <b>посту́пок</b> việc làm</div>'
)

# ----------------------------------------------------------------- преступник
S["преступник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пре-</span>'
    '<span class="hd-gloss">VƯỢT QUA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ступ-</span>'
    '<span class="hd-gloss">BƯỚC CHÂN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ник</span>'
    '<span class="hd-gloss">NGƯỜI, như <b>рабо́тник</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Kẻ bước vượt lằn ranh của luật ⇒ tội phạm. Cùng gốc với '
    '<b>преступле́ние</b> — nhưng trọng âm khác chỗ: <b>престу́пник</b> nhấn <b>у</b>, '
    '<b>преступле́ние</b> nhấn <b>е</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>преступле́ние</b> tội ác · <b>престу́пность</b> tình hình tội phạm · '
    '<b>престу́пный</b> phạm pháp</div>'
)

# ----------------------------------------------------------------- убийца
S["убийца"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">làm cho mất đi — như <b>уби́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-бий-</span>'
    '<span class="hd-gloss">ĐÁNH — gốc của <b>бить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ца</span>'
    '<span class="hd-gloss">NGƯỜI, như <b>пья́ница</b> kẻ nghiện rượu</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Kẻ đã <b>уби́ть</b> — đánh cho mất mạng ⇒ kẻ giết người.</div>'
    '<div class="hd-warn">Chữ không đổi, nhưng tính từ và động từ quá khứ theo giới tính thật: '
    '<b>жесто́кий уби́йца</b> (đàn ông) · <b>жесто́кая уби́йца</b> (phụ nữ).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уби́йство</b> vụ giết người · <b>уби́ть</b> giết · <b>убива́ть</b> giết (CHT) · '
    '<b>бить</b> đánh</div>'
)

# ----------------------------------------------------------------- убийство
S["убийство"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-бий-</span>'
    '<span class="hd-gloss">đánh cho mất mạng — như <b>уби́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ство</span>'
    '<span class="hd-gloss">→ danh từ giống trung chỉ việc, sự kiện</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng thân với <b>уби́йца</b>: <b>-ца</b> là NGƯỜI làm, <b>-ство</b> là VỤ việc. '
    '<b>умы́шленное уби́йство</b> = tội cố ý giết người.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уби́йца</b> kẻ sát nhân · <b>уби́ть</b> giết · <b>убива́ть</b> giết (CHT) · '
    '<b>бить</b> đánh</div>'
)

# ----------------------------------------------------------------- обвинение
S["обвинение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">tiền tố, ở đây ≈ nhắm vào ai đó</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вин-</span>'
    '<span class="hd-gloss">LỖI, TỘI — như <b>вина́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gán LỖI vào một người ⇒ lời buộc tội. Danh từ của <b>обвини́ть</b> buộc tội; '
    'cùng gốc với <b>извини́те</b> «gỡ lỗi ra».</div>'
    '<div class="hd-warn">Buộc tội VỀ việc gì: <b>в</b> + cách 6 — '
    '<b>обвине́ние в уби́йстве</b> cáo buộc giết người.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вина́</b> lỗi · <b>винова́т</b> có lỗi · <b>обвиня́ть</b> buộc tội (CHT) · '
    '<b>обвиня́емый</b> bị cáo</div>'
)

# ----------------------------------------------------------------- жертва
S["жертва"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc cổ <b>жертв-</b> «dâng lễ cho thần», tiếng Nga hiện đại không chẻ nhỏ hơn '
    'được; <b>-а</b> là đuôi giống cái.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc là vật hiến tế; người bị «dâng» cho tai hoạ ⇒ nạn nhân: '
    '<b>же́ртвы ава́рии</b> nạn nhân vụ tai nạn.</div>'
    '<div class="hd-warn">Luôn là giống cái, kể cả khi nạn nhân là đàn ông: '
    '<b>Он стал же́ртвой обма́на.</b> Anh ta thành nạn nhân của một vụ lừa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>же́ртвовать</b> hy sinh, quyên góp · <b>поже́ртвование</b> khoản quyên góp</div>'
)

# ----------------------------------------------------------------- бомба
S["бомба"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn quốc tế (cùng gốc <i>bomb</i>), không chẻ được; đuôi <b>-а</b> ⇒ giống cái.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đọc ra là nhận ngay <i>bomb</i>. Chữ <b>б</b> cuối gốc mà tiếng Anh để câm thì '
    'tiếng Nga đọc rõ: <b>бо́мба</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бомби́ть</b> ném bom · <b>бомбёжка</b> trận ném bom</div>'
)

# ----------------------------------------------------------------- шанс
S["шанс"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn tiếng Pháp <i>chance</i>, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>chance</i> của tiếng Anh: <b>У меня́ есть шанс.</b> '
    'Nói về phần thắng thì hay dùng số nhiều: <b>ша́нсы на побе́ду</b> cơ hội thắng.</div>'
    '<div class="hd-warn"><b>шанс</b> = khả năng làm được; <b>слу́чай</b> = dịp, chuyện xảy ra.</div>'
)

# ----------------------------------------------------------------- федеральный
S["федеральный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">федер-</span>'
    '<span class="hd-gloss">LIÊN BANG — <b>федера́ция</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-альный</span>'
    '<span class="hd-gloss">đuôi tính từ của từ quốc tế (<i>-al</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>federal</i>. Nga là một liên bang: <b>Росси́йская Федера́ция</b>, nên chữ này '
    'có mặt khắp tên cơ quan nhà nước — <b>федера́льный зако́н</b> luật liên bang.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>федера́ция</b> liên bang</div>'
)

B = {
    "docbangmat": 74,
    "loitubat": 3,
    "nguonsai": 2,
    "baolen": [
        "V правильный «đúng, đúng đắn, hợp quy tắc»: bỏ «chính xác» (va то́чный); THÊM «hợp quy tắc» từ gloss regular/proper (правильный глагол). Vẫn chung «đúng» với ве́рный «đúng, trung thành» và пра́вый «bên phải, đúng» — cả danh sách khác nhau nên tôi giữ; bỏ «đúng» thì mất nghĩa chính — cần duyệt.",
        "V шанс «cơ hội, khả năng»: chỉ đổi «;» → «,». Chung «cơ hội» với слу́чай «trường hợp, dịp, cơ hội, sự việc» nhưng danh sách khác nhau. Rút gọn thành «khả năng» là mất nghĩa chính — cần duyệt; phương án lùi: «khả năng».",
        "V охрана «sự canh gác, đội bảo vệ, sự bảo tồn»: bỏ «sự bảo vệ» (va защи́та) và ngoặc «(đội)»; ba nghĩa lấy từ gloss guarding / guards / conservation — cần duyệt.",
        "V право: thêm «luật, bằng lái xe» (gloss law / driving licence; «bằng lái» chỉ ở số nhiều khẩu ngữ права́) — cần duyệt. V преступление: «tội» → «tội ác» cho khỏi lẫn вина́. V приказ: bỏ «quyết định (hành chính)», thêm «mệnh lệnh, chỉ thị» (gloss command/directive).",
        "Chưa chạy `vacham` (lệnh đó đọc Anki) — luồng chính soát lại va chạm cho các V mới: «tội ác», «lệnh», «luật», «đội bảo vệ».",
        "Nguồn sai (2): (a) TRONG AM LECH bảo пода́ть phải là по́дать — nouns.csv lấy nhầm danh từ cổ «thuế»; động từ đúng là пода́ть. Tôi viết lại câu cho khỏi in nguyên thể thay vì chép dấu sai. (b) BAT THUONG của суд ghi «trọng âm DỊCH ngay trong số ít» — gây hiểu lầm, thật ra chỉ là nhấn đuôi kiểu стол → стола́; thẻ viết theo cách đó.",
        "Lỗi tự bắt (3): уби́йца ví dụ «Она́ — уби́йца» không cho thấy hợp giống — đổi sang жесто́кий/жесто́кая уби́йца; свиде́тель chẻ «-е-тель» gán nhầm е — е thuộc thân ви́деть, sửa «-вид-е- · -тель»; шанс viết «khả năng thành công thì dùng số nhiều» — nói quá, hạ thành «hay dùng».",
        "Không chắc: свиде́тель — từ nguyên gốc là съвѣдѣтель (вѣдѣти «biết», tức ве́дать), về sau mới gắn với ви́деть; hai gốc cùng một gốc Ấn-Âu *weid-. Thẻ theo khuôn вид- THẤY như thẻ свида́ние (k33), không hạ mức tin. о- trong охра́на = «quanh» và об- trong обвине́ние ≈ «nhắm vào» là cách đọc nghĩa tiền tố, đã viết dè dặt.",
        "Họ hàng cố ý vắng: шанс (từ mượn đứng một mình). Không thấy thẻ cũ nào khai lệch với khuôn прав-/хран-/-каз-/вид-/суд- được giao.",
    ],
}
