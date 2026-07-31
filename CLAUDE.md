# CLAUDE.md — luật làm việc trong repo này (đọc trước khi làm bất cứ gì)

## 🔀 Chọn model cho việc đang làm — AI TỰ ĐỐI CHIẾU, user không cần nhớ

**Opus khi việc là QUYẾT ĐỊNH** (thiết kế, chọn cái gì KHÔNG làm, gỡ lỗi nhiều vòng, viết tài liệu
tầng kiến trúc). **Sonnet khi việc là THI HÀNH theo spec đã có** (sửa cơ học, `git mv`, script chỉ
đọc, diff nhỏ có sẵn lệnh nghiệm thu). Lệch thì **DỪNG LẠI, nói user gõ `/model` đổi trước**, đừng
làm rồi mới báo — trừ khi lệch theo hướng mạnh hơn mức cần, lúc đó chỉ cần nói một câu rồi làm tiếp.

---

Sổ tay đầy đủ: `CACHLAM.md` (luật `L1`–`L5`, có số hiệu để viện dẫn). Quyết định kỹ thuật: `QUYETDINH.md` (`QD-nn`). Nợ kỹ thuật: `SONO.md`. Mọi lần sửa xong: ghi `CHANGELOG.md` (mới nhất trên cùng, kèm **vì sao**).

**Sửa việc XUYÊN MẢNG, hoặc đụng file đã ghi nợ trong `SONO.md` → đọc `KIENTRUC.md` TRƯỚC.** Nó giữ: bản đồ 4 mảng + chiều import một chiều · các cửa L1 · **coupling ẩn qua file dữ liệu** (thứ grep `import` không thấy) · vòng `grammar↔wiktionary` đang bẻ bằng import-trong-hàm · vùng im lặng + công cụ cứu hộ · 5 bất biến dây chuyền kho.

## 5 luật

- **L1 — Một cửa cho tài nguyên ngoài.** AnkiConnect → `anki_tools/anki_client.py`; cào OpenRussian → `grammar.fetch_page`; AI API → `ai_client`. CẤM viết wrapper mới / trỏ thẳng `:8765`. Ngoại lệ duy nhất: `data/huongdan/kho/` cố tình đóng băng (QD-01).
- **L2 — Script một lần phải chết trong cùng commit.** Đặt tên `_va_<việc>.py`, chạy xong chuyển vào `_daxong/` ngay. Thư mục gốc chứa **đúng ba** file `.py`: `bot.py`, `main.py`, `soatkientruc.py` — script vận hành còn dùng lại thì để `scripts/` (nhớ 3 dòng bootstrap `sys.path`). Thêm tên vào danh sách trắng S6 là **nới luật**, phải ghi `QD-nn` trước.
- **L3 — Mọi việc sửa code kết thúc bằng mục "Lệnh nghiệm thu:" và CHẠY nó.** Tối thiểu: `python soatkientruc.py` (cửa soát kiến trúc — ĐỎ là dừng, xem `soat_baseline.json`) rồi `python -c "import bot, main"`. Cả hai đã cắm sẵn vào `deploy.ps1` nên không deploy được khi ĐỎ.
- **L4 — Vùng im lặng đứng riêng một mình** (danh sách bên dưới): không gộp việc khác, backup trước, kiểm sau.
- **L5 — Rẽ nhánh thì ghi `QUYETDINH.md`**: mục 4 dòng (Chọn / Thay vì / Vì / Hết hạn), số hiệu `QD-nn`, commit thi hành nhắc số hiệu.

## DỪNG LẠI HỎI trước khi

1. Đổi/thêm/xoá field của model Anki hay bất cứ gì kích full sync (schema mod → VPS kẹt "Sync status 2" **im lặng**, đã xảy ra thật).
2. Xoá hoặc ghi đè hàng loạt thẻ/note thật.
3. Tạo file `.py` mới ở thư mục gốc.
4. Viết hàm thứ hai cùng vai với hàm đã có — trước khi viết bất cứ gì, **liệt kê hàm/module có sẵn dùng lại được**; có cái gần giống thì mở rộng nó.
5. Đụng hạ tầng/repo ngoài phạm vi việc được giao.

## Chỗ đặt code (4 mảng, gặp nhau CHỈ ở bộ sưu tập Anki)

- Chỉ bot dùng → `tgbot/` · chỉ dây chuyền soạn kho → `data/huongdan/` · chỉ thẻ ngữ pháp → `grammar_forms/` · từ HAI mảng trở lên thật sự cần → `anki_tools/`.
- Chiều import một chiều: các mảng import `anki_tools`; `anki_tools` không import ngược.
- File >400 dòng: đừng thêm vào nữa, ghi `SONO.md`; >700 dòng: tách trước khi thêm.
- Chép-dán chỉ hợp lệ khi là **ảnh chụp cố ý**: dòng đầu file ghi `# ẢNH CHỤP từ <gốc> ngày <d>, lý do, hết hạn khi <sự kiện>` + một mục QD. Còn lại: import.
- Agent soạn lô kho: KHÔNG chạm Anki, KHÔNG chạm git, chỉ đẻ file dữ liệu.

## Nghiệm thu (khai cuối mỗi việc)

Ba mục: **đã đổi gì (từng file, vì sao) · lệnh nghiệm thu · rủi ro im lặng nào có thể có**. Sửa ít file nhất có thể; diff to hơn lời hứa thì giải thích trước khi nhận.

## Bẫy đã trả học phí

- Chuẩn hoá tiếng Nga phải `unicodedata.normalize("NFC", ...)` — hai hàm lệch nhau là `ё` hỏng **im lặng**.
- Anki trên VPS chạy trong Docker (uid 1000): đường dẫn file trong lệnh AnkiConnect theo góc nhìn **của Anki trong container** + quyền đọc được; luôn thử thật trên VPS.
- Callback data Telegram trần 64 byte → nút mang chỉ số, không mang chuỗi dài.
- Mọi `findNotes` phải lọc `note:"<model>"` — một từ có thể có cả thẻ từ vựng lẫn thẻ ngữ pháp.
- `getReviewsOfCards` phải truyền int, không truyền str.
- Cảnh báo cho user đi qua `tgbot/alerts.py`, không `send_message` thẳng (chống spam).
- KHÔNG in nghiêng chữ Nga trong HTML thẻ (đổi mặt chữ, mất dấu trọng âm).
