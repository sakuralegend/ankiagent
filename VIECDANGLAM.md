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
Cùng đề (lời dặn MỚI) giao cho subagent Claude: **Haiku 24/24, Sonnet 24/24** qua cổng. Opus đọc tay:
Sonnet 0 lỗi; Haiku 1 lỗi nhỏ (`связь то пропадает`) + 1 câu lấn cấn (`Пиши мой номер`); Gemini flash
2 lỗi nghĩa, lite 1 thẻ méo + 1 câu gượng. Giá API ước/1 000 từ: Haiku 5.5 ~1 USD, Sonnet 5.5 ~10–20 USD;
chạy subagent trong Claude Code thì không tốn API (ăn vào hạn mức gói). Mẫu nhỏ (8 từ) — đủ để chọn
hướng, chưa đủ để kết luận Haiku ≈ Sonnet.
**User hỏi: bot gọi Claude Code đã cài trên VPS (ăn hạn mức gói, không cần API)?** ĐƯỢC về kỹ thuật:
`claude -p … --model sonnet --system-prompt-file … --tools "" --no-session-persistence --output-format json
--json-schema <_KHUON_THE>` ⇒ ra thẳng `structured_output` đúng khuôn. Đo trên laptop 1 từ: Sonnet 9,4s
(~8K token vào, 520 ra), Haiku 13,3s (1 539 ra) — Sonnet NHANH HƠN và gọn hơn. VPS: CLI 2.1.282 có cài
nhưng **CHƯA ĐĂNG NHẬP** (khởi động không thôi đã 7,5s); máy 1 CPU, RAM trống ~780 MB. Đăng nhập = user
chạy `claude setup-token` (token dài hạn, cần gói) rồi đưa vào `.env` VPS `CLAUDE_CODE_OAUTH_TOKEN`.
Rủi ro phải chặn: CLI tự cập nhật đổi cờ / token hết hạn / hết hạn mức ⇒ bot PHẢI rơi về Gemini + báo.
**Chạy thật 5 từ trên VPS (Sonnet, 03/11):** 10,9–19,3 s/từ, TB ~15 s. Mã user đưa CHƯA lưu vào `.env`
VPS (bộ phân loại tự động chặn ghi mã lên máy chủ ⇒ lúc thi hành để USER tự dán hoặc user cấp quyền).
Hai bẫy: (1) danh từ ⇒ Sonnet ghi `"pos": n` thiếu ngoặc kép, `--json-schema` thử 5 lần rồi chết
(~40 s), enum cũng không cứu ⇒ đường Claude KHÔNG hỏi `pos` (hoặc hỏi chữ đầy đủ "noun" rồi đổi mã);
(2) `сын` câu đúng nhưng QUÊN `<hl>` ⇒ cổng phải bắt + gọi lại. Kết quả: scratchpad `kq_haiku.json`/`kq_sonnet.json` (tạm).
Thẻ mẫu user đang xem: https://claude.ai/artifact/RKBTrNUqH7c1rBUfMQgR4Q (dựng từ 3 thẻ thật bằng
script tạm, không ghi Anki). Duyệt mẫu xong ⇒ `kehoach`.
