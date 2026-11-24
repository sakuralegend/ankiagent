# -*- coding: utf-8 -*-
"""Vá sau đợt k247–k256 (25/11/2026). L2: chạy một lần.

Câu ví dụ gượng / thiếu nghĩa / dịch lệch đề mới (agent soạn từng lô ghi); bảng chia sai từ
OpenRussian (рассыпаться «рассыпаются», сформироваться trống, прошлогодний/настольный dạng ngắn máy
sinh…); gloss Anh lạc; выбежать/выбегать theo bảng вы-/у- user duyệt 24/11; Кора́н viết hoa."""
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
    ('объехать', 2): (_, _, 'Anh ấy <hl>lái xe vòng qua</hl> cái hố và suýt quệt vào lề đường.'),
    ('объехать', 3): ('За неделю можно <hl>объехать</hl> все острова.', 'In a week you can <hl>travel around</hl> all the islands.', 'Trong một tuần có thể <hl>đi khắp</hl> các hòn đảo.'),
    ('пересесть', 1): (_, _, 'Anh ấy sẽ <hl>chuyển chỗ</hl> ra cạnh cửa sổ, bên đó trống.'),
    ('пересесть', 3): ('Здесь нам надо <hl>пересесть</hl> на другой поезд.', 'Here we need to <hl>change</hl> to another train.', 'Đến đây chúng ta phải <hl>đổi tàu</hl>.'),
    ('трогаться', 1): (_, _, 'Ở đèn giao thông tôi lúc nào cũng <hl>chuyển bánh</hl> giật quá.'),
    ('трогаться', 3): (_, _, 'Đừng <hl>chuyển bánh</hl> khi mọi người chưa ngồi hết.'),
    ('тронуться', 1): ('Поезд <hl>тронется</hl> только через полчаса.', 'The train <hl>will start moving</hl> only in half an hour.', _),
    ('тронуться', 3): (_, _, 'Xe buýt sắp <hl>khởi hành</hl> rồi, chỉ vài phút nữa thôi.'),
    ('куда-либо', 1): (_, _, 'Hôm nay tôi mệt quá, không <hl>đi bất cứ đâu</hl> nổi.'),
    ('куда-либо', 2): (_, _, 'Trước khi <hl>đi bất cứ đâu</hl>, hãy xem thời tiết đã.'),
    ('куда-либо', 3): (_, _, 'Buổi tối cô ấy hiếm khi ra ngoài <hl>đi bất cứ đâu</hl>.'),
    ('зачем-то', 1): (_, _, 'Anh ấy lại mua cái dù thứ ba, <hl>chẳng biết để làm gì</hl>.'),
    ('зачем-то', 2): (_, _, 'Tôi mang theo áo khoác mùa đông, <hl>chẳng biết để làm gì</hl>.'),
    ('зачем-то', 3): ('Мама <hl>зачем-то</hl> хранит старые чеки.', 'Mum keeps old receipts <hl>for some reason</hl>.', 'Mẹ cứ giữ mấy tờ hoá đơn cũ, <hl>chẳng biết để làm gì</hl>.'),
    ('вписывать', 2): ('Она весь вечер <hl>вписывала</hl> имена в приглашения.', 'She <hl>was writing</hl> names into the invitations all evening.', 'Suốt cả buổi tối cô ấy <hl>ghi</hl> tên <hl>vào</hl> thiệp mời.'),
    ('зарегистрироваться', 1): ('Мы <hl>зарегистрируемся</hl> на рейс онлайн.', 'We <hl>will check in</hl> for the flight online.', 'Bọn mình sẽ <hl>làm thủ tục check-in</hl> chuyến bay trên mạng.'),
    ('регистрироваться', 2): (_, 'I <hl>registered</hl> three times, but no email came.', _),
    ('расстегнуть', 3): (_, _, '<hl>Mở khóa</hl> sau lưng cho tớ với.'),
    ('досуг', 1): ('Как вы обычно проводите <hl>досуг</hl>?', 'How do you usually spend your <hl>free time</hl>?', 'Anh chị thường làm gì vào <hl>lúc rỗi</hl>?'),
    ('досуг', 3): ('В опросе спрашивали о <hl>досуге</hl> подростков.', "The survey asked about teenagers' <hl>leisure</hl>.", 'Bảng khảo sát hỏi về chuyện <hl>giải trí</hl> của tuổi teen.'),
    ('нырнуть', 1): (_, _, 'Anh ấy sẽ <hl>lặn</hl> xuống lấy cái kính của cậu ngay.'),
    ('нырнуть', 2): ('Кот <hl>нырнул</hl> под одеяло и затих.', 'The cat <hl>ducked</hl> under the blanket and went quiet.', 'Con mèo <hl>chui tọt vào</hl> trong chăn rồi im thin thít.'),
    ('нырнуть', 3): (_, _, '<hl>Lặn</hl> xuống xem dưới đáy có gì.'),
    ('нырять', 1): (_, _, 'Sáng nào bọn mình cũng <hl>nhảy ùm xuống nước</hl> từ cái cầu này.'),
    ('созревать', 1): ('Девочки обычно <hl>созревают</hl> раньше мальчиков.', 'Girls usually <hl>mature</hl> earlier than boys.', 'Con gái thường <hl>trưởng thành</hl> sớm hơn con trai.'),
    ('созреть', 1): ('У меня <hl>созрел</hl> план на выходные.', 'A plan for the weekend has <hl>ripened</hl> in my head.', 'Trong đầu tôi đã <hl>chín muồi</hl> một kế hoạch cho cuối tuần.'),
    ('созреть', 3): ('Эти груши <hl>созреют</hl> только в октябре.', 'These pears will only <hl>ripen</hl> in October.', 'Mấy quả lê này phải đến tháng mười mới <hl>chín</hl>.'),
    ('приморский', 1): ('Летом <hl>приморские</hl> города полны туристов.', 'In summer <hl>seaside</hl> towns are full of tourists.', 'Mùa hè các thành phố <hl>ven biển</hl> đầy khách du lịch.'),
    ('заграничный', 1): (_, _, 'Hộ chiếu đi <hl>nước ngoài</hl> của tôi hết hạn từ tháng ba.'),
    ('безграничный', 1): (_, _, 'Bà tôi có sự kiên nhẫn <hl>vô hạn</hl>.'),
    ('безграничный', 2): ('У неё <hl>безграничная</hl> фантазия, честное слово.', 'She has a <hl>boundless</hl> imagination, honestly.', 'Trí tưởng tượng của cô ấy <hl>không giới hạn</hl>, thật đấy.'),
    ('подстригать', 2): (_, _, 'Trước đây cô ấy <hl>tỉa</hl> lông cho con chó mỗi tháng.'),
    ('подстригать', 3): (_, _, 'Nhưng đừng <hl>cắt tóc</hl> ngắn quá nhé, xin đấy.'),
    ('похудеть', 1): (_, _, 'Đến hè tôi chắc chắn sẽ <hl>giảm</hl> được năm <hl>cân</hl>.'),
    ('худеть', 3): ('Врач советует <hl>худеть</hl> медленно, без строгих диет.', 'The doctor advises <hl>losing weight</hl> slowly, without strict diets.', 'Bác sĩ khuyên <hl>giảm cân</hl> từ từ, không ăn kiêng khắt khe.'),
    ('гибнуть', 3): ('На дорогах каждый день <hl>гибнут</hl> люди.', 'People <hl>get killed</hl> on the roads every day.', 'Ngày nào cũng có người <hl>thiệt mạng</hl> trên đường.'),
    ('приезжий', 1): (_, _, 'Cậu kia <hl>từ nơi khác đến</hl>, chẳng biết gì về thành phố cả.'),
    ('приезжий', 3): (_, _, 'Mùa hè ở đây toàn <hl>người từ nơi khác đến</hl>, dân bản địa gần như không có.'),
    ('африканский', 2): ('<hl>Африканские</hl> слоны крупнее индийских.', '<hl>African</hl> elephants are bigger than Indian ones.', 'Voi <hl>châu Phi</hl> to hơn voi Ấn Độ.'),
    ('африканский', 3): ('Она уже год занимается <hl>африканскими</hl> танцами.', "She's been doing <hl>African</hl> dance for a year now.", 'Cô ấy tập các điệu nhảy <hl>châu Phi</hl> cả năm nay rồi.'),
    ('коран', 1): ('Он каждое утро читает <hl>Коран</hl> дома.', _, _),
    ('коран', 2): ('По <hl>Корану</hl> это запрещено, он мне объяснил.', _, _),
    ('коран', 3): ('На полке лежал старый <hl>Коран</hl> в кожаной обложке.', 'An old leather-bound <hl>Koran</hl> lay on the shelf.', 'Trên giá có một quyển <hl>kinh Koran</hl> cũ bìa da.'),
    ('безработица', 1): (_, _, 'Ở thị trấn bọn mình, <hl>nạn thất nghiệp</hl> kinh khủng lắm.'),
    ('безработица', 2): (_, _, 'Ai cũng quen với <hl>tình trạng thất nghiệp</hl> rồi, buồn thật.'),
    ('дворник', 3): ('Включи <hl>дворники</hl>, ничего не видно.', "Turn on the <hl>wipers</hl>, I can't see a thing.", 'Bật <hl>cần gạt nước</hl> lên đi, chẳng thấy gì cả.'),
    ('сантехник', 2): ('Я вызвал <hl>сантехника</hl>, в ванной течёт труба.', "I've called a <hl>plumber</hl>, a pipe is leaking in the bathroom.", 'Tôi gọi <hl>thợ sửa ống nước</hl> rồi, ống trong phòng tắm bị rò.'),
    ('шахтёр', 2): ('После взрыва под землёй остались трое <hl>шахтёров</hl>.', 'After the explosion three <hl>miners</hl> were trapped underground.', 'Sau vụ nổ, ba <hl>thợ mỏ</hl> còn kẹt dưới lòng đất.'),
    ('шахтёр', 3): (_, "Almost everyone in town is a <hl>miner</hl>, there's no other work.", _),
    ('специализироваться', 1): (_, _, 'Họ <hl>chuyên về</hl> sửa xe cũ.'),
    ('специализироваться', 2): (_, _, 'Trước đây bọn mình chỉ <hl>chuyên về</hl> bánh cưới.'),
    ('качаться', 1): (_, _, 'Tối nào tớ với con gái cũng <hl>đu đưa</hl> trên xích đu.'),
    ('качаться', 3): (_, _, 'Đừng <hl>lắc lư</hl> trên ghế, hỏng mất!'),
    ('удариться', 1): (_, _, 'Tớ sắp <hl>đập</hl> đầu <hl>vào</hl> cái kệ này rồi!'),
    ('удариться', 2): (_, _, 'Bọn tớ <hl>đụng mạnh</hl> đầu gối vào nhau ở dưới bàn.'),
    ('удариться', 3): ('Только не <hl>ударься</hl> об угол, там темно.', "Just don't <hl>hit yourself</hl> on the corner, it's dark there.", 'Đừng <hl>va phải</hl> góc tường nhé, chỗ đó tối.'),
    ('подвинуться', 3): (_, _, 'Cậu <hl>dịch sang</hl> trái một chút được không?'),
    ('неопределённый', 2): (_, _, 'Cả ngày nay tâm trạng cô ấy cứ <hl>không rõ ràng</hl> sao đó.'),
    ('горизонтальный', 1): ('Нарисуй сверху <hl>горизонтальную</hl> синюю линию.', _, _),
    ('горизонтальный', 2): ('Поверни телефон в <hl>горизонтальное</hl> положение и снимай.', 'Turn the phone to a <hl>horizontal</hl> position and start filming.', 'Xoay điện thoại sang vị trí <hl>nằm ngang</hl> rồi quay đi.'),
    ('горизонтальный', 3): (_, _, 'Mấy đường kẻ <hl>nằm ngang</hl> này làm tớ trông béo ra.'),
    ('выразительный', 2): (_, _, 'Cô ấy làm vẻ mặt <hl>đầy ý nghĩa</hl> rồi im lặng.'),
    ('пушистый', 1): (_, _, 'Nhà bên cạnh có con mèo <hl>lông xù</hl> ghê!'),
    ('даром', 2): (_, _, 'Vé tớ có được <hl>không mất tiền</hl>, bạn tớ cho.'),
    ('даром', 3): ('Три года учёбы не прошли <hl>даром</hl>.', "Three years of study weren't <hl>in vain</hl>.", 'Ba năm học đã không <hl>uổng phí</hl>.'),
    ('серебристый', 1): (_, _, 'Anh ấy lấy cái laptop <hl>màu bạc</hl> thay vì màu đen.'),
    ('серебристый', 2): ('Её ногти покрыты <hl>серебристым</hl> лаком.', 'Her nails are covered in <hl>silvery</hl> polish.', _),
    ('серебристый', 3): (_, _, 'Mặc chiếc váy <hl>ánh bạc</hl> đó cậu sang thật sự.'),
    ('потемнеть', 1): ('Перед грозой небо вдруг <hl>потемнело</hl>.', 'Right before the storm the sky suddenly <hl>got dark</hl>.', 'Ngay trước cơn giông, bầu trời bỗng <hl>tối đi</hl>.'),
    ('потемнеть', 2): (_, _, 'Cái dây bạc đã <hl>sẫm lại</hl> vì nước.'),
    ('потемнеть', 3): ('Без лимона авокадо в салате быстро <hl>потемнеет</hl>.', 'Without lemon the avocado in the salad will quickly <hl>go dark</hl>.', 'Không có chanh thì bơ trong món salad sẽ nhanh <hl>thâm đen</hl>.'),
    ('темнеть', 2): (_, _, 'Mấy quả táo cứ <hl>sẫm lại</hl> trong lúc tớ đang cắt.'),
    ('темнеть', 3): (_, _, 'Mùa đông trời bắt đầu <hl>tối đi</hl> rất sớm.'),
    ('заключительный', 2): (_, _, 'Tập <hl>cuối cùng</hl> sẽ ra vào thứ Sáu.'),
    ('заключительный', 3): (_, _, 'Ở đoạn <hl>kết thúc</hl> thì viết một kết luận ngắn nhé.'),
    ('преобладать', 1): ('В нашем классе <hl>преобладают</hl> девочки.', 'Girls <hl>predominate</hl> in our class.', 'Trong lớp tớ, con gái <hl>chiếm phần lớn</hl>.'),
    ('преобладать', 3): ('Сухая погода будет <hl>преобладать</hl> до конца недели.', 'Dry weather will <hl>prevail</hl> until the end of the week.', 'Thời tiết khô sẽ <hl>chiếm ưu thế</hl> đến hết tuần.'),
    ('подвинуть', 1): (_, _, 'Mai họ sẽ <hl>dịch chuyển</hl> cái sofa lại sát cửa sổ.'),
    ('подвинуть', 2): (_, _, 'Tớ đã <hl>xê dịch</hl> cái ghế của cậu, ngồi đây thoải mái hơn.'),
    ('подвинуть', 3): ('Можешь <hl>подвинуть</hl> кастрюлю? Мне надо помыть руки.', 'Can you <hl>move</hl> the pot? I need to wash my hands.', 'Cậu <hl>đẩy nhẹ</hl> cái nồi <hl>sang</hl> bên được không? Tớ cần rửa tay.'),
    ('переложить', 3): ('Нужно <hl>переложить</hl> мясо в морозилку, а то оно оттает.', "We need <hl>to move</hl> the meat to the freezer or it'll thaw.", _),
    ('подбежать', 3): ('<hl>Подбеги</hl> к бабушке и обними её.', '<hl>Run up</hl> to grandma and hug her.', '<hl>Chạy lại</hl> chỗ bà rồi ôm bà đi con.'),
    ('испачкать', 3): ('Боюсь <hl>испачкать</hl> твоё белое платье.', "I'm afraid of <hl>getting</hl> your white dress <hl>dirty</hl>.", 'Mình sợ <hl>làm bẩn</hl> cái váy trắng của cậu.'),
    ('пролетать', 1): ('Выходные всегда так быстро <hl>пролетают</hl>!', 'Weekends always <hl>fly by</hl> so fast!', 'Cuối tuần lúc nào cũng <hl>trôi vèo</hl> đi mất!'),
    ('пролететь', 1): (_, _, 'Kỳ nghỉ sẽ <hl>trôi vèo</hl> thôi, cậu chẳng kịp nhận ra đâu.'),
    ('тереть', 1): (_, _, 'Mấy đứa đang <hl>dụi</hl> mắt rồi, đến giờ đi ngủ thôi.'),
    ('лить', 1): (_, _, 'Sao họ <hl>đổ</hl> nhiều nước lên bãi cỏ thế?'),
    ('лить', 2): ('Всю ночь <hl>лил</hl> дождь, я не мог уснуть.', "It was <hl>pouring</hl> with rain all night, I couldn't fall asleep.", 'Mưa <hl>trút</hl> suốt đêm, mình không ngủ được.'),
    ('выливать', 1): (_, _, 'Tối nào bọn mình cũng <hl>đổ</hl> nước ở cái khay <hl>ra</hl>.'),
    ('выливать', 2): (_, _, 'Sáng nào bà ấy cũng <hl>đổ</hl> bã trà cũ <hl>ra</hl> bồn rửa.'),
    ('выливать', 3): (_, _, 'Đừng <hl>đổ</hl> dầu <hl>ra</hl> bồn rửa, tắc ống đấy.'),
    ('вылить', 1): (_, _, 'Anh ấy sắp <hl>đổ</hl> chỗ trà nguội <hl>ra</hl> bồn rửa.'),
    ('вылить', 2): (_, _, 'Mình <hl>đổ</hl> sữa cũ <hl>đi</hl> rồi, nó hôi kinh khủng.'),
    ('вылить', 3): (_, _, 'Phải <hl>đổ</hl> nước trong bình <hl>ra</hl>, hoa tàn hết rồi.'),
    ('возвратить', 3): ('Прошу <hl>возвратить</hl> мне документы до конца недели.', 'Please <hl>return</hl> the documents to me by the end of the week.', 'Xin <hl>gửi trả</hl> tôi giấy tờ trước cuối tuần.'),
    ('двухэтажный', 3): ('Мы катались по Лондону на <hl>двухэтажном</hl> автобусе.', _, _),
    ('выселить', 1): (_, _, 'Thêm một bữa tiệc nữa là tôi <hl>đuổi</hl> cậu <hl>ra khỏi nhà</hl>.'),
    ('выселить', 2): (_, _, 'Chủ nhà <hl>đuổi</hl> mấy người hàng xóm <hl>ra khỏi nhà</hl> vì nợ tiền.'),
    ('выселить', 3): (_, _, 'Người ta muốn <hl>buộc</hl> bọn mình <hl>dọn đi</hl> trước cuối tháng.'),
    ('выселять', 1): (_, _, 'Mùa đông bọn mình không <hl>đuổi</hl> người thuê <hl>ra khỏi nhà</hl>, đó là quy định.'),
    ('выселять', 2): (_, _, 'Mỗi mùa hè bà chủ lại <hl>đuổi</hl> sinh viên <hl>ra khỏi nhà</hl>.'),
    ('выселять', 3): (_, _, 'Đừng <hl>buộc</hl> họ <hl>dọn đi</hl> gấp thế, cho họ chút thời gian.'),
    ('перевязать', 1): (_, _, 'Giờ bọn mình <hl>băng bó</hl> đầu gối cho con rồi con đi chơi.'),
    ('перевязать', 2): (_, _, 'Cô điều dưỡng <hl>băng bó</hl> tay cho mình rất nhanh.'),
    ('перевязать', 3): ('Осталось <hl>перевязать</hl> коробку красной лентой.', "All that's left is to <hl>tie up</hl> the box with a red ribbon.", 'Chỉ còn <hl>buộc quanh</hl> cái hộp bằng dải ruy băng đỏ nữa thôi.'),
    ('перевязывать', 1): (_, _, 'Ở bệnh viện này người ta <hl>băng bó</hl> vết thương mỗi sáng.'),
    ('перевязывать', 2): (_, _, 'Ngày nào mẹ cũng <hl>băng bó</hl> ngón tay cho mình.'),
    ('перевязывать', 3): (_, _, 'Đừng <hl>băng bó</hl> chặt thế, đau lắm.'),
    ('поранить', 1): (_, _, 'Để tớ tự làm, không thì tớ lấy kéo <hl>làm</hl> cậu <hl>bị thương</hl> mất.'),
    ('скрипач', 3): ('На конкурсе выступали двадцать <hl>скрипачей</hl>.', 'Twenty <hl>violinists</hl> performed at the competition.', 'Có hai mươi <hl>nghệ sĩ violin</hl> biểu diễn ở cuộc thi.'),
    ('нарядный', 1): (_, 'You look so <hl>dressed up</hl> today!', 'Hôm nay bạn <hl>diện</hl> quá!'),
    ('нарядный', 2): (_, "Put on a <hl>fancy</hl> dress, we're going to the theatre.", _),
    ('нарядный', 3): (_, _, 'Mấy đứa trẻ đã <hl>ăn mặc đẹp</hl> rồi, thợ ảnh đang chờ.'),
    ('сушить', 1): (_, _, 'Kem này <hl>làm khô</hl> da, tôi không mua nữa.'),
    ('сушить', 2): (_, _, 'Cô ấy đang <hl>sấy khô</hl> tóc nên không nghe tiếng gọi cửa.'),
    ('сушить', 3): (_, _, 'Mùa đông tôi không muốn <hl>phơi khô</hl> quần áo ngoài ban công.'),
    ('погаснуть', 1): ('Костёр может <hl>погаснуть</hl>, подбрось дров.', 'The campfire may <hl>go out</hl>, throw on some wood.', 'Đống lửa có thể <hl>lụi tàn</hl> mất, cho thêm củi đi.'),
    ('погаснуть', 3): ('Экран <hl>погаснет</hl>, если его не трогать.', "The screen will <hl>turn off</hl> if you don't touch it.", 'Màn hình sẽ <hl>tự tắt</hl> nếu không chạm vào.'),
    ('дополнить', 3): (_, _, '<hl>Thêm</hl> vài dòng <hl>vào</hl> thư rồi gửi đi.'),
    ('разбиваться', 1): ('На уроке мы часто <hl>разбиваемся</hl> на группы.', 'In class we often <hl>split up</hl> into groups.', 'Trong giờ học chúng tôi hay <hl>chia thành nhóm</hl>.'),
    ('разбиваться', 2): (_, _, 'Sóng <hl>vỡ tan</hl> vào đá suốt cả buổi tối.'),
    ('разбиться', 1): ('Самолёт <hl>разбился</hl> в горах, но все выжили.', 'The plane <hl>crashed</hl> in the mountains, but everyone survived.', 'Máy bay <hl>gặp nạn</hl> trên núi, nhưng mọi người đều sống sót.'),
    ('усиливаться', 1): ('Запах в подъезде <hl>усиливается</hl> с каждым днём.', _, 'Mùi ở sảnh chung cư mỗi ngày một <hl>mạnh lên</hl>.'),
    ('усиливаться', 2): (_, _, 'Cái rét cứ <hl>tăng lên</hl> suốt tuần trước.'),
    ('усиливаться', 3): ('К ночи ветер начал <hl>усиливаться</hl>.', 'Toward night the wind started to <hl>get stronger</hl>.', 'Về đêm gió bắt đầu <hl>mạnh lên</hl>.'),
    ('усилиться', 2): (_, _, 'Đến tối cơn đau <hl>dữ dội hơn</hl>, phải uống thuốc.'),
    ('сформироваться', 1): ('Новая привычка <hl>сформируется</hl> примерно за месяц.', 'A new habit will <hl>form</hl> in about a month.', 'Thói quen mới sẽ <hl>hình thành</hl> sau khoảng một tháng.'),
    ('сформироваться', 2): ('Команда окончательно <hl>сформировалась</hl> прошлой осенью.', 'The team finally <hl>took shape</hl> last fall.', 'Đội đã <hl>hình thành</hl> hẳn vào mùa thu năm ngoái.'),
    ('сформироваться', 3): (_, _, 'Tính cách đã kịp <hl>hình thành</hl> từ hồi còn đi học.'),
    ('ломаться', 1): ('Зимой ветки <hl>ломаются</hl> под тяжёлым снегом.', 'In winter branches <hl>snap</hl> under heavy snow.', 'Mùa đông cành cây <hl>gãy</hl> vì tuyết nặng.'),
    ('сломаться', 1): (_, _, 'Cho tôi một ngày nghỉ, kiểu làm này tôi sắp <hl>suy sụp</hl> rồi.'),
    ('рассыпаться', 1): ('Держи пакет ровно, а то конфеты <hl>рассыплются</hl>!', _, 'Giữ túi cho thẳng, không thì kẹo <hl>đổ tung</hl> ra hết!'),
    ('рассыпаться', 3): ('Печенье в рюкзаке совсем <hl>рассыпалось</hl>.', 'The cookies in my backpack totally <hl>fell apart</hl>.', 'Bánh quy trong ba lô <hl>vỡ vụn</hl> hết rồi.'),
    ('геноцид', 3): ('За <hl>геноцид</hl> его судили в Гааге.', 'He was tried in The Hague for <hl>genocide</hl>.', 'Ông ta bị xét xử ở La Hay vì <hl>tội diệt chủng</hl>.'),
    ('единогласный', 2): ('Судьи вынесли <hl>единогласное</hl> решение.', 'The judges delivered a <hl>unanimous</hl> decision.', 'Các trọng tài đưa ra quyết định <hl>nhất trí</hl>.'),
    ('патриотизм', 2): ('Меня бесит этот показной <hl>патриотизм</hl> в рекламе.', 'This showy <hl>patriotism</hl> in the ads drives me nuts.', 'Tôi phát điên với kiểu <hl>lòng yêu nước</hl> phô trương trong quảng cáo.'),
    ('настоять', 2): (_, _, 'Mẹ <hl>nhất quyết đòi</hl> tôi phải mang áo khoác.'),
    ('настоять', 3): (_, _, 'Phải <hl>khăng khăng</hl> đòi giảm giá thôi, giá cao quá.'),
    ('разговорчивый', 2): ('После кофе бабушка становится <hl>разговорчивой</hl>.', 'After coffee Grandma gets <hl>talkative</hl>.', 'Uống cà phê xong là bà <hl>nói nhiều</hl> hẳn lên.'),
    ('легкомысленный', 1): ('Не обижайся на него, он просто <hl>легкомысленный</hl>.', "Don't be offended, he's just <hl>thoughtless</hl>.", 'Đừng giận cậu ấy, cậu ấy chỉ <hl>nông nổi</hl> thôi.'),
    ('легкомысленный', 3): ('Не делай <hl>легкомысленных</hl> покупок перед зарплатой.', _, 'Đừng mua sắm <hl>thiếu suy nghĩ</hl> trước ngày lĩnh lương.'),
    ('беззащитный', 2): (_, _, 'Chúng tôi tìm thấy ngoài sân một con chim nhỏ <hl>không tự vệ được</hl>.'),
    ('сентиментальный', 3): ('Над этим <hl>сентиментальным</hl> сериалом я рыдала весь вечер.', _, _),
    ('темперамент', 1): ('У моего младшего брата бурный <hl>темперамент</hl>.', 'My little brother has a fiery <hl>temperament</hl>.', 'Thằng em tôi có <hl>tính khí</hl> sôi nổi lắm.'),
    ('мармелад', 2): ('Дети за вечер съели весь <hl>мармелад</hl>.', 'The kids ate all the <hl>fruit jellies</hl> in one evening.', 'Bọn trẻ ăn hết sạch <hl>kẹo dẻo trái cây</hl> trong một buổi tối.'),
    ('продовольственный', 2): ('Пострадавшим отправили <hl>продовольственную</hl> помощь.', '<hl>Food</hl> aid was sent to the victims.', 'Người ta đã gửi viện trợ <hl>lương thực</hl> cho người bị nạn.'),
    ('окорок', 1): (_, _, 'Bố nướng <hl>đùi lợn</hl> cho ngày lễ.'),
    ('окорок', 2): ('Нарежь немного <hl>окорока</hl> на бутерброды.', 'Slice some <hl>ham</hl> for sandwiches.', 'Thái ít <hl>giăm bông</hl> để làm bánh mì kẹp đi.'),
    ('окорок', 3): (_, _, 'Trong cửa hàng <hl>giăm bông</hl> nhiều loại kinh khủng.'),
    ('ананас', 3): ('Этот <hl>ананас</hl> ещё зелёный, пусть полежит.', 'This <hl>pineapple</hl> is still unripe, let it sit for a while.', 'Quả <hl>dứa</hl> này còn xanh, cứ để thêm đã.'),
    ('откусить', 2): (_, _, 'Mấy đứa <hl>cắn</hl> mỗi đứa <hl>một miếng</hl> rồi chạy đi chơi.'),
    ('откусывать', 1): (_, _, 'Bọn mình <hl>cắn</hl> bánh mỗi lần <hl>một miếng</hl> nhỏ.'),
    ('откусывать', 2): (_, _, 'Cô ấy thỉnh thoảng <hl>cắn một miếng</hl> táo, mắt vẫn xem phim bộ.'),
    ('откусывать', 3): (_, _, 'Đừng <hl>cắn một miếng</hl> to thế, nhai hết đã.'),
    ('греть', 1): (_, _, 'Em đang <hl>làm nóng</hl> súp đây, ngồi vào bàn đi.'),
    ('греть', 2): (_, _, 'Cô ấy <hl>làm nóng</hl> sữa cho em bé mỗi sáng.'),
    ('греть', 3): ('Зимой кошка <hl>греет</hl> мне ноги.', 'In winter the cat <hl>warms</hl> my feet.', 'Mùa đông con mèo <hl>sưởi ấm</hl> chân cho tớ.'),
    ('социология', 3): ('Сестра сдала экзамен по <hl>социологии</hl> на пятёрку.', 'My sister got an A on her <hl>sociology</hl> exam.', 'Chị tôi thi môn <hl>xã hội học</hl> được điểm năm.'),
    ('опровержение', 1): (_, 'The newspaper printed a <hl>retraction</hl> only a week later.', 'Mãi một tuần sau tờ báo mới đăng <hl>lời cải chính</hl>.'),
    ('уточнение', 1): (_, _, 'Cho tôi <hl>làm rõ</hl> thêm một chút về buổi gặp nhé?'),
    ('уточнение', 3): ('Цена на сайте требует <hl>уточнения</hl>.', 'The price on the website needs <hl>clarification</hl>.', 'Giá trên trang web cần được <hl>làm rõ</hl>.'),
    ('продолжительный', 1): (_, _, 'Một buổi nói chuyện <hl>kéo dài</hl> với giám đốc đang chờ chúng ta.'),
    ('продолжительный', 3): (_, _, 'Không ngờ cuộc nói chuyện <hl>kéo dài</hl> đến thế, tôi bị trễ.'),
    ('устаревать', 1): (_, _, 'Hình như chúng ta đang <hl>lỗi thời</hl> dần cùng với mấy câu đùa của mình.'),
    ('устаревать', 2): (_, _, 'Ngày trước máy tính <hl>lỗi thời</hl> chỉ trong hai năm.'),
    ('устаревать', 3): ('Некоторые слова начинают <hl>устаревать</hl>, так уже не говорят.', "Some words are starting to <hl>become obsolete</hl>, people don't talk like that anymore.", 'Một số từ bắt đầu <hl>cũ đi</hl>, giờ chẳng ai nói thế nữa.'),
    ('калькулятор', 1): (_, _, 'Cho tôi cái <hl>máy tính bỏ túi</hl>, tôi tự tính không nổi.'),
    ('калькулятор', 2): (_, _, 'Mấy cái <hl>máy tính cầm tay</hl> này nút đã mờ hết rồi.'),
    ('калькулятор', 3): (_, _, 'Tính bằng <hl>máy tính bỏ túi</hl> đi, tôi không tin cậu.'),
    ('брести', 3): ('Не хочу <hl>брести</hl> через весь парк в темноте.', "I don't want to <hl>trudge</hl> across the whole park in the dark.", 'Tôi không muốn <hl>lê bước</hl> qua cả công viên trong bóng tối.'),
    ('взвесить', 2): ('Давай сначала <hl>взвесим</hl> все за и против.', "Let's <hl>weigh up</hl> all the pros and cons first.", 'Mình <hl>cân nhắc</hl> hết lợi hại trước đã.'),
    ('взвесить', 3): (_, _, '<hl>Cân</hl> bột mì đi rồi hãy cho vào bột nhào.'),
    ('взвешивать', 3): ('Она всегда <hl>взвешивает</hl> каждое слово.', 'She always <hl>weighs</hl> every word.', 'Cô ấy lúc nào cũng <hl>cân nhắc</hl> từng lời.'),
    ('бездействовать', 2): ('Старая фабрика <hl>бездействует</hl> уже два года.', 'The old factory has been <hl>standing idle</hl> for two years.', 'Nhà máy cũ <hl>không hoạt động</hl> đã hai năm nay.'),
}
VI = {w: ("chạy ra", "chạy ra (ra ngoài, lúc xuất phát)") for w in ("выбежать", "выбегать")}
OL = '<ol class="meaning-list">%s</ol>'
li = lambda *a: "".join(f"<li>{x}</li>" for x in a)                       # noqa: E731
TB = li("to break down", "to stop working", "to break", "to break", "to snap", "to crack", "to break off")
MEANING = {
    "сломаться": (TB + li("to put on airs", "to pose", "to be affected", "to make difficulties"), TB.replace(li("to break"), "", 1)),
    "испачкать": (li("to soil/make dirty/desecrate with awful words"), li("to soil", "to make dirty", "to tarnish")),
    "переслать": (li("to forward/to send back"), li("to forward", "to send on")),
    "зачем-то": (li("for some reason"), li("for some purpose", "for some reason")),
    "где-либо": (li("somewhere", "anywhere"), li("anywhere", "somewhere")),
    "куда-либо": (li("somewhere", "anywhere"), li("anywhere", "somewhere")),
    "пересаживаться": (li("to take another seat", "to change places", "to exchange seats"),
                       li("to take another seat", "to change places", "to exchange seats", "to change (trains, buses)")),
    "расстегнуть": (li("to undo or unfasten unbutton"), li("to undo", "to unfasten", "to unbutton")),
    "бездельничать": (li("to idle loaf do nothing"), li("to idle", "to loaf", "to do nothing")),
    "греть": (li("to heat something up to a certain point or target temperature"), li("to warm", "to heat", "to give off warmth")),
    "кульминация": (li("culmination"), li("climax", "culmination")),
    "потереть": (li("to rub"), li("to rub", "to grate")),
    "квалифицированный": (li("qualified adj"), li("qualified", "skilled")),
}
HD = {
    "прошлогодний": [(" Bảng có dạng ngắn nhưng không ai dùng — bỏ qua.", " Không có dạng ngắn.")],
}


