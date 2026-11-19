# -*- coding: utf-8 -*-
"""k122 — actions: 9 cặp thể + существова́ть; trục là TIỀN TỐ ghép vào gốc đã học.

Chỗ cần nhất quán trong lô:
(1) Lõi -ня-/-ним- «nắm, lấy» (như взять k03, поня́ть/приня́ть): подня́ть = под- (từ dưới lên)
    + nắm; снять = с- (khỏi bề mặt) + nắm. Tương lai lộ -ним-: подниму́, сниму́.
(2) Tiền tố ghép vào động từ đã có thẻ: от-+дать (k01), вы-+звать (k01), вы-+игра́ть (k54),
    у-+брать (k01), о-+-станов- (như остано́вка k49, оста́вить k113). вы- HT luôn giữ trọng âm.
(3) Ngoại động vs -ся (k123 soạn song song): подня́ть/останови́ть = làm CÁI GÌ (cách 4);
    tự đi lên / tự dừng là подня́ться / останови́ться.
(4) про́бовать: про- KHÔNG phải tiền tố; проб- là một khối (mượn gốc Latin probare).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa, ngăn bằng dấu phẩy.
V = {
    "отдавать": "đưa lại, giao lại, cống hiến",       # RÚT «trả lại» (trùng возвращать) + «đưa» (trùng давать)
    "отдать": "đưa lại, giao lại, cống hiến",         # RÚT «trả lại» — trùng верну́ть
    "останавливать": "làm dừng lại, chặn lại, ngăn lại",  # RÚT «dừng» — trùng стоять; nghiêng về ngoại động
    "остановить": "làm dừng lại, chặn lại, ngăn lại",     # RÚT «dừng lại» — trùng остановиться (k123)
    "пробовать": "làm thử, nếm thử",                  # RÚT «thử» — trùng проверять, пытаться
    "попробовать": "làm thử",                         # RÚT «thử» — trùng попыта́ться; gloss không có «taste»
    "существовать": "tồn tại, hiện hữu",              # RÚT «có» — trùng быть/есть/иметь; «tồn tại» vẫn trùng (báo lên)
    "вызвать": "gọi đến, triệu tập, gây ra, khơi dậy",
    "вызывать": "gọi đến, triệu tập, gây ra, khơi dậy",   # thẻ cũ thiếu hẳn nghĩa gốc «gọi đến»
    "выиграть": "thắng, giành được",
    "выигрывать": "thắng, giành được",
    "поднимать": "nhấc lên, nâng lên, nhặt lên",
    "поднять": "nhấc lên, nâng lên, nhặt lên",
    "снимать": "cởi, tháo, lấy xuống, thuê nhà, quay phim",   # «thuê» trần trùng брать/взять; «chụp ảnh» trùng фотографировать
    "снять": "cởi, tháo, lấy xuống, thuê nhà, quay phim",
    "убирать": "dọn dẹp, dọn đi, cất đi",
    "убрать": "dọn dẹp, dọn đi, cất đi",
    "бросать": "ném, quăng, bỏ rơi, từ bỏ",
    "бросить": "ném, quăng, bỏ rơi, từ bỏ",
}

# ------------------------------------------------------------------ от- + дать
S["отдать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">TỪ, rời khỏi mình</span></div>'
    '<div class="hd-row"><span class="hd-piece">-да-</span>'
    '<span class="hd-gloss">CHO — chính là <b>дать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cho RỜI khỏi tay mình ⇒ đưa lại, giao lại, dốc hết: <b>отда́ть долг</b> '
    'trả nợ, <b>отда́ть все си́лы</b> dốc hết sức. Bảng chia chép y nguyên <b>дать</b> '
    '(<b>отда́м · отда́шь · отдаду́т</b>); quá khứ trọng âm lên tiền tố <b>о́тдал</b>, riêng '
    'giống cái <b>отдала́</b>.</div>'
    '<div class="hd-warn">Gần <b>верну́ть</b> nhưng khác hướng nhìn: <b>верну́ть</b> = đưa VỀ '
    'chỗ cũ; <b>отда́ть</b> = cho RỜI khỏi mình, kể cả cho hẳn người khác.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отдава́ть</b> (CHT) · <b>дать</b> cho · <b>прода́ть</b> bán · '
    '<b>переда́ть</b> chuyển, trao lại · <b>сдать</b> nộp, giao lại</div>'
)

S["отдавать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">TỪ, rời khỏi mình</span></div>'
    '<div class="hd-row"><span class="hd-piece">-да-</span>'
    '<span class="hd-gloss">CHO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва-</span>'
    '<span class="hd-gloss">hậu tố "đang / hay làm" → CHT</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>отда́ть</b> — nghĩa xem ở thẻ đó. Đúng như '
    '<b>дава́ть</b>: chia hiện tại BỎ HẲN <i>-ва-</i> — <b>отдаю́ · отдаёшь · отдаю́т</b>, '
    'không phải *отдава́ю.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отда́ть</b> (HT) · <b>дава́ть</b> cho · <b>продава́ть</b> bán · '
    '<b>передава́ть</b> chuyển, trao lại</div>'
)

# ------------------------------------------------------------------ о- + -станов-
S["остановить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">tiền tố, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-станов-</span>'
    '<span class="hd-gloss">ĐỨNG — cùng gốc <b>стать</b>, <b>стоя́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho ĐỨNG lại ⇒ dừng xe, chặn người, cầm máu. Luôn cần cái bị dừng '
    'ở cách 4: <b>останови́ть маши́ну</b>. Ngôi «tôi» thêm <i>л</i>: <b>остановлю́</b>; các '
    'ngôi sau trọng âm lùi vào giữa: <b>остано́вишь</b>.</div>'
    '<div class="hd-warn">Tự mình dừng thì phải có <i>-ся</i>: <b>Авто́бус останови́лся</b> '
    '(xe tự dừng) · <b>Води́тель останови́л авто́бус</b> (tài xế cho xe dừng).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>остана́вливать</b> (CHT) · <b>останови́ться</b> dừng lại · '
    '<b>остано́вка</b> điểm dừng, bến xe · <b>стоя́ть</b> đứng</div>'
)

S["останавливать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">tiền tố, không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-станавл-</span>'
    '<span class="hd-gloss">= <i>-станов-</i> ĐỨNG, đã biến mặt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ива-</span>'
    '<span class="hd-gloss">hậu tố kéo dài → CHT</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>останови́ть</b> — nghĩa và cách dùng xem ở thẻ đó. '
    'Thêm <i>-ива-</i> kéo theo hai thay đổi: <i>о</i> gốc hoá <i>а</i>, và phụ âm biến y như '
    'ngôi «tôi» (<b>остановлю́</b>) — cùng luật với <b>спроси́ть → спра́шивать</b>. '
    'Chia đều: <b>остана́вливаю</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>останови́ть</b> (HT) · <b>остана́вливаться</b> dừng lại · '
    '<b>остано́вка</b> điểm dừng</div>'
)

# ------------------------------------------------------------------ проб- THỬ
S["пробовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">проб-</span>'
    '<span class="hd-gloss">THỬ — theo từ nguyên mượn từ Latin <i>probare</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ть</span>'
    '<span class="hd-gloss">đuôi tạo động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng nguồn với tiếng Anh <i>probe</i>, <i>prove</i>: đem ra thử để biết. '
    'Thử bằng lưỡi ⇒ nếm: <b>про́бовать суп</b>. Đuôi <i>-ова-</i> khi chia thành <i>-у-</i>: '
    '<b>про́бую · про́буешь</b>.</div>'
    '<div class="hd-warn">🔴 <i>про-</i> ở đây KHÔNG phải tiền tố «xuyên qua» như trong '
    '<b>проверя́ть</b> — <i>проб-</i> là một khối, đừng chẻ.</div>'
    '<div class="hd-warn"><b>про́бовать</b> = làm thử xem sao · <b>пыта́ться</b> = cố làm '
    '(chưa chắc được). Khác gốc, đừng gộp.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>попро́бовать</b> (HT) · <b>про́ба</b> mẫu thử, sự thử</div>'
)

S["попробовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">chỉ đánh dấu XONG, không thêm nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пробовать</span>'
    '<span class="hd-gloss">THỬ — chính là <b>про́бовать</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bản HT của <b>про́бовать</b>, chia y hệt: <b>попро́бую · попро́буешь</b>. '
    'Câu hay dùng nhất: <b>Попро́буй!</b> = Thử đi! — kể cả mời nếm đồ ăn: '
    '<b>Попро́буйте торт</b>.</div>'
    '<div class="hd-warn"><b>Попро́бую</b> = tôi thử xem · <b>Попыта́юсь</b> = tôi sẽ cố. '
    'Hai gốc khác nhau, gần nghĩa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>про́бовать</b> (CHT) · <b>про́ба</b> mẫu thử, sự thử</div>'
)

# ------------------------------------------------------------------ сущ- ĐANG CÓ
S["существовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">сущ-</span>'
    '<span class="hd-gloss">ĐANG CÓ — theo từ nguyên là dạng cổ của <b>быть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-еств-</span>'
    '<span class="hd-gloss">đuôi danh từ → <b>существо́</b> sinh vật, thực thể</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ть</span>'
    '<span class="hd-gloss">đuôi tạo động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>существо́</b> = «cái đang có»; thêm đuôi động từ ⇒ là một cái đang có '
    '= tồn tại. Đuôi <i>-ова-</i> chia thành <i>-у-</i>: <b>существу́ет</b>. Khác chữ «có» '
    'thường ngày (<b>есть</b>): từ này trang trọng — <b>Э́та пробле́ма существу́ет</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>существо́</b> sinh vật · <b>существова́ние</b> sự tồn tại · '
    '<b>существи́тельное</b> DANH TỪ (ngữ pháp: từ chỉ cái tồn tại)</div>'
)

# ------------------------------------------------------------------ вы- + звать
S["вызвать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">RA ngoài</span></div>'
    '<div class="hd-row"><span class="hd-piece">-зв-</span>'
    '<span class="hd-gloss">GỌI — chính là <b>звать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gọi RA ⇒ gọi tới: <b>вы́звать врача́</b>, <b>вы́звать такси́</b>. Gọi ra '
    'một phản ứng ⇒ gây ra: <b>вы́звать интере́с</b>. Cùng hình ảnh (không cùng gốc) với tiếng Anh '
    '<i>evoke</i>, <i>provoke</i>. Chia như <b>звать</b>: <b>вы́зову · вы́зовешь</b>.</div>'
    '<div class="hd-warn"><i>вы-</i> ở động từ HT luôn giữ trọng âm suốt bảng (<b>вы́звать</b>, '
    '<b>вы́зову</b>) — bản CHT <b>вызыва́ть</b> thì không.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вызыва́ть</b> (CHT) · <b>звать</b> gọi · <b>позва́ть</b> gọi, mời · '
    '<b>назва́ть</b> đặt tên · <b>вы́зов</b> lời gọi, lời thách</div>'
)

S["вызывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">RA ngoài</span></div>'
    '<div class="hd-row"><span class="hd-piece">-зыв-</span>'
    '<span class="hd-gloss">GỌI — gốc <i>зв-/зов-</i> của <b>звать</b>, đổi mặt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi kéo dài → CHT</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>вы́звать</b>; mặt gốc <i>-зыв-</i> y hệt '
    '<b>называ́ть</b>. Hay gặp nhất ở nghĩa «gây ra»: <b>Э́то вызыва́ет вопро́сы</b> = cái này '
    'làm dấy lên câu hỏi. Chia đều: <b>вызыва́ю</b>, trọng âm KHÔNG nằm ở <i>вы-</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́звать</b> (HT) · <b>называ́ть</b> gọi là · <b>звать</b> gọi</div>'
)

# ------------------------------------------------------------------ вы- + играть
S["выиграть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">RA — làm tới khi lấy được kết quả ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">-игр-</span>'
    '<span class="hd-gloss">CHƠI — như <b>игра́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chơi cho RA được cái gì ⇒ thắng, giành được: <b>вы́играть матч</b>, '
    '<b>вы́играть приз</b>. Chia đều như <b>игра́ть</b>; <i>вы-</i> HT giữ trọng âm suốt bảng: '
    '<b>вы́играю</b>.</div>'
    '<div class="hd-warn">Thắng ĐỐI THỦ thì dùng <b>у</b> + cách 2: <b>вы́играть у Ива́на</b>. '
    'Trận, giải thì cách 4.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>выи́грывать</b> (CHT) · <b>игра́</b> trò chơi · <b>вы́игрыш</b> tiền '
    'thắng, giải thưởng · <b>проигра́ть</b> THUA</div>'
)

S["выигрывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">RA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-игр-</span>'
    '<span class="hd-gloss">CHƠI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-</span>'
    '<span class="hd-gloss">hậu tố kéo dài → CHT</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>вы́играть</b>: thêm <i>-ыва-</i> thì trọng âm rời '
    '<i>вы-</i> sang <b>выи́грывать</b> — chỗ hay đọc sai. Chia đều: <b>выи́грываю</b>. '
    'Cũng là «đang dẫn»: <b>На́ша кома́нда выи́грывает</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́играть</b> (HT) · <b>игра́ть</b> chơi · <b>вы́игрыш</b> tiền thắng</div>'
)

# ------------------------------------------------------------------ под- + -ня-/-ним-
S["поднять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span>'
    '<span class="hd-gloss">DƯỚI → từ dưới lên</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ня-</span>'
    '<span class="hd-gloss">NẮM, LẤY — lõi của <b>взять</b>, <b>поня́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nắm từ dưới đưa lên ⇒ nhấc, nhặt, nâng: <b>подня́ть ру́ку</b> giơ tay, '
    '<b>подня́ть це́ны</b> tăng giá. Tương lai lộ mặt <i>-ним-</i>: <b>подниму́ · подни́мешь</b>; '
    'quá khứ trọng âm lên tiền tố <b>по́днял</b>, riêng giống cái <b>подняла́</b>.</div>'
    '<div class="hd-warn">Nhấc CÁI GÌ (cách 4) — <b>подня́ть чемода́н</b>. Tự mình đi lên là '
    '<b>подня́ться</b>: <b>подня́ться на эта́ж</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поднима́ть</b> (CHT) · <b>подня́ться</b> đi lên, tăng lên · '
    '<b>подъём</b> sự đi lên · <b>снять</b> lấy xuống · <b>взять</b> lấy</div>'
)

S["поднимать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span>'
    '<span class="hd-gloss">DƯỚI → từ dưới lên</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ним-</span>'
    '<span class="hd-gloss">NẮM, LẤY — mặt khác của <i>-ня-</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi kéo dài → CHT</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>подня́ть</b> — nghĩa xem ở thẻ đó. Ghép đúng khuôn '
    '<b>понима́ть : поня́ть</b>, <b>принима́ть : приня́ть</b>. Chia đều: <b>поднима́ю</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>подня́ть</b> (HT) · <b>поднима́ться</b> đi lên · '
    '<b>понима́ть</b> hiểu · <b>снима́ть</b> cởi, tháo</div>'
)

# ------------------------------------------------------------------ с- + -ня-/-ним-
S["снять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">KHỎI bề mặt, từ trên xuống</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ня-</span>'
    '<span class="hd-gloss">NẮM, LẤY — như <b>взять</b>, <b>подня́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nắm lấy KHỎI chỗ đang bám ⇒ cởi áo, tháo tranh xuống. Lấy hình ra khỏi '
    'cảnh ⇒ quay, chụp: <b>снять фильм</b>. Nghĩa «thuê» thì phải thuộc: <b>снять кварти́ру</b>. '
    'Tương lai lộ <i>-ним-</i>: <b>сниму́ · сни́мешь</b>; quá khứ giống cái <b>сняла́</b>.</div>'
    '<div class="hd-warn">Người thuê <b>снима́ет</b> кварти́ру · chủ nhà <b>сдаёт</b> кварти́ру '
    '(cho thuê). Đừng lẫn hai chiều.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>снима́ть</b> (CHT) · <b>сни́мок</b> bức ảnh chụp · '
    '<b>подня́ть</b> nhấc lên · <b>взять</b> lấy</div>'
)

S["снимать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">KHỎI bề mặt, từ trên xuống</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ним-</span>'
    '<span class="hd-gloss">NẮM, LẤY — mặt khác của <i>-ня-</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi kéo dài → CHT</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>снять</b> — nghĩa xem ở thẻ đó, khuôn y như '
    '<b>поднима́ть : подня́ть</b>. Chia đều: <b>снима́ю</b>. Việc lặp lại hằng ngày: '
    '<b>В до́ме снима́ют о́бувь</b> = vào nhà thì cởi giày.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>снять</b> (HT) · <b>сни́мок</b> bức ảnh · <b>поднима́ть</b> nhấc lên · '
    '<b>понима́ть</b> hiểu</div>'
)

# ------------------------------------------------------------------ у- + брать
S["убрать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">RỜI KHỎI, ra xa — như <b>уйти́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-бр-</span>'
    '<span class="hd-gloss">LẤY — chính là <b>брать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lấy ĐI chỗ khác ⇒ cất đi, dọn đi; dọn hết đồ thừa thì phòng gọn ⇒ '
    'dọn dẹp: <b>убра́ть ко́мнату</b>. Chia y như <b>брать</b>, <i>е</i> mọc lại: '
    '<b>уберу́ · уберёшь</b>; quá khứ giống cái <b>убрала́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>убира́ть</b> (CHT) · <b>брать</b> lấy · <b>собра́ть</b> gom lại · '
    '<b>вы́брать</b> chọn · <b>убо́рка</b> sự dọn dẹp</div>'
)

S["убирать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">RỜI KHỎI, ra xa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бир-</span>'
    '<span class="hd-gloss">LẤY — gốc <i>бр-/бер-</i> của <b>брать</b>, mọc <i>и</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi kéo dài → CHT</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>убра́ть</b>; khuôn <i>-бр- → -бир-</i> y như '
    '<b>собра́ть → собира́ть</b>. Chia đều: <b>убира́ю</b>. Việc lặp lại: '
    '<b>Я убира́ю ко́мнату по суббо́там</b> — tôi dọn phòng mỗi thứ Bảy.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>убра́ть</b> (HT) · <b>собира́ть</b> thu gom · <b>убо́рка</b> sự dọn dẹp</div>'
)

# ------------------------------------------------------------------ брос- NÉM
S["бросить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">брос-</span>'
    '<span class="hd-gloss">NÉM — gốc trơn, không chẻ thêm được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ném khỏi tay ⇒ quăng; ném lại phía sau ⇒ bỏ rơi, bỏ hẳn. Ngôi «tôi» '
    '<i>с</i> hoá <i>ш</i>: <b>бро́шу</b>, các ngôi khác giữ <i>с</i>: <b>бро́сишь</b>.</div>'
    '<div class="hd-warn"><b>бро́сить</b> + nguyên thể = BỎ hẳn một thói quen: '
    '<b>бро́сить кури́ть</b> bỏ thuốc lá.</div>'
    '<div class="hd-warn">Bỏ một NGƯỜI: <b>Она́ его́ бро́сила</b> = cô ấy bỏ anh ta.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>броса́ть</b> (CHT) · <b>бросо́к</b> cú ném</div>'
)

S["бросать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">брос-</span>'
    '<span class="hd-gloss">NÉM — gốc trơn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi kéo dài → CHT</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>бро́сить</b>: đổi <i>-и-</i> thành <i>-а-</i>, trọng âm dời '
    'ra đuôi — <b>броса́ть</b>, chia đều <b>броса́ю</b>. Dùng cho ném nhiều lần, hoặc đang bỏ '
    'dần: <b>Я броса́ю кури́ть</b> = tôi đang cai thuốc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бро́сить</b> (HT) · <b>бросо́к</b> cú ném</div>'
)
