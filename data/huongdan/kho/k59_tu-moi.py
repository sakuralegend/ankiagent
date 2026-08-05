# -*- coding: utf-8 -*-
"""k59 — tu-moi: 13 động từ THỂ HOÀN THÀNH dựng bằng tiền tố (вы-/на-/по-/с-/у-/подо-),
mỗi từ là bản hoàn thành của một động từ chưa hoàn thành ĐÃ CÓ trong kho.

🔴 Trục có thật nhưng KHÔNG đồng đều — và thẻ phải nói đúng chỗ nó khác:
  · tiền tố RỖNG thật (chỉ đổi thể, nghĩa y nguyên): нарисова́ть · сде́лать · позвони́ть
  · tiền tố kèm sắc thái "MỘT LÁT" (по- hạn định): погуля́ть · потанцева́ть · подожда́ть
  · tiền tố kèm sắc thái "HẾT SẠCH" (kết quả): вы́пить · вы́учить · съесть
  · tiền tố kèm sắc thái "BẮT ĐƯỢC / chợt nhận ra": уви́деть · услы́шать · смочь
Từ điển nguồn gộp cả bốn nhóm làm một; thẻ tách ra vì đó chính là chỗ user gõ sai.

Chuẩn v3 (data/huongdan/CHUAN.md). Mỗi thẻ đứng một mình.
"""

# 🔴 KHÔNG dựng biến khối dùng chung rồi cộng vào mọi thẻ — xem README §3.

S = {}
V = {}

# --------------------------------------------------------------- вы- : cho tới HẾT

S["выпить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span>'
    '<span class="hd-gloss">RA NGOÀI → ở đây: cho tới HẾT, cạn sạch</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пи-</span>'
    '<span class="hd-gloss">UỐNG — chính là <b>пить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là "uống cho ra hết", nên đây không phải là "đã uống" chung '
    'chung mà là uống <b>cạn</b> phần đó: <i>вы́пить чай</i> = uống hết cốc trà.</div>'
    '<div class="hd-why"><b>Chú ý bảng chia:</b> thân hiện tại là <b>пь-</b>, không đoán ra từ '
    'nguyên thể được — phải nhớ kèm <i>вы́пью, вы́пьешь</i>. Bù lại trọng âm khỏi lo: tiền tố '
    '<b>вы́-</b> của thể hoàn thành hút trọng âm về mình ở <b>mọi</b> dạng, trong khi '
    '<b>пить</b> nhấn đuôi (<i>пьёшь</i>).</div>'
    '<div class="hd-warn"><b>Đứng một mình là chuyện rượu:</b> <i>Он лю́бит вы́пить</i> không phải '
    '"anh ấy thích uống nước" mà là "anh ấy hay nhậu".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пить</b> uống · <b>напи́ток</b> đồ uống · <b>попи́ть</b> uống một chút</div>'
)

S["выучить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span>'
    '<span class="hd-gloss">tới cùng, cho XONG hẳn — và hút trọng âm về mình</span></div>'
    '<div class="hd-row"><span class="hd-piece">-уч-</span>'
    '<span class="hd-gloss">HỌC / DẠY — chính là <b>учи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi nguyên thể, chia lớp hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>учи́ть</b> là đang học, <b>вы́-</b> đóng nắp lại: học tới lúc '
    '<b>thuộc</b>, kết quả nằm sẵn trong đầu. Trọng âm theo đó nhảy hẳn về tiền tố — '
    '<b>учи́ть</b> nhấn đuôi, còn <b>вы́учить</b> nhấn <b>вы́-</b> ở mọi dạng.</div>'
    '<div class="hd-warn"><b>Ba chữ "học" đừng lẫn:</b> <b>вы́учить</b> = học thuộc một bài cụ thể · '
    '<b>учи́ться</b> = đi học, là học sinh · <b>изуча́ть</b> = nghiên cứu một môn. Và <b>учи́ть</b> '
    'một mình còn nghĩa <b>dạy</b>, trong khi <b>вы́учить</b> hầu như chỉ là "học thuộc".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>учи́ть</b> học, dạy · <b>учи́ться</b> đi học · <b>учи́тель</b> giáo viên · '
    '<b>учени́к</b> học sinh · <b>нау́ка</b> khoa học</div>'
)

