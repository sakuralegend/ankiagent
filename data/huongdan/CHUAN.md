# 📏 SỔ CHUẨN — mỗi số hiệu là một bộ tiêu chuẩn, ghi đủ để đối chiếu về sau

> **Chuẩn hiện hành: `v3`** (chốt 29/07/2026).
> Thẻ đạt chuẩn mang tag **`chuan::3`** — tra thẳng trong app Anki: `tag:chuan::3`.

Số hiệu nằm ở `CHUAN_V` trong `data/huongdan/kho/congcu.py`, **file này là phần định nghĩa
của nó**. Sửa một chỗ mà quên chỗ kia là mất hết tác dụng.

---

## 🔴 Vì sao phải có số hiệu, và vì sao phải có file này

Trước 29/07 chỉ có nhãn `dat` trong `hangdoi.json`, ghi *"thẻ này đạt"* mà **không ghi đạt theo
chuẩn nào**. Chuẩn đổi bên dưới thì nhãn **hết hạn mà không ai biết** — đo lại 29/07 thì **7/75**
thẻ mang nhãn đó đã vỡ trần, và cả một phiên bị loạn vì tưởng chúng còn tốt.

Hai thứ chữa hai lỗ khác nhau, **phải có cả hai**:

| | Chữa gì |
|---|---|
| **Số hiệu** (`chuan::3` trên tag thẻ) | "Thẻ này soạn theo chuẩn nào" — nằm trên chính thẻ nên không lệch được với bộ sưu tập |
| **File này** | "Chuẩn đó đòi những gì" — không có nó thì số hiệu chỉ là con số vô nghĩa sau vài tháng |

⚠️ Dùng **tag** chứ không phải field mới: thêm field là **schema mod** ⇒ Anki đòi full sync, mà
mỗi lần như vậy VPS kẹt im lặng. Tag sync thường, lại tra được ngay trong app.

## 🔧 Quy trình ĐỔI CHUẨN — làm đủ ba bước

1. Thêm một mục `## v<N+1>` vào file này, ghi **đủ tiêu chuẩn** (không chỉ ghi phần thay đổi —
   người đọc sau này cần đọc một mục là biết trọn bộ, không phải ghép từ nhiều mục).
2. Tăng `CHUAN_V` trong `congcu.py`.
3. Xong. **Không phải đụng thẻ nào**: mọi thẻ cũ tự thành `chuan::<N>` = "đạt chuẩn CŨ", và
   `python data/huongdan/dochuan.py` tự xếp chúng vào diện phải soạn lại.

`congcu.py nap` **gỡ mọi `chuan::*` cũ rồi mới gắn số hiện hành**, nên một thẻ luôn mang đúng
một số hiệu — câu hỏi "thẻ này đạt chuẩn nào" luôn có đáp án duy nhất.

---

## v3 — chuẩn HIỆN HÀNH (chốt 29/07/2026)

Một thẻ đạt `chuan::3` khi thoả **tất cả** các điều dưới đây.

### A. Ba con số cứng

| # | Tiêu chuẩn | Kiểm bằng |
|---|---|---|
| 1 | **Vừa MỘT màn hình iPhone** — cao ≤ **700px**, nhắm < 600px (máy thật: iPhone 16 Pro Max 440×956). Bảng chia gấp trong `<details>` **không tính** vào chiều cao. | `congcu.py dodai kNN` → `QUA 1 MAN HINH (700px): 0` |
| 2 | **Tối đa 2 ô đỏ** (`hd-warn`) mỗi thẻ | `congcu.py dodai kNN` → `QUA 2 O DO: 0` |
| 3 | **Mặc định KHÔNG có khối hệ thống dùng chung**. Cần lắm thì trải đủ ở đúng một thẻ của lô, thẻ khác dẫn chiếu một dòng. | `congcu.py dodai kNN` → `khoi dung chung: 0%` |

🔴 **Đừng canh theo BYTE** — byte là đại lượng sai: một bảng 6 dòng và một đoạn văn cùng số byte
chiếm chiều cao khác nhau tới ba lần.

### B. Cấu trúc nội dung

