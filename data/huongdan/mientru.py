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
    "двери́": "CÁCH VỊ TRÍ (locative) của дверь, chỉ dùng sau в/на: в двери́ = ở ngay khung "
             "cửa — grammar_cache ghi rõ ô prep số ít là 'две́ри, в двери́', tức hai dạng cùng "
             "tồn tại; thẻ k68 cố ý nêu cặp này để user khỏi tưởng bảng in sai. nouns.csv chỉ "
             "có đồng tự две́ри = cách 2 số ít / cách 1 số nhiều",
    "ду́хи": "SỐ NHIỀU của дух (linh hồn, hơi) — ду́хи · ду́хов; thẻ k76 cố ý nêu cặp đối lập "
            "ду́хи (các linh hồn) ↔ духи́ (nước hoa) vì hai từ chỉ khác nhau đúng chỗ trọng âm, "
            "nouns.csv chỉ có духи́ = nước hoa (danh từ chỉ dùng số nhiều). Cùng lớp với "
            "дорога́ và до́бро ở dưới",
    "ви́лок": "số nhiều cách 2 của ви́лка (cái nĩa), dạng chèn nguyên âm chạy — thẻ k77 dạy "
             "đúng cặp này, và chính nouns.csv ghi pl_gen của ви́лка là ви́лок. Máy vẫn kêu vì "
             "khoá tra là mặt chữ trần: nó khớp phải DÒNG RIÊNG của đồng tự вило́к = bắp cải "
             "(head of cabbage), một lexeme khác hẳn. Cùng lớp với бе́лок và по́лок ở trên",
    "замо́к": "замо́к = Ổ KHOÁ, đồng tự với за́мок = lâu đài — nouns.csv có ĐỦ CẢ HAI dòng "
             "(за'мок castle · замо'к lock) nhưng khoá tra gộp về một mặt chữ nên chỉ một dòng "
             "sống sót; thẻ k77 dùng đúng nghĩa ổ khoá trong вста́вить ключ в замо́к. "
             "Đây là cặp trọng âm kinh điển của tiếng Nga, không phải lỗi soạn",
    "до́бро": "DẠNG NGẮN giống trung của tính từ до́брый (tốt bụng) — grammar_cache ghi rõ bộ "
             "добр · добра́ · до́бро · до́бры; thẻ k42 cố ý nêu cặp đối lập до́бро (dạng ngắn) ↔ "
             "добро́ (DANH TỪ: điều thiện, của cải) vì hai từ chỉ khác nhau đúng chỗ trọng âm, "
             "nouns.csv chỉ có добро́. Cùng lớp với жарка́, ни́зок, дорога́ ở trên",
    "у́ток": "số nhiều cách 2 của у́тка (con vịt), dạng chèn nguyên âm chạy — chính nouns.csv "
            "ghi pl_gen của у́тка là у́ток, thẻ k78 dạy đúng cặp này. Máy vẫn kêu vì khoá tra là "
            "mặt chữ trần: nó khớp phải DÒNG RIÊNG của đồng tự уто́к = sợi ngang khi dệt vải "
            "(weft, woof), một lexeme khác hẳn. Cùng lớp với бе́лок, по́лок, ви́лок ở trên",
    "коро́бок": "số nhiều cách 2 của коро́бка (cái hộp), dạng chèn nguyên âm chạy — chính "
               "nouns.csv ghi pl_gen của коро́бка là коро́бок, thẻ k78 dạy đúng cặp này. Máy khớp "
               "phải DÒNG RIÊNG của đồng tự коробо́к = hộp nhỏ, bao diêm (коробо́к спи́чек). "
               "Cùng lớp với ви́лок ở trên",
    "сера́": "DẠNG NGẮN giống cái của tính từ се́рый (xám) — grammar_cache ghi rõ bộ "
            "сер · сера́ · се́ро · се́ры; thẻ k82 cố ý nêu cặp сера́ (xám) ↔ се́ра (lưu huỳnh, "
            "gốc của се́рный) vì hai từ chỉ khác nhau đúng chỗ trọng âm, nouns.csv chỉ có "
            "danh từ се́ра. Cùng lớp với жарка́, дорога́, до́бро ở trên",
    "волна́": "danh từ волна́ = con sóng (gốc của волнова́ться, thẻ k98) — chính nouns.csv có "
             "DÒNG RIÊNG волна' (wave, breaker) với đủ bảng biến cách. Máy kêu vì khoá tra mặt "
             "chữ trần khớp phải dòng ĐỨNG TRƯỚC во'лна (sg_only), tức đồng tự cổ/phương ngữ "
             "во́лна = len, lông cừu (cùng gốc tiếng Ukraina во́вна) mà csv glossed nhầm là wave. "
             "Cùng lớp với у́ток, коро́бок ở trên",
    "я́рок": "DẠNG NGẮN giống đực của tính từ я́ркий (sáng chói), dạng chèn nguyên âm chạy — "
            "grammar_cache ghi rõ bộ я́рок · ярка́ · я́рко · я́рки, thẻ k109 dạy đúng chỗ chèn о "
            "này; nouns.csv chỉ có danh từ đồng tự яро́к (chỉ glossed tiếng Đức 'Jarok', không "
            "có nghĩa tiếng Anh). Cùng lớp với ни́зок ở trên",
    "ярка́": "DẠNG NGẮN giống cái của tính từ я́ркий — cùng bộ я́рок · ярка́ · я́рко · я́рки "
            "trong grammar_cache, thẻ k109 dạy đúng chỗ trọng âm nhảy ra đuôi; nouns.csv chỉ có "
            "danh từ đồng tự я́рка = cừu cái non (young ewe). Cùng lớp với жарка́, сера́ ở trên",
    "по́лон": "DẠNG NGẮN giống đực của tính từ по́лный (đầy), dạng chèn nguyên âm chạy — "
             "grammar_cache ghi rõ bộ по́лон · полна́ · полно́ · полны́, thẻ k113 dạy đúng chỗ "
             "chèn о này; nouns.csv chỉ có danh từ cổ đồng tự поло́н = cảnh bị bắt làm tù binh "
             "(glossed tiếng Đức Gefangenschaft, không có nghĩa tiếng Anh). Cùng lớp với ни́зок, "
             "я́рок ở trên",
    "орга́н": "орга́н = CÂY ĐÀN ORGAN, đồng tự với о́рган = cơ quan (cơ thể, nhà nước) — thẻ k152 "
             "cố ý nêu cặp này để user khỏi lẫn vì hai từ chỉ khác nhau đúng chỗ trọng âm; "
             "nouns.csv chỉ có о́рган. Cùng lớp với замо́к, ду́хи ở trên",
    "виски́": "số nhiều cách 1/4 của висо́к (thái dương) — chính nouns.csv dòng висо́к ghi pl_nom "
             "виски'; thẻ k168 cố ý nêu cặp виски́ ↔ ви́ски (rượu whisky) vì hai từ chỉ khác "
             "nhau đúng chỗ trọng âm. Máy kêu vì khoá tra mặt chữ trần khớp dòng ви́ски. "
             "Cùng lớp với орга́н ở trên",
    "пропа́сть": "ĐỘNG TỪ пропа́сть = biến mất (thể hoàn thành của пропада́ть, thẻ k175) — từ điển "
                "chỉ có danh từ đồng tự про́пасть = vực thẳm; thẻ k175 cố ý nêu cặp này. "
                "Cùng lớp với помо́чь ở trên",
    "мука́": "мука́ = BỘT, BỘT MÌ (chính từ đầu thẻ k192, mục id 58505) — đồng tự với му́ка = "
            "nỗi đau khổ; nouns.csv chỉ có му́ка nên máy kêu oan ngay cả từ đầu thẻ. Thẻ k192 cố "
            "ý nêu cặp này vì hai từ chỉ khác nhau đúng chỗ trọng âm. Cùng lớp với орга́н ở trên",
    "тупи́к": "тупи́к = NGÕ CỤT, BẾ TẮC (chính từ đầu thẻ k191, mục id 58607) — đồng tự với ту́пик "
             "= chim hải âu cổ rụt (puffin). nouns.csv có ĐỦ CẢ HAI dòng (ту'пик animate=1 là con "
             "chim nhưng glossed nhầm dead end · тупи'к) mà khoá tra gộp mặt chữ nên dòng chim "
             "thắng, máy kêu oan ngay cả từ đầu thẻ. Agent k172 đã gặp đúng chỗ này. Cùng lớp "
             "với замо́к, мука́ ở trên",
    "белка́": "cách 2 số ít của бело́к (lòng trắng, chất đạm), dạng nguyên âm chạy — bảng chia "
             "ghi бело́к · белка́ · белку́ · белко́м, thẻ k205 cố ý nêu cặp белка́ ↔ бе́лка (con "
             "sóc) vì hai từ chỉ khác chỗ trọng âm; nouns.csv chỉ có бе́лка. Mặt gương của mục "
             "бе́лок ở trên, cùng lớp với курка́",
}

# VÁ NGUỒN — dòng `nouns.csv` mà cột `accented` trái với CHÍNH cột `pl_nom` của nó.
# Khác MIEN_TRU (thẻ đúng, máy kêu oan vì đồng tự): ở đây TỪ ĐIỂN sai, nên sửa từ
# điển chứ không miễn trừ thẻ. Không vá vào file: csv là dump tải về, bị gitignore,
# tải lại là mất. Đo 21/11: 206 dòng chỉ-số-nhiều, đúng 2 dòng lệch trọng âm thật.
SUA_NGUON = {
    "усы": "усы́",          # csv `у'сы`, pl_nom `усы'` — agent k139 bắt; số ít là у́с
    "стринги": "стри́нги",  # csv `стринги'`, pl_nom `стри'нги`
}
