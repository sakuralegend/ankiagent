# -*- coding: utf-8 -*-
"""LÔ 7 — field `HuongDan`: 19 ĐỘNG TỪ.

Nhóm quan trọng nhất trong số từ còn lại, vì động từ tiếng Nga có hai thứ mà
người mới bắt buộc phải hiểu sớm, càng muộn càng đắt:
  * CẶP THỂ (вид): chưa hoàn thành / hoàn thành — học một từ là phải biết bạn nó
  * HAI LỚP CHIA (спряжение): lớp -ать/-еть và lớp -ить

⚠️ Bộ soát `kiemtra.py` chỉ tra được DANH TỪ, nên lô này nó đỡ được ít nhất.
Chỗ nào là luật chắc chắn, chỗ nào chỉ là cách nhìn cho dễ nhớ — đã ghi rõ
trong từng thẻ bằng `.hd-warn`.

Chạy: python data/huongdan/lo07_dongtu_2026-07-27.py [--apply]
"""
import json
import sys
import urllib.request
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from anki_tools import grammar

ANKI = "http://127.0.0.1:8765"

THE = (
    '<div class="hd-sec">Cặp thể — khái niệm đắt nhất của động từ Nga</div>'
    '<div class="hd-why">Gần như mọi động từ Nga sống thành <b>CẶP</b>, hai từ cho một nghĩa. '
    'Chọn từ nào là chọn <b>cách nhìn</b> sự việc, không phải chọn thì.</div>'
    '<div class="hd-row"><span class="hd-piece">chưa HT</span>'
    '<span class="hd-gloss">tiến trình, thói quen, lặp lại — "đang làm", "hay làm"</span></div>'
    '<div class="hd-row"><span class="hd-piece">hoàn thành</span>'
    '<span class="hd-gloss">một lần, xong hẳn, có kết quả — "đã làm xong"</span></div>'
    '<div class="hd-why">Cách dựng phổ biến nhất: thêm tiền tố <b>по-</b> vào dạng chưa hoàn thành. '
    'Nên rất nhiều cặp chỉ khác đúng hai chữ: <b>ду́мать → поду́мать</b>.</div>'
    '<div class="hd-warn">Hệ quả thực dụng: <b>động từ hoàn thành KHÔNG có thì hiện tại</b>. '
    'Chia nó ở dạng hiện tại thì ra nghĩa TƯƠNG LAI — <b>я поду́маю</b> = tôi sẽ nghĩ.</div>'
)

CHIA = (
    '<div class="hd-sec">Hai lớp chia động từ</div>'
    '<div class="hd-row"><span class="hd-piece">lớp 1</span>'
    '<span class="hd-gloss">phần lớn đuôi <b>-ать -еть</b>: ду́ма<b>ю</b>, ду́ма<b>ешь</b>, ду́ма<b>ет</b>, '
    'ду́ма<b>ем</b>, ду́ма<b>ете</b>, ду́ма<b>ют</b> — nguyên âm <b>Е</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">lớp 2</span>'
    '<span class="hd-gloss">phần lớn đuôi <b>-ить</b>: говор<b>ю́</b>, говор<b>и́шь</b>, говор<b>и́т</b>, '
    'говор<b>и́м</b>, говор<b>и́те</b>, говор<b>я́т</b> — nguyên âm <b>И</b></span></div>'
    '<div class="hd-why">Nhìn nguyên âm ở đuôi là biết lớp: <b>Е</b> → lớp 1, <b>И</b> → lớp 2. '
    'Biết lớp là chia được cả sáu ngôi.</div>'
)

MUTATION = (
    '<div class="hd-warn"><b>Luật biến âm ngôi "tôi":</b> ở lớp 2, riêng ngôi <b>я</b> hay bị đổi phụ âm '
    'cuối gốc — <b>д→ж</b> (ви́деть → ви́<b>ж</b>у) · <b>с→ш</b> (проси́ть → про<b>ш</b>у́) · '
    '<b>т→ч</b> (плати́ть → пла<b>ч</b>у́) · <b>б/п/в/м</b> mọc thêm <b>л</b> (люби́ть → лю<b>бл</b>ю́). '
    'Chỉ ngôi "tôi" đổi, năm ngôi còn lại nguyên vẹn.</div>'
)

