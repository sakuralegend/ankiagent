# -*- coding: utf-8 -*-
"""k148 — life::food: món ăn, cách nấu, giặt giũ, người và nghề, tính từ dân tộc.

Chỗ cần nhất quán trong lô:
(1) gốc жар- = HƠI NÓNG, LỬA — жа́рить/пожа́рить/жа́реный, khớp жар·жа́ркий (k27), пожа́р (k08).
(2) gốc вар- = ĐUN SÔI — самова́р, khớp вари́ть (k102), по́вар (k71); жа́рить đối lập вари́ть.
(3) gốc корм- = THỨC ĂN — покорми́ть, khớp корми́ть/накорми́ть (k139), cùng khuôn giải thích.
(4) gốc друг-/друж- = BẠN, г → ж — дру́жеский, khớp дру́жба (k04), дру́жный (k104), дружи́ть (k139).
(5) gốc -вык-/-ыч- = QUEN — обы́чай, khớp обы́чный/обыкнове́нный (k108); необыкнове́нный ở k149.
(6) стира́ть có HAI cặp hoàn thành: постира́ть (giặt) · стере́ть (xoá).
Họ hàng cố ý vắng: котле́та, шашлы́к (từ mượn đứng một mình).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "библиотекарь": "thủ thư",                    # bỏ ngoặc «(nam)» — badge giống đực đã in
    "котлета": "chả thịt băm, miếng cốt lết",     # «chả thịt viên» lệch sang фрикаде́лька; gloss «patty / cutlet»
    "виноград": "nho, cây nho",                   # dấu «;» → dấu phẩy
    "жареный": "chiên, rán, nướng",               # bỏ ngoặc «(tính từ)» — badge từ loại tách khỏi жа́рить
    "покормить": "cho ăn, cho bú",                # bỏ ngoặc «(một lần)»; «cho bú» từ gloss «breast-feed / nurse» — tách khỏi накорми́ть «cho ăn, cho ăn no»
    "пожарить": "chiên, rán",                     # bỏ ngoặc «(xong)» — badge thể tách khỏi жа́рить
    "самовар": "ấm samovar",                      # bỏ ngoặc giải thích
    "постирать": "giặt",                          # bỏ «xong (một lần)» — badge thể tách khỏi стира́ть
    "стирать": "giặt, xoá",                       # bỏ ngoặc «(quần áo)»; thêm «xoá» từ gloss «to erase / to wipe off»
}

# ----------------------------------------------------------------- обычай
S["обычай"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">tiền tố</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ы́ч-</span>'
    '<span class="hd-gloss">QUEN — <b>-вык-</b> của <b>привы́кнуть</b>, <b>к → ч</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ай</span>'
    '<span class="hd-gloss">đuôi danh từ giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Điều cả cộng đồng đã QUEN làm ⇒ phong tục: <b>ру́сские обы́чаи</b>. '
    'Từ nó ra tính từ <b>обы́чный</b> thường lệ.</div>'
    '<div class="hd-warn">Thói quen của MỘT người là <b>привы́чка</b>; <b>обы́чай</b> là tục lệ '
    'chung của làng, của dân tộc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обы́чный</b> thường lệ · <b>обы́чно</b> thường · <b>привы́кнуть</b> quen · '
    '<b>привы́чка</b> thói quen · <b>обыкнове́нный</b> thông thường</div>'
)

# ----------------------------------------------------------------- дружеский
S["дружеский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">друж-</span>'
    '<span class="hd-gloss">BẠN (<b>друг</b>, г → ж)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-еск-ий</span>'
    '<span class="hd-gloss">đuôi tính từ «thuộc về, kiểu của»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Kiểu của bạn bè» ⇒ thân tình: <b>дру́жеский разгово́р</b>, '
    '<b>дру́жеский сове́т</b>. Đuôi <b>-ский</b> nên không có dạng ngắn; trạng từ là '
    '<b>по-дру́жески</b>, cùng khuôn <b>по-ру́сски</b>.</div>'
    '<div class="hd-warn"><b>дру́жеский</b> = giữa BẠN BÈ, thân tình; <b>дру́жный</b> = hoà thuận, '
    'đồng lòng: <b>дру́жная семья́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>друг</b> bạn · <b>дру́жба</b> tình bạn · <b>дружи́ть</b> chơi thân · '
    '<b>дру́жный</b> hoà thuận</div>'
)

# ----------------------------------------------------------------- славянский
S["славянский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">славя́н-</span>'
    '<span class="hd-gloss">NGƯỜI SLAV — <b>славя́не</b> (số ít <b>славяни́н</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ск-ий</span>'
    '<span class="hd-gloss">đuôi tính từ, như <b>ру́сский</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người Nga, Ukraina, Ba Lan, Séc… đều là <b>славя́не</b>: '
    '<b>славя́нские языки́</b> các tiếng Slav. Thân <b>славя́н-</b> lấy từ số nhiều, '
    'vì <b>-ин</b> rụng ở số nhiều như <b>англича́нин → англича́не</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: <b>славя́не</b> gốc từ <b>сло́во</b> (người nói cùng thứ tiếng) '
    'hay <b>сла́ва</b> (vinh quang) — giới ngôn ngữ còn tranh cãi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>славяни́н</b> một người Slav · <b>славя́не</b> các dân tộc Slav</div>'
)

# ----------------------------------------------------------------- интернациональный
S["интернациональный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">интер-</span>'
    '<span class="hd-gloss">GIỮA (Latin <i>inter</i>, như <b>интерне́т</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-национ-</span>'
    '<span class="hd-gloss">DÂN TỘC (<b>на́ция</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́льн-ый</span>'
    '<span class="hd-gloss">đuôi tính từ quốc tế</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Khớp từng mảnh <i>inter-nation-al</i>. Dịch mảnh sang Nga ra '
    '<b>междунаро́дный</b>. Dạng ngắn như <b>национа́льный</b>: giống đực chèn <b>е</b> — '
    '<b>интернациона́лен</b>, ba dạng kia chỉ cắt đuôi.</div>'
    '<div class="hd-warn"><b>междунаро́дный</b> = GIỮA các nước: <b>междунаро́дный аэропо́рт</b>. '
    '<b>интернациона́льный</b> = GỒM nhiều dân tộc: <b>интернациона́льная семья́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>на́ция</b> dân tộc · <b>национа́льный</b> thuộc dân tộc · '
    '<b>национа́льность</b> dân tộc, tộc người</div>'
)

# ----------------------------------------------------------------- кассир
S["кассир"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">касс-</span>'
    '<span class="hd-gloss">QUẦY TIỀN (<b>ка́сса</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́р</span>'
    '<span class="hd-gloss">người làm nghề — đuôi mượn Pháp, như <b>банки́р</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người ngồi ở <b>ка́сса</b> ⇒ thu ngân, y như <i>cash → cashier</i>. '
    'Trọng âm nhảy sang đuôi: <b>ка́сса → касси́р</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ка́сса</b> quầy thu ngân, quầy vé · <b>ка́ссовый</b> thuộc quầy tiền</div>'
)

# ----------------------------------------------------------------- дипломат
S["дипломат"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дипло́м-</span>'
    '<span class="hd-gloss">VĂN THƯ chính thức (Hy Lạp <i>diplōma</i> «tờ gấp đôi»)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́т</span>'
    '<span class="hd-gloss">người — đuôi mượn qua tiếng Pháp</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ngoại giao xưa xoay quanh văn thư, quốc thư ⇒ người lo việc đó là '
    '<b>диплома́т</b>, y hệt <i>diplomat</i>. Ngày nay <b>дипло́м</b> là tấm bằng tốt nghiệp.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дипло́м</b> bằng tốt nghiệp · <b>диплома́тия</b> ngoại giao · '
    '<b>дипломати́ческий</b> thuộc ngoại giao</div>'
)

# ----------------------------------------------------------------- библиотекарь
S["библиотекарь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">библиоте́к-</span>'
    '<span class="hd-gloss">THƯ VIỆN (<b>библиоте́ка</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-арь</span>'
    '<span class="hd-gloss">người làm việc ở đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người trông kho sách ⇒ thủ thư. Cùng khuôn <b>апте́ка → апте́карь</b> '
    'người bán thuốc. Trọng âm đứng yên ở <b>-те́-</b>; đuôi <b>-арь</b> ở đây là giống ĐỰC, '
    'như <b>слова́рь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>библиоте́ка</b> thư viện · <b>библиоте́чный</b> thuộc thư viện</div>'
)

# ----------------------------------------------------------------- говядина
S["говядина"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">говя́д-</span>'
    '<span class="hd-gloss">BÒ — từ cổ <i>говядо</i> «bò, gia súc», cùng gốc Ấn-Âu với <i>cow</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ин-а</span>'
    '<span class="hd-gloss">THỊT của con vật đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <b>-ина</b> biến tên con vật thành tên thịt: <b>свинья́ → свини́на</b> '
    'thịt lợn. Chỉ dùng số ít.</div>'
    '<div class="hd-warn">Con bò là <b>коро́ва</b>, thịt bò là <b>говя́дина</b> — khác hẳn mặt chữ, '
    'giống <i>cow ↔ beef</i> tiếng Anh.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>говя́жий</b> bằng thịt bò · <b>свини́на</b> thịt lợn (cùng đuôi)</div>'
)

# ----------------------------------------------------------------- котлета
S["котлета"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn Pháp <i>côtelette</i> «miếng sườn nhỏ» '
    '(<i>côte</i> xương sườn) — chính là chữ <i>cốt lết</i> trong tiếng Việt.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Sang Nga nó đổi nghĩa: <b>котле́та</b> thường là miếng CHẢ THỊT BĂM nặn dẹt '
    'rồi rán — món nhà nào cũng có: <b>котле́ты с карто́шкой</b>.</div>'
)

# ----------------------------------------------------------------- виноград
S["виноград"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вино-</span>'
    '<span class="hd-gloss">RƯỢU VANG (<b>вино́</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-град</span>'
    '<span class="hd-gloss">VƯỜN có rào — dạng cổ của <b>го́род</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Vườn làm rượu vang» ⇒ cây nho, quả nho. <b>-град = го́род</b> còn thấy '
    'trong tên thành phố: <b>Волгогра́д</b>.</div>'
    '<div class="hd-warn">Danh từ TẬP HỢP: <b>купи́ть виногра́д</b> mua nho (số ít). Một quả là '
    '<b>виногра́дина</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вино́</b> rượu vang · <b>виногра́дник</b> vườn nho · <b>го́род</b> thành phố</div>'
)

# ----------------------------------------------------------------- жареный
S["жареный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">жа́р-</span>'
    '<span class="hd-gloss">HƠI NÓNG, LỬA (<b>жар</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ен-ый</span>'
    '<span class="hd-gloss">đuôi «đã bị làm» — từ động từ <b>жа́рить</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đã bị <b>жа́рить</b>» ⇒ rán, chiên, nướng: <b>жа́реная карто́шка</b> '
    'khoai tây rán, <b>жа́реная ры́ба</b> cá rán.</div>'
    '<div class="hd-warn">Đứng trơn viết MỘT <b>н</b>: <b>жа́реный</b>. Có tiền tố hoặc có từ đi kèm '
    'thì thành HAI <b>н</b>: <b>поджа́ренный</b>, <b>жа́ренный в ма́сле</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жа́рить</b> rán, nướng · <b>жар</b> hơi nóng · <b>жа́ркий</b> nóng nực</div>'
)

# ----------------------------------------------------------------- шашлык
S["шашлык"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn tiếng Tatar Krym, gốc <i>şiş</i> «cái xiên».</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thịt xiên que nướng trên than. Trọng âm luôn ở đuôi, đuôi thêm vào là nó '
    'chạy theo: <b>шашлыка́</b>, <b>шашлыко́м</b>, <b>шашлыки́</b> — như <b>стол → стола́</b>.</div>'
    '<div class="hd-warn"><b>пое́хать на шашлыки́</b> (số nhiều) = đi dã ngoại nướng thịt — '
    'thú vui cuối tuần của người Nga.</div>'
)

# ----------------------------------------------------------------- покормить
S["покормить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tạo thể hoàn thành, kèm chút nghĩa «một bữa, một chút»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-корм-и-ть</span>'
    '<span class="hd-gloss">cho ăn (<b>корми́ть</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cho ăn một bữa, xong việc: <b>покорми́ть ко́шку</b>; với em bé còn là cho bú. '
    'Chia y hệt <b>корми́ть</b>: <b>покормлю́</b>, <b>поко́рмишь</b>; ai → cách 4, gì → cách 5.</div>'
    '<div class="hd-warn"><b>покорми́ть</b> chỉ nói ĐÃ cho ăn; <b>накорми́ть</b> nhấn kết quả: '
    'cho ăn tới NO.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>корми́ть</b> cho ăn · <b>накорми́ть</b> cho ăn no · <b>корм</b> thức ăn cho thú</div>'
)

# ----------------------------------------------------------------- жарить
S["жарить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">жар-</span>'
    '<span class="hd-gloss">HƠI NÓNG, LỬA (<b>жар</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đưa vào hơi lửa» ⇒ rán, chiên trong dầu hoặc nướng trên lửa: '
    '<b>жа́рить мя́со</b>. Chia đều, trọng âm đứng yên ở gốc: <b>жа́рю</b>, <b>жа́ришь</b>. '
    'Cặp hoàn thành: <b>пожа́рить</b>.</div>'
    '<div class="hd-warn">Có NƯỚC thì là <b>вари́ть</b>: <b>вари́ть суп</b>, nhưng '
    '<b>жа́рить карто́шку</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жар</b> hơi nóng · <b>жа́реный</b> đã rán · <b>жа́ркий</b> nóng nực · '
    '<b>пожа́р</b> đám cháy</div>'
)

# ----------------------------------------------------------------- пожарить
S["пожарить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tạo thể hoàn thành, không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-жар-и-ть</span>'
    '<span class="hd-gloss">rán, nướng (<b>жа́рить</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp hoàn thành của <b>жа́рить</b>, chia y hệt: <b>пожа́рю</b>, '
    '<b>пожа́ришь</b> — <b>пожа́рить я́йца</b> rán xong mấy quả trứng.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>пожа́р</b> đám cháy: cùng gốc <b>жар</b>, nhưng ở đó '
    '<b>по-</b> là «lan khắp».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жа́рить</b> rán, nướng · <b>жа́реный</b> đã rán · <b>пожа́р</b> đám cháy</div>'
)

# ----------------------------------------------------------------- самовар
S["самовар"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сам-</span>'
    '<span class="hd-gloss">TỰ (<b>сам</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о-</span>'
    '<span class="hd-gloss">nguyên âm nối hai gốc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вар</span>'
    '<span class="hd-gloss">ĐUN SÔI (<b>вари́ть</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Ấm tự đun»: lò than nằm ngay trong lòng ấm, nước tự sôi để pha trà. '
    'Cùng khuôn <b>самолёт</b> «tự bay».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>самолёт</b> máy bay · <b>вари́ть</b> nấu, luộc · <b>по́вар</b> đầu bếp</div>'
)

# ----------------------------------------------------------------- постирать
S["постирать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tạo thể hoàn thành, không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-стир-а-ть</span>'
    '<span class="hd-gloss">giặt (<b>стира́ть</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp hoàn thành của <b>стира́ть</b> ở nghĩa GIẶT: <b>постира́ть руба́шку</b>. '
    'Chia đều: <b>постира́ю</b>, <b>постира́ешь</b>.</div>'
    '<div class="hd-warn">Nghĩa XOÁ của <b>стира́ть</b> có cặp khác: <b>стере́ть</b>. '
    '<b>постира́ть</b> chỉ là giặt.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>стира́ть</b> giặt · <b>сти́рка</b> việc giặt giũ · '
    '<b>стира́льная маши́на</b> máy giặt</div>'
)

# ----------------------------------------------------------------- стирать
S["стирать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">tiền tố «khỏi, đi»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тир-а-ть</span>'
    '<span class="hd-gloss">CHÀ, XÁT — gốc <b>тер-/тир-</b> của <b>тере́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Chà cho đi mất»: chà vải ⇒ GIẶT, chà lên bảng ⇒ XOÁ — '
    '<b>стира́ть с доски́</b>. Hai nghĩa hai cặp hoàn thành: <b>постира́ть</b> giặt xong, '
    '<b>стере́ть</b> xoá xong.</div>'
    '<div class="hd-warn">Quần áo, vải → <b>стира́ть</b>; tay, bát, sàn, xe → <b>мыть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>постира́ть</b> giặt xong · <b>стере́ть</b> xoá xong · <b>сти́рка</b> việc giặt giũ</div>'
)

B = {
    "docbangmat": 62,
    "loitubat": 2,
    "nguonsai": 1,
    "baolen": [
        "V покормить ↔ накормить (k139 «cho ăn, cho ăn no»): RÚT GỌN không gỡ được — bỏ ngoặc thì còn «cho ăn», nằm gọn trong danh sách của накорми́ть. Tôi THÊM «cho bú» (gloss «to breast-feed / to nurse / to suckle») ⇒ «cho ăn, cho bú». Trái lời dặn «đừng thêm chữ» — cần duyệt; phương án lùi: «cho ăn» và chấp nhận đề bài hai đáp án.",
        "V интернациональный ↔ международный (k108 «quốc tế»): GIỮ NGUYÊN «quốc tế, đa quốc tịch», không khai V. Rút gọn thành «quốc tế» là trùng TOÀN BỘ (cả hai đều tính từ, không badge nào tách). «đa quốc tịch» là nghĩa thật (gồm nhiều dân tộc: интернациона́льная семья́/кома́нда) nhưng gloss tiếng Anh chỉ ghi «international» — cần duyệt.",
        "V стирать: thêm «xoá» (gloss «to erase / to wipe off») ⇒ «giặt, xoá» — cần duyệt. Bỏ «lau» vì dễ đụng nghĩa của động từ khác.",
        "V котлета: đổi «miếng chả thịt viên» → «chả thịt băm, miếng cốt lết» — «thịt viên» là фрикаде́лька, gloss chỉ «patty / cutlet» — cần duyệt.",
        "V пожарить «chiên, rán» trùng hai nghĩa với жа́рить «chiên, rán, nướng» và жа́реный — để nguyên vì badge thể / từ loại tách.",
        "Nguồn sai (1): BAT THUONG của шашлык ghi «trọng âm DỊCH ngay trong số ít» — gây hiểu lầm, thật ra trọng âm ĐỨNG YÊN ở âm tiết cuối (шашлы́к → шашлыка́, kiểu стол → стола́). Viết theo bảng, không theo dòng ghi chú.",
        "Lỗi tự bắt (2): библиоте́карь viết «đuôi -арь LUÔN giống đực» — nói quá, hạ thành «ở đây»; покорми́ть viết «với em bé LÀ cho bú» — nói quá, sửa «còn là».",
        "Không chắc: виногра́д = вино + град (= го́род) và говя́дина cùng gốc Ấn-Âu với «cow» — viết thẳng vì là từ nguyên chuẩn (Vasmer), không hạ mức tin; славя́не ← сло́во/сла́ва đã hạ mức tin bằng ô ⚠️.",
        "Họ hàng cố ý vắng: котле́та, шашлы́к (từ mượn đứng một mình). Không đụng file k149 (необыкнове́нный chỉ nhắc trong docstring).",
    ],
}
