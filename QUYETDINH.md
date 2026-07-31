# 📌 QUYẾT ĐỊNH KỸ THUẬT (`QD-nn`)

> Mỗi mục **đúng 4 dòng**: Chọn / Thay vì / Vì (+Hết hạn nếu có). Mới nhất TRÊN CÙNG.
> Chỉ ghi khi RẼ NHÁNH (4 cửa ở `CACHLAM.md` Q5) — việc thường ghi `CHANGELOG.md`.
> Commit thi hành quyết định thì nhắc số hiệu, ví dụ `(QD-01)`.

---

## 📏 ĐÃ ĐO RỒI BÁC — đừng làm lại, đã tốn tiền một lần

> Mỗi dòng dưới đây là một hướng **nghe rất hợp lý**, đã có người (hoặc AI) thử, **đo bằng số liệu
> thật rồi loại bỏ**. Đây là loại lỗi đắt nhất: AI phiên sau đọc code thấy "chỗ này tối ưu được"
> rồi làm lại từ đầu. **Trước khi "tối ưu" bất cứ thứ gì trong bảng này, đọc cột Vì.**
> Muốn lật một dòng: phải ĐO LẠI ra số khác, không được lật bằng lập luận suông.

| Hướng nghe hợp lý | Phán quyết | Vì (số liệu thật) |
|---|---|---|
| Bỏ `grammar_cache.json`, đọc thẳng field `GrammarJSON` trong thẻ | **BÁC** | Đo 31/07/2026 trên 976 thẻ: cache **bao trùm** thẻ, **88 thẻ thiếu hẳn** `present`/`future`/`parts`; không thẻ nào có khoá mà cache thiếu. Xem QD-05 |
| Dùng `_family()` của OpenRussian để dựng mục "Họ hàng" | **BÁC** | Nó gộp `groups` (cùng gốc) với `relateds` (đồng nghĩa **khác gốc hẳn**) vào một rổ ⇒ dạy sai từ nguyên. Mục Họ hàng do người soạn tự nghĩ, cố ý không có cửa máy |
| Lọc từ theo tag trình độ A1–C2 của OpenRussian | **BÁC** | `паспорт`, `яблоко`, `сахар` bị gắn **C1**. Dùng **thứ hạng tần suất** thay thế (top 2500 danh từ ≈ A1→B2) |
| Đối chiếu chéo `nouns.csv` với `grammar_cache.json` để bắt lỗi dữ liệu | **KHÔNG ĐỦ** | Hai file **cùng thượng nguồn OpenRussian** ⇒ trùng nhau không chứng minh đúng. `фон` sai ở **cả hai**. Cửa duy nhất còn lại là người đọc bằng mắt |
| Chờ Difficulty của thẻ tự hồi phục khi trả lời Good | **BÁC** | Đo thật: `w7=0.001` ở sàn, cần **610 lần** Good mới về 50%; **0/84 thẻ** hồi phục. Chỉ Forget/Reset mới cứu |
| Gộp 4 hàm chuẩn hoá tiếng Nga làm một cho gọn | **CHƯA CẦN** | Đo 1748 từ Nga thật (31/07/2026): **0 bất đồng** ở cả hai cặp hàm cùng mục đích. Rủi ro `ё` tổ hợp có thật về lý thuyết nhưng chưa chạm dữ liệu nào ⇒ **đo lại trước khi gộp**, đừng gộp mò |
| "Lô soạn kho càng to càng lợi" | **ĐÚNG MỘT NỬA** | Đúng về token, nhưng lý do thứ hai (khối dùng chung gánh nhiều thẻ) **chết rồi** — chuẩn v3 cấm khối dùng chung, đo ra `0%`. Cỡ lô do CHẤT LƯỢNG quyết định: chốt 16–18 từ |
| Dựng "agent soát riêng" để kiểm lô sau khi soạn | **BÁC** | Lô 22 từ + agent rà lại ≈ **7,9K token/từ**, đắt hơn lô 14 từ tự soát (**7,3K**) mà chưa chắc tốt hơn: người viết biết chỗ mình lăn tăn, người rà phải dựng lại từ đầu |
| Cho VPS tự động "Download from AnkiWeb" theo lịch cho an toàn | **BÁC — NGUY HIỂM** | Lệnh đó **ghi đè sạch** collection trên VPS (xoá thẻ bot vừa thêm), và không cứu được gì khi quên sync điện thoại vì dữ liệu ôn lúc đó nằm **trong điện thoại** |

---

