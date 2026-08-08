# -*- coding: utf-8 -*-
"""k08 — concepts::misc: 15 danh từ rời, KHÔNG cùng một họ. Mỗi thẻ đứng một
mình (README §2b, §3): không có khối hệ thống dùng chung, tối đa 2 ô đỏ, nhắm
dưới một màn hình iPhone.

Trục thật của lô: 7/15 từ có bảng chia BẤT THƯỜNG (nguyên âm chạy, trọng âm
nhảy giữa số ít và số nhiều, một từ không biến cách) — mỗi thẻ đó mang đúng
MỘT câu chú ý đọc xong là hiểu cả bảng, chứ không kê bảng ra thêm lần nữa.
"""

# 🔴 KHÔNG dựng biến khối dùng chung rồi cộng vào mọi thẻ — xem README §3.

S = {}
V = {}

S["рисунок"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рис-</span>'
    '<span class="hd-gloss">gốc VẼ — chính là gốc của <b>рисова́ть</b> (vẽ)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-у́нок</span>'
    '<span class="hd-gloss">đuôi biến việc làm thành VẬT làm ra được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vẽ thì ra cái vẽ được — y hệt cặp <b>подари́ть</b> (tặng) → '
    '<b>пода́рок</b> (món quà). Đuôi <b>-ок</b> này gặp lại rất nhiều.</div>'
    '<div class="hd-why"><b>Chú ý bảng chia:</b> chữ <i>о</i> của <b>-ок</b> là nguyên âm '
    'chạy — hễ đuôi có nguyên âm là nó rơi mất, còn trọng âm thì đứng yên: '
    '<i>рису́нок → рису́нка, рису́нку, рису́нки</i>.</div>'
    '<div class="hd-warn">Vẽ bằng NÉT thì là <b>рису́нок</b> (hình vẽ, bản vẽ, hoa văn '
    'trên vải); còn bức hoạ treo tường là <b>карти́на</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рисова́ть</b> vẽ · <b>рисова́ние</b> việc vẽ, môn vẽ · '
    '<b>зарисо́вка</b> bản phác hoạ</div>'
)

S["диск"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — mượn nguyên khối từ tiếng Latin <i>discus</i> '
    '(cái đĩa ném), vốn của tiếng Hy Lạp. Danh từ giống đực đuôi phụ âm, biến cách đều '
    'tăm tắp và trọng âm không nhúc nhích.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng một từ Latin đó đẻ ra cả loạt từ tiếng Anh bạn đã biết: '
    '<i>disc, disk, discus, dish, desk</i>. Ở đây không có gì phải suy, chỉ cần nhận mặt '
    'bốn chữ <b>диск</b>.</div>'
    '<div class="hd-warn">Đây là đĩa TRÒN DẸT của kỹ thuật và thể thao: đĩa CD/DVD, ổ đĩa '
    'máy tính, đĩa ném. Cái đĩa ĂN CƠM là <b>таре́лка</b>, khác hẳn từ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ди́сковый</b> thuộc về đĩa · <b>дисково́д</b> ổ đĩa · '
    '<b>дискоте́ка</b> sàn nhảy (gốc là kho đĩa nhạc)</div>'
)

S["футбол"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">фут-</span>'
    '<span class="hd-gloss">foot — bàn chân</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бо́л</span>'
    '<span class="hd-gloss">ball — quả bóng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn nguyên cụm <i>football</i>, chép lại y cách đọc tiếng Anh nên '
    'trọng âm rơi vào mảnh sau. Mảnh <b>-бо́л</b> sống độc lập và luôn giữ trọng âm, ghép ra '
    'cả kệ môn thể thao: <b>волейбо́л</b>, <b>баскетбо́л</b>, <b>гандбо́л</b>.</div>'
    '<div class="hd-warn"><b>футбо́лка</b> không phải quả bóng nhỏ mà là ÁO PHÔNG — vốn là '
    'cái áo cầu thủ mặc, rồi thành tên gọi chung của áo thun.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>футболи́ст</b> cầu thủ bóng đá · <b>футбо́льный</b> thuộc bóng đá · '
    '<b>футбо́лка</b> áo phông</div>'
)

