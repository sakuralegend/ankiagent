# -*- coding: utf-8 -*-
"""k229 — concepts::emotion: thái độ với người khác (thờ ơ, tế nhị, ganh tị, đoàn kết) và những cơn buồn, giận, bối rối.

Chỗ cần nhất quán trong lô:
(1) за-вид- NHÌN: зави́довать / позави́довать — khớp за́висть [k208].
(2) рас- RÃ RA: расстро́иться / расстра́иваться (стро- XẾP, khớp настрое́ние [k117], устро́ить [k160]), растеря́ться (теря́ть [k125]).
(3) мут- ĐỤC, khuấy: возмути́ться / возмуща́ться (т → щ).
(4) серд- TIM: серди́тый — khớp серди́ться [k226]; равн- BẰNG NHAU [k156] + душ- [k115]; помощ- [k52], бес- [k197].
(5) со- CÙNG + общ- CHUNG: сообща́ — khớp сообщи́ть [k100]. солида́рность KHÔNG có со- này.
Họ hàng không vắng ở thẻ nào.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "интеллигентный": "có văn hóa, có học thức, lịch thiệp, trí thức",  # THIẾU educated
    "ироничный": "mỉa mai, châm biếm",                        # gloss chỉ ironic; «hài hước kiểu trêu, đầy ẩn ý» là nới rộng
    "сердитый": "giận dữ, tức giận, cáu kỉnh",                # angry / cross; «giận dỗi» là hờn, «hầm hè» không có trong gloss
    "траур": "sự để tang, thời gian để tang",                 # «tang lễ» là по́хороны, gloss chỉ mourning
    "завидовать": "ganh tị, ghen tị, đố kỵ",                  # «thèm được như» là nới rộng; cùng dãy với cặp HT
    "позавидовать": "ganh tị, ghen tị, đố kỵ",                # như trên
    "расстраиваться": "buồn, thất vọng, đổ bể",               # THIẾU fall through / come to nothing; «chạnh lòng» không có trong gloss
    "расстроиться": "buồn, thất vọng, đổ bể",                 # như trên
    "возмутиться": "phẫn nộ, bất bình",                       # «nổi giận» là рассерди́ться
    "возмущаться": "phẫn nộ, bất bình",                       # «phản ứng dữ dội» không có trong gloss
    "теряться": "bị mất, bị lạc, biến mất, bối rối, luống cuống",  # THIẾU get flustered / be at a loss
}

# ------------------------------------------------------------ деликатный
S["деликатный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">деликат-</span>'
    '<span class="hd-gloss">gốc mượn, cùng ổ với Anh <i>delicate</i></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">→ tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chính là <i>delicate</i>, hai mặt của một ý «phải nhẹ tay»: NGƯỜI thì tế nhị, biết ý — <b>делика́тный челове́к</b>; CHUYỆN thì nhạy cảm, khó xử — <b>делика́тный вопро́с</b> câu hỏi nhạy cảm. Dạng ngắn giống đực chen <b>е</b>: <b>делика́тен</b>.</div>'
    '<div class="hd-warn">Đồ vật mong manh dễ vỡ thì <i>delicate</i> tiếng Anh lại là <b>хру́пкий</b>: <b>хру́пкая ва́за</b>.</div>'
    '<div class="hd-warn">Nút trên máy giặt: <b>делика́тная сти́рка</b> = giặt nhẹ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>делика́тность</b> sự tế nhị · <b>делика́тно</b> một cách tế nhị · <b>деликате́с</b> món ngon hiếm (Anh <i>delicacy</i>)</div>'
)

# ------------------------------------------------------------ интеллигентный
S["интеллигентный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">интеллигент-</span>'
    '<span class="hd-gloss">NGƯỜI TRÍ THỨC — <b>интеллиге́нт</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">→ tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ra dáng một <b>интеллиге́нт</b> ⇒ có học thức, có văn hoá; nói về cả cách cư xử nhã nhặn: <b>интеллиге́нтный челове́к</b>. Dạng ngắn giống đực chen <b>е</b>: <b>интеллиге́нтен</b>.</div>'
    '<div class="hd-warn">Bạn giả của Anh <i>intelligent</i>: «thông minh» là <b>у́мный</b>. <b>интеллиге́нтный</b> nói về HỌC VẤN, VĂN HOÁ chứ không phải đầu óc nhanh nhạy.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>интеллиге́нт</b> người trí thức · <b>интеллиге́нция</b> giới trí thức · <b>интелле́кт</b> trí tuệ</div>'
)

# ------------------------------------------------------------ ироничный
S["ироничный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ирон-</span>'
    '<span class="hd-gloss">SỰ MỈA MAI — <b>иро́ния</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ч-н-ый</span>'
    '<span class="hd-gloss">→ tính từ; trọng âm dời vào đây</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>иро́ния</b> bỏ <b>-ия</b>, thêm <b>-ичный</b> = Anh <i>ironic</i> ⇒ mỉa mai, châm biếm: <b>ирони́чная улы́бка</b> nụ cười mỉa. Dạng ngắn giống đực chen <b>е</b>: <b>ирони́чен</b>.</div>'
    '<div class="hd-warn">Nói NGƯỜI hay GIỌNG mỉa. Cảnh đời «trớ trêu» (<i>ironically…</i>) thì dùng cụm <b>по иро́нии судьбы́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>иро́ния</b> sự mỉa mai · <b>ирони́чно</b> một cách mỉa mai · <b>иронизи́ровать</b> châm biếm</div>'
)

# ------------------------------------------------------------ равнодушный
S["равнодушный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">равн-о-</span>'
    '<span class="hd-gloss">BẰNG NHAU — <b>ра́вный</b>; <b>о</b> nối hai gốc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-душ-</span>'
    '<span class="hd-gloss">TÂM HỒN — <b>душа́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ный</span>'
    '<span class="hd-gloss">→ tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Lòng lúc nào cũng bằng phẳng», được hay mất đều như nhau ⇒ thờ ơ. Thờ ơ VỚI gì → <b>к</b> + cách 3: <b>Я равноду́шен к футбо́лу</b> (dạng ngắn giống đực chen <b>е</b>).</div>'
    '<div class="hd-warn">Thêm <b>не-</b> thì không chỉ là «quan tâm»: <b>Он к ней неравноду́шен</b> = cậu ấy có tình ý với cô ấy.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>равноду́шие</b> sự thờ ơ · <b>всё равно́</b> sao cũng được · <b>душа́</b> tâm hồn · <b>доброду́шный</b> hiền hậu</div>'
)

# ------------------------------------------------------------ беспомощный
S["беспомощный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">бес-</span>'
    '<span class="hd-gloss">KHÔNG CÓ — <b>без-</b> viết thành <b>бес-</b> trước phụ âm vô thanh (п)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-помощ-</span>'
    '<span class="hd-gloss">SỰ GIÚP ĐỠ — <b>по́мощь</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ный</span>'
    '<span class="hd-gloss">→ tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ghép y như Anh <i>help-less</i>: không ai giúp là bó tay ⇒ bất lực, không tự lo được: <b>беспо́мощный ребёнок</b>. Trọng âm giữ chỗ của <b>по́мощь</b>. Dạng ngắn giống đực chen <b>е</b>: <b>беспо́мощен</b>.</div>'
    '<div class="hd-warn"><b>бесси́льный</b> cũng là «bất lực» nhưng do KHÔNG ĐỦ SỨC làm gì (<b>си́ла</b>); <b>беспо́мощный</b> là phải có người đỡ cho.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>по́мощь</b> sự giúp đỡ · <b>помога́ть</b> giúp · <b>мо́щный</b> mạnh · <b>беспо́мощность</b> sự bất lực</div>'
)

# ------------------------------------------------------------ сердитый
S["сердитый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">серд-</span>'
    '<span class="hd-gloss">TIM, cơn giận — <b>се́рдце</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́т-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cùng hình ảnh với <b>серди́ться</b>, tim đang nổi lên ⇒ cáu, giận: <b>серди́тый го́лос</b> giọng giận dữ. Giận AI → <b>на</b> + cách 4, hay dùng dạng ngắn: <b>Ты на меня́ серди́та?</b> = Em giận anh à?</div>'
    '<div class="hd-warn"><b>дёшево и серди́то</b> = rẻ mà tốt — cụm cố định, ở đây <b>серди́то</b> mang nghĩa «mạnh, ra trò», không giận dữ gì.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>серди́ться</b> giận · <b>рассерди́ться</b> nổi giận (HT) · <b>серди́то</b> giận dữ (trạng từ) · <b>се́рдце</b> trái tim</div>'
)

# ------------------------------------------------------------ оптимизм
S["оптимизм"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">оптим-</span>'
    '<span class="hd-gloss">Latin <i>optimus</i> — TỐT NHẤT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́зм</span>'
    '<span class="hd-gloss">chủ nghĩa, lối nghĩ (Anh <i>-ism</i>)</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= <i>optimism</i>: lối nghĩ «rồi sẽ tốt nhất». Người thì đổi <b>-изм → -ист</b>: <b>оптими́ст</b>. Trái nghĩa cùng khuôn: <b>пессими́зм</b> (gốc khác).</div>'
    '<div class="hd-warn">«Một cách lạc quan» = <b>с</b> + cách 5: <b>с оптими́змом смотре́ть в бу́дущее</b> nhìn tương lai một cách lạc quan.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>оптими́ст</b> người lạc quan · <b>оптимисти́чный</b> lạc quan · <b>оптима́льный</b> tối ưu</div>'
)

# ------------------------------------------------------------ траур
S["траур"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn nguyên tiếng Đức <i>Trauer</i> «nỗi đau, tang».</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Việc để tang và quãng thời gian để tang: <b>объяви́ть тра́ур</b> tuyên bố để tang, <b>быть в тра́уре</b> đang chịu tang. Kết bằng phụ âm → giống đực, thường chỉ dùng số ít.</div>'
    '<div class="hd-warn">Buổi «tang lễ» là <b>по́хороны</b> (luôn số nhiều), không phải <b>тра́ур</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>тра́урный</b> thuộc tang tóc</div>'
)

# ------------------------------------------------------------ завидовать
S["завидовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">tiền tố, nay không còn tách nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вид-</span>'
    '<span class="hd-gloss">NHÌN — <b>ви́деть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ть</span>'
    '<span class="hd-gloss">đuôi lớp 1, hiện tại <b>-ова- → -у-</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Nhìn sang» của người khác ⇒ ganh tị. Danh từ là <b>за́висть</b>; ở động từ chữ <b>д</b> gốc còn nguyên. Chia <b>зави́дую</b>, <b>зави́дуешь</b>. Cặp HT: <b>позави́довать</b>.</div>'
    '<div class="hd-warn">Ganh tị AI hay CÁI GÌ đều cách 3, không phải cách 4: <b>Я зави́дую тебе́</b> · <b>зави́довать чужо́му успе́ху</b>.</div>'
    '<div class="hd-warn">Ghen TUÔNG trong tình cảm là <b>ревнова́ть</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>за́висть</b> sự đố kỵ · <b>позави́довать</b> ganh tị (HT) · <b>зави́дный</b> đáng ghen tị · <b>зави́стливый</b> hay đố kỵ</div>'
)

# ------------------------------------------------------------ позавидовать
S["позавидовать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">chỉ đánh dấu thể hoàn thành</span></div>'
    '<div class="hd-row"><span class="hd-piece">за-вид-</span>'
    '<span class="hd-gloss">NHÌN sang người khác — <b>зави́довать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ть</span>'
    '<span class="hd-gloss">đuôi lớp 1, chia <b>-ова- → -у-</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp hoàn thành của <b>зави́довать</b>: lòng ganh tị chợt dấy lên. Chia <b>позави́дую</b>, <b>позави́дуешь</b>; vẫn đòi cách 3: <b>позави́довать его́ споко́йствию</b>.</div>'
    '<div class="hd-warn"><b>Ему́ не позави́дуешь</b> = chẳng ai muốn ở vào cảnh của anh ta — ngôi «bạn» nói chung cho mọi người.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>зави́довать</b> ganh tị (CHT) · <b>за́висть</b> sự đố kỵ · <b>зави́дный</b> đáng ghen tị</div>'
)

# ------------------------------------------------------------ грустить
S["грустить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">груст-</span>'
    '<span class="hd-gloss">NỖI BUỒN — <b>грусть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Mang nỗi buồn trong lòng» một thời gian. Chỉ ngôi «tôi» đổi <b>ст → щ</b>: <b>грущу́</b>, rồi <b>грусти́шь</b>, <b>грустя́т</b>. Đừng buồn: <b>Не грусти́!</b></div>'
    '<div class="hd-warn">Buồn VÌ NHỚ ai, nhớ đâu → <b>по</b> + cách 3: <b>грусти́ть по до́му</b>.</div>'
    '<div class="hd-warn">Lúc này đang thấy buồn thì tự nhiên hơn là <b>мне гру́стно</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>грусть</b> nỗi buồn · <b>гру́стный</b> buồn · <b>гру́стно</b> buồn (trạng từ) · <b>погрусти́ть</b> buồn một lúc</div>'
)

# ------------------------------------------------------------ солидарность
S["солидарность"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">солидар-н-</span>'
    '<span class="hd-gloss">ĐỒNG LÒNG — <b>солида́рный</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span>'
    '<span class="hd-gloss">→ danh từ giống cái, như <b>но́вость</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">= Anh <i>solidarity</i>, gốc Latin <i>solidus</i> «đặc, chắc»: nhiều người kết thành một khối chắc ⇒ tình đoàn kết. Đoàn kết VỚI ai → <b>с</b> + cách 5: <b>в знак солида́рности с рабо́чими</b> để tỏ tình đoàn kết với công nhân.</div>'
    '<div class="hd-warn">Chữ <b>со</b> đầu từ nằm trong gốc mượn, KHÔNG phải tiền tố <b>со-</b> CÙNG của <b>сочу́вствие</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>солида́рный</b> đồng lòng · <b>соли́дный</b> bề thế, đáng nể (cùng gốc Latin)</div>'
)

# ------------------------------------------------------------ расстраиваться
S["расстраиваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рас-</span>'
    '<span class="hd-gloss">RÃ RA, hỏng trật tự</span></div>'
    '<div class="hd-row"><span class="hd-piece">-стра́и-</span>'
    '<span class="hd-gloss">= <b>стро-</b> XẾP, dựng (о → а)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ва-ть-ся</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành, phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>настрое́ние</b> là lòng đã «lên dây» đúng; <b>рас-</b> làm nó lạc dây ⇒ buồn, thất vọng. Thể CHT đổi <b>о → а</b>, cùng khuôn <b>устро́ить → устра́ивать</b>. Chia đều: <b>расстра́иваюсь</b>. Buồn VÌ gì → <b>из-за</b> + cách 2.</div>'
    '<div class="hd-warn">An ủi ai thì dùng đúng thể này: <b>Не расстра́ивайся!</b> = Đừng buồn!</div>'
    '<div class="hd-warn">Viết <b>hai с</b>: một của <b>рас-</b>, một của <b>стро-</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>расстро́иться</b> buồn (HT) · <b>настрое́ние</b> tâm trạng · <b>расстро́енный</b> đang buồn · <b>стро́ить</b> xây</div>'
)

# ------------------------------------------------------------ расстроиться
S["расстроиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рас-</span>'
    '<span class="hd-gloss">RÃ RA, hỏng trật tự</span></div>'
    '<div class="hd-row"><span class="hd-piece">-стро-</span>'
    '<span class="hd-gloss">XẾP, dựng — <b>стро́ить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ить-ся</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai, phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thứ đang xếp ngay ngắn bị rã»: LÒNG rã ⇒ buồn, thất vọng (<b>Я расстро́ился из-за оце́нки</b>); KẾ HOẠCH rã ⇒ đổ bể (<b>Пое́здка расстро́илась</b>). Chia như <b>стро́ить</b>: <b>расстро́юсь</b>, <b>расстро́ишься</b>. Viết <b>hai с</b>.</div>'
    '<div class="hd-warn">Cơ thể cũng «rã» được: <b>расстро́йство желу́дка</b> = rối loạn tiêu hoá.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>расстра́иваться</b> buồn (CHT) · <b>настрое́ние</b> tâm trạng · <b>расстро́ить</b> làm buồn, làm hỏng · <b>устро́ить</b> sắp xếp</div>'
)

# ------------------------------------------------------------ любоваться
S["любоваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">люб-</span>'
    '<span class="hd-gloss">YÊU, thấy hợp ý — <b>люби́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова́-ть-ся</span>'
    '<span class="hd-gloss">đuôi lớp 1 (<b>-ова- → -у-</b>), phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhìn mà thấy YÊU ⇒ ngắm, chiêm ngưỡng. Hiện tại <b>любу́юсь</b>, <b>любу́ешься</b>. Cặp HT: <b>полюбова́ться</b>.</div>'
    '<div class="hd-warn">Ngắm CÁI GÌ → cách 5 trơ, không giới từ: <b>любова́ться зака́том</b> ngắm hoàng hôn, <b>любова́ться ви́дом</b> ngắm cảnh.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>люби́ть</b> yêu, thích · <b>любо́вь</b> tình yêu · <b>люби́мый</b> yêu thích · <b>полюбова́ться</b> ngắm (HT)</div>'
)

# ------------------------------------------------------------ возмутиться
S["возмутиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">воз-</span>'
    '<span class="hd-gloss">LÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мут-</span>'
    '<span class="hd-gloss">ĐỤC, khuấy — <b>му́тный</b> đục</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ть-ся</span>'
    '<span class="hd-gloss">đuôi lớp chia thứ hai, phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Lòng như nước bị «khuấy đục lên» ⇒ phẫn nộ, bất bình. Ngôi «tôi» đổi <b>т → щ</b>: <b>возмущу́сь</b>, <b>возмути́шься</b>. Phẫn nộ VÌ gì → cách 5: <b>возмути́ться его́ отве́том</b>. Cặp CHT: <b>возмуща́ться</b>.</div>'
    '<div class="hd-warn">Đứng sau lời thoại trong truyện thì nghĩa là «bất bình NÓI»: <b>«Как так?!» — возмути́лась она́.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>возмуща́ться</b> phẫn nộ (CHT) · <b>возмуще́ние</b> sự phẫn nộ · <b>возмути́тельный</b> đáng phẫn nộ · <b>му́тный</b> đục</div>'
)

# ------------------------------------------------------------ возмущаться
S["возмущаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">воз-</span>'
    '<span class="hd-gloss">LÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-мущ-</span>'
    '<span class="hd-gloss">= <b>мут-</b> ĐỤC, khuấy — <b>му́тный</b> đục (т → щ)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́ть-ся</span>'
    '<span class="hd-gloss">đuôi chưa hoàn thành, phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Cặp chưa hoàn thành của <b>возмути́ться</b>: lòng cứ bị «khuấy đục lên», hay gặp ở nghĩa kêu ca, phản đối kéo dài — <b>Сосе́ди возмуща́ются</b>. Chia đều: <b>возмуща́юсь</b>. Vẫn đòi cách 5: <b>возмуща́ться це́нами</b> bất bình về giá cả.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>возмути́ться</b> phẫn nộ (HT) · <b>возмуще́ние</b> sự phẫn nộ · <b>возмути́тельный</b> đáng phẫn nộ · <b>му́тный</b> đục</div>'
)

# ------------------------------------------------------------ растеряться
S["растеряться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рас-</span>'
    '<span class="hd-gloss">RÃ RA, tứ tán</span></div>'
    '<div class="hd-row"><span class="hd-piece">-теря́-ть</span>'
    '<span class="hd-gloss">MẤT — <b>теря́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">quay việc về CHÍNH MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Tự đánh mất mình, hồn vía tứ tán» ⇒ bối rối, luống cuống: <b>Я растеря́лся и забы́л её и́мя</b>. Chia đều: <b>растеря́юсь</b>, <b>растеря́ешься</b>.</div>'
    '<div class="hd-warn">Bị lạc (không biết đường) là <b>потеря́ться</b>. <b>растеря́ться</b> là lạc ĐẦU ÓC; nói đồ vật thì là thất lạc dần từng cái.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>теря́ть</b> mất · <b>теря́ться</b> bị mất, luống cuống (CHT) · <b>расте́рянный</b> bối rối · <b>расте́рянность</b> sự bối rối</div>'
)

# ------------------------------------------------------------ теряться
S["теряться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">теря́-ть</span>'
    '<span class="hd-gloss">MẤT — chính là <b>теря́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">quay việc về CHÍNH MÌNH</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Tự mình «mất»: ĐỒ thì bị mất, NGƯỜI thì bị lạc, ĐẦU ÓC thì luống cuống. Chia đều: <b>теря́юсь</b>, <b>теря́ешься</b>. <b>Не теря́йся!</b> = đừng để bị lạc; đừng bối rối.</div>'
    '<div class="hd-warn">Cặp HT chọn theo nghĩa: bị mất, bị lạc → <b>потеря́ться</b>; luống cuống → <b>растеря́ться</b>.</div>'
    '<div class="hd-warn"><b>теря́ться в дога́дках</b> = đoán mãi không ra.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>теря́ть</b> mất, đánh mất · <b>потеря́ть</b> mất (HT) · <b>поте́ря</b> sự mất mát · <b>растеря́ться</b> luống cuống</div>'
)

# ------------------------------------------------------------ сообща
S["сообща"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG</span></div>'
    '<div class="hd-row"><span class="hd-piece">-общ-</span>'
    '<span class="hd-gloss">CHUNG — gốc của <b>о́бщий</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́</span>'
    '<span class="hd-gloss">đuôi cách 2 cổ đông cứng thành trạng từ, như <b>спра́ва</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">CÙNG + CHUNG ⇒ chung sức, hợp lực làm một việc: <b>реши́ть пробле́му сообща́</b> chung sức giải quyết vấn đề. Trạng từ nên không biến đổi.</div>'
    '<div class="hd-warn"><b>вме́сте</b> chỉ cần CÙNG NHAU (đi, ở, ngồi); <b>сообща́</b> là mỗi người GÓP một phần vào việc chung.</div>'
    '<div class="hd-warn">Thêm <b>-ть</b> thành <b>сообща́ть</b> báo tin — cùng hai mảnh <b>со- + общ-</b>, nghĩa rẽ khác.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>о́бщий</b> chung · <b>о́бщество</b> xã hội · <b>сообщи́ть</b> báo tin (HT) · <b>вообще́</b> nói chung</div>'
)

B = {
    "docbangmat": 125,
    "loitubat": 4,   # деликатный: lấy делика́тная ко́жа làm ví dụ nòng cốt (chuẩn là чувстви́тельная ко́жа) -> bỏ, thay делика́тный челове́к
                     # сердитый: viết «tính từ CỦA серди́ться» (thật ra cùng đi từ се́рдце) -> «cùng hình ảnh với»
                     # грустить: ghi погрусти́ть là cặp HT (chỉ là «buồn một lúc») -> bỏ nhãn HT
                     # интеллигентный: «không khen trí óc» nói quá (gloss có intellectual) -> «học vấn, văn hoá chứ không phải đầu óc nhanh nhạy»
    "nguonsai": 1,   # интеллигентный: gloss đặt «intelligent» đầu dòng — bạn giả, «thông minh» là у́мный; bác ở ô đỏ
    "baolen": [
        "Va chạm вме́сте [k74] «cùng nhau» nằm gọn trong сообща: KHÔNG đổi V сообща — đã có sẵn «chung sức, hợp lực» nên không trùng HẾT; phân biệt ở ô đỏ thẻ сообща.",
        "V cần duyệt (11 thẻ): интеллигентный (THÊM có học thức) · ироничный (BỎ hài hước kiểu trêu, đầy ẩn ý; THÊM mỉa mai) · сердитый (tức tối, giận dỗi, hầm hè -> giận dữ, tức giận, cáu kỉnh) · траур (BỎ tang lễ) · завидовать, позавидовать (cùng dãy ganh tị, ghen tị, đố kỵ) · расстраиваться, расстроиться (BỎ chạnh lòng; THÊM đổ bể) · возмутиться, возмущаться (cùng dãy phẫn nộ, bất bình) · теряться (THÊM bối rối, luống cuống, biến mất).",
        "теряться / растеряться KHÔNG san cùng dãy: cặp HT của теряться tuỳ nghĩa (потеря́ться bị lạc, растеря́ться luống cuống) — chỉ chung «bối rối, luống cuống». «lịch thiệp» ở интеллигентный gloss không ghi thẳng, GIỮ theo «cultured» và cách dùng thật.",
        "Trùng hết nghĩa trong lô chỉ có 3 cặp thể (завид-, расстр-, возму-) — badge thể tách. Chưa chạy lại vacham với V mới (không đọc Anki).",
        "Từ nguyên máy báo đều ĐÚNG. Không chắc, KHÔNG đưa lên thẻ: смути́ться / смуща́ться cùng gốc мут- (nghĩ là đúng, nhưng chưa có thẻ để khớp).",
        "Ngoài phạm vi: câu ví dụ trong _opus_k229.json dùng số nhiều gượng — «дешёвые оптими́змы», «пусты́х солида́рностей», «в национа́льных тра́урах» (ba từ này thực tế chỉ dùng số ít).",
    ],
}
