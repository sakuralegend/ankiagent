# 🎯 VIỆC ĐANG LÀM
> Phiếu bị GHI ĐÈ ở việc kế tiếp. Xong việc thì để trống, chừa đúng dòng tiêu đề.

## Làm sạch câu ví dụ + đổi cách bot đặt câu — ĐANG LÀM (duyệt 03/11/2026)
Số đo đủ: `git log -p VIECDANGLAM.md` (03/11). Gốc lỗi = lời dặn bắt AI làm 6 việc + KHÔNG cổng, không
phải model nhỏ: lời dặn gọn (máy chọn dạng, máy đánh dấu) ⇒ Gemini Lite 39/39 (1,7 s), Sonnet 39/39.
User chốt: bot giữ Gemini Lite · làm sạch thẻ cũ bằng Sonnet `claude -p` trên laptop (Gemini 500 lượt/ngày).
Xếp hàng sau: câu điền từ (mẫu đã duyệt: gõ dạng từ điển, field `ClozeHTML`, full sync) → chấm phát âm
Azure. Báo cáo: https://claude.ai/artifact/RJ3QZHRqnYXexXnXnZiskY

### Kế hoạch (đã duyệt 03/11) — bước 1–2 XONG code + test, chờ deploy + user thử 2–3 từ
1. `anki_tools/vi_du.py` MỚI: máy chọn 3 dạng/loại từ, lời dặn gọn, cổng, máy đánh dấu. Thay hẳn
   `call_claude_ai`/`_freestyle`/prompt cũ trong `ai_client.py` (xoá, không để song song).
2. `html_builder.build_examples_html` + `anki_the.build_card_fields`: truyền `GrammarJSON` vào; topic/pos
   gọi `call_claude_topic`/`call_claude_pos` có sẵn. Test mới cho cổng + bộ chọn dạng. Deploy bot.
3. Việc ĐỨNG RIÊNG (L4): `scripts/_va_lam_sach_vi_du.py` — máy soát 5 382 câu → Sonnet chấm câu còn lại
   → Sonnet viết lại câu hỏng → cổng → backup + kéo sync → ghi `--apply` + tiếng Yandex câu mới.
