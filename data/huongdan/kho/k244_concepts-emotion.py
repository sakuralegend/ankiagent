# -*- coding: utf-8 -*-
"""k244 — concepts::emotion: nghĩ và tính (phân tích, kế hoạch, nghĩ kỹ, đối chiếu, nhầm); nết người; ngắm và ngưỡng mộ.

Chỗ cần nhất quán trong lô:
(1) про- = XUYÊN SUỐT ở проанализировать, продумать, продумывать; -дум- NGHĨ như обдумать [k198], придумать [k170].
(2) путать / перепутать: -пут- LÀM RỐI, quấn chân (пу́ты) — KHÔNG dính путь.
(3) сопоставить / сопоставлять: со- CÙNG + поставить ĐẶT [k02], л chêm như составлять [k80].
(4) полюбоваться chẻ y любоваться [k229]; воспитанный y воспитать [k147]; ревн- y ревновать [k208]; жад- y жадность [k208].
(5) восхититься / восхищаться: вос- LÊN + хит- CHỘP, т → щ.
(6) Phân từ hoá tính từ (воспитанный, рассеянный): dạng ngắn tính từ giữ -нн-.
Họ hàng không vắng ở thẻ nào.
"""

S = {}

# 🔴 Dòng tiếng Việt = đề bài deck 1-go (README §2c): thuần danh sách nghĩa.
V = {
    "проанализировать": "phân tích",                                    # «mổ xẻ» là nới rộng; khớp анализировать
    "продумать": "nghĩ kỹ, tính toán kỹ, cân nhắc",                     # «cân nhắc xong» là chú thể, badge lo
    "продумывать": "nghĩ kỹ, tính toán kỹ, cân nhắc",                   # giữ nguyên, khai để cặp thể cùng dãy
    "перепутать": "nhầm, lẫn lộn, làm rối",                             # cặp thể cùng dãy
    "путать": "nhầm, lẫn lộn, làm rối",                                 # giữ nguyên
    "сопоставить": "đối chiếu, đặt cạnh nhau để xét",                   # BỎ «so sánh» (bọc trọn сравнить); thêm juxtapose
    "сопоставлять": "đối chiếu, đặt cạnh nhau để xét",                  # như trên
    "героический": "anh hùng, hào hùng",                                # «dũng cảm» là смелый, gloss chỉ heroic
    "жадный": "tham lam, hám lợi, keo kiệt, bủn xỉn, thèm khát",        # THIẾU avid / hungry; khớp жадность
    "воспитанный": "lễ phép, có giáo dục, được dạy dỗ tử tế",           # «ngoan ngoãn» là послушный
    "рассеянный": "lơ đãng, đãng trí, mất tập trung, tản mát, khuếch tán",  # THIẾU scattered / diffuse
    "властный": "hống hách, đầy uy quyền, hay ra lệnh, thuộc chính quyền",  # «uy quyền» trơ là danh từ; THIẾU governmental
    "полюбоваться": "ngắm, chiêm ngưỡng, thưởng ngoạn",                 # cùng thứ tự любоваться
    "восхититься": "ngưỡng mộ, trầm trồ khen, thích thú",               # cặp thể cùng dãy
    "восхищаться": "ngưỡng mộ, trầm trồ khen, thích thú",               # «say mê» là увлекаться
}

# --------------------------------------------------------------------- проанализировать
S["проанализировать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">XUYÊN SUỐT, từ đầu đến cuối</span></div>'
    '<div class="hd-row"><span class="hd-piece">анализ-</span>'
    '<span class="hd-gloss">← <b>ана́лиз</b> sự phân tích</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ровать</span>'
    '<span class="hd-gloss">khuôn biến từ mượn thành động từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Phân tích SUỐT từ đầu đến cuối ⇒ đã phân tích xong, có kết luận. Vế HT của <b>анализи́ровать</b>: trọng âm vẫn đứng ở <b>-и́р-</b>, <b>-ова-</b> co thành <b>-у-</b> — <b>проанализи́рую</b>, <b>проанализи́руешь</b>.</div>'
    '<div class="hd-warn">Đi thẳng cách 4, không giới từ: <b>проанализи́ровать оши́бки</b> phân tích các lỗi.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ана́лиз</b> sự phân tích · <b>анализи́ровать</b> phân tích (CHT) · <b>анали́тик</b> nhà phân tích</div>'
)

