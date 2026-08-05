# -*- coding: utf-8 -*-
"""k04 — concepts::abstract: 13 danh từ trừu tượng + 1 tính từ + 1 đại từ.

Trục của lô: **danh từ trừu tượng dựng từ một gốc có sẵn**
(дру́жба ← друг · борьба́ ← боро́ться · рабо́та ← раб · переры́в ← рвать ·
рёв ← реве́ть · воскресе́ние ← воскре́снуть). Mỗi thẻ chỉ nói cái hậu tố
DÍNH VÀO CHÍNH NÓ, không có khối hệ thống dùng chung (README §3).
"""

S = {}
V = {}

# ─────────────────────────────────────────────────────────── дружба
S["дружба"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">друж-</span>'
    '<span class="hd-gloss">BẠN (từ <b>друг</b>, г đổi thành ж)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ба</span>'
    '<span class="hd-gloss">đuôi cổ, biến việc/quan hệ thành danh từ giống CÁI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">"Cái sự làm bạn". Đuôi <b>-ба</b> kéo theo phép đổi phụ âm '
    'г/к/х → ж/ч/ш ngay trước nó, nên <b>друг</b> ra <b>дру́жба</b> chứ không phải '
    '"другба" — cùng khuôn với <b>борьба́</b> trong lô này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>друг</b> bạn (số nhiều bất thường <b>друзья́</b>) · '
    '<b>подру́га</b> bạn gái · <b>дружи́ть</b> chơi thân với ai · '
    '<b>дру́жеский</b> thân tình</div>'
)
V["дружба"] = "tình bạn, tình bằng hữu"

# ─────────────────────────────────────────────────────────── борьба
S["борьба"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бор-</span>'
    '<span class="hd-gloss">gốc của <b>боро́ться</b> — VẬT LỘN, CHỐNG LẠI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ьба</span>'
    '<span class="hd-gloss">vẫn là đuôi <b>-ба</b> của <b>дру́жба</b>, tạo danh từ chỉ VIỆC</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">"Cái sự vật lộn" — nên một chữ ôm cả nghĩa trừu tượng (cuộc đấu tranh) '
    'lẫn nghĩa cụ thể (môn đấu vật). Trọng âm nằm hẳn ở đuôi: <b>борьба́</b>, <b>борьбы́</b>.</div>'
    '<div class="hd-warn">Học kèm cách mà động từ gốc đòi: <b>боро́ться с</b> + cách 5 = chống lại '
    'ai/cái gì · <b>боро́ться за</b> + cách 4 = đấu tranh VÌ điều gì.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>боро́ться</b> đấu tranh, vật lộn · <b>боре́ц</b> đô vật, chiến sĩ</div>'
)
V['борьба'] = 'cuộc đấu tranh, sự vật lộn, môn đấu vật'

# ─────────────────────────────────────────────────────────── правда
S["правда"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">прав-</span>'
    '<span class="hd-gloss">THẲNG, ĐÚNG, NGAY</span></div>'
    '<div class="hd-row"><span class="hd-piece">-да</span>'
    '<span class="hd-gloss">đuôi cổ hiếm gặp, tạo danh từ trừu tượng (như <b>вражда́</b> mối thù)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">"Cái ngay thẳng" ⇒ sự thật. Cùng ổ với <b>пра́вильный</b> (đúng) và '
    '<b>пра́вый</b> (bên phải, có lý): với tiếng Nga, THẲNG và ĐÚNG là cùng một gốc.</div>'
    '<div class="hd-warn"><b>пра́вда</b> rất hay đứng ngoài vai danh từ, làm một tiếng đệm: '
    'cuối câu = "…đúng không?", đứng riêng = "thật à?", giữa câu = "thì đúng là, có điều".</div>'
    '<div class="hd-warn">Cụm phải thuộc: <b>по пра́вде говоря́</b> = "nói thật ra thì…".</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пра́вильный</b> đúng · <b>пра́вый</b> bên phải · <b>пра́во</b> quyền, luật · '
    '<b>правди́вый</b> chân thật</div>'
)
V['правда'] = 'sự thật, lẽ phải'

