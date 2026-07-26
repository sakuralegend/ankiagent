# -*- coding: utf-8 -*-
"""LÔ 8 — field `HuongDan`: 17 TÍNH TỪ MÔ TẢ.

Ba hệ thống dạy kèm, dùng được rất xa:
  * SO SÁNH HƠN: -е + biến âm г/к/х → ж/ч/ш (близкий → ближе, узкий → уже)
    — chính là luật biến âm đã học ở lô thời tiết, nay hiện ra ở chỗ khác
  * DẠNG NGẮN: счастли́вый → сча́стлив — chỉ làm vị ngữ, thường chỉ trạng thái nhất thời
  * TÍNH TỪ HOÁ DANH TỪ: выходно́й, учёный — tính từ đứng một mình làm danh từ

Chạy: python data/huongdan/lo08_tinhtu_mota_2026-07-27.py [--apply]
"""
import json
import sys
import urllib.request

ANKI = "http://127.0.0.1:8765"

SOSANH = (
    '<div class="hd-sec">So sánh hơn — và luật biến âm quay lại</div>'
    '<div class="hd-why">Muốn nói "hơn" thì bỏ đuôi tính từ, thay bằng <b>-е</b> (hoặc <b>-ее</b>). '
    'Và phụ âm cuối gốc lại đổi mặt đúng như luật bạn đã gặp: <b>г→ж · к→ч · х→ш · з→ж · с→ш</b>.</div>'
    '<div class="hd-fam">бли́зкий gần → <b>бли́же</b> · у́зкий hẹp → <b>у́же</b> · '
    'широ́кий rộng → <b>ши́ре</b> · дорого́й đắt → <b>доро́же</b> · высо́кий cao → <b>вы́ше</b></div>'
    '<div class="hd-why">Tính từ "hiền" hơn thì chỉ cần <b>-ее</b>, không biến âm gì: '
    '<b>сла́бый</b> → <b>слабе́е</b> · <b>интере́сный</b> → <b>интере́снее</b>.</div>'
    '<div class="hd-why">Dạng so sánh này <b>không biến đổi</b> theo giống hay cách — đó là chỗ dễ, '
    'bù cho chỗ khó là phải nhớ biến âm.</div>'
)

NGAN = (
    '<div class="hd-sec">Dạng ngắn — thứ tiếng Việt không có</div>'
    '<div class="hd-why">Tính từ Nga có hai bộ mặt. <b>Dạng dài</b> (счастли́вый) đứng trước danh từ '
    'để mô tả nó. <b>Dạng ngắn</b> (сча́стлив) chỉ làm <b>vị ngữ</b> — "anh ấy ĐANG hạnh phúc".</div>'
    '<div class="hd-row"><span class="hd-piece">dài</span>'
    '<span class="hd-gloss">счастли́вый челове́к = một người hạnh phúc (thuộc tính lâu dài)</span></div>'
    '<div class="hd-row"><span class="hd-piece">ngắn</span>'
    '<span class="hd-gloss">Он сча́стлив = anh ấy đang hạnh phúc (trạng thái lúc này)</span></div>'
    '<div class="hd-why">Dạng ngắn đổi theo giống và số, KHÔNG đổi theo cách: '
    '<b>сча́стлив</b> (đực) · <b>сча́стлива</b> (cái) · <b>сча́стливо</b> (trung) · <b>сча́стливы</b> (nhiều).</div>'
)

S = {}

# ---------- Cặp đối lập: học đôi rẻ hơn học lẻ ----------

S["узкий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">уз-</span><span class="hd-gloss">HẸP, thắt lại — cùng gốc <b>у́зел</b> (nút thắt)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-ий</span><span class="hd-gloss">hậu tố + đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>уз-</b> mang ý <b>thắt lại</b>, nên nó sinh ra cả <b>у́зкий</b> (hẹp) lẫn <b>у́зел</b> (nút thắt) và <b>сою́з</b> (liên minh — cái buộc chung lại). Ba từ, một hình ảnh.</div>'
    '<div class="hd-warn"><b>BẪY TRỌNG ÂM chết người:</b> <b>у́же</b> (nhấn đầu) = hẹp hơn · <b>уже́</b> (nhấn cuối) = <b>đã, rồi</b>. Cùng mặt chữ, khác hẳn nghĩa và từ loại. Đây là lý do dấu trọng âm không phải trang trí.</div>'
    '<div class="hd-warn"><b>Cặp đối:</b> <b>у́зкий</b> hẹp ↔ <b>широ́кий</b> rộng. Học chung một chỗ.</div>'
    + SOSANH
)