# --------------------------------------------------------------------- запланировать
S["запланировать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">за-</span>'
    '<span class="hd-gloss">chỉ báo thể hoàn thành, không thêm nghĩa riêng</span></div>'
    '<div class="hd-row"><span class="hd-piece">план-</span>'
    '<span class="hd-gloss">kế hoạch — chính là <b>план</b> (La-tinh <i>planum</i>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-ирова-ть</span>'
    '<span class="hd-gloss">biến từ mượn thành động từ, chia <i>-у-</i>: <b>заплани́рую</b></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Kế hoạch đã CHỐT ⇒ lên kế hoạch xong, xếp lịch. Cặp CHT là <b>плани́ровать</b> (còn đang tính). Có thêm một vế HT gần như đồng nghĩa: <b>сплани́ровать</b>.</div>'
    '<div class="hd-warn">Xếp vào NGÀY NÀO → <b>на</b> + cách 4: <b>заплани́ровать встре́чу на суббо́ту</b> xếp cuộc gặp vào thứ Bảy.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>план</b> kế hoạch · <b>плани́ровать</b> lập kế hoạch (CHT) · <b>заплани́рованный</b> đã lên kế hoạch · <b>планиро́вка</b> cách bố trí mặt bằng</div>'
)

# --------------------------------------------------------------------- продумать
S["продумать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">XUYÊN SUỐT, từ đầu đến cuối</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дум-</span>'
    '<span class="hd-gloss">NGHĨ — như <b>ду́мать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi động từ, thể hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nghĩ SUỐT từ đầu đến cuối, không sót bước nào ⇒ nghĩ kỹ, tính toán kỹ. Trọng âm đứng yên ở <b>-ду́-</b> như <b>ду́мать</b>. Vế CHT: <b>проду́мывать</b>.</div>'
    '<div class="hd-warn">Khác <b>ду́мать о</b> + cách 6: <b>проду́мать</b> đi THẲNG cách 4, không giới từ — <b>проду́мать план</b>.</div>'
    '<div class="hd-warn">Khác <b>обду́мать</b> (nghĩ QUANH một chuyện rồi mới quyết): <b>проду́мать</b> là tính đủ từng chi tiết của thứ sắp làm.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ду́мать</b> nghĩ · <b>обду́мать</b> suy nghĩ kỹ · <b>приду́мать</b> nghĩ ra · <b>проду́манный</b> được tính kỹ</div>'
)

# --------------------------------------------------------------------- продумывать
S["продумывать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">про-</span>'
    '<span class="hd-gloss">XUYÊN SUỐT, từ đầu đến cuối</span></div>'
    '<div class="hd-row"><span class="hd-piece">-дум-</span>'
    '<span class="hd-gloss">NGHĨ — như <b>ду́мать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ыва-ть</span>'
    '<span class="hd-gloss">kéo dài ⇒ thể CHT</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vế CHT của <b>проду́мать</b>: đang tính từng bước, hoặc lần nào cũng tính. Chia đều lớp 1: <b>проду́мываю</b>, <b>проду́мываешь</b>. Cùng khuôn <b>обду́мывать</b>, <b>приду́мывать</b>.</div>'
    '<div class="hd-warn">Cũng đi thẳng cách 4: <b>проду́мывать ка́ждый шаг</b> tính kỹ từng bước.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>проду́мать</b> nghĩ kỹ (HT) · <b>ду́мать</b> nghĩ · <b>обду́мывать</b> nghiền ngẫm · <b>приду́мывать</b> nghĩ ra (CHT)</div>'
)

