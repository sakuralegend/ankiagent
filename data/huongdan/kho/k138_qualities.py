# -*- coding: utf-8 -*-
"""k138 — qualities: 21 từ, trục là GỐC Nga dưới động từ -ся và tính từ chất liệu.

Không khối hệ thống. Chỗ phải khớp với thẻ đã có / lô song song:
(1) кон-/конч- «ĐẦU MÚT, KẾT» — y như коне́ц, ко́нчиться, оконча́ние (cũ);
(2) дел- «PHẦN, CHIA PHẦN» — khớp дели́ть/раздели́ть (k137, đang soạn song song);
(3) цен- «GIÁ» — y như цена́, оце́нка, оцени́ть (cũ);
(4) вис- «TREO» — y như зави́сеть (cũ); вой-/во- «CHIẾN» — y như война́, вое́нный (cũ);
(5) từ mượn (мета́лл, парла́мент, демонстра́ция, конститу́ция, демократи́ческий,
    уника́льный) không bịa cấu trúc Nga — chỉ nói mảnh Latin/Hy Lạp khi tiếng Anh cùng mảnh.
"""

V = {
    "развиваться": "phát triển, tiến triển",     # bỏ «(đang)» — nhãn thể
    "развиться": "phát triển, tiến triển",       # bỏ «(xong)» — nhãn thể; badge PERF tách
    "заканчиваться": "hết dần",                  # RÚT «đang kết thúc» — «đang» là nhãn thể, «kết thúc» trùng конча́ться (cũ)
    "закончиться": "hết",                        # RÚT «kết thúc» — trùng ко́нчиться (cũ); «hết» TV phủ cả «hết phim» lẫn «hết tiền»
    "ценный": "có giá trị",                      # RÚT «quý giá» — trùng дорого́й (cũ)
    "вредный": "có hại, xấu tính",               # thêm nghĩa người — gloss nasty/spiteful/mean
    "воевать": "tham chiến, đánh trận",          # bỏ ngoặc; «đánh nhau» trơn là ẩu đả (драться)
    "демонстрация": "cuộc biểu tình, sự trình diễn",  # «;» → «,»
}

S = {}

# --------------------------------------------------------------- развиваться
S["развиваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span>'
    '<span class="hd-gloss">tháo ra, mở tung</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ви-</span>'
    '<span class="hd-gloss">gốc XOẮN, BỆN — <b>вить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва́-ться</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành + tự mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen «tự tháo cuộn ra» ⇒ phát triển — giống hệt cách tiếng Anh '
    '<i>de-velop</i> «mở bọc ra». Chia đều: <b>развива́юсь, развива́ешься</b>. Cặp thể hoàn '
    'thành: <b>разви́ться</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>разви́тие</b> sự phát triển · <b>развива́ть</b> phát triển (cái gì) · '
    '<b>вить</b> xoắn, bện</div>'
)

# --------------------------------------------------------------- развиться
S["развиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span>'
    '<span class="hd-gloss">tháo ra, mở tung</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ви́-ться</span>'
    '<span class="hd-gloss">gốc XOẮN — <b>вить</b> + tự mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thể hoàn thành của <b>развива́ться</b>: «tự tháo cuộn» ⇒ phát triển. '
    'Nghĩa đen vẫn còn sống: sợi dây, lọn tóc <b>разви́лся</b> = bung xoắn ra.</div>'
    '<div class="hd-warn">Thân tương lai đổi hình, phải thuộc riêng: <b>разовью́сь, '
    'разовьёшься</b> — <i>раз-</i> thêm <i>о</i>, <i>-ви-</i> thành <i>-вь-</i>, theo đúng '
    '<b>вить → вью, вьёшь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>развива́ться</b> (CHT) · <b>разви́тие</b> sự phát triển · '
    '<b>вить</b> xoắn, bện</div>'
)

