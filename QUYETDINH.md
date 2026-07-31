# 📌 QUYẾT ĐỊNH KỸ THUẬT (`QD-nn`)

> Mỗi mục **đúng 4 dòng**: Chọn / Thay vì / Vì (+Hết hạn nếu có). Mới nhất TRÊN CÙNG.
> Chỉ ghi khi RẼ NHÁNH (4 cửa ở `CACHLAM.md` Q5) — việc thường ghi `CHANGELOG.md`.
> Commit thi hành quyết định thì nhắc số hiệu, ví dụ `(QD-01)`.

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
