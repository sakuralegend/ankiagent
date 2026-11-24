# -*- coding: utf-8 -*-
"""k224 — places::city: thời tiết, phố xá, chở đi, giấy tờ; trục là GỐC + TIỀN TỐ.

Chỗ cần nhất quán trong lô:
(1) восход: вос- (воз-) LÊN + ход ĐI — khớp закат k186, восток k84, вход k37.
(2) прохожий: хож- = ход- với д → ж — khớp проходить k113.
(3) перевезти / вывезти / вывозить: вез-/воз- CHỞ — khớp везти k94, перевозить k143, увезти k143.
(4) кое-куда: кое- = người nói BIẾT chỗ nào, chỉ chưa nói ra — khớp кое-что k154, кое-кто k173.
(5) вследствие: след- — khớp следить k171, впоследствии k200.
(6) оформление: о- LÀM CHO CÓ + форм- KHUÔN — khớp оформить k146; -л- là âm chèn.
(7) вступление: в- VÀO + ступ- BƯỚC — khớp вступить k185.
(8) каталог: -ло́г — khớp диалог k04. водопад: пад- RƠI — khớp падение k176.
Họ hàng cố ý vắng: филиал, тротуар (từ mượn đứng một mình).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "всемирный": "toàn thế giới, toàn cầu",                  # bỏ «thế giới» trơn — nuốt trọn đề мировой
    "филиал": "chi nhánh, phân hiệu",                        # «công ty con» = дочерняя компания
    "каталог": "danh mục, catalô",                           # «mục lục» sách = оглавление; gloss chỉ catalogue
    "перевезти": "chở sang, chở qua",                        # khớp перевозить k143 (hai thể cùng gloss)
    "вывозить": "chở ra, chở đi, đưa ra khỏi",               # khớp вывезти (hai thể cùng gloss)
    "кое-куда": "đến một chỗ nào đó, tới vài chỗ",           # «đâu đó» trơn không nói HƯỚNG — nhoè sang где-то
    "вследствие": "do, do hậu quả của",                 # giữ «do» (nghĩa chính); из-за nới «vì, tại…» để hết lọt
    "оформление": "cách trang trí, cách trình bày, thiết kế, việc làm thủ tục giấy tờ",  # «trình bày» trơn là động từ
    "вступление": "sự gia nhập, phần mở đầu, đoạn dạo đầu",  # «sự tham gia» = участие, gloss không có
}

# --------------------------------------------------------------------- лужа
S["лужа"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn <i>луж-</i>, không chẻ được; <i>-а</i> là đuôi giống cái.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vũng nước mưa trên đường, hay vũng bất kỳ chất lỏng nào đổ ra: '
    '<b>лу́жа кро́ви</b> vũng máu. Giẫm vào: <b>наступи́ть в лу́жу</b>.</div>'
    '<div class="hd-warn"><b>сесть в лу́жу</b> «ngồi vào vũng nước» = bẽ mặt, hớ to.</div>'
    '<div class="hd-warn">Nhìn giống mà KHÔNG cùng gốc: <b>лужа́йка</b> bãi cỏ là từ <b>луг</b> '
    'đồng cỏ (<i>г → ж</i>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лу́жица</b> vũng nước nhỏ</div>'
)

# --------------------------------------------------------------------- восход
S["восход"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вос-</span>'
    '<span class="hd-gloss">LÊN — <i>воз-</i>, viết <i>с</i> trước <i>х</i>; như <b>восто́к</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ход</span>'
    '<span class="hd-gloss">SỰ ĐI — từ <b>ходи́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mặt trời «đi lên» ⇒ lúc mặt trời mọc. Nói đủ là <b>восхо́д со́лнца</b>; '
    'mặt trăng cũng được: <b>восхо́д луны́</b>. Cặp đối: <b>зака́т</b> mặt trời lặn.</div>'
    '<div class="hd-warn"><b>восхо́д</b> là lúc mặt trời NHÔ LÊN; <b>рассве́т</b> là lúc trời '
    'SÁNG DẦN, đến trước, và thường ngày hay nói hơn. Cả hai đi với <b>на</b>: '
    '<b>на восхо́де</b>, <b>на рассве́те</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>восходи́ть</b> mọc lên · <b>вход</b> lối vào · <b>вы́ход</b> lối ra · '
    '<b>ходи́ть</b> đi</div>'
)

# --------------------------------------------------------------------- прохладный
S["прохладный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-хлад-</span>'
    '<span class="hd-gloss">LẠNH — dạng Slav cổ của <b>хо́лод</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><i>хлад- ↔ холод-</i> y như <i>глав- ↔ голов-</i> (cái đầu): một gốc, hai '
    'dạng. Lạnh vừa phải = mát. Dạng ngắn giống đực chèn <i>е</i>: <b>прохла́ден</b>, rồi '
    '<b>прохла́дна, прохла́дно</b> — trọng âm không nhúc nhích.</div>'
    '<div class="hd-warn">Nghĩa bóng «lạnh nhạt»: <b>прохла́дный приём</b> sự đón tiếp lạnh nhạt.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прохла́да</b> cái mát · <b>прохла́дно</b> (trời) mát · '
    '<b>охлади́ть</b> làm lạnh · <b>холо́дный</b> lạnh</div>'
)

# --------------------------------------------------------------------- водопад
S["водопад"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вод-</span>'
    '<span class="hd-gloss">NƯỚC — <b>вода́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-о-</span>'
    '<span class="hd-gloss">nguyên âm nối hai gốc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пад</span>'
    '<span class="hd-gloss">RƠI — <b>па́дать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Nước rơi» ⇒ thác, ghép y như Anh <i>water-fall</i>. Cùng khuôn ghép: '
    '<b>снегопа́д</b> tuyết rơi, <b>листопа́д</b> lá rụng — trọng âm đều ở mảnh cuối.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вода́</b> nước · <b>па́дать</b> rơi, ngã · <b>паде́ние</b> sự rơi · '
    '<b>за́пад</b> phía tây (nơi mặt trời rơi xuống)</div>'
)

# --------------------------------------------------------------------- всемирный
S["всемирный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">все-</span>'
    '<span class="hd-gloss">TOÀN, cả — <b>весь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-мир-</span>'
    '<span class="hd-gloss">THẾ GIỚI — <b>мир</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Toàn-thế-giới», nhấn vào chữ TOÀN. Hay gặp trong tên gọi chính thức: '
    '<b>Всеми́рный банк</b> Ngân hàng Thế giới. Từ điển có ghi dạng ngắn (giống đực chèn <i>е</i>: '
    '<b>всеми́рен</b>) nhưng thực tế hầu như không gặp.</div>'
    '<div class="hd-warn">Hai tính từ chia nhau cụm cố định: <b>мирова́я война́</b> chiến tranh thế '
    'giới, nhưng <b>Всеми́рная паути́на</b> mạng toàn cầu (World Wide Web).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мир</b> thế giới, hòa bình · <b>мирово́й</b> thuộc thế giới · '
    '<b>весь</b> toàn bộ</div>'
)

# --------------------------------------------------------------------- полюс
S["полюс"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn (Latin <i>polus</i>, gốc Hy Lạp «trục»), không chẻ được — cùng nguồn '
    'với Anh <i>pole</i> (cực).</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai đầu trục Trái Đất: <b>Се́верный по́люс</b> cực Bắc, <b>Ю́жный по́люс</b> '
    'cực Nam; cũng là cực của nam châm, của pin. Ở cực thì dùng <b>на</b>: <b>на по́люсе</b>.</div>'
    '<div class="hd-warn">Số nhiều có hai bộ song song: <b>по́люсы, по́люсов</b> (nhấn gốc) và '
    '<b>полюса́, полюсо́в</b> (nhấn đuôi). Số ít luôn nhấn gốc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поля́рный</b> thuộc vùng cực (<b>поля́рная ночь</b> đêm vùng cực) · '
    '<b>поля́рник</b> người làm việc ở vùng cực</div>'
)

# --------------------------------------------------------------------- витрина
S["витрина"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn tiếng Pháp <i>vitrine</i> (từ <i>vitre</i> ô kính), không chẻ theo lối '
    'Nga được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chốt ở chữ KÍNH: hàng bày sau lớp kính, dù là mặt kính ngoài phố của cửa hàng '
    'hay tủ kính bên trong.</div>'
    '<div class="hd-warn">Đồ đang bày: <b>в витри́не</b> hay <b>на витри́не</b> đều gặp. '
    '<b>рассма́тривать витри́ны</b> ngắm tủ kính các cửa hàng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>витра́ж</b> tranh kính màu (cũng từ <i>vitre</i> của Pháp)</div>'
)

# --------------------------------------------------------------------- прохожий
S["прохожий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">NGANG QUA — như <b>проходи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-хож-</span>'
    '<span class="hd-gloss">ĐI — <i>ход-</i> với д → ж, như <b>хожу́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ий</span>'
    '<span class="hd-gloss">đuôi TÍNH TỪ, dù đây là danh từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Kẻ đang đi ngang qua» ⇒ người qua đường. Chia hệt tính từ, sau <i>ж</i> là '
    '<i>-его</i> chứ không <i>-ого</i>: <b>прохо́жего, прохо́жему, прохо́жие</b>. Phụ nữ là '
    '<b>прохо́жая</b>.</div>'
    '<div class="hd-warn"><b>прохо́жий</b> là người lạ tình cờ đi qua; <b>пешехо́д</b> là người đi BỘ, '
    'phân biệt với người đi xe (từ của luật giao thông).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>проходи́ть</b> đi qua · <b>прохо́д</b> lối đi · <b>пешехо́д</b> người đi bộ · '
    '<b>ходи́ть</b> đi</div>'
)

# --------------------------------------------------------------------- перекрёсток
S["перекрёсток"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span>'
    '<span class="hd-gloss">CẮT NGANG, từ bên này sang bên kia</span></div>'
    '<div class="hd-row"><span class="hd-piece">-крёст-</span>'
    '<span class="hd-gloss">CHỮ THẬP — <b>крест</b>, ở đây <i>е → ё</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ок</span>'
    '<span class="hd-gloss">đuôi danh từ giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai con đường cắt nhau thành chữ thập ⇒ ngã tư. Chữ <i>о</i> của <i>-ок</i> '
    'chạy mất khi thêm đuôi: <b>перекрёстка, перекрёстки</b>; <i>ё</i> thì giữ nguyên.</div>'
    '<div class="hd-warn">Ở ngã tư dùng <b>на</b>: <b>на перекрёстке</b>. Chỗ sang đường cho người đi '
    'bộ là <b>перехо́д</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>крест</b> chữ thập · <b>кре́стик</b> dấu × · '
    '<b>перекрёстный</b> đan chéo nhau</div>'
)

# --------------------------------------------------------------------- филиал
S["филиал"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Từ mượn gốc Latin <i>filius</i> «con trai», không chẻ được; Anh cùng nguồn '
    'có <i>affiliate</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đứa con» của một cơ quan mẹ, đặt ở nơi khác: <b>филиа́л ба́нка</b> chi nhánh '
    'ngân hàng, <b>филиа́л университе́та</b> phân hiệu đại học. Trọng âm ở cuối, như <b>материа́л</b>.</div>'
    '<div class="hd-warn"><b>филиа́л</b> vẫn là một phần của cơ quan mẹ. Công ty con, đứng riêng về '
    'pháp lý, là <b>доче́рняя компа́ния</b> («công ty con gái»).</div>'
)

# --------------------------------------------------------------------- тротуар
S["тротуар"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn tiếng Pháp <i>trottoir</i> (từ <i>trotter</i> đi lon ton, cùng nguồn Anh '
    '<i>trot</i>), không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỗ dành cho đôi chân ⇒ vỉa hè. Đuôi <i>-уар</i> là <i>-oir</i> của Pháp, '
    'mang trọng âm — gặp lại ở <b>резервуа́р</b> bể chứa.</div>'
    '<div class="hd-warn">Đi DỌC trên vỉa hè: <b>идти́ по тротуа́ру</b> (cách 3). Đứng yên ở đó: '
    '<b>на тротуа́ре</b>.</div>'
)

# --------------------------------------------------------------------- перевезти
S["перевезти"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span>'
    '<span class="hd-gloss">SANG, từ chỗ này qua chỗ kia</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вез-ти́</span>'
    '<span class="hd-gloss">CHỞ bằng xe — chính là <b>везти́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chở xong sang chỗ khác: <b>перевезти́ ве́щи на но́вую кварти́ру</b>. Quá khứ '
    'như <b>везти́</b>: <b>перевёз</b> (không có -л), rồi trọng âm dồn về cuối: <b>перевезла́</b>, '
    '<b>перевезли́</b>. Cặp CHT: <b>перевози́ть</b>.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>перевести́</b> (с) dẫn sang; dịch; chuyển tiền — nguyên thể '
    'nghe y hệt. Chia ra mới tách: <b>перевезу́, перевёз</b> ↔ <b>переведу́, перевёл</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>перевози́ть</b> (CHT) · <b>перево́зка</b> sự vận chuyển · '
    '<b>везти́</b> chở · <b>увезти́</b> chở đi mất</div>'
)

# --------------------------------------------------------------------- вывезти
S["вывезти"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span>'
    '<span class="hd-gloss">RA NGOÀI — ở thể HT luôn giữ trọng âm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вез-ти</span>'
    '<span class="hd-gloss">CHỞ bằng xe — <b>везти́</b>, mất trọng âm</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chở RA khỏi một nơi: <b>вы́везти му́сор</b> chở rác đi, <b>вы́везти дете́й на '
    'мо́ре</b> đưa bọn trẻ ra biển. Trọng âm đóng đinh ở <i>вы</i> nên không còn <i>ё</i>: '
    '<b>вы́везу, вы́вез, вы́везла</b>. Cặp CHT: <b>вывози́ть</b>.</div>'
    '<div class="hd-warn">Lệch một chữ với <b>вы́вести</b> dẫn ra, rút ra: <b>вы́везу, вы́вез</b> ↔ '
    '<b>вы́веду, вы́вел</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вывози́ть</b> (CHT) · <b>вы́воз</b> sự chở đi; xuất khẩu · '
    '<b>увезти́</b> chở đi mất · <b>привезти́</b> chở đến</div>'
)

# --------------------------------------------------------------------- вывозить
S["вывозить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">RA NGOÀI — ở thể CHT mất trọng âm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-воз-и́ть</span>'
    '<span class="hd-gloss">CHỞ — chính là <b>вози́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>вы́везти</b>: chở ra nhiều lần, hay đang chở — '
    '<b>му́сор выво́зят по вто́рникам</b> rác được chở đi vào các thứ Ba. Chia như <b>вози́ть</b>: '
    '«tôi» <i>з → ж</i>, rồi trọng âm lùi — <b>вывожу́</b>, <b>выво́зишь</b>.</div>'
    '<div class="hd-warn"><b>вывожу́</b> là ngôi «tôi» của CẢ <b>вывози́ть</b> chở ra lẫn '
    '<b>выводи́ть</b> dẫn ra; từ ngôi «bạn» mới tách: <b>выво́зишь</b> ↔ <b>выво́дишь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́везти</b> (HT) · <b>вы́воз</b> sự chở đi; xuất khẩu · '
    '<b>вози́ть</b> chở qua lại · <b>увози́ть</b> chở đi mất</div>'
)

# --------------------------------------------------------------------- кое-куда
S["кое-куда"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">кое-</span>'
    '<span class="hd-gloss">người nói BIẾT là chỗ nào, chỉ chưa nói ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">куда́</span>'
    '<span class="hd-gloss">ĐI ĐÂU (hướng tới)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>Мне на́до кое-куда́ зайти́</b> = Tôi phải ghé một chỗ (biết rõ chỗ nào, '
    'không nói ra). Còn <b>куда́-то</b> là chính người nói cũng không biết: <b>Он куда́-то ушёл</b>. '
    'Cũng dùng cho «tới vài chỗ».</div>'
    '<div class="hd-warn">Hướng đi mới là <b>кое-куда́</b>; đứng yên thì <b>кое-где́</b> — đúng cặp '
    '<b>куда́ / где</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>куда́</b> đi đâu · <b>куда́-то</b> đi đâu đó · <b>кое-что́</b> một thứ · '
    '<b>кое-кто́</b> có người · <b>кое-где́</b> đây đó</div>'
)

# --------------------------------------------------------------------- вследствие
S["вследствие"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">giới từ <b>в</b> dính liền</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сле́дствие</span>'
    '<span class="hd-gloss">HỆ QUẢ, «cái đi theo sau» — gốc <b>след</b> dấu vết</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Như hệ quả của» ⇒ do, vì. Kéo cách 2: <b>всле́дствие ава́рии</b> do sự cố. Từ '
    'của văn viết, thông báo; nói thường ngày dùng <b>из-за</b> (cũng cách 2).</div>'
    '<div class="hd-warn">Cuối từ: <b>всле́дствие</b> (do) là <i>-е</i>, <b>впосле́дствии</b> (về sau) '
    'là <i>-и</i>.</div>'
    '<div class="hd-warn">Viết RỜI là chuyện khác: <b>сле́дствие</b> còn là cuộc điều tra — '
    '<b>вмеша́ться в сле́дствие</b> can thiệp vào cuộc điều tra.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сле́дствие</b> hệ quả; cuộc điều tra · <b>след</b> dấu vết · '
    '<b>после́дствие</b> hậu quả · <b>сле́дующий</b> tiếp theo</div>'
)

# --------------------------------------------------------------------- строчка
S["строчка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">строч-</span>'
    '<span class="hd-gloss">DÒNG — <b>строка́</b> với к → ч</span></div>'
    '<div class="hd-row"><span class="hd-piece">-к-а</span>'
    '<span class="hd-gloss">hậu tố nhỏ, thân mật</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một hàng chạy thẳng: hàng chữ ⇒ dòng, hàng mũi khâu ⇒ đường chỉ may. Cách 2 số '
    'nhiều chèn <i>е</i>: <b>стро́чек</b>. Không dính gì tới <b>стро́ить</b> xây: gốc ở đây là '
    '<i>строк-</i>.</div>'
    '<div class="hd-warn"><b>чита́ть ме́жду строк</b> «đọc giữa các dòng» = hiểu ra ý ẩn — cụm này '
    'dùng <b>строка́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>строка́</b> dòng · <b>строчи́ть</b> khâu máy; viết lia lịa · '
    '<b>строчна́я бу́ква</b> chữ thường (không viết hoa)</div>'
)

# --------------------------------------------------------------------- каталог
S["каталог"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ката-</span>'
    '<span class="hd-gloss">XUỐNG, lần lượt cho hết (Hy Lạp <i>kata-</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ло́г</span>'
    '<span class="hd-gloss">LỜI, kể ra (Hy Lạp <i>logos</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Kể ra lần lượt cho hết» ⇒ danh mục. Mảnh <i>-лог</i> mang trọng âm ở cuối như '
    '<b>диало́г</b>: <b>катало́г</b>, đừng nhấn đầu theo Anh <i>CATalogue</i>.</div>'
    '<div class="hd-warn"><b>катало́г</b> liệt kê hàng, sách, tranh, thường kèm mô tả; danh sách trơn là '
    '<b>спи́сок</b>, mục lục của một cuốn sách là <b>оглавле́ние</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>диало́г</b> cuộc đối thoại · <b>моноло́г</b> lời độc thoại · '
    '<b>ло́гика</b> logic</div>'
)

# --------------------------------------------------------------------- оформление
S["оформление"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-форм-</span>'
    '<span class="hd-gloss">đưa vào KHUÔN, BIỂU MẪU — như <b>офо́рмить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-л-</span>'
    '<span class="hd-gloss">âm chèn sau <i>м</i>, không mang nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ние</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đi theo hai nghĩa của <b>офо́рмить</b>: làm giấy tờ cho đúng mẫu — '
    '<b>оформле́ние ви́зы</b> việc làm visa; và tạo hình cho đẹp — <b>оформле́ние кни́ги</b> cách '
    'trình bày cuốn sách. Trọng âm dời sang đuôi: <b>офо́рмить → оформле́ние</b>.</div>'
    '<div class="hd-warn">Thứ được làm đứng cách 2, không giới từ: <b>оформле́ние докуме́нтов</b> thủ '
    'tục giấy tờ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>офо́рмить</b> (HT), <b>оформля́ть</b> (CHT) làm thủ tục; trang trí · '
    '<b>фо́рма</b> khuôn, biểu mẫu · <b>форма́льный</b> hình thức</div>'
)

# --------------------------------------------------------------------- вступление
S["вступление"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO TRONG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ступ-л-</span>'
    '<span class="hd-gloss">BƯỚC (<i>л</i> là âm chèn, như <b>вступлю́</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ние</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Sự «bước vào»: vào một tổ chức ⇒ sự gia nhập; vào cuốn sách, bản nhạc ⇒ '
    'phần mở đầu, đoạn dạo đầu.</div>'
    '<div class="hd-warn">Giới từ tách hai nghĩa: <b>вступле́ние в клуб</b> (в + cách 4) gia nhập câu '
    'lạc bộ · <b>вступле́ние к рома́ну</b> (к + cách 3) lời mở đầu tiểu thuyết.</div>'
    '<div class="hd-warn">Đổi tiền tố là đổi từ: <b>выступле́ние</b> (bước RA) buổi biểu diễn, bài phát '
    'biểu · <b>преступле́ние</b> (bước QUA luật) tội ác.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вступи́ть</b> (HT), <b>вступа́ть</b> (CHT) gia nhập · '
    '<b>вступи́тельный экза́мен</b> kỳ thi đầu vào · <b>ступе́нь</b> bậc</div>'
)

B = {
    "docbangmat": 106,
    "loitubat": 3,
    "nguonsai": 4,
    "baolen": [
        "V cần duyệt (9): всемирный (bỏ «thế giới» trơn ⇒ hết nuốt мировой) · вступление (bỏ «sự tham gia» ⇒ hết nuốt участие; gloss không có participation) · вследствие (bỏ «do» trơn ⇒ hết nuốt из-за; còn «vì, bởi, do hậu quả của») · филиал (bỏ «công ty con») · каталог (bỏ «mục lục») · перевезти (khớp перевозить) · вывозить (khớp вывезти) · кое-куда (bỏ «đâu đó» trơn, không nói hướng) · оформление («trình bày» trơn là động từ ⇒ «cách trình bày»).",
        "вследствие — luồng chính cân: «do» với «vì/bởi» đồng nghĩa nên bỏ một từ không mất nghĩa, nhưng 2/3 câu ví dụ (_opus_k224.json) dịch từ này là «do». Đề из-за chỉ có một chữ «do» nên mỏng sẵn (mồ côi, không được đụng).",
        "Nguồn đã bác (4): vi + gloss «subsidiary» của филиал (công ty con = доче́рняя компа́ния, филиал không có tư cách pháp nhân riêng); vi «mục lục» của каталог (= оглавле́ние); vi «sự tham gia» của вступление; dạng ngắn всеми́рен (thẻ ghi hầu như không gặp).",
        "Lỗi tự bắt (3): филиал «mọi danh từ mượn đuôi -а́л nhấn cuối» nói quá ⇒ chỉ so với материа́л; водопад «-па́д luôn mang trọng âm» sai với за́пад ⇒ giới hạn từ ghép снегопа́д, листопа́д; тротуар/каталог «luôn giữ trọng âm» ⇒ bỏ chữ luôn.",
        "вывозить: theo id 8882 đã chọn (CHT); không nhắc вы́возить HT «làm lấm bẩn» trên thẻ vì hiếm. «sơ tán» / «xuất khẩu» (gloss evacuate, export) không thêm vào V của cặp вывезти/вывозить, chưa thấy cần.",
        "Không chắc: тротуар «lề đường» — nơi hiểu là vỉa hè, nơi hiểu là mép đường (обо́чина); giữ nguyên đề cũ.",
        "Họ hàng cố ý vắng: филиал, тротуар. Va chạm sau khi áp V chưa chạy lại trên Anki (agent không chạm Anki).",
    ],
}
