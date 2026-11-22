# -*- coding: utf-8 -*-
"""k204 — concepts::state (lô trộn): xã hội, chính trị, phẩm chất trí óc.

Chỗ cần nhất quán trong lô:
(1) голосова́ть / проголосова́ть: thẻ CHT giữ cách đòi (за + C4, про́тив + C2); thẻ HT dẫn chiếu.
    Khớp го́лос [k79] («lá phiếu» = cất tiếng).
(2) наступле́ние: на- + -ступ- BƯỚC + -л-ение — chẻ y khuôn выступле́ние [k135], преступле́ние [k151].
    KHÔNG cùng gốc плен / плёнка (máy ghép nhầm).
(3) восста́ние: вос- + -ста- ĐỨNG — khớp восстанови́ть [k176] (thẻ đó đã liệt kê восста́ние).
(4) Đuôi quốc tế: -и́зм / -и́ст (террори́зм ↔ террори́ст [k167]), -и́ческий (социалисти́ческий),
    -ите́т = -ity (авторите́т), -уа́льный = -ual (интеллектуа́льный).
(5) неуда́чный khớp уда́чный [k190]; убеди́тельный khớp убеди́ть [k124]; пожела́ние khớp
    жела́ние [k117] / пожела́ть [k76]; уме́ние khớp уме́ть [k81].
Họ hàng cố ý vắng: không có — mọi từ đều có họ thật.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "наступление": "sự bắt đầu, sự đến, sự tới, cuộc tấn công, sự tiến công",  # thiếu hẳn nghĩa offensive/attack/advance
    "голосовать": "bỏ phiếu, bầu, biểu quyết, vẫy xe",                         # gloss: to hitchhike / to flag down a car
}

# --------------------------------------------------------------------- неудачный
S["неудачный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не-</span>'
    '<span class="hd-gloss">KHÔNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">уда́чный</span>'
    '<span class="hd-gloss">trót lọt, thành công — tính từ của <b>уда́ча</b> vận may</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Không trót lọt» ⇒ hỏng, thất bại, chọn không khéo. Như <b>уда́чный</b>, nói về '
    'VIỆC, LỰA CHỌN: <b>неуда́чная попы́тка</b> lần thử hỏng, <b>неуда́чная шу́тка</b> câu đùa nhạt. '
    'Dạng ngắn chèn <b>-е-</b>: <b>неуда́чен</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уда́ча</b> vận may · <b>неуда́ча</b> thất bại · <b>уда́чный</b> thành công · '
    '<b>уда́ться</b> làm được</div>'
)

# --------------------------------------------------------------------- моральный
S["моральный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мора́ль-</span>'
    '<span class="hd-gloss">ĐẠO ĐỨC — Latin <i>moralis</i>, tiếng Anh <i>moral</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>moral</i>. Nghĩa thứ hai: TINH THẦN, đối lập với vật chất — như '
    '<i>moral support</i>: <b>мора́льная подде́ржка</b> sự động viên tinh thần, <b>мора́льный вред</b> tổn thất '
    'tinh thần.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мора́ль</b> đạo đức; bài học rút ra · <b>амора́льный</b> vô đạo đức · '
    '<b>мора́льно</b> về mặt tinh thần</div>'
)

# --------------------------------------------------------------------- убедительный
S["убедительный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">убеди́-</span>'
    '<span class="hd-gloss">THUYẾT PHỤC — gốc của <b>убеди́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-тельный</span>'
    '<span class="hd-gloss">tính từ «có sức làm việc đó» — như <b>удиви́тельный</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Có sức thuyết phục: <b>убеди́тельный аргуме́нт</b> lý lẽ thuyết phục. '
    'Dạng ngắn chèn <b>-е-</b>: <b>убеди́телен</b>.</div>'
    '<div class="hd-warn"><b>Убеди́тельная про́сьба…</b> = «Đề nghị khẩn thiết…» — mở đầu quen thuộc '
    'của biển báo: <b>Убеди́тельная про́сьба не кури́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>убеди́ть</b> thuyết phục · <b>убеди́ться</b> tin chắc · '
    '<b>убежде́ние</b> niềm tin · <b>убеди́тельно</b> một cách thuyết phục</div>'
)

# --------------------------------------------------------------------- авторитет
S["авторитет"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">а́втор-</span>'
    '<span class="hd-gloss">Latin <i>auctor</i> người tạo ra — như <b>а́втор</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ите́т</span>'
    '<span class="hd-gloss">= <i>-ity</i> tiếng Anh, danh từ giống đực — như <b>университе́т</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>authority</i>, nhưng chỉ nghĩa UY TÍN, tiếng nói có trọng lượng — và cả '
    'người có uy tín: <b>Он авторите́т в медици́не</b>. Trọng âm chạy ra đuôi: <b>а́втор</b> → '
    '<b>авторите́т</b>.</div>'
    '<div class="hd-warn">«Chính quyền, nhà chức trách» (<i>the authorities</i>) KHÔNG phải '
    '<b>авторите́т</b> mà là <b>вла́сти</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>а́втор</b> tác giả · <b>авторите́тный</b> có uy tín · '
    '<b>авторита́рный</b> độc đoán</div>'
)

# --------------------------------------------------------------------- контрабанда
S["контрабанда"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">контра-</span>'
    '<span class="hd-gloss">CHỐNG LẠI — như <b>контрата́ка</b> phản công</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ба́нда</span>'
    '<span class="hd-gloss">LỆNH, chiếu chỉ — tiếng Ý <i>bando</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn nguyên khối từ Ý <i>contrabbando</i> «trái lệnh» = tiếng Anh '
    '<i>contraband</i>. Buôn trái lệnh cấm ⇒ buôn lậu; một từ chỉ cả việc lẫn món hàng: '
    '<b>занима́ться контраба́ндой</b> buôn lậu, <b>провезти́ контраба́нду</b> chở hàng lậu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>контрабанди́ст</b> kẻ buôn lậu · <b>контраба́ндный</b> lậu</div>'
)

# --------------------------------------------------------------------- восстание
S["восстание"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вос-</span>'
    '<span class="hd-gloss">LÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ста-</span>'
    '<span class="hd-gloss">ĐỨNG — như <b>стать</b>, <b>встать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ние</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cả dân ĐỨNG LÊN ⇒ khởi nghĩa, nổi dậy. Hai chữ <b>с</b> vì <b>вос-</b> gặp '
    '<b>ста-</b>. Động từ: <b>восста́ть про́тив</b> + cách 2 = nổi dậy chống lại.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>восстановле́ние</b> = sự khôi phục (cho ĐỨNG LẠI) — cùng '
    'gốc, thêm <b>-нов-</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>восста́ть</b> nổi dậy · <b>восстанови́ть</b> khôi phục · '
    '<b>встать</b> đứng dậy · <b>стать</b> trở thành</div>'
)

# --------------------------------------------------------------------- наступление
S["наступление"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">LÊN, ĐÈ LÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ступ-</span>'
    '<span class="hd-gloss">BƯỚC — như <b>выступле́ние</b>, <b>преступле́ние</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-л-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Quân BƯỚC TỚI đè lên ⇒ cuộc tấn công. Thời gian bước tới ⇒ sự bắt đầu, '
    'sự đến: <b>наступле́ние весны́</b> mùa xuân đến. Động từ <b>наступи́ть</b> còn là «giẫm lên»: '
    '<b>наступи́ть на но́гу</b>.</div>'
    '<div class="hd-warn"><b>С наступа́ющим!</b> = chúc mừng (năm mới) SẮP ĐẾN — câu chúc những '
    'ngày cuối tháng 12.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>наступа́ть</b> / <b>наступи́ть</b> tấn công; đến · '
    '<b>выступле́ние</b> bài phát biểu · <b>преступле́ние</b> tội ác</div>'
)

# --------------------------------------------------------------------- социалистический
S["социалистический"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">социал-</span>'
    '<span class="hd-gloss">XÃ HỘI — như <b>социа́льный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ист-</span>'
    '<span class="hd-gloss">= <i>-ist</i>: người theo</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ческий</span>'
    '<span class="hd-gloss">= <i>-ic</i>, đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>socialist</i>. Trọng âm luôn đứng ở <b>-и́ческий</b>, như '
    '<b>террористи́ческий</b>. Chữ «С» thứ ba trong <b>СССР</b>: Сою́з Сове́тских '
    '<b>Социалисти́ческих</b> Респу́блик.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>социали́зм</b> chủ nghĩa xã hội · <b>социали́ст</b> người theo CNXH · '
    '<b>социа́льный</b> thuộc xã hội</div>'
)

# --------------------------------------------------------------------- терроризм
S["терроризм"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">терро́р-</span>'
    '<span class="hd-gloss">KHỦNG BỐ — Latin <i>terror</i> nỗi kinh hoàng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́зм</span>'
    '<span class="hd-gloss">= <i>-ism</i>: chủ nghĩa, hoạt động</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>terrorism</i>. <b>-и́зм</b> luôn nhận trọng âm và là giống đực, như '
    '<b>социали́зм</b>. Cặp đuôi đi đôi: <b>-и́зм</b> chủ nghĩa ↔ <b>-и́ст</b> người — '
    '<b>террори́зм</b> / <b>террори́ст</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>терро́р</b> sự khủng bố · <b>террори́ст</b> kẻ khủng bố · '
    '<b>террористи́ческий</b> thuộc khủng bố</div>'
)

# --------------------------------------------------------------------- плен
S["плен"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được. Không dính gì tới <b>плёнка</b> (màng, phim) — chỉ '
    'giống mặt chữ.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cảnh bị bắt giữ trong chiến tranh. Hầu như chỉ gặp trong hai khuôn: '
    'rơi VÀO thì cách 4, đang Ở thì cách 6 đuôi <b>-у́</b>.</div>'
    '<div class="hd-warn"><b>попа́сть в плен</b> bị bắt làm tù binh · <b>взять в плен</b> bắt làm tù '
    'binh · <b>быть в плену́</b> đang bị giam cầm (<b>пле́не</b> chỉ đi sau <b>о</b>: <b>о пле́не</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пле́нный</b> tù binh · <b>пле́нник</b> người bị bắt giữ · '
    '<b>плени́ть</b> bắt giữ; làm say mê</div>'
)

# --------------------------------------------------------------------- голосовать
S["голосовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">го́лос-</span>'
    '<span class="hd-gloss">TIẾNG NÓI; lá phiếu</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ть</span>'
    '<span class="hd-gloss">đuôi động từ, chia đổi <b>-ова-</b> → <b>-у-</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Xưa bỏ phiếu bằng cách cất tiếng ⇒ bỏ phiếu, biểu quyết. Chia: '
    '<b>голосу́ю</b>, <b>голосу́ешь</b>. Nghĩa đời thường: đứng bên đường giơ tay ⇒ vẫy xe xin đi '
    'nhờ. Cặp HT: <b>проголосова́ть</b>.</div>'
    '<div class="hd-warn"><b>голосова́ть за</b> + cách 4 = bầu cho, ủng hộ · <b>про́тив</b> + cách 2 '
    '= chống: <b>Я голосу́ю за него́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>го́лос</b> giọng; lá phiếu · <b>голосова́ние</b> cuộc bỏ phiếu · '
    '<b>проголосова́ть</b> (HT)</div>'
)

# --------------------------------------------------------------------- проголосовать
S["проголосовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">tiền tố thể hoàn thành — không thêm nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">голосова́ть</span>'
    '<span class="hd-gloss">bỏ phiếu</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vẫn là <b>голосова́ть</b>, chỉ là bỏ phiếu MỘT LẦN cho xong: '
    '<b>Я уже́ проголосова́л</b> — tôi đã bầu rồi. Chia và cách đòi y như thẻ <b>голосова́ть</b>: '
    '<b>проголосу́ю за</b> + cách 4.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>голосова́ть</b> (CHT) · <b>го́лос</b> lá phiếu · '
    '<b>голосова́ние</b> cuộc bỏ phiếu</div>'
)

# --------------------------------------------------------------------- привилегия
S["привилегия"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">приви-</span>'
    '<span class="hd-gloss">Latin <i>privus</i> RIÊNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лег-</span>'
    '<span class="hd-gloss">Latin <i>lex, legis</i> LUẬT — như <i>legal</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ия</span>'
    '<span class="hd-gloss">danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Luật riêng cho một người» ⇒ đặc quyền = <i>privilege</i>. Mượn nguyên khối: '
    '<b>при-</b> ở đây KHÔNG phải tiền tố Nga <b>при-</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>привилегиро́ванный</b> có đặc quyền</div>'
)

# --------------------------------------------------------------------- пожелание
S["пожелание"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пожела́-</span>'
    '<span class="hd-gloss">CHÚC — gốc của <b>пожела́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ние</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>жела́ние</b> là điều mình muốn trong lòng; <b>пожела́ние</b> là điều NÓI RA '
    'cho người khác — lời chúc, hoặc nguyện vọng, góp ý: <b>Ва́ши пожела́ния?</b> Anh chị có yêu cầu '
    'gì không?</div>'
    '<div class="hd-warn"><b>С наилу́чшими пожела́ниями</b> = «Thân chúc mọi điều tốt đẹp» — câu kết '
    'thư, như <i>Best wishes</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пожела́ть</b> chúc · <b>жела́ть</b> mong, chúc · <b>жела́ние</b> mong muốn</div>'
)

# --------------------------------------------------------------------- умение
S["умение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">уме́-</span>'
    '<span class="hd-gloss">BIẾT CÁCH — gốc của <b>уме́ть</b> (← <b>ум</b> trí óc)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ние</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>уме́ть</b>: cái «biết cách làm» đã học được ⇒ kỹ năng. Như '
    'động từ gốc, theo sau là nguyên thể: <b>уме́ние слу́шать</b> kỹ năng lắng nghe.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уме́ть</b> biết (làm) · <b>суме́ть</b> xoay sở được · '
    '<b>уме́лый</b> khéo tay · <b>ум</b> trí óc</div>'
)

# --------------------------------------------------------------------- интеллектуальный
S["интеллектуальный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">интеллект-</span>'
    '<span class="hd-gloss">TRÍ TUỆ — <b>интелле́кт</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-уа́льный</span>'
    '<span class="hd-gloss">= <i>-ual</i>, đuôi tính từ — như <b>индивидуа́льный</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>intellectual</i>: <b>интеллектуа́льная со́бственность</b> sở hữu trí tuệ, '
    '<b>интеллектуа́льный труд</b> lao động trí óc.</div>'
    '<div class="hd-warn">«Người trí thức» thường nói <b>интеллиге́нт</b>, tầng lớp trí thức là '
    '<b>интеллиге́нция</b> — họ hàng gần, nhưng là từ khác.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>интелле́кт</b> trí tuệ · <b>интеллиге́нт</b> người trí thức · '
    '<b>интеллиге́нция</b> giới trí thức</div>'
)

# --------------------------------------------------------------------- мудрый
S["мудрый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn <b>мудр-</b>, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Khôn ngoan nhờ TRẢI NGHIỆM — ông bà, hiền triết. Thông minh nhanh nhạy là '
    '<b>у́мный</b>. Dạng ngắn: trọng âm nhảy ra đuôi ở giống cái — <b>мудр</b>, <b>мудра́</b>, '
    '<b>му́дро</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>му́дрость</b> sự thông thái · <b>мудре́ц</b> nhà hiền triết · '
    '<b>му́дро</b> một cách sáng suốt</div>'
)

# --------------------------------------------------------------------- нарочно
S["нарочно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">наро́ч-</span>'
    '<span class="hd-gloss">gốc cổ, nay không còn từ đứng riêng — không chẻ thêm được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-но</span>'
    '<span class="hd-gloss">đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm có chủ đích ⇒ cố ý, cố tình. Câu hay gặp nhất là lời thanh minh: '
    '<b>Я не наро́чно!</b> — Tôi đâu có cố ý!</div>'
    '<div class="hd-warn"><b>как наро́чно</b> = như thể cố tình, xui thế nào: <b>Как наро́чно, пошёл '
    'дождь</b> — xui sao trời lại đổ mưa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нарочи́тый</b> cố ý, gượng gạo · <b>понаро́шку</b> (trẻ con) giả vờ, '
    'chơi thôi</div>'
)

# --------------------------------------------------------------------- интеллект
S["интеллект"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được trong tiếng Nga: mượn nguyên khối từ Latin <i>intellectus</i> '
    '= tiếng Anh <i>intellect</i>. Hai chữ <b>л</b> như tiếng Anh.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Năng lực suy nghĩ, trí tuệ — từ trang trọng; nói thường thì là <b>ум</b>.</div>'
    '<div class="hd-warn"><b>иску́сственный интелле́кт</b> = trí tuệ nhân tạo (AI), viết tắt '
    'ИИ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>интеллектуа́льный</b> thuộc trí tuệ · <b>интеллиге́нт</b> người trí thức</div>'
)

B = {
    "docbangmat": 73,
    "loitubat": 2,
    "nguonsai": 0,
    "baolen": [
        "V cần duyệt (2): наступле́ние +«cuộc tấn công, sự tiến công» (đề cũ thiếu hẳn nghĩa offensive/attack/advance mà gloss có) · голосова́ть +«vẫy xe» (gloss to hitchhike / flag down a car; là nghĩa khẩu ngữ nhưng thông dụng — user coi là lóng thì bỏ).",
        "Va chạm nghĩa: mô phỏng do_va_cham (chỉ đọc Anki, áp V lô này) = 0 cụm trùng đủ 4 badge dính k204. Bỏ lọc badge còn 1: «thuyết phục» của убеди́ть/убежда́ть/уговори́ть… nằm trong убеди́тельный — badge adj/v tách sạch, không sửa.",
        "Lỗi tự bắt (2): мора́льный — đã viết «nghĩa tinh thần tiếng Anh ít dùng», sai (moral support dùng y hệt) → sửa; плен — đã viết «không nói в пле́не», quá tay: пле́не vẫn đúng sau о (о пле́не) → sửa thành câu đó.",
        "Không chắc / cần biết: контраба́нда chẻ theo tiếng Ý contra+bando, привиле́гия theo Latin privus+lex — từ nguyên chuẩn của từ mượn, đã ghi là mượn nguyên khối, không ghi Mức tin. наро́чно: không nêu gốc cổ (нарок), chỉ ghi «gốc cổ, không chẻ thêm» để khỏi tốn ô Mức tin. наступи́ть на но́гу: chọn trọng âm на но́гу (cũng chuẩn như на́ ногу) vì soát không đọc được trọng âm rơi lên giới từ.",
        "Gốc ступ- của наступле́ние đã nối đúng выступле́ние/преступле́ние; плен ghi rõ trên thẻ là KHÔNG cùng gốc плёнка. Họ hàng: 19/19 thẻ có. Không đụng MIEN_TRU.",
    ],
}
