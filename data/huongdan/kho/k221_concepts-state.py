# -*- coding: utf-8 -*-
"""k221 — concepts::state (lô trộn): chính trị, công lý, tiền hối lộ, đoán trước, giấc mơ.

Chỗ cần nhất quán trong lô:
(1) пред- TRƯỚC (như пре́док, предположи́ть đã có): предсказа́ть/предска́зывать NÓI trước,
    предви́деть THẤY trước, предвы́борный trước cuộc bầu. -каз- NÓI RA như сказа́ть, рассказа́ть.
(2) добр- TỐT LÀNH (до́брый): одо́брить/одобря́ть = «coi là tốt».
(3) влек- KÉO, у- mờ nghĩa (như увлека́ться, увлече́ние); о-хот- MUỐN, о- mờ nghĩa (như охо́та).
(4) демо- DÂN + -крат- QUYỀN (như демократи́ческий); отеч- CHA (như оте́чественный).
(5) сни́ться/присни́ться: người mơ ở cách 3, cái được mơ thấy là chủ ngữ (khớp thẻ сон, мечта́ть).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "улучшение": "sự cải thiện, sự cải tiến, sự chuyển biến tốt",   # thiếu recovery/upturn; «sự tiến bộ» = прогресс
    "имидж": "hình ảnh, hình ảnh trước công chúng, danh tiếng",     # RÚT «uy tín»: nới rộng (авторитет, престиж)
    "увлекательный": "hấp dẫn, cuốn hút, lôi cuốn",                 # «say mê» là của NGƯỜI (увлечённый), không phải của vật
    "одобрять": "tán thành, phê duyệt, chấp thuận",                 # khớp одобрить; «đồng ý» là соглашаться
    "взятка": "tiền hối lộ, của đút lót",                           # bỏ nghĩa bài bạc (hiếm); «sự hối lộ» là hành vi
    "льгота": "ưu đãi, sự miễn giảm",                               # «đặc quyền» là привилегия (k204)
    "либеральный": "theo chủ nghĩa tự do, tự do, phóng khoáng",     # «dễ dãi» gloss không có; đưa nghĩa chính lên đầu
    "коррупция": "tham nhũng",                                      # «sự hối lộ» là взятка / взяточничество
    "предсказывать": "tiên đoán, dự đoán, đoán trước",              # khớp предсказать; «báo trước» là предупредить
    "предвидеть": "thấy trước, lường trước, tiên liệu",             # «dự đoán trước» trùng предсказать
    "сниться": "hiện ra trong giấc mơ, mơ thấy",                    # khớp присниться; «được mơ thấy» chỉ lặp nghĩa 1
}

# --------------------------------------------------------------------- квадрат
S["квадрат"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">квадра́т</span><span class="hd-gloss">mượn '
    'nguyên khối: Latin <i>quadratus</i> «vuông», từ <i>quattuor</i> BỐN</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hình BỐN cạnh bằng nhau, BỐN góc vuông ⇒ hình vuông, ô vuông. Cùng gốc tiếng Anh '
    '<i>quadrant, quadratic</i>. Diện tích hình vuông là «cạnh nhân cạnh» nên nó còn là '
    'bình phương, y như <i>square</i>.</div>'
    '<div class="hd-warn"><b>в квадра́те</b> = bình phương: <b>пять в квадра́те</b> = 5².</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>квадра́тный</b> vuông · <b>квадра́тный метр</b> mét vuông · '
    '<b>квадра́тик</b> ô vuông nhỏ</div>'
)

# --------------------------------------------------------------------- блестеть
S["блестеть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">блест-</span><span class="hd-gloss">LẤP LÁNH — '
    'như <b>блеск</b> ánh lấp lánh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ть</span><span class="hd-gloss">đuôi nguyên '
    'thể; ở đây chia lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ này đẻ ra <b>блестя́щий</b> «đang lấp lánh». Mắt, tóc, sàn nhà, '
    'vàng… hắt ánh sáng lại thì <b>блестя́т</b>; người trổ tài thì «toả sáng».</div>'
    '<div class="hd-why">Chỉ ngôi «tôi» đổi <i>ст → щ</i>: <b>я блещу́</b>, còn lại giữ '
    '<i>ст</i>: <b>ты блести́шь</b>, <b>они́ блестя́т</b>. Trọng âm luôn ở đuôi.</div>'
    '<div class="hd-warn">Ánh lên VÌ gì: <b>от</b> + cách 2 — <b>Глаза́ блестя́т от '
    'ра́дости.</b> Mắt sáng lên vì vui.</div>'
    '<div class="hd-warn"><b>Не всё то зо́лото, что блести́т.</b> Không phải cứ lấp lánh là '
    'vàng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>блестя́щий</b> sáng bóng, xuất sắc · <b>блеск</b> ánh lấp lánh · '
    '<b>блесну́ть</b> loé lên (HT)</div>'
)

# --------------------------------------------------------------------- улучшение
S["улучшение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span><span class="hd-gloss">làm cho TRỞ '
    'NÊN…</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лучш-</span><span class="hd-gloss">TỐT HƠN — '
    'như <b>лу́чше</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ние</span><span class="hd-gloss">đuôi danh từ, '
    'giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>улу́чшить</b>: việc trở nên tốt hơn ⇒ sự cải thiện; '
    'người bệnh khá lên cũng là <b>улучше́ние</b>. Trọng âm rời <i>лу́</i> sang <i>-е́ние</i>.</div>'
    '<div class="hd-warn">Cải thiện CÁI GÌ: cách 2 — <b>улучше́ние усло́вий</b> cải thiện điều '
    'kiện. Lật ngược: <b>ухудше́ние</b> sự xấu đi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>улу́чшить</b> / <b>улучша́ть</b> cải thiện · <b>улу́чшиться</b> tốt '
    'lên · <b>лу́чший</b> tốt nhất</div>'
)

# --------------------------------------------------------------------- имидж
S["имидж"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn nguyên tiếng Anh <i>image</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỉ lấy ĐÚNG MỘT nghĩa của <i>image</i>: hình ảnh mà một người hay một '
    'hãng dựng lên trước mắt công chúng. Trọng âm ở đầu như tiếng Anh, đứng yên suốt '
    'bảng.</div>'
    '<div class="hd-warn">Tiếng Anh dùng chung <i>image</i>, tiếng Nga tách: hình vẽ, hình hiện '
    'trên màn là <b>изображе́ние</b>, tấm ảnh chụp là <b>фотогра́фия</b>.</div>'
    '<div class="hd-warn"><b>смени́ть и́мидж</b> = thay đổi hình ảnh (tóc, áo, phong cách).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>имиджме́йкер</b> người xây dựng hình ảnh (<i>image-maker</i>)</div>'
)

# --------------------------------------------------------------------- увлекательный
S["увлекательный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span><span class="hd-gloss">tiền tố — ở từ '
    'này không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-влек-</span><span class="hd-gloss">KÉO, LÔI — '
    'như <b>увлека́ться</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-тельный</span><span class="hd-gloss">«có sức '
    'gây ra việc đó»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Có sức LÔI người ta theo ⇒ cuốn hút: phim, truyện, chuyến đi. Dạng '
    'ngắn giống đực chèn <i>е</i>: <b>увлека́телен</b>, nhưng <b>увлека́тельна</b>; trạng từ '
    '<b>увлека́тельно</b>.</div>'
    '<div class="hd-warn">Cùng gốc, cùng đuôi, khác tiền tố: <b>привлека́тельный</b> kéo VỀ '
    'PHÍA mình (ngoại hình, lời mời hấp dẫn); <b>увлека́тельный</b> cuốn ta ĐI THEO (câu '
    'chuyện). Còn NGƯỜI đang say mê là <b>увлечённый</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>увлека́ться</b> say mê · <b>увлече́ние</b> niềm say mê · '
    '<b>развлече́ние</b> trò giải trí</div>'
)

# --------------------------------------------------------------------- несправедливость
S["несправедливость"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не-</span><span class="hd-gloss">KHÔNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">справедли́в-</span><span class="hd-gloss">công '
    'bằng — <b>справедли́вый</b>, gốc <i>-прав-</i> ĐÚNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span><span class="hd-gloss">tính từ → '
    'danh từ trừu tượng, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>несправедли́вый</b> bất công + <i>-ость</i> ⇒ sự bất công. Trọng âm '
    'đứng nguyên chỗ của tính từ. Số nhiều <b>несправедли́вости</b> là những chuyện bất công '
    'cụ thể.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>справедли́вость</b> sự công bằng · <b>несправедли́вый</b> bất công · '
    '<b>пра́вда</b> sự thật · <b>пра́во</b> quyền</div>'
)

# --------------------------------------------------------------------- одобрить
S["одобрить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span><span class="hd-gloss">ghép với tính từ '
    'thành động từ; ở đây: COI LÀ…</span></div>'
    '<div class="hd-row"><span class="hd-piece">-до́бр-</span><span class="hd-gloss">TỐT LÀNH — '
    'như <b>до́брый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span><span class="hd-gloss">đuôi lớp chia '
    '2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Coi là tốt rồi gật đầu ⇒ tán thành, phê duyệt — xong một lần. Trọng '
    'âm giữ nguyên chỗ của <b>до́брый</b>: <b>одо́брю</b>, <b>одо́бришь</b>, <b>одо́брят</b>. Cặp '
    'CHT: <b>одобря́ть</b>.</div>'
    '<div class="hd-warn">Được ngân hàng duyệt vay: <b>Мне одо́брили креди́т.</b> Người được '
    'duyệt ở cách 3.</div>'
    '<div class="hd-warn">Đổi <i>о-</i> thành <i>у-</i> là <b>удо́брить</b> bón phân («làm cho '
    'đất tốt»): <b>одобре́ние</b> sự tán thành, <b>удобре́ние</b> phân bón.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>одобре́ние</b> sự tán thành · <b>до́брый</b> tốt bụng · '
    '<b>добро́</b> điều thiện</div>'
)

# --------------------------------------------------------------------- одобрять
S["одобрять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span><span class="hd-gloss">ghép với tính từ '
    'thành động từ; ở đây: COI LÀ…</span></div>'
    '<div class="hd-row"><span class="hd-piece">-добр-</span><span class="hd-gloss">TỐT LÀNH — '
    'như <b>до́брый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ть</span><span class="hd-gloss">đuôi thể CHƯA '
    'hoàn thành, chia đều: <b>одобря́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vẫn là coi cái gì đó là tốt ⇒ tán thành — thái độ kéo dài, hay lặp '
    'lại. Trọng âm dời từ <i>до́</i> (<b>одо́брить</b>) sang đuôi <i>-я́ть</i>.</div>'
    '<div class="hd-warn">Tiếng Anh <i>approve of</i> có giới từ, tiếng Nga thì cách 4 đi '
    'thẳng: <b>Я не одобря́ю твой вы́бор.</b> Tôi không tán thành lựa chọn của cậu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>одо́брить</b> (HT) · <b>одобре́ние</b> sự tán thành · '
    '<b>до́брый</b> tốt bụng</div>'
)

# --------------------------------------------------------------------- взятка
S["взятка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">взят-</span><span class="hd-gloss">ĐÃ LẤY — '
    '<b>взять</b>, <b>взя́тый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span><span class="hd-gloss">đuôi danh từ '
    'giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Món lấy được» ⇒ tiền hối lộ (nhìn từ phía kẻ nhận). Nguyên âm chạy: '
    'chỉ cách 2 số nhiều chèn <i>о</i> — <b>мно́го взя́ток</b>.</div>'
    '<div class="hd-warn">Hai chiều: <b>дать взя́тку</b> đưa hối lộ ↔ <b>взять взя́тку</b> nhận '
    'hối lộ. Việc thường làm thì <b>дава́ть</b> / <b>брать взя́тки</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>взять</b> lấy · <b>взя́точник</b> kẻ ăn hối lộ · '
    '<b>взя́точничество</b> nạn hối lộ</div>'
)

# --------------------------------------------------------------------- льгота
S["льгота"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">льг-</span><span class="hd-gloss">gốc cổ NHẸ, '
    'DỄ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́т-а</span><span class="hd-gloss">đuôi danh từ '
    'giống cái, như <b>доброта́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Được làm cho NHẸ gánh ⇒ ưu đãi, miễn giảm mà nhà nước hay cơ quan cho '
    'một nhóm người (người về hưu, sinh viên). Hay ở số nhiều: <b>льго́ты</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: từ nguyên — <i>льг-</i> cùng gốc cổ với <b>лёгкий</b> nhẹ '
    'và mảnh <i>-льз-</i> của <b>по́льза</b>, <b>нельзя́</b>; không phải luật suy ra được.</div>'
    '<div class="hd-warn">Ưu đãi về khoản gì: <b>на</b> + cách 4 — <b>льго́та на прое́зд</b>; cho '
    'AI: <b>для</b> + cách 2 — <b>льго́ты для студе́нтов</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>льго́тный</b> ưu đãi: <b>льго́тный биле́т</b> vé giảm giá · '
    '<b>лёгкий</b> nhẹ, dễ</div>'
)

# --------------------------------------------------------------------- предвыборный
S["предвыборный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пред-</span><span class="hd-gloss">TRƯỚC — như '
    '<b>пре́док</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-вы́бор-</span><span class="hd-gloss"><b>вы́боры</b> '
    'cuộc bầu cử (<i>вы-</i> RA + <i>-бор-</i> LẤY)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span><span class="hd-gloss">đuôi tính '
    'từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thuộc về lúc TRƯỚC ngày bầu ⇒ trước bầu cử, tranh cử. Trọng âm giữ ở '
    '<i>вы́</i> như <b>вы́боры</b>.</div>'
    '<div class="hd-why">Bảng dưới có in dạng ngắn <b>предвы́борен</b> (chèn <i>е</i>), nhưng '
    'tính từ chỉ quan hệ như từ này thực tế chỉ dùng dạng dài.</div>'
    '<div class="hd-warn"><b>предвы́борная кампа́ния</b> chiến dịch tranh cử · '
    '<b>предвы́борные обеща́ния</b> lời hứa trước bầu cử.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́бор</b> sự lựa chọn · <b>вы́боры</b> cuộc bầu cử · '
    '<b>вы́брать</b> chọn, bầu</div>'
)

# --------------------------------------------------------------------- либеральный
S["либеральный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">либер-</span><span class="hd-gloss">Latin '
    '<i>liber</i> TỰ DO — như <i>liberty</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́льный</span><span class="hd-gloss">đuôi tính từ '
    '= tiếng Anh <i>-al</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>liberal</i>: về chính trị là theo chủ nghĩa tự do; về tính '
    'người, cách dạy dỗ là phóng khoáng, không khắt khe. Dạng ngắn giống đực chèn <i>е</i>: '
    '<b>либера́лен</b>, nhưng <b>либера́льна</b>.</div>'
    '<div class="hd-warn">«Tự do» = rảnh, không bị buộc thì là <b>свобо́дный</b>. '
    '<b>либера́льный</b> nói về quan điểm, cách đối xử: <b>либера́льные взгля́ды</b> quan điểm '
    'tự do.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>либера́л</b> người theo chủ nghĩa tự do · <b>либерали́зм</b> chủ '
    'nghĩa tự do</div>'
)

# --------------------------------------------------------------------- референдум
S["референдум"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ре-</span><span class="hd-gloss">LẠI — Latin '
    '<i>re-</i>, như <b>рефо́рма</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-фер-</span><span class="hd-gloss">MANG, ĐƯA — '
    'Latin <i>ferre</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ндум</span><span class="hd-gloss">Latin '
    '<i>-endum</i> «điều PHẢI được…»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Điều phải được đưa trở lại» cho dân quyết ⇒ cuộc trưng cầu dân ý = '
    '<i>referendum</i>. Mượn nguyên khối nhưng biến cách như danh từ giống đực thường: '
    '<b>на рефере́ндуме</b>.</div>'
    '<div class="hd-warn"><b>провести́ рефере́ндум</b> tổ chức trưng cầu dân ý.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рефера́т</b> bài tóm lược (cùng Latin <i>referre</i>)</div>'
)

# --------------------------------------------------------------------- отечество
S["отечество"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">оте́ч-</span><span class="hd-gloss">CHA — như '
    '<b>оте́ц</b> (<i>ц → ч</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-еств-о</span><span class="hd-gloss">đuôi danh từ, '
    'giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đất của cha» ⇒ tổ quốc, y hệt <i>fatherland</i>. Trang trọng hơn '
    '<b>ро́дина</b> (nơi mình SINH RA) — gặp trong diễn văn, sử sách, thường viết hoa.</div>'
    '<div class="hd-warn">Khác nhau một chữ <i>е</i> và chỗ nhấn: <b>оте́чество</b> tổ quốc ↔ '
    '<b>о́тчество</b> tên đệm theo cha.</div>'
    '<div class="hd-warn"><b>День защи́тника Оте́чества</b> — Ngày Người bảo vệ Tổ quốc, '
    '23/2.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оте́ц</b> cha · <b>оте́чественный</b> nội địa, trong nước · '
    '<b>о́тчество</b> tên đệm theo cha</div>'
)

# --------------------------------------------------------------------- демократ
S["демократ"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">демо-</span><span class="hd-gloss">Hy Lạp '
    '<i>demos</i> DÂN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-кра́т</span><span class="hd-gloss">Hy Lạp '
    '<i>kratos</i> quyền cai trị; ở cuối từ chỉ NGƯỜI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người muốn quyền về tay dân ⇒ người theo dân chủ = <i>democrat</i>; '
    'cũng là đảng viên Đảng Dân chủ. Trọng âm ở <i>-кра́т</i> suốt bảng: <b>демокра́ты</b>.</div>'
    '<div class="hd-warn">Đổi nửa đầu, giữ <i>-кра́т</i>: <b>аристокра́т</b> quý tộc, '
    '<b>бюрокра́т</b> kẻ quan liêu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>демокра́тия</b> nền dân chủ · <b>демократи́ческий</b> dân chủ</div>'
)

# --------------------------------------------------------------------- коррупция
S["коррупция"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кор-</span><span class="hd-gloss">Latin '
    '<i>com-</i>, ở đây chỉ nhấn mạnh: HẲN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-руп-</span><span class="hd-gloss">Latin '
    '<i>rupt-</i> VỠ, như <i>rupture, bankrupt</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ция</span><span class="hd-gloss">= tiếng Anh '
    '<i>-tion</i>, danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Vỡ hẳn, hỏng hẳn» từ bên trong ⇒ tham nhũng = <i>corruption</i>. Hai '
    'chữ <i>р</i> như hai chữ <i>r</i> tiếng Anh. Thường chỉ dùng số ít.</div>'
    '<div class="hd-warn"><b>корру́пция</b> là cả tệ nạn, không đếm được; một món tiền đút cụ '
    'thể là <b>взя́тка</b>.</div>'
    '<div class="hd-warn"><b>борьба́ с корру́пцией</b> cuộc chống tham nhũng (<b>с</b> + cách '
    '5).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>коррупционе́р</b> kẻ tham nhũng · <b>коррупцио́нный</b> thuộc tham '
    'nhũng · <b>коррумпи́рованный</b> bị tha hoá, tham nhũng</div>'
)

# --------------------------------------------------------------------- охотно
S["охотно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span><span class="hd-gloss">tiền tố mờ nghĩa, '
    'ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-хо́т-</span><span class="hd-gloss">MUỐN — '
    '<b>хоте́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-о</span><span class="hd-gloss">đuôi trạng '
    'từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm vì chính mình MUỐN ⇒ sẵn lòng, vui vẻ. Từ này giữ nghĩa gốc «sự '
    'thèm muốn» của <b>охо́та</b>, không dính gì tới đi săn.</div>'
    '<div class="hd-warn">Trái nghĩa: <b>неохо́тно</b> miễn cưỡng. So sánh hơn: '
    '<b>охо́тнее</b> sẵn lòng hơn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>охо́та</b> sự thèm muốn; việc đi săn · <b>хоте́ть</b> muốn · '
    '<b>неохо́та</b> ngại, không buồn làm</div>'
)

# --------------------------------------------------------------------- предсказать
S["предсказать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пред-</span><span class="hd-gloss">TRƯỚC — như '
    '<b>предположи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-с-каз-</span><span class="hd-gloss">NÓI RA — '
    'chính là <b>сказа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span><span class="hd-gloss">đuôi nguyên '
    'thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">NÓI ra TRƯỚC khi việc xảy ra ⇒ tiên đoán; ráp y như <i>pre-dict</i> '
    '(Latin «nói trước»). Cặp CHT: <b>предска́зывать</b>.</div>'
    '<div class="hd-why">Chia y hệt <b>сказа́ть</b>: <i>з → ж</i> ở mọi ngôi, trọng âm chỉ ở đuôi '
    'tại ngôi «tôi» — <b>предскажу́</b>, nhưng <b>предска́жешь</b>, <b>предска́жут</b>.</div>'
    '<div class="hd-warn">Đoán trước cái gì: cách 4; cho ai: cách 3 — <b>предсказа́ть дру́гу '
    'бу́дущее</b> đoán tương lai cho bạn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>предсказа́ние</b> lời tiên đoán · <b>сказа́ть</b> nói · '
    '<b>рассказа́ть</b> kể lại</div>'
)

# --------------------------------------------------------------------- предсказывать
S["предсказывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пред-</span><span class="hd-gloss">TRƯỚC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-с-ка́з-</span><span class="hd-gloss">NÓI RA — '
    'như <b>сказа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть</span><span class="hd-gloss">hậu tố biến '
    'hoàn thành → CHƯA hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">NÓI TRƯỚC, đang hoặc nhiều lần ⇒ tiên đoán. Thêm <i>-ыва-</i> thì '
    'trọng âm nhảy về ngay trước nó, y như <b>рассказа́ть → расска́зывать</b>; chia đều, không '
    'biến âm: <b>предска́зываю</b>.</div>'
    '<div class="hd-warn"><b>предска́зывать судьбу́</b> bói vận mệnh · <b>предска́зывать '
    'пого́ду</b> đoán thời tiết.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>предсказа́ть</b> (HT) · <b>предсказа́тель</b> nhà tiên tri · '
    '<b>предсказу́емый</b> dễ đoán trước</div>'
)

# --------------------------------------------------------------------- предвидеть
S["предвидеть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пред-</span><span class="hd-gloss">TRƯỚC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ви́деть</span><span class="hd-gloss">THẤY — chính '
    'là <b>ви́деть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">THẤY TRƯỚC, ráp y như <i>fore-see</i> ⇒ lường trước. Chia như '
    '<b>ви́деть</b>, chỉ ngôi «tôi» đổi <i>д → ж</i>: <b>предви́жу</b>, nhưng '
    '<b>предви́дишь</b>, <b>предви́дят</b>. Không có bạn cặp hoàn thành.</div>'
    '<div class="hd-warn"><b>предсказа́ть</b> là NÓI ra điều sẽ tới; <b>предви́деть</b> chỉ là '
    'lường thấy trong đầu, không cần nói.</div>'
    '<div class="hd-warn"><b>непредви́денные обстоя́тельства</b> tình huống không lường '
    'trước — cụm hay gặp trong hợp đồng, giấy tờ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ви́деть</b> thấy · <b>предви́дение</b> sự thấy trước · '
    '<b>непредви́денный</b> ngoài dự liệu</div>'
)

# --------------------------------------------------------------------- присниться
S["присниться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span><span class="hd-gloss">ở đây chỉ làm '
    'thành thể hoàn thành, không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сн-</span><span class="hd-gloss">GIẤC MƠ — '
    '<b>сон</b>, <i>о</i> rụng như <b>сна</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть-ся</span><span class="hd-gloss">đuôi lớp chia '
    '2 + phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hiện ra trong giấc mơ của ai, xong một lần. Trọng âm luôn ở đuôi: '
    '<b>присню́сь</b>, <b>присни́тся</b>. Cặp CHT: <b>сни́ться</b>.</div>'
    '<div class="hd-warn">Người mơ ở cách 3, cái mơ thấy làm chủ ngữ: <b>Мне присни́лась '
    'шко́ла.</b> Tôi mơ thấy trường học (nghĩa đen: trường hiện ra cho tôi trong mơ).</div>'
    '<div class="hd-warn">Mơ thấy cả một chuyện: <b>Мне присни́лось, что…</b> — giống trung, '
    'không chủ ngữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сни́ться</b> (CHT) · <b>сон</b> giấc ngủ, giấc mơ · '
    '<b>бессо́нница</b> chứng mất ngủ</div>'
)

# --------------------------------------------------------------------- сниться
S["сниться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сн-</span><span class="hd-gloss">GIẤC MƠ — '
    '<b>сон</b>, <i>о</i> rụng như <b>сна</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть-ся</span><span class="hd-gloss">đuôi lớp chia '
    '2 + phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hiện ra trong giấc mơ. Tiếng Việt «TÔI mơ thấy MẸ», tiếng Nga lật lại: '
    'mẹ làm chủ ngữ, tôi xuống cách 3 — <b>Мне сни́тся ма́ма.</b> Động từ chia theo CÁI được mơ '
    'thấy: <b>мне сни́лся дом</b>, <b>мне сни́лись го́ры</b>.</div>'
    '<div class="hd-warn">Ba kiểu «mơ»: lúc ngủ là <b>мне сни́тся</b> hoặc <b>ви́деть во сне</b>; '
    'mơ ước lúc thức là <b>мечта́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>присни́ться</b> (HT) · <b>сон</b> giấc ngủ, giấc mơ · '
    '<b>спать</b> ngủ (cùng gốc xa, theo từ nguyên)</div>'
)

B = {
    "docbangmat": 110,
    "loitubat": 4,
    "nguonsai": 10,
    "baolen": [
        "V cần duyệt (11 thẻ): улучшение, имидж, увлекательный, одобрять, взятка, льгота, либеральный, коррупция, предсказывать, предвидеть, сниться — lý do từng dòng ghi cạnh V. 11 thẻ còn lại giữ đề cũ; 3 cặp thể nay cùng một dãy nghĩa.",
        "Va chạm: льгота rút «đặc quyền» nên hết chứa trọn привилегия (còn chung «ưu đãi»). взятка và коррупция nay không chung nghĩa nào. Máy chưa đo lại với V mới (không đụng Anki): chỗ đáng soi khi nạp là увлекательный ↔ привлекательный vì «lôi cuốn» là chữ mới.",
        "Đánh đổi: взятка bỏ nghĩa bài bạc (gloss có «trick in cards» nhưng hiếm, đề cũ «nước ăn trong đánh bài» khó hiểu); коррупция còn một nghĩa «tham nhũng». Muốn giữ nghĩa bài bạc thì user quyết.",
        "льгота: gloss CÓ «privilege», nên rút «đặc quyền» là chọn nghĩa thông dụng (ưu đãi, miễn giảm có tính xã hội), không phải nguồn sai.",
        "Câu ví dụ đã soạn (vi_du) của взятка dịch «khoản hối lộ», улучшение dịch «cải tiến», имидж dịch «hình ảnh»: không trái V mới, không cần sửa.",
        "Không chắc: (1) льгота cùng gốc лёгкий/польза/нельзя là từ nguyên, thẻ đã ghi «Mức tin»; (2) о- trong одобрить «COI LÀ» là cách hiểu theo nghĩa, о- + tính từ thường là «làm cho thành»; (3) предвыборный: thẻ nói dạng ngắn trong bảng thực tế không dùng.",
        "Nguồn sai đã bác (10): dạng ngắn предвыборен; CACH DUNG của взятка (câu trích không chứa từ này); «say mê» ở увлекательный; «sự hối lộ» ở коррупция và взятка (tính 2); «đồng ý» ở одобрять; «báo trước» ở предсказывать; «dễ dãi» ở либеральный; «uy tín» ở имидж; «sự tiến bộ» ở улучшение.",
        "Lỗi tự bắt (4): квадрат thiếu «bốn góc vuông» (thành hình thoi); взятка chẻ «cái đã bị lấy»; охотно có câu đáp «Охотно!» không chắc tự nhiên (đã bỏ); предвидеть nói «cụm có trong mọi hợp đồng» (nói quá).",
    ],
}
