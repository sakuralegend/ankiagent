# -*- coding: utf-8 -*-
"""k188 — concepts::emotion (lô trộn): cảm xúc, tính cách, động từ tâm trí.

Chỗ cần nhất quán trong lô:
(1) логи́чный / ло́гика: mượn Hy Lạp logos; bẫy chung là lẫn логи́чный (hợp lý) với логи́ческий (thuộc logic).
(2) догада́ться / дога́дываться: до- TỚI + гад- ĐOÁN (гада́ть, зага́дка).
(3) жале́ть / пожале́ть: -жал- THƯƠNG XÓT, khớp сожале́ние [k57], жаль [k80], жа́лость [k180].
(4) изме́на: из- RA KHỎI + -мен- ĐỔI, khớp измени́ть / изменя́ть [k95], измене́ние [k160].
(5) ощути́ть / ощуща́ть: ощут-/ощущ- CẢM THẤY (т → щ), khớp ощуще́ние [k159].
(6) поража́ть / порази́ть: -раз-/-раж- ĐÁNH, GIÁNG (з → ж), khớp пораже́ние [k128].
(7) отве́тственный ← отве́т + -ствен-н-, khớp отве́тственность [k159].
(8) зли́ться / разозли́ться ← зл- (зло, злой [k40]).
Họ hàng cố ý vắng: không có (mọi từ trong lô đều có họ thật).
"""

# 🔴 KHÔNG dựng biến khối dùng chung (HE/LUAT/THE…) rồi cộng vào mọi thẻ — README §3.

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "ощутить": "cảm thấy, cảm nhận được, nhận thấy",          # va chạm почувствовать [k88]: «cảm nhận» -> «cảm nhận được» (to sense, HT); «nhận ra» -> «nhận thấy» (gloss chỉ feel/sense)
    "догадываться": "đoán ra, nhận ra, hiểu ra, phỏng đoán, ngờ ngợ",  # thiếu surmise / suspect
    "нежный": "dịu dàng, âu yếm, mềm mại, êm ái, mỏng manh",   # «non nớt» = immature, không phải delicate
    "верность": "lòng trung thành, sự chung thuỷ, sự đúng đắn, sự chính xác",  # «trung thực» = честность; thiếu fidelity
    "логика": "logic, lý lẽ, sự hợp lý",                         # «lô-gic» lặp đúng «logic»
}

# --------------------------------------------------------------------- логичный
S["логичный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">логич-</span>'
    '<span class="hd-gloss">LOGIC — <b>ло́гика</b>, <b>к → ч</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">→ tính từ chỉ PHẨM CHẤT</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Có logic ⇒ hợp lý: <b>логи́чный вы́вод</b> kết luận hợp lý. Trọng âm dời từ '
    '<b>ло́-</b> sang <b>-ги́-</b>; dạng ngắn giống đực chèn <b>е</b>: <b>логи́чен</b>. Trạng từ '
    '<b>логи́чно</b> = «nghe có lý».</div>'
    '<div class="hd-warn">Đừng lẫn <b>логи́ческий</b> = THUỘC VỀ logic (<b>логи́ческая '
    'зада́ча</b> bài toán logic) — không nói được «hợp lý».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ло́гика</b> logic · <b>логи́ческий</b> thuộc logic · '
    '<b>нелоги́чный</b> vô lý</div>'
)

# --------------------------------------------------------------------- логика
S["логика"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">лог-</span>'
    '<span class="hd-gloss">LỜI, LÝ LẼ — Hy Lạp <i>logos</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ик-а</span>'
    '<span class="hd-gloss">đuôi tên môn/ngành, giống cái — như <b>фи́зика</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là tiếng Anh <i>logic</i> thêm đuôi <b>-а</b>. Trọng âm đầu từ '
    '<b>ло́-</b>, nhưng sang tính từ thì dời: <b>логи́чный</b>.</div>'
    '<div class="hd-warn"><b>Где ло́гика?</b> = Lý lẽ ở đâu ra thế? — câu bắt bẻ rất hay nghe.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>логи́чный</b> hợp lý · <b>логи́ческий</b> thuộc logic · '
    '<b>нелоги́чный</b> vô lý</div>'
)

