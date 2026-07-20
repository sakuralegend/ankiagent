# ==============================================================================
# --- GRAMMAR_FORMS: mảng THẺ BIẾN CÁCH, tách hẳn khỏi mảng từ vựng ---
#
# Vì sao tách riêng khỏi anki_tools/?
#   anki_tools/ lo deck từ vựng RUSSIAN::<chủ đề> (model RU_Word) đang chạy ổn.
#   Package này lo deck ngữ pháp GRAMMAR::<loại> (model riêng), thẻ có cấu trúc
#   KHÁC hẳn: mặt trước hỏi 1 dạng, mặt sau trả lời dạng biến đổi.
#   Tách ra để sửa/nâng cấp mảng này KHÔNG bao giờ làm hỏng deck từ vựng.
#
# Quan hệ MỘT CHIỀU: grammar_forms -> anki_tools (chỉ mượn hạ tầng dùng chung:
# tải audio, lưu media, gọi AI, tiện ích chữ). anki_tools KHÔNG bao giờ import
# ngược lại đây. Xóa cả thư mục này đi thì deck từ vựng vẫn chạy nguyên vẹn.
#
# Muốn thêm loại biến cách mới (vd genitive số nhiều, chia động từ):
#   1. Khai báo deck + model trong config.py
#   2. Viết prompt trong ai.py
#   3. Thêm 1 nút trong tgbot/flow_special.py
# ==============================================================================
