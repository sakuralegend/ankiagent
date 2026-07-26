# -*- coding: utf-8 -*-
"""LÔ 1b — phần MNEMONIC (`.mn-story`) cho 271 thẻ RUSSIAN::0-inbox (25/07/2026).

Bổ sung cho `batch01_inbox_2026-07-25.py`: file kia là phần PHÂN TÍCH GỐC TỪ,
file này là phần MNEMONIC được chèn LÊN ĐẦU field `Mnemonic` (nhãn thẻ: "Hướng dẫn").

Thứ tự cuối cùng trong field:
    <div class="mn-read">phiên âm</div>
    <div class="mn-story">MNEMONIC — bắt buộc có, đứng đầu</div>   <- file này
    phân tích gốc từ (nằm trần trong .mn-content)                   <- batch01
    <div class="mn-tip">dòng cách nhớ</div>                         <- batch01

Luật viết mnemonic:
  * TỪ NÀO CŨNG PHẢI CÓ — kể cả từ mượn tiếng Anh và từ có gốc rõ ràng.
  * Cụm âm mồi in đậm, BẮT BUỘC là tiếng Việt CÓ THẬT (hoặc từ tiếng Anh user đã biết).
  * Một cảnh ngắn, cụ thể, nhìn thấy được — không giải thích ngữ pháp ở đây.
  * Bám phiên âm THẬT (о không nhấn -> "a", е không nhấn -> "i", г trong -ого -> "v").

Key = từ đã bỏ dấu trọng âm (U+0301) và ký tự zero-width (U+200B).
"""

S = {}

# ── Quốc gia / quốc tịch ────────────────────────────────────────────────────
S["Китай"] = "«<b>KÌ TÀY</b>» — Vạn Lý Trường Thành, kỳ quan to <b>tày</b> trời."
S["китаец"] = "«ki-<b>TA</b>-yets» — anh Trung Quốc gánh trà <b>Tàu</b> qua Vạn Lý."
S["китаянка"] = "«ki-ta-<b>YAN</b>-ka» — cô gái Trung Quốc pha trà, khói bay <b>yên</b> ả."
S["китайский"] = "«ki-<b>TAY</b>-skiy» — lá cờ Trung Quốc cắm trên đôi <b>ski</b> (ván trượt)."
S["китайски"] = "«ki-<b>TAY</b>-ski» — trượt đôi <b>ski</b> sang đất Trung Hoa là nói được tiếng Trung."
S["американец"] = "«a-mi-ri-<b>KA</b>-nhets» — anh Mỹ <b>nhét</b> tay vào túi quần bò, nhai kẹo cao su."
S["американка"] = "«a-mi-ri-<b>KAN</b>-ka» — cô Mỹ cầm lon (<b>can</b>) Coca lạnh."
S["американский"] = "«a-mi-ri-<b>KAN</b>-skiy» — cái mác <i>Made in USA</i> dán trên đôi <b>ski</b>."
S["английски"] = "«an-<b>GLIY</b>-ski» — xỏ đôi <b>ski</b> trượt qua eo biển sang Anh."
S["английский"] = "«an-<b>GLIY</b>-skiy» — cờ Anh phấp phới trên đôi <b>ski</b>."
S["англичанин"] = "«an-gli-<b>CHA</b>-nhin» — quý ông Anh nhấp tách <b>trà</b> lúc 5 giờ chiều."
S["англичанка"] = "«an-gli-<b>CHAN</b>-ka» — quý bà Anh <b>chan</b> sữa vào tách trà."
S["араб"] = "«a-<b>RÁP</b>» — người Ả <b>Rập</b> <b>ráp</b> lều giữa sa mạc."
S["арабка"] = "«a-<b>RÁP</b>-ka» — cô gái Ả Rập <b>ráp</b> khăn trùm kín mặt."
S["арабский"] = "«a-<b>RÁP</b>-skiy» — tấm thảm bay Ả Rập lướt như đôi <b>ski</b> trên trời."
S["испанец"] = "«is-<b>PA</b>-nhets» — anh Tây Ban Nha vung áo choàng đỏ, bò tót <b>nhắm</b> vào."
S["испанка"] = "«is-<b>PAN</b>-ka» — cô Tây Ban Nha múa flamenco, váy xoè như cái <b>bàn</b> xoay."
S["испанский"] = "«is-<b>PAN</b>-skiy» — chảo <b>paella</b> nóng đặt trên đôi <b>ski</b>."
S["итальянец"] = "«i-ta-<b>LYA</b>-nhets» — anh Ý tung bột pizza, tay <b>lia</b> một vòng."
S["итальянка"] = "«i-ta-<b>LYAN</b>-ka» — cô Ý quấn sợi mì <b>liền</b> một vòng quanh nĩa."
S["итальянский"] = "«i-ta-<b>LYAN</b>-skiy» — tháp nghiêng Pisa nghiêng như người đang trượt <b>ski</b>."
S["немец"] = "«<b>NHE</b>-mhets» — anh Đức <b>nhễ</b> nhại bia, im như thóc (немой = câm)."
S["немка"] = "«<b>NHEM</b>-ka» — cô Đức bưng vại bia, môi <b>nhệch</b> ra cười."
S["немецкий"] = "«nhi-<b>MHE</b>-tskiy» — chiếc xe Đức chạy êm, bánh lăn như đôi <b>ski</b>."
S["кореец"] = "«ka-<b>RYE</b>-yets» — anh Hàn Quốc nướng thịt, mỡ <b>rớt</b> xèo xèo."
S["кореянка"] = "«ka-ri-<b>YAN</b>-ka» — cô gái Hàn <b>duyên</b> dáng cúi chào."
S["француз"] = "«fran-<b>TSUS</b>» — anh Pháp cắp bánh mì, hô <b>xúyt</b> xoa vì nóng."
S["француженка"] = "«fran-<b>TSU</b>-zhen-ka» — cô Pháp đội mũ nồi, tay cầm <b>chùm</b> nho."
S["французский"] = "«fran-<b>TSUS</b>-kiy» — tháp Eiffel nhọn như mũi đôi <b>ski</b>."
S["русский"] = "«<b>RÚT</b>-skiy» — chàng Nga đi đôi <b>ski</b>, <b>rút</b> đàn ra chơi giữa tuyết."
S["русски"] = "«<b>RÚT</b>-ki» — trượt đôi <b>ski</b> trên tuyết Nga thì bật ra tiếng Nga."
S["вьетнамский"] = "«vyet-<b>NAM</b>-skiy» — <b>Việt Nam</b> mình, chỉ thêm đôi <b>ski</b> vào đuôi."
S["чех"] = "«<b>CHÉCH</b>» — anh <b>Czech</b> nâng vại bia Pilsner, bọt <b>chệch</b> ra ngoài."
S["национальность"] = "«na-tsy-a-<b>NAL</b>-nast» — quầy hải quan hỏi <b>national</b>-ity, giơ hộ chiếu ra."