S = {}

# ---------- Chùm BỮA ĂN: danh từ bữa ăn -> động từ ăn bữa đó ----------

BUAAN = (
    '<div class="hd-sec">Bộ ba bữa ăn — một luật, ba từ</div>'
    '<div class="hd-why">Tiếng Nga không nói "ăn sáng" bằng hai từ như tiếng Việt. Nó lấy thẳng '
    '<b>tên bữa ăn</b> rồi biến thành động từ bằng <b>-ать</b>.</div>'
    '<div class="hd-fam"><b>за́втрак</b> bữa sáng → <b>за́втракать</b> ăn sáng · '
    '<b>обе́д</b> bữa trưa → <b>обе́дать</b> ăn trưa · '
    '<b>у́жин</b> bữa tối → <b>у́жинать</b> ăn tối</div>'
    '<div class="hd-why">Cả ba đều <b>lớp 1</b>, chia y hệt nhau, và cả ba đều lấy <b>по-</b> làm dạng '
    'hoàn thành. Học một là được ba.</div>'
)

S["завтракать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">завтрак-</span><span class="hd-gloss">за́втрак — BỮA SÁNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span><span class="hd-gloss">đuôi nguyên thể, lớp 1</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bản thân <b>за́втрак</b> cũng chẻ được: <b>за</b> (cho, vào lúc) + <b>у́тро</b> (buổi sáng) — "phần dành cho buổi sáng". Cùng một nguồn với <b>за́втра</b> (ngày mai), vốn nghĩa "vào sáng hôm sau".</div>'
    '<div class="hd-warn">⚠️ Mức tin: mối liên hệ <b>за́втрак ↔ за́втра</b> là <b>từ nguyên</b>, không phải luật bạn suy ra được. Nhưng nó có thật và giúp nhớ hai từ cùng lúc.</div>'
    '<div class="hd-warn"><b>Cặp thể:</b> <b>за́втракать</b> (chưa HT) / <b>поза́втракать</b> (HT). "Tôi thường ăn sáng lúc 7 giờ" dùng cái đầu; "Tôi đã ăn sáng xong" dùng cái sau.</div>'
    + BUAAN + THE
)

S["обедать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">обед-</span><span class="hd-gloss">обе́д — BỮA TRƯA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span><span class="hd-gloss">đuôi nguyên thể, lớp 1</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>Обе́д</b> ở Nga là bữa <b>chính</b> trong ngày, thường có xúp — không nhẹ như bữa trưa của nhiều nước. Vì thế <b>обе́денный переры́в</b> (giờ nghỉ trưa) là một phần cố định của ngày làm việc.</div>'
    '<div class="hd-warn"><b>Cặp thể:</b> <b>обе́дать</b> / <b>пообе́дать</b>.</div>'
    + BUAAN + THE
)

S["ужинать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ужин-</span><span class="hd-gloss">у́жин — BỮA TỐI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span><span class="hd-gloss">đuôi nguyên thể, lớp 1</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hoàn tất bộ ba. Nhớ theo trục thời gian trong ngày: <b>за́втрак → обе́д → у́жин</b>, mỗi cái dán <b>-ать</b> là thành động từ.</div>'
    '<div class="hd-warn"><b>Cặp thể:</b> <b>у́жинать</b> / <b>поу́жинать</b>. Trọng âm ở <b>у</b> đầu từ và không dịch đi đâu cả.</div>'
    + BUAAN + THE
)

# ---------- Chùm CHẺ ĐƯỢC, gốc lộ nghĩa ----------

