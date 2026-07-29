# -*- coding: utf-8 -*-
"""LÔ 11 — field `HuongDan`: 17 từ THIÊN NHIÊN, NGƯỜI, TÌNH CẢM.

Ba hệ thống trục:
  * DANH TỪ GIỐNG CÁI ĐUÔI -ь (nhóm biến cách thứ 3) — lô này có tới NĂM từ:
    вещь · дочь · любо́вь · мышь · рожь
  * NGUYÊN ÂM CHẠY — лёд→льда, лён→льна, ве́тер→ве́тра: nguyên âm biến mất khi biến cách
  * HỌ HÀNG ẤN–ÂU — мышь~mouse, рожь~rye, лён~linen, мо́ре~marine, дочь~daughter:
    năm từ nhận ra được ngay nếu biết tiếng Anh

Chạy: python data/huongdan/lo11_thiennhien_2026-07-27.py [--apply]
"""
import json
import sys
import urllib.request
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from anki_tools import grammar

ANKI = "http://127.0.0.1:8765"

MEM = (
    '<div class="hd-sec">Danh từ GIỐNG CÁI đuôi -ь — nhóm biến cách thứ 3</div>'
    '<div class="hd-why">Tiếng Nga có ba nhóm biến cách danh từ. Nhóm này nhỏ nhất nhưng chứa toàn '
    'từ lõi, nên phải nhận ra sớm: <b>tận cùng bằng -ь và GIỐNG CÁI</b>.</div>'
    '<div class="hd-fam"><b>вещь</b> đồ vật · <b>дочь</b> con gái · <b>любо́вь</b> tình yêu · '
    '<b>мышь</b> con chuột · <b>рожь</b> lúa mạch đen · <b>по́мощь</b> sự giúp đỡ · <b>ночь</b> đêm</div>'
    '<div class="hd-warn"><b>Mẹo nhận biết chắc chắn:</b> nếu trước <b>-ь</b> là <b>ж ш ч щ</b> thì '
    '<b>luôn luôn giống cái</b> (мышь, рожь, ночь, по́мощь). Còn sau phụ âm khác thì phải nhớ từng từ '
    '— <b>день</b> (ngày) là giống đực, <b>дверь</b> (cửa) là giống cái.</div>'
    '<div class="hd-why">Đặc điểm dễ chịu: nhóm này <b>KHÔNG đổi</b> ở cách 4 — <i>Я ви́жу мышь</i> '
    'y hệt dạng gốc. Đỡ được một chỗ phải nhớ.</div>'
)

CHAY = (
    '<div class="hd-sec">Nguyên âm chạy — chữ biến mất khi biến cách</div>'
    '<div class="hd-why">Một số từ có nguyên âm <b>chỉ xuất hiện ở dạng gốc</b>, rồi rụng mất ngay '
    'khi thêm đuôi. Không biết thì tưởng là hai từ khác nhau.</div>'
    '<div class="hd-fam">лёд băng → <b>льда</b> · лён lanh → <b>льна</b> · ве́тер gió → <b>ве́тра</b> · '
    'день ngày → <b>дня</b> · оте́ц cha → <b>отца́</b> · у́гол góc → <b>угла́</b></div>'
    '<div class="hd-why">Nguyên âm rụng luôn là <b>о</b>, <b>е</b> hoặc <b>ё</b> — chúng vốn là âm đệm '
    'cho dễ đọc, hết cần thì bỏ. Nhận ra khuôn này thì gặp dạng lạ vẫn tra được về từ gốc.</div>'
)

S = {}

# ---------- Nhóm giống cái đuôi -ь ----------

S["вещь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ <b>gốc trơn</b>, kết bằng <b>щ + ь</b> ⇒ <b>giống cái</b>, nhóm biến cách 3.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa rộng: <b>đồ vật, món đồ</b> — và số nhiều <b>ве́щи</b> còn nghĩa là <b>hành lý, đồ đạc</b>. <i>Собира́ть ве́щи</i> = xếp đồ đi đâu đó.</div>'
    '<div class="hd-why">Dùng cả cho cái trừu tượng: <b>стра́нная вещь</b> = một điều kỳ lạ. Giống hệt tiếng Việt "chuyện lạ", tiếng Anh <i>a strange thing</i>.</div>'
    '<div class="hd-warn"><b>Nhắc lại luật:</b> <b>вещь</b> có <b>-ь</b> nên giống cái; còn <b>плащ</b>, <b>борщ</b> không có <b>-ь</b> nên giống đực. Dấu mềm ở đây làm nhiệm vụ <b>báo giống</b>, không phải báo cách đọc.</div>'
    + MEM
)

