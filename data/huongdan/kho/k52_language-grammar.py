# -*- coding: utf-8 -*-
"""k52 — language-grammar: hai chỗ chính tả tiếng Nga gặp nhau trong một lô —
dấu cứng `ъ` ở ranh giới tiền tố/gốc (об-, под-, раз-, с- + е/ё/я), và nhóm
âm rít `ч/щ` cuối từ, với thói quen dời trọng âm sang đuôi ngay khi thêm cách."""

S = {}
V = {}

# ---------------------------------------------------------------- đuôi rít ч/щ

S["врач"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вр-</span>'
    '<span class="hd-gloss">gốc cổ «nói, đọc lời chú»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ч</span>'
    '<span class="hd-gloss">hậu tố NGƯỜI LÀM NGHỀ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thầy lang Nga xưa chữa bệnh bằng lời chú, nên «người nói» '
    'thành «thầy thuốc». Hậu tố <b>-а́ч</b> mở khoá cả một lớp tên nghề và luôn '
    'kéo trọng âm về phía mình.</div>'
    '<div class="hd-warn">⚠️ Mức tin: cách chẻ вр- + -а́ч và mối nối với <b>врать</b> '
    '«nói dối» đều là từ nguyên, không phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>труба́ч</b> người thổi kèn · <b>скрипа́ч</b> người kéo vĩ cầm '
    '· <b>враче́бный</b> thuộc về y</div>'
    '<div class="hd-why">Chú ý bảng chia: chỉ mình dạng trần <b>врач</b> giữ trọng âm ở '
    'gốc; hễ thêm đuôi là trọng âm dời hẳn ra sau rồi ở lì đó — <b>врача́, врачу́, '
    'врачи́, враче́й</b>.</div>'
)

S["грач"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — từ tượng thanh một khối, dựng thẳng từ tiếng '
    '«гра-гра» của bầy quạ.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Loài quạ đen về làm tổ sớm nhất trong năm, nên với người Nga '
    '<b>грачи́</b> bay về là mùa xuân đã tới — bức tranh <b>Грачи́ прилете́ли</b> ai '
    'cũng biết.</div>'
    '<div class="hd-warn">⚠️ Khác <b>врач</b> «bác sĩ» đúng một chữ đầu, mà hai từ lại '
    'chia y hệt nhau — nhìn kỹ chữ đầu.</div>'
    '<div class="hd-why">Chú ý bảng chia: thêm đuôi là trọng âm dời hẳn ra sau — '
    '<b>грача́, грачу́, грачи́, граче́й</b>.</div>'
)

S["луч"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">луч-</span>'
    '<span class="hd-gloss">gốc «sáng» (một khối)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Gốc Ấn–Âu «sáng», cùng nhà với Latin <i>lux</i> và tiếng Anh '
    '<i>lucid, translucent</i>. Nên đây là một VỆT sáng có hướng — tia nắng, chùm đèn '
    '— chứ không phải ánh sáng nói chung.</div>'
    '<div class="hd-warn">⚠️ Đừng lẫn với <b>лу́чший</b> «tốt hơn cả»: trông giống mà '
    'khác gốc hoàn toàn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>излуче́ние</b> bức xạ · <b>лучево́й</b> thuộc về tia · '
    '<b>лучи́стый</b> rạng rỡ</div>'
    '<div class="hd-why">Chú ý bảng chia: trọng âm dời sang đuôi ngay từ cách 2 và ở '
    'đó suốt bảng — <b>луча́, лучу́, лучи́, луче́й</b>.</div>'
)

S["плач"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">плак-/плач-</span>'
    '<span class="hd-gloss">gốc «khóc», к đổi thành ч</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ trần dựng thẳng từ <b>пла́кать</b>, chữ к đổi thành ч '
    'đúng luật biến âm г/к/х → ж/ч/ш. Nghĩa là tiếng khóc kéo dài, trang trọng hơn '
    'động từ đời thường.</div>'
    '<div class="hd-warn">⚠️ <b>плач</b> giữ trọng âm ở gốc suốt bảng (<b>пла́ча, '
    'пла́чем</b>), còn <b>плащ</b> «áo mưa» lại dời sang đuôi (<b>плаща́</b>) — nghe '
    'gần giống nhau mà chia khác hẳn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пла́кать</b> khóc · <b>пла́кса</b> đứa mít ướt · '
    '<b>опла́кивать</b> than khóc ai đó</div>'
)

