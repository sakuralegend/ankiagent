# -*- coding: utf-8 -*-
"""LÔ 12 — field `HuongDan`: 14 TRẠNG TỪ và TỪ CHỨC NĂNG (lô cuối của hai deck học).

Hai hệ thống trục:
  * TÍNH TỪ → TRẠNG TỪ bằng `-о`: бли́зкий→бли́зко, пра́вильный→пра́вильно.
    Một luật, và nó nhân đôi vốn từ mà không phải học thêm chữ nào.
  * CÁCH 5 LÀM TRẠNG TỪ THỜI GIAN: ве́чером, у́тром, днём, но́чью —
    không phải từ riêng, chỉ là danh từ chia ở cách 5.

Chạy: python data/huongdan/lo12_trangtu_2026-07-27.py [--apply]
"""
import json
import sys
import urllib.request

ANKI = "http://127.0.0.1:8765"

TRANGTU = (
    '<div class="hd-sec">Tính từ → trạng từ: đổi đuôi thành -о</div>'
    '<div class="hd-why">Luật rẻ nhất tiếng Nga: lấy tính từ, thay đuôi bằng <b>-о</b>, xong. '
    'Trạng từ <b>không biến đổi</b> gì cả — không giống, không cách, không số.</div>'
    '<div class="hd-fam">бли́зкий gần → <b>бли́зко</b> · пра́вильный đúng → <b>пра́вильно</b> · '
    'отли́чный xuất sắc → <b>отли́чно</b> · ча́стый thường xuyên → <b>ча́сто</b> · '
    'бы́стрый nhanh → <b>бы́стро</b> · хоро́ший tốt → <b>хорошо́</b></div>'
    '<div class="hd-warn"><b>Khuôn câu cực hay dùng — "cách 3 + trạng từ":</b> tiếng Nga nói cảm giác '
    'bằng cách "đối với ai thì thế nào", chứ không lấy người làm chủ ngữ. '
    '<b>Мне хо́лодно</b> tôi lạnh · <b>Мне ску́чно</b> tôi chán · <b>Мне интере́сно</b> tôi thấy thú vị.</div>'
)

CACH5 = (
    '<div class="hd-sec">Cách 5 làm trạng từ thời gian</div>'
    '<div class="hd-why">Bốn buổi trong ngày KHÔNG phải bốn từ riêng phải học — chúng chỉ là danh từ '
    'thường, chia ở <b>cách 5</b>. Biết vậy thì khỏi học thuộc bảng.</div>'
    '<div class="hd-fam"><b>у́тро</b> buổi sáng → <b>у́тром</b> vào buổi sáng · '
    '<b>день</b> ban ngày → <b>днём</b> · <b>ве́чер</b> buổi tối → <b>ве́чером</b> · '
    '<b>ночь</b> đêm → <b>но́чью</b></div>'
    '<div class="hd-why">Cùng khuôn cho mùa: <b>зимо́й</b> vào mùa đông · <b>ле́том</b> mùa hè · '
    '<b>весно́й</b> mùa xuân · <b>о́сенью</b> mùa thu. Một luật, tám từ.</div>'
)

S = {}

# ---------- Trạng từ từ tính từ ----------

S["близко"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">близ-</span><span class="hd-gloss">GẦN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-о</span><span class="hd-gloss">hậu tố + đuôi TRẠNG TỪ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Là <b>бли́зкий</b> (mà bạn đã có thẻ) đổi đuôi <b>-ий</b> thành <b>-о</b>. Hai thẻ này là một cặp: tính từ tả danh từ, trạng từ tả động từ.</div>'
    '<div class="hd-warn"><b>Dùng thật:</b> <b>Э́то бли́зко</b> = Chỗ đó gần thôi · <b>бли́зко от до́ма</b> = gần nhà. Muốn nói "gần cái gì" thì dùng <b>от</b> + cách 2.</div>'
    '<div class="hd-warn"><b>So sánh vẫn là бли́же</b> — dạng so sánh dùng chung cho CẢ tính từ lẫn trạng từ, không phải nhớ hai lần.</div>'
    + TRANGTU
)

