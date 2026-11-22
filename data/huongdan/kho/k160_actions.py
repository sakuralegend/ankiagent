# -*- coding: utf-8 -*-
"""k160 — actions: 11 cặp/nhóm động từ hành động + 2 danh từ cùng họ.

Chỗ cần nhất quán trong lô:
(1) gốc держ- GIỮ, CẦM — подде́ржка, đúng khuôn thẻ держа́ть (k94).
(2) gốc мен- ĐỔI, из- RA KHỎI — измене́ние, đúng khuôn измени́ть (k95).
(3) gốc ста- ĐỨNG — доста́ть/достава́ть (до- TỚI), khớp доста́точно (k116), стать (k113).
    Khuôn -ва- rụng ở hiện tại (достаю́) giải thích trên thẻ достава́ть.
(4) gốc стро- XÂY, DỰNG, sắp đặt — устро́ить/устра́ивать, đúng khuôn стро́ить (k85).
    Đề tiếng Việt cố ý KHÔNG có «tổ chức» (đã thuộc организова́ть/организо́вывать, k131).
(5) gốc станов- ĐỨNG VÀO chỗ — установи́ть/устана́вливать, khớp станови́ться (k113).
(6) gốc вяз- BUỘC — связа́ть/свя́зывать, khớp связь (k05).
(7) gốc бег-/беж- CHẠY — сбега́ть/сбежа́ть, khớp бежа́ть (k94), бе́гать (k131).
    сбега́ть ở lô này = «chạy trốn» (CHT của сбежа́ть), KHÔNG phải đồng tự сбе́гать «chạy đi một chuyến».
(8) gốc мет- DẤU — отме́тить/отмеча́ть, khớp отме́тка (k141).
(9) ничто́ «không gì» — уничто́жить/уничтожа́ть, khớp ничто́ (k154).
Báo oan của máy đã bỏ: прекрати́ть↔прекра́сный (gốc крат- NGẮN ≠ крас-), устана́вливать↔уста́ть,
доста́ть↔мо́лодость/ра́дость/статья́.
Họ hàng: không thẻ nào vắng.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "доставать": "lấy ra, rút ra, với tới, kiếm được, làm phiền",      # thiếu reach/obtain/pester từ gloss
    "достать": "lấy ra, rút ra, với tới, kiếm được, làm phiền",        # cùng bộ với cặp thể; badge tách
    "устраивать": "sắp xếp, thu xếp, bố trí, bày ra, xếp chỗ, xếp việc, hợp ý",  # bỏ «tổ chức» — nằm gọn trong организо́вывать
    "устроить": "sắp xếp, thu xếp, bố trí, bày ra, xếp chỗ, xếp việc, hợp ý",    # bỏ «tổ chức» — nằm gọn trong организова́ть
    "устанавливать": "lắp đặt, cài đặt, thiết lập, ấn định, xác định",  # bỏ «(đang/thường)» — nhãn thể
    "установить": "lắp đặt, cài đặt, thiết lập, ấn định, xác định",     # thêm establish/fix/ascertain
    "действовать": "hành động, có tác dụng, hoạt động, có hiệu lực",     # thêm work / be in force
    "связать": "buộc, trói, nối, liên kết, kết nối, đan",               # thêm tie/knit/put in touch
    "связывать": "buộc, trói, nối, liên kết, kết nối, gắn với",         # bỏ «bó lại»; thêm connect/associate
    "сбегать": "chạy trốn, bỏ trốn, chạy xuống",                        # bỏ «hay» — nhãn thể trá hình; run down
    "сбежать": "chạy trốn, bỏ trốn, chạy xuống",                        # run down
    "уничтожать": "tiêu diệt, phá huỷ, huỷ diệt, xoá bỏ",               # bỏ «(thường xuyên)»; abolish
    "уничтожить": "tiêu diệt, phá huỷ, huỷ diệt, xoá bỏ",               # abolish
    "возникать": "nảy sinh, phát sinh, xuất hiện",                      # bỏ «hay» — nhãn thể trá hình
    "возникнуть": "nảy sinh, phát sinh, xuất hiện, nảy ra",             # thêm cross one's mind
    "отметить": "đánh dấu, ghi nhận, nhắc đến, lưu ý, kỷ niệm, ăn mừng",    # thiếu celebrate
    "отмечать": "đánh dấu, ghi nhận, nhắc đến, lưu ý, kỷ niệm, ăn mừng",    # thiếu mark/celebrate
    "прекратить": "chấm dứt, ngừng, dừng lại, cắt đứt",                 # thêm cease/sever
    "взглянуть": "liếc nhìn, nhìn qua, xem qua, nhìn nhận",             # bỏ «một cái» — nhãn thể trá hình
}

# --------------------------------------------------------------------- поддержка
S["поддержка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span>'
    '<span class="hd-gloss">DƯỚI — đỡ từ bên dưới</span></div>'
    '<div class="hd-row"><span class="hd-piece">-держ-</span>'
    '<span class="hd-gloss">gốc GIỮ, CẦM — <b>держа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">→ danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giữ từ bên DƯỚI cho khỏi ngã ⇒ sự đỡ, sự ủng hộ — cùng cấu tạo tiếng Anh '
    '<i>support</i> (<i>sub-</i> «dưới» + <i>portare</i> «mang»). Cách 2 số nhiều chêm <b>е</b>: '
    '<b>подде́ржек</b>.</div>'
    '<div class="hd-warn"><b>техни́ческая подде́ржка</b> — bộ phận hỗ trợ kỹ thuật (của app, '
    'trang web).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поддержа́ть</b> · <b>подде́рживать</b> ủng hộ, đỡ · '
    '<b>держа́ть</b> giữ, cầm · <b>держа́ться</b> bám vào</div>'
)

# --------------------------------------------------------------------- изменение
S["изменение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">из-</span>'
    '<span class="hd-gloss">RA KHỎI (trạng thái cũ)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мен-</span>'
    '<span class="hd-gloss">ĐỔI — như <b>меня́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>измени́ть</b>: sự vật bị đổi cho ra khỏi dáng cũ ⇒ sự thay '
    'đổi. Rất hay ở số nhiều: <b>измене́ния</b> những thay đổi; <b>измене́ние кли́мата</b> biến '
    'đổi khí hậu.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>переме́на</b>: cũng là «thay đổi» nhưng nhấn ĐỔI SANG cái '
    'khác, và ở trường còn là giờ ra chơi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>измени́ть</b> · <b>изменя́ть</b> thay đổi · <b>измени́ться</b> tự thay '
    'đổi · <b>изме́на</b> sự phản bội · <b>меня́ть</b> đổi</div>'
)

# --------------------------------------------------------------------- доставать
S["доставать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ста-</span>'
    '<span class="hd-gloss">ĐỨNG — gốc của <b>стать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва́-ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vươn TỚI được ⇒ với lấy, lấy ra (<b>достава́ть ключи́ из су́мки</b> lấy '
    'chìa khoá ra khỏi túi), kiếm được. Hiện tại RỤNG <b>-ва-</b>: <b>достаю́, достаёшь</b> — cùng '
    'khuôn <b>дава́ть → даю́</b>, <b>встава́ть → встаю́</b>. Cặp HT: <b>доста́ть</b>.</div>'
    '<div class="hd-warn"><b>достава́ть до</b> + cách 2 — với tới: <b>Я не достаю́ до по́лки</b> '
    'tôi không với tới cái kệ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>доста́ть</b> lấy ra (HT) · <b>доста́точно</b> đủ · '
    '<b>встава́ть</b> đứng dậy · <b>стать</b> trở thành</div>'
)

# --------------------------------------------------------------------- достать
S["достать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ста-ть</span>'
    '<span class="hd-gloss">ĐỨNG — như <b>стать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vươn TỚI được ⇒ với tới, lấy ra; thứ khó tìm thì là kiếm được, xoay được: '
    '<b>доста́ть биле́ты</b> kiếm được vé. Tương lai mọc <b>н</b>, y như <b>стать → ста́ну</b>: '
    '<b>доста́ну, доста́нешь</b>. Cặp CHT: <b>достава́ть</b>.</div>'
    '<div class="hd-warn"><b>Ты меня́ доста́л!</b> — mày làm tao phát bực rồi! (khẩu ngữ: «với tới» '
    'giới hạn chịu đựng).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>достава́ть</b> lấy ra (CHT) · <b>доста́точно</b> đủ — «với tới được '
    'mức cần» · <b>стать</b> trở thành</div>'
)

# --------------------------------------------------------------------- устраивать
S["устраивать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố, không mang nghĩa riêng rõ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-стра́и-</span>'
    '<span class="hd-gloss">= <b>стро-</b> gốc XÂY, DỰNG, sắp đặt (о → а)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва-ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dựng cho đâu vào đấy ⇒ sắp xếp, thu xếp, bày ra: <b>устра́ивать пра́здник</b> '
    'bày ra một buổi lễ. Thể CHT đổi <b>о → а</b> trước <b>-ива-</b>: <b>устро́ить → устра́ивать</b>, '
    'cùng khuôn <b>успоко́ить → успока́ивать</b>. Chia đều: <b>устра́иваю</b>.</div>'
    '<div class="hd-warn"><b>Меня́ э́то устра́ивает</b> — cái đó hợp với tôi, tôi thấy ổn (vật làm '
    'chủ ngữ, người ở cách 4).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>устро́ить</b> sắp xếp (HT) · <b>стро́ить</b> xây · <b>устро́йство</b> '
    'thiết bị, cơ cấu · <b>устро́иться</b> ổn định chỗ, xin được việc</div>'
)

# --------------------------------------------------------------------- устроить
S["устроить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố, không mang nghĩa riêng rõ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-стро-</span>'
    '<span class="hd-gloss">gốc XÂY, DỰNG, sắp đặt — <b>стро́ить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dựng xong cho đâu vào đấy ⇒ sắp xếp, thu xếp; xếp cả chỗ, việc cho người '
    'khác: <b>устро́ить сы́на на рабо́ту</b> xin việc cho con trai. Chia như <b>стро́ить</b>: '
    '<b>устро́ю, устро́ишь</b>. Cặp CHT: <b>устра́ивать</b>.</div>'
    '<div class="hd-warn"><b>устро́ить сканда́л</b> — làm ầm lên, gây chuyện.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>устра́ивать</b> sắp xếp (CHT) · <b>стро́ить</b> xây · '
    '<b>устро́йство</b> thiết bị · <b>устро́иться</b> xin được việc</div>'
)

# --------------------------------------------------------------------- устанавливать
S["устанавливать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố, không mang nghĩa riêng rõ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-стана́вл-</span>'
    '<span class="hd-gloss">= <b>станов-</b> ĐỨNG VÀO chỗ (о → а, в → вл)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho đứng vững vào chỗ ⇒ lắp đặt, cài: <b>устана́вливать '
    'програ́мму</b> cài phần mềm. Đứng vững ⇒ cũng là ấn định, thiết lập: <b>устана́вливать '
    'пра́вила</b> đặt ra luật. Chia đều: <b>устана́вливаю</b>. Cặp HT: <b>установи́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>установи́ть</b> lắp đặt (HT) · <b>устано́вка</b> sự lắp đặt · '
    '<b>станови́ться</b> trở nên · <b>останови́ть</b> dừng lại · <b>ста́вить</b> đặt đứng</div>'
)

# --------------------------------------------------------------------- установить
S["установить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố, không mang nghĩa riêng rõ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-станов-</span>'
    '<span class="hd-gloss">ĐỨNG VÀO chỗ — như <b>станови́ться</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đặt cho đứng vững vào chỗ ⇒ lắp đặt, cài đặt; ấn định, thiết lập. Ngôi '
    '«tôi» thêm <b>л</b> rồi trọng âm lùi: <b>установлю́, устано́вишь</b> — y như '
    '<b>становлю́сь, стано́вишься</b>. Cặp CHT: <b>устана́вливать</b>.</div>'
    '<div class="hd-warn"><b>Устано́влено, что…</b> — Đã xác định được rằng… (văn báo chí, khoa '
    'học).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>устана́вливать</b> lắp đặt (CHT) · <b>устано́вка</b> sự lắp đặt · '
    '<b>станови́ться</b> trở nên · <b>ста́вить</b> đặt đứng</div>'
)

# --------------------------------------------------------------------- действовать
S["действовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">действ-</span>'
    '<span class="hd-gloss">HÀNH ĐỘNG — như <b>де́йствие</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ть</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người thì hành động; máy, thuốc, luật thì «đang hoạt động, còn hiệu lực»: '
    '<b>Лифт не де́йствует</b> thang máy không chạy. Hiện tại <b>-ова- → -у-</b>: '
    '<b>де́йствую, де́йствуешь</b> (như <b>рисова́ть → рису́ю</b>). Cặp HT: '
    '<b>поде́йствовать</b>.</div>'
    '<div class="hd-warn"><b>де́йствовать на</b> + cách 4 — tác động lên: <b>Э́то де́йствует мне на '
    'не́рвы</b> cái đó làm tôi phát bực.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поде́йствовать</b> có tác dụng (HT) · <b>де́йствие</b> hành động, tác '
    'dụng · <b>действи́тельно</b> thật sự</div>'
)

# --------------------------------------------------------------------- подействовать
S["подействовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố HT, không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-действ-ова-ть</span>'
    '<span class="hd-gloss">HÀNH ĐỘNG, tác động — <b>де́йствовать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp HT của <b>де́йствовать</b>, gần như chỉ dùng theo nghĩa «đã có tác '
    'dụng»: <b>Лека́рство поде́йствовало</b> thuốc đã có tác dụng. Chia: <b>поде́йствую, '
    'поде́йствуешь</b>.</div>'
    '<div class="hd-warn">Tác động lên AI: <b>на</b> + cách 4 — <b>Его́ слова́ на меня́ '
    'поде́йствовали</b> lời anh ấy đã tác động đến tôi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>де́йствовать</b> hành động (CHT) · <b>де́йствие</b> tác dụng · '
    '<b>действи́тельно</b> thật sự</div>'
)

# --------------------------------------------------------------------- связать
S["связать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">gộp lại với nhau</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вяз-</span>'
    '<span class="hd-gloss">BUỘC, THẮT — <b>вяза́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Buộc hai thứ lại với nhau ⇒ buộc, trói; rồi nối, liên kết (<b>с</b> + cách '
    '5). Nghĩa «đan» của <b>вяза́ть</b> vẫn còn: <b>связа́ть сви́тер</b> đan xong cái áo len. '
    'Tương lai <b>з → ж</b> ở MỌI ngôi, trọng âm lùi từ ngôi hai: <b>свяжу́, свя́жешь</b>.</div>'
    '<div class="hd-warn"><b>связа́ться с</b> + cách 5 — liên lạc với ai: <b>Я свяжу́сь с ва́ми</b> '
    'tôi sẽ liên lạc với anh.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>свя́зывать</b> buộc, nối (CHT) · <b>связь</b> mối liên hệ, liên lạc · '
    '<b>вяза́ть</b> buộc, đan</div>'
)

# --------------------------------------------------------------------- связывать
S["связывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">gộp lại với nhau</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вяз-</span>'
    '<span class="hd-gloss">BUỘC, THẮT — <b>вяза́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>связа́ть</b>: <b>-ыва-</b> kéo trọng âm về gốc, chia đều '
    '<b>свя́зываю</b>, không còn <b>ж</b>. Hay dùng cho mối dây vô hình: <b>Что нас свя́зывает?</b> '
    'Điều gì gắn chúng ta với nhau? · <b>свя́зывать с</b> + cách 5 = gắn (trong đầu) với.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>связа́ть</b> buộc, nối (HT) · <b>связь</b> mối liên hệ · '
    '<b>вяза́ть</b> buộc, đan</div>'
)

# --------------------------------------------------------------------- сбегать
S["сбегать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">RỜI KHỎI, từ trên xuống</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бег-</span>'
    '<span class="hd-gloss">CHẠY — như <b>бе́гать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chạy RỜI KHỎI ⇒ chạy trốn, bỏ trốn; chạy từ trên xuống: <b>сбега́ть по '
    'ле́стнице</b> chạy xuống cầu thang. Cặp CHT của <b>сбежа́ть</b>, chia đều: <b>сбега́ю, '
    'сбега́ешь</b>.</div>'
    '<div class="hd-warn">Đồng tự khác trọng âm: <b>сбе́гать</b> (nhấn <b>бе́</b>, HT) = chạy đi một '
    'chuyến rồi về — <b>сбе́гать в магази́н</b> chạy ra cửa hàng. Nhấn <b>га́</b> là TRỐN.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сбежа́ть</b> chạy trốn (HT) · <b>бе́гать</b> chạy · '
    '<b>убега́ть</b> bỏ chạy · <b>побе́г</b> cuộc trốn chạy</div>'
)

# --------------------------------------------------------------------- сбежать
S["сбежать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">RỜI KHỎI, từ trên xuống</span></div>'
    '<div class="hd-row"><span class="hd-piece">-беж-</span>'
    '<span class="hd-gloss">CHẠY — như <b>бежа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chạy rời khỏi ⇒ trốn thoát: <b>сбежа́ть из тюрьмы́</b> vượt ngục, '
    '<b>сбежа́ть с уро́ка</b> trốn tiết. Chia trộn hai gốc y như <b>бежа́ть</b>: <b>сбегу́, '
    'сбежи́шь, сбегу́т</b> — chỉ «tôi» và «họ» mang <b>г</b>. Cặp CHT: <b>сбега́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сбега́ть</b> chạy trốn (CHT) · <b>бежа́ть</b> chạy · '
    '<b>убежа́ть</b> chạy mất · <b>побе́г</b> cuộc trốn chạy</div>'
)

# --------------------------------------------------------------------- уничтожать
S["уничтожать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">làm cho thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ничтож-</span>'
    '<span class="hd-gloss">KHÔNG GÌ — <b>ничто́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Biến thành KHÔNG CÒN GÌ ⇒ tiêu diệt, huỷ diệt — đúng cấu tạo tiếng Anh '
    '<i>annihilate</i> (Latin <i>nihil</i> «không gì»). Chia đều: <b>уничтожа́ю, '
    'уничтожа́ешь</b>. Cặp HT: <b>уничто́жить</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уничто́жить</b> tiêu diệt (HT) · <b>ничто́</b> không gì · '
    '<b>ничто́жный</b> nhỏ mọn, vô giá trị · <b>уничтоже́ние</b> sự tiêu diệt</div>'
)

# --------------------------------------------------------------------- уничтожить
S["уничтожить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">làm cho thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ничтож-</span>'
    '<span class="hd-gloss">KHÔNG GÌ — <b>ничто́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho thành <b>ничто́</b> ⇒ huỷ diệt sạch: <b>уничто́жить врага́</b> '
    'tiêu diệt kẻ thù, <b>уничто́жить докуме́нты</b> huỷ tài liệu. Chia đều, trọng âm đứng yên: '
    '<b>уничто́жу, уничто́жишь</b>. Cặp CHT: <b>уничтожа́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уничтожа́ть</b> tiêu diệt (CHT) · <b>ничто́</b> không gì · '
    '<b>ничто́жный</b> nhỏ mọn · <b>уничтоже́ние</b> sự tiêu diệt</div>'
)

# --------------------------------------------------------------------- возникать
S["возникать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">воз-</span>'
    '<span class="hd-gloss">LÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ник-</span>'
    '<span class="hd-gloss">gốc «cúi rạp xuống» — <b>воз-</b> đảo chiều: ngóc lên</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trồi LÊN ⇒ nảy sinh, phát sinh: <b>Ча́сто возника́ют пробле́мы</b> vấn đề '
    'hay nảy sinh. Chủ ngữ là cái nảy sinh, không phải người. Chia đều: <b>возника́ет</b>. Cặp HT: '
    '<b>возни́кнуть</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: nghĩa «cúi rạp» của <b>-ник-</b> là từ nguyên, không phải luật '
    'suy ra được. Chắc chắn chỉ có: <b>прони́кнуть</b> «thâm nhập» cùng khuôn <b>-никнуть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>возни́кнуть</b> nảy sinh (HT) · <b>возникнове́ние</b> sự nảy sinh · '
    '<b>прони́кнуть</b> thâm nhập</div>'
)

# --------------------------------------------------------------------- возникнуть
S["возникнуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">воз-</span>'
    '<span class="hd-gloss">LÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ник-</span>'
    '<span class="hd-gloss">gốc trồi ra (xem thẻ <b>возника́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ну-ть</span>'
    '<span class="hd-gloss">đuôi HT</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp HT của <b>возника́ть</b>. Quá khứ RỤNG <b>-ну-</b>: <b>возни́к, '
    'возни́кла, возни́кли</b> — cùng khuôn <b>исче́знуть → исче́з</b> (biến mất). Dạng '
    '<b>возни́кнул</b> cũng có nhưng hiếm.</div>'
    '<div class="hd-warn"><b>У меня́ возни́к вопро́с</b> — tôi nảy ra một câu hỏi: người ở '
    '<b>у</b> + cách 2, câu hỏi làm chủ ngữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>возника́ть</b> nảy sinh (CHT) · <b>возникнове́ние</b> sự nảy sinh · '
    '<b>прони́кнуть</b> thâm nhập</div>'
)

# --------------------------------------------------------------------- отметить
S["отметить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">tách ra, ghi riêng ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мет-</span>'
    '<span class="hd-gloss">DẤU — <b>ме́тка</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đặt dấu riêng lên ⇒ đánh dấu, ghi nhận, nhắc đến. Đánh dấu một ngày trong '
    'năm ⇒ kỷ niệm, ăn mừng. <b>т → ч</b> chỉ ở ngôi «tôi»: <b>отме́чу, отме́тишь</b>. Cặp CHT: '
    '<b>отмеча́ть</b>.</div>'
    '<div class="hd-warn"><b>отме́тить день рожде́ния</b> — mừng sinh nhật (thường là tụ tập ăn '
    'uống).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отмеча́ть</b> đánh dấu (CHT) · <b>отме́тка</b> điểm, dấu · '
    '<b>ме́тка</b> dấu, nhãn · <b>заме́тить</b> nhận ra</div>'
)

# --------------------------------------------------------------------- отмечать
S["отмечать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">tách ra, ghi riêng ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">-меч-</span>'
    '<span class="hd-gloss">= <b>мет-</b> DẤU (т → ч)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>отме́тить</b>: đuôi <b>-а́ть</b> mang <b>ч</b> suốt mọi '
    'dạng, chia đều <b>отмеча́ю</b> — đúng khuôn <b>заме́тить → замеча́ть</b>. Hai nghĩa hay gặp: '
    '<b>отмеча́ть в спи́ске</b> đánh dấu trong danh sách · <b>отмеча́ть Но́вый год</b> đón mừng '
    'năm mới.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отме́тить</b> đánh dấu (HT) · <b>отме́тка</b> điểm, dấu · '
    '<b>ме́тка</b> dấu, nhãn · <b>замеча́ть</b> nhận thấy</div>'
)

# --------------------------------------------------------------------- прекратить
S["прекратить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пре-</span>'
    '<span class="hd-gloss">QUÁ, tới tận cùng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-крат-</span>'
    '<span class="hd-gloss">NGẮN — gốc của <b>кра́ткий</b>, <b>сократи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cắt ngắn tới tận cùng ⇒ chấm dứt hẳn. Ngôi «tôi» đổi <b>т → щ</b> (không '
    'phải ч): <b>прекращу́, прекрати́шь</b> — như <b>защити́ть → защищу́</b>. Cặp CHT '
    '<b>прекраща́ть</b> mang <b>щ</b> suốt.</div>'
    '<div class="hd-warn"><b>Прекрати́!</b> — Thôi ngay! Theo sau là cách 4 hoặc nguyên thể CHT: '
    '<b>прекрати́ть кури́ть</b> bỏ hút thuốc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прекраща́ть</b> chấm dứt (CHT) · <b>прекраще́ние</b> sự chấm dứt · '
    '<b>сократи́ть</b> rút ngắn · <b>кра́ткий</b> ngắn gọn</div>'
)

# --------------------------------------------------------------------- взглянуть
S["взглянуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вз-</span>'
    '<span class="hd-gloss">LÊN, hướng tới</span></div>'
    '<div class="hd-row"><span class="hd-piece">-гля-</span>'
    '<span class="hd-gloss">NHÌN — gốc <b>гляд-</b>, <b>д</b> rụng trước <b>-ну-</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ну́-ть</span>'
    '<span class="hd-gloss">làm MỘT cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Động từ của <b>взгляд</b>: đưa mắt nhìn một lần ⇒ liếc, nhìn qua; nhìn '
    'cái gì thì <b>на</b> + cách 4. Trọng âm lùi từ ngôi hai: <b>взгляну́, взгля́нешь</b>.</div>'
    '<div class="hd-warn"><b>взгляну́ть на ве́щи ина́че</b> — nhìn nhận mọi chuyện theo cách '
    'khác.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>взгляд</b> cái nhìn, quan điểm · <b>гляде́ть</b> nhìn · '
    '<b>гля́нуть</b> liếc một cái · <b>вы́глядеть</b> trông có vẻ</div>'
)

B = {
    "docbangmat": 143,
    "loitubat": 1,     # устра́ивать: ví dụ о→а ban đầu là спроси́ть→спра́шивать — kèm cả с→ш, dạy lẫn hai luật; đổi sang успоко́ить→успока́ивать
    "nguonsai": 1,     # CACH DUNG возникнуть «Возникнили проблемы с транспортной компаней» sai chính tả (đúng: Возникли … компанией) — không dùng
    "baolen": [
        "V cần duyệt: устро́ить/устра́ивать BỎ «tổ chức» (gloss có organize) để gỡ va chạm với организова́ть/организо́вывать (k131 đã nạp); tôi đánh giá arrange/sắp xếp là nghĩa chính nên bỏ được, hai thẻ cặp thể cùng một bộ nghĩa",
        "Mô phỏng do_va_cham trên toàn bộ thẻ RU_Word với V mới: 0 va chạm dính lô k160 (chung lẻ một nghĩa: «xác định» với определи́ть, «xuất hiện» với появи́ться, «hợp ý» với нра́виться — bình thường theo §2c)",
        "Không chắc: прекрати́ть chẻ -крат- NGẮN (cùng gốc кра́ткий, сократи́ть) — từ nguyên tôi khá chắc nên KHÔNG đặt ô Mức tin; luồng chính nên soát lại",
        "Không chắc: -ник- «cúi rạp» (ни́кнуть) ở возника́ть/возни́кнуть là từ nguyên — đã hạ mức tin bằng ô ⚠️ trên thẻ возника́ть",
        "сбега́ть: ô đỏ nhắc đồng tự сбе́гать «chạy đi một chuyến»; soat KHÔNG báo trọng âm lệch nên không đụng MIEN_TRU",
        "V sửa 19/22 thẻ (chủ yếu bỏ nhãn thể trá hình «hay», «(thường xuyên)», «(đang/thường)», «một cái» và thêm nghĩa gloss xác nhận); giữ nguyên поддержка, изменение, подействовать",
    ],
}
