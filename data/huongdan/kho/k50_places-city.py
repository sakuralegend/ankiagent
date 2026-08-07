# -*- coding: utf-8 -*-
"""k50 — places::city: phương tiện đi lại và các điểm mốc giao thông. Trục của
lô: phần lớn là TỪ GHÉP đọc ra được (gốc + -о- + -лёт/-ход/-фор) hoặc từ mượn
quốc tế chẻ theo mảnh Latin/Hy Lạp — nhìn ra mảnh là ra nghĩa, không phải học vẹt."""

S = {}
V = {}

S["транспорт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">транс-</span>'
    '<span class="hd-gloss">QUA, XUYÊN SANG bên kia</span></div>'
    '<div class="hd-row"><span class="hd-piece">-порт</span>'
    '<span class="hd-gloss">MANG, CHỞ (Latin <i>portare</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng chữ <i>transport</i> tiếng Anh: "chở qua". Cùng mảnh -порт '
    'với <b>и́мпорт</b> (chở VÀO) và <b>э́кспорт</b> (chở RA) — ba từ chỉ khác nhau ở '
    'tiền tố chỉ hướng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тра́нспортный</b> thuộc giao thông · <b>и́мпорт</b> nhập khẩu · '
    '<b>э́кспорт</b> xuất khẩu</div>'
)

S["метро"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">метро́</span>'
    '<span class="hd-gloss">năm chữ đầu cắt ra từ <b>метрополите́н</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiếng Pháp gọi đường sắt ngầm Paris là <i>métropolitain</i> — '
    'đường sắt của THỦ ĐÔ (Hy Lạp <i>metro-polis</i> "thành phố mẹ"). Người Nga giữ lại '
    'đúng năm chữ đầu, và bấy nhiêu đã là cả từ.</div>'
    '<div class="hd-warn">Từ mượn BẤT BIẾN: mọi ô trong bảng dưới đều là <b>метро́</b>. '
    'Muốn biết nó đang ở cách nào phải nhìn từ đứng cạnh: <i>на метро́</i>, '
    '<i>ста́нция метро́</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>метрополите́н</b> dạng đầy đủ, nay chỉ còn gặp trong văn bản '
    'chính thức</div>'
)

S["такси"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">такси́</span>'
    '<span class="hd-gloss">mượn nguyên khối từ Pháp <i>taximètre</i> — đồng hồ đo TIỀN '
    'CƯỚC; không có mảnh Nga nào bên trong</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái được đặt tên trước là chiếc đồng hồ tính cước, rồi tên đó '
    'trùm sang cả chiếc xe. Từ vào tiếng Nga y nguyên nên nó cũng không chịu biến cách.</div>'
    '<div class="hd-warn">Bất biến hệt <b>метро́</b>: <i>на такси́</i>, <i>два такси́</i>, '
    '<i>в такси́</i> — mọi ô trong bảng đều là <b>такси́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>такси́ст</b> tài xế taxi · <b>тури́ст</b> khách du lịch — cùng '
    'đuôi -и́ст chỉ NGƯỜI theo một việc</div>'
)

S["трамвай"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">трам-</span>'
    '<span class="hd-gloss">TOA CHẠY TRÊN RAY (<i>tram</i> tiếng Anh)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва́й</span>'
    '<span class="hd-gloss">ĐƯỜNG, tuyến (<i>way</i> tiếng Anh)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đọc trại thẳng chữ <i>tramway</i>: "đường ray cho toa". Đây là '
    'mượn phiên âm nguyên khối — hai mảnh đều là tiếng Anh, tiếng Nga hầu như không dùng lại '
    'chúng ở chỗ khác.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>трамва́йный</b> thuộc về tàu điện — tiếng Nga chỉ đẻ thêm được '
    'tính từ này</div>'
)

S["троллейбус"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тролле́й-</span>'
    '<span class="hd-gloss">CẦN LẤY ĐIỆN trượt trên dây (<i>trolley</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бус</span>'
    '<span class="hd-gloss">XE CHỞ KHÁCH, cắt ra từ <b>авто́бус</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ghép hai nửa: chiếc buýt ăn điện qua cái cần trên nóc. Mảnh -бус '
    'đi khắp nơi, cứ thấy nó là biết đang nói tới một loại xe chở khách.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>авто́бус</b> xe buýt · <b>микроавто́бус</b> xe buýt nhỏ</div>'
)

