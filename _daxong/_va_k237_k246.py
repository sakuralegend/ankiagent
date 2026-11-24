# -*- coding: utf-8 -*-
"""Vá sau đợt k237–k246 (24/11/2026). L2: chạy một lần.

Câu ví dụ gượng / thiếu nghĩa / dịch lệch đề mới; bảng chia sai từ OpenRussian (вытереть ghi
hai thể, финмнсируем, функционировать trống ngôi, консервы/мемуары chia số ít, воспитанный/
рассеянный dạng ngắn một н); аллея dịch «alley» là bạn giả; вкус/вкусный nối nhầm gốc кусать."""
import copy
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
ROOT = ROOT if os.path.exists(os.path.join(ROOT, "bot.py")) else os.path.dirname(ROOT)
sys.path.insert(0, ROOT)
from anki_tools import grammar                                            # noqa: E402
from anki_tools.anki_client import (doc_notes_cua_model, gan_tieng_vi_du, sync_now,   # noqa: E402
                                    sync_truoc_khi_ghi_lo, update_note_fields)
from anki_tools.backup import run_backup                                  # noqa: E402
from anki_tools.config import MODEL_NAME                                  # noqa: E402
from anki_tools.html_builder import dung_cloze, thay_vi_du                # noqa: E402

_ = None   # giữ nguyên dòng đó
CAU = {  # (từ, câu số): (ru, en, vi)
    ("походка", 3): ("В их <hl>походке</hl> сразу видна военная выправка.", "You can immediately see military bearing in their <hl>gait</hl>.", "Trong <hl>dáng đi</hl> của họ thấy ngay phong thái quân nhân."),
    ("зрительный", 1): ("<hl>Зрительный</hl> контакт очень важен на собеседовании.", "<hl>Eye</hl> contact is very important at an interview.", "Tiếp xúc <hl>bằng mắt</hl> rất quan trọng khi phỏng vấn."),
    ("зрительный", 3): ("С хорошей <hl>зрительной</hl> памятью учить слова легко.", "With a good <hl>visual</hl> memory it's easy to learn words.", "Có trí nhớ <hl>thị giác</hl> tốt thì học từ rất dễ."),
    ("ботаник", 2): ("Мой дед был <hl>ботаником</hl> и изучал редкие цветы.", "My grandfather was a <hl>botanist</hl> and studied rare flowers.", "Ông tớ là <hl>nhà thực vật học</hl>, chuyên nghiên cứu hoa quý hiếm."),
    ("латинский", 2): ("Напиши своё имя <hl>латинскими</hl> буквами.", "Write your name in <hl>Latin</hl> letters.", "Viết tên cậu bằng chữ cái <hl>La Tinh</hl> đi."),
    ("соотечественник", 1): (_, _, "Trên tàu có một <hl>người cùng nước</hl> ngồi cạnh, bọn tớ nói chuyện cả đêm."),
    ("вата", 3): ("В такой <hl>вате</hl> иногда бывает синтетика.", "<hl>Cotton wool</hl> like that sometimes has synthetic stuff in it.", "Trong loại <hl>bông gòn</hl> đó đôi khi có sợi tổng hợp."),
    ("йод", 3): ("Мама обработала порез <hl>йодом</hl>.", "Mom treated the cut with <hl>iodine</hl>.", "Mẹ sát trùng vết đứt bằng <hl>i-ốt</hl>."),
    ("склероз", 3): ("Рассеянный <hl>склероз</hl> лечат годами.", "Multiple <hl>sclerosis</hl> is treated for years.", "<hl>Bệnh xơ cứng</hl> rải rác phải chữa hàng năm trời."),
    ("бессонница", 3): ("После такой <hl>бессонницы</hl> голова совсем не работает.", "After <hl>insomnia</hl> like that my head just doesn't work.", "Sau đợt <hl>mất ngủ</hl> như vậy đầu óc chẳng làm việc nổi."),
    ("жемчуг", 3): ("Такого <hl>жемчуга</hl> я раньше не видел.", _, _),
    ("заражаться", 1): (_, _, "Mùa đông nào bọn tôi cũng <hl>bị lây</hl> bệnh của nhau."),
    ("репертуар", 2): (_, _, "<hl>Danh mục tiết mục</hl> của ca sĩ này chỉ toàn ballad."),
    ("брошь", 1): (_, _, "Bà tặng tôi một chiếc <hl>trâm cài áo</hl> cổ."),
    ("брошь", 2): (_, _, "Cô ấy ghim khăn lại bằng chiếc <hl>ghim cài áo</hl>."),
    ("брошь", 3): (_, _, "Trên mấy chiếc <hl>trâm cài áo</hl> này là bạc thật."),
    ("бас", 2): (_, _, "Anh ấy lúc nào cũng nói bằng <hl>giọng nam trầm</hl> rất dày."),
    ("бас", 3): (_, _, "Trong <hl>giọng nam trầm</hl> của anh ấy có gì đó thân thương."),
    ("индекс", 1): (_, "Write the <hl>postcode</hl> on the envelope, otherwise the letter won't arrive.", _),
    ("индекс", 2): (_, "With this <hl>postcode</hl> I quickly found your street.", _),
    ("индекс", 3): (_, _, _),
    ("предшествовать", 1): ("Выборам <hl>предшествовали</hl> долгие переговоры.", "Long negotiations <hl>preceded</hl> the election.", "Những cuộc đàm phán dài <hl>có trước</hl> cuộc bầu cử."),
    ("предшествовать", 2): ("Грозе <hl>предшествовал</hl> сильный ветер.", "A strong wind <hl>preceded</hl> the thunderstorm.", "Gió mạnh <hl>đi trước</hl> cơn dông."),
    ("продолжительность", 3): ("<hl>Продолжительность</hl> урока — сорок пять минут.", "The <hl>duration</hl> of a lesson is forty-five minutes.", "<hl>Thời lượng</hl> một tiết học là bốn mươi lăm phút."),
    ("одерживать", 3): ("Они редко <hl>одерживают</hl> победу в гостях.", "They rarely <hl>win</hl> a victory away from home.", "Họ hiếm khi <hl>giành được</hl> chiến thắng trên sân khách."),
    ("препятствовать", 3): ("Ничто не <hl>препятствует</hl> нашему сотрудничеству.", "Nothing <hl>stands in the way of</hl> our cooperation.", "Không gì <hl>cản trở</hl> sự hợp tác của chúng ta."),
    ("интервал", 3): ("Поезда идут с <hl>интервалом</hl> в пять минут.", "Trains run at an <hl>interval</hl> of five minutes.", "Tàu chạy với <hl>khoảng cách</hl> năm phút một chuyến."),
    ("доделывать", 2): ("Мы весь вечер <hl>доделывали</hl> ремонт на кухне.", "We <hl>were finishing</hl> the kitchen renovation all evening.", "Cả tối chúng tôi <hl>làm nốt</hl> việc sửa bếp."),
    ("наименее", 2): ("Это <hl>наименее</hl> опасный путь через горы.", "It's the <hl>least</hl> dangerous way through the mountains.", "Đây là con đường <hl>ít</hl> nguy hiểm <hl>nhất</hl> qua núi."),
    ("расходиться", 1): (_, _, "Quan điểm của tớ với bố lúc nào cũng <hl>khác nhau</hl>."),
    ("расходиться", 3): (_, "The guests didn't want <hl>to part</hl> until morning.", "Khách khứa không muốn <hl>chia tay nhau</hl> cho đến sáng."),
    ("греться", 3): (_, _, "Con mèo thích nằm <hl>sưởi ấm</hl> trên bệ cửa sổ."),
    ("возвратиться", 1): ("Мы <hl>возвратимся</hl> к этому вопросу позже.", "We'll <hl>return</hl> to this question later.", "Bọn mình sẽ <hl>trở lại</hl> vấn đề này sau."),
    ("возвратиться", 3): ("Из командировки он <hl>возвратился</hl> только в пятницу.", "He only <hl>got back</hl> from the business trip on Friday.", "Mãi thứ Sáu anh ấy mới <hl>trở về</hl> từ chuyến công tác."),
    ("повторный", 1): (_, _, "Họ hẹn tớ một buổi khám <hl>lần hai</hl> với bác sĩ."),
    ("повторный", 2): (_, _, "Nỗ lực <hl>lần hai</hl> cũng thất bại."),
    ("повторный", 3): ("<hl>Повторный</hl> анализ ничего не показал.", "The <hl>repeat</hl> test showed nothing.", "Xét nghiệm <hl>lần hai</hl> không cho thấy gì."),
    ("фирменный", 2): (_, _, "Anh giao hàng mang cái túi <hl>của hãng</hl> có logo."),
    ("вертикальный", 1): ("Проведи <hl>вертикальную</hl> линию посередине листа.", "Draw a <hl>vertical</hl> line down the middle of the sheet.", "Kẻ một đường <hl>thẳng đứng</hl> ở giữa tờ giấy."),
    ("радикальный", 2): ("Врачи предложили <hl>радикальный</hl> метод лечения.", "The doctors suggested a <hl>radical</hl> treatment method.", "Các bác sĩ đề nghị một phương pháp điều trị <hl>triệt để</hl>."),
    ("потребительский", 3): ("Она изучает <hl>потребительское</hl> поведение молодёжи.", "She studies the <hl>consumer</hl> behaviour of young people.", "Cô ấy nghiên cứu hành vi <hl>tiêu dùng</hl> của giới trẻ."),
    ("минеральный", 3): ("Мне <hl>минеральную</hl> воду без газа, пожалуйста.", "<hl>Mineral</hl> water, still, please.", "Cho tôi nước <hl>khoáng</hl> không ga."),
    ("новинка", 1): (_, _, "<hl>Hàng mới ra</hl> này đã có ở các cửa hàng rồi."),
    ("новинка", 3): ("Магазин показал все <hl>новинки</hl> сезона.", "The store showed all the season's <hl>new products</hl>.", "Cửa hàng trưng ra mọi <hl>sản phẩm mới</hl> của mùa này."),
    ("соловей", 1): (_, _, "Suốt đêm có con <hl>chim hoạ mi</hl> hót dưới cửa sổ."),
    ("соловей", 2): (_, _, "Tôi chưa bao giờ nghe <hl>chim hoạ mi</hl> hót trực tiếp."),
    ("соловей", 3): (_, _, "Mùa xuân ở đây <hl>chim hoạ mi</hl> hót tới sáng."),
    ("цвести", 1): ("В нашем саду уже <hl>цветут</hl> вишни.", "The cherry trees are already <hl>blooming</hl> in our garden.", "Trong vườn nhà tôi anh đào đã <hl>nở hoa</hl>."),
    ("баран", 3): ("Вот <hl>баран</hl>, опять забыл ключи!", "What an <hl>idiot</hl>, he forgot his keys again!", "Đúng là <hl>kẻ ngốc</hl>, lại quên chìa khoá!"),
    ("град", 2): ("<hl>Град</hl> побил все яблони в саду.", "The <hl>hail</hl> damaged all the apple trees in the garden.", "<hl>Mưa đá</hl> làm dập nát hết mấy cây táo trong vườn."),
    ("мёрзнуть", 2): (_, _, "Hôm qua ở trận bóng chúng tôi <hl>bị lạnh</hl> kinh khủng."),
    ("кое-как", 2): (_, _, "Cô ấy <hl>chật vật lắm mới</hl> mặc được cái jean cũ."),
    ("аллея", 1): (_, "A long linden <hl>avenue</hl> starts behind the house.", _),
    ("аллея", 2): (_, "We strolled along the <hl>avenue</hl> for almost an hour.", _),
    ("аллея", 3): (_, "This park has so many <hl>tree-lined paths</hl> that you can get lost.", _),
    ("въезжать", 3): ("Мы <hl>въезжаем</hl> в новую квартиру в субботу.", "We're <hl>moving into</hl> the new flat on Saturday.", "Thứ Bảy chúng tôi <hl>dọn vào ở</hl> căn hộ mới."),
    ("въехать", 1): ("Он задумался и <hl>въехал</hl> в столб.", "He got lost in thought and <hl>crashed into</hl> a pole.", "Anh ấy mải nghĩ nên <hl>đâm vào</hl> cột."),
    ("ориентироваться", 2): ("Она отлично <hl>ориентируется</hl> в законах.", "She <hl>is well versed</hl> in the law.", "Cô ấy rất <hl>am hiểu</hl> luật."),
    ("капитализм", 3): ("Профессор полтора часа говорил об истории <hl>капитализма</hl>.", "The professor talked about the history of <hl>capitalism</hl> for an hour and a half.", "Giáo sư nói về lịch sử <hl>chủ nghĩa tư bản</hl> suốt tiếng rưỡi."),
    ("расцвет", 1): (_, _, "Thành phố tôi giờ đang có <hl>sự nở rộ</hl> thật sự của đồ ăn đường phố."),
    ("расцвет", 2): (_, _, "Bà bảo tôi đang ở đúng <hl>thời kỳ đỉnh cao</hl> của sức lực."),
    ("расцвет", 3): ("При этом царе начался <hl>расцвет</hl> русской культуры.", "Under this tsar the <hl>flourishing</hl> of Russian culture began.", "Dưới thời sa hoàng này, <hl>thời kỳ hưng thịnh</hl> của văn hoá Nga bắt đầu."),
    ("пошлина", 1): (_, _, "<hl>Thuế nhập khẩu</hl> cho cái kiện này còn đắt hơn cả món đồ."),
    ("пошлина", 2): ("После введения новой <hl>пошлины</hl> телефоны сразу подорожали.", "After the new <hl>duty</hl> was introduced, phones immediately got more expensive.", "Sau khi áp <hl>thuế nhập khẩu</hl> mới, điện thoại đắt lên ngay."),
    ("примитивный", 2): ("У него очень <hl>примитивный</hl> телефон, без интернета.", "He has a very <hl>primitive</hl> phone, with no internet.", "Anh ấy dùng cái điện thoại rất <hl>thô sơ</hl>, không có mạng."),
    ("адекватный", 1): (_, _, "Ông láng giềng mới trông <hl>bình thường</hl>, không ồn ào gì."),
    ("вульгарный", 3): (_, _, "Tôi không thấy màu này <hl>kém thẩm mỹ</hl> gì cả, tôi thích mà."),
    ("дефект", 2): (_, _, "Trong phần mô tả không có chữ nào về <hl>lỗi</hl>, họ lừa mình."),
    ("протестовать", 3): (_, "Don't <hl>protest</hl>, just sign these papers.", _),
    ("погасить", 3): ("Он наконец <hl>погасил</hl> кредит за машину.", "He finally <hl>paid off</hl> the car loan.", "Cuối cùng anh ấy đã <hl>trả hết nợ</hl> vay mua xe."),
    ("гасить", 2): ("Мы <hl>гасим</hl> кредит маленькими суммами.", "We are <hl>paying off</hl> the loan in small amounts.", "Bọn tôi <hl>trả hết nợ</hl> vay bằng từng khoản nhỏ."),
    ("тушить", 2): ("Бабушка <hl>тушит</hl> капусту с мясом.", "Grandma <hl>is stewing</hl> cabbage with meat.", "Bà đang <hl>hầm</hl> bắp cải với thịt."),
    ("потушить", 1): ("<hl>Потушим</hl> овощи с курицей на ужин?", "Shall we <hl>stew</hl> some vegetables with chicken for dinner?", "Tối nay mình <hl>hầm</hl> rau với gà nhé?"),
    ("поделить", 3): ("<hl>Подели</hl> конфеты поровну, не жадничай.", "<hl>Divide</hl> the candy equally, don't be greedy.", "<hl>Chia</hl> kẹo cho đều đi, đừng tham."),
    ("кусать", 3): ("Летом на даче нас всё время <hl>кусают</hl> комары.", "In summer at the dacha mosquitoes <hl>bite</hl> us all the time.", "Mùa hè ở nhà vườn bọn tôi bị muỗi <hl>đốt</hl> suốt."),
    ("ползать", 2): ("Я весь вечер <hl>ползала</hl> под столом, искала провод.", _, _),
    ("переключать", 2): ("Мы <hl>переключали</hl> песни каждые две минуты.", "We <hl>kept switching</hl> the songs every two minutes.", "Bọn tôi cứ hai phút lại <hl>chuyển</hl> bài một lần."),
    ("ограничиваться", 1): (_, _, "Thứ Sáu bọn tôi thường <hl>chỉ dừng ở</hl> vài chai bia."),
    ("ограничиваться", 2): (_, _, "Trước đây bọn tôi <hl>chỉ dừng ở</hl> những tin nhắn ngắn."),
    ("ограничиваться", 3): ("Не <hl>ограничивайся</hl> учебником, смотри ещё и видео.", _, "Đừng <hl>bó hẹp</hl> trong sách giáo trình, xem thêm video nữa."),
    ("ограничиться", 2): (_, _, "Chúng tôi <hl>chỉ dừng ở</hl> cà phê, chẳng muốn ăn gì cả."),
    ("обмениваться", 3): (_, _, "Đừng <hl>trao đổi</hl> mật khẩu với bất cứ ai."),
    ("сопоставлять", 1): ("Учёные <hl>сопоставляют</hl> результаты двух опытов.", "Scientists <hl>are comparing</hl> the results of two experiments.", "Các nhà khoa học đang <hl>đối chiếu</hl> kết quả hai thí nghiệm."),
    ("сопоставлять", 3): ("Следователь <hl>сопоставляет</hl> показания свидетелей.", "The investigator <hl>is comparing</hl> the witnesses' statements.", "Điều tra viên đang <hl>đối chiếu</hl> lời khai của các nhân chứng."),
    ("продумать", 1): (_, _, "Mai mình ngồi lại <hl>tính toán kỹ</hl> mọi thứ cho yên tâm."),
    ("жадный", 1): (_, "My brother is <hl>stingy</hl>, he never shares his sweets.", "Anh tôi <hl>keo kiệt</hl>, chẳng bao giờ chia kẹo cho ai."),
    ("запланировать", 3): (_, _, "Hãy <hl>xếp lịch</hl> cuộc gặp vào buổi sáng nhé."),
    ("восхититься", 1): ("Ты <hl>восхитишься</hl>, когда увидишь этот дворец.", "You'll <hl>be amazed</hl> when you see this palace.", "Bạn sẽ <hl>trầm trồ khen</hl> khi thấy cung điện này."),
    ("обаятельный", 1): ("Твой новый коллега такой <hl>обаятельный</hl>, он всем понравился.", "Your new colleague is so <hl>charming</hl>, everyone liked him.", "Đồng nghiệp mới của bạn <hl>dễ mến</hl> thật, ai cũng quý."),
    ("перепутать", 2): ("Я <hl>перепутал</hl> соль с сахаром и испортил кофе.", "I <hl>mixed up</hl> salt and sugar and ruined the coffee.", "Tôi <hl>nhầm</hl> muối với đường nên hỏng cả cốc cà phê."),
    ("воспитанный", 3): ("<hl>Воспитанный</hl> человек так не поступает.", "A <hl>well brought up</hl> person doesn't act like that.", "Người <hl>có giáo dục</hl> không làm thế."),
    ("мемуары", 1): ("Дед пишет <hl>мемуары</hl> о своей молодости.", "Grandpa is writing his <hl>memoirs</hl> about his youth.", "Ông mình đang viết <hl>hồi ký</hl> về thời trẻ."),
    ("мемуары", 2): ("Я прочитала половину <hl>мемуаров</hl> за один вечер.", "I read half of the <hl>memoirs</hl> in one evening.", "Mình đọc hết nửa cuốn <hl>hồi ký</hl> trong một buổi tối."),
    ("подслушать", 2): (_, _, "Mình <hl>tình cờ nghe được</hl> họ nói chuyện trong bếp."),
    ("грубить", 3): (_, _, "Đừng <hl>nói thô lỗ</hl> với em gái nữa, nó mới sáu tuổi."),
    ("намекать", 1): ("Мы третий день <hl>намекаем</hl> ему на уборку.", _, _),
    ("консервы", 1): ("Остались одни <hl>консервы</hl>, больше ничего нет.", "There's only <hl>canned food</hl> left, nothing else.", "Chỉ còn mỗi <hl>đồ hộp</hl>, ngoài ra chẳng có gì."),
    ("консервы", 2): ("У меня не осталось ни одной банки <hl>консервов</hl>.", "I don't have a single can of <hl>canned food</hl> left.", "Tôi không còn lon <hl>đồ hộp</hl> nào cả."),
    ("фарфор", 2): ("Такого тонкого <hl>фарфора</hl> я раньше не видел.", "I've never seen such delicate <hl>porcelain</hl> before.", "Tôi chưa từng thấy <hl>đồ sứ</hl> nào mỏng như thế."),
    ("уксус", 3): ("Такого <hl>уксуса</hl> в обычном магазине не найдёшь.", "You won't find <hl>vinegar</hl> like this in an ordinary shop.", "Loại <hl>giấm</hl> như thế không tìm được ở tiệm thường."),
    ("бульон", 3): ("Терпеть не могу <hl>бульон</hl> из кубиков.", "I can't stand <hl>broth</hl> made from cubes.", _),
    ("морс", 1): (_, _, "Mẹ nấu <hl>nước quả</hl> từ nam việt quất."),
    ("свекровь", 2): (_, _, "<hl>Mẹ chồng</hl> tôi khéo tay thật đấy."),
    ("свекровь", 3): ("Про <hl>свекровь</hl> в нашем чате можно роман написать.", "You could write a novel about <hl>mothers-in-law</hl> from our chat.", "Chuyện <hl>mẹ chồng</hl> trong nhóm chat của tụi tôi đủ viết thành tiểu thuyết."),
    ("урна", 2): ("Она опустила бюллетень в <hl>урну</hl>.", "She dropped her ballot into the <hl>ballot box</hl>.", "Cô ấy bỏ lá phiếu vào <hl>hòm phiếu</hl>."),
    ("рулет", 2): ("На праздник мама сделала мясной <hl>рулет</hl>.", "Mum made a <hl>meat roll</hl> for the holiday.", "Ngày lễ mẹ làm món <hl>thịt cuộn</hl>."),
}
del CAU[("индекс", 3)]
VI = {
    "примитивный": ("nguyên thuỷ, sơ khai", "nguyên thuỷ, sơ khai, thô sơ"),
    "диктор": ("phát thanh viên, người đọc bản tin trên đài/TV", "phát thanh viên, người đọc bản tin"),
    "проанализировать": ("phân tích", "phân tích, mổ xẻ"),      # «phân tích» trơ nằm gọn trong разобрать
    "анализировать": ("phân tích", "phân tích, mổ xẻ"),
}
OL = '<ol class="meaning-list">%s</ol>'
MEANING = {
    "аллея": ("<li>alley</li>", "<li>tree-lined path</li><li>avenue</li>"),
    "индекс": ("<li>index</li>", "<li>index</li><li>postcode</li>"),
    "заразиться": ("<li>to contract</li><li>to infect</li><li>to spread</li><li>to catch</li>",
                   "<li>to contract</li><li>to catch</li>"),
}
HD = {  # từ: [(cũ, mới)] — sửa cả thẻ lẫn file lô
    "воспитанный": [("Bản một <b>н</b> trong bảng là phân từ", "Bản một <b>н</b> là phân từ")],
    "рассеянный": [("Bản một <b>н</b> trong bảng (<b>рассе́яна</b>) là", "Bản một <b>н</b> (<b>рассе́яна</b>) là")],
    "вкус": [("CẮN, NẾM — như <b>кусо́к</b> miếng", "NẾM — trùng mặt chữ <b>кусо́к</b> miếng nhưng khác gốc"),
             ("Cắn vào miệng thì biết VỊ", "Nếm vào miệng thì biết VỊ"),
             ("<b>кусо́к</b> miếng · <b>куса́ть</b> cắn · <b>безвку́сный</b>", "<b>безвку́сный</b>")],
    "вкусный": [("CẮN, NẾM", "NẾM"), ("đưa vào miệng mà cắn", "đưa vào miệng mà nếm"),
                ("Nhận ra gốc кус- là đọc được cả <b>кусо́к</b> lẫn <b>заку́ска</b>.",
                 "Mượn <b>куса́ть</b> cắn làm móc nhớ cũng được, nhưng gốc thì khác."),
                (" · <b>заку́ска</b> món khai vị · <b>кусо́к</b> miếng", "")],
}


