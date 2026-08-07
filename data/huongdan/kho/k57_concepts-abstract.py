# -*- coding: utf-8 -*-
"""k57 — concepts-abstract: lô KHÔNG đồng nhất, tên topic chỉ là nhãn xếp kho.
Bên trong là danh từ trừu tượng (вина, начало, счастье, сожаление, особенность),
hai từ mượn quốc tế (физика, спорт, тип), một lời chào (привет), hai danh từ
dân tộc giống cái (англичанка, немка) và một tính từ quan hệ (китайский).
Mỗi thẻ soạn độc lập, KHÔNG ép một trục chung.
"""

# 🔴 KHÔNG dựng biến khối dùng chung (HE/LUAT/THE…) rồi cộng vào mọi thẻ.
# Đó là cách cũ, đã bỏ 28/07 — xem README §3.

S = {}
V = {}

# ------------------------------------------------- danh từ dựng từ động từ
S["упражнение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">упражн-</span>'
    '<span class="hd-gloss">gốc của <b>упражня́ть</b> rèn, luyện</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ giống TRUNG, tên của chính việc đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <b>-ение</b> biến động từ thành tên gọi của việc: '
    '"rèn" → "cái để rèn" = bài tập. Cùng khuôn với <b>сожале́ние</b> trong lô này, '
    'và trọng âm hai từ đều rơi đúng vào chữ <b>е</b> mở đầu cái đuôi ấy.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>упражня́ть</b> rèn (trí nhớ, cơ bắp) · '
    '<b>упражня́ться</b> tự tập luyện</div>'
)

S["физика"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">физ-</span>'
    '<span class="hd-gloss">Hy Lạp <i>physis</i> — TỰ NHIÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ика</span>'
    '<span class="hd-gloss">đuôi chỉ một NGÀNH học</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp đuôi phải nhớ: <b>-ика</b> là NGÀNH, <b>-ик</b> là NGƯỜI làm '
    'ngành đó — <b>фи́зика</b> vật lý ↔ <b>фи́зик</b> nhà vật lý, và trọng âm đứng yên ở cả '
    'hai. Cùng khuôn: <b>матема́тика</b>, <b>поли́тика</b>.</div>'
    '<div class="hd-warn">Nhưng sang tính từ thì trọng âm MỚI nhảy: '
    '<b>фи́зика</b> → <b>физи́ческий</b> thuộc về vật chất, thể chất.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>фи́зик</b> nhà vật lý · <b>физи́ческий</b> thuộc vật lý · '
    '<b>физкульту́ра</b> môn thể dục</div>'
)

S["вина"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вин-</span>'
    '<span class="hd-gloss">LỖI, TỘI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>вин-</b> nằm sẵn trong câu user nói hằng ngày: '
    '<b>извини́те</b> = из- (bỏ RA) + вин- (lỗi) → "gỡ lỗi cho tôi". Cẩn thận mặt chữ: '
    '<b>вина́</b> còn là cách 2 của <b>вино́</b> rượu vang — phải nhìn câu mới biết.</div>'
    '<div class="hd-warn">Bảng dưới: trọng âm ĐỔI CHỖ giữa hai số. Số ít dồn xuống đuôi '
    '(<b>вины́</b>, <b>вине́</b>), số nhiều kéo ngược lên gốc (<b>ви́ны</b>, <b>вин</b>).</div>'
    '<div class="hd-warn">Cụm phải thuộc: <b>по вине́</b> + cách 2 = "do lỗi của…", '
    '<i>по вине́ води́теля</i> tại lỗi người lái.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>винова́т</b> tôi có lỗi · <b>вино́вный</b> có tội · '
    '<b>извини́ть</b> tha lỗi · <b>обвиня́ть</b> buộc tội</div>'
)
V["вина"] = "lỗi, tội lỗi, sự có lỗi"