S["правильно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">прав-</span><span class="hd-gloss">ĐÚNG, thẳng, phải</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ильн-</span><span class="hd-gloss">hậu tố tính từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span><span class="hd-gloss">đuôi TRẠNG TỪ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>прав-</b> là một trong những gốc <b>giàu nhất</b> tiếng Nga, và nó gom vào một chỗ ba ý mà tiếng Việt cũng gom: <b>bên phải</b> · <b>đúng đắn</b> · <b>quyền</b>. Ta nói "lẽ phải", "bên phải", "có quyền" — cùng một chữ "phải".</div>'
    '<div class="hd-warn"><b>Dùng thật mỗi ngày:</b> <b>Пра́вильно!</b> = Đúng rồi! — câu thầy cô nói khi bạn trả lời trúng. Và <b>непра́вильно</b> = sai (thêm <b>не-</b>, đúng cỗ máy nhân đôi vốn từ).</div>'
    '<div class="hd-sec">Họ hàng — gốc прав (rất lớn)</div>'
    '<div class="hd-fam"><b>пра́вда</b> sự thật · <b>пра́во</b> quyền · <b>пра́вый</b> bên phải; đúng · <b>пра́вило</b> quy tắc · <b>прави́тельство</b> chính phủ · <b>испра́вить</b> sửa cho đúng</div>'
    + TRANGTU
)

S["отлично"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span><span class="hd-gloss">RỜI RA, tách khỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лич-</span><span class="hd-gloss">MẶT, diện mạo — cùng gốc <b>лицо́</b> (khuôn mặt)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-о</span><span class="hd-gloss">hậu tố + đuôi trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>khác mặt hẳn ra</b> — nổi bật khỏi đám đông. Từ "khác biệt" mà thành "xuất sắc". Tiếng Anh đi đúng đường: <i>distinguished</i> ← <i>distinguish</i> (phân biệt).</div>'
    '<div class="hd-warn"><b>Đây là ĐIỂM SỐ cao nhất ở Nga:</b> thang điểm Nga là 5 bậc, và <b>отли́чно</b> = điểm 5 = giỏi xuất sắc. Học sinh giỏi gọi là <b>отли́чник</b>. Dưới nó là <b>хорошо́</b> (4), <b>удовлетвори́тельно</b> (3).</div>'
    '<div class="hd-warn">Trong hội thoại, <b>Отли́чно!</b> = "Tuyệt vời!" — dùng như tiếng Việt "Ngon!", rất thông dụng.</div>'
    '<div class="hd-sec">Họ hàng — gốc лиц/лич</div>'
    '<div class="hd-fam"><b>лицо́</b> khuôn mặt · <b>ли́чный</b> cá nhân · <b>отлича́ть</b> phân biệt · <b>разли́чие</b> sự khác biệt · <b>отли́чник</b> học sinh giỏi</div>'
    + TRANGTU
)

S["часто"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">част-</span><span class="hd-gloss">DÀY, sít nhau (<b>ча́стый</b> = dày đặc, thường xuyên)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span><span class="hd-gloss">đuôi TRẠNG TỪ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa lõi là <b>DÀY</b> — các lần xảy ra sít vào nhau thì gọi là "thường xuyên". Cùng một hình ảnh, tiếng Nga dùng <b>ча́стый лес</b> (rừng rậm, cây mọc dày) và <b>ча́сто</b> (thường xuyên).</div>'
    '<div class="hd-warn"><b>Cặp đối:</b> <b>ча́сто</b> thường xuyên ↔ <b>ре́дко</b> hiếm khi. Và mức giữa: <b>иногда́</b> = đôi khi (nhớ chưa: <b>ино-</b> = khác + <b>когда</b> = khi nào → "vào lúc khác").</div>'
    '<div class="hd-warn"><b>Vị trí trong câu:</b> trạng từ tần suất đứng <b>trước động từ</b> — <i>Я ча́сто чита́ю</i> = Tôi hay đọc sách.</div>'
    + TRANGTU
)

# ---------- Trạng từ dựng từ giới từ + danh từ ----------

S["вечером"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вечер-</span><span class="hd-gloss">ве́чер — BUỔI TỐI (danh từ)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ом</span><span class="hd-gloss">đuôi CÁCH 5 giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây <b>không phải từ mới</b> — chỉ là danh từ <b>ве́чер</b> chia ở cách 5. Cách 5 vốn nghĩa "bằng, nhờ", dùng cho thời gian thì thành "vào lúc đó".</div>'
    '<div class="hd-why">Nhận ra điều này thì bạn được luôn tám từ mà không phải học thêm chữ nào — xem bảng dưới.</div>'
    '<div class="hd-warn"><b>Không cần giới từ:</b> nói <b>ве́чером</b> là đủ, KHÔNG thêm <b>в</b>. Sai phổ biến của người mới: <i>*в вечером</i>.</div>'
    '<div class="hd-sec">Họ hàng — gốc вечер</div>'
    '<div class="hd-fam"><b>ве́чер</b> buổi tối · <b>ве́чером</b> vào buổi tối · <b>вече́рний</b> thuộc buổi tối · <b>вчера́</b> hôm qua (cùng gốc cổ: "buổi tối vừa rồi"!)</div>'
    + CACH5
)