# --------------------------------------------------------------------- гениальный
S["гениальный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гени-</span>'
    '<span class="hd-gloss">THIÊN TÀI — <b>ге́ний</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́льн-ый</span>'
    '<span class="hd-gloss">đuôi tính từ gốc Latin — như <b>норма́льный</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Của thiên tài ⇒ xuất chúng; đời thường khen ý hay: <b>Гениа́льно!</b> = '
    'Tuyệt quá! Đuôi <b>-а́льн-</b> hút trọng âm về mình (<b>ге́ний → гениа́льный</b>); dạng ngắn giống '
    'đực chèn <b>е</b>: <b>гениа́лен</b>.</div>'
    '<div class="hd-warn">Bạn giả: tiếng Anh <i>genial</i> là «thân thiện, vui tính» — '
    '<b>гениа́льный</b> thì không hề có nghĩa đó.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ге́ний</b> thiên tài · <b>гениа́льность</b> sự xuất chúng</div>'
)

# --------------------------------------------------------------------- догадаться
S["догадаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-</span>'
    '<span class="hd-gloss">TỚI ĐÍCH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-гад-</span>'
    '<span class="hd-gloss">ĐOÁN — <b>гада́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть-ся</span>'
    '<span class="hd-gloss">đuôi động từ phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đoán cho TỚI đích ⇒ đoán ra, tự hiểu ra (không ai nói cho). Đoán ra điều gì: '
    '<b>о</b> + cách 6 — <b>догада́ться о пра́вде</b>. Cặp thể: <b>дога́дываться</b>.</div>'
    '<div class="hd-warn"><b>догада́ться</b> + nguyên thể = biết ý mà làm: <b>Он догада́лся '
    'позвони́ть.</b> Anh ấy biết ý gọi điện.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гада́ть</b> đoán, bói · <b>дога́дка</b> sự phỏng đoán · '
    '<b>зага́дка</b> câu đố · <b>дога́дливый</b> nhanh trí</div>'
)

# --------------------------------------------------------------------- догадываться
S["догадываться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">до-гад-</span>'
    '<span class="hd-gloss">ĐOÁN TỚI ĐÍCH — <b>догада́ться</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть-ся</span>'
    '<span class="hd-gloss">đuôi CHƯA hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp thể của <b>догада́ться</b>: thêm <b>-ыва-</b>, trọng âm lùi về '
    '<b>-га́-</b>, chia đều: <b>дога́дываюсь</b>. Thể chưa xong nên hay mang nghĩa đang ngờ ngợ, '
    'chưa chắc.</div>'
    '<div class="hd-warn"><b>Я дога́дываюсь, о чём ты.</b> = Tôi đoán được cậu định nói gì.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>догада́ться</b> đoán ra (HT) · <b>дога́дка</b> sự phỏng đoán · '
    '<b>гада́ть</b> đoán, bói</div>'
)

# --------------------------------------------------------------------- задуматься
S["задуматься"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">CHÌM VÀO, bắt đầu</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дум-</span>'
    '<span class="hd-gloss">NGHĨ — <b>ду́мать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть-ся</span>'
    '<span class="hd-gloss">đuôi động từ phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chìm vào suy nghĩ ⇒ trầm ngâm, đâm ra nghĩ ngợi. Nghĩ VỀ gì: <b>о</b> + cách 6 '
    'hoặc <b>над</b> + cách 5 — <b>заду́маться над вопро́сом</b>. Cặp thể: <b>заду́мываться</b>.</div>'
    '<div class="hd-warn">Bỏ <b>-ся</b> là sang nghĩa khác: <b>заду́мать</b> = định làm, nghĩ ra '
    '(một kế hoạch).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ду́мать</b> nghĩ · <b>заду́мчивый</b> đăm chiêu · '
    '<b>приду́мать</b> nghĩ ra</div>'
)

