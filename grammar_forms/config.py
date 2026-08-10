# ==============================================================================
# --- CẤU HÌNH MẢNG THẺ BIẾN CÁCH ---
# Tách khỏi anki_tools/config.py để đổi gì ở đây cũng không đụng deck từ vựng.
# ==============================================================================

# Deck tổng của mảng ngữ pháp. Đứng riêng, KHÔNG nằm trong cây RUSSIAN:: để
# thống kê/tìm kiếm deck từ vựng không bị lẫn thẻ biến cách.
GRAMMAR_DECK_PARENT = "GRAMMAR"

# --- Loại biến cách 1: số nhiều bất quy tắc ---
PLURAL_DECK = f"{GRAMMAR_DECK_PARENT}::plural-irregular"
PLURAL_MODEL = "RU_Plural"

# Tên deck cũ (trước 20/07/2026) — chỉ dùng cho bước đổi tên một lần.
PLURAL_DECK_LEGACY = "Irregular"

# Thứ tự field của model RU_Plural. 3 field cuối là MỚI (thêm 20/07/2026):
# thẻ cũ chỉ có 8 field đầu, thêm field không làm hỏng thẻ cũ (giá trị rỗng).
PLURAL_FIELDS = [
    "Word",          # số ít, có dấu nhấn:  до́м
    "WordClean",     # số ít, không dấu nhấn (để dò trùng): дом
    "Plural",        # số nhiều, có dấu nhấn: дома́
    "PluralClean",   # số nhiều, không dấu nhấn (để gõ đáp án): дома
    "Meaning",       # nghĩa tiếng Anh (HTML <ol>)
    "Vietnamese",    # nghĩa tiếng Việt
    "Audio",         # [sound:...] phát âm số ít
    "PluralAudio",   # [sound:...] phát âm số nhiều
    "ExamplesHTML",  # 3 ví dụ dùng ĐÚNG dạng số nhiều
    "KindLabel",     # nhãn kiểu bất quy tắc, vd "Đực -а/-я (nhấn cuối)"
    "RawExamples",   # JSON ví dụ thô, để làm lại thẻ sau này
]

PLURAL_CARD_NAME = "RU Plural Typing v1"

# ==============================================================================
# --- Loại biến cách 2: CHI PHỐI (từ nào bắt từ đứng sau nó dùng cách nào) ---
# Cây deck xếp theo TỪ LOẠI rồi tới tên từng từ, để vào deck một từ là luyện
# riêng nó, vào deck cha là luyện tổng hợp (hành vi gốc của Anki).
# ==============================================================================
CHIPHOI_DECK = f"{GRAMMAR_DECK_PARENT}::chi phối"
CHIPHOI_DECK_GIOITU = f"{CHIPHOI_DECK}::giới từ"
CHIPHOI_MODEL = "RU_ChiPhoi"
CHIPHOI_CARD_NAME = "RU ChiPhoi Typing v1"

# Nguồn dữ liệu. Người soạn chỉ viết 4 cột; cụm Nga và dòng đối chiếu do MÁY
# sinh lúc nạp — xem `grammar_forms/chi_phoi.py`.
CHIPHOI_TSV = "data/chi_phoi.tsv"

CHIPHOI_FIELDS = [
    "Khoa",        # khoá chống trùng, máy dựng:  в|школа|4
    "GioiTu",      # dạng GỐC, hiện ở mặt trước:  в   (kể cả khi đáp án là `во`)
    "Lemma",       # từ nguyên thể có dấu nhấn:   Фра́нция
    "Cum",         # cụm đúng, có dấu nhấn:       во Фра́нции      ← MÁY SINH
    "CumClean",    # cụm không dấu, để gõ:        во франции      ← MÁY SINH
    "Cach",        # nhãn hiện trên huy hiệu:     cách 6
    "Vietnamese",  # đề bài — THỨ DUY NHẤT quyết định đáp án nào là đúng
    "DoiChieu",    # các cách khác của cùng danh từ (HTML)         ← MÁY SINH
    "Nguon",       # `bảng` = ghép từ bảng chia · `tay` = gõ tay (ngoại lệ)
]

# Biến thể chính tả → dạng gốc. Dùng để (1) hiện mặt trước (2) xếp deck.
# 🔴 Chiều NGƯỢC LẠI (gốc → biến thể) CỐ Ý không có: luật `в→во` phụ thuộc cụm
# phụ âm đứng sau, máy đoán sai là đẻ ra tiếng Nga SAI mà vẫn báo XANH — người
# học không có cách nào biết. Nên người soạn viết thẳng dạng sẽ hiện vào cột 1.
BIEN_THE_GOC = {"во": "в", "со": "с", "об": "о", "обо": "о", "ко": "к"}

# Số cách → khoá trong bảng chia của OpenRussian, và nhãn tiếng Việt.
CACH_KHOA = {"1": "nom", "2": "gen", "3": "dat", "4": "acc", "5": "inst", "6": "prep"}

# Nhãn tiếng Việt cho từng kiểu bất quy tắc (khớp cột `kind` của TSV).
# Hiện lên mặt sau thẻ để bạn nhận ra QUY LUẬT chứ không học vẹt từng từ.
KIND_LABELS = {
    "a-я":      "Giống đực → -а́/-я́ (nhấn vào đuôi)",
    "ья":       "Đuôi -ья (thân mở rộng)",
    "ена":      "Đuôi -ена (danh từ -мя)",
    "ане":      "Đuôi -ане (mất -ин)",
    "еса":      "Đuôi -еса (thân mở rộng)",
    "ева":      "Đuôi -ева",
    "ята":      "Đuôi -ята (con non)",
    "ер":       "Đuôi -ери (thân mở rộng)",
    "e-yo":     "Đổi nguyên âm е → ё",
    "o-i":      "Trung tính → -и (không phải -а)",
    "thay-goc": "Thay gốc từ hoàn toàn",
    "khac":     "Bất quy tắc khác",
}