S["вслух"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span><span class="hd-gloss">giới từ <b>в</b> (vào) đã dính liền</span></div>'
    '<div class="hd-row"><span class="hd-piece">-слух</span><span class="hd-gloss">слух — THÍNH GIÁC, sự nghe</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>vào chỗ nghe được</b> = <b>đọc to lên</b>. Đây là kiểu trạng từ dựng bằng cách <b>dính liền giới từ với danh từ</b> — rất nhiều trạng từ Nga sinh ra như vậy.</div>'
    '<div class="hd-fam"><b>вме́сте</b> cùng nhau (в + ме́сто chỗ) · <b>вниз</b> xuống dưới (в + низ) · <b>наверху́</b> ở trên (на + верх) · <b>сра́зу</b> ngay lập tức (с + раз)</div>'
    '<div class="hd-warn"><b>Cặp động từ phải phân biệt cho rõ:</b> <b>слы́шать</b> = NGHE THẤY (tai bắt được, không chủ ý) · <b>слу́шать</b> = LẮNG NGHE (có chủ ý). Đúng như <i>hear</i> ↔ <i>listen</i>. Cùng gốc <b>слух</b> nhưng khác hẳn cách dùng.</div>'
    '<div class="hd-warn"><b>Dùng thật:</b> <b>чита́ть вслух</b> = đọc thành tiếng — chính là việc thẻ giai đoạn 1 của bạn bảo làm.</div>'
    '<div class="hd-sec">Họ hàng — gốc слух/слыш</div>'
    '<div class="hd-fam"><b>слух</b> thính giác; tin đồn · <b>слы́шать</b> nghe thấy · <b>слу́шать</b> lắng nghe · <b>слу́шатель</b> thính giả</div>'
)

S["позавчера"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span><span class="hd-gloss">tiền tố</span></div>'
    '<div class="hd-row"><span class="hd-piece">-за-</span><span class="hd-gloss">PHÍA SAU, lùi thêm một bậc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вчера</span><span class="hd-gloss">вчера́ — HÔM QUA</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>lùi ra sau hôm qua</b> = hôm kia. Chẻ ra thì không cần nhớ gì thêm — bạn đã biết <b>вчера́</b> rồi.</div>'
    '<div class="hd-why">Có từ đối xứng hoàn hảo ở đầu kia trục thời gian: <b>послеза́втра</b> = <b>по́сле</b> (sau) + <b>за́втра</b> (ngày mai) = <b>ngày kia</b>. Học một cặp là phủ được năm ngày liền.</div>'
    '<div class="hd-fam"><b>позавчера́</b> hôm kia · <b>вчера́</b> hôm qua · <b>сего́дня</b> hôm nay · <b>за́втра</b> ngày mai · <b>послеза́втра</b> ngày kia</div>'
    '<div class="hd-warn"><b>Bẫy trọng âm:</b> nhấn ở âm tiết CUỐI — <b>позавчера́</b>, y như <b>вчера́</b>. Từ càng dài càng dễ nhấn nhầm về đầu.</div>'
)

S["час"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ <b>gốc trơn</b> một âm tiết, giống đực. Nghĩa: <b>giờ</b> (đơn vị 60 phút).</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-warn"><b>Từ quan trọng nhất mọc ra từ đây:</b> <b>сейча́с</b> (bây giờ) = <b>сей</b> (này — đại từ cổ) + <b>час</b> (giờ) = <b>"giờ này"</b>. Đây là một trong những từ bạn dùng nhiều nhất, và giờ nó chẻ được.</div>'
    '<div class="hd-warn"><b>BẪY SỐ NHIỀU đổi nghĩa:</b> <b>час</b> = giờ, nhưng <b>часы́</b> (số nhiều) = <b>CÁI ĐỒNG HỒ</b>. Cùng nhóm "chỉ có số nhiều" với <b>де́ньги</b>, <b>очки́</b>, <b>щи</b> mà bạn đã gặp.</div>'
    '<div class="hd-warn"><b>Đếm giờ — bẫy ngữ pháp kinh điển:</b> <b>1 час</b> · <b>2, 3, 4 часа́</b> (cách 2 số ít) · <b>5–20 часо́в</b> (cách 2 số nhiều). Con số quyết định đuôi danh từ — luật này áp cho MỌI danh từ đếm được trong tiếng Nga.</div>'
    '<div class="hd-sec">Họ hàng — gốc час</div>'
    '<div class="hd-fam"><b>час</b> giờ · <b>часы́</b> đồng hồ · <b>сейча́с</b> bây giờ · <b>часово́й</b> thuộc giờ · <b>ча́с пик</b> giờ cao điểm</div>'
)

