# -*- coding: utf-8 -*-
"""k82 — tu-moi: 7 từ user vừa thêm, KHÔNG cùng họ nhau.

Mỗi thẻ soạn độc lập, không ép trục chung, không khối hệ thống. Ba thẻ có họ
đã nằm trong kho (здоро́вый→здоро́вье, съе́здить→е́здить, термо́метр→метр):
chỉ trỏ về, không kể lại, và nói cái thẻ kia CHƯA nói.
"""

S = {}

# -------------------------------------------------------------- дельфин
# Từ mượn nguyên khối, không có từ phái sinh Nga nào đáng học ⇒ BỎ mục Họ hàng
# (lựa chọn có ý thức, xem README §2).
S["дельфин"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn nguyên khối từ Hy Lạp '
    '<i>delphís</i> (thân <i>delphin-</i>), cũng chính là <i>dolphin</i> '
    'tiếng Anh. Chữ <b>-ин</b> ở cuối là phần thân Hy Lạp, không phải hậu tố '
    'Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vì <b>-ин</b> không phải hậu tố «người» như ở '
    '<b>англича́нин</b> → <b>англича́не</b>, số nhiều của nó hoàn toàn bình '
    'thường: <b>дельфи́ны</b>. Trọng âm đứng yên trên <b>и</b> ở mọi dạng.</div>'
)

# ------------------------------------------------------------- здоровый
S["здоровый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">здоро́в-</span>'
    '<span class="hd-gloss">gốc KHOẺ — mặt Nga của cặp здоров-/здрав- đã kể ở '
    'thẻ <b>здоро́вье</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là tính từ gốc, từ đó mới có <b>здоро́вье</b> và '
    '<b>здра́вствуйте</b>. Chỗ riêng của tính từ: dạng ngắn <b>здоро́в, '
    'здоро́ва</b> giữ nguyên trọng âm, và chính dạng ngắn đó đứng trong '
    '<b>Будь здоро́в!</b> — nói khi ai hắt hơi, hoặc lúc chia tay «giữ sức khoẻ '
    'nhé». Khẩu ngữ còn dùng cho «to đùng»: <b>здоро́вый па́рень</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: từ nguyên, không phải luật. '
    '<b>здоро́в-</b> được cho là <b>съ-</b> + gốc «cây» (<b>де́рево</b>): khoẻ = '
    '«chắc như thân cây tốt».</div>'
    '<div class="hd-warn">Trọng âm đổi là đổi từ: <b>здо́рово</b> = «tuyệt!», '
    'còn <b>здоро́во</b> = «chào!» thân mật giữa bạn bè.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>здоро́вье</b> sức khoẻ · <b>здра́вствуйте</b> xin chào · '
    '<b>вы́здороветь</b> khỏi bệnh · <b>нездоро́вый</b> ốm yếu, không lành mạnh</div>'
)

# -------------------------------------------------------------- молоток
S["молоток"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мо́лот-</span>'
    '<span class="hd-gloss">BÚA LỚN — cái búa trong «серп и мо́лот» búa liềm'
    '</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́к</span>'
    '<span class="hd-gloss">hậu tố «nhỏ», như <b>кусо́к</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Búa lớn của thợ rèn thu nhỏ lại thành cái búa cầm tay '
    'đóng đinh hằng ngày. Đừng dùng <b>молото́к</b> cho biểu tượng búa liềm — '
    'ở đó là <b>мо́лот</b> không có <b>-ок</b>.</div>'
    '<div class="hd-warn">Hậu tố <b>-о́к</b> kéo trọng âm về mình, rồi ở mọi '
    'cách khác chữ <b>о</b> rơi mất: <b>молотка́, молотко́м</b>, số nhiều '
    '<b>молотки́</b> — y hệt <b>кусо́к → куска́</b>.</div>'
    '<div class="hd-warn"><b>прода́ть с молотка́</b> = bán đấu giá — «từ cái '
    'búa» của người điều hành gõ xuống.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мо́лот</b> búa tạ · <b>молоти́ть</b> đập lúa, nện · '
    '<b>молото́чек</b> búa nhỏ xíu</div>'
)

# -------------------------------------------------------------- пустошь
S["пустошь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пуст-</span>'
    '<span class="hd-gloss">gốc TRỐNG, RỖNG (<b>пусто́й</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ошь</span>'
    '<span class="hd-gloss">hậu tố danh từ hiếm, giống cái, không nghĩa riêng'
    '</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đất TRỐNG không ai dùng — bãi hoang, mảnh đất bỏ. Đuôi '
    '<b>ш + ь</b> cho biết giống cái ngay: danh từ tận cùng ж/ш/ч/щ mà có '
    '<b>ь</b> thì luôn giống cái (<b>мышь, ночь, вещь</b>). Trọng âm đứng yên '
    'ở <b>пу́-</b>.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>пусты́ня</b> sa mạc: <b>пу́стошь</b> '
    'là đất bỏ hoang không canh tác, có thể nằm ngay giữa vùng mưa ẩm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пусто́й</b> trống rỗng · <b>пусты́ня</b> sa mạc · '
    '<b>пустота́</b> sự trống rỗng · <b>пустя́к</b> chuyện vặt</div>'
)