# ─────────────────────────────────────────────────────────── обида
S["обида"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">tiền tố: QUANH, LƯỚT QUA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ид-</span>'
    '<span class="hd-gloss">gốc <b>ви́деть</b> NHÌN, chữ в rụng sau об-</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen "bị nhìn lướt qua, bị coi như không có" — đúng cảm giác của '
    'người bị xử tệ. Đây là từ nguyên chứ không phải luật suy ra được, nhưng nó giữ đúng trọng '
    'tâm nghĩa: <b>оби́да</b> là nỗi TỦI của người bị làm tổn thương.</div>'
    '<div class="hd-warn">Đi với <b>на</b> + cách 4: <b>обижа́ться на</b> кого́ = giận dỗi ai. '
    'Và <b>мне оби́дно</b> = "tôi thấy tủi thân" — câu dùng hằng ngày.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оби́деть</b> làm ai tủi · <b>обижа́ться</b> giận dỗi · '
    '<b>оби́дно</b> thật đáng tủi · <b>оби́дчивый</b> hay tự ái</div>'
)
V['обида'] = 'nỗi tủi thân, sự phật lòng, điều xúc phạm'

# ─────────────────────────────────────────────────────────── реплика
S["реплика"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ре-</span>'
    '<span class="hd-gloss">LẠI, đáp trả (La Tinh <i>re-</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-плик-</span>'
    '<span class="hd-gloss">GẤP, GẬP (La Tinh <i>plicare</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mượn nguyên khối từ La Tinh <i>replicare</i> "gập trở lại" ⇒ đáp lại. '
    'Cùng ổ với tiếng Anh <i>reply</i> và <i>replica</i>. Nghĩa dùng hằng ngày là MỘT LƯỢT LỜI: '
    'câu đế trong lúc trò chuyện, hay lời thoại của một nhân vật trong kịch/phim. Nghĩa "bản sao" '
    'thì có nhưng chỉ gặp trong ngành mỹ thuật.</div>'
    '<div class="hd-why">Từ mượn đứng một mình: tiếng Nga không dựng thêm từ phái sinh nào từ nó, '
    'nên không có mục họ hàng.</div>'
)
V['реплика'] = 'lời đối đáp, câu thoại, lời nhận xét'

# ─────────────────────────────────────────────────────────── шутка
S["шутка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">шут-</span>'
    '<span class="hd-gloss">gốc <b>шут</b> — thằng HỀ, anh pha trò</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">đuôi tạo danh từ chỉ một VIỆC/VẬT lẻ, luôn giống CÁI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">"Một trò của thằng hề" ⇒ một câu đùa lẻ. <b>шу́тка</b> luôn là MỘT câu đùa '
    'cụ thể, đếm được; còn sự hài hước nói chung thì tiếng Nga dùng chữ khác (<b>ю́мор</b>).</div>'
    '<div class="hd-warn">Bảng chia có nguyên âm chạy: bỏ đuôi ở số nhiều cách 2 thì cụm тк khó đọc, '
    'nên chèn о vào giữa — <b>шу́ток</b> (không phải "шутк").</div>'
    '<div class="hd-warn">Hai cụm dùng liên tục: <b>в шу́тку</b> = đùa thôi, không thật · '
    '<b>кро́ме шу́ток</b> = nói nghiêm túc đấy.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>шути́ть</b> đùa · <b>шутли́вый</b> hay bỡn cợt · <b>шут</b> thằng hề</div>'
)
V["шутка"] = "câu nói đùa, trò đùa"

# ─────────────────────────────────────────────────────────── игра
S["игра"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">игр-</span>'
    '<span class="hd-gloss">gốc trơn: CHƠI (không chẻ nhỏ hơn được)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi danh từ giống CÁI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc игр- cho cả việc chơi lẫn việc diễn và việc chơi nhạc: '
    '<b>игра́ть в футбо́л</b> chơi bóng, <b>игра́ть на гита́ре</b> chơi đàn — một chữ, đổi giới từ '
    'là đổi nghĩa.</div>'
    '<div class="hd-warn">Trọng âm nhảy khi sang số nhiều: số ít bám đuôi (<b>игра́</b>, '
    '<b>игры́</b>), số nhiều lùi về gốc (<b>и́гры</b>, <b>и́грам</b>) — như trong '
    '<b>Олимпи́йские и́гры</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>игра́ть</b> chơi · <b>игро́к</b> người chơi · <b>игру́шка</b> đồ chơi</div>'
)

