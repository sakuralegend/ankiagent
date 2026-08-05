# -*- coding: utf-8 -*-
"""k02 — actions: 14 động từ thường ngày.

Trục của lô: TIỀN TỐ đổi kiểu hành động chứ không đổi gốc — по- (một lát rồi thôi)
· про- (hết một lượt) · вы- (làm cho xong, hút trọng âm) · со- (gộp lại) · в- (vào trong).
Ba từ cùng gốc -став- (вставить · поставить · составить) soạn cùng nhau cho khớp nhau.

Chuẩn v3: mỗi thẻ ≤ 700px (nhắm < 600), tối đa 2 ô đỏ, KHÔNG khối dùng chung.
Bảng chia do `congcu.py bang` tự nối lúc ghi — ở đây không chép dạng từ thành bảng.
"""

S = {}
V = {}

# ---------------------------------------------------------------- gốc -вет- (lời nói)
S["отвечать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">trở lại, đáp lại</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вет-</span>'
    '<span class="hd-gloss">LỜI NÓI (gốc cổ, không đứng một mình)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi động từ, chia đều</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nói <b>trở lại</b> phía người vừa hỏi → trả lời. Nhận ra gốc '
    '<b>-вет-</b> là mở được cả chùm từ quen: <b>приве́т</b> (lời gửi tới), '
    '<b>сове́т</b> (lời cùng bàn), <b>отве́т</b> (lời đáp).</div>'
    '<div class="hd-warn">Giới từ tách hẳn hai nghĩa: <b>отвеча́ть на вопро́с</b> '
    '(на + cách 4) = trả lời câu hỏi · <b>отвеча́ть за</b> + cách 4 = chịu trách '
    'nhiệm về.</div>'
    '<div class="hd-warn">Cặp thể: <b>отвеча́ть</b> đang trả lời / hay trả lời — '
    '<b>отве́тить</b> trả lời một lần rồi xong.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отве́т</b> câu trả lời · <b>отве́тственность</b> trách nhiệm · '
    '<b>приве́т</b> chào · <b>сове́т</b> lời khuyên, hội đồng</div>'
)
V['отвечать'] = 'trả lời, hồi đáp, chịu trách nhiệm'

# ---------------------------------------------------------------- gốc слух- (tai, sự nghe)
S["слушать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">слуш-</span>'
    '<span class="hd-gloss">← <b>слух</b> TAI, sự nghe</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">chia đều, trọng âm đứng yên ở <b>слу́-</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>слух</b> là cái tai → <b>слу́шать</b> là HƯỚNG tai về phía '
    'gì đó, tức nghe có chủ ý. Nghe cái gì thì để cách 4: <b>слу́шать му́зыку</b>.</div>'
    '<div class="hd-warn">Cặp phải phân biệt cả đời: <b>слу́шать</b> chủ ý lắng nghe — '
    '<b>слы́шать</b> âm tự lọt vào tai. Câu kinh điển: <b>Я слу́шал, но не слы́шал</b> '
    '= tôi lắng nghe mà không nghe ra gì.</div>'
    '<div class="hd-warn"><b>слу́шать кра́ем у́ха</b> = nghe bằng mép tai → nghe lơ là, '
    'nghe cho có.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>слух</b> thính giác; tin truyền miệng · <b>слу́шатель</b> '
    'người nghe · <b>послу́шный</b> biết vâng lời · <b>послу́шать</b> nghe một lát</div>'
)
V['слушать'] = 'nghe, lắng nghe'

