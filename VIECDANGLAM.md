# 🎯 VIỆC ĐANG LÀM
> Phiếu bị GHI ĐÈ ở việc kế tiếp. Xong việc thì để trống, chừa đúng dòng tiêu đề.

## 🔊 Chuyển TOÀN BỘ phát âm sang giọng máy trả phí đọc đúng dấu nhấn

**Một câu:** mọi thẻ (cũ + bot thêm mới) có tiếng máy (hãng thắng bài nghe) đọc đúng trọng âm, đủ âm tiết.
**User đã chốt 18/10:** chọn giọng bằng BÀI NGHE Yandex SpeechKit (`+` trước nguyên âm nhấn) vs Azure (chỉ có IPA) — chờ user tạo 2 tài khoản, khoá vào `.env` · có phí cũng được, cần rõ từng âm · tự viết script (không HyperTTS) · thay TOÀN BỘ ~2042 file, kể cả bản người Shtooka · 27 file cụt đầu để nguyên chờ giọng mới.
**Coi là XONG khi:** user nghe согла́сный · дома́ · за́мок đủ âm, đúng nhấn; bot thêm từ mới tự có giọng mới.
**CỐ Ý KHÔNG làm:** HyperTTS · đọc câu ví dụ · giữ song song OpenRussian làm phao.
**Đã đo:** không trùng "ĐÃ ĐO RỒI BÁC". OpenRussian hỏng cả hai phía: máy đọc kiểu MỚI 48 kHz (27/98 file tiếng bắt đầu ở 0,000 s) VÀ bản Shtooka của согласный (user nghe trên app thiếu âm đầu). Azure nhận dấu nhấn đơn giản hay không: CHƯA rõ. Thử cặp за́мок/замо́к, до́ма/дома́.
