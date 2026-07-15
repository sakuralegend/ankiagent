# 🇷🇺 Anki Agent — OpenRussian → Anki, điều khiển bằng Telegram, chạy 24/7 trên VPS

Hệ thống tự động xây thẻ Anki tiếng Nga: cào dữ liệu từ [OpenRussian](https://en.openrussian.org/),
dùng AI (Gemini, qua endpoint OpenAI-compatible) dịch nghĩa + viết ví dụ 3 thứ tiếng (Nga–Anh–Việt),
đẩy thẻ vào Anki qua [AnkiConnect](https://git.sr.ht/~foosoft/anki-connect), rồi tự sync lên AnkiWeb
để điện thoại kéo về. Toàn bộ thao tác hằng ngày làm qua **bot Telegram** — không cần mở máy tính.

## 🏗 Kiến trúc

```
iPhone (Telegram) ──> bot.py ──> pipeline.py ──> scraper (OpenRussian)
   │                (VPS, systemd)    │      └──> ai_client (Gemini + fallback model)
   │                                  └──> anki_client ──> AnkiConnect :8765 (nội bộ)
   │                                                          │
   │                                              Anki desktop headless (Docker
   │                                              thisisnttheway/headless-anki)
   │                                                          │ sync
   └───────── app Anki (bấm sync) <──────── AnkiWeb <─────────┘
```

- AnkiConnect (8765) và VNC (5900) chỉ bind `127.0.0.1` trên VPS — **không mở ra internet**.
- Bot dùng long-polling + whitelist đúng 1 Telegram user ID → không cần domain/SSL/port.
- Sau mỗi lần thêm/sửa thẻ, bot gọi sync → AnkiWeb → iPhone chỉ việc bấm sync trong app Anki.

## 📁 Cấu trúc project

```
bot.py               # Bot Telegram (giao diện chính hằng ngày, chạy 24/7 trên VPS)
main.py              # CLI trên PC (vẫn dùng được y hệt trước: python main.py)
anki_tools/
  config.py          # Đọc cấu hình từ .env (KHÔNG còn secret nào nằm trong code)
  pipeline.py        # Logic dùng chung: process_word() thêm từ, refine_note() sửa thẻ
  ai_client.py       # Gọi AI: system prompt, OUTPUT CONTRACT khi sửa thẻ, preset 1/2/3,
                     #   validate kết quả, chuỗi model dự phòng khi hết quota (429)
  scraper.py         # Cào dữ liệu OpenRussian
  html_builder.py    # NƠI DUY NHẤT dựng HTML khối ví dụ (thêm mới + sửa thẻ đều qua đây)
  anki_client.py     # Giao tiếp AnkiConnect (deck/model/note/sync)
  templates/         # CSS + HTML thẻ (tĩnh thuần — không còn JS gọi AI trong thẻ)
docker-compose.yml   # Container Anki headless trên VPS
setup_vps.sh         # Cài VPS lần đầu (Docker, swap, addon AnkiConnect, venv, systemd)
anki-bot.service     # systemd unit: bot tự chạy khi VPS khởi động, tự restart khi crash
deploy.ps1           # Deploy từ PC: push GitHub → VPS pull → restart bot (1 lệnh)
deploy.bat           # Vỏ bọc deploy.ps1 — double-click là deploy, khỏi mở PowerShell
VPS_SETUP.md         # Hướng dẫn cài VPS từng bước + xử lý lỗi thường gặp
CHANGELOG.md         # Nhật ký thay đổi (mỗi lần sửa gì đều ghi vào đây)
```

## ⚙️ Cấu hình — file `.env` (không đưa lên git)

Tạo từ mẫu: copy `.env.example` → `.env` rồi điền. `config.py` chỉ đọc, không chứa secret.

| Biến | Ý nghĩa |
|---|---|
| `CLAUDE_API_URL` | Endpoint chat completions OpenAI-compatible (đang dùng lớp OpenAI của Gemini) |
| `CLAUDE_API_KEY` | API key ([Google AI Studio](https://aistudio.google.com/apikey)) |
| `CLAUDE_MODEL` | Model chính (đang dùng `gemini-3.1-flash-lite` — 500 lượt free/ngày) |
| `CLAUDE_FALLBACK_MODELS` | Model dự phòng, tự chuyển khi model chính hết quota (lỗi 429) |
| `ANKI_CONNECT_URL` | Địa chỉ AnkiConnect (mặc định `http://127.0.0.1:8765`) |
| `TELEGRAM_BOT_TOKEN` | Token bot từ @BotFather |
| `TELEGRAM_USER_ID` | Telegram user ID duy nhất được phép dùng bot |

## 📱 Dùng hằng ngày (trong Telegram)

| Muốn làm gì | Thao tác |
|---|---|
| Bắt đầu phiên | Nhắn gì đó → bấm nút chọn deck: 📂 deck có sẵn (liệt kê hết) / ➕ tạo mới |
| Thêm từ | Gõ thẳng từ tiếng Nga, vd `хороший` |
| Từ không có trên OpenRussian | AI đoán từ nguyên mẫu (biến cách/sai chính tả) → bấm nút ✅ xác nhận hoặc 🚫 Hủy |
| Từ bị trùng | Bot hiện nút: Hủy / Chuyển deck / Xóa cũ + thêm mới / Vẫn thêm trùng |
| Thẻ AI bị khuyết (thiếu ví dụ) | Bot cảnh báo kèm 2 nút: 🔧 Tự sửa (chạy preset đổi ví dụ) / ⏭ Bỏ qua |
| Đổi deck | `/deck` (hoặc nút 📚 trong menu) → bảng chọn deck bằng nút |
| Sửa thẻ | `/sua` (hoặc nút ✏️) → bot hỏi từ → gõ từ → chọn nút **1** Ngắn hơn / **2** Đổi ví dụ / **3** Dài hơn / Tự viết |
| Sửa theo ý mình | Trong bảng kiểu sửa bấm **Tự viết yêu cầu** → gõ thẳng yêu cầu |
| Sửa TOÀN BỘ deck (ít dùng) | `/suadeck` → chọn deck → kiểu sửa → màn xác nhận → chạy nền có tin tiến độ tự cập nhật + nút ⏹ Dừng |
| Menu nút bấm | `/menu` (hoặc chờ — nghỉ >3 phút bot tự reset phiên và gửi menu) |
| Ép sync ngay | `/sync` |

Ghi chú: nghỉ >3 phút → bot **quên deck đang chọn** (chống thêm nhầm deck — thẻ trong
Anki không mất gì) và gửi đúng 1 tin: báo đã reset + menu nút bấm y hệt `/menu`.

Triết lý giao diện: **bấm chức năng trước, bot hỏi, rồi mới gõ từ** — nhờ vậy chỉ cần
để bàn phím tiếng Nga suốt phiên, không phải đổi bàn phím gõ lệnh Latin.
(`/deck <tên>`, `/sua <từ> [yêu cầu]` vẫn chạy như đường tắt cho ai thích gõ 1 dòng.)

## 🤖 Luồng AI

- **Một nguồn chân lý duy nhất**: system prompt ở `_CORE_SYSTEM_PROMPT` (`ai_client.py`),
  HTML khối ví dụ ở `html_builder.py`. Không còn nơi thứ 2 phải đồng bộ.
- **Sửa thẻ (`/sua`) có OUTPUT CONTRACT cứng**: yêu cầu kiểu "ngắn đi" không thể khiến AI trả
  thiếu ví dụ — luôn phải đủ nghĩa tiếng Việt + đúng 3 ví dụ đủ ru/en/vi có `<hl>` highlight.
  Kết quả được validate phía Python, sai thì retry 1 lần, vẫn sai thì **không ghi đè thẻ**.
- **Hết quota không chết**: model chính 429 → tự thử lần lượt các model trong
  `CLAUDE_FALLBACK_MODELS`; tất cả đều hỏng mới rơi về ví dụ thô từ từ điển.

## 🔁 Quy trình phát triển

```
PC:  sửa code (Claude Code) → test → double-click deploy.bat (hoặc .\deploy.ps1)
     (tự động: git push → VPS git pull → pip install nếu cần → restart bot, ~10 giây)
```

Không bị hỏi mật khẩu VPS: PC đã cài SSH key (`~/.ssh/id_ed25519`) chép lên VPS.

Container Anki không bị đụng tới khi deploy — không downtime.

Cài VPS lần đầu: xem [VPS_SETUP.md](VPS_SETUP.md) (7 bước + mục "Lỗi thường gặp").

## 🔐 Bảo mật

- Secrets chỉ nằm trong `.env` (bị `.gitignore` chặn) — code trên GitHub sạch key.
- API key **không còn bị nhúng vào thẻ Anki** (nút AI Refine trong thẻ đã gỡ — sửa thẻ qua bot).
- AnkiConnect không có mật khẩu → tuyệt đối không mở port 8765/5900 ra internet;
  bot là cổng duy nhất, whitelist đúng 1 user ID.

## 💻 Chạy CLI trên PC (tuỳ chọn, như bản gốc)

1. Mở Anki desktop (có addon AnkiConnect).
2. `pip install -r requirements.txt`
3. `python main.py` → nhập deck → nhập từng từ (gõ `c` đổi deck, `exit` thoát).
