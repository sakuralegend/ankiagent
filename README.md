# 🇷🇺 Anki Agent — OpenRussian → Anki, điều khiển bằng Telegram, chạy 24/7 trên VPS

Hệ thống tự động xây thẻ Anki tiếng Nga: cào dữ liệu từ [OpenRussian](https://en.openrussian.org/),
dùng AI (Gemini, qua endpoint OpenAI-compatible) dịch nghĩa + viết ví dụ 3 thứ tiếng (Nga–Anh–Việt)
+ tự phân loại chủ đề, đẩy thẻ vào Anki qua [AnkiConnect](https://git.sr.ht/~foosoft/anki-connect),
rồi tự sync lên AnkiWeb để điện thoại kéo về. Toàn bộ thao tác hằng ngày làm qua **bot Telegram** —
kể cả **chụp ảnh trang sách để thêm từ hàng loạt** — không cần mở máy tính.

## ✨ Làm được gì

- **Thêm từ**: gõ 1 từ tiếng Nga → cào + AI → thẻ có phát âm, nghĩa, 3 ví dụ song ngữ, tag chủ đề.
- **📷 Quét ảnh trang sách**: gửi ảnh → AI đọc mọi từ Nga, đưa về nguyên thể, lọc từ đã có → bạn
  **duyệt** rồi bot mới thêm (bot không bao giờ tự thêm).
- **📥 Inbox + cây deck theo chủ đề**: từ mới gom một chỗ để học; thẻ tốt nghiệp learning thì tự
  chuyển về deck chủ đề theo tag.
- **🔄 Làm lại thẻ** (`/sua`, `/suadeck`): cào lại + AI sinh lại, **giữ nguyên tiến trình học**.
- **⭐ Thẻ ngữ pháp** (`/dacbiet`): mảng thứ hai, tách hẳn — dạng số nhiều bất quy tắc, model riêng.
- **📖 Field hướng dẫn**: mỗi thẻ có phần chẻ gốc từ · cách nhớ · họ hàng, soạn theo lô có chuẩn
  và có cửa soát bằng máy.
- **🛡 Tự bảo vệ**: sync 2 chiều định kỳ + sao lưu `.apkg` hằng đêm (kèm lịch ôn), `/backup` để
  sao lưu ngay. Hỏng thì nhắn Telegram; thành công thì im lặng.
- **Chống hết quota AI**: model chính trả 429 → tự chuyển model dự phòng.

## 📚 Tài liệu — ai trả lời câu hỏi nào

Mỗi câu hỏi có **đúng một** file sở hữu nó. Đừng tìm câu trả lời ở hai nơi.

| Bạn muốn biết | Đọc |
|---|---|
| 👤 **Bot vừa có gì mới / sửa được gì?** (file DUY NHẤT cho người dùng) | **[PHIENBAN.md](PHIENBAN.md)** |
| Hệ thống là gì, chạy thế nào, **sửa ở đâu** | **[KIENTRUC.md](KIENTRUC.md)** |
| Luật làm việc trong repo (đọc trước khi sửa bất cứ gì) | [CLAUDE.md](CLAUDE.md) · sổ tay đầy đủ [CACHLAM.md](CACHLAM.md) |
| Vì sao chọn A mà không chọn B | [QUYETDINH.md](QUYETDINH.md) (`QD-nn`) |
| Nợ kỹ thuật đang có, điều kiện trả | [SONO.md](SONO.md) |
| Hôm qua/tuần trước đã đổi gì | [CHANGELOG.md](CHANGELOG.md) |
| Cài VPS lần đầu · lỗi thường gặp · khôi phục backup | [VPS_SETUP.md](VPS_SETUP.md) |
| Soạn một lô hướng dẫn thế nào, chuẩn nội dung ra sao | `data/huongdan/README.md` + `CHUAN.md` |

## ⚙️ Cấu hình — file `.env` (không đưa lên git)

Tạo từ mẫu: copy `.env.example` → `.env` rồi điền. `config.py` chỉ đọc, không chứa secret.

| Biến | Ý nghĩa |
|---|---|
| `CLAUDE_API_URL` · `CLAUDE_API_KEY` | Endpoint chat completions OpenAI-compatible + API key |
| `CLAUDE_MODEL` · `CLAUDE_FALLBACK_MODELS` | Model chính + model dự phòng (tự chuyển khi 429) |
| `ANKI_CONNECT_URL` | Địa chỉ AnkiConnect |
| `TELEGRAM_BOT_TOKEN` · `TELEGRAM_USER_ID` | Token bot + user ID **duy nhất** được phép dùng |
| `GOOGLE_TTS_API_KEY` · `GOOGLE_TTS_VOICE` | (tuỳ chọn) Phao audio. ⚠️ Key **Google Cloud** đã bật *Cloud Text-to-Speech API* — KHÁC key Gemini. Chỉ dùng giọng `*-Standard-*` để nằm trong hạn mức miễn phí |
| `TOPIC_DECK_PARENT` · `BACKUP_DIR` · `BACKUP_KEEP` | (tuỳ chọn) Tên deck kho, chỗ lưu và số bản backup |

## 🚀 Chạy

```bash
python bot.py            # bot Telegram (systemd chạy cái này trên VPS)
python main.py           # thêm từ bằng dòng lệnh trên PC (cần Anki desktop đang mở)
python soatkientruc.py   # cửa soát kiến trúc — bậc 1 của mọi lệnh nghiệm thu
.\deploy.ps1             # soát → import-check → push → VPS kéo code → restart bot
```

Bảng lệnh Telegram dùng hằng ngày nằm ở [VPS_SETUP.md](VPS_SETUP.md#dùng-hằng-ngày).

## 🔐 Bảo mật

- Secrets chỉ nằm trong `.env` (đã `.gitignore`) — code trên GitHub sạch key.
- AnkiConnect và VNC chỉ bind `127.0.0.1` trên VPS, **không mở ra internet**. Bot dùng long-polling
  + whitelist đúng 1 user ID nên không cần domain/SSL/mở port.
- Key Google Cloud TTS nên **Restrict** đúng một API + đặt quota dưới ngưỡng free.

---

📌 **Một điểm cần biết khi sửa code**: HTML mặt thẻ **đáng lẽ** chỉ dựng ở `anki_tools/html_builder.py`,
nhưng hiện thực tế còn hai nơi khác cũng tự dựng — đây là nợ đã ghi trong [SONO.md](SONO.md), và
`soatkientruc.py` mục S5 chặn không cho mọc thêm nơi thứ tư. Đừng tin câu "nơi duy nhất" ở bất cứ
đâu mà không chạy cửa soát.
