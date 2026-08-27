# -*- coding: utf-8 -*-
"""k80 — động từ chuyển động có tiền tố + прыгать + vài hư từ.

Trục thật của lô: **hai gốc chuyển động** `-ход-` (bằng CHÂN) và `-езж-` (bằng XE),
mỗi gốc ghép với `в- / вы- / до- / при-`. Bốn thẻ `доходить · доезжать · приходить ·
приезжать` cùng badge [v/IMPF] nên badge KHÔNG tách được chúng — chỉ dòng tiếng Việt
tách, và phải tách theo đúng lối các thẻ thể hoàn thành đã có sẵn trong kho
(`дойти` = đi bộ tới tận nơi · `доехать` = đi xe tới tận nơi · `приехать` = đến bằng xe).

Bộ ba `прыгать / прыгнуть / попрыгать` khác nhau ở SỐ LẦN — nói đủ ở đúng thẻ
`прыгать`, hai thẻ kia chỉ nhắc một dòng (README §3).
"""

S = {}

# ---------------------------------------------------------------- входить
S["входить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO, vào bên trong</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ход-</span>'
    '<span class="hd-gloss">gốc ĐI BẰNG CHÂN (như <b>ходи́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đi bằng chân (<b>-ход-</b>) mà tiến VÀO trong (<b>в-</b>). '
    'Nghĩa «bao gồm, là thành viên» vẫn đúng hình ảnh đó: cái này đi VÀO bên trong '
    'tập hợp kia.</div>'
    '<div class="hd-warn">Ngôi «tôi» đổi <b>д→ж</b> và trọng âm nhảy ra đuôi: '
    'я <b>вхожу́</b> nhưng ты <b>вхо́дишь</b>. Cả bốn động từ <b>-ходи́ть</b> của lô này '
    'đều theo đúng luật đó.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>войти́</b> đi vào (một lần) · <b>вход</b> lối vào · '
    '<b>ходи́ть</b> đi, đi lại</div>'
)

# --------------------------------------------------------------- выходить
S["выходить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">RA, ra khỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ход-</span>'
    '<span class="hd-gloss">gốc ĐI BẰNG CHÂN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đi RA ngoài. Mọi nghĩa còn lại đều là cái «ra» đó: ra khỏi xe '
    '= xuống xe, sách «ra» = được xuất bản.</div>'
    '<div class="hd-warn">Ngôi «tôi» đổi <b>д→ж</b>, trọng âm nhảy ra đuôi: '
    'я <b>выхожу́</b> / ты <b>выхо́дишь</b>. Nhưng ở thể hoàn thành <b>вы́йти</b> thì '
    'tiền tố <b>вы-</b> hút trọng âm về mình — đúng cho mọi động từ <b>вы-</b> hoàn '
    'thành.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́йти</b> đi ra (một lần) · <b>вы́ход</b> lối ra · '
    '<b>вход</b> lối vào</div>'
)

# --------------------------------------------------------------- доходить
S["доходить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI TẬN, cho đến hết mức</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ход-</span>'
    '<span class="hd-gloss">gốc ĐI BẰNG CHÂN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đi bộ cho TỚI TẬN đích. Vì <b>до-</b> là «tới tận mức» nên từ '
    'này dùng được cả cho con số (lên tới bao nhiêu) lẫn cho ý nghĩ: '
    '<b>до меня́ дохо́дит</b> = tôi đang vỡ ra, hiểu ra.</div>'
    '<div class="hd-warn">Ngôi «tôi» đổi <b>д→ж</b>: я <b>дохожу́</b> / '
    'ты <b>дохо́дишь</b>. Từ này luôn kéo theo <b>до</b> + cách 2.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дойти́</b> đi bộ tới nơi (một lần) · <b>доезжа́ть</b> đi xe '
    'tới nơi · <b>ходи́ть</b> đi, đi lại</div>'
)

# -------------------------------------------------------------- приходить
S["приходить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">TỚI NƠI, áp sát vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ход-</span>'
    '<span class="hd-gloss">gốc ĐI BẰNG CHÂN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đi bộ mà TỚI NƠI. Khác <b>доходи́ть</b> ở chỗ nhấn: <b>до-</b> '
    'nhấn quãng đường đi cho hết, <b>при-</b> nhấn việc đã có mặt ở đây. Đi với '
    '<b>в/на</b> + cách 4: <b>приходи́ть на рабо́ту</b>.</div>'
    '<div class="hd-warn">Ngôi «tôi» đổi <b>д→ж</b>: я <b>прихожу́</b> / '
    'ты <b>прихо́дишь</b>. Thể chưa hoàn thành này là đến ĐỀU ĐẶN, thường xuyên; một lần '
    'cụ thể thì dùng <b>прийти́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прийти́</b> đến (một lần) · <b>приезжа́ть</b> đến bằng xe · '
    '<b>ходи́ть</b> đi, đi lại</div>'
)

