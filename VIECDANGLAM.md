# 🎯 VIỆC ĐANG LÀM
> Phiếu này bị GHI ĐÈ ở việc kế tiếp. Xong việc thì xoá nội dung, để lại đúng dòng tiêu đề.

## 📐 TÁCH `soatkientruc.py` THÀNH GÓI `soat/` — user đã chốt 03/08, chờ thi hành

**Vì sao gấp:** file đang **700/700 dòng** ⇒ mọi cửa soát mới đều đâm tường. Làm việc này TRƯỚC,
rồi mới tới lô từ.

⚠️ **Đính chính một hiểu sai:** QD-02 **KHÔNG** cấm tách — nó nói `soatkientruc.py` là điểm vào ở
gốc, dùng stdlib, không import module dự án. Nó không hề nói *"mọi cửa phải nằm trong file đó"*.
Ràng buộc thật chỉ là **trần 700 trong `soat_nguong.json`**. Tách gói giữ nguyên **cả hai** lý do
gốc của QD-02 (vẫn gõ `python soatkientruc.py`, vẫn không import module dự án).

**Chẻ theo NHÓM VIỆC, không theo số dòng:**

| File | Nội dung | ~dòng |
|---|---|---|
| `soat/khung.py` | `GOC` · `PhatHien` · đọc cây AST · liệt kê file | 90 |
| `soat/cua_code.py` | S1–S8 — cấu trúc code | 220 |
| `soat/cua_quytrinh.py` | S9 · S11 — commit message, hook | 145 |
| `soat/cua_nguong.py` | `_nguong` · S10 · S12–S14 — ngưỡng & tài liệu | 180 |
| `soatkientruc.py` | điểm vào + bảng đăng ký cửa + ratchet baseline | **~90** |

### 🔴 CÁI BẪY — đọc trước khi gõ dòng nào

62 test hiện gán `sk.GOC = thư_mục_tạm`. Cửa chuyển sang `soat/` sẽ đọc `khung.GOC`, **không đọc
`sk.GOC` nữa** ⇒ test trỏ vào repo THẬT thay vì repo giả, không thấy vi phạm nào nên **xanh hết mà
không kiểm gì cả**. Lưới an toàn thành lưới giả, im lặng. Đúng loại hỏng repo này sợ nhất.

### Nghiệm thu — test XANH không chứng minh gì, phải chứng minh test biết ĐỎ

1. Chụp toàn bộ đầu ra `python soatkientruc.py` **trước** khi sửa → sau khi sửa diff phải **= 0**.
2. **Phá từng đích rồi xác nhận test tương ứng ĐỎ**: thêm dòng thứ 701 · trỏ ngưỡng vào file ma ·
   gỡ ngòi `raise SystemExit` của lô cũ · thêm file `.py` lạ ở gốc. Test không đỏ ⇒ **HOÀN TÁC**.
3. Ba cửa: `soatkientruc.py` · `import bot, main` · 62 test.

**Lùi lại:** `git revert <commit>` — không đụng thẻ, dữ liệu, bot. Sạch tuyệt đối.
**Ghi `QD-22`** (tách gói, nới chữ "một file" của QD-02) + cập nhật `da_ghi_no` trong
`soat_nguong.json` cho các file mới.

**Xong rồi mới tới:** lô `k32`(12) · `k33`(21) · `k34`(20) = 53 từ ≈ 80% hạn mức.
