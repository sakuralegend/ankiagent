# -*- coding: utf-8 -*-
"""k53 — qualities: LÔ SỬA. Giữ phần đang tốt của 14 thẻ tính từ, thêm mục
"Họ hàng" cho thẻ thiếu, hạ xuống tối đa 2 ô đỏ, và BỎ HẲN mọi khối hệ thống
dùng chung (luật -н-, biến âm г·к·х, so sánh hơn, dạng ngắn) — chúng lặp ở
8/14 thẻ và nuốt quá nửa chiều cao. Mỗi thẻ giờ đứng một mình."""

# 🔴 KHÔNG dựng biến khối dùng chung rồi cộng vào mọi thẻ — xem README §3.

S = {}
V = {}

S["будничный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">будн-</span>'
    '<span class="hd-gloss">бу́дни — ngày thường, ngày phải đi làm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ичн-</span>'
    '<span class="hd-gloss">hậu tố tạo tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiếng Nga chia tuần làm hai nửa có tên riêng: '
    '<b>бу́дни</b> (ngày phải đi làm) và <b>выходны́е</b> (ngày nghỉ). '
    '<b>Бу́дничный</b> = thuộc về nửa phải đi làm.</div>'
    '<div class="hd-why">Từ đó ra nghĩa bóng rất hay dùng: <b>đều đều, tẻ nhạt, '
    'không có gì đặc biệt</b> — <b>бу́дничный го́лос</b> = giọng dửng dưng như mọi ngày.</div>'
    '<div class="hd-warn"><b>Nối với thẻ bạn đã có:</b> <b>выходно́й</b> (ngày nghỉ) '
    'chính là vế đối của từ này. Học cặp đối rẻ hơn học hai từ rời.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бу́дни</b> ngày thường trong tuần (chỉ có số nhiều) · '
    '<b>бу́днично</b> (trạng từ) một cách tẻ nhạt · gần nghĩa nhưng khác gốc: '
    '<b>повседне́вный</b> thường nhật</div>'
)

S["ветреный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ветр-</span>'
    '<span class="hd-gloss">ве́тер (gió) — chữ <b>е</b> rụng khi thêm hậu tố</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ен-</span>'
    '<span class="hd-gloss">hậu tố tạo tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là <b>lộng gió</b>. Nhưng chỗ đáng học là nghĩa bóng: '
    '<b>ве́треный челове́к</b> = người <b>nông nổi, đứng núi này trông núi nọ</b> — '
    'đầu óc bị gió thổi bay. Tiếng Việt có hình ảnh gần y hệt: "gió chiều nào theo chiều ấy".</div>'
    '<div class="hd-warn"><b>Ngoại lệ chính tả nổi tiếng:</b> <b>ве́треный</b> viết MỘT chữ '
    '<b>н</b>, trong khi hầu hết tính từ cùng lớp viết hai (<b>-енный</b>). Hễ thêm tiền tố '
    'thì lại quay về hai <b>н</b>: <b>безве́тренный</b> (lặng gió).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ве́тер</b> gió · <b>ветеро́к</b> làn gió nhẹ · '
    '<b>ветряно́й</b> chạy bằng sức gió (cối xay gió) · <b>прове́трить</b> mở cửa cho thoáng</div>'
)

S["дождливый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дожд-</span>'
    '<span class="hd-gloss">дождь (mưa)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лив-</span>'
    '<span class="hd-gloss">HAY, ĐẦY, dễ bị — hậu tố chỉ khuynh hướng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không phải <b>-ный</b> mà là <b>-ливый</b>, nên nghĩa không phải '
    '"thuộc về mưa" mà là <b>mưa dai, mưa nhiều</b> — nói về cả một mùa, một vùng.</div>'
    '<div class="hd-why">Nắm <b>-ливый</b> là mở khoá cả lớp tính từ tả tính cách: '
    '<b>терпели́вый</b> kiên nhẫn · <b>тала́нтливый</b> có tài · <b>лени́вый</b> lười · '
    '<b>молчали́вый</b> ít nói.</div>'
    '<div class="hd-warn"><b>Bẫy chính tả:</b> cụm <b>-ждь</b> trong <b>дождь</b> mỗi vùng '
    'đọc một kiểu. Cứ viết đúng mặt chữ, đừng suy chính tả từ cái tai nghe được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дождь</b> mưa · <b>до́ждик</b> mưa nhỏ · '
    '<b>дождево́й</b> thuộc về mưa (<b>дождева́я вода́</b> nước mưa) · '
    '<b>дождеви́к</b> áo mưa</div>'
)