# --------------------------------------------------------------------- перепутать
S["перепутать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пере-</span>'
    '<span class="hd-gloss">CHÉO qua nhau, lẫn chỗ này sang chỗ kia</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пут-</span>'
    '<span class="hd-gloss">LÀM RỐI, quấn chân — như <b>пу́тать</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi động từ, thể hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Các sợi đan CHÉO vào nhau ⇒ làm rối; trong đầu thì cái này lẫn sang cái kia ⇒ nhầm. Cặp CHT: <b>пу́тать</b>. Chia đều lớp 1: <b>перепу́таю</b>, <b>перепу́таешь</b>.</div>'
    '<div class="hd-warn">Nhầm CÁI GÌ (cách 4) VỚI cái gì → <b>с</b> + cách 5: <b>перепу́тать соль с са́харом</b>. Hai thứ ngang nhau thì nối bằng <b>и</b>: <b>перепу́тать имена́ и да́ты</b>.</div>'
    '<div class="hd-warn"><b>ошиби́ться</b> là sai nói chung; <b>перепу́тать</b> luôn là lấy thứ NÀY thành thứ KIA.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>пу́тать</b> nhầm (CHT) · <b>пу́таница</b> sự lộn xộn · <b>запу́таться</b> bị rối, lạc lối · <b>распу́тать</b> gỡ rối</div>'
)

# --------------------------------------------------------------------- путать
S["путать"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">пут-</span>'
    '<span class="hd-gloss">LÀM RỐI, quấn chân — cùng gốc <b>пу́ты</b> dây buộc chân ngựa</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-ть</span>'
    '<span class="hd-gloss">đuôi động từ, chia đều lớp 1</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Quấn rối như dây ⇒ làm rối; rối trong đầu ⇒ nhầm cái này với cái kia. <b>Вы меня́ с ке́м-то пу́таете.</b> = Anh nhầm tôi với ai rồi. Cặp HT: <b>перепу́тать</b>.</div>'
    '<div class="hd-warn">Nhầm CÁI GÌ (cách 4) VỚI cái gì → <b>с</b> + cách 5: <b>пу́тать дру́жбу с любо́вью</b>.</div>'
    '<div class="hd-warn">KHÔNG dính <b>путь</b> con đường, <b>путеше́ствие</b> chuyến đi — mặt chữ giống nhưng khác gốc.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>перепу́тать</b> nhầm (HT) · <b>пу́таница</b> sự lộn xộn · <b>запу́таться</b> bị rối, lạc lối · <b>распу́тать</b> gỡ rối</div>'
)

# --------------------------------------------------------------------- сопоставить
S["сопоставить"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG, gộp lại với nhau</span></div>'
    '<div class="hd-row"><span class="hd-piece">-по-став-</span>'
    '<span class="hd-gloss">ĐẶT cho đứng — như <b>поста́вить</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-и-ть</span>'
    '<span class="hd-gloss">đuôi động từ lớp 2, thể hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đặt hai thứ ĐỨNG CẠNH NHAU mà soi ⇒ đối chiếu. Ngôi «tôi» chêm <b>л</b> như <b>поста́влю</b>: <b>сопоста́влю</b>, còn lại <b>сопоста́вишь</b>… Cặp CHT: <b>сопоставля́ть</b>.</div>'
    '<div class="hd-warn">Đối chiếu cái gì (cách 4) VỚI cái gì → <b>с</b> + cách 5: <b>сопоста́вить слова́ с фа́ктами</b> đối chiếu lời nói với sự thật.</div>'
    '<div class="hd-warn">Khác <b>сравни́ть</b> (xem hơn kém, giống khác — nói hằng ngày): <b>сопоста́вить</b> là đặt dữ kiện cạnh nhau để RÚT RA điều gì, giọng sách vở hơn.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сопоставля́ть</b> đối chiếu (CHT) · <b>сопоставле́ние</b> sự đối chiếu · <b>поста́вить</b> đặt đứng · <b>соста́вить</b> lập ra</div>'
)

# --------------------------------------------------------------------- сопоставлять
S["сопоставлять"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">со-</span>'
    '<span class="hd-gloss">CÙNG, gộp lại với nhau</span></div>'
    '<div class="hd-row"><span class="hd-piece">-по-ставл-</span>'
    '<span class="hd-gloss">ĐẶT cho đứng — <b>л</b> chêm sau <b>в</b> như ở <b>сопоста́влю</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-я́ть</span>'
    '<span class="hd-gloss">đuôi thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vế CHT của <b>сопоста́вить</b>: chữ <b>л</b> mà vế HT chỉ có ở ngôi «tôi» thì ở đây có mặt mọi ngôi. Trọng âm nhảy ra đuôi, chia đều: <b>сопоставля́ю</b>, <b>сопоставля́ешь</b>. Cùng khuôn <b>составля́ть</b>.</div>'
    '<div class="hd-warn">Vẫn <b>с</b> + cách 5: <b>сопоставля́ть тео́рию с пра́ктикой</b> đối chiếu lý thuyết với thực tế.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>сопоста́вить</b> đối chiếu (HT) · <b>сопоставле́ние</b> sự đối chiếu · <b>составля́ть</b> lập, cấu thành · <b>ста́вить</b> đặt</div>'
)

