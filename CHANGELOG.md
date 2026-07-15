# 📜 Nhật ký thay đổi (CHANGELOG)

> File này là "bộ nhớ chung" của dự án: mỗi lần sửa gì đều ghi vào đây (mới nhất ở TRÊN CÙNG),
> để phiên chat mới / người mới đọc là nắm được ngay hệ thống đã đi qua những gì.
> Quy ước mỗi mục: **ngày — commit — làm gì + vì sao**.

## 15/07/2026

- **Vá lỗi RPM cho /suadeck + tính năng Sửa tiếp** — đợt sửa deck Матрёшка (309 thẻ)
  bị 44 lỗi vì model lite trả lời nhanh → vòng lặp bắn >15 lượt/phút (trần RPM
  free là 15); code cũ coi mọi 429 là hết quota ngày nên nhảy sang model dự phòng
  (quota bé) rồi chết. Fix: (1) 429 KHÔNG có chữ "PerDay" = giới hạn mỗi phút →
  chờ đúng retryDelay Google gợi ý (tối đa 2 lần) rồi thử lại CHÍNH model đó;
  (2) batch nghỉ 3s giữa 2 thẻ (~10 lượt/phút < 15); (3) batch dừng/lỗi → lưu
  danh sách thẻ còn dở vào `suadeck_resume.json` (gitignore) → /suadeck lần sau
  hỏi "▶️ Sửa tiếp N thẻ". Đợt Матрёшка được cứu bằng script quét mod-time trên
  VPS: xác nhận đúng 200 thẻ đã sửa, 109 thẻ dở đã vào danh sách Sửa tiếp.
- **/suadeck — sửa TOÀN BỘ thẻ trong 1 deck** (tính năng ít dùng nên là lệnh riêng
  trong danh sách "/", KHÔNG chiếm chỗ menu chính). Luồng toàn nút: chọn deck →
  kiểu sửa (1/2/3/tự viết) → màn xác nhận (số thẻ, ước tính thời gian, cảnh báo
  nếu >450 thẻ vì quota Gemini 500/ngày) → chạy nền. Tiến độ = ĐÚNG 1 tin nhắn
  tự cập nhật tại chỗ (thẻ i/N, vừa xong từ nào ✅/❌, đếm xong/lỗi) + nút ⏹ Dừng.
  Xong/dừng: sync AnkiWeb 1 lần, tổng kết liệt kê ≤10 từ lỗi (thẻ lỗi giữ nguyên
  nhờ OUTPUT CONTRACT + validate). Kỹ thuật: `get_deck_note_ids()` (anki_client),
  tách lõi `refine_note_id()` từ `refine_note()` (pipeline), batch chạy
  `asyncio.create_task` vì PTB xử lý update tuần tự (không thì nút Dừng chết),
  guard `sd_running` chống chạy 2 đợt, idle timer được đẩy mỗi thẻ.
- **Giao diện "bấm trước, gõ sau" (đỡ đổi bàn phím Nga↔Latin)** — user dùng bàn phím
  tiếng Nga liên tục nên gõ lệnh kiểu `/sua <từ>` rất bất tiện. Đổi logic:
  `/sua` (hoặc nút ✏️ Sửa thẻ) → bot hỏi "gõ từ cần sửa" → gõ từ → nút chọn kiểu sửa;
  nút "Tự viết yêu cầu" → bot hỏi → gõ thẳng yêu cầu (không cần gõ lại lệnh/từ).
  **Xóa lệnh `c` đổi deck** — đổi deck chỉ qua `/deck` hoặc nút 📚.
  Kỹ thuật: trạng thái chờ `user_data["awaiting"]` = `sua_word` / `sua_custom`,
  idle reset có dọn. Đường tắt `/deck <tên>`, `/sua <từ> [yêu cầu]` vẫn chạy ngầm.
- **vnc.bat** — double-click là xem màn hình Anki trên VPS: tự mở đường hầm SSH
  (cổng 15900, không hỏi pass nhờ SSH key) rồi bật TightVNC Viewer
  (`C:\Program Files\TightVNC\tvnviewer.exe`). Đóng cửa sổ SSH thu nhỏ = ngắt VNC.
- **Quyết định: KHÔNG cập nhật Anki trên VPS** dù có thông báo bản mới — hệ đang
  chạy ổn, addon AnkiConnect từng phải vá tay, bản trong Docker image chỉ đổi khi
  chủ động `docker compose pull`. Chỉ cập nhật khi AnkiWeb từ chối sync vì
  "client quá cũ" (lúc đó làm cùng Claude để có đường lùi).

- **Reset 3 phút gọn hơn + menu liền** — tin nhắn reset giờ chỉ báo "đã reset phiên"
  (nói rõ chỉ quên deck đang chọn, thẻ trong Anki không mất gì) và kèm luôn menu nút bấm
  y hệt `/menu` trong cùng 1 tin, để lần vào tới bấm chọn ngay.