S["по-английски"] = "«pa-an-<b>GLIY</b>-ski» — <b>по-</b> là bàn đạp, <b>-ски</b> là đôi ván: trượt thẳng vào tiếng Anh."
S["по-испански"] = "«pa-is-<b>PAN</b>-ski» — đạp một cái, trượt <b>ski</b> vào quán tapas Tây Ban Nha."
S["по-китайски"] = "«pa-ki-<b>TAY</b>-ski» — trượt <b>ski</b> thẳng vào chợ đêm Bắc Kinh."
S["по-немецки"] = "«pa-nhi-<b>MYE</b>-tski» — trượt <b>ski</b> xuống dốc Alps vào lễ hội bia Đức."
S["по-русски"] = "«pa-<b>RÚT</b>-ki» — trượt <b>ski</b> trên tuyết Nga, mở miệng là ra tiếng Nga."
S["по-французски"] = "«pa-fran-<b>TSUS</b>-ki» — trượt <b>ski</b> từ Alps xuống Paris, gọi ngay ly vang."

# ── Từ mượn quốc tế (vẫn phải có cảnh, không chỉ chỉ mặt từ tiếng Anh) ──────
S["актриса"] = "«ắc-<b>TRI</b>-xa» — nàng <b>actress</b> cúi chào khán giả ngồi tít đằng <b>xa</b>."
S["бизнесмен"] = "«bít-nhes-<b>MHEN</b>» — <b>businessman</b>: người đàn ông (<b>men</b>) vest đen, cặp da."
S["билет"] = "«bi-<b>LIẾT</b>» — người soát vé <b>liếc</b> tấm vé một cái rồi xé toạc."
S["буфет"] = "«bu-<b>PHIẾT</b>» — quầy <b>buffet</b> bày bánh, ai đi qua cũng <b>phết</b> một miếng bơ."
S["диалог"] = "«đi-a-<b>LỐC</b>» — hai người đối thoại, lời qua lời lại <b>lọc cọc</b> như bóng bàn."
S["диктант"] = "«đik-<b>TANT</b>» — cô đọc <b>dictation</b>, cả lớp cắm cúi chép, bút chạy <b>tanh tách</b>."
S["грамматика"] = "«gra-<b>MA</b>-ti-ka» — <b>grammar</b> là bà giáo cầm thước, gõ <b>ma</b> lanh một cái."
S["глагол"] = "«gla-<b>GÔN</b>» — động từ là quả <b>gôn</b> (goal): câu nào cũng phải sút bóng vào đó."
S["императив"] = "«im-pi-ra-<b>TIF</b>» — <b>imperative</b>: ông vua chỉ tay quát “Làm ngay!”."
S["инженер"] = "«in-zhy-<b>NHER</b>» — <b>engineer</b> đội mũ bảo hộ, tay cầm bản vẽ."
S["интересный"] = "«in-ti-<b>RYES</b>-nyy» — chuyện <b>interesting</b> đến mức bạn <b>rướn</b> cả người tới nghe."
S["неинтересный"] = "«nhi-in-ti-<b>RYES</b>-nyy» — thêm <b>не</b> đằng trước là ngáp dài: <b>không</b> interesting."
S["конструкция"] = "«kan-<b>STRUK</b>-tsy-ya» — <b>construction</b>: giàn giáo dựng lên, khung sắt đan nhau."
S["конфета"] = "«kan-<b>PHIẾT</b>-ta» — viên kẹo <b>confection</b>, bóc giấy <b>phựt</b> một cái."
S["курс"] = "«<b>KURS</b>» — <b>course</b>: con tàu giữ đúng hướng, cũng là khoá học giữ đúng lộ trình."
S["музыка"] = "«<b>MU</b>-zy-ka» — <b>music</b>, nhưng trọng âm nhảy về đầu: <b>MU</b>, không phải mu-ZY."
S["музей"] = "«mu-<b>ZYEY</b>» — <b>museum</b> Nga: bước vào là im phăng phắc, chỉ nghe tiếng giày."
S["натуральный"] = "«na-tu-<b>RAL</b>-nyy» — <b>natural</b>: mật ong nguyên chất chảy ròng ròng."
S["нормальный"] = "«nar-<b>MAL</b>-nyy» — <b>normal</b>: hỏi “khoẻ không?”, nhún vai “bình thường”."
S["профессор"] = "«pra-<b>FYE</b>-sar» — <b>professor</b> Nga: trọng âm rơi giữa, <b>FYE</b>, râu bạc kính dày."
S["реплика"] = "«<b>RYE</b>-pli-ka» — <b>replica</b>/<b>reply</b>: diễn viên đế lại đúng một câu thoại."
S["салат"] = "«sa-<b>LAT</b>» — <b>salad</b>: rau trộn bị <b>lắc</b> trong tô cho đều."
S["спорт"] = "«<b>SPORT</b>» — y hệt <b>sport</b>, chỉ khác là chữ р phải rung lưỡi."
S["спортивный"] = "«spar-<b>TIV</b>-nyy» — <b>sportive</b>: đôi giày thể thao, chân bật <b>tưng</b> lên."
S["текст"] = "«<b>TYEKST</b>» — <b>text</b>: nguyên khối chữ đặc kín cả trang."
S["тест"] = "«<b>TYEST</b>» — <b>test</b>: tờ đề úp xuống bàn, tim đập thình thịch."
S["тип"] = "«<b>TIP</b>» — <b>type</b>: xếp đồ vào từng hộp, mỗi hộp một loại."
S["фирма"] = "«<b>FIR</b>-ma» — <b>firm</b>: tấm biển công ty gắn chắc trên tường."
S["форма"] = "«<b>FOR</b>-ma» — <b>form</b>: cái khuôn bánh, đổ bột vào là ra đúng hình."
S["физика"] = "«<b>FI</b>-zi-ka» — <b>physics</b>: quả táo rơi trúng đầu, trọng âm rơi ngay chữ <b>FI</b>."
S["физик"] = "«<b>FI</b>-zik» — nhà <b>physicist</b>: tóc rối bù đứng trước bảng đầy công thức."
S["экономист"] = "«e-ka-na-<b>MIST</b>» — <b>economist</b>: chỉ tay vào biểu đồ đang lao dốc."
S["юрист"] = "«yu-<b>RIST</b>» — <b>jurist</b>: luật sư gõ búa, hồ sơ dày cộp."
S["юридический"] = "«yu-ri-<b>DHI</b>-chis-kiy» — <b>juridical</b>: con dấu đỏ đóng “<b>đì</b>” một cái xuống giấy."
S["шоколад"] = "«sha-ka-<b>LAT</b>» — <b>chocolate</b>: thanh sô-cô-la bẻ đôi kêu <b>rắc</b>, trọng âm ở cuối."
S["шофёр"] = "«sha-<b>FYOR</b>» — <b>chauffeur</b> (tiếng Pháp): bác tài đeo găng trắng mở cửa xe."
S["центральный"] = "«tsyn-<b>TRAL</b>-nyy» — <b>central</b>: ga trung tâm, mọi đường tàu đổ về."
S["танцевать"] = "«tan-tsy-<b>VAT</b>» — <b>dance</b>: chân dậm <b>tan tách</b> theo nhịp."
S["аналогичный"] = "«a-na-la-<b>GHÌCH</b>-nyy» — <b>analogical</b>: hai bức ảnh <b>ghì</b> sát vào nhau, giống hệt."
S["отрицательный"] = "«a-tri-<b>TSA</b>-tyel-nyy» — dấu trừ đỏ chót, mặt <b>xa</b> sầm lại: tiêu cực."
S["положительный"] = "«pa-la-<b>ZHY</b>-tyel-nyy» — dấu cộng xanh: đặt (<b>положить</b>) thêm vào là tích cực."
S["современный"] = "«sa-vri-<b>MHEN</b>-nyy» — cùng <b>thời</b> (время) với mình: toà nhà kính bóng loáng."

