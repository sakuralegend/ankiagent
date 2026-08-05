# -*- coding: utf-8 -*-
"""k22 — life::food: đồ ăn thức uống hằng ngày; trục của lô là chỗ CÁI TÊN
lộ ra cách làm ra món đó (ма́сло ← ма́зать phết, пи́во ← пить uống,
сыр ← сыро́й chua/ẩm) và một dúm từ mượn đứng riêng (изю́м, бато́н, суп,
рис, карто́фель) — mượn thì nói thẳng là mượn, không bịa gốc Nga."""

# 🔴 KHÔNG dựng biến khối dùng chung (HE/LUAT/THE…) rồi cộng vào mọi thẻ.

S = {}

S["лук"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được — nhưng đây thực ra là '
    '<b>hai</b> từ khác hẳn nhau tình cờ đọc giống nhau.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>лук</b> “hành” là từ vay của tiếng Giéc-manh cổ, '
    'cùng gốc với <i>leek</i> (tỏi tây) trong tiếng Anh. Còn <b>лук</b> “cung '
    'bắn tên” là gốc Slav nghĩa “cong”, gốc đó còn thấy ở <b>лука́вый</b> '
    '(quanh co, ranh mãnh) và <b>излу́чина</b> (khúc sông cong).</div>'
    '<div class="hd-warn">⚠️ Mức tin: đây là hai <b>từ nguyên</b> riêng biệt, '
    'không phải một từ nhiều nghĩa. Đừng bắc cầu “cây cung cong như củ hành” — '
    'nhớ tách hẳn hai nghĩa ra.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лу́ковица</b> củ hành; củ (của cây hoa) · '
    '<b>лу́ковый</b> thuộc về hành · <b>зелёный лук</b> hành lá</div>'
)

S["изюм"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn thẳng của các tiếng Turk '
    '(<i>üzüm</i> = quả nho), vào tiếng Nga nguyên khối.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bên tiếng Turk từ này là nho <i>nói chung</i>; sang '
    'tiếng Nga nghĩa hẹp lại còn đúng nho <b>đã sấy khô</b>. Từ mượn thường bị '
    'thu hẹp như vậy — nhớ cái nghĩa hẹp, đừng nhớ nghĩa gốc.</div>'
    '<div class="hd-warn"><b>изю́м</b> chỉ dùng cho nho khô. Nho tươi là '
    '<b>виногра́д</b> — hai từ không thay nhau được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>изю́минка</b> hạt nho khô; nghĩa bóng rất hay dùng: '
    '“nét duyên riêng, cái làm nên chất riêng”</div>'
)

S["батон"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn tiếng Pháp <i>bâton</i> = cây '
    'gậy.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng một từ Pháp đó cũng vào tiếng Anh thành '
    '<i>baton</i> (gậy chỉ huy). Ổ bánh mì này mang tên “cây gậy” vì hình nó '
    'dài và thuôn.</div>'
    '<div class="hd-warn"><b>бато́н</b> là ổ bánh mì trắng <b>dài</b>. Bánh mì '
    'nói chung là <b>хлеб</b>; ổ đen vuông vức là <b>буха́нка</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бато́нчик</b> thanh nhỏ hình que (thanh sô cô la, '
    'thanh ngũ cốc)</div>'
)

S["пиво"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пи-</span>'
    '<span class="hd-gloss">gốc UỐNG, đúng gốc của <b>пить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-во</span>'
    '<span class="hd-gloss">đuôi tạo danh từ giống trung “thứ dùng để…”</span>'
    '</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là “thứ để uống” — bia từng là đồ uống mặc '
    'định nên chiếm luôn cái tên chung. Đuôi <b>-во</b> này còn đẻ ra '
    '<b>ва́рево</b> (thứ để nấu, món hầm) và <b>ку́рево</b> (thứ để hút).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пить</b> uống · <b>напи́ток</b> đồ uống · '
    '<b>пивна́я</b> quán bia · <b>пивно́й</b> thuộc về bia</div>'
)

S["яблоко"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">я́блок-</span>'
    '<span class="hd-gloss">gốc TÁO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc Ấn–Âu rất cổ, cùng nhà với <i>apple</i> (Anh) và '
    '<i>Apfel</i> (Đức) — nghe kỹ vẫn còn nhận ra. Nghĩa “quả cầu” của nó nằm '
    'trong <b>глазно́е я́блоко</b> = nhãn cầu (quả táo của mắt).</div>'
    '<div class="hd-warn">Giống trung nhưng số nhiều <b>KHÔNG</b> lấy đuôi '
    '<b>-а</b> như thường lệ: <b>я́блоки</b> (nhiều quả táo), cách 2 số nhiều '
    '<b>я́блок</b>. Trọng âm đứng yên ở đầu suốt cả bảng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>я́блоня</b> cây táo · <b>я́блочный</b> thuộc về táo '
    '(<b>я́блочный сок</b> nước táo)</div>'
)