# ---------------------------------------------------------------- поехать
S["поехать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố KHỞI SỰ — bắt đầu đi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́хать</span>'
    '<span class="hd-gloss">gốc ĐI BẰNG XE</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gắn <b>по-</b> vào động từ chuyển động thì được nghĩa KHỞI HÀNH: '
    '<b>е́хать</b> là đang trên đường, còn <b>пое́хать</b> là lên đường, xuất phát.</div>'
    '<div class="hd-warn">Hai chỗ phải thuộc riêng: thân tương lai là <b>пое́ду</b>, '
    '<b>пое́дешь</b> (không suy thẳng từ nguyên thể); mệnh lệnh lại mượn hẳn mặt chữ khác '
    '— <b>поезжа́й</b>, <b>поезжа́йте</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>е́хать</b> đi xe · <b>е́здить</b> đi lại bằng xe · '
    '<b>прие́хать</b> đến bằng xe</div>'
)

# --------------------------------------------------------------- доезжать
S["доезжать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI TẬN, cho đến hết mức</span></div>'
    '<div class="hd-row"><span class="hd-piece">-езж-</span>'
    '<span class="hd-gloss">gốc ĐI BẰNG XE</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi kéo dài → thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng một khuôn với <b>доходи́ть</b>, chỉ đổi gốc: <b>-ход-</b> là '
    'bằng chân, <b>-езж-</b> là bằng xe. Nhớ được một cặp là có luôn cả bốn từ.</div>'
    '<div class="hd-warn">Gốc «đi xe» có ba mặt chữ, đừng tưởng là ba từ lạ: <b>е́хать</b> '
    '(nguyên thể), <b>е́здить</b> (đi lại nhiều lần), và <b>-езжа́ть</b> — mặt chữ dành '
    'riêng cho các từ có tiền tố.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дое́хать</b> đi xe tới nơi (một lần) · <b>приезжа́ть</b> đến '
    'bằng xe · <b>е́здить</b> đi lại bằng xe</div>'
)

# -------------------------------------------------------------- приезжать
S["приезжать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">TỚI NƠI, áp sát vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-езж-</span>'
    '<span class="hd-gloss">gốc ĐI BẰNG XE</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi kéo dài → thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng cặp với <b>приходи́ть</b>, chỉ khác phương tiện: tới nơi bằng '
    'chân thì <b>приходи́ть</b>, tới nơi bằng xe thì <b>приезжа́ть</b>. Đường xa — sang '
    'thành phố khác, sang nước khác — gần như luôn là <b>приезжа́ть</b>.</div>'
    '<div class="hd-warn">Nhóm <b>-езжа́ть</b> chia đều theo lớp 1 (<b>приезжа́ю</b>, '
    '<b>приезжа́ешь</b>), không có <b>д→ж</b> như nhóm <b>-ходи́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прие́хать</b> đến bằng xe (một lần) · <b>доезжа́ть</b> đi xe '
    'tới nơi · <b>е́хать</b> đi xe</div>'
)

# ---------------------------------------------------------------- прыгать
S["прыгать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пры́г-</span>'
    '<span class="hd-gloss">gốc NHẢY (<b>прыг</b> là tiếng «phốc»)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi lớp 1, chia đều</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ba từ cùng gốc trong lô khác nhau ở SỐ LẦN: <b>пры́гать</b> đang '
    'hoặc hay nhảy · <b>пры́гнуть</b> bật đúng một cú · <b>попры́гать</b> nhảy vài cái rồi '
    'thôi.</div>'
    '<div class="hd-warn">Danh từ <b>прыжо́к</b> «cú nhảy» lộ hai chỗ một lúc: phép biến âm '
    'quen thuộc <b>г→ж</b>, và trọng âm rời gốc nhảy hẳn xuống đuôi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пры́гнуть</b> nhảy một cái · <b>попры́гать</b> nhảy nhót một '
    'lúc · <b>прыжо́к</b> cú nhảy</div>'
)

