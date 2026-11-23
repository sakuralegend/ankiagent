# -*- coding: utf-8 -*-
"""k210 — concepts::state: từ của toà án, bầu cử, chiến tranh và suy nghĩ; trục là GỐC.

Chỗ cần nhất quán trong lô:
(1) избирать-/разобрать: -бир-/-бр-/-бер- gốc LẤY — khớp выбирать k94, разобраться k159 (разо- TÁCH RA).
(2) завоевать/завоёвывать: во- gốc CHIẾN — khớp воевать k138.
(3) осудить/осуждать/рассуждать: суд- XÉT, д → жд — khớp судить k167, обсуждать k124.
(4) противоречие: реч- NÓI (к → ч) — khớp речь k06; противо- — khớp противоположный k197.
(5) беженец: беж-/бег- CHẠY — khớp бежать k94.
(6) расследовать: след- DẤU VẾT — khớp следить k171, исследовать k141.
(7) передумать: дум- Ý NGHĨ — khớp думать k54. (8) угад-: гад- ĐOÁN — khớp загадка k134, догадаться k188.
(9) намерен — khớp намерение k170. (10) планировать — khớp план k91. (11) заинтересовать — khớp k136.
Họ hàng cố ý vắng: không có (mọi từ đều có họ thật).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "разобрать": "tháo rời, tháo dỡ, đọc ra, nghe ra, sắp xếp, phân tích, mua hết",  # + make out, sort, analyse, buy up
    "завоёвывать": "chinh phục, chiếm, giành được",                # «tranh giành» gloss không xác nhận
    "осудить": "kết án, tuyên án, lên án, chỉ trích",              # + condemn / denounce; «xử tội» trùng ý
    "осуждать": "lên án, chỉ trích, phê phán, không tán thành, kết án",  # + to convict
    "угадать": "đoán, đoán ra, đoán đúng",                         # «nghĩ ra» là приду́мать, không phải nghĩa
    "угадывать": "đoán, đoán ra, đoán đúng",                       # «phỏng đoán» là дога́дываться/предполага́ть
}

# ------------------------------------------------------------- коммунистический
S["коммунистический"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">коммуни́ст-</span>'
    '<span class="hd-gloss">người cộng sản; lõi <i>коммун-</i> CHUNG (La-tinh <i>communis</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ческ-ий</span>'
    '<span class="hd-gloss">đuôi tính từ «thuộc về …», như <b>полити́ческий</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thuộc về người cộng sản» ⇒ cộng sản. Trọng âm luôn rơi vào chính đuôi '
    '<i>-и́ческий</i>, nên nó rời chỗ cũ của <b>коммуни́ст</b>: <b>коммунисти́ческий</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>коммуни́ст</b> người cộng sản · <b>коммуни́зм</b> chủ nghĩa cộng sản · '
    '<b>коммуна́льный</b> thuộc dịch vụ chung</div>'
)

# ---------------------------------------------------------------- избирательный
S["избирательный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">из-</span>'
    '<span class="hd-gloss">RA — lấy ra từ trong đám</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бир-а-</span>'
    '<span class="hd-gloss">gốc LẤY, cùng gốc <b>брать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-тельн-ый</span>'
    '<span class="hd-gloss">đuôi tính từ, như <b>внима́тельный</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Lấy ra» người mình muốn ⇒ thuộc bầu cử: <b>избира́тельный уча́сток</b> điểm bỏ '
    'phiếu. «Lấy ra» vài thứ, bỏ phần còn lại ⇒ có chọn lọc: <b>избира́тельный подхо́д</b> cách tiếp '
    'cận chọn lọc.</div>'
    '<div class="hd-warn">Dạng ngắn giống đực chèn <i>е</i> và mất <i>ь</i>: <b>избира́телен</b>; ba dạng '
    'kia giữ <i>ь</i>: <b>избира́тельна, избира́тельно, избира́тельны</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>избира́тель</b> cử tri · <b>избира́ть</b> bầu ra · <b>вы́боры</b> cuộc bầu cử · '
    '<b>выбира́ть</b> chọn</div>'
)

# ----------------------------------------------------------------------- ветеран
S["ветеран"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được thành mảnh Nga: từ mượn, gốc La-tinh <i>veteranus</i>, từ '
    '<i>vetus</i> «già, cũ» — cùng chữ với tiếng Anh <i>veteran</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người «cũ» trong nghề lính ⇒ cựu chiến binh; «cũ» trong một nghề, một đội ⇒ người '
    'kỳ cựu. Muốn nói rõ loại thì thêm cách 2: <b>ветера́н войны́</b> cựu chiến binh, '
    '<b>ветера́н труда́</b> người lao động lâu năm (một danh hiệu).</div>'
    '<div class="hd-warn"><b>ве́тер</b> (gió) trông giống nhưng KHÔNG cùng gốc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ветера́нский</b> thuộc cựu chiến binh</div>'
)

# ----------------------------------------------------------------------- беженец
S["беженец"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">беж-</span>'
    '<span class="hd-gloss">gốc CHẠY (<i>бег-</i>, г → ж) — như <b>бежа́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ен-ец</span>'
    '<span class="hd-gloss">NGƯỜI, giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Người phải chạy» ⇒ người tị nạn. Trọng âm lùi về gốc: <b>бежа́ть</b> → '
    '<b>бе́женец</b>. Chạy TỪ đâu thì <b>из</b> + cách 2: <b>бе́женец из Си́рии</b>.</div>'
    '<div class="hd-warn"><b>е trong -ец rụng</b> hễ thêm đuôi: <b>бе́женца, бе́женцу, бе́женцы</b>; '
    'cách 2 số nhiều là <b>бе́женцев</b> — <b>ла́герь для бе́женцев</b> trại tị nạn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бежа́ть</b> chạy · <b>убежа́ть</b> bỏ chạy · <b>побе́г</b> cuộc trốn chạy · '
    '<b>бе́женка</b> người tị nạn (nữ)</div>'
)

# ------------------------------------------------------------------- избиратель
S["избиратель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">из-</span>'
    '<span class="hd-gloss">RA — lấy ra từ trong đám</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бир-а-</span>'
    '<span class="hd-gloss">gốc LẤY, cùng gốc <b>брать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-тель</span>'
    '<span class="hd-gloss">NGƯỜI làm việc đó, như <b>учи́тель</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người «lấy ra», tức bầu ra ⇒ cử tri. Đứng sau nó là <b>избира́ть</b>: anh em với '
    '<b>выбира́ть</b>, nhưng trang trọng hơn và thiên về bầu vào một chức — '
    '<b>избира́ть президе́нта</b>.</div>'
    '<div class="hd-warn">Đuôi <i>-тель</i> chỉ người luôn là GIỐNG ĐỰC, đừng tưởng giống cái vì có '
    '<i>-ь</i>: <b>ка́ждый избира́тель</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>избира́ть</b> bầu ra · <b>избира́тельный</b> thuộc bầu cử · '
    '<b>вы́боры</b> cuộc bầu cử · <b>брать</b> lấy</div>'
)

# ------------------------------------------------------------------- разобрать
S["разобрать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">разо-</span>'
    '<span class="hd-gloss">TÁCH RA — <i>раз-</i> chêm <i>о</i> trước cụm <i>бр</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-бр-</span>'
    '<span class="hd-gloss">gốc LẤY — cùng gốc <b>брать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi nguyên thể; thể hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lấy TÁCH RA từng phần ⇒ tháo rời; tách từng món ⇒ sắp xếp; tách từng ý ⇒ phân '
    'tích; tách được từng chữ ⇒ đọc ra, nghe ra; mỗi người lấy một cái ⇒ mua hết. '
    'Cặp CHT: <b>разбира́ть</b>.</div>'
    '<div class="hd-warn">Chia y như <b>брать</b>, <i>е</i> mọc lại và <i>о</i> biến mất: <b>разберу́, '
    'разберёшь</b>. Quá khứ chỉ giống cái nhấn đuôi: <b>разобра́л, разобрала́, разобра́ли</b>.</div>'
    '<div class="hd-warn"><b>Не могу́ разобра́ть твой по́черк.</b> = Tớ không đọc ra chữ cậu. Thêm '
    '<i>-ся</i> mới là «hiểu ra»: <b>разобра́ться в</b> + cách 6.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>разобра́ться</b> hiểu ra · <b>собра́ть</b> gom, lắp lại · '
    '<b>убра́ть</b> dọn · <b>брать</b> lấy</div>'
)

# ----------------------------------------------------------------- расследовать
S["расследовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рас-</span>'
    '<span class="hd-gloss">TÁCH RA từng phần, làm tới nơi (<i>раз-</i> thành <i>рас-</i> trước с)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-след-</span>'
    '<span class="hd-gloss">DẤU VẾT — chính là <b>след</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ть</span>'
    '<span class="hd-gloss">đuôi động từ, chia <i>-у-</i>: <b>рассле́дую</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lần dấu vết cho ra nhẽ từng phần ⇒ điều tra. Viết hai <i>с</i>: một của tiền tố, '
    'một của gốc. Đối tượng ở cách 4: <b>рассле́довать преступле́ние</b> điều tra tội ác.</div>'
    '<div class="hd-warn">Anh em <b>иссле́довать</b> là NGHIÊN CỨU (khoa học); <b>рассле́довать</b> là ĐIỀU '
    'TRA (vụ án, tai nạn). Cả hai đều là một từ dùng cho HAI thể.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рассле́дование</b> cuộc điều tra · <b>сле́дователь</b> điều tra viên · '
    '<b>иссле́довать</b> nghiên cứu · <b>следи́ть</b> theo dõi</div>'
)

# ------------------------------------------------------------------ завоевать
S["завоевать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">CHIẾM lấy, giành về tay</span></div>'
    '<div class="hd-row"><span class="hd-piece">-воева́ть</span>'
    '<span class="hd-gloss">đánh trận — gốc <i>во-</i> CHIẾN, như <b>война́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đánh trận mà CHIẾM được ⇒ chinh phục, chiếm được. Nghĩa bóng còn hay gặp hơn: '
    '<b>завоева́ть дове́рие</b> giành được lòng tin, <b>завоева́ть зо́лото</b> giành huy chương vàng. '
    'Thể HT; chia <i>-ева-</i> → <i>-ю-</i> y như <b>воева́ть</b>: <b>завою́ю, завою́ешь</b>.</div>'
    '<div class="hd-warn"><b>воева́ть</b> cần <b>с</b> + cách 5 (đánh với ai); '
    '<b>завоева́ть</b> đi THẲNG cách 4: <b>завоева́ть страну́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>завоёвывать</b> (CHT) · <b>завоева́ние</b> cuộc chinh phục · '
    '<b>завоева́тель</b> kẻ chinh phục · <b>война́</b> chiến tranh</div>'
)

# --------------------------------------------------------------- завоёвывать
S["завоёвывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">CHIẾM lấy, giành về tay</span></div>'
    '<div class="hd-row"><span class="hd-piece">-воёв-</span>'
    '<span class="hd-gloss">= <i>-воев-</i> đánh trận, gốc <i>во-</i> CHIẾN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть</span>'
    '<span class="hd-gloss">kéo dài ⇒ thể CHƯA hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>завоева́ть</b>: đang giành dần, hay lần nào cũng giành được. Trọng '
    'âm đứng ngay trước <i>-ыва-</i>, nên <i>е</i> hoá <i>ё</i>. Chia đều: <b>завоёвываю, '
    'завоёвываешь</b> — không co thành <i>-ю-</i> như vế HT.</div>'
    '<div class="hd-warn"><b>Она́ до́лго завоёвывала его́ дове́рие.</b> = Cô ấy mất rất lâu để giành lòng '
    'tin của anh ta — <b>до́лго</b> (lâu) nên phải là vế này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>завоева́ть</b> (HT) · <b>воева́ть</b> đánh trận · '
    '<b>завоева́ние</b> cuộc chinh phục · <b>во́ин</b> chiến binh</div>'
)

# ----------------------------------------------------------------------- осудить
S["осудить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">làm ra thể hoàn thành, nghĩa riêng không rõ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-суд-</span>'
    '<span class="hd-gloss">XÉT — gốc của <b>суд</b> toà án</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>суди́ть</b> là còn đang xét; <b>осуди́ть</b> là xét xong và thấy CÓ TỘI ⇒ kết án; '
    'ngoài toà ⇒ lên án. Dạng «tôi» д → ж, rồi trọng âm lùi: <b>осужу́, осу́дишь, осу́дят</b>.</div>'
    '<div class="hd-warn">Vì tội gì: <b>за</b> + cách 4; chịu án gì: <b>на</b> + cách 4 — '
    '<b>Его́ осуди́ли за кра́жу на пять лет.</b> Anh ta bị kết án năm năm vì tội trộm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>осужда́ть</b> (CHT) · <b>осуждённый</b> người bị kết án · '
    '<b>суди́ть</b> xét xử · <b>судья́</b> thẩm phán</div>'
)

# ---------------------------------------------------------------------- осуждать
S["осуждать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">tiền tố của <b>осуди́ть</b>, nghĩa riêng không rõ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сужд-</span>'
    '<span class="hd-gloss">= <i>-суд-</i> XÉT, biến âm д → жд</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>осуди́ть</b>, д → жд như <b>обсужда́ть</b>. Ngoài đời chủ yếu là '
    'phán xét, lên án người khác: <b>Не осужда́й его́.</b> Đừng lên án anh ấy. '
    'Chia đều: <b>осужда́ю, осужда́ешь</b>.</div>'
    '<div class="hd-warn">Chỉ khác <b>обсужда́ть</b> một chữ <i>б</i>: <b>обсужда́ть</b> = bàn bạc, '
    '<b>осужда́ть</b> = lên án. Lên án vì gì: <b>за</b> + cách 4.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>осуди́ть</b> (HT) · <b>осужде́ние</b> sự lên án · '
    '<b>суди́ть</b> phán xét · <b>рассужда́ть</b> lập luận</div>'
)

# ------------------------------------------------------------------------ абсурд
S["абсурд"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được thành mảnh Nga: từ mượn, gốc La-tinh <i>absurdus</i> «chối tai, '
    'lạc điệu» — cùng chữ với tiếng Anh <i>absurd</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Nghe chối tai» ⇒ vô lý. Tiếng Anh <i>absurd</i> là tính từ, còn <b>абсу́рд</b> là '
    'DANH TỪ: <b>Э́то абсу́рд!</b> Thật vô lý! Tính từ phải thêm <i>-н-</i>: '
    '<b>абсу́рдная иде́я</b> ý tưởng vô lý.</div>'
    '<div class="hd-warn">Cụm hay gặp: <b>довести́ до абсу́рда</b> = đẩy (cái gì) tới mức vô lý, '
    '<b>дойти́ до абсу́рда</b> = đi tới mức vô lý.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>абсу́рдный</b> vô lý · <b>абсу́рдность</b> tính vô lý</div>'
)

# ------------------------------------------------------------------ противоречие
S["противоречие"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">противо-</span>'
    '<span class="hd-gloss">CHỐNG LẠI, đối diện — như <b>про́тив</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-реч-</span>'
    '<span class="hd-gloss">gốc NÓI (<i>рек-</i>, к → ч) — như <b>речь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ие</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Nói ngược nhau» ⇒ mâu thuẫn. Ghép y hệt tiếng Anh <i>contradiction</i>: '
    '<i>contra-</i> chống + <i>dict-</i> nói.</div>'
    '<div class="hd-warn">Mâu thuẫn VỚI: <b>противоре́чие с</b> + cách 5. Nhưng động từ thì đòi cách 3, không '
    'giới từ: <b>Э́то противоре́чит зако́ну.</b> Điều này trái với luật.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>противоре́чить</b> mâu thuẫn với · <b>противоречи́вый</b> đầy mâu thuẫn · '
    '<b>речь</b> lời nói · <b>про́тив</b> chống lại</div>'
)

# ----------------------------------------------------------------------- намерен
S["намерен"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">VÀO, nhắm vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мер-</span>'
    '<span class="hd-gloss">ĐO — như <b>ме́ра</b>, <b>ме́рить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ен</span>'
    '<span class="hd-gloss">đuôi dạng ngắn, giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đã «đo ngắm vào» một đích ⇒ có ý định. Đi với nguyên thể: '
    '<b>Я наме́рен бро́сить кури́ть.</b> Tôi định bỏ thuốc. Nghe dứt khoát, trang trọng hơn '
    '<b>собира́юсь</b>.</div>'
    '<div class="hd-warn">Nghĩa «có ý định» chỉ ở DẠNG NGẮN, phải hợp với CHỦ NGỮ: <b>он наме́рен, '
    'она́ наме́рена, они́ наме́рены</b>. Dạng dài <b>наме́ренный</b> lại là «cố ý».</div>'
    '<div class="hd-warn">Quá khứ, tương lai thêm <b>быть</b>: <b>Она́ была́ наме́рена уе́хать.</b> Cô ấy đã '
    'định đi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>наме́рение</b> ý định · <b>наме́ренно</b> một cách cố ý · '
    '<b>намерева́ться</b> định làm · <b>ме́рить</b> đo</div>'
)

# -------------------------------------------------------------------- компромисс
S["компромисс"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được thành mảnh Nga: từ mượn, gốc La-tinh <i>compromissum</i> — '
    '<i>com-</i> cùng + <i>promissum</i> lời hứa; cùng chữ với tiếng Anh <i>compromise</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hai bên «cùng hứa» chấp nhận một lối giải quyết ⇒ thoả hiệp. Mặt chữ khác tiếng Anh ở đuôi: '
    'hai <i>с</i>, không có <i>е</i> — nên là danh từ giống đực.</div>'
    '<div class="hd-warn">Hai cụm phải thuộc: <b>найти́ компроми́сс</b> tìm ra thoả hiệp · '
    '<b>пойти́ на компроми́сс</b> chịu thoả hiệp (<b>на</b> + cách 4).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>компроми́ссный</b> mang tính thoả hiệp · '
    '<b>бескомпроми́ссный</b> không khoan nhượng</div>'
)

# ------------------------------------------------------------------ планировать
S["планировать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">план-</span>'
    '<span class="hd-gloss">kế hoạch — chính là <b>план</b> (La-tinh <i>planum</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ирова-ть</span>'
    '<span class="hd-gloss">biến từ mượn thành động từ, chia <i>-у-</i>: <b>плани́рую</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Làm ra <b>план</b>» ⇒ lập kế hoạch, dự định. Đi với cách 4 (<b>плани́ровать '
    'о́тпуск</b> lên kế hoạch nghỉ phép) hoặc nguyên thể: <b>Я плани́рую пое́хать на мо́ре.</b> Tôi dự '
    'định đi biển.</div>'
    '<div class="hd-warn">Thể CHT. Vế HT là <b>заплани́ровать</b> hoặc <b>сплани́ровать</b> — kế hoạch đã '
    'chốt xong.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>план</b> kế hoạch · <b>планиро́вка</b> cách bố trí mặt bằng · '
    '<b>заплани́рованный</b> đã lên kế hoạch</div>'
)

# --------------------------------------------------------------- заинтересовать
S["заинтересовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">BẮT ĐẦU → thể hoàn thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">-интерес-</span>'
    '<span class="hd-gloss">mối quan tâm — <b>интере́с</b> (Anh <i>interest</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова́-ть</span>'
    '<span class="hd-gloss">biến danh từ thành động từ, chia <i>-у-</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm mối quan tâm BẮT ĐẦU nảy ra ⇒ gây hứng thú. Vế CHT thường ngày là '
    '<b>интересова́ть</b>. Chia: <b>заинтересу́ю, заинтересу́ешь</b>.</div>'
    '<div class="hd-warn">AI bị cuốn hút ở cách 4, BẰNG gì ở cách 5: <b>заинтересова́ть дете́й му́зыкой</b> '
    'làm bọn trẻ hứng thú với nhạc. Thêm <i>-ся</i> là đảo vai: <b>Он заинтересова́лся му́зыкой.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>интере́с</b> mối quan tâm · <b>интере́сный</b> thú vị · '
    '<b>заинтересова́ться</b> thấy hứng thú · <b>заинтересо́ванный</b> có quan tâm</div>'
)

# ----------------------------------------------------------------------- угадать
S["угадать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">làm ĐƯỢC, trúng kết quả</span></div>'
    '<div class="hd-row"><span class="hd-piece">-гад-</span>'
    '<span class="hd-gloss">ĐOÁN — như <b>гада́ть</b> đoán, bói</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть</span>'
    '<span class="hd-gloss">đuôi lớp chia 1; thể hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đoán mà TRÚNG ⇒ đoán ra, đoán đúng. Đi thẳng cách 4: <b>угада́ть число́</b> đoán '
    'trúng con số. Chia đều: <b>угада́ю, угада́ешь</b>.</div>'
    '<div class="hd-warn"><b>угада́ть</b> = đoán trúng, có thể nhờ may; <b>догада́ться</b> = suy từ dấu hiệu '
    'mà hiểu ra (<b>о</b> + cách 6).</div>'
    '<div class="hd-warn"><b>Угада́й, кто пришёл!</b> = Đoán xem ai đến!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>уга́дывать</b> (CHT) · <b>гада́ть</b> đoán, bói · '
    '<b>зага́дка</b> câu đố · <b>догада́ться</b> đoán ra</div>'
)

# --------------------------------------------------------------------- угадывать
S["угадывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">làm ĐƯỢC, trúng kết quả</span></div>'
    '<div class="hd-row"><span class="hd-piece">-гад-</span>'
    '<span class="hd-gloss">ĐOÁN — như <b>гада́ть</b> đoán, bói</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть</span>'
    '<span class="hd-gloss">kéo dài ⇒ thể CHƯA hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp CHT của <b>угада́ть</b>: đoán trúng hết lần này đến lần khác, hay đang ngồi đoán. '
    'Thêm <i>-ыва-</i> thì trọng âm lùi về <i>-га́-</i>, y như <b>дога́дываться</b>. Chia đều: '
    '<b>уга́дываю, уга́дываешь</b>.</div>'
    '<div class="hd-warn"><b>Она́ всегда́ уга́дывает.</b> Cô ấy lúc nào cũng đoán trúng — '
    '<b>всегда́</b> (luôn luôn) nên phải là vế này.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>угада́ть</b> (HT) · <b>гада́ть</b> đoán, bói · '
    '<b>зага́дка</b> câu đố · <b>дога́дываться</b> ngờ ngợ</div>'
)

# -------------------------------------------------------------------- рассуждать
S["рассуждать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рас-</span>'
    '<span class="hd-gloss">TÁCH RA từng phần (<i>раз-</i> thành <i>рас-</i> trước с)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сужд-</span>'
    '<span class="hd-gloss">= <i>-суд-</i> XÉT, biến âm д → жд</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tách vấn đề ra mà XÉT từng phần ⇒ lập luận, bàn luận. Bàn VỀ gì là <b>о</b> + cách '
    '6: <b>рассужда́ть о поли́тике</b>. Chia đều: <b>рассужда́ю, рассужда́ешь</b>.</div>'
    '<div class="hd-warn">Đừng coi <b>рассуди́ть</b> là cặp HT của nghĩa này: nó là phân xử ai đúng ai '
    'sai.</div>'
    '<div class="hd-warn"><b>Хва́тит рассужда́ть!</b> = Thôi đừng lý luận nữa!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рассужде́ние</b> lập luận · <b>рассу́док</b> lý trí · '
    '<b>обсужда́ть</b> bàn bạc · <b>осужда́ть</b> lên án · <b>суди́ть</b> phán xét</div>'
)

# -------------------------------------------------------------------- передумать
S["передумать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span>'
    '<span class="hd-gloss">LẠI, đổi sang cái khác</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дум-</span>'
    '<span class="hd-gloss">Ý NGHĨ — như <b>ду́мать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi lớp chia 1; thể hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩ LẠI và ra ý khác ⇒ đổi ý. Đứng một mình là đủ, không cần thêm chữ «ý»: '
    '<b>Я переду́мал.</b> Tôi đổi ý rồi. Cặp CHT: <b>переду́мывать</b>.</div>'
    '<div class="hd-warn"><b>переду́мать</b> + nguyên thể (thường là CHT) = đổi ý, THÔI KHÔNG làm nữa: '
    '<b>Я переду́мал е́хать.</b> Tôi thôi không đi nữa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ду́мать</b> nghĩ · <b>поду́мать</b> nghĩ một lát · '
    '<b>обду́мать</b> suy nghĩ kỹ · <b>приду́мать</b> nghĩ ra</div>'
)

B = {
    "docbangmat": 132,
    "loitubat": 3,
    "nguonsai": 5,
    "baolen": [
        "V cần duyệt (6 thẻ): разобра́ть «tháo rời, tháo dỡ, đọc ra, nghe ra, sắp xếp, phân tích, mua hết» (đề cũ chỉ có nghĩa tháo); завоёвывать «chinh phục, chiếm, giành được» (bỏ «tranh giành»); осуди́ть «kết án, tuyên án, lên án, chỉ trích»; осужда́ть + «kết án»; угада́ть và уга́дывать cùng «đoán, đoán ra, đoán đúng» (badge thể tách). 15 thẻ còn lại giữ đề cũ.",
        "Đã chạy thử do_va_cham (chỉ đọc Anki) với V mới thay vào: 0 va chạm dính từ của lô.",
        "Nguồn sai đã bác (5): завоёвывать «tranh giành»; угада́ть «nghĩ ra» (là приду́мать); уга́дывать «phỏng đoán»; избира́тель gloss «constituency» (không đưa vào); плани́ровать gloss «level / grade / even out» thuộc từ khác trọng âm планирова́ть (không đưa vào).",
        "Chỗ KHÔNG chắc: (1) плани́ровать nghĩa «lượn» (glide) là từ đồng âm gốc Pháp, cố ý bỏ; ranh giới «quy hoạch, thiết kế» giữa плани́ровать và планирова́ть không kiểm được bằng máy nên giữ đề cũ. (2) о- của осуди́ть/осужда́ть: ghi thẳng «nghĩa riêng không rõ», không bịa. (3) беженец: -ен-ец gộp thành một mảnh NGƯỜI, không tách -ен- riêng.",
        "loitubat (3): наме́рен «hợp với người nói» → hợp với CHỦ NGỮ; компроми́сс «cùng hứa chịu nhường» nói quá từ nguyên; рассужда́ть «không có cặp HT» → chỉ nói рассуди́ть không phải cặp của nghĩa này.",
    ],
}
