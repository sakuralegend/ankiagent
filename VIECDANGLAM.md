# 🎯 VIỆC ĐANG LÀM
> Phiếu bị GHI ĐÈ ở việc kế tiếp. Xong việc thì để trống, chừa đúng dòng tiêu đề.

## 🔊 Giọng Yandex alena cho từ + câu ví dụ, thêm nút chỉnh tốc độ

**Một câu:** mọi thẻ (cũ + bot thêm mới) đọc từ và 3 câu ví dụ bằng Yandex alena, đúng trọng âm; khi chủ động muốn thì nghe chậm lại được.
**User đã chốt:** alena 1× · thay TOÀN BỘ tiếng từ (kể cả Shtooka) · câu ví dụ BẤM mới phát (▶ mờ cuối câu) · lật thẻ: từ TỰ PHÁT 1×, không theo nút tốc độ · nút tốc độ = chữ mờ ĐÁY thẻ, chạm 1× → 0,75× → 0,5×, áp cho mọi lần BẤM ▶, sang thẻ mới về 1× · trọng âm trong câu để Yandex đoán HẾT (90% từ chính không dấu; tra bảng thẻ phủ 94% — user không làm) · TẢI ĐỦ rồi MỚI ghi Anki.
**Coi là XONG khi:** iPhone: lật thẻ nghe согла́сный đủ âm; chạm "1×" → "0,75×" rồi bấm ▶ từ/câu thì đọc chậm; sang thẻ khác lại 1×.
**CỐ Ý KHÔNG làm:** Azure (đã thử, bác — đầu audio.py) · HyperTTS · tự phát câu · thanh trượt · nhớ tốc độ giữa các thẻ.
**Đã đo:** OpenRussian hỏng cả máy đọc mới (27 file cụt) lẫn Shtooka. Mặt sau thẻ: `<script>` hay chết lặng trên AnkiMobile ⇒ chỉ onclick.
### Tiến độ 19/10: ✅ tải đủ 7725 file (187 MB, 0 hỏng, 0 cụt) · ✅ ghi thử 2 thẻ (согласный 1792085276442, дом 1783401951202) — CHỜ user kiểm iPhone · ⏳ `fix_audio.py --apply` cả kho TRƯỚC 31/10 (Yandex free tới đó) · ⏳ deploy NGAY sau đó (bot VPS cũ đẩy mẫu thẻ cũ mỗi lần khởi động) + chép YANDEX_TTS_API_KEY lên .env VPS.