## QD-02 · 31/07/2026 · `soatkientruc.py` là điểm vào thứ 3 ở gốc + ratchet + cửa trong `deploy.ps1`
Chọn: một file `soatkientruc.py` ở thư mục gốc (stdlib, `ast`+regex, KHÔNG import module dự án), baseline ratchet một chiều trong `soat_baseline.json`, cắm làm bậc 1 của `deploy.ps1` trước `git push`.
Thay vì: để luật kiến trúc nằm trong `CACHLAM.md`/`CLAUDE.md` và trông vào tự giác; hoặc dựng pytest/CI/pre-commit.
Vì: chỗ nào có máy đo (dây chuyền kho, tag `chuan::N`) thì sạch, chỗ nào chỉ có luật viết ra thì trôi — 10 wrapper ra đời SAU khi phát biểu "MỘT chức năng MỘT script". Đặt ở gốc là **ngoại lệ L2 có chủ ý** (L2: gốc chỉ chứa điểm vào đang sống): nó phải nằm nơi `python soatkientruc.py` gõ được không cần nhớ đường dẫn, và chính nó là thứ canh L2. Ratchet chỉ cho GIẢM ⇒ nợ không mọc lại; nới được thì nó thành bảng ghi nợ chứ không phải cửa. Hết hạn: không — thay bằng CI chỉ khi dự án có người thứ hai viết code.

## QD-05 · 31/07/2026 · Cache ngữ pháp của bot nằm NGOÀI repo (biến `ANKI_GRAMMAR_CACHE`)
Chọn: `grammar.CACHE_PATH` đọc biến môi trường, mặc định giữ chỗ cũ; VPS trỏ `/root/anki-cache/`.
Thay vì: bỏ file khỏi git (mất bản sao lưu công cào), hoặc bỏ hẳn cache để đọc field `GrammarJSON` trong thẻ (`TIEPTUC.md` từng đề xuất).
Vì: một file vừa do git quản vừa bị runtime ghi thì `git pull` bỏ cuộc mỗi lần deploy — đã xảy ra thật 31/07. **Hướng "đọc từ thẻ" đã ĐO và BÁC**: cache bao trùm thẻ, 88 thẻ thiếu hẳn `present`/`future`/`parts`. Cache là ảnh chụp cào lại được nhưng đắt, nên vẫn giữ trong git cho PC. Hết hạn: khi nào bot không còn tự cào (không thấy trước).

## QD-04 · 31/07/2026 · Cảnh báo "bot chết" đi đường ĐỘC LẬP, cố ý không qua `tgbot/alerts.py`
Chọn: `scripts/canhbao_bot_chet.sh` gọi thẳng Telegram API bằng `curl`; systemd `OnFailure=` + cron 15 phút; chống spam bằng mốc trạng thái nên chỉ nhắn khi trạng thái ĐỔI.
Thay vì: dùng `alerts.py` như mọi cảnh báo khác (luật thường lệ trong `CLAUDE.md`).
Vì: `alerts.py` gửi tin **qua chính bot** ⇒ bot chết thì lời cảnh báo chết theo, im lặng tuyệt đối — đúng thứ cần diệt. Đường báo phải không nạp một dòng code Python nào của dự án mới sống sót được khi dự án hỏng. Hết hạn: không.

## QD-03 · 31/07/2026 · Tháo ngòi 12 file lô thế hệ 1 thay vì xoá
Chọn: chèn `raise SystemExit(...)` ngay sau docstring của `lo01…lo12_*.py` — file còn đọc được, chỉ không chạy lại được nữa.
Thay vì: xoá hẳn 12 file.
Vì: chúng vẫn là bản tham chiếu nội dung của 168 thẻ đang phủ dở bởi k51–k60; chạy nhầm lại sẽ XOÁ bảng chia thẻ thật không một tiếng kêu — đã từng xảy ra 29/07/2026. Hết hạn: khi 168 thẻ đó mang tag `chuan::3` hết (đo bằng `findNotes`) → xoá hẳn, git giữ lịch sử.

## QD-01 · 30/07/2026 · Nhận hệ CACHLAM v1 + CLAUDE.md
Chọn: luật L1–L5 thi hành qua `CLAUDE.md` (AI tự đọc mỗi phiên) + lệnh grep; wrapper riêng của `data/huongdan/kho/` được đóng băng làm ngoại lệ L1 hợp lệ.
Thay vì: nguyên tắc chỉ nằm trong trí nhớ/memory phiên chat (đã chứng minh không tự thi hành — 10 wrapper ra đời SAU khi phát biểu "MỘT chức năng MỘT script").
Vì: chỗ có luật-trong-file + máy canh (CHUAN.md) không loạn, chỗ luật-trong-đầu loạn sau 3 tuần. Hết hạn ngoại lệ kho/: khi xong 61 lô.
