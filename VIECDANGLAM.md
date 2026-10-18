# 🎯 VIỆC ĐANG LÀM
> Phiếu bị GHI ĐÈ ở việc kế tiếp. Xong việc thì để trống, chừa đúng dòng tiêu đề.

## 🔊 Giọng Yandex alena cho từ + câu ví dụ, thêm nút chỉnh tốc độ

**Một câu:** mọi thẻ (cũ + bot thêm mới) đọc từ và 3 câu ví dụ bằng Yandex alena, đúng trọng âm; khi chủ động muốn thì nghe chậm lại được.
**User đã chốt 18/10:** alena 1× · thay TOÀN BỘ tiếng từ (kể cả Shtooka) · tự viết script · câu ví dụ BẤM mới phát (▶ mờ cuối câu Nga) · lật thẻ: từ TỰ PHÁT 1× như cũ, KHÔNG theo nút tốc độ · nút tốc độ = chữ mờ ở ĐÁY thẻ, chạm đổi 1× → 0,75× → 0,5× → 1× (user đổi 19/10), áp cho mọi lần BẤM ▶ (từ + câu), sang thẻ mới về 1× · không nút "nghe lại" riêng · trọng âm trong câu để Yandex đoán HẾT (đo: 90% từ chính trong câu KHÔNG có dấu; tra bảng của thẻ phủ được 94% — user vẫn chọn không làm) · làm MỘT lượt · TẢI ĐỦ toàn bộ tiếng rồi MỚI đụng Anki (`fix_audio.py --tai` → `--apply`).
**Coi là XONG khi:** iPhone: lật thẻ nghe согла́сный đủ âm ở 1×; chạm "1×" thành "0,75×" rồi bấm ▶ từ/câu thì đọc chậm; sang thẻ khác lại 1×.
**CỐ Ý KHÔNG làm:** Azure · HyperTTS · tự đánh dấu mọi từ trong câu · tự phát câu · thanh trượt · nhớ tốc độ giữa các thẻ.
**Đã đo:** OpenRussian hỏng cả máy đọc mới (27 file cụt) lẫn Shtooka (согласный). Yandex: за́мок/замо́к, до́ма/дома́ ra 2 bản khác nhau, 0 file cụt. 5754 câu/276k ký tự ⇒ ~4 USD, ~130 MB. Mặt sau thẻ: `<script>` hay chết lặng trên AnkiMobile ⇒ chỉ dùng lệnh gắn thẳng vào nút (onclick).
### Kế hoạch (đã duyệt 18/10): 1 audio.py→Yandex · 2 ▶ từ tự làm · 3 tiếng câu (2 chỗ ghi) · 4 mẫu thẻ "· 1× ·" đáy (1/0,75/0,5), chỉ onclick · 5 thử 2 thẻ trên iPhone — CHỜ user · 6 vá toàn bộ TRƯỚC 31/10 (Yandex free tới đó) · 7 deploy + khoá lên VPS.
🔴 **CẤM deploy trước `--apply`:** bot VPS đẩy mẫu thẻ mới mỗi lần khởi động ⇒ deploy sớm = đụng Anki trước khi tải đủ. Sau `--apply` phải deploy NGAY, kẻo bot cũ đẩy mẫu cũ đè lại.