# --------------------------------------------------------------- заканчиваться
S["заканчиваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">hầu như không thêm nghĩa — <b>ко́нчиться</b> cũng là «hết»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка́нч-</span>'
    '<span class="hd-gloss">gốc ĐẦU MÚT — <b>коне́ц</b> (о → а)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ться</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành + tự mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đang đi dần tới đầu mút ⇒ sắp hết, hết dần: <b>Вре́мя '
    'зака́нчивается</b> = thời gian sắp hết. Cặp hoàn thành: <b>зако́нчиться</b>.</div>'
    '<div class="hd-warn">Gắn <i>-ива-</i> thì <i>о</i> của gốc thành <i>а</i>: '
    '<b>зако́нчиться → зака́нчиваться</b>, cùng luật <b>спроси́ть → спра́шивать</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>коне́ц</b> điểm cuối · <b>зака́нчивать</b> kết thúc (cái gì) · '
    '<b>конча́ться</b> gần đồng nghĩa · <b>оконча́ние</b> phần kết</div>'
)

# --------------------------------------------------------------- закончиться
S["закончиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">hầu như không thêm nghĩa — <b>ко́нчиться</b> cũng là «hết»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ко́нч-</span>'
    '<span class="hd-gloss">gốc ĐẦU MÚT — <b>коне́ц</b> (<i>ц → ч</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ться</span>'
    '<span class="hd-gloss">đuôi động từ + tự mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chạm đầu mút ⇒ hết: hết phim, hết tiền đều dùng được — '
    '<b>Де́ньги зако́нчились</b> = hết tiền. Dùng thay <b>ко́нчиться</b> được trong hầu hết '
    'câu. <b>Ещё не зако́нчилось</b> = chưa xong đâu.</div>'
    '<div class="hd-warn"><i>-ся</i> = sự việc TỰ hết, không ai làm: <b>Фильм зако́нчился</b> '
    '(phim hết). Có người làm cho xong thì bỏ <i>-ся</i>: <b>Я зако́нчил рабо́ту</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>коне́ц</b> điểm cuối · <b>зако́нчить</b> làm xong · '
    '<b>ко́нчиться</b> gần đồng nghĩa · <b>оконча́ние</b> phần kết</div>'
)

# --------------------------------------------------------------- делиться
S["делиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дел-</span>'
    '<span class="hd-gloss">gốc PHẦN, CHIA PHẦN — <b>дели́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть-ся</span>'
    '<span class="hd-gloss">đuôi động từ + của mình / tự mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chia phần CỦA MÌNH cho người khác ⇒ chia sẻ; hoặc tự tách thành phần: '
    '<b>Де́сять де́лится на два</b> = 10 chia hết cho 2. Trọng âm nhảy lên gốc từ ngôi 2: '
    '<b>делю́сь</b> nhưng <b>де́лишься, де́лится</b>.</div>'
    '<div class="hd-warn">Cái được chia ở <b>cách 5</b>, người nhận đi với <b>с</b>: '
    '<b>дели́ться о́пытом с друзья́ми</b> = chia sẻ kinh nghiệm với bạn bè.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дели́ть</b> chia · <b>раздели́ться</b> tách ra · '
    '<b>разде́л</b> phần, mục</div>'
)

# --------------------------------------------------------------- разделиться
S["разделиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span>'
    '<span class="hd-gloss">tách ra, mỗi bên một ngả</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дел-</span>'
    '<span class="hd-gloss">gốc PHẦN, CHIA PHẦN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть-ся</span>'
    '<span class="hd-gloss">đuôi động từ + tự mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tự tách thành nhiều phần ⇒ chia ra: <b>Мы раздели́лись на две '
    'гру́ппы</b> = chúng tôi chia thành hai nhóm (số phần đi với <b>на</b> + cách 4). '
    'Trọng âm nhảy như <b>дели́ться</b>: <b>разделю́сь, разде́лишься</b>. Cặp chưa hoàn '
    'thành: <b>разделя́ться</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>раздели́ть</b> chia ra · <b>дели́ться</b> chia sẻ · '
    '<b>разде́л</b> phần, mục</div>'
)

