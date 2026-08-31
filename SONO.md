# 💳 SỔ NỢ KỸ THUẬT

> Ghi khi vượt ngưỡng ở `CACHLAM.md` Q4 — KHÔNG sửa ngay giữa việc khác.
> **MỘT NỢ = MỘT DÒNG BẢNG** (trần ký tự ở `soat_nguong.json`, cửa **S18** đếm thật).
> Chi tiết dài thì để `git log --grep`, đừng nhét vào đây — sổ này phình là hết người đọc.
>
> 🔴 **CỘT "HẾT HẠN" LÀ BẮT BUỘC** (QD-25). Quá hạn ⇒ **S18 kêu ĐỎ, chặn deploy** cho tới khi:
> trả nợ (xoá dòng) · hoặc gia hạn kèm lý do mới trong commit. Không cho món nợ nằm im mãi.
> 🔴 **TRẢ XONG THÌ XOÁ DÒNG, đừng đánh dấu rồi để đó** (cửa **S16**, QD-24) — sổ chỉ chứa nợ
> CHƯA trả. Nợ đã trả là lịch sử, và lịch sử ở `git log`. Bài học còn sống thì dời sang nơi
> được đọc lúc cần (vùng im lặng `KIENTRUC.md`, comment cạnh đúng đoạn code), đừng giữ làm nghĩa trang.

## Nợ

| Nợ | Vì sao chưa trả | Hết hạn |
|---|---|---|
| Luồng QUÉT ẢNH chưa thử thật sau khi refactor sang `core.them_loat_tu` (23/08) | Cần một ảnh trang sách để thử; 160 test không phủ được đường đi Telegram. Đọc lại mã thì khớp | 2026-09-15 |
| `tgbot/core.py` 370 → 477 dòng (trần tách 700) | Nhận 2 hàm dùng chung từ `flow_scan` (màn duyệt + thêm loạt từ); `flow_scan` giảm 249→174 nên code DỜI chứ không đẻ. Tách lúc này là trộn việc | 2026-10-31 |
| `tgbot/dispatch.py` 460 → 484 dòng | 🔔 **ĐIỀU KIỆN GOM ĐÃ TỚI**: luồng thứ 5 (`banthe`) vừa thêm, giờ có 5 khối huỷ/dừng/xác nhận y hệt nhau. Cố ý CHƯA gom trong commit này — gom 5 khối là sờ vào 4 luồng đang chạy tốt, trộn vào việc khác là trái L4 | 2026-09-30 |
| `tgbot/flow_add.py` 326 → 403 dòng (trần ghi nợ 400) | +77: dựng lại nhóm sau khi thêm động từ + màn mời thêm bạn thể (QD-39). Đúng chỗ theo luật đặt code (chỉ bot dùng); tách ra là đẻ file thứ hai cho một luồng | 2026-10-31 |
| `data/huongdan/kho/congcu.py` 493 → 509 dòng | +16: `bang` đọc `GrammarJSON` của CHÍNH thẻ thay vì tra bộ đệm theo tên (QD-40) + giữ lại lời kêu "bản ghi cũ phiên bản" mà `get_cached` từng kêu hộ | 2026-10-31 |
| `anki_tools/anki_client.py` 646 → 659 dòng (trần tách 700) | +13 dòng: bẫy `ReadTimeout` trong `_ac()`, và cửa TỪ CHỐI ghi khi 2 thẻ trùng `WordClean` (QD-39). Cả hai nằm ở đường mà MỌI lệnh AnkiConnect đi qua — đặt chỗ khác là đặt chỗ không ai đọc | 2026-10-31 |
| `anki_tools/anki_the.py` 393 → 404 dòng (trần tách 700) | +96: `nhom_dong_tu()` nối động từ cùng gốc (QD-39). Để ở đây vì cả bot lẫn dây chuyền kho đều gọi, và nó đọc note y như phần còn lại của file. Tách khi có việc thứ hai cần ; +11 lấy từ loại AI vá khi nguồn bỏ trống (QD-41) | 2026-10-31 |
| `anki_tools/grammar.py` 502 → 506 dòng (trần tách 700) | +4 dòng luồn `note_id` qua `fetch_grammar`/`remember` để ghi thẻ theo id thay vì tìm lại bằng tên (QD-39) | 2026-10-31 |
| `anki_tools/ai_client.py` 521 → 607 dòng (trần tách 700) | +86: hỏi thêm TỪ LOẠI ở lượt AI sẵn có + `call_claude_pos()` xếp theo lô (QD-41). Cùng file vì cùng một cửa gọi AI (L1) | 2026-10-31 |
| `backfill_badge.py --apply` ghi đè SAI ô thể của `быть` và `нарезать` | Docstring dặn CHỪA `быть` từ 12/08 nhưng KHÔNG có dòng code nào thi hành; `нарезать` là bẫy đồng tự QD-40. Bắt được 01/09 lúc vá từ loại, đã bó tạm bằng cờ `--chi-tuloai`. Phải cân từng ca, L4 cấm gộp | 2026-10-31 |
| XOÁ lệnh `/suadeck` (user chốt 01/09) — ~260 dòng ở `flow_edit.py`+`dispatch.py`+`core.py`, kèm `PHIENBAN.md` | Ra đời 15/07, cây deck chủ đề 18/07 ⇒ di tích thời deck-theo-ngày; `VPS_SETUP.md` đã ghi "ít dùng". Nguy: 1 nút điện thoại ghi đè CẢ deck, không xem trước | 2026-10-31 |
| Web luyện CHI PHỐI ĐỘNG TỪ (repo `slushai`) — cửa 1 xong 11/08, chưa duyệt kế hoạch | Nhường lượt cho việc thay cây chủ đề + lệnh thêm từ. Toàn văn: `git log --grep "CHI PHOI"` (5 commit) | 2026-10-31 |

🔴 **Trước khi thêm dòng, hỏi: đây có phải NỢ không?** Nợ = việc mình BIẾT phải làm
mà cố ý hoãn. KHÔNG phải nợ, và cấm ghi vào đây:
· **Con số trần** (dòng/ký tự) — chúng ở `soat_nguong.json`, cửa S13/S10 canh thật.
  Chép sang đây là dựng sổ thứ hai, mà hai sổ song song thì không sổ nào được tin.
· **Sự thật về môi trường** đã có quyết định "để yên" — chỗ của nó là bảng
  "📏 ĐÃ ĐO RỒI BÁC" ở `QUYETDINH.md`, để phiên sau khỏi đề xuất lại.