# ---------------------------------------------------------------- серый
S["серый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn <b>сер-</b> «xám» + đuôi tính từ <b>-ый</b>, '
    'không chẻ thêm được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Xám là màu của ngày không nắng và của thứ không nổi '
    'bật, nên từ này chạy sang nghĩa ảm đạm / mờ nhạt: <b>се́рые бу́дни</b> '
    'ngày thường xám xịt, <b>се́рая мышь</b> người mờ nhạt. Dạng ngắn giống cái '
    'nhảy trọng âm ra đuôi: <b>сер, сера́, се́ро, се́ры</b> — <b>сера́</b> (xám) '
    'khác hẳn danh từ <b>се́ра</b> lưu huỳnh, gốc của <b>се́рный</b>.</div>'
    '<div class="hd-warn">Tóc bạc KHÔNG phải <b>се́рый</b>: tiếng Nga có từ '
    'riêng <b>седо́й</b>. <b>се́рый</b> là xám của đồ vật, bầu trời, mắt '
    '(<b>се́рые глаза́</b>).</div>'
    '<div class="hd-warn"><b>се́рая зарпла́та</b> = lương «xám», một phần trả '
    'ngoài sổ sách để né thuế · <b>се́рый кардина́л</b> = người giật dây trong '
    'bóng tối.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>се́ренький</b> xám nhạt · <b>серова́тый</b> hơi xám · '
    '<b>сере́ть</b> ngả xám · <b>се́рость</b> sự tẻ nhạt, xám xịt</div>'
)

# ------------------------------------------------------------- съездить
S["съездить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">съ-</span>'
    '<span class="hd-gloss">tiền tố thể: MỘT CHUYẾN trọn, đi rồi về — '
    '<b>ъ</b> vì <b>е</b> đứng ngay sau</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́зд-</span>'
    '<span class="hd-gloss">gốc ĐI XE (<b>е́здить</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi nhóm chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thể hoàn thành của đúng nghĩa đi-về mà thẻ '
    '<b>е́здить</b> đã nói: <b>съе́здить в Москву́</b> = đi Moskva MỘT chuyến, '
    'đã về. Chia y hệt <b>е́здить</b> (kể cả зд → зж ở «tôi»: <b>я '
    'съе́зжу</b>), nhưng vì hoàn thành nên các dạng ấy chỉ TƯƠNG LAI: <b>Я '
    'съе́зжу за хле́бом</b> = tôi chạy đi mua bánh mì rồi về ngay. Cặp đi bộ '
    'song song: <b>ходи́ть</b> → <b>сходи́ть</b>.</div>'
    '<div class="hd-warn"><b>с-</b> ở đây KHÔNG phải с- «dồn về / xuống khỏi» '
    'của <b>съезд</b>. Ba từ nhìn giống nhau mà khác hẳn: <b>съе́здить</b> đi '
    'một chuyến rồi về · <b>съе́хать</b> trượt xuống, dọn nhà đi · '
    '<b>съе́хаться</b> tụ về một chỗ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>е́здить</b> đi lại bằng xe · <b>сходи́ть</b> đi bộ '
    'một chuyến rồi về · <b>сбе́гать</b> chạy đi rồi về · <b>пое́здка</b> chuyến '
    'đi</div>'
)

# ------------------------------------------------------------ термометр
S["термометр"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">термо-</span>'
    '<span class="hd-gloss">NHIỆT — Hy Lạp <i>thermós</i>, chữ <i>thermo</i> '
    'của <i>thermos</i> tiếng Anh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-метр</span>'
    '<span class="hd-gloss">CÁI ĐO — mảnh đã học ở thẻ <b>метр</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái đo nhiệt = nhiệt kế; thẻ <b>метр</b> đã xếp nó cạnh '
    '<b>баро́метр</b>. Trọng âm rơi vào chữ <b>о́</b> nối giữa hai mảnh.</div>'
    '<div class="hd-warn">Trọng âm tách hai lớp từ: DỤNG CỤ đo → <b>-о́метр</b> '
    '(<b>термо́метр, баро́метр, спидо́метр</b>); ĐƠN VỊ đo → <b>-ме́тр</b> '
    '(<b>киломе́тр, сантиме́тр</b>).</div>'
    '<div class="hd-warn">Cặp nhiệt độ cho người ốm ở nhà thường gọi là '
    '<b>гра́дусник</b> (từ <b>гра́дус</b> độ); <b>термо́метр</b> nghe kỹ thuật '
    'hơn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>метр</b> mét · <b>те́рмос</b> bình giữ nhiệt · '
    '<b>терма́льный</b> nhiệt, suối nóng · <b>баро́метр</b> áp kế</div>'
)

# ---------------------------------------------------- field Vietnamese (§2c)
# серый: bỏ «xám xịt» vì trùng пасмурный (k53, đã xong, không được sửa nó);
#        giữ «ảm đạm» vì gloss Anh có dull/drab/dreary và không trùng thẻ nào.
#        Không dùng «tẻ nhạt»: trùng будничный (cùng adj).
# съездить: bản cũ có ngoặc «(bằng phương tiện)» — vi phạm §2c. Badge PERF/IMPF
#        đã tách nó với е́здить («đi lại bằng xe, lui tới bằng xe»).
V = {
    "серый": "màu xám, ảm đạm",
    "съездить": "đi một chuyến bằng xe, đi rồi về bằng xe",
}