# --------------------------------------------------------------- прыгнуть
S["прыгнуть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пры́г-</span>'
    '<span class="hd-gloss">gốc NHẢY</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ну-</span>'
    '<span class="hd-gloss">hậu tố MỘT PHÁT, đúng một lần</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hậu tố <b>-ну-</b> ở đây có nghĩa «một cái duy nhất», nên '
    '<b>пры́гнуть</b> là bật lên đúng một cú rồi hết — cùng khuôn với <b>крича́ть</b> (kêu '
    'la) → <b>кри́кнуть</b> (kêu một tiếng). Ba từ cùng gốc phân biệt ở thẻ '
    '<b>пры́гать</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пры́гать</b> nhảy, nhảy nhót · <b>попры́гать</b> nhảy nhót một '
    'lúc · <b>прыжо́к</b> cú nhảy</div>'
)

# -------------------------------------------------------------- попрыгать
S["попрыгать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">LÀM MỘT LÚC rồi thôi</span></div>'
    '<div class="hd-row"><span class="hd-piece">пры́г-</span>'
    '<span class="hd-gloss">gốc NHẢY</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi lớp 1</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gắn <b>по-</b> vào một động từ chưa hoàn thành thì được nghĩa «làm '
    'một lát rồi dừng» — như <b>говори́ть</b> → <b>поговори́ть</b> (nói chuyện một '
    'lúc).</div>'
    '<div class="hd-warn">Đừng gộp hai <b>по-</b> làm một: ở <b>пое́хать</b> nó là BẮT ĐẦU '
    'đi, ở <b>попры́гать</b> nó là LÀM MỘT LÚC. Cùng một tiền tố, nghĩa do gốc quyết '
    'định.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пры́гать</b> nhảy · <b>пры́гнуть</b> nhảy một cái · '
    '<b>прыжо́к</b> cú nhảy</div>'
)

# --------------------------------------------------------------------- ни
S["ни"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hư từ một âm tiết, không chẻ được. Việc của nó là KHUẾCH ĐẠI một '
    'câu đã phủ định sẵn: <b>не</b> làm ra cái «không», <b>ни</b> đẩy cái không đó thành '
    '«không một tí nào». Dùng đôi <b>ни… ни…</b> = «không… mà cũng không…».</div>'
    '<div class="hd-warn">Dán <b>ни</b> vào một từ để hỏi thì đẻ ra cả bộ từ phủ định — đây '
    'là lý do phải nhớ nó: <b>кто</b> → <b>никто́</b>, <b>где</b> → <b>нигде́</b>, '
    '<b>когда́</b> → <b>никогда́</b>.</div>'
    '<div class="hd-warn">Cụm phải thuộc: <b>ни за что</b> = đời nào, không bao giờ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>никто́</b> không ai · <b>ничего́</b> không gì · '
    '<b>никогда́</b> không bao giờ · <b>нигде́</b> không đâu</div>'
)

# ------------------------------------------------------------------ пусть
S["пусть"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vốn là dạng mệnh lệnh cũ của <b>пусти́ть</b> «thả ra, để cho», nay '
    'đông cứng thành hư từ. Ghép <b>пусть</b> + động từ chia ngôi 3 là cách tiếng Nga ra '
    'lệnh cho người thứ ba, vì mệnh lệnh thật chỉ có ở ngôi 2: <b>Пусть он идёт</b> = cứ để '
    'anh ấy đi.</div>'
    '<div class="hd-warn">Nghĩa thứ hai là nhượng bộ, «cứ cho là, dẫu rằng»: '
    '<b>Пусть так</b> = thì cứ cho là thế.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пусти́ть</b> thả ra, cho đi · <b>пуска́й</b> cũng là «cứ để», '
    'khẩu ngữ hơn</div>'
)

# ------------------------------------------------------------------- надо
S["надо"] = (
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hư từ, không chẻ được. Điều phải thuộc là CẤU TRÚC CÂU: câu với '
    '<b>на́до</b> không có chủ ngữ cách 1 — người phải làm đứng ở CÁCH 3. '
    '<b>Мне на́до идти́</b> = tôi phải đi. Quá khứ chèn <b>бы́ло</b>, tương lai chèn '
    '<b>бу́дет</b>, đặt ngay sau <b>на́до</b>.</div>'
    '<div class="hd-warn">Phủ định <b>не на́до</b> nghĩa là «đừng, khỏi cần», không phải '
    '«không phải»: <b>Не на́до!</b> = Thôi đừng!</div>'
    '<div class="hd-warn">Gần như thay được cho <b>ну́жно</b>; <b>на́до</b> đời thường hơn, '
    '<b>ну́жно</b> trang trọng hơn một chút.</div>'
)