def _v(d):
    return {"sg": {k: "" for k in ("nom", "gen", "dat", "acc", "inst", "prep")}, "pl": d}


def g_vyteret(g):
    assert g["aspect"] == "both"
    g.update(aspect="perfective", present=[""] * 6, future=list(g["presfut"]))
    for x in g["parts"]["gerundPast"]:
        x["f"] = {"вытерши": "вы́терши"}.get(x["f"], x["f"])


def g_fin(g):
    assert g["presfut"][3] == "финмнси́руем" == g["present"][3]
    g["presfut"][3] = g["present"][3] = "финанси́руем"


def g_func(g):
    assert not any(g["presfut"] + g["past"] + g["imper"])
    b = "функциони́р"
    g["presfut"] = g["present"] = [b + x for x in ("ую", "уешь", "ует", "уем", "уете", "уют")]
    g["past"] = [b + x for x in ("овал", "овала", "овало", "овали")]
    g["imper"] = [b + "уй", b + "уйте"]
    for x in g["parts"]["gerundPast"]:
        x["f"] = {"функционировавши": "функциони́ровавши"}.get(x["f"], x["f"])


def g_kons(g):
    assert g["decl"]["pl"]["gen"] == "консерв"
    g["decl"] = _v({k: "консе́рв" + e for k, e in zip(("nom", "gen", "dat", "acc", "inst", "prep"),
                                                     ("ы", "ов", "ам", "ы", "ами", "ах"))})