S["широкий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">широ-</span><span class="hd-gloss">RỘNG (<b>ширина́</b> = chiều rộng)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-ий</span><span class="hd-gloss">hậu tố + đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dạng so sánh <b>ши́ре</b> đáng chú ý: nó vừa rụng hậu tố <b>-к-</b> vừa <b>kéo trọng âm về đầu</b> — широ́кий (nhấn giữa) → ши́ре (nhấn đầu). Cùng khuôn với <b>высо́кий → вы́ше</b>.</div>'
    '<div class="hd-why">Nghĩa bóng dùng nhiều: <b>широ́кая душа́</b> = tấm lòng rộng rãi — một lời khen rất Nga, chỉ người hào phóng và chân thành.</div>'
    '<div class="hd-sec">Họ hàng — gốc шир</div>'
    '<div class="hd-fam"><b>ширина́</b> chiều rộng · <b>расширя́ть</b> mở rộng · <b>вширь</b> theo chiều rộng</div>'
    + SOSANH
)

S["близкий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">близ-</span><span class="hd-gloss">GẦN (<b>близ</b> cũng là một giới từ cổ: gần bên)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-ий</span><span class="hd-gloss">hậu tố + đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa không chỉ là gần về khoảng cách mà còn <b>gần về tình cảm</b>: <b>бли́зкий друг</b> = bạn thân · <b>бли́зкие</b> (danh từ hoá) = những người thân thiết. Hai nghĩa này tiếng Việt cũng gộp chung — "gần gũi".</div>'
    '<div class="hd-warn"><b>So sánh:</b> <b>бли́же</b> (з→ж). Và bạn đã có sẵn thẻ trạng từ <b>бли́зко</b> (ở gần) — cùng gốc, chỉ khác đuôi: <b>-ий</b> tính từ, <b>-о</b> trạng từ.</div>'
    '<div class="hd-warn"><b>Cặp đối:</b> <b>бли́зкий</b> gần ↔ <b>далёкий</b> xa.</div>'
    '<div class="hd-sec">Họ hàng — gốc близ</div>'
    '<div class="hd-fam"><b>бли́зко</b> ở gần · <b>прибли́зиться</b> tiến lại gần · <b>приблизи́тельно</b> xấp xỉ · <b>бли́жний</b> lân cận</div>'
    + SOSANH
)

# ---------- Chùm chẻ ra lộ nghĩa bất ngờ ----------

S["богатый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бог-</span><span class="hd-gloss">Бог — THẦN, THƯỢNG ĐẾ; nghĩa cổ hơn: PHẦN ĐƯỢC CHIA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ат-ый</span><span class="hd-gloss">hậu tố "có nhiều" + đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc gây bất ngờ: <b>giàu</b> nghĩa đen là <b>được thần ban phần</b>. Nghĩa cổ nhất của <b>бог</b> không phải "thần" mà là <b>phần của cải được chia</b> — giàu tức là được chia nhiều.</div>'
    '<div class="hd-why">Chứng cứ nằm ngay trong từ trái nghĩa: <b>убо́гий</b> (nghèo hèn, thảm hại) = <b>у-</b> (mất, không có) + <b>бог</b> = <b>không có phần</b>. Hai từ soi sáng nhau.</div>'
    '<div class="hd-warn">⚠️ Mức tin: đây là <b>từ nguyên</b>. Người Nga hôm nay dùng <b>бога́тый</b> hoàn toàn đời thường, không cảm thấy chút nghĩa tôn giáo nào.</div>'
    '<div class="hd-sec">Họ hàng — gốc бог</div>'
    '<div class="hd-fam"><b>бога́тство</b> sự giàu có · <b>богате́ть</b> giàu lên · <b>убо́гий</b> nghèo hèn · <b>спаси́бо</b> cảm ơn (rút từ <i>спаси Бог</i> = cầu Chúa cứu độ!)</div>'
)