S["молоко"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">молок-</span>'
    '<span class="hd-gloss">gốc SỮA, dạng Nga có đủ hai chữ <b>о</b></span>'
    '</div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Ấn–Âu với <i>milk</i> (Anh) và <i>Milch</i> '
    '(Đức); tiếng Nga chèn thêm nguyên âm nên thành <b>-оло-</b>. Trọng âm '
    'nằm ở đuôi <b>молоко́</b>, nhưng vừa thêm hậu tố là nó chạy ngược vào '
    'giữa: <b>моло́чный</b>.</div>'
    '<div class="hd-warn">Cùng gốc này còn một dạng Slav cổ <b>млеч-</b> '
    '(không có <b>-оло-</b>), nay chỉ còn trong <b>Мле́чный Путь</b> = dải '
    'Ngân Hà. Gặp cặp <b>оло/ле</b> kiểu này thì đó là hai lớp cũ–mới của '
    'CÙNG một gốc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>моло́чный</b> thuộc về sữa · <b>моло́чник</b> bình '
    'rót sữa · <b>сгущённое молоко́</b> sữa đặc</div>'
)

S["масло"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">маз-</span>'
    '<span class="hd-gloss">gốc BÔI, PHẾT — như <b>ма́зать</b> phết lên</span>'
    '</div>'
    '<div class="hd-row"><span class="hd-piece">-сло</span>'
    '<span class="hd-gloss">đuôi chỉ CÁI DÙNG ĐỂ…, như <b>весло́</b> mái '
    'chèo</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: “thứ để phết” → bơ, rồi rộng ra thành mọi '
    'thứ dầu mỡ. Ghép <b>маз+сло</b> thì <b>з</b> bị chữ <b>с</b> nuốt mất, '
    'còn lại <b>ма́сло</b>. Bảng chia có hai chỗ lệch: số nhiều dồn trọng âm ra '
    'đuôi <b>масла́</b> (các loại dầu), còn cách 2 số nhiều chèn thêm một chữ '
    '<b>е</b> cho đọc được: <b>ма́сел</b>.</div>'
    '<div class="hd-warn">Một mình <b>ма́сло</b> không cho biết loại nào. Phải '
    'kèm tính từ: <b>сли́вочное ма́сло</b> bơ (làm từ kem sữa) · '
    '<b>расти́тельное ма́сло</b> dầu ăn thực vật.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ма́зать</b> phết, bôi · <b>масли́на</b> quả ô liu '
    '(quả cho dầu) · <b>маслёнка</b> hộp đựng bơ</div>'
)

S["мясо"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мяс-</span>'
    '<span class="hd-gloss">gốc THỊT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc Slav cổ, chỉ phần thịt trên cơ thể lẫn thịt để '
    'ăn — nên câu “vết thương lộ cả thịt” cũng dùng từ này. Nó '
    '<b>không</b> họ hàng gì với <i>meat</i> tiếng Anh, dù nghe na ná; đừng '
    'bắc cầu.</div>'
    '<div class="hd-warn">Thịt con gì thì có từ riêng, không ghép với '
    '<b>мя́со</b>: đuôi <b>-ина</b> nghĩa là “thịt của…” — <b>говя́дина</b> '
    'thịt bò · <b>свини́на</b> thịt lợn · <b>бара́нина</b> thịt cừu. Riêng gà '
    'thì gọi thẳng tên con vật: <b>ку́рица</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мясно́й</b> thuộc về thịt · <b>мясни́к</b> người '
    'bán thịt · <b>мясору́бка</b> máy xay thịt (thịt + <b>руби́ть</b> chặt)</div>'
)

