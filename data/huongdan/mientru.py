# -*- coding: utf-8 -*-
"""Từ ĐỒNG TỰ miễn trừ khỏi soát trọng âm — CỬA DUY NHẤT (G0, 31/07/2026, QD-03).

Vì sao tách riêng: `congcu.py` và `kiemtra.py` từng tự giữ hai bản `MIEN_TRU`
lệch nhau (5 mục vs 1 mục) — bản thiếu của `kiemtra.py` khiến nó kêu oan 4 từ
đúng chính tả (жила́, запа́х, помо́чь, у́ха) là "trọng âm lệch". Một bộ soát kêu
oan là bộ soát chết, nên gộp về MỘT nơi, cả hai script cùng import.

Máy không phân biệt được hai từ khác nhau viết giống hệt (đồng tự) — mỗi mục
phải miễn trừ TAY và ghi rõ lý do, học từ chính `MIEN_TRU` gốc của `congcu.py`.
"""

MIEN_TRU = {
    "ви́на": "số nhiều của вино́ (rượu vang); từ điển chỉ có вина́ = lỗi lầm",
    "жила́": "quá khứ giống cái của động từ жить (sống); từ điển chỉ có danh từ жи́ла = gân, mạch",
    "запа́х": "đồng tự với за́пах (mùi): запа́х = vạt áo choàng chồng lên nhau (từ запахну́ть); "
             "thẻ k05 dạy đúng cặp trọng âm này, từ điển chỉ có за́пах",
    "помо́чь": "ĐỘNG TỪ помо́чь = giúp đỡ (thể hoàn thành của помога́ть); từ điển chỉ có danh từ "
              "phương ngữ по́мочь = buổi làm giúp tập thể (số nhiều по́мочи = dây đeo quần)",
    "бе́лок": "số nhiều cách 2 của бе́лка (con sóc), dạng chèn nguyên âm chạy — thẻ k25 dạy "
             "đúng cặp trọng âm này; từ điển chỉ có đồng tự бело́к = lòng trắng trứng, chất đạm",
    "по́лок": "số nhiều cách 2 của по́лка (cái kệ), dạng chèn nguyên âm chạy — thẻ k23 dạy "
             "đúng cặp trọng âm này; từ điển chỉ có đồng tự поло́к = bệ nằm trong nhà tắm hơi Nga",
    "полка́": "cách 2 số ít của полк (trung đoàn); thẻ k23 dạy đúng cặp đối lập по́лка (kệ) ↔ "
             "полка́ (của trung đoàn), từ điển chỉ có по́лка = cái kệ",
    "нёбо": "нёбо = VÒM MIỆNG, từ khác hẳn не́бо (bầu trời) — thẻ k26 cố ý nêu cặp này để "
            "user khỏi lẫn. Máy không tách được vì khoá tra từ điển gộp ё về е "
            "(nouns.csv in ё thành е), nên нёбо bị đọc thành небо rồi báo lệch trọng âm; "
            "bản thân нёбо không có mục riêng trong nouns.csv",
    "жарка́": "DẠNG NGẮN giống cái của tính từ жа́ркий (nóng) — grammar_cache ghi rõ bộ dạng "
             "ngắn жа́рок · жарка́ · жа́рко · жа́рки, thẻ k27 dạy đúng chỗ trọng âm dịch này; "
             "nouns.csv chỉ có danh từ đồng tự жа́рка = việc rán (từ жа́рить)",
    "сорока́": "cách 2·3·5·6 của số từ со́рок (bốn mươi) — grammar_cache ghi rõ cả bảng chỉ có "
              "một dạng gián tiếp сорока́; thẻ k29 cố ý nêu cặp này để user khỏi lẫn, "
              "nouns.csv chỉ có danh từ đồng tự соро́ка = chim ác là",
    "у́ха": "cách 2 của у́хо (cái tai), dùng trong thành ngữ слу́шать кра́ем у́ха (thẻ k02); "
           "từ điển chỉ có danh từ đồng tự уха́ = canh cá",
    "курка́": "cách 2 số ít của куро́к (cò súng), dạng nguyên âm chạy — grammar_cache ghi rõ "
             "куро́к · курка́ · курку́ · курко́м, thẻ k64 dạy đúng chỗ chữ о rơi mất; "
             "nouns.csv chỉ có danh từ phương ngữ đồng tự ку́рка = gà mái (glossed toàn tiếng Đức "
             "Henne, không có nghĩa tiếng Anh)",
}
