# -*- coding: utf-8 -*-
"""k49 — places::city: đi lại trong thành phố. Bốn động từ "đến/tới" chẻ đôi
theo ĐI BỘ hay ĐI XE, cộng nhóm chỉ hướng và tên các điểm mốc giao thông."""

S = {}
V = {}

S["дойти"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI TẬN ĐÍCH, hết chặng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-йти</span>'
    '<span class="hd-gloss">ĐI BỘ (chính là идти́)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">до- ở đây chính là giới từ <b>до</b> "cho tới" đã học, nên đích '
    'đến cũng nhắc lại nó: <i>дойти́ до угла́</i> = đi bộ tới tận góc phố.</div>'
    '<div class="hd-warn">Quá khứ KHÔNG dựng từ nguyên thể mà mượn nguyên thân của идти́: '
    '<b>дошёл</b>, <b>дошла́</b>, <b>дошли́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>доходи́ть</b> dạng chưa xong · <b>дохо́д</b> thu nhập '
    '(cái "đi tới" túi mình) · <b>до</b> cho tới</div>'
)

S["доехать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI TẬN ĐÍCH, hết chặng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́хать</span>'
    '<span class="hd-gloss">ĐI BẰNG XE</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Song sinh với <b>дойти́</b>, chỉ đổi đôi chân lấy bánh xe. Đích '
    'cũng đi kèm до: <i>дое́хать до це́нтра</i>.</div>'
    '<div class="hd-warn">Chia ra thì х biến thành д: <b>дое́ду</b>, <b>дое́дешь</b>, '
    '<b>дое́дут</b> — không suy thẳng từ nguyên thể được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>доезжа́ть</b> dạng chưa xong · <b>по́езд</b> tàu hoả · '
    '<b>пое́здка</b> chuyến đi</div>'
)

S["прийти"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">TỚI NƠI, đến gần</span></div>'
    '<div class="hd-row"><span class="hd-piece">-йти</span>'
    '<span class="hd-gloss">ĐI BỘ (chính là идти́)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">до- nhấn "tới tận đích", còn при- chỉ nhấn "đã có mặt": '
    '<b>дойти́</b> là đi hết chặng, <b>прийти́</b> là đến nơi.</div>'
    '<div class="hd-warn">Chữ й chỉ sống ở nguyên thể; chia ngôi ra là mất: <b>приду́</b>, '
    '<b>придёшь</b>, <b>приду́т</b> — không có «прийду».</div>'
    '<div class="hd-warn">Quá khứ mượn thân của идти́: <b>пришёл</b>, <b>пришла́</b>, '
    '<b>пришли́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>приходи́ть</b> dạng chưa xong · <b>прихо́д</b> sự đến · '
    '<b>прихо́жая</b> phòng ngoài cửa</div>'
)

S["приехать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">TỚI NƠI, đến gần</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́хать</span>'
    '<span class="hd-gloss">ĐI BẰNG XE</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Với người Nga, tới nơi bằng chân và tới nơi bằng xe là hai động từ '
    'khác hẳn nhau: <b>прийти́</b> hay <b>прие́хать</b> — chọn sai là sai nghĩa.</div>'
    '<div class="hd-warn">Chia ra thì х biến thành д: <b>прие́ду</b>, <b>прие́дешь</b>, '
    '<b>прие́дут</b>; mệnh lệnh mượn của dạng chưa xong: <b>приезжа́й</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>приезжа́ть</b> dạng chưa xong · <b>прие́зд</b> sự đến bằng xe · '
    '<b>прие́зжий</b> người mới tới</div>'
)

S["ехать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">е́ха-</span>'
    '<span class="hd-gloss">ĐI BẰNG PHƯƠNG TIỆN — gốc trơn, chia ra thành е́д-</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính gốc này đẻ ra <b>по́езд</b> tàu hoả — "cái để người ta '
    'е́хать". Nhớ по́езд là giữ được thân е́д-.</div>'
    '<div class="hd-why">Mệnh lệnh không lấy từ chính nó: dạng chuẩn là <b>поезжа́й</b>, '
    'còn <b>езжа́й</b> chỉ dùng khi nói năng thân mật.</div>'
    '<div class="hd-warn">Hiện tại lấy thân е́д-: <b>е́ду</b>, <b>е́дешь</b>, <b>е́дут</b> — '
    'nguyên thể có х nhưng bảng chia thì không.</div>'
    '<div class="hd-warn">Là chuyến đi MỘT CHIỀU đang diễn ra: <i>я е́ду в шко́лу</i> lúc '
    'này; còn đi lại thường xuyên là <b>е́здить</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>е́здить</b> đi xe nhiều chiều · <b>по́езд</b> tàu hoả · '
    '<b>пое́здка</b> chuyến đi · <b>езда́</b> sự đi xe</div>'
)

