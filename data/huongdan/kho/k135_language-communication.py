# -*- coding: utf-8 -*-
"""k135 — language::communication: danh từ và cặp thể động từ «nói, viết, dạy, ra lệnh».

Chỗ cần nhất quán trong lô:
(1) gốc пис- = VIẾT (записка, подписать/подписывать, описать/описывать) — khớp расписание
    (k126) và писать/записать đã soạn; с → ш ở thân hiện tại (пишу́, опишу́, подпишу́).
(2) gốc каз- = NÓI RA, CHỈ RA (приказать/приказывать) — khớp сказать (k54), показывать (k79);
    з → ж (прикажу́).
(3) gốc раз-/раж- = ĐÁNH, GIÁNG (выразить/выражать) — khớp поражение (k128); từ nguyên, hạ mức tin.
(4) gốc уч- = HỌC, DẠY (обучение ↔ изучение, ô đỏ phân biệt hai từ, mỗi thẻ một chiều).
(5) -ыва- kéo trọng âm lùi về trước: подпи́сывать, опи́сывать, прика́зывать (như пока́зывать).
Họ hàng: không thẻ nào cố ý vắng.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "подписать": "ký, ký tên",                    # bỏ «xong (một lần)» — nhãn thể trá hình
    "подписывать": "ký, ký tên",                  # bỏ «(thường xuyên)»
    "воспитание": "sự nuôi dạy, giáo dưỡng, gia giáo",  # bỏ «giáo dục» — dễ lẫn образова́ние; gloss có good manners/breeding
    "открытие": "phát hiện, khám phá, khai trương, khai mạc",  # «;» → «,»; gloss discovery/opening/unveiling
    "спутник": "vệ tinh, người đồng hành",        # «;» → «,»
    "беседа": "cuộc trò chuyện, buổi nói chuyện, cuộc trao đổi",  # «nói chuyện» trơn là động từ; gloss talk/discussion
    "приказать": "ra lệnh",                       # bỏ «(một lần)»
    "приказывать": "ra lệnh",                     # bỏ «(thường xuyên)»
    "описать": "mô tả, miêu tả",                  # bỏ «xong», «(một lần)»
    "описывать": "mô tả, miêu tả",                # bỏ «(thường xuyên)»
    "выражать": "bày tỏ, diễn đạt",               # RÚT «thể hiện» — trùng пока́зывать (đã nạp)
    "выразить": "bày tỏ, diễn đạt",               # bỏ «(xong)»
    "закричать": "kêu lên, la lên",               # RÚT «hét lên» — trùng кри́кнуть (k124, đã nạp)
}

# ----------------------------------------------------------------- записка
S["записка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">đưa VÀO, ghi lại (như <b>записа́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пис-</span>'
    '<span class="hd-gloss">gốc VIẾT — <b>писа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">→ danh từ giống cái, một VẬT nhỏ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Mẩu ghi lại bằng chữ» ⇒ tờ giấy nhắn để lại cho ai đó. '
    'Danh từ của chính <b>записа́ть</b> ghi lại.</div>'
    '<div class="hd-warn">Số nhiều cách 2 chen <b>о</b> vào giữa: <b>запи́сок</b> '
    '(như <b>ка́рточка → ка́рточек</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>записа́ть</b> ghi lại · <b>за́пись</b> bản ghi · '
    '<b>писа́ть</b> viết · <b>по́дпись</b> chữ ký</div>'
)

# ---------------------------------------------------------------- карточка
S["карточка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ка́рт-</span>'
    '<span class="hd-gloss">gốc <b>ка́рта</b> — tấm giấy cứng (Latin <i>charta</i>, '
    'cùng gốc <i>card, chart</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-очк-а</span>'
    '<span class="hd-gloss">đuôi thu nhỏ: tấm NHỎ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>ка́рта</b> là tấm lớn (bản đồ, lá bài) → thu nhỏ thành tấm vừa '
    'tay: thẻ, phiếu, thẻ ngân hàng. Số nhiều cách 2: <b>ка́рточек</b> (chen <b>е</b>).</div>'
    '<div class="hd-warn">Danh thiếp = <b>визи́тная ка́рточка</b>. Trả bằng thẻ = '
    '<b>плати́ть ка́рточкой</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ка́рта</b> bản đồ, lá bài · <b>ка́рточный</b> thuộc thẻ, thuộc bài</div>'
)

# --------------------------------------------------------------- подписать
S["подписать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span>'
    '<span class="hd-gloss">DƯỚI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пис-</span>'
    '<span class="hd-gloss">gốc VIẾT — <b>писа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">VIẾT ở DƯỚI văn bản ⇒ ký tên. Đúng hình ảnh tiếng Anh '
    '<i>sub-scribe</i> (Latin «viết dưới»). Cặp CHT: <b>подпи́сывать</b>.</div>'
    '<div class="hd-warn">Chia như <b>писа́ть</b>: <b>с → ш</b>, trọng âm lùi từ ngôi 2 — '
    '<b>я подпишу́, ты подпи́шешь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́дпись</b> chữ ký · <b>подписа́ться</b> đăng ký theo dõi · '
    '<b>подпи́ска</b> sự đặt mua dài hạn · <b>писа́ть</b> viết</div>'
)

# ------------------------------------------------------------- подписывать
S["подписывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-пис-</span>'
    '<span class="hd-gloss">viết ở DƯỚI = ký (xem <b>подписа́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-</span>'
    '<span class="hd-gloss">hậu tố biến hoàn thành → CHƯA hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ký đang diễn ra, ký nhiều lần: <b>Он подпи́сывает докуме́нты</b> = '
    'Anh ấy đang ký giấy tờ. Chia đều, không đổi phụ âm: <b>подпи́сываю</b>.</div>'
    '<div class="hd-warn">Thêm <b>-ыва-</b> thì trọng âm nhảy về trước: '
    '<b>подписа́ть → подпи́сывать</b>, y như <b>показа́ть → пока́зывать</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>подписа́ть</b> ký (HT) · <b>по́дпись</b> chữ ký · '
    '<b>опи́сывать</b> mô tả · <b>запи́сывать</b> ghi lại</div>'
)

# -------------------------------------------------------------- воспитание
S["воспитание"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вос-</span>'
    '<span class="hd-gloss">LÊN (dạng của <b>воз-</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пит-</span>'
    '<span class="hd-gloss">NUÔI — gốc của <b>пита́ние</b> dinh dưỡng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ание</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«NUÔI cho LỚN LÊN» ⇒ nuôi dạy con, dạy nết. Nên nó còn chỉ '
    'chính cái nết được dạy: người <b>без воспита́ния</b> = người thiếu gia giáo.</div>'
    '<div class="hd-warn">Khác <b>обуче́ние</b> (dạy KIẾN THỨC, kỹ năng): '
    '<b>воспита́ние</b> là dạy NẾT, dạy cách làm người.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>воспита́ть</b> nuôi dạy · <b>воспита́тель</b> cô giáo mầm non · '
    '<b>воспи́танный</b> lễ phép · <b>пита́ние</b> dinh dưỡng</div>'
)

# ---------------------------------------------------------------- обучение
S["обучение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">tiền tố HT, không tách ra nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-уч-</span>'
    '<span class="hd-gloss">gốc HỌC, DẠY — <b>учи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>обучи́ть</b> dạy cho ai một kỹ năng ⇒ việc dạy, '
    'việc đào tạo: <b>обуче́ние води́телей</b> đào tạo tài xế.</div>'
    '<div class="hd-warn">Hướng NGƯỜI DẠY → học trò. Người học tự đào sâu một môn thì là '
    '<b>изуче́ние</b>: <b>изуче́ние ру́сского языка́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>учи́ть</b> dạy, học thuộc · <b>учи́тель</b> giáo viên · '
    '<b>изуче́ние</b> việc nghiên cứu · <b>учёба</b> việc học</div>'
)

# ---------------------------------------------------------------- изучение
S["изучение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">из-</span>'
    '<span class="hd-gloss">RA HẾT, thấu tới cùng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-уч-</span>'
    '<span class="hd-gloss">gốc HỌC — <b>учи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Học cho THẤU» ⇒ việc học kỹ, việc nghiên cứu một đối tượng. '
    'Danh từ của <b>изуча́ть</b>; đối tượng đứng sau ở cách 2: '
    '<b>изуче́ние ко́смоса</b>.</div>'
    '<div class="hd-warn">Đây là phía NGƯỜI HỌC. Phía người dạy, đào tạo người khác là '
    '<b>обуче́ние</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>изуча́ть</b> nghiên cứu · <b>изучи́ть</b> nghiên cứu (HT) · '
    '<b>учи́ть</b> học thuộc, dạy · <b>обуче́ние</b> việc đào tạo</div>'
)

# ---------------------------------------------------------------- открытие
S["открытие"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-кры-</span>'
    '<span class="hd-gloss">gỡ cái CHE ra — chính là <b>откры́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-тие</span>'
    '<span class="hd-gloss">→ danh từ giống trung, từ động từ đuôi <b>-ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai nghĩa đi đúng hai nghĩa của <b>откры́ть</b>: mở cửa (lễ khai '
    'trương, khai mạc) và gỡ màn bí mật — y như tiếng Anh <i>dis-cover-y</i>: '
    '<b>откры́тие Аме́рики</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>откры́ть</b> mở · <b>открыва́ть</b> mở (CHT) · '
    '<b>откры́тка</b> bưu thiếp · <b>закры́тие</b> sự đóng cửa</div>'
)

# ----------------------------------------------------------------- спутник
S["спутник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">CÙNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пут-</span>'
    '<span class="hd-gloss">ĐƯỜNG — gốc của <b>путь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ник</span>'
    '<span class="hd-gloss">→ NGƯỜI / vật làm việc đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Kẻ CÙNG ĐƯỜNG» ⇒ bạn đồng hành; vật cứ bay cùng đường quanh hành '
    'tinh ⇒ vệ tinh. Tiếng Anh mượn lại thẳng <i>Sputnik</i> từ vệ tinh Liên Xô 1957.</div>'
    '<div class="hd-warn">Vệ tinh nhân tạo = <b>иску́сственный спу́тник</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>путь</b> con đường · <b>путеше́ствие</b> chuyến du lịch · '
    '<b>попу́тчик</b> người đi cùng chuyến</div>'
)

# ------------------------------------------------------------------ беседа
S["беседа"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бе-</span>'
    '<span class="hd-gloss">có lẽ từ <b>без</b> «ra ngoài»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сед-</span>'
    '<span class="hd-gloss">NGỒI — như <b>сосе́д</b> hàng xóm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«NGỒI cùng nhau» ⇒ cuộc trò chuyện từ tốn, trao đổi nghiêm túc. '
    'Trang trọng hơn <b>разгово́р</b>; cũng là buổi nói chuyện chuyên đề.</div>'
    '<div class="hd-warn">⚠️ Mức tin: chẻ <b>бе-</b> là từ nguyên, các nhà ngôn ngữ còn bàn; '
    'chỉ <b>-сед-</b> «ngồi» là chắc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бесе́довать</b> trò chuyện · <b>собесе́дник</b> người cùng nói chuyện · '
    '<b>собесе́дование</b> buổi phỏng vấn xin việc</div>'
)

# ------------------------------------------------------------------ доклад
S["доклад"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI nơi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-клад</span>'
    '<span class="hd-gloss">ĐẶT — gốc của <b>класть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«ĐẶT (thông tin) TỚI trước người nghe» ⇒ bản báo cáo, bài thuyết '
    'trình ở hội nghị. Đọc báo cáo = <b>де́лать докла́д</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>докла́дчик</b> người báo cáo · <b>докла́дывать</b> báo cáo · '
    '<b>класть</b> đặt, để</div>'
)

# ------------------------------------------------------------- выступление
S["выступление"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">RA ngoài, ra trước</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ступ-</span>'
    '<span class="hd-gloss">gốc BƯỚC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-л-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>вы́ступить</b>: BƯỚC RA trước mọi người ⇒ bài phát '
    'biểu, tiết mục biểu diễn.</div>'
    '<div class="hd-warn"><b>л</b> chen vào sau <b>п</b>, đúng như dạng «tôi» của động từ: '
    '<b>вы́ступлю</b> → <b>выступле́ние</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>выступа́ть</b> phát biểu, biểu diễn · <b>вы́ступить</b> (HT) · '
    '<b>ступе́нька</b> bậc thang</div>'
)

# -------------------------------------------------------------- объяснение
S["объяснение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-ъ-</span>'
    '<span class="hd-gloss">khắp lượt; dấu cứng giữ <b>я</b> đọc tách</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ясн-</span>'
    '<span class="hd-gloss">RÕ — chính là <b>я́сно</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Làm cho RÕ khắp lượt» ⇒ lời giải thích. Danh từ của '
    '<b>объясни́ть</b>; trọng âm đứng ở <b>-не́-</b>: <b>объясне́ние</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>объясни́ть</b> giải thích · <b>объясня́ть</b> giải thích (CHT) · '
    '<b>я́сно</b> rõ · <b>я́сный</b> rõ ràng, trong trẻo</div>'
)

# ------------------------------------------------------------- переговоры
S["переговоры"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span>'
    '<span class="hd-gloss">QUA LẠI giữa hai bên</span></div>'
    '<div class="hd-row"><span class="hd-piece">-говор-</span>'
    '<span class="hd-gloss">NÓI — gốc của <b>говори́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ы</span>'
    '<span class="hd-gloss">đuôi số nhiều</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«NÓI QUA NÓI LẠI» giữa hai phía ⇒ đàm phán. Cùng kiểu '
    '<b>перепи́ска</b> thư từ qua lại.</div>'
    '<div class="hd-warn">Chỉ có số nhiều ở nghĩa này: <b>перегово́ры шли</b> (động từ chia số '
    'nhiều). Tiến hành đàm phán = <b>вести́ перегово́ры</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>говори́ть</b> nói · <b>разгово́р</b> cuộc trò chuyện · '
    '<b>договори́ться</b> thoả thuận được</div>'
)

# --------------------------------------------------------------- приказать
S["приказать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">hướng TỚI người kia</span></div>'
    '<div class="hd-row"><span class="hd-piece">-каз-</span>'
    '<span class="hd-gloss">NÓI RA, CHỈ RA — như <b>сказа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">CHỈ cho người kia việc phải làm ⇒ ra lệnh. Chia y hệt '
    '<b>сказа́ть</b>: <b>з → ж</b>, trọng âm lùi — <b>прикажу́, прика́жешь</b>. '
    'Cặp CHT: <b>прика́зывать</b>.</div>'
    '<div class="hd-warn">Ra lệnh cho AI ở cách 3 + nguyên thể: <b>Он приказа́л солда́там '
    'стреля́ть</b> = Anh ta ra lệnh cho lính bắn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прика́з</b> mệnh lệnh · <b>сказа́ть</b> nói · '
    '<b>показа́ть</b> cho xem · <b>ука́з</b> sắc lệnh</div>'
)

# ------------------------------------------------------------- приказывать
S["приказывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-каз-</span>'
    '<span class="hd-gloss">chỉ ra cho người kia = ra lệnh (xem <b>приказа́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-</span>'
    '<span class="hd-gloss">hậu tố biến hoàn thành → CHƯA hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ra lệnh thường xuyên, quen thói ra lệnh. Chia đều, giữ <b>з</b>: '
    '<b>прика́зываю</b>. Cũng đòi cách 3: <b>прика́зывать кому́</b>.</div>'
    '<div class="hd-warn">Thêm <b>-ыва-</b> thì trọng âm nhảy về trước: '
    '<b>приказа́ть → прика́зывать</b>, y như <b>показа́ть → пока́зывать</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прика́з</b> mệnh lệnh · <b>пока́зывать</b> cho xem · '
    '<b>расска́зывать</b> kể</div>'
)

# ----------------------------------------------------------------- описать
S["описать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">VÒNG QUANH, khắp mặt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пис-</span>'
    '<span class="hd-gloss">gốc VIẾT — <b>писа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">VIẾT VÒNG QUANH một vật, đủ mọi mặt ⇒ mô tả. Giống tiếng Anh '
    '<i>de-scribe</i> cũng chứa «viết». Cặp CHT: <b>опи́сывать</b>.</div>'
    '<div class="hd-warn">Chia như <b>писа́ть</b>: <b>с → ш</b>, trọng âm lùi từ ngôi 2 — '
    '<b>я опишу́, ты опи́шешь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>описа́ние</b> bản mô tả · <b>писа́ть</b> viết · '
    '<b>записа́ть</b> ghi lại · <b>подписа́ть</b> ký</div>'
)

# --------------------------------------------------------------- описывать
S["описывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-пис-</span>'
    '<span class="hd-gloss">viết VÒNG QUANH = mô tả (xem <b>описа́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-</span>'
    '<span class="hd-gloss">hậu tố biến hoàn thành → CHƯA hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đang tả, hay tả: <b>Кни́га опи́сывает жизнь в дере́вне</b> = Cuốn '
    'sách tả cuộc sống ở làng. Chia đều, giữ <b>с</b>: <b>опи́сываю</b>.</div>'
    '<div class="hd-warn">Thêm <b>-ыва-</b> thì trọng âm nhảy về trước: '
    '<b>описа́ть → опи́сывать</b>, y như <b>подписа́ть → подпи́сывать</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>описа́ние</b> bản mô tả · <b>запи́сывать</b> ghi lại · '
    '<b>подпи́сывать</b> ký</div>'
)

# ---------------------------------------------------------------- выражать
S["выражать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">RA ngoài</span></div>'
    '<div class="hd-row"><span class="hd-piece">-раж-</span>'
    '<span class="hd-gloss">dạng <b>ж</b> của gốc <b>раз-</b> «đánh, giáng» (xem <b>вы́разить</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>выража́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đưa ý nghĩ RA ngoài thành lời, thành nét mặt ⇒ bày tỏ, diễn đạt. '
    'Cặp HT <b>вы́разить</b> giữ <b>з</b>, ở đây đã thành <b>ж</b>.</div>'
    '<div class="hd-warn">Bày tỏ CÁI GÌ ở cách 4: <b>выража́ть благода́рность</b> = bày tỏ '
    'lòng biết ơn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>выраже́ние</b> thành ngữ, nét mặt · <b>вырази́тельный</b> có hồn, '
    'diễn cảm · <b>вы́разить</b> (HT)</div>'
)

# ---------------------------------------------------------------- выразить
S["выразить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span>'
    '<span class="hd-gloss">RA ngoài</span></div>'
    '<div class="hd-row"><span class="hd-piece">-раз-</span>'
    '<span class="hd-gloss">gốc «đánh, giáng» (<b>рази́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đánh/ép ý nghĩ RA thành hình» ⇒ diễn đạt (tiếng Anh <i>ex-press</i> '
    'cũng là «ép ra»). Tiền tố <b>вы-</b> ở thể HT luôn nhận trọng âm: <b>вы́разить</b>, '
    '<b>вы́ступить</b>. Biến <b>з → ж</b> ở «tôi»: <b>я вы́ражу</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: nghĩa «đánh» của gốc là từ nguyên, không phải luật suy '
    'ra được — cùng gốc với <b>порази́ть</b> đánh trúng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>выража́ть</b> (CHT) · <b>выраже́ние</b> thành ngữ, nét mặt · '
    '<b>пораже́ние</b> thất bại</div>'
)

# --------------------------------------------------------------- закричать
S["закричать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">BẮT ĐẦU làm việc gì</span></div>'
    '<div class="hd-row"><span class="hd-piece">-крич-</span>'
    '<span class="hd-gloss">gốc HÉT — <b>крича́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể; chia như <b>крича́ть</b>: <b>закричу́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>за-</b> đánh dấu lúc khởi đầu: bỗng kêu lên, la lên (và có thể la '
    'tiếp). Cùng khuôn <b>засмея́ться</b> bật cười, <b>запла́кать</b> oà khóc.</div>'
    '<div class="hd-warn"><b>кри́кнуть</b> = hét MỘT tiếng rồi thôi; <b>закрича́ть</b> = BẮT ĐẦU '
    'la (có thể kéo dài).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>крича́ть</b> la hét · <b>кри́кнуть</b> hét lên một tiếng · '
    '<b>крик</b> tiếng hét</div>'
)
