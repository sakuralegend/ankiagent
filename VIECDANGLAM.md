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

**User CHỐT 03/11** (ghi tay trong báo cáo): (1) gõ DẠNG TỪ ĐIỂN · (2) giữ NGUYÊN mọi thứ ở hai mặt,
mặt trước chỉ THÊM câu trống (đặt dưới "Translate into Russian"), mặt sau thêm câu lên ĐẦU thẻ, tô
đậm dạng đã chia (+ nhãn dạng) · (3) Azure: thử ngay — chờ user mở tài khoản, khoá để vào `.env`.
**User duyệt thẻ mẫu, nhưng đòi LÀM SẠCH CÂU VÍ DỤ TRƯỚC (03/11).** Đo: ~300 câu máy bắt được
(mất từ do thẻ `<hl>` méo bị lột · dùng cặp thể/từ giảm nhẹ/từ cùng gốc · đánh dấu sai chữ) + ước
~4% câu sai ngữ pháp/nghĩa máy KHÔNG bắt được. Thử 8 từ lỗi × 4 cấu hình (cổng = chữ `hl` có trong
bảng chia): lite+lời dặn cũ 21/24 · lite+MỚI 23/24 · flash+cũ **20/24** · flash+MỚI 24/24 ⇒ thủ phạm
chính là LỜI DẶN (không cho danh sách dạng, không cấm cặp thể — model to còn hay dùng cặp thể hơn vì
tự nhiên hơn), rồi tới việc KHÔNG CÓ CỔNG. Ép thể chưa hoàn thành mà không dặn "chọn tình huống hợp
thể đó" ⇒ câu gượng (`Можно брать эту книжку…`). Lỗi nghĩa (`Сними очки, а то слишком ярко`) cả
flash cũng mắc ⇒ chỉ Opus/người bắt được. Kho câu người viết (Tatoeba = RawExamples, НКРЯ, OpenSubtitles)
đều không dán thẳng được: vẫn cần model chọn + dịch Việt + cổng.
Thẻ mẫu user đang xem: https://claude.ai/artifact/RKBTrNUqH7c1rBUfMQgR4Q (dựng từ 3 thẻ thật bằng
script tạm, không ghi Anki). Duyệt mẫu xong ⇒ `kehoach`.
