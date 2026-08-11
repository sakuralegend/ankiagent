# -*- coding: utf-8 -*-
"""k75 — thời gian + việc hằng ngày: từ mới user vừa thêm.

Không có một trục chung: mỗi thẻ đứng độc lập. Ba chỗ phải nhất quán trong lô
này là cặp thể `лечь`↔`ложиться`, mặt đối lập `вставать`, và bộ trạng từ thời
gian `днём`/`ночью` (cách 5 đóng băng, nối thẳng với `день`/`ночь` đã học).
"""

S = {}

# ---------------------------------------------------------------- всего
S["всего"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вс-</span>'
    '<span class="hd-gloss">gốc của <b>весь</b> / <b>всё</b> — toàn bộ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-его́</span>'
    '<span class="hd-gloss">đuôi cách 2, giống đực và trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>всего́</b> chính là cách 2 của <b>всё</b> — «của tất cả». '
    'Gộp hết mọi thứ lại thì ra «tổng cộng»; khi con số gộp ấy bé tí thì hoá ra '
    '«vỏn vẹn, chỉ có».</div>'
    '<div class="hd-warn">So sánh nhất tách đôi: <b>лу́чше всего́</b> = hơn mọi THỨ, '
    'còn <b>лу́чше всех</b> = hơn mọi NGƯỜI. Vật thì <b>всего́</b>, người thì <b>всех</b>.</div>'
    '<div class="hd-warn">Câu chào tạm biệt phải thuộc: <b>Всего́ хоро́шего!</b> = Chúc mọi '
    'sự tốt lành — cả hai chữ đều đứng ở cách 2.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>весь</b> toàn bộ · <b>всё</b> mọi thứ · <b>все</b> mọi người · '
    '<b>всегда́</b> luôn luôn</div>'
)

# -------------------------------------------------------------- вставать
S["вставать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">vào, lên</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ста-</span>'
    '<span class="hd-gloss">gốc ĐỨNG (như <b>стоя́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва́ть</span>'
    '<span class="hd-gloss">hậu tố kéo dài → thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>ста</b> là «đứng». Thêm <b>в-</b> thành «đứng lên», thêm '
    '<b>-ва-</b> thì việc ấy hoá ra LẶP LẠI — sáng nào cũng dậy.</div>'
    '<div class="hd-warn">Hiện tại nuốt mất <b>-ва-</b>: <b>встаю́, встаёшь, встаю́т</b> — '
    'y hệt <b>дава́ть</b> → <b>даю́, даёшь</b>. Cả lớp động từ đuôi <b>-ва́ть</b> đều thế.</div>'
    '<div class="hd-warn">Cặp thể: <b>встава́ть</b> là thói quen — <b>Обы́чно я встаю́ ра́но</b>; '
    'còn <b>встать</b> là một lần đã xong — <b>Вчера́ я встал ра́но</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>встать</b> dậy một lần · <b>стоя́ть</b> đứng · '
    '<b>вста́вить</b> cắm vào</div>'
)

# ---------------------------------------------------------------- дальше
S["дальше"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">даль-</span>'
    '<span class="hd-gloss">xa (<b>далеко́</b>, <b>далёкий</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ше</span>'
    '<span class="hd-gloss">đuôi so sánh hơn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <b>-ше</b> là so sánh hơn, cùng khuôn với <b>ра́но</b> → '
    '<b>ра́ньше</b>. Nghĩa đen «xa hơn»; đẩy sang thời gian thì thành «tiếp theo, rồi sao nữa».</div>'
    '<div class="hd-warn">Hai câu cửa miệng: <b>Что да́льше?</b> = Rồi sao nữa? · '
    '<b>Чита́й да́льше</b> = Đọc tiếp đi. Ở đây nó là «tiếp tục», hết dính tới khoảng cách.</div>'
    '<div class="hd-warn"><b>да́льше</b> là trạng từ, đứng một mình. Muốn nói «tuần TỚI, lần '
    'TỚI» thì phải mượn tính từ <b>сле́дующий</b> đặt trước danh từ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>далеко́</b> xa · <b>далёкий</b> xa xôi, cách trở</div>'
)