# ------------------------------------------------------- на-/с-/по- : tiền tố RỖNG

S["нарисовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">ở đây KHÔNG mang nghĩa riêng — chỉ đóng dấu "xong"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-рисова-</span>'
    '<span class="hd-gloss">VẼ — chính là <b>рисова́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là tiền tố <b>rỗng</b> đúng nghĩa: <b>нарисова́ть</b> không thêm sắc '
    'thái nào so với <b>рисова́ть</b>, chỉ đổi "đang vẽ" thành "vẽ xong, ra được bức tranh". Nói ai '
    'đó biết vẽ hay vẽ hằng ngày thì vẫn phải quay về bản chưa hoàn thành.</div>'
    '<div class="hd-why"><b>Chú ý bảng chia:</b> mảnh <b>-ова-</b> biến mất khi chia, đổi thành '
    '<b>-у-</b> — <i>нарису́ю, нарису́ешь, нарису́ют</i>. Chính cái thân đó nằm sẵn trong danh từ '
    '<b>рису́нок</b> (bức vẽ), nhớ một cái là ra cái kia.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рисова́ть</b> vẽ · <b>рису́нок</b> bức vẽ, hình vẽ · '
    '<b>рисова́ние</b> việc vẽ, môn vẽ</div>'
)

S["сделать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">tiền tố RỖNG — không thêm nghĩa gì, chỉ đổi sang thể hoàn thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дел-</span>'
    '<span class="hd-gloss">LÀM — chính là danh từ <b>де́ло</b> (việc)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi nguyên thể, chia lớp một</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là cặp thể <b>sạch</b> nhất nên học thuộc làm mẫu: '
    '<b>де́лать</b> và <b>сде́лать</b> nghĩa y hệt nhau, khác đúng một chuyện "đang làm" hay '
    '"làm xong". Bảng chia cũng không giấu gì — trọng âm đứng yên ở <b>де́-</b> suốt lượt.</div>'
    '<div class="hd-warn"><b>Biến A thành B thì dùng cách 5:</b> vật bị tác động ở cách 4, '
    'kết quả ở cách 5 — <i>Э́то сде́лало его́ счастли́вым</i> = điều đó làm anh ấy hạnh phúc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>де́лать</b> làm · <b>де́ло</b> việc, chuyện · <b>сде́лка</b> vụ giao dịch · '
    '<b>неде́ля</b> tuần — nghĩa gốc "ngày KHÔNG làm việc"</div>'
)

S["позвонить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố RỖNG — chỉ đóng dấu hoàn thành, không thêm nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-звон-</span>'
    '<span class="hd-gloss">TIẾNG CHUÔNG — chính là <b>звон</b>, <b>звоно́к</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi nguyên thể, chia lớp hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiếng Nga không "gọi" mà <b>làm cho chuông reo</b> — gốc <b>звон-</b> là '
    'tiếng chuông. <b>позвони́ть</b> = bấm gọi một cuộc rồi xong, còn <b>звони́ть</b> là đang gọi '
    'hoặc hay gọi.</div>'
    '<div class="hd-warn"><b>Gọi cho AI thì cách 3, không có giới từ:</b> <i>позвони́ть '
    '<b>ма́ме</b></i>, <i>позвони́ <b>мне</b></i>. Gọi <b>tới đâu</b> mới cần giới từ: '
    '<i>позвони́ть в банк</i> (в + cách 4).</div>'
    '<div class="hd-warn"><b>Trọng âm luôn ở đuôi, suốt bảng:</b> <i>позвоню́, позвони́шь, '
    'позвони́т, позвоня́т</i>. Dạng <i>позво́нит</i> là lỗi phổ biến tới mức người Nga cũng dính — '
    'đừng học theo.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>звони́ть</b> gọi điện · <b>звоно́к</b> cú điện thoại, chuông cửa · '
    '<b>звон</b> tiếng chuông</div>'
)

# ------------------------------------------------ по- hạn định : làm MỘT LÁT rồi thôi