S["дочь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ <b>gốc trơn</b>, kết bằng <b>ч + ь</b> ⇒ <b>giống cái</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>Họ hàng Ấn–Âu rất rõ:</b> <b>дочь</b> ~ tiếng Anh <i>daughter</i> ~ tiếng Đức <i>Tochter</i>. Cùng một từ cổ, tách ra vài nghìn năm trước rồi mòn đi mỗi nơi một kiểu. Từ chỉ quan hệ ruột thịt thường là từ cổ nhất và bền nhất của một ngôn ngữ.</div>'
    '<div class="hd-warn"><b>BIẾN CÁCH BẤT THƯỜNG — mọc thêm -ер-:</b> <b>дочь</b> → <b>до́чери</b>, <b>до́черью</b>. Chỉ hai từ trong tiếng Nga làm vậy, và đúng là hai từ ruột thịt: <b>дочь</b> (con gái) và <b>мать</b> (mẹ) → <b>ма́тери</b>. Đây cũng là dấu vết Ấn–Âu — so <i>mother/mater</i>, <i>daughter</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дочь</b> con gái · <b>до́чка</b> con gái (thân mật) · <b>сын</b> con trai · <b>мать</b> mẹ · <b>оте́ц</b> cha</div>'
    + MEM
)

S["любовь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">люб-</span><span class="hd-gloss">YÊU, ưa thích</span></div>'
    '<div class="hd-row"><span class="hd-piece">-овь</span><span class="hd-gloss">đuôi danh từ trừu tượng, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>люб-</b> sinh ra cả một họ bạn sẽ gặp liên tục, trong đó có một từ trông chẳng liên quan gì: <b>любо́й</b> = <b>bất kỳ cái nào</b> — nghĩa gốc "cái nào cũng ưa được".</div>'
    '<div class="hd-warn"><b>Nguyên âm chạy:</b> <b>любо́вь</b> → <b>любви́</b> — chữ <b>о</b> rụng mất. Nên câu "vì tình yêu" là <i>из-за любви́</i>, không phải <i>*любови</i>.</div>'
    '<div class="hd-warn"><b>Люба́вь cũng là TÊN NGƯỜI:</b> <b>Любо́вь</b> là một tên nữ phổ biến ở Nga, gọi thân mật là <b>Лю́ба</b>. Cùng bộ với <b>Ве́ра</b> (niềm tin) và <b>Наде́жда</b> (hy vọng) — ba đức tin, hy vọng, tình yêu.</div>'
    '<div class="hd-sec">Họ hàng — gốc люб</div>'
    '<div class="hd-fam"><b>люби́ть</b> yêu · <b>люби́мый</b> yêu dấu; ưa thích nhất · <b>любо́й</b> bất kỳ · <b>любо́вь</b> tình yêu · <b>влюби́ться</b> phải lòng</div>'
    + MEM
)

S["мышь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ <b>gốc trơn</b>, kết bằng <b>ш + ь</b> ⇒ <b>giống cái</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>Họ hàng Ấn–Âu thấy ngay:</b> <b>мышь</b> ~ <i>mouse</i> ~ tiếng Đức <i>Maus</i> ~ Latin <i>mus</i>. Đọc lên gần như trùng nhau. Đây là từ cổ tới mức mọi nhánh Ấn–Âu đều giữ.</div>'
    '<div class="hd-why">Nghĩa hiện đại đi theo tiếng Anh luôn: <b>компью́терная мышь</b> = con chuột máy tính. Người Nga cũng thấy hình dáng ấy giống con chuột.</div>'
    '<div class="hd-warn"><b>Nhắc luật ЖИ ШИ:</b> số nhiều là <b>мы́ши</b> — viết <b>ши</b> với <b>И</b>, dù đọc nghe như "ы". Đây đúng chỗ luật đó cứu bạn.</div>'
    + MEM
)

