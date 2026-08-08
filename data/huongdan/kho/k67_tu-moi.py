# -*- coding: utf-8 -*-
"""k67 — tu-moi: 12 từ user vừa thêm, KHÔNG cùng một họ.

Mỗi thẻ đứng độc lập, không có trục chung và không có khối hệ thống dùng chung.
Bốn từ nghề (`-и́ст` · `-а́нт` ×2 · `-е́нт` · đuôi mượn `-альо́н`) đều nói phần
hậu tố của CHÍNH nó ngay trong "Cách nhớ", không đánh số hệ thống.
Ba nhạc cụ (гита́ра · скри́пка · пиани́но) cố ý KHÔNG có bảng nhạc cụ chung.
"""

# 🔴 KHÔNG dựng biến khối dùng chung (HE/LUAT/THE…) rồi cộng vào mọi thẻ.

S = {}
V = {}

# ----------------------------------------------------------------- бе́дный
S["бедный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бед-</span>'
    '<span class="hd-gloss">gốc TAI HOẠ, CẢNH KHỐN (<b>беда́</b> tai hoạ)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi TÍNH TỪ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc của <b>беда́</b> gắn đuôi tính từ ⇒ "đang ở trong cảnh '
    'khốn". Từ đúng một hình ảnh đó ra cả hai nghĩa: thiếu thốn tiền của, và đáng '
    'thương — <b>бе́дный ма́льчик</b> tội nghiệp thằng bé.</div>'
    '<div class="hd-warn">⚠️ Dạng ngắn KHÔNG suy thẳng từ dạng dài: bỏ -ый còn cụm '
    'дн khó đọc nên chèn -е- ⇒ <b>бе́ден</b>; riêng giống cái đẩy trọng âm ra đuôi ⇒ '
    '<b>бедна́</b>. Hai dạng còn lại đứng yên: <b>бе́дно</b>, <b>бе́дны</b> (số nhiều '
    'còn gặp cả <b>бедны́</b>).</div>'
    '<div class="hd-warn">⚠️ Không dính gì tới <b>обе́д</b> bữa trưa / <b>обе́дать</b> '
    'ăn trưa: bên đó là об- + gốc ед- (ăn), chỉ trùng mặt chữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>беда́</b> tai hoạ · <b>бе́дность</b> sự nghèo khó · '
    '<b>бедня́к</b> người nghèo · <b>бе́дствие</b> tai ương</div>'
)

# ------------------------------------------------------------------ геро́й
S["герой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn nguyên khối từ Hy Lạp <i>hērōs</i> '
    '(qua tiếng Pháp <i>héros</i>) — cùng một từ đẻ ra <i>hero</i> tiếng Anh, nên '
    'mặt chữ герой- nhận ra ngay.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi -й ⇒ giống đực, chia đều đặn (<b>геро́я</b>, '
    '<b>геро́ю</b>…). Cụm đáng thuộc: <b>ме́стный геро́й</b> người hùng của vùng.</div>'
    '<div class="hd-warn">⚠️ Hai nghĩa rất xa nhau, ngữ cảnh quyết định: người dũng '
    'cảm (<b>геро́й войны́</b>) và nhân vật trong tác phẩm (<b>геро́й рома́на</b> '
    'nhân vật chính của tiểu thuyết) — nghĩa sau không hàm ý dũng cảm gì cả.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>герои́ня</b> nữ anh hùng, nữ nhân vật chính · '
    '<b>герои́ческий</b> anh hùng (tính từ) · <b>геро́йство</b> hành động anh hùng</div>'
)

# ----------------------------------------------------------------- гита́ра
S["гитара"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гитар-</span>'
    '<span class="hd-gloss">thân từ mượn: Tây Ban Nha <i>guitarra</i>, xa hơn nữa là '
    'Hy Lạp <i>kithara</i> — một loại đàn dây cổ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi ⇒ giống cái, chia đều đặn</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng một dây chuyền mượn với <i>guitar</i> tiếng Anh. Muốn '
    'gọi NGƯỜI chơi thì bỏ -а, thay bằng hậu tố nghề -и́ст: <b>гитари́ст</b>.</div>'
    '<div class="hd-warn">⚠️ Chơi nhạc cụ thì dùng <b>игра́ть на</b> + CÁCH 6: '
    '<b>игра́ть на гита́ре</b>. Không phải cách 4 như "chơi bóng".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гитари́ст</b> người chơi ghi-ta · <b>гита́рный</b> thuộc '
    'đàn ghi-ta</div>'
)