# --------------------------------------------------------------------- героический
S["героический"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">геро-</span>'
    '<span class="hd-gloss"><b>геро́й</b> anh hùng (<b>й</b> rụng trước <b>и</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́ческий</span>'
    '<span class="hd-gloss">đuôi tính từ quốc tế, ứng với tiếng Anh <i>-ic</i></span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Ghép đúng như <i>hero-ic</i> ⇒ anh hùng, hào hùng. Đuôi <b>-и́ческий</b> luôn giữ trọng âm ở <b>и́</b>: <b>истори́ческий</b>, <b>полити́ческий</b>. Trạng từ: <b>герои́чески</b>.</div>'
    '<div class="hd-warn">Cụm hay gặp: <b>герои́ческий посту́пок</b> hành động anh hùng. Từ này theo nghĩa «người dũng cảm» của <b>геро́й</b>, không theo nghĩa «nhân vật truyện».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>геро́й</b> anh hùng; nhân vật · <b>герои́ня</b> nữ anh hùng · <b>герои́зм</b> tinh thần anh hùng · <b>геро́йство</b> hành động anh hùng</div>'
)

# --------------------------------------------------------------------- везучий
S["везучий"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вез-</span>'
    '<span class="hd-gloss">gốc CHỞ, ở đây theo nghĩa GẶP MAY — như <b>мне везёт</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-у́ч-ий</span>'
    '<span class="hd-gloss">«sẵn tính hay làm thế»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Người mà lúc nào cũng <b>везёт</b> ⇒ may mắn, hên. Cùng khuôn: <b>колю́чий</b> hay đâm ⇒ có gai, <b>лету́чий</b> hay bay. Trái nghĩa: <b>невезу́чий</b> xui xẻo.</div>'
    '<div class="hd-warn">Chỉ nói về NGƯỜI có số hên. Việc suôn sẻ thì dùng <b>уда́чный</b>: <b>уда́чный день</b>.</div>'
    '<div class="hd-warn">Đừng lẫn với <b>везу́щий</b> (chữ <b>щ</b>): phân từ thật, nghĩa «đang chở».</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>везти́</b> chở; gặp may · <b>повезти́</b> gặp may (HT) · <b>везе́ние</b> vận may · <b>невезу́чий</b> xui</div>'
)

# --------------------------------------------------------------------- трусливый
S["трусливый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">трус-</span>'
    '<span class="hd-gloss">KẺ NHÁT GAN — chính là <b>трус</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ли́в-ый</span>'
    '<span class="hd-gloss">«có nết đó»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Có nết của một <b>трус</b> ⇒ nhát gan, hèn nhát. Đuôi <b>-лив-</b> gọi tên nết người: <b>терпели́вый</b> kiên nhẫn, <b>молчали́вый</b> ít nói. Trạng từ: <b>трусли́во</b>.</div>'
    '<div class="hd-warn">Mắng một người hèn thì dùng thẳng danh từ: <b>Ты трус!</b> Tính từ để tả nết, kể cả con vật: <b>трусли́вый пёс</b> con chó nhát.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>трус</b> kẻ nhát gan · <b>тру́сость</b> sự hèn nhát · <b>тру́сить</b> sợ, chùn bước</div>'
)

# --------------------------------------------------------------------- ревнивый
S["ревнивый"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">ревн-</span>'
    '<span class="hd-gloss">GANH ĐUA — như trong <b>ревнова́ть</b> (nay = ghen)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́в-ый</span>'
    '<span class="hd-gloss">đuôi tính từ «có tính đó»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Có tính ganh đua giành một người ⇒ hay ghen. Cùng đuôi với <b>трудолюби́вый</b> chăm chỉ. Trạng từ: <b>ревни́во</b>.</div>'
    '<div class="hd-warn">Đây là ghen vì sợ bị GIÀNH MẤT. Ghen tị vì người ta có cái mình không có là <b>зави́стливый</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>ревнова́ть</b> ghen · <b>ре́вность</b> sự ghen tuông · <b>соревнова́ние</b> cuộc thi đấu</div>'
)