S["морозный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мороз-</span>'
    '<span class="hd-gloss">моро́з — băng giá, rét cắt da (dưới 0°C)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span>'
    '<span class="hd-gloss">hậu tố tạo tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ ghép thẳng với <b>-н-</b>, không đổi chữ nào — lấy từ này '
    'làm mẫu chuẩn rồi soi các từ khác lệch chỗ nào.</div>'
    '<div class="hd-why"><b>Моро́з</b> là một trong những từ Nga nhất: <b>Дед Моро́з</b> = '
    'Ông già Tuyết (nghĩa đen "Ông Nội Băng Giá"), nhân vật Năm Mới thay cho ông già Noel.</div>'
    '<div class="hd-warn"><b>Phân biệt sắc thái:</b> <b>моро́зный</b> = rét ÂM ĐỘ, đóng băng. '
    'Còn <b>холо́дный</b> chỉ là lạnh nói chung. Người Nga tách bạch hai mức này rất rõ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>моро́з</b> băng giá · <b>моро́женое</b> kem (nghĩa đen: thứ đã bị '
    'làm đông) · <b>морози́льник</b> tủ đông · <b>замёрзнуть</b> chết cóng, đóng băng</div>'
)

S["облачный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">облач-</span>'
    '<span class="hd-gloss">о́блако (đám mây) — chữ <b>к</b> đã mềm thành <b>ч</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span>'
    '<span class="hd-gloss">hậu tố tạo tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỗ phải để mắt là chữ <b>к</b> của <b>о́блако</b> mềm thành <b>ч</b> '
    'khi gặp hậu tố. Biết vậy thì <b>о́блачный</b> không còn là từ mới, chỉ là từ cũ mặc áo khác.</div>'
    '<div class="hd-why">Nghĩa hiện đại dùng y như tiếng Anh: <b>о́блачное хране́ние</b> = '
    'lưu trữ đám mây.</div>'
    '<div class="hd-warn">⚠️ Mức tin: <b>о́блако</b> vốn là <b>об-</b> (quanh) + gốc '
    '<b>-волок-</b> (bọc, kéo phủ) — cùng họ với <b>оболо́чка</b> (lớp vỏ bọc). Đây là từ '
    'nguyên, không phải luật suy ra được; người Nga hôm nay không còn cảm thấy nó nữa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>о́блако</b> đám mây · <b>о́блачность</b> lượng mây, độ che phủ · '
    '<b>безо́блачный</b> quang mây, không một gợn mây · <b>о́блачно</b> (trạng từ) trời nhiều mây</div>'
)

S["пасмурный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">па-</span>'
    '<span class="hd-gloss">tiền tố cổ, ý "phủ lên, hơi hướng"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-смур-</span>'
    '<span class="hd-gloss">U ÁM, tối sầm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">hậu tố + đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trời <b>xám xịt kín mây, không thấy mặt trời</b>. Nặng hơn '
    '<b>о́блачный</b> (chỉ là có mây, vẫn hửng nắng) — <b>па́смурный</b> là kín đặc, tối trời.</div>'
    '<div class="hd-why">Dùng cho cả người: <b>па́смурное лицо́</b> = gương mặt rầu rĩ. Tiếng Nga '
    'rất hay mượn thời tiết để tả tâm trạng, và bạn cũng dùng được luôn kiểu đó.</div>'
    '<div class="hd-warn">⚠️ Mức tin: cách chẻ <b>па- + -смур-</b> là lối phân tích từ nguyên, '
    'không phải thứ người Nga hôm nay còn cảm thấy. Nhớ nó gắn với <b>хму́рый</b> (cau có, ảm đạm) '
    'là đủ dùng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>па́смурно</b> (trạng từ) trời u ám · gần nghĩa, khác gốc: '
    '<b>хму́рый</b> cau có, ảm đạm · <b>су́мрачный</b> tối mờ · <b>я́сный</b> quang đãng (vế đối)</div>'
)