- **Từ không có trên OpenRussian → AI đoán từ nguyên mẫu** — gõ từ biến cách
  (vd `дома`) hoặc sai chính tả (vd `хорошшо`): bot nhờ Gemini đoán dạng từ điển
  (lemma) + giải thích ngắn tiếng Việt, hiện nút `✅ Thêm '<từ>'` (kèm 0–2 phương án
  phụ nếu mơ hồ) và `🚫 Hủy`. Bấm xác nhận thì mới cào OpenRussian bằng từ đó —
  AI chỉ đoán, KHÔNG tự quyết. Kỹ thuật: `pipeline.process_word` trả cờ
  `not_found`; `ai_client.call_claude_lemma()`; nút dùng chỉ số
  (`lemma:i`, danh sách trong `user_data["lemma_choices"]`) để né giới hạn
  64 byte callback_data.
- **Thêm CHANGELOG.md này** — quy trình mới: mỗi lần sửa code phải cập nhật
  CHANGELOG + memory của Claude, để không phải kể lại ngữ cảnh ở phiên chat mới.

## 14/07/2026 — ngày chuyển toàn bộ hệ thống lên VPS

- `6e5040a` — Cập nhật docs: deploy.bat, /deck mở bảng chọn, nút Tự sửa/Bỏ qua.
- `9000213` — **deploy.bat**: double-click là deploy, khỏi mở PowerShell.
  Kèm theo (ngoài git): tạo SSH key trên PC + chép lên VPS → deploy không hỏi mật khẩu.
- `19aad56` — Thẻ AI bị khuyết (thiếu ví dụ): 2 nút bấm liền **🔧 Tự sửa** (chạy
  preset 2 đổi ví dụ) / **⏭ Bỏ qua**; `/deck` không tham số mở bảng chọn deck.
- `c718d70` — **Chọn deck bằng nút bấm**: [📂 Deck có sẵn (liệt kê hết, tối đa 24)]
  [➕ Tạo deck mới (gõ tên)]; gõ `c` mở cùng bảng này, deck cũ giữ đến khi chọn xong.
- `603e283` — Báo rõ thẻ khuyết khi AI thất bại (cờ `ai_degraded` + cảnh báo),
  thêm dòng 🇬🇧 vào tin nhắn tổng kết, AI freestyle retry 2 lần.
- `7e04cc7` — **CHÍNH SÁCH SYNC** (sau sự cố mất deck 00 do chọn Upload trên iPhone):
  sync AnkiWeb NGAY sau MỌI hành động sửa đổi + báo rõ khi sync thất bại.
  Quy tắc trên iPhone: LUÔN chọn "Download from AnkiWeb".
- `f94ed83` — Nâng cấp lớn bot: `/sua` có OUTPUT CONTRACT cứng (không thể trả thiếu
  ví dụ) + validate + retry; preset 1 Ngắn hơn / 2 Đổi ví dụ / 3 Dài hơn; bỏ deck
  mặc định (hỏi deck đầu phiên như CLI); idle reset 3 phút; /menu; viết lại README.
- `fdea689` — Thêm trùng dùng `options.allowDuplicate` chính thống (mánh ký tự vô
  hình ZWSP bị Anki ≥25.x tự xóa nên hỏng).
- `83a1271` — Hết quota không chết: chuỗi model dự phòng khi 429
  (chính: `gemini-3.1-flash-lite` 500 lượt/ngày); ping API bằng GET /models không đốt quota.
- `e403a94` — Sửa báo động giả "AI chưa phản hồi" (parse lỗi Google bọc trong list).
- `88613d7` — setup_vps.sh tự cài addon AnkiConnect vào volume (addon gốc là symlink
  bị volume che mất) + set webBindAddress.
- `aea5733` — Vá lỗi quyền thư mục anki-data (chmod 777) + hướng dẫn VNC qua tunnel cổng 15900.
- `ff38068` — Gỡ nút AI Refine + toàn bộ JS khỏi thẻ Anki → thẻ tĩnh, key không còn
  nhúng vào thẻ, prompt chỉ còn 1 nơi (`ai_client.py`). Sửa thẻ = `/sua` qua bot.
- `066f291` — Commit đầu: chuyển hệ thống lên VPS — bot Telegram + pipeline dùng
  chung CLI/bot + secrets tách ra `.env` + docker-compose (headless-anki) +
  setup_vps.sh + systemd + deploy.ps1 + VPS_SETUP.md.

## Hạ tầng cố định (để khỏi tìm lại)

- VPS: FPT `161.248.146.56` (1 vCPU/2GB/16GB + swap 2GB), code tại `/root/ankiagent`,
  bot chạy bằng systemd `anki-bot`, Anki headless trong Docker container tên `anki`
  (image `thisisnttheway/headless-anki`), AnkiConnect `127.0.0.1:8765`, VNC `127.0.0.1:5900`
  (cả 2 KHÔNG mở ra internet).
- GitHub: `sakuralegend/ankiagent` (private, VPS đọc qua deploy key).
- Deploy: double-click `deploy.bat` (hoặc `.\deploy.ps1`) — push → VPS pull → restart bot.
- Secrets: chỉ trong `.env` (PC + VPS, không có trong git). Đổi `.env` thì phải
  `scp .env root@161.248.146.56:/root/ankiagent/.env` + restart bot.
