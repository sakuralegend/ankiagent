# -*- coding: utf-8 -*-
"""k14 — tu-moi: 18 từ user vừa thêm, trục ĐI MUA SẮM.

Một cảnh thật: vào siêu thị / ki-ốt → cân đong (gam, cái, gói, chai) →
xem giá và độ tươi → trả tiền ở quầy → cầm hóa đơn và tiền thừa.
KHÔNG có khối hệ thống dùng chung (README §3): mỗi thẻ chỉ nói kiến thức
dính TRỰC TIẾP vào chính từ đó.
"""

S = {}
V = {}

# ─────────────────────────────────────────────────────────── апельсин
S["апельсин"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">апель-</span>'
    '<span class="hd-gloss">quả TÁO (Hà Lan <i>appel</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-син</span>'
    '<span class="hd-gloss">TRUNG HOA (<i>Sina</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn nguyên khối tiếng Hà Lan <i>appelsien</i> = "táo Trung Hoa" — '
    'thời buôn tàu, cam được chở từ Trung Quốc sang châu Âu. Tiếng Đức <i>Apfelsine</i> '
    'cùng một chữ.</div>'
    '<div class="hd-warn">MÀU cam là <b>ора́нжевый</b> — từ khác hẳn, mượn thẳng tiếng Pháp '
    '<i>orange</i>. Còn <b>апельси́новый</b> chỉ có nghĩa "làm từ quả cam".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>апельси́новый</b> làm từ cam — nước cam là '
    '<b>апельси́новый сок</b></div>'
)
V["апельсин"] = "quả cam"

# ─────────────────────────────────────────────────────────── бутылка
S["бутылка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">буты́л-</span>'
    '<span class="hd-gloss">gốc mượn: CHAI, BÌNH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">đuôi làm danh từ chỉ VẬT, luôn giống CÁI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ tiếng Pháp <i>bouteille</i> vào Nga qua tiếng Ba Lan — cùng ổ '
    'với tiếng Anh <i>bottle</i>, đều từ La Tinh <i>butticula</i> "thùng nhỏ".</div>'
    '<div class="hd-warn">Đếm chai: <b>две буты́лки</b> · <b>пять буты́лок</b> — mất đuôi '
    '-а thì cụm <b>лк</b> đứng cuối khó đọc, nên chèn thêm -о-.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>буты́ль</b> bình lớn · <b>буты́лочка</b> chai con</div>'
)
V["бутылка"] = "cái chai"

# ─────────────────────────────────────────────────────────── грамм
S["грамм"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn nguyên khối tiếng Pháp <i>gramme</i>, '
    'gốc Hy Lạp <i>gramma</i> — vốn là tên một đơn vị cân rất nhỏ.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhận mặt ngay qua tiếng Anh <i>gram</i>. Kết thúc bằng phụ âm nên '
    'là giống ĐỰC, biến cách như mọi danh từ đực đuôi cứng.</div>'
    '<div class="hd-warn">Ở quầy hàng người Nga nói dạng TRỤI ĐUÔI: '
    '<b>две́сти грамм сы́ра</b> (200 g phô mai). Văn viết chuẩn mới là <b>гра́ммов</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>килогра́мм</b> ki-lô-gam · <b>кило́</b> ki-lô (khẩu ngữ, '
    'không biến cách)</div>'
)

# ─────────────────────────────────────────────────────────── касса
S["касса"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn tiếng Ý <i>cassa</i> "cái két, cái hộp", '
    'gốc La Tinh <i>capsa</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng ổ với tiếng Anh <i>case</i>, <i>cash</i>, <i>cashier</i> — '
    'tất cả xuất phát từ cái HỘP đựng tiền. Ở siêu thị là quầy tính tiền, ở rạp hay nhà ga '
    'là quầy bán vé.</div>'
    '<div class="hd-warn">Câu nghe hằng ngày: <b>Пройди́те на ка́ссу</b> '
    '(mời anh/chị ra quầy thanh toán).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>касси́р</b> nhân viên thu ngân · <b>ка́ссовый чек</b> biên lai '
    'máy tính tiền in ra</div>'
)
V['касса'] = 'quầy thu ngân, quầy vé, két tiền'

