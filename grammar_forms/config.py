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
