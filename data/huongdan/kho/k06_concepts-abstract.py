# -*- coding: utf-8 -*-
"""k06 — concepts::abstract: 4 từ (2 động từ lịch sự + 2 danh từ giống cái đuôi -ь).

Soạn lại từ đầu theo chuẩn v3. Bản cũ của lô này chồng BA khối hệ thống dùng chung
(hậu tố trừu tượng · biến cách 3 · bảng mệnh lệnh) lên cả 4 thẻ nên vỡ trần rất xa.
Ở đây KHÔNG có khối dùng chung nào: mỗi thẻ chỉ nói kiến thức dính trực tiếp vào
chính từ đó, tối đa 2 ô đỏ.

часть và речь đều có bảng chia BẤT THƯỜNG (trọng âm dịch trong số nhiều) ⇒ mỗi thẻ
có đúng một câu chú ý phía trên bảng.
"""

S = {}
V = {}

# ────────────────────────────────────────────────────────── здравствовать
S["здравствовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">здра́в-</span>'
    '<span class="hd-gloss">KHOẺ MẠNH — gốc <b>здоро́в-</b> của <b>здоро́вье</b>, ở dạng '
    'Slav Nhà thờ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ствова-</span>'
    '<span class="hd-gloss">đuôi dựng động từ: "ở trong trạng thái…"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cộng lại: <b>ở trong trạng thái khoẻ mạnh</b>. Cặp <b>здоро́в-</b> ↔ '
    '<b>здра́в-</b> là song sinh gặp khắp nơi: bản <b>-оро-</b> đời thường, bản '
    '<b>-ра-</b> trang trọng (<b>го́род</b> ↔ <b>град</b>).</div>'
    '<div class="hd-warn"><b>Здра́вствуйте!</b> "xin chào" chính là dạng MỆNH LỆNH, '
    'nghĩa đen "hãy khoẻ mạnh!", nên có đủ hai bậc: <b>здра́вствуй</b> (người thân quen) ↔ '
    '<b>здра́вствуйте</b> (người lạ, người trên). Chữ <b>в</b> trong <i>-вств-</i> viết mà '
    'không đọc.</div>'
    '<div class="hd-warn">Ngoài lời chào, động từ này gần như chỉ còn sống trong khẩu hiệu '
    '<b>Да здра́вствует…!</b> = "…muôn năm!" — <b>да</b> + ngôi 3 hiện tại là khuôn cổ cầu chúc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>здоро́вье</b> sức khoẻ · <b>здоро́вый</b> khoẻ mạnh · '
    '<b>здра́вый</b> sáng suốt (<b>здра́вый смысл</b> lẽ thường) · <b>поздравля́ть</b> chúc mừng</div>'
)
V['здравствовать'] = 'mạnh khoẻ, an khang, trường tồn'

# ───────────────────────────────────────────────────────────── извинить
S["извинить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">из-</span>'
    '<span class="hd-gloss">RA KHỎI (cùng nghĩa giới từ <b>из</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вин-</span>'
    '<span class="hd-gloss">gốc <b>вина́</b> = LỖI, tội — đừng lẫn với <b>вино́</b> (rượu vang), '
    'hai từ khác hẳn nhau</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể; <b>-ить</b> = lớp chia 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cộng thẳng: <b>gỡ cái LỖI RA KHỎI</b> người ta = tha lỗi, bỏ qua. '
    'Tiếng Anh <i>ex-cuse</i> dựng y hệt (<i>ex</i> "ra" + <i>causa</i> "vụ việc"); cặp đối xứng '
    '<i>ac-cuse</i> là <b>обвини́ть</b> buộc tội.</div>'
    '<div class="hd-warn"><b>Cách nó đòi:</b> <b>извини́ть кого́</b> (cách 4) <b>за что</b> '
    '(<b>за</b> + cách 4) — <i>Извини́те меня́ за опозда́ние</i> = xin lỗi vì tôi đến muộn.</div>'
    '<div class="hd-warn">Dạng mệnh lệnh <b>Извини́те!</b> vừa là "xin lỗi" chuyện nhỏ, vừa là câu '
    'bắt chuyện với người lạ (<i>Извини́те, где метро́?</i>). Lỗi nặng hơn thì nói '
    '<b>Прости́те!</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>извине́ние</b> lời xin lỗi · <b>извиня́ться</b> tự mình xin lỗi '
    '(từ này là THA lỗi cho người khác) · <b>вина́</b> lỗi</div>'
)
V['извинить'] = 'tha lỗi, bỏ qua, thứ lỗi'