S["погулять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">MỘT LÁT, một quãng ngắn — không phải tiền tố rỗng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-гуля-</span>'
    '<span class="hd-gloss">ĐI DẠO, rong chơi — chính là <b>гуля́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>по-</b> ở đây đóng khung <b>thời lượng</b> chứ không đóng khung kết quả: '
    'ra ngoài đi dạo <b>một lát</b> rồi về, chứ không phải "đi dạo xong" — đi dạo vốn chẳng có chỗ '
    'nào để xong. Vì thế nó là chữ dùng để rủ nhau: <i>Пойдём погуля́ем?</i></div>'
    '<div class="hd-warn"><b>Không nhận tân ngữ:</b> đi dạo là việc tự thân. Dắt ai hay con gì đi '
    'cùng thì phải mượn giới từ — <i>гуля́ть <b>с соба́кой</b></i> (с + cách 5) = dắt chó đi dạo.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гуля́ть</b> đi dạo · <b>прогу́лка</b> cuộc dạo chơi · '
    '<b>прогу́ливаться</b> đi dạo thong thả</div>'
)

S["потанцевать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">MỘT LÁT, cho vui rồi thôi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-танц-</span>'
    '<span class="hd-gloss">ĐIỆU NHẢY — chính là <b>та́нец</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-евать</span>'
    '<span class="hd-gloss">đuôi dựng động từ, chia thành <b>-у-</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>та́нец</b> cùng một nhà với <i>dance</i> tiếng Anh và <i>Tanz</i> tiếng '
    'Đức, nên mặt chữ nhận ra ngay. <b>по-</b> vẫn là "một lát": nhảy một lúc cho vui, chứ không '
    'phải nhảy hết bài — nhảy làm gì có chỗ để xong.</div>'
    '<div class="hd-why"><b>Chú ý bảng chia:</b> mảnh <b>-ева-</b> rụng mất khi chia, thay bằng '
    '<b>-у-</b>: <i>потанцу́ю, потанцу́ешь, потанцу́ют</i> — cùng nếp với <b>рисова́ть → нарису́ю</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>танцева́ть</b> nhảy múa · <b>та́нец</b> điệu nhảy · '
    '<b>танцо́р</b> vũ công</div>'
)

S["подождать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">подо-</span>'
    '<span class="hd-gloss">= <b>под-</b> thêm <b>-о-</b> cho đọc được trước cụm <b>жд</b>; nghĩa: một chút</span></div>'
    '<div class="hd-row"><span class="hd-piece">-жд-</span>'
    '<span class="hd-gloss">ĐỢI — chính là <b>ждать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>под-</b> vốn là "dưới", nhưng trước động từ nó thu nhỏ hành động lại: '
    'đợi <b>một chút</b>. Đó là lý do <b>подожди́</b> nghĩa là "khoan đã, chờ tí" chứ không phải '
    '"hãy đợi cho xong".</div>'
    '<div class="hd-why"><b>Chú ý bảng chia:</b> quá khứ nhấn thân ở ba dạng nhưng riêng giống '
    '<b>cái</b> dồn trọng âm ra đuôi — <i>подожда́л / подождала́ / подожда́ли</i>. Cả họ <b>ждать</b> '
    'đều vậy (<i>ждала́</i>).</div>'
    '<div class="hd-warn"><b>Đợi cái chắc chắn thì cách 4, đợi cái mơ hồ thì cách 2:</b> '
    '<i>подожда́ть <b>Ма́шу</b></i> (đợi Masha, người cụ thể) nhưng <i>подожда́ть <b>отве́та</b></i> '
    '(đợi một câu trả lời, chưa biết có hay không).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ждать</b> đợi · <b>ожида́ние</b> sự chờ đợi · '
    '<b>неожи́данный</b> bất ngờ, không ngờ tới</div>'
)