S["начало"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">tiền tố, ở đây KHÔNG mang nghĩa riêng tách ra được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-чал-</span>'
    '<span class="hd-gloss">gốc BẮT ĐẦU (chính là <b>нача́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi danh từ giống TRUNG</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ đọc thẳng ra từ động từ <b>нача́ть</b>, trọng âm giữ '
    'nguyên chỗ cũ. Nghĩa trượt từ "việc bắt đầu" sang "phần đầu của một vật": '
    '<i>нача́ло кни́ги</i> phần đầu quyển sách.</div>'
    '<div class="hd-warn">Hai cụm gặp liên tục: <b>в са́мом нача́ле</b> ngay từ đầu · '
    '<b>для нача́ла</b> để bắt đầu đã, trước hết.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нача́ть</b> bắt đầu · <b>начина́ть</b> dạng chưa xong · '
    '<b>снача́ла</b> từ đầu · <b>нача́льник</b> thủ trưởng (người đứng ở đầu)</div>'
)
V["начало"] = "sự bắt đầu, khởi đầu, phần đầu"

S["особенность"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">осо́б-</span>'
    '<span class="hd-gloss">RIÊNG, KHÁC với phần còn lại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-енн-</span>'
    '<span class="hd-gloss">mảnh nối, dựng tính từ <b>осо́бенный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span>'
    '<span class="hd-gloss">tính từ → danh từ TRỪU TƯỢNG giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hậu tố <b>-ость</b> là cỗ máy đổi tính từ thành danh từ trừu tượng '
    'giống cái, đuôi mềm <b>-ь</b> nên biến cách theo lối thứ ba. Đọc ngược lại là ra nghĩa: '
    '"cái làm cho nó khác" = đặc điểm.</div>'
    '<div class="hd-warn">Dạng user gặp nhiều nhất lại là trạng từ <b>осо́бенно</b> '
    '"nhất là, đặc biệt là"; còn cụm <b>в осо́бенности</b> cũng nghĩa đó nhưng trang trọng '
    'hơn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>осо́бый</b> riêng, đặc thù · <b>осо́бенный</b> đặc biệt · '
    '<b>осо́бенно</b> nhất là</div>'
)
V["особенность"] = "đặc điểm, nét đặc trưng, tính chất riêng"

S["привет"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">TỚI, hướng về phía ai</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вет</span>'
    '<span class="hd-gloss">gốc LỜI NÓI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>-вет</b> "lời" đã gặp hai lần: <b>отве́т</b> lời đáp LẠI, '
    '<b>сове́т</b> lời bàn CÙNG nhau. Thêm при- "tới" thì ra lời gửi TỚI người khác — '
    'tức lời chào.</div>'
    '<div class="hd-warn">Chỉ nói với bạn bè, người ngang hàng hoặc nhỏ tuổi hơn. Với người '
    'lạ, người lớn tuổi, cấp trên phải dùng <b>здра́вствуйте</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отве́т</b> câu trả lời · <b>сове́т</b> lời khuyên · '
    '<b>приве́тствовать</b> chào đón</div>'
)
V["привет"] = "chào, lời chào"

S["род"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">род</span>'
    '<span class="hd-gloss">gốc trơn: SINH RA, DÒNG GIỐNG</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một gốc mở khoá cả loạt từ quen: <b>роди́тели</b> bố mẹ, '
    '<b>ро́дина</b> quê hương, <b>приро́да</b> thiên nhiên (cái sinh ra QUANH ta), '
    '<b>наро́д</b> dân tộc. Nghĩa đi từ "những người cùng sinh ra" → dòng họ → giống loài '
    '→ giống ngữ pháp.</div>'
    '<div class="hd-warn">Đây chính là thứ mà badge giống trên mỗi thẻ danh từ đang nói '
    'tới: <b>мужско́й род</b> '
    'giống đực · <b>же́нский род</b> giống cái · <b>сре́дний род</b> giống trung.</div>'
    '<div class="hd-warn">Bảng dưới: số nhiều dồn trọng âm xuống đuôi (<b>родо́в</b>, '
    '<b>рода́ми</b>), và mấy ô in HAI–BA dạng song song — cứ dùng dạng đứng đầu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>роди́тели</b> bố mẹ · <b>ро́дина</b> quê hương · '
    '<b>приро́да</b> thiên nhiên · <b>наро́д</b> dân tộc · <b>родно́й</b> ruột thịt</div>'
)
V["род"] = "dòng họ, dòng dõi, giống loài, giống"