# ------------------------------------------------------------------ днём
S["днём"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дн-</span>'
    '<span class="hd-gloss">gốc của <b>день</b>, chữ е chạy mất</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ём</span>'
    '<span class="hd-gloss">đuôi cách 5, giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>днём</b> đúng là cách 5 của <b>день</b> đóng băng lại thành trạng '
    'từ thời gian — cùng một khuôn với <b>у́тром</b>, <b>ве́чером</b>, <b>но́чью</b>.</div>'
    '<div class="hd-warn"><b>день</b> đánh rơi chữ е mỗi khi biến cách: <b>день</b> → '
    '<b>дня</b> → <b>днём</b>. Không có dạng «деньём».</div>'
    '<div class="hd-warn">Người Nga cắt ngày làm bốn khúc, nên <b>днём</b> vừa là «ban ngày» '
    'vừa là «buổi chiều» — quãng từ trưa tới chiều muộn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>день</b> ngày · <b>дневно́й</b> thuộc ban ngày · '
    '<b>по́лдень</b> giữa trưa</div>'
)

# ---------------------------------------------------------------- ездить
S["ездить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">е́зд-</span>'
    '<span class="hd-gloss">gốc ĐI XE (<b>е́хать</b>, <b>по́езд</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi nhóm chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp <b>е́хать</b> / <b>е́здить</b> lặp lại đúng cặp <b>идти́</b> / '
    '<b>ходи́ть</b> đã học: <b>е́хать</b> là đang đi xe tới MỘT nơi lúc này, còn <b>е́здить</b> '
    'là đi đi về về, nhiều lần, nhiều hướng.</div>'
    '<div class="hd-warn">Chỉ ngôi «tôi» biến âm зд → зж: <b>я е́зжу</b>. Các ngôi còn lại giữ '
    'nguyên thân: <b>ты е́здишь, они́ е́здят</b>.</div>'
    '<div class="hd-warn">Quá khứ của nó hàm ý ĐÃ VỀ: <b>Я е́здил в Москву́</b> = tôi đi Moskva '
    'rồi về. Đang trên đường thì mới dùng <b>е́хать</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>е́хать</b> đi xe · <b>по́езд</b> tàu hoả · '
    '<b>пое́здка</b> chuyến đi</div>'
)

# -------------------------------------------------------------- заняться
S["заняться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">bắt đầu, chiếm lấy</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ня-</span>'
    '<span class="hd-gloss">gốc LẤY, CẦM (như <b>заня́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">phản thân: làm với chính mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen «tự chiếm lấy mình bằng việc gì» → bắt tay vào làm. Cặp thể '
    'với <b>занима́ться</b>: <b>занима́ться</b> là làm đều đặn, <b>заня́ться</b> là bắt đầu, '
    'làm một đợt.</div>'
    '<div class="hd-warn">Nó đòi CÁCH 5, không phải cách 4: <b>заня́ться спо́ртом</b>, '
    '<b>заня́ться де́лом</b>.</div>'
    '<div class="hd-warn">Thân tương lai đổi hẳn mặt, phải nhớ riêng: <b>займу́сь, займёшься, '
    'займу́тся</b>. Quá khứ trọng âm chạy: <b>заня́лся</b> / <b>заняла́сь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>занима́ться</b> chuyên tâm · <b>заня́тие</b> buổi học · '
    '<b>за́нятый</b> bận</div>'
)

# -------------------------------------------------------------- каникулы
S["каникулы"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ mượn qua tiếng Latin, không chẻ ra mảnh tiếng Nga nào — đừng cố '
    'tìm gốc. Nét phải nhớ nằm chỗ khác: đây là danh từ CHỈ CÓ SỐ NHIỀU, cùng kiểu với '
    '<b>де́ньги</b>, <b>выходны́е</b>.</div>'
    '<div class="hd-warn">Không có dạng số ít, mọi cách đều là số nhiều: <b>кани́кулы, '
    'кани́кул, на кани́кулах</b>.</div>'
    '<div class="hd-warn">Cùng giới từ <b>на</b> mà đổi cách là đổi nghĩa: <b>на кани́кулах</b> '
    '= đang trong kỳ nghỉ, cách 6 · <b>на кани́кулы</b> = đi nghỉ, cách 4.</div>'
    '<div class="hd-why">Đừng lẫn: <b>кани́кулы</b> chỉ là kỳ nghỉ của trường học. Người đi làm '
    'nghỉ phép thì dùng <b>о́тпуск</b> — từ số ít, đếm được.</div>'
)

