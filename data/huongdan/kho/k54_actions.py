# -*- coding: utf-8 -*-
"""k54 — actions: 19 động từ việc-thường-ngày.

Trục của lô: mỗi động từ được nhớ qua CÁI DANH TỪ hoặc CÁI GỐC nằm sẵn trong nó
(за́втрак → за́втракать, звон → звони́ть, второ́й → повторя́ть), rồi mới tới chỗ
riêng của nó: cặp thể, cách mà nó đòi, và chỗ bảng chia lệch quy tắc.

🔴 KHÔNG dựng biến khối dùng chung rồi cộng vào mọi thẻ — README §3.
Luật -ова́ть/-ева́ть → -у́ю trải đủ ở ĐÚNG một thẻ (рисова́ть); танцева́ть và
целова́ть chỉ nhắc dạng của chính nó.
"""

S = {}
V = {}

S["видеть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вид-</span>'
    '<span class="hd-gloss">THẤY — cái nhìn, vẻ ngoài</span></div>'
    '<div class="hd-row"><span class="hd-piece">-еть</span>'
    '<span class="hd-gloss">đuôi động từ, lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>вид-</b> là "mắt bắt được": <b>вид</b> cảnh, vẻ ngoài; '
    '<b>очеви́дно</b> rành rành trước mắt. Nên <b>ви́деть</b> là mắt nhận ra, không cần cố ý — '
    'còn chủ động hướng mắt vào cái gì là <b>смотре́ть</b>. Thể hoàn thành: <b>уви́деть</b>.</div>'
    '<div class="hd-warn">Bảng chia chỉ lệch ở ngôi "tôi": <b>д</b> hoá <b>ж</b> — '
    '<b>я ви́жу</b>. Từ <b>ты ви́дишь</b> trở đi <b>д</b> quay lại nguyên chỗ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вид</b> vẻ, cảnh · <b>свида́ние</b> cuộc hẹn · '
    '<b>телеви́дение</b> truyền hình · <b>уви́деть</b> thấy được</div>'
)

S["гулять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гуля-</span>'
    '<span class="hd-gloss">rong chơi, ra ngoài cho thoáng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>гуля́ть</b> là đi mà KHÔNG nhắm tới đâu, ra ngoài cho thoáng; đi tới '
    'một đích mới là <b>идти́</b>. Cùng gốc có <b>прогу́лка</b> cuộc dạo và <b>прогу́л</b> buổi '
    'trốn học — trốn học chính là đi chơi thay vì đến lớp.</div>'
    '<div class="hd-warn">Dạo QUANH đâu thì <b>по</b> + cách 3: <b>гуля́ть по па́рку</b>. '
    'Dạo VỚI ai thì <b>с</b> + cách 5: <b>гуля́ть с соба́кой</b> (dắt chó đi dạo).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прогу́лка</b> cuộc đi dạo · <b>прогу́л</b> buổi trốn việc · '
    '<b>погуля́ть</b> đi dạo một lát (hoàn thành)</div>'
)

S["думать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дум-</span>'
    '<span class="hd-gloss">Ý NGHĨ, sự suy tính</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ nhất</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Có sẵn danh từ <b>ду́ма</b> "ý nghĩ", thêm đuôi là thành "làm việc '
    'nghĩ"; trọng âm đứng yên ở <b>ду́-</b> suốt bảng chia. Thể hoàn thành <b>поду́мать</b> là '
    'nghĩ một lúc rồi thôi, còn "nghĩ RA được" lại là <b>приду́мать</b>.</div>'
    '<div class="hd-warn">Nghĩ VỀ cái gì thì <b>о</b> + cách 6: <b>ду́мать о рабо́те</b>. '
    'Nghĩ rằng… thì <b>ду́мать, что…</b>, tiếng Nga luôn có dấu phẩy trước <b>что</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ду́ма</b> ý nghĩ · <b>приду́мать</b> nghĩ ra · '
    '<b>заду́мчивый</b> đăm chiêu · <b>поду́мать</b> nghĩ một lát</div>'
)