S["сожаление"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-жал-</span>'
    '<span class="hd-gloss">THƯƠNG XÓT, thấy tiếc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen "cùng thấy tiếc với ai" — đúng chữ đồng cảm. Tiền tố '
    '<b>со-</b> "cùng" chính là со- trong <b>совреме́нный</b> (cùng thời) đã học.</div>'
    '<div class="hd-warn">Cùng gốc жал- với từ user nói mỗi ngày: <b>пожа́луйста</b> '
    'làm ơn.</div>'
    '<div class="hd-warn">Cụm phải thuộc: <b>к сожале́нию</b> = tiếc là, đáng tiếc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жаль</b> tiếc · <b>жа́лко</b> đáng tiếc · '
    '<b>жа́ловаться</b> than phiền · <b>жа́лость</b> lòng thương · '
    '<b>пожа́луйста</b> làm ơn</div>'
)
V["сожаление"] = "sự hối tiếc, sự tiếc nuối, lòng thương xót"

S["счастье"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">CÓ, cùng với</span></div>'
    '<div class="hd-row"><span class="hd-piece">-часть-</span>'
    '<span class="hd-gloss">PHẦN (chính là <b>часть</b> đã học)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е</span>'
    '<span class="hd-gloss">đuôi danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cách đọc từ nguyên được chấp nhận rộng rãi: "người CÓ PHẦN của '
    'mình" — được chia phần thì là có phúc. Cụm <b>сч</b> đầu từ đọc gộp làm một âm, '
    'y như <b>счёт</b> cùng lô.</div>'
    '<div class="hd-warn">Bảng dưới vẫn in đủ số nhiều, nhưng ô đáng nhớ là cách 2 số '
    'nhiều <b>сча́стий</b>: <b>ь</b> đổi thành <b>и</b>, không phải «счастьев».</div>'
    '<div class="hd-warn">Cặp song sinh với <b>к сожале́нию</b> cùng lô: '
    '<b>к сча́стью</b> = may thay, may mà.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>счастли́вый</b> hạnh phúc, may mắn · <b>часть</b> phần · '
    '<b>уча́ствовать</b> tham gia (nhận một phần vào việc)</div>'
)
V["счастье"] = "hạnh phúc, sự may mắn, vận may"

S["чудо"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">чуд-</span>'
    '<span class="hd-gloss">LẠ LÙNG, làm người ta sững sờ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о</span>'
    '<span class="hd-gloss">đuôi danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>чуд-</b> xoay quanh cái làm người ta kinh ngạc: '
    'đẹp đến sững sờ thì là <b>чуде́сный</b>, xấu đến sững sờ thì là <b>чудо́вище</b> '
    'quái vật.</div>'
    '<div class="hd-warn">Số nhiều mọc thêm mảnh <b>-ес-</b>: <b>чудеса́</b>, '
    '<b>чуде́с</b>, <b>чудеса́м</b> — cùng nhóm nhỏ với <b>не́бо</b> → <b>небеса́</b>. '
    'Bảng dưới còn in чу́да/чуд song song, đó là dạng hiếm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>чуде́сный</b> kỳ diệu · <b>чу́дный</b> tuyệt vời · '
    '<b>чудо́вище</b> quái vật · <b>чуда́к</b> người lập dị</div>'
)

S["счёт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">GỘP LẠI, cộng vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-чёт</span>'
    '<span class="hd-gloss">gốc ĐẾM (chính là <b>счита́ть</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">"Cái đã đếm gộp lại" — đếm tiền phải trả ra hóa đơn, đếm bàn '
    'thắng ra tỉ số, chỗ tiền nằm chờ được đếm là tài khoản. Một từ, ba nghĩa đều là '
    'kết quả của việc đếm.</div>'
    '<div class="hd-warn">Chữ <b>ё</b> chỉ sống khi mang trọng âm. Trọng âm rời gốc là '
    'phải viết <b>е</b>: <b>счёт</b> nhưng <b>счета́</b>, <b>счето́в</b>, '
    '<b>на счету́</b> — chỉ <b>о счёте</b> giữ lại ё.</div>'
    '<div class="hd-warn">Hai cụm phải thuộc: <b>за счёт</b> + cách 2 = nhờ vào, bằng '
    'tiền của · <b>счёт в ба́нке</b> = tài khoản ngân hàng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>счита́ть</b> đếm, cho rằng · <b>счётчик</b> đồng hồ đo · '
    '<b>расчёт</b> sự tính toán</div>'
)