def g_rassyp(g):
    for k in ("presfut", "future"):
        assert g[k][5] == "рассы́паются"
        g[k][5] = "рассы́плются"


def g_sform(g):
    assert not any(g["presfut"] + g["past"] + g["imper"])
    g["presfut"] = ["сформиру́" + x for x in ("юсь", "ешься", "ется", "емся", "етесь", "ются")]
    g["future"] = list(g["presfut"])
    g["past"] = ["сформирова́л" + x for x in ("ся", "ась", "ось", "ись")]
    g["imper"] = ["сформиру́йся", "сформиру́йтесь"]


def g_rasch(g):
    p = g["parts"]
    assert "discharged" in p["activePresent"][0]["en"] and "anticipated" in p["activePast"][0]["en"]
    p["activePresent"][0]["en"] = "settling up, paying"
    p["activePast"][0]["en"] = "that was settling up, that was paying"


def g_dopoln(g):
    assert g["parts"].pop("gerundPresent") == [{"f": "допо́лня"}]
    for x in g["parts"]["gerundPast"]:
        x["f"] = {"дополнивши": "допо́лнивши"}.get(x["f"], x["f"])


def g_khongngan(g):
    assert any(g["shorts"])
    g["shorts"], g["adverb"] = [""] * 4, ""


def g_kval(g):
    assert g["shorts"][0] == "квалифици́ровен"
    b = "квалифици́рован"
    g["shorts"], g["adverb"] = [b, b + "на", b + "но", b + "ны"], b + "но"


GR = {"рассыпаться": g_rassyp, "сформироваться": g_sform, "рассчитываться": g_rasch, "дополнить": g_dopoln,
      "прошлогодний": g_khongngan, "настольный": g_khongngan, "квалифицированный": g_kval}
O = {"коран": {"Word": "Кора́н"}}

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
if not sync_truoc_khi_ghi_lo("vá k247-k256"):
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
