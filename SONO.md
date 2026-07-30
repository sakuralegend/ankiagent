# 💳 SỔ NỢ KỸ THUẬT

> Ghi khi vượt ngưỡng ở `CACHLAM.md` Q4 — KHÔNG sửa ngay giữa việc khác.
> Trả nợ khi: sắp sửa tiếp đúng file đó, hoặc sổ chạm 10 mục (dành một phiên riêng chỉ trả nợ).
> Định dạng: `- [ ] <file/hàm>: <ngưỡng nào vỡ> (ngày ghi)`

## Nợ

> Nợ **cấu trúc code** tồn đọng trước 30/07/2026 do `_fable_plan.md` (G0–G4) quản, không chép lại đây.
> Bên dưới là các món **plan đó KHÔNG quản** — phát hiện khi rà lại 31/07/2026.

### 🔴 Vận hành — hỏng thì mất dữ liệu hoặc mất nhiều giờ truy lỗi

- [ ] **Sao lưu chưa từng khôi phục thử.** `anki_tools/backup.py` chỉ biết TẠO `.apkg` + xoay vòng;
      grep `restore|khoi_phuc|importPackage` toàn repo = **rỗng**. Một bản sao lưu chưa khôi phục thử
      thì không phải bản sao lưu. Rủi ro lớn nhất đã tự nhận diện (full sync nhầm chiều) chính là loại
      xoá sạch. **Trả:** khôi phục 1 bản vào profile Anki RỖNG trên PC, đếm thẻ, mở 1 thẻ nhìn tận mắt,
      ghi 6 dòng các bước vào `VPS_SETUP.md`. (31/07/2026)
- [ ] **`requirements.txt` không ghim phiên bản** (`>=` cả 6 gói) mà `deploy.ps1` lại chạy
      `pip install -r requirements.txt` MỖI lần deploy ⇒ một bản `python-telegram-bot` mới có breaking
      change sẽ giết bot, **và nguyên nhân không nằm trong diff của bạn**. **Trả:** `pip freeze` trên
      VPS, ghim `==`. Nâng cấp phải là hành động có chủ đích. (31/07/2026)

### 🟡 Vận hành — cần thiết kế riêng, ĐỪNG làm trong đợt dọn G0–G4

- [ ] **Không có logging.** `logging.basicConfig` không tồn tại ở đâu; bot chỉ `print` ra journalctl,
      mà journalctl xoay vòng theo mặc định systemd ⇒ lỗi tuần trước có thể đã mất. (31/07/2026)
- [ ] **Không ai báo khi BOT chết.** `tgbot/alerts.py` gửi cảnh báo QUA CHÍNH BOT ⇒ bot chết thì im
      lặng tuyệt đối. `anki-bot.service` có `Restart=always`+`RestartSec=10` nhưng không có
      `StartLimitBurst`/`OnFailure=` ⇒ crash-loop quay vô hạn không ai biết. Cần một cơ chế báo
      ĐỘC LẬP với bot. (31/07/2026)
- [ ] **15 chỗ nuốt lỗi im lặng** (`except: pass` / `except Exception:` trống) trong 3 gói.
      **Không sửa hết ngay.** Áp luật từ nay: mọi `except` phải log, hoặc phải có comment nói vì sao
      được phép nuốt. (31/07/2026)

### 🟡 Code — rơi giữa hai ghế, không plan nào quản

- [ ] **4 luật chuẩn hoá tiếng Nga khác nhau.** `_fable_plan.md` nhắc đúng một lần ở dòng chẩn đoán
      rồi bỏ: không có trong G0–G4, không có trong bảng Q5 "cái không làm". `ai_client.py:422` có
      `unicodedata.normalize("NFC")`, `utils.py:24 strip_accents_perfectly` thì KHÔNG ⇒ hai hàm cùng
      mục đích cho **kết quả khác nhau với chữ `ё` dạng tổ hợp**. Đây là món **hỏng im lặng** duy nhất
      còn lại: không giết bot, chỉ làm thẻ sai âm thầm.
      **Trả (rẻ, rủi ro 0):** script CHỈ ĐỌC gom mọi từ Nga thật (`grammar_cache.json` + `tudien.json`
      + `WordClean` của thẻ), chạy cả 4 luật, in tập BẤT ĐỒNG. Rỗng ⇒ đóng nợ. Không rỗng ⇒ đó là lỗi
      thật, vá theo luật "kiểm ngược lô cũ" (CACHLAM). **KHÔNG gộp hàm trước khi đo.** (31/07/2026)
- [ ] **Thư mục gốc vi phạm chính luật L2 bảy lần.** L2: *"gốc chỉ chứa điểm vào đang sống"*. Sau G3
      của Fable, gốc vẫn còn **9 file `.py`** (S6 hợp thức bằng danh sách trắng = ghi nhận vi phạm chứ
      không sửa). Luật bị phá ngay ngày đầu bởi chính repo của nó là luật chết — đúng bệnh đã giết
      README. **Trả:** mở rộng G3 — dời 6 script còn lại xuống `scripts/` kèm 3 dòng bootstrap
      `sys.path` mỗi file (chúng thiếu, nên hiện chạy được chỉ nhờ nằm ở gốc); gốc còn đúng
      `bot.py`, `main.py`, `soatkientruc.py`. (31/07/2026)

## Ý TƯỞNG (chưa làm, chờ xong 61 lô)

_(trống)_
