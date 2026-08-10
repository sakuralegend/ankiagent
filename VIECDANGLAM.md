# 🎯 VIỆC ĐANG LÀM

## Thẻ CHI PHỐI — lô 1: 14 giới từ ≈ 85 thẻ (deck `GRAMMAR::chi phối::…` + nhãn `cach::N`)
Trước: giới từ **dạng GỐC** (`в`, user tự nhớ viết `во`) + từ nguyên thể + 1 dòng Việt. Sau: đáp án · huy hiệu cách · dòng đối chiếu gom theo DANH TỪ. KHÔNG giải thích — user chốt "sai thì bấm Again".
- 🔴 Đáp án + dòng đối chiếu **MÁY SINH lúc nạp** từ `GrammarJSON`, CẤM gõ tay. Nhưng cột 1 của `data/chi_phoi.tsv` phải viết dạng SẼ HIỆN (`во`/`со`/`об`/`ко`): để máy đoán biến thể là đẻ tiếng Nga SAI mà vẫn báo XANH — đã dính thật lúc chạy thử (`в вто́рник` ❌).
- 🔴 Dòng Việt mơ hồ = hỏng IM LẶNG (gõ đúng bị chấm sai → Again → học ngược). Cửa soát bắt được: cùng danh từ + cùng cách, hoặc dòng Việt giống hệt. "Khác chữ mà cùng nghĩa" thì máy chịu ⇒ user phải đọc.
- 🔴 1 thẻ = 1 CÔNG DỤNG mà chọn sai thì câu sai — đếm RIÊNG từng từ, ra 3–7, CẤM chia đều (`к` 1 cách mà cần 6 thẻ). Ô `HuongDan` cũ chỉ là ĐÁP ÁN, **CẤM chép văn**.
### Kế hoạch (user duyệt 10/08) — bước 1 XONG
1. ✅ `data/chi_phoi.tsv` — 17 thẻ (в·на·с). 17/17 đáp án sinh được, 0 cặp đề bài đụng nhau.
2. `grammar_forms/`: thêm `chi_phoi.py` + 3 template `chiphoi_*`; sửa `config.py` · `cards.py` (cửa AnkiConnect DUY NHẤT của mảng) · `setup.py`. Cửa soát "đáp án lệch bảng chia" xây cùng commit, VÌ SAO chép vào lời báo lỗi của nó.
3. DỪNG gọi user: full sync 1 lần do model mới — Upload (laptop) → Download (VPS). Theo L4: đứng riêng một mình, backup `.apkg` trước, kiểm `journalctl -u anki-bot` sau.
4. Nạp 17 thẻ, user ôn thật 3–5 ngày rồi mới soạn nốt 11 giới từ — dòng Việt chỉ lộ mơ hồ khi dùng thật.
5. +5 dòng vào `congcu.py tiep`: từ mới có `usage` khai cách ⇒ in một dòng nhắc. KHÔNG dựng dòng chảy thứ hai — giới từ là tập ĐÓNG, quét xong là xong.