S["поезд"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố KHỞI HÀNH — cùng cái по- trong <b>пое́хать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-езд</span>'
    '<span class="hd-gloss">ĐI BẰNG XE — gốc езд/езж của <b>е́хать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc езд đã gặp ở <b>пое́здка</b> và <b>прие́зд</b>. <b>По́езд</b> là '
    'cái "đi xe" đã đông cứng thành vật: đoàn toa chạy theo lộ trình định sẵn.</div>'
    '<div class="hd-warn">Số nhiều nhảy trọng âm ra đuôi -а́ rồi giữ nguyên đó suốt bảng: '
    '<b>по́езд</b> → <b>поезда́</b>, <b>поездо́в</b>, <b>поезда́х</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пое́здка</b> chuyến đi · <b>прие́зд</b> sự đến nơi · '
    '<b>отъе́зд</b> sự rời đi · <b>е́хать</b> đi xe</div>'
)

S["вагон"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ваго́н</span>'
    '<span class="hd-gloss">mượn nguyên khối — chính là <i>wagon</i> tiếng Anh, '
    '<i>Wagen</i> tiếng Đức</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỉ đổi mặt chữ w → в là ra. Nhưng nghĩa hẹp lại: tiếng Nga dùng '
    'cho toa nằm trong một đoàn tàu hay tàu điện, không dùng cho xe ngựa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ваго́нчик</b> toa nhỏ, ca bin di động — đuôi -чик làm nhỏ đi</div>'
)

S["самолёт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сам-</span>'
    '<span class="hd-gloss">TỰ MÌNH (<b>сам</b> chính mình)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о-</span>'
    '<span class="hd-gloss">nguyên âm nối hai gốc lại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лёт</span>'
    '<span class="hd-gloss">BAY — gốc лёт/лет của <b>лете́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen "vật tự bay". Khuôn gốc + -о- + -лёт này dựng luôn ra '
    '<b>вертолёт</b> ngay trong lô, nên học một lần dùng được cả hai từ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лета́ть</b> bay · <b>полёт</b> chuyến bay · <b>лётчик</b> phi '
    'công</div>'
)

S["вертолёт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">верт-</span>'
    '<span class="hd-gloss">XOAY TRÒN (<b>верте́ть</b> xoay)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о-</span>'
    '<span class="hd-gloss">nguyên âm nối</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лёт</span>'
    '<span class="hd-gloss">BAY — cùng mảnh với <b>самолёт</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen "bay bằng cách xoay" — đúng cái cánh quạt trên nóc. '
    'Cùng một khuôn với <b>самолёт</b>, chỉ thay gốc đầu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>верте́ть</b> xoay · <b>полёт</b> chuyến bay · <b>самолёт</b> '
    'máy bay</div>'
)

S["теплоход"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">тепл-</span>'
    '<span class="hd-gloss">NHIỆT, hơi ấm (<b>тёплый</b> ấm)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о-</span>'
    '<span class="hd-gloss">nguyên âm nối</span></div>'
    '<div class="hd-row"><span class="hd-piece">-хо́д</span>'
    '<span class="hd-gloss">SỰ CHẠY, đi — gốc ход của <b>ходи́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen "chạy bằng nhiệt": tàu máy nổ, đặt tên đối lại với '
    '<b>парохо́д</b> "chạy bằng hơi" (<i>пар</i>). Đuôi -ход báo một phương tiện tự chạy được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ходи́ть</b> đi bộ · <b>вы́ход</b> lối ra · <b>парохо́д</b> tàu '
    'hơi nước · <b>тёплый</b> ấm</div>'
)