S["прослушать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">xuyên suốt, từ đầu đến cuối</span></div>'
    '<div class="hd-row"><span class="hd-piece">-слуш-</span>'
    '<span class="hd-gloss">nghe (← <b>слух</b> tai)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiền tố <b>про-</b> là đi XUYÊN hết chiều dài của vật: '
    '<b>прочита́ть</b> đọc hết cuốn sách, <b>прослу́шать</b> nghe hết bài giảng, '
    'hết bản nhạc. Thân từ giữ nguyên <b>слу́шать</b>, chia đều.</div>'
    '<div class="hd-warn">Hai thể hoàn thành của <b>слу́шать</b>, khác nhau ở tiền tố: '
    '<b>послу́шать</b> nghe MỘT LÁT rồi thôi — <b>прослу́шать</b> nghe TRỌN từ đầu '
    'đến cuối.</div>'
    '<div class="hd-warn">Trong lời nói còn dùng theo nghĩa ngược: <b>Я прослу́шал</b> '
    'có thể là “tôi để lọt, không nghe ra” — cũng là <b>про-</b>, nhưng theo lối '
    '“để trượt mất”.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>слу́шать</b> nghe · <b>слух</b> thính giác · '
    '<b>слу́шатель</b> người nghe · <b>прочита́ть</b> đọc hết (cùng lối <b>про-</b>)</div>'
)
V['прослушать'] = 'nghe hết một lượt, nghe trọn'

# ---------------------------------------------------------------- gốc пе-/по- (hát)
S["петь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пе-</span>'
    '<span class="hd-gloss">HÁT — gốc một âm tiết, không chẻ thêm được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc trơn, nên chỗ đáng nhớ là nó đẻ ra những từ nào: '
    '<b>пе́сня</b> bài hát, và cả <b>пету́х</b> con gà trống — con vật “hát” báo sáng.</div>'
    '<div class="hd-warn">Từ này có HAI thân: nguyên thể và quá khứ giữ <b>пе-</b> '
    '(<b>петь</b>, <b>пел</b>), còn toàn bộ hiện tại đổi sang <b>по-</b>: <b>пою́</b>, '
    '<b>поёшь</b> … <b>пою́т</b>, mệnh lệnh <b>пой!</b> Không suy ra được, phải nhớ riêng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пе́сня</b> bài hát · <b>певе́ц</b> / <b>певи́ца</b> ca sĩ · '
    '<b>пе́ние</b> việc ca hát · <b>спеть</b> hát xong một bài</div>'
)
V['петь'] = 'hát, ca'

# ---------------------------------------------------------------- gốc -мотр- (nhìn)
S["смотреть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">ở từ này không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мотр-</span>'
    '<span class="hd-gloss">NHÌN, quan sát — chỉ sống khi có tiền tố</span></div>'
    '<div class="hd-row"><span class="hd-piece">-еть</span>'
    '<span class="hd-gloss">đuôi lớp chia 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>-мотр-</b> là chủ ý hướng mắt tới, và đổi tiền tố là đổi '
    'kiểu nhìn. Nhìn vào ai/cái gì: <b>смотре́ть на</b> + cách 4; nhưng xem phim, xem TV '
    'thì cách 4 trực tiếp, không giới từ.</div>'
    '<div class="hd-warn">Chủ ý hay không: <b>смотре́ть</b> bỏ mắt ra xem — '
    '<b>ви́деть</b> mắt bắt được, không cố ý.</div>'
    '<div class="hd-warn">“Mặc dù” là <b>несмотря́ на</b> + cách 4 — viết LIỀN; tách ra '
    '<b>не смотря́</b> thì chỉ còn nghĩa “không nhìn vào”.</div>'
    '<div class="hd-why">Bảng chia: trọng âm dịch — chỉ ngôi “tôi” <b>смотрю́</b> mang '
    'trọng âm ở đuôi, năm ngôi còn lại kéo về gốc: <b>смо́тришь</b> … <b>смо́трят</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>осмотре́ть</b> khám, xem khắp · <b>рассмотре́ть</b> xem xét '
    'kỹ · <b>осмо́тр</b> cuộc khám · <b>посмотре́ть</b> xem một lát</div>'
)
V['смотреть'] = 'nhìn, xem, ngắm'