S["жить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">жи-</span>'
    '<span class="hd-gloss">SỐNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một gốc <b>жи-</b> ngắn nuôi cả họ: <b>жизнь</b> cuộc sống, '
    '<b>живо́й</b> còn sống, <b>жи́тель</b> cư dân. Nguyên thể trông trơn tru, nhưng thân hiện '
    'tại mọc thêm một chữ <b>в</b> không báo trước.</div>'
    '<div class="hd-warn">Bảng chia phải nhớ RIÊNG: thân hiện tại là <b>жив-</b> — '
    '<b>я живу́</b>, <b>ты живёшь</b>. Quá khứ giống cái dồn trọng âm ra cuối: '
    '<b>он жил</b> nhưng <b>она́ жила́</b>.</div>'
    '<div class="hd-warn">Sống Ở ĐÂU thì <b>в</b>/<b>на</b> + cách 6: <b>я живу́ в Москве́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жизнь</b> cuộc sống · <b>живо́й</b> sống, sinh động · '
    '<b>жи́тель</b> cư dân · <b>живо́тное</b> động vật</div>'
)

S["завтракать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">завтрак-</span>'
    '<span class="hd-gloss">BỮA SÁNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi "dùng bữa đó"</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không phải nhớ thêm gì: tên bữa <b>за́втрак</b> gắn thẳng <b>-ать</b> '
    'là ra động từ, trọng âm bám chặt <b>за́-</b> ở mọi ngôi lẫn quá khứ. Ăn xong bữa sáng '
    '(một lần cụ thể) là <b>поза́втракать</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: <b>за́втрак</b> và <b>за́втра</b> (ngày mai) cùng gốc '
    '<b>у́тро</b> "buổi sáng" — đây là từ nguyên, không phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>за́втрак</b> bữa sáng · <b>поза́втракать</b> ăn xong bữa sáng · '
    '<b>за́втра</b> ngày mai</div>'
)

S["звонить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">звон-</span>'
    '<span class="hd-gloss">TIẾNG CHUÔNG, tiếng ngân</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>звон</b> là tiếng chuông ngân, nên gọi điện chính là làm chuông nhà '
    'người ta reo lên. Danh từ <b>звоно́к</b> vì thế mang cả hai nghĩa: cái chuông và cuộc gọi. '
    'Gọi một cuộc, gọi xong: <b>позвони́ть</b>.</div>'
    '<div class="hd-warn">Trọng âm ở ĐUÔI suốt bảng chia, không bao giờ lùi về gốc: '
    '<b>она́ звони́т</b>, <b>они́ звоня́т</b>. Chính người Nga cũng hay nói sai chỗ này.</div>'
    '<div class="hd-warn">Gọi CHO AI thì cách 3, không giới từ: <b>звони́ть ма́ме</b>, '
    '<b>звони́ть врачу́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>звоно́к</b> cuộc gọi; chuông · <b>звон</b> tiếng chuông · '
    '<b>позвони́ть</b> gọi một cuộc (hoàn thành)</div>'
)

S["играть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">игр-</span>'
    '<span class="hd-gloss">TRÒ CHƠI, cuộc chơi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ nhất</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ <b>игра́</b> "trò chơi" có trước, động từ mọc ra từ đó. Bảng '
    'chia đều tay, không bẫy gì; chỗ phải học là GIỚI TỪ, vì nó mới quyết định "chơi" ở đây là '
    'chơi cái gì.</div>'
    '<div class="hd-warn">Chơi TRÒ hay MÔN nào: <b>в</b> + cách 4 — <b>игра́ть в футбо́л</b>. '
    'Chơi NHẠC CỤ nào: <b>на</b> + cách 6 — <b>игра́ть на гита́ре</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>игра́</b> trò chơi · <b>игру́шка</b> đồ chơi · '
    '<b>игро́к</b> người chơi · <b>сыгра́ть</b> chơi xong một ván (hoàn thành)</div>'
)