S["рожь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ <b>gốc trơn</b>, kết bằng <b>ж + ь</b> ⇒ <b>giống cái</b>. Nghĩa: <b>lúa mạch đen</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>Họ hàng Ấn–Âu:</b> <b>рожь</b> ~ tiếng Anh <i>rye</i> ~ tiếng Đức <i>Roggen</i>. Cùng một hạt ngũ cốc, cùng một tên gọi cổ.</div>'
    '<div class="hd-why">Vì sao đáng nhớ dù là từ ít gặp: <b>ржано́й хлеб</b> (bánh mì đen) là <b>bánh mì mặc định</b> ở Nga — thứ có mặt trên mọi bàn ăn. Nói "bánh mì" mà không nói rõ thì người Nga hình dung ra bánh đen này chứ không phải bánh trắng.</div>'
    '<div class="hd-warn"><b>Nguyên âm chạy dữ dội:</b> <b>рожь</b> → <b>ржи</b>, chữ <b>о</b> rụng sạch, còn lại cụm <b>ржи</b> không có nguyên âm nào ở đầu. Tính từ cũng vậy: <b>ржано́й</b>.</div>'
    + MEM + CHAY
)

# ---------- Nguyên âm chạy ----------

S["лёд"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ <b>gốc trơn</b> một âm tiết. Nghĩa: <b>băng, nước đá</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-warn"><b>Nguyên âm chạy — và chạy mạnh nhất trong lô:</b> <b>лёд</b> → <b>льда</b>, <b>льду</b>. Chữ <b>ё</b> biến mất, chỗ nó để lại thành dấu mềm <b>ь</b>. Nhìn <b>льда</b> mà không biết luật thì không đời nào tra ra <b>лёд</b>.</div>'
    '<div class="hd-why">Lý do rất gọn: <b>ё luôn mang trọng âm</b>. Khi thêm đuôi, trọng âm chuyển sang đuôi, thế là <b>ё</b> mất chỗ đứng và biến đi.</div>'
    '<div class="hd-warn"><b>Từ hay dùng ở xứ lạnh:</b> <b>ледяно́й</b> băng giá · <b>гололёд</b> đường đóng băng trơn trượt · <b>Ледо́вое побо́ище</b> "Trận chiến trên băng" (1242) — sự kiện lịch sử trẻ con Nga nào cũng học.</div>'
    '<div class="hd-sec">Họ hàng — gốc лед/льд</div>'
    '<div class="hd-fam"><b>лёд</b> băng · <b>ледяно́й</b> bằng băng, lạnh buốt · <b>ледни́к</b> sông băng · <b>моро́женое</b> kem (đã đông lại)</div>'
    + CHAY
)

S["лён"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ <b>gốc trơn</b>. Nghĩa: <b>cây lanh</b>, và vải lanh dệt từ nó.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>Họ hàng Ấn–Âu rất đẹp:</b> <b>лён</b> ~ Latin <i>linum</i> ~ tiếng Anh <i>linen</i> ~ <i>line</i> (sợi chỉ). Cả từ <b>line</b> (đường kẻ) cũng từ đó mà ra — vì đường kẻ đầu tiên người ta căng là sợi dây lanh.</div>'
    '<div class="hd-warn"><b>Nguyên âm chạy y hệt лёд:</b> <b>лён</b> → <b>льна</b>. Tính từ là <b>льняно́й</b> (bằng vải lanh) — nhìn không ra từ gốc nếu chưa biết luật.</div>'
    '<div class="hd-why">Vải lanh là chất liệu truyền thống của Nga (khí hậu hợp trồng lanh, không hợp trồng bông), nên <b>льняна́я руба́шка</b> = áo sơ mi vải lanh là hình ảnh quen thuộc.</div>'
    + CHAY
)

S["ветер"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ <b>gốc trơn</b>, giống đực. Nghĩa: <b>gió</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-warn"><b>Nguyên âm chạy:</b> <b>ве́тер</b> → <b>ве́тра</b>, <b>ве́тру</b> — chữ <b>е</b> thứ hai rụng. Đây cũng là lý do tính từ là <b>ве́треный</b> (thân từ <b>ветр-</b>) chứ không phải <i>*ветереный</i>.</div>'
    '<div class="hd-why">Bạn đã có thẻ <b>ве́треный</b> — hai thẻ này là một cặp, học chung thì hiểu luôn vì sao chữ <b>е</b> biến mất.</div>'
    '<div class="hd-warn"><b>Nghĩa bóng hay dùng:</b> <b>ве́тер в голове́</b> (gió trong đầu) = đầu óc trên mây, không chín chắn. Cùng hình ảnh với <b>ве́треный челове́к</b> = người nông nổi.</div>'
    '<div class="hd-sec">Họ hàng — gốc ветр</div>'
    '<div class="hd-fam"><b>ве́тер</b> gió · <b>ветеро́к</b> làn gió nhẹ · <b>ве́треный</b> lộng gió; nông nổi · <b>прове́трить</b> mở cửa cho thoáng</div>'
    + CHAY
)

