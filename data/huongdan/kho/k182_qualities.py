# -*- coding: utf-8 -*-
"""k182 — qualities (lô trộn): tính chất, ưu/nhược điểm, khó/dễ chịu.

Chỗ cần nhất quán trong lô:
(1) Họ -сто-/-ста-: досто́йный / досто́инство là gốc -сто́й- của сто́ить «ĐÁNG (giá)»;
    недоста́ток là gốc -ста- của доста́ть / доста́точно «ĐỦ». Trái nghĩa nhau
    (досто́инства и недоста́тки) nhưng KHÁC gốc — mỗi thẻ nói một câu.
(2) Ba danh từ -ость (жи́дкость, тру́дность, то́чность): mỗi thẻ một câu «tính từ + -ость»,
    không bảng. Báo oan кость / восто́чный.
(3) Năm từ ghép не-/бес- (неудо́бный, несправедли́вый, неприя́тный, недоста́ток, беспоря́док):
    chẻ ra «не- + từ đã có thẻ», dẫn chiếu thẻ gốc.
(4) пахнуть = «có mùi» (đồng tự пахну́ть «thổi phù» cố ý không nhắc).
Họ hàng cố ý vắng: không thẻ nào — блок là từ mượn nhưng có блокно́т / блоки́ровать.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "блок": "khối, liên minh, cụm, mô-đun",          # bỏ «liên kết» (không phải nghĩa); unit/module/assembly
    "заключаться": "nằm ở, cốt ở, là, được ký kết",  # «bao gồm ở» gượng; to consist/lie in, to be concluded/signed
}

# ------------------------------------------------------------ характеристика
S["характеристика"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">характер-</span>'
    '<span class="hd-gloss">TÍNH CÁCH, bản chất — <b>хара́ктер</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-истика</span>'
    '<span class="hd-gloss">→ danh từ giống cái (như <i>-istic</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng tiếng Anh <i>characteristic</i>: cái nói lên bản chất của một thứ ⇒ '
    '<b>đặc điểm, đặc tính</b>. Viết về bản chất của một con người ⇒ <b>bản nhận xét</b>. '
    'Trọng âm dời: <b>хара́ктер → характери́стика</b>.</div>'
    '<div class="hd-warn"><b>характери́стика с ме́ста рабо́ты</b> — bản nhận xét của nơi làm việc '
    '(giấy kèm hồ sơ), nghĩa người Nga dùng rất thường.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>хара́ктер</b> tính cách · <b>характе́рный</b> đặc trưng · '
    '<b>характеризова́ть</b> mô tả đặc điểm</div>'
)

# ------------------------------------------------------------------ жёсткий
S["жёсткий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">жёст-</span>'
    '<span class="hd-gloss">CỨNG, rắn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-кий</span>'
    '<span class="hd-gloss">→ tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cứng theo kiểu <b>không chịu uốn</b>: thịt dai, giường cứng, rồi sang người — '
    'luật <b>khắt khe</b>, giọng gay gắt. Đối lập với <b>мя́гкий</b> mềm. '
    'Dạng ngắn giống cái <b>жестка́</b>: trọng âm nhảy ra đuôi nên <b>ё</b> thành <b>е</b>.</div>'
    '<div class="hd-warn"><b>жёсткий диск</b> — ổ cứng (máy tính).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жесто́кий</b> tàn nhẫn · <b>жесть</b> tôn, sắt tây</div>'
)

# ---------------------------------------------------------------- неудобный
S["неудобный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не-</span>'
    '<span class="hd-gloss">KHÔNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">удо́бный</span>'
    '<span class="hd-gloss">thoải mái, tiện — thẻ đã học</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lật nghĩa <b>удо́бный</b>: ghế không thoải mái, giờ giấc bất tiện. '
    'Dạng ngắn giống đực chen thêm <b>е</b>: <b>неудо́бен</b>.</div>'
    '<div class="hd-warn"><b>Мне неудо́бно</b> — thường là «tôi ngại, tôi thấy khó xử», '
    'không phải ghế cứng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>удо́бный</b> tiện lợi · <b>удо́бно</b> tiện · '
    '<b>удо́бство</b> sự tiện nghi</div>'
)

# ------------------------------------------------------------- традиционный
S["традиционный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">традици-</span>'
    '<span class="hd-gloss">TRUYỀN THỐNG — <b>тради́ция</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-онный</span>'
    '<span class="hd-gloss">→ tính từ (danh từ <i>-ция</i> → <i>-ционный</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiếng Anh <i>tradition → traditional</i>, tiếng Nga cũng thế: '
    '<b>-ция → -ционный</b>. Trọng âm dời về <b>-о́н-</b>. Dạng ngắn giống đực '
    '<b>традицио́нен</b> (-нн- → -нен).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тради́ция</b> truyền thống · <b>традицио́нно</b> theo truyền thống</div>'
)

# ------------------------------------------------------------------- мощный
S["мощный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мощ-</span>'
    '<span class="hd-gloss">SỨC MẠNH — <b>мощь</b>, gốc của <b>мочь</b> «có thể»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ный</span>'
    '<span class="hd-gloss">→ tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>мог-</b> của <b>мочь / могу́</b> sang danh từ thành <b>мощ-</b> — '
    'đúng như <b>помо́чь → по́мощь</b>. «Có khả năng làm được nhiều» ⇒ mạnh, hùng mạnh. '
    'Dạng ngắn giống cái trọng âm ra đuôi: <b>мощна́</b>.</div>'
    '<div class="hd-warn"><b>мо́щный</b> hợp với máy móc, sức đẩy, quy mô: <b>мо́щный дви́гатель</b> '
    'động cơ mạnh. Người khoẻ thì <b>си́льный</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мощь</b> sức mạnh · <b>мо́щность</b> công suất · '
    '<b>мочь</b> có thể · <b>по́мощь</b> sự giúp đỡ</div>'
)

# ------------------------------------------------------------- материальный
S["материальный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">матери-</span>'
    '<span class="hd-gloss">VẬT CHẤT — <b>мате́рия</b>, <b>материа́л</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-альный</span>'
    '<span class="hd-gloss">→ tính từ (như <i>-al</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng tiếng Anh <i>material</i>: thuộc về vật chất, sờ được — rồi hẹp lại '
    'thành «về tiền bạc»: <b>материа́льная по́мощь</b> hỗ trợ tài chính. '
    'Trọng âm: <b>материа́льный</b>.</div>'
    '<div class="hd-warn"><b>материа́льный мир</b> thế giới vật chất ↔ <b>духо́вный</b> tinh thần — '
    'cặp đối hay đi cùng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>материа́л</b> vật liệu · <b>мате́рия</b> vật chất, vải</div>'
)

# --------------------------------------------------------------- беспорядок
S["беспорядок"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бес-</span>'
    '<span class="hd-gloss">KHÔNG CÓ — <b>без</b>, đổi <b>з→с</b> trước <b>п</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">поря́док</span>'
    '<span class="hd-gloss">trật tự — thẻ đã học</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Không có trật tự» ⇒ bừa bộn, hỗn loạn. Nguyên âm <b>о</b> chạy như ở '
    '<b>поря́док</b>: <b>беспоря́дка</b>. <b>бес-</b> như trong <b>беспла́тный</b>.</div>'
    '<div class="hd-warn">Số nhiều <b>беспоря́дки</b> = <b>bạo loạn</b> (<b>ма́ссовые беспоря́дки</b>), '
    'không phải «nhiều chỗ bừa».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поря́док</b> trật tự · <b>в поря́дке</b> ổn cả</div>'
)

# --------------------------------------------------------------------- блок
S["блок"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn nguyên <i>bloc / block</i> của Pháp, Anh. '
    'Chữ <b>блок</b> nằm lọt trong <b>я́блоко</b> chỉ là trùng mặt chữ.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mang đủ hai nghĩa của <i>bloc</i>: một <b>khối</b> liền (khối nhà, cụm máy) '
    'và một <b>liên minh</b> nhiều nước gắn thành khối (<i>NATO bloc</i>).</div>'
    '<div class="hd-warn"><b>блок пита́ния</b> — bộ nguồn (máy tính, thiết bị điện).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>блокно́т</b> sổ tay (xấp giấy đóng khối) · '
    '<b>блоки́ровать</b> chặn, phong toả</div>'
)

# ---------------------------------------------------------------- жидкость
S["жидкость"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">жидк-</span>'
    '<span class="hd-gloss">LỎNG — <b>жи́дкий</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span>'
    '<span class="hd-gloss">→ danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái lỏng» ⇒ <b>chất lỏng</b>. Cắt đúng chỗ là <b>жидк|ость</b> — '
    'chữ <b>кость</b> «xương» ở đuôi chỉ là trùng mặt chữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жи́дкий</b> lỏng, loãng</div>'
)

# ---------------------------------------------------------------- трудность
S["трудность"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">трудн-</span>'
    '<span class="hd-gloss">KHÓ — <b>тру́дный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span>'
    '<span class="hd-gloss">→ danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>тру́дный + -ость</b> = «cái khó». Gốc <b>труд</b> là lao động vất vả — '
    'việc tốn sức ⇒ khó. Hay dùng số nhiều: <b>тру́дности</b> những khó khăn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>труд</b> lao động · <b>тру́дный</b> khó · <b>тру́дно</b> khó · '
    '<b>сотру́дничество</b> sự hợp tác</div>'
)

# ----------------------------------------------------------------- точность
S["точность"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">точн-</span>'
    '<span class="hd-gloss">CHÍNH XÁC — <b>то́чный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span>'
    '<span class="hd-gloss">→ danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>то́чный + -ость</b> = «độ chính xác». Mang theo cả nghĩa «đúng giờ» '
    'của <b>то́чный</b>. Đừng cắt nhầm theo <b>восто́чный</b> — từ đó là <b>восто́к</b> + <b>-чный</b>.</div>'
    '<div class="hd-warn"><b>в то́чности</b> — y hệt, đúng từng li.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>то́чный</b> chính xác · <b>то́чно</b> chính xác, đúng thế · '
    '<b>то́чка</b> dấu chấm, điểm</div>'
)

# ------------------------------------------------------------------ пахнуть
S["пахнуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пах-</span>'
    '<span class="hd-gloss">MÙI — như <b>за́пах</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-нуть</span>'
    '<span class="hd-gloss">đuôi động từ, ở đây KHÔNG mang nghĩa «một lần»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thứ có <b>за́пах</b> thì <b>па́хнет</b>. Chia như <b>привы́кнуть</b>: '
    'quá khứ rụng <b>-ну-</b> — <b>пах</b>, <b>па́хла</b>.</div>'
    '<div class="hd-warn">Mùi GÌ đi cách 5: <b>па́хнет хле́бом</b> — có mùi bánh mì. '
    'Nghĩa bóng: <b>па́хнет войно́й</b> — có mùi chiến tranh.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>за́пах</b> mùi</div>'
)

# -------------------------------------------------------------- заключаться
S["заключаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">KHÉP LẠI, đóng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ключ-</span>'
    '<span class="hd-gloss">CHÌA KHOÁ — <b>ключ</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ться</span>'
    '<span class="hd-gloss">động từ phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Khoá chặt bên trong ⇒ cái cốt lõi <b>nằm gói trong</b> đó. '
    'Bản không <b>-ся</b> <b>заключа́ть</b> là ký kết (khoá hợp đồng lại) — nên <b>-ся</b> còn nghĩa «được ký kết».</div>'
    '<div class="hd-warn"><b>Пробле́ма заключа́ется в том, что…</b> — vấn đề nằm ở chỗ… '
    '(<b>в</b> + cách 6).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>заключе́ние</b> kết luận, sự ký kết · <b>ключ</b> chìa khoá</div>'
)

# ------------------------------------------------------------- перспектива
S["перспектива"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga: mượn Latin <i>perspectiva</i> '
    '(<i>per-</i> xuyên qua + <i>spect-</i> nhìn) — nhìn xuyên ra xa.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhìn ra xa phía trước ⇒ <b>viễn cảnh, triển vọng</b>; trong hội hoạ là '
    '<b>phối cảnh</b>. Số nhiều <b>перспекти́вы</b> = những triển vọng.</div>'
    '<div class="hd-warn">KHÔNG phải «góc nhìn, quan điểm» như <i>perspective</i> tiếng Anh — '
    'cái đó là <b>то́чка зре́ния</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>перспекти́вный</b> có triển vọng</div>'
)

# ------------------------------------------------------------------ всерьёз
S["всерьёз"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">giới từ dính liền → trạng từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-серьёз</span>'
    '<span class="hd-gloss">NGHIÊM TÚC — thân của <b>серьёзный</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Vào thế nghiêm túc» ⇒ không đùa. Khác <b>серьёзно</b> ở chỗ chỉ có '
    'nghĩa «thật lòng, không đùa», không có nghĩa «nghiêm trọng».</div>'
    '<div class="hd-warn"><b>принима́ть всерьёз</b> — coi là thật, để tâm · '
    '<b>Ты э́то всерьёз?</b> — Cậu nói thật đấy à?</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>серьёзный</b> nghiêm túc · <b>серьёзно</b> nghiêm túc, nghiêm trọng</div>'
)

# ----------------------------------------------------------- несправедливый
S["несправедливый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не-</span>'
    '<span class="hd-gloss">KHÔNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">справедли́вый</span>'
    '<span class="hd-gloss">công bằng — thẻ đã học, gốc <b>-прав-</b> ĐÚNG</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lật nghĩa <b>справедли́вый</b>. Gốc <b>-прав-</b> như <b>пра́вда</b>, '
    '<b>пра́вый</b>: không theo lẽ phải ⇒ bất công.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>справедли́вый</b> công bằng · <b>справедли́вость</b> công lý · '
    '<b>несправедли́вость</b> sự bất công · <b>пра́вда</b> sự thật</div>'
)

# ---------------------------------------------------------------- достойный
S["достойный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI, đạt tới</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сто́й-</span>'
    '<span class="hd-gloss">ĐÁNG — như <b>сто́ить</b> «đáng giá»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ный</span>'
    '<span class="hd-gloss">→ tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đạt tới mức đáng» ⇒ xứng đáng, đáng kính. Dạng ngắn giống đực lệch '
    'mặt chữ: <b>досто́ин</b> (không phải «достоен») — chính nó nằm trong <b>досто́инство</b>.</div>'
    '<div class="hd-warn">Xứng đáng CÁI GÌ đi cách 2: <b>досто́ин уваже́ния</b> — đáng được tôn trọng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>досто́инство</b> phẩm giá, ưu điểm · <b>сто́ить</b> đáng giá</div>'
)

# --------------------------------------------------------------- неприятный
S["неприятный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не-</span>'
    '<span class="hd-gloss">KHÔNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">прия́тный</span>'
    '<span class="hd-gloss">dễ chịu — thẻ đã học</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lật nghĩa <b>прия́тный</b>: người, mùi, chuyện khiến mình khó chịu. '
    'Dạng ngắn chen <b>е</b>: <b>неприя́тен</b>. Thành danh từ: <b>неприя́тность</b> chuyện rắc rối.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прия́тный</b> dễ chịu · <b>прия́тно</b> dễ chịu · '
    '<b>неприя́тность</b> chuyện không hay · <b>прия́тель</b> bạn bè</div>'
)

# --------------------------------------------------------------- недостаток
S["недостаток"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не-</span>'
    '<span class="hd-gloss">KHÔNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">доста́-</span>'
    '<span class="hd-gloss">ĐỦ, với tới — <b>доста́ть</b>, <b>доста́точно</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ток</span>'
    '<span class="hd-gloss">→ danh từ giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Không đủ» ⇒ <b>sự thiếu</b>; chỗ con người/đồ vật không đủ ⇒ '
    '<b>khuyết điểm</b>. Nguyên âm <b>о</b> chạy: <b>недоста́тка</b>. Thiếu CÁI GÌ đi cách 2: '
    '<b>недоста́ток вре́мени</b> thiếu thời gian.</div>'
    '<div class="hd-warn">Trái nghĩa <b>досто́инство</b> (ưu điểm) nhưng KHÁC gốc: '
    '<b>-ста-</b> «đủ» ≠ <b>-сто́й-</b> «đáng».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>доста́точно</b> đủ · <b>доста́ть</b> lấy được, với tới</div>'
)

# ------------------------------------------------------------- преимущество
S["преимущество"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пре-</span>'
    '<span class="hd-gloss">VƯỢT HƠN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-иму́щ-</span>'
    '<span class="hd-gloss">CÓ — gốc của <b>име́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ество</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Có nhiều hơn người khác» ⇒ <b>ưu thế, lợi thế</b>. Bỏ <b>пре-</b> là '
    '<b>иму́щество</b> «cái mình có» = tài sản.</div>'
    '<div class="hd-warn">Hơn AI đi <b>пе́ред</b> + cách 5: <b>преиму́щество пе́ред конкуре́нтами</b> — '
    'lợi thế so với đối thủ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>име́ть</b> có · <b>иму́щество</b> tài sản · '
    '<b>преиму́щественно</b> chủ yếu</div>'
)

# ------------------------------------------------------------- достоинство
S["достоинство"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">досто́ин-</span>'
    '<span class="hd-gloss">XỨNG ĐÁNG — dạng ngắn của <b>досто́йный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ство</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái làm người ta xứng đáng»: ở con người là <b>phẩm giá, lòng tự trọng</b>; '
    'ở đồ vật, phương án là <b>ưu điểm</b>.</div>'
    '<div class="hd-warn"><b>досто́инства и недоста́тки</b> — ưu và nhược điểm. '
    'Hai từ KHÁC gốc, xem thẻ <b>недоста́ток</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>досто́йный</b> xứng đáng · <b>сто́ить</b> đáng giá</div>'
)

B = {
    "docbangmat": 67,
    "loitubat": 2,
    "nguonsai": 1,
    "baolen": [
        "Va chạm nghĩa: không có (máy báo 0; tự soát thêm cũng không thấy cặp trùng HẾT nghĩa mà badge không tách).",
        "Nguồn sai bác: BAT THUONG của жёсткий in dạng ngắn giống đực «жесто́к» — đó là dạng ngắn của жесто́кий (tàn nhẫn); của жёсткий là жёсток. Thẻ chỉ nêu жестка́ (ё→е khi trọng âm ra đuôi), không chép dạng sai.",
        "Dữ liệu thiếu (không bác, chỉ báo): dòng tiep của материальный không có dấu trọng âm ở cột dạng nhấn; đã viết материа́льный theo bảng dạng ngắn.",
        "Lỗi tự bắt (loitubat=2): thẻ блок viết «giống đuôi я́блоко» (блок nằm GIỮA từ, không ở đuôi) → sửa; thẻ заключаться viết «bản không -ся là ký kết» (заключа́ть còn nghĩa kết luận, giam) → sửa thành «заключа́ть là ký kết (khoá hợp đồng)», hẹp vào đúng nghĩa cần dẫn.",
        "Không chắc (mức tin vừa, chưa đối chiếu nguồn): то́чный cùng gốc то́чка; прия́тель cùng gốc прия́тный (cùng từ приять); досто́йный cùng họ với сто́ить. Cả ba viết như liên hệ nhớ, không gắn ô Mức tin.",
        "V cần duyệt (2 thẻ): блок «khối, liên minh, liên kết» → «khối, liên minh, cụm, mô-đun» (bỏ «liên kết» — không phải nghĩa; cố ý bỏ «ròng rọc» vì chuyên ngành); заключаться «nằm ở, bao gồm ở, là» → «nằm ở, cốt ở, là, được ký kết» (thêm nghĩa to be concluded/signed). 19 thẻ còn lại đề cũ đã đúng, không viết V.",
    ],
}