S["точка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">точ-</span>'
    '<span class="hd-gloss">CHẤM, chỗ bị chọc một cái</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">hậu tố vật nhỏ, kéo theo giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ cái chấm nhỏ nhất mà ra tính từ <b>то́чный</b> "chính xác" — '
    'chính xác nghĩa là trúng đúng một điểm, không lệch.</div>'
    '<div class="hd-warn">Cách 2 số nhiều chèn thêm nguyên âm chạy: <b>то́чка</b> → '
    '<b>то́чек</b>. Chỉ chèn khi hai phụ âm dính nhau trước -ка (như <b>ще́пка</b> cùng '
    'lô); <b>рука́</b> → <b>рук</b> thì không cần.</div>'
    '<div class="hd-warn"><b>то́чка зре́ния</b> = quan điểm, nghĩa đen "điểm nhìn" — '
    'còn <b>то́чка</b> một mình chỉ là dấu chấm hoặc một điểm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>то́чный</b> chính xác · <b>то́чно</b> đúng thế · '
    '<b>уто́чнить</b> làm rõ thêm</div>'
)
V["точка"] = "dấu chấm, điểm"

# ------------------------------------------------------ tính từ, từ mượn quốc tế
S["китайский"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">Кита́й-</span>'
    '<span class="hd-gloss">tên nước Trung Quốc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ск-</span>'
    '<span class="hd-gloss">mảnh dựng tính từ "thuộc về"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span>'
    '<span class="hd-gloss">đuôi tính từ giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ghép thẳng tên nước với <b>-ский</b> là ra tính từ, trọng âm ở '
    'nguyên chỗ cũ của <b>Кита́й</b>. Là tính từ quan hệ nên không có dạng ngắn và không '
    'có so sánh hơn — bảng dưới bỏ trống đúng hai chỗ đó.</div>'
    '<div class="hd-warn">Cặp dễ lẫn: <b>кита́йский язы́к</b> là TÍNH TỪ đứng trước danh '
    'từ, còn <b>говори́ть по-кита́йски</b> là TRẠNG TỪ đứng sau động từ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>Кита́й</b> Trung Quốc · <b>кита́ец</b> người Trung Quốc · '
    '<b>китая́нка</b> phụ nữ Trung Quốc · <b>по-кита́йски</b> bằng tiếng Trung</div>'
)
V["китайский"] = "thuộc về nước Trung Quốc, tiếng Trung"

S["некоторый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не́-</span>'
    '<span class="hd-gloss">KHÔNG RÕ CÁI NÀO (không phải phủ định)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-котор-</span>'
    '<span class="hd-gloss">gốc của <b>кото́рый</b> "cái nào"</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đây là не- "không xác định", khác hẳn не- phủ định, và dấu nhận '
    'ra là TRỌNG ÂM nằm ngay trên nó: <b>не́который</b>, <b>не́сколько</b>, <b>не́кто</b> '
    '— cả nhóm nhấn vào не-, trong khi <b>кото́рый</b> nhấn ở giữa.</div>'
    '<div class="hd-warn">Đứng một mình ở số nhiều thì thành danh từ: '
    '<b>не́которые</b> = "một số người". Cụm hay gặp: <b>не́которое вре́мя</b> = một '
    'thời gian.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кото́рый</b> cái mà, người mà · <b>не́сколько</b> vài · '
    '<b>не́кто</b> một người nào đó</div>'
)
V["некоторый"] = "một vài, một số, nào đó"

S["спорт"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn thẳng tiếng Anh <i>sport</i>, <b>không chẻ được</b> bằng '
    'phụ tố Nga — năm chữ cái là trọn cả từ.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Kết bằng phụ âm TRẦN, không có <b>ь</b> ⇒ giống đực, biến cách '
    'theo lối thường. Cái phải học không phải mặt chữ mà là cách nó đi với động từ.</div>'
    '<div class="hd-warn">Nói "chơi thể thao" thì dùng <b>занима́ться спо́ртом</b> — động '
    'từ này đòi cách 5. Còn "một môn thể thao" là <b>вид спо́рта</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спорти́вный</b> thuộc thể thao · <b>спортсме́н</b> vận động '
    'viên · <b>спортсме́нка</b> nữ vận động viên · <b>спортза́л</b> phòng tập</div>'
)