# ------------------------------------------------------------------ лечь
S["лечь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ле- / ля-</span>'
    '<span class="hd-gloss">gốc NẰM (như <b>лежа́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-чь</span>'
    '<span class="hd-gloss">đuôi nguyên thể của thân tận cùng г/к</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>лежа́ть</b> là ĐANG nằm — một trạng thái. <b>лечь</b> là hạ mình '
    'xuống nằm, một cái là xong — một hành động. Cặp thể của nó là <b>ложи́ться</b>.</div>'
    '<div class="hd-warn">Chia không đoán được, phải thuộc: <b>я ля́гу, ты ля́жешь, они́ '
    'ля́гут</b>; quá khứ <b>лёг</b> / <b>легла́</b>; mệnh lệnh <b>ляг!</b></div>'
    '<div class="hd-warn">Nó nói MỘT lần đã xong: <b>Вчера́ я лёг ра́но</b>. Việc lặp hằng ngày '
    'thì đổi sang <b>ложи́ться</b>. Cụm phải thuộc: <b>лечь спать</b> = đi ngủ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лежа́ть</b> nằm · <b>ложи́ться</b> nằm xuống, chưa hoàn thành · '
    '<b>положи́ть</b> đặt nằm xuống</div>'
)

# -------------------------------------------------------------- ложиться
S["ложиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">лож-</span>'
    '<span class="hd-gloss">vẫn gốc NẰM, đổi mặt chữ từ <b>лечь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-</span>'
    '<span class="hd-gloss">đuôi nhóm chia thứ hai</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">phản thân: tự đặt MÌNH xuống</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỗ khác <b>лечь</b> hiện ngay ở <b>-ся</b>: <b>ложи́ться</b> là tự hạ '
    'mình xuống, làm đi làm lại; <b>лечь</b> không có <b>-ся</b> và chỉ nói một lần đã xong.</div>'
    '<div class="hd-warn">Thói quen thì <b>ложи́ться</b>: <b>Я ложу́сь спать в де́сять</b> — ngày '
    'nào cũng vậy. Một tối cụ thể đã xong thì <b>лечь</b>: <b>Вчера́ я лёг ра́но</b>.</div>'
    '<div class="hd-warn">Mời người khác đi nằm cũng dùng dạng này: <b>Ложи́тесь, '
    'пожа́луйста</b>. Mệnh lệnh <b>ляг!</b> của <b>лечь</b> nghe cộc lốc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лечь</b> nằm xuống, hoàn thành · <b>лежа́ть</b> đang nằm · '
    '<b>положи́ть</b> đặt xuống</div>'
)

# -------------------------------------------------------------- некогда
S["некогда"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не́-</span>'
    '<span class="hd-gloss">tiền tố hút trọng âm: «không có ... mà»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-когда</span>'
    '<span class="hd-gloss">khi nào (<b>когда́</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen «không có LÚC NÀO mà làm» → không có thì giờ. Trọng âm nhảy '
    'lên <b>не́</b>, và <b>когда́</b> mất luôn dấu của nó.</div>'
    '<div class="hd-warn">Bẫy lớn: <b>не́когда</b> trọng âm ĐẦU = không có thì giờ, còn '
    '<b>никогда́</b> trọng âm CUỐI = không bao giờ. Chỉ khác chữ е/и và chỗ đặt trọng âm.</div>'
    '<div class="hd-warn">Câu không có chủ ngữ: người bị đẩy sang cách 3 — <b>Мне не́когда</b>, '
    '<b>Ему́ не́когда чита́ть</b>. Không nói «Я некогда».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>когда́</b> khi nào · <b>никогда́</b> không bao giờ · '
    '<b>иногда́</b> thỉnh thoảng</div>'
)

# ----------------------------------------------------------------- ночью
S["ночью"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ноч-</span>'
    '<span class="hd-gloss">gốc của <b>ночь</b> — đêm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ью</span>'
    '<span class="hd-gloss">đuôi cách 5 của giống cái tận cùng -ь</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>но́чью</b> là cách 5 của <b>ночь</b> đóng băng thành trạng từ thời '
    'gian. <b>ночь</b> thuộc lớp giống cái đuôi mềm <b>-ь</b> nên cách 5 của nó ra <b>-ью</b>, '
    'còn <b>день</b> giống đực thì ra <b>-ём</b>.</div>'
    '<div class="hd-warn">Bộ bốn học liền một thể: <b>у́тром</b> sáng · <b>днём</b> ngày · '
    '<b>ве́чером</b> tối · <b>но́чью</b> đêm — cả bốn đều là cách 5 của danh từ tương ứng.</div>'
    '<div class="hd-warn">Câu chúc ngủ ngon lại dùng cách 2: <b>Споко́йной но́чи!</b> — chỗ đó '
    'là <b>но́чи</b>, không phải <b>но́чью</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ночь</b> đêm · <b>ночно́й</b> thuộc về đêm · '
    '<b>по́лночь</b> nửa đêm</div>'
)

