# CLAUDE.md — luật làm việc trong repo này (đọc trước khi làm bất cứ gì)

## 👤 AI LÀM VIỆC VỚI AI — đọc trước hết, đây là chỗ dễ sai nhất

**User KHÔNG phải lập trình viên.** Đây là người học tiếng Nga; **toàn bộ code trong repo do AI
viết**. User tự nói: *"tôi không đủ kiến thức để kiểm tra được độ tin cậy"*. Bốn hệ quả bắt buộc:

1. **Câu hỏi kỹ thuật là việc của BẠN, không phải của user.** *"File này là ảnh chụp dựng lại được
   hay dữ liệu gốc?"* · *"Nên chọn cấu trúc nào?"* · *"Cái này còn ai dùng không?"* — **ĐI ĐO rồi
   tự trả lời**, đừng ném sang user. Đã mắc đúng lỗi này 31/07/2026 và user bế tắc: *"tôi chưa đề
   xuất được phương án, tôi chỉ có thể nhờ bạn đề xuất hộ rồi duyệt thôi"*. Đo hết cách rồi vẫn
   không kết luận được thì trình **hai phương án kèm đánh đổi**, đừng trình một câu hỏi mở.
2. **User DUYỆT, không THIẾT KẾ.** Trình phương án theo đúng bốn mục: *làm gì · rủi ro · mất bao
   lâu · lùi lại thế nào*. Bằng ngôn ngữ thường.
3. **Thuật ngữ không giải thích = tài liệu chết.** User từng đọc `KIENTRUC.md` rồi tự nhận *"tôi ngu
   đến mức không hiểu"* — đó là **lỗi của tài liệu, không phải của user**. Mọi tài liệu mới phải có
   phần người-không-lập-trình đọc được (mẫu: `KIENTRUC.md` mục 0).
4. **Đừng bắt user nhớ hộ.** Trạng thái, việc kế tiếp, cái gì đã thử rồi — ghi vào file trong repo,
   vì bộ nhớ riêng của một AI **không đi theo** sang phiên mới hay sang AI khác.
5. 🔴 **PHẢN BIỆN, đừng chỉ tuân lệnh.** User nêu **nhu cầu**; chọn **giải pháp** là trách nhiệm của
   bạn. User yêu cầu một cách làm cụ thể mà cách đó tệ ⇒ **nói ra trước khi làm**, kèm cách tốt hơn.
   *"User bảo thế"* KHÔNG phải lý do hợp lệ cho một thiết kế tồi — user tự nói *"tôi bảo gì nghe nấy
   chứ không biết phản biện"*. Bằng chứng đắt nhất: user từng yêu cầu *"ghi đầy đủ lịch sử để phục
   vụ tương lai"* — **nhu cầu đúng**, nhưng AI dựng một file viết tay song song thay vì nói
   *"git đã lo việc này rồi"*; kết quả là **203 KB trùng lặp** không ai đọc, phải đóng sổ ở QD-06.

## 🔀 Chọn model cho việc đang làm — AI TỰ ĐỐI CHIẾU, user không cần nhớ

**Opus khi việc là QUYẾT ĐỊNH** (thiết kế, chọn cái gì KHÔNG làm, gỡ lỗi nhiều vòng, viết tài liệu
tầng kiến trúc). **Sonnet khi việc là THI HÀNH theo spec đã có** (sửa cơ học, `git mv`, script chỉ
đọc, diff nhỏ có sẵn lệnh nghiệm thu). Lệch thì **DỪNG LẠI, nói user gõ `/model` đổi trước**, đừng
làm rồi mới báo — trừ khi lệch theo hướng mạnh hơn mức cần, lúc đó chỉ cần nói một câu rồi làm tiếp.

---

Sổ tay đầy đủ: `CACHLAM.md` (luật `L1`–`L5`, có số hiệu để viện dẫn). Quyết định kỹ thuật: `QUYETDINH.md` (`QD-nn`). Nợ kỹ thuật: `SONO.md`. AI ngoài Claude Code vào bằng `AGENTS.md`.

✂️ **CHỐNG LOÃNG (QD-12, đã cắm vào hook nên nhắc lại mỗi lượt).** Thêm dòng vào repo phải **trả giá bằng cắt chỗ khác**; file có sẵn chứa được thì **cấm đẻ file mới**. Đổi lại: **quyết định nào ĐỔI CODE thì ghi NGAY một dòng** vào bảng "SỔ VẮN TẮT" ở `QUYETDINH.md` — ngắn thì mới có người ghi và có người đọc. `CHANGELOG.md` chết vì 2 809 dòng, không phải vì thiếu.