S["привет"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span><span class="hd-gloss">TỚI, hướng về phía ai</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вет</span><span class="hd-gloss">NÓI — gốc cổ nghĩa "lời, tiếng nói"</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>lời nói hướng tới ai</b> = lời chào. Gốc <b>вет-</b> này không còn đứng một mình, nhưng nó nằm trong mấy từ bạn sẽ dùng liên tục — nhận ra nó là được cả chùm.</div>'
    '<div class="hd-fam"><b>приве́т</b> chào (thân mật) · <b>отве́т</b> câu trả lời (<b>от</b>+вет = nói lại) · <b>отвеча́ть</b> trả lời · <b>сове́т</b> lời khuyên (<b>со</b>+вет = cùng bàn) · <b>сове́товать</b> khuyên</div>'
    '<div class="hd-warn"><b>Mức trang trọng — dùng sai là bất lịch sự:</b> <b>приве́т</b> chỉ dùng với <b>bạn bè, người ngang hàng, người nhỏ tuổi hơn</b>. Với người lớn tuổi, thầy cô, người lạ thì phải nói <b>здра́вствуйте</b>. Đây là khác biệt người Việt hay xem nhẹ vì tiếng Việt chào bằng đại từ chứ không đổi hẳn từ.</div>'
    '<div class="hd-warn">Còn dùng như danh từ: <b>Переда́й приве́т ма́ме</b> = Cho tớ gửi lời chào mẹ cậu.</div>'
)

# ---------- Từ chức năng ----------

S["себя"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Đại từ <b>PHẢN THÂN</b> — trỏ ngược về chính chủ ngữ của câu. Nghĩa: <b>bản thân mình</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-warn"><b>Đặc điểm lạ nhất:</b> <b>себя́ KHÔNG CÓ dạng cách 1</b> — không bao giờ làm chủ ngữ. Cũng <b>không đổi theo ngôi hay giống</b>: dùng chung cho tôi, bạn, anh ấy, chúng ta. Đây là chỗ dễ hơn tiếng Anh, vốn phải chọn <i>myself / yourself / himself</i>.</div>'
    '<div class="hd-fam"><b>себя́</b> (cách 2, 4) · <b>себе́</b> (cách 3, 6) · <b>собо́й</b> (cách 5)</div>'
    '<div class="hd-warn"><b>Đây chính là nguồn gốc của đuôi -ся!</b> <b>учи́ть + ся</b> = dạy chính mình = học. Đuôi <b>-ся</b> là dạng rút gọn cổ của <b>себя́</b>. Biết điều này thì cả lớp động từ phản thân bỗng có lý.</div>'
    '<div class="hd-warn"><b>Cụm dùng hằng ngày:</b> <b>у себя́</b> = ở chỗ mình · <b>про себя́</b> = thầm trong bụng (đối lại <b>вслух</b> = đọc to!) · <b>к себе́</b> = KÉO (chữ trên cửa) · <b>от себя́</b> = ĐẨY.</div>'
)

S["только"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ chức năng, không chẻ ra thành phần có nghĩa được. Nghĩa lõi: <b>CHỈ, chỉ có</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ngoài nghĩa "chỉ", nó còn hai việc nữa mà bạn sẽ gặp rất sớm:</div>'
    '<div class="hd-row"><span class="hd-piece">chỉ, mỗi</span><span class="hd-gloss">У меня́ <b>то́лько</b> оди́н вопро́с = Tôi chỉ có một câu hỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">vừa mới</span><span class="hd-gloss">Я <b>то́лько что</b> пришёл = Tôi vừa mới đến</span></div>'
    '<div class="hd-row"><span class="hd-piece">ngay khi</span><span class="hd-gloss"><b>Как то́лько</b> он придёт… = Ngay khi anh ấy đến…</span></div>'
    '<div class="hd-warn"><b>Vị trí quyết định nghĩa:</b> <b>то́лько</b> nhấn mạnh <b>từ đứng ngay SAU nó</b>. <i>То́лько я чита́л</i> = chỉ MÌNH TÔI đọc · <i>Я чита́л то́лько кни́гу</i> = tôi chỉ đọc MỖI quyển sách. Đặt sai chỗ là đổi nghĩa cả câu.</div>'
)