# ─────────────────────────────────────────────────────────── киоск
S["киоск"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn tiếng Pháp <i>kiosque</i>, gốc Thổ '
    '<i>köşk</i> "chòi, nhà mát trong vườn".</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng một từ với tiếng Anh <i>kiosk</i>. Là cái sạp nhỏ ngoài phố '
    'mua bán qua ô cửa sổ (báo, thuốc lá, hoa) — khác <b>магази́н</b> là cửa hàng bước hẳn '
    'được vào trong.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>киоскёр</b> người bán ở ki-ốt — đuôi <b>-ёр</b> chỉ NGƯỜI LÀM '
    'NGHỀ, như <b>шофёр</b>, <b>актёр</b></div>'
)
V["киоск"] = "ki-ốt, sạp bán hàng nhỏ ngoài phố"

# ─────────────────────────────────────────────────────────── купить
S["купить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">куп-</span>'
    '<span class="hd-gloss">gốc MUA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc trần, không tiền tố — và đây là thể HOÀN THÀNH: mua xong, '
    'một lần, có kết quả. Bạn đồng hành chưa hoàn thành là <b>покупа́ть</b> (cùng lô này).</div>'
    '<div class="hd-warn">Riêng ngôi "tôi" chèn thêm <b>л</b>: <b>куплю́</b> — luật chung cho '
    'mọi thân kết thúc bằng <b>б в м п ф</b> (<b>люблю́</b>, <b>гото́влю</b>). Các ngôi khác '
    'không có: <b>ку́пишь</b>.</div>'
    '<div class="hd-warn">Mua CHO ai thì người nhận đi cách 3: '
    '<b>Купи́ мне ко́фе</b> (mua cho tôi cà phê nhé).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>покупа́ть</b> mua (chưa hoàn thành) · <b>поку́пка</b> món đồ đã '
    'mua · <b>покупа́тель</b> khách mua</div>'
)
V['купить'] = 'mua, sắm'

# ─────────────────────────────────────────────────────────── недорогой
S["недорогой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не-</span>'
    '<span class="hd-gloss">KHÔNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дорог-</span>'
    '<span class="hd-gloss">gốc ĐẮT, QUÝ GIÁ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ, luôn có trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng nghĩa đen "không đắt". Cùng gốc <b>дорого́й</b> — từ đó còn '
    'nghĩa "thân yêu" (<b>Дорого́й друг</b>), vì cái gì quý giá thì mới đắt.</div>'
    '<div class="hd-warn"><b>недорого́й</b> ≠ <b>дешёвый</b>: từ này khen giá phải chăng, '
    'còn <b>дешёвый</b> hay kèm ý rẻ tiền, kém chất lượng.</div>'
    '<div class="hd-warn">Dạng ngắn dồn trọng âm về gốc — câu nói khi xem giá: '
    '<b>Э́то недо́рого</b> (cái này không đắt đâu).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дорого́й</b> đắt; thân mến · <b>до́рого</b> đắt (trạng từ) · '
    '<b>дорожа́ть</b> lên giá</div>'
)
V['недорогой'] = 'không đắt, phải chăng'

# ─────────────────────────────────────────────────────────── овощ
S["овощ"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: gốc Slav cổ, không tiền tố cũng không hậu tố.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gần như luôn dùng ở số nhiều <b>о́вощи</b> cho "rau củ" nói chung; '
    'số ít chỉ dùng khi bàn từng loại một. Cặp đối của nó ngay trong lô này là '
    '<b>фрукт</b>.</div>'
    '<div class="hd-warn">Số nhiều các cách gián tiếp dồn trọng âm ra đuôi: '
    '<b>сала́т из овоще́й</b> (salad rau củ) — nhớ <b>овоще́й</b> là nắm được cả bảng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>овощно́й</b> thuộc rau củ — <b>овощно́й магази́н</b> cửa hàng '
    'rau quả</div>'
)
V['овощ'] = 'rau, rau củ'

# ─────────────────────────────────────────────────────────── пачка
S["пачка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пач-</span>'
    '<span class="hd-gloss">gốc mượn: BÓ, GÓI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">đuôi danh từ chỉ VẬT, giống CÁI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ tiếng Đức <i>Pack</i> qua tiếng Ba Lan <i>paczka</i>, cùng ổ với '
    'tiếng Anh <i>pack</i>. Là gói CỨNG và DẸT: <b>па́чка сигаре́т</b>, <b>па́чка ма́сла</b>. '
    'Đếm: <b>пять па́чек</b> (mất đuôi thì chèn -е-).</div>'
    '<div class="hd-warn">Ba kiểu bao bì đừng lẫn: <b>па́чка</b> gói cứng dẹt · '
    '<b>паке́т</b> túi (ni-lông, giấy) · <b>коро́бка</b> hộp.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>паке́т</b> túi, gói · <b>упако́вка</b> bao bì · '
    '<b>упакова́ть</b> đóng gói</div>'
)
V['пачка'] = 'gói, xấp, bó'

