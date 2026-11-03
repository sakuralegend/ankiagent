# 🎯 VIỆC ĐANG LÀM
> Phiếu bị GHI ĐÈ ở việc kế tiếp. Xong việc thì để trống, chừa đúng dòng tiêu đề.

## Câu điền từ — ĐANG LÀM (phiên làm sạch)
🎨 THIẾT KẾ đã duyệt: https://claude.ai/artifact/RKBTrNUqH7c1rBUfMQgR4Q · Nút 🎤 Azure XONG 03/11 (`git log --grep QD-49`):
hàng ▶︎🎤🎧 ĐÃ vào `back_template.html`+`card.css`+`mic.js` và đã ghi vào Anki ⇒ điền từ dựng TRÊN bản này.
Báo cáo khả thi: https://claude.ai/artifact/RJ3QZHRqnYXexXnXnZiskY
Làm sạch câu ví dụ XONG 03/11 (`git log --grep QD-47`): 535/538 câu thay. CHỜ USER: thẻ `варенный` ghi sai
chữ (chuẩn `варёный`) — sửa chữ thẻ thì 3 câu Sonnet viết sẵn ở scratchpad dùng được; thẻ `весь` mang bảng chia
của danh từ cổ `весь`=làng (`весях`) ⇒ bảng chia trên thẻ SAI, cần cào lại đúng đại từ.

### Kế hoạch câu điền từ — phương án A (duyệt 03/11) — bước 1–2 XONG (`e0c136c`)
1. `vi_du.nhan_dang` (dạng → "cách 5, số ít") + `html_builder.dung_cloze`: chọn câu 2/3 (không câu 1 đang mở sẵn),
   dựng `ClozeHTML` = phần trước (chỗ trống + dịch Việt) + phần sau (đáp án đậm + nhãn); CSS ẩn phần không thuộc mặt.
2. Test + `scripts/_va_dien_cloze.py` (khan: 1 793/1 794). Nối `build_card_fields`+`anki_moitruong` CỐ Ý để bước 4.
3. Mẫu thẻ: sửa `front/back_template.html` + `card.css` (giữ nguyên hàng ▶︎🎤🎧 của QD-49).
4. Triển khai ĐÚNG THỨ TỰ: kéo sync → thêm ô trên laptop → điền → user Upload laptop → user Download VPS (`vnc.bat`)
   → MỚI deploy (deploy trước ⇒ bot VPS tự `modelFieldAdd` ⇒ hai bên lệch schema) → `journalctl` → iPhone Download.