S["тип"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ quốc tế, gốc Hy Lạp <i>typos</i> "khuôn in" — đúng chữ '
    '<i>type</i> tiếng Anh. <b>Không chẻ được</b> bằng phụ tố Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhận ra ngay qua tiếng Anh, và kéo theo cả <b>типи́чный</b> = '
    '<i>typical</i>. Từ khuôn in mà ra nghĩa "loại, kiểu": những cái đúc từ cùng một '
    'khuôn thì cùng một тип.</div>'
    '<div class="hd-warn">Dùng cho NGƯỜI thì mang sắc thái xấu, kiểu "gã, tay nào đó": '
    '<i>стра́нный тип</i>. Khẩu ngữ còn có <b>ти́па того́</b> = "đại loại thế".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>типи́чный</b> điển hình · <b>типово́й</b> theo mẫu chuẩn</div>'
)

# ------------------------------------------ nguyên âm chạy ở cách 2 số nhiều
S["щепка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">щеп-</span>'
    '<span class="hd-gloss">CHẺ, tách dọc thớ gỗ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">hậu tố vật nhỏ, kéo theo giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng nghĩa đen của gốc: mảnh nhỏ CHẺ ra từ khúc gỗ. Cách 2 số '
    'nhiều chèn nguyên âm chạy giống <b>то́чка</b> cùng lô: <b>ще́пок</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: bảng chia máy dựng cho từ này đang LỖI — mấy ô số '
    'ít bị in nhầm dạng số nhiều. Dạng đúng của số ít: <b>ще́пка</b>, <b>ще́пки</b>, '
    '<b>ще́пке</b>, <b>ще́пку</b>, <b>ще́пкой</b>.</div>'
    '<div class="hd-warn">Chỗ user chắc chắn gặp từ này là câu tục ngữ '
    '<b>лес ру́бят — ще́пки летя́т</b>: chặt rừng thì dăm gỗ phải bay.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>щепа́</b> dăm gỗ (nói gộp) · <b>расщепи́ть</b> chẻ tách ra</div>'
)

S["англичанка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">англи-</span>'
    '<span class="hd-gloss">gốc tên nước <b>А́нглия</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-чан-</span>'
    '<span class="hd-gloss">mảnh dựng tên NGƯỜI theo vùng đất</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không phải nước nào cũng dùng bộ -ец/-ка; nhóm này dùng '
    '-анин/-анка: <b>англича́нин</b> ↔ <b>англича́нка</b>. Trọng âm dịch dần về cuối theo '
    'độ dài từ: <b>А́нглия</b> → <b>англи́йский</b> → <b>англича́нка</b>.</div>'
    '<div class="hd-warn">Cách 2 và cách 4 số nhiều chèn nguyên âm chạy: '
    '<b>англича́нок</b> — thêm <b>о</b> vào giữa н và к cho đỡ dính phụ âm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>А́нглия</b> nước Anh · <b>англича́нин</b> người đàn ông Anh · '
    '<b>англи́йский</b> thuộc về nước Anh · <b>по-англи́йски</b> bằng tiếng Anh</div>'
)

S["немка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">нем-</span>'
    '<span class="hd-gloss">gốc của <b>немо́й</b> — CÂM, không nói được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ điển từ nguyên giải thích: người nước ngoài không nói được '
    'tiếng Slav thì bị gọi là "người câm", từ đó ra <b>не́мец</b> / <b>не́мка</b>. Đây là '
    'từ nguyên, không phải luật suy ra được.</div>'
    '<div class="hd-warn">Trọng âm đứng yên ở не́- trong <b>не́мец</b>, <b>не́мка</b>, '
    'nhưng nhảy xuống giữa ở tính từ <b>неме́цкий</b>. Cách 2 số nhiều chèn nguyên âm '
    'chạy: <b>не́мок</b>.</div>'
    '<div class="hd-warn">Tên NƯỚC lại không dựng từ gốc này: nước Đức là '
    '<b>Герма́ния</b>, chỉ người và tiếng mới đi theo нем-.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>не́мец</b> người đàn ông Đức · <b>неме́цкий</b> thuộc về nước '
    'Đức · <b>по-неме́цки</b> bằng tiếng Đức · <b>немо́й</b> câm</div>'
)
