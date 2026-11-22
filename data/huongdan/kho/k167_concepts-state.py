# -*- coding: utf-8 -*-
"""k167 — concepts::state: nhà nước, luật pháp, và vài tính từ đánh giá.

Chỗ cần nhất quán trong lô:
(1) gốc прав- = THẲNG, ĐÚNG — справедли́вый, правосу́дие; khớp пра́во, пра́вый, пра́вда.
(2) gốc -суд- = XÉT — суди́ть, правосу́дие; khớp обсуди́ть («gốc của суд toà án, суди́ть xét xử»).
(3) gốc -лог-/-лож- = ĐẶT, NẰM (г ↔ ж) — нало́г, зало́жник; khớp положи́ть («gốc NẰM»).
(4) без-/бес- — бесполе́зный (бес- trước п) vs безопа́сный (без- trước nguyên âm); luật nói ở
    бесполе́зный, безопа́сный chỉ trỏ sang.
(5) -каз- = NÓI RA, chỉ ra — наказа́ние; khớp сказа́ть, заказа́ть, каза́ться.
(6) Latin ministrare «phục vụ» — администрати́вный nhắc мини́стр một câu; министе́рство khớp
    thẻ мини́стр (k121: «thêm -ство là ra cơ quan, trọng âm nhảy sang е́»).
Họ hàng cố ý vắng: комите́т, кампа́ния, флот (mượn đứng một mình, không phái sinh thông dụng).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
# министе́рство: ngoặc cũ do máy tạo thẻ sinh (luồng chính xác nhận 22/11, sẽ gỡ trước khi nạp).
V = {
    "министерство": "bộ",                             # bỏ ngoặc; gloss board/office/department là nghĩa phụ, không thông dụng
    "кампания": "chiến dịch, cuộc vận động",         # gỡ va chạm với опера́ция; gloss: drive
    "превосходный": "tuyệt vời, xuất sắc, vượt trội",  # gỡ va chạm отли́чный/прекра́сный; gloss: superior/outstanding
    "судить": "phán xét, đánh giá, xét xử",          # gloss: to try (in court) — nghĩa gốc của суд
    "считаться": "được coi là, được xem là, tính đến",  # gloss: to take into account / reckon with
}

# ----------------------------------------------------------------- влияние
S["влияние"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ли-</span>'
    '<span class="hd-gloss">RÓT, CHẢY — gốc của <b>лить</b> rót</span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ние</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Chảy vào» người khác ⇒ ảnh hưởng — y hệt tiếng Anh <i>in-fluence</i> '
    '(Latin <i>influere</i> «chảy vào»).</div>'
    '<div class="hd-warn">Ảnh hưởng LÊN cái gì: <b>на</b> + cách 4 — <b>влия́ние на дете́й</b>, '
    '<b>влия́ть на здоро́вье</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>влия́ть</b> ảnh hưởng (động từ) · <b>влия́тельный</b> có thế lực · '
    '<b>лить</b> rót, đổ</div>'
)

# ----------------------------------------------------------------- справедливый
S["справедливый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">tiền tố, KHÔNG tách ra nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-прав-</span>'
    '<span class="hd-gloss">THẲNG, ĐÚNG — như <b>пра́вда</b>, <b>пра́во</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-едли́в-ый</span>'
    '<span class="hd-gloss">đuôi tính từ, không chẻ tiếp được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Theo đúng lẽ thẳng ⇒ công bằng; đòi hỏi đúng lẽ ⇒ chính đáng: '
    '<b>справедли́вое тре́бование</b> yêu cầu chính đáng. Câu than hay gặp nhất dùng dạng '
    '<b>-о</b>: <b>Э́то несправедли́во!</b> = Thật bất công!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>справедли́вость</b> sự công bằng · <b>несправедли́вый</b> bất công · '
    '<b>пра́вда</b> sự thật · <b>пра́вый</b> đúng, bên phải</div>'
)

# ----------------------------------------------------------------- превосходный
S["превосходный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пре-</span>'
    '<span class="hd-gloss">VƯỢT QUÁ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вос-</span>'
    '<span class="hd-gloss">LÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-хо́д-н-ый</span>'
    '<span class="hd-gloss">ĐI — như <b>выходи́ть</b>; -н-ый đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đi vượt lên trên» người khác ⇒ vượt trội, xuất sắc — từ động từ '
    '<b>превосходи́ть</b> vượt hơn. Nghe trang trọng, sách vở hơn <b>отли́чный</b>. '
    'Dạng ngắn chèn е: <b>превосхо́ден</b>.</div>'
    '<div class="hd-warn">Ngữ pháp gọi cấp so sánh cao nhất là <b>превосхо́дная сте́пень</b> '
    '— đúng nghĩa «cấp vượt trội».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>превосходи́ть</b> vượt hơn · <b>превосхо́дство</b> sự vượt trội · '
    '<b>выходи́ть</b> đi ra · <b>происходи́ть</b> xảy ra</div>'
)

# ----------------------------------------------------------------- бесполезный
S["бесполезный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бес-</span>'
    '<span class="hd-gloss">KHÔNG CÓ (= <b>без</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-поле́з-н-ый</span>'
    '<span class="hd-gloss">CÓ ÍCH — <b>по́льза</b> lợi ích</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không có <b>по́льза</b> ⇒ vô ích; bỏ <b>бес-</b> là ra <b>поле́зный</b>. '
    'Dạng ngắn chèn е y như <b>поле́зен</b>: <b>бесполе́зен</b>. Câu hay dùng: '
    '<b>Э́то бесполе́зно</b> = Vô ích thôi.</div>'
    '<div class="hd-warn">Luật viết: <b>без-</b> gặp phụ âm vô thanh (п, т, к, с…) thì thành '
    '<b>бес-</b> — <b>бесполе́зный</b>, <b>беспла́тный</b>; còn trước nguyên âm giữ nguyên: '
    '<b>безопа́сный</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́льза</b> lợi ích · <b>поле́зный</b> có ích · '
    '<b>испо́льзовать</b> sử dụng</div>'
)

# ----------------------------------------------------------------- безопасный
S["безопасный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">без-</span>'
    '<span class="hd-gloss">KHÔNG CÓ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-опа́с-н-ый</span>'
    '<span class="hd-gloss">E NGẠI — gốc <b>опаса́ться</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không có gì phải e ngại ⇒ an toàn; bỏ <b>без-</b> là ra nghĩa ngược '
    '<b>опа́сный</b> nguy hiểm. Giữ <b>без-</b> vì đứng trước nguyên âm (luật ở thẻ '
    '<b>бесполе́зный</b>). Dạng ngắn chèn е: <b>безопа́сен</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>безопа́сность</b> sự an toàn, an ninh · <b>опа́сный</b> nguy hiểm · '
    '<b>опа́сность</b> sự nguy hiểm · <b>опаса́ться</b> e ngại</div>'
)

# ----------------------------------------------------------------- считаться
S["считаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">GỘP LẠI, cộng vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-чит-а́ть</span>'
    '<span class="hd-gloss">ĐẾM — cùng gốc <b>чита́ть</b> đọc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">ở đây = ĐƯỢC (bị động)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Được tính là» ⇒ được coi là. Cái «là» đứng ở cách 5: '
    '<b>Он счита́ется лу́чшим врачо́м</b> = Anh ấy được coi là bác sĩ giỏi nhất. '
    'Không chủ ngữ: <b>Счита́ется, что…</b> = Người ta cho rằng…</div>'
    '<div class="hd-warn"><b>счита́ться с</b> + cách 5 = tính đến, tôn trọng: '
    '<b>счита́ться с мне́нием други́х</b> tôn trọng ý kiến người khác.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>счита́ть</b> cho rằng, đếm · <b>посчита́ть</b> đếm xong · '
    '<b>счёт</b> hóa đơn, tỉ số</div>'
)

# ----------------------------------------------------------------- налог
S["налог"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">LÊN, đè lên</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лог</span>'
    '<span class="hd-gloss">ĐẶT, NẰM — cùng gốc -лож- của <b>положи́ть</b>, họ với <b>лежа́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái được «đặt lên» vai người dân ⇒ thuế; động từ cùng gốc '
    '<b>наложи́ть</b> = đặt lên, áp đặt. <b>-лог-</b> và <b>-лож-</b> là một gốc, г hoá ж '
    '(như <b>друг → дружи́ть</b>).</div>'
    '<div class="hd-warn">Nộp thuế: <b>плати́ть нало́ги</b> — thường dùng số nhiều.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нало́говый</b> thuộc thuế · <b>положи́ть</b> đặt · '
    '<b>предложи́ть</b> đề nghị · <b>зало́жник</b> con tin</div>'
)

# ----------------------------------------------------------------- правосудие
S["правосудие"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">прав-о-</span>'
    '<span class="hd-gloss">THẲNG, ĐÚNG — <b>пра́во</b> luật, quyền; -о- nối hai gốc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-суд-</span>'
    '<span class="hd-gloss">XÉT — gốc của <b>суд</b> toà án, <b>суди́ть</b> xét xử</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ие</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Xét xử theo lẽ đúng» ⇒ công lý; rộng ra là cả bộ máy làm việc đó '
    '⇒ nền tư pháp. Hai gốc đều đã có thẻ: ghép <b>пра́во</b> với <b>суд</b> là ra.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>суд</b> toà án · <b>суди́ть</b> xét xử · <b>судья́</b> thẩm phán · '
    '<b>пра́во</b> luật, quyền · <b>справедли́вый</b> công bằng</div>'
)

# ----------------------------------------------------------------- заседание
S["заседание"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">tiền tố, ở đây KHÔNG tách ra nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сед-</span>'
    '<span class="hd-gloss">NGỒI — như <b>сиде́ть</b>, <b>сесть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ние</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Các thành viên «ngồi lại» làm việc ⇒ phiên họp của một cơ quan: '
    '<b>заседа́ние суда́</b> phiên toà, <b>заседа́ние прави́тельства</b> phiên họp chính phủ. '
    'Họp toàn thể thành viên một tập thể (họp phụ huynh, họp cư dân) thì dùng <b>собра́ние</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сиде́ть</b> ngồi · <b>сесть</b> ngồi xuống · '
    '<b>сосе́д</b> hàng xóm (người ngồi cạnh) · <b>председа́тель</b> chủ tịch (người ngồi trước)</div>'
)

# ----------------------------------------------------------------- наказание
S["наказание"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">tiền tố, ở đây KHÔNG tách ra nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-каз-</span>'
    '<span class="hd-gloss">NÓI RA, chỉ ra — như <b>сказа́ть</b>, <b>показа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ние</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>наказа́ть</b> phạt (CHT <b>нака́зывать</b>). '
    'Nghĩa cổ của động từ này là «dặn bảo, răn dạy» — còn sót trong <b>нака́з</b> lời dặn; '
    'răn dạy kẻ có lỗi ⇒ phạt.</div>'
    '<div class="hd-warn">Phạt AI (cách 4) VÌ cái gì (<b>за</b> + cách 4): '
    '<b>наказа́ть сы́на за ложь</b> phạt con trai vì nói dối.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>наказа́ть</b> phạt · <b>сказа́ть</b> nói ra · '
    '<b>показа́ть</b> cho xem · <b>прика́з</b> mệnh lệnh</div>'
)

# ----------------------------------------------------------------- административный
S["административный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga: = <i>administrative</i>, làm từ '
    '<b>администра́ция</b>; đuôi <b>-ивный</b> là bản Nga của <i>-ive</i> '
    '(<b>акти́вный</b> <i>active</i>).</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Latin <i>ad-</i> «hướng tới» + <i>ministrare</i> «phục vụ» — cùng gốc xa '
    'với <b>мини́стр</b>. Dùng cho bộ máy quản lý: <b>администрати́вный центр</b> trung tâm '
    'hành chính. Là tính từ chỉ quan hệ nên gần như chỉ dùng dạng dài.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>администра́ция</b> ban quản lý, chính quyền · '
    '<b>администра́тор</b> quản trị viên, lễ tân · <b>мини́стр</b> bộ trưởng</div>'
)

# ----------------------------------------------------------------- заложник
S["заложник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">tiền tố, ở đây KHÔNG tách ra nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лож-</span>'
    '<span class="hd-gloss">ĐẶT, NẰM — như <b>положи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ник</span>'
    '<span class="hd-gloss">→ người</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ <b>зало́г</b> «vật thế chấp, tiền đặt cọc» ⇒ người bị giữ làm vật '
    'thế chấp = con tin. Cùng gốc với <b>нало́г</b> thuế cùng lô (<b>-лог-/-лож-</b>, г hoá ж).</div>'
    '<div class="hd-warn">Bắt làm con tin: <b>взять в зало́жники</b> — <b>в</b> + số nhiều mang '
    'dạng như cách 1, kể cả khi chỉ bắt một người: <b>Его́ взя́ли в зало́жники</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>зало́г</b> tiền đặt cọc, vật thế chấp · <b>нало́г</b> thuế · '
    '<b>положи́ть</b> đặt</div>'
)

# ----------------------------------------------------------------- министерство
S["министерство"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">министр-</span>'
    '<span class="hd-gloss">BỘ TRƯỞNG — <b>мини́стр</b>, mượn Latin <i>minister</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ство</span>'
    '<span class="hd-gloss">→ cơ quan, giống trung — như <b>прави́тельство</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cơ quan của bộ trưởng ⇒ bộ. Trọng âm rời chỗ cũ, nhảy sang <b>е́</b>: '
    '<b>мини́стр → министе́рство</b>.</div>'
    '<div class="hd-warn">Bộ Ngoại giao: <b>министе́рство иностра́нных дел</b> (viết tắt МИД).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мини́стр</b> bộ trưởng · <b>прави́тельство</b> chính phủ (cùng đuôi '
    '-ство)</div>'
)

# ----------------------------------------------------------------- губернатор
S["губернатор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga: mượn Latin <i>gubernator</i> «người cầm lái» '
    '— chính là gốc của tiếng Anh <i>governor</i>, <i>govern</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người «cầm lái» một tỉnh ⇒ tỉnh trưởng, thống đốc. Thời Nga hoàng, vùng '
    'ông cai quản gọi là <b>губе́рния</b>; nay là <b>о́бласть</b> nhưng chức vẫn gọi '
    '<b>губерна́тор</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>губе́рния</b> tỉnh (thời Nga hoàng)</div>'
)

# ----------------------------------------------------------------- кандидат
S["кандидат"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga: Latin <i>candidatus</i> «người mặc áo trắng» '
    '(<i>candidus</i> trắng) — ở La Mã người ra ứng cử mặc áo choàng trắng. = <i>candidate</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giống tiếng Anh, trọng âm ở cuối: <b>кандида́т</b>. '
    '<b>кандида́т в президе́нты</b> ứng cử viên tổng thống.</div>'
    '<div class="hd-warn"><b>кандида́т нау́к</b> là học vị sau đại học của Nga — Việt Nam trước '
    'đây dịch là «phó tiến sĩ».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кандидату́ра</b> sự ứng cử, người được đề cử</div>'
)

# ----------------------------------------------------------------- комитет
S["комитет"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga: mượn tiếng Pháp <i>comité</i> '
    '(tiếng Anh <i>committee</i>).</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>committee</i>, trọng âm cuối: <b>комите́т</b>. Chữ К trong КГБ chính là '
    'từ này: <b>Комите́т госуда́рственной безопа́сности</b> Uỷ ban An ninh Nhà nước — có '
    '<b>безопа́сность</b> họ với <b>безопа́сный</b> cùng lô.</div>'
)

# ----------------------------------------------------------------- флот
S["флот"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga: mượn từ Tây Âu (Hà Lan / Pháp) thời Pi-e '
    'Đại đế, họ hàng với tiếng Anh <i>fleet</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cả đội tàu ⇒ hạm đội; tàu chiến của cả nước ⇒ hải quân. Số nhiều có '
    'hai cách nhấn song song, cả hai đều đúng: <b>фло́ты</b> / <b>флоты́</b>.</div>'
    '<div class="hd-warn">Đi lính hải quân: <b>служи́ть на флоту́</b> — dạng riêng cho «ở đâu», '
    'đuôi <b>-у́</b> mang trọng âm.</div>'
)

# ----------------------------------------------------------------- террорист
S["террорист"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">терро́р-</span>'
    '<span class="hd-gloss">KHỦNG BỐ — Latin <i>terror</i> nỗi kinh hoàng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ст</span>'
    '<span class="hd-gloss">→ người làm / theo (= <i>-ist</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>terrorist</i>. Đuôi <b>-и́ст</b> luôn nhận trọng âm và chỉ người, '
    'như <b>тури́ст</b> khách du lịch.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>терро́р</b> sự khủng bố · <b>террори́зм</b> chủ nghĩa khủng bố · '
    '<b>террористи́ческий</b> thuộc khủng bố</div>'
)

# ----------------------------------------------------------------- судить
S["судить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">суд-</span>'
    '<span class="hd-gloss">XÉT — gốc của <b>суд</b> toà án</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Xét ở toà ⇒ xét xử (cách 4: <b>суди́ть престу́пника</b>); xét trong đầu ⇒ '
    'đánh giá (<b>о</b> + cách 6). Dạng «tôi» д → ж, trọng âm lùi ở ngôi khác: '
    '<b>я сужу́</b>, <b>ты су́дишь</b>. Cặp HT tuỳ nghĩa: kết án là <b>осуди́ть</b>.</div>'
    '<div class="hd-warn">Mở đầu câu rất hay gặp: <b>су́дя по</b> + cách 3 = xét theo — '
    '<b>Су́дя по всему́…</b> = Xét mọi lẽ thì…</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>суд</b> toà án · <b>судья́</b> thẩm phán, trọng tài · '
    '<b>обсуди́ть</b> thảo luận · <b>правосу́дие</b> công lý</div>'
)

# ----------------------------------------------------------------- кампания
S["кампания"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga: mượn tiếng Pháp <i>campagne</i> «cánh đồng» '
    '(Latin <i>campus</i>) — quân đội ra đồng đánh trận theo mùa ⇒ chiến dịch. = <i>campaign</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Rộng ra là mọi cuộc vận động có tổ chức: <b>избира́тельная кампа́ния</b> '
    'chiến dịch tranh cử, <b>рекла́мная кампа́ния</b> chiến dịch quảng cáo.</div>'
    '<div class="hd-warn">Đọc lên gần như y hệt <b>компа́ния</b> công ty, nhóm bạn (о không nhấn '
    'đọc thành а) — chỉ khác chữ viết: chiến dịch là к<b>а</b>мпания như <i>campaign</i>, '
    'công ty là к<b>о</b>мпания như <i>company</i>.</div>'
)

# ----------------------------------------------------------------- вывод
S["вывод"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span>'
    '<span class="hd-gloss">RA, và luôn mang trọng âm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вод</span>'
    '<span class="hd-gloss">DẪN — như <b>вести́</b>, <b>води́тель</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Dẫn ra» từ những gì đã biết ⇒ điều rút ra được = kết luận; dẫn quân ra '
    '⇒ rút quân: <b>вы́вод войск</b>.</div>'
    '<div class="hd-warn">Rút ra kết luận: <b>сде́лать вы́вод</b> — nói đúng là «làm» một kết luận.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вести́</b> dẫn, dắt · <b>води́тель</b> tài xế · '
    '<b>перево́д</b> bản dịch · <b>привести́</b> dẫn đến</div>'
)

# ----------------------------------------------------------------- трус
S["трус"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: gốc trơn — chính nó là gốc của cả họ bên dưới.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Câu mắng quen: <b>Ты трус!</b> = Đồ hèn! Nghĩa «động đất» trong từ điển '
    'là nghĩa cổ, bỏ qua.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>трусы́</b> quần lót, quần đùi (trọng âm cuối). Số nhiều '
    'của <b>трус</b> giữ trọng âm ở gốc: <b>тру́сов</b>, <b>тру́сам</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>трусли́вый</b> nhát gan · <b>тру́сость</b> sự hèn nhát</div>'
)

B = {
    "docbangmat": 82,
    "loitubat": 2,
    "nguonsai": 0,
    "baolen": [
        "Va chạm nghĩa đã gỡ phía mình, mô phỏng do_va_cham (chỉ đọc, V mới thay vào) = 0 va chạm dính k167: кампа́ния +«cuộc vận động» (gloss drive) · превосхо́дный +«vượt trội» (gloss superior/outstanding). Cần duyệt hai V này.",
        "V khác cần duyệt: суди́ть +«xét xử» (gloss to try in court) · счита́ться +«tính đến» (gloss to take into account / reckon with — nghĩa của счита́ться с).",
        "министе́рство: V = «bộ» theo lệnh ngoại lệ của luồng chính (ngoặc do máy sinh). Đề MỎNG: «bộ» tiếng Việt còn nghĩa «bộ đồ, bộ sưu tập»; hiện không thẻ nào khác mang nghĩa «bộ» nên không va chạm, nhưng user có thể muốn tự chú thích tay.",
        "трус: cửa soát báo lệch тру́сы vs từ điển трусы́ (quần lót) — đồng tự THẬT. KHÔNG nới MIEN_TRU: đã viết lại ô đỏ dùng тру́сов/тру́сам để vẫn dạy được bẫy трусы́.",
        "Chỗ KHÔNG chắc hẳn (đã viết mềm, chưa hạ ô Mức tin): наказа́ть nghĩa cổ «dặn bảo, răn dạy» (theo từ nguyên phổ biến, нака́з còn nghĩa lời dặn) · флот mượn Hà Lan HAY Pháp (ghi cả hai) · превосхо́дный «trang trọng hơn отли́чный» (sắc thái) · администрати́вный «gần như chỉ dùng dạng dài».",
        "наказа́ние: ĐÃ ghép với -каз- (сказа́ть, показа́ть) — khớp thẻ заказа́ть/сказа́ть «NÓI RA, chỉ ra»; không dùng câu chữ của thẻ каза́ться.",
        "администрати́вный: có nhắc мини́стр một câu (Latin ad + ministrare), đặt trong Cách nhớ, không chẻ.",
        "Họ hàng vắng có chủ ý: комите́т, кампа́ния, флот (mượn đứng một mình). кампа́ния dùng ô đỏ cho bẫy компа́ния thay vào.",
    ],
}