S["яйцо"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">яй-</span>'
    '<span class="hd-gloss">gốc TRỨNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-цо</span>'
    '<span class="hd-gloss">vốn là đuôi làm nhỏ, nay dính hẳn vào từ</span>'
    '</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc Ấn–Âu xa, cùng nhà với <i>ovum</i> / <i>oval</i> '
    'trong tiếng Latinh–Anh: cái hình bầu dục. Đuôi làm nhỏ đã chết nghĩa nên '
    'đừng dịch là “trứng con”.</div>'
    '<div class="hd-warn">Số nhiều lệch hai đường, phải thuộc: trọng âm chạy '
    'ngược về đầu <b>я́йца</b> (những quả trứng), và cách 2 số nhiều rụng luôn '
    'chữ <b>й</b>: <b>яи́ц</b> (<b>пять яи́ц</b> năm quả trứng).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>яи́чница</b> trứng rán (chỗ <b>чн</b> đọc thành '
    '“шн”, y như <b>коне́чно</b>) · <b>яи́чный</b> thuộc về trứng</div>'
)

S["суп"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn tiếng Pháp <i>soupe</i> hồi thế '
    'kỷ 18, vào nguyên khối một âm tiết.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng một từ Pháp cho ra <i>soup</i> (Anh) và '
    '<i>Suppe</i> (Đức) — nhận mặt là xong, không có gì để phân tích. Chỗ duy '
    'nhất cần nhớ là bảng chia: số nhiều dồn trọng âm ra đuôi <b>супы́</b> '
    '(các món súp).</div>'
    '<div class="hd-warn">Muốn nói <b>một ít</b> thì cách 2 có dạng riêng đuôi '
    '<b>-у</b>: <b>нале́й су́пу</b> = rót cho ít súp (so với <b>таре́лка '
    'су́па</b> = một đĩa súp). Dạng cũ này chỉ còn ở vài từ chỉ chất, trong lô '
    'này là <b>суп</b>, <b>са́хар</b>, <b>чай</b>.</div>'
)

S["сахар"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn qua tiếng Hy Lạp '
    '<i>sakkharon</i>, gốc xa hơn nữa là tiếng Phạn <i>sharkara</i> = hạt '
    'cát, hạt sỏi.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng một gốc đó đi đường khác vào tiếng Anh thành '
    '<i>sugar</i> và <i>saccharin</i>. Cái nghĩa gốc “hạt cát” còn sống '
    'nguyên trong tiếng Nga lẫn tiếng Việt: <b>са́харный песо́к</b> = đường '
    'cát. Cách 2 cũng có dạng “một ít” <b>са́хару</b> — cùng kiểu với '
    '<b>су́пу</b> ở thẻ <b>суп</b> cùng lô.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>са́харный</b> thuộc về đường · <b>са́харница</b> '
    'lọ đựng đường (đuôi <b>-ница</b> = đồ để đựng)</div>'
)

S["сыр"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сыр-</span>'
    '<span class="hd-gloss">gốc ẨM, CHUA — cùng gốc với <b>сыро́й</b></span>'
    '</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Phô mai là sữa <b>để chua lại</b> cho đông, nên nó '
    'mang đúng cái gốc của <b>сыро́й</b> (ẩm ướt; còn sống, chưa nấu). Số '
    'nhiều dồn trọng âm ra đuôi: <b>сыры́</b> = các loại phô mai.</div>'
    '<div class="hd-warn">⚠️ Mức tin: mối nối <b>сыр–сыро́й</b> là <b>từ '
    'nguyên</b>, không phải luật suy ra được — dùng nó để nhớ thì tốt, đừng '
    'đem áp cho từ khác.</div>'
    '<div class="hd-warn">Thành ngữ phải thuộc: <b>как сыр в ма́сле</b> '
    '(thường đi với <b>ката́ться</b>) = sống sung sướng đủ đầy. Nghĩa đen: '
    'lăn lóc như phô mai trong bơ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сы́рный</b> thuộc về phô mai · <b>сы́рник</b> bánh '
    'rán làm từ phô mai tươi</div>'
)

S["рис"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: từ đi vòng quanh thế giới, vào tiếng '
    'Nga qua châu Âu, gốc rất xa là tiếng Hy Lạp <i>oryza</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng một từ đó cho ra <i>rice</i> (Anh), <i>Reis</i> '
    '(Đức), <i>riso</i> (Ý). Một từ mượn ngắn, không có gì bên trong để chẻ — '
    'nhận mặt chữ là đủ.</div>'
    '<div class="hd-warn">Bẫy mặt chữ: <b>рисова́ть</b> (vẽ) <b>không</b> họ '
    'hàng gì với <b>рис</b> — nó mượn đường khác, từ tiếng Đức qua tiếng Ba '
    'Lan. Giống nhau ba chữ đầu thôi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ри́совый</b> thuộc về gạo (<b>ри́совая ка́ша</b> '
    'cháo gạo)</div>'
)