S["послушать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">nghe MỘT LƯỢT, một lát rồi thôi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-слуш-</span>'
    '<span class="hd-gloss">NGHE có chủ ý — cùng gốc <b>слух</b> (thính giác)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi nguyên thể, chia đều lớp một</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>слу́шать</b> là chĩa tai vào một cách cố ý; thêm <b>по-</b> thì thành '
    'nghe trọn <b>một lượt</b> rồi thôi — nghe hết bài hát, nghe một lời khuyên.</div>'
    '<div class="hd-warn"><b>Cặp dễ lẫn nhất, và cùng nằm trong lô này:</b> <b>послу́шать</b> = '
    'mình <b>chọn</b> nghe (bật nhạc lên nghe) · <b>услы́шать</b> = âm thanh <b>tự lọt</b> vào tai, '
    'ngoài ý muốn (nghe thấy tiếng động).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>слу́шать</b> lắng nghe · <b>слух</b> thính giác, tin đồn · '
    '<b>слу́шатель</b> thính giả · <b>послу́шный</b> ngoan, biết nghe lời</div>'
)

# ------------------------------------------ с-/вы- kèm nét KẾT QUẢ, у- kèm nét BẮT ĐƯỢC

S["съесть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">съ-</span>'
    '<span class="hd-gloss">= <b>с-</b> (cho HẾT sạch) + dấu cứng <b>ъ</b> bắt buộc chèn khi tiền tố '
    'kết thúc bằng phụ âm mà gặp <b>е ё ю я</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-есть</span>'
    '<span class="hd-gloss">ĂN — chính là động từ <b>есть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dấu <b>ъ</b> không đọc thành âm nào cả, nó chỉ làm hàng rào: "đừng dính '
    '<b>с</b> vào <b>е</b> thành một vần". Còn <b>с-</b> ở đây mang nét <b>hết sạch</b> — ăn cho '
    'hết phần đó, chứ không phải chỉ "đã ăn".</div>'
    '<div class="hd-why"><b>Chú ý bảng chia:</b> <b>есть</b> là một trong vài động từ cổ chia riêng, '
    'không theo lớp nào — số ít cụt ngủn (<i>съем, съешь, съест</i>), số nhiều đột nhiên mọc thêm '
    '<b>-д-</b> và dồn trọng âm ra đuôi (<i>съеди́м, съеди́те, съедя́т</i>); quá khứ cũng không phải '
    '"bỏ -ть thêm -л" mà là <i>съел / съе́ла</i>.</div>'
    '<div class="hd-warn"><b>есть</b> trần trụi có HAI nghĩa — "ăn" và "có, thì là" '
    '(<i>У меня́ есть…</i>). Gắn tiền tố vào thì hết mơ hồ: <b>съесть</b> chỉ còn một nghĩa ăn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>есть</b> ăn · <b>еда́</b> thức ăn · <b>съедо́бный</b> ăn được · '
    '<b>обе́д</b> bữa trưa (<b>об-</b> + gốc <b>-ед-</b>)</div>'
)

S["увидеть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">BẮT ĐƯỢC, chợt nhận ra — không hẳn là tiền tố rỗng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вид-</span>'
    '<span class="hd-gloss">NHÌN, THẤY — cùng gốc <b>вид</b> (cảnh, dáng vẻ)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-еть</span>'
    '<span class="hd-gloss">đuôi nguyên thể, chia lớp hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>ви́деть</b> là có mắt và đang thấy; <b>уви́деть</b> là <b>khoảnh khắc</b> '
    'hình lọt vào mắt — "chợt thấy, thấy được". Vì thế "hẹn gặp lại" là <i>Уви́димся!</i>, nghĩa đen: '
    'rồi ta sẽ thấy nhau.</div>'
    '<div class="hd-why"><b>Chú ý bảng chia:</b> <b>д</b> đổi thành <b>ж</b> đúng một chỗ — ngôi '
    '"tôi" (<i>уви́жу</i>); năm ngôi còn lại giữ nguyên <b>д</b>. Dạng mệnh lệnh <i>уви́дь</i> có in '
    'trong bảng nhưng thực tế gần như không ai dùng — khó mà ra lệnh cho người khác "hãy thấy".</div>'
    '<div class="hd-warn"><b>Thấy khác Xem:</b> <b>ви́деть / уви́деть</b> là việc của mắt, xảy ra dù '
    'mình không định · <b>смотре́ть / посмотре́ть</b> là việc mình chọn làm (nhìn vào, xem).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ви́деть</b> thấy · <b>вид</b> cảnh, dáng vẻ · <b>ви́дно</b> thấy rõ, có vẻ · '
    '<b>свида́ние</b> cuộc hẹn</div>'
)

