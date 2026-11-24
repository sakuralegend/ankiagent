# -*- coding: utf-8 -*-
"""k140 — life::health (lô trộn): chữa bệnh, quần áo, thể thao, thiên nhiên, phố phường.

Chỗ cần nhất quán trong lô:
(1) gốc леч- (← лек- THUỐC, к → ч) = лечить/вылечить, nối лекарство; KHÔNG nối лечь (khác gốc).
(2) gốc -де- = ĐẶT (одевать/одеть) — khớp надевать/надеть (k132): одеть + NGƯỜI, надеть + MÓN ĐỒ;
    thân tương lai mọc -н- (одену ↔ надену).
(3) gốc образ- = HÌNH ẢNH (изображать/изобразить), з → ж ở изображу/изображать.
(4) gốc игр- = CHƠI (проиграть/проигрывать) đối với выиграть: thua КОМУ (C3) ↔ thắng У КОГО (C2).
(5) nguyên âm chạy: кашель → кашля, платок → платка, переулок → переулка, овца → овец.
Họ hàng cố ý vắng: свитер (mượn Anh, đứng một mình).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "изображать": "khắc họa, giả làm, bắt chước",    # RÚT «vẽ» (рисова́ть) + «thể hiện» (пока́зывать); không dùng «đóng vai» — trùng игра́ть
    "изобразить": "khắc họa, giả làm, bắt chước",    # RÚT «vẽ» (нарисова́ть), bỏ «(xong)»
    "одеть": "mặc quần áo cho ai",                    # bỏ «(xong)» — nhãn thể trá hình
    "проиграть": "thua",                              # bỏ «(một lần, xong việc)»
    "проигрывать": "thua",                            # bỏ «(thường xuyên, liên tục)»
    "тренироваться": "tập luyện, rèn luyện",          # «tập dượt» là репети́ровать; chung «tập luyện» với занима́ться là ổn (user duyệt 24/11)
    "платок": "khăn trùm đầu, khăn vuông, khăn tay",  # thiếu nghĩa handkerchief (носово́й плато́к)
}

# --------------------------------------------------------------------- укол
S["укол"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố của <b>уколо́ть</b> chích một cái</span></div>'
    '<div class="hd-row"><span class="hd-piece">-кол</span>'
    '<span class="hd-gloss">gốc ĐÂM, CHÍCH — <b>коло́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Một cái chích» ⇒ mũi tiêm, cũng là vết kim châm. Danh từ giống đực, '
    'chia đều: <b>уко́ла</b>.</div>'
    '<div class="hd-warn">Tiêm cho ai = <b>сде́лать уко́л</b> + cách 3: '
    '<b>Медсестра́ сде́лала мне уко́л.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>коло́ть</b> đâm, chích · <b>уколо́ть</b> chích một cái · '
    '<b>колю́чий</b> có gai</div>'
)

# ------------------------------------------------------------------- кашель
S["кашель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — gốc trơn <b>ка́шл-</b>, giữ nguyên trong '
    '<b>ка́шлять</b> ho.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chữ <b>е</b> chỉ có ở dạng từ điển, rụng khi thêm đuôi: '
    '<b>ка́шель → ка́шля, ка́шлем</b> (như <b>день → дня</b>). Tận cùng <b>-ь</b> nhưng là '
    'giống đực.</div>'
    '<div class="hd-warn">Tôi bị ho = <b>У меня́ ка́шель.</b> (như <b>У меня́ температу́ра.</b>)</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ка́шлять</b> ho · <b>ка́шлянуть</b> ho một tiếng</div>'
)

# ------------------------------------------------------------------- лечить
S["лечить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">леч-</span>'
    '<span class="hd-gloss">gốc THUỐC — <b>лек-</b> như <b>лека́рство</b>, к → ч</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ, chia lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cho thuốc» ⇒ chữa, điều trị — nói quá trình, chưa hứa khỏi. Trọng âm '
    'nhảy: <b>лечу́</b> nhưng <b>ле́чишь, ле́чат</b>. Chữa ai khỏi gì: '
    '<b>лечи́ть кого́ от чего́</b>.</div>'
    '<div class="hd-warn"><b>я лечу́</b> «tôi chữa» trùng mặt chữ với <b>я лечу́</b> «tôi bay» '
    '(<b>лете́ть</b>, т → ч). Ngôi khác thì tách: <b>ле́чишь</b> / <b>лети́шь</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>лека́рство</b> thuốc · <b>лече́ние</b> sự điều trị · '
    '<b>вы́лечить</b> chữa khỏi · <b>лечи́ться</b> đi chữa bệnh</div>'
)

# ----------------------------------------------------------------- вылечить
S["вылечить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы́-</span>'
    '<span class="hd-gloss">RA, làm tới nơi; luôn mang trọng âm</span></div>'
    '<div class="hd-row"><span class="hd-piece">-лечить</span>'
    '<span class="hd-gloss">chữa — <b>лечи́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>лечи́ть</b> = điều trị (đang chữa); thêm <b>вы́-</b> «đưa ra khỏi bệnh» '
    '⇒ chữa KHỎI hẳn. Động từ hoàn thành có <b>вы́-</b> thì trọng âm đóng đinh ở đó: '
    '<b>вы́лечу, вы́лечишь</b>.</div>'
    '<div class="hd-warn"><b>Его́ лечи́ли, но не вы́лечили.</b> = Người ta chữa cho anh ấy, '
    'nhưng không khỏi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>вы́лечиться</b> khỏi bệnh · <b>лечи́ть</b> chữa · '
    '<b>лека́рство</b> thuốc</div>'
)

# --------------------------------------------------------------- изображать
S["изображать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">из-</span>'
    '<span class="hd-gloss">RA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ображ-</span>'
    '<span class="hd-gloss">HÌNH ẢNH — <b>о́браз</b>, з → ж</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đưa ra thành hình ảnh» ⇒ khắc họa bằng nét vẽ, lời văn hay điệu bộ: '
    '<b>Карти́на изобража́ет мо́ре.</b> Chia đều: <b>изобража́ю</b>.</div>'
    '<div class="hd-warn"><b>изобража́ть из себя́</b> + cách 4 = ra vẻ, giả làm: '
    '<b>изобража́ть из себя́ геро́я</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>о́браз</b> hình ảnh · <b>изображе́ние</b> hình ảnh, bức vẽ · '
    '<b>образе́ц</b> mẫu · <b>образова́ние</b> giáo dục</div>'
)

# --------------------------------------------------------------- изобразить
S["изобразить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">из-</span>'
    '<span class="hd-gloss">RA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-образ-</span>'
    '<span class="hd-gloss">HÌNH ẢNH — <b>о́браз</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đưa ra thành hình» ⇒ khắc họa xong. Gốc <b>-образ-</b> lộ nguyên, riêng '
    'ngôi «tôi» đổi з → ж: <b>изображу́</b>, rồi <b>изобрази́шь</b>, <b>изобразя́т</b>. Cặp chưa '
    'hoàn thành: <b>изобража́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>о́браз</b> hình ảnh · <b>изображе́ние</b> bức vẽ · '
    '<b>образе́ц</b> mẫu · <b>образова́ние</b> giáo dục (nghĩa gốc: sự tạo hình)</div>'
)

# ------------------------------------------------------------------ мелодия
S["мелодия"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — mượn gốc Hy Lạp qua châu Âu, chính là '
    '<i>melody</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <b>-ия</b> ⇒ giống cái, như <b>исто́рия</b>. Trọng âm rơi vào âm '
    'giữa: <b>мело́дия</b>, khác chỗ nhấn của <i>mélody</i>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мелоди́чный</b> du dương</div>'
)

# ------------------------------------------------------------------- платок
S["платок"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">плат-</span>'
    '<span class="hd-gloss">TẤM VẢI (từ cổ)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-о́к</span>'
    '<span class="hd-gloss">đuôi thu nhỏ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Tấm vải nhỏ» ⇒ khăn vuông: trùm đầu, choàng vai hay lau tay. <b>о</b> rụng '
    'khi thêm đuôi, trọng âm dồn về đuôi: <b>плато́к → платка́, платко́м</b> (như '
    '<b>звоно́к → звонка́</b>).</div>'
    '<div class="hd-warn"><b>носово́й плато́к</b> = khăn tay (nghĩa đen: khăn cho mũi).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пла́тье</b> váy (cùng gốc «tấm vải») · <b>плато́чек</b> khăn nhỏ</div>'
)

# ------------------------------------------------------------------- свитер
S["свитер"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — mượn tiếng Anh <i>sweater</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giữ trọng âm âm đầu như tiếng Anh: <b>сви́тер</b>; tận cùng phụ âm ⇒ giống '
    'đực. Số nhiều có hai dạng, gặp cái nào cũng đúng: <b>сви́теры</b> (chuẩn) và '
    '<b>свитера́</b> (khẩu ngữ).</div>'
)

# ------------------------------------------------------------------ одевать
S["одевать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">QUANH, bao lấy (một người)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-де-</span>'
    '<span class="hd-gloss">gốc ĐẶT (<b>деть</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва-ть</span>'
    '<span class="hd-gloss">hậu tố chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đặt đồ quanh một người» ⇒ mặc quần áo cho AI ĐÓ. Chia đều: '
    '<b>одева́ю</b>, <b>одева́ешь</b>. Tự mặc cho mình thì thêm <b>-ся</b>: <b>одева́ться</b>.</div>'
    '<div class="hd-warn">Cặp hay nhầm: <b>одева́ть</b> + NGƯỜI (<b>одева́ть ребёнка</b>) · '
    '<b>надева́ть</b> + MÓN ĐỒ (<b>надева́ть пальто́</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оде́жда</b> quần áo · <b>одева́ться</b> mặc đồ · '
    '<b>надева́ть</b> mặc vào · <b>раздева́ть</b> cởi đồ cho ai</div>'
)

# -------------------------------------------------------------------- одеть
S["одеть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">QUANH, bao lấy (một người)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-де-ть</span>'
    '<span class="hd-gloss">gốc ĐẶT (<b>деть</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>одева́ть</b> bỏ <b>-ва-</b> ⇒ hoàn thành: mặc cho ai xong. Thân tương lai '
    'mọc thêm <b>-н-</b>, phải nhớ riêng: <b>оде́ну</b>, <b>оде́нешь</b>, <b>оде́нут</b> — y như '
    '<b>наде́ну</b>.</div>'
    '<div class="hd-warn">Câu người Nga dạy nhau: <b>Оде́ть Наде́жду, наде́ть оде́жду.</b> = mặc cho '
    'NGƯỜI (cô Nadezhda) · mặc MÓN ĐỒ vào.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>одева́ть</b> (chưa hoàn thành) · <b>оде́ться</b> mặc đồ · '
    '<b>оде́жда</b> quần áo · <b>наде́ть</b> mặc vào</div>'
)

# --------------------------------------------------------------- чемпионат
S["чемпионат"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">чемпио́н-</span>'
    '<span class="hd-gloss">NHÀ VÔ ĐỊCH — mượn <i>champion</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́т</span>'
    '<span class="hd-gloss">đuôi danh từ; kéo trọng âm về cuối</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cuộc đấu tìm ra nhà vô địch» ⇒ giải vô địch. Giống đực, chia đều.</div>'
    '<div class="hd-warn"><b>чемпиона́т ми́ра</b> = giải vô địch thế giới. Ở giải dùng <b>на</b>: '
    '<b>на чемпиона́те</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>чемпио́н</b> nhà vô địch · <b>чемпио́нка</b> nữ vô địch</div>'
)

# ---------------------------------------------------------------- проиграть
S["проиграть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">QUA MẤT — làm gì tới mức lỡ, mất (như <b>проспа́ть</b> ngủ quên)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-игра́ть</span>'
    '<span class="hd-gloss">gốc CHƠI — <b>игра́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Chơi tới mất» ⇒ thua. Đối lập <b>вы́играть</b> «chơi mà lấy ra được» = '
    'thắng. Chia đều như <b>игра́ть</b>: <b>проигра́ю</b>.</div>'
    '<div class="hd-warn">Cách lệch nhau: thua AI = <b>проигра́ть кому́</b> (cách 3) · thắng AI = '
    '<b>вы́играть у кого́</b> (у + cách 2).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>игра́ть</b> chơi · <b>вы́играть</b> thắng · '
    '<b>про́игрыш</b> trận thua, tiền thua · <b>игра́</b> trò chơi</div>'
)

# -------------------------------------------------------------- проигрывать
S["проигрывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">QUA MẤT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-игр-</span>'
    '<span class="hd-gloss">gốc CHƠI — <b>игра́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть</span>'
    '<span class="hd-gloss">hậu tố chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thua nhiều lần, hoặc đang thua dần. <b>-ыва-</b> kéo trọng âm về âm đứng '
    'trước: <b>прои́грывать, прои́грываю</b> (như <b>пока́зывать</b>). Đòi cách như '
    '<b>проигра́ть</b>: <b>прои́грывать кому́</b> (cách 3).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>игра́ть</b> chơi · <b>вы́игрывать</b> thắng · '
    '<b>про́игрыш</b> trận thua</div>'
)

# ------------------------------------------------------------ тренироваться
S["тренироваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">трен-</span>'
    '<span class="hd-gloss">TẬP — mượn <i>train</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-иро́ва-ть</span>'
    '<span class="hd-gloss">đuôi động từ mượn</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">cho CHÍNH MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Tự tập cho mình» ⇒ tập luyện (thể thao, kỹ năng). <b>-ова-</b> đổi thành '
    '<b>-у-</b> khi chia: <b>трениру́юсь, трениру́ешься</b>.</div>'
    '<div class="hd-warn">Bỏ <b>-ся</b> là huấn luyện NGƯỜI KHÁC: '
    '<b>Тре́нер трениру́ет кома́нду.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тре́нер</b> huấn luyện viên · <b>трениро́вка</b> buổi tập · '
    '<b>тренирова́ть</b> huấn luyện</div>'
)

# --------------------------------------------------------------------- овца
S["овца"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — gốc trơn rất cổ, họ hàng xa của Latin <i>ovis</i> và '
    'tiếng Anh <i>ewe</i> (cừu cái).</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Số nhiều trọng âm nhảy lên đầu: <b>овца́ → о́вцы</b>. Cách 2 số nhiều chen '
    '<b>е</b>: <b>ове́ц</b> — cũng là cách 4, vì là con vật.</div>'
    '<div class="hd-warn"><b>заблу́дшая овца́</b> = con chiên lạc (người lầm đường).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ове́чка</b> cừu non · <b>ове́чий</b> thuộc về cừu</div>'
)

# ------------------------------------------------------------------ урожай
S["урожай"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">tiền tố của <b>уроди́ться</b> «mọc được, trúng mùa»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-рож-</span>'
    '<span class="hd-gloss">gốc SINH RA — <b>род-</b>, д → ж</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́й</span>'
    '<span class="hd-gloss">đuôi danh từ giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái đất sinh ra được» ⇒ vụ thu hoạch, sản lượng mùa màng. Cùng phép '
    '<b>д → ж</b> như <b>роди́ть → рожа́ть</b>.</div>'
    '<div class="hd-warn"><b>собира́ть урожа́й</b> = thu hoạch (nghĩa đen: gom vụ mùa).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>роди́ться</b> sinh ra · <b>ро́дина</b> quê hương · '
    '<b>урожа́йный</b> bội thu</div>'
)

# ----------------------------------------------------------- землетрясение
S["землетрясение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">земл-е-</span>'
    '<span class="hd-gloss">ĐẤT — <b>земля́</b>; <b>-е-</b> là nguyên âm nối</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тряс-</span>'
    '<span class="hd-gloss">RUNG, LẮC — <b>трясти́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ние</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Sự rung lắc của đất» ⇒ động đất — ghép thẳng, y như tiếng Việt. Từ dài '
    'nhưng không có chỗ nào phải thuộc: chia đều theo <b>-ение</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>земля́</b> đất · <b>трясти́</b> rung, lắc · '
    '<b>тря́ска</b> sự xóc nảy</div>'
)

# -------------------------------------------------------------------- туман
S["туман"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — gốc trơn, nhiều khả năng mượn từ tiếng Turk.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giống đực, chia đều: <b>в тума́не</b> = trong sương mù. Cách 2 đôi khi gặp '
    '<b>тума́ну</b> (khẩu ngữ, «chút sương»), dạng chuẩn vẫn là <b>тума́на</b>.</div>'
    '<div class="hd-warn"><b>как в тума́не</b> = mơ mơ màng màng, không nhớ rõ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тума́нный</b> có sương mù; mơ hồ</div>'
)

# ------------------------------------------------------------------ училище
S["училище"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">уч-</span>'
    '<span class="hd-gloss">HỌC, DẠY — <b>учи́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́лищ-е</span>'
    '<span class="hd-gloss">→ NƠI CHỐN (như <b>храни́лище</b> kho chứa)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Nơi học» ⇒ trường, nhưng là trường trung cấp, dạy nghề: '
    '<b>музыка́льное учи́лище</b>. Đuôi <b>-е</b> ⇒ giống trung.</div>'
    '<div class="hd-warn">Không phải trường phổ thông (<b>шко́ла</b>), cũng không phải đại học '
    '(<b>университе́т</b>) — bậc giữa, học nghề sau lớp 9 hoặc 11.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>учи́ть</b> học, dạy · <b>учи́ться</b> học · '
    '<b>учи́тель</b> giáo viên · <b>учёба</b> việc học</div>'
)

# ----------------------------------------------------------------- переулок
S["переулок"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span>'
    '<span class="hd-gloss">NGANG QUA</span></div>'
    '<div class="hd-row"><span class="hd-piece">-у́л-</span>'
    '<span class="hd-gloss">gốc của <b>у́лица</b> đường phố</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ок</span>'
    '<span class="hd-gloss">đuôi thu nhỏ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đường nhỏ cắt ngang phố» ⇒ hẻm, ngõ. <b>о</b> rụng khi thêm đuôi: '
    '<b>переу́лок → переу́лка, в переу́лке</b>.</div>'
    '<div class="hd-warn"><b>на у́лице</b> nhưng <b>в переу́лке</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>у́лица</b> đường phố · <b>закоу́лок</b> ngõ ngách</div>'
)

B = {
    "docbangmat": 96,
    "loitubat": 1,
    "nguonsai": 1,
    "baolen": [
        "V тренироваться: 'tập luyện' (trùng заниматься) -> 'tập dượt, rèn luyện' — ĐỔI chữ, không rút được vì chỉ có một nghĩa; cần duyệt.",
        "V изображать/изобразить: -> 'khắc họa, giả làm, bắt chước' — thay chữ chứ không chỉ rút; né 'vẽ' (рисовать), 'thể hiện' (показывать), 'đóng vai' (играть), 'miêu tả' (описывать); cần duyệt.",
        "V платок: thêm 'khăn tay' (gloss có handkerchief = носовой платок); cần duyệt.",
        "V проиграть/проигрывать và одевать/одеть: hai vế cặp thể ghi nghĩa y hệt, chỉ badge thể tách (như các cặp k135).",
        "Không chắc (đã hạ mức trong chữ): туман 'nhiều khả năng mượn tiếng Turk'; урожай <- уродиться và платье cùng gốc плат là từ nguyên, khá chắc nhưng không suy ra được.",
        "одеть: ô đỏ dùng câu vần 'Одеть Надежду, надеть одежду' — câu người Nga dạy quy tắc, không phải mnemonic âm; user coi là mnemonic thì bỏ ô đó.",
        "Nguồn sai đã bác: gloss Anh của училище là 'academy' (sai bậc) — giữ nghĩa Việt 'trường trung cấp chuyên nghiệp', thêm ô đỏ phân biệt школа/университет.",
    ],
}