S["орех"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">оре́х-</span>'
    '<span class="hd-gloss">gốc HẠT CỨNG, gốc Slav, không chẻ nhỏ hơn</span>'
    '</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ Slav thuần, trọng âm đứng yên ở đuôi gốc suốt cả '
    'bảng chia (<b>оре́хи</b>, <b>оре́хов</b>) — không có gì lệch để phải nhớ '
    'thêm.</div>'
    '<div class="hd-warn">Một mình <b>оре́х</b> chỉ là “quả hạch” chung chung. '
    'Loại nào thì kèm tính từ: <b>гре́цкий оре́х</b> quả óc chó (nghĩa đen '
    '“hạt Hy Lạp” — chú ý là <b>гре́цкий</b>, không phải <b>гре́ческий</b>) · '
    '<b>лесно́й оре́х</b> hạt phỉ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оре́ховый</b> thuộc về hạt; màu nâu hạt dẻ · '
    '<b>оре́шек</b> hạt nhỏ</div>'
)

S["огурец"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">огур-</span>'
    '<span class="hd-gloss">phần mượn, tự nó không mang nghĩa trong tiếng '
    'Nga</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ц</span>'
    '<span class="hd-gloss">đuôi giống đực, có nguyên âm chạy</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn tiếng Hy Lạp <i>aguros</i> = <b>chưa chín</b> — '
    'đúng thật, dưa chuột là thứ hái ăn lúc còn xanh, để chín là hỏng. Mức '
    'tin: đây là từ nguyên, không suy ra được.</div>'
    '<div class="hd-warn">Đuôi <b>-ец</b> luôn có <b>nguyên âm chạy</b>: hễ '
    'thêm đuôi vào là chữ <b>е</b> biến mất và trọng âm nhảy ra đuôi mới — '
    '<b>огуре́ц</b> nhưng <b>огурца́</b>, <b>огурцо́м</b>, số nhiều '
    '<b>огурцы́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>огу́рчик</b> quả dưa chuột nhỏ (nói thân mật) · '
    '<b>огуре́чный</b> thuộc về dưa chuột</div>'
)

S["картофель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn tiếng Đức <i>Kartoffel</i>, gốc '
    'xa hơn là tiếng Ý <i>tartufolo</i> = nấm cục — hai thứ củ mọc dưới đất '
    'nên bị gọi chung tên.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <b>-ь</b> ở đây <b>không</b> cho biết giống: '
    '<b>карто́фель</b> là giống đực, trong khi <b>соль</b> cùng lô cũng đuôi '
    '<b>-ь</b> lại là giống cái. Gặp đuôi mềm thì phải nhớ giống theo từng '
    'từ, không suy được.</div>'
    '<div class="hd-warn">Trong bữa ăn hằng ngày người Nga nói '
    '<b>карто́шка</b>; <b>карто́фель</b> là từ sách vở, biển hàng, thực đơn. '
    'Nó còn là danh từ <b>gộp</b> — một chữ số ít đã có nghĩa cả đống củ, nên '
    'gần như không dùng số nhiều.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>карто́шка</b> khoai tây (lời nói thường ngày) · '
    '<b>карто́фельный</b> thuộc về khoai tây (<b>карто́фельное пюре́</b> khoai '
    'tây nghiền)</div>'
)

S["соль"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">соль</span>'
    '<span class="hd-gloss">gốc trơn, gốc Ấn–Âu <i>sal-</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng một gốc cổ với <i>salt</i> (Anh), <i>sal</i> '
    '(Latinh) và cả <i>salad</i> (nghĩa gốc: rau đã <b>ướp muối</b>). Đuôi '
    '<b>-ь</b> ở đây là giống cái. Bảng chia có một chỗ lệch: số nhiều từ '
    'cách 2 trở đi dồn trọng âm ra đuôi — <b>соле́й</b>, <b>соля́ми</b>, '
    'trong khi <b>со́ли</b> vẫn giữ trọng âm đầu.</div>'
    '<div class="hd-warn">Nghĩa bóng rất hay gặp: <b>соль</b> = cái cốt lõi, '
    'cái tinh tuý — <b>в э́том вся соль</b> = mấu chốt nằm ở chỗ đó.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>солёный</b> mặn; muối chua · <b>соли́ть</b> cho '
    'muối vào, ướp muối · <b>соло́нка</b> lọ muối để bàn</div>'
)