# --------------------------------------------------------------------- измена
S["измена"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">из-</span>'
    '<span class="hd-gloss">RA KHỎI (trạng thái cũ)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мен-</span>'
    '<span class="hd-gloss">ĐỔI — như <b>меня́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">ĐỔI lòng, bỏ người mình đã hứa ⇒ phản bội. Danh từ của <b>измени́ть</b> '
    'ở nghĩa «phản bội» — nên cũng đi với cách 3.</div>'
    '<div class="hd-warn">Phản bội AI → cách 3: <b>изме́на жене́</b> ngoại tình · '
    '<b>изме́на ро́дине</b> tội phản quốc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>измени́ть</b> thay đổi; phản bội · <b>изме́нник</b> kẻ phản bội · '
    '<b>измене́ние</b> sự thay đổi</div>'
)

# --------------------------------------------------------------------- нежный
S["нежный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">неж-</span>'
    '<span class="hd-gloss">DỊU, ÊM</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một chữ phủ cả cảm giác lẫn chạm: <b>не́жный взгляд</b> ánh mắt dịu dàng · '
    '<b>не́жная ко́жа</b> làn da mềm mại. Dạng ngắn chèn <b>е</b> và giống cái nhảy trọng âm: '
    '<b>не́жен</b> · <b>нежна́</b> · <b>не́жно</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: gốc <b>неж-</b> nối với từ cổ <b>не́га</b> «sự êm ái» '
    '(<b>г → ж</b>) là từ nguyên, không phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>не́жность</b> sự dịu dàng · <b>не́жно</b> dịu dàng, nhẹ nhàng</div>'
)

# --------------------------------------------------------------------- ответственный
S["ответственный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ответ-</span>'
    '<span class="hd-gloss">TRẢ LỜI — <b>отве́т</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ствен-н-ый</span>'
    '<span class="hd-gloss">→ tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Phải TRẢ LỜI cho việc mình làm ⇒ có trách nhiệm — y như <i>respond</i> → '
    '<i>responsible</i>. Nói về VIỆC thì là hệ trọng: <b>отве́тственный моме́нт</b> giây phút quyết '
    'định. Dạng ngắn giống đực có hai: <b>отве́тствен</b> / <b>отве́тственен</b>.</div>'
    '<div class="hd-warn">Chịu trách nhiệm VỀ: <b>за</b> + cách 4 — <b>Кто отве́тственный за '
    'э́то?</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>отве́тственность</b> trách nhiệm · <b>безотве́тственный</b> vô trách '
    'nhiệm · <b>отвеча́ть</b> trả lời; chịu trách nhiệm</div>'
)

# --------------------------------------------------------------------- аккуратный
S["аккуратный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ theo gốc Nga: mượn Latin <i>accuratus</i> «làm chu đáo», cùng gốc '
    'tiếng Anh <i>accurate</i>; chỉ <b>-н-ый</b> là đuôi tính từ Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa chính trong tiếng Nga là NGĂN NẮP, CẨN THẬN (<b>аккура́тный '
    'по́черк</b> nét chữ gọn gàng), không phải «chính xác». Viết hai <b>к</b>; dạng ngắn chèn '
    '<b>е</b>: <b>аккура́тен</b>.</div>'
    '<div class="hd-warn"><b>Аккура́тно!</b> = Cẩn thận đấy! — lời dặn khi bưng bê, đi đường.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>аккура́тно</b> cẩn thận · <b>аккура́тность</b> tính ngăn nắp · '
    '<b>неаккура́тный</b> cẩu thả</div>'
)