S["понимать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span><span class="hd-gloss">tiền tố</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ним-</span><span class="hd-gloss">LẤY, NẮM — cùng gốc <b>-ём/-ня-</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span><span class="hd-gloss">đuôi nguyên thể, lớp 1</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>NẮM ĐƯỢC</b> — hiểu tức là túm được ý. Đây chính là gốc bạn đã gặp ở <b>подъём</b> và <b>объём</b>, nay hiện ra dưới mặt nạ <b>-ним-</b>.</div>'
    '<div class="hd-why">Tiếng Anh dùng đúng hình ảnh đó: <i>to grasp an idea</i> = nắm được ý. Và <i>comprehend</i> ← Latin <i>com-</i> + <i>prehendere</i> = <b>túm lấy</b>. Ba thứ tiếng cùng một ẩn dụ.</div>'
    '<div class="hd-warn"><b>Cặp thể ĐỔI MẶT rất mạnh:</b> <b>понима́ть</b> (chưa HT) / <b>поня́ть</b> (HT). Hai từ trông khác hẳn nhau nhưng là một cặp — đây là kiểu cặp bạn buộc phải nhớ nguyên đôi, không suy ra được.</div>'
    '<div class="hd-sec">Họ hàng — gốc ня/ним/ём (lấy)</div>'
    '<div class="hd-fam"><b>поня́ть</b> hiểu (HT) · <b>приня́ть</b> nhận · <b>заня́ть</b> chiếm, mượn · <b>подня́ть</b> nâng lên · <b>сня́ть</b> cởi ra, thuê · <b>подъём</b> sự nâng lên</div>'
    + THE
)

S["повторять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span><span class="hd-gloss">tiền tố</span></div>'
    '<div class="hd-row"><span class="hd-piece">-втор-</span><span class="hd-gloss">THỨ HAI — chính là <b>второ́й</b> (thứ hai)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ять</span><span class="hd-gloss">đuôi nguyên thể, lớp 1</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen đẹp và trong: <b>làm lần thứ HAI</b> = lặp lại, ôn lại. Thấy <b>втор</b> là thấy số 2.</div>'
    '<div class="hd-why">Từ này bạn sẽ dùng suốt đời học: <b>повторя́ть слова́</b> = ôn từ vựng. Chính là việc bạn đang làm với Anki mỗi ngày.</div>'
    '<div class="hd-warn"><b>Cặp thể:</b> <b>повторя́ть</b> (chưa HT, ôn đi ôn lại) / <b>повтори́ть</b> (HT, nhắc lại một lần). Chú ý đuôi đổi <b>-ять → -ить</b> nên cũng <b>đổi lớp chia</b>: lớp 1 sang lớp 2.</div>'
    '<div class="hd-sec">Họ hàng — gốc втор (hai)</div>'
    '<div class="hd-fam"><b>второ́й</b> thứ hai · <b>вто́рник</b> thứ Ba (ngày thứ HAI của tuần Nga, vì tuần bắt đầu từ thứ Hai!) · <b>повторе́ние</b> sự ôn tập</div>'
    + THE
)

S["проверять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span><span class="hd-gloss">XUYÊN QUA, làm suốt lượt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вер-</span><span class="hd-gloss">TIN — chính là <b>ве́ра</b> (niềm tin), <b>ве́рить</b> (tin)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ять</span><span class="hd-gloss">đuôi nguyên thể, lớp 1</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>rà suốt lượt xem có tin được không</b> = kiểm tra. Tiếng Anh <i>verify</i> đi cùng đường: ← Latin <i>verus</i> = thật.</div>'
    '<div class="hd-why">Tiền tố <b>про-</b> rất đáng thuộc, luôn mang ý "xuyên suốt, từ đầu đến cuối": <b>прочита́ть</b> đọc hết · <b>пройти́</b> đi qua · <b>проду́мать</b> nghĩ cho thấu.</div>'
    '<div class="hd-warn"><b>Cặp thể:</b> <b>проверя́ть</b> / <b>прове́рить</b>, lại đúng kiểu <b>-ять/-ить</b> như <b>повторя́ть</b>. Nhận ra khuôn này thì đoán được dạng còn lại của rất nhiều động từ.</div>'
    '<div class="hd-sec">Họ hàng — gốc вер (tin)</div>'
    '<div class="hd-fam"><b>ве́рить</b> tin · <b>ве́ра</b> niềm tin · <b>ве́рный</b> đúng, trung thành · <b>прове́рка</b> cuộc kiểm tra · <b>уве́рен</b> chắc chắn</div>'
    + THE
)