def g_mem(g):
    assert g["gender"] == "m" and g["decl"]["sg"]["nom"] == "мемуар"
    g["gender"], g["decl"] = None, _v(g["decl"]["pl"])


def g_nn(goc):
    def f(g):
        assert g["shorts"][1] == goc + "а"
        g["shorts"] = [goc] + [goc + x for x in ("на", "но", "ны")]
        g["adverb"] = goc + "но"
    return f


def g_kk(g):
    assert g["acc"] == "ко́е-ка́к"
    g["acc"] = "кое-ка́к"


GR = {"вытереть": g_vyteret, "финансировать": g_fin, "функционировать": g_func, "консервы": g_kons,
      "мемуары": g_mem, "воспитанный": g_nn("воспи́тан"), "рассеянный": g_nn("рассе́ян"), "кое-как": g_kk}
PL = '<div class="badge plural">PL 👥</div>'
O = {"вытереть": {"AspectBadge": grammar.aspect_badge_html("perfective", "вытереть")},
     "консервы": {"GenderBadge": PL}, "мемуары": {"GenderBadge": PL}, "кое-как": {"Word": "кое-ка́к"}}

kho = {n["noteId"]: {k: v["value"] for k, v in n["fields"].items()} for n in doc_notes_cua_model(MODEL_NAME)}
id_ = {}
for i, f in kho.items():
    id_.setdefault(f["WordClean"].strip(), []).append(i)