S["плащ"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">плащ-</span>'
    '<span class="hd-gloss">gốc «tấm vải dẹt» (một khối)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nguyên là tấm vải PHẲNG khoác lên vai, nay là áo mưa dài có '
    'mũ. Chỉ khác <b>плач</b> «tiếng khóc» ở chữ cuối, mà щ đọc mềm và dài hơn ч.</div>'
    '<div class="hd-warn">⚠️ Mức tin: nối <b>плащ</b> với <b>пло́ский</b> «phẳng» và '
    '<b>пло́щадь</b> «quảng trường» là từ nguyên (chung gốc «dẹt, trải rộng»), không '
    'phải luật suy ra được.</div>'
    '<div class="hd-why">Chú ý bảng chia: trọng âm dời sang đuôi ngay từ cách 2 — '
    '<b>плаща́, плащу́, плащи́, плаще́й</b>.</div>'
)

S["хвощ"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">хвост-</span>'
    '<span class="hd-gloss">gốc «cái đuôi»</span></div>'
    '<div class="hd-row"><span class="hd-piece">ст → щ</span>'
    '<span class="hd-gloss">biến âm khi thêm đuôi</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cây mọc từng đốt, nhánh xoè ra như chùm lông ĐUÔI ngựa — '
    'tiếng Việt gọi đúng như vậy. Phép biến âm ст → щ còn gặp lại nhiều lần '
    '(<b>пусти́ть</b> → <b>пущу́</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>хвост</b> cái đuôi · <b>хво́стик</b> đuôi nhỏ, kiểu tóc '
    'buộc túm</div>'
    '<div class="hd-why">Chú ý bảng chia: trọng âm dời sang đuôi ngay từ cách 2 — '
    '<b>хвоща́, хвощу́, хвощи́, хвоще́й</b>.</div>'
)

S["щит"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">щит-</span>'
    '<span class="hd-gloss">gốc «che chắn» (một khối)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhớ ngược từ chỗ hay gặp hơn: за + щит = đứng SAU tấm khiên, '
    'ra <b>защи́та</b> «sự bảo vệ». Nghĩa mở rộng đi theo hình dáng tấm phẳng lớn: '
    'bảng quảng cáo, bảng điện.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>защи́та</b> sự bảo vệ · <b>защища́ть</b> bảo vệ · '
    '<b>защи́тник</b> người che chắn, hậu vệ</div>'
    '<div class="hd-why">Chú ý bảng chia: trọng âm dời sang đuôi từ cách 2 '
    '(<b>щита́, щиты́</b>); riêng số nhiều cách 2 lấy đuôi cứng <b>щито́в</b>, không '
    'phải -е́й như <b>луч</b>, <b>врач</b>.</div>'
)

S["щи"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được — từ một khối rất cổ, vỏn vẹn một âm tiết.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Món súp bắp cải quốc dân. Tiếng Nga bắt nó luôn đứng ở số '
    'nhiều: <b>щи горя́чие</b> «súp còn nóng». Cách 2 là <b>щей</b> — một trong những '
    'dạng ngắn nhất tiếng Nga.</div>'
    '<div class="hd-warn">⚠️ Không có dạng số ít, nên mọi tính từ và động từ đi kèm '
    'đều phải chia số nhiều.</div>'
)

S["щука"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">щу́к-</span>'
    '<span class="hd-gloss">gốc, không chẻ nhỏ hơn được</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cá săn mồi mõm nhọn răng sắc, kẻ dữ nhất ao hồ Nga. Trong cổ '
    'tích đây là con cá biết nói: <b>По щу́чьему веле́нию</b> «theo lệnh cá chó» là câu '
    'thần chú ai cũng thuộc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>щу́чий</b> thuộc về cá chó — chính dạng tính từ nằm trong '
    'câu thần chú trên</div>'
)