S["посмотреть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">một lần, một lát rồi xong</span></div>'
    '<div class="hd-row"><span class="hd-piece">-смотр-</span>'
    '<span class="hd-gloss">NHÌN, quan sát</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>по-</b> biến “đang xem” thành “xem một cái rồi xong”: '
    '<b>посмотре́ть фильм</b> xem xong bộ phim, <b>посмотри́!</b> nhìn xem này! Cùng lối '
    'đó: <b>послу́шать</b> nghe một lát, <b>поговори́ть</b> nói chuyện một hồi.</div>'
    '<div class="hd-warn"><b>Мы посмо́трим</b> = “để rồi xem” — câu hoãn quyết định, '
    'không nói về việc xem thật.</div>'
    '<div class="hd-why">Bảng chia: trọng âm dịch y như <b>смотре́ть</b> — '
    '<b>посмотрю́</b> ở đuôi, năm ngôi còn lại về gốc <b>посмо́-</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>смотре́ть</b> nhìn, xem (chưa xong) · <b>рассмотре́ть</b> '
    'xem xét kỹ · <b>осмотре́ть</b> khám, xem khắp</div>'
)
V['посмотреть'] = 'xem, nhìn thử'

# ---------------------------------------------------------------- gốc хот-/хоч- (muốn)
S["хотеть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">хот- / хоч-</span>'
    '<span class="hd-gloss">MUỐN — gốc trơn, không chẻ thêm được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-еть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không chẻ được, nên cái phải nhớ là nó đòi gì: <b>хоте́ть</b> + '
    'cách 4 (<b>хочу́ ко́фе</b>), hoặc + động từ nguyên thể (<b>хочу́ спать</b>), hoặc '
    '+ <b>что́бы</b> khi muốn NGƯỜI KHÁC làm.</div>'
    '<div class="hd-warn">Bảng chia lệch, hai nửa theo hai lớp khác nhau: ba ngôi số ít '
    'đổi <b>т→ч</b> và chia như lớp 1 — <b>хочу́</b>, <b>хо́чешь</b>, <b>хо́чет</b>; ba '
    'ngôi số nhiều giữ <b>т</b>, chia như lớp 2, trọng âm ở đuôi — <b>хоти́м</b>, '
    '<b>хоти́те</b>, <b>хотя́т</b>. Dạng mệnh lệnh trong bảng gần như không ai dùng.</div>'
    '<div class="hd-warn"><b>хоте́л бы</b> = “tôi muốn…” nói lịch sự, mềm hơn '
    '<b>хочу́</b> (đúng vai <i>would like</i>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>охо́та</b> sự ham muốn (nay còn nghĩa đi săn) · '
    '<b>охо́тно</b> sẵn lòng · <b>захоте́ть</b> chợt muốn · <b>хоте́ться</b>: '
    '<b>мне хо́чется</b> tôi thấy muốn</div>'
)
V['хотеть'] = 'muốn, thích, định'

# ---------------------------------------------------------------- gốc би-/бь- (giáng, đánh)
S["бить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">би- / бь-</span>'
    '<span class="hd-gloss">GIÁNG XUỐNG, đánh — gốc trơn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc là “giáng xuống”, nên nó dùng cả cho đồng hồ điểm giờ: '
    '<b>часы́ бьют</b>. Đánh ai, đánh cái gì thì để cách 4.</div>'
    '<div class="hd-warn">Nguyên thể có <b>и</b>, hiện tại thì không: <b>и</b> rút thành '
    '<b>ь</b> — <b>бью</b>, <b>бьёшь</b>, <b>бьёт</b> … <b>бьют</b>, mệnh lệnh '
    '<b>бей!</b> Xem bảng đừng tìm chữ <b>и</b>, nó không còn ở đó.</div>'
    '<div class="hd-warn"><b>бить</b> là một bên đánh bên kia; còn “đánh nhau” (hai bên) '
    'là từ khác: <b>дра́ться</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уби́ть</b> giết (đánh cho mất mạng) · <b>разби́ть</b> đập vỡ · '
    '<b>поби́ть</b> đánh cho một trận · <b>би́тва</b> trận đánh · <b>бой</b> cuộc chiến</div>'
)
V['бить'] = 'đánh, đập, gõ, giáng'

