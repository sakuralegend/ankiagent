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