S["обедать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">tiền tố (bao quanh, làm trọn)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ед-</span>'
    '<span class="hd-gloss">ĂN — cùng gốc với есть</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi "dùng bữa đó"</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chẻ ra là thấy chữ ăn nằm giữa: <b>обе́д</b> "bữa trưa" giấu gốc '
    '<b>-ед-</b> của <b>есть</b> ăn và <b>еда́</b> thức ăn. Có <b>обе́д</b> rồi thì '
    '<b>обе́дать</b> chỉ là "dùng bữa đó"; ăn trưa xong là <b>пообе́дать</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: chẻ <b>об-</b> + <b>-ед-</b> là từ nguyên, không phải luật '
    'suy ra được. Chắc chắn thì cứ nhớ cặp <b>обе́д</b> ↔ <b>обе́дать</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обе́д</b> bữa trưa · <b>обе́денный</b> thuộc bữa trưa · '
    '<b>еда́</b> thức ăn · <b>пообе́дать</b> ăn xong bữa trưa</div>'
)

S["повторять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố (làm một lượt)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-втор-</span>'
    '<span class="hd-gloss">THỨ HAI — второ́й</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ять</span>'
    '<span class="hd-gloss">đuôi động từ chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen hiện ngay khi chẻ: "làm lần THỨ HAI". Cùng gốc <b>второ́й</b> '
    'còn có <b>вто́рник</b> — ngày thứ hai của tuần Nga. Ôn bài cũng là làm lại lần nữa, nên '
    'từ này gánh luôn nghĩa "ôn tập".</div>'
    '<div class="hd-warn">Cặp thể: <b>повторя́ть</b> lặp nhiều lần, đang lặp — '
    '<b>повтори́ть</b> nhắc lại MỘT lần rồi thôi. Câu phải thuộc: '
    '<b>Повтори́те, пожа́луйста</b> = Xin nhắc lại.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>второ́й</b> thứ hai · <b>вто́рник</b> thứ Ba · '
    '<b>повторе́ние</b> sự lặp lại, ôn tập · <b>повтори́ть</b> nhắc lại một lần</div>'
)

S["понимать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố (làm trọn một lượt)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ним-</span>'
    '<span class="hd-gloss">NẮM, cầm lấy — gốc của приня́ть</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi động từ chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là "nắm được" ý người ta — cùng hình ảnh với '
    '<b>to grasp</b> trong tiếng Anh. Gốc <b>-ним-/-ня-</b> "cầm lấy" này còn cho '
    '<b>приня́ть</b> nhận lấy và <b>поня́тие</b> khái niệm.</div>'
    '<div class="hd-warn">Thể hoàn thành đổi hẳn mặt chữ, phải nhớ riêng: <b>поня́ть</b> — '
    '<b>я пойму́</b>, <b>он по́нял</b>, <b>она́ поняла́</b> (trọng âm chạy ra cuối ở giống cái).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поня́ть</b> hiểu ra (hoàn thành) · <b>поня́тно</b> đã rõ · '
    '<b>поня́тие</b> khái niệm · <b>приня́ть</b> nhận, tiếp nhận</div>'
)

S["проверять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">xuyên suốt, làm hết một lượt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вер-</span>'
    '<span class="hd-gloss">TIN — ве́ра niềm tin</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ять</span>'
    '<span class="hd-gloss">đuôi động từ chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: soi hết một lượt cho tới khi TIN được. Cùng gốc có '
    '<b>ве́ра</b> niềm tin và <b>ве́рный</b> "đúng, chuẩn" — kiểm tra tức là xem cái đó có '
    '<b>ве́рный</b> hay không.</div>'
    '<div class="hd-warn">Cặp thể: <b>проверя́ть</b> đang kiểm, thường kiểm — '
    '<b>прове́рить</b> kiểm xong một lần. Chú ý trọng âm nhảy chỗ giữa hai thể.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ве́ра</b> niềm tin · <b>ве́рить</b> tin · '
    '<b>ве́рный</b> đúng; trung thành · <b>прове́рка</b> cuộc kiểm tra</div>'
)