# ── Đồ ăn, đồ vật, đời sống ─────────────────────────────────────────────────
S["блюдо"] = "«<b>BLIU</b>-đa» — đĩa thức ăn nóng bưng ra, khói bay <b>liu riu</b>."
S["борщ"] = "«<b>BORSHCH</b>» — nồi súp củ dền đỏ au sôi sùng sục, nổi đầy <b>bọt</b>."
S["щи"] = "«<b>SHI</b>» — bát súp bắp cải nóng, húp một cái kêu <b>xì</b> khói."
S["капуста"] = "«ka-<b>PUS</b>-ta» — bắp cải tròn như <b>cái đầu</b> (Latin <i>caput</i>), bóc từng lớp tóc lá."
S["картошка"] = "«kar-<b>TOSH</b>-ka» — nghe như “<b>cạo tóc</b>-ka”: củ khoai tây gọt vỏ trọc lóc."
S["помидор"] = "«pa-mi-<b>DOR</b>» — <b>pomodoro</b>: cái đồng hồ hẹn giờ hình quả cà chua đỏ."
S["хлеб"] = "«<b>KHLYEP</b>» — ổ bánh mì bẻ đôi kêu <b>khép</b>, ruột trắng bốc khói."
S["конфета "] = ""
S["чашка"] = "«<b>CHASH</b>-ka» — cái <b>tách</b> sứ, đặt xuống đĩa kêu <b>cạch</b> một tiếng."
S["щётка"] = "«<b>SHCHOT</b>-ka» — bàn chải <b>chọt</b> vào kẽ răng, lông cứng sồn sột."
S["скобка"] = "«<b>SKOP</b>-ka» — hai dấu ngoặc ôm lấy chữ như nắp <b>cốp</b> xe đóng lại."
S["точка"] = "«<b>TOCH</b>-ka» — đầu bút <b>chọc</b> xuống giấy một cái: dấu chấm hết câu."
S["щепка"] = "«<b>SHCHEP</b>-ka» — nhát rìu <b>chép</b> vào thân cây, vụn gỗ bay tứ tung."
S["щит"] = "«<b>SHCHIT</b>» — <b>shield</b>: giơ tấm khiên lên, tên bắn vào kêu <b>sít</b>."
S["щука"] = "«<b>SHCHU</b>-ka» — con cá chó phóng ra đớp mồi, đuôi quẫy <b>súc</b> nước."
S["хвощ"] = "«<b>KHVOSHCH</b>» — cây cỏ tháp bút <b>vọt</b> thẳng lên khỏi mặt đất."
S["плащ"] = "«<b>PLASHCH</b>» — khoác áo mưa, nước <b>lách tách</b> trên vai."
S["плач"] = "«<b>PLACH</b>» — tiếng khóc, nước mắt <b>lách</b> qua kẽ tay."
S["луч"] = "«<b>LUCH</b>» — tia nắng <b>lọt</b> qua khe cửa, đúng <b>lúc</b> trời hửng."
S["лёд"] = "«<b>LYOT</b>» — mặt băng trơn, trượt chân <b>lướt</b> một đường dài."
S["лён"] = "«<b>LYON</b>» — <b>linen</b>: tấm vải lanh mộc phơi bay phần phật."
S["лев"] = "«<b>LYEF</b>» — <b>lion</b>/<b>Leo</b>: sư tử rung bờm, gầm một tiếng <b>liếp</b> tai."
S["мышь"] = "«<b>MYSH</b>» — <b>mouse</b>: con chuột chui vào khe, kêu <b>chít</b>."
S["врач"] = "«<b>VRACH</b>» — nghe như “<b>vờ-rách</b>”: bác sĩ khâu lại chỗ <b>rách</b> trên da."
S["грач"] ="«<b>GRACH</b>» — con quạ đen <b>rạch</b> ngang bầu trời, báo mùa xuân đã về."
S["море"] = "«<b>MO</b>-rye» — <b>marine</b>: sóng biển vỗ bờ, muối mặn trên môi."
S["земля"] = "«zim-<b>LYA</b>» — nắm đất đen ẩm trong lòng bàn tay giữa mùa đông (<i>zima</i>)."
S["лес"] = "«<b>LYES</b>» — rừng thông dày, nắng <b>liếc</b> qua kẽ lá thành từng vệt."
S["поле"] = "«<b>PO</b>-lye» — sân <b>polo</b>: cánh đồng phẳng lì trải tới chân trời."
S["рожь"] = "«<b>ROSH</b>» — <b>rye</b>: đồng lúa mạch đen rì rào, hạt <b>rơi</b> lộp bộp."
S["чудо"] = "«<b>CHU</b>-đa» — thấy phép màu thì thốt lên “<b>Chu cha!</b>”."
S["дачка"] = "«<b>DACH</b>-ka» — mảnh <b>đất</b> nhỏ ngoại ô, căn nhà gỗ xinh giữa vườn táo."
S["малыш"] = "«ma-<b>LYSH</b>» — thằng bé <b>lích nhích</b>, bé <b>tí</b> mà chạy nhanh."
S["ребёнок"] = "«ri-<b>BYO</b>-nak» — nghe như “<b>bố… nhóc</b>”: ông bố bế thằng nhóc trên vai."
S["дочь"] = "«<b>DOCH</b>» — <b>daughter</b>: con gái nhỏ <b>đọc</b> sách trong lòng bố."
S["жена"] = "«zhy-<b>NA</b>» — <b>queen</b> của căn nhà: vợ đứng cửa gọi “về ăn cơm!”."
S["слеза"] = "«sli-<b>ZA</b>» — “<b>lệ sa</b>”: giọt nước mắt lăn dọc má rồi rơi."
S["любовь"] = "«lyu-<b>BOF</b>» — <b>love</b>: chữ l và b ôm nhau, tim đập <b>bốp</b> một cái."
S["ветер"] = "«<b>VYE</b>-tyer» — gió lùa qua cửa sổ, thổi bay trang giấy đang <b>viết</b>."
S["музей "] = ""

