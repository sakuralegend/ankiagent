# -*- coding: utf-8 -*-
"""LÔ 6 — field `HuongDan`: nhóm chữ Щ và Ч (14 từ).

Đây là nhóm user hay gõ sai, nên trục không phải nghĩa mà là CHÍNH TẢ + nguồn gốc
của chữ щ:
  * luật trường học Nga: ЧА ЩА viết А · ЧУ ЩУ viết У · ЖИ ШИ viết И
  * chữ щ phần lớn KHÔNG phải chữ gốc — nó sinh ra từ biến âm ст/ск/т + j
    (хвост → хвощ, мощь ← мог, защита ← щит)
  * danh từ giống cái đuôi -ь (по́мощь, вещь, мышь) = biến cách nhóm 3

Chạy: python data/huongdan/lo06_shcha_cha_2026-07-27.py [--apply]
"""
raise SystemExit("KHAI TU 30/07/2026: chuan v1 — chay lai se XOA BANG CHIA the that. Xem QD-03.")
import json
import sys
import urllib.request
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from anki_tools import grammar

ANKI = "http://127.0.0.1:8765"

CHINHTA = (
    '<div class="hd-sec">Luật chính tả trẻ con Nga nào cũng thuộc</div>'
    '<div class="hd-row"><span class="hd-piece">ЧА ЩА</span>'
    '<span class="hd-gloss">viết <b>А</b>, không bao giờ Я: <b>ча</b>с · <b>ща</b>ве́ль · поща́да</span></div>'
    '<div class="hd-row"><span class="hd-piece">ЧУ ЩУ</span>'
    '<span class="hd-gloss">viết <b>У</b>, không bao giờ Ю: <b>чу</b>до · <b>щу</b>ка · чу́вство</span></div>'
    '<div class="hd-row"><span class="hd-piece">ЖИ ШИ</span>'
    '<span class="hd-gloss">viết <b>И</b>, không bao giờ Ы: <b>жи</b>ть · <b>ши</b>ть · маши́на</span></div>'
    '<div class="hd-why">Lý do: <b>ч</b> và <b>щ</b> tự thân đã MỀM sẵn, còn <b>ж</b> và <b>ш</b> tự thân '
    'đã CỨNG sẵn — không cần nguyên âm đi kèm báo hộ, nên tiếng Nga chọn luôn dạng đơn giản. '
    'Hiểu lý do thì khỏi học vẹt.</div>'
)

NGUON = (
    '<div class="hd-sec">Chữ Щ ở đâu ra — mẹo chẻ từ</div>'
    '<div class="hd-why">Phần lớn chữ <b>щ</b> KHÔNG phải chữ gốc: nó là <b>ск · ст · т</b> bị làm '
    'mềm khi thêm hậu tố. Nên gặp <b>щ</b> thì thử thay ngược lại, thường lòi ra từ quen.</div>'
    '<div class="hd-fam">хвост đuôi → хво<b>щ</b> · мочь có thể → мо<b>щ</b>ь sức mạnh · '
    'пусти́ть thả → пу<b>щ</b>у́ tôi sẽ thả · чи́стить lau → чи́<b>щ</b>у tôi lau</div>'
)

S = {}

# ---------- Chùm CÓ HỌ HÀNG THẬT: щит → защита, мощь → помощь ----------

S["щит"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ <b>gốc trơn</b> một âm tiết — đây là chữ <b>щ</b> gốc thật, không phải do biến âm. Nghĩa: <b>cái khiên</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là <b>từ mẹ</b> của cả một chùm, nên đáng nhớ kỹ hơn nghĩa "cái khiên" của nó: từ <b>щит</b> mọc ra <b>защи́та</b> (sự bảo vệ) và <b>защища́ть</b> (bảo vệ) — hai từ bạn sẽ dùng nhiều hơn hẳn từ gốc.</div>'
    '<div class="hd-why">Nghĩa hiện đại rất đời thường: <b>щит</b> còn là <b>bảng điện, bảng quảng cáo lớn</b> — bất cứ tấm phẳng nào chắn phía trước.</div>'
    '<div class="hd-sec">Họ hàng — gốc щит</div>'
    '<div class="hd-fam"><b>щит</b> cái khiên · <b>защи́та</b> sự bảo vệ · <b>защища́ть</b> bảo vệ · <b>защи́тник</b> người bảo vệ, hậu vệ (bóng đá)</div>'
    + CHINHTA
)