# ---------- Thiên nhiên ----------

S["море"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ <b>gốc trơn</b>, đuôi <b>-е</b> ⇒ <b>giống trung</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>Họ hàng Ấn–Âu:</b> <b>мо́ре</b> ~ Latin <i>mare</i> ~ tiếng Anh <i>marine</i>, <i>maritime</i> ~ tiếng Pháp <i>mer</i>. Biết <i>marine</i> là gần như biết sẵn từ này.</div>'
    '<div class="hd-warn"><b>Cụm chỉ nơi chốn phải thuộc:</b> <b>на мо́ре</b> = ở biển / ra biển. Chú ý dùng <b>на</b> chứ không phải <b>в</b> — tiếng Nga coi biển là bề mặt, không phải cái hộp. Cùng nhóm: <b>на по́чте</b>, <b>на рабо́те</b>, <b>на уро́ке</b>.</div>'
    '<div class="hd-why">Với người Nga, <b>е́хать на мо́ре</b> (đi biển) gần như đồng nghĩa với "đi nghỉ hè" — vì phần lớn nước Nga cách biển rất xa.</div>'
    '<div class="hd-sec">Họ hàng — gốc мор</div>'
    '<div class="hd-fam"><b>мо́ре</b> biển · <b>морско́й</b> thuộc biển · <b>моря́к</b> thuỷ thủ · <b>примо́рский</b> ven biển</div>'
)

S["поле"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ <b>gốc trơn</b>, đuôi <b>-е</b> ⇒ <b>giống trung</b>, y như <b>мо́ре</b>. Nghĩa lõi: <b>khoảng đất PHẲNG và trống</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ một hình ảnh "mặt phẳng trống" toả ra mọi nghĩa: <b>cánh đồng</b> · <b>sân bóng</b> (футбо́льное по́ле) · <b>lề giấy</b> (поля́ тетра́ди) · <b>trường</b> trong vật lý (магни́тное по́ле).</div>'
    '<div class="hd-why">Nghĩa "lề giấy" đáng nhớ vì bạn sẽ gặp trong vở học: <b>поля́</b> (số nhiều) = phần trắng hai bên trang — đúng là khoảng trống.</div>'
    '<div class="hd-warn">⚠️ Mức tin: mối nối <b>по́ле</b> ~ tiếng Anh <i>plain</i>, <i>floor</i> là <b>từ nguyên</b> Ấn–Âu, đã xa tới mức không nhìn ra bằng mắt. Cứ nhớ nghĩa "mặt phẳng trống" là đủ dùng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́ле</b> cánh đồng · <b>полево́й</b> thuộc đồng ruộng · <b>по́лка</b> cái kệ (mặt phẳng!) · <b>по́лный</b> đầy</div>'
)

S["земля"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">земл-</span><span class="hd-gloss">ĐẤT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-я</span><span class="hd-gloss">đuôi danh từ GIỐNG CÁI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ba nghĩa xếp theo cỡ, dùng chung một từ: <b>đất</b> (dưới chân) → <b>vùng đất, lãnh thổ</b> → <b>Trái Đất</b> (viết hoa: <b>Земля́</b>).</div>'
    '<div class="hd-warn"><b>Từ ghép đáng nhớ vì chẻ ra là hiểu:</b> <b>землетрясе́ние</b> = động đất = <b>земле</b> (đất) + <b>трясе́ние</b> (sự rung). Tiếng Anh dựng y hệt: <i>earth-quake</i>. Ghép hai từ đã biết thành một từ dài — đó là cách tiếng Nga tạo từ khoa học.</div>'
    '<div class="hd-warn"><b>Trọng âm DỊCH ở số nhiều:</b> <b>земля́</b> (nhấn cuối) → <b>зе́мли</b> (nhấn đầu). Chuyện rất thường ở danh từ giống cái đuôi <b>-а/-я</b>.</div>'
    '<div class="hd-sec">Họ hàng — gốc зем</div>'
    '<div class="hd-fam"><b>земля́</b> đất · <b>земно́й</b> thuộc trái đất · <b>землетрясе́ние</b> động đất · <b>зе́мли</b> các vùng đất</div>'
)