S["щётка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">щёт-</span>'
    '<span class="hd-gloss">gốc «lông cứng»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">hậu tố TÊN ĐỒ VẬT</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Bàn chải chính là túm lông cứng cắm vào cán — <b>щети́на</b> '
    'là lông lợn rừng, thứ người ta vẫn dùng làm nó. Đuôi -ка biến gốc thành tên đồ '
    'dùng, y như <b>ру́чка</b> cái bút, <b>ви́лка</b> cái nĩa.</div>'
    '<div class="hd-warn">⚠️ Cụm phải thuộc: <b>зубна́я щётка</b> «bàn chải đánh răng».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>щети́на</b> lông cứng, râu lởm chởm · <b>щети́нистый</b> tua tủa</div>'
    '<div class="hd-why">Chú ý bảng chia: ё luôn mang trọng âm nên cả bảng đứng yên ở '
    'щё-; chỗ duy nhất đổi mặt chữ là số nhiều cách 2, chèn thêm о cho đọc được — '
    '<b>щёток</b>.</div>'
)

S["защита"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">chắn ra phía trước</span></div>'
    '<div class="hd-row"><span class="hd-piece">-щи́т-</span>'
    '<span class="hd-gloss">tấm khiên</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đứng sau tấm <b>щит</b> mà đỡ đòn thay người khác. Cùng khuôn '
    'này có <b>защи́тник</b> — hậu vệ bóng đá, đúng nghĩa «người đứng chắn».</div>'
    '<div class="hd-warn">⚠️ Cặp thể: <b>защища́ть</b> (chưa hoàn thành) / '
    '<b>защити́ть</b> (hoàn thành). Chuyển thể thì т của <b>щит</b> hoá thành щ — nhớ '
    'mặt chữ này để khỏi viết sai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>щит</b> tấm khiên · <b>защища́ть</b> bảo vệ · '
    '<b>защи́тник</b> hậu vệ · <b>беззащи́тный</b> không ai che chở</div>'
)

S["пощада"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố thể, KHÔNG mang nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ща́д-</span>'
    '<span class="hd-gloss">gốc «nương tay, tha»</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Toàn bộ nghĩa nằm ở gốc щад- (<b>щади́ть</b> «nương tay với '
    'ai»); по- chỉ đánh dấu làm một lần cho xong. Từ này hầu như luôn xuất hiện ở '
    'dạng phủ định.</div>'
    '<div class="hd-warn">⚠️ Chỗ gặp thật: <b>без поща́ды</b> «không thương tiếc» và '
    '<b>беспоща́дный</b> «tàn nhẫn».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>щади́ть</b> nương tay · <b>пощади́ть</b> tha cho · '
    '<b>беспоща́дный</b> tàn nhẫn</div>'
)

S["помощь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мощь</span>'
    '<span class="hd-gloss">gốc «sức, khả năng»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đem cái sức mình có mà cho người khác. Chữ щ là dạng Slav cổ '
    'của ч trong <b>мочь</b> «có thể» — đó là lý do <b>помога́ть</b> viết г mà '
    '<b>по́мощь</b> viết щ, cùng một gốc hai lớp áo.</div>'
    '<div class="hd-warn">⚠️ <b>по́мощь</b> (danh từ, trọng âm đầu) khác <b>помо́чь</b> '
    '(động từ «giúp», trọng âm sau) — đặt sai trọng âm là sai luôn từ loại.</div>'
    '<div class="hd-warn">⚠️ Cụm phải thuộc: <b>пе́рвая по́мощь</b> «sơ cứu».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>помога́ть</b> giúp đỡ · <b>мо́щный</b> mạnh mẽ · '
    '<b>возмо́жно</b> có thể</div>'
)

# -------------------------------------------------- dấu cứng ъ sau tiền tố

S["объявить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">ra khắp xung quanh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ъяв-</span>'
    '<span class="hd-gloss">gốc «làm lộ ra» (<b>я́вный</b> rõ ràng)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm cho một việc lộ ra trước mọi người → tuyên bố. Dấu cứng ъ '
    'đứng đây chỉ vì tiền tố об- tận cùng bằng phụ âm mà gốc lại mở đầu bằng я — cả '
    'lô này đều chung một luật đó.</div>'
    '<div class="hd-warn">⚠️ Cặp thể: <b>объявля́ть</b> (chưa hoàn thành) / '
    '<b>объяви́ть</b> (hoàn thành). Đòi cách 3 cho người nghe và о + cách 6 cho nội '
    'dung: <b>объяви́ть кому́ о чём</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>объявле́ние</b> thông báo · <b>я́вный</b> rõ ràng · '
    '<b>появи́ться</b> xuất hiện · <b>заявле́ние</b> đơn từ</div>'
    '<div class="hd-why">Chú ý bảng chia: chỉ ngôi «tôi» chèn thêm л và giữ trọng âm ở '
    'đuôi — <b>объявлю́</b>; từ ngôi hai trở đi л biến mất và trọng âm lùi về gốc: '
    '<b>объя́вишь, объя́вит, объя́вят</b>.</div>'
)