S["находиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">LÊN TỚI, chạm vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ход-</span>'
    '<span class="hd-gloss">ĐI (gốc của ходи́ть)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ться</span>'
    '<span class="hd-gloss">đuôi phản thân: hành động quay về chính mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>находи́ть</b> là "tìm ra"; thêm -ся thành "tự thấy mình ở đâu" '
    '→ nằm ở đâu. Đúng lối nói của Pháp <i>se trouver</i>, Anh <i>to be found</i>.</div>'
    '<div class="hd-warn">Ngôi "tôi" đổi д thành ж và trọng âm ra đuôi: <b>нахожу́сь</b>; '
    'từ ngôi thứ hai trở đi trọng âm lùi vào gốc: <b>нахо́дишься</b>, <b>нахо́дятся</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>находи́ть</b> tìm thấy · <b>нахо́дка</b> vật nhặt được · '
    '<b>найти́</b> tìm ra · <b>ходи́ть</b> đi lại</div>'
)

S["налево"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">VỀ PHÍA (có chuyển động)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ле́во</span>'
    '<span class="hd-gloss">BÊN TRÁI, từ ле́вый</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">на- là rẽ về hướng đó, с- là đứng yên ở hướng đó: '
    '<b>нале́во</b> sang trái ↔ <b>сле́ва</b> ở bên trái.</div>'
    '<div class="hd-warn"><b>ходи́ть нале́во</b> không phải "đi sang trái" mà là ngoại '
    'tình; <b>рабо́тать нале́во</b> là làm thêm chui.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ле́вый</b> bên trái · <b>сле́ва</b> ở bên trái · '
    '<b>напра́во</b> sang phải</div>'
)

S["направо"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">VỀ PHÍA (có chuyển động)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пра́во</span>'
    '<span class="hd-gloss">BÊN PHẢI, từ пра́вый</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>пра́вый</b> vừa là "bên phải" vừa là "đúng" — y hệt chữ '
    '<i>right</i> tiếng Anh. Từ nghĩa "đúng" mà ra <b>пра́вда</b> và <b>пра́во</b>.</div>'
    '<div class="hd-why">Bộ ba phải thuộc khi hỏi đường: <b>напра́во</b> · <b>нале́во</b> · '
    '<b>пря́мо</b> đi thẳng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пра́вый</b> bên phải, đúng · <b>спра́ва</b> ở bên phải · '
    '<b>пра́вда</b> sự thật · <b>пра́во</b> quyền</div>'
)

S["напротив"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">VỀ PHÍA, quay mặt tới</span></div>'
    '<div class="hd-row"><span class="hd-piece">-про́тив</span>'
    '<span class="hd-gloss">CHỐNG LẠI, phía đối lập</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">"Quay mặt về phía đối lập" — đứng trong không gian thì là '
    '<i>đối diện</i>, đặt vào lời nói thì là <i>trái lại</i>.</div>'
    '<div class="hd-warn">Đòi cách 2 đứng sau: <b>напро́тив до́ма</b> = đối diện ngôi '
    'nhà.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>про́тив</b> chống lại · <b>противополо́жный</b> đối lập · '
    '<b>проти́вник</b> đối thủ</div>'
)

S["туда"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ту-</span>'
    '<span class="hd-gloss">ĐÓ, KIA — cùng gốc với тот</span></div>'
    '<div class="hd-row"><span class="hd-piece">-да́</span>'
    '<span class="hd-gloss">đuôi chỉ HƯỚNG ĐI TỚI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiếng Nga tách hẳn "ở đó" và "tới đó" thành hai từ: <b>там</b> '
    'là chỗ đứng yên, <b>туда́</b> là chỗ đi tới. Cặp tương ứng: <b>здесь</b> / '
    '<b>сюда́</b>.</div>'
    '<div class="hd-warn"><b>туда́ и обра́тно</b> = đi và về — đúng chữ ghi trên vé khứ '
    'hồi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>там</b> ở đó · <b>отту́да</b> từ đó tới · <b>сюда́</b> tới '
    'đây</div>'
)