# --------------------------------------------------------------- скидка
S["скидка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">xuống, khỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-кид-</span>'
    '<span class="hd-gloss">gốc NÉM — <b>кида́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">đuôi danh từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Ném bớt xuống» ⇒ khoản bớt khỏi giá. Giảm cho món gì đi với '
    '<b>на</b>: <b>ски́дка на о́бувь</b>; mua được giảm giá: <b>со ски́дкой</b>. Số nhiều '
    'cách 2 chen <i>о</i>: <b>ски́док</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кида́ть</b> ném · <b>ски́нуть</b> ném xuống, cởi vứt ra</div>'
)

# --------------------------------------------------------------- каменный
S["каменный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ка́мен-</span>'
    '<span class="hd-gloss">gốc ĐÁ — <b>ка́мень</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ «làm bằng»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>ка́мень</b> + <i>-ный</i> ⇒ bằng đá. Hai cụm hay gặp: <b>ка́менный '
    'век</b> thời đồ đá · <b>ка́менный у́голь</b> than đá. Dạng ngắn (<b>ка́менен</b>…) chỉ '
    'gặp ở nghĩa bóng «lạnh như đá»; nghĩa «bằng đá» luôn dùng dạng dài.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ка́мень</b> hòn đá · <b>драгоце́нные ка́мни</b> đá quý</div>'
)

# --------------------------------------------------------------- серебряный
S["серебряный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сере́бр-</span>'
    '<span class="hd-gloss">gốc BẠC — <b>серебро́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ян-ый</span>'
    '<span class="hd-gloss">đuôi tính từ chất liệu «làm bằng»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>серебро́</b> + <i>-ян-</i> ⇒ bằng bạc. Trọng âm lùi từ đuôi lên '
    'gốc: <b>серебро́ → сере́бряный</b>.</div>'
    '<div class="hd-warn">Đuôi <i>-ян-</i> viết MỘT <i>н</i>. Chỉ ba từ ngoại lệ viết '
    '<i>-янн-</i>: <b>стекля́нный</b> bằng kính, <b>деревя́нный</b> bằng gỗ, '
    '<b>оловя́нный</b> bằng thiếc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>серебро́</b> bạc</div>'
)

# --------------------------------------------------------------- металл
S["металл"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn (Hy Lạp <i>metallon</i>, qua Latin — tiếng Anh <i>metal</i>), '
    'không chẻ được theo gốc Nga. Trọng âm ở cuối: <b>мета́лл</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cụm cố định: <b>драгоце́нные мета́ллы</b> kim loại quý · <b>чёрные '
    'мета́ллы</b> kim loại đen (sắt, thép).</div>'
    '<div class="hd-warn">Viết HAI <i>л</i>, khác tiếng Anh <i>metal</i> chỉ một.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>металли́ческий</b> bằng kim loại</div>'
)

# --------------------------------------------------------------- серебро
S["серебро"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được. Đuôi <i>-о</i> ⇒ giống trung; là chất nên '
    'không dùng số nhiều.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trọng âm ở cuối <b>серебро́</b>, sang tính từ thì lùi lên: '
    '<b>сере́бряный</b>. Tục ngữ: <b>Сло́во — серебро́, молча́ние — зо́лото</b> = lời nói là '
    'bạc, im lặng là vàng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сере́бряный</b> bằng bạc</div>'
)

# --------------------------------------------------------------- уголь
S["уголь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được. Đuôi <i>-ь</i> nhưng giống đực.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nguyên âm chạy: <i>о</i> rơi khi thêm đuôi — <b>у́голь → у́гля, '
    'у́глем</b>. Than đá: <b>ка́менный у́голь</b>.</div>'
    '<div class="hd-warn">Đừng lẫn <b>у́гол</b> = GÓC (không <i>ь</i>): <b>у́гол → угла́</b>, '
    'còn <b>у́голь → у́гля</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>углеро́д</b> cacbon (<i>угле-</i> than + <i>-род</i> sinh ra)</div>'
)