def mot(w):
    assert len(id_[w]) == 1, (w, id_[w])
    return id_[w][0]


ghi, gram = {}, {}
for w, o in O.items():
    ghi.setdefault(mot(w), {}).update(o)
for w, (cu, moi) in VI.items():
    assert kho[mot(w)]["Vietnamese"] == cu, (w, kho[mot(w)]["Vietnamese"])
    ghi.setdefault(mot(w), {})["Vietnamese"] = moi
for w, (cu, moi) in MEANING.items():
    assert kho[mot(w)]["Meaning"] == OL % cu, w
    ghi.setdefault(mot(w), {})["Meaning"] = OL % moi
for w, ds in HD.items():
    h = kho[mot(w)]["HuongDan"]
    for cu, moi in ds:
        assert h.count(cu) == 1, (w, cu, h.count(cu))
        h = h.replace(cu, moi)
    ghi.setdefault(mot(w), {})["HuongDan"] = h
for w, fn in GR.items():
    g = copy.deepcopy(json.loads(kho[mot(w)]["GrammarJSON"]))
    fn(g)
    gram[mot(w)] = g
_hl = re.compile(r'<span class="hl">(.*?)</span>')
_DAU = {"ru": r'<div class="ex-ru">(.*?)(?:<span class="nghe"|</div>)', "en": r'<div class="ex-en">(.*?)</div>',
        "vi": r'<span class="vi-text">(.*?)</span></div>'}