# --------------------------------------------------------------------- жадный
S["жадный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">жад-</span>'
    '<span class="hd-gloss">THÈM KHÁT — như trong <b>жа́дность</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Thèm thêm nữa ⇒ tham lam; thèm giữ khư khư ⇒ keo kiệt; thèm biết ⇒ <b>жа́дный к зна́ниям</b> khát khao hiểu biết. Trạng từ <b>жа́дно</b> = ngấu nghiến. Trái nghĩa: <b>ще́дрый</b> hào phóng.</div>'
    '<div class="hd-warn">Dạng ngắn: giống đực chen <b>е</b> — <b>жа́ден</b>; giống cái đẩy trọng âm ra đuôi — <b>жадна́</b>.</div>'
    '<div class="hd-warn">Tham CÁI GÌ → <b>до</b> + cách 2: <b>жа́дный до де́нег</b> hám tiền.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>жа́дность</b> sự tham lam · <b>жа́дина</b> đồ keo kiệt · <b>жа́дничать</b> keo kiệt, bo bo giữ · <b>жа́жда</b> cơn khát</div>'
)

# --------------------------------------------------------------------- воспитанный
S["воспитанный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вос-</span>'
    '<span class="hd-gloss">LÊN (dạng của <b>воз-</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-пит-</span>'
    '<span class="hd-gloss">NUÔI — gốc của <b>пита́ние</b> dinh dưỡng</span></div>'
    '<div class="hd-row"><span class="hd-piece">-а-нн-ый</span>'
    '<span class="hd-gloss">đuôi phân từ «đã được…»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">«Đã được NUÔI DẠY cho lớn lên» tử tế ⇒ lễ phép, có giáo dục. Là phân từ của <b>воспита́ть</b>, trọng âm lùi về <b>пи́</b>. Trái nghĩa: <b>невоспи́танный</b> vô lễ.</div>'
    '<div class="hd-warn">Dạng ngắn: khen nết thì giữ HAI <b>н</b> — <b>она́ воспи́танна</b>. Bản một <b>н</b> trong bảng là phân từ «được ai nuôi dạy»: <b>она́ воспи́тана ба́бушкой</b>. Giống đực chung một dạng <b>воспи́тан</b>.</div>'
    '<div class="hd-warn"><b>ве́жливый</b> là lịch sự trong cách nói năng; <b>воспи́танный</b> là NẾT được dạy từ nhà.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>воспита́ть</b> nuôi dạy · <b>воспита́ние</b> sự nuôi dạy · <b>воспита́тель</b> cô giáo mầm non · <b>пита́ние</b> dinh dưỡng</div>'
)

# --------------------------------------------------------------------- рассеянный
S["рассеянный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">рас-</span>'
    '<span class="hd-gloss">TẢN ra khắp nơi</span></div>'
    '<div class="hd-row"><span class="hd-piece">-сея-</span>'
    '<span class="hd-gloss">GIEO — <b>се́ять</b> gieo hạt</span></div>'
    '<div class="hd-row"><span class="hd-piece">-нн-ый</span>'
    '<span class="hd-gloss">đuôi phân từ «đã bị…»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Phân từ của <b>рассе́ять</b> gieo tản ra. Ánh sáng bị tản ⇒ khuếch tán: <b>рассе́янный свет</b>. Đầu óc bị tản ⇒ lơ đãng, đãng trí — đúng hình ảnh của <i>scatterbrained</i>.</div>'
    '<div class="hd-warn">Dạng ngắn: nói người lơ đãng thì giữ HAI <b>н</b> — <b>она́ рассе́янна</b>. Bản một <b>н</b> trong bảng (<b>рассе́яна</b>) là phân từ «đã bị tản ra». Giống đực chung một dạng <b>рассе́ян</b>.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>рассе́янность</b> tính lơ đãng · <b>рассе́ять</b> làm tản ra · <b>се́ять</b> gieo · <b>се́мя</b> hạt giống</div>'
)