# --------------------------------------------------------------- вредный
S["вредный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вред-</span>'
    '<span class="hd-gloss">gốc CÁI HẠI — <b>вред</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>вред</b> + <i>-ный</i> ⇒ có hại. Nói về người: <b>вре́дный '
    'челове́к</b> = người xấu tính, hay gây khó dễ. Dạng ngắn giống cái nhảy trọng âm ra '
    'đuôi: <b>вредна́</b>, còn lại giữ ở gốc — <b>вре́ден, вре́дно</b>.</div>'
    '<div class="hd-warn"><b>Кури́ть вре́дно для здоро́вья</b> = hút thuốc có hại cho sức '
    'khoẻ (<b>для</b> + cách 2).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вред</b> cái hại · <b>вреди́ть</b> làm hại (+ cách 3) · '
    '<b>безвре́дный</b> vô hại</div>'
)

# --------------------------------------------------------------- ценный
S["ценный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">цен-</span>'
    '<span class="hd-gloss">gốc GIÁ — <b>цена́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Có giá ⇒ có giá trị: <b>це́нный о́пыт</b> kinh nghiệm quý. Dạng ngắn '
    'thêm <i>е</i> ở giống đực: <b>це́нен</b>.</div>'
    '<div class="hd-warn"><b>дорого́й</b> = ĐẮT (giá bán cao), và «thân yêu». <b>це́нный</b> = '
    'có GIÁ TRỊ thật, không mang nghĩa «đắt».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>цена́</b> giá · <b>оце́нка</b> sự đánh giá, điểm · '
    '<b>оцени́ть</b> đánh giá · <b>драгоце́нный</b> quý báu</div>'
)

# --------------------------------------------------------------- уникальный
S["уникальный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">уник-</span>'
    '<span class="hd-gloss">Latin <i>unicus</i> «duy nhất» — tiếng Anh <i>unique</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́льный</span>'
    '<span class="hd-gloss">đuôi Nga hoá tính từ mượn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><i>unique</i> + <i>-а́льный</i>, cùng khuôn <b>норма́льный</b>. Dạng '
    'ngắn giống đực chen <i>е</i>: <b>уника́лен</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уника́льность</b> tính độc nhất</div>'
)

# --------------------------------------------------------------- демократический
S["демократический"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">демо-</span>'
    '<span class="hd-gloss">Hy Lạp <i>demos</i> dân</span></div>'
    '<div class="hd-row"><span class="hd-piece">-крат-</span>'
    '<span class="hd-gloss">Hy Lạp <i>kratos</i> quyền cai trị</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ческий</span>'
    '<span class="hd-gloss">đuôi tính từ = tiếng Anh <i>-ic</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><i>democrat-ic</i>. Khuôn danh từ <i>-ия/-ика</i> → tính từ '
    '<i>-и́ческий</i>, trọng âm luôn rơi vào <i>и́</i>: <b>демокра́тия → демократи́ческий</b>, '
    '<b>эконо́мика → экономи́ческий</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>демокра́тия</b> nền dân chủ · <b>демокра́т</b> người theo dân chủ</div>'
)

# --------------------------------------------------------------- парламент
S["парламент"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn (Pháp <i>parlement</i>, tiếng Anh <i>parliament</i>), không '
    'chẻ được theo gốc Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc Pháp <i>parler</i> «nói» ⇒ nơi để bàn bạc. Trọng âm giữa: '
    '<b>парла́мент</b>; giống đực, biến cách đều.</div>'
)

# --------------------------------------------------------------- воевать
S["воевать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">во-</span>'
    '<span class="hd-gloss">gốc CHIẾN (<i>вой-</i>) — <b>война́</b>, <b>во́ин</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ева́ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp <i>-овать/-евать</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>война́</b> ⇒ làm chiến tranh. Lớp <i>-ова-/-ева-</i> khi chia thì '
    'thành <i>-у-/-ю-</i>: <b>вою́ю, вою́ешь</b>, như <b>рисова́ть → рису́ю</b>.</div>'
    '<div class="hd-warn"><b>воева́ть с</b> + cách 5 = đánh VỚI ai tức là CHỐNG ai, không phải '
    'cùng phe: <b>воева́ть с враго́м</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>война́</b> chiến tranh · <b>вое́нный</b> quân sự · '
    '<b>во́ин</b> chiến binh</div>'
)