S["далеко"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">далек-</span>'
    '<span class="hd-gloss">XA — gốc của далёкий, cùng họ với даль</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́</span>'
    '<span class="hd-gloss">đuôi biến tính từ thành trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chữ ё chỉ sống được khi mang trọng âm; ở đây trọng âm dời hẳn ra '
    'đuôi nên nó tụt xuống thành е: <b>далёкий</b> → <b>далеко́</b>.</div>'
    '<div class="hd-warn"><b>далеко́ не</b> không phải "không xa" mà là "còn lâu mới": '
    '<i>он далеко́ не глуп</i> = anh ta chẳng ngu chút nào.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>далёкий</b> xa · <b>даль</b> phương xa · <b>да́льше</b> xa hơn '
    '· <b>вдали́</b> ở đằng xa</div>'
)

S["недалеко"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не-</span>'
    '<span class="hd-gloss">KHÔNG — dính liền thành một chữ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-далеко́</span>'
    '<span class="hd-gloss">XA</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gắn не- vào trạng từ là cách tiếng Nga dựng nghĩa ngược ngay '
    'trong một chữ. Nó chỉ phủ nhận "xa", nhẹ hơn <b>бли́зко</b> vốn khẳng định là sát.</div>'
    '<div class="hd-warn">Muốn nói cách chỗ nào thì thêm от + cách 2: '
    '<b>недалеко́ от до́ма</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>далеко́</b> xa · <b>далёкий</b> xa · <b>даль</b> phương xa</div>'
)

S["пешком"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пеш-</span>'
    '<span class="hd-gloss">ĐI CHÂN, từ пе́ший</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́м</span>'
    '<span class="hd-gloss">dấu vết đuôi cách 5, nay đã hoá đá thành trạng từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cách 5 trả lời "bằng cái gì", nên nghĩa đen là "bằng chân". Cùng '
    'gốc có <b>пешехо́д</b> = пеш + ход, người-đi-bộ — chữ trên biển báo sang đường.</div>'
    '<div class="hd-warn"><b>идти́ пешко́м</b> không thừa: <b>идти́</b> chỉ nói "đi", phải '
    'có <b>пешко́м</b> mới chốt là bằng chân chứ không phải bằng xe.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пе́ший</b> đi bộ · <b>пешехо́д</b> người đi bộ · '
    '<b>пехо́та</b> bộ binh</div>'
)

S["нужно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">нуж-</span>'
    '<span class="hd-gloss">SỰ CẦN, thiếu thốn — gốc của нужда́</span></div>'
    '<div class="hd-row"><span class="hd-piece">-но</span>'
    '<span class="hd-gloss">đuôi giống trung, ở đây làm vị ngữ không ngôi</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Câu không có chủ ngữ: người cần đứng ở cách 3, việc cần làm đứng '
    'ở nguyên thể — <i>мне ну́жно идти́</i> = tôi cần đi.</div>'
    '<div class="hd-warn">Cái cần là ĐỒ VẬT thì đuôi phải chạy theo đồ vật đó: '
    '<b>мне ну́жен биле́т</b> · <b>мне нужна́ ка́рта</b> · <b>мне нужны́ де́ньги</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ну́жный</b> cần thiết · <b>нужда́</b> nhu cầu, sự thiếu '
    'thốn</div>'
)

S["адрес"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">а́дрес</span>'
    '<span class="hd-gloss">mượn nguyên khối, KHÔNG chẻ được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn từ tiếng Pháp <i>adresse</i>, cùng cội với <i>address</i> '
    'tiếng Anh — chỉ cần nhớ mặt chữ Nga, nghĩa thì đã biết sẵn.</div>'
    '<div class="hd-warn">Số nhiều không lấy đuôi -ы mà lấy -а́ có trọng âm: '
    '<b>адреса́</b> — cùng kiểu với <b>дом</b> → <b>дома́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>а́дресный</b> thuộc về địa chỉ · <b>адресова́ть</b> gửi tới '
    'địa chỉ</div>'
)

S["схема"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">схе́ма</span>'
    '<span class="hd-gloss">mượn nguyên khối, KHÔNG chẻ được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ Hy Lạp <i>skhēma</i> "hình, dáng" — tiếng Anh giữ thành '
    '<i>scheme</i> và <i>schema</i>. Nghĩa lõi: bản vẽ thu gọn của một thứ phức tạp.</div>'
    '<div class="hd-warn"><b>схе́ма метро́</b> = sơ đồ tàu điện ngầm — tấm bảng bạn tra '
    'mỗi ngày trong thành phố.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>схемати́ческий</b> thuộc sơ đồ · <b>схемати́чный</b> sơ '
    'lược</div>'
)

