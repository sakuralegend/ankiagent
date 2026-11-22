# -*- coding: utf-8 -*-
"""k177 — language::communication (lô trộn): giao tiếp, văn bản, tranh cãi, vị trí, -либо.

Chỗ cần nhất quán trong lô:
(1) họ -пис- VIẾT: описа́ние chẻ đúng khuôn thẻ описа́ть [k135] «о- VÒNG QUANH + -пис-»;
    на́дпись dùng cùng gốc, đối với по́дпись (над- TRÊN / под- DƯỚI).
(2) обще́ние: gốc о́бщ- CHUNG như thẻ о́бщий [k108] và сообще́ние [k100].
(3) -либо (что́-либо, како́й-либо): «bất cứ / bất kỳ», văn viết — KHÔNG phải «… nào đó» của -то.
    Lời so sánh đặt ở что́-либо; како́й-либо dẫn chiếu một dòng.
(4) верх: khớp thẻ вверх/наве́рх/све́рху/ве́рхний đã có — ở đây chỉ dạy chỗ BẤT THƯỜNG của chính верх.
(5) спор: khớp thẻ спо́рить [k77]; lời báo oan спорт/тра́нспорт đã nằm ở thẻ đó, không lặp.
(6) кислоро́д: khớp dòng họ hàng ở thẻ ки́слый [k21] «ки́слый + gốc род sinh ra».
Họ hàng cố ý vắng: không thẻ nào (ген, сканда́л, инстру́кция, табли́ца là từ mượn nhưng vẫn có
phái sinh Nga thật).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "верх": "phần trên, đỉnh, nóc, tột đỉnh",                    # the ultimate (верх глу́пости)
    "поход": "chuyến đi bộ đường dài, chuyến cắm trại, chuyến đi, cuộc hành quân, chiến dịch",  # campaign / march
    "груз": "hàng hóa, lô hàng, vật nặng, gánh nặng",            # burden
    "какой-либо": "bất kỳ… nào, bất cứ… nào",                    # any whatsoever; «nào đó» là của како́й-то
    "что-либо": "bất cứ thứ gì, bất cứ điều gì",                 # anything at all; «cái gì đó» là của что́-то
    "выпуск": "số phát hành, kỳ, tập, bản tin, sự phát hành, sản lượng, khoá tốt nghiệp",  # episode, bulletin, release, graduating class
    "телевидение": "truyền hình, ngành truyền hình, đài truyền hình",  # «tivi» (cái máy) là телеви́зор
}

# ------------------------------------------------------------------------ верх
S["верх"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn <b>верх</b> = ĐỈNH, PHẦN TRÊN — không chẻ được, nhưng chính nó '
    'là lõi của <b>вверх</b>, <b>наверху́</b>, <b>све́рху</b>, <b>ве́рхний</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai chỗ lệch: số nhiều trọng âm nhảy ra đuôi — <b>верхи́</b> (còn có '
    'nghĩa «giới chóp bu»); và «ở trên đỉnh» dùng đuôi riêng <b>-у́</b>: <b>на верху́</b>, còn '
    '«nói về phần trên» vẫn là <b>о ве́рхе</b>. Đối của nó: <b>низ</b> phần dưới.</div>'
    '<div class="hd-warn"><b>на верху́ горы́</b> (hai chữ) = trên đỉnh núi · <b>наверху́</b> '
    '(viết liền) = ở trên, trên lầu — trạng từ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ве́рхний</b> ở trên · <b>вверх</b> lên trên · <b>наверху́</b> ở '
    'trên · <b>све́рху</b> từ trên xuống · <b>верши́на</b> đỉnh núi (х → ш)</div>'
)

# ------------------------------------------------------------------------ вдоль
S["вдоль"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO, THEO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-доль</span>'
    '<span class="hd-gloss">CHIỀU DÀI (từ cổ)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Theo chiều dài» của một vật ⇒ dọc theo. Là giới từ thì đòi '
    '<b>cách 2</b>: <b>вдоль реки́</b> dọc bờ sông. Đứng một mình là trạng từ: '
    '<b>разре́зать вдоль</b> cắt theo chiều dọc. Đối của nó: <b>поперёк</b> ngang qua.</div>'
    '<div class="hd-warn"><b>вдоль и поперёк</b> = khắp ngang dọc, tường tận: '
    '<b>знать вдоль и поперёк</b> thuộc như lòng bàn tay.</div>'
    '<div class="hd-warn">⚠️ Mức tin: <b>-доль</b> cùng gốc với <b>длина́</b> chiều dài, '
    '<b>до́лгий</b> lâu — đây là từ nguyên, không phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>продо́льный</b> theo chiều dọc · <b>поперёк</b> ngang qua (đối '
    'nghĩa)</div>'
)

# --------------------------------------------------------------- присутствовать
S["присутствовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">Ở BÊN, TẠI CHỖ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сутств-</span>'
    '<span class="hd-gloss">SỰ HIỆN HỮU — gốc «đang có», như <b>существова́ть</b> tồn tại (т → щ)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-овать</span>'
    '<span class="hd-gloss">đuôi động từ: <b>-ова-</b> → <b>-у-</b> khi chia</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đang hiện hữu tại chỗ» ⇒ có mặt. Thay <b>при-</b> bằng <b>от-</b> '
    'RỜI KHỎI là ra đối nghĩa: <b>отсу́тствовать</b> vắng mặt. Chia: <b>я прису́тствую</b>, '
    '<b>ты прису́тствуешь</b>.</div>'
    '<div class="hd-warn">Có mặt Ở một sự kiện: <b>на</b> + cách 6 — <b>прису́тствовать на '
    'собра́нии</b>, <b>на уро́ке</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прису́тствие</b> sự có mặt · <b>отсу́тствовать</b> vắng mặt · '
    '<b>отсу́тствие</b> sự vắng mặt · <b>существова́ть</b> tồn tại</div>'
)

# ------------------------------------------------------------------------ поход
S["поход"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">LÊN ĐƯỜNG — như trong <b>пойти́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ход</span>'
    '<span class="hd-gloss">ĐI — gốc của <b>ходи́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Một lần lên đường đi» ⇒ chuyến đi; đi đông người, dài ngày thì thành '
    'cuộc hành quân, chiến dịch. Khẩu ngữ dùng cho cả chuyến đi ngắn: <b>похо́д в кино́</b> '
    'một buổi đi xem phim.</div>'
    '<div class="hd-warn"><b>идти́ в похо́д</b> = đi dã ngoại, đi bộ đường dài và cắm trại.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ходи́ть</b> đi · <b>похо́дка</b> dáng đi · <b>вход</b> lối vào · '
    '<b>вы́ход</b> lối ra · <b>перехо́д</b> chỗ sang đường</div>'
)

# ------------------------------------------------------------------------- груз
S["груз"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn <b>груз</b> = VẬT NẶNG, HÀNG CHỞ — không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc này dựng cả họ chất/dỡ hàng: <b>загрузи́ть</b> chất lên, '
    '<b>разгрузи́ть</b> dỡ xuống — trên máy tính <b>загрузи́ть</b> chính là «tải» (load). '
    'Nghĩa bóng: <b>груз отве́тственности</b> gánh nặng trách nhiệm.</div>'
    '<div class="hd-warn"><b>Гру́зия</b> (nước Gruzia) KHÔNG cùng gốc — tên nước đến từ tiếng '
    'nước ngoài, chỉ trùng mặt chữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>грузови́к</b> xe tải · <b>грузи́ть</b> chất hàng · <b>гру́зчик</b> '
    'người bốc vác · <b>нагру́зка</b> tải trọng, khối lượng công việc</div>'
)

# ------------------------------------------------------------------ какой-либо
S["какой-либо"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">како́й</span>'
    '<span class="hd-gloss">NÀO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-либо</span>'
    '<span class="hd-gloss">từ <b>ли́бо</b> «hoặc» ⇒ cái nào cũng được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Bất kỳ … nào», chưa nhắm cái nào — giọng văn viết. Gặp nhiều nhất '
    'trong câu hỏi và sau <b>без</b>: <b>без каки́х-либо пробле́м</b> = không gặp bất kỳ vấn '
    'đề nào. Chỉ phần <b>како́й</b> đổi đuôi. So với -то, -нибудь: xem thẻ <b>что́-либо</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>како́й</b> nào · <b>како́й-то</b> nào đó · <b>како́й-нибудь</b> '
    'gì đó · <b>что́-либо</b> bất cứ thứ gì</div>'
)

# -------------------------------------------------------------------- что-либо
S["что-либо"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">что</span>'
    '<span class="hd-gloss">CÁI GÌ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-либо</span>'
    '<span class="hd-gloss">từ <b>ли́бо</b> «hoặc» ⇒ cái này hoặc cái kia, cái nào cũng được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Bất cứ thứ gì» — nghĩa gần như <b>что́-нибудь</b>, nhưng là giọng '
    'văn viết, thông báo, giấy tờ: <b>Е́сли что́-либо случи́тся, звони́те</b> = Nếu có bất cứ '
    'chuyện gì xảy ra, hãy gọi. Chỉ phần <b>что</b> biến cách: <b>чего́-либо</b>.</div>'
    '<div class="hd-warn"><b>что́-либо</b> = bất cứ gì, chưa nhắm cái nào · <b>что́-то</b> = '
    'một cái gì đó CÓ THẬT, chỉ là không rõ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>что</b> cái gì · <b>что́-то</b> cái gì đó · <b>что́-нибудь</b> bất '
    'cứ thứ gì · <b>кто́-либо</b> bất kỳ ai · <b>ли́бо</b> hoặc là</div>'
)

# ----------------------------------------------------------------------- выпуск
S["выпуск"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span>'
    '<span class="hd-gloss">RA NGOÀI — trong danh từ này mang trọng âm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пуск</span>'
    '<span class="hd-gloss">THẢ, CHO ĐI — gốc của <b>пусти́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mọi nghĩa đều là «thả ra ngoài»: nhà máy thả hàng ra ⇒ sản lượng; '
    'toà soạn thả ra ⇒ số báo, tập phim; trường thả học sinh ra ⇒ khoá tốt nghiệp. Danh '
    'từ không đuôi, cùng thân <b>-пуск-</b> với <b>выпуска́ть</b>.</div>'
    '<div class="hd-warn"><b>вы́пуск новосте́й</b> = bản tin thời sự.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́пустить</b> / <b>выпуска́ть</b> thả ra, phát hành · '
    '<b>выпускни́к</b> người tốt nghiệp · <b>о́тпуск</b> kỳ nghỉ phép · <b>про́пуск</b> thẻ '
    'ra vào</div>'
)

# ---------------------------------------------------------------------- надпись
S["надпись"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">над-</span>'
    '<span class="hd-gloss">TRÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пис-</span>'
    '<span class="hd-gloss">VIẾT — gốc của <b>писа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ь</span>'
    '<span class="hd-gloss">→ danh từ GIỐNG CÁI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chữ viết LÊN TRÊN mặt một vật — biển, bia, bìa sách. Đổi tiền tố là '
    'đổi chỗ viết: <b>по́дпись</b> viết ở DƯỚI cuối văn bản ⇒ chữ ký. Danh từ đuôi '
    '<b>-пись</b> đều giống cái, trọng âm rơi vào tiền tố: <b>на́дпись</b>, <b>по́дпись</b>, '
    '<b>за́пись</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>писа́ть</b> viết · <b>надписа́ть</b> đề chữ lên · <b>по́дпись</b> '
    'chữ ký · <b>за́пись</b> bản ghi · <b>описа́ние</b> bản mô tả</div>'
)

# ------------------------------------------------------------------- инструкция
S["инструкция"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">инструк-</span>'
    '<span class="hd-gloss">từ mượn, gốc Latin <i>instruct-</i> «chỉ bảo, trang bị»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ция</span>'
    '<span class="hd-gloss">= đuôi <i>-tion</i> tiếng Anh, luôn giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>instruction</i>: đổi <i>-tion</i> thành <b>-ция</b>, như '
    '<b>ста́нция</b> <i>station</i>, <b>информа́ция</b> <i>information</i>.</div>'
    '<div class="hd-warn">Hướng dẫn VỀ cái gì: <b>по</b> + cách 3 — <b>инстру́кция по '
    'эксплуата́ции</b> = hướng dẫn sử dụng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>инстру́ктор</b> người hướng dẫn (dạy lái xe, thể thao) · '
    '<b>инструкта́ж</b> buổi phổ biến quy tắc</div>'
)

# ---------------------------------------------------------------------- таблица
S["таблица"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">табл-</span>'
    '<span class="hd-gloss">TẤM BẢNG — từ mượn, gốc Latin <i>tabula</i> (Anh <i>table</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ца</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bảng kẻ ô chứa số liệu: <b>табли́ца умноже́ния</b> bảng cửu chương, '
    '<b>табли́ца Менделе́ева</b> bảng tuần hoàn.</div>'
    '<div class="hd-warn">Bẫy tiếng Anh: <i>table</i> «cái bàn» là <b>стол</b> — '
    '<b>табли́ца</b> chỉ là bảng biểu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>табли́чка</b> tấm biển nhỏ · <b>табло́</b> bảng điện tử</div>'
)

# --------------------------------------------------------------------- кислород
S["кислород"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кисл-</span>'
    '<span class="hd-gloss">CHUA — gốc của <b>ки́слый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-о-</span>'
    '<span class="hd-gloss">nguyên âm nối, không mang nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-род</span>'
    '<span class="hd-gloss">SINH RA — gốc của <b>род</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Chất sinh ra vị chua» — dịch từng mảnh từ <i>oxygen</i> (Hy Lạp '
    '<i>oxys</i> chua + <i>-gen</i> sinh ra). Hai nguyên tố khác dựng y hệt: <b>водоро́д</b> '
    'hydro (sinh ra nước), <b>углеро́д</b> cacbon (sinh ra than).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ки́слый</b> chua · <b>кислота́</b> axit · <b>водоро́д</b> hydro · '
    '<b>углеро́д</b> cacbon</div>'
)

# -------------------------------------------------------------------------- ген
S["ген"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn (Anh <i>gene</i>, Đức <i>Gen</i>) — không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giống hệt tiếng Anh. Giống đực, biến cách đều: <b>ге́на</b>, '
    '<b>ге́ны</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гене́тика</b> di truyền học · <b>генети́ческий</b> thuộc về di '
    'truyền</div>'
)

# --------------------------------------------------------------------- описание
S["описание"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">VÒNG QUANH, khắp mặt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пис-</span>'
    '<span class="hd-gloss">VIẾT — gốc của <b>писа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ние</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>описа́ть</b> (thẻ đã học): viết vòng quanh mọi mặt '
    'một vật ⇒ bản mô tả — y như tiếng Anh <i>de-scription</i> cũng chứa «viết».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>описа́ть</b> / <b>опи́сывать</b> mô tả · <b>писа́ть</b> viết · '
    '<b>на́дпись</b> dòng chữ · <b>о́пись</b> bản kê</div>'
)

# ------------------------------------------------------------------ телевидение
S["телевидение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">теле-</span>'
    '<span class="hd-gloss">XA (Hy Lạp, như <b>телефо́н</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вид-</span>'
    '<span class="hd-gloss">NHÌN — gốc của <b>ви́деть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Nhìn từ xa» — dịch đúng từng mảnh <i>tele-vision</i>; gốc '
    '<b>вид-</b> và Latin <i>vid-</i> (video) là họ hàng xa thật. Làm việc ở đài: '
    '<b>рабо́тать на телеви́дении</b>.</div>'
    '<div class="hd-warn"><b>телеви́дение</b> = ngành, sóng truyền hình · <b>телеви́зор</b> = '
    'cái máy tivi. «Xem trên tivi» là <b>по телеви́зору</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ви́деть</b> nhìn thấy · <b>телеви́зор</b> máy tivi · <b>вид</b> '
    'quang cảnh, dáng vẻ</div>'
)

# ---------------------------------------------------------------------- общение
S["общение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">общ-</span>'
    '<span class="hd-gloss">CHUNG — gốc của <b>о́бщий</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ние</span>'
    '<span class="hd-gloss">→ danh từ giống trung, từ <b>обща́ться</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho thành CHUNG giữa người với người ⇒ giao tiếp, giao lưu. Cùng '
    'gốc ấy: <b>сообще́ние</b> = làm cho mọi người cùng biết ⇒ tin nhắn. Giao tiếp VỚI ai: '
    '<b>с</b> + cách 5 — <b>обще́ние с друзья́ми</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обща́ться</b> giao tiếp · <b>о́бщий</b> chung · <b>о́бщество</b> xã '
    'hội · <b>сообще́ние</b> tin nhắn · <b>общи́тельный</b> cởi mở, dễ gần</div>'
)

# ---------------------------------------------------------------------- скандал
S["скандал"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn (Pháp <i>scandale</i>, Anh <i>scandal</i>) — không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ngoài «vụ bê bối» như tiếng Anh, trong đời thường nó hay là trận cãi '
    'vã ầm ĩ giữa người với người.</div>'
    '<div class="hd-warn"><b>устро́ить сканда́л</b> = làm ầm lên, gây chuyện om sòm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сканда́льный</b> tai tiếng, gây ồn ào · <b>сканда́лить</b> làm ầm '
    'ĩ, gây sự</div>'
)

# ------------------------------------------------------------------------ обман
S["обман"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">VÒNG QUANH, qua mặt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ман</span>'
    '<span class="hd-gloss">DỤ, VẪY GỌI — gốc của <b>мани́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dụ người ta đi vòng qua sự thật ⇒ lừa. Danh từ không đuôi, rút thẳng '
    'từ <b>обману́ть</b> lừa.</div>'
    '<div class="hd-warn"><b>обма́н зре́ния</b> = ảo giác thị giác (nghĩa đen: mắt bị lừa).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обману́ть</b> / <b>обма́нывать</b> lừa · <b>обма́нщик</b> kẻ lừa '
    'đảo · <b>мани́ть</b> vẫy gọi, quyến rũ · <b>замани́ть</b> dụ vào</div>'
)

# ------------------------------------------------------------------------- спор
S["спор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn <b>спор</b> — không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>спо́рить</b> (thẻ đã học) — cuộc tranh cãi. Cãi VỀ '
    'chuyện gì: <b>о</b> + cách 6 — <b>спор о поли́тике</b>. Câu hay dùng: <b>Не спо́рю</b> = '
    'tôi không cãi (tức là đồng ý).</div>'
    '<div class="hd-warn"><b>на спор</b> = để cá cược, vì bị thách: <b>сде́лать на спор</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спо́рить</b> tranh cãi · <b>поспо́рить</b> cãi nhau, cá cược · '
    '<b>спо́рный</b> gây tranh cãi · <b>бесспо́рно</b> không bàn cãi</div>'
)

B = {
    "docbangmat": 71,
    "loitubat": 2,
    "nguonsai": 2,
    "baolen": [
        "VA CHẠM KHÔNG GỠ ĐƯỢC BẰNG NGHĨA: что́-либо ↔ что́-нибудь — gloss tiếng Anh của HAI thẻ trùng nguyên văn «anything at all», cùng badge pron; khác nhau chỉ ở văn phong (-либо văn viết), thứ bị cấm ghi vào đề. V что-либо đã viết «bất cứ thứ gì, bất cứ điều gì»; nếu Vietnamese của что-нибудь cũng chứa «bất cứ thứ gì» thì đề 1-go không có đáp án duy nhất. Không thêm ngoặc — cần user quyết.",
        "Có thể va chạm (CHƯA kiểm được — không được đọc Anki): какой-либо V «bất kỳ… nào, bất cứ… nào» có thể nằm gọn trong V của любо́й (gloss «any, either, whichever…», cùng badge pron). Luồng chính chạy vacham để chắc.",
        "Nguồn sai bác (nguonsai=2): Vietnamese cũ что-либо «…, cái gì đó» và какой-либо «…, nào đó» mang sắc thái -то (có thật, không rõ) — sai với -либо «bất cứ/bất kỳ»; đã bỏ trong V. (Riêng «cái gì đó» chính là va chạm máy bắt với что́-то.)",
        "Lỗi tự bắt (loitubat=2): thẻ выпуск viết «вы́- luôn mang trọng âm» trong khi Họ hàng cùng thẻ có выпуска́ть (trọng âm ở đuôi) → sửa «trong danh từ này»; viết «danh từ rút thẳng từ вы́пустить» → đúng hơn là cùng thân -пуск- với выпуска́ть.",
        "Không chắc (mức tin vừa): по- trong похо́д gắn nghĩa «lên đường» như пойти́ — hợp lý nhưng là cách đọc, không phải luật; -доль (вдоль) cùng gốc длина́/до́лгий đã ghi ô ⚠️ Mức tin trên thẻ; Гру́зия chỉ ghi «tên đến từ tiếng nước ngoài» (không khẳng định ngôn ngữ nguồn).",
        "V cần duyệt (7 thẻ): верх (+tột đỉnh — «the ultimate»), поход (+cuộc hành quân, chiến dịch — «campaign/march»), груз (+gánh nặng — «burden»), какой-либо, что-либо, выпуск (+tập, bản tin, sự phát hành, khoá tốt nghiệp — gloss có episode/bulletin/release/graduating class), телевидение (bỏ «tivi» vì tiếng Việt «tivi» là cái máy = телеви́зор; thay bằng ngành/đài truyền hình — có phải cắt nghĩa chính không thì user xét). Không viết V cho 12 thẻ còn lại (đề cũ đã đúng).",
    ],
}