# --------------------------------------------------------------- независимость
S["независимость"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не-</span>'
    '<span class="hd-gloss">không</span></div>'
    '<div class="hd-row"><span class="hd-piece">-за-ви́с-</span>'
    '<span class="hd-gloss">gốc TREO — <b>зави́сеть</b> «treo vào» ⇒ phụ thuộc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-им-</span>'
    '<span class="hd-gloss">đuôi tính từ — <b>зави́симый</b> phụ thuộc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span>'
    '<span class="hd-gloss">danh từ trừu tượng, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không bị treo vào ai ⇒ độc lập ⇒ sự độc lập. Xếp từng lớp: '
    '<b>зави́сеть → незави́симый → незави́симость</b>. <b>День незави́симости</b> = Ngày '
    'Độc lập.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>зави́сеть</b> phụ thuộc · <b>незави́симый</b> độc lập · '
    '<b>зави́симость</b> sự phụ thuộc · <b>висе́ть</b> treo</div>'
)

# --------------------------------------------------------------- демонстрация
S["демонстрация"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">демонстр-</span>'
    '<span class="hd-gloss">= tiếng Anh <i>demonstr-</i> (Latin «chỉ ra»)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ция</span>'
    '<span class="hd-gloss">= tiếng Anh <i>-ation</i>, danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đổi <i>-ation</i> thành <i>-а́ция</i> là ra từ Nga, và mang đủ hai nghĩa '
    'như tiếng Anh: cuộc biểu tình trên phố · sự trình diễn. Động từ: <i>-ate</i> → '
    '<i>-и́ровать</i> — <b>демонстри́ровать</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>демонстри́ровать</b> trình diễn, phô ra · <b>демонстра́нт</b> '
    'người biểu tình</div>'
)

# --------------------------------------------------------------- конституция
S["конституция"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">конститу́-</span>'
    '<span class="hd-gloss">= tiếng Anh <i>constitu-</i> (Latin «dựng nên»)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ция</span>'
    '<span class="hd-gloss">= tiếng Anh <i>-tion</i>, danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><i>constitution</i> với <i>-tion → -ция</i>, cùng khuôn '
    '<b>демонстра́ция</b>. Trọng âm đứng ngay trước <i>-ция</i>: <b>конститу́ция</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>конституцио́нный</b> thuộc hiến pháp</div>'
)

B = {
    "docbangmat": 88,
    "loitubat": 6,   # за- bịa nghĩa «chạm điểm cuối» (2 thẻ, tiền tố thể) · у́гол/у́голь khẳng định «khác gốc» không hạ mức tin · -им- glossed «bị…» sai · воева́ть so -ева- với рисова́ть -ова- lệch khuôn · chẻ «вое-» sai ranh giới (gốc là во-/вой-) · «đọc ngược» tả sai chiều phái sinh
    "nguonsai": 0,
    "baolen": [
        "зако́нчиться/ко́нчиться và зака́нчиваться/конча́ться là cặp ĐỒNG NGHĨA thật: đã RÚT V còn «hết» / «hết dần» nên máy hết trùng, nhưng với người học vẫn sát «hết sạch, cạn kiệt, kết thúc» của thẻ cũ — gỡ triệt để phải sửa thẻ mồ côi ко́нчиться/конча́ться (không thuộc quyền lô này)",
        "це́нный: RÚT «quý giá» (trùng дорого́й) còn «có giá trị»",
        "V cần duyệt: вре́дный THÊM «xấu tính» (gloss nasty/spiteful/mean); воева́ть bỏ «đánh nhau (chiến tranh)» → «tham chiến, đánh trận» vì «đánh nhau» trơn là ẩu đả",
        "Không chắc: ка́менный — câu «dạng ngắn chỉ gặp ở nghĩa bóng» là hiểu biết chung, chưa có nguồn máy xác nhận",
        "парла́мент cố ý KHÔNG có Họ hàng: từ mượn đứng một mình, парла́ментский không chắc trọng âm nên không viết",
        "Hạ tầng: scratchpad DÙNG CHUNG giữa các lô song song — file vi.json của tôi bị lô khác ghi đè giữa chừng; đã đổi sang tên có tiền tố k138_",
    ],
}