S["сказать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span><span class="hd-gloss">tiền tố hoàn thành (làm trọn một lần)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-каз-</span><span class="hd-gloss">CHỈ RA, phô ra, nói ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span><span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>каз-</b> nghĩa "làm cho thấy" — sinh ra cả một họ lớn mà bạn sẽ gặp liên tục.</div>'
    '<div class="hd-warn"><b>CẶP THỂ BẤT THƯỜNG, phải nhớ nguyên đôi:</b> <b>говори́ть</b> (chưa HT) / <b>сказа́ть</b> (HT). Hai từ <b>khác gốc hoàn toàn</b> mà vẫn là một cặp. Quy tắc dùng gọn: kể lể, trò chuyện, nói một thứ tiếng → <b>говори́ть</b>; nói bật ra một câu cụ thể → <b>сказа́ть</b>.</div>'
    '<div class="hd-warn"><b>Chia bất quy tắc:</b> <b>сказа́ть</b> → <b>скажу́, ска́жешь, ска́жет</b> — chữ <b>з</b> đổi thành <b>ж</b> ở MỌI ngôi (khác luật thường, vốn chỉ đổi ở ngôi "tôi").</div>'
    '<div class="hd-sec">Họ hàng — gốc каз (chỉ ra)</div>'
    '<div class="hd-fam"><b>показа́ть</b> cho xem · <b>рассказа́ть</b> kể lại · <b>ска́зка</b> truyện cổ tích (cái được kể) · <b>прика́з</b> mệnh lệnh · <b>отказа́ться</b> từ chối</div>'
    + THE
)

S["спросить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span><span class="hd-gloss">tiền tố hoàn thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-прос-</span><span class="hd-gloss">HỎI, XIN — cùng gốc <b>проси́ть</b> (xin)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span><span class="hd-gloss">đuôi nguyên thể, lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một gốc <b>прос-</b> sinh ra hai việc rất gần nhau: <b>проси́ть</b> = xin (mong được cho), <b>спроси́ть</b> = hỏi (mong được trả lời). Tiếng Việt tách hẳn hai từ, tiếng Nga thấy chúng cùng một gốc.</div>'
    '<div class="hd-warn"><b>Cặp thể:</b> <b>спра́шивать</b> (chưa HT) / <b>спроси́ть</b> (HT). Chú ý dạng chưa hoàn thành mọc thêm <b>-ива-</b> và đổi cả nguyên âm gốc — kiểu cặp phải nhớ đôi.</div>'
    '<div class="hd-warn"><b>Ngôi "tôi" biến âm:</b> <b>спроси́ть → спрошу́</b> (с→ш), nhưng <b>спро́сишь, спро́сит</b> giữ nguyên. Đúng luật chung của lớp 2.</div>'
    '<div class="hd-sec">Họ hàng — gốc прос/праш</div>'
    '<div class="hd-fam"><b>проси́ть</b> xin, nhờ · <b>спроси́ть</b> hỏi · <b>вопро́с</b> câu hỏi · <b>про́сьба</b> lời thỉnh cầu</div>'
    + MUTATION + THE
)

