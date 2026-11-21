# -*- coding: utf-8 -*-
"""k150 — life::health (lô trộn): ốm vặt, vệ sinh thân thể, sân khấu-âm nhạc.

Chỗ cần nhất quán trong lô:
(1) họ мыть: мы́ться = tắm CẢ NGƯỜI · умыва́ться/умы́ться = chỉ rửa MẶT-TAY · вы́мыться = tắm sạch bong;
    thân hiện tại đổi ы → о ở cả bốn (мо́юсь, умо́юсь, вы́моюсь) — khớp мыть/вымыть/помыть (k79).
(2) бри́ться/побри́ться: nguyên thể бри-, thân hiện tại бре- (бре́юсь).
(3) gốc здоров- (k76/k82/k142) → вы́здороветь / выздора́вливать (о → а, chêm л như остана́вливать).
(4) роя́ль + анса́мбль: mượn Pháp, đuôi -ь mà giống ĐỰC.
Họ hàng cố ý vắng: анги́на, афи́ша, анса́мбль, роя́ль (mượn, đứng một mình trong tiếng Nga).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "выздоравливать": "hồi phục, khỏi bệnh",           # bỏ «đang», «dần» — nhãn thể trá hình
    "умыться": "rửa mặt",                               # bỏ «(xong)»; badge thể tách khỏi умываться
    "побриться": "cạo râu",                             # bỏ «(xong)»; badge thể tách khỏi бриться
    "вымыться": "tắm rửa, tắm cho sạch",               # bỏ «xong» — nhãn thể trá hình
    "документальный": "tài liệu",                       # bỏ «(phim tài liệu)»; badge từ loại tách khỏi документ
    "сфотографироваться": "được chụp ảnh, chụp ảnh mình",  # bỏ «(tự mình)»; «chụp ảnh» trơn trùng сфотографировать; khớp фотографироваться (k77)
}

# --------------------------------------------------------------------- ангина
S["ангина"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — mượn Latin <i>angina</i>, '
    'từ <i>angere</i> «siết, bóp nghẹt».</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Họng sưng tới mức như bị siết lại. Nói «tôi bị» theo khuôn '
    '<b>у</b> + cách 2: <b>У меня́ анги́на</b>.</div>'
    '<div class="hd-warn">Bẫy tiếng Anh: <i>angina</i> là đau thắt NGỰC, còn '
    '<b>анги́на</b> chỉ là viêm họng, viêm amidan. Đau thắt ngực là <b>стенокарди́я</b>.</div>'
)

# --------------------------------------------------------------------- зубной
S["зубной"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">зуб-</span>'
    '<span class="hd-gloss">RĂNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ «thuộc về», nhấn đuôi</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>зуб</b> + <b>-но́й</b> = thuộc về răng. Trọng âm rơi vào đuôi '
    '<b>-о́й</b>, như <b>родно́й</b>.</div>'
    '<div class="hd-warn">Gặp nhiều nhất trong ba cụm: <b>зубна́я щётка</b> bàn chải đánh răng · '
    '<b>зубна́я па́ста</b> kem đánh răng · <b>зубно́й врач</b> nha sĩ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>зуб</b> răng · <b>беззу́бый</b> không răng, móm</div>'
)

# --------------------------------------------------------------------- насморк
S["насморк"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">tiền tố danh từ, không dịch riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сморк</span>'
    '<span class="hd-gloss">XÌ MŨI — <b>сморка́ться</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thứ bắt bạn phải xì mũi suốt ngày = sổ mũi. Giống đực, đuôi phụ âm; '
    'trọng âm đứng yên trên <b>на́-</b>.</div>'
    '<div class="hd-warn">Tiếng Nga không có động từ «bị»: <b>У меня́ на́сморк</b> = Tôi bị sổ mũi '
    '(<b>у</b> + cách 2).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сморка́ться</b> xì mũi</div>'
)

# --------------------------------------------------------------------- выздоравливать
S["выздоравливать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">RA — ra khỏi cơn bệnh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-здора́вл-</span>'
    '<span class="hd-gloss">KHOẺ — <b>здоро́вый</b>, о → а và chêm <b>л</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-ть</span>'
    '<span class="hd-gloss">hậu tố chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đang khoẻ dần ra khỏi bệnh. Thể chưa hoàn thành dựng từ <b>вы́здороветь</b> '
    'nhìn giống hệt <b>останови́ть → остана́вливать</b>: о → а, sau <b>в</b> chêm <b>л</b>. '
    'Chia đều: <b>выздора́вливаю</b>.</div>'
    '<div class="hd-warn">Câu chúc người ốm: <b>Выздора́вливай!</b> / <b>Выздора́вливайте!</b> '
    '= Mau khoẻ nhé! — lời chúc quen dùng thể chưa hoàn thành này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́здороветь</b> khỏi bệnh (HT) · <b>здоро́вый</b> khoẻ mạnh · '
    '<b>здоро́вье</b> sức khoẻ · <b>выздоровле́ние</b> sự bình phục</div>'
)

# --------------------------------------------------------------------- выздороветь
S["выздороветь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span>'
    '<span class="hd-gloss">RA — ra khỏi cơn bệnh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-здоров-</span>'
    '<span class="hd-gloss">KHOẺ — <b>здоро́вый</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е-ть</span>'
    '<span class="hd-gloss">đuôi «TRỞ NÊN» (như <b>красне́ть</b> đỏ lên)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trở nên khoẻ, ra khỏi bệnh = khỏi hẳn. Chia theo lớp <b>-еть</b>: '
    '<b>вы́здоровею, вы́здоровеешь</b>.</div>'
    '<div class="hd-warn">Như mọi động từ hoàn thành có <b>вы-</b>, trọng âm nằm trên <b>вы́</b> '
    'ở mọi dạng: <b>вы́здоровею, вы́здоровел</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>выздора́вливать</b> hồi phục (CHT) · <b>здоро́вый</b> khoẻ mạnh · '
    '<b>здоро́вье</b> sức khoẻ</div>'
)

# --------------------------------------------------------------------- умываться
S["умываться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố — ở đây KHÔNG dịch ra nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мы-</span>'
    '<span class="hd-gloss">RỬA — <b>мыть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва-ть-ся</span>'
    '<span class="hd-gloss">hậu tố chưa hoàn thành + phản thân: rửa CHO MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vẫn là «rửa mình», nhưng <b>у-</b> thu hẹp lại: chỉ mặt và tay, ở bồn rửa — '
    'bồn đó chính là <b>умыва́льник</b>. Chia đều: <b>умыва́юсь, умыва́ешься</b>.</div>'
    '<div class="hd-warn">Sáng ngủ dậy rửa mặt là <b>умыва́ться</b>; tắm cả người là '
    '<b>мы́ться</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>умы́ться</b> rửa mặt (HT) · <b>умыва́льник</b> bồn rửa mặt · '
    '<b>мы́ться</b> tắm · <b>мыть</b> rửa</div>'
)

# --------------------------------------------------------------------- умыться
S["умыться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố — KHÔNG dịch ra nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мы-ть-ся</span>'
    '<span class="hd-gloss">RỬA (<b>мыть</b>) + phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bỏ <b>-ва-</b> khỏi <b>умыва́ться</b> là ra thể hoàn thành: rửa mặt, tay '
    'xong một lượt.</div>'
    '<div class="hd-warn">Thân đổi ы → о y như <b>мыть</b>: <b>умо́юсь, умо́ешься, умо́ются</b>. '
    'Mệnh lệnh: <b>Умо́йся!</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>умыва́ться</b> rửa mặt (CHT) · <b>мы́ться</b> tắm · <b>мыть</b> rửa</div>'
)

# --------------------------------------------------------------------- простудиться
S["простудиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">XUYÊN QUA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-студ-</span>'
    '<span class="hd-gloss">LẠNH — <b>студёный</b> lạnh buốt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть-ся</span>'
    '<span class="hd-gloss">đuôi động từ + phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bị cái lạnh thấm xuyên người = cảm lạnh. Thể chưa hoàn thành: '
    '<b>простужа́ться</b>.</div>'
    '<div class="hd-warn">Chỉ ngôi «tôi» đổi <b>д → ж</b> và nhấn đuôi: <b>простужу́сь</b>; '
    'các ngôi khác lùi trọng âm về gốc: <b>просту́дишься, просту́дятся</b>.</div>'
    '<div class="hd-warn"><b>студе́нт</b> nhìn giống mà KHÁC gốc — nó từ Latin <i>studere</i> «học».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>просту́да</b> cảm lạnh · <b>простужа́ться</b> bị cảm (CHT) · '
    '<b>студёный</b> lạnh buốt</div>'
)

# --------------------------------------------------------------------- бриться
S["бриться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бри-</span>'
    '<span class="hd-gloss">CẠO — <b>брить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть-ся</span>'
    '<span class="hd-gloss">đuôi nguyên thể + phản thân: cạo CHO MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>брить</b> là cạo cho người khác (việc của thợ cạo); thêm <b>-ся</b> '
    'là tự cạo.</div>'
    '<div class="hd-warn">Nguyên thể có <b>и</b>, thân hiện tại là <b>бре-</b>: '
    '<b>бре́юсь, бре́ешься, бре́ются</b>. Nhớ một dạng là ra cả bảng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>побри́ться</b> cạo râu (HT) · <b>брить</b> cạo · '
    '<b>бри́тва</b> dao cạo</div>'
)

# --------------------------------------------------------------------- побриться
S["побриться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể — KHÔNG mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бри́ться</span>'
    '<span class="hd-gloss">tự cạo, gốc <b>брить</b> CẠO</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>побри́ться</b> = <b>бри́ться</b> ở thể hoàn thành: cạo xong một lượt.</div>'
    '<div class="hd-warn">Thân tương lai y như <b>бри́ться</b>: <b>побре́юсь, побре́ешься</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бри́ться</b> cạo râu (CHT) · <b>брить</b> cạo · <b>бри́тва</b> dao cạo</div>'
)

# --------------------------------------------------------------------- вымыться
S["вымыться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span>'
    '<span class="hd-gloss">RA HẾT — sạch tới cùng, như <b>вы́мыть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-мы-ть-ся</span>'
    '<span class="hd-gloss">RỬA (<b>мыть</b>) + phản thân: rửa CHÍNH MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>вы́мыть</b> rửa sạch bong + <b>-ся</b> = tắm cho mình sạch bong. '
    'Cặp thể thường ngày của <b>мы́ться</b> là <b>помы́ться</b>; <b>вы́мыться</b> nhấn kết quả SẠCH.</div>'
    '<div class="hd-warn">Thân đổi ы → о, trọng âm luôn trên <b>вы́</b>: <b>вы́моюсь, вы́моешься</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мы́ться</b> tắm (CHT) · <b>помы́ться</b> tắm xong · '
    '<b>вы́мыть</b> rửa sạch bong · <b>мы́ло</b> xà phòng</div>'
)

# --------------------------------------------------------------------- мыться
S["мыться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мы-</span>'
    '<span class="hd-gloss">RỬA — <b>мыть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть-ся</span>'
    '<span class="hd-gloss">đuôi nguyên thể + phản thân: rửa CHÍNH MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Rửa chính mình, cả người = tắm. Thân đổi ы → о y như <b>мыть</b>: '
    '<b>мо́юсь, мо́ешься</b> — <b>Я мо́юсь в ду́ше</b>.</div>'
    '<div class="hd-warn">Chỉ rửa mặt-tay là <b>умыва́ться</b>, không phải <b>мы́ться</b>.</div>'
    '<div class="hd-warn">Tắm cho SẠCH (xà phòng, vòi sen) là <b>мы́ться</b>; ngâm mình, tắm biển, '
    'tắm sông là <b>купа́ться</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>помы́ться</b>, <b>вы́мыться</b> tắm xong (HT) · <b>умыва́ться</b> rửa mặt · '
    '<b>мыть</b> rửa · <b>мы́ло</b> xà phòng</div>'
)

# --------------------------------------------------------------------- балерина
S["балерина"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — mượn nguyên khối tiếng Ý <i>ballerina</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhìn thấy ngay gốc <b>бал-</b> «nhảy múa» của <b>бале́т</b> và <b>бал</b>. '
    'Trọng âm ở <b>-ри́-</b> và đứng yên cả bảng.</div>'
    '<div class="hd-warn">Chỉ dùng cho NỮ. Nam diễn viên ba lê là <b>танцо́вщик</b> hoặc '
    '<b>арти́ст бале́та</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бале́т</b> ba lê · <b>бал</b> dạ hội khiêu vũ</div>'
)

# --------------------------------------------------------------------- афиша
S["афиша"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — mượn tiếng Pháp <i>affiche</i> «tờ dán lên».</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tờ dán ngoài nhà hát, rạp phim báo buổi diễn. Mở rộng ra là cả «lịch chiếu, '
    'lịch diễn»: <b>афи́ша кино́</b>.</div>'
    '<div class="hd-warn"><b>афи́ша</b> chỉ báo SỰ KIỆN (kịch, phim, hoà nhạc). Áp phích cổ động, '
    'tranh khẩu hiệu là <b>плака́т</b>.</div>'
)

# --------------------------------------------------------------------- архитектурный
S["архитектурный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">архитекту́р-</span>'
    '<span class="hd-gloss">KIẾN TRÚC — <b>архитекту́ра</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ «thuộc về»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bỏ <b>-а</b>, thêm <b>-ный</b>; trọng âm giữ nguyên trên <b>-ту́р-</b> — '
    'y như <b>культу́ра → культу́рный</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>архитекту́ра</b> kiến trúc · <b>архите́ктор</b> kiến trúc sư</div>'
)

# --------------------------------------------------------------------- документальный
S["документальный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">документ-</span>'
    '<span class="hd-gloss">TÀI LIỆU, giấy tờ — <b>докуме́нт</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́льн-ый</span>'
    '<span class="hd-gloss">đuôi tính từ quốc tế, = <i>-al</i> tiếng Anh</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Dựa trên tài liệu thật = <i>documentary</i>. Trọng âm nhảy từ <b>-ме́-</b> '
    'sang đuôi <b>-а́льный</b>, như <b>норма́льный</b>, <b>официа́льный</b>. Dạng ngắn hầu như không gặp.</div>'
    '<div class="hd-warn">Gặp gần như chỉ trong <b>документа́льный фильм</b> phim tài liệu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>докуме́нт</b> giấy tờ, tài liệu</div>'
)

# --------------------------------------------------------------------- мюзикл
S["мюзикл"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — mượn thẳng tiếng Anh <i>musical</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc xa với <b>му́зыка</b>, nhưng mượn qua tiếng Anh nên giữ âm '
    '<i>mju-</i>: viết <b>мю-</b>, không phải <b>му-</b>. Giống đực, đuôi phụ âm, trọng âm đầu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>му́зыка</b> âm nhạc · <b>музыка́нт</b> nhạc công</div>'
)

# --------------------------------------------------------------------- дирижёр
S["дирижёр"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дириж-</span>'
    '<span class="hd-gloss">ĐIỀU KHIỂN (Pháp <i>diriger</i>, = <i>direct</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ёр</span>'
    '<span class="hd-gloss">NGƯỜI LÀM (Pháp <i>-eur</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người điều khiển dàn nhạc. Đuôi <b>-ёр</b> luôn giữ trọng âm, cả bảng: '
    '<b>дирижёра, дирижёры</b>.</div>'
    '<div class="hd-warn">Động từ <b>дирижи́ровать</b> đòi cách 5, không phải cách 4: '
    '<b>дирижи́ровать орке́стром</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дирижи́ровать</b> chỉ huy dàn nhạc · cùng đuôi <b>-ёр</b>: '
    '<b>шофёр</b> tài xế · <b>режиссёр</b> đạo diễn</div>'
)

# --------------------------------------------------------------------- ансамбль
S["ансамбль"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — mượn tiếng Pháp <i>ensemble</i> «cùng nhau».</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một nhóm biểu diễn CÙNG NHAU — y như <i>ensemble</i> tiếng Anh. '
    'Trọng âm ở <b>-са́-</b>, đứng yên cả bảng.</div>'
    '<div class="hd-warn">Đuôi <b>-ь</b> mà giống ĐỰC, như <b>роя́ль</b> (cũng từ Pháp): '
    '<b>но́вый анса́мбль</b>, <b>анса́мбля</b>.</div>'
)

# --------------------------------------------------------------------- рояль
S["рояль"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — mượn tiếng Pháp <i>royal</i> «của vua».</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cây đàn «hoàng gia»: to, nằm ngang, đặt trên sân khấu. Chơi đàn dùng '
    '<b>на</b> + cách 6: <b>игра́ть на роя́ле</b>.</div>'
    '<div class="hd-warn"><b>роя́ль</b> là đàn NẰM (grand piano); đàn đứng để trong nhà là '
    '<b>пиани́но</b>.</div>'
    '<div class="hd-warn">Đuôi <b>-ь</b> mà giống ĐỰC: <b>большо́й роя́ль</b>.</div>'
)

# --------------------------------------------------------------------- сфотографироваться
S["сфотографироваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">chỉ đánh dấu XONG, không thêm nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-фотографи́роваться</span>'
    '<span class="hd-gloss">chụp ảnh mình — ánh sáng + vẽ + <b>-ся</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đứng cho người ta chụp một tấm, xong. Chia đổi <b>-ова-</b> → <b>-у-</b>: '
    '<b>сфотографи́руюсь, сфотографи́руешься</b>.</div>'
    '<div class="hd-warn">Bỏ <b>-ся</b> là mình chụp NGƯỜI KHÁC: <b>сфотографи́ровать</b> '
    '<b>дру́га</b>; còn <b>сфотографи́роваться с дру́гом</b> = chụp chung với bạn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>фотографи́роваться</b> chụp ảnh mình (CHT) · <b>сфотографи́ровать</b> chụp '
    '(người, vật) · <b>фото́граф</b> thợ ảnh</div>'
)

B = {
    "docbangmat": 71,
    "loitubat": 3,
    "nguonsai": 2,
    "baolen": [
        "Va chạm «tắm» мыться ↔ купаться: theo phân xử luồng chính, мыться GIỮ «tắm, rửa mình» (không đổi V); ô Hướng dẫn мыться có ô đỏ phân biệt với купа́ться. Phía k144 phải bỏ «tắm» khỏi купаться — chưa làm thì cụm vẫn trùng.",
        "V сфотографироваться -> 'được chụp ảnh, chụp ảnh mình' (khớp фотографироваться k77): ĐỔI chữ chứ không chỉ bỏ ngoặc, vì bỏ «(tự mình)» để lại «chụp ảnh» trơn trùng сфотографировать; cần duyệt.",
        "V các cặp thể chỉ badge thể tách: умываться/умыться «rửa mặt», бриться/побриться «cạo râu», выздоравливать «hồi phục, khỏi bệnh»/выздороветь «khỏi bệnh», мыться «tắm»/вымыться «tắm rửa, tắm cho sạch». документальный «tài liệu» trùng документ, badge từ loại tách.",
        "Vacham (đọc Anki 21/11) không thấy cụm trùng nào khác cho lô này; KHÔNG soi được nghĩa mới «hồi phục», «tắm rửa», «được chụp ảnh» với toàn bộ bộ sưu tập (lệnh dump Anki bị chặn) — luồng chính chạy lại `congcu.py vacham` sau nap.",
        "Không chắc (đã hạ chữ): про- = «xuyên qua» trong простудиться là cách đọc từ nguyên tự nhiên, không phải luật; рояль <- Pháp royal và насморк <- сморкать là từ nguyên, khá chắc.",
        "Nguồn sai đã bác: gloss Anh умываться/умыться «to wash oneself» quá rộng (thật: rửa mặt-tay) — giữ «rửa mặt»; gloss сфотографироваться «to take a picture» lệch chủ thể (thật: được chụp) — theo nghĩa thật.",
        "Họ hàng cố ý vắng 4 thẻ: ангина, афиша, ансамбль, рояль (mượn, đứng một mình).",
    ],
}
