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
    "лет": "cách 2 số nhiều của год (năm) — `пять лет`, thẻ k29 dạy đúng chỗ này. Từ điển "
           "chỉ có đồng tự лёт = sự bay (на лету́). Miễn trừ này SINH RA 08/08 cùng lúc với "
           "việc mở khoá so sánh `ё`: trước đó mọi dạng có `ё` bị bỏ qua nên chưa ai kêu",
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
    "ни́зок": "DẠNG NGẮN giống đực của tính từ ни́зкий (thấp), dạng chèn nguyên âm chạy — "
            "grammar_cache ghi rõ bộ dạng ngắn ни́зок · низка́ · ни́зко · ни́зки, thẻ k40 dạy "
            "đúng chỗ chèn о này; nouns.csv chỉ có danh từ đồng tự низо́к = phần dưới nhỏ "
            "(dạng nhỏ của низ). Cùng lớp với жарка́ đã miễn trừ ở trên",
    "дорога́": "DẠNG NGẮN giống cái của tính từ дорого́й (đắt) — grammar_cache ghi rõ bộ "
              "до́рог · дорога́ · до́рого · до́роги; thẻ k40 cố ý nêu cặp đối lập дорога́ (đắt) ↔ "
              "доро́га (con đường) vì đây là cặp chỉ khác nhau ở chỗ trọng âm, "
              "nouns.csv chỉ có доро́га. Cùng lớp với жарка́ và ни́зок ở trên",
    "вели́к": "DẠNG NGẮN giống đực của tính từ вели́кий, đồng thời là dạng ngắn mà "
             "большо́й mượn dùng — grammar_cache ghi rõ bộ вели́к · велика́ · велико́ · велики́, "
             "thẻ k41 dạy đúng chỗ này; nouns.csv chỉ có danh từ khẩu ngữ đồng tự ве́лик = "
             "cái xe đạp (rút gọn của велосипе́д). Cùng lớp với жарка́ và ни́зок ở trên",
    "силён": "DẠNG NGẮN giống đực của tính từ си́льный (mạnh) — grammar_cache ghi rõ bộ "
            "силён · сильна́ · си́льно · си́льны, thẻ k42 dạy đúng chỗ ь biến thành ё và "
            "trọng âm chạy ra cuối. Máy đọc nhầm vì khoá tra từ điển gộp ё về е (như нёбо ở "
            "trên), nên силён bị đọc thành силен rồi khớp phải danh từ đồng tự силе́н = "
            "Silenus, thần rừng Hy Lạp (nouns.csv chỉ có nghĩa tiếng Đức Satyr, không có "
            "nghĩa tiếng Anh)",
    "до́бро": "DẠNG NGẮN giống trung của tính từ до́брый (tốt bụng) — grammar_cache ghi rõ bộ "
             "добр · добра́ · до́бро · до́бры; thẻ k42 cố ý nêu cặp đối lập до́бро (dạng ngắn) ↔ "
             "добро́ (DANH TỪ: điều thiện, của cải) vì hai từ chỉ khác nhau đúng chỗ trọng âm, "
             "nouns.csv chỉ có добро́. Cùng lớp với жарка́, ни́зок, дорога́ ở trên",
}