S["учиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">уч-</span><span class="hd-gloss">DẠY / HỌC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-</span><span class="hd-gloss">nối, lớp 2</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ться</span><span class="hd-gloss">đuôi PHẢN THÂN — hành động quay về chính mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là chỗ đuôi <b>-ся/-сь</b> lộ ra hết công dụng: <b>учи́ть</b> = dạy người khác; gắn <b>-ся</b> vào thành <b>учи́ться</b> = <b>dạy CHÍNH MÌNH</b> = học. Chỉ hai chữ mà lật ngược chiều của hành động.</div>'
    '<div class="hd-why"><b>-ся</b> vốn là dạng rút của <b>себя́</b> (bản thân) — từ bạn cũng có thẻ. Nhớ điều này thì cả lớp động từ phản thân trở nên có lý: <b>мы́ться</b> tắm (rửa mình) · <b>одева́ться</b> mặc đồ (mặc cho mình) · <b>называ́ться</b> được gọi là.</div>'
    '<div class="hd-warn"><b>Chính tả:</b> sau nguyên âm viết <b>-сь</b>, sau phụ âm viết <b>-ся</b> — <b>учу́сь</b> nhưng <b>у́чится</b>. Và <b>у́чится</b> (ngôi 3) khác <b>учи́ться</b> (nguyên thể) đúng một dấu mềm.</div>'
    '<div class="hd-sec">Họ hàng — gốc уч</div>'
    '<div class="hd-fam"><b>учи́ть</b> dạy; học thuộc · <b>учи́ться</b> đi học · <b>учи́тель</b> thầy giáo · <b>учени́к</b> học trò · <b>учёный</b> nhà khoa học · <b>нау́ка</b> khoa học</div>'
    + THE
)

S["спрягаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span><span class="hd-gloss">CÙNG, gộp lại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пряг-</span><span class="hd-gloss">BUỘC, THẮNG (ngựa vào xe)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-аться</span><span class="hd-gloss">đuôi nguyên thể + phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hình ảnh gốc rất cụ thể: <b>thắng mấy con ngựa vào chung một cỗ xe</b>. Chia động từ cũng là buộc một gốc vào cả bộ đuôi cho sáu ngôi — cùng một hình ảnh.</div>'
    '<div class="hd-why">Tiếng Anh trùng khít: <i>conjugate</i> ← Latin <i>con-</i> (cùng) + <i>iugum</i> (cái ách buộc bò). Hai ngôn ngữ độc lập chọn đúng một ẩn dụ.</div>'
    '<div class="hd-warn"><b>Đây là thuật ngữ trong sách giáo khoa của bạn:</b> <b>глаго́л спряга́ется</b> = động từ được chia. Dạng phản thân <b>-ся</b> ở đây mang nghĩa <b>bị động</b> — "được chia", chứ không phải "tự chia mình".</div>'
    '<div class="hd-sec">Họ hàng — gốc пряг/пряж</div>'
    '<div class="hd-fam"><b>спряже́ние</b> sự chia động từ · <b>запря́чь</b> thắng ngựa vào xe · <b>упря́жка</b> bộ yên cương</div>'
    + THE
)

S["целовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">цел-</span><span class="hd-gloss">NGUYÊN VẸN, lành lặn — chính là <b>це́лый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ов-</span><span class="hd-gloss">hậu tố tạo động từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span><span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc bất ngờ mà nhớ rất lâu: hôn vốn là <b>chúc cho lành lặn, nguyên vẹn</b> — cùng gốc với <b>це́лый</b> (nguyên vẹn) và <b>исцели́ть</b> (chữa lành). Tiếng Anh song song: <i>whole</i> và <i>heal</i> cũng cùng gốc.</div>'
    '<div class="hd-warn"><b>Lớp -овать rất năng suất, và chia LẠ:</b> phần <b>-ова-</b> biến mất, thay bằng <b>-у-</b> — <b>целова́ть → целу́ю, целу́ешь</b>. Cùng khuôn: <b>рисова́ть → рису́ю</b> · <b>танцева́ть → танцу́ю</b>. Nhớ khuôn này là chia được cả trăm động từ.</div>'
    '<div class="hd-sec">Họ hàng — gốc цел</div>'
    '<div class="hd-fam"><b>це́лый</b> nguyên vẹn, cả · <b>целова́ть</b> hôn · <b>поцелу́й</b> nụ hôn · <b>цель</b> mục tiêu</div>'
    + THE
)

