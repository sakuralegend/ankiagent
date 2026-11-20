# -*- coding: utf-8 -*-
"""k132 — life::art: lô hỗn hợp — nhóm «nghệ thuật» (tính từ -ный/-енный, danh từ -ство/-ение,
từ mượn sân khấu) + đồ dùng hằng ngày + ba cặp/động từ, soạn từng thẻ độc lập.

Chỗ cần nhất quán trong lô:
(1) gốc ез-/езд- «đi bằng xe» (переезжа́ть/перее́хать) — cùng khuôn với е́хать, уезжа́ть, отъе́зд.
(2) gốc -де- «đặt» (надева́ть/наде́ть) — cùng khuôn với одева́ться, оде́жда; cặp наде́ть ↔ оде́ть.
(3) худож- «tài nghệ» (худо́жественный) — cùng cách chẻ với худо́жник (k35).
(4) gốc дых-/дух- «hơi» (дыша́ть) — cùng nhà với во́здух, духи́ đã soạn.
Họ hàng cố ý vắng: со́ус, реце́пт, пье́са, брю́ки (từ mượn đứng một mình, không có từ phái sinh
thông dụng).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "рецепт": "công thức, đơn thuốc",                        # «;» → «,»
    "поесть": "ăn, ăn một chút",                             # bỏ «(hoàn thành)» — badge đã có
    "автомат": "máy tự động, máy bán hàng tự động, súng tiểu liên",  # gloss: submachine gun/assault rifle
    "переезжать": "chuyển nhà, đi xe qua",                   # RÚT «dọn đi» — trùng убира́ть (cũ); bỏ nhãn thể
    "переехать": "chuyển nhà, đi xe qua",                    # RÚT «dọn đi» — trùng убра́ть (cũ); bỏ nhãn thể
    "культурный": "văn hoá, có văn hoá",                     # «;» → «,»
    "надевать": "mặc vào, đội vào, đeo vào",                 # bỏ nhãn thể; «đeo» = надеть очки́/кольцо́
    "надеть": "mặc vào, đội vào, đeo vào",
}

# -------------------------------------------------------------------- соус
S["соус"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — mượn thẳng tiếng Pháp <i>sauce</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>sauce</i>, nhấn vào âm đầu: <b>со́ус</b>. Tận cùng phụ âm '
    '⇒ giống đực, chia đều. «Sốt gì đó» nói bằng <b>в</b> + cách 6: '
    '<b>ры́ба в тома́тном со́усе</b> = cá sốt cà chua.</div>'
)

# ------------------------------------------------------------------ рецепт
S["рецепт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — mượn Latin <i>receptum</i> «cái đã nhận», '
    'cùng gốc với <i>recipe</i> và <i>receipt</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một chữ, hai nghĩa — đúng như <i>recipe</i> thuở xưa: công thức nấu ăn '
    '(<b>реце́пт сала́та</b>) và đơn thuốc bác sĩ kê. Nhấn âm thứ hai: <b>реце́пт</b>.</div>'
    '<div class="hd-warn"><b>по реце́пту</b> = theo đơn (thuốc kê đơn) · '
    '<b>без реце́пта</b> = không cần đơn.</div>'
)

# ------------------------------------------------------------------ поесть
S["поесть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">«một chút, một lúc» (như <b>погуля́ть</b> dạo một lúc)</span></div>'
    '<div class="hd-row"><span class="hd-piece">есть</span>'
    '<span class="hd-gloss">ĂN</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chia y hệt <b>есть</b>, chỉ gắn thêm <b>по-</b>: <b>пое́шь</b>, <b>пое́ст</b> — số nhiều mọc <b>д</b>: <b>поеди́м</b>, <b>поедя́т</b>; quá khứ <b>пое́л</b>. '
    '<b>Я хочу́ пое́сть</b> = tôi muốn ăn chút gì. Ăn «một ít» món gì thì món đó ở cách 2: '
    '<b>пое́сть хле́ба</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>есть</b> ăn · <b>еда́</b> thức ăn · <b>съесть</b> ăn hết</div>'
)

# -------------------------------------------------------------------- дача
S["дача"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">да-</span>'
    '<span class="hd-gloss">gốc CHO (<b>дать</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ча</span>'
    '<span class="hd-gloss">đuôi danh từ «cái được…» (như <b>сда́ча</b>, <b>зада́ча</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Theo từ nguyên, gốc là «đất được ban cho» ⇒ mảnh đất có nhà ngoài thành phố, '
    'nơi người Nga trồng rau, nghỉ hè.</div>'
    '<div class="hd-warn">Đi với <b>на</b>, không phải <b>в</b>: <b>на да́че</b> = ở dacha · '
    '<b>на да́чу</b> = tới dacha.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дать</b> cho · <b>сда́ча</b> tiền thối lại · '
    '<b>переда́ча</b> chương trình (TV) · <b>зада́ча</b> nhiệm vụ, bài toán</div>'
)

# --------------------------------------------------------------- полотенце
S["полотенце"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">полот-</span>'
    '<span class="hd-gloss">tấm VẢI (<b>полотно́</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-енц-е</span>'
    '<span class="hd-gloss">đuôi thu nhỏ, giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Mảnh vải nhỏ» ⇒ khăn lau, khăn tắm. Trọng âm đứng yên ở <b>-те́-</b>. '
    'Chỗ lệch duy nhất: cách 2 số nhiều bỏ đuôi và chen <b>-е-</b>: <b>мно́го полоте́нец</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>полотно́</b> tấm vải, bức tranh vải</div>'
)

# ----------------------------------------------------------------- кошелёк
S["кошелёк"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кошел-</span>'
    '<span class="hd-gloss">cái túi, cái giỏ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ёк</span>'
    '<span class="hd-gloss">đuôi thu nhỏ, giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái túi nhỏ» ⇒ ví tiền. Đuôi <b>-ёк</b> luôn rụng <b>ё</b> khi thêm đuôi, '
    'trọng âm nhảy xuống đuôi: <b>кошелька́</b>, <b>кошельку́</b>, <b>в кошельке́</b> — y như '
    '<b>огонёк</b> → <b>огонька́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кошёлка</b> giỏ xách đi chợ</div>'
)

# ----------------------------------------------------------------- автомат
S["автомат"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">авто-</span>'
    '<span class="hd-gloss">TỰ (Hy Lạp, như <i>auto-</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мат</span>'
    '<span class="hd-gloss">phần còn lại của <i>automat(ic)</i>, không tách nghĩa riêng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Máy TỰ chạy, không cần người ⇒ máy bán hàng, máy bán vé. '
    '<b>банкома́т</b> (máy ATM) chính là <b>банк</b> + <b>автома́т</b>.</div>'
    '<div class="hd-warn">Trong đời thường <b>автома́т</b> còn là SÚNG TIỂU LIÊN: '
    '<b>автома́т Кала́шникова</b> = khẩu AK.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>автомати́ческий</b> tự động · <b>банкома́т</b> máy ATM</div>'
)

# -------------------------------------------------------------- переезжать
S["переезжать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span>'
    '<span class="hd-gloss">SANG, QUA — từ chỗ này sang chỗ kia</span></div>'
    '<div class="hd-row"><span class="hd-piece">-езжа-</span>'
    '<span class="hd-gloss">gốc ĐI BẰNG XE (<b>ез-/езд-</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đi xe sang chỗ khác ⇒ <b>chuyển nhà</b>: <b>переезжа́ть в Москву́</b> '
    '(<b>в</b> + cách 4). Nghĩa đen vẫn dùng: đi xe qua — <b>переезжа́ть мост</b>. '
    'Chia đều lớp 1: <b>переезжа́ю</b>, <b>переезжа́ешь</b>. Đi BỘ qua thì là '
    '<b>переходи́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>перее́хать</b> (HT) · <b>перее́зд</b> cuộc chuyển nhà · '
    '<b>е́хать</b> đi xe · <b>отъе́зд</b> sự rời đi</div>'
)

# --------------------------------------------------------------- переехать
S["переехать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span>'
    '<span class="hd-gloss">SANG, QUA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́х-ать</span>'
    '<span class="hd-gloss">gốc ĐI BẰNG XE (như <b>е́хать</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hoàn thành của <b>переезжа́ть</b>: chuyển nhà xong. Thân tương lai lấy '
    '<b>е́д-</b> như <b>е́хать</b>: <b>перее́ду</b>, <b>перее́дешь</b>, <b>перее́дут</b> — nhớ '
    '<b>е́ду</b> là ra cả bảng. <b>Мы перее́хали в но́вую кварти́ру.</b></div>'
    '<div class="hd-warn">Xe đè qua ai/cái gì cũng là <b>перее́хать</b> + cách 4: '
    '<b>соба́ку перее́хала маши́на</b> = con chó bị xe cán.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>переезжа́ть</b> (CHT) · <b>перее́зд</b> cuộc chuyển nhà · '
    '<b>прие́хать</b> đến bằng xe · <b>уе́хать</b> rời đi bằng xe</div>'
)

# ------------------------------------------------------------------ дышать
S["дышать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дыш-</span>'
    '<span class="hd-gloss">gốc HƠI THỞ (<b>дых-</b>, х → ш)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể, chia lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc «hơi» này cũng nằm trong <b>во́здух</b>, <b>духи́</b>, <b>о́тдых</b> '
    '(nghỉ = lấy lại hơi). Chia lớp 2, chỉ «tôi» nhấn đuôi, còn lại lùi lên '
    'thân — <b>дышу́</b>, <b>ды́шишь</b>, <b>ды́шат</b>. Bác sĩ hay nói: '
    '<b>Дыши́те глу́бже!</b> = Thở sâu vào!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дыха́ние</b> hơi thở · <b>вдох</b> hơi hít vào · '
    '<b>вы́дох</b> hơi thở ra · <b>о́тдых</b> nghỉ ngơi · <b>во́здух</b> không khí</div>'
)

# ------------------------------------------------------------------- пьеса
S["пьеса"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — mượn tiếng Pháp <i>pièce</i> «một mẩu, một tác phẩm» '
    '(= <i>piece</i>).</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><i>A piece</i> viết cho sân khấu ⇒ vở kịch. Dàn dựng một vở là '
    '<b>ста́вить пье́су</b>.</div>'
    '<div class="hd-warn"><b>пье́са</b> là vở kịch dạng VĂN BẢN (đọc được, in thành sách); buổi diễn '
    'trên sân khấu là <b>спекта́кль</b>: <b>спекта́кль по пье́се Че́хова</b>.</div>'
)

# ------------------------------------------------------------ произведение
S["произведение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-из-</span>'
    '<span class="hd-gloss">đưa RA phía trước (hai tiền tố chồng nhau)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вед-</span>'
    '<span class="hd-gloss">DẪN, ĐƯA (như <b>вести́</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Khớp từng mảnh với <i>pro-duce</i> (ra + dẫn): «cái được làm ra» ⇒ tác phẩm. '
    '<b>произведе́ние иску́сства</b> = tác phẩm nghệ thuật. Trong toán nó cũng là «tích», '
    'đúng như <i>product</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>произвести́</b> / <b>производи́ть</b> sản xuất, tạo ra · '
    '<b>произво́дство</b> sự sản xuất · <b>вести́</b> dẫn</div>'
)

# --------------------------------------------------------- художественный
S["художественный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">худож-</span>'
    '<span class="hd-gloss">TÀI NGHỆ (như <b>худо́жник</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-еств-енн-ый</span>'
    '<span class="hd-gloss">danh từ trừu tượng <b>худо́жество</b> → tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thuộc tài nghệ» ⇒ thuộc nghệ thuật. Dạng ngắn hiếm gặp.</div>'
    '<div class="hd-warn">Hai cụm phải thuộc: <b>худо́жественная литерату́ра</b> = văn học hư cấu '
    '(truyện, tiểu thuyết) · <b>худо́жественный фильм</b> = phim truyện, đối lập phim tài liệu.</div>'
    '<div class="hd-warn">Danh từ «nghệ thuật» là <b>иску́сство</b>, nhưng <b>иску́сственный</b> lại là '
    '«nhân tạo» — tính từ «nghệ thuật» là <b>худо́жественный</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>худо́жник</b> họa sĩ · <b>худо́жество</b> mỹ thuật</div>'
)

# ------------------------------------------------------------ литературный
S["литературный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">литерату́р-</span>'
    '<span class="hd-gloss">VĂN HỌC (<b>литерату́ра</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">→ tính từ «thuộc về…»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ + <b>-ный</b>, trọng âm đứng yên ở <b>-ту́-</b>. Dạng ngắn giống '
    'đực chen <b>-е-</b>: <b>литерату́рен</b>.</div>'
    '<div class="hd-warn"><b>литерату́рный язы́к</b> = ngôn ngữ CHUẨN (tiếng Nga chuẩn mực), '
    'không chỉ là «ngôn ngữ văn chương».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>литерату́ра</b> văn học · <b>литера́тор</b> người viết văn</div>'
)

# -------------------------------------------------------------- культурный
S["культурный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">культу́р-</span>'
    '<span class="hd-gloss">VĂN HOÁ (<b>культу́ра</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">→ tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai nghĩa: «thuộc văn hoá» (<b>культу́рная жизнь</b> đời sống văn hoá) và, '
    'nói về người, «có văn hoá, lịch sự» (<b>культу́рный челове́к</b>). Trạng từ '
    '<b>культу́рно</b> = đúng mực: <b>вести́ себя́ культу́рно</b>. Dạng ngắn chen <b>-е-</b>: '
    '<b>культу́рен</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>культу́ра</b> văn hoá · <b>некульту́рный</b> thiếu văn hoá, thô lỗ · '
    '<b>физкульту́ра</b> thể dục</div>'
)

# -------------------------------------------------------------- творчество
S["творчество"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">твор-</span>'
    '<span class="hd-gloss">TẠO RA (<b>твори́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ч-</span>'
    '<span class="hd-gloss">ц → ч, từ <b>творе́ц</b> người tạo ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ество</span>'
    '<span class="hd-gloss">danh từ trừu tượng, giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Khuôn y hệt <b>оте́ц</b> → <b>оте́чество</b> (tổ quốc): <b>-ец</b> gặp '
    '<b>-ество</b> thì <b>ц</b> thành <b>ч</b>. Nghĩa là việc sáng tác, và cả TOÀN BỘ sáng tác của '
    'một người: <b>тво́рчество Пу́шкина</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>твори́ть</b> sáng tạo · <b>тво́рческий</b> sáng tạo (tính từ) · '
    '<b>творе́ние</b> tác phẩm, tạo vật</div>'
)

# --------------------------------------------------------------------- хор
S["хор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — mượn Hy Lạp, cùng gốc với <i>chorus</i>, <i>choir</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Số nhiều nhấn xuống đuôi: <b>хоры́</b>, <b>хоро́в</b>. <b>петь в хо́ре</b> = '
    'hát trong dàn hợp xướng. Cách 5 <b>хо́ром</b> thành trạng từ «đồng thanh»: '
    '<b>все отве́тили хо́ром</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>хорово́й</b> thuộc hợp xướng · <b>хорово́д</b> điệu múa vòng tròn '
    '(<b>хор</b> + <b>води́ть</b> dẫn)</div>'
)

# ----------------------------------------------------------------- зритель
S["зритель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">зри-</span>'
    '<span class="hd-gloss">gốc NHÌN (<b>зре́ние</b> thị lực)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тель</span>'
    '<span class="hd-gloss">NGƯỜI làm việc ấy</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người nhìn» ⇒ khán giả. Đuôi <b>-тель</b> luôn là giống đực dù tận '
    'cùng <b>-ь</b>, như <b>учи́тель</b>, <b>писа́тель</b>. Cả khán phòng là số nhiều: '
    '<b>зри́тели</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>зре́ние</b> thị lực · <b>зри́тельный зал</b> khán phòng · '
    '<b>зре́лище</b> cảnh tượng, màn trình diễn</div>'
)

# ---------------------------------------------------------------- трагедия
S["трагедия"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">траге́д-</span>'
    '<span class="hd-gloss">= <i>traged-</i> tiếng Anh (Hy Lạp)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ия</span>'
    '<span class="hd-gloss">= đuôi <i>-y</i>, danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><i>Tragedy</i> đổi <i>-y</i> → <b>-ия</b>, như <b>коме́дия</b>. '
    'Hai nghĩa như tiếng Anh: vở bi kịch, và chuyện đau lòng ngoài đời — '
    '<b>Для неё э́то траге́дия.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>траги́ческий</b> / <b>траги́чный</b> bi thảm (trọng âm dời sang '
    '<b>-ги́-</b>)</div>'
)

# ------------------------------------------------------------------- брюки
S["брюки"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — mượn tiếng Hà Lan <i>broek</i>, cùng gốc với '
    '<i>breeches</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỉ có SỐ NHIỀU, như <b>джи́нсы</b>: một cái quần vẫn là <b>брю́ки</b>. '
    'Cách 2 không đuôi: <b>нет брюк</b>. Mặc quần vào: <b>наде́ть брю́ки</b>.</div>'
    '<div class="hd-warn">Đếm thì đếm theo ĐÔI: hai cái quần = <b>две па́ры брюк</b>.</div>'
)

# ---------------------------------------------------------------- надевать
S["надевать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">LÊN, đặt lên trên</span></div>'
    '<div class="hd-row"><span class="hd-piece">-де-</span>'
    '<span class="hd-gloss">gốc ĐẶT (<b>деть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва-ть</span>'
    '<span class="hd-gloss">hậu tố chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đặt lên người» ⇒ mặc, đội, đeo bất cứ món gì: <b>надева́ть ку́ртку</b>, '
    '<b>ша́пку</b>, <b>очки́</b>. Chia đều lớp 1: <b>надева́ю</b>, <b>надева́ешь</b>.</div>'
    '<div class="hd-warn">Cặp hay nhầm: <b>надева́ть</b> + MÓN ĐỒ (<b>надева́ть пальто́</b>) · '
    '<b>одева́ть</b> + NGƯỜI (<b>одева́ть ребёнка</b> = mặc đồ cho con).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>наде́ть</b> (HT) · <b>одева́ться</b> mặc đồ · <b>оде́жда</b> quần áo · '
    '<b>раздева́ться</b> cởi đồ</div>'
)

# ------------------------------------------------------------------ надеть
S["надеть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">LÊN, đặt lên trên</span></div>'
    '<div class="hd-row"><span class="hd-piece">-де-ть</span>'
    '<span class="hd-gloss">gốc ĐẶT (<b>деть</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>надева́ть</b> bỏ <b>-ва-</b> ⇒ hoàn thành: mặc vào xong. Thân tương lai '
    'mọc thêm <b>-н-</b>, phải nhớ riêng: <b>наде́ну</b>, <b>наде́нешь</b>, <b>наде́нут</b> — y như '
    '<b>оде́нусь</b>. <b>Наде́нь ша́пку!</b> = Đội mũ vào!</div>'
    '<div class="hd-warn"><b>наде́ть</b> + MÓN ĐỒ (<b>наде́ть шу́бу</b>) · <b>оде́ть</b> + NGƯỜI '
    '(<b>оде́ть ребёнка</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>надева́ть</b> (CHT) · <b>оде́ться</b> mặc đồ · <b>оде́жда</b> quần áo · '
    '<b>разде́ться</b> cởi đồ</div>'
)
