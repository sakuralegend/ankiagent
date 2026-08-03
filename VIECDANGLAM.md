# 🎯 VIỆC ĐANG LÀM
> Phiếu này bị GHI ĐÈ ở việc kế tiếp. Xong việc thì xoá nội dung, để lại đúng dòng tiêu đề.

**Phiên 03/08 (chiều): chạy 47 TỪ MỚI user thêm sáng nay.**

`moi --apply` gom cả 47 vào một lô `k62` (vượt trần 22) ⇒ luồng chính chia tay theo **chủ đề lấy
từ tag Anki**, không tự đặt trục ngôn ngữ (bài học k59: trục đặt bằng hình thức chỉ đúng 3/13):

| Lô | Từ | Nhóm |
|---|---|---|
| `k62` | 16 | danh từ đồ ăn / quần áo / đồ vật trong nhà |
| `k63` | 16 | tính từ phẩm chất, trạng từ, hư từ |
| `k64` | 15 | danh từ thiên nhiên / người / khái niệm + `ходить` |

Cả ba đang chạy song song, mỗi lô một agent context trắng. Luồng chính **không soạn chữ nào**.

🔴 Đã quét `vacham` trên cả 1023 thẻ TRƯỚC khi giao và **gửi kèm danh sách va chạm vào lời nhắn**
(k62: 0 · k63: **7** · k64: **5**) — đây là lần đầu làm bước này trước thay vì sau; bài học k30 là
lô mới dễ đẻ đề bài trùng với một hệ thống đã nằm trong kho mà agent không nhìn thấy.

**Còn phải làm khi agent báo xong (từng lô một):** `soat` → `dodai` → ghi 1 dòng `dolo.tsv` →
`xong kNN` → `nap --apply` (đối chiếu số note với số từ) → commit theo đường dẫn cụ thể
(**đừng `git add -A`**, có lô chạy song song).