# --------------------------------------------------------------------- властный
S["властный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">власт-</span>'
    '<span class="hd-gloss"><b>власть</b> quyền lực</span></div>'
    '<div class="hd-row"><span class="hd-piece">-н-ый</span>'
    '<span class="hd-gloss">đuôi tính từ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Đầy <b>власть</b> trong giọng, trong mắt ⇒ đầy uy quyền, hống hách, hay ra lệnh: <b>вла́стный го́лос</b>. Nghĩa giấy tờ: thuộc chính quyền — <b>вла́стные структу́ры</b> các cơ quan quyền lực.</div>'
    '<div class="hd-warn">Dạng ngắn giống đực chen <b>е</b>: <b>вла́стен</b>, còn lại trọng âm đứng yên (<b>вла́стна</b>). Cụm hay gặp: <b>не вла́стен над</b> + cách 5 = không làm chủ được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>власть</b> quyền lực · <b>вла́стность</b> tính hống hách · <b>владе́ть</b> làm chủ, sở hữu · <b>о́бласть</b> tỉnh, vùng</div>'
)

# --------------------------------------------------------------------- обаятельный
S["обаятельный"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">о-</span>'
    '<span class="hd-gloss">QUANH, bủa vây</span></div>'
    '<div class="hd-row"><span class="hd-piece">-бая-</span>'
    '<span class="hd-gloss">NÓI (động từ cổ <b>ба́ять</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-тельн-ый</span>'
    '<span class="hd-gloss">«có khả năng làm thế»</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nói bủa quanh tới mức người ta bị BỎ BÙA ⇒ có sức hút, quyến rũ, dễ mến. <i>Charm</i> tiếng Anh cùng hình ảnh: gốc La-tinh <i>carmen</i> là bài hát, câu thần chú.</div>'
    '<div class="hd-warn">⚠️ Mức tin: chẻ <b>о-</b> + <b>ба́ять</b> là từ nguyên, không phải luật suy ra được.</div>'
    '<div class="hd-warn">Dạng ngắn: cả lớp <b>-тельный</b> chen <b>е</b> ở giống đực — <b>обая́телен</b>, <b>обая́тельна</b>. Khác <b>краси́вый</b>: khen SỨC HÚT của cả con người, không khen nét mặt.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>обая́ние</b> sức quyến rũ · <b>обая́тельно</b> một cách duyên dáng · <b>ба́сня</b> truyện ngụ ngôn</div>'
)

# --------------------------------------------------------------------- полюбоваться
S["полюбоваться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">по-</span>'
    '<span class="hd-gloss">MỘT LÚC cho thoả mắt</span></div>'
    '<div class="hd-row"><span class="hd-piece">люб-</span>'
    '<span class="hd-gloss">YÊU, thấy hợp ý — <b>люби́ть</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-ова́-ть-ся</span>'
    '<span class="hd-gloss">đuôi lớp 1 (<b>-ова- → -у-</b>), phản thân</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Nhìn mà thấy YÊU, và nhìn MỘT LÚC cho thoả ⇒ ngắm, chiêm ngưỡng. Vế HT của <b>любова́ться</b>: <b>полюбу́юсь</b>, <b>полюбу́ешься</b>.</div>'
    '<div class="hd-warn">Ngắm CÁI GÌ → cách 5 trơ, không giới từ: <b>полюбова́ться зака́том</b> ngắm hoàng hôn.</div>'
    '<div class="hd-warn">Mệnh lệnh <b>Полюбу́йся!</b> hay mang giọng mỉa: <b>Полюбу́йся на него́!</b> = Nhìn hắn mà xem! (lúc này là <b>на</b> + cách 4).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>любова́ться</b> ngắm (CHT) · <b>люби́ть</b> yêu, thích · <b>любо́вь</b> tình yêu · <b>люби́мый</b> yêu thích</div>'
)