S["переход"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span>'
    '<span class="hd-gloss">QUA, SANG BÊN KIA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-хо́д</span>'
    '<span class="hd-gloss">SỰ ĐI, gốc của ходи́ть</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen "sự đi qua", nên vừa là chỗ đi qua đường vừa là sự '
    'chuyển từ trạng thái này sang trạng thái khác. Cùng khuôn: <b>вход</b> lối vào, '
    '<b>вы́ход</b> lối ra.</div>'
    '<div class="hd-warn"><b>пешехо́дный перехо́д</b> = vạch sang đường; còn dưới ga tàu '
    'điện ngầm, <b>перехо́д</b> là hành lang nối sang tuyến khác.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>переходи́ть</b> đi qua · <b>ход</b> sự đi, nước cờ · '
    '<b>вход</b> lối vào · <b>вы́ход</b> lối ra</div>'
)

S["пересадка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span>'
    '<span class="hd-gloss">SANG CHỖ KHÁC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сад-</span>'
    '<span class="hd-gloss">ĐẶT NGỒI XUỐNG, gốc của сади́ться</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">đuôi biến việc làm thành danh từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen "đặt sang chỗ khác" giải thích cả ba nghĩa: đặt mình '
    'sang xe khác, đặt cây sang chậu khác, đặt tạng sang người khác.</div>'
    '<div class="hd-warn">Cách 2 số nhiều chạy thêm nguyên âm о: <b>переса́док</b> — luật '
    'của danh từ đuôi -ка khi bỏ đuôi thì hai phụ âm chụm sát vào nhau.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пересади́ть</b> đặt sang chỗ khác · <b>сади́ться</b> ngồi '
    'xuống · <b>сад</b> vườn</div>'
)

S["остановка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">tiền tố thể, ở đây KHÔNG mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-станов-</span>'
    '<span class="hd-gloss">ĐỨNG LẠI, gốc của станови́ться</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">đuôi biến việc làm thành danh từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ <b>останови́ться</b> "dừng lại" mà ra, nên nó vừa là bản thân '
    'sự dừng, vừa là cái chỗ xe dừng.</div>'
    '<div class="hd-warn">Cách 2 số nhiều chạy thêm о: <b>остано́вок</b> — y hệt '
    '<b>переса́дка</b> → <b>переса́док</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>останови́ться</b> dừng lại · <b>останови́ть</b> cho dừng · '
    '<b>стать</b> đứng lại, trở thành</div>'
)

# ---------------------------------------------------------------------------
# Ô ĐỀ BÀI tiếng Việt (README §2c) — thuần danh sách nghĩa, ngăn bằng dấu phẩy.
# Phương thức di chuyển (đi bộ / đi xe) là MỘT PHẦN NGHĨA của động từ chuyển
# động tiếng Nga nên được viết thẳng vào danh sách, không phải chú thích.
V["дойти"]      = "đi bộ tới tận nơi, đi bộ đến được, đạt tới"
V["доехать"]    = "đi xe tới tận nơi, đi xe đến được"
V["прийти"]     = "đến, tới, đến nơi"
V["приехать"]   = "đến bằng xe, tới nơi bằng xe"
V["ехать"]      = "đi xe, đi bằng xe, đang đi tới bằng xe"
V["находиться"] = "nằm ở, tọa lạc, được đặt ở"
V["налево"]     = "sang trái, về bên trái"
V["направо"]    = "sang phải, về bên phải"
V["напротив"]   = "đối diện, trái lại"
V["туда"]       = "tới đó, sang đó, về phía đó"
V["далеко"]     = "xa, ở xa"
V["недалеко"]   = "không xa"
V["пешком"]     = "đi bộ"
V["нужно"]      = "cần, phải"
V["схема"]      = "sơ đồ, kế hoạch"
V["переход"]    = "lối qua đường, vạch sang đường, sự chuyển tiếp, sự chuyển đổi"
V["пересадка"]  = "chuyển tàu xe, quá cảnh, cấy ghép"
V["остановка"]  = "bến xe buýt, điểm dừng xe, sự dừng lại"
