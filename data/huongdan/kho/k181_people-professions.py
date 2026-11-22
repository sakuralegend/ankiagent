# -*- coding: utf-8 -*-
"""k181 — people::professions (lô trộn): thân thể, đạo, nghề, nơi làm việc.

Chỗ cần nhất quán trong lô:
(1) Bốn từ mượn Tây Âu (коллекти́в, реда́ктор, креди́т, би́блия) — "không chẻ theo tiếng Nga",
    cách nhớ bắc cầu tiếng Anh cùng gốc; профессиона́л cũng mượn nhưng soi được профе́сси-.
(2) Ba danh từ Nga có gốc lộ rõ chẻ đủ mảnh: покло́нник (-клон-), отста́вка (-став-),
    сотру́дничество (со-труд-ник-ество, nối thẻ сотру́дник).
(3) Từ nguyên xa (печень↔печь, ноготь↔nail/нога, гроб↔погребение, крест↔крестьянин)
    đều mang ô "⚠️ Mức tin", không khẳng định.
(4) посети́тель ↔ гость [k74]: ô đỏ tách cách dùng; đề bài Việt bỏ «khách» trơn.
Họ hàng cố ý vắng: không thẻ nào.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "причёска": "kiểu tóc, đầu tóc",                               # hairstyle; «mái tóc» = волосы
    "голый": "trần, trần trụi, khỏa thân, trơ trụi",               # bare; «trơ trọi» = cô đơn, sai nghĩa
    "поклонник": "người hâm mộ, người ái mộ, người theo đuổi, người tôn thờ",  # THIẾU suitor
    "посетитель": "khách tham quan, khách đến thăm, người đến thăm, khách của quán, người truy cập",  # bỏ «khách» trơn (nằm gọn trong гость)
    "библия": "Kinh Thánh",                                       # gloss chỉ «Bible»; bỏ «sách kinh điển»
    "отставка": "sự từ chức, việc thôi chức, sự nghỉ hưu, sự bãi nhiệm",  # THIẾU dismissal/discharge
    "профессионал": "người chuyên nghiệp, dân chuyên nghiệp, người trong nghề",  # «tay nghề cao» không phải danh từ
    "православный": "Chính Thống giáo, thuộc Chính Thống giáo, tín đồ Chính Thống giáo",  # THIẾU believer
    "редактор": "biên tập viên, người biên tập, trình soạn thảo",  # THIẾU text editor (текстовый редактор)
}

# --------------------------------------------------------------------- причёска
S["причёска"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">при-</span>'
    '<span class="hd-gloss">tiền tố của <b>причеса́ть</b> chải cho xong</span></div>'
    '<div class="hd-row"><span class="hd-piece">-чёс-</span>'
    '<span class="hd-gloss">CHẢI — gốc của <b>чеса́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">→ danh từ chỉ kết quả</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chải cho gọn rồi, cái còn lại trên đầu là kiểu tóc. <b>е</b> của '
    '<b>чеса́ть</b> thành <b>ё</b> khi mang trọng âm. Số nhiều cách 2 chen <b>-о-</b>: '
    '<b>причёсок</b>.</div>'
    '<div class="hd-warn"><b>сде́лать причёску</b> — làm tóc (ở tiệm).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>причеса́ться</b> chải đầu · <b>расчёска</b> cái lược · '
    '<b>чеса́ть</b> gãi, chải</div>'
)

# --------------------------------------------------------------------- голый
S["голый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">гол-</span>'
    '<span class="hd-gloss">TRẦN, trụi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Trần» theo nghĩa rộng: người không mặc gì, cây trụi lá, tường trơ. '
    'Dạng ngắn giống cái trọng âm nhảy ra đuôi: <b>гол, гола́, го́ло, го́лы</b>.</div>'
    '<div class="hd-warn"><b>голы́ми рука́ми</b> — tay không (nghĩa đen «bằng tay trần»).</div>'
    '<div class="hd-warn">Dạng ngắn <b>гол</b> trùng mặt chữ với <b>гол</b> «bàn thắng» '
    '(mượn tiếng Anh <i>goal</i>) — hai từ khác hẳn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оголи́ть</b> lột trần, để lộ · <b>гололёд</b> băng trơn mặt '
    'đường · <b>на́голо</b> (cạo) trọc</div>'
)

# --------------------------------------------------------------------- бок
S["бок"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một chữ cho «sườn» của cả người lẫn vật: hông người, mạn thuyền, cạnh '
    'hộp. Số nhiều nhấn đuôi: <b>бока́</b>. Chỉ vị trí thì đuôi <b>-у́</b> có trọng âm: '
    '<b>на боку́</b> nằm nghiêng, <b>в боку́</b> ở hông.</div>'
    '<div class="hd-warn"><b>бок о бок</b> — sát cánh, kề vai (nghĩa đen «hông kề hông»).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сбо́ку</b> ở bên cạnh · <b>бо́ком</b> nghiêng người, đi ngang · '
    '<b>боково́й</b> ở bên hông</div>'
)

# --------------------------------------------------------------------- организм
S["организм"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">орган-</span>'
    '<span class="hd-gloss">CƠ QUAN — thẻ <b>о́рган</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-изм</span>'
    '<span class="hd-gloss">đuôi mượn (= <i>-ism</i>), ở đây KHÔNG phải «chủ nghĩa»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Khối gồm nhiều cơ quan làm việc cùng nhau ⇒ cơ thể, một sinh vật — '
    'như tiếng Anh <i>organism</i>. Trọng âm dời ra cuối: <b>о́рган → органи́зм</b>.</div>'
    '<div class="hd-warn"><b>в органи́зме челове́ка</b> — trong cơ thể người: «cơ thể» kiểu sinh '
    'học, y học. Thân thể nhìn thấy được là <b>те́ло</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>о́рган</b> cơ quan · <b>организа́ция</b> tổ chức · '
    '<b>организова́ть</b> tổ chức (động từ)</div>'
)

# --------------------------------------------------------------------- печень
S["печень"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">печ-</span>'
    '<span class="hd-gloss">NƯỚNG — gốc của <b>печь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ень</span>'
    '<span class="hd-gloss">→ danh từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩa đen «món nướng»: lá gan là phần nội tạng xưa kia đem nướng ăn. '
    'Cùng gốc với <b>пече́нье</b> bánh quy (món nướng) đã học. Giống cái, dù đuôi <b>-ь</b> '
    'không báo trước.</div>'
    '<div class="hd-warn">⚠️ Mức tin: nối với <b>печь</b> «nướng» là từ nguyên, không phải luật '
    'suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>печь</b> nướng; cái lò · <b>пече́нье</b> bánh quy · '
    '<b>печёнка</b> gan (món ăn)</div>'
)

# --------------------------------------------------------------------- ноготь
S["ноготь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>-о-</b> cuối rơi mất khi thêm đuôi: <b>но́готь → но́гтя, но́гтем</b>. '
    'Số nhiều <b>но́гти</b>, nhưng các cách còn lại trọng âm nhảy ra đuôi: <b>ногте́й, '
    'ногтя́м</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: cùng gốc xa với tiếng Anh <i>nail</i>, Đức <i>Nagel</i>, '
    'và có lẽ với <b>нога́</b> (gốc xưa «móng, guốc») — từ nguyên, không phải luật.</div>'
    '<div class="hd-warn"><b>с молоды́х ногте́й</b> — từ thuở nhỏ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ногото́к</b> cái móng nhỏ · <b>нога́</b> chân (gốc xa, xem trên)</div>'
)

# --------------------------------------------------------------------- гроб
S["гроб"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Gốc trơn, không chẻ được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Số nhiều nhấn đuôi: <b>гробы́</b>. Nằm trong quan tài là <b>в гробу́</b> '
    '(đuôi <b>-у́</b> chỉ vị trí). Nghĩa «mồ» là nghĩa cũ, còn trong <b>Гроб Госпо́день</b> '
    'Mộ Chúa. <b>до гро́ба</b> — cho tới chết, suốt đời.</div>'
    '<div class="hd-warn">⚠️ Mức tin: gốc xưa là «đào» (cái hố đào xuống), nên cùng nhà với '
    '<b>погребе́ние</b> — từ nguyên, không phải luật.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гробни́ца</b> lăng mộ · <b>погребе́ние</b> sự chôn cất · '
    '<b>по́греб</b> hầm chứa</div>'
)

# --------------------------------------------------------------------- православный
S["православный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">право-</span>'
    '<span class="hd-gloss">ĐÚNG — như <b>пра́вый</b>, <b>пра́во</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-слав-</span>'
    '<span class="hd-gloss">TÔN VINH — như <b>сла́ва</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ный</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Tôn vinh (Chúa) cho đúng» — dịch từng mảnh tiếng Hy Lạp '
    '<i>orthodox</i>: <i>ortho-</i> đúng = <b>пра́во-</b>, <i>-dox</i> = <b>-сла́в-</b>. '
    'Cũng dùng làm danh từ: <b>правосла́вные</b> các tín đồ. Dạng ngắn '
    '(<b>правосла́вен</b>) hiếm gặp.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>правосла́вие</b> đạo Chính Thống · <b>сла́ва</b> vinh quang · '
    '<b>пра́вый</b> đúng; bên phải · <b>просла́вить</b> làm rạng danh</div>'
)

# --------------------------------------------------------------------- поклонник
S["поклонник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố của <b>поклони́ться</b>, không mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-клон-</span>'
    '<span class="hd-gloss">CÚI, NGHIÊNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ник</span>'
    '<span class="hd-gloss">→ người</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người cúi mình trước ai ⇒ người tôn thờ, nhẹ đi thành người hâm mộ. '
    'Gốc <b>-клон-</b> «nghiêng» cũng nằm trong <b>склоне́ние</b> biến cách: từ «uốn mình» '
    'theo cách.</div>'
    '<div class="hd-warn"><b>у неё мно́го покло́нников</b> — cô ấy có nhiều người theo đuổi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поклони́ться</b> cúi chào · <b>покло́н</b> cái cúi chào · '
    '<b>кла́няться</b> cúi chào (chưa hoàn thành) · <b>наклони́ться</b> cúi xuống</div>'
)

# --------------------------------------------------------------------- крест
S["крест"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn rất sớm (qua tiếng Đức cổ <i>Krist</i> «Chúa Kitô»), không chẻ '
    'được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Trọng âm nhảy ra đuôi ở mọi dạng còn lại: <b>креста́, кресто́м, '
    'кресты́</b>. Hình chữ thập ở đâu cũng là <b>крест</b>: thánh giá, dấu × trên giấy, '
    '<b>кре́стики-но́лики</b> trò X-O.</div>'
    '<div class="hd-warn">⚠️ Mức tin: <b>крестья́нин</b> nông dân (đã học) vốn là '
    '<b>христиани́н</b> «người theo đạo Kitô» — cùng nguồn «Kitô» với <b>крест</b>. Từ nguyên, '
    'không phải luật.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>крести́ть</b> rửa tội · <b>кре́стный оте́ц</b> cha đỡ đầu · '
    '<b>перекрёсток</b> ngã tư (đường cắt chữ thập) · <b>крестья́нин</b> nông dân</div>'
)

# --------------------------------------------------------------------- посетитель
S["посетитель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">посети-</span>'
    '<span class="hd-gloss">ĐẾN THĂM — thân của <b>посети́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-тель</span>'
    '<span class="hd-gloss">→ người làm việc đó</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Khuôn <b>-тель</b> như <b>учи́тель</b>, <b>писа́тель</b>: động từ + '
    '<b>-тель</b> = người làm. Người đến một nơi: bảo tàng, quán, trang web. Sang thể chưa hoàn '
    'thành thì <b>т → щ</b>: <b>посеща́ть</b>.</div>'
    '<div class="hd-warn">Khác <b>гость</b>: <b>гость</b> là khách được mời tới nhà; '
    '<b>посети́тель</b> là người tới một nơi công cộng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>посети́ть</b> thăm · <b>посеща́ть</b> thăm, lui tới · '
    '<b>посеще́ние</b> chuyến thăm, lượt truy cập</div>'
)

# --------------------------------------------------------------------- библия
S["библия"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn Hy Lạp <i>biblia</i> «những cuốn sách», không chẻ theo tiếng '
    'Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc <i>biblio-</i> «sách» với <b>библиоте́ка</b> thư viện (đã học) '
    '— «kho sách». Tiếng Anh: <i>Bible</i>, <i>bibliography</i>. Chỉ Kinh Thánh thì viết hoa.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>библиоте́ка</b> thư viện · <b>библиоте́карь</b> thủ thư · '
    '<b>библиогра́фия</b> thư mục</div>'
)

# --------------------------------------------------------------------- отставка
S["отставка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">от-</span>'
    '<span class="hd-gloss">RỜI RA, ra xa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-став-</span>'
    '<span class="hd-gloss">ĐẶT — như <b>ста́вить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">→ danh từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>отста́вить</b> = đặt sang một bên ⇒ người bị (hoặc tự) đặt ra '
    'ngoài công việc: từ chức, về hưu, bị bãi nhiệm. Số nhiều cách 2 chen <b>-о-</b>: '
    '<b>отста́вок</b>.</div>'
    '<div class="hd-warn"><b>уйти́ в отста́вку</b> — từ chức · <b>в отста́вке</b> — đã về '
    'hưu (quân nhân, quan chức).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ста́вить</b> đặt · <b>отста́вить</b> gác lại · '
    '<b>поста́вить</b> đặt (hoàn thành) · <b>вы́ставка</b> triển lãm</div>'
)

# --------------------------------------------------------------------- коллектив
S["коллектив"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn (Latin <i>collectivus</i> «gom lại»), không chẻ theo tiếng Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc tiếng Anh <i>collect</i>: những người được gom lại làm chung '
    '⇒ tập thể, nhất là tập thể nơi làm việc. Đuôi <b>-и́в</b> ứng với <i>-ive</i>.</div>'
    '<div class="hd-warn">Tiếng Anh <i>collective</i> thường là tính từ; <b>коллекти́в</b> là '
    'DANH TỪ: <b>в на́шем коллекти́ве</b> ở cơ quan chúng tôi. Tính từ là '
    '<b>коллекти́вный</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>коллекти́вный</b> tập thể (tính từ) · <b>колле́кция</b> bộ sưu tập · '
    '<b>коллекционе́р</b> nhà sưu tầm</div>'
)

# --------------------------------------------------------------------- пожарный
S["пожарный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пожар-</span>'
    '<span class="hd-gloss">ĐÁM CHÁY — thẻ <b>пожа́р</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ный</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vốn là tính từ «thuộc đám cháy»; bỏ chữ «người» đi thì tính từ thành '
    'danh từ ⇒ lính cứu hoả. Vì thế chia như tính từ: <b>пожа́рного</b>, <b>пожа́рные</b>. '
    'Tính từ vẫn sống song song: <b>пожа́рная маши́на</b> xe cứu hoả.</div>'
    '<div class="hd-warn"><b>на вся́кий пожа́рный</b> — phòng khi có chuyện, cho chắc '
    '(khẩu ngữ).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пожа́р</b> đám cháy · <b>жар</b> hơi nóng; cơn sốt · '
    '<b>жа́рить</b> rán, chiên · <b>жа́ркий</b> nóng</div>'
)

# --------------------------------------------------------------------- профессионал
S["профессионал"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn (Pháp <i>professionnel</i>), nhưng nhìn ra ngay thân '
    '<b>профе́сси-</b> NGHỀ của <b>профе́ссия</b> đã học.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người làm việc như một nghề thật sự — trái với <b>люби́тель</b> người '
    'nghiệp dư. Trọng âm dồn về cuối: <b>профе́ссия → профессиона́л</b>.</div>'
    '<div class="hd-warn">Danh từ ≠ tính từ: <b>он профессиона́л</b> anh ấy là dân chuyên · '
    '<b>профессиона́льный спорт</b> thể thao chuyên nghiệp.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>профе́ссия</b> nghề nghiệp · <b>профессиона́льный</b> chuyên '
    'nghiệp · <b>профессионали́зм</b> tính chuyên nghiệp</div>'
)

# --------------------------------------------------------------------- сотрудничество
S["сотрудничество"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-труд-</span>'
    '<span class="hd-gloss">LAO ĐỘNG — như <b>труд</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ник-</span>'
    '<span class="hd-gloss">→ người; <b>к → ч</b> trước đuôi sau</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ество</span>'
    '<span class="hd-gloss">→ danh từ chỉ việc, trạng thái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>сотру́дник</b> người cùng lao động (nhân viên, đã học) → việc cùng '
    'lao động ⇒ hợp tác. Khớp từng mảnh với tiếng Anh <i>col-labor-ation</i>.</div>'
    '<div class="hd-warn"><b>сотру́дничество с</b> + cách 5 — hợp tác với ai · '
    '<b>в сотру́дничестве с</b> phối hợp cùng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>труд</b> lao động · <b>сотру́дник</b> nhân viên · '
    '<b>сотру́дничать</b> hợp tác · <b>тру́дный</b> khó · <b>тру́дность</b> khó khăn</div>'
)

# --------------------------------------------------------------------- редактор
S["редактор"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn (Latin <i>redactor</i>), không chẻ theo tiếng Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc tiếng Anh <i>redact</i> «soạn lại văn bản»: người sửa bài '
    'trước khi in ⇒ biên tập viên. Cũng là phần mềm soạn thảo: <b>тексто́вый реда́ктор</b>.</div>'
    '<div class="hd-warn"><b>гла́вный реда́ктор</b> — tổng biên tập. Chỗ họ làm là '
    '<b>реда́кция</b> toà soạn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>реда́кция</b> toà soạn; bản biên tập · <b>редакти́ровать</b> '
    'biên tập</div>'
)

# --------------------------------------------------------------------- кредит
S["кредит"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn (Latin <i>creditum</i> «điều được tin giao»), không chẻ theo '
    'tiếng Nga.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Latin <i>credere</i> «tin»: người ta cho vay vì TIN anh sẽ trả ⇒ '
    'khoản vay, tín dụng. Cùng gốc tiếng Anh <i>credit</i>, nhưng trọng âm ở sau: '
    '<b>креди́т</b>.</div>'
    '<div class="hd-warn"><b>взять креди́т</b> — vay tiền ngân hàng · <b>купи́ть в креди́т</b> — '
    'mua trả góp.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>креди́тный</b> tín dụng (<b>креди́тная ка́рта</b>) · '
    '<b>кредито́р</b> chủ nợ · <b>кре́до</b> tôn chỉ</div>'
)

B = {
    "docbangmat": 73,
    "loitubat": 3,
    "nguonsai": 0,
    "baolen": [
        "Va chạm nghĩa: посетитель «khách» nằm gọn trong гость [k74] — đã gỡ bằng V (bỏ «khách» trơn, liệt kê khách tham quan / khách đến thăm / người đến thăm / khách của quán / người truy cập, KHÔNG ngoặc). Không còn cặp nào trùng HẾT nghĩa mà badge không tách.",
        "Lỗi tự bắt (loitubat=3): организм gloss -изм «khối gồm…» là bịa nghĩa hậu tố → sửa thành «đuôi mượn, không phải chủ nghĩa»; гроб viết «nghĩa mồ chỉ còn trong до гроба» (sai ví dụ) → Гроб Господень; сотрудничество chẻ -ник- mà quên к → ч (-нич-ество).",
        "Cửa TRONG AM LECH báo пода́ть ↔ по́дать: từ điển chỉ có danh từ по́дать «thuế» (đồng tự), không phải nguồn sai — đã BỎ cụm подать в отставку khỏi thẻ отставка thay vì nới MIEN_TRU.",
        "Khớp chuỗi đã kiểm: печень↔печенье CÙNG gốc печь (từ nguyên, ghi ⚠️ Mức tin, có ghép); крест↔крестьянин cùng nguồn «Kitô» (крестьянин < христианин, ghi ⚠️ Mức tin, có ghép); ноготь↔много OAN (không ghép; ноготь ghép nail/нога ở mức tin); пожарный↔пожарить: cùng gốc жар nhưng пожарить = по- + жарить, không phải từ mẹ ⇒ chỉ ghép жар/жарить vào Họ hàng, không ghép пожарить. Cố ý KHÔNG ghép коллега vào коллектив (Latin legare ≠ legere).",
        "Không chắc (mức tin vừa): гроб ↔ погребение/погреб (gốc «đào»); ноготь ↔ нога; на́голо (cạo trọc) trọng âm theo trí nhớ, cửa soát không tra được trạng từ.",
        "V cần duyệt (9 thẻ): причёска (bỏ «mái tóc» = волосы), голый («trơ trọi» → «trơ trụi»), поклонник (THIẾU «người theo đuổi» — suitor), посетитель (va chạm гость), библия (bỏ «sách kinh điển», gloss chỉ Bible), отставка (THIẾU dismissal), профессионал (bỏ «tay nghề cao», «chuyên gia»), православный (THIẾU believer), редактор (THIẾU «trình soạn thảo»). Không viết V cho бок, организм, печень, ноготь, гроб, крест, коллектив, пожарный, сотрудничество, кредит.",
    ],
}