# ── Thời tiết ───────────────────────────────────────────────────────────────
S["ветреный"] = "«<b>VYE</b>-tri-nyy» — ngày lộng gió: chữ <b>viết</b> trên cát bị thổi bay sạch."
S["дождливый"] = "«dazhd-<b>LI</b>-vyy» — mưa lộp độp, <b>lì</b> cả ngày không chịu tạnh."
S["морозный"] = "«ma-<b>ROZ</b>-nyy» — rét cắt da, mũi đỏ như củ cà <b>rốt</b>."
S["снежный"] = "«<b>SNHEZH</b>-nyy» — <b>snow</b>: tuyết rơi dày, bước chân <b>nghiến</b> lạo xạo."
S["солнечный"] = "«<b>SOL</b>-nhich-nyy» — <b>solar</b>: mặt trời chói, phải <b>nhích</b> vào bóng râm."
S["облачный"] = "«<b>O</b>-blach-nyy» — bầu trời như cái <b>ô</b> mây khổng lồ che kín đầu."
S["пасмурный"] = "«<b>PAS</b>-mur-nyy» — trời úp cái <b>bát mờ</b> xuống, xám xịt, buồn thiu."

# ── Tính từ, trạng từ ───────────────────────────────────────────────────────
S["близкий"] = "«<b>BLIS</b>-kiy» — hai người đứng sát đến mức <b>bịt</b> cả lối đi."
S["близко"] = "«<b>BLIS</b>-ka» — gần đến nỗi thò tay ra là <b>bịt</b> được miệng nhau."
S["богатый"] = "«ba-<b>GA</b>-tyy» — nhà giàu có tới ba cái <b>ga</b>-ra ô tô."
S["будничный"] = "«<b>BUD</b>-nhich-nyy» — ngày thường: cầm <b>bút</b> chấm công, nhích từng phút."
S["весёлый"] = "«vi-<b>SYO</b>-lyy» — vui đến mức cười <b>xỉu</b>, ôm bụng lăn ra."
S["каждый"] = "«<b>KAZH</b>-dyy» — đếm từng hạt <b>cát</b>, hạt nào cũng phải đếm."
S["модный"] = "«<b>MOD</b>-nyy» — chính là chữ “hợp <b>mốt</b>” tiếng Việt mượn từ đây."
S["ну́жный"] = ""
S["нужный"] = "«<b>NUZH</b>-nyy» — đúng thứ mình đang <b>nhu</b> cầu, thiếu là không xong."
S["острый"] = "«<b>OS</b>-tryy» — quả <b>ớt</b> đỏ: vừa nhọn, vừa cay xé lưỡi."
S["слабый"] = "«<b>SLA</b>-byy» — <b>slack</b>: sợi dây chùng, tay <b>lả</b> đi không giữ nổi."
S["узкий"] = "«<b>US</b>-kiy» — con hẻm hẹp bằng đúng ngón <b>út</b>, lách mãi mới qua."
S["широкий"] = "«shy-<b>RO</b>-kiy» — đổ ly <b>xi-rô</b> ra bàn, vệt loang <b>rộng</b> mãi ra."
S["настоящий"] = "«nas-ta-<b>YA</b>-shchiy» — hàng thật đang <b>đứng</b> (стоять) ngay đây, sờ được."
S["домашний"] = "«da-<b>MASH</b>-nhiy» — về <b>nhà</b> (дом) là <b>mát</b> rượi, cơm mẹ nấu."
S["другой"] = "«dru-<b>GOY</b>» — “không, cái <b>gói</b> kia cơ!” — chỉ sang thứ khác."
S["некоторый"] = "«<b>NHE</b>-ka-ta-ryy» — <b>không</b> phải tất cả, chỉ dăm ba cái nào đó."
S["небольшой"] = "«nhi-bal-<b>SHOY</b>» — <b>không</b> to (большой): cái hộp bé <b>xoè</b> lòng bàn tay."
S["немного"] = "«nhi-<b>MNO</b>-ga» — <b>không</b> nhiều (много): nhón đúng một nhúm muối."
S["скучный"] = "«<b>SKUSH</b>-nyy» — chán đến <b>cụt</b> hứng, ngáp sái quai hàm."
S["часто"] = "«<b>CHAS</b>-ta» — hàng <b>giờ</b> (час) lại làm một lần: quá thường xuyên."
S["отлично"] = "«at-<b>LICH</b>-na» — điểm 5 tròn trĩnh, cả lớp vỗ tay <b>lách cách</b>."
S["правильно"] = "«<b>PRA</b>-vil-na» — làm đúng <b>правда</b> (sự thật): tick xanh đánh <b>rắc</b>."
S["только"] = "«<b>TOL</b>-ka» — cả kho chỉ còn đúng một tấm <b>tôn</b>, không hơn."
S["вслух"] = "«<b>FSLUKH</b>» — đọc to cho cái tai (<b>слух</b>) nghe, không lẩm bẩm nữa."
S["письменно"] = "«<b>PIS</b>-mhen-na» — nộp bằng giấy trắng mực đen, không nói miệng."
S["вместо"] = "«<b>VMYES</b>-ta» — bước <b>vào chỗ</b> (место) của người kia mà đứng."
S["между"] = "«<b>MYEZH</b>-du» — <b>medium</b>: kẹt cứng ở giữa hai người trên xe buýt."
S["иностранный"] = "«i-na-<b>STRAN</b>-nyy» — nước (страна) <b>khác</b>: tấm hộ chiếu lạ hoắc."
S["вечером"] = "«<b>VYE</b>-chi-ram» — nghe như “<b>việc… chiều… rồi</b>”: xong việc, chiều buông."
S["позавчера"] = "«pa-za-fchi-<b>RA</b>» — lùi thêm một nấc sau <b>вчера</b> (hôm qua) = hôm kia."
S["выходной"] = "«vy-kha-<b>DNOY</b>» — <b>выход</b> = lối ra: ngày bạn bước <b>ra khỏi</b> chỗ làm."
S["множественный"] = "«<b>MNO</b>-zhyst-vhen-nyy» — <b>много</b> = nhiều: một chữ mà kéo theo cả đàn."
S["вопросительный"] = "«va-pra-<b>SI</b>-tyel-nyy» — dấu hỏi cong như cái móc, <b>sĩ</b> tử giơ tay hỏi."
S["ответный"] = "«at-<b>VYET</b>-nyy» — quả bóng bị đánh trả lại: lời <b>đáp</b> bật ngược về."
S["особенность"] = "«a-<b>SO</b>-bhen-nast» — trong đàn có <b>một</b> con lông trắng: nét riêng đó."
S["прошедший"] = "«pra-<b>SHYED</b>-shyy» — đoàn tàu vừa <b>đi qua</b>, chỉ còn khói."
S["прошедшее"] = "«pra-<b>SHYED</b>-shy-ye» — thì quá khứ: cả đoàn tàu ấy đã khuất sau đồi."
S["жена́тый"] = ""
S["женатый"] = "«zhy-<b>NA</b>-tyy» — đã có <b>жена</b> (vợ): nhẫn cưới đeo chặt ngón tay anh."
S["замужем"] = "«<b>ZA</b>-mu-zhem» — đứng nép <b>sau lưng chồng</b> (за + муж): cô ấy đã lấy chồng."
S["родной"] = "«rad-<b>NOY</b>» — cùng một <b>rễ</b> (род/<i>root</i>): máu mủ ruột thịt, tiếng mẹ đẻ."
S["учёный"] = "«u-<b>CHO</b>-nyy» — người <b>học</b> (уч-) mãi không thôi, kính dày cộp."
S["счастливый"] = "«shas-<b>LI</b>-vyy» — được chia <b>phần</b> (часть) ngon nhất: cười tít mắt."