# -------------------------------------------------------------------- жаль
S["жаль"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">жал-</span>'
    '<span class="hd-gloss">gốc THƯƠNG XÓT, tiếc</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc <b>-жал-</b> với <b>сожале́ние</b> và <b>пожа́луйста</b>. '
    'Là từ vô nhân xưng: người thấy tiếc đứng CÁCH 3 — <b>Мне жаль</b> = tôi thấy '
    'tiếc.</div>'
    '<div class="hd-warn">Hai kiểu dùng khác hẳn nhau: <b>жаль</b> + cách 4 là THƯƠNG ai '
    '(<b>Мне жаль тебя́</b> = tôi tội nghiệp cậu), còn <b>жаль, что…</b> là TIẾC rằng…</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жале́ть</b> thương, tiếc · <b>жа́лко</b> tội nghiệp · '
    '<b>жа́лость</b> lòng thương · <b>сожале́ние</b> sự tiếc nuối</div>'
)

# ---------------------------------------------------------------- ставить
S["ставить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">-став-</span>'
    '<span class="hd-gloss">gốc LÀM CHO ĐỨNG (họ với <b>стоя́ть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>стоя́ть</b> là tự nó đứng, <b>ста́вить</b> là làm cho nó đứng — '
    'tức đặt THẲNG ĐỨNG: chai, cốc, ấm. Đặt cho NẰM NGANG thì tiếng Nga dùng động từ '
    'khác hẳn — <b>класть</b>.</div>'
    '<div class="hd-warn">Ngôi «tôi» chèn thêm <b>л</b>: я <b>ста́влю</b>. Luật chung dùng '
    'lại được suốt đời: gốc kết thúc bằng <b>б в м п ф</b> thì ngôi «tôi» thêm <b>л</b> — '
    'giống <b>люби́ть</b> → <b>люблю́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поста́вить</b> đặt đứng (một lần) · <b>соста́вить</b> lập ra · '
    '<b>составля́ть</b> cấu thành · <b>стоя́ть</b> đứng</div>'
)

# ---------------------------------------------------------------- найтись
S["найтись"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">найти́</span>'
    '<span class="hd-gloss">TÌM RA cái gì đó</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сь</span>'
    '<span class="hd-gloss">đuôi phản thân → «tự nó»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thêm <b>-сь</b> là lật câu lại: không còn ai đi tìm nữa, mà chính '
    'vật đó tự lộ ra. <b>Ключи́ нашли́сь</b> = chìa khoá đã thấy rồi — không nói ai tìm '
    'được.</div>'
    '<div class="hd-warn">Quá khứ đổi hẳn mặt chữ, phải thuộc riêng: <b>нашёлся</b> / '
    '<b>нашла́сь</b> / <b>нашли́сь</b>. Chữ <b>ё</b> trong <b>нашёлся</b> chính là chỗ '
    'trọng âm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>найти́</b> tìm thấy · <b>находи́ться</b> nằm ở, tọa lạc · '
    '<b>нахо́дка</b> vật nhặt được</div>'
)

# ----------------------------------------------------------------- разбить
S["разбить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span>'
    '<span class="hd-gloss">TÁCH RA từng mảnh, ra các phía</span></div>'
    '<div class="hd-row"><span class="hd-piece">-би́ть</span>'
    '<span class="hd-gloss">gốc ĐÁNH, ĐẬP (như <b>бить</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đánh cho TÁCH RA = đập vỡ. Cũng chính cái <b>раз-</b> ấy cho nghĩa '
    '«chia thành phần» (chia lớp thành nhóm) và nghĩa «đánh tan» quân địch.</div>'
    '<div class="hd-warn">Thân tương lai không suy được từ nguyên thể — gốc thật <b>бь-</b> '
    'hiện ra và phải chèn <b>о</b> cho khỏi dồn phụ âm: <b>разобью́</b>, '
    '<b>разобьёшь</b>; mệnh lệnh <b>разбе́й</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бить</b> đánh, đập · <b>разбива́ть</b> đập vỡ (chưa xong) · '
    '<b>разби́тый</b> vỡ tan</div>'
)

# -------------------------------------------------------------- составлять
S["составлять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG, gộp lại với nhau</span></div>'
    '<div class="hd-row"><span class="hd-piece">-став-</span>'
    '<span class="hd-gloss">gốc ĐẶT (như <b>ста́вить</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ля́ть</span>'
    '<span class="hd-gloss">đuôi kéo dài → thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">ĐẶT các mảnh lại CÙNG nhau = gộp thành, lập nên. Nghĩa con số cũng '
    'từ đó mà ra: các phần cộng lại «gộp thành» bao nhiêu, tức tổng cộng lên tới bấy '
    'nhiêu.</div>'
    '<div class="hd-warn">Chữ <b>л</b> trong <b>-ля́ть</b> mọc ra đúng chỗ chữ <b>л</b> của '
    'я <b>ста́влю</b> mọc ra: ngay sau <b>в</b> cuối gốc. Thấy được chỗ đó thì '
    '<b>ста́вить</b>, <b>соста́вить</b> và <b>составля́ть</b> gộp thành một họ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>соста́вить</b> lập ra (một lần) · <b>ста́вить</b> đặt, để · '
    '<b>соста́в</b> thành phần, đội hình</div>'
)