# ------------------------------------------- gốc -став- (làm cho đứng) — ba tiền tố khác nhau
S["вставить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO TRONG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-став-</span>'
    '<span class="hd-gloss">làm cho ĐỨNG, đặt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>-став-</b> là “làm cho đứng”, họ với <b>стоя́ть</b> (đứng). '
    'Cộng <b>в-</b> vào trong: đặt vật vào bên trong cái khác → <b>вста́вить ключ</b> cắm '
    'chìa khoá, <b>вста́вить сло́во</b> chen vào một câu.</div>'
    '<div class="hd-warn">Chỉ ngôi “tôi” chèn thêm <b>л</b>: <b>я вста́влю</b>. Đây là luật '
    'chung cho động từ <b>-ить</b> có thân kết thúc bằng <b>б п в м ф</b> '
    '(<b>люби́ть → люблю́</b>); năm ngôi còn lại đều đặn <b>вста́вишь</b> … '
    '<b>вста́вят</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вставля́ть</b> đang chèn vào · <b>вста́вка</b> phần chèn thêm · '
    '<b>ста́вить</b> đặt, dựng · <b>стоя́ть</b> đứng</div>'
)
V['вставить'] = 'cắm vào, chèn vào, nhét vào'

S["поставить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">một lần cho xong</span></div>'
    '<div class="hd-row"><span class="hd-piece">-став-</span>'
    '<span class="hd-gloss">làm cho ĐỨNG, đặt</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đặt sao cho vật ĐỨNG lên (chai, cốc, sách dựng). Nơi đặt trả lời '
    'câu hỏi <b>куда́</b> (đến đâu), nên sau <b>на</b> / <b>в</b> phải dùng cách 4, '
    'không phải cách 6.</div>'
    '<div class="hd-warn">Cặp đối phải thuộc: <b>поста́вить</b> đặt cho ĐỨNG (họ với '
    '<b>стоя́ть</b>) — <b>положи́ть</b> đặt cho NẰM (họ với <b>лежа́ть</b>). Tiếng Việt '
    'cùng là “đặt”, tiếng Nga bắt phải chọn.</div>'
    '<div class="hd-warn">Bảng chia: vẫn luật <b>л</b> ở ngôi “tôi” — <b>я поста́влю</b>, '
    'các ngôi khác đều đặn <b>поста́вишь</b> … <b>поста́вят</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ста́вить</b> đang đặt · <b>поставля́ть</b> cung cấp · '
    '<b>вста́вить</b> chèn vào · <b>соста́вить</b> lập ra</div>'
)
V['поставить'] = 'đặt đứng, dựng lên, để vào'

S["составить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG, gộp lại với nhau</span></div>'
    '<div class="hd-row"><span class="hd-piece">-став-</span>'
    '<span class="hd-gloss">làm cho ĐỨNG, đặt</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đặt các phần LẠI VỚI NHAU → lập ra, soạn: <b>соста́вить план</b>, '
    '<b>соста́вить спи́сок</b>. Cũng tiền tố <b>со-</b> gộp lại: <b>сове́т</b> (cùng bàn '
    'lời), <b>соста́в</b> (thứ do các phần gộp thành).</div>'
    '<div class="hd-warn">Nghĩa thứ hai gặp đầy trên báo: “lên tới, chiếm” một con số — '
    '<b>Цена́ соста́вила 100 рубле́й</b> giá lên tới 100 rúp.</div>'
    '<div class="hd-warn">Bảng chia: vẫn <b>л</b> ở ngôi “tôi” — <b>я соста́влю</b>, '
    'còn lại <b>соста́вишь</b> … <b>соста́вят</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>соста́в</b> thành phần, đội hình · <b>составля́ть</b> đang lập; '
    'chiếm (con số) · <b>ста́вить</b> đặt · <b>вста́вить</b> chèn vào</div>'
)
V['составить'] = 'lập ra, soạn thảo, gộp thành, lên tới'