S["угол"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Danh từ gốc, không chẻ được. Nhưng thân của nó có hai mặt: dạng '
    'nguyên là <b>у́гол</b>, còn hễ thêm đuôi vào là thành <i>угл-</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Ấn–Âu với tiếng Latin <i>angulus</i>, tức là chính chữ '
    '<i>angle</i> của tiếng Anh — nghĩa hình học lẫn nghĩa góc nhà đều nằm trong một từ.</div>'
    '<div class="hd-why"><b>Chú ý bảng chia:</b> chỉ mỗi dạng nguyên <b>у́гол</b> là giữ chữ '
    '<i>о</i> và nhấn ở đầu; mọi ô còn lại rơi <i>о</i> rồi dồn trọng âm ra đuôi — '
    '<i>угла́, углу́, угло́м, углы́, угло́в</i>.</div>'
    '<div class="hd-warn">Cách 6 có hai dạng, chia việc rõ ràng: <b>в углу́</b> trong góc '
    '(phòng), <b>на углу́</b> ở góc phố — còn nói VỀ cái góc thì <b>об угле́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>треуго́льник</b> tam giác (ba góc) · <b>углово́й</b> ở góc · '
    '<b>уголо́к</b> góc nhỏ, xó</div>'
)

S["фильм"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — mượn thẳng chữ <i>film</i> của tiếng Anh, giữ '
    'nguyên cả nghĩa cuộn phim lẫn nghĩa bộ phim. Biến cách đều, trọng âm đứng yên.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ này sống mạnh nhất ở dạng ghép: cứ dán tên một thứ vào trước là '
    'ra loại phim đó, và trọng âm vẫn nằm nguyên chỗ cũ — <b>кинофи́льм</b>, '
    '<b>телефи́льм</b>.</div>'
    '<div class="hd-warn">Phim NÓI VỀ cái gì có hai lối: <b>фильм о войне́</b> (cách 6, '
    'trang trọng) hoặc <b>фильм про войну́</b> (cách 4, đời thường).</div>'
    '<div class="hd-warn"><b>фильм</b> là MỘT bộ phim cụ thể; còn nền điện ảnh nói chung và '
    'cả cái rạp thì là <b>кино́</b> — <b>идти́ в кино́</b> là đi xem phim ngoài rạp.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мультфи́льм</b> phim hoạt hình · <b>телефи́льм</b> phim truyền '
    'hình · <b>фильмоте́ка</b> kho phim</div>'
)