# Từ mượn đứng một mình: tiếng Nga không đẻ ra từ phái sinh nào từ ка́тер
# -> BỎ HẲN mục Họ hàng (README §2, đây là lựa chọn có ý thức, không phải quên).
S["катер"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ка́тер</span>'
    '<span class="hd-gloss">mượn nguyên khối từ <i>cutter</i> tiếng Anh — loại xuồng nhỏ '
    'chạy nhanh</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không có mảnh Nga nào bên trong. Đừng nối nó với <b>кати́ть</b> '
    '"lăn": hai từ chỉ trùng ba chữ đầu chứ không cùng gốc.</div>'
    '<div class="hd-warn">Số nhiều nhảy trọng âm ra đuôi -а́ y hệt <b>по́езд</b>: '
    '<b>ка́тер</b> → <b>катера́</b>, <b>катеро́в</b>.</div>'
)

S["велосипед"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">велоси-</span>'
    '<span class="hd-gloss">NHANH (Latin <i>velox</i>, như <i>velocity</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пе́д</span>'
    '<span class="hd-gloss">CHÂN (Latin <i>pes / pedis</i>, như <i>pedal</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen "chân nhanh" — cỗ máy giúp đôi chân đi nhanh hơn. Nhớ '
    'hai chữ Anh <i>velocity</i> + <i>pedal</i> là dựng lại được cả từ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>велосипеди́ст</b> người đi xe đạp · <b>мопе́д</b> giữ đúng mảnh '
    '-пед · <b>педа́ль</b> bàn đạp</div>'
)

S["мопед"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мо-</span>'
    '<span class="hd-gloss">cắt từ <b>мото́р</b> — ĐỘNG CƠ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пе́д</span>'
    '<span class="hd-gloss">cắt từ <b>велосипе́д</b> / <b>педа́ль</b> — BÀN ĐẠP</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ ghép cắt cụt: xe đạp gắn động cơ mà vẫn còn bàn đạp. Tiếng Nga '
    'mượn sẵn cả từ này từ châu Âu, nhưng chẻ ra hai mảnh thì vẫn đọc đúng như vậy.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мото́р</b> động cơ · <b>велосипе́д</b> xe đạp · <b>мотоци́кл</b> '
    'xe mô tô</div>'
)

S["мотоцикл"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мото-</span>'
    '<span class="hd-gloss">ĐỘNG CƠ (<b>мото́р</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ци́кл</span>'
    '<span class="hd-gloss">VÒNG, bánh xe (Hy Lạp <i>kyklos</i>, như <i>bicycle</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ghép thẳng thành <i>motor-cycle</i>: bánh xe có động cơ. Mảnh мото- '
    'dùng chung với <b>мопе́д</b>, mảnh -цикл chính là chữ <i>cycle</i> trong <i>bicycle</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мото́р</b> động cơ · <b>мопе́д</b> xe gắn máy · <b>цикл</b> '
    'chu kỳ</div>'
)

S["аэропорт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">аэро-</span>'
    '<span class="hd-gloss">KHÔNG KHÍ, hàng không (Hy Lạp <i>aer</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-по́рт</span>'
    '<span class="hd-gloss">CẢNG (Latin <i>portus</i>) — đứng riêng cũng là một từ: '
    '<b>порт</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng nghĩa "cảng hàng không", tiếng Việt gọi y hệt. Mảnh аэро- còn '
    'thấy ở <b>аэрофло́т</b>.</div>'
    '<div class="hd-warn">Cách 6 có HAI dạng và chúng chia việc: nói Ở ĐÂU thì '
    '<b>в аэропорту́</b> (trọng âm nhảy ra đuôi), nói VỀ nó thì <b>об аэропо́рте</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>порт</b> cảng · <b>Аэрофло́т</b> hãng hàng không Nga</div>'
)

S["станция"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">стан-</span>'
    '<span class="hd-gloss">ĐỨNG, chỗ dừng lại (Latin <i>stare</i> đứng)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ция</span>'
    '<span class="hd-gloss">đuôi Latin <i>-tio</i> hoá thành danh từ Nga, đều giống '
    'cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>station</i> tiếng Anh. Đuôi -ция là cửa vào của cả kho '
    'từ quốc tế trong tiếng Nga, và nó kéo theo giống cái.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>вокза́л</b>: вокза́л là TOÀ NHÀ ga lớn, còn <b>ста́нция</b> là điểm dừng trên tuyến — ga xép, ga tàu điện ngầm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>на́ция</b> dân tộc · <b>по́рция</b> khẩu phần — cùng đuôi -ция '
    'mượn Latin</div>'
)