S["рисовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рис-</span>'
    '<span class="hd-gloss">NÉT VẼ, hình vẽ (gốc mượn)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-</span>'
    '<span class="hd-gloss">khuôn Nga hoá động từ mượn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thấy đuôi <b>-ова́ть</b> là biết ngay hai điều: gốc từ nước ngoài vào, '
    'và bảng chia sẽ rụng mất khúc <b>-ов-</b>. Vẽ xong một bức là <b>нарисова́ть</b>.</div>'
    '<div class="hd-warn">Luật của cả lớp <b>-ова́ть/-ева́ть</b>: hiện tại RỤNG <b>-ов-/-ев-</b>, '
    'thay bằng <b>-у-</b> — <b>я рису́ю</b>, <b>ты рису́ешь</b>. Cùng lô có '
    '<b>танцева́ть → танцу́ю</b>, <b>целова́ть → целу́ю</b>.</div>'
    '<div class="hd-warn"><b>рис</b> (gạo) chỉ trùng mặt chữ, KHÔNG cùng gốc với '
    '<b>рисова́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рису́нок</b> bức vẽ, hình vẽ · '
    '<b>нарисова́ть</b> vẽ xong (hoàn thành)</div>'
)

S["сказать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">gom lại, làm xong một lần</span></div>'
    '<div class="hd-row"><span class="hd-piece">-каз-</span>'
    '<span class="hd-gloss">NÓI RA, chỉ ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc <b>-каз-</b> "nói ra, chỉ ra" đông con cháu nhất tiếng Nga: '
    '<b>ска́зка</b> chuyện kể, <b>расска́з</b> truyện, <b>прика́з</b> mệnh lệnh. Tiền tố '
    '<b>с-</b> đóng hành động lại thành một câu nói đã xong.</div>'
    '<div class="hd-warn">Bảng chia lệch hai chỗ cùng lúc: <b>з</b> hoá <b>ж</b> ở mọi ngôi, và '
    'trọng âm lùi về gốc từ ngôi thứ hai — <b>я скажу́</b> nhưng <b>ты ска́жешь</b>, '
    '<b>они́ ска́жут</b>.</div>'
    '<div class="hd-warn">Câu phải thuộc: <b>Скажи́те, пожа́луйста…</b> = Làm ơn cho hỏi…</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ска́зка</b> truyện cổ tích · <b>расска́з</b> truyện kể · '
    '<b>прика́з</b> mệnh lệnh · <b>показа́ть</b> chỉ cho xem</div>'
)

S["спросить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">làm xong một lần</span></div>'
    '<div class="hd-row"><span class="hd-piece">-прос-</span>'
    '<span class="hd-gloss">HỎI, thỉnh cầu — вопро́с</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc với <b>вопро́с</b> câu hỏi và <b>про́сьба</b> lời thỉnh cầu — '
    'chẻ ra là nhận ngay chữ "hỏi" nằm giữa. Bản chưa hoàn thành đổi mặt chữ khá nhiều: '
    '<b>спра́шивать</b>.</div>'
    '<div class="hd-warn">Bảng chia: riêng ngôi "tôi" đổi <b>с</b> thành <b>ш</b> — '
    '<b>я спрошу́</b>; các ngôi sau trở lại <b>с</b> và trọng âm lùi về gốc: '
    '<b>ты спро́сишь</b>.</div>'
    '<div class="hd-warn"><b>спроси́ть</b> là hỏi để BIẾT — <b>спроси́ть у ма́мы</b> (cách 2). '
    'Còn nhờ vả, xin xỏ lại là <b>проси́ть</b>: cùng gốc mà khác hẳn việc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вопро́с</b> câu hỏi · <b>про́сьба</b> lời thỉnh cầu · '
    '<b>проси́ть</b> xin, nhờ · <b>спра́шивать</b> hỏi (chưa hoàn thành)</div>'
)

