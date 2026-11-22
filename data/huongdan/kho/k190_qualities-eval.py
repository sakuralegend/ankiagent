# -*- coding: utf-8 -*-
"""k190 — qualities::eval (lô trộn): tính từ đánh giá + vài danh từ mượn (chính trị, quân sự).

Chỗ cần nhất quán trong lô:
(1) уда́чный ← уда́ча [k76]: «у- đạt tới, xong xuôi + -да- gốc CHO, như дать».
(2) бессмы́сленный ← смысл [k115]: «с- gom lại + -мысл Ý NGHĨ»; бес- = без- (з → с trước с).
(3) привлека́тельный ← привлека́ть [k175]: «при- TỚI GẦN + -влек- KÉO, LÔI»; đuôi -тельный.
(4) исключи́тельно ← исключе́ние [k161]: «ис- = из- RA KHỎI + -ключ- MÓC, KHOÁ».
(5) вооружённый ← ору́жие [k115]: gốc VŨ KHÍ.  (6) запре́т ↔ запрети́ть [k137]: «-прет- CẤM».
(7) убеждённый ↔ убежда́ть [k124]: «-бежд- = -бед-, д → жд».
(8) подходя́щий ↔ подходи́ть [k125]: «под- SÁT LẠI GẦN + -ход- ĐI»; đuôi -ящий như сле́дующий [k75].
(9) чрезвыча́йный: -вычай- = -вык- QUEN, khớp обы́чай [k148] / обы́чный [k108] (ở đây chữ в CÒN nguyên).
(10) полк ↔ полко́вник [k162]; нужда́ться ↔ ну́жный [k05] (k05 đã chẻ «нуж- gốc của нужда́»).
Họ hàng cố ý vắng: чепуха́ (gốc không rõ, không phái sinh thông dụng), конгре́сс (mượn đứng một mình).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    # gloss: exclusively/solely/only/exceptionally/extremely/remarkably — «hoàn toàn» không khớp
    # gloss nào (và đụng совсе́м/по́лностью); thêm «riêng» (solely), «đặc biệt» (exceptionally).
    "исключительно": "chỉ, duy nhất, riêng, đặc biệt, cực kỳ",
}

# --------------------------------------------------------------------- чепуха
S["чепуха"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — gốc từ còn tranh cãi, học như một khối.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ giống cái, trọng âm cuối, gần như chỉ dùng số ít. Hay đứng một mình '
    'làm câu cảm thán: <b>Чепуха́!</b> = Vớ vẩn! · <b>Что за чепуха́!</b> = Nhảm nhí gì thế!</div>'
    '<div class="hd-warn"><b>нести́ чепуху́</b> = nói nhảm (nghĩa đen «mang chuyện vớ vẩn đi»), '
    'cách 4 đuôi -у́.</div>'
)

# --------------------------------------------------------------------- подходящий
S["подходящий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span>'
    '<span class="hd-gloss">SÁT LẠI GẦN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ход-</span>'
    '<span class="hd-gloss">ĐI — như <b>ходи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́щий</span>'
    '<span class="hd-gloss">đuôi phân từ hiện tại: «đang …»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Phân từ của <b>подходи́ть</b> «hợp với» đông cứng thành tính từ: cái «đang hợp» '
    '⇒ phù hợp. <b>Э́то мне подхо́дит</b> → <b>подходя́щий моме́нт</b> thời điểm thích hợp. '
    'Cùng đuôi với <b>сле́дующий</b> «cái đang theo sau». Hợp cho ai: <b>для</b> + cách 2. '
    'Không có dạng ngắn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>подходи́ть</b> lại gần, hợp · <b>подойти́</b> (HT) · '
    '<b>подхо́д</b> cách tiếp cận · <b>ходи́ть</b> đi</div>'
)

# --------------------------------------------------------------------- чрезвычайный
S["чрезвычайный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">чрез-</span>'
    '<span class="hd-gloss">VƯỢT QUA — dạng sách vở của <b>че́рез</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-вычай-</span>'
    '<span class="hd-gloss">THÔNG LỆ — như <b>обы́чай</b> (gốc -вык- QUEN, к → ч)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">VƯỢT QUA thông lệ ⇒ phi thường, khẩn cấp — dựng y hệt tiếng Anh '
    '<i>extra-ordinary</i>. Dạng ngắn giống đực chèn <b>-е-</b>: <b>чрезвыча́ен</b>. Trạng từ '
    '<b>чрезвыча́йно</b> = cực kỳ: <b>чрезвыча́йно ва́жно</b>.</div>'
    '<div class="hd-warn"><b>чрезвыча́йная ситуа́ция</b> (ЧС) = tình huống khẩn cấp; '
    '<b>МЧС</b> = Bộ Tình trạng khẩn cấp Nga.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обы́чай</b> phong tục · <b>обы́чный</b> thường lệ · '
    '<b>привы́кнуть</b> quen · <b>че́рез</b> qua</div>'
)

# --------------------------------------------------------------------- бессмысленный
S["бессмысленный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бес-</span>'
    '<span class="hd-gloss">= <b>без-</b> KHÔNG (з → с trước с)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-смысл-</span>'
    '<span class="hd-gloss">Ý NGHĨA — chính là <b>смысл</b> (с- gom lại + -мысл Ý NGHĨ)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-енн-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">KHÔNG có ý nghĩa ⇒ vô nghĩa, vô ích. Trạng từ <b>Э́то бессмы́сленно</b> = '
    'làm thế chẳng ích gì — cùng ý với <b>Нет смы́сла</b>. Dạng ngắn giống đực rụng một н: '
    '<b>бессмы́слен</b>; các dạng khác giữ нн.</div>'
    '<div class="hd-warn">Viết HAI chữ с: <b>бес</b> + <b>смысл</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>смысл</b> ý nghĩa · <b>мысль</b> ý nghĩ · <b>осмы́слить</b> thấu hiểu · '
    '<b>бесполе́зный</b> vô ích (cùng бес-)</div>'
)

# --------------------------------------------------------------------- удачный
S["удачный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">đạt tới, xong xuôi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-да-</span>'
    '<span class="hd-gloss">gốc CHO, như <b>дать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ч-н-ый</span>'
    '<span class="hd-gloss">tính từ của <b>уда́ча</b> vận may</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Việc ra đúng như ý, trót lọt ⇒ thành công, đạt, khéo: <b>уда́чный вы́бор</b> '
    'lựa chọn khéo. Dạng ngắn chèn <b>-е-</b>: <b>уда́чен</b>. Trạng từ hay nói: '
    '<b>Уда́чно!</b> = Trót lọt rồi!</div>'
    '<div class="hd-warn">Nói về VIỆC, LỜI, LỰA CHỌN (<b>уда́чная шу́тка</b> câu đùa đắt). Người '
    'thành đạt là <b>успе́шный</b>, người gặp may là <b>уда́чливый</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уда́ча</b> may mắn · <b>уда́ться</b> thành công, làm được · '
    '<b>неуда́чный</b> hỏng, không thành · <b>дать</b> cho</div>'
)

# --------------------------------------------------------------------- привлекательный
S["привлекательный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">TỚI GẦN, về phía mình</span></div>'
    '<div class="hd-row"><span class="hd-piece">-влек-</span>'
    '<span class="hd-gloss">KÉO, LÔI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-тельный</span>'
    '<span class="hd-gloss">đuôi «có sức gây ra việc đó»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Có sức KÉO người khác về phía mình ⇒ hấp dẫn. Đuôi <b>-тельный</b> biến động '
    'từ thành tính từ: <b>привлека́ть</b> → <b>привлека́тельный</b>, y như <b>убеди́ть</b> → '
    '<b>убеди́тельный</b> có sức thuyết phục. Dạng ngắn chèn <b>-е-</b>: '
    '<b>привлека́телен</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>привлека́ть</b> thu hút · <b>привле́чь</b> (HT) · '
    '<b>увлече́ние</b> sở thích · <b>развлече́ние</b> trò giải trí</div>'
)

# --------------------------------------------------------------------- исключительно
S["исключительно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ис-</span>'
    '<span class="hd-gloss">= из- RA KHỎI (з → с trước к)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ключ-</span>'
    '<span class="hd-gloss">MÓC, KHOÁ — như <b>ключ</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́тельн-о</span>'
    '<span class="hd-gloss">trạng từ của <b>исключи́тельный</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai nghĩa, cùng một hình ảnh «loại ra»: loại hết thứ khác ⇒ CHỈ: '
    '<b>исключи́тельно для вас</b> chỉ dành riêng cho bạn; nằm ngoài lệ thường (<b>исключе́ние</b> '
    'ngoại lệ) ⇒ CỰC KỲ: <b>исключи́тельно ва́жно</b>. Mẹo: đứng trước tính từ, trạng từ thường là '
    '«cực kỳ».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>исключе́ние</b> ngoại lệ · <b>исключи́ть</b> loại trừ · '
    '<b>включи́ть</b> bật, gộp vào · <b>ключ</b> chìa khoá</div>'
)

# --------------------------------------------------------------------- гарантия
S["гарантия"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn (Pháp <i>garantie</i>) — không chẻ kiểu Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gần y tiếng Anh <i>guarantee</i>. Đuôi <b>-ия</b> ⇒ giống cái, chia như '
    '<b>ста́нция</b>. Hàng còn bảo hành: <b>на гара́нтии</b>.</div>'
    '<div class="hd-warn">Bảo hành MỘT NĂM: <b>гара́нтия на год</b> — <b>на</b> + cách 4.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гаранти́ровать</b> bảo đảm · <b>гаранти́йный</b> thuộc bảo hành</div>'
)

# --------------------------------------------------------------------- нуждаться
S["нуждаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">нужд-</span>'
    '<span class="hd-gloss"><b>нужда́</b> NHU CẦU, CẢNH THIẾU — gốc của <b>ну́жный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть-ся</span>'
    '<span class="hd-gloss">đuôi động từ phản thân, chia đều</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Ở trong cảnh thiếu» ⇒ cần đến. Khác <b>ну́жно</b>: ở đây NGƯỜI CẦN làm chủ '
    'ngữ — <b>Он нужда́ется в по́мощи</b>, còn <b>Ему́ нужна́ по́мощь</b>. Đứng trơn = túng thiếu: '
    '<b>Они́ нужда́ются</b>. Chỉ có thể chưa hoàn thành.</div>'
    '<div class="hd-warn">Thứ được cần: <b>в</b> + cách 6 (<b>нужда́ться в деньга́х</b>), không dùng '
    'cách 4.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нужда́</b> nhu cầu, cảnh túng · <b>ну́жный</b> cần thiết · '
    '<b>ну́жно</b> cần phải</div>'
)

# --------------------------------------------------------------------- вооружённый
S["вооружённый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">во-</span>'
    '<span class="hd-gloss">= в- VÀO, lên người</span></div>'
    '<div class="hd-row"><span class="hd-piece">-оруж-</span>'
    '<span class="hd-gloss">VŨ KHÍ — như <b>ору́жие</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ённ-ый</span>'
    '<span class="hd-gloss">đuôi phân từ bị động «đã được …»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đã được cho vũ khí lên người» ⇒ có vũ trang; là phân từ của '
    '<b>вооружи́ть</b>. Chữ ё luôn mang trọng âm — sách báo hay bỏ hai chấm: вооруженный. Dạng ngắn '
    'giống đực rụng một н: <b>вооружён</b>.</div>'
    '<div class="hd-warn"><b>вооружённые си́лы</b> = lực lượng vũ trang.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ору́жие</b> vũ khí · <b>вооружи́ть</b> trang bị vũ khí · '
    '<b>вооруже́ние</b> vũ khí trang bị · <b>ружьё</b> súng trường</div>'
)

# --------------------------------------------------------------------- полк
S["полк"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giống đực; hễ thêm đuôi là trọng âm nhảy ra đuôi: <b>полка́</b>, số nhiều '
    '<b>полки́</b>. Ở trong trung đoàn: <b>в полку́</b> — cách 6 riêng đuôi -у́, như <b>в лесу́</b>. '
    'Người cầm một полк là <b>полко́вник</b> đại tá.</div>'
    '<div class="hd-warn">Đừng lẫn <b>по́лка</b> cái kệ với <b>полка́</b> «của trung đoàn» — chỉ khác '
    'chỗ trọng âm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>полко́вник</b> đại tá · <b>подполко́вник</b> trung tá</div>'
)

# --------------------------------------------------------------------- танк
S["танк"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn tiếng Anh <i>tank</i> — không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Y tiếng Anh: <i>tank</i> «thùng chứa» là tên che mắt người Anh đặt cho xe '
    'tăng đầu tiên (1916). Giống đực, chia đều: <b>та́нка</b>, số nhiều <b>та́нки</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>та́нковый</b> thuộc xe tăng · <b>танки́ст</b> lính xe tăng</div>'
)

# --------------------------------------------------------------------- конгресс
S["конгресс"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn (La-tinh <i>congressus</i> «cùng bước tới») — tiếng Nga không chẻ.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Y tiếng Anh <i>congress</i>, chỉ cần nhớ viết HAI с ở cuối. Giống đực, chia '
    'đều: <b>конгре́сса</b>. Quốc hội Mỹ: <b>Конгре́сс США</b>.</div>'
)

# --------------------------------------------------------------------- запрет
S["запрет"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">tiền tố — ở từ này không tách ra nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-прет</span>'
    '<span class="hd-gloss">CẤM — như <b>запрети́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bỏ đuôi -ить của <b>запрети́ть</b> là ra danh từ giống đực, y khuôn '
    '<b>отве́т</b> ← <b>отве́тить</b>. Cấm cái gì: <b>на</b> + cách 4 — <b>запре́т на куре́ние</b> '
    'lệnh cấm hút thuốc.</div>'
    '<div class="hd-warn"><b>под запре́том</b> = đang bị cấm (nằm «dưới lệnh cấm»).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>запрети́ть</b> cấm (HT) · <b>запреща́ть</b> (CHT) · '
    '<b>запрещено́</b> bị cấm</div>'
)

# --------------------------------------------------------------------- коммунист
S["коммунист"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">коммун-</span>'
    '<span class="hd-gloss">CHUNG (La-tinh <i>communis</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ст</span>'
    '<span class="hd-gloss">NGƯỜI theo một chủ nghĩa / làm một nghề, = <i>-ist</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Y tiếng Anh <i>communist</i>. Đuôi <b>-ист</b> ăn cặp với <b>-изм</b> '
    'chủ nghĩa, như <b>журнали́ст</b>. Cùng gốc «chung» có <b>коммуна́льные услу́ги</b> = '
    'tiền điện nước, dịch vụ chung của nhà.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>коммуни́зм</b> chủ nghĩa cộng sản · <b>коммунисти́ческий</b> cộng sản · '
    '<b>коммуна́льный</b> thuộc dịch vụ chung</div>'
)

# --------------------------------------------------------------------- мафия
S["мафия"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn tiếng Ý <i>mafia</i> — không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <b>-ия</b> ⇒ giống cái, chia như <b>а́рмия</b>: <b>ма́фии</b>, '
    '<b>ма́фию</b>. Nghĩa bóng: nhóm khép kín bao che cho nhau.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мафио́зи</b> dân mafia (không biến cách) · <b>мафио́зный</b> kiểu mafia</div>'
)

# --------------------------------------------------------------------- цивилизация
S["цивилизация"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">цивилиз-</span>'
    '<span class="hd-gloss">La-tinh <i>civilis</i> thuộc công dân</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ция</span>'
    '<span class="hd-gloss">= <i>-ation</i>, danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đổi <i>-ation</i> thành <b>-а́ция</b> là ra từ Nga: <i>civilization</i> → '
    '<b>цивилиза́ция</b>, như <b>организа́ция</b>. Trọng âm luôn ở <b>-а́-</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>цивилизо́ванный</b> văn minh (tính từ)</div>'
)

# --------------------------------------------------------------------- инициатива
S["инициатива"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">инициат-</span>'
    '<span class="hd-gloss">La-tinh <i>initium</i> sự bắt đầu</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ва</span>'
    '<span class="hd-gloss">= <i>-ive</i>, danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Y tiếng Anh <i>initiative</i>: người BẮT ĐẦU trước ⇒ sáng kiến, thế chủ động. '
    '<b>проявля́ть инициати́ву</b> = tỏ ra chủ động.</div>'
    '<div class="hd-warn">Theo sáng kiến của ai: <b>по инициати́ве</b> + cách 2 — '
    '<b>по инициати́ве президе́нта</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>инициа́тор</b> người khởi xướng · <b>инициати́вный</b> năng nổ, chủ động</div>'
)

# --------------------------------------------------------------------- убеждённый
S["убеждённый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố, nghĩa riêng đã mờ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бежд-</span>'
    '<span class="hd-gloss">= -бед- biến âm д → жд, như <b>убежда́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ённ-ый</span>'
    '<span class="hd-gloss">đuôi phân từ bị động «đã được …»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đã được thuyết phục» (<b>убеди́ть</b>) ⇒ tin chắc. Làm vị ngữ dùng dạng '
    'ngắn: <b>Я убеждён, что…</b> = tôi tin chắc rằng…; nữ nói <b>Я убеждена́</b> — ngoài giống đực, '
    'trọng âm ra đuôi và ё thành е. Trước danh từ là «kiên định»: <b>убеждённый сторо́нник</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>убеди́ть</b> thuyết phục · <b>убежде́ние</b> niềm tin · '
    '<b>убеди́тельный</b> có sức thuyết phục</div>'
)

B = {
    "docbangmat": 83,
    "loitubat": 2,   # чрезвычайный: mảnh «-вы́чай-» đặt dấu ở ы (chép từ обы́чай) trong khi trọng âm thật ở -ча́й- -> bỏ dấu
                     # запрет: «ку́рение» sai trọng âm (đúng: куре́ние) — cửa TRONG AM LECH bắt, không phải mắt
    "nguonsai": 0,   # không có chỗ từ điển sai phải bác; dạng ngắn «вооружённа» chưa chắc nên chỉ ghi giống đực вооружён
    "baolen": [
        "VA CHẠM KHÔNG GỠ ĐƯỢC TỪ LÔ NÀY: đề của успе́шный [k76, đã nạp] chỉ là «thành công» ⊂ đề уда́чный. "
        "Gloss уда́чный mở đầu bằng «successful» ⇒ «thành công» là nghĩa chính, cấm cắt; thêm nghĩa vào уда́чный "
        "cũng không gỡ được (bên hẹp là успе́шный). Muốn tách phải nới đề успе́шный (vd «thành công, thành đạt» "
        "nếu gloss của nó xác nhận) — ngoài lô, chờ user. Thẻ уда́чный đã có một ô đỏ phân biệt hai từ.",
        "V cần duyệt (1): исключительно «chỉ, duy nhất, hoàn toàn, cực kỳ» -> «chỉ, duy nhất, riêng, đặc biệt, cực kỳ» "
        "(«hoàn toàn» không khớp gloss nào và đụng совсе́м/по́лностью; thêm solely/exceptionally).",
        "Đề KHÔNG sửa dù hơi rộng hơn gloss (có thể là bản user chữa tay, QD-27): убеждённый «… triệt để» (gloss chỉ "
        "«convinced»); ма́фия «… hội kín»; подходя́щий «vừa» (đơn lẻ dễ hiểu nhầm «vừa mới»). Luồng chính cân.",
        "Chỗ KHÔNG chắc: вооружённый chẻ «во- = в- VÀO, lên người» (nghĩa tiền tố ở đây khá mờ); mẹo исключи́тельно "
        "«trước tính từ/trạng từ thường là cực kỳ» là quy tắc kinh nghiệm, không tuyệt đối; уда́чный «nói về việc, lời, "
        "lựa chọn — người thì успе́шный/уда́чливый» là xu hướng dùng, không phải luật cứng.",
        "Họ hàng cố ý vắng: чепуха́ (gốc tranh cãi, không phái sinh thông dụng), конгре́сс (mượn đứng một mình).",
    ],
}