S["стоянка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">стоя́-</span>'
    '<span class="hd-gloss">ĐỨNG, đỗ lại (<b>стоя́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-нка</span>'
    '<span class="hd-gloss">đuôi dựng danh từ chỉ CHỖ / việc, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa suy thẳng ra: "chỗ đứng". Tiếng Nga dùng <b>стоя́ть</b> cho '
    'cả người đứng lẫn xe đỗ, nên chỗ xe đứng yên chính là <b>стоя́нка</b>.</div>'
    '<div class="hd-warn">Chỗ duy nhất phải nhớ: cách 2 số nhiều chèn thêm о cho khỏi đọng '
    'cụm -нк — <b>стоя́нок</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стоя́ть</b> đứng, đỗ · <b>остано́вка</b> bến dừng — cùng nhánh '
    'gốc сто-/ста- "đứng"</div>'
)

S["светофор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">свет-</span>'
    '<span class="hd-gloss">ÁNH SÁNG (<b>свет</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о-</span>'
    '<span class="hd-gloss">nguyên âm nối</span></div>'
    '<div class="hd-row"><span class="hd-piece">-фо́р</span>'
    '<span class="hd-gloss">KẺ MANG (Hy Lạp <i>-phoros</i> mang, vác)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen "kẻ mang ánh sáng". Mảnh -фор ấy cũng nằm trong '
    '<b>семафо́р</b> và <b>фо́сфор</b> — thấy nó là có ai đó đang mang một thứ gì.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>свет</b> ánh sáng · <b>све́тлый</b> sáng sủa · <b>семафо́р</b> '
    'cột tín hiệu đường sắt</div>'
)

S["стадион"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">стадио́н</span>'
    '<span class="hd-gloss">mượn nguyên khối từ Hy Lạp <i>stadion</i> — vốn là ĐƠN VỊ ĐO '
    'dài chừng 185 m</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đường chạy dài đúng một <i>stadion</i> đã đặt tên cho cả cái sân '
    'bao quanh nó. Chính là <i>stadium</i> tiếng Anh; không có mảnh Nga nào bên trong.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ста́дия</b> giai đoạn — theo từ nguyên là cùng chữ Hy Lạp đó, '
    'nhưng vào tiếng Nga bằng lối sách vở nên nghĩa dừng ở "một chặng"</div>'
)

S["общежитие"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">общ-</span>'
    '<span class="hd-gloss">CHUNG (<b>о́бщий</b> chung)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е-</span>'
    '<span class="hd-gloss">nguyên âm nối — sau щ thì dùng е, không phải о</span></div>'
    '<div class="hd-row"><span class="hd-piece">-жи-</span>'
    '<span class="hd-gloss">SỐNG (<b>жить</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тие</span>'
    '<span class="hd-gloss">đuôi dựng danh từ, giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen "việc sống chung" → cái nhà để sống chung. Đuôi -ие báo '
    'ngay danh từ giống trung, cùng khuôn với <b>заня́тие</b> "buổi học".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>о́бщий</b> chung · <b>о́бщество</b> xã hội · <b>жить</b> sống · '
    '<b>жизнь</b> cuộc sống</div>'
)

# --------------------------------------------------------------------------
# Field `Vietnamese` — đề bài của deck 1-go (README §2c): THUẦN danh sách nghĩa.
# Chỉ ghi những từ THẬT SỰ cần sửa.
V["транспорт"] = "phương tiện giao thông, sự vận chuyển"
V["теплоход"] = "tàu thuỷ"
V["катер"] = "ca nô, xuồng máy, tàu cao tốc"
V["мопед"] = "xe gắn máy, xe đạp máy"
V["мотоцикл"] = "xe mô tô, xe máy"
V["аэропорт"] = "sân bay, cảng hàng không"
# "ga" trơn KHÔNG dùng được: nó đã là nghĩa của газ ("khí, chất khí, ga").
V["станция"] = "ga tàu, trạm"