S["позавтракать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố làm thành thể hoàn thành; ở đây KHÔNG '
    'thêm nghĩa gì</span></div>'
    '<div class="hd-row"><span class="hd-piece">за́втрак-</span>'
    '<span class="hd-gloss">bữa sáng (vốn là <b>за</b> + <b>у́тро</b>: cái '
    'dành cho sáng ra)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi động từ nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vì cùng cái gốc “sáng mai” đó mà <b>за́втра</b> = '
    'ngày mai và <b>за́втрак</b> = bữa sáng giống nhau tới thế. Chia theo lối '
    'thường, trọng âm dính chặt ở <b>за́</b>: <b>поза́втракаю</b>, '
    '<b>поза́втракаешь</b>, quá khứ <b>поза́втракал</b>.</div>'
    '<div class="hd-warn">Cặp thể: <b>за́втракать</b> = đang ăn sáng / hay ăn '
    'sáng; <b>поза́втракать</b> = ăn xong bữa sáng, một lần rồi thôi. Nói '
    '<b>я поза́втракал</b> nghĩa là bữa đó đã xong.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>за́втрак</b> bữa sáng · <b>за́втра</b> ngày mai · '
    'cùng khuôn “tên bữa ăn → động từ”: <b>обе́д</b> → <b>обе́дать</b> ăn '
    'trưa, <b>у́жин</b> → <b>у́жинать</b> ăn tối</div>'
)

S["пить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пи-</span>'
    '<span class="hd-gloss">gốc UỐNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi động từ nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng cái gốc nằm trong <b>пи́во</b> cùng lô: “thứ để '
    'uống”. Bảng chia lệch hẳn, phải nhớ riêng chứ không suy từ '
    '<b>пить</b> ra được: <b>пью, пьёшь, пьёт, пьём, пьёте, пьют</b>, sai '
    'khiến <b>пей</b>. Quá khứ dồn trọng âm ra đuôi ở giống cái: <b>пил</b> '
    'nhưng <b>пила́</b>.</div>'
    '<div class="hd-warn">Cặp thể: <b>пить</b> = đang uống / hay uống; '
    '<b>вы́пить</b> = uống cạn một lần rồi xong (tiền tố <b>вы-</b> luôn hút '
    'trọng âm về mình).</div>'
    '<div class="hd-warn">Tiếng Nga không có động từ “khát” riêng: nói '
    '<b>я хочу́ пить</b> = tôi muốn uống, tức là tôi khát.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пи́во</b> bia · <b>напи́ток</b> đồ uống · '
    '<b>пья́ный</b> say rượu</div>'
)

S["вишня"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ви́шн-</span>'
    '<span class="hd-gloss">gốc ANH ĐÀO, gốc Slav chung</span></div>'
    '<div class="hd-row"><span class="hd-piece">-я</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một từ dùng cho cả <b>cây</b> lẫn <b>quả</b>, và '
    'thường dùng số ít theo nghĩa gộp (cả rổ anh đào vẫn là <b>ви́шня</b>). '
    'Cách 2 số nhiều chèn thêm chữ <b>е</b> cho đọc được: <b>ви́шен</b> — y '
    'như <b>ма́сел</b> ở thẻ <b>ма́сло</b> cùng lô.</div>'
    '<div class="hd-warn">Đừng lẫn hai loại: <b>ви́шня</b> quả nhỏ, sẫm màu, '
    '<b>chua</b> (để làm mứt, nhân bánh) — còn loại to, ngọt, ăn tươi là '
    '<b>чере́шня</b>. Tiếng Việt gọi chung là anh đào nên rất dễ gõ nhầm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вишнёвый</b> (thuộc) anh đào; màu đỏ sẫm — vở kịch '
    '<b>Вишнёвый сад</b> của Chekhov chính là “Vườn anh đào”</div>'
)


# ── Đề bài mặt trước deck 1-go (README §2c): sát tới mức chỉ có MỘT đáp án.
# Không ghi từ loại / giống / thể / phản thân — bốn badge đã in sẵn.
V = {
    'лук': 'củ hành, cây cung',
    'батон': 'ổ bánh mì dài, bánh mì que',
    'масло': 'bơ, dầu ăn, dầu',
    'суп': 'món súp, canh',
    'сахар': 'đường',
    'рис': 'gạo, hạt gạo',
    'орех': 'quả hạch, hạt cứng, hạt dẻ',
    'картофель': 'khoai tây, cây khoai tây',
    'позавтракать': 'ăn sáng',
    'пить': 'uống',
    'вишня': 'quả anh đào chua, cây anh đào chua',
}