# --------------------------------------------------------------------- радостный
S["радостный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">радост-</span>'
    '<span class="hd-gloss">NIỀM VUI — <b>ра́дость</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mang niềm vui ⇒ vui mừng, hân hoan: <b>ра́достная но́вость</b> tin vui. '
    'Khác <b>рад</b> (chỉ có dạng ngắn, «tôi thấy vui»): <b>ра́достный</b> tả vẻ mặt, tin, '
    'sự kiện. Dạng ngắn chèn <b>е</b>: <b>ра́достен</b>.</div>'
    '<div class="hd-warn">Cụm <b>-стн-</b> đọc nuốt <b>т</b> nhưng VIẾT vẫn phải có: '
    '<b>ра́достный</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рад</b> vui · <b>ра́дость</b> niềm vui · <b>ра́доваться</b> vui mừng · '
    '<b>обра́доваться</b> mừng rỡ</div>'
)

# --------------------------------------------------------------------- поражать
S["поражать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố — trúng vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-раж-</span>'
    '<span class="hd-gloss">ĐÁNH, GIÁNG (<i>раз-</i>, <i>з → ж</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi CHƯA hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đánh trúng ⇒ nghĩa đen «trúng đích» (<b>поража́ть цель</b>), nghĩa bóng '
    '«đánh trúng tâm trí» ⇒ làm sửng sốt. <b>ж</b> đứng yên suốt bảng chia: <b>поража́ю</b>. '
    'Cặp thể: <b>порази́ть</b>.</div>'
    '<div class="hd-warn"><b>Ты меня́ поража́ешь!</b> = Cậu làm tôi kinh ngạc đấy! — khen lẫn '
    'mỉa đều dùng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>порази́ть</b> làm sửng sốt (HT) · <b>пораже́ние</b> thất bại · '
    '<b>порази́тельный</b> đáng kinh ngạc</div>'
)

# --------------------------------------------------------------------- поразить
S["поразить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố — trúng vào</span></div>'
    '<div class="hd-row"><span class="hd-piece">-раз-</span>'
    '<span class="hd-gloss">ĐÁNH, GIÁNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giáng một đòn trúng ⇒ làm choáng, sửng sốt; trên chiến trường là đánh bại '
    '(nên mới có <b>пораже́ние</b>). Chỉ ngôi «tôi» hoá <b>ж</b>: <b>я поражу́</b>, còn <b>ты '
    'порази́шь</b>.</div>'
    '<div class="hd-warn"><b>Я был поражён.</b> = Tôi sững sờ. — dạng bị động hay gặp nhất.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поража́ть</b> làm sửng sốt (CHT) · <b>пораже́ние</b> thất bại · '
    '<b>порази́тельный</b> đáng kinh ngạc</div>'
)

# --------------------------------------------------------------------- ощутить
S["ощутить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ощут-</span>'
    '<span class="hd-gloss">CẢM THẤY (bằng giác quan)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Khác <b>почу́вствовать</b> ở chỗ thiên về cái da thịt, giác quan báo về — '
    '<b>ощути́ть хо́лод</b> thấy rõ cái lạnh — y như <b>ощуще́ние</b>. Ngôi «tôi» <b>т → щ</b>: '
    '<b>я ощущу́</b>, <b>ты ощути́шь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ощуща́ть</b> cảm thấy (CHT) · <b>ощуще́ние</b> cảm giác · '
    '<b>ощути́мый</b> rõ rệt, sờ thấy được</div>'
)

# --------------------------------------------------------------------- ощущать
S["ощущать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ощущ-</span>'
    '<span class="hd-gloss">CẢM THẤY — <b>ощути́ть</b>, <b>т → щ</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi CHƯA hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp thể của <b>ощути́ть</b>: <b>щ</b> có sẵn trong thân, chia đều '
    '<b>ощуща́ю</b>. Cùng mặt chữ với danh từ <b>ощуще́ние</b> — nhớ một là ra hai.</div>'
    '<div class="hd-warn">Thấy mình ra sao thì thêm <b>себя́</b>: <b>Я ощуща́ю себя́ свобо́дным.</b> '
    'Tôi thấy mình tự do.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ощути́ть</b> cảm thấy (HT) · <b>ощуще́ние</b> cảm giác · '
    '<b>ощути́мый</b> rõ rệt</div>'
)

