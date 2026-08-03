# 🆕 Có gì mới — dành cho NGƯỜI DÙNG

> File **duy nhất trong repo viết cho bạn**, không phải cho người sửa code. Mọi file còn lại
> (`KIENTRUC.md`, `QUYETDINH.md`, `SONO.md`, `CACHLAM.md`, `CLAUDE.md`) là tài liệu kỹ thuật —
> bạn không cần đọc.
>
> **Luật viết file này — AI phải theo:**
> 1. Chỉ ghi thứ **bạn cảm nhận được**: bot có thêm nút gì, sửa lỗi bạn từng gặp, thẻ hiện khác đi.
>    Dọn code, đổi cấu trúc, thêm cửa soát… **không ghi** — bạn không thấy chúng.
> 2. Ngôn ngữ thường, **không thuật ngữ**. Mỗi mục một dòng, tối đa 5 mục/bản.
> 3. **Giữ 10 bản gần nhất, cũ hơn thì XOÁ.** Lịch sử đầy đủ đã có `git log` lo. File này mà dài
>    quá một màn hình là nó đi đúng đường `CHANGELOG.md` cũ — 200 KB không ai đọc.
> 4. Số hiệu: `vMAJOR.MINOR.PATCH` — **MAJOR** khi bạn phải tự làm gì đó (vd đồng bộ lại điện
>    thoại) · **MINOR** khi có tính năng mới · **PATCH** khi chỉ sửa lỗi.

---

## v1.0.2 — 03/08/2026

- 🔄 **Sửa 21 thẻ trong deck `0-quen` sáng nay bị lật sang mặt gõ.** Đêm qua máy chủ đã nâng chúng
  lên chặng gõ, nhưng sáng nay bạn học chúng trên thiết bị **chưa tải bản mới về**, nên khi đồng bộ
  thì thẻ bị kéo ngược về deck cũ mà cái nhãn "đã lên chặng gõ" thì còn nguyên — thành ra sai mặt.
  Nay 21 thẻ đã về đúng mặt làm quen, **tiến độ ôn sáng nay giữ nguyên**, bạn không phải làm gì.
  Đêm nay máy chủ sẽ tự nâng chúng lên chặng gõ như bình thường.
- 💡 **Mẹo tránh lặp lại: buổi sáng hãy để app Anki đồng bộ xong rồi mới bắt đầu học.** Nếu app đã
  mở sẵn từ tối hôm trước, nó không tự tải bản mới về.
- 📝 45 thẻ mới có ô Hướng dẫn: **số hàng chục/trăm/nghìn · số thứ tự · đơn vị đo**.

## v1.0.1 — 02/08/2026

- ⌨️ **Sửa 23 thẻ trong deck `1-go` hiện sai mặt: đã học xong phần làm quen mà vẫn không có ô gõ.**
  Nguyên nhân: đêm 31/07 bot trên máy chủ đã nâng chúng lên chặng GÕ, nhưng sáng hôm sau laptop
  chạy một đợt cập nhật hàng loạt khi chưa tải bản mới về, nên vô tình ghi đè ngược lại. Nay 23 thẻ
  đã về đúng mặt gõ, **lịch ôn giữ nguyên**, bạn không phải làm gì cả. Cũng đã chặn để lần sau
  không lặp lại: mọi đợt cập nhật hàng loạt buộc phải tải bản mới nhất về trước khi ghi.

## v1.0.0 — 31/07/2026

Mốc đầu tiên được đánh số. Từ hôm nay dự án có máy tự kiểm code trước mỗi lần cập nhật, nên
những thay đổi sau này ít có khả năng làm hỏng thứ đang chạy.

- 🔔 **Bot tự nhắn cho bạn nếu nó chết.** Trước đây bot ngừng chạy thì hoàn toàn im lặng, bạn chỉ
  biết khi nhắn mà không ai trả lời. Giờ có chuông báo riêng, không phụ thuộc bot. Bot sống lại
  cũng nhắn. Chết cả ngày cũng chỉ nhận **một** tin, không spam.
- 💾 **Sao lưu đã được kiểm chứng là khôi phục được thật.** Trước đây chỉ có bản sao lưu mà chưa ai
  thử phục hồi — nay đã thử: 950/950 thẻ về đúng. Các bước ghi trong `VPS_SETUP.md`.
- 🩹 **Sửa một lỗi có thể làm thẻ hiện sai giống từ.** Với vài danh từ chỉ người (kiểu `дя́дя` —
  chú/bác), máy có thể gắn nhãn giống cái trong khi đó là giống đực. Đã kiểm: **không thẻ nào của
  bạn đang bị sai**, lỗi được vá trước khi kịp xảy ra.
- ⚙️ **Cập nhật bot lên máy chủ không còn bị kẹt giữa chừng.** Trước đây có lần cập nhật thất bại
  mà vẫn báo "Xong!", khiến bot chạy bản cũ mà không ai biết.
