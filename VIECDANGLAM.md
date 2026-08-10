# 🎯 VIỆC ĐANG LÀM

## Thẻ CHI PHỐI — lô 1 giới từ. 17 thẻ ĐÃ VÀO ANKI 10/08, chờ user sync tay
Trước: giới từ **dạng GỐC** (`в`, user tự nhớ viết `во`) + từ nguyên thể **có dấu nhấn** + 1 dòng Việt. Sau: đáp án · huy hiệu cách · dòng đối chiếu. KHÔNG giải thích — "sai thì bấm Again".
- 🔴 Đáp án + dòng đối chiếu **MÁY SINH lúc nạp** từ `GrammarJSON`; người soạn chỉ viết 4 cột trong `data/chi_phoi.tsv`. Cột 1 viết dạng SẼ HIỆN (`во`/`со`) — máy đoán biến thể là đẻ tiếng Nga SAI mà báo XANH (dính thật 10/08, nay có test canh).
- 🔴 Dòng Việt mơ hồ = hỏng IM LẶNG. `chi_phoi.soat()` bắt 4 loại lỗi; ca "khác chữ mà cùng nghĩa" thì máy chịu ⇒ **user phải đọc từng dòng trước khi nạp**.
- 🔴 1 thẻ = 1 CÔNG DỤNG mà chọn sai thì câu sai — đếm RIÊNG từng từ, ra 3–7, CẤM chia đều. Ô `HuongDan` cũ chỉ là ĐÁP ÁN, **CẤM chép văn**.
### 🔴 VIỆC KẾ TIẾP — CẦN TAY USER, chưa ai làm được hộ
Đã tạo model `RU_ChiPhoi` ⇒ Anki đòi **full sync**. Backup sẵn ở `backups/2026-08-10_2325` (60,7 MB, 0 lỗi).
1. LAPTOP: `Tools → Sync` → chọn **UPLOAD**.  2. VPS: `vnc.bat` → Sync → chọn **DOWNLOAD**.  3. Kiểm `journalctl -u anki-bot -n 50`.
Chọn sai chiều là mất dữ liệu và KHÔNG có gì kêu (`KIENTRUC.md` §6). Đừng gọi `trigger_sync()` — AnkiConnect không chọn được chiều.
### Còn lại của lô 1
Sync xong: user ôn thật 3–5 ngày (dòng Việt chỉ lộ mơ hồ khi dùng), rồi soạn nốt **11 giới từ** vào `data/chi_phoi.tsv` và chạy `python -m grammar_forms.chi_phoi --apply`.
Chưa làm: +5 dòng cảnh báo vào `congcu.py tiep` (từ mới có `usage` khai cách ⇒ in nhắc). Lô sau: 49 động từ (28 cần giới từ) + số/lượng; tính từ KHÔNG làm (hợp dạng ≠ chi phối).