# ─────────────────────────────────────────────────────────── показать
S["показать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể, ở đây KHÔNG mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-каз-</span>'
    '<span class="hd-gloss">gốc CHỈ RA, LÀM CHO THẤY</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nắm gốc <b>каз-</b> là mở được cả một họ: nói RA, kể RA, tỏ RA — '
    'xem mục dưới.</div>'
    '<div class="hd-warn">Đòi HAI cách một lúc: cho AI (cách 3) xem CÁI GÌ (cách 4) — '
    '<b>Покажи́те мне э́ту су́мку</b> (cho tôi xem cái túi này).</div>'
    '<div class="hd-warn">Thân hiện tại đổi <b>з → ж</b>: <b>покажу́</b>, <b>пока́жешь</b> — '
    'đúng luật của <b>сказа́ть → скажу́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пока́зывать</b> cho xem (chưa hoàn thành) · <b>сказа́ть</b> nói ra · '
    '<b>рассказа́ть</b> kể · <b>каза́ться</b> có vẻ</div>'
)
V['показать'] = 'cho xem, chìa ra, chỉ ra'

# ─────────────────────────────────────────────────────────── покупать
S["покупать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố, không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-куп-</span>'
    '<span class="hd-gloss">gốc MUA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi kéo dài / lặp lại → thể CHƯA HOÀN THÀNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Việc mua đang diễn ra, thường xuyên, hoặc nói chung: '
    '<b>Я покупа́ю хлеб ка́ждый день</b>. Xong việc một lần thì dùng <b>купи́ть</b>.</div>'
    '<div class="hd-warn">Cặp này NGƯỢC linh cảm quen thuộc: thường có tiền tố là hoàn thành, '
    'nhưng ở đây <b>купи́ть</b> (trần) mới hoàn thành, còn <b>покупа́ть</b> (có по-) lại chưa '
    'hoàn thành. Cái quyết định là đuôi <b>-а́ть</b>, không phải tiền tố.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>купи́ть</b> mua (hoàn thành) · <b>поку́пка</b> món đồ đã mua · '
    '<b>де́лать поку́пки</b> đi mua sắm · <b>покупа́тель</b> khách mua</div>'
)
V['покупать'] = 'mua, sắm'

# ─────────────────────────────────────────────────────────── размер
S["размер"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span>'
    '<span class="hd-gloss">tiền tố: RA, TRẢI RỘNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ме́р</span>'
    '<span class="hd-gloss">gốc ĐO (không thêm đuôi nào)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái "đo trải ra được" — cùng gốc với <b>ме́ра</b> (mức, thước đo) và '
    '<b>ме́рить</b> (đo). Ở cửa hàng quần áo giày dép thì <b>разме́р</b> chính là CỠ.</div>'
    '<div class="hd-warn">Câu ở tiệm: <b>Како́й у вас разме́р?</b> (anh/chị mặc cỡ nào?). '
    'Muốn mặc thử là <b>примеря́ть</b>, phòng thử đồ là <b>приме́рочная</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ме́ра</b> mức, thước đo · <b>ме́рить</b> đo · '
    '<b>примеря́ть</b> mặc thử · <b>изме́рить</b> đo đạc</div>'
)
V['размер'] = 'cỡ, kích thước, kích cỡ'

# ─────────────────────────────────────────────────────────── свежий
S["свежий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">свеж-</span>'
    '<span class="hd-gloss">gốc TƯƠI, MÁT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc kết thúc bằng <b>ж</b> nên đuôi buộc phải viết И chứ không viết '
    'Ы — luật ЖИ ШИ: <b>све́жие о́вощи</b>.</div>'
    '<div class="hd-warn">Rộng hơn chữ "tươi" nhiều: <b>све́жий хлеб</b> bánh mới ra lò · '
    '<b>све́жая газе́та</b> báo số mới nhất · <b>све́жий во́здух</b> không khí trong lành. '
    'Ý chung là CHƯA CŨ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>све́жесть</b> sự tươi mát · <b>свежо́</b> mát mẻ (trạng từ) · '
    '<b>освежи́ть</b> làm tươi mát lại</div>'
)
V['свежий'] = 'tươi, mới'