# --------------------------------------------------------------------- восхититься
S["восхититься"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вос-</span>'
    '<span class="hd-gloss">LÊN (dạng của <b>воз-</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-хит-</span>'
    '<span class="hd-gloss">CHỘP, giật lấy — như <b>похи́тить</b> bắt cóc</span></div>'
    '<div class="hd-row"><span class="hd-piece">-и́-ть-ся</span>'
    '<span class="hd-gloss">đuôi lớp 2, phản thân, thể hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Hồn bị CHỘP bốc LÊN ⇒ trầm trồ, ngưỡng mộ (bật ra một lần). <i>Rapture</i> tiếng Anh cùng hình ảnh (La-tinh <i>rapere</i> chộp lấy). Ngôi «tôi» <b>т → щ</b>: <b>восхищу́сь</b>, còn lại <b>восхити́шься</b>… Cặp CHT: <b>восхища́ться</b>.</div>'
    '<div class="hd-warn">Ngưỡng mộ AI, CÁI GÌ → cách 5 trơ: <b>восхити́ться её го́лосом</b>.</div>'
    '<div class="hd-warn">⚠️ Mức tin: gốc <b>хит-</b> CHỘP là từ nguyên, không phải luật suy ra được.</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>восхища́ться</b> ngưỡng mộ (CHT) · <b>восхище́ние</b> sự ngưỡng mộ · <b>восхити́тельный</b> tuyệt vời · <b>похи́тить</b> bắt cóc</div>'
)

# --------------------------------------------------------------------- восхищаться
S["восхищаться"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">вос-</span>'
    '<span class="hd-gloss">LÊN (dạng của <b>воз-</b>)</span></div>'
    '<div class="hd-row"><span class="hd-piece">-хищ-</span>'
    '<span class="hd-gloss">CHỘP, giật lấy — <b>хит-</b> đổi <b>т → щ</b></span></div>'
    '<div class="hd-row"><span class="hd-piece">-а́-ть-ся</span>'
    '<span class="hd-gloss">đuôi lớp 1, phản thân, thể chưa hoàn thành</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">Vế CHT của <b>восхити́ться</b>: ngưỡng mộ lâu dài. Chữ <b>щ</b> mà vế HT chỉ có ở ngôi «tôi» thì ở đây có mặt mọi ngôi, chia đều: <b>восхища́юсь</b>, <b>восхища́ешься</b>.</div>'
    '<div class="hd-warn">Cách 5 trơ, không giới từ, y như <b>любова́ться</b>: <b>Я восхища́юсь тобо́й.</b> Nhưng <b>любова́ться</b> là NGẮM bằng mắt, còn <b>восхища́ться</b> phục cả thứ không nhìn thấy (tài, lòng dũng cảm).</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>восхити́ться</b> trầm trồ khen (HT) · <b>восхище́ние</b> sự ngưỡng mộ · <b>восхищённый</b> đầy ngưỡng mộ · <b>хи́щник</b> thú săn mồi</div>'
)

