# -*- coding: utf-8 -*-
"""k152 — people::professions: nghề, chức danh, cơ thể và vài danh từ đời sống.

Chỗ cần nhất quán trong lô:
(1) gốc -я-/-ят- = LẤY, NHẬN — прия́тель, предприя́тие; khớp прия́тный, приня́ть (thẻ cũ).
(2) gốc -чал- = BẮT ĐẦU — нача́льник; khớp нача́ло/нача́ть («на- không mang nghĩa riêng»).
(3) gốc -кус- = CẮN, NẾM — вкус; khớp вку́сный, кусо́к.
(4) gốc бол- = ĐAU — боль; khớp больно́й, больни́ца, боле́ть. бо́льше/большо́й KHÁC gốc.
(5) gốc рос-/раст- = LỚN, MỌC — рост; khớp расти́, вы́расти, взро́слый.
(6) о́рган khớp организа́ция/организова́ть (thẻ cũ: «орган-из- = organ-iz-e»).
(7) từ mượn Latin/Pháp: капита́н, адвока́т, прое́кт, лейтена́нт, аге́нт, да́ма — chẻ theo gốc gốc
    tiếng Anh cùng nguồn, KHÔNG bịa mảnh tiếng Nga.
Họ hàng cố ý vắng: адвока́т, лейтена́нт (từ mượn đứng một mình trong tiếng Nga).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa, ngăn bằng dấu phẩy.
V = {
    "мозг": "não, tủy",                                  # dấu «;» → dấu phẩy
    "орган": "cơ quan",                                  # bỏ ngoặc «(cơ thể, tổ chức)»
    "рост": "sự tăng, tăng trưởng, chiều cao",           # «;» → «,»; THÊM «chiều cao» — gloss «height / stature», nghĩa hằng ngày
    "свадьба": "lễ cưới, đám cưới",                      # «;» → «,»
    "дама": "quý bà, phu nhân, con đầm",                         # bỏ «bà» (trùng бабушка) + «quý bà» (trùng госпожа); xem baolen
    "секс": "tình dục, sex",                             # «;» → «,»
    "святой": "thánh, thánh thiện, thiêng liêng",        # «;» → «,»; «thiêng» → «thiêng liêng»; thêm «thánh» (gloss «Saint»)
    "приятель": "bạn bè, bạn quen",                      # «;» → «,»
    "предприятие": "doanh nghiệp, xí nghiệp",            # «;» → «,»
    "начальник": "thủ trưởng, sếp, cấp trên",                        # bỏ «thủ trưởng» (trùng руководитель); thêm «sếp» (gloss «boss»)
    "капитан": "thuyền trưởng, đội trưởng, đại úy",      # «;» → «,»; thêm «đại úy» (gloss «captain» = cả cấp bậc quân hàm)
    "адвокат": "luật sư bào chữa, người bào chữa",       # «luật sư» trơn trùng юрист; gloss «advocate / defender»
    "проект": "dự án, đồ án",                            # «;» → «,»
    "агент": "đại lý, đặc vụ",                           # «;» → «,»
    "вкус": "vị, khẩu vị, gu",                                    # bỏ «sở thích» (trùng интерес); «;» → «,»
    "немой": "câm, không tiếng",                         # «;» → «,»
    "боль": "cơn đau, nỗi đau",                          # «;» → «,»
}

# ----------------------------------------------------------------- мозг
S["мозг"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — gốc Slav trơn.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa gốc là CHẤT MỀM nằm trong hộp sọ, trong xương ⇒ cả não lẫn tủy: '
    '<b>спинно́й мозг</b> tủy sống. Số nhiều trọng âm nhảy ra đuôi (<b>мозги́</b>), và '
    '«trong não» là <b>в мозгу́</b>, đuôi <b>-у́</b> như <b>в лесу́</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: cùng gốc Ấn-Âu xa với tiếng Anh <i>marrow</i> (tủy) — '
    'từ nguyên, không phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мозгово́й</b> thuộc về não · <b>мозжечо́к</b> tiểu não (г → ж)</div>'
)

# ----------------------------------------------------------------- орган
S["орган"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — mượn Hy Lạp <i>organon</i> «công cụ», '
    'cùng nguồn tiếng Anh <i>organ</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Công cụ» làm một việc riêng ⇒ bộ phận của cơ thể (<b>о́рганы '
    'зре́ния</b> cơ quan thị giác) hoặc của nhà nước (<b>о́рганы вла́сти</b> cơ quan chính quyền).</div>'
    '<div class="hd-warn">Chớ nhầm: <b>о́рган</b> nhấn đầu là cơ quan; <b>орга́н</b> nhấn sau '
    'là cây đàn organ. Mặt chữ y hệt, chỉ khác trọng âm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>организа́ция</b> tổ chức · <b>организова́ть</b> tổ chức · '
    '<b>органи́зм</b> cơ thể sống</div>'
)

# ----------------------------------------------------------------- рост
S["рост"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рост-</span>'
    '<span class="hd-gloss">LỚN, MỌC — cùng gốc <b>расти́</b> (о ↔ а)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái đang LỚN LÊN ⇒ sự tăng (<b>рост цен</b> giá tăng); lớn tới đâu ⇒ '
    'chiều cao của người. Số nhiều hiếm dùng, khi có thì đuôi <b>-а́</b>: <b>роста́</b>.</div>'
    '<div class="hd-warn">Hỏi chiều cao NGƯỜI: <b>Како́й у тебя́ рост?</b> — chiều cao của '
    'vật (núi, nhà) là <b>высота́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>расти́</b> lớn lên · <b>вы́расти</b> lớn lên · '
    '<b>взро́слый</b> người lớn · <b>расте́ние</b> cây cối</div>'
)

# ----------------------------------------------------------------- свадьба
S["свадьба"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">свад-</span>'
    '<span class="hd-gloss">từ <b>сват</b> ông mối (т → д trước б)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ьба</span>'
    '<span class="hd-gloss">đuôi danh từ chỉ việc, như <b>борьба́</b>, <b>судьба́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Việc ông mối se duyên đi tới cùng ⇒ đám cưới. Số nhiều cách 2 chèn '
    '<b>е</b>, rụng <b>ь</b>: <b>сва́деб</b>.</div>'
    '<div class="hd-warn">«Tổ chức đám cưới» người Nga nói «chơi»: <b>сыгра́ть сва́дьбу</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сват</b> ông mối, thông gia · <b>сва́ха</b> bà mối · '
    '<b>сва́дебный</b> thuộc đám cưới</div>'
)

# ----------------------------------------------------------------- дама
S["дама"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ — mượn Pháp <i>dame</i> «quý bà».</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiếng Việt mượn đúng chữ Pháp đó: «bà <u>đầm</u>», «con <u>đầm</u>» '
    'trong bộ bài. Nên <b>да́ма</b> = người phụ nữ lịch sự, và là quân Q trong bộ bài.</div>'
    '<div class="hd-warn">Lời chào mở đầu: <b>Да́мы и господа́!</b> — Thưa quý bà, quý ông!</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>да́мский</b> dành cho phụ nữ (<b>да́мская су́мочка</b> túi xách nữ)</div>'
)

# ----------------------------------------------------------------- секс
S["секс"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ — mượn tiếng Anh <i>sex</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giống hệt tiếng Anh, chỉ có nghĩa «tình dục»; giới tính là <b>пол</b>.</div>'
    '<div class="hd-warn">«Quan hệ tình dục»: <b>занима́ться се́ксом</b> — <b>занима́ться</b> '
    'kéo cách 5.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сексуа́льный</b> gợi cảm, thuộc tình dục</div>'
)

# ----------------------------------------------------------------- ад
S["ад"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ — mượn Hy Lạp <i>Hadēs</i>, cõi người chết.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>ад</b> ← <i>Hades</i>: rụng âm đầu, còn trơ «ad». «Ở dưới địa ngục» '
    'là <b>в аду́</b> (đuôi <b>-у́</b>), còn «nói về địa ngục» thì <b>об а́де</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>а́дский</b> khủng khiếp như địa ngục (<b>а́дская жара́</b> nóng kinh hồn)</div>'
)

# ----------------------------------------------------------------- святой
S["святой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">свят-</span>'
    '<span class="hd-gloss">THÁNH</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ, nhấn đuôi</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đứng trước tên là «thánh»: <b>свята́я вода́</b> nước thánh, '
    '<b>Свято́й Никола́й</b> thánh Nicholas. Dạng ngắn giống cái nhấn đuôi: <b>свят, свята́, свя́то</b>.</div>'
    '<div class="hd-warn"><b>т → щ</b> khi sang từ phái sinh: <b>свят-</b> → <b>свяще́нный</b> '
    'thiêng liêng, <b>свяще́нник</b> linh mục — nhìn khác mà cùng gốc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>свяще́нный</b> thiêng liêng · <b>свяще́нник</b> linh mục · '
    '<b>свя́тость</b> sự thánh thiện</div>'
)

# ----------------------------------------------------------------- приятель
S["приятель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">về phía mình</span></div>'
    '<div class="hd-row"><span class="hd-piece">-я-</span>'
    '<span class="hd-gloss">LẤY, NHẬN — như <b>-я́т-</b> trong <b>прия́тный</b>, <b>приня́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-тель</span>'
    '<span class="hd-gloss">đuôi chỉ người, như <b>учи́тель</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người mình đón nhận về phía mình ⇒ bạn quen, bạn chơi; cùng gốc với '
    '<b>прия́тный</b> «dễ chịu» — người dễ chịu để chơi cùng.</div>'
    '<div class="hd-warn">Thang thân: <b>знако́мый</b> người quen → <b>прия́тель</b> bạn chơi → '
    '<b>друг</b> bạn thân thật sự.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прия́тельница</b> bạn nữ · <b>прия́тный</b> dễ chịu · '
    '<b>приня́ть</b> nhận · <b>предприя́тие</b> doanh nghiệp</div>'
)

# ----------------------------------------------------------------- предприятие
S["предприятие"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пред-</span>'
    '<span class="hd-gloss">TRƯỚC</span></div>'
    '<div class="hd-row"><span class="hd-piece">-при-я-</span>'
    '<span class="hd-gloss">nhận về mình — như <b>приня́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-тие</span>'
    '<span class="hd-gloss">đuôi danh từ, như <b>заня́тие</b>, <b>поня́тие</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đứng ra NHẬN LẤY một việc ⇒ việc mình đảm đương ⇒ cơ sở làm ăn. Cùng '
    'cách ghép với tiếng Anh <i>under-take</i>, tiếng Pháp <i>entre-prise</i> (prendre = lấy).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>предприня́ть</b> tiến hành · <b>предпринима́тель</b> doanh nhân · '
    '<b>прия́тель</b> bạn quen</div>'
)

# ----------------------------------------------------------------- начальник
S["начальник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">на-</span>'
    '<span class="hd-gloss">tiền tố, ở đây KHÔNG mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ча́ль-</span>'
    '<span class="hd-gloss">BẮT ĐẦU — như <b>нача́ло</b>, <b>нача́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ник</span>'
    '<span class="hd-gloss">đuôi chỉ người</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người đứng ở ĐẦU ⇒ sếp, cấp trên trực tiếp. Sếp CỦA cái gì thì theo '
    'cách 2: <b>нача́льник отде́ла</b> trưởng phòng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нача́ло</b> sự bắt đầu · <b>нача́ть</b> bắt đầu · '
    '<b>нача́льный</b> ban đầu · <b>нача́льство</b> ban lãnh đạo</div>'
)

# ----------------------------------------------------------------- капитан
S["капитан"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — từ mượn châu Âu (Ý <i>capitano</i>), gốc '
    'Latin <i>caput</i> «cái đầu»; tiếng Anh <i>captain</i> cùng nguồn.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người đứng ĐẦU ⇒ thuyền trưởng, đội trưởng; trong quân hàm là đại úy, '
    'ngay trên <b>ста́рший лейтена́нт</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>капита́л</b> vốn (cũng từ <i>caput</i>) · <b>капита́льный</b> căn bản '
    '(<b>капита́льный ремо́нт</b> đại tu)</div>'
)

# ----------------------------------------------------------------- адвокат
S["адвокат"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — mượn Latin <i>advocatus</i>: <i>ad-</i> '
    '«tới» + <i>vocare</i> «gọi» (<i>voice</i>), tiếng Anh <i>advocate</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người được GỌI TỚI để nói giúp mình ⇒ luật sư bào chữa trước tòa.</div>'
    '<div class="hd-warn"><b>адвока́т</b> = luật sư đứng ra bào chữa; <b>юри́ст</b> = người làm '
    'nghề luật nói chung.</div>'
)

# ----------------------------------------------------------------- проект
S["проект"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — mượn Latin <i>projectum</i>: <i>pro-</i> '
    '«về phía trước» + <i>jacere</i> «ném»; tiếng Anh <i>project</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ý định «ném ra phía trước» ⇒ dự án, bản thiết kế, bản dự thảo: '
    '<b>прое́кт зако́на</b> dự thảo luật.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>прое́ктор</b> máy chiếu · <b>проекти́ровать</b> thiết kế</div>'
)

# ----------------------------------------------------------------- лейтенант
S["лейтенант"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — mượn Pháp <i>lieutenant</i>: <i>lieu</i> '
    '«chỗ» + <i>tenant</i> «giữ» = người giữ chỗ thay cấp trên.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cấp sĩ quan thấp nhất hay gặp. Thang cấp: <b>лейтена́нт</b> trung úy '
    '→ <b>ста́рший лейтена́нт</b> thượng úy → <b>капита́н</b> đại úy.</div>'
)

# ----------------------------------------------------------------- агент
S["агент"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — mượn Latin <i>agens</i> «người hành động», '
    'tiếng Anh <i>agent</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người làm việc THAY cho ai đó ⇒ đại lý, người môi giới; làm thay cho cơ '
    'quan tình báo ⇒ đặc vụ: <b>секре́тный аге́нт</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>аге́нтство</b> hãng, cơ quan (<b>тураге́нтство</b> công ty du lịch)</div>'
)

# ----------------------------------------------------------------- вкус
S["вкус"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">vào (miệng)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-кус-</span>'
    '<span class="hd-gloss">CẮN, NẾM — như <b>кусо́к</b> miếng</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cắn vào miệng thì biết VỊ; mở rộng ra «vị» trong cách chọn đồ ⇒ gu: '
    '<b>одева́ться со вку́сом</b> ăn mặc có gu.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вку́сный</b> ngon · <b>вку́сно</b> ngon · <b>кусо́к</b> miếng · '
    '<b>куса́ть</b> cắn · <b>безвку́сный</b> nhạt, kém gu</div>'
)

# ----------------------------------------------------------------- немой
S["немой"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">нем-</span>'
    '<span class="hd-gloss">CÂM</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́й</span>'
    '<span class="hd-gloss">đuôi tính từ, nhấn đuôi</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Không nói được ⇒ câm; không có tiếng ⇒ <b>немо́е кино́</b> phim câm. '
    'Dạng ngắn trọng âm ra đuôi: <b>нем, нема́, немы́</b> — <b>нем как ры́ба</b> câm như hến.</div>'
    '<div class="hd-warn">⚠️ Mức tin: <b>не́мец</b> người Đức gốc là «kẻ câm» — người nước ngoài '
    'không nói được tiếng mình. Từ nguyên được chấp nhận rộng, không phải luật.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>не́мец</b> người Đức · <b>неме́цкий</b> thuộc nước Đức · '
    '<b>онеме́ть</b> lặng câm, tê dại</div>'
)

# ----------------------------------------------------------------- боль
S["боль"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бол-</span>'
    '<span class="hd-gloss">ĐAU</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ь</span>'
    '<span class="hd-gloss">đuôi danh từ, ở đây giống CÁI</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc ĐAU trơn, cả đau thân lẫn đau lòng: <b>головна́я боль</b> đau đầu, '
    '<b>си́льная боль</b> cơn đau dữ dội.</div>'
    '<div class="hd-warn">«Tôi đau X» dùng ĐỘNG TỪ, không dùng danh từ: <b>У меня́ боли́т '
    'голова́</b>. Còn <b>бо́льше</b> «nhiều hơn» khác gốc, chỉ trùng mặt chữ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>боле́ть</b> đau, ốm · <b>больно́й</b> ốm, bệnh nhân · '
    '<b>больни́ца</b> bệnh viện · <b>боле́знь</b> bệnh · <b>бо́льно</b> đau</div>'
)

B = {
    "docbangmat": 63,
    "loitubat": 2,
    "nguonsai": 0,
    "baolen": [
        "MIEN_TRU (data/huongdan/mientru.py) THÊM 1 mục «орга́н» — đồng tự thật: орга́н = đàn organ ↔ о́рган = cơ quan, nouns.csv chỉ có о́рган. Thẻ орган cố ý nêu cặp này trong ô đỏ (theo gợi ý luồng chính). Cần luồng chính duyệt; phương án lùi: bỏ in đậm орга́н trong ô đỏ rồi gỡ mục miễn trừ.",
        "V да́ма «phu nhân, con đầm»: bỏ «bà» (trùng ба́бушка) và «quý bà» (trùng госпожа́ «quý bà, quý cô»). Rút gọn thuần thì chỉ còn «con đầm» — quá hẹp so với nghĩa chính «lady», nên tôi THÊM «phu nhân» (không trùng thẻ nào). «phu nhân» trong tiếng Việt hơi nghiêng về «vợ người quyền quý» — cần duyệt. Phương án khác cần luồng chính quyết: trả «quý bà» cho да́ма và đổi госпожа́ sang nghĩa xưng hô («bà, cô» trước họ tên).",
        "V адвока́т «luật sư bào chữa, người bào chữa»: rút gọn «luật sư» thì không còn gì; đổi sang nghĩa hẹp đúng của адвока́т (gloss «advocate / defender»), юри́ст giữ «luật sư» chung — cần duyệt.",
        "V нача́льник «sếp, cấp trên»: bỏ «thủ trưởng» (trùng руководи́тель), thêm «sếp» (gloss «boss»). «cấp trên» trùng ста́рший nhưng badge từ loại tách.",
        "V вкус «vị, gu»: bỏ «sở thích» (trùng интере́с) — rút gọn thuần.",
        "V thêm nghĩa gloss xác nhận: рост + «chiều cao» (height/stature — nghĩa hằng ngày, thẻ cũ thiếu hẳn); капита́н + «đại úy» (captain cũng là quân hàm, lô có лейтена́нт); свято́й + «thánh» (Saint) và «thiêng» → «thiêng liêng». Cả ba cần duyệt vì là thêm chữ, không chỉ bỏ.",
        "V 13 từ còn lại chỉ đổi dấu «;» → «,» hoặc bỏ ngoặc (орган bỏ «(cơ thể, tổ chức)»). ад, лейтенант không đổi.",
        "Đã soi nghĩa mới với ~2731 thẻ (đọc Anki chỉ-đọc, so bằng tach_nghia + đủ 4 badge): không cụm nào trùng.",
        "Máy bắt (không tính vào loitubat): tôi viết предприни́матель, đúng là предпринима́тель — cửa TRONG AM LECH bắt, đã sửa.",
        "Lỗi tự bắt (2): свадьба chẻ «сва-» → đúng là «свад-» (д là т của сват bị hữu thanh hoá trước б); капита́н viết «mượn Ý capitano» như chắc chắn — đường mượn không chắc, hạ thành «từ mượn châu Âu (Ý capitano)».",
        "Không chắc (đã hạ mức tin bằng ô ⚠️): мозг cùng gốc Ấn-Âu với marrow; не́мец ← немо́й «kẻ câm». Viết thẳng vì là từ nguyên chuẩn (Vasmer): сва́дьба ← сват, ад ← Hades, вкус ← в- + кус-, прия́тель ← прия́ть.",
        "Họ hàng cố ý vắng: адвока́т, лейтена́нт (từ mượn đứng một mình). Họ hàng của капита́н (капита́л) là cùng gốc Latin caput, mượn riêng — ghi rõ trên thẻ.",
    ],
}