# --------------------------------------------------------------------- ненавидеть
S["ненавидеть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">не-</span>'
    '<span class="hd-gloss">KHÔNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-на-вид-</span>'
    '<span class="hd-gloss">ƯA NHÌN — gốc <b>вид-</b> của <b>ви́деть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е-ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen «không chịu nổi nhìn mặt» ⇒ căm ghét. <i>навидеть</i> đứng một '
    'mình không còn dùng. Chia y <b>ви́деть</b>: <b>я ненави́жу</b>, <b>ты ненави́дишь</b>.</div>'
    '<div class="hd-warn">Danh từ dời trọng âm lên đầu: <b>не́нависть</b> lòng căm ghét.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>не́нависть</b> lòng căm ghét · <b>ви́деть</b> thấy · <b>вид</b> vẻ, '
    'cảnh</div>'
)

# --------------------------------------------------------------------- жалеть
S["жалеть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">жал-</span>'
    '<span class="hd-gloss">THƯƠNG XÓT, thấy tiếc — như <b>жаль</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е-ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ nhất: <b>жале́ю</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một gốc, hai nghĩa tách bằng cách: <b>жале́ть</b> + cách 4 = THƯƠNG ai '
    '(<b>жале́ть ребёнка</b>); <b>о</b> + cách 6 = TIẾC điều gì (<b>жале́ть о про́шлом</b>). '
    'Cặp thể: <b>пожале́ть</b>.</div>'
    '<div class="hd-warn"><b>не жале́ть сил</b> = không tiếc sức — «tiếc» ở đây là tiếc của, không '
    'nỡ bỏ ra.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жаль</b> tiếc · <b>жа́лость</b> lòng thương · <b>сожале́ние</b> sự '
    'tiếc nuối · <b>пожа́луйста</b> làm ơn</div>'
)

# --------------------------------------------------------------------- пожалеть
S["пожалеть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">chỉ đánh dấu XONG, không thêm nghĩa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-жал-е-ть</span>'
    '<span class="hd-gloss">THƯƠNG, TIẾC — chính là <b>жале́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thể hoàn thành của <b>жале́ть</b>, giữ nguyên hai lối: + cách 4 thương ai, '
    '<b>о</b> + cách 6 tiếc điều gì. Chia đều: <b>пожале́ю</b>, <b>пожале́ешь</b>.</div>'
    '<div class="hd-warn"><b>Ты пожале́ешь!</b> = Rồi cậu sẽ hối hận! · <b>Не пожале́ешь.</b> = '
    'Cậu sẽ không phải tiếc đâu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жале́ть</b> thương, tiếc (CHT) · <b>сожале́ние</b> sự tiếc nuối · '
    '<b>жа́лость</b> lòng thương</div>'
)

# --------------------------------------------------------------------- верность
S["верность"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вер-н-</span>'
    '<span class="hd-gloss">TRUNG THÀNH; ĐÚNG — <b>ве́рный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span>'
    '<span class="hd-gloss">→ danh từ trừu tượng, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mang cả hai nhánh của <b>ве́рный</b>: với NGƯỜI là lòng trung thành, chung '
    'thuỷ; với LỜI, phép tính là sự đúng đắn (<b>ве́рность отве́та</b>).</div>'
    '<div class="hd-warn">Trung thành VỚI ai → cách 3, như <b>ве́рен</b>: <b>ве́рность жене́</b>, '
    '<b>ве́рность сло́ву</b> sự giữ lời.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ве́рный</b> trung thành; đúng · <b>ве́ра</b> niềm tin · <b>ве́рить</b> '
    'tin · <b>неве́рность</b> sự không chung thuỷ</div>'
)