S["спрягаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">gắn vào nhau</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пряг-</span>'
    '<span class="hd-gloss">BUỘC ÁCH, thắng ngựa vào xe</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">tự nó / bị động</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen: "được buộc vào nhau" — chia động từ đúng là buộc cái đuôi '
    'vào cái thân. Danh từ là <b>спряже́ние</b> phép chia động từ — <b>г</b> hoá <b>ж</b> khi '
    'thêm đuôi <b>-ение</b>. Có <b>-ся</b> nên từ này hầu như chỉ gặp ở dạng bị động.</div>'
    '<div class="hd-warn">Cặp thuật ngữ đừng đổi chỗ: động từ thì <b>спряга́ется</b> (chia theo '
    'ngôi), còn danh từ và tính từ thì <b>склоня́ется</b> (biến cách).</div>'
    '<div class="hd-warn">⚠️ Mức tin: gốc <b>-пряг-</b> "buộc ách" là từ nguyên, không phải luật '
    'suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>спряже́ние</b> phép chia động từ · <b>упря́жка</b> bộ yên cương · '
    '<b>запряга́ть</b> thắng ngựa vào xe</div>'
)

S["танцевать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">танц-</span>'
    '<span class="hd-gloss">← та́нец, điệu nhảy</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ева-</span>'
    '<span class="hd-gloss">khuôn động từ hoá (bản mềm của -ова-)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ <b>та́нец</b> (mượn từ tiếng Đức <b>Tanz</b>) có trước. Chữ '
    '<b>е</b> trong <b>та́нец</b> là nguyên âm CHẠY: vừa thêm đuôi vào là nó biến mất. Nhảy một '
    'lúc cho vui là <b>потанцева́ть</b>.</div>'
    '<div class="hd-warn">Hai chỗ rụng cùng lúc: nguyên âm chạy làm mất <b>е</b> của '
    '<b>та́нец</b>, rồi khuôn <b>-ева́ть</b> lại rụng tiếp ở hiện tại — <b>я танцу́ю</b>.</div>'
    '<div class="hd-warn"><b>танцева́ть</b> là nhảy có bài bản, có bước. Nhảy nhót tự do kiểu '
    'dân gian tiếng Nga gọi bằng từ khác: <b>пляса́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>та́нец</b> điệu nhảy · <b>танцо́р</b> vũ công · '
    '<b>танцева́льный</b> thuộc khiêu vũ</div>'
)

S["ужинать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ужин-</span>'
    '<span class="hd-gloss">BỮA TỐI</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ать</span>'
    '<span class="hd-gloss">đuôi "dùng bữa đó"</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đúng khuôn của bữa ăn: có <b>у́жин</b> rồi thì <b>у́жинать</b> chỉ là '
    '"dùng bữa đó". Trọng âm dính chặt <b>у́-</b> ở mọi ngôi và cả quá khứ, không bao giờ nhảy '
    'ra đuôi.</div>'
    '<div class="hd-warn">Ăn xong một bữa tối cụ thể thì dùng thể hoàn thành: '
    '<b>Мы поу́жинали</b> = Chúng tôi đã ăn tối xong.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>у́жин</b> bữa tối · <b>поу́жинать</b> ăn xong bữa tối '
    '(hoàn thành)</div>'
)