S["лес"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ <b>gốc trơn</b> một âm tiết, giống đực. Nghĩa: <b>rừng</b>; và cả <b>gỗ nguyên liệu</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-warn"><b>Đặc điểm ngữ pháp phải biết:</b> <b>лес</b> thuộc nhóm nhỏ danh từ có <b>cách 6 riêng cho nơi chốn</b>, đuôi <b>-у́</b> có trọng âm: <b>в лесу́</b> = trong rừng (không phải <i>*в ле́се</i>). Cùng nhóm: <b>в саду́</b> trong vườn · <b>на берегу́</b> trên bờ · <b>в году́</b> trong năm.</div>'
    '<div class="hd-why">Rừng chiếm gần một nửa diện tích nước Nga, nên <b>лес</b> có mặt khắp văn hoá: truyện cổ tích nào cũng bắt đầu bằng ai đó đi vào rừng, và <b>Ба́ба-Яга́</b> luôn sống trong rừng sâu.</div>'
    '<div class="hd-sec">Họ hàng — gốc лес</div>'
    '<div class="hd-fam"><b>лес</b> rừng · <b>лесно́й</b> thuộc rừng · <b>лесни́к</b> kiểm lâm · <b>переле́сок</b> khoảnh rừng thưa</div>'
)

# ---------- Người và tình cảm ----------

S["малыш"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мал-</span><span class="hd-gloss">NHỎ — cùng gốc <b>ма́ленький</b> (nhỏ), <b>ма́ло</b> (ít)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыш</span><span class="hd-gloss">hậu tố SINH VẬT NON</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>đứa nhỏ</b>. Hậu tố <b>-ыш</b> chuyên chỉ con non, sinh vật bé: <b>малы́ш</b> em bé · <b>детёныш</b> con non của thú · <b>найдёныш</b> đứa trẻ bị bỏ rơi được nhặt về.</div>'
    '<div class="hd-why">Đây là từ mang <b>giọng âu yếm</b>, người lớn gọi trẻ con và người yêu gọi nhau. Không phải từ trung tính — muốn nói "trẻ em" chung chung thì dùng <b>ребёнок</b>.</div>'
    '<div class="hd-warn"><b>Giống ngữ pháp:</b> <b>малы́ш</b> kết thúc bằng phụ âm ⇒ <b>giống đực</b>, kể cả khi gọi bé gái. Bé gái có từ riêng nếu cần: <b>малы́шка</b>.</div>'
    '<div class="hd-sec">Họ hàng — gốc мал</div>'
    '<div class="hd-fam"><b>ма́ленький</b> nhỏ · <b>ма́ло</b> ít · <b>малы́ш</b> em bé · <b>ме́ньше</b> ít hơn, nhỏ hơn</div>'
)

S["слеза"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ <b>gốc trơn</b>, đuôi <b>-а</b> ⇒ <b>giống cái</b>. Nghĩa: <b>giọt nước mắt</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-warn"><b>Số nhiều đổi mặt chữ:</b> <b>слеза́</b> → <b>слёзы</b>. Chữ <b>е</b> thành <b>ё</b> khi trọng âm nhảy về đầu — vì <b>ё chỉ tồn tại ở chỗ có nhấn</b>. Cùng luật với <b>счёт → счета́</b>, chỉ ngược chiều.</div>'
    '<div class="hd-why">Dạng số nhiều <b>слёзы</b> mới là dạng bạn gặp nhiều hơn — người ta ít khi khóc một giọt. <b>В слеза́х</b> = đang khóc, đầm đìa nước mắt.</div>'
    '<div class="hd-why">Bạn đã có thẻ <b>плач</b> (tiếng khóc) — hai từ này đi cùng cảnh: <b>плач</b> là âm thanh, <b>слёзы</b> là thứ chảy ra.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>слеза́</b> giọt nước mắt · <b>слёзы</b> nước mắt · <b>слезли́вый</b> hay mau nước mắt · <b>прослези́ться</b> rưng rưng</div>'
)