S["защита"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span><span class="hd-gloss">CHE PHÍA SAU, chắn lại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-щит-</span><span class="hd-gloss">щит — CÁI KHIÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span><span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen trong veo: <b>đưa cái khiên ra chắn</b> = sự bảo vệ. Chẻ ra rồi thì không cần học thuộc nữa — bạn đã có sẵn <b>щит</b> trong bộ thẻ.</div>'
    '<div class="hd-why">Tiền tố <b>за-</b> mang ý "chắn, phía sau, bắt đầu" và gặp khắp nơi: <b>закры́ть</b> đóng lại · <b>забы́ть</b> quên (để lại phía sau) · <b>заходи́ть</b> ghé vào.</div>'
    '<div class="hd-warn"><b>Nghĩa bạn sẽ gặp ở trường:</b> <b>защи́та дипло́ма</b> = bảo vệ luận văn. Đúng hình ảnh: đứng trước hội đồng, giơ khiên đỡ câu hỏi.</div>'
    '<div class="hd-sec">Họ hàng — gốc щит</div>'
    '<div class="hd-fam"><b>щит</b> cái khiên · <b>защи́та</b> sự bảo vệ · <b>защища́ть</b> bảo vệ · <b>защи́тник</b> người bảo vệ, hậu vệ</div>'
    + CHINHTA
)

S["помощь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span><span class="hd-gloss">tiền tố, ý "góp vào, làm một lượt"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мощ-</span><span class="hd-gloss">SỨC MẠNH, khả năng — biến âm từ <b>мог-</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ь</span><span class="hd-gloss">dấu mềm — dấu hiệu DANH TỪ GIỐNG CÁI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>góp sức vào</b> = sự giúp đỡ. Và gốc <b>мощ-</b> chính là <b>мочь / могу́</b> (có thể) mà bạn sẽ học rất sớm — cùng một gốc, ba mặt nạ: <b>мог</b> → <b>мож</b> → <b>мощ</b>.</div>'
    '<div class="hd-why">Chuỗi biến âm <b>г → ж → щ</b> này là một trong những chuỗi năng suất nhất tiếng Nga. Nhận ra nó thì <b>мочь</b>, <b>мо́жет</b>, <b>мощь</b>, <b>по́мощь</b>, <b>возмо́жность</b> gộp lại chỉ còn MỘT gốc phải nhớ.</div>'
    '<div class="hd-warn"><b>Luật giống cái đuôi -ь:</b> danh từ tận cùng bằng <b>-ь</b> mà trước đó là <b>ж ш ч щ</b> thì <b>luôn luôn GIỐNG CÁI</b>. Trong bộ thẻ của bạn: <b>по́мощь</b>, <b>вещь</b> (đồ vật), <b>мышь</b> (con chuột), <b>рожь</b> (lúa mạch), <b>дочь</b> (con gái) — tất cả cùng nhóm.</div>'
    '<div class="hd-sec">Họ hàng — gốc мог/мож/мощ</div>'
    '<div class="hd-fam"><b>мочь</b> có thể · <b>мо́жно</b> được phép · <b>мощь</b> sức mạnh · <b>по́мощь</b> sự giúp đỡ · <b>помога́ть</b> giúp đỡ · <b>возмо́жность</b> khả năng</div>'
    + CHINHTA + NGUON
)