# ---------------------------------------------------------------- обычно
S["обычно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">обы́ч-</span>'
    '<span class="hd-gloss">lệ thường (<b>обы́чай</b> phong tục)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span>'
    '<span class="hd-gloss">đuôi tính từ → <b>обы́чный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">tính từ → trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Luật đã học: tính từ bỏ <b>-ый</b>, thêm <b>-о</b> là ra trạng từ. '
    'Nghĩa đen «theo lệ thường» → «thường thì».</div>'
    '<div class="hd-warn">Nó kể THÓI QUEN nên kéo theo động từ thể chưa hoàn thành: '
    '<b>Обы́чно я встаю́ ра́но</b>. Không ghép được với <b>встать</b> hay <b>лечь</b>.</div>'
    '<div class="hd-warn">Thang tần suất để xếp chỗ cho nó: <b>всегда́</b> luôn luôn, '
    '<b>обы́чно</b> thường, <b>иногда́</b> thỉnh thoảng, <b>никогда́</b> không bao giờ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обы́чный</b> thông thường · <b>необы́чный</b> khác thường · '
    '<b>обы́чай</b> phong tục</div>'
)

# ----------------------------------------------------------------- опять
S["опять"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hư từ ngắn, không chẻ ra mảnh nào còn mang nghĩa riêng trong tiếng Nga '
    'hôm nay. Cái đáng học ở <b>опя́ть</b> là SẮC THÁI dùng, không phải cấu tạo.</div>'
    '<div class="hd-why">Chỗ chỉ mình nó vào được: <b>опя́ть же</b> = vả lại, hơn nữa.</div>'
    '<div class="hd-warn">Nó hay kèm bực bội: <b>Опя́ть ты опозда́л!</b> = Lại trễ nữa rồi! Muốn '
    'trung tính thì nói <b>сно́ва</b>. Nhờ ai nhắc lại phải nói <b>Ещё раз, пожа́луйста</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: <b>опя́ть</b> trông giống <b>пять</b> (số 5) nhưng không '
    'cùng gốc. Đây là chuyện từ nguyên, không phải luật suy ra được — đừng suy nghĩa từ số 5.</div>'
)

# ---------------------------------------------------------------- поздно
S["поздно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по́здн-</span>'
    '<span class="hd-gloss">muộn (<b>по́здний</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">tính từ → trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng khuôn với <b>обы́чно</b>: tính từ <b>по́здний</b> bỏ đuôi, thêm '
    '<b>-о</b> thành trạng từ. Riêng dạng so sánh hơn đổi hẳn mặt: <b>по́зже</b>.</div>'
    '<div class="hd-warn">Cụm <b>здн</b> có chữ <b>д</b> câm — nghe không ra nhưng viết bắt '
    'buộc phải có: <b>по́здно</b>, <b>пра́здник</b>. Bỏ chữ д đi là sai chính tả.</div>'
    '<div class="hd-warn">Trạng từ này làm được cả câu, không cần chủ ngữ: <b>Уже́ по́здно</b> = '
    'Muộn rồi. Còn <b>по́здний</b> là tính từ, phải có danh từ theo sau.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́здний</b> muộn · <b>по́зже</b> muộn hơn · '
    '<b>опозда́ть</b> đến muộn, lỡ</div>'
)

# ----------------------------------------------------------------- пойти
S["пойти"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">bắt đầu, cất bước một chặng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-йти</span>'
    '<span class="hd-gloss">dạng của <b>идти́</b> khi có tiền tố</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>по-</b> gắn vào động từ chuyển động nghĩa là «bắt đầu đi», nên '
    '<b>пойти́</b> là thể hoàn thành của <b>идти́</b>. <b>Я пошёл</b> = tôi đi đây, vừa cất bước.</div>'
    '<div class="hd-warn">Quá khứ không dựng từ nguyên thể mà mượn nguyên của <b>идти́</b>: '
    '<b>пошёл, пошла́, пошли́</b>. Tương lai thì đều đặn: <b>пойду́, пойдёшь</b>.</div>'
    '<div class="hd-warn">Hai câu rủ nhau nghe hằng ngày: <b>Пойдём!</b> hoặc <b>Пошли́!</b> = '
    'Đi thôi!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>идти́</b> đi bộ · <b>ходи́ть</b> đi lại · <b>прийти́</b> đến nơi · '
    '<b>войти́</b> đi vào</div>'
)

