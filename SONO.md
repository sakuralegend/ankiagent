# 💳 SỔ NỢ KỸ THUẬT

> Ghi khi vượt ngưỡng ở `CACHLAM.md` Q4 — KHÔNG sửa ngay giữa việc khác.
> Trả nợ khi: sắp sửa tiếp đúng file đó, hoặc sổ chạm 10 mục (dành một phiên riêng chỉ trả nợ).
> Định dạng: `- [ ] <file/hàm>: <ngưỡng nào vỡ> (ngày ghi)`

## Nợ

> Nợ **cấu trúc code** tồn đọng trước 30/07/2026 do `_fable_plan.md` (G0–G4) quản, không chép lại đây.
> Bên dưới là các món **plan đó KHÔNG quản** — phát hiện khi rà lại 31/07/2026.

### 🔴 Vận hành — hỏng thì mất dữ liệu hoặc mất nhiều giờ truy lỗi (ĐÃ TRẢ 31/07/2026)

- [x] **Sao lưu chưa từng khôi phục thử.** Đã khôi phục `backups/2026-07-29_1225/RUSSIAN.apkg` vào
      profile Anki RỖNG trên PC qua AnkiConnect: 950/950 note phục hồi đúng, xem tận field 1 thẻ
      (`да`) còn nguyên chữ Nga/tiếng Việt. Các bước ghi ở `VPS_SETUP.md` mục "Khôi phục thử một bản
      `.apkg`". (31/07/2026)
- [x] **`requirements.txt` không ghim phiên bản.** Đã `pip freeze` trên VPS lấy đúng bản đang chạy
      thật, ghim `==` cho cả 6 gói. Nâng cấp từ nay là hành động có chủ đích. (31/07/2026)

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

- [x] **4 luật chuẩn hoá tiếng Nga khác nhau — ĐÃ ĐO 31/07/2026, ĐÓNG NỢ.** Script chỉ đọc
      `_daxong/_va_do_bat_dong_chuan_hoa.py` gom 1748 từ Nga thật (`grammar_cache.json` 978 +
      `tudien.json` 976 + `Word`/`WordClean` của mọi thẻ RU_Word qua AnkiConnect), chạy cả 4 hàm:
      **A/B** (`utils.strip_accents_perfectly` vs công thức NFC-normalize của `ai_client._clean_scan_word`,
      cùng mục đích) → **0 bất đồng**; **C/D** (`bare()` của `congcu.py` vs `kiemtra.py`, cùng mục
      đích tra `nouns.csv`) → **0 bất đồng**. Rủi ro `ё` dạng tổ hợp (е + U+0308) mà `_fable_plan.md`
      nghi ngờ chưa từng xảy ra trên dữ liệu thật hiện có — code vẫn khác hàm nhau (KHÔNG gộp, đúng
      dặn dò), chỉ là chưa có từ nào chạm trúng khác biệt đó. Đo lại nếu sau này nạp dữ liệu từ nguồn
      copy-paste không rõ chuẩn hoá (vd dán trực tiếp từ web ngoài OpenRussian).
- [x] **Thư mục gốc vi phạm chính luật L2 — ĐÃ TRẢ 31/07/2026 (G3 mở rộng).** Gốc nay còn **đúng ba**
      file `.py` (`bot.py`, `main.py`, `soatkientruc.py`); 6 script vận hành xuống `scripts/`, 2 script
      chạy-một-lần vào `_daxong/`, mỗi file thêm 3 dòng bootstrap `sys.path` (chúng đều thiếu, trước
      đây chạy được chỉ nhờ nằm ở gốc). Danh sách trắng S6 thu về đúng 3 tên — thêm tên vào đó từ nay
      là **nới luật**, phải ghi `QUYETDINH.md` trước. (31/07/2026)

## Ý TƯỞNG (chưa làm, chờ xong 61 lô)

_(trống)_