S["положительный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể hoàn thành — ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лож-</span>'
    '<span class="hd-gloss">ĐẶT, ĐỂ (положи́ть = đặt xuống)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тельн-</span>'
    '<span class="hd-gloss">biến động từ → tính từ: "có tính chất làm việc đó"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái gì đã được <b>đặt xuống</b>, đã chốt rồi, thì là <b>khẳng định</b>. '
    'Tiếng Anh đi đúng con đường ấy: <i>positive</i> ← Latin <i>ponere</i> = <b>đặt</b>.</div>'
    '<div class="hd-why">Đuôi <b>-тельный</b> báo hiệu <b>tính từ sinh ra từ động từ</b>: '
    '<b>внима́тельный</b> chăm chú · <b>обяза́тельный</b> bắt buộc.</div>'
    '<div class="hd-warn"><b>Cặp đối:</b> <b>отрица́тельный</b> tiêu cực, phủ định — <b>от-</b> '
    '(rời ra) + <b>-риц-</b> (NÓI) → "nói ngược lại". Lại trùng tiếng Anh: <i>negative</i> ← '
    '<i>negare</i> = nói không.</div>'
    '<div class="hd-sec">Họ hàng — gốc лож- / лаг- / леж- (đặt, nằm)</div>'
    '<div class="hd-fam"><b>положи́ть</b> đặt · <b>предложе́ние</b> câu; lời đề nghị · '
    '<b>положе́ние</b> vị trí, tình thế · <b>приложе́ние</b> ứng dụng · <b>лежа́ть</b> nằm</div>'
    '<div class="hd-warn"><b>Bẫy:</b> <b>ложь</b> (lời nói dối) KHÔNG cùng gốc — nó ra từ '
    '<b>лгать</b>. Giống mặt chữ, khác hẳn họ.</div>'
)

S["снежный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">снеж-</span>'
    '<span class="hd-gloss">снег (tuyết) — chữ <b>г</b> đã mềm thành <b>ж</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span>'
    '<span class="hd-gloss">hậu tố tạo tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là <b>ví dụ mẫu</b> của luật <b>г → ж</b>. Không biết luật thì bạn '
    'tưởng <b>снег</b> và <b>сне́жный</b> là hai từ phải học riêng; biết rồi thì chỉ còn một từ.</div>'
    '<div class="hd-why">Nghĩa là "thuộc về tuyết, đầy tuyết": <b>сне́жная зима́</b> = mùa đông '
    'nhiều tuyết.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>снег</b> tuyết · <b>снежи́нка</b> bông tuyết · '
    '<b>снегови́к</b> người tuyết · <b>Снегу́рочка</b> Cô Bé Tuyết (cháu gái ông già Tuyết, '
    'nhân vật Năm Mới của Nga)</div>'
)

S["солнечный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">солн-</span>'
    '<span class="hd-gloss">со́лнце (mặt trời)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ечн-</span>'
    '<span class="hd-gloss">hậu tố tính từ, chữ <b>ц</b> mềm thành <b>ч</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thêm một nhánh của luật biến âm bạn đã gặp: <b>ц → ч</b>. So cả bộ: '
    'снег → сне́<b>ж</b>ный · о́блако → о́бла<b>ч</b>ный · со́лнце → со́лне<b>ч</b>ный.</div>'
    '<div class="hd-warn"><b>Bẫy chính tả kinh điển:</b> chữ <b>л</b> trong <b>со́лнце</b> KHÔNG '
    'được đọc — người Nga nói "SON-tse". Nhưng viết thì bắt buộc phải có <b>л</b>. Đúng loại lỗi '
    'bạn sẽ mắc ở ô gõ nếu chép theo tai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>со́лнце</b> mặt trời · <b>со́лнечно</b> (trạng từ) trời nắng · '
    '<b>подсо́лнух</b> hoa hướng dương (nghĩa đen: cái dưới mặt trời) · <b>со́лнышко</b> '
    'mặt trời bé bỏng — cách gọi âu yếm người thân, y như "cục vàng" tiếng Việt</div>'
)