# ── Danh từ trừu tượng / học tập ───────────────────────────────────────────
S["вещь"] = "«<b>VYESHCH</b>» — ôm đống đồ lỉnh kỉnh nặng đến <b>vẹo</b> cả lưng."
S["вина"] = "«vi-<b>NA</b>» — <b>vi</b> phạm thì phải nhận lỗi, cúi đầu."
S["воскресение"] = "«vas-kri-<b>SYE</b>-nhiye» — sáng Chủ nhật, người chết <b>sống</b> dậy bước ra khỏi mộ."
S["зачёт"] = "«za-<b>CHOT</b>» — bài kiểm tra <b>chốt</b> điểm cuối kỳ, đỗ hay trượt là ở đây."
S["защита"] = "«za-<b>SHCHI</b>-ta» — nấp <b>sau tấm khiên</b> (щит), tên bắn rào rào."
S["жительство"] = "«<b>ZHY</b>-tyel-stva» — nơi bạn <b>sống</b> (жить): địa chỉ ghi trong hộ khẩu."
S["начало"] = "«na-<b>CHA</b>-la» — mở đầu bữa tiệc bằng miếng <b>chả</b> nóng."
S["образец"] = "«a-bra-<b>ZYETS</b>» — miếng vải mẫu <b>ghim</b> trên bảng cho mọi người ngó."
S["образование"] = "«a-bra-za-<b>VA</b>-nhiye» — nhà trường <b>nặn hình</b> (образ) một con người."
S["объявление"] = "«ab-yiv-<b>LYE</b>-nhiye» — tờ rao vặt dán cột điện, gió thổi <b>lật</b> phật."
S["объём"] = "«ab-<b>YOM</b>» — cái bụng thùng <b>ôm</b> trọn được bao nhiêu nước."
S["ответ"] = "«at-<b>VYET</b>» — muốn trả lời thì phải <b>viết</b> ra (gốc вет- = nói)."
S["помощь"] = "«<b>PO</b>-mashch» — có người ghé vai vào cho bạn thêm <b>sức</b> (мочь)."
S["пощада"] = "«pa-<b>SHCHA</b>-da» — kiếm đã giơ lên rồi hạ xuống: <b>tha</b> cho một mạng."
S["упражнение"] = "«u-prazh-<b>NHE</b>-nhiye» — <b>practice</b>: vở bài tập chi chít, làm đi làm lại."
S["спряжение"] = "«spri-<b>ZHE</b>-nhiye» — đóng <b>ách</b> cho con bò: mỗi ngôi một cái ách khác nhau."
S["сожаление"] = "«sa-zhy-<b>LYE</b>-nhiye» — <b>жаль</b> (tiếc): lắc đầu thở dài “tiếc thật”."
S["переводчик"] = "«pi-ri-<b>VOT</b>-chik» — người <b>dẫn</b> (вод-) nghĩa lội <b>qua</b> (пере-) bờ bên kia."
S["счастье"] = "«<b>SHAS</b>-tye» — được chia đúng <b>phần</b> (часть) mình mong: hạnh phúc."
S["счёт"] = "«<b>SHCHOT</b>» — bồi bàn đưa hoá đơn, bạn <b>sốt</b> ruột nhìn con số."
S["съезд"] = "«<b>SYEST</b>» — cả nghìn người <b>đi</b> (езд) dồn <b>về một chỗ</b> (с): đại hội."
S["разъезд"] = "«raz-<b>YEST</b>» — <b>раз-</b> = tản ra: quanh năm đi công tác, chẳng ở nhà."
S["разъём"] = "«raz-<b>YOM</b>» — <b>tách</b> (раз-) hai đầu giắc ra, kêu <b>tách</b> một cái."
S["подъезд"] = "«pad-<b>YEST</b>» — <b>под</b> = dưới: chui vào cái cửa dưới chân toà chung cư."
S["подъём"] = "«pad-<b>YOM</b>» — 6 giờ sáng còi hú: nhấc <b>từ dưới</b> lên khỏi giường."
S["язык"] = "«yi-<b>ZYK</b>» — cái <b>lưỡi</b> trong miệng cũng chính là <b>ngôn ngữ</b> bạn nói."
S["курс "] = ""
S["род"] = "«<b>ROT</b>» — <b>root</b>: cái <b>rễ</b> của cả dòng họ ăn sâu xuống đất."
S["час"] = "«<b>CHAS</b>» — kim đồng hồ gõ “<b>chát</b>” một tiếng: hết một giờ."
S["цвет"] = "«<b>TSVYET</b>» — bông hoa (цветок) bung cánh, khoe đủ <b>màu</b>."
S["рисунок"] = "«ri-<b>SU</b>-nak» — bức tranh đã vẽ xong, đóng khung treo lên."