S["пощада"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span><span class="hd-gloss">tiền tố hoàn thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-щад-</span><span class="hd-gloss">THA, nương tay (<b>щади́ть</b> = tha cho)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span><span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa: <b>sự tha thứ, sự nương tay</b> — thường gặp trong câu phủ định <b>без поща́ды</b> = không thương tiếc, không nương tay.</div>'
    '<div class="hd-why">Từ này ít dùng trong hội thoại đời thường, nhưng nó là <b>ví dụ sạch của luật ЩА viết А</b>: поща́да, chứ không đời nào là <i>*пощяда</i>.</div>'
    '<div class="hd-sec">Họ hàng — gốc щад-</div>'
    '<div class="hd-fam"><b>щади́ть</b> tha, nương tay · <b>поща́да</b> sự tha thứ · <b>беспоща́дный</b> tàn nhẫn, không thương tiếc</div>'
    + CHINHTA
)

# ---------- Chùm ĐỒ VẬT ----------

S["щётка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">щёт-</span><span class="hd-gloss">từ <b>щети́на</b> — LÔNG CỨNG, lông bàn chải</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-а</span><span class="hd-gloss">hậu tố vật nhỏ + đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>cái có lông cứng</b> = bàn chải. Từ bạn dùng mỗi sáng: <b>зубна́я щётка</b> = bàn chải đánh răng.</div>'
    '<div class="hd-warn"><b>Nhắc lại luật quà tặng:</b> chữ <b>ё</b> LUÔN mang trọng âm. Thấy <b>щётка</b> là biết nhấn ngay đó, không phải phân vân.</div>'
    '<div class="hd-why">Hậu tố <b>-ка</b> ở đây là "vật nhỏ, đồ dùng" — cực kỳ năng suất, gặp suốt: <b>ру́чка</b> cái bút · <b>ча́шка</b> cái chén · <b>ло́жка</b> cái thìa · <b>ще́пка</b> mảnh dăm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>щети́на</b> lông cứng, râu lởm chởm · <b>щётка</b> bàn chải · <b>чи́стить щёткой</b> chải, cọ</div>'
    + CHINHTA
)

S["щепка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">щеп-</span><span class="hd-gloss">CHẺ, tách ra (<b>щепа́</b> = dăm gỗ)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-а</span><span class="hd-gloss">hậu tố vật nhỏ + đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa: <b>mảnh dăm gỗ</b> — mẩu nhỏ chẻ ra từ khúc củi. Cùng gốc với <b>расщепи́ть</b> (chẻ đôi, tách hạt nhân) nên gốc <b>щеп-</b> luôn mang ý "tách nhỏ".</div>'
    '<div class="hd-why">Có thành ngữ rất hay dùng: <b>худо́й как ще́пка</b> = gầy như que củi. Đúng kiểu ví von tiếng Việt.</div>'
    '<div class="hd-sec">Họ hàng — gốc щеп-</div>'
    '<div class="hd-fam"><b>щепа́</b> dăm gỗ · <b>ще́пка</b> mảnh dăm · <b>расщепи́ть</b> chẻ ra, tách · <b>щепо́тка</b> một nhúm (muối) — thứ bạn nhón tách ra</div>'
    + CHINHTA
)

S["плащ"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ <b>gốc trơn</b>, không chẻ được. Nghĩa: <b>áo mưa, áo choàng</b> — thứ khoác ngoài che mưa gió.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nối với nhóm thời tiết bạn vừa học: trời <b>дождли́вый</b> (mưa dai) hay <b>ве́треный</b> (gió) thì mặc <b>плащ</b>. Học từ theo tình huống dùng, đừng học rời.</div>'
    '<div class="hd-warn"><b>Bẫy chính tả:</b> kết thúc bằng <b>щ</b> trần, KHÔNG có dấu mềm — <b>плащ</b> chứ không phải <i>*плащь</i>. Đây là danh từ <b>giống đực</b>; chỉ danh từ GIỐNG CÁI mới đội <b>-ь</b> sau ж ш ч щ.</div>'
    '<div class="hd-why">Đối chiếu cho rõ luật: <b>плащ</b> (đực, không ь) ↔ <b>по́мощь</b>, <b>вещь</b>, <b>мышь</b> (cái, có ь). Dấu mềm ở đây làm nhiệm vụ <b>báo giống</b>, không phải báo cách đọc.</div>'
    + CHINHTA
)