S["вина"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вин-</span><span class="hd-gloss">LỖI, tội</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span><span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>вин-</b> nhỏ mà sinh ra một từ bạn dùng <b>mỗi ngày</b>: <b>извини́те</b> (xin lỗi) = <b>из-</b> (ra khỏi) + <b>вин</b> (lỗi) = <b>"xin gỡ lỗi ra cho tôi"</b>. Biết điều này thì <b>извините</b> không còn là chuỗi âm vô nghĩa phải học vẹt.</div>'
    '<div class="hd-warn"><b>BẪY TRÙNG MẶT CHỮ với вино́ (rượu vang) — hai tầng:</b><br>'
    '<b>ви́на</b> (nhấn ĐẦU) = <i>các loại rượu vang</i> (số nhiều của вино́) — khác chỗ nhấn nên còn phân biệt được.<br>'
    '<b>вина́</b> (nhấn CUỐI) = vừa là <i>lỗi lầm</i>, vừa là <i>của rượu vang</i> (cách 2 của вино́) — <b>trùng khít cả chữ lẫn dấu</b>, chỉ ngữ cảnh mới tách được.</div>'
    '<div class="hd-warn"><b>Câu dùng thật:</b> <b>Э́то моя́ вина́</b> = Đó là lỗi của tôi. Và <b>винова́т</b> (dạng ngắn) = "tôi có lỗi", một cách xin lỗi rất thường gặp.</div>'
    '<div class="hd-sec">Họ hàng — gốc вин</div>'
    '<div class="hd-fam"><b>вина́</b> lỗi · <b>винова́тый</b> có lỗi · <b>извини́ть</b> tha lỗi · <b>обвиня́ть</b> buộc tội · <b>невино́вный</b> vô tội</div>'
)

S["сожаление"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span><span class="hd-gloss">CÙNG — cùng cảm thấy với ai</span></div>'
    '<div class="hd-row"><span class="hd-piece">-жал-</span><span class="hd-gloss">THƯƠNG XÓT, tiếc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span><span class="hd-gloss">biến động từ → danh từ, giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>cùng thấy tiếc</b> = sự tiếc nuối, lòng thương cảm. Tiền tố <b>со-</b> đúng cái bạn đã gặp ở <b>совреме́нный</b> (cùng thời).</div>'
    '<div class="hd-warn"><b>Từ cùng gốc bạn dùng HẰNG NGÀY:</b> <b>пожа́луйста</b> (làm ơn / không có gì) cũng ra từ gốc <b>жал-</b> này. Và <b>жаль</b> = "tiếc quá" — <i>Как жаль!</i> = Tiếc thật!</div>'
    '<div class="hd-warn"><b>Cụm cực hay gặp trong văn viết:</b> <b>к сожале́нию</b> = <b>tiếc thay, rất tiếc là…</b>. Đây là cách mở đầu câu từ chối lịch sự. Đáng thuộc nguyên cụm.</div>'
    '<div class="hd-sec">Họ hàng — gốc жал</div>'
    '<div class="hd-fam"><b>жаль</b> tiếc · <b>жа́лко</b> đáng thương, tiếc · <b>жа́ловаться</b> than phiền · <b>пожа́луйста</b> làm ơn · <b>сожале́ние</b> sự tiếc nuối</div>'
)

S["счастье"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span><span class="hd-gloss">TỐT LÀNH, cùng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-часть-</span><span class="hd-gloss">PHẦN, suất được chia</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ье</span><span class="hd-gloss">đuôi danh từ trừu tượng, GIỐNG TRUNG</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: <b>có được phần tốt của mình</b>. Bạn đã gặp gốc này ở <b>счастли́вый</b> — đây là dạng danh từ của nó.</div>'
    '<div class="hd-why">Cùng cách nghĩ với <b>бога́тый</b> (giàu = được thần ban phần): người Slav xưa hình dung vận may như <b>một suất được chia</b>, không phải thứ mình tự tạo ra.</div>'
    '<div class="hd-warn"><b>Bẫy phát âm:</b> <b>сч</b> đọc thành <b>щ</b> — "ЩАС-tye", và chữ <b>т</b> câm. Y hệt <b>счастли́вый</b>, <b>счита́ть</b>. Đừng chép chính tả theo tai.</div>'
    '<div class="hd-warn"><b>Câu chúc phải thuộc:</b> <b>Сча́стья!</b> (chúc hạnh phúc) — dùng cách 2, là cách chúc chuẩn của tiếng Nga. Và <b>На сча́стье!</b> = chúc may mắn.</div>'
    '<div class="hd-sec">Họ hàng — gốc часть</div>'
    '<div class="hd-fam"><b>часть</b> phần · <b>сча́стье</b> hạnh phúc · <b>счастли́вый</b> hạnh phúc (tính từ) · <b>уча́стие</b> sự tham gia (nhận một phần) · <b>уча́ствовать</b> tham gia</div>'
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
