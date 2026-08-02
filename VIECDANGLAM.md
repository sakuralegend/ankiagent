# 🎯 VIỆC ĐANG LÀM — hai việc user ĐÃ DUYỆT 02/08/2026, làm ĐẦU phiên sau
> Phiếu này bị GHI ĐÈ ở việc kế tiếp. Xong việc thì xoá nội dung, để lại đúng dòng tiêu đề.

Làm hai việc này **trước** khi mở lô mới (lô kế tiếp là `k22`). Cả hai đã hỏi trắc nghiệm và
user đã chọn — **không hỏi lại**.

### 1. Tách nghĩa hai thẻ bị gộp sai — user chọn "giữ 1 thẻ mỗi từ"

Hai lỗi dữ liệu treo từ phiên 30/07, nay đã có hướng:

| Từ | Đang sai thế nào |
|---|---|
| `есть` | `PoS=oth`, nghĩa `"có, ăn"` — gộp **hai động từ khác hẳn nhau**; bảng chia gắn vào thẻ chỉ thuộc nghĩa «ăn» |
| `слу́шать` | nghĩa gộp luôn `слы́шать` (nghe chủ động vs nghe thấy) |

**Cách làm user đã chọn:** sửa dòng `Vietnamese` cho rõ nghĩa nào là chính, **KHÔNG đẻ thẻ mới**,
không đụng cấu trúc bộ sưu tập. Lô k19 đã ghi chú tách nghĩa ngay trên mặt thẻ `есть` rồi — việc
còn lại là dòng đề bài. ⚠️ Nhớ `слу́шать` chưa được lô nào chạm, phải kiểm cả thẻ `слы́шать`.

### 2. Dựng cửa soát dữ liệu ngữ pháp — user chọn "làm ngay đầu phiên sau"

Nợ đã ghi ở `SONO.md` (mục 02/08). Phiên này bắt được `кеды` bị nguồn **đảo cách 5 với cách 6**
mà `soat`/`dodai` mù hoàn toàn — chúng chỉ đo phần agent VIẾT, không đo bảng máy NỐI vào lúc `nap`.

Phép quét đã dùng và đã chạy thật trên 976 thẻ (ra đúng 2 chỗ, cả hai của `кеды`):
đuôi cách 5 tiếng Nga không bao giờ là `-е`/`-и`/`-ах`; đuôi cách 6 không bao giờ là
`-ом`/`-ем`/`-ами`. Lệch cả hai chiều cùng lúc ⇒ đảo thật, không phải biến thể.

**Gắn vào đâu:** đọc `GrammarJSON`, chạy offline, không cần Anki mở. Cân nhắc `congcu.py soat`
(cùng chỗ agent đã chạy sẵn) thay vì đẻ file mới — QD-12 cấm đẻ file khi file có sẵn chứa được.
🔴 Và **viết một test cho nó** (L3): dựng một `GrammarJSON` giả bị đảo, kỳ vọng cửa báo ĐỎ.