S["объявление"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">объяв-</span>'
    '<span class="hd-gloss">từ <b>объяви́ть</b> tuyên bố</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ле́ние</span>'
    '<span class="hd-gloss">hậu tố danh từ hoá → giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hành động <b>объяви́ть</b> đóng gói lại thành sự vật: tờ giấy '
    'thông báo. Đuôi -ение đã tự nói đây là giống trung; còn dấu ъ thì thừa hưởng '
    'nguyên xi từ động từ mẹ.</div>'
    '<div class="hd-warn">⚠️ Chỗ gặp nhiều nhất: <b>дать объявле́ние</b> «đăng tin rao '
    'vặt».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>объяви́ть</b> tuyên bố · <b>заявле́ние</b> đơn từ · '
    '<b>явле́ние</b> hiện tượng</div>'
)

S["объём"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">об-</span>'
    '<span class="hd-gloss">bao quanh</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ъём</span>'
    '<span class="hd-gloss">gốc «lấy vào, chứa»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái mà một vật ôm quanh và chứa được → thể tích, dung tích; '
    'nghĩa bóng là khối lượng công việc. об- gặp ё nên phải có ъ chen vào ngăn.</div>'
    '<div class="hd-warn">⚠️ <b>объём</b> đo thứ KHÔNG đếm được (nước, công việc, thông '
    'tin); thứ đếm được thì dùng <b>коли́чество</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>подъём</b> sự nâng lên · <b>разъём</b> giắc cắm · '
    '<b>приём</b> sự tiếp nhận · <b>объя́ть</b> ôm trọn</div>'
)

S["подъём"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span>'
    '<span class="hd-gloss">từ dưới lên</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ъём</span>'
    '<span class="hd-gloss">gốc «nâng, lấy» (<b>подня́ть</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Danh từ của <b>подня́ть</b>. Nghĩa nào cũng là một mũi tên ĐI '
    'LÊN: leo dốc, thức dậy khỏi giường, kinh tế tăng trưởng, tinh thần phấn chấn.</div>'
    '<div class="hd-warn">⚠️ <b>Подъём!</b> là khẩu lệnh «Dậy!» trong quân đội và trại hè.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>подня́ть</b> nâng lên · <b>поднима́ться</b> đi lên · '
    '<b>объём</b> thể tích · <b>разъём</b> giắc cắm</div>'
)

S["подъезд"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span>'
    '<span class="hd-gloss">tới sát</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ъе́зд</span>'
    '<span class="hd-gloss">gốc «đi xe» (<b>е́здить</b>, <b>по́езд</b>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỗ cỗ xe chạy tới sát cửa nhà. Dấu ъ giữ cho е vẫn đọc thành '
    '«ye» chứ không dính vào д. Nghĩa hiện đại mới là nghĩa hay dùng: cả cái sảnh và '
    'cầu thang chung của một chung cư Nga.</div>'
    '<div class="hd-warn">⚠️ Địa chỉ Nga đọc theo số này: <b>Я живу́ в тре́тьем '
    'подъе́зде</b> «tôi ở lối vào số 3».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>е́здить</b> đi xe · <b>по́езд</b> tàu hoả · '
    '<b>прие́зд</b> sự đến nơi · <b>съезд</b> đại hội</div>'
)

S["разъезд"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span>'
    '<span class="hd-gloss">tản ra mọi phía</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ъе́зд</span>'
    '<span class="hd-gloss">gốc «đi xe»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">раз- luôn là động tác tách ra; ghép với «đi xe» thành cảnh mỗi '
    'người lên xe một ngả. Nghĩa dùng nhiều nhất lại là chuyện đi công tác liên miên, '
    'nay đây mai đó.</div>'
    '<div class="hd-warn">⚠️ Gần như luôn gặp ở số nhiều cách 6: <b>быть в '
    'разъе́здах</b> «đi lại suốt, công tác liên tục».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>разъе́хаться</b> mỗi người một ngả · <b>съезд</b> đại hội · '
    '<b>подъе́зд</b> lối vào · <b>е́здить</b> đi xe</div>'
)