# --------------------------------------------------------------- прошлый
S["прошлый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">qua, xuyên qua</span></div>'
    '<div class="hd-row"><span class="hd-piece">-шл-</span>'
    '<span class="hd-gloss">thân quá khứ của «đi» (<b>шёл</b>, <b>шла</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen «đã đi qua rồi». Chính cái thân <b>шл-</b> của <b>пошёл</b> '
    'nay đông cứng lại thành tính từ chỉ thời gian.</div>'
    '<div class="hd-warn">Cụm thời gian phải thuộc, và để ý nó đòi cách 6: '
    '<b>в про́шлом году́</b> = năm ngoái · <b>на про́шлой неде́ле</b> = tuần trước.</div>'
    '<div class="hd-warn">Nó là mặt đối lập của <b>сле́дующий</b>: <b>про́шлая неде́ля</b> tuần '
    'vừa rồi, <b>сле́дующая неде́ля</b> tuần tới.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>проше́дший</b> đã qua · <b>про́шлое</b> quá khứ · '
    '<b>пройти́</b> đi qua, trôi qua</div>'
)

# ------------------------------------------------------------------ свой
S["свой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сво-</span>'
    '<span class="hd-gloss">gốc phản thân, cùng nhà với <b>себя́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-й</span>'
    '<span class="hd-gloss">đuôi đại từ sở hữu (như <b>мой</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Toàn bộ lý do nó tồn tại nằm ở một phép so: <b>Он лю́бит свою́ жену́</b> '
    '= yêu vợ MÌNH, còn <b>Он лю́бит его́ жену́</b> = yêu vợ người KHÁC. <b>свой</b> luôn trỏ về '
    'chủ ngữ của chính câu đó.</div>'
    '<div class="hd-warn">Ngôi 1 và 2 thì <b>свой</b> với <b>мой, твой, наш</b> thay nhau được. '
    'Ngôi 3 thì BẮT BUỘC phân biệt: <b>его́</b>, <b>её</b>, <b>их</b> luôn là người khác.</div>'
    '<div class="hd-warn">Không phải học bảng mới: nó biến cách y hệt <b>мой</b> — '
    '<b>свой, своя́, своё, свои́</b> đối với <b>мой, моя́, моё, мои́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>себя́</b> chính mình · <b>по-сво́ему</b> theo ý mình</div>'
)

# ------------------------------------------------------------ следующий
S["следующий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">след-</span>'
    '<span class="hd-gloss">dấu vết, theo sau (<b>сле́довать</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ущ-</span>'
    '<span class="hd-gloss">đuôi phân từ hiện tại: «đang làm»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là phân từ của <b>сле́довать</b> (nối gót) đông cứng thành tính từ: '
    '«cái đang theo sau» = cái tiếp theo. Đuôi <b>-ущий</b> luôn có nghĩa «đang ...».</div>'
    '<div class="hd-warn">Cụm phải thuộc: <b>на сле́дующей неде́ле</b> tuần tới · '
    '<b>в сле́дующий раз</b> lần tới · <b>Сле́дующий!</b> = Mời người tiếp theo.</div>'
    '<div class="hd-warn">Nó là tính từ nên luôn kéo theo một danh từ. Muốn nói trống không '
    '«tiếp đi, tiếp theo nữa» thì phải đổi sang trạng từ <b>да́льше</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сле́довать</b> đi theo · <b>след</b> dấu vết · '
    '<b>после́дний</b> cuối cùng</div>'
)

# ============================================================ field Vietnamese
# Chỉ sửa dòng thật sự hỏng: có ngoặc chú thích (README §2c cấm), nghĩa sai,
# hoặc trùng NGUYÊN CỤM với một thẻ khác mà bốn badge không tách nổi.
V = {
    # bỏ ngoặc chú thích; "kỳ nghỉ" trơn đã là đề bài của отпуск
    "каникулы": "kỳ nghỉ học, nghỉ hè",
    # bỏ ngoặc; xếp song song đúng kiểu cặp идти/ходить đã có sẵn trong bộ
    "ездить": "đi lại bằng xe, lui tới bằng xe",
    # bỏ ngoặc; nghĩa "bắt đầu mưa/tuyết" không có trong gloss tiếng Anh của thẻ
    "пойти": "đi, bắt đầu đi, khởi hành",
    # "thực hiện" là nghĩa của выполнить, không phải заняться
    "заняться": "bắt tay vào làm, bắt đầu làm, chuyên tâm vào việc gì",
    # thêm nghĩa vị ngữ vô nhân xưng "it is late" mà по́здний không có
    "поздно": "muộn, trễ, muộn rồi",
    # bỏ "cũ" (trùng nguyên cụm với старый, cùng badge adj) và bỏ "vừa qua"
    # (trùng với прошедший, cũng adj) — hai chỗ badge không tách được
    "прошлый": "trước, vừa rồi, trước đó",
}