S["рисовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рис-</span><span class="hd-gloss">VẼ — mượn qua tiếng Ba Lan từ tiếng Đức <i>reißen</i> (vạch nét)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ов-ать</span><span class="hd-gloss">hậu tố + đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-warn"><b>Bẫy nghĩa nguy hiểm:</b> <b>рис</b> đứng một mình nghĩa là <b>GẠO</b>, chẳng liên quan gì tới vẽ. Hai từ trùng mặt chữ, khác gốc hoàn toàn — đừng nối chúng lại.</div>'
    '<div class="hd-why">Nhớ theo khuôn chia thì chắc hơn nhớ theo gốc: <b>рисова́ть → рису́ю, рису́ешь</b>, đúng lớp <b>-овать</b> mà bạn thấy ở <b>целова́ть</b> và <b>танцева́ть</b>.</div>'
    '<div class="hd-warn"><b>Cặp thể:</b> <b>рисова́ть</b> / <b>нарисова́ть</b>. Ở đây tiền tố hoàn thành là <b>на-</b> chứ không phải <b>по-</b> — không có luật chọn tiền tố nào, phải nhớ theo từng từ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рису́нок</b> bức vẽ · <b>рисова́ние</b> việc vẽ · <b>нарисова́ть</b> vẽ xong</div>'
    + THE
)