# --------------------------------------------------------------- проверить
S["проверить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">XUYÊN QUA, soi từ đầu đến cuối</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вер-</span>'
    '<span class="hd-gloss">gốc <b>ве́ра</b> — niềm tin</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Soi XUYÊN QUA cái gì để xem có TIN được không = kiểm tra. Cùng gốc '
    'với <b>ве́рить</b> «tin» — kiểm tra chính là hành động xác nhận lòng tin.</div>'
    '<div class="hd-warn">Cặp thể lệch cả trọng âm, phải để ý: <b>прове́рить</b> là kiểm '
    'xong một lần, <b>проверя́ть</b> là đang hoặc thường xuyên kiểm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>проверя́ть</b> kiểm tra (chưa xong) · <b>ве́рить</b> tin · '
    '<b>ве́ра</b> niềm tin · <b>прове́рка</b> cuộc kiểm tra</div>'
)

# ============================================================ field Vietnamese
# Chỉ sửa dòng thật sự hỏng: ngoặc chú thích (README §2c cấm ③), va chạm nghĩa với
# thẻ khác cùng badge, hoặc nghĩa sai/thiếu mà gloss tiếng Anh xác nhận được.
V = {
    # === BỐN THẺ VA CHẠM CHÉO NHAU ('đến nơi' · 'đi đến' · 'đến') ===
    # Tách theo đúng lối các thẻ PERF đã có trong kho: gốc ход = đi bộ, gốc езж =
    # bằng xe, viết thẳng vào nghĩa chứ không nhét vào ngoặc.
    # доходить: khớp дойти "đi bộ tới tận nơi, đi bộ đến được"; hai nghĩa riêng
    # (amount / it sinks in) giữ lại nên không mục nào còn trùng ba thẻ kia.
    # "lên tới" bị bỏ vì trùng nguyên mục với составлять (cùng [v/IMPF]) — dùng
    # lại "đến mức" của bản cũ, không mục nào khác mang cụm đó
    "доходить": "đi bộ tới tận nơi, đi bộ đến được, đến mức, hiểu ra",
    # доезжать: khớp nguyên đôi với доехать "đi xe tới tận nơi, đi xe đến được"
    "доезжать": "đi xe tới tận nơi, đi xe đến được",
    # приходить: bỏ "đến" trần và "đi đến" (hai mục gây va chạm), thay bằng cách
    # nói có gốc ход như прийти/дойти
    "приходить": "đi bộ đến, đi bộ tới nơi, ghé qua",
    # приезжать: bỏ ngoặc "(bằng phương tiện)" — phạm cấm ③; khớp приехать
    "приезжать": "đến bằng xe, tới nơi bằng xe",

    # === BỎ NGOẶC ===
    # bỏ "(bằng phương tiện)"; по- ở đây là KHỞI HÀNH nên viết ra thành nghĩa
    "поехать": "đi bằng xe, lên đường bằng xe",
    # bỏ "(tổng số)"; khớp bộ nghĩa của соста́вить đã có trên thẻ
    "составлять": "lập nên, soạn thảo, cấu thành, lên tới",

    # === VA CHẠM VỚI THẺ NGOÀI LÔ (mồ côi ⇒ chỉ sửa vế của mình) ===
    # bỏ "nhảy" trần: trùng nguyên mục với танцевать (cùng [v/IMPF], badge không tách)
    "прыгать": "nhảy lên, nhảy nhót",
    # bỏ "chẳng": trùng nguyên mục với не "không, chẳng" (cùng [oth])
    "ни": "cũng không",

    # === SỬA NGHĨA SAI / THIẾU ===
    # "xuất phát" không có trong gloss và sai nghĩa (выходить không phải khởi hành);
    # thay bằng hai nghĩa gloss xác nhận: "get off" và "to be published"
    "выходить": "đi ra, bước ra, ra ngoài, xuống xe, được xuất bản",
    # найтись là PHẢN THÂN: vật tự lộ ra, không phải mình tìm thấy nó — "tìm thấy"
    # ở thể chủ động là nghĩa của найти
    "найтись": "được tìm thấy, tự lộ ra, xuất hiện, có sẵn",
    # gloss có "defeat" — nghĩa thông dụng đang thiếu hẳn
    "разбить": "làm vỡ, đập vỡ, chia nhỏ, đánh bại",
}
