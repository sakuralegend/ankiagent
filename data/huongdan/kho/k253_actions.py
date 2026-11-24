# -*- coding: utf-8 -*-
"""k253 — actions: hỏng / vỡ / rã (разбиться, сломаться, рассыпаться), khô, tắt, bổ sung, mạnh lên, nhìn kỹ, thanh toán, đuổi, cắn.

Chỗ cần nhất quán trong lô:
(1) -ся = «việc xảy ra với chính nó» như формироваться; thẻ đối ngoại động đã nạp: разбить [k80], разбивать [k239], ломать/сломать [k137].
(2) раз-/рас- TÁCH RA: разбиться, рассчитаться, рассыпаться. -с-чит- GỘP + ĐẾM như рассчитать.
(3) -сматр-/-смотр- gốc -мотр- như рассматривать [k170]; в- VÀO trong như вглядеться [k240].
(4) по-гас- như погасить [k243]; до-полн- như дополнительный [k172]; сып- RẮC, VÃI như сыпь [k32].
Họ hàng không vắng ở thẻ nào.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "высушить": "làm khô, phơi khô, sấy khô",  # cặp thể cùng dãy; sấy / phơi trơ gộp vào
    "сушить": "làm khô, phơi khô, sấy khô",  # như trên
    "погаснуть": "tắt, tự tắt, lụi tàn",  # THIẾU ý TỰ tắt; tách погасить
    "дополнить": "bổ sung, thêm vào, làm đầy đủ thêm",  # THIẾU ý полн- (supplement); tách добавить
    "дополнять": "bổ sung, thêm vào, làm đầy đủ thêm",  # cặp thể cùng dãy
    "разбиваться": "vỡ, vỡ tan, gặp nạn, bị thương nặng, chia thành nhóm",  # THIẾU crash / be injured / split up; «va đập vỡ» gượng
    "разбиться": "vỡ, vỡ tan, gặp nạn, bị thương nặng, chia thành nhóm",  # cặp thể cùng dãy
    "усиливаться": "mạnh lên, tăng lên, dữ dội hơn",  # «dần» là chú thể
    "усилиться": "mạnh lên, tăng lên, dữ dội hơn",  # giữ nguyên, khai để cặp thể cùng dãy
    "всматриваться": "nhìn kỹ, căng mắt nhìn, dán mắt nhìn, xem xét kỹ",  # cặp thể cùng dãy; scrutinize
    "всмотреться": "nhìn kỹ, căng mắt nhìn, dán mắt nhìn, xem xét kỹ",  # «ngắm kỹ» là рассматривать
    "сформироваться": "hình thành, được hình thành, phát triển thành",  # khớp формироваться [đã nạp]
    "рассчитаться": "thanh toán, trả tiền, tính tiền, trả hết nợ, tính sổ",  # «xong» là chú thể; THIẾU get even
    "рассчитываться": "thanh toán, trả tiền, tính tiền, trả hết nợ, tính sổ",  # cặp thể cùng dãy
    "ломаться": "hỏng, hư, gãy, suy sụp",  # BỎ «vỡ» (là разбиться), «rạn nứt» không có trong gloss
    "сломаться": "hỏng, hư, gãy, suy sụp",  # «kiệt sức» không có trong gloss
    "рассыпаться": "đổ tung, vương vãi, vỡ vụn, rã ra, tản ra",  # «đổ ra, tràn ra» là chất lỏng; THIẾU crumble / disperse
    "кусаться": "cắn, hay cắn, đốt, làm ngứa ráp, đắt cắt cổ",  # «châm» gộp vào đốt; THIẾU be steep
}

# -------------------------------------------------------------- высушить
S["высушить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span>'
    '<span class="hd-gloss">TỚI HẾT, trọn — thể hoàn thành, luôn giành trọng âm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-суш-</span>'
    '<span class="hd-gloss">KHÔ — <b>сухо́й</b>, <i>х → ш</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">LÀM cho — đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho khô HẲN, bằng nắng, máy sấy hay lò đều được: <b>вы́сушить во́лосы '
    'фе́ном</b> sấy khô tóc bằng máy sấy. Cặp CHT: <b>суши́ть</b>.</div>'
    '<div class="hd-warn">Trọng âm đứng yên trên <i>вы́-</i> ở mọi dạng (<b>вы́сушу, вы́сушишь, '
    'вы́суши</b>), trong khi <b>суши́ть</b> thì dịch: <b>сушу́, су́шишь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>суши́ть</b> (CHT) · <b>сухо́й</b> khô · <b>су́ша</b> đất liền · '
    '<b>за́суха</b> hạn hán</div>'
)

# ---------------------------------------------------------------- сушить
S["сушить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">суш-</span>'
    '<span class="hd-gloss">KHÔ — <b>сухо́й</b>, <i>х → ш</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">LÀM cho — đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho khô: <b>суши́ть бельё</b> phơi quần áo, <b>суши́ть во́лосы</b> sấy tóc '
    '— tiếng Nga dùng chung một từ, phơi hay sấy là tuỳ cách làm. Cặp HT: <b>вы́сушить</b>.</div>'
    '<div class="hd-warn">Trọng âm lùi từ ngôi «bạn»: <b>сушу́, су́шишь, су́шат</b>.</div>'
    '<div class="hd-warn"><b>су́ши</b> (món sushi) nhìn giống mà là từ Nhật, không cùng gốc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́сушить</b> (HT) · <b>сухо́й</b> khô · <b>суши́лка</b> giá phơi, máy sấy · '
    '<b>за́суха</b> hạn hán</div>'
)

# ------------------------------------------------------------- погаснуть
S["погаснуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">chỉ làm thành thể hoàn thành, KHÔNG thêm nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-гас-</span>'
    '<span class="hd-gloss">TẮT — như <b>погаси́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ну-ть</span>'
    '<span class="hd-gloss">tự CHUYỂN SANG trạng thái ấy</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đèn, lửa, màn hình TỰ tắt: <b>Свет пога́с.</b> Đèn tắt rồi. Không có ai đứng ra '
    'làm nên không bao giờ kèm cách 4. Cặp CHT: <b>га́снуть</b>.</div>'
    '<div class="hd-warn"><i>-ну-</i> rụng ở quá khứ: <b>пога́с, пога́сла, пога́сли</b> — nhưng tương '
    'lai vẫn còn: <b>пога́снет</b>.</div>'
    '<div class="hd-warn">Có người TẮT nó thì dùng <b>погаси́ть</b>: <b>погаси́ть свет</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>га́снуть</b> (CHT) · <b>погаси́ть</b> tắt, dập tắt · <b>угаса́ть</b> lụi '
    'dần</div>'
)

# ------------------------------------------------------------- дополнить
S["дополнить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI ĐỦ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-полн-</span>'
    '<span class="hd-gloss">ĐẦY — <b>по́лный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">LÀM cho — đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thêm cho tới ĐẦY ⇒ bổ sung, làm đầy đủ thêm. Từ nó ra <b>дополни́тельный</b> bổ '
    'sung. Cặp CHT: <b>дополня́ть</b>.</div>'
    '<div class="hd-warn">Cái ĐƯỢC LÀM ĐẦY đứng cách 4, thứ thêm vào đứng cách 5: <b>допо́лнить отчёт '
    'ци́фрами</b> bổ sung số liệu vào báo cáo. <b>доба́вить</b> thì ngược lại, thứ thêm vào đứng cách 4: '
    '<b>доба́вить соль в суп</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дополня́ть</b> (CHT) · <b>дополни́тельный</b> bổ sung · <b>дополне́ние</b> '
    'phần bổ sung · <b>по́лный</b> đầy</div>'
)

# ------------------------------------------------------------- дополнять
S["дополнять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI ĐỦ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-полн-</span>'
    '<span class="hd-gloss">ĐẦY — <b>по́лный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>дополня́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>допо́лнить</b>: thêm cho tới ĐẦY ⇒ bổ sung. Đổi <i>-ить</i> sang '
    '<i>-я́ть</i> thì trọng âm dời xuống đuôi và đứng yên ở đó.</div>'
    '<div class="hd-warn"><b>дополня́ть друг дру́га</b> = bổ sung cho nhau: hai người, hai màu, hai món '
    'hợp nhau.</div>'
    '<div class="hd-warn">Thêm CÁI GÌ → cách 5: <b>дополня́ть расска́з дета́лями</b> thêm chi tiết vào '
    'câu chuyện.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>допо́лнить</b> (HT) · <b>дополни́тельный</b> bổ sung · <b>дополне́ние</b> '
    'phần bổ sung · <b>по́лный</b> đầy</div>'
)

# ----------------------------------------------------------- разбиваться
S["разбиваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span>'
    '<span class="hd-gloss">TÁCH RA từng mảnh, ra các phía</span></div>'
    '<div class="hd-row"><span class="hd-piece">-би-</span>'
    '<span class="hd-gloss">gốc ĐÁNH, ĐẬP — <b>бить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>разбива́юсь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">việc xảy ra với chính nó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>разбива́ть</b> là người đập vỡ; thêm <i>-ся</i> là tự nó VỠ ra mảnh: '
    '<b>Во́лны разбива́ются о ка́мни.</b> Sóng vỡ tan vào đá. Xe, máy bay, người đi xe «vỡ» ⇒ gặp nạn. '
    'Cặp HT: <b>разби́ться</b>.</div>'
    '<div class="hd-warn">Đập VÀO cái gì → <b>о</b> + cách 4. Chia THÀNH phần → <b>на</b> + cách 4: '
    '<b>разбива́ться на гру́ппы</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>разби́ться</b> (HT) · <b>разбива́ть</b> làm vỡ · <b>бить</b> đánh, đập · '
    '<b>разби́тый</b> vỡ tan</div>'
)

# ------------------------------------------------------------- разбиться
S["разбиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span>'
    '<span class="hd-gloss">TÁCH RA từng mảnh, ra các phía</span></div>'
    '<div class="hd-row"><span class="hd-piece">-би́ть</span>'
    '<span class="hd-gloss">gốc ĐÁNH, ĐẬP — <b>бить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">việc xảy ra với chính nó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bị va đập mà TÁCH ra mảnh ⇒ vỡ (cốc, kính, gương). Máy bay hay người đi xe '
    '<b>разби́лся</b> = gặp nạn, thường là chết. Cặp CHT: <b>разбива́ться</b>.</div>'
    '<div class="hd-warn">Gốc lộ ra là <i>бь</i>, chèn thêm <i>о</i> như <b>разби́ть</b>: <b>разобью́сь, '
    'разобьётся</b>; mệnh lệnh <b>разбе́йся</b>.</div>'
    '<div class="hd-warn">Ba kiểu hỏng: <b>разби́ться</b> vỡ ra mảnh · <b>слома́ться</b> gãy, hết chạy · '
    '<b>рассы́паться</b> rã vụn, tung ra.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>разбива́ться</b> (CHT) · <b>разби́ть</b> làm vỡ · <b>бить</b> đánh, đập · '
    '<b>разби́тый</b> vỡ tan</div>'
)

# ----------------------------------------------------------- усиливаться
S["усиливаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">LÀM CHO thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-си́л-</span>'
    '<span class="hd-gloss">SỨC — <b>си́ла</b>, <b>си́льный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành, chia đều: <b>уси́ливаюсь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">việc xảy ra với chính nó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>уси́ливать</b> là làm cho cái khác mạnh; thêm <i>-ся</i> là TỰ nó mạnh lên: '
    '<b>Ве́тер уси́ливается.</b> Gió đang mạnh lên. Chủ ngữ hay gặp: gió, mưa, rét, cơn đau, tiếng ồn. '
    'Cặp HT: <b>уси́литься</b>.</div>'
    '<div class="hd-warn">Trọng âm đứng yên ở <i>си́</i> trong cả hai thể.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уси́литься</b> (HT) · <b>уси́лить</b> tăng cường · <b>уси́лие</b> nỗ lực · '
    '<b>си́ла</b> sức mạnh</div>'
)

# ------------------------------------------------------------- усилиться
S["усилиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">LÀM CHO thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-си́л-</span>'
    '<span class="hd-gloss">SỨC — <b>си́ла</b>, <b>си́льный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">việc xảy ra với chính nó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tự nó có thêm SỨC ⇒ mạnh lên: <b>Дождь уси́лился.</b> Mưa to lên rồi. Cặp CHT: '
    '<b>уси́ливаться</b>.</div>'
    '<div class="hd-warn">Có người làm cho mạnh thì bỏ <i>-ся</i>: <b>уси́лить звук</b> khuếch đại âm '
    'thanh.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уси́ливаться</b> (CHT) · <b>уси́лить</b> tăng cường · <b>усиле́ние</b> sự '
    'tăng cường · <b>си́ла</b> sức mạnh</div>'
)

# --------------------------------------------------------- всматриваться
S["всматриваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO trong</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сматр-</span>'
    '<span class="hd-gloss">= <b>-смотр-</b> NHÌN (gốc <b>-мотр-</b> như <b>смотре́ть</b>), <i>о → '
    'а</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">dồn mắt của chính mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dồn mắt nhìn VÀO TRONG, mà <i>-ива-</i> kéo dài ra ⇒ căng mắt nhìn. <i>о → '
    'а</i> y như <b>рассмотре́ть → рассма́тривать</b>. Cặp HT: <b>всмотре́ться</b>.</div>'
    '<div class="hd-warn">Lặp lại <b>в</b> + cách 4: <b>всма́триваться в темноту́</b> căng mắt nhìn vào '
    'bóng tối.</div>'
    '<div class="hd-warn"><b>вгля́дываться</b> khác gốc mà gần như cùng nghĩa, cùng lối dựng <i>в- … '
    '-ся</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>всмотре́ться</b> (HT) · <b>смотре́ть</b> nhìn · <b>рассма́тривать</b> ngắm '
    'kỹ · <b>осма́тривать</b> khám, xem xét</div>'
)

# ----------------------------------------------------------- всмотреться
S["всмотреться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO trong</span></div>'
    '<div class="hd-row"><span class="hd-piece">-с-мотр-</span>'
    '<span class="hd-gloss">NHÌN — <b>смотре́ть</b> (<i>с-</i> ở đó không mang nghĩa riêng)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia 2</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">dồn mắt của chính mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dồn mắt nhìn VÀO TRONG ⇒ nhìn kỹ một cái cho ra. Nhìn thường là <b>смотре́ть '
    'на</b>; nhìn xoáy vào thì <b>всмотре́ться в</b> + cách 4: <b>всмотре́ться в лицо́</b>. Cặp CHT: '
    '<b>всма́триваться</b>.</div>'
    '<div class="hd-warn">Trọng âm dịch y như <b>смотре́ть</b>: <b>всмотрю́сь, всмо́тришься, '
    'всмо́трятся</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>всма́триваться</b> (CHT) · <b>смотре́ть</b> nhìn · <b>рассмотре́ть</b> xem '
    'xét, nhìn rõ · <b>осмотре́ть</b> khám, xem xét</div>'
)

# -------------------------------------------------------- сформироваться
S["сформироваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">tiền tố thể, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-форм-</span>'
    '<span class="hd-gloss">HÌNH, KHUÔN — chính là <b>фо́рма</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ирова́ть</span>'
    '<span class="hd-gloss">đuôi động từ mượn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">việc xảy ra với chính nó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tự nó thành HÌNH, như Anh <i>form</i>: <b>Хара́ктер сформирова́лся в '
    'де́тстве.</b> Tính cách đã hình thành từ bé. Cặp CHT: <b>формирова́ться</b>.</div>'
    '<div class="hd-warn">Nguyên thể nhấn đuôi, khi chia nhấn <i>-у́-</i>: <b>сформиру́юсь, '
    'сформиру́ется</b>.</div>'
    '<div class="hd-warn">Phát triển THÀNH cái gì → <b>в</b> + cách 4: <b>сформирова́ться в '
    'систе́му</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>формирова́ться</b> (CHT) · <b>сформирова́ть</b> tạo thành · '
    '<b>формирова́ние</b> sự hình thành · <b>фо́рма</b> hình dạng</div>'
)

# ---------------------------------------------------------- рассчитаться
S["рассчитаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рас-</span>'
    '<span class="hd-gloss">TÁCH RA từng phần, làm tới nơi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-с-чит-а́ть</span>'
    '<span class="hd-gloss">chính là <b>счита́ть</b>: <i>с-</i> GỘP + <i>-чит-</i> ĐẾM</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">về phần của chính mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>рассчита́ть</b> là tính ra; thêm <i>-ся</i> là tính xong phần MÌNH với người '
    'ta ⇒ thanh toán, trả hết. Nghĩa bóng: tính sổ với kẻ thù. Cặp CHT: <b>рассчи́тываться</b>.</div>'
    '<div class="hd-warn">Trả AI → <b>с</b> + cách 5, trả VÌ cái gì → <b>за</b> + cách 4: '
    '<b>рассчита́ться с такси́стом за пое́здку</b>. Nợ cũng là <b>с</b>: <b>рассчита́ться с долга́ми</b> '
    'trả hết nợ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рассчи́тываться</b> (CHT) · <b>рассчита́ть</b> tính ra · <b>счита́ть</b> đếm '
    '· <b>расчёт</b> sự tính toán</div>'
)

# -------------------------------------------------------- рассчитываться
S["рассчитываться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рас-</span>'
    '<span class="hd-gloss">TÁCH RA từng phần, làm tới nơi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-с-чит-</span>'
    '<span class="hd-gloss">như <b>счита́ть</b>: GỘP + ĐẾM</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành, chia đều: <b>рассчи́тываюсь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">về phần của chính mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tính phần MÌNH với người ta ⇒ thanh toán, trả tiền. Trả BẰNG gì → cách 5: '
    '<b>рассчи́тываться ка́ртой</b> trả bằng thẻ. Cặp HT: <b>рассчита́ться</b>.</div>'
    '<div class="hd-warn">Có hay không <i>-ся</i> là hai nghĩa xa nhau: <b>рассчи́тывать на дру́га</b> '
    'trông cậy vào bạn — <b>рассчи́тываться с дру́гом</b> trả tiền cho bạn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рассчита́ться</b> (HT) · <b>рассчи́тывать</b> trông cậy · <b>счёт</b> hóa '
    'đơn · <b>расчёт</b> sự tính toán</div>'
)

# -------------------------------------------------------------- ломаться
S["ломаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">лом-</span>'
    '<span class="hd-gloss">GÃY, BẺ — như <b>лом</b> xà beng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành, chia đều: <b>лома́юсь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">việc xảy ra với chính nó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>лома́ть</b> là bẻ gãy, làm hỏng; thêm <i>-ся</i> là TỰ nó gãy, tự nó hỏng: '
    '<b>Телефо́н ча́сто лома́ется.</b> Điện thoại hay hỏng. Cặp HT: <b>слома́ться</b>.</div>'
    '<div class="hd-warn">Khẩu ngữ <b>Не лома́йся!</b> = Đừng làm bộ, đừng làm cao! (nói với người được '
    'mời mà cứ từ chối)</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>слома́ться</b> (HT) · <b>лома́ть</b> làm gãy · <b>поло́мка</b> sự hỏng hóc · '
    '<b>перело́м</b> chỗ gãy xương</div>'
)

# ------------------------------------------------------------- сломаться
S["сломаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">tiền tố thể hoàn thành, không thêm nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лом-а́ть</span>'
    '<span class="hd-gloss">BẺ GÃY — chính là <b>лома́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">việc xảy ra với chính nó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đồ vật TỰ hỏng, tự gãy: <b>Маши́на слома́лась.</b> Xe hỏng rồi. Người mà '
    '<b>слома́лся</b> = suy sụp tinh thần. Cặp CHT: <b>лома́ться</b>.</div>'
    '<div class="hd-warn">Người gãy tay thì nói <b>Я слома́л ру́ку</b> — chủ động, bỏ <i>-ся</i>.</div>'
    '<div class="hd-warn">Rơi mà vỡ ra mảnh là <b>разби́ться</b>: <b>Ва́за разби́лась</b>, nhưng '
    '<b>Часы́ слома́лись</b> Đồng hồ hỏng rồi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лома́ться</b> (CHT) · <b>слома́ть</b> làm gãy · <b>поло́мка</b> sự hỏng hóc '
    '· <b>перело́м</b> chỗ gãy xương</div>'
)

# --------------------------------------------------------------- гнаться
S["гнаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гн- / гон-</span>'
    '<span class="hd-gloss">ĐUỔI, PHÓNG — nguyên thể giấu <i>о</i>, hiện tại lộ ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">tự mình lao đi</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>гнать</b> là bắt kẻ khác chạy phía TRƯỚC; thêm <i>-ся</i> là chính mình lao '
    'THEO SAU ⇒ đuổi theo. Một hướng, đang đuổi; đuổi kịp rồi là <b>догна́ть</b>.</div>'
    '<div class="hd-warn">Đuổi theo AI / CÁI GÌ → <b>за</b> + cách 5: <b>гна́ться за авто́бусом</b>, '
    '<b>гна́ться за мо́дой</b> chạy theo mốt.</div>'
    '<div class="hd-warn">Chia như <b>гнать</b>: <b>гоню́сь, го́нишься, го́нятся</b>; quá khứ giống cái '
    'nhấn đuôi: <b>гна́лся, гнала́сь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гнать</b> lùa, đuổi · <b>догна́ть</b> đuổi kịp · <b>пого́ня</b> cuộc rượt '
    'đuổi · <b>го́нка</b> cuộc đua</div>'
)

# ----------------------------------------------------------- рассыпаться
S["рассыпаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рас-</span>'
    '<span class="hd-gloss">TÁCH RA các phía</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сы́п-</span>'
    '<span class="hd-gloss">RẮC, VÃI thứ dạng hạt — <b>сы́пать</b>, <b>сыпь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">việc xảy ra với chính nó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tự nó VÃI RA các phía ⇒ đổ tung (đường, kẹo); thứ khô giòn thì vỡ vụn, rã ra; '
    'đám người thì tản ra.</div>'
    '<div class="hd-warn">Hai từ cùng mặt chữ, chỉ khác trọng âm: <b>рассы́паться</b> HT (thẻ này) — '
    '<b>рассыпа́ться</b> CHT, chia đều <b>рассыпа́ется</b>.</div>'
    '<div class="hd-warn">Tương lai <i>п → пл</i> ở mọi ngôi: <b>рассы́плюсь, рассы́плется, '
    'рассы́плются</b>; mệnh lệnh <b>рассы́пься</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сы́пать</b> rắc, đổ · <b>рассы́пать</b> làm đổ tung · <b>сыпь</b> nốt '
    'ban</div>'
)

# -------------------------------------------------------------- кусаться
S["кусаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кус-</span>'
    '<span class="hd-gloss">CẮN — như <b>кусо́к</b> miếng (cái cắn ra được)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть</span>'
    '<span class="hd-gloss">đuôi CHT, chia đều: <b>куса́юсь, куса́ется</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">nói TÍNH hay thế</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>куса́ть</b> là cắn một ai cụ thể (cách 4); thêm <i>-ся</i> thì bỏ nạn nhân '
    'đi, chỉ còn cái TÍNH hay cắn: <b>Соба́ка куса́ется.</b> Con chó này hay cắn. Áo len «cắn» da ⇒ làm '
    'ngứa ráp.</div>'
    '<div class="hd-warn"><b>Це́ны куса́ются</b> — giá «cắn» người ⇒ đắt cắt cổ.</div>'
    '<div class="hd-warn">Cắn một phát vào ai thì dùng <b>укуси́ть</b>: <b>Меня́ укуси́ла '
    'соба́ка.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>куса́ть</b> cắn, đốt · <b>укуси́ть</b> cắn (HT) · <b>уку́с</b> vết cắn · '
    '<b>кусо́к</b> miếng</div>'
)

B = {
    "docbangmat": 121,
    "loitubat": 3,
    "nguonsai": 4,
    "baolen": [
        "Bảng chia (GrammarJSON + BangMay) рассыпаться: tương lai ngôi «họ» ghi «рассы́паются» là SAI (lẫn CHT рассыпа́ются) — đúng: рассы́плются. Phải sửa; ô hướng dẫn đã ghi dạng đúng.",
        "Bảng chia сформироваться RỖNG (presfut / past / imper trống) — đúng: сформиру́юсь, сформиру́ешься, сформиру́ется, сформиру́емся, сформиру́етесь, сформиру́ются; сформирова́лся, сформирова́лась, сформирова́лось, сформирова́лись; сформиру́йся, сформиру́йтесь.",
        "Gloss tiếng Anh сломаться có «to put on airs / to pose / to be affected / to make difficulties»: nghĩa này chỉ thuộc CHT ломаться — nên gỡ khỏi thẻ сломаться.",
        "Gloss phân từ trong bảng рассчитываться sai: рассчи́тывавшийся «Calculated, expected, anticipated, counted on» và рассчи́тывающийся «being discharged, being dismissed» — đúng: settling up, paying.",
        "дополнить: bảng ghi gerundPresent «допо́лня» — dạng cổ, nay chỉ dùng допо́лнив; nên gỡ.",
        "V cần duyệt: сформироваться bỏ «định hình» để cùng dãy формироваться đã nạp (user muốn giữ thì sửa cả hai thẻ).",
        "V cần duyệt: ломаться không đưa nghĩa khẩu ngữ «làm bộ, làm cao» vào đề bài vì cặp chung dãy mà сломаться không có nghĩa này; đã nói ở ô đỏ.",
        "V cần duyệt: погаснуть giữ «tắt» (nghĩa chính) dù погасить / выключить cùng badge cũng có; hai nghĩa còn lại tách.",
        "V gần nhau: всматриваться / всмотреться ↔ вглядываться / вглядеться (nhìn kỹ, căng mắt nhìn) — đồng nghĩa thật; tách bằng «dán mắt nhìn, xem xét kỹ» ↔ «nhìn chăm chú».",
        "Nghĩa có trong V mà chưa câu ví dụ nào dùng: разбиваться (gặp nạn, bị thương nặng), разбиться (bị thương nặng, chia thành nhóm), рассчитаться / рассчитываться (tính tiền, trả hết nợ, tính sổ), всматриваться / всмотреться (dán mắt nhìn, xem xét kỹ), рассыпаться (vương vãi, tản ra, rã ra), кусаться (đốt, làm ngứa ráp, đắt cắt cổ).",
        "Câu cũ рассыпаться số 1 dùng «рассыпаются» (dạng CHT / dạng sai của bảng) — đã sửa thành рассыплются trong sua_k253.py.",
    ],
}