# ---------------------------------------------------------------- gốc -полн- (đầy)
S["выполнить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">ra — ở đây: cho tới HẾT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-полн-</span>'
    '<span class="hd-gloss">← <b>по́лный</b> ĐẦY</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là “làm cho đầy ra hết” → làm trọn cái đã nhận: '
    '<b>вы́полнить план</b>, <b>вы́полнить обеща́ние</b> giữ trọn lời hứa.</div>'
    '<div class="hd-warn">Ở động từ thể hoàn thành, tiền tố <b>вы-</b> HÚT trọng âm về '
    'mình và giữ suốt bảng chia: <b>вы́полнить</b>, <b>вы́полню</b> … <b>вы́полнят</b>. '
    'Sang thể chưa hoàn thành thì trọng âm rời <b>вы-</b>: <b>выполня́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́лный</b> đầy · <b>по́лностью</b> hoàn toàn · '
    '<b>выполня́ть</b> đang thực hiện · <b>выполне́ние</b> việc thực hiện</div>'
)
V['выполнить'] = 'thực hiện, hoàn thành'

# ---------------------------------------------------------------- gốc говор- (lời nói)
S["говорить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">говор-</span>'
    '<span class="hd-gloss">LỜI NÓI, tiếng nói</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">lớp chia 2, trọng âm luôn ở đuôi</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhớ gốc <b>говор-</b> là đọc ra được cả nhóm: <b>разгово́р</b> '
    'cuộc trò chuyện, <b>догово́р</b> hợp đồng (lời đã thoả), <b>погово́рка</b> câu tục '
    'ngữ. Trọng âm không dịch: <b>говорю́</b>, <b>говори́шь</b> … <b>говоря́т</b>.</div>'
    '<div class="hd-warn">Từ này có HAI thể hoàn thành, nghĩa khác hẳn nhau: '
    '<b>сказа́ть</b> nói RA một câu — <b>поговори́ть</b> trò chuyện một hồi.</div>'
    '<div class="hd-warn">Nói VỚI ai: <b>с</b> + cách 5 · nói VỀ cái gì: <b>о</b> + '
    'cách 6 · còn “nói tiếng Nga” là <b>говори́ть по-ру́сски</b>, không thêm giới từ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>разгово́р</b> cuộc trò chuyện · <b>разгова́ривать</b> trò '
    'chuyện · <b>догово́р</b> hợp đồng · <b>погово́рка</b> câu tục ngữ</div>'
)
V['говорить'] = 'nói, trò chuyện, nói được'

S["поговорить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">một lúc rồi thôi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-говор-</span>'
    '<span class="hd-gloss">LỜI NÓI, tiếng nói</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gắn <b>по-</b> vào một động từ chỉ hoạt động là “làm việc đó một '
    'lát”: <b>послу́шать</b> nghe một lát, <b>посмотре́ть</b> xem một lát. Nên '
    '<b>поговори́ть</b> không phải “nói xong điều gì” mà là “trò chuyện xong một buổi”.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>сказа́ть</b>: <b>сказа́ть</b> là nói ra NỘI DUNG '
    '(<b>сказа́ть пра́вду</b> nói ra sự thật), còn <b>поговори́ть</b> là trò chuyện VỚI '
    'ai — <b>поговори́ть с</b> + cách 5.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>говори́ть</b> nói, trò chuyện · <b>разгово́р</b> cuộc trò '
    'chuyện · <b>договори́ться</b> thoả thuận xong · <b>погово́рка</b> câu tục ngữ</div>'
)
V['поговорить'] = 'nói chuyện một lúc, trò chuyện một hồi'
