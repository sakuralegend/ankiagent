# -*- coding: utf-8 -*-
"""k208 — concepts::emotion: ghen, tham, buồn, cãi nhau, phải lòng.

Chỗ cần nhất quán trong lô:
(1) д + т → ст: страсть (страд-) và за́висть (завид-) giải cùng một luật, khớp вла́сть [k115], не́нависть [k170].
(2) волнова́ть / взволнова́ть: волн- SÓNG, вз- BỪNG LÊN — khớp волнова́ться [k98], взволно́ванный [k198].
(3) руга́ться / поруга́ться, ссо́риться / поссо́риться: -ся «với nhau», по- chỉ biến thành HT.
    Ô đỏ «với ai / vì gì» đặt ở vế CHT, vế HT nói riêng điều của nó.
(4) влюби́ться / влюбля́ться: в- VÀO + люб- YÊU — khớp влюблённый [k159]. «в + cách 4» nói ở cả hai.
(5) ревнова́ть: ревн- GANH ĐUA, khớp соревнова́ние [k134]. за́висть KHÔNG cùng gốc зави́сеть [k128] (вид ≠ вис).
(6) нра́вственный: нрав- TÍNH NẾT, khớp нра́виться [k48].
Họ hàng không vắng ở thẻ nào (хулига́н là từ mượn nhưng có phái sinh thông dụng).
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "мрачный": "tối, âm u, u tối, ảm đạm, rầu rĩ, cau có",                      # THIẾU grim/dismal · morose
    "взволновать": "làm lo lắng, làm xúc động, làm hồi hộp, khiến bất an",      # «khiến bối rối» là смути́ть, gloss không có; THIẾU excite
    "волновать": "làm lo lắng, làm bận lòng, làm xúc động, làm hồi hộp, khiến bất an",  # THIẾU to move · to excite
    "жадность": "sự tham lam, lòng tham, tính hám lợi, tính keo kiệt, sự thèm khát",  # THIẾU stinginess · avidity
    "ругаться": "chửi thề, nói tục, chửi mắng, cãi nhau, chửi nhau",            # THIẾU to quarrel/argue · call each other names
    "влюбиться": "phải lòng, đem lòng yêu, đâm ra yêu",                         # «yêu» là люби́ть; «đổ» là lóng, đứng một mình dễ ra упа́сть/лить
    "влюбляться": "phải lòng, đem lòng yêu, đâm ra yêu",                        # như trên
}

# --------------------------------------------------------------------- унижение
S["унижение"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">у-</span>'
    '<span class="hd-gloss">LÀM CHO thành — như trong <b>увели́чить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ниж-</span>'
    '<span class="hd-gloss">THẤP — <b>ни́зкий</b>, з → ж như <b>ни́же</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ение</span>'
    '<span class="hd-gloss">→ danh từ, giống trung</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Làm cho thấp xuống» ⇒ hạ nhục, nỗi nhục. Tiếng Anh cùng hình ảnh: '
    '<i>humiliation</i> từ Latin <i>humilis</i> «thấp». Động từ gốc: <b>уни́зить</b> (HT) — '
    'thêm <b>-ение</b> thì з đổi thành ж.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>унижа́ть</b> hạ nhục (CHT) · <b>унизи́тельный</b> nhục nhã · '
    '<b>ни́зкий</b> thấp · <b>пони́зить</b> hạ xuống</div>'
)

# --------------------------------------------------------------------- трагический
S["трагический"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">траг-</span>'
    '<span class="hd-gloss">= <i>trag-</i> tiếng Anh (Hy Lạp)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ческий</span>'
    '<span class="hd-gloss">= đuôi <i>-ic(al)</i> của từ quốc tế, nhấn vào <b>и́</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Chữ <b>д</b> của <b>траге́дия</b> rơi mất, y như <i>tragedy → tragic</i>. '
    'Dùng cho cả kịch (<b>траги́ческая роль</b> vai bi kịch) lẫn chuyện đau lòng ngoài đời '
    '(<b>траги́ческий слу́чай</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>траге́дия</b> bi kịch · <b>траги́чный</b> bi thảm (gần như đồng nghĩa) · '
    '<b>траги́чески</b> một cách bi thảm</div>'
)

# --------------------------------------------------------------------- нравственный
S["нравственный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">нрав-</span>'
    '<span class="hd-gloss">TÍNH NẾT — <b>нрав</b>, như trong <b>нра́виться</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ств-</span>'
    '<span class="hd-gloss">đuôi danh từ trừu tượng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-енный</span>'
    '<span class="hd-gloss">→ tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Thuộc về nết ăn ở» ⇒ có đạo đức. Tiếng Anh cùng đường: <i>moral</i> từ Latin '
    '<i>mos, moris</i> «nếp, thói». Dạng ngắn giống đực có hai bản: <b>нра́вствен</b> / '
    '<b>нра́вственен</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>нра́вственность</b> đạo đức · <b>безнра́вственный</b> vô đạo đức · '
    '<b>нрав</b> tính khí · <b>нра́виться</b> thấy ưng</div>'
)

# --------------------------------------------------------------------- страстный
S["страстный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">страст-</span>'
    '<span class="hd-gloss">ĐAM MÊ — <b>страсть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi danh từ → tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why"><b>страсть</b> + <b>-ный</b> = đầy đam mê. Về từ nguyên, <b>страсть</b> ra từ '
    '<b>страда́ть</b> chịu đau (д + т → ст như <b>власть</b>) — y hệt <i>passion</i> từ Latin <i>pati</i> «chịu '
    'đựng». Dạng ngắn chen <b>-е-</b>: <b>стра́стен</b>, <b>стра́стна</b>.</div>'
    '<div class="hd-warn">Chữ <b>т</b> thứ hai không đọc nhưng PHẢI viết. Đừng lẫn với '
    '<b>стра́шный</b> đáng sợ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>страсть</b> đam mê · <b>стра́стно</b> say đắm (trạng từ) · '
    '<b>бесстра́стный</b> thản nhiên · <b>страда́ть</b> đau khổ</div>'
)

# --------------------------------------------------------------------- мрачный
S["мрачный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">мрач-</span>'
    '<span class="hd-gloss">BÓNG TỐI — <b>мрак</b>, к → ч trước -н-</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi danh từ → tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đầy bóng tối» ⇒ âm u (trời, nhà), rồi ảm đạm, rầu rĩ (mặt mày, ý nghĩ): '
    '<b>мра́чное лицо́</b> mặt rầu rĩ. Dạng ngắn chen <b>-е-</b>: <b>мра́чен</b>; giống cái nhấn đuôi: '
    '<b>мрачна́</b>.</div>'
    '<div class="hd-warn"><b>тёмный</b> chỉ là thiếu sáng hoặc sẫm màu, trung tính (tóc, áo, phòng); '
    '<b>мра́чный</b> là tối kèm cảm giác nặng nề.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>мрак</b> bóng tối · <b>мра́чно</b> ảm đạm (trạng từ) · '
    '<b>омрачи́ть</b> làm vẩn đục (niềm vui)</div>'
)

# --------------------------------------------------------------------- хулиган
S["хулиган"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: mượn nguyên tiếng Anh <i>hooligan</i> (h → <b>х</b>, oo → <b>у</b>).</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Rộng hơn <i>hooligan</i> bóng đá của tiếng Anh: mọi kẻ quậy phá nơi công cộng, '
    'và gọi cả đứa trẻ nghịch: <b>Ах ты, хулига́н!</b> Trọng âm ở <b>-га́н</b>, đứng yên khi thêm đuôi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>хулига́нка</b> (nữ) · <b>хулига́нить</b> quậy phá · '
    '<b>хулига́нство</b> hành vi côn đồ · <b>хулига́нский</b> côn đồ</div>'
)

# --------------------------------------------------------------------- ревновать
S["ревновать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ревн-</span>'
    '<span class="hd-gloss">GANH ĐUA — như trong <b>соревнова́ние</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ть</span>'
    '<span class="hd-gloss">đuôi động từ; ở hiện tại <b>-ова-</b> đổi thành <b>-у-</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ganh đua giành một người ⇒ ghen. Chia: <b>ревну́ю, ревну́ешь</b>.</div>'
    '<div class="hd-warn">Người mình yêu ở cách 4, tình địch là <b>к</b> + cách 3: '
    '<b>Он ревну́ет жену́ к сосе́ду</b> = anh ta ghen vợ với ông hàng xóm.</div>'
    '<div class="hd-warn">Ghen tình là <b>ревнова́ть</b>; ghen tị vì người ta có cái mình không có là '
    '<b>зави́довать</b> + cách 3.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ре́вность</b> sự ghen tuông · <b>ревни́вый</b> hay ghen · '
    '<b>соревнова́ние</b> cuộc thi đấu</div>'
)

# --------------------------------------------------------------------- взволновать
S["взволновать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вз-</span>'
    '<span class="hd-gloss">BỪNG LÊN</span></div>'
    '<div class="hd-row"><span class="hd-piece">-волн-</span>'
    '<span class="hd-gloss">SÓNG — <b>волна́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ть</span>'
    '<span class="hd-gloss">đuôi động từ; khi chia <b>-ова-</b> đổi thành <b>-у-</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Làm sóng bừng lên» trong lòng ai ⇒ làm xao động, lo lắng hay xúc động. Vế HT của '
    '<b>волнова́ть</b>: một tin, một cảnh làm lòng người DẬY lên — '
    '<b>Но́вость взволнова́ла всех.</b> Người bị xao động ở cách 4.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>волнова́ть</b> (CHT) · <b>взволно́ванный</b> xúc động · '
    '<b>волне́ние</b> sự xúc động · <b>волна́</b> con sóng</div>'
)

# --------------------------------------------------------------------- волновать
S["волновать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">волн-</span>'
    '<span class="hd-gloss">SÓNG — <b>волна́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова-ть</span>'
    '<span class="hd-gloss">đuôi động từ; ở hiện tại <b>-ова-</b> đổi thành <b>-у-</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Làm lòng ai «dậy sóng» ⇒ làm lo, làm xúc động. Chia: <b>волну́ю</b>, <b>волну́ет</b>.</div>'
    '<div class="hd-warn">Cái GÂY lo làm chủ ngữ, người lo ở cách 4: <b>Меня́ волну́ет его́ здоро́вье.</b> '
    'Người TỰ lo thì thêm <b>-ся</b>: <b>Я волну́юсь.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>взволнова́ть</b> (HT) · <b>волнова́ться</b> lo lắng · '
    '<b>волне́ние</b> sự xúc động · <b>волна́</b> con sóng</div>'
)

# --------------------------------------------------------------------- зависть
S["зависть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">tiền tố, nay không còn tách nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-вис-</span>'
    '<span class="hd-gloss">= <b>вид-</b> NHÌN — <b>ви́деть</b> (д trước т thành с)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ть</span>'
    '<span class="hd-gloss">đuôi danh từ giống cái, như <b>власть</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Nhìn sang» của người khác ⇒ đố kỵ. Chữ <b>д</b> gốc hiện lại ở <b>зави́довать</b>. '
    'Tiếng Anh cùng hình ảnh: <i>envy</i> từ Latin <i>in-videre</i> (<i>video</i> «nhìn»). '
    'Từ nguyên, không phải luật.</div>'
    '<div class="hd-warn">KHÔNG cùng gốc <b>зави́сеть</b> phụ thuộc (gốc <b>вис-</b> TREO) dù mặt chữ gần y hệt; '
    'trọng âm cũng khác chỗ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>зави́довать</b> ghen tị · <b>зави́дный</b> đáng ghen tị · '
    '<b>зави́стливый</b> hay đố kỵ · <b>не́нависть</b> lòng căm ghét</div>'
)

# --------------------------------------------------------------------- жадность
S["жадность"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">жад-</span>'
    '<span class="hd-gloss">THÈM KHÁT</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-</span>'
    '<span class="hd-gloss">đuôi tính từ — <b>жа́дный</b> tham</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ость</span>'
    '<span class="hd-gloss">danh từ trừu tượng, giống cái</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thèm thêm nữa ⇒ tham lam; thèm giữ khư khư ⇒ keo kiệt. Cùng gốc <b>жа́жда</b> cơn khát '
    '(từ nguyên, không phải luật).</div>'
    '<div class="hd-warn">Không phải lúc nào cũng xấu: <b>с жа́дностью</b> = ngấu nghiến, háo hức '
    '(<b>чита́ть с жа́дностью</b>).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жа́дный</b> tham, keo · <b>жа́дно</b> ngấu nghiến · '
    '<b>жа́дина</b> đồ keo kiệt · <b>жа́жда</b> cơn khát</div>'
)

# --------------------------------------------------------------------- грусть
S["грусть"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-why">Không chẻ được: gốc trơn <b>груст-</b> NỖI BUỒN — chính nó sinh ra '
    '<b>гру́стный</b>.</div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đuôi <b>-ь</b> ở đây là giống CÁI, chỉ dùng số ít: <b>лёгкая грусть</b> nỗi buồn man mác, '
    '<b>с гру́стью</b> một cách buồn bã. Động từ <b>грусти́ть</b> đổi ст → щ ở ngôi «tôi»: <b>грущу́</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>гру́стный</b> buồn · <b>гру́стно</b> buồn (trạng từ) · '
    '<b>грусти́ть</b> buồn rầu</div>'
)

# --------------------------------------------------------------------- поругаться
S["поругаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">chỉ biến thành HT, không nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-руг-а-ть</span>'
    '<span class="hd-gloss">MẮNG — <b>руга́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">với NHAU</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Mắng nhau» ⇒ cãi nhau to, thường là thành giận: '
    '<b>Я поруга́лся с бра́том.</b> Với ai: <b>с</b> + cách 5; vì gì: <b>из-за</b> + cách 2.</div>'
    '<div class="hd-warn">Bạo hơn <b>поссо́риться</b>: <b>поруга́ться</b> là to tiếng, nặng lời; '
    '<b>поссо́риться</b> có thể chỉ là giận nhau.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>руга́ться</b> (CHT) · <b>руга́ть</b> mắng · '
    '<b>отруга́ть</b> mắng cho một trận (HT) · <b>ру́гань</b> lời chửi bới</div>'
)

# --------------------------------------------------------------------- ругаться
S["ругаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">руг-а-ть</span>'
    '<span class="hd-gloss">MẮNG — <b>руга́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">với NHAU, hoặc mắng trống không</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Mắng nhau ⇒ cãi nhau; mắng trống không chẳng nhắm ai ⇒ chửi thề '
    '(<b>руга́ться ма́том</b> nói tục). Chia đều: <b>руга́юсь, руга́ешься</b>.</div>'
    '<div class="hd-warn">Giới từ đổi nghĩa: <b>с</b> + cách 5 = cãi nhau VỚI ai; '
    '<b>на</b> + cách 4 = chửi mắng ai.</div>'
    '<div class="hd-warn">Hai nghĩa, hai vế HT: cãi nhau → <b>поруга́ться</b>; chửi thề → <b>вы́ругаться</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>руга́ть</b> mắng · <b>ру́гань</b> lời chửi bới · '
    '<b>руга́тельство</b> câu chửi</div>'
)

# --------------------------------------------------------------------- поссориться
S["поссориться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">chỉ biến thành HT, không nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ссор-и-ть</span>'
    '<span class="hd-gloss">CÃI VÃ — <b>ссо́ра</b> cuộc cãi vã</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">với NHAU</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vế HT của <b>ссо́риться</b>: đã cãi và thành giận nhau — '
    '<b>Они́ поссо́рились</b> = họ cãi nhau rồi (đang giận). Làm hoà lại là <b>помири́ться</b>.</div>'
    '<div class="hd-warn">Bỏ <b>-ся</b> là nghĩa khác: <b>поссо́рить</b> + cách 4 = làm cho người ta bất hoà '
    'với nhau.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ссо́риться</b> (CHT) · <b>ссо́ра</b> cuộc cãi vã · '
    '<b>поссо́рить</b> gây bất hoà</div>'
)

# --------------------------------------------------------------------- ссориться
S["ссориться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ссор-</span>'
    '<span class="hd-gloss">CÃI VÃ — <b>ссо́ра</b>, viết HAI chữ <b>с</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть</span>'
    '<span class="hd-gloss">đuôi lớp 2: <b>ссо́рюсь, ссо́ришься</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">với NHAU</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vào cuộc <b>ссо́ра</b> với nhau ⇒ cãi nhau. Với ai: <b>с</b> + cách 5; vì gì: '
    '<b>из-за</b> + cách 2 — <b>Они́ ссо́рятся из-за де́нег.</b></div>'
    '<div class="hd-warn"><i>Argue</i> tiếng Anh gộp hai thứ: <b>ссо́риться</b> là cãi vã, sứt mẻ tình cảm; '
    '<b>спо́рить</b> là tranh luận, có thể vẫn vui vẻ.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>поссо́риться</b> (HT) · <b>ссо́ра</b> cuộc cãi vã · '
    '<b>поссо́рить</b> gây bất hoà</div>'
)

# --------------------------------------------------------------------- влюбиться
S["влюбиться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-люб-и-ть</span>'
    '<span class="hd-gloss">YÊU — <b>люби́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ся</span>'
    '<span class="hd-gloss">tự mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Tự rơi VÀO yêu» — y như <i>fall in love</i>. Chia y <b>люби́ть</b>: chỉ ngôi «tôi» '
    'chêm <b>л</b> và nhấn đuôi <b>влюблю́сь</b>, còn lại trọng âm lùi về gốc <b>влю́бишься</b>.</div>'
    '<div class="hd-warn">Phải lòng AI: <b>в</b> + cách 4 — <b>Он влюби́лся в неё.</b> '
    'Còn <b>люби́ть</b> thì cách 4 trơn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>влюбля́ться</b> (CHT) · <b>влюблённый</b> đang yêu · '
    '<b>люби́ть</b> yêu · <b>любо́вь</b> tình yêu</div>'
)

# --------------------------------------------------------------------- влюбляться
S["влюбляться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">в-</span>'
    '<span class="hd-gloss">VÀO</span></div>'
    '<div class="hd-row"><span class="hd-piece">-любл-</span>'
    '<span class="hd-gloss">YÊU — <b>люби́ть</b>, chêm <b>л</b> như <b>люблю́</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я-ть-ся</span>'
    '<span class="hd-gloss"><b>-я-</b> kéo dài ⇒ CHT; <b>-ся</b> tự mình</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vế CHT của <b>влюби́ться</b>: đang dần phải lòng, hoặc phải lòng hết lần này tới lần khác. '
    'Chữ <b>л</b> có ở MỌI ngôi, trọng âm đứng yên: <b>влюбля́юсь, влюбля́ешься</b>. Vẫn <b>в</b> + cách 4: '
    '<b>Он ча́сто влюбля́ется в актри́с.</b></div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>влюби́ться</b> (HT) · <b>влюблённый</b> đang yêu · '
    '<b>люби́ть</b> yêu · <b>любо́вь</b> tình yêu</div>'
)

B = {
    "docbangmat": 96,
    "loitubat": 3,   # страстный: viết «một chữ lệch là стра́шный» (lệch hai chữ) -> «đừng lẫn với»
                     # трагический: viết đuôi -и́ческий «luôn» nhấn и́ — nói quá -> bỏ «luôn»
                     # жадность: viện luật д → жд như рожде́ние cho жа́жда — không chắc đúng cơ chế -> bỏ, chỉ giữ «cùng gốc (từ nguyên)»
    "nguonsai": 1,   # bác khớp họ máy báo зависть ↔ зависеть (вид- NHÌN ≠ вис- TREO)
    "baolen": [
        "Khớp họ máy báo: зависть ↔ зависеть BÁC (ô đỏ cảnh báo trên thẻ); ревновать ↔ соревнование, нравственный ↔ нрав/нравиться, страстный ↔ страсть, жадность ↔ жадный ĐÚNG.",
        "Mức tin vừa (ghi rõ là từ nguyên ngay trên thẻ): страсть ← страда́ть (kèm passion ← pati), зависть ← ви́деть (kèm envy ← in-videre), жадность cùng gốc жа́жда.",
        "Không chắc, KHÔNG đưa lên thẻ: nguồn gốc ссо́ра, грусть, руг- và жад- ↔ ждать; мрак ↔ о́бморок (k203 đã hạ mức tin) không đưa vào Họ hàng.",
        "V cần duyệt (7 thẻ): мрачный (THÊM ảm đạm, cau có) · взволновать (BỎ «khiến bối rối» — đó là смути́ть; THÊM làm hồi hộp, khiến bất an) · волновать (THÊM làm xúc động, làm hồi hộp) · жадность (THÊM tính keo kiệt, sự thèm khát) · ругаться (THÊM cãi nhau, chửi nhau — gloss quarrel/argue) · влюбиться, влюбляться (BỎ «yêu» = люби́ть và «đổ» lóng; THÊM đem lòng yêu).",
        "поругаться / поссориться giữ «cãi nhau một trận» của đề cũ (gloss «have a row»), trùng một nghĩa nhưng khác phần còn lại; nếu coi «một trận» là dấu thể trá hình thì cần quyết chung cả với поспо́рить [k77].",
        "Trùng hết nghĩa trong lô chỉ có влюбиться/влюбляться — badge thể tách. Không có ca không gỡ được.",
    ],
}