S["близкий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">близ-</span>'
    '<span class="hd-gloss">GẦN (<b>близ</b> cũng là một giới từ cổ: gần bên)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-ий</span>'
    '<span class="hd-gloss">hậu tố + đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không chỉ gần về khoảng cách mà còn <b>gần về tình cảm</b>: '
    '<b>бли́зкий друг</b> = bạn thân · <b>бли́зкие</b> (dùng như danh từ) = những người thân '
    'thiết. Tiếng Việt cũng gộp chung hai nghĩa đó — "gần gũi".</div>'
    '<div class="hd-warn"><b>Đừng lẫn với thẻ trạng từ bạn đã có:</b> <b>бли́зкий</b> đứng trước '
    'danh từ (bạn thân, người thân), còn <b>бли́зко</b> đi với động từ (đứng ở gần). '
    'Cùng gốc, chỉ khác đuôi: <b>-ий</b> tính từ, <b>-о</b> trạng từ.</div>'
    '<div class="hd-warn"><b>So sánh hơn:</b> <b>бли́же</b> (gần hơn) — <b>з</b> đổi thành '
    '<b>ж</b> đúng luật biến âm. Cặp đối: <b>бли́зкий</b> gần ↔ <b>далёкий</b> xa.</div>'
    '<div class="hd-sec">Họ hàng — gốc близ</div>'
    '<div class="hd-fam"><b>бли́зко</b> ở gần · <b>бли́зость</b> sự gần gũi · '
    '<b>прибли́зиться</b> tiến lại gần · <b>приблизи́тельно</b> xấp xỉ · '
    '<b>бли́жний</b> lân cận</div>'
)

S["весёлый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">весел-</span>'
    '<span class="hd-gloss">VUI, hớn hở</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Sắc thái quyết định: <b>весёлый</b> là <b>vui ra ngoài</b> — cười nói, '
    'hoạt náo, làm người khác cũng vui lây. Khác <b>счастли́вый</b> (hạnh phúc, sâu và lặng bên '
    'trong). Một người có thể счастли́вый mà không весёлый.</div>'
    '<div class="hd-warn"><b>Trọng âm:</b> chữ <b>ё</b> luôn mang trọng âm → <b>весёлый</b> nhấn '
    'ở <b>ё</b>. Nhưng dạng ngắn giống cái lại dời chỗ nhấn ra đuôi: <b>весела́</b>.</div>'
    '<div class="hd-sec">Họ hàng — gốc весел</div>'
    '<div class="hd-fam"><b>весе́лье</b> niềm vui, cuộc vui · <b>весели́ться</b> vui chơi · '
    '<b>ве́село</b> (trạng từ) vui vẻ · <b>развесели́ть</b> làm cho ai đó vui lên · '
    '<b>весельча́к</b> người vui tính</div>'
)

S["каждый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кажд-</span>'
    '<span class="hd-gloss">MỖI, từng cái một</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Về mặt hình thức nó là <b>tính từ</b> — hợp giống, hợp cách với danh từ '
    'đi sau, y như <b>но́вый</b>. Nên đừng coi nó là từ đặc biệt: biết chia tính từ là biết chia nó.</div>'
    '<div class="hd-warn"><b>Cụm chỉ thời gian dùng hằng ngày</b> — luôn ở <b>cách 4</b>: '
    '<b>ка́ждый день</b> mỗi ngày · <b>ка́ждую неде́лю</b> mỗi tuần · <b>ка́ждый год</b> mỗi năm · '
    '<b>ка́ждое у́тро</b> mỗi sáng.</div>'
    '<div class="hd-warn"><b>Phân biệt:</b> <b>ка́ждый</b> = mỗi, từng cái RIÊNG LẺ · '
    '<b>весь / все</b> = tất cả, GỘP CHUNG. <i>ка́ждый студе́нт</i> = từng sinh viên một; '
    '<i>все студе́нты</i> = toàn thể sinh viên.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">Gốc <b>кажд-</b> hầu như không đẻ ra từ phái sinh nào — nhưng ba từ này '
    'luôn đứng cùng chỗ với nó: <b>вся́кий</b> mọi loại, đủ thứ · <b>любо́й</b> bất kỳ cái nào '
    'cũng được · <b>все</b> tất cả (gộp chung)</div>'
)

S["слабый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">слаб-</span>'
    '<span class="hd-gloss">YẾU, lỏng lẻo</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Phủ khắp mọi kiểu "yếu", không chỉ sức người: <b>сла́бый чай</b> = '
    'trà nhạt · <b>сла́бый сигна́л</b> = sóng yếu · <b>сла́бый у́зел</b> = nút thắt lỏng.</div>'
    '<div class="hd-why">Nối với thứ bạn đã học: hậu tố <b>-ость</b> biến tính từ thành danh từ '
    '— <b>сла́бость</b> = sự yếu ớt, điểm yếu. Trọng âm đứng nguyên chỗ cũ.</div>'
    '<div class="hd-warn"><b>Cặp đối:</b> <b>сла́бый</b> yếu ↔ <b>си́льный</b> mạnh. So sánh hơn '
    'thì hiền, chỉ thêm <b>-ее</b>, không biến âm gì: <b>слабе́е</b> yếu hơn.</div>'
    '<div class="hd-sec">Họ hàng — gốc слаб</div>'
    '<div class="hd-fam"><b>сла́бость</b> điểm yếu, sự yếu ớt · <b>ослабе́ть</b> yếu đi · '
    '<b>слабе́ть</b> đang yếu dần · <b>слабе́е</b> yếu hơn</div>'
)

