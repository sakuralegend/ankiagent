# 🇷🇺 OpenRussian → Anki Flashcard Builder

Công cụ tự động cào dữ liệu từ [OpenRussian](https://en.openrussian.org/), dùng AI (Claude, qua
1 proxy OpenAI-compatible) để dịch nghĩa + viết ví dụ tự nhiên, rồi đẩy thẻ lên Anki qua
[AnkiConnect](https://ankiweb.net/shared/info/2055492159).

## 📁 Cấu trúc project

```
main.py                          # Vòng lặp chính: nhập từ, cào dữ liệu, đẩy lên Anki
anki_tools/
  config.py                      # ⚙️ TOÀN BỘ cấu hình (URL, API key, tên model...)
  utils.py                       # Hàm tiện ích nhỏ (log, xử lý chữ, bỏ dấu...)
  ai_client.py                   # Giao tiếp AI (Claude) - system prompt, few-shot, gọi API
  scraper.py                     # Cào dữ liệu từ trang OpenRussian
  html_builder.py                # Dựng HTML khối ví dụ (nhánh AI + nhánh fallback)
  anki_client.py                 # Giao tiếp AnkiConnect (tạo deck/model, đẩy note, in tóm tắt)
  templates/
    card.css                     # CSS chung cho thẻ
    front_template.html          # Mặt trước thẻ
    back_template.html           # Mặt sau thẻ (có nút "AI Refine" chạy JS ngay trong Anki)
```

## ⚙️ Cấu hình (`anki_tools/config.py`)

Đây là **nơi duy nhất** cần sửa khi muốn đổi endpoint AI, model, API key, hoặc địa chỉ AnkiConnect:

| Hằng số | Ý nghĩa |
|---|---|
| `ANKI_CONNECT_URL` | Địa chỉ AnkiConnect dùng bởi Python (mặc định `http://127.0.0.1:8765`) |
| `CLAUDE_API_URL` | Endpoint chat completions (OpenAI-compatible). Hiện trỏ tới lớp tương thích OpenAI của Gemini (`.../v1beta/openai/chat/completions`), có thể đổi lại sang proxy Claude hoặc endpoint OpenAI-compatible khác |
| `CLAUDE_API_KEY` | API key để gọi endpoint AI ở trên (hiện cần API key từ [Google AI Studio](https://aistudio.google.com/apikey) vì đang dùng Gemini) |
| `CLAUDE_MODEL` | Tên model AI dùng qua endpoint trên (hiện đang dùng `gemini-3.5-flash`, free tier; có thể đổi sang `gemini-2.5-flash`, `claude-haiku-4-5` qua proxy Claude, `gpt-4o-mini`, v.v.) |
| `OPENRUSSIAN_AUDIO_TEMPLATE` | Template URL lấy file audio phát âm từ OpenRussian |
| `MODEL_NAME` | Tên Note Type (model) sẽ tạo/cập nhật trong Anki |
| `ANKI_CONNECT_LOCAL_URL` / `ANKI_CONNECT_MOBILE_URL` | Địa chỉ AnkiConnect dùng bởi JS **chạy trong thẻ Anki** (khi bấm nút AI Refine) |

> Muốn đổi sang model Claude khác hoặc đổi proxy: chỉ cần sửa `CLAUDE_API_URL` /
> `CLAUDE_API_KEY` / `CLAUDE_MODEL` trong file này, KHÔNG cần sửa gì thêm — các giá trị này sẽ
> tự động được tiêm vào cả code Python và code JS trong thẻ khi bạn chạy lại `python main.py`
> (hàm `setup_anki_environment()` sẽ cập nhật lại template trong Anki).

## ▶️ Cách chạy

1. Mở Anki, đảm bảo add-on **AnkiConnect** đã cài và đang chạy.
2. Cài dependency: `pip install requests`
3. Chạy: `python main.py`
4. Nhập tên bộ bài (deck), sau đó nhập từng từ tiếng Nga muốn thêm. Gõ `exit`/`quit`/`thoát` để dừng,
   gõ `c` để đổi deck khác giữa chừng.

## 🤖 Luồng xử lý AI — 2 nơi cần đồng bộ khi update

Có **2 nơi hoàn toàn độc lập** cùng gọi AI, và bạn **PHẢI cập nhật cả 2** nếu đổi cách AI viết câu
hoặc đổi cấu trúc HTML của khối ví dụ:

1. **Lúc thêm thẻ mới** (Python, `anki_tools/ai_client.py` + `html_builder.py`):
   - `main.py` gọi `push_to_anki()` → `build_examples_html()` → `call_claude_ai()` /
     `call_claude_ai_freestyle()` → dựng HTML bằng `_build_example_block()`.
2. **Lúc bấm nút "🤖 Trợ lý AI Refine" ngay trong thẻ Anki** (JavaScript,
   `anki_tools/templates/back_template.html`):
   - Vì đây chạy trong webview của Anki (không có Python hỗ trợ), JS phải tự gọi `fetch()` đến
     Claude proxy và đến AnkiConnect, tự build lại HTML ví dụ bằng tay.

Để tránh 2 nơi này lệch nhau:
- **System prompt** (văn phong AI) chỉ viết ở `_CORE_SYSTEM_PROMPT` trong `ai_client.py`. Nó được
  tự động tiêm vào JS qua placeholder `__SYSTEM_PROMPT_JSON__` khi `setup_anki_environment()` chạy.
  → Muốn đổi văn phong, **chỉ sửa `ai_client.py`**, không sửa tay trong `back_template.html`.
- **Cấu trúc HTML khối ví dụ** (`class="example-toggle"`, `ex-ru`, `ex-en`, `ex-vi`...) được định
  nghĩa ở `_build_example_block()` trong `html_builder.py`, và được **lặp lại thủ công** trong đoạn
  JS build `examplesHtml` ở `back_template.html`. Nếu đổi cấu trúc/class CSS này, phải sửa **cả 2
  nơi** để card không hiển thị khác nhau tùy theo cách nó được tạo/sửa.
- **URL/API key/model AI** chỉ định nghĩa ở `config.py`, được tiêm vào JS qua các placeholder
  `__CLAUDE_API_URL__`, `__CLAUDE_API_KEY__`, `__CLAUDE_MODEL__` (xem `_build_back_template()`
  trong `anki_client.py`).

## ⚠️ Cảnh báo bảo mật (API key)

Nút "AI Refine" chạy trực tiếp trong webview Anki, không có Python đứng giữa. Vì vậy
`CLAUDE_API_KEY` (đọc từ `config.py`) sẽ được **nhúng thẳng vào mã nguồn của Note Type** (mặt sau
thẻ). Điều này có nghĩa:

- Bất kỳ ai xem "Card Info" / export deck / mở file `.apkg` của bạn đều có thể lấy được API key.
- Đây là rủi ro đã được cân nhắc và chấp nhận để đơn giản hóa kiến trúc (không cần chạy thêm 1
  server proxy Python nền chỉ để giữ key an toàn).
- **Không share deck này công khai** (ví dụ AnkiWeb, forum...) nếu không muốn lộ API key. Nếu cần
  share, hãy đổi key trong `config.py`, chạy lại `python main.py` để refresh template với key mới,
  rồi thu hồi (revoke) key cũ.

## 🔁 Nếu muốn đổi lại AI khác trong tương lai

Chỉ cần sửa:
1. `anki_tools/config.py` — đổi 3 hằng `CLAUDE_*`.
2. `anki_tools/ai_client.py` — hàm `_send_ai_request()` nếu cấu trúc request/response của
   endpoint mới khác chuẩn OpenAI (`messages` + `choices[0].message.content`).
3. `anki_tools/templates/back_template.html` — đoạn `fetch(urlAI, ...)` tương ứng, nếu format khác.

Sau đó chạy lại `python main.py` một lần để `setup_anki_environment()` cập nhật template mới vào
Anki (không cần làm gì thêm trong app Anki).