# --------------------------------------------------------------------- злиться
S["злиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">зл-</span>'
    '<span class="hd-gloss">CÁI ÁC, cơn tức — <b>зло</b>, <b>злой</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть-ся</span>'
    '<span class="hd-gloss">đuôi phản thân, lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>зли́ть</b> = chọc tức ai; thêm <b>-ся</b> thành tự mình tức ⇒ đang giận, '
    'đang cáu. Chia: <b>я злю́сь</b>, <b>ты зли́шься</b>. Cặp thể: <b>разозли́ться</b>.</div>'
    '<div class="hd-warn">Giận AI → <b>на</b> + cách 4: <b>Не злись на меня́!</b> = Đừng giận tớ!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>злой</b> ác; đang cáu · <b>зло</b> điều ác · <b>зло́сть</b> cơn tức · '
    '<b>разозли́ться</b> nổi giận</div>'
)

# --------------------------------------------------------------------- разозлиться
S["разозлиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span>'
    '<span class="hd-gloss">BÙNG LÊN tới mức — như <b>рассерди́ться</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-о-</span>'
    '<span class="hd-gloss">nguyên âm nối, chèn trước cụm <b>зл</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-зл-и-ть-ся</span>'
    '<span class="hd-gloss">TỨC GIẬN — <b>зли́ться</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thể hoàn thành của <b>зли́ться</b>: cơn giận bùng lên tới nơi ⇒ nổi giận. '
    'Vẫn <b>на</b> + cách 4: <b>Он разозли́лся на бра́та.</b> Chia: <b>я разозлю́сь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>зли́ться</b> đang giận (CHT) · <b>зло́сть</b> cơn tức · <b>злой</b> ác; '
    'đang cáu</div>'
)

B = {
    "docbangmat": 94,
    "loitubat": 1,   # гениальный: viết «-а́льн- GIỮ trọng âm» trong khi trọng âm DỜI (ге́ний → гениа́льный) -> sửa «hút trọng âm về mình»
                     # (ngoài ra: ví dụ «жале́ть о проше́дшем» gượng -> «о про́шлом»; câu изме́на lủng củng — văn phong, không đếm)
    "nguonsai": 2,   # Vietnamese cũ sai: верность «sự trung thực» (= честность, không phải fidelity);
                     # нежный «non nớt» (= immature, không phải delicate)
    "baolen": [
        "VA CHẠM ощути́ть ↔ почу́вствовать [k88, đã nạp, mồ côi]: gỡ bằng V của lô này — ощутить = «cảm thấy, "
        "cảm nhận được, nhận thấy» (đổi «cảm nhận» -> «cảm nhận được» = to sense, thể HT; «nhận ra» -> «nhận thấy» "
        "vì gloss chỉ có feel/sense). Hết va chạm THEO MÁY (chuỗi), nhưng về NGHĨA hai từ vẫn gần như đồng nghĩa: "
        "nhìn đề «cảm nhận, cảm thấy» của почувствовать user vẫn có thể gõ ощутить. Gỡ thật phải sửa thẻ "
        "почувствовать, vd thêm «chợt cảm thấy, bắt đầu cảm thấy» (gloss của nó có «to start to feel») — ngoài lô, chờ user.",
        "Chỗ KHÔNG chắc: нежный ← не́га (г → ж) đã gắn ⚠️ Mức tin trên thẻ. ненави́деть = не- + на-вид- «ưa nhìn» "
        "ghi KHÔNG kèm Mức tin (Vasmer/Wiktionary đều nhận *ne-naviděti) — luồng chính muốn chặt thì hạ thêm.",
        "Cố ý KHÔNG nối ощути́ть với чу́вство/чу́ять (từ nguyên tôi không chắc) — chẻ ощут- như thẻ ощуще́ние [k159].",
        "V cần duyệt (5): ощутить (như trên) · догадываться thêm «phỏng đoán, ngờ ngợ» (gloss surmise/suspect) · "
        "нежный «non nớt» -> «mỏng manh» · верность «sự trung thực» -> «sự chung thuỷ, sự đúng đắn» · "
        "логика bỏ «lô-gic» (lặp đúng «logic»).",
    ],
}