S["счастливый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">CÙNG, tốt lành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-часть-</span>'
    '<span class="hd-gloss">PHẦN, suất được chia</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лив-ый</span>'
    '<span class="hd-gloss">hậu tố "đầy, hay có" + đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen rất đẹp: <b>có được phần tốt của mình</b>. <b>сча́стье</b> = '
    '<b>с</b> (tốt) + <b>часть</b> (phần) — người Slav xưa hình dung vận may là <b>được chia phần</b>.</div>'
    '<div class="hd-why">Hậu tố <b>-ливый</b> đúng cái bạn gặp ở <b>дождли́вый</b>: "đầy, hay có". '
    'Счастли́вый = <b>đầy phần may</b>.</div>'
    '<div class="hd-warn"><b>Bẫy chính tả:</b> viết <b>сч</b> nhưng đọc như <b>щ</b> — "щас-ЛИ-вый", '
    'và chữ <b>т</b> câm hoàn toàn. Đừng bao giờ chép từ này theo tai.</div>'
    '<div class="hd-warn"><b>Câu chúc phải thuộc:</b> <b>Счастли́вого пути́!</b> = Thượng lộ bình an. '
    'Nghe suốt khi ai đó lên đường.</div>'
    '<div class="hd-sec">Họ hàng — gốc счаст</div>'
    '<div class="hd-fam"><b>сча́стье</b> hạnh phúc, vận may · <b>сча́стлив</b> (dạng ngắn) '
    'đang hạnh phúc · <b>несча́стье</b> bất hạnh, tai hoạ · <b>несчастли́вый</b> không may mắn</div>'
)


# --------------------------------------------------------------------------
# V — sửa field Vietnamese (§2c). Dòng này là ĐỀ BÀI của deck 1-go: user nhìn
# nó rồi GÕ từ Nga, nên phải sát tới mức chỉ có MỘT đáp án đúng.
# Ba cặp phải tách bạch trong lô này:
#   облачный (có mây, vẫn hửng nắng) ↔ пасмурный (xám kín, không thấy trời)
#   весёлый (vui ra ngoài)          ↔ счастливый (hạnh phúc bên trong)
#   близкий (TÍNH TỪ)               ↔ близко (TRẠNG TỪ, đã có thẻ riêng)
# Và ba chỗ nghĩa Việt cũ đang trùng với từ Nga KHÁC:
#   "bình thường" -> обычный · "tất cả" -> все · "tích cực" -> активный
# --------------------------------------------------------------------------

V["будничный"]     = "thuộc ngày thường phải đi làm; đều đều, tẻ nhạt"
V["ветреный"]      = "lộng gió, nhiều gió; (nói về người) nông nổi, hay thay đổi"
V["дождливый"]     = "mưa nhiều, mưa dai dẳng (nói về thời tiết, mùa)"
V["морозный"]      = "băng giá, rét dưới 0 độ (không phải \"lạnh\" nói chung)"
V["облачный"]      = "có mây, nhiều mây (trời vẫn hửng); (công nghệ) đám mây"
V["пасмурный"]     = "xám kín mây, âm u không thấy mặt trời; (mặt người) rầu rĩ"
V["положительный"] = "tích cực, khẳng định, dương (kết quả, câu trả lời)"
V["близкий"]       = "gần, thân thiết (bạn thân, người thân)"
V["весёлый"]       = "vui vẻ, tươi tắn, hoạt náo (vui ra ngoài)"
V["каждый"]        = "mỗi, từng cái một (riêng lẻ — không phải \"tất cả\" gộp chung)"
V["слабый"]        = "yếu, ốm yếu; nhạt (trà, màu); lỏng lẻo"
V["счастливый"]    = "hạnh phúc, may mắn (niềm vui sâu bên trong)"