# ─────────────────────────────────────────────────────────── сдача
S["сдача"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">tiền tố: trao RA, giao XUỐNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-да-</span>'
    '<span class="hd-gloss">gốc CHO, ĐƯA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ча</span>'
    '<span class="hd-gloss">đuôi danh từ giống CÁI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái người bán ĐƯA TRẢ lại cho mình — danh từ của động từ '
    '<b>сдать</b> (giao lại, nộp lại).</div>'
    '<div class="hd-warn">Câu ở quầy: <b>Сда́чи не на́до</b> (khỏi thối lại ạ). Sau '
    '<b>не на́до</b> danh từ phải sang cách 2, nên là <b>сда́чи</b> chứ không phải '
    '<b>сда́ча</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дать</b> cho · <b>сдать</b> giao nộp; thi đỗ · '
    '<b>прода́ть</b> bán · <b>продаве́ц</b> người bán hàng · <b>отда́ть</b> trả lại</div>'
)
V['сдача'] = 'tiền thừa trả lại, sự đầu hàng, sự nộp lại'

# ─────────────────────────────────────────────────────────── супермаркет
S["супермаркет"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">супер-</span>'
    '<span class="hd-gloss">SIÊU, trên mức thường</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ма́ркет</span>'
    '<span class="hd-gloss">CHỢ, cửa hàng (mượn tiếng Anh <i>market</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bê nguyên khối tiếng Anh <i>supermarket</i>, chỉ đổi chỗ nhấn: '
    'tiếng Nga nhấn vào giữa <b>суперма́ркет</b>. Nhỏ hơn thì gọi là <b>магази́н</b>, '
    'chợ ngoài trời là <b>ры́нок</b> — hai từ đó không cùng gốc với từ này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гипермарке́т</b> đại siêu thị · tiền tố <b>супер-</b> còn nằm '
    'trong <b>суперзвезда́</b> siêu sao</div>'
)

# ─────────────────────────────────────────────────────────── фрукт
S["фрукт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn từ La Tinh <i>fructus</i> "hoa lợi, quả", '
    'vào tiếng Nga qua tiếng Ba Lan.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng một từ với tiếng Anh <i>fruit</i> và <i>fructose</i>. Cặp đối '
    'của nó ngay trong lô này là <b>о́вощ</b> (rau củ).</div>'
    '<div class="hd-warn">Nói "hoa quả" nói chung thì luôn dùng số nhiều <b>фру́кты</b>; '
    'số ít <b>фрукт</b> là một quả cụ thể. Ở chợ: <b>Я люблю́ фру́кты</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>фрукто́вый</b> làm từ trái cây — <b>фрукто́вый сок</b> nước ép '
    'trái cây</div>'
)
V['фрукт'] = 'trái cây, hoa quả'

# ─────────────────────────────────────────────────────────── чек
S["чек"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn thẳng tiếng Anh <i>check / cheque</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tờ giấy máy tính tiền in ra SAU KHI đã trả — nói đầy đủ là '
    '<b>ка́ссовый чек</b>, tức tờ giấy của cái <b>ка́сса</b> (cùng lô). Giữ nó lại thì mới '
    'đổi hay trả hàng được.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>счёт</b>: <b>чек</b> là biên lai ĐÃ trả (siêu thị) '
    '· <b>счёт</b> là hóa đơn CẦN trả (nhà hàng). Hai từ khác gốc hẳn nhau.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>че́ковый</b> thuộc về séc — <b>че́ковая кни́жка</b> quyển séc '
    '(đúng tiếng Anh <i>checkbook</i>)</div>'
)
V["чек"] = "biên lai, phiếu tính tiền"

# ─────────────────────────────────────────────────────────── штука
S["штука"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">штук-</span>'
    '<span class="hd-gloss">gốc mượn: MIẾNG, MÓN RỜI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi danh từ giống CÁI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ tiếng Đức <i>Stück</i> "mảnh, miếng" qua tiếng Ba Lan. Là đơn vị '
    'đếm vật rời — đúng chỗ tiếng Việt nói "cái, chiếc". Ngoài chợ còn dùng để gọi tên món đồ '
    'mà mình quên mất tên thật.</div>'
    '<div class="hd-warn">Đếm sau số: <b>одна́ шту́ка</b> · <b>две шту́ки</b> (2–4) · '
    '<b>пять штук</b> (từ 5 trở lên, dạng trụi đuôi).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>шту́чный</b> tính theo từng cái — <b>шту́чный това́р</b> hàng '
    'bán lẻ từng cái</div>'
)
V['штука'] = 'cái, chiếc, thứ, món'