S["или"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Liên từ, hai âm tiết, không chẻ được. Nghĩa: <b>HOẶC</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-warn"><b>Bẫy dễ lẫn nhất — ba từ trông giống nhau:</b><br>'
    '<b>и́ли</b> = hoặc<br>'
    '<b>и</b> = và<br>'
    '<b>е́сли</b> = nếu<br>'
    'Chỉ khác một hai chữ mà nối câu theo ba kiểu khác hẳn. Đáng đọc to cả ba cạnh nhau vài lần.</div>'
    '<div class="hd-warn"><b>Dạng nhấn mạnh:</b> <b>и́ли… и́ли…</b> = hoặc là… hoặc là… — dùng khi bắt buộc chọn một. <i>И́ли ты, и́ли я</i> = Hoặc cậu, hoặc tớ.</div>'
    '<div class="hd-why">Trọng âm ở <b>и́</b> đầu từ, và trong câu nói nhanh nó thường bị nuốt gần hết — nghe như "ль".</div>'
)

S["за"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Giới từ một chữ, nhưng là một trong những giới từ <b>nhiều việc nhất</b> tiếng Nga.</div>'
    '<div class="hd-sec">Cách nhớ — nó đi với HAI cách, và cách quyết định nghĩa</div>'
    '<div class="hd-row"><span class="hd-piece">за + cách 5</span>'
    '<span class="hd-gloss">Ở ĐÂU (đứng yên): <b>за столо́м</b> = ở bàn (ngồi sau bàn)</span></div>'
    '<div class="hd-row"><span class="hd-piece">за + cách 4</span>'
    '<span class="hd-gloss">ĐI ĐÂU (chuyển động) / ĐỔI LẤY: <b>за стол</b> = vào bàn · <b>спаси́бо за по́мощь</b> = cảm ơn VÌ sự giúp đỡ</span></div>'
    '<div class="hd-why">Đây là <b>khuôn chung</b> của mấy giới từ chỉ vị trí: cách 5 = đứng yên, cách 4 = có chuyển động. Cùng khuôn: <b>под</b> (dưới), <b>над</b> (trên), <b>пе́ред</b> (trước).</div>'
    '<div class="hd-warn"><b>Nghĩa "vì, để đổi lấy" bạn dùng mỗi ngày:</b> <b>Спаси́бо за всё</b> = Cảm ơn vì tất cả · <b>плати́ть за обе́д</b> = trả tiền bữa trưa.</div>'
    '<div class="hd-warn"><b>Nó cũng là TIỀN TỐ</b> mà bạn đã gặp: <b>защи́та</b> (che bằng khiên) · <b>забы́ть</b> (quên = để lại phía sau) · <b>закры́ть</b> (đóng) · <b>зачёт</b> (tính vào).</div>'
)

S["про"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Giới từ, luôn đi với <b>cách 4</b>. Nghĩa: <b>VỀ, về chuyện…</b></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-warn"><b>Cặp phải phân biệt — cùng nghĩa, khác giọng:</b><br>'
    '<b>про</b> + cách 4 = <b>khẩu ngữ</b>, nói chuyện hằng ngày: <i>Расскажи́ про себя́</i> = Kể về cậu đi<br>'
    '<b>о / об</b> + cách 6 = <b>trung tính, văn viết</b>: <i>Я ду́маю о тебе́</i> = Tôi nghĩ về bạn<br>'
    'Trong bài viết và thi cử thì dùng <b>о</b>. Trong hội thoại thì <b>про</b> nghe tự nhiên hơn.</div>'
    '<div class="hd-warn"><b>Nó cũng là TIỀN TỐ rất năng suất</b>, nghĩa "xuyên suốt, từ đầu đến cuối": <b>проверя́ть</b> kiểm tra (rà suốt lượt) · <b>прочита́ть</b> đọc hết · <b>пройти́</b> đi qua. Bạn đã gặp ở thẻ <b>проверя́ть</b>.</div>'
    '<div class="hd-why">Mẹo nhớ đuôi: <b>про</b> đi với cách 4 nên dùng chung dạng với <b>себя́</b> — <b>про себя́</b> = thầm trong bụng, không nói ra.</div>'
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