# ──────────────────────────────────────────────────────────────── часть
S["часть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">част-</span>'
    '<span class="hd-gloss">gốc PHẦN — mảnh được chia ra từ một cái toàn thể</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ь</span>'
    '<span class="hd-gloss">không mang nghĩa; đứng sau <b>ч</b> thì nó chỉ còn một việc là '
    'báo GIỐNG CÁI (như <b>ночь</b>, <b>дочь</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là viên gạch dựng cả một họ từ: <b>уча́стие</b> nghĩa đen "ở trong '
    'một phần" ⇒ sự tham gia; và theo từ nguyên <b>сча́стье</b> = <b>с-</b> cổ ("tốt") + '
    '<b>часть</b> ⇒ "được chia cho phần TỐT". Thuật ngữ <b>ча́сти ре́чи</b> = từ loại.</div>'
    '<div class="hd-warn"><b>Số nhiều nhảy trọng âm:</b> <b>ча́сти</b> (cách 1 và 4) nhấn ở đầu, '
    'nhưng từ cách 2 trở đi trọng âm dồn hết xuống đuôi — <b>часте́й</b>, <b>частя́м</b>, '
    '<b>частя́ми</b>, <b>частя́х</b>.</div>'
    '<div class="hd-warn"><b>часть</b> là phần của một tổng thể có cấu trúc, đi với <b>cách 2</b>: '
    '<i>часть кни́ги</i>. Còn <b>miếng cắt ra</b> phải dùng <b>кусо́к</b> — <i>кусо́к хле́ба</i> '
    'miếng bánh mì, không nói <i>часть хле́ба</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уча́стие</b> sự tham gia · <b>уча́стник</b> người tham gia · '
    '<b>уча́сток</b> thửa đất, khu vực · <b>ча́стный</b> riêng, tư nhân (đừng lẫn với '
    '<b>ча́сто</b> thường xuyên) · <b>сча́стье</b> hạnh phúc</div>'
)
V['часть'] = 'phần, bộ phận'

# ───────────────────────────────────────────────────────────────── речь
S["речь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">реч-</span>'
    '<span class="hd-gloss">gốc NÓI — là gốc <b>рек-</b> sau phép biến âm к → ч</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ь</span>'
    '<span class="hd-gloss">báo GIỐNG CÁI (như <b>ночь</b>); cách 5 là <b>ре́чью</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Biến âm к → ч là bộ luật gặp khắp nơi (<b>рука́</b> → <b>ру́чка</b>). '
    '<b>речь</b> là việc NÓI NĂNG thực tế, còn <b>язы́к</b> mới là ngôn ngữ như một hệ thống. '
    'Đừng lẫn với <b>река́</b>/<b>ре́чка</b> (sông) — khác gốc hẳn, so <b>речево́й</b> (thuộc lời '
    'nói) với <b>речно́й</b> (thuộc sông).</div>'
    '<div class="hd-warn"><b>Số nhiều nhảy trọng âm:</b> <b>ре́чи</b> (cách 1 và 4) nhấn ở đầu, '
    'nhưng từ cách 2 trở đi trọng âm dồn hết xuống đuôi — <b>рече́й</b>, <b>реча́м</b>, '
    '<b>реча́ми</b>, <b>реча́х</b>.</div>'
    '<div class="hd-warn">Cụm phải thuộc: <b>речь идёт о</b> + <b>cách 6</b> = "chuyện đang bàn '
    'là về…" — <i>Речь идёт о деньга́х</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>наре́чие</b> trạng từ; phương ngữ · <b>противоре́чие</b> mâu thuẫn · '
    '<b>уро́к</b> bài học (cùng gốc, ở bậc <b>-рок-</b>) · <b>речево́й</b> thuộc về lời nói</div>'
)
V['речь'] = 'bài phát biểu, bài diễn văn, lời nói, cách nói năng'