# ─────────────────────────────────────────────────────────── работа
S["работа"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раб-</span>'
    '<span class="hd-gloss">gốc <b>раб</b> — kẻ NÔ LỆ, việc nặng nhọc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-от(а)</span>'
    '<span class="hd-gloss">đuôi biến tính chất/việc thành danh từ (<b>доброта́</b>, <b>красота́</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc là "phận việc của kẻ tôi tớ" — từ nguyên, không suy ra được, '
    'nhưng nó nối luôn sang tiếng Đức <i>Arbeit</i> cùng một gốc. Trọng âm ở giữa, '
    '<b>рабо́та</b>, và đứng yên trong cả bảng chia.</div>'
    '<div class="hd-warn">Chỗ nơi làm việc dùng <b>на</b> chứ không dùng в: '
    '<b>на рабо́те</b> (đang ở chỗ làm) · <b>на рабо́ту</b> (đi tới chỗ làm).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рабо́тать</b> làm việc · <b>рабо́тник</b> người làm · '
    '<b>рабо́чий</b> công nhân, thuộc lao động · <b>безрабо́тица</b> nạn thất nghiệp</div>'
)
V['работа'] = 'công việc, việc làm, chỗ làm'

# ─────────────────────────────────────────────────────────── охота
S["охота"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">tiền tố mờ nghĩa, ở đây không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-хот-</span>'
    '<span class="hd-gloss">gốc <b>хоте́ть</b> — MUỐN, THÈM</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc là "sự thèm muốn", còn "đi săn" là lối nói tránh của thợ săn '
    'thời xưa — họ kiêng gọi thẳng tên việc săn, chỉ nói "cái sự ham" (từ nguyên, không suy ra '
    'được). Hai nghĩa cách nhau xa nhưng chung một chữ, cứ nhìn câu mà đoán.</div>'
    '<div class="hd-warn"><b>мне охо́та</b> + động từ nguyên thể = "tôi thèm/muốn làm gì" — lối nói '
    'thân mật thay cho <b>я хочу́</b>. Ngược lại <b>неохо́та</b> = ngại, không buồn làm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>хоте́ть</b> muốn · <b>охо́титься</b> đi săn · <b>охо́тник</b> thợ săn · '
    '<b>охо́тно</b> sẵn lòng</div>'
)
V['охота'] = 'việc đi săn, sự thèm muốn'

# ─────────────────────────────────────────────────────────── перерыв
S["перерыв"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span>'
    '<span class="hd-gloss">NGANG QUA, cắt đứt ở giữa chừng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ры́в</span>'
    '<span class="hd-gloss">gốc XÉ, ĐỨT (của <b>рвать</b> xé, <b>разры́в</b> vết đứt)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">"Chỗ mạch bị xé ngang" ⇒ quãng ngắt giữa chừng. Danh từ dựng bằng cách bỏ '
    'trần đuôi động từ cùng gốc, không thêm hậu tố nào — nên nó dừng ở phụ âm в.</div>'
    '<div class="hd-warn">Chữ hay gặp nhất ở cửa hàng Nga: <b>обе́денный переры́в</b> = nghỉ trưa. '
    'Thấy tấm biển <b>переры́в</b> nghĩa là đang đóng cửa nghỉ, chờ một lát.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рвать</b> xé · <b>прерыва́ть</b> ngắt lời · <b>разры́в</b> vết đứt, sự đổ vỡ · '
    '<b>непреры́вный</b> liên tục, không đứt quãng</div>'
)
V["перерыв"] = "giờ giải lao, quãng nghỉ giữa chừng"

# ─────────────────────────────────────────────────────────── рёв
S["рёв"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рёв</span>'
    '<span class="hd-gloss">chính gốc động từ <b>реве́ть</b>, bỏ trần đuôi làm danh từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc trơn bắt chước tiếng kêu, không chẻ nhỏ hơn được. Đáng để ý là chữ ё: '
    'trong tiếng Nga <b>ё</b> chỉ tồn tại khi nó MANG trọng âm — đẩy trọng âm xuống đuôi là nó '
    'thành е ngay, nên danh từ <b>рёв</b> nhưng động từ <b>реве́ть</b>.</div>'
    '<div class="hd-why">Nghĩa trải từ tiếng thú gầm, tiếng máy rú, tới tiếng người khóc gào — '
    'điểm chung là ÂM TO KÉO DÀI, không phải nội dung tiếng kêu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>реве́ть</b> gầm, gào khóc · <b>рёва</b> đứa hay khóc nhè</div>'
)