S["счастливый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span><span class="hd-gloss">CÙNG, tốt lành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-часть-</span><span class="hd-gloss">PHẦN, suất được chia</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лив-ый</span><span class="hd-gloss">hậu tố "đầy, hay có" + đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen tuyệt đẹp: <b>có được phần tốt của mình</b>. <b>сча́стье</b> = <b>с</b> (tốt) + <b>часть</b> (phần) — hạnh phúc là nhận đúng phần mình đáng được. Cùng ý với <b>бога́тый</b> ở trên: người Slav xưa hình dung vận may là <b>được chia phần</b>.</div>'
    '<div class="hd-why">Hậu tố <b>-ливый</b> đúng cái bạn đã gặp ở <b>дождли́вый</b>: "đầy, hay có". Счастли́вый = <b>đầy phần may</b>.</div>'
    '<div class="hd-warn"><b>Bẫy phát âm:</b> viết <b>сч</b> nhưng đọc là <b>щ</b> — "щас-ЛИ-вый", và chữ <b>т</b> câm hoàn toàn. Đừng bao giờ chép chính tả từ cái tai nghe được ở từ này.</div>'
    '<div class="hd-warn"><b>Câu chúc phải thuộc:</b> <b>Счастли́вого пути́!</b> = Thượng lộ bình an. Nghe suốt khi ai đó lên đường.</div>'
    + NGAN
)

S["весёлый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">весел-</span><span class="hd-gloss">VUI, hớn hở</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span><span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Sắc thái quan trọng: <b>весёлый</b> là <b>vui vẻ ồn ào, tươi tắn ra ngoài</b> — cười nói, hoạt náo. Khác <b>сча́стливый</b> (hạnh phúc, sâu và lặng bên trong). Một người có thể счастливый mà không весёлый.</div>'
    '<div class="hd-warn"><b>Nhắc lại luật quà tặng:</b> <b>ё</b> luôn mang trọng âm → <b>весёлый</b> nhấn ở <b>ё</b>. Nhưng dạng ngắn giống cái lại đổi chỗ nhấn: <b>весела́</b>.</div>'
    '<div class="hd-sec">Họ hàng — gốc весел</div>'
    '<div class="hd-fam"><b>весе́лье</b> niềm vui, cuộc vui · <b>весели́ться</b> vui chơi · <b>ве́село</b> (trạng từ) vui vẻ · <b>развлека́ться</b> giải trí</div>'
    + NGAN
)

