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
| `tgbot/dispatch.py` 430 → 460 dòng | Khối nút của 4 luồng chạy lô (sd·scan·sp·tumoi) gần như y hệt nhau: huỷ/dừng/xác nhận. Gom lại được, nhưng đợi luồng thứ 5 rồi gom một thể cho đáng | 2026-10-31 |
| `anki_tools/anki_client.py` 637 → 646 dòng (trần tách 700) | +9 dòng ghi bẫy `ReadTimeout` vào `_ac()` — cửa mà MỌI lệnh AnkiConnect đi qua, tức chỗ người gỡ lỗi chắc chắn mở. Đặt chỗ khác là đặt chỗ không ai đọc | 2026-10-31 |
| `anki_tools/ai_client.py` 486 → 521 dòng (trần tách 700) | Lô hoá `call_claude_topic` để xếp lại 1212 thẻ bằng ~49 lượt thay vì 1212. Tách file lúc đang sửa cây chủ đề là trộn hai việc (L4) | 2026-10-31 |
| Web luyện CHI PHỐI ĐỘNG TỪ (repo `slushai`) — cửa 1 xong 11/08, chưa duyệt kế hoạch | Nhường lượt cho việc thay cây chủ đề + lệnh thêm từ. Toàn văn: `git log --grep "CHI PHOI"` (5 commit) | 2026-10-31 |

🔴 **Trước khi thêm dòng, hỏi: đây có phải NỢ không?** Nợ = việc mình BIẾT phải làm
mà cố ý hoãn. KHÔNG phải nợ, và cấm ghi vào đây:
· **Con số trần** (dòng/ký tự) — chúng ở `soat_nguong.json`, cửa S13/S10 canh thật.
  Chép sang đây là dựng sổ thứ hai, mà hai sổ song song thì không sổ nào được tin.
· **Sự thật về môi trường** đã có quyết định "để yên" — chỗ của nó là bảng
  "📏 ĐÃ ĐO RỒI BÁC" ở `QUYETDINH.md`, để phiên sau khỏi đề xuất lại.