S["щи"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ <b>gốc trơn</b>, chỉ hai chữ cái — một trong những từ ngắn nhất tiếng Nga. Nghĩa: <b>xúp bắp cải</b>, món quốc hồn quốc tuý của Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-warn"><b>Chỉ có SỐ NHIỀU:</b> <b>щи</b> không có dạng số ít, y như tiếng Việt nói "bún riêu" chứ không đếm được. Nhóm "chỉ số nhiều" này còn có <b>де́ньги</b> tiền · <b>часы́</b> đồng hồ · <b>очки́</b> kính mắt · <b>кани́кулы</b> kỳ nghỉ.</div>'
    '<div class="hd-why">Có câu tục ngữ mọi người Nga đều biết, đọc lên là thấy hết đời sống của họ: <b>«Щи да ка́ша — пи́ща на́ша»</b> = "Xúp bắp cải với cháo — ấy là cơm của ta".</div>'
    '<div class="hd-why">Nối với bộ thẻ của bạn: <b>щи</b> nấu từ <b>капу́ста</b> (bắp cải), còn <b>борщ</b> thì thêm củ dền. Hai món xúp Nga bạn đều đã có thẻ — nhớ chung một chỗ.</div>'
    + CHINHTA
)

S["щука"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ <b>gốc trơn</b>. Nghĩa: <b>cá măng, cá chó</b> — loài cá dữ răng nhọn sống ở sông hồ Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ví dụ sạch của luật <b>ЩУ viết У</b>: <b>щу́ка</b>, không đời nào là <i>*щюка</i>.</div>'
    '<div class="hd-why"><b>Щу́ка</b> là nhân vật cổ tích ai cũng biết — trong truyện <i>По щу́чьему веле́нию</i> ("Theo lệnh con cá măng"), chàng lười Emelya bắt được cá măng thần và mọi ước đều thành. Nhớ từ qua câu chuyện thì chắc hơn nhớ qua nghĩa.</div>'
    + CHINHTA
)

S["хвощ"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">хво-</span><span class="hd-gloss">từ <b>хвост</b> — CÁI ĐUÔI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-щ</span><span class="hd-gloss">chữ <b>ст</b> của хвост bị làm mềm thành <b>щ</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa: <b>cỏ đuôi ngựa</b> — loài cây có thân đốt trông đúng như cái đuôi. Tiếng Anh gọi y hệt: <i>horsetail</i>. Ba thứ tiếng cùng nhìn ra một hình ảnh.</div>'
    '<div class="hd-why">Đây là <b>ví dụ đẹp nhất của luật ст → щ</b> trong cả lô: <b>хвост</b> (đuôi) → <b>хвощ</b>. Nhớ cặp này là nhớ luôn được luật.</div>'
    '<div class="hd-warn">Từ hiếm, gần như chỉ gặp trong sách sinh học. Đừng tốn sức nhớ nghĩa — hãy nhớ nó vì <b>cái luật biến âm</b> nó minh hoạ.</div>'
    + NGUON + CHINHTA
)

# ---------- Chùm chữ Ч ----------

S["врач"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вра-</span><span class="hd-gloss">gốc cổ nghĩa NÓI, đọc thần chú</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ч</span><span class="hd-gloss">hậu tố NGƯỜI LÀM (như -чик, -щик)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa hôm nay: <b>bác sĩ</b>. Nhưng gốc thì kể một câu chuyện — thời xưa người chữa bệnh là người <b>đọc thần chú</b>, nên <b>врач</b> họ hàng xa với <b>врать</b> (nghĩa cổ: nói; nghĩa nay: nói dối).</div>'
    '<div class="hd-warn">⚠️ Nói rõ mức tin: đây là <b>từ nguyên</b>, không phải thứ người Nga hôm nay còn cảm thấy. Đừng bao giờ nói đùa rằng bác sĩ liên quan tới nói dối — nghĩa hiện đại của hai từ đã tách hẳn.</div>'
    '<div class="hd-warn"><b>Điểm ngữ pháp thật sự quan trọng:</b> <b>врач</b> luôn là <b>giống đực</b> về mặt ngữ pháp, kể cả khi bác sĩ là phụ nữ. Người ta nói <b>«Она́ хоро́ший врач»</b> (dùng tính từ giống đực). Cùng nhóm nghề bất biến: <b>инжене́р</b>, <b>дире́ктор</b>, <b>профе́ссор</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>врач</b> bác sĩ · <b>враче́бный</b> thuộc y khoa · <b>вра́чебная по́мощь</b> sự cứu chữa y tế · <b>лечи́ть</b> chữa bệnh (từ thường dùng hơn)</div>'
    + CHINHTA
)