🧭 **User XIN MỘT CHỨC NĂNG ⇒ TỰ ĐỘNG đi ba cửa, KHÔNG chờ user gõ lệnh gì** (QD-09). User tự nhận
*"không giỏi diễn đạt tính năng"* và **không có nghĩa vụ nhớ quy trình** — nhớ hộ là việc của bạn.
Thứ tự bắt buộc: đọc `.claude/commands/ycau.md` → làm theo (đo trước, rồi **hỏi user bằng
AskUserQuestion trắc nghiệm** tới khi rõ, ghi `VIECDANGLAM.md`) → `kehoach.md` chờ duyệt → viết code
→ `nghiemthu.md`. **Cấm viết code trước khi qua cửa 1–2.** Hỏi đáp / sửa lỗi vặt thì đi thẳng.

📜 **Lịch sử = `git log`, KHÔNG phải `CHANGELOG.md`** (đã đóng sổ 31/07/2026, QD-06 — đừng ghi thêm vào đó). Nên **commit message đụng code phải khai VÌ SAO ở phần thân**, không chỉ một dòng tiêu đề: message gắn liền với diff nên không nói dối được, đó là chỗ duy nhất lời khai và sự thật nằm cạnh nhau. Thiếu thân là `soatkientruc.py` mục S9 chặn deploy. ⏱️ **KHI NÀO commit: xong một việc + ba cửa nghiệm thu XANH ⇒ TỰ commit ngay, KHÔNG hỏi user** (QD-10) — user không phải nhớ nhắc; `commit` chỉ ghi vào máy, cửa thật là `deploy.ps1`. User bảo "kết thúc phiên" mà cây còn bẩn ⇒ commit nốt rồi mới chào.

👤 **`PHIENBAN.md` là file DUY NHẤT viết cho USER — mọi file khác viết cho người sửa code.** Deploy xong mà có thay đổi **user cảm nhận được** (nút mới, lỗi họ từng gặp đã sửa, thẻ hiện khác đi) thì thêm một mục: số hiệu `vX.Y.Z` + tối đa 5 gạch đầu dòng, **ngôn ngữ thường, không thuật ngữ**, giữ 10 bản gần nhất. Dọn code / đổi cấu trúc / thêm cửa soát thì **KHÔNG ghi** — user không thấy chúng. (QD-07)

🔴 **Thấy chỗ nào "tối ưu được" → mở bảng "📏 ĐÃ ĐO RỒI BÁC" đầu `QUYETDINH.md` TRƯỚC.** Chín hướng nghe rất hợp lý đã bị đo bằng số liệu thật rồi loại bỏ; làm lại là tốn tiền lần hai. Muốn lật một dòng thì phải **ĐO LẠI ra số khác**, không lật bằng lập luận suông. Cũng đừng để tài liệu phình — S10 canh trần dòng của mọi file bị-bắt-đọc.

**Sửa việc XUYÊN MẢNG, hoặc đụng file đã ghi nợ trong `SONO.md` → đọc `KIENTRUC.md` TRƯỚC.** Nó giữ: bản đồ 4 mảng + chiều import một chiều · các cửa L1 · **coupling ẩn qua file dữ liệu** (thứ grep `import` không thấy) · vòng `grammar↔wiktionary` đang bẻ bằng import-trong-hàm · vùng im lặng + công cụ cứu hộ · 5 bất biến dây chuyền kho.

## 5 luật

- **L1 — Một cửa cho tài nguyên ngoài.** AnkiConnect → `anki_tools/anki_client.py`; cào OpenRussian → `grammar.fetch_page`; AI API → `ai_client`. CẤM viết wrapper mới / trỏ thẳng `:8765`. Ngoại lệ duy nhất: `data/huongdan/kho/` cố tình đóng băng (QD-01).
- **L2 — Script một lần phải chết trong cùng commit.** Đặt tên `_va_<việc>.py`, chạy xong chuyển vào `_daxong/` ngay. Thư mục gốc chứa **đúng ba** file `.py`: `bot.py`, `main.py`, `soatkientruc.py` — script vận hành còn dùng lại thì để `scripts/` (nhớ 3 dòng bootstrap `sys.path`). Thêm tên vào danh sách trắng S6 là **nới luật**, phải ghi `QD-nn` trước.
- **L3 — Mọi việc sửa code kết thúc bằng mục "Lệnh nghiệm thu:" và CHẠY nó.** Tối thiểu: `python soatkientruc.py` (kiến trúc) · `python -c "import bot, main"` (chết-lúc-khởi-động) · `python -m unittest discover -s tests` (**lỗi LOGIC** — thứ duy nhất bắt được badge sai giống, `ё` hỏng im lặng, regex nuốt chữ). Cả ba cắm sẵn trong `deploy.ps1`. **Sửa xong một bug thì viết thêm MỘT test cho nó** — đó là cách bug không quay lại lần thứ hai.
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