# ── Động từ ─────────────────────────────────────────────────────────────────
S["видеть"] = "«<b>VI</b>-dyet» — <b>video</b>: con mắt như cái máy quay, ghi lại tất cả."
S["говорить"] = "«ga-va-<b>RIT</b>» — nói mãi nói mãi đến <b>rít</b> cả cổ họng."
S["поговорить"] = "«pa-ga-va-<b>RIT</b>» — thêm <b>по-</b> = ngồi xuống <b>tán gẫu một lát</b> rồi thôi."
S["думать"] = "«<b>DU</b>-mat» — ngồi <b>đu</b> đưa trên võng mà nghĩ ngợi, mắt nhìn xa xăm."
S["гулять"] = "«gu-<b>LYAT</b>» — đi dạo lang thang tới <b>lết</b> cả chân."
S["дать"] = "«<b>DAT</b>» — <b>đưa</b>: cả tiếng Nga lẫn tiếng Việt đều mở đầu bằng chữ <b>đ</b>."
S["жить"] = "«<b>ZHYT</b>» — <b>zest</b>: sống là phải có tí lửa, không thì chỉ là tồn tại."
S["забыть"] = "«za-<b>BYT</b>» — <b>за</b> = bỏ lại phía sau: cái ô để quên trên xe buýt."
S["записывать"] = "«za-<b>PI</b>-sy-vat» — <b>писать</b> = viết: cắm cúi ghi từng dòng vào sổ."
S["написать"] = "«na-pi-<b>SAT</b>» — <b>на-</b> đóng nắp: viết xong hẳn rồi, bấm gửi."
S["звонить"] = "«zva-<b>NHIT</b>» — <b>звон</b> = tiếng chuông: máy đổ chuông <b>reng</b> lên."
S["играть"] = "«i-<b>GRAT</b>» — gảy đàn tới <b>rát</b> cả đầu ngón tay."
S["использовать"] = "«is-<b>POL</b>-za-vat» — moi cái <b>lợi</b> (польза) ra mà dùng."
S["мочь"] = "«<b>MOCH</b>» — <b>might</b>: gồng tay lên, “được, tôi làm được”."
S["обедать"] = "«a-<b>BYE</b>-dat» — trưa rồi, bụng <b>biết</b> đói: kéo ghế ngồi vào mâm."
S["завтракать"] = "«<b>ZAF</b>-tra-kat» — sáng dậy <b>đạp</b> chân xuống giường đi kiếm bữa sáng."
S["ужинать"] = "«<b>U</b>-zhy-nat» — bữa tối: cả nhà quây quần, đèn vàng <b>u</b> ám ấm cúng."
S["объявить"] = "«ab-yi-<b>VIT</b>» — làm cho <b>hiện ra</b> (явить) trước mặt mọi người: tuyên bố."
S["отвечать"] = "«at-vi-<b>CHAT</b>» — gốc <b>вет-</b> ~ “<b>viết</b>”: đang trả lời, còn dở dang."
S["ответить"] = "«at-<b>VYE</b>-tit» — cũng gốc “<b>viết</b>” ấy, nhưng đáp <b>dứt một câu</b> rồi thôi."
S["повторять"] = "«paf-ta-<b>RYAT</b>» — làm lại lần <b>thứ hai</b> (второй): đúng việc bạn đang làm với Anki."
S["понимать"] = "«pa-nhi-<b>MAT</b>» — hiểu ra rồi thì đầu nhẹ bẫng, <b>mát</b> rượi."
S["поставить"] = "«pa-<b>STA</b>-vit» — <b>став-</b> = dựng đứng: đặt cái cốc xuống bàn kêu <b>cạch</b>."
S["вставить"] = "«fsta-<b>VIT</b>» — <b>в</b> = vào: cắm phích điện, nghe <b>tách</b> một cái."
S["составить"] = "«sa-<b>STA</b>-vit» — <b>с-</b> = gom lại: dựng nhiều mảnh thành một bản kế hoạch."
S["проверять"] = "«pra-vi-<b>RYAT</b>» — <b>prove</b>: soi lại xem có đáng <b>tin</b> (вера) không."
S["прослушать"] = "«pra-<b>SLU</b>-shat» — <b>слух</b> = tai: nghe hết từ đầu đến cuối, không bỏ đoạn nào."
S["прочитать"] = "«pra-chi-<b>TAT</b>» — <b>про-</b> = xuyên suốt: đọc từ trang đầu tới trang cuối."
S["рассказать"] = "«ra-ska-<b>ZAT</b>» — <b>сказать</b> = nói, thêm <b>рас-</b> = kể trải ra cả câu chuyện."
S["сказать"] = "«ska-<b>ZAT</b>» — <b>сказка</b> = truyện cổ tích: bà kể, cháu há hốc mồm nghe."
S["рисовать"] = "«ri-sa-<b>VAT</b>» — bút chì <b>rì rà</b> kéo từng <b>vạch</b> trên giấy."
S["родиться"] = "«ra-<b>DI</b>-tsa» — bật ra từ cái <b>rễ</b> (род): một mầm non vừa nhú."
S["спрашивать"] = "«<b>SPRA</b>-shy-vat» — hỏi dồn dập, câu hỏi <b>phun</b> ra như mưa rào."
S["спросить"] = "«spra-<b>SIT</b>» — cũng gốc ấy, nhưng hỏi <b>đúng một câu</b> rồi im."
S["спрягаться"] = "«spri-<b>GA</b>-tsa» — động từ tự chui vào <b>ách</b>, mỗi ngôi một dạng."
S["учиться"] = "«u-<b>CHI</b>-tsa» — gốc <b>уч-</b>: tự mình <b>chúi</b> đầu vào sách."
S["хотеть"] = "«kha-<b>TYET</b>» — <b>hot</b>: nóng lòng muốn có cho bằng được."
S["целовать"] = "«tsy-la-<b>VAT</b>» — <b>целый</b> = nguyên lành: đặt lên má một nụ hôn <b>chụt</b>."
S["выполнить"] = "«<b>VY</b>-pal-nhit» — đổ cho <b>đầy</b> (полный) cái bình: xong việc."
S["конечно"] = "«ka-<b>NHESH</b>-na» — “tất nhiên rồi!” — <b>nhếch</b> mép cười vì câu hỏi quá thừa."

# ── Từ chức năng ────────────────────────────────────────────────────────────
S["а"] = "Đang khen thì bật ra “<b>à</b>, nhưng mà…” — chữ <b>а</b> chính là cái ngoặt đó."
S["и"] = "«<b>I</b>» — chữ и bé xíu nối hai vế lại, đúng như dấu <b>+</b>."
S["или"] = "«<b>I</b>-li» — <b>и</b> (và) đứng trước, nhưng đuôi <b>-ли</b> bẻ nó sang “hoặc là…”."
S["не"] = "«<b>NHE</b>» — chữ <b>н</b> chính là <b>n</b> trong <b>no</b>: lắc đầu một cái."
S["за"] = "«<b>ZA</b>» — lùi <b>xa</b> ra đằng <b>sau</b>: за luôn đứng phía sau lưng."
S["по"] = "«<b>PA</b>» — bàn chân đi <b>dọc theo</b> con đường, bước từng bước một."
S["про"] = "«<b>PRA</b>» — kể <b>về</b> ai đó, như <b>про</b>file: hồ sơ về một người."
S["у"] = "«<b>U</b>» — đứng sát bên cạnh ai: “<b>у</b> меня” = ở chỗ tôi = tôi có."
S["они"] = "«a-<b>NHI</b>» — <b>они</b> ~ tiếng Việt “<b>nhị</b>, tam…”: từ hai người trở lên = họ."
S["его"] = "«yi-<b>VO</b>» — viết <b>г</b> mà đọc <b>в</b>: cái bẫy kinh điển, đọc là <b>“i-vô”</b>."
S["себя"] = "«si-<b>BYA</b>» — <b>self</b>: quay lại tự chỉ vào ngực <b>bản thân</b> mình."
S["какой"] = "«ka-<b>KOY</b>» — chỉ vào con gà <b>còi</b>: “loại nào cơ?”."
S["потому"] = "«pa-ta-<b>MU</b>» — “<b>bởi cái đó</b>”: chìa tay chỉ vào nguyên nhân."
S["почему"] = "«pa-chi-<b>MU</b>» — “<b>vì cái gì?</b>” — nhíu mày, ngửa tay lên hỏi."
S["сначала"] = "«s-na-<b>CHA</b>-la» — quay về <b>начало</b> (khởi đầu): làm lại từ miếng <b>chả</b> đầu tiên."
S["привет"] = "«pri-<b>VYET</b>» — gốc <b>вет-</b> ~ “<b>viết</b>” = nói: một lời nói ném về phía bạn."