| Mục | Lớp CSS | Bắt buộc? |
|---|---|---|
| **Chẻ từ** | `hd-sec` + `hd-row` | ✅ (từ gốc trơn thì nói thẳng "không chẻ được", đừng bịa) |
| **Cách nhớ** | `hd-why` | ✅ |
| **Họ hàng** | `hd-sec` + `hd-fam` | ⬜ **Được phép vắng** — xem D |

### C. 🆕 ĐIỂM MỚI CỦA v3 — câu chú ý cho bảng chia bất thường

**Từ nào `congcu.py tiep` in ra khối `BAT THUONG` thì BẮT BUỘC có một câu chú ý** đặt phía trên
bảng chia. Tiêu chí user nêu: *"đọc câu đó là hiểu toàn bộ bảng"*.

- **364/950 từ (38%) rơi vào diện này** — đo 29/07.
- Máy chỉ **trỏ chỗ** (`grammar.analyze()` báo thân từ đổi / nguyên âm chạy / trọng âm dịch /
  biến âm giữa các ngôi / dạng ngắn bất thường…). Câu chữ là người soạn viết —
  **đừng chép nguyên văn** mô tả thô của máy.
- Từ **không** có khối `BAT THUONG` thì không cần câu này.

### D. Mục "Họ hàng" — được phép vắng, agent quyết định

Từ thật sự không có họ hàng (**gốc trơn, hư từ, từ mượn đứng một mình** như `бассе́йн` ← Pháp
`bassin`) thì **bỏ hẳn mục đó**. `congcu.py soat` chỉ **đếm và in**, không chặn.

🔴 Nhưng vắng phải là **lựa chọn có ý thức**, không phải chỗ quên. Và **chỉ viết khi chắc chắn
cùng gốc** — hai lỗi đã bắt được: `о́блако`↔`во́лос`, `целова́ть`↔`цель` (nhìn giống gốc mà không
cùng gốc). Không có dữ liệu máy cho mục này, và đó là chủ ý (xem README §2).

### E. Field `Vietnamese` — đề bài của deck `1-go`

User **gõ từ Nga** từ dòng này, nên nó phải sát tới mức **chỉ có MỘT đáp án đúng**.
Động từ **luôn ghi rõ thể**. 🔴 **Đừng ghi từ loại/giống** — mặt đề bài đã in sẵn badge
(`PoS`, `GenderBadge`, `AspectBadge`); ngoại lệ là từ có `PoS = oth` thì badge vô dụng.

### F. Ba cửa soát phải sạch

`congcu.py soat kNN` báo `(khong co)` ở **cả ba** mục đầu:
cấu trúc HTML · từ Nga in đậm thiếu dấu trọng âm · trọng âm lệch so với từ điển.
Rồi **đọc bằng mắt** danh sách `PHAI DOC BANG MAT` — đó là cửa **duy nhất** bắt được "lời giải
thích sai", và là chỗ duy nhất đỡ được lô động từ/tính từ (`nouns.csv` chỉ có danh từ).

---

## v2 — §2b NGẮN GỌN (chốt 28/07/2026) · ĐÃ THAY

Giống v3 ở mục **A, B, E, F**, **thiếu mục C** (chưa có khối `BAT THUONG` nên không ai viết câu
chú ý), và mục **D ngược lại**: `.hd-fam` là **bắt buộc**, thiếu bị `soat` coi là lỗi cấu trúc.

📌 Không thẻ nào được gắn `chuan::2` — dấu chỉ có từ v3 trở đi. Các thẻ soạn theo v2
(k13, k51–k54 — 78 từ) nằm ở diện **"chưa có dấu"**.

## v1 — chuẩn DÀI (trước 28/07/2026) · ĐÃ BỎ

Nhắm **6–10 KB mỗi thẻ**, không đếm ô đỏ, không đếm khối lặp. User học hết rồi kết luận ngược:
*"tham quá khiến thẻ dài tôi đọc xong không nhớ gì"*. Đo lại thì k04 trung bình **13 403 byte,
10,5 ô đỏ, 80% là khối lặp** — đỉnh `реплика` cao **6 335px = 9 màn hình**.

📌 Không thẻ nào được gắn `chuan::1`.

---

## 📊 Ảnh chụp 29/07/2026

| | Thẻ | |
|---|---|---|
| `chuan::3` | **38** | **4,0%** — k14 + k48 |
| chưa có dấu | 912 | 96,0% |

Đo lại bất cứ lúc nào: `python data/huongdan/dochuan.py`