# ------------------------------------------------------------- журнали́ст
S["журналист"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">журнал-</span>'
    '<span class="hd-gloss">gốc TẠP CHÍ, BÁO (<b>журна́л</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ст</span>'
    '<span class="hd-gloss">hậu tố NGƯỜI LÀM NGHỀ ĐÓ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>журна́л</b> mượn từ Pháp <i>journal</i> ← <i>jour</i> '
    '"ngày": thứ ghi theo ngày — báo, tạp chí, và cả sổ điểm ở trường. Thêm -и́ст ⇒ '
    'người làm ra nó. Khuôn này mở khoá cả lớp: <b>тури́ст</b>, <b>арти́ст</b>, '
    '<b>гитари́ст</b>.</div>'
    '<div class="hd-warn">⚠️ Hậu tố -и́ст hầu như luôn KÉO trọng âm về mình, nên trọng âm '
    'dịch chỗ khi ghép: <b>журна́л</b> (âm 2) → <b>журнали́ст</b> (âm 3).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>журна́л</b> tạp chí, sổ ghi · <b>журнали́стка</b> nữ nhà '
    'báo · <b>журнали́стика</b> nghề báo, ngành báo chí</div>'
)

# ---------------------------------------------------------------- исто́рия
S["история"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">истор-</span>'
    '<span class="hd-gloss">gốc Hy Lạp <i>historía</i> — sự tìm hiểu, chuyện kể '
    'lại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ия</span>'
    '<span class="hd-gloss">đuôi danh từ mượn quốc tế ⇒ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một gốc, hai nghĩa Việt phải tách bằng ngữ cảnh: chuỗi việc '
    'đã xảy ra của cả loài người (lịch sử, môn sử) và chuỗi việc của một lần (câu '
    'chuyện, vụ việc). Tiếng Anh cũng chia đôi đúng chỗ này: <i>history</i> và '
    '<i>story</i> vốn là một từ.</div>'
    '<div class="hd-warn">⚠️ Danh từ đuôi -ия có cách 3 và cách 6 số ít đều là -ии, '
    'không phải -е như đa số từ đuôi -а/-я: <b>в исто́рии</b> trong lịch sử.</div>'
    '<div class="hd-warn">⚠️ Đừng lẫn với <b>расска́з</b>: <b>исто́рия</b> là bản '
    'thân sự việc đã xảy ra (và là dòng lịch sử), còn <b>расска́з</b> là LỜI KỂ về '
    'nó hoặc một truyện ngắn — nó sinh ra từ <b>рассказа́ть</b> kể.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>исто́рик</b> nhà sử học · <b>истори́ческий</b> thuộc lịch '
    'sử · <b>предысто́рия</b> tiền sử, chuyện xảy ra trước đó</div>'
)

# --------------------------------------------------------------- мужчи́на
S["мужчина"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">муж-</span>'
    '<span class="hd-gloss">gốc ĐÀN ÔNG (<b>муж</b> chồng)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-чина</span>'
    '<span class="hd-gloss">đuôi tạo danh từ chỉ người, rút gọn từ мужьск- '
    '(<b>мужско́й</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>муж</b> vốn nghĩa rộng "người đàn ông", về sau hẹp '
    'lại chỉ còn "chồng"; <b>мужчи́на</b> chính là chỗ giữ lại nghĩa rộng cũ. Nên khi '
    'muốn nói "một người đàn ông" thì dùng từ này, <b>муж</b> chỉ là chồng.</div>'
    '<div class="hd-warn">⚠️ Đuôi -а nhưng GIỐNG ĐỰC. Nó chia y hệt <b>ма́ма</b> '
    '(<b>мужчи́ны</b>, <b>мужчи́не</b>…), song mọi thứ đi kèm phải ở giống đực: '
    '<b>ста́рый мужчи́на</b>, <b>мужчи́на пришёл</b>. Cùng loại: <b>па́па</b>, '
    '<b>де́душка</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>муж</b> chồng · <b>мужско́й</b> thuộc nam giới · '
    '<b>за́мужем</b> (nữ) đã có chồng · <b>му́жество</b> lòng dũng cảm</div>'
)