# ── Số thứ tự ───────────────────────────────────────────────────────────────
S["второй"] = "«fta-<b>ROY</b>» — về nhì thì chỉ được cái <b>roi</b>, không được cúp vàng."
S["третий"] = "«<b>TRYE</b>-tiy» — <b>three</b>: cùng cụm <b>tr-</b>, huy chương đồng."
S["четвёртый"] = "«chit-<b>VYOR</b>-tyy» — <b>четыре</b> (4) ~ <i>quattro</i>: bốn bánh xe."
S["пятый"] = "«<b>PYA</b>-tyy» — <b>пять</b> (5): bàn tay xoè đủ năm ngón, <b>phía</b> nào cũng thấy."
S["шестой"] = "«shys-<b>TOY</b>» — <b>шесть</b> ~ <b>six</b>: mặt xúc xắc sáu chấm."
S["седьмой"] = "«sid-<b>MOY</b>» — <b>семь</b> ~ <b>seven</b>: bảy sắc cầu vồng."
S["восьмой"] = "«vas-<b>MOY</b>» — số 8 nằm ngang là dấu vô cực, xoay đến <b>mỏi</b> mắt."
S["девятый"] = "«di-<b>VYA</b>-tyy» — <b>девять</b> (9): số 9 lộn ngược thành 6, nhìn muốn <b>vẹo</b> cổ."
S["десятый"] = "«di-<b>SYA</b>-tyy» — <b>десять</b> ~ <b>deca</b>/<b>decimal</b>: đủ mười ngón tay."
S["сороковой"] = "«sa-ra-ka-<b>VOY</b>» — <b>сорок</b> (40) nghe như “<b>sa rốc</b>”: bốn mươi chai xếp hàng."
S["пятидесятый"] = "«pya-ti-di-<b>SYA</b>-tyy» — <b>пять</b>(5) + <b>десят</b>(mươi) + <b>-ый</b>: thứ năm mươi."
S["девяностый"] = "«di-vi-<b>NOS</b>-tyy» — <b>девяносто</b> (90): còn một bước nữa là tròn trăm."
S["восьмидесятый"] = "«va-smi-di-<b>SYA</b>-tyy» — <b>восемь</b>(8) + <b>десят</b>(mươi): thứ tám mươi."
S["сотый"] = "«<b>SO</b>-tyy» — <b>сто</b> ~ <b>cent</b> (100): tờ bạc một trăm."
S["тысячный"] = "«<b>TY</b>-sich-nyy» — <b>тысяча</b> (1000): người thứ một nghìn bước qua cổng."
S["двухтысячный"] = "«dvukh-<b>TY</b>-sich-nyy» — <b>два</b>(2) × <b>тысяча</b>(1000): pháo hoa năm 2000."