S["выходной"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span><span class="hd-gloss">RA, ra ngoài</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ход-</span><span class="hd-gloss">ĐI BỘ (cùng gốc <b>ходи́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ой</span><span class="hd-gloss">hậu tố + đuôi tính từ (nhấn ở đuôi)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>thuộc về việc đi ra</b> — ngày người ta ra khỏi nhà đi chơi, tức là <b>ngày nghỉ</b>.</div>'
    '<div class="hd-sec">Tính từ hoá danh từ — một nét rất Nga</div>'
    '<div class="hd-why">Đầy đủ phải là <b>выходно́й день</b> (ngày nghỉ), nhưng người ta lược mất <b>день</b>, để tính từ đứng một mình làm danh từ. Rất nhiều từ Nga sinh ra kiểu đó.</div>'
    '<div class="hd-fam"><b>выходно́й</b> ngày nghỉ · <b>учёный</b> nhà khoa học · <b>больно́й</b> bệnh nhân · <b>столо́вая</b> nhà ăn · <b>ва́нная</b> phòng tắm · <b>моро́женое</b> kem</div>'
    '<div class="hd-warn"><b>Dấu hiệu nhận biết:</b> chúng vẫn <b>biến cách như TÍNH TỪ</b>, không như danh từ. Thấy một "danh từ" có đuôi <b>-ый/-ой/-ая/-ое</b> thì gần như chắc là loại này.</div>'
    '<div class="hd-sec">Họ hàng — gốc ход</div>'
    '<div class="hd-fam"><b>ходи́ть</b> đi bộ · <b>вы́ход</b> lối ra · <b>вход</b> lối vào · <b>выходны́е</b> (số nhiều) cuối tuần</div>'
)

S["учёный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">уч-</span><span class="hd-gloss">DẠY / HỌC — gốc bạn đã gặp ở <b>учи́ться</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ён-ый</span><span class="hd-gloss">đuôi phân từ bị động: "đã được…"</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>người đã được dạy</b>. Vốn là một phân từ (dạng động từ), rồi đông cứng lại thành danh từ = <b>nhà khoa học, học giả</b>. Đúng kiểu tính từ hoá danh từ như <b>выходно́й</b>.</div>'
    '<div class="hd-why">Nó vẫn còn dùng được như tính từ thật: <b>учёная сте́пень</b> = học vị.</div>'
    '<div class="hd-warn"><b>ё luôn nhấn</b> → <b>учёный</b>. Và đừng lẫn với <b>учени́к</b> (học trò) hay <b>учи́тель</b> (thầy giáo) — cùng gốc <b>уч-</b> nhưng ba vai khác nhau.</div>'
    '<div class="hd-sec">Họ hàng — gốc уч</div>'
    '<div class="hd-fam"><b>учи́ть</b> dạy · <b>учи́ться</b> học · <b>учи́тель</b> thầy giáo · <b>учени́к</b> học trò · <b>учёный</b> nhà khoa học · <b>нау́ка</b> khoa học · <b>уче́бник</b> sách giáo khoa</div>'
)

# ---------- Chùm -ный từ danh từ ----------

S["интересный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">интерес-</span><span class="hd-gloss">интере́с — SỰ QUAN TÂM (<i>interest</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span><span class="hd-gloss">hậu tố + đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ quốc tế, bạn đã biết nghĩa. Việc phải học chỉ là <b>trọng âm rơi vào -ре́с-</b>, khác tiếng Anh (<i>INterest</i>).</div>'
    '<div class="hd-warn"><b>Cấu trúc rất hay dùng:</b> <b>Мне интере́сно</b> = Tôi thấy thú vị. Tiếng Nga nói "đối với tôi thì thú vị" — dùng <b>cách 3</b> (мне) chứ không dùng "tôi" làm chủ ngữ. Khuôn này lặp lại khắp nơi: <b>мне ску́чно</b> tôi chán · <b>мне хо́лодно</b> tôi lạnh.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>интере́с</b> sự quan tâm · <b>интересова́ться</b> quan tâm tới · <b>неинтере́сный</b> nhạt nhẽo</div>'
)

S["неинтересный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не-</span><span class="hd-gloss">KHÔNG — tiền tố phủ định</span></div>'
    '<div class="hd-row"><span class="hd-piece">интерес-</span><span class="hd-gloss">интере́с — sự quan tâm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span><span class="hd-gloss">hậu tố + đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là <b>cỗ máy nhân đôi vốn từ</b> của bạn: dán <b>не-</b> vào là có ngay từ trái nghĩa, không phải học từ mới nào cả.</div>'
    '<div class="hd-fam"><b>большо́й</b> to → <b>небольшо́й</b> nhỏ · <b>дорого́й</b> đắt → <b>недорого́й</b> rẻ · <b>пра́вильный</b> đúng → <b>непра́вильный</b> sai · <b>возмо́жный</b> có thể → <b>невозмо́жный</b> bất khả</div>'
    '<div class="hd-warn"><b>Luật viết liền hay rời:</b> khi <b>не-</b> tạo ra một từ mới có nghĩa riêng thì <b>viết LIỀN</b> (неинтере́сный = nhạt nhẽo). Khi nó phủ định để đối chiếu thì viết <b>RỜI</b>: <i>не интере́сный, а ску́чный</i> = không phải thú vị, mà là chán. Sắc thái khác nhau.</div>'
)

S["модный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мод-</span><span class="hd-gloss">мо́да — THỜI TRANG, mốt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span><span class="hd-gloss">hậu tố + đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ quốc tế qua tiếng Pháp <i>mode</i> — tiếng Việt cũng mượn đúng từ đó thành <b>"mốt"</b>. Bạn đã biết sẵn, chỉ cần nhớ mặt chữ.</div>'
    '<div class="hd-why">Đây cũng là mẫu sạch nhất của luật <b>danh từ + -ный = tính từ</b>: <b>мо́да → мо́дный</b>, không biến âm, không thêm bớt.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мо́да</b> thời trang · <b>мо́дный</b> hợp mốt · <b>моде́ль</b> người mẫu; mô hình</div>'
)

S["скучный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">скуч-</span><span class="hd-gloss">ску́ка — SỰ BUỒN CHÁN (<b>к</b> đã mềm thành <b>ч</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span><span class="hd-gloss">hậu tố + đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lại một lần nữa luật <b>к → ч</b>: <b>ску́ка</b> → <b>ску́чный</b>, y như <b>о́блако → о́блачный</b>.</div>'
    '<div class="hd-warn"><b>BẪY PHÁT ÂM nổi tiếng:</b> cụm <b>чн</b> ở đây đọc thành <b>шн</b> — "SKUSH-ny". Đây là một nhóm nhỏ từ giữ cách đọc cổ, đáng thuộc cả cụm: <b>ску́чно</b> · <b>коне́чно</b> (dĩ nhiên) → "kaNESHna" · <b>что</b> → "shto". Ngoài nhóm này thì <b>чн</b> vẫn đọc bình thường.</div>'
    '<div class="hd-warn"><b>Cấu trúc:</b> <b>Мне ску́чно</b> = Tôi chán. Cùng khuôn "cách 3 + trạng từ" với <b>мне интере́сно</b>.</div>'
    '<div class="hd-sec">Họ hàng — gốc скук/скуч</div>'
    '<div class="hd-fam"><b>ску́ка</b> sự buồn chán · <b>скуча́ть</b> buồn chán; nhớ ai đó · <b>Я скуча́ю по тебе́</b> tôi nhớ bạn</div>'
)

S["слабый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">слаб-</span><span class="hd-gloss">YẾU, lỏng lẻo</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span><span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Phủ khắp mọi kiểu "yếu": người yếu sức, ánh sáng yếu, trà loãng, tín hiệu kém — <b>сла́бый чай</b> = trà nhạt, <b>сла́бый сигна́л</b> = sóng yếu.</div>'
    '<div class="hd-why">Nối với thứ bạn đã học: hậu tố <b>-ость</b> biến nó thành danh từ — <b>сла́бость</b> = điểm yếu, sự yếu ớt. Trọng âm giữ nguyên chỗ cũ.</div>'
    '<div class="hd-warn"><b>Cặp đối:</b> <b>сла́бый</b> yếu ↔ <b>си́льный</b> mạnh.</div>'
    '<div class="hd-sec">Họ hàng — gốc слаб</div>'
    '<div class="hd-fam"><b>сла́бость</b> điểm yếu · <b>ослабе́ть</b> yếu đi · <b>слабе́е</b> yếu hơn</div>'
    + SOSANH + NGAN
)

S["острый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">остр-</span><span class="hd-gloss">NHỌN, SẮC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span><span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một gốc, ba nghĩa toả ra từ đúng một hình ảnh <b>mũi nhọn</b>: dao <b>sắc</b> · món ăn <b>cay</b> (vị đâm vào lưỡi) · trí óc <b>sắc sảo</b>. Tiếng Việt cũng nói "lời nói sắc", nên hình ảnh này bạn đã quen.</div>'
    '<div class="hd-why">Họ hàng Ấn–Âu xa: Latin <i>acer</i> (nhọn, gắt) → tiếng Anh <i>acute</i>, <i>acrid</i>. Cùng một gốc cổ nghĩa "nhọn".</div>'
    '<div class="hd-warn"><b>Rất thực dụng khi gọi món:</b> <b>о́строе блю́до</b> = món cay. Bạn có sẵn thẻ <b>блю́до</b> — ghép hai từ lại là dùng được ngay.</div>'
    '<div class="hd-sec">Họ hàng — gốc остр</div>'
    '<div class="hd-fam"><b>остриё</b> mũi nhọn · <b>обостри́ть</b> làm gay gắt thêm · <b>о́стров</b> hòn đảo (mũi đất nhô ra)</div>'
)

S["домашний"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дом-</span><span class="hd-gloss">дом — NHÀ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ашн-</span><span class="hd-gloss">hậu tố tính từ dạng MỀM</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span><span class="hd-gloss">đuôi tính từ mềm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thấy <b>дом</b> là ra nghĩa: thuộc về nhà, tự làm ở nhà. <b>дома́шняя еда́</b> = cơm nhà · <b>дома́шние живо́тные</b> = vật nuôi.</div>'
    '<div class="hd-warn"><b>TÍNH TỪ MỀM — một lớp riêng phải biết:</b> phần lớn tính từ Nga đuôi cứng <b>-ый/-ой</b>, nhưng có một nhóm nhỏ đuôi <b>MỀM -ний</b> và biến cách hơi khác. Đáng thuộc cả nhóm: <b>дома́шний</b> · <b>си́ний</b> xanh dương · <b>ле́тний</b> mùa hè · <b>после́дний</b> cuối cùng · <b>сего́дняшний</b> của hôm nay.</div>'
    '<div class="hd-warn"><b>Cụm phải thuộc:</b> <b>дома́шнее зада́ние</b> = bài tập về nhà. Người Nga hay gọi tắt là <b>дома́шка</b>.</div>'
    '<div class="hd-sec">Họ hàng — gốc дом</div>'
    '<div class="hd-fam"><b>дом</b> nhà · <b>до́ма</b> ở nhà · <b>домо́й</b> về nhà · <b>дома́шний</b> thuộc về nhà · <b>хозя́йка</b> bà chủ nhà</div>'
)

# ---------- Chùm đại từ - tính từ ----------

S["каждый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кажд-</span><span class="hd-gloss">MỖI, từng cái một</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span><span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Về mặt hình thức nó là <b>tính từ</b> — hợp giống, hợp cách với danh từ đi sau, y như <b>но́вый</b>. Nên đừng coi nó là từ đặc biệt: biết chia tính từ là biết chia nó.</div>'
    '<div class="hd-warn"><b>Cụm chỉ thời gian bạn dùng hằng ngày</b> — luôn ở <b>cách 4</b>: <b>ка́ждый день</b> mỗi ngày · <b>ка́ждую неде́лю</b> mỗi tuần · <b>ка́ждый год</b> mỗi năm · <b>ка́ждое у́тро</b> mỗi sáng.</div>'
    '<div class="hd-warn"><b>Phân biệt:</b> <b>ка́ждый</b> = mỗi (từng cái riêng lẻ) · <b>весь / все</b> = tất cả (gộp chung). <i>ка́ждый студе́нт</i> = từng sinh viên một; <i>все студе́нты</i> = toàn thể sinh viên.</div>'
)

S["некоторый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не-</span><span class="hd-gloss">tiền tố — ở đây KHÔNG phủ định, mà làm thành từ PHIẾM CHỈ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-котор-</span><span class="hd-gloss">кото́рый — CÁI NÀO, người mà</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span><span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là một cơ chế rất gọn của tiếng Nga: dán <b>не-</b> vào từ để hỏi thì được từ <b>phiếm chỉ</b> — "không rõ là cái nào" = <b>một vài, nào đó</b>. Nghe ngược đời nhưng cực kỳ đều đặn.</div>'
    '<div class="hd-fam"><b>кто</b> ai → <b>не́кто</b> một ai đó · <b>что</b> gì → <b>не́что</b> một cái gì đó · <b>ско́лько</b> bao nhiêu → <b>не́сколько</b> một vài · <b>когда́</b> khi nào → <b>не́когда</b> có thời, xưa kia</div>'
    '<div class="hd-warn"><b>Trọng âm là chìa khoá:</b> ở nhóm này <b>не-</b> LUÔN mang trọng âm — <b>не́который, не́сколько, не́кто</b>. Chính chỗ nhấn đó phân biệt chúng với <b>не</b> phủ định (không nhấn).</div>'
    '<div class="hd-warn">Nghĩa dùng thật: <b>не́которые студе́нты</b> = một số sinh viên · <b>в не́котором смы́сле</b> = theo một nghĩa nào đó.</div>'
)


# ---------------------------------------------------------------------------
def ac(action, **params):
    req = urllib.request.Request(
        ANKI, json.dumps({"action": action, "version": 6, "params": params}).encode())
    out = json.load(urllib.request.urlopen(req, timeout=180))
    if out.get("error"):
        raise RuntimeError(f"{action}: {out['error']}")
    return out["result"]


def main():
    apply = "--apply" in sys.argv
    ok, miss = [], []
    for word, html in S.items():
        ids = ac("findNotes", query=f'note:RU_Word WordClean:{word}')
        if len(ids) != 1:
            miss.append((word, len(ids)))
            continue
        if apply:
            ac("updateNoteFields", note={"id": ids[0], "fields": {"HuongDan": html}})
        ok.append(word)
    print(f"khop: {len(ok)}/{len(S)}")
    for w, n in miss:
        print(f"  !! {w}: tim thay {n} note")
    if apply:
        print("da ghi. sync:", ac("sync"))
    else:
        print("(chua ghi gi — them --apply de ghi that)")


if __name__ == "__main__":
    main()
