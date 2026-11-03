# 🎯 VIỆC ĐANG LÀM
> Phiếu bị GHI ĐÈ ở việc kế tiếp. Xong việc thì để trống, chừa đúng dòng tiêu đề.

## Chấm phát âm Azure — ĐANG LÀM (phiên khác)
Nút 🎤 trong thẻ (`git log --grep Azure`); đang thử thẻ dò micro `_THU_MICRO` — XOÁ nó + media `_thu_micro.js` `_micro.js` `_mic_v*.js` (bản nháp mới nhất = `_mic_v7.js`, chép ra trước khi xoá).
ĐANG LÀM (phiên làm sạch): câu điền từ. 🎨 THIẾT KẾ đã duyệt: https://claude.ai/artifact/RKBTrNUqH7c1rBUfMQgR4Q — phiên
Azure CŨNG sửa `front/back_template.html` + `card.css` ⇒ user merge 2 thiết kế TRƯỚC khi ai ghi mẫu thẻ vào Anki.
Báo cáo khả thi: https://claude.ai/artifact/RJ3QZHRqnYXexXnXnZiskY
Làm sạch câu ví dụ XONG 03/11 (`git log --grep QD-47`): 535/538 câu thay. CHỜ USER: thẻ `варенный` ghi sai
chữ (chuẩn `варёный`) — sửa chữ thẻ thì 3 câu Sonnet viết sẵn ở scratchpad dùng được; thẻ `весь` mang bảng chia
của danh từ cổ `весь`=làng (`весях`) ⇒ bảng chia trên thẻ SAI, cần cào lại đúng đại từ.

### Kế hoạch câu điền từ — phương án A (duyệt 03/11) — bước 1–2 XONG (`e0c136c`), chờ user gộp thiết kế
1. `vi_du.nhan_dang` (dạng → "cách 5, số ít") + `html_builder.dung_cloze`: chọn câu 2/3 (không câu 1 đang mở sẵn),
   dựng `ClozeHTML` = phần trước (chỗ trống + dịch Việt) + phần sau (đáp án đậm + nhãn); CSS ẩn phần không thuộc mặt.
2. Test + `scripts/_va_dien_cloze.py` (khan: 1 793/1 794). Nối `build_card_fields`+`anki_moitruong` CỐ Ý để bước 4.
3. Mẫu thẻ: CHỈ sửa `front/back_template.html` + `card.css` SAU KHI user gộp thiết kế với phiên Azure.
4. Triển khai ĐÚNG THỨ TỰ: kéo sync → thêm ô trên laptop → điền → user Upload laptop → user Download VPS (`vnc.bat`)
   → MỚI deploy (deploy trước ⇒ bot VPS tự `modelFieldAdd` ⇒ hai bên lệch schema) → `journalctl` → iPhone Download.
