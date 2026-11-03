# 🎯 VIỆC ĐANG LÀM
> Phiếu bị GHI ĐÈ ở việc kế tiếp. Xong việc thì để trống, chừa đúng dòng tiêu đề.

**03/11/2026 — NGHIÊN CỨU XONG, CHỜ USER CHỐT (chưa qua cửa `ycau`, chưa viết code).**
Báo cáo đầy đủ: https://claude.ai/artifact/RJ3QZHRqnYXexXnXnZiskY

1. **Câu ví dụ điền từ (cloze).** Đo 1 794 thẻ `RU_Word` / 5 382 câu: `span.hl` đánh dấu sẵn chỗ từ ở
   99,3% câu; 50,5% câu là dạng từ điển, 45,2% là dạng chia CÓ trong `GrammarJSON` của chính thẻ,
   **3,7% (197 câu) AI dùng từ khác** (`писать→написал`, `стол→столик`) ⇒ phải lọc: chỉ nhận câu có
   chữ `hl` nằm trong bảng chia. 1 781 thẻ còn ≥1 câu. Đề xuất: gõ DẠNG TỪ ĐIỂN (giữ `{{type:WordClean}}`),
   field mới `ClozeHTML` do Python dựng (⇒ full sync 1 lần), mặt sau tô dạng thật + nhãn dạng.
2. **Chấm phát âm.** Azure có `ru-RU` nhưng prosody (trọng âm) CHỈ `en-US`, ru chỉ có điểm từng âm
   không tên âm. Đề xuất: BƯỚC 0 thử 10–15 từ đọc đúng vs cố ý sai trọng âm bằng script tạm; điểm
   tụt rõ mới làm lệnh bot Telegram nhận voice (OGG 48 kHz → cần ffmpeg đổi 16 kHz).

Chờ user trả lời 3 câu (mục cuối báo cáo): A/B dạng gõ · mặt trước giữ nghĩa+badge hay không ·
Azure thử ngay hay để sau.