S["разъём"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">раз-</span>'
    '<span class="hd-gloss">tách rời ra</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ъём</span>'
    '<span class="hd-gloss">gốc «lấy, cầm»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chỗ tháo rời ra được rồi cắm lại → giắc cắm, cổng kết nối. Từ '
    'kỹ thuật mới, nhưng dựng đúng khuôn cũ <b>объём</b> · <b>подъём</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>разъедини́ть</b> tách rời · <b>объём</b> thể tích · '
    '<b>подъём</b> sự nâng lên</div>'
)

S["съезд"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">с-</span>'
    '<span class="hd-gloss">dồn về một chỗ / xuống khỏi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ъезд</span>'
    '<span class="hd-gloss">gốc «đi xe»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tiền tố с- chỉ có một chữ cái mà vẫn phải có ъ, vì е đứng ngay '
    'sau. Hai nghĩa đi theo đúng hai nghĩa của с-: người từ khắp nơi ĐỔ VỀ → đại hội; '
    'xe ĐI XUỐNG khỏi đường lớn → lối rẽ ra.</div>'
    '<div class="hd-warn">⚠️ <b>съезд</b> «dồn về» ngược hẳn <b>разъе́зд</b> «tản ra» — '
    'chỉ khác nhau ở tiền tố.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>съе́хаться</b> tụ về · <b>съе́хать</b> trượt xuống · '
    '<b>разъе́зд</b> sự tản đi · <b>по́езд</b> tàu hoả</div>'
)

# ------------------------------------------------------------------ đề bài 1-go
# Chỉ những từ mà dòng tiếng Việt cũ còn cho ra nhiều hơn MỘT đáp án đúng,
# hoặc dịch sai hẳn loài/nghĩa. Không ghi từ loại/giống — mặt thẻ đã có badge.

# "chim sáo" là DỊCH SAI: chim sáo là скворец. грач là loài quạ đen (rook).
V['грач'] = 'chim rook, quạ đen'

# "áo choàng" đụng пальто, шуба — chốt lại đúng một hình ảnh.
V["плащ"] = "áo mưa dài có mũ, áo khoác đi mưa"

# "bảng quảng cáo" đụng проспект; giữ nghĩa cốt lõi cho khỏi hai đáp án.
V['щит'] = 'tấm khiên, lá chắn, bảng'

# từ chỉ dùng số nhiều — không field nào chứa thông tin này.
V['щи'] = 'súp bắp cải Nga'

V['щётка'] = 'bàn chải, chổi'

# "lòng thương hại" đụng nghĩa жалость; пощада là việc THA, không ra đòn tới cùng.
V['пощада'] = 'sự tha thứ, sự nương tay'

# động từ: diễn thể BẰNG LỜI, không chép nhãn — mặt đề bài đã in badge PERF/IMPF.
V['объявить'] = 'thông báo, tuyên bố'

# "quảng cáo" đụng проспект; đây là tờ/bản thông báo dán lên.
V['объявление'] = 'thông báo, tờ rao vặt, quảng cáo'

# "khối lượng" đụng грамм; объём là sức chứa của thứ không đếm được.
V['объём'] = 'thể tích, dung tích, sức chứa, khối lượng'

# "lối vào" đụng вход; подъезд là cả sảnh + cầu thang chung của chung cư.
V['подъезд'] = 'lối vào chung cư, sảnh cầu thang'

# ba nghĩa rời rạc không cho ra một đáp án — gom về một hình ảnh chung "đi lên".
V['подъём'] = 'sự đi lên, sự leo dốc, sự thức dậy, sự tăng trưởng'

V['разъезд'] = 'sự tản đi mỗi người một ngả, việc đi công tác, ga tránh tàu'

V['съезд'] = 'đại hội, lối rẽ xuống'

# "tiếng khóc" đụng рёв «tiếng khóc thét» — tách bằng sắc thái.
V['плач'] = 'sự khóc, tiếng khóc'