S["танцевать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">танц-</span><span class="hd-gloss">та́нец — ĐIỆU NHẢY (mượn từ tiếng Đức <i>Tanz</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ев-ать</span><span class="hd-gloss">hậu tố + đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ quốc tế — bạn đã biết qua <i>dance</i>. Việc duy nhất phải học là bộ đuôi.</div>'
    '<div class="hd-warn"><b>Vì sao là -ев- chứ không -ов-:</b> sau <b>ц</b> (và ж, ч, ш, щ) thì <b>о</b> không nhấn phải viết thành <b>е</b>. Đây là luật chính tả chạy khắp tiếng Nga, không riêng từ này.</div>'
    '<div class="hd-warn"><b>Chia:</b> <b>танцу́ю, танцу́ешь</b> — <b>-ева-</b> rụng, thay bằng <b>-у-</b>, đúng khuôn <b>целова́ть → целу́ю</b>.</div>'
    '<div class="hd-warn"><b>Chữ е rụng:</b> та́н<b>е</b>ц → танц-. Lại là "nguyên âm chạy", y như <b>ве́тер → ве́тр-</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>та́нец</b> điệu nhảy · <b>танцева́ть</b> nhảy múa · <b>танцо́р</b> vũ công</div>'
    + THE
)

# ---------- Chùm GỐC TRƠN, trọng tâm là CHIA và CẶP THỂ ----------

S["думать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дум-</span><span class="hd-gloss">NGHĨ (<b>ду́ма</b> = ý nghĩ; và là tên Quốc hội Nga)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span><span class="hd-gloss">đuôi nguyên thể, lớp 1</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là <b>động từ mẫu</b> của lớp 1 — chia đều tăm tắp, không biến âm, không rụng chữ. Học thuộc bộ đuôi ở đây rồi áp cho hàng trăm động từ <b>-ать</b> khác.</div>'
    '<div class="hd-fam"><b>ду́маю</b> tôi nghĩ · <b>ду́маешь</b> · <b>ду́мает</b> · <b>ду́маем</b> · <b>ду́маете</b> · <b>ду́мают</b></div>'
    '<div class="hd-warn"><b>Cấu trúc bắt buộc phải thuộc:</b> <b>ду́мать о</b> + cách 6 = nghĩ VỀ. <i>Я ду́маю о тебе́</i> = Tôi nghĩ về bạn. Động từ Nga từ nào cũng kéo theo một cách nhất định — học động từ là phải học luôn cái cách nó đòi.</div>'
    + CHIA + THE
)

S["видеть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вид-</span><span class="hd-gloss">THẤY, cảnh tượng (<b>вид</b> = quang cảnh, dáng vẻ)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-еть</span><span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>вид-</b> có họ hàng Ấn–Âu rất xa mà vẫn nhận ra: Latin <i>videre</i> (nhìn) → tiếng Anh <i>video</i>, <i>evident</i>. Cùng một gốc cổ.</div>'
    '<div class="hd-warn"><b>NGOẠI LỆ PHẢI THUỘC:</b> đuôi <b>-еть</b> thường là lớp 1, nhưng <b>ви́деть</b> thuộc <b>LỚP 2</b>. Có một nhóm nhỏ ngoại lệ như vậy, đáng thuộc cả cụm: <b>смотре́ть</b> nhìn · <b>ви́деть</b> thấy · <b>слы́шать</b> nghe · <b>терпе́ть</b> chịu đựng · <b>зави́сеть</b> phụ thuộc.</div>'
    '<div class="hd-warn"><b>Ngôi "tôi" biến âm:</b> <b>ви́жу</b> (д→ж), rồi <b>ви́дишь, ви́дит, ви́дим, ви́дите, ви́дят</b> trở lại bình thường.</div>'
    '<div class="hd-warn"><b>Phân biệt cặp dễ lẫn:</b> <b>ви́деть</b> = thấy (không chủ ý, mắt bắt được) ↔ <b>смотре́ть</b> = nhìn, xem (có chủ ý). Đúng như <i>see</i> ↔ <i>watch</i>.</div>'
    '<div class="hd-sec">Họ hàng — gốc вид</div>'
    '<div class="hd-fam"><b>вид</b> quang cảnh; thể (ngữ pháp) · <b>уви́деть</b> nhìn thấy (HT) · <b>свида́ние</b> cuộc hẹn · <b>ви́дно</b> có thể thấy, rõ ràng · <b>до свида́ния</b> tạm biệt (nghĩa đen: cho tới lần gặp lại)</div>'
    + MUTATION + CHIA
)

S["звонить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">звон-</span><span class="hd-gloss">TIẾNG CHUÔNG (<b>звон</b> = tiếng ngân)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span><span class="hd-gloss">đuôi nguyên thể, lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc là <b>rung chuông</b>; thời có điện thoại thì thành <b>gọi điện</b> — vì máy điện thoại cũng đổ chuông. Hình ảnh vẫn còn nguyên trong từ.</div>'
    '<div class="hd-warn"><b>TRỌNG ÂM — bẫy nổi tiếng nhất tiếng Nga hiện đại:</b> chuẩn mực là <b>звони́т</b>, <b>звоня́т</b> (nhấn đuôi). Rất nhiều người Nga nói <i>зво́нит</i> và bị coi là nói sai — đây là lỗi bị chê nhiều nhất trên truyền hình Nga. Bạn cứ nhấn đuôi là an toàn.</div>'
    '<div class="hd-warn"><b>Cấu trúc bắt buộc:</b> <b>звони́ть кому́</b> + cách 3 = gọi cho ai. <i>Я звоню́ ма́ме</i> = Tôi gọi cho mẹ. Không phải cách 4 như tiếng Việt "gọi ai".</div>'
    '<div class="hd-sec">Họ hàng — gốc звон/звен</div>'
    '<div class="hd-fam"><b>звон</b> tiếng chuông · <b>звоно́к</b> cú điện thoại; chuông cửa · <b>позвони́ть</b> gọi điện (HT) · <b>звене́ть</b> ngân vang</div>'
    + CHIA + THE
)

S["играть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">игр-</span><span class="hd-gloss">игра́ — TRÒ CHƠI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span><span class="hd-gloss">đuôi nguyên thể, lớp 1</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-warn"><b>Điểm đáng giá nhất của từ này là hai giới từ đi kèm — nhớ sai là sai hẳn nghĩa:</b></div>'
    '<div class="hd-row"><span class="hd-piece">игра́ть в</span><span class="hd-gloss">chơi MÔN THỂ THAO / trò chơi: игра́ть <b>в</b> футбо́л</span></div>'
    '<div class="hd-row"><span class="hd-piece">игра́ть на</span><span class="hd-gloss">chơi NHẠC CỤ: игра́ть <b>на</b> гита́ре</span></div>'
    '<div class="hd-why">Mẹo phân biệt: thể thao thì bạn ở <b>trong</b> cuộc chơi (в), còn nhạc cụ thì bạn gảy <b>trên</b> mặt đàn (на).</div>'
    '<div class="hd-sec">Họ hàng — gốc игр</div>'
    '<div class="hd-fam"><b>игра́</b> trò chơi · <b>игру́шка</b> đồ chơi · <b>игро́к</b> người chơi · <b>сыгра́ть</b> chơi một ván (HT)</div>'
    + CHIA + THE
)

S["гулять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гул-</span><span class="hd-gloss">gốc trơn, nghĩa DẠO CHƠI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ять</span><span class="hd-gloss">đuôi nguyên thể, lớp 1</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không phải "đi bộ" theo nghĩa di chuyển, mà là <b>đi dạo cho thư thái</b> — đi chơi ngoài trời, không nhằm tới đâu cả. Đây là một hoạt động có vị trí hẳn hoi trong đời sống Nga: <b>гуля́ть в па́рке</b>.</div>'
    '<div class="hd-warn"><b>Phân biệt với ba từ "đi" khác</b> — tiếng Nga bắt bạn chọn, không có từ chung chung: <b>идти́</b> đi bộ tới đâu đó (một chiều, lúc này) · <b>ходи́ть</b> đi bộ thường xuyên · <b>е́хать</b> đi bằng xe · <b>гуля́ть</b> đi dạo chơi.</div>'
    '<div class="hd-warn"><b>Cặp thể:</b> <b>гуля́ть</b> / <b>погуля́ть</b> (đi dạo một lát).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прогу́лка</b> cuộc dạo chơi · <b>погуля́ть</b> dạo một lát · <b>прогу́ливать</b> trốn học, trốn làm</div>'
    + CHIA + THE
)

S["жить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">жи-</span><span class="hd-gloss">SỐNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span><span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một trong những động từ cốt lõi nhất, và là ví dụ sạch của luật <b>ЖИ viết И</b>.</div>'
    '<div class="hd-warn"><b>Chia BẤT THƯỜNG — phải thuộc lòng:</b> gốc mọc thêm <b>-в-</b> khi chia. <b>живу́, живёшь, живёт, живём, живёте, живу́т</b>. Nguyên thể không hề báo trước điều đó, nên đây là từ không suy được, chỉ nhớ được.</div>'
    '<div class="hd-warn"><b>Cấu trúc bắt buộc:</b> <b>жить в</b> + cách 6 = sống ở đâu. <i>Я живу́ в Москве́</i>.</div>'
    '<div class="hd-sec">Họ hàng — gốc жи (sống)</div>'
    '<div class="hd-fam"><b>жизнь</b> cuộc sống · <b>живо́й</b> sống, sinh động · <b>живо́т</b> cái bụng (xưa nghĩa là "sự sống"!) · <b>жи́тель</b> cư dân · <b>живо́тное</b> con vật</div>'
    + THE
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
            # 🔴 GIỮ BẢNG CHIA. Script này viết 27/07, trước khi ô Hướng dẫn có
            # bảng chia máy dựng ở cuối. Ghi thẳng `html` là XOÁ MẤT bảng, im
            # lặng, chỉ phát hiện khi mở thẻ ra xem. `attach_table` nối lại bảng
            # từ dữ liệu từ điển nên chạy lại script cũ cũng không phá gì.
            ac("updateNoteFields", note={"id": ids[0], "fields": {
                "HuongDan": grammar.attach_table(html, grammar.get_cached(word))}})
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
