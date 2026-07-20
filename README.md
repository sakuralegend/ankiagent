# 🇷🇺 Anki Agent — OpenRussian → Anki, điều khiển bằng Telegram, chạy 24/7 trên VPS

Hệ thống tự động xây thẻ Anki tiếng Nga: cào dữ liệu từ [OpenRussian](https://en.openrussian.org/),
dùng AI (Gemini, qua endpoint OpenAI-compatible) dịch nghĩa + viết ví dụ 3 thứ tiếng (Nga–Anh–Việt)
+ tự phân loại chủ đề, đẩy thẻ vào Anki qua [AnkiConnect](https://git.sr.ht/~foosoft/anki-connect),
rồi tự sync lên AnkiWeb để điện thoại kéo về. Toàn bộ thao tác hằng ngày làm qua **bot Telegram** —
kể cả **chụp ảnh trang sách để thêm từ hàng loạt** — không cần mở máy tính.

## ✨ Tính năng chính

- **Thêm từ**: gõ 1 từ tiếng Nga → cào + AI → thẻ đẹp có phát âm, nghĩa, 3 ví dụ song ngữ.
- **📷 Quét ảnh trang sách**: gửi ảnh → AI đọc mọi từ Nga, đưa về nguyên thể, lọc từ đã có →
  bạn **duyệt** danh sách rồi bot mới thêm hàng loạt (bot không bao giờ tự thêm).
- **Tag chủ đề + cây deck**: mỗi thẻ được AI gắn 1 tag `topic::<chủ đề>` (địa chỉ nhà), xếp vào
  cây deck `RUSSIAN::<chủ đề>` (vd `RUSSIAN::life::food`).
- **📥 Deck inbox**: từ mới gom vào `RUSSIAN::0-inbox` học một chỗ; thẻ tốt nghiệp learning thì
  job 3h sáng (hoặc `/don`) tự chuyển về deck chủ đề theo tag.
- **🔄 Làm lại thẻ (`/sua`)**: cào lại + AI sinh lại y như thẻ mới, **giữ nguyên tiến trình học**.
- **🔊 Âm thanh có phao dự phòng**: OpenRussian trước, lỗi 500 thì tự sinh giọng chuẩn tiếng Nga
  bằng Google Cloud TTS.
- **Chống hết quota AI**: model chính 429 → tự chuyển model dự phòng.

## 🏗 Kiến trúc

```
iPhone (Telegram) ──> tgbot/ ─────> pipeline.py ──> scraper (OpenRussian)
   │              (VPS, systemd)        │      ├──> ai_client (Gemini + fallback model)
   │                                    │      └──> audio (OpenRussian → Google TTS)
   │                                    └──> anki_client ──> AnkiConnect :8765 (nội bộ)
   │                                                            │
   │                                                Anki desktop headless (Docker
   │                                                thisisnttheway/headless-anki)
   │                                                            │ sync
   └───────── app Anki (bấm sync) <──────── AnkiWeb <───────────┘
```

- AnkiConnect (8765) và VNC (5900) chỉ bind `127.0.0.1` trên VPS — **không mở ra internet**.
- Bot dùng long-polling + whitelist đúng 1 Telegram user ID → không cần domain/SSL/port.
- Sau mỗi lần thêm/sửa thẻ, bot gọi sync → AnkiWeb → iPhone chỉ việc bấm sync trong app Anki.

## 📁 Cấu trúc project

```
bot.py               # Điểm vào bot Telegram (~10 dòng) — systemd chạy `python bot.py`
main.py              # CLI trên PC (python main.py — thêm từ bằng dòng lệnh)
tgbot/               # Ruột bot Telegram, tách theo luồng (một chiều core←flows←dispatch←app)
  core.py            #   phiên, deck hiện tại, menu, đồng hồ reset 3 phút, format thẻ
  commands.py        #   lệnh 1 phát: /start /menu /deck /thongke /don /sync + job 3h sáng
  flow_add.py        #   thêm từ: dò trùng, AI đoán từ nguyên mẫu
  flow_edit.py       #   /sua (làm lại 1 thẻ) + /suadeck (làm lại cả deck)
  flow_scan.py       #   📷 quét ảnh trang sách → duyệt → thêm loạt
  dispatch.py        #   bộ chia tin nhắn/nút bấm (on_word + on_callback), không chứa nghiệp vụ
  app.py             #   lắp handler + khởi động (long-polling, trần chờ HTTP nới rộng)
anki_tools/
  config.py          # Đọc cấu hình từ .env (KHÔNG còn secret nào nằm trong code)
  topics.py          # Nguồn chân lý danh sách chủ đề (TOPICS) + chuẩn hóa slug
  pipeline.py        # Logic dùng chung: process_word() thêm từ, redo_note() làm lại thẻ
  ai_client.py       # Gọi AI: sinh ví dụ, phân loại topic, đoán lemma, quét ảnh; chuỗi model 429
  scraper.py         # Cào dữ liệu OpenRussian
  audio.py           # Lấy phát âm: OpenRussian → Google Cloud TTS (phao dự phòng khi 500)
  html_builder.py    # NƠI DUY NHẤT dựng HTML khối ví dụ
  anki_client.py     # Giao tiếp AnkiConnect (deck/model/note/media/tag/sync)
  templates/         # CSS + HTML thẻ (tĩnh thuần — không có JS gọi AI trong thẻ)
tag_topics.py        # Gắn/đổi tag topic:: cho thẻ (bảng tra thủ công + AI cho thẻ lẻ)
build_subdecks.py    # Dựng cây deck RUSSIAN::<topic> + dọn thẻ về đúng deck con
setup_inbox.py       # Tạo deck inbox + ép luật ôn-trước-học-sau + gom thẻ chưa học vào inbox
fix_audio.py         # Vá thẻ đang thiếu tiếng (tải lại OpenRussian → Google TTS)
docker-compose.yml   # Container Anki headless trên VPS
setup_vps.sh         # Cài VPS lần đầu (Docker, swap, addon AnkiConnect, venv, systemd)
anki-bot.service     # systemd unit: bot tự chạy khi VPS khởi động, tự restart khi crash
deploy.ps1 / .bat    # Deploy từ PC: push GitHub → VPS pull → restart bot (1 lệnh)
VPS_SETUP.md         # Hướng dẫn cài VPS từng bước + xử lý lỗi thường gặp
CHANGELOG.md         # Nhật ký thay đổi (mỗi lần sửa gì đều ghi vào đây)
```

## ⚙️ Cấu hình — file `.env` (không đưa lên git)

Tạo từ mẫu: copy `.env.example` → `.env` rồi điền. `config.py` chỉ đọc, không chứa secret.

| Biến | Ý nghĩa |
|---|---|
| `CLAUDE_API_URL` | Endpoint chat completions OpenAI-compatible (đang dùng lớp OpenAI của Gemini) |
| `CLAUDE_API_KEY` | API key AI ([Google AI Studio](https://aistudio.google.com/apikey)) |
| `CLAUDE_MODEL` | Model chính (đang dùng `gemini-3.1-flash-lite` — 500 lượt free/ngày) |
| `CLAUDE_FALLBACK_MODELS` | Model dự phòng, tự chuyển khi model chính hết quota (lỗi 429) |
| `ANKI_CONNECT_URL` | Địa chỉ AnkiConnect (mặc định `http://127.0.0.1:8765`) |
| `TELEGRAM_BOT_TOKEN` | Token bot từ @BotFather |
| `TELEGRAM_USER_ID` | Telegram user ID duy nhất được phép dùng bot |
| `GOOGLE_TTS_API_KEY` | (tuỳ chọn) Key **Google Cloud** đã bật *Cloud Text-to-Speech API* — phao audio dự phòng. ⚠️ KHÁC key Gemini AI Studio; để trống thì bỏ qua phao |
| `GOOGLE_TTS_VOICE` | (tuỳ chọn) Giọng đọc, mặc định `ru-RU-Standard-A` (nữ). **Chỉ dùng giọng `*-Standard-*`** để nằm trong hạn mức miễn phí 4tr ký tự/tháng |
| `TOPIC_DECK_PARENT` | (tuỳ chọn) Tên deck kho, mặc định `RUSSIAN` |

## 📱 Dùng hằng ngày (trong Telegram)

| Muốn làm gì | Thao tác |
|---|---|
| Thêm từ | Gõ thẳng từ tiếng Nga, vd `хороший` → thẻ vào 📥 `RUSSIAN::0-inbox`, AI gắn tag chủ đề |
| Thêm hàng loạt từ sách | Gửi 📷 **ảnh** trang sách (dạng photo) → bot quét từ mới → bạn duyệt (nhắn `bỏ 3 7` để loại) → bấm ✅ Thêm |
| Từ không có trên OpenRussian | AI đoán từ nguyên mẫu (biến cách/sai chính tả) → bấm nút ✅ xác nhận hoặc 🚫 Hủy |
| Từ bị trùng | Bot hiện nút: Hủy / Chuyển deck / Xóa cũ + thêm mới / Vẫn thêm trùng |
| Thẻ AI bị khuyết (thiếu ví dụ) | Bot cảnh báo kèm 2 nút: 🔄 Làm lại thẻ / ⏭ Bỏ qua |
| Chọn deck cố định | `/deck` (hoặc nút 📚) → 🤖 tự động theo chủ đề / 🕘 deck gần nhất / 📂 có sẵn / ➕ mới |
| Làm lại 1 thẻ | `/sua` → gõ từ → bot cào lại + AI sinh lại (giữ nguyên tiến trình học), vá audio nếu thiếu |
| Làm lại cả deck | `/suadeck` → chọn deck → xác nhận → chạy nền có tin tiến độ + nút ⏹ Dừng (tốn nhiều AI) |
| Dọn inbox | `/don` — chuyển ngay thẻ tốt nghiệp learning từ inbox về deck chủ đề (job 3h sáng tự làm) |
| Thống kê chủ đề | `/thongke` — phân bố thẻ theo chủ đề + cảnh báo khi cần tách deck |
| Menu / ép sync | `/menu` / `/sync` |

Ghi chú: nghỉ >3 phút → bot **quên deck đang chọn** (về chế độ tự động — thẻ trong Anki không mất
gì) và gửi đúng 1 tin menu. Triết lý giao diện: **bấm chức năng trước, bot hỏi, rồi mới gõ từ** —
để dùng bàn phím tiếng Nga suốt phiên, không phải đổi bàn phím gõ lệnh Latin.

## 📥 Tag chủ đề, cây deck & inbox

- **Tag = địa chỉ nhà**: mỗi thẻ đúng 1 tag `topic::<slug>` do AI chọn (nguồn chân lý là
  `anki_tools/topics.py`). Deck chỉ là chỗ ở tạm; đổi cây deck không mất "địa chỉ".
- **Cây deck kho**: `RUSSIAN::<chủ đề>` (vd `RUSSIAN::life::food`), dựng bằng `build_subdecks.py`.
- **Inbox**: từ mới vào `RUSSIAN::0-inbox` (ưu tiên từ thêm gần nhất, 50 từ mới/ngày) để học gom
  một chỗ. Thẻ tốt nghiệp learning → `/don` hoặc job 3h sáng chuyển về `RUSSIAN::<tag>` để ôn.
- **Luật ôn tập**: ôn HẾT thẻ cũ (hạn cũ nhất trước) rồi mới hiện thẻ mới — ép trong `setup_inbox.py`.
- **Scripts vận hành** (chạy trên PC có Anki mở, mặc định dry-run, thêm `--apply` để làm thật):
  `tag_topics.py` (gắn/đổi tag), `build_subdecks.py` (dựng cây deck), `setup_inbox.py` (1 lần).

## 🔊 Âm thanh (phao dự phòng Google Cloud TTS)

Bot tự tải mp3 phát âm rồi lưu vào Anki: thử OpenRussian trước, nếu lỗi 500 thì gọi **Google Cloud
TTS** giọng Standard tiếng Nga. Điều kiện: điền `GOOGLE_TTS_API_KEY` (key Google Cloud, đã bật
*Cloud Text-to-Speech API* — **không** dùng được key Gemini AI Studio). Giọng Standard miễn phí
4 triệu ký tự/tháng nên với nhu cầu học từ thực tế là $0. Vá thẻ cũ đang thiếu tiếng:
`python fix_audio.py --apply`.

## 🤖 Luồng AI

- **Một nguồn chân lý duy nhất**: system prompt ở `_CORE_SYSTEM_PROMPT` (`ai_client.py`),
  HTML khối ví dụ ở `html_builder.py`. Không còn nơi thứ 2 phải đồng bộ.
- **Thêm & làm lại thẻ dùng chung** `build_card_fields()`: `/sua` tạo lại thẻ y hệt lúc thêm mới,
  chỉ khác là ghi đè cùng note nên tiến trình học không đổi. Kết quả AI được validate phía Python,
  thiếu ví dụ thì rơi về AI tự sinh (freestyle) rồi ví dụ thô — không để thẻ trắng.
- **Quét ảnh**: 1 request Gemini/trang (ảnh base64) OCR + đưa mọi từ về lemma; lọc từ đã có bằng
  danh sách `WordClean` toàn kho trước khi hỏi người dùng duyệt.
- **Hết quota không chết**: model chính 429 → tự thử lần lượt `CLAUDE_FALLBACK_MODELS`.

## 🔁 Quy trình phát triển

```
PC:  sửa code (Claude Code) → test → double-click deploy.bat (hoặc .\deploy.ps1)
     (tự động: git push → VPS git pull → pip install nếu cần → restart bot, ~10 giây)
```

- Không bị hỏi mật khẩu VPS: PC đã cài SSH key (`~/.ssh/id_ed25519`) chép lên VPS.
- Container Anki không bị đụng tới khi deploy — không downtime.
- Cài VPS lần đầu: xem [VPS_SETUP.md](VPS_SETUP.md) (7 bước + mục "Lỗi thường gặp").

## 🔐 Bảo mật

- Secrets chỉ nằm trong `.env` (bị `.gitignore` chặn) — code trên GitHub sạch key.
- API key **không còn bị nhúng vào thẻ Anki** (đã gỡ nút AI trong thẻ — mọi thao tác qua bot).
- AnkiConnect không có mật khẩu → tuyệt đối không mở port 8765/5900 ra internet;
  bot là cổng duy nhất, whitelist đúng 1 user ID.
- Key Google Cloud TTS nên **Restrict** chỉ cho *Cloud Text-to-Speech API* + đặt quota ký tự/ngày
  dưới ngưỡng free để không bao giờ phát sinh phí.

## 💻 Chạy CLI trên PC (tuỳ chọn)

1. Mở Anki desktop (có addon AnkiConnect).
2. `pip install -r requirements.txt`
3. `python main.py` → nhập deck → nhập từng từ (gõ `c` đổi deck, `exit` thoát).