S["учиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">уч-</span>'
    '<span class="hd-gloss">DẠY / HỌC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">← себя́: chính mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>учи́ть</b> là "dạy ai" hoặc "học thuộc cái gì"; gắn <b>-ся</b> vào '
    'thành "dạy chính mình" = đi học, theo học. Cùng gốc là cả nhà trường: <b>учи́тель</b>, '
    '<b>учени́к</b>, <b>учёба</b>.</div>'
    '<div class="hd-warn">Trọng âm chỉ ra đuôi ở ngôi "tôi" — <b>я учу́сь</b>; từ '
    '<b>ты у́чишься</b> trở đi nó lùi hẳn về gốc <b>у́-</b>.</div>'
    '<div class="hd-warn">Học Ở ĐÂU: cách 6 — <b>учи́ться в шко́ле</b>. Học MÔN gì: cách 3 — '
    '<b>учи́ться ру́сскому языку́</b>. Còn học thuộc cái gì thì phải dùng <b>учи́ть</b> + '
    'cách 4.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>учи́тель</b> thầy giáo · <b>учени́к</b> học trò · '
    '<b>учёба</b> việc học · <b>нау́ка</b> khoa học</div>'
)

S["целовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">цел-</span>'
    '<span class="hd-gloss">NGUYÊN VẸN, lành lặn — це́лый</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-</span>'
    '<span class="hd-gloss">khuôn động từ hoá</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen là "chúc cho lành lặn": nụ hôn vốn là lời chúc sức khoẻ, đúng '
    'đường đi của <b>whole → hale</b> trong tiếng Anh. Chia theo khuôn <b>-ова́ть</b>: '
    '<b>я целу́ю</b>. Hôn một cái là <b>поцелова́ть</b>.</div>'
    '<div class="hd-warn"><b>цель</b> (mục tiêu) chỉ NHÌN giống chứ không cùng gốc với '
    '<b>целова́ть</b> — đừng nối hai từ này với nhau.</div>'
    '<div class="hd-warn">⚠️ Mức tin: nối <b>целова́ть</b> với <b>це́лый</b> là từ nguyên, không '
    'phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>це́лый</b> nguyên vẹn, cả · <b>поцелу́й</b> nụ hôn · '
    '<b>поцелова́ть</b> hôn một cái (hoàn thành)</div>'
)


# ---------------------------------------------------------------------------
# V — ĐỀ BÀI của deck 1-go (README §2c). User đọc dòng này rồi GÕ từ Nga, nên
# nó phải sát tới mức chỉ còn MỘT đáp án đúng.
#
# 🔴 Đã kiểm bằng `notesInfo` chứ không đoán: cả 19 note đều CÓ sẵn `AspectBadge`
# in ở MẶT ĐỀ BÀI (`IMPF` cho 17 từ, `PERF` cho сказа́ть và спроси́ть), và
# учи́ться · спряга́ться còn có `ReflexiveBadge`. Nên ở đây KHÔNG chép lại nhãn
# "hoàn thành / chưa hoàn thành" — đó đúng là thứ user đang nhìn thấy. Chỗ nào
# thể thật sự đổi NGHĨA VIỆT thì diễn bằng lời ("một lần rồi xong", "đang/thường")
# để đề bài vẫn chỉ có một đáp án. Xem báo cáo cuối lô.
#
# Chỉ liệt từ CẦN SỬA; những từ mà dòng cũ đã sát (за́втракать "ăn sáng",
# целова́ть "hôn"…) thì để nguyên.
# ---------------------------------------------------------------------------

V["думать"] = "nghĩ, suy nghĩ về điều gì"
V["звонить"] = "gọi điện thoại cho ai"
V['повторять'] = 'lặp lại, nhắc lại, ôn lại'
V['понимать'] = 'hiểu, nhận ra'
V['проверять'] = 'kiểm tra, rà soát, thử'
V['рисовать'] = 'vẽ, phác hoạ'
V['сказать'] = 'nói, bảo, kể'
V['спросить'] = 'hỏi, hỏi thăm'
V['спрягаться'] = 'được chia theo ngôi'
V['танцевать'] = 'nhảy, khiêu vũ, múa'
V['учиться'] = 'học, theo học'