S["гимн"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — mượn từ tiếng Hy Lạp <i>hymnos</i> (bài ca ngợi '
    'ca thần linh), cùng nguồn với <i>hymn</i> của tiếng Anh.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không phải bài hát nào cũng là <b>гимн</b>: đây là bài ca CHÍNH '
    'THỨC, hát lên trong nghi lễ — <b>госуда́рственный гимн</b> là quốc ca. Bài hát thường '
    'thì gọi là <b>пе́сня</b>.</div>'
    '<div class="hd-warn">Nhìn giống mà khác gốc hẳn: <b>гимна́стика</b> và '
    '<b>гимна́зия</b> đi ra từ chữ Hy Lạp <i>gymnos</i> (trần trụi — chỗ tập luyện), không '
    'dính dáng gì tới <b>гимн</b>.</div>'
)

S["фон"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — mượn tiếng Pháp <i>fond</i> (đáy, nền), gốc Latin '
    '<i>fundus</i>, cùng nhà với <i>foundation</i> và <i>fundamental</i> của tiếng Anh: cái '
    'nằm dưới cùng, đằng sau tất cả.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nền của bức ảnh, của màn hình, của một câu chuyện — thứ ở phía sau '
    'để cho cái chính nổi lên.</div>'
    '<div class="hd-why"><b>Chú ý bảng chia:</b> thực tế từ này gần như chỉ dùng ở số ít; '
    'phần số nhiều hiếm tới mức các từ điển ghi trọng âm vênh nhau, đừng học thuộc nó.</div>'
    '<div class="hd-warn">Cụm phải thuộc: <b>на фо́не</b> + cách 2 = trên nền của…, giữa bối '
    'cảnh… — <b>на фо́не окна́</b> (trên nền cửa sổ), <b>на фо́не кри́зиса</b> (giữa lúc '
    'khủng hoảng).</div>'
    '<div class="hd-warn"><b>фон</b> (nền) không dính gì tới mảnh <i>-фон</i> trong '
    '<b>телефо́н</b>, <b>микрофо́н</b> — mảnh kia là tiếng Hy Lạp <i>phone</i> (âm thanh).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>фо́новый</b> thuộc về nền, chạy nền</div>'
)

S["пятно"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пятн-</span>'
    '<span class="hd-gloss">VẾT, DẤU để lại trên một bề mặt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́</span>'
    '<span class="hd-gloss">đuôi danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một mảnh <i>пятн-</i> lo hết mọi thứ dây bẩn và mọi thứ lốm đốm: '
    'vết mực trên áo, đốm trên da con báo, cả vết nhơ danh dự.</div>'
    '<div class="hd-why"><b>Chú ý bảng chia:</b> trọng âm nhảy hẳn giữa hai số — số ít nhấn '
    'đuôi (<i>пятно́, пятна́, пятну́</i>), số nhiều kéo về thân (<i>пя́тна</i>); riêng cách 2 '
    'số nhiều chèn thêm <i>е</i> cho khỏi kẹt ba phụ âm: <b>пя́тен</b>.</div>'
    '<div class="hd-warn">Trông giống mà không họ hàng: <b>пять</b> (năm) và '
    '<b>пя́тница</b> (thứ sáu) khác gốc hoàn toàn với <b>пятно́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пятни́стый</b> lốm đốm · <b>пя́тнышко</b> đốm nhỏ · '
    '<b>запятна́ть</b> làm vấy bẩn, bôi nhọ</div>'
)

S["золото"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">зо́лот-</span>'
    '<span class="hd-gloss">VÀNG — thứ ánh lên màu vàng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi danh từ giống trung, đây là tên một CHẤT</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc Ấn–Âu với chữ <i>gold</i> của tiếng Anh, và trong chính '
    'tiếng Nga thì cùng nhà với <b>жёлтый</b> (vàng — màu) và <b>зелёный</b> (xanh lá): cả ba '
    'đi ra từ một nghĩa gốc là ánh lên, sáng lên.</div>'
    '<div class="hd-warn"><b>зо́лото</b> là CHẤT, là kim loại. Nói về màu của một vật thì '
    'phải chuyển sang tính từ: <b>золото́й</b> (vàng óng, bằng vàng) hoặc <b>жёлтый</b> '
    '(vàng thường).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>золото́й</b> bằng vàng, quý như vàng · <b>золоти́стый</b> vàng '
    'óng · <b>позоло́та</b> lớp mạ vàng</div>'
)

S["фото"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">фо́то</span>'
    '<span class="hd-gloss">chặt ngắn từ <b>фотогра́фия</b>, giữ lại đúng nửa đầu</span></div>'
    '<div class="hd-row"><span class="hd-piece">фот-</span>'
    '<span class="hd-gloss">tiếng Hy Lạp: ÁNH SÁNG (+ <i>-графия</i> ghi, vẽ)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen của cả từ đầy đủ là vẽ bằng ánh sáng. Nhận ra mảnh '
    '<i>фото-</i> là mở được cả loạt từ: máy ảnh, thợ ảnh, quang hợp.</div>'
    '<div class="hd-why"><b>Chú ý bảng chia:</b> vì là từ chặt ngắn nên nó KHÔNG biến cách — '
    'cả sáu cách, cả số ít lẫn số nhiều đều viết y hệt <b>фо́то</b>: <i>на фо́то, два фо́то, '
    'мно́го фо́то</i>.</div>'
    '<div class="hd-warn">Từ đứng im thì tính từ phải gánh hết phần cách, và gánh theo giống '
    'TRUNG: <b>ста́рое фо́то</b> (tấm ảnh cũ), <b>на э́том фо́то</b> (trên tấm ảnh này).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>фотогра́фия</b> bức ảnh; nghề ảnh · <b>фото́граф</b> thợ chụp ảnh · '
    '<b>фотоаппара́т</b> máy ảnh</div>'
)

S["место"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мест-</span>'
    '<span class="hd-gloss">CHỖ, khoảng không gian dành cho cái gì</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mảnh <i>мест-</i> nằm sẵn trong mấy từ dùng hằng ngày: '
    '<b>вме́сте</b> cùng nhau (chung một chỗ) · <b>вме́сто</b> thay chỗ cho · '
    '<b>ме́стный</b> tại chỗ, địa phương.</div>'
    '<div class="hd-why"><b>Chú ý bảng chia:</b> số ít nhấn thân, số nhiều dồn hết trọng âm '
    'ra đuôi — nên <b>ме́ста</b> (nhấn đầu) là cách 2 số ít, còn <b>места́</b> (nhấn cuối) là '
    'số nhiều: <i>два ме́ста</i> nhưng <i>все места́, мно́го мест</i>.</div>'
    '<div class="hd-warn">Ba nghĩa dùng thật, đừng chỉ nhớ nghĩa nơi chốn: chỗ trống '
    '(<b>есть свобо́дное ме́сто?</b>), chỗ ngồi đánh số trên vé, và chỗ làm việc '
    '(<b>рабо́чее ме́сто</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вме́сте</b> cùng nhau · <b>вме́сто</b> thay cho · '
    '<b>ме́стный</b> địa phương · <b>ме́стность</b> vùng, địa hình</div>'
)

S["пожар"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố: phủ khắp, lan ra khắp</span></div>'
    '<div class="hd-row"><span class="hd-piece">-жа́р</span>'
    '<span class="hd-gloss">SỨC NÓNG, hơi lửa — chính là danh từ <b>жар</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nóng phủ khắp thì thành đám cháy. Mảnh <i>жар-</i> quen mặt ở '
    '<b>жа́рко</b> (trời nóng) và <b>жа́рить</b> (rán, nướng) — cùng một hơi lửa đó, chỉ khác '
    'quy mô.</div>'
    '<div class="hd-warn"><b>пожа́р</b> là TAI HOẠ, không phải ngọn lửa nói chung: ngọn lửa là '
    '<b>ого́нь</b>, đống lửa trại là <b>костёр</b>. Cháy nhà thì gọi <b>пожа́рных</b> (lính '
    'cứu hoả).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жар</b> hơi nóng; cơn sốt · <b>жа́рко</b> nóng · '
    '<b>жа́рить</b> rán, nướng · <b>пожа́рный</b> lính cứu hoả</div>'
)

S["шар"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn một mảnh, không chẻ được: <b>шар</b> là KHỐI CẦU — hình '
    'tròn đặc, tròn đều mọi phía.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cứ là vật tròn phồng lên thì gọi bằng từ này: bóng bay, viên bi, quả '
    'địa cầu. Dạng nhỏ <b>ша́рик</b> mới là cái hay nghe nhất ngoài đời.</div>'
    '<div class="hd-why"><b>Chú ý bảng chia:</b> số ít nhấn thân (<i>ша́ра, ша́ру, ша́ром</i>), '
    'sang số nhiều thì trọng âm dồn hết ra đuôi — <i>шары́, шаро́в, шара́м, шара́ми</i>.</div>'
    '<div class="hd-warn">Hai cụm phải thuộc: <b>возду́шный шар</b> quả bóng bay, khinh khí '
    'cầu · <b>земно́й шар</b> quả địa cầu, Trái Đất.</div>'
    '<div class="hd-warn">Quả bóng để CHƠI thể thao không phải <b>шар</b> mà là <b>мяч</b> — '
    '<b>футбо́льный мяч</b>. <b>шар</b> chỉ là khối cầu về mặt hình dạng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ша́рик</b> quả bóng nhỏ, bóng bay · <b>шарово́й</b> hình cầu</div>'
)

S["билет"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — mượn tiếng Pháp <i>billet</i> (mảnh giấy nhỏ, tờ '
    'ghi). Kiểu Pháp nên trọng âm rơi vào âm cuối và đứng yên suốt bảng: '
    '<i>биле́т, биле́та, биле́ты</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc là TỜ GIẤY NHỎ CÓ GIÁ TRỊ — từ đó ra cả tấm vé lẫn tờ '
    'phiếu, nên đừng ngạc nhiên khi gặp nó ngoài chỗ bán vé.</div>'
    '<div class="hd-warn">Đi tới đâu thì <b>биле́т на</b> + cách 4: <b>биле́т на по́езд</b> vé '
    'tàu, <b>биле́т на конце́рт</b>. Vào bên trong một nơi thì <b>биле́т в кино́</b>, '
    '<b>биле́т в теа́тр</b>.</div>'
    '<div class="hd-warn">Nghĩa thứ hai gặp suốt ở trường: <b>биле́т</b> còn là PHIẾU ĐỀ THI — '
    '<b>вы́тянуть биле́т</b> là bốc trúng phiếu đề.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>биле́тный</b> thuộc về vé (<b>биле́тная ка́сса</b> quầy bán vé) · '
    '<b>билетёр</b> người soát vé</div>'
)

S["бюст"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — mượn tiếng Pháp <i>buste</i>, gốc Ý <i>busto</i> '
    '(phần thân trên). Biến cách đều, trọng âm đứng yên.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỉ một hình ảnh lo cả hai nghĩa: PHẦN NGƯỜI TỪ NGỰC TRỞ LÊN. Tạc đá '
    'tới đó thì ra bức tượng bán thân; nói về cơ thể thì là vòng ngực.</div>'
    '<div class="hd-warn">Nghĩa nào là do ngữ cảnh, không có từ riêng: <b>бюст Пу́шкина</b> '
    'tượng bán thân Pushkin, còn trong tiệm quần áo thì đang nói tới số đo vòng ngực.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бюстга́льтер</b> áo ngực — mượn tiếng Đức <i>Büstenhalter</i>, '
    'nghĩa đen là cái giữ ngực</div>'
)


# --------------------------------------------------------------------------
# FIELD `Vietnamese` — đề bài của deck 1-go (README §2c).
# Cả 15 từ đều là danh từ nên badge PoS/giống đã lo phần từ loại; ở đây chỉ
# lo đúng một việc: chặn những từ Nga KHÁC cũng dịch ra đúng dòng tiếng Việt đó.
# --------------------------------------------------------------------------
V['рисунок'] = 'hình vẽ, bản vẽ, hoạ tiết'
V['диск'] = 'đĩa tròn, đĩa CD, ổ đĩa'
V['угол'] = 'góc'
V['фильм'] = 'bộ phim'
V["гимн"] = "quốc ca, bài ca chính thức của một nước hay tổ chức"   # đụng пе́сня
V["пятно"] = "vết bẩn, vết ố, đốm trên bề mặt"
V['золото'] = 'vàng'
V['фото'] = 'bức ảnh, tấm hình'
V['место'] = 'chỗ, nơi, chỗ ngồi, chỗ làm'
V["пожар"] = "đám cháy, vụ hoả hoạn"                    # đụng ого́нь = ngọn lửa
V['шар'] = 'khối cầu, hình cầu, bóng bay'
V['билет'] = 'vé, thẻ, phiếu đề thi'
V['бюст'] = 'tượng bán thân, vòng ngực'