# --------------------------------------------------------------- музыка́нт
S["музыкант"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">музык-</span>'
    '<span class="hd-gloss">gốc ÂM NHẠC (<b>му́зыка</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́нт</span>'
    '<span class="hd-gloss">hậu tố NGƯỜI LÀM VIỆC ĐÓ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>му́зыка</b> ← Hy Lạp <i>mousikē</i> "nghệ thuật của các '
    'Nàng Thơ", cùng gốc <i>music</i> tiếng Anh. Gắn -а́нт ⇒ người CHƠI nhạc, không '
    'phải người sáng tác. Cùng khuôn -а́нт: <b>официа́нт</b>, <b>консульта́нт</b>, '
    '<b>практика́нт</b>.</div>'
    '<div class="hd-warn">⚠️ Trọng âm nhảy hẳn hai âm tiết khi ghép: <b>му́зыка</b> '
    '(âm 1) → <b>музыка́нт</b> (âm 3). Đọc sai chỗ này là người nghe không nhận '
    'ra từ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>му́зыка</b> âm nhạc · <b>музыка́льный</b> thuộc âm nhạc, '
    'có khiếu nhạc</div>'
)

# --------------------------------------------------------------- официа́нт
S["официант"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">офици-</span>'
    '<span class="hd-gloss">gốc Latin <i>officium</i> — phận sự, việc phục vụ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́нт</span>'
    '<span class="hd-gloss">hậu tố NGƯỜI LÀM VIỆC ĐÓ, y như ở <b>музыка́нт</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: "người đang làm phận sự" ⇒ người phục vụ bàn. '
    'Cùng cái gốc Latin ấy còn cho <b>официа́льный</b> chính thức (việc thuộc phận '
    'sự công) và <b>офице́р</b> sĩ quan.</div>'
    '<div class="hd-warn">⚠️ Mức tin: chỗ nối <b>официа́нт</b> — <b>официа́льный</b> — '
    '<b>офице́р</b> — <b>о́фис</b> là TỪ NGUYÊN, đường vòng qua Latin, KHÔNG phải luật '
    'suy ra được. Buộc mấy từ này lại cho dễ nhớ thì tốt, nhưng đừng lấy nó đoán nghĩa '
    'từ mới.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>официа́нтка</b> nữ phục vụ bàn · <b>официа́льный</b> chính '
    'thức · <b>офице́р</b> sĩ quan · <b>о́фис</b> văn phòng</div>'
)

# --------------------------------------------------------------- пиани́но
S["пианино"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn nguyên khối từ Ý <i>pianino</i>, dạng '
    'nhỏ của <i>piano</i> ← <i>pianoforte</i> "nhẹ–mạnh" — cây đàn đánh được cả nhẹ '
    'lẫn mạnh, thứ mà đàn phím trước nó không làm được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi -о của từ mượn ⇒ giống trung. <b>пиани́но</b> là cây đàn '
    'ĐỨNG kê sát tường; đàn cánh nằm ngang là <b>роя́ль</b> (giống đực). Người chơi: '
    '<b>пиани́ст</b>.</div>'
    '<div class="hd-warn">⚠️ KHÔNG biến cách — mọi cách đều viết y hệt nhau: '
    '<b>игра́ть на пиани́но</b>, <b>купи́ть пиани́но</b>, <b>два пиани́но</b>. Muốn '
    'biết đang ở cách nào thì nhìn tính từ đi kèm: <b>ста́рое пиани́но</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пиани́ст</b> nghệ sĩ dương cầm · <b>пиани́стка</b> nữ nghệ '
    'sĩ dương cầm</div>'
)

# ------------------------------------------------------------- почтальо́н
S["почтальон"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">почт-</span>'
    '<span class="hd-gloss">gốc BƯU ĐIỆN, THƯ TỪ (<b>по́чта</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-альо́н</span>'
    '<span class="hd-gloss">đuôi chỉ người, mượn nguyên từ Pháp–Đức <i>postillon</i> '
    '— không phải hậu tố Nga tự ghép được</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>по́чта</b> + đuôi người ⇒ người mang thư. Chữ ь ở đây '
    'là dấu TÁCH: nó chen vào giữa л và о nên hai chữ không dính thành một âm. Tổ hợp '
    'ь + о chỉ gặp trong từ mượn, nhớ một lượt cả bộ: <b>батальо́н</b>, '
    '<b>медальо́н</b>, <b>бульо́н</b>.</div>'
    '<div class="hd-warn">⚠️ Trọng âm nằm ở âm cuối -о́н và ĐỨNG YÊN suốt bảng chia '
    '(<b>почтальо́на</b>, <b>почтальо́ны</b>) — đừng kéo nó về đầu theo '
    '<b>по́чта</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́чта</b> bưu điện, thư từ · <b>почто́вый</b> thuộc bưu '
    'điện</div>'
)