# ────────────────────────────────────────────────────────────────────────────
# BẢN VÁ 26/07/2026 — user bắt lỗi: "прошedший bạn giải thích là đoàn tàu vừa đi
# qua, chỉ còn khói. Mnemonic ở chỗ nào vậy? Mnemonic phải có những từ âm tiết ở
# trong câu chuyện chứ". Đúng: ~45 câu dưới đây trước đó chỉ là GIẢI THÍCH NGHĨA
# bằng hình ảnh, KHÔNG có cầu âm thanh. Viết lại, mỗi câu bắt buộc có cụm tiếng
# Việt đọc gần giống từ Nga. (Các từ mượn quốc tế không nằm trong danh sách này
# vì chính từ tiếng Anh đã là cầu âm thanh: economist ↔ экономист.)
S.update({
"испанец": "«is-<b>PA</b>-nhets» — anh Tây Ban Nha <b>pha</b> bình sangria, <b>nhét</b> thêm lát cam vào.",
"француженка": "«fran-<b>TSU</b>-zhen-ka» — cô Pháp <b>chen</b> qua chợ hoa, tay ôm bó tulip.",
"отрицательный": "«a-tri-<b>TSA</b>-tyel-nyy» — nghe như “<b>a, trừ… xa</b>”: dấu <b>trừ</b> đỏ đẩy mọi thứ ra <b>xa</b>.",
"положительный": "«pa-la-<b>ZHY</b>-tyel-nyy» — nghe như “<b>bỏ lại… giỏ</b>”: <b>bỏ</b> thêm hàng vào <b>giỏ</b>, kim cân nhích sang phía cộng.",
"современный": "«sa-vri-<b>MHEN</b>-nyy» — nghe như “<b>xoa vào… MEN</b>”: sờ lớp <b>men</b> kính bóng loáng của toà nhà mới.",
"земля": "«zim-<b>LYA</b>» — nghe như “<b>GIẪM… LIA</b>”: <b>giẫm</b> chân <b>lia</b> lịa xuống <b>mặt đất</b>.",
"жена": "«zhy-<b>NA</b>» — nghe như “<b>giữ NHÀ</b>”: vợ là người <b>giữ nhà</b>, đứng cửa gọi về ăn cơm.",
"женатый": "«zhy-<b>NA</b>-tyy» — đã có người “<b>giữ nhà</b>” (жена) rồi: nhẫn cưới siết chặt ngón tay anh.",
"замужем": "«<b>ZA</b>-mu-zhem» — <b>за</b> nghe như “<b>sau</b>”: cô ấy đứng nép <b>sau</b> lưng <b>муж</b> (chồng).",
"настоящий": "«nas-ta-<b>YA</b>-shchiy» — nghe như “<b>nắn tay</b>”: hàng thật thì <b>nắn tay</b> vào là biết ngay.",
"некоторый": "«<b>NHE</b>-ka-ta-ryy» — hỏi “cái nào?”, đáp “<b>nhé</b>, vài cái thôi” — không phải tất cả.",
"часто": "«<b>CHAS</b>-ta» — nghe như “<b>chạy tới</b>”: <b>chạy tới</b> chạy lui suốt ngày = thường xuyên.",
"правильно": "«<b>PRA</b>-vil-na» — làm xong được khen “<b>phải rồi!</b>”: đúng, chính xác.",
"вслух": "«<b>FSLUKH</b>» — nghe như “<b>phun ra… LÚC</b>”: đừng lẩm bẩm, <b>phun</b> thành tiếng ngay <b>lúc</b> đọc.",
"письменно": "«<b>PIS</b>-mhen-na» — nghe như “<b>bịt miệng</b>”: <b>bịt miệng</b> lại, viết ra giấy!",
"вместо": "«<b>VMYES</b>-ta» — nghe như “<b>vô một chỗ ta</b>”: bước <b>vào chỗ</b> (место) người kia mà đứng.",
"иностранный": "«i-na-<b>STRAN</b>-nyy» — nghe như “<b>tràn</b>”: người nước ngoài <b>tràn</b> qua biên giới.",
"позавчера": "«pa-za-fchi-<b>RA</b>» — <b>за</b> nghe như “<b>xa</b>”: lùi <b>xa</b> hơn <b>вчера</b> (hôm qua) một bậc.",
"выходной": "«vy-kha-<b>DNOY</b>» — nghe như “<b>vi vu</b>”: ngày bạn <b>ra khỏi</b> (выход) chỗ làm mà đi chơi.",
"множественный": "«<b>MNO</b>-zhyst-vhen-nyy» — nghe như “<b>mờ… NHIỀU</b>”: <b>nhiều</b> (много) đến mức nhìn <b>mờ</b> cả mắt.",
"особенность": "«a-<b>SO</b>-bhen-nast» — nghe như “<b>a, SO bên nào</b>”: <b>so</b> ra được nét riêng khác cả đàn.",
"прошедший": "«pra-<b>SHYED</b>-shyy» — nghe như “<b>bờ-ra… XIẾT</b>”: chuyện đã <b>xiết</b> chặt lại, khoá cứng vào sau lưng.",
"прошедшее": "«pra-<b>SHYED</b>-shy-ye» — cũng cái “<b>XIẾT</b>” ấy: <i>прошедшее время</i> = quãng thời gian đã <b>xiết</b> lại = thì quá khứ.",
"учёный": "«u-<b>CHO</b>-nyy» — nghe như “<b>u… CHÚI</b>”: <b>chúi</b> đầu vào sách (уч-) đến <b>u</b> cả trán.",
"воскресение": "«vas-kri-<b>SYE</b>-nhiye» — nghe như “<b>vọt khỏi</b>”: người chết <b>vọt khỏi</b> nấm mồ mà sống lại.",
"жительство": "«<b>ZHY</b>-tyel-stva» — nghe như “<b>ghi tên</b>”: nơi bạn <b>ghi tên</b> thường trú (жить = sống).",
"образец": "«a-bra-<b>ZYETS</b>» — nghe như “<b>a, bà… DẸT</b>”: miếng vải mẫu ép <b>dẹt</b>, ghim lên bảng.",
"образование": "«a-bra-za-<b>VA</b>-nhiye» — nghe như “<b>va</b>”: bao năm <b>va</b> đầu vào sách mới nặn (образ) ra một con người.",
"помощь": "«<b>PO</b>-mashch» — nghe như “<b>bơm mạch</b>”: có người <b>bơm</b> thêm <b>mạch</b> sức cho bạn (мочь = có thể).",
"спряжение": "«spri-<b>ZHE</b>-nhiye» — nghe như “<b>xếp GHẾ</b>”: mỗi ngôi ngồi một cái <b>ghế</b> riêng = chia động từ.",
"спрягаться": "«spri-<b>GA</b>-tsa» — động từ tự leo lên <b>ghế</b> của ngôi mình (cùng nhà với спряжение).",
"съезд": "«<b>SYEST</b>» — nghe như “<b>XÉT</b>”: cả nghìn người dồn về một chỗ để <b>xét</b> việc lớn.",
"разъезд": "«raz-<b>YEST</b>» — nghe như “<b>dạt</b>”: người <b>dạt</b> đi khắp nơi, quanh năm không ở nhà.",
"разъём": "«raz-<b>YOM</b>» — nghe như “<b>rời… ÔM</b>”: hai đầu đang <b>ôm</b> nhau thì <b>rời</b> ra — đó là giắc cắm.",
"подъезд": "«pad-<b>YEST</b>» — nghe như “<b>bậc</b>”: bước lên <b>bậc</b> thềm, chui vào cửa <b>dưới</b> (под) chân chung cư.",
"подъём": "«pad-<b>YOM</b>» — nghe như “<b>bật… ÔM</b>”: còi hú, <b>bật</b> dậy, <b>ôm</b> chăn ngồi lên.",
"язык": "«yi-<b>ZYK</b>» — nghe như “<b>dí… DZÍCH</b>”: thè cái <b>lưỡi</b> <b>dí</b> vào răng mới bật ra tiếng.",
"цвет": "«<b>TSVYET</b>» — nghe như “<b>xờ-VIẾT</b>”: cầm bút <b>viết</b> lên giấy bằng đủ thứ <b>màu</b>.",
"рисунок": "«ri-<b>SU</b>-nak» — cặp với рисовать (“<b>rì rà vạch</b>”): vạch xong thì thành “<b>ri-SU-nốc</b>”, bức tranh treo tường.",
"забыть": "«za-<b>BYT</b>» — nghe như “<b>xa… BỊT</b>”: trí nhớ bị <b>bịt</b> lại, đẩy ra <b>xa</b> (за = ra sau).",
"звонить": "«zva-<b>NHIT</b>» — nghe như “<b>dzoong… NHÍT</b>”: chuông <b>dzoong</b> một cái, tay <b>nhít</b> lấy máy.",
"объявить": "«ab-yi-<b>VIT</b>» — nghe như “<b>vít</b>”: tờ tin được <b>vít</b> chặt lên bảng cho cả làng xem.",
"целовать": "«tsy-la-<b>VAT</b>» — nghe như “<b>XÌ-la-VÁT</b>”: chụm môi <b>xì</b> một cái lên má.",
"себя": "«si-<b>BYA</b>» — nghe như “<b>xi… BIA</b>”: tự rót <b>bia</b> cho <b>chính mình</b>.",
"потому": "«pa-ta-<b>MU</b>» — nghe như “<b>bởi ta mà</b>”: câu đáp cho “tại sao”.",
"почему": "«pa-chi-<b>MU</b>» — nghe như “<b>vì chi mà?</b>” — <b>chi</b> = gì: tại sao vậy?",
"девяностый": "«di-vi-<b>NOS</b>-tyy» — nghe như “<b>nốt</b>”: 90 rồi, thêm một <b>nốt</b> nữa là chạm mốc trăm.",
"тысячный": "«<b>TY</b>-sich-nyy» — <b>тысяча</b> ~ <b>thousand</b>: cùng mở đầu <b>t/th</b>, người thứ một nghìn.",
"двухтысячный": "«dvukh-<b>TY</b>-sich-nyy» — <b>два</b>(2) × <b>тысяча</b>(~<b>thousand</b>): pháo hoa đêm giao thừa năm 2000.",
"восьмидесятый": "«va-smi-di-<b>SYA</b>-tyy» — số 8 xoay đến <b>mỏi</b> mắt (восьмой), nhân lên <b>десят</b> (mươi).",
"пятидесятый": "«pya-ti-di-<b>SYA</b>-tyy» — cùng cái “<b>phía</b>” của <b>пять</b>(5), cộng <b>десят</b>(mươi): thứ năm mươi.",
})

S = {k: v for k, v in S.items() if v}