B = {
    "docbangmat": 127,
    "loitubat": 3,   # обаятельный: đưa баю́кать vào Họ hàng (chưa chắc cùng gốc) -> bỏ
                     # запланировать: gán за- nghĩa «CHỐT vào lịch» (bịa) -> «chỉ báo thể, không nghĩa riêng»
                     # рассеянный: câu «không phải trí nhớ kém» tự mâu thuẫn với đãng trí -> bỏ
    "nguonsai": 2,   # воспитанный, рассеянный: bảng máy chỉ in dạng ngắn của PHÂN TỪ (воспи́тана, рассе́яна);
                     # tính từ giữ -нн- (воспи́танна, рассе́янна — ru.wiktionary xác nhận) -> dạy cả hai, không chép
    "baolen": [
        "Va chạm сопоставить/сопоставлять ⊃ сравнить/сравнивать [k136]: RÚT «so sánh», giữ «đối chiếu» + «đặt cạnh nhau để xét» (gloss juxtapose). Hết bọc trọn.",
        "V cần duyệt (13 thẻ đổi thật): проанализировать (BỎ mổ xẻ) · продумать (BỎ «cân nhắc xong», «tính kỹ»; cùng dãy продумывать) · перепутать (THÊM làm rối, cùng dãy путать) · сопоставить, сопоставлять · героический (BỎ dũng cảm) · жадный (THÊM keo kiệt, thèm khát, khớp жадность k208) · воспитанный (BỎ ngoan ngoãn, THÊM được dạy dỗ tử tế) · рассеянный (BỎ hay quên, THÊM đãng trí, tản mát, khuếch tán) · властный (uy quyền -> đầy uy quyền, THÊM thuộc chính quyền) · полюбоваться (đổi thứ tự theo любоваться) · восхититься, восхищаться (cùng dãy; BỎ say mê). продумывать, путать khai nhưng không đổi.",
        "воспитанный cố ý KHÔNG thêm «lịch sự» (gloss polite): thêm là bọc trọn вежливый [k136] {lịch sự, lễ phép}, cùng badge adj.",
        "запланировать: KHÔNG viết V («lên kế hoạch, dự định, xếp lịch»); cặp планировать [k210] là «lập kế hoạch, dự định, quy hoạch, thiết kế» — hai nghĩa sau không thuộc запланировать. Muốn nhất quán chữ thì đổi «lên» thành «lập» kèm 2 câu ví dụ.",
        "Trùng hết nghĩa: проанализировать–анализировать [k145], полюбоваться–любоваться [k229] và 4 cặp thể trong lô — badge thể tách.",
        "Dịch lệch V — сопоставлять câu 1 (so sánh) -> «Учёные сопоставляют результаты двух опытов. / Scientists <b>are comparing</b> the results of two experiments. / Các nhà khoa học đang <b>đối chiếu</b> kết quả hai thí nghiệm.»",
        "Câu gượng + lệch V — сопоставлять câu 3 (Не сопоставляй меня с братом: người Nga nói сравнивай) -> «Следователь сопоставляет показания свидетелей. / The investigator <b>is comparing</b> the witnesses' statements. / Điều tra viên đang <b>đối chiếu</b> lời khai của các nhân chứng.»",
        "Dịch lệch V — продумать câu 1 («tính kỹ»), giữ câu Nga/Anh -> «Mai mình ngồi lại <b>tính toán kỹ</b> mọi thứ cho yên tâm.»",
        "Dịch lệch nghĩa — жадный câu 1 (không chia kẹo = keo, không phải tham), giữ câu Nga -> «My brother is <b>stingy</b>, he never shares his sweets. / Anh tôi <b>keo kiệt</b>, chẳng bao giờ chia kẹo cho ai.»",
        "Dịch lệch nghĩa — запланировать câu 3 (schedule), giữ câu Nga/Anh -> «Hãy <b>xếp lịch</b> cuộc gặp vào buổi sáng nhé.»",
        "Câu gượng — восхититься câu 1 (я обязательно восхищусь) -> «Ты восхитишься, когда увидишь этот дворец. / You'll <b>be amazed</b> when you see this palace. / Bạn sẽ <b>trầm trồ khen</b> khi thấy cung điện này.»",
        "Câu gượng — обаятельный câu 1 (такой обаятельный, все смеются: hai vế rời nhau) -> «Твой новый коллега такой обаятельный, он всем понравился. / Your new colleague is so <b>charming</b>, everyone liked him. / Đồng nghiệp mới của bạn <b>dễ mến</b> thật, ai cũng quý.»",
        "Câu gượng — перепутать câu 2 (соль с сахаром в кофе) -> «Я перепутал соль с сахаром и испортил кофе. / I <b>mixed up</b> salt and sugar and ruined the coffee. / Tôi <b>nhầm</b> muối với đường nên hỏng cả cốc cà phê.»",
        "Câu gượng — воспитанный câu 3 -> «Воспитанный человек так не поступает. / A <b>well brought up</b> person doesn't act like that. / Người <b>có giáo dục</b> không làm thế.»",
        "Nghĩa có trong V mà chưa câu ví dụ nào dùng: рассеянный (tản mát, khuếch tán) · властный (thuộc chính quyền) · жадный (thèm khát) · путать, перепутать (làm rối) · восхититься, восхищаться (thích thú).",
        "Đã tự kiểm: путать < пу́то dây buộc chân (ru.wiktionary, *pǫtati) — KHÔNG dính путь; thẻ có ô đỏ nói rõ.",
        "Bảng chia trên thẻ воспитанный và рассеянный in dạng ngắn phân từ (một н); thẻ đã có ô đỏ giải thích, muốn sạch hẳn thì sửa GrammarJSON + BangMay thành -нна / -нно / -нны.",
        "Mức tin ghi ô đỏ: обаятельный (о- + ба́ять, Фасмер), восхититься (хит- CHỘP).",
    ],
}