S["луч"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ <b>gốc trơn</b> một âm tiết. Nghĩa: <b>tia sáng</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ này có <b>họ hàng Ấn–Âu rất xa mà vẫn nhận ra được</b>: Latin <i>lux</i> (ánh sáng), tiếng Anh <i>lucid</i>, <i>translucent</i>. Cùng một gốc cổ nghĩa "sáng", tách ra hàng nghìn năm trước.</div>'
    '<div class="hd-why">Dùng thật: <b>луч со́лнца</b> tia nắng · <b>лучи́</b> (số nhiều) các tia · <b>рентге́новские лучи́</b> tia X.</div>'
    '<div class="hd-warn"><b>Bẫy nhìn nhầm:</b> <b>луч</b> (tia sáng) KHÔNG liên quan gì tới <b>лу́чше</b> (tốt hơn) — hai từ khác gốc hoàn toàn, chỉ trùng mấy chữ đầu.</div>'
    + CHINHTA
)

S["плач"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">плач-</span><span class="hd-gloss">KHÓC — từ động từ <b>пла́кать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là kiểu <b>danh từ trần</b>: lấy động từ, cắt trụi đuôi, thành danh từ chỉ chính hành động đó. <b>пла́кать</b> (khóc) → <b>плач</b> (tiếng khóc). Cùng kiểu: <b>крича́ть</b> hét → <b>крик</b> tiếng hét · <b>смотре́ть</b> nhìn → <b>смотр</b> cuộc duyệt.</div>'
    '<div class="hd-warn"><b>BẪY QUAN TRỌNG NHẤT của từ này:</b> <b>плач</b> (không ь) = DANH TỪ, tiếng khóc. <b>плачь</b> (có ь) = MỆNH LỆNH "khóc đi!". Chỉ khác một dấu mềm mà khác hẳn từ loại. Luật đứng sau: danh từ giống đực không đội <b>-ь</b>, còn động từ mệnh lệnh thì có.</div>'
    '<div class="hd-sec">Họ hàng — gốc плак/плач</div>'
    '<div class="hd-fam"><b>пла́кать</b> khóc · <b>плач</b> tiếng khóc · <b>запла́кать</b> oà khóc · <b>плакси́вый</b> hay mè nheo</div>'
    + CHINHTA
)

S["грач"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ <b>gốc trơn</b>. Nghĩa: <b>quạ đen mỏ trắng</b> (loài rook), họ hàng gần với quạ.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tên gọi bắt chước tiếng kêu "gra-gra" — cùng kiểu đặt tên với <b>куку́шка</b> (chim cu, kêu "ku-ku") hay tiếng Việt "con quạ" từ tiếng "quạ quạ".</div>'
    '<div class="hd-why">Vì sao người Nga ai cũng biết từ này: <b>грачи́</b> là <b>chim báo xuân</b> — loài bay về sớm nhất sau mùa đông. Bức tranh <i>«Грачи́ прилете́ли»</i> ("Đàn quạ đã bay về") là tranh phong cảnh nổi tiếng nhất nước Nga, trẻ con nào cũng học.</div>'
    '<div class="hd-warn"><b>Nhóm vần dễ lẫn</b> — bốn từ đều một âm tiết kết bằng <b>-ч</b>, nên phân biệt bằng nghĩa: <b>врач</b> bác sĩ · <b>грач</b> con quạ · <b>плач</b> tiếng khóc · <b>луч</b> tia sáng.</div>'
    + CHINHTA
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
