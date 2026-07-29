# -*- coding: utf-8 -*-
"""k13 — tu-moi: 4 từ user vừa thêm, KHÔNG cùng họ nhau.

Mỗi thẻ soạn độc lập, không ép một trục chung, không khối hệ thống dùng chung.
Chuẩn v3: một màn hình iPhone (≤700px), tối đa 2 ô đỏ, Họ hàng được phép vắng.
"""

S = {}

S["здание"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">зд-</span>'
    '<span class="hd-gloss">XÂY, ĐẮP (gốc cổ)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ание</span>'
    '<span class="hd-gloss">đuôi tạo danh từ giống TRUNG</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái được dựng lên». Gốc <b>зд-</b> nghĩa cổ là đắp, xây — '
    'nay chỉ còn sống trong <b>созда́ть</b> (tạo ra) và <b>зо́дчий</b> (kiến trúc sư). '
    'Đuôi <b>-ание</b> cho biết đây là danh từ giống TRUNG.</div>'
    '<div class="hd-warn">🏢 <b>зда́ние</b> là công trình xây (trường, bệnh viện, cao ốc); '
    '<b>дом</b> mới là nhà để ở. Cụm phải thuộc: <b>высо́тное зда́ние</b> nhà cao tầng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>созда́ть</b> tạo ra · <b>созда́ние</b> sự tạo ra, tạo vật · '
    '<b>созда́тель</b> người tạo ra · <b>зо́дчий</b> kiến trúc sư (từ cổ)</div>'
)

S["лучше"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">луч-</span>'
    '<span class="hd-gloss">gốc riêng, không phải хорош-</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ше</span>'
    '<span class="hd-gloss">đuôi so sánh hơn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhớ cả bộ đuôi <b>-ше</b>: <b>ра́но</b> → <b>ра́ньше</b>, '
    '<b>далеко́</b> → <b>да́льше</b>, <b>мно́го</b> → <b>бо́льше</b>, '
    '<b>хорошо́</b> → <b>лу́чше</b>. Hai cái cuối đổi hẳn gốc nên phải thuộc, không suy ra '
    'được; gốc <b>луч-</b> ở đây không dính gì tới луч «tia sáng».</div>'
    '<div class="hd-warn">⚠️ Tính từ <b>хоро́ший</b> và trạng từ <b>хорошо́</b> dùng CHUNG '
    'đúng một dạng so sánh hơn là <b>лу́чше</b> — không bên nào có dạng riêng.</div>'
    '<div class="hd-warn">💡 <b>лу́чше</b> + nguyên thể = «tốt hơn là nên…»: '
    '<b>Лу́чше пойти́ домо́й</b>. Còn <b>Мне лу́чше</b> = tôi đỡ hơn rồi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лу́чший</b> tốt nhất · <b>улучша́ть</b> – <b>улу́чшить</b> '
    'cải thiện · <b>улучше́ние</b> sự cải thiện</div>'
)

# Từ mượn đứng một mình: KHÔNG có mục "Họ hàng" — tiếng Nga không đẻ ra từ phái
# sinh nào từ `отель` (mọi thứ quanh nó đều dựng trên gốc Nga `гость`).
S["отель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — mượn nguyên tiếng Pháp <i>hôtel</i> '
    '(h câm, nên vào tiếng Nga chỉ còn <b>оте́ль</b>).</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Biết chữ <i>hotel</i> là biết từ này: chỉ đọc lại theo lối Nga, '
    'trọng âm rơi vào âm cuối như hầu hết từ mượn phương Tây — <b>бале́т</b>, '
    '<b>биле́т</b>, <b>музе́й</b>.</div>'
    '<div class="hd-warn">⚠️ Đuôi <b>-ь</b> thường báo giống CÁI, nhưng <b>оте́ль</b> là '
    'giống ĐỰC: <b>в но́вом оте́ле</b>. Từ mượn không chịu luật đuôi <b>-ь</b>.</div>'
    '<div class="hd-warn">🏨 Từ Nga gốc cho «khách sạn» là <b>гости́ница</b> '
    '(từ <b>гость</b> khách) và vẫn phổ biến hơn; <b>оте́ль</b> nghiêng về khách sạn lớn, '
    'kiểu quốc tế.</div>'
)

S["столица"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">стол-</span>'
    '<span class="hd-gloss">NGAI VUA (nghĩa cổ của стол)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ица</span>'
    '<span class="hd-gloss">đuôi danh từ giống CÁI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thành phố đặt ngai vua = thủ đô. Nghĩa «ngai» của <b>стол</b> nay '
    'chỉ còn thấy trong ít từ như <b>престо́л</b> (ngai vàng); nghĩa thường ngày «cái bàn» '
    'là lớp nghĩa mới hơn.</div>'
    '<div class="hd-warn">⚠️ Hai nghĩa của <b>стол</b> rẽ hai ngả: <b>столи́ца</b> ← «ngai» '
    '(thủ đô), còn <b>столо́вая</b> ← «bàn ăn» (nhà ăn). Nhìn gần giống nhau, đừng lẫn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стол</b> cái bàn · <b>престо́л</b> ngai vàng · '
    '<b>столи́чный</b> thuộc về thủ đô</div>'
)


# --- Field Vietnamese: đề bài của deck 1-go, phải chỉ có MỘT đáp án đúng ------
# `лучше` (tốt hơn) và `столица` (thủ đô) đã đủ sát, không đụng từ nào khác
# trong kho -> giữ nguyên.
V = {
    # "tòa nhà" trần trụi dễ bị gõ thành `дом` (nhà, ngôi nhà, tổ ấm)
    "здание": "tòa nhà, công trình xây (trường, cao ốc — không phải nhà để ở)",
    # tiếng Nga có hai từ cho "khách sạn": отель (mượn) và гостиница (gốc Nga)
    "отель": "khách sạn (từ mượn, kiểu quốc tế)",
}