# -------------------------------------------------------------- президе́нт
S["президент"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пре-</span>'
    '<span class="hd-gloss">Latin <i>prae-</i> TRƯỚC, PHÍA ĐẦU</span></div>'
    '<div class="hd-row"><span class="hd-piece">-зид-</span>'
    '<span class="hd-gloss">Latin <i>sed-</i> NGỒI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́нт</span>'
    '<span class="hd-gloss">đuôi NGƯỜI ĐANG LÀM (họ gần của -а́нт)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: "người ngồi ở phía trước" = người chủ toạ — đúng '
    'như <i>preside</i>/<i>president</i> tiếng Anh. Đuôi -е́нт chỉ người, cùng khuôn '
    '<b>студе́нт</b>, <b>клие́нт</b>.</div>'
    '<div class="hd-warn">⚠️ Bảng chia in HAI dạng ở cách 4 (<b>президе́нта</b> và '
    '<b>президе́нт</b>): chỉ dạng đầu dùng cho từ này. Từ chỉ người ⇒ danh từ động '
    'vật ⇒ cách 4 mượn nguyên cách 2 — <b>ви́жу президе́нта</b>, số nhiều '
    '<b>президе́нтов</b>. Dạng thứ hai là ô của danh từ bất động vật.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>президе́нтский</b> thuộc tổng thống · '
    '<b>президе́нтство</b> nhiệm kỳ tổng thống · <b>прези́диум</b> đoàn chủ tịch</div>'
)

# ---------------------------------------------------------------- скри́пка
S["скрипка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">скрип-</span>'
    '<span class="hd-gloss">gốc TIẾNG RÍT, TIẾNG CÓT KÉT (<b>скрип</b>, '
    '<b>скрипе́ть</b> kêu cót két)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">hậu tố ⇒ danh từ giống cái, ở đây chỉ ĐỒ VẬT</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người Nga gọi cây vĩ cầm theo ÂM THANH nó phát ra: vĩ cọ vào '
    'dây thì rít lên ⇒ "cái đồ kêu rít". Người chơi là <b>скрипа́ч</b>, chơi thì '
    '<b>игра́ть на скри́пке</b>.</div>'
    '<div class="hd-warn">⚠️ Cách 2 số nhiều cắt sạch đuôi, để lại cụm пк không đọc '
    'nổi nên chèn -о- vào giữa ⇒ <b>скри́пок</b>. Chỉ chèn khi CÓ cụm phụ âm: '
    '<b>рука́</b> cắt ra còn <b>рук</b>, chẳng chèn gì cả.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>скрип</b> tiếng cót két · <b>скрипе́ть</b> kêu cót két · '
    '<b>скрипа́ч</b> nghệ sĩ vĩ cầm · <b>скрипи́чный</b> thuộc vĩ cầm</div>'
)

# ================================================== field Vietnamese (đề bài)
# Chỉ sửa hai từ. Mười từ còn lại đã là danh sách nghĩa thuần, không có nhãn từ
# loại / cách chi phối / ghi chú trong ngoặc — đúng §2c, nên để nguyên.
#
# музыкант: dòng cũ chỉ có "nhạc sĩ", mà trong tiếng Việt "nhạc sĩ" hiểu mặc định
#   là NGƯỜI SÁNG TÁC (композитор). музыкант là người CHƠI nhạc ⇒ đặt "nhạc công"
#   lên đầu, vẫn giữ "nhạc sĩ" ở cuối cho khớp thói quen cũ của user.
# история: dòng cũ thiếu hẳn nhánh event / affair / thing của gloss tiếng Anh,
#   và thiếu nghĩa "môn sử". Liệt kê đủ thì tự tách khỏi расска́з.
V["музыкант"] = "nhạc công, người chơi nhạc, nhạc sĩ"
V["история"] = "lịch sử, môn sử, câu chuyện, sự việc, vụ việc"