S["услышать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">BẮT ĐƯỢC, tóm được âm thanh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-слыш-</span>'
    '<span class="hd-gloss">NGHE THẤY — cùng gốc <b>слух</b> (thính giác)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi nguyên thể, nhưng chia lớp HAI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>слы́шать</b> là tai đang bắt được âm thanh, <b>услы́шать</b> là đúng '
    'khoảnh khắc bắt được nó. Không cần cố ý — ngược hẳn với <b>послу́шать</b> ở cùng lô, chữ đó là '
    'mình chủ động chĩa tai vào.</div>'
    '<div class="hd-why"><b>Bẫy đuôi:</b> nhìn đuôi <b>-ать</b> dễ tưởng chia lớp một, nhưng nó nằm '
    'trong nhóm nhỏ chia <b>lớp hai</b>: <i>услы́шу, услы́шишь, услы́шат</i> — cùng nhóm với '
    '<b>слы́шать</b>, <b>держа́ть</b>, <b>дыша́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>слы́шать</b> nghe thấy · <b>слух</b> thính giác, tin đồn · '
    '<b>слы́шно</b> nghe được · <b>слу́шать</b> lắng nghe</div>'
)

S["смочь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">đóng dấu hoàn thành, kèm nét "xoay xở được"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мочь</span>'
    '<span class="hd-gloss">CÓ THỂ — chính là <b>мочь</b>, gốc <b>мог-/мощ-</b> = sức</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>мочь</b> là có khả năng nói chung; <b>смочь</b> là lần này <b>xoay xở '
    'làm được</b>. Vì vậy nó hầu như chỉ sống ở tương lai và quá khứ: <i>Я не смог</i> = tôi đã '
    'không làm nổi. Gốc <b>мощ-</b> lộ ra ở <b>по́мощь</b> (sự giúp đỡ) và <b>мо́щный</b> (mạnh).</div>'
    '<div class="hd-why"><b>Chú ý bảng chia:</b> gốc đảo <b>г ↔ ж</b> — chỉ hai đầu bảng giữ '
    '<b>г</b> (<i>смогу́ … смо́гут</i>), bốn ngôi giữa thành <b>ж</b> (<i>смо́жешь, смо́жет, смо́жем, '
    'смо́жете</i>). Quá khứ giống đực cụt hẳn đuôi <b>-л</b> (<i>смог</i>), ba dạng còn lại dồn trọng '
    'âm ra đuôi (<i>смогла́, смогло́, смогли́</i>).</div>'
    '<div class="hd-warn"><b>Luôn kéo theo một động từ nguyên thể:</b> <i>Я смогу́ прийти́</i> = '
    'tôi sẽ đến được. Nó không đứng với danh từ, và cũng gần như không có dạng mệnh lệnh.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мочь</b> có thể · <b>мо́жно</b> được phép · <b>по́мощь</b> sự giúp đỡ · '
    '<b>помо́чь</b> giúp · <b>мо́щный</b> mạnh mẽ</div>'
)

# ------------------------------------------------------------------ field Vietnamese
# CHỈ sửa chỗ dòng tiếng Việt tự nó SAI hoặc mơ hồ về NGHĨA.
# KHÔNG sửa chỉ vì trùng nghĩa với bản chưa hoàn thành — mặt đề bài đã in badge
# PERF/IMPF, badge lo phần thể rồi (đo thật trên 976 thẻ: không cặp nào của k59
# bị badge bỏ sót).

# Thiếu CÁCH mà động từ chi phối — không field nào chứa thông tin này (README §2c).
V['позвонить'] = 'gọi điện thoại, rung chuông'

# Mơ hồ THẬT về nghĩa, không phải về thể: "nghe" trần trụi trỏ đúng vào услышать,
# cũng là thẻ PERF + v trong chính lô này. Tách bằng nét chủ động / bị động.
V['послушать'] = 'lắng nghe, nghe một lượt'