for (w, i), moi in CAU.items():
    nid = mot(w)
    h = ghi.get(nid, {}).get("ExamplesHTML", kho[nid]["ExamplesHTML"])
    khoi = re.findall(r"<details\b.*?</details>", h, re.S)
    assert len(khoi) == 3, w
    cu = {k: _hl.sub(r"<hl>\1</hl>", re.search(p, khoi[i - 1], re.S).group(1)) for k, p in _DAU.items()}
    ex = {k: m or cu[k] for k, m in zip(("ru", "en", "vi"), moi)}
    assert all("<hl>" in x for x in ex.values()), (w, i, ex)
    if moi[2]:
        v = ghi.get(nid, {}).get("Vietnamese", kho[nid]["Vietnamese"]).lower()
        b = " ".join(re.findall(r"<hl>(.*?)</hl>", moi[2])).lower()
        if b not in v:
            print("  ? ngoài đề:", w, i, "|", b, "|", v)
    ghi.setdefault(nid, {})["ExamplesHTML"] = thay_vi_du(h, i - 1, ex)
cz = {}
for nid in set(gram) | {n for n, o in ghi.items() if "ExamplesHTML" in o}:
    f = kho[nid]
    g = gram.get(nid) or json.loads(f["GrammarJSON"])
    cz[nid] = dung_cloze(ghi.get(nid, {}).get("ExamplesHTML", f["ExamplesHTML"]), g, f["WordClean"])
    if not cz[nid]:
        print("  ! cloze trống:", f["WordClean"], "| trước đây", bool(f["ClozeHTML"]))
print("KHAN: mọi bản cũ khớp —", len(set(ghi) | set(gram)), "thẻ,", len(CAU), "câu")
if "--apply" not in sys.argv:
    raise SystemExit
run_backup()
if not sync_truoc_khi_ghi_lo("vá k237-k246"):
    raise SystemExit("sync hỏng")
for nid, g in gram.items():
    grammar.remember(kho[nid]["WordClean"].strip(), g, note_id=nid)
for nid, o in ghi.items():
    f = kho[nid]
    if "ExamplesHTML" in o:
        h = gan_tieng_vi_du(o["ExamplesHTML"])
        assert h.count("<audio") == 3 == h.count('class="nghe"'), nid
        o["ExamplesHTML"] = h
        o["ClozeHTML"] = dung_cloze(h, gram.get(nid) or json.loads(f["GrammarJSON"]), f["WordClean"])
    assert update_note_fields(nid, o), nid
    print("ok", f["WordClean"], list(o))
print("sync:", sync_now())
