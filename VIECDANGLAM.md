# 🎯 VIỆC ĐANG LÀM

## Thẻ CHI PHỐI — lô 1: 17 thẻ giới từ ĐÃ CHẠY THẬT (laptop + VPS) 10/08
Trước: giới từ **dạng GỐC** (`в`, user tự nhớ viết `во`) + từ nguyên thể **có dấu nhấn** + 1 dòng Việt. Sau: đáp án · huy hiệu cách · dòng đối chiếu. KHÔNG giải thích — "sai thì bấm Again".
- 🔴 Đáp án + dòng đối chiếu **MÁY SINH lúc nạp** từ `GrammarJSON`; người soạn chỉ viết 4 cột trong `data/chi_phoi.tsv`. Cột 1 viết dạng SẼ HIỆN (`во`/`со`) — máy đoán biến thể là đẻ tiếng Nga SAI mà báo XANH (dính thật 10/08, nay có test canh).
- 🔴 Dòng Việt mơ hồ = hỏng IM LẶNG. `chi_phoi.soat()` bắt 4 loại lỗi; ca "khác chữ mà cùng nghĩa" thì máy chịu ⇒ **user phải đọc từng dòng trước khi nạp**.
- 🔴 1 thẻ = 1 CÔNG DỤNG mà chọn sai thì câu sai — đếm RIÊNG từng từ, ra 3–7, CẤM chia đều. Ô `HuongDan` cũ chỉ là ĐÁP ÁN, **CẤM chép văn**.
### Việc kế tiếp — CHỜ USER ÔN THẬT, đừng soạn tiếp vội
User ôn 17 thẻ **3–5 ngày** rồi mới soạn nốt **11 giới từ**: dòng Việt chỉ lộ mơ hồ lúc ngập ngừng trước thẻ, không lộ lúc ngồi duyệt. Thêm dòng vào `data/chi_phoi.tsv` rồi `python -m grammar_forms.chi_phoi --apply` (sửa dòng cũ cũng được — thẻ dựng lại mà giữ tiến trình học).
Chưa làm: +5 dòng cảnh báo vào `congcu.py tiep` (từ mới có `usage` khai cách ⇒ in nhắc). Lô sau: 49 động từ (28 cần giới từ, mặt trước thành 3 ô) + số/lượng; tính từ KHÔNG làm (hợp dạng ≠ chi phối).
### Nợ nhỏ phát hiện 10/08 — chưa trả
`.env` thiếu `ANKI_COLLECTION` ⇒ cửa soát "đã gửi hết lên AnkiWeb chưa" (QD-34, dựng sau vụ 4 thẻ kẹt 7 tiếng) **im từ trước tới giờ**. Đã khai vào `.env`, nhưng chạy lúc Anki đang mở vẫn `database is locked` ⇒ chỉ đọc được khi đóng Anki. Chưa rõ trên VPS có bị vậy không.
