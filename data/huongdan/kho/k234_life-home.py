# -*- coding: utf-8 -*-
"""k234 — life::home: đồ đạc, chất liệu trong nhà; nửa lô là từ MƯỢN, nửa kia bám gốc đã có thẻ.

Chỗ cần nhất quán với các lô đã nạp:
(1) выключатель: ключ- chìa khoá — khớp ключ k85, включить/выключать k94 · -тель — учитель k36.
(2) гладить/погладить: глад- NHẴN — khớp гладкий k201, утюг k23.
(3) подоконник: ок- MẮT + -но — khớp окно k24; под- DƯỚI — khớp подвал k174, подбородок k216.
(4) пылесос: пыль k183 + сос- HÚT; -е- nối như землетрясение k140, -о- như теплоход k50.
(5) отопление: топ- cùng gốc тёплый k27; п → пл như укрепление k214; KHÔNG dính плен k204.
(6) обои: -бой- cùng gốc бить k02, бой k121 · одеколон ↔ духи k76 · фундамент ↔ основа k156.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài (README §2c): thuần danh sách nghĩa.
V = {
    "таз": "chậu, thau, khung chậu",                      # THIẾU pelvis
    "гель": "gel, chất gel",                              # bỏ «keo» — đó là клей, gloss không có
    "гладить": "vuốt, xoa, âu yếm, ủi, là quần áo",       # THIẾU iron / press
    "погладить": "vuốt, xoa, âu yếm, ủi, là quần áo",     # cùng dãy cặp thể; THIẾU caress
}

# --------------------------------------------------------------------- нитка
S["нитка"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">нит-</span>'
    '<span class="hd-gloss">SỢI — <b>нить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ка</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Sợi chỉ khâu, đi đôi với cây kim: <b>иго́лка с ни́ткой</b> kim chỉ. '
    'Chỉ khâu nói chung thì dùng số nhiều <b>ни́тки</b>; cách 2 số nhiều chen <i>о</i> như '
    '<b>верёвок</b>: <b>ни́ток</b>.</div>'
    '<div class="hd-warn"><b>ни́тка</b> là sợi chỉ cầm được; <b>нить</b> trang trọng hơn, hay dùng '
    'nghĩa bóng: <b>потеря́ть нить разгово́ра</b> mất mạch câu chuyện.</div>'
    '<div class="hd-warn"><b>промо́кнуть до ни́тки</b> — ướt «tới tận sợi chỉ» = ướt sũng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нить</b> sợi, mạch · <b>ни́точка</b> sợi chỉ nhỏ</div>'
)

# ----------------------------------------------------------------- отопление
S["отопление"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">KHẮP, trùm cả chỗ</span></div>'
    '<div class="hd-row"><span class="hd-piece">-топ-л-</span>'
    '<span class="hd-gloss">ĐUN, SƯỞI — <b>топи́ть</b>; <i>п</i> thêm <i>л</i> như '
    '<b>укрепле́ние</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е́ние</span>'
    '<span class="hd-gloss">→ danh từ giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Sự sưởi khắp nhà» ⇒ hệ thống sưởi. Gốc <i>топ-</i> cùng nhà với '
    '<b>тёплый</b> ấm: đun là làm cho ấm. Đầu mùa lạnh ai cũng nói: '
    '<b>Включи́ли отопле́ние!</b> Có sưởi rồi!</div>'
    '<div class="hd-warn"><b>топи́ть</b> có hai nghĩa: đốt lò, sưởi (<b>топи́ть печь</b>) và '
    'nhấn chìm (cặp với <b>тону́ть</b> chìm). Từ này thuộc nghĩa SƯỞI.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>топи́ть</b> đốt lò, sưởi · <b>то́пливо</b> nhiên liệu · '
    '<b>отопи́тельный сезо́н</b> mùa sưởi · <b>тёплый</b> ấm · <b>тепло́</b> hơi ấm</div>'
)

# ----------------------------------------------------------------------- таз
S["таз"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn từ các thứ tiếng Turk (<i>tas</i> = chậu).</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cái chậu to, nông để giặt, rửa. Khung xương hông trông như cái chậu nên cũng '
    'gọi là <b>таз</b> — y hệt tiếng Việt «khung CHẬU», và <i>pelvis</i> trong tiếng Latin cũng '
    'nghĩa là cái chậu.</div>'
    '<div class="hd-warn">Trọng âm: số ít ở gốc (<b>та́за</b>, <b>та́зом</b>), số nhiều ra đuôi '
    '(<b>тазы́</b>, <b>тазо́в</b>). Sau <i>в</i> dùng đuôi riêng <i>-у́</i>: <b>в тазу́</b> '
    'trong chậu — như <b>в бою́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>та́зик</b> chậu nhỏ · <b>та́зовый</b> thuộc khung chậu</div>'
)

# ---------------------------------------------------------------------- обои
S["обои"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">= об- BAO QUANH (<i>б</i> nhập vào <i>б</i> của gốc)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бо(й)-</span>'
    '<span class="hd-gloss">ĐÁNH, ĐÓNG — <b>бить</b>, <b>бой</b> (и ↔ ой)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и</span>'
    '<span class="hd-gloss">đuôi SỐ NHIỀU</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Xưa người ta ĐÓNG đinh vải bọc QUANH tường (<b>оби́ть</b> bọc); nay là giấy '
    'dán. Chỉ có số nhiều, như <b>брю́ки</b>; đếm theo cuộn: <b>два руло́на обо́ев</b>.</div>'
    '<div class="hd-warn">Dán giấy dán tường: <b>кле́ить обо́и</b>; dán cho cả phòng: '
    '<b>окле́ить ко́мнату обо́ями</b> (cách 5).</div>'
    '<div class="hd-warn">Cách 2 là <b>обо́ев</b>. Đừng lẫn với <b>обо́их</b> — cách 2 của '
    '<b>о́ба</b> cả hai.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оби́ть</b> bọc, đóng bọc · <b>бить</b> đánh · <b>бой</b> trận đánh</div>'
)

# ---------------------------------------------------------------- подоконник
S["подоконник"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">под-</span>'
    '<span class="hd-gloss">DƯỚI — như <b>подва́л</b>, <b>подборо́док</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-окон-</span>'
    '<span class="hd-gloss">CỬA SỔ — <b>окно́</b>; <i>о</i> bật lên như ở <b>о́кон</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ник</span>'
    '<span class="hd-gloss">hậu tố chỉ VẬT, giống đực</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái nằm DƯỚI cửa sổ» ⇒ bệ cửa sổ. Viết hai <i>н</i>: một của '
    '<b>окно́</b>, một của <i>-ник</i>. Đặt lên đó dùng <i>на</i>: <b>цветы́ на подоко́ннике</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>окно́</b> cửa sổ · <b>око́шко</b> cửa sổ nhỏ, ô cửa giao dịch · '
    '<b>очки́</b> kính mắt (gốc <i>ок-</i> MẮT)</div>'
)

# ------------------------------------------------------------------ одеколон
S["одеколон"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Mượn nguyên khối tiếng Pháp <i>eau de Cologne</i> «nước của thành phố Köln» — '
    'đừng thấy <i>оде-</i> mà nối với <b>оде́жда</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đọc lại từng khúc: <i>о</i> (eau, nước) + <i>де</i> (de, của) + '
    '<i>колон</i> (Cologne). Tiếng Nga dính cả ba làm một danh từ giống đực, chia đều: '
    '<b>па́хнуть одеколо́ном</b> có mùi nước thơm.</div>'
    '<div class="hd-warn"><b>духи́</b> (chỉ số nhiều) là nước hoa đậm, quen dùng cho nữ; '
    '<b>одеколо́н</b> loãng hơn, thường là đồ của đàn ông, xức sau khi cạo râu.</div>'
)

# --------------------------------------------------------------------- бетон
S["бетон"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn tiếng Pháp <i>béton</i> — chính là chữ «bê tông» của '
    'tiếng Việt.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Một từ, hai thứ tiếng cùng mượn, nên nghe là nhận ra. Gốc xa là Latin '
    '<i>bitumen</i> nhựa đường. Là chất liệu nên thường dùng số ít.</div>'
    '<div class="hd-warn">Đừng suy từ tiếng Anh <i>concrete</i>: <b>конкре́тный</b> chỉ là «cụ thể», '
    'không bao giờ là bê tông.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>бето́нный</b> bằng bê tông · <b>железобето́н</b> bê tông cốt thép '
    '(<b>желе́зо</b> sắt)</div>'
)

# ------------------------------------------------------------------- пылесос
S["пылесос"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пыл-</span>'
    '<span class="hd-gloss">BỤI — <b>пыль</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-е-</span>'
    '<span class="hd-gloss">nguyên âm nối, vì <i>ль</i> mềm (<b>теплохо́д</b>: <i>л</i> cứng → '
    '<i>-о-</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сос</span>'
    '<span class="hd-gloss">HÚT — <b>соса́ть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái hút bụi» ⇒ máy hút bụi, ghép y như tiếng Việt. <b>пыль</b> giống cái, '
    'nhưng giống của từ ghép theo mảnh CUỐI <i>-сос</i> ⇒ giống đực.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пыль</b> bụi · <b>пылесо́сить</b> hút bụi · <b>соса́ть</b> mút, hút · '
    '<b>насо́с</b> máy bơm · <b>со́ска</b> núm vú giả. Không cùng gốc: <b>соси́ска</b> xúc xích '
    '(mượn tiếng Pháp)</div>'
)

# ----------------------------------------------------------------- фундамент
S["фундамент"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ trong tiếng Nga — mượn Latin <i>fundamentum</i>, từ <i>fundus</i> '
    '«đáy».</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc tiếng Anh <i>fundamental</i> và <i>foundation</i>: phần đáy đỡ cả '
    'ngôi nhà ⇒ móng nhà; nghĩa bóng ⇒ nền tảng. Cụm nên thuộc: <b>заложи́ть фунда́мент</b> '
    'đặt móng.</div>'
    '<div class="hd-warn">Móng nhà xây thật ⇒ <b>фунда́мент</b>. «Cơ sở, nguyên lý» của môn học, '
    'lập luận ⇒ <b>осно́ва</b>: <b>осно́вы грамма́тики</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>фундамента́льный</b> cơ bản, nền tảng (<i>fundamental</i>)</div>'
)

# ---------------------------------------------------------------------- гель
S["гель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn từ quốc tế <i>gel</i>, vốn là chữ <i>gelatin</i> '
    'cắt ngắn.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chất sánh đặc như thạch. Nói rõ dùng để làm gì bằng <i>для</i> + cách 2: '
    '<b>гель для бритья́</b> gel cạo râu, <b>гель для рук</b> gel rửa tay.</div>'
    '<div class="hd-warn">Đuôi <i>-ь</i> mà giống ĐỰC, như <b>шампу́нь</b>: <b>прозра́чный гель</b>, '
    '<b>ге́ля</b>, <b>ге́лем</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam">cùng gốc Latin «đông lại»: <b>желати́н</b> gelatin · <b>желе́</b> thạch</div>'
)

# --------------------------------------------------------------- выключатель
S["выключатель"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вы-</span>'
    '<span class="hd-gloss">RA ngoài</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ключ-а-</span>'
    '<span class="hd-gloss">chìa khoá (<b>ключ</b>) — thân của <b>выключа́ть</b> tắt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тель</span>'
    '<span class="hd-gloss">NGƯỜI / VẬT làm việc đó — như <b>учи́тель</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Cái để tắt» ⇒ công tắc; dùng cả để BẬT, nhưng tiếng Nga đặt tên theo việc '
    'tắt. Giữ nguyên trọng âm của động từ: <b>выключа́ть</b> → <b>выключа́тель</b>. Đuôi <i>-тель</i> '
    '⇒ giống đực.</div>'
    '<div class="hd-warn"><b>выключа́тель</b> bấm bật/tắt đèn; nút chuyển giữa nhiều chế độ là '
    '<b>переключа́тель</b> (<i>пере-</i> chuyển sang).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>выключа́ть</b> / <b>вы́ключить</b> tắt · <b>включа́ть</b> bật · '
    '<b>ключ</b> chìa khoá · <b>отключа́ть</b> ngắt kết nối</div>'
)

# ------------------------------------------------------------------- шампунь
S["шампунь"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn tiếng Anh <i>shampoo</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghe ra ngay <i>shampoo</i>, chỉ thêm <i>-нь</i> ở cuối. Gội ĐẦU trong tiếng '
    'Nga là rửa đầu: <b>мыть го́лову шампу́нем</b> (cách 5).</div>'
    '<div class="hd-warn">Giống ĐỰC dù đuôi <i>-ь</i>: <b>хоро́ший шампу́нь</b>, <b>шампу́ня</b>, '
    '<b>шампу́нем</b>.</div>'
)

# ------------------------------------------------------------------- гладить
S["гладить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">глад-</span>'
    '<span class="hd-gloss">NHẴN — <b>гла́дкий</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Làm cho nhẵn»: miết tay lên lông mèo ⇒ vuốt; miết bàn là lên vải ⇒ ủi. '
    'Cả hai đều kéo cách 4: <b>гла́дить ко́шку</b>, <b>гла́дить руба́шку</b>. Vuốt ở CHỖ NÀO thì '
    '<i>по</i> + cách 3: <b>гла́дить соба́ку по голове́</b>.</div>'
    '<div class="hd-warn">Chỉ ngôi «tôi» đổi д → ж: <b>гла́жу</b>, rồi <b>гла́дишь</b>, '
    '<b>гла́дит</b>. Trọng âm đứng yên.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>погла́дить</b> (HT) · <b>гла́дкий</b> nhẵn · <b>гла́дко</b> suôn sẻ</div>'
)

# ----------------------------------------------------------------- погладить
S["погладить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">tiền tố làm HT, không thêm nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-глад-и-ть</span>'
    '<span class="hd-gloss">LÀM NHẴN — chính là <b>гла́дить</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ủi xong cái quần, hoặc vuốt một cái: <b>погла́дить брю́ки</b>, '
    '<b>погла́дить кота́</b>. Ngôi «tôi» cũng д → ж: <b>погла́жу</b>, rồi <b>погла́дишь</b>; '
    'mệnh lệnh <b>погла́дь</b>.</div>'
    '<div class="hd-warn"><b>За э́то по голо́вке не погла́дят</b> — «không ai xoa đầu vì việc đó đâu» '
    '= sẽ bị phạt, bị mắng.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гла́дить</b> (CHT) · <b>гла́дкий</b> nhẵn · khác gốc: <b>утю́г</b> bàn là</div>'
)

# ------------------------------------------------------------------ скатерть
S["скатерть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Nay không chẻ được nữa. Không dính gì tới <b>ка́тер</b> xuồng máy.</div>'
    '<div class="hd-warn">⚠️ Mức tin: thường được giải là <b>доска́</b> (tấm ván, mặt bàn) + gốc '
    '<i>тер-</i> của <b>тере́ть</b> chà, lau — «khăn lau bàn». Đây là từ nguyên, không phải luật '
    'suy ra được.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Giống CÁI: <b>бе́лая ска́терть</b>; trải ra: <b>постели́ть ска́терть</b>. '
    'Số nhiều <b>ска́терти</b> nhấn đầu, các cách sau nhảy ra đuôi: <b>скатерте́й</b>, '
    '<b>скатертя́м</b> — như <b>че́тверть</b>.</div>'
    '<div class="hd-warn"><b>Ска́тертью доро́га!</b> — vốn chúc «đường phẳng như khăn trải bàn», nay là '
    'lời đuổi mỉa: đi luôn cho khuất mắt!</div>'
)

# ------------------------------------------------------------------ кастрюля
S["кастрюля"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: từ mượn, gốc xa là tiếng Pháp <i>casserole</i>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng gốc với <i>casserole</i> tiếng Anh. Nồi sâu, có nắp, để nấu canh, luộc: '
    '<b>кастрю́ля су́па</b> một nồi canh; nấu trong nồi: <b>вари́ть в кастрю́ле</b>.</div>'
    '<div class="hd-warn"><b>кастрю́ля</b> nồi sâu để nấu nước; chảo nông để rán là '
    '<b>сковорода́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>кастрю́лька</b> nồi nhỏ</div>'
)

B = {
    "docbangmat": 78,
    "loitubat": 2,   # погладить: thành ngữ viết «по голове» -> đúng là «по головке не погладят»
                     # нитка: khai số nhiều = «cả cuộn chỉ» (cuộn là кату́шка) -> «chỉ khâu nói chung»
    "nguonsai": 0,   # không bác dòng từ điển nào; nghĩa Việt sửa nằm hết ở V
    "baolen": [
        "V cần duyệt (4 thẻ): таз (THÊM khung chậu) · гель (BỎ keo — đó là клей) · гладить, погладить (san cùng dãy «vuốt, xoa, âu yếm, ủi, là quần áo»: гладить thiếu iron, погладить thiếu caress). Chưa chạy lại vacham với V mới (không đọc Anki).",
        "Trùng hết nghĩa trong lô chỉ có гладить / погладить — badge thể tách. Lót nhau một phần, không gỡ: фундамент ↔ осно́ва [k156] chung «nền móng, nền tảng» (mỗi bên còn một nghĩa riêng, badge giống khác); таз ↔ ми́ска chung ý «chậu»; одеколон ↔ духи́ chung «nước hoa».",
        "Câu ví dụ cần sửa (_opus_k234): отопление «Таких дорогих отоплений я ещё не видел» — từ này hầu như không có số nhiều, câu gượng.",
        "Câu ví dụ гладить cả ba đều nghĩa vuốt, V nay có «ủi»: nên đổi một câu sang ủi (vd «Я не люблю гладить рубашки»).",
        "Báo oan đúng như đề bài: скатерть↔катер (ghi rõ trên thẻ), отопление↔плен (không ghi). Bỏ mục Họ hàng có chủ ý: одеколон, шампунь (mượn đứng một mình), скатерть (từ nguyên để ở ô mức tin).",
        "Không chắc, KHÔNG đưa lên thẻ: нить ↔ needle (Ấn–Âu xa) · гладкий ↔ glad/glatt · таз ↔ tasse/Tasse. «гель для душа» bỏ khỏi ô vì cửa soát nhầm ду́ша (душ C2) với душа́; битум bỏ vì từ điển lệch trọng âm.",
        "отопление: о- giải là KHẮP, топ- cùng gốc тёплый — theo từ điển từ nguyên, viết không gắn «Mức tin».",
    ],
}