# ─────────────────────────────────────────────────────────── диалог
S["диалог"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">диа-</span>'
    '<span class="hd-gloss">QUA LẠI, xuyên giữa (Hy Lạp <i>dia-</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ло́г</span>'
    '<span class="hd-gloss">LỜI, lời nói (Hy Lạp <i>logos</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">"Lời đi qua lại" ⇒ cuộc đối thoại. Mảnh <b>-ло́г</b> luôn hút trọng âm về '
    'cuối từ, thấy ở cả <b>моноло́г</b> và <b>катало́г</b>.</div>'
    '<div class="hd-warn">Bẫy: <b>диа-</b> KHÔNG có nghĩa "hai" — cái nghĩa "hai" là ди-. '
    'Người ta tưởng thế vì hay đặt cạnh <b>моноло́г</b> (mono- = một mình).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>моноло́г</b> lời độc thoại · <b>ло́гика</b> logic · '
    '<b>катало́г</b> danh mục</div>'
)
V['диалог'] = 'cuộc đối thoại, lời đối đáp'

# ─────────────────────────────────────────────────────────── воскресение
S["воскресение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вос-</span>'
    '<span class="hd-gloss">tiền tố воз- LÊN, TRỞ LẠI (viết с trước phụ âm câm к)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-крес-</span>'
    '<span class="hd-gloss">gốc cổ: SỐNG DẬY, HỒI LẠI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">đuôi tạo danh từ chỉ SỰ VIỆC, luôn giống TRUNG</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">"Sự dựng dậy trở lại" ⇒ sự sống lại. Cứ thấy đuôi <b>-ение</b> là biết ngay '
    'hai điều: đây là danh từ chỉ việc, và nó giống trung.</div>'
    '<div class="hd-warn">Đổi mỗi đuôi là đổi hẳn nghĩa: <b>воскресе́нье</b> (-нье) = ngày CHỦ NHẬT, '
    'gọi thế vì đó là ngày Chúa sống lại. Cùng gốc, khác chữ, đừng lẫn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>воскре́снуть</b> sống lại · <b>воскреси́ть</b> làm cho sống lại · '
    '<b>воскресе́нье</b> chủ nhật</div>'
)
V["воскресение"] = "sự sống lại, sự phục sinh"

# ─────────────────────────────────────────────────────────── юридический
S["юридический"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">юр-</span>'
    '<span class="hd-gloss">LUẬT, quyền (La Tinh <i>ius / iuris</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ид-</span>'
    '<span class="hd-gloss">NÓI, phán (La Tinh <i>dicere</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ческий</span>'
    '<span class="hd-gloss">đuôi biến từ quốc tế thành tính từ; trọng âm luôn rơi vào chữ и của nó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">La Tinh <i>iuridicus</i> = "người nói lẽ luật", cùng ổ với tiếng Anh '
    '<i>juridical</i>, <i>jurisdiction</i>. Đuôi <b>-и́ческий</b> mở khoá cả một lớp: tiếng Anh tận '
    'cùng <i>-ical</i> thì tiếng Nga gần như luôn là -и́ческий.</div>'
    '<div class="hd-warn">Cụm phải thuộc: <b>юриди́ческое лицо́</b> = pháp nhân (một tổ chức), đối lại '
    'là <b>физи́ческое лицо́</b> = thể nhân (một con người).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>юри́ст</b> luật gia · <b>юриспруде́нция</b> luật học · '
    '<b>юриди́чески</b> về mặt pháp lý</div>'
)

# ─────────────────────────────────────────────────────────── другой
S["другой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">друг-</span>'
    '<span class="hd-gloss">vẫn là <b>друг</b>, nhưng theo nghĩa cổ: KẺ ĐI CÙNG, người thứ hai</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ có trọng âm rơi vào chính nó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Từ "người thứ hai trong cặp" trượt sang "cái thứ hai" rồi thành "cái kia, '
    'cái khác" — đây là từ nguyên chứ không phải luật suy ra được, nhưng nó buộc <b>друго́й</b> vào '
    'chung một tổ với <b>дру́жба</b> của lô này, nhớ một là ra hai.</div>'
    '<div class="hd-warn"><b>друго́й</b> = MỘT CÁI KHÁC thay cho cái này. Còn "khác nhau, không giống '
    'nhau" thì phải dùng <b>ра́зный</b>.</div>'
    '<div class="hd-warn">Dạng cổ còn đông cứng trong cụm <b>друг дру́га</b> = lẫn nhau (mảnh đầu '
    'không bao giờ đổi, chỉ mảnh sau chia theo cách).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>друг</b> bạn · <b>дру́жба</b> tình bạn · <b>по-друго́му</b> theo cách khác</div>'
)
V['другой'] = 'khác, cái khác, người khác, còn lại'
