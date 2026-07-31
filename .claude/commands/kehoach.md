---
description: Chẻ việc trong VIECDANGLAM.md thành các bước, chỉ rõ file nào bị đụng, chờ user duyệt
---

# /kehoach — cửa số 2: nói TRƯỚC sẽ đụng vào đâu, rồi mới được đụng

Chạy nối tiếp ngay sau cửa 1 — **không chờ user gõ gì**. Đọc `VIECDANGLAM.md`; phiếu rỗng nghĩa là
cửa 1 bị bỏ qua → quay lại làm `.claude/commands/ycau.md` trước, đừng bắt user đi lấy.

🔴 **CẤM viết code trong lệnh này.** Đầu ra là một kế hoạch chờ user gật đầu.

## Vì sao có lệnh này

Bệnh sử repo: **10 wrapper AnkiConnect** ra đời vì mỗi phiên AI chọn thứ an toàn cho *phiên của
mình* (chép thì chắc chạy, import phải đi đọc code người khác). Cách chặn rẻ nhất là bắt khai
đường đi **trước khi gõ**, lúc còn sửa được bằng một câu chứ không phải bằng một commit.

## Bước 1 — Liệt kê CÁI CÓ SẴN trước khi nghĩ tới cái mới (L1, cửa DỪNG LẠI HỎI số 4)

Bắt buộc, không được bỏ qua kể cả khi việc trông nhỏ:

- Hàm/module có sẵn mà việc này **nên dùng lại** — kể cả chỉ gần giống.
- Đụng tài nguyên ngoài? Đi đúng **một cửa**: AnkiConnect → `anki_tools/anki_client.py`,
  cào OpenRussian → `grammar.fetch_page`, gọi AI → `ai_client`. **Cấm** wrapper mới, cấm trỏ
  thẳng `:8765`.
- Định viết hàm **trùng vai** với hàm đã có, hay tạo file `.py` mới ở thư mục gốc?
  → **DỪNG LẠI HỎI USER**, đừng ghi vào kế hoạch rồi làm luôn.

## Bước 2 — Chọn chỗ đặt (`CACHLAM.md` 3a)

Chỉ bot dùng → `tgbot/` · chỉ dây chuyền soạn kho → `data/huongdan/` · chỉ thẻ ngữ pháp →
`grammar_forms/` · **từ HAI mảng trở lên thật sự cần** → `anki_tools/`.
Chiều import một chiều: các mảng import `anki_tools`, `anki_tools` không import ngược.

Đếm dòng file định sửa: **>400 dòng** → ghi `SONO.md`; **>700 dòng** → tách trước khi thêm.

## Bước 3 — Trình kế hoạch cho user duyệt, đúng bốn mục

Bằng **ngôn ngữ thường**, thuật ngữ nào bắt buộc dùng thì mở ngoặc giải thích ngay:

1. **Làm gì** — từng bước, mỗi bước một dòng, kèm **file nào bị đụng và vì sao file đó**.
2. **Rủi ro** — nói thẳng loại nguy hiểm nhất của repo này: **hỏng im lặng**. Có chạm
   **vùng im lặng** không (đổi field/model Anki, xoá–ghi đè hàng loạt thẻ thật, sync)?
   Có → đây là việc **đứng riêng một mình** theo L4: backup trước, kiểm `journalctl` sau,
   không gộp việc khác vào.
3. **Mất bao lâu** — và quy đổi sang đơn vị user hiểu: *"tốn khoảng bằng N lô soạn kho"*.
4. **Lùi lại thế nào** — hỏng thì gõ đúng lệnh gì để trở về như cũ.

Kèm hai dòng nữa:

- **Lệnh nghiệm thu** (L3) — chính xác lệnh sẽ chạy khi xong, ghi ngay từ bây giờ.
- **Có phải ghi `QD-nn` không** (L5) — có rẽ nhánh (chọn A thay vì B mà 6 tháng sau nhìn code
  không tự thấy lý do) → soạn sẵn mục 4 dòng *Chọn / Thay vì / Vì / Hết hạn* để user duyệt luôn.

## Bước 4 — Nối kế hoạch vào phiếu việc, rồi DỪNG

Thêm mục `## Kế hoạch (đã duyệt <ngày>)` vào `VIECDANGLAM.md` — giữ ngắn, cả file vẫn phải
dưới 60 dòng. Rồi **chờ user gật đầu**. User duyệt xong mới bắt đầu viết code; viết xong chạy
`/nghiemthu`.
