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

### 🟡 Vận hành — ĐÃ TRẢ 31/07/2026 (user duyệt cả ba)

- [x] **Không ai báo khi BOT chết → ĐÃ CÓ CHUÔNG (QD-04).** `scripts/canhbao_bot_chet.sh` nói thẳng
      với Telegram bằng `curl`, không nạp dòng code Python nào của dự án. Hai lớp: systemd
      `OnFailure=` (chết hẳn = 5 lần khởi động trong 5 phút) + cron 15′ bắt trường hợp bị dừng hẳn.
      Chống spam bằng mốc trạng thái ⇒ bot chết cả ngày = ĐÚNG MỘT tin, và có tin báo khi sống lại.
      **Đã thử thật:** Telegram trả `ok:true`; stop bot → bắt được; start lại → báo "đã chạy lại";
      gọi thêm 2 lần → im lặng. (31/07/2026)
- [x] **`grammar_cache.json` kẹt deploy → ĐÃ TÁCH CHỖ GHI (QD-05).** Bot trên VPS nay ghi vào
      `/root/anki-cache/` (biến `ANKI_GRAMMAR_CACHE`), ngoài repo ⇒ repo không bao giờ bẩn.
      **Đã đo và BÁC hướng cũ** ("bỏ cache, đọc field `GrammarJSON`"): cache bao trùm thẻ, 88 thẻ
      thiếu hẳn `present`/`future`/`parts`. (31/07/2026)
      ⬆️ **BỊ QD-11 THAY THẾ 02/08/2026** — lý do bác đã chết (đo lại: thẻ khớp cache 100%), nên
      chính hướng cũ này được thi hành: bỏ hẳn file, đọc thẳng `GrammarJSON`. Mục này giữ nguyên
      làm sử, không phải hướng dẫn còn hiệu lực.
- [x] **Log xoay vòng mất dấu → ĐÃ ĐẶT TRẦN.** `SystemMaxUse=500M` + `MaxRetentionSec=3month`.
      Đo trước khi sửa: log vẫn còn từ 14/07 (~17 ngày, 212 MB) nên món này nhẹ hơn lo ngại — việc
      thật chỉ là chặn phình vô hạn. Bản gốc lưu ở `/root/journald.conf.bak`. (31/07/2026)

### 🔴 Tự soi 31/07/2026 — AI tự tìm ra, user KHÔNG phải người phát hiện

- [x] **DỰ ÁN KHÔNG CÓ TEST NÀO → ĐÃ CÓ `tests/`, và nó BẮT ĐƯỢC BUG THẬT NGAY LẦN CHẠY ĐẦU.**
      20 test bằng `unittest` (stdlib, không thêm phụ thuộc), chạy offline ~0,1 giây, cắm vào
      `deploy.ps1`. Nguyên tắc cố ý HẸP: **chỉ test chỗ ĐÃ HỎNG THẬT một lần**, không đuổi độ phủ.
      **Thu hoạch ngay:** `suy_giong()` phán `дя́дя` (giống ĐỰC, biến cách như giống cái) là `'f'` —
      comment cảnh báo đúng ca này lại nằm nhầm nhánh nên vô tác dụng. Đo ra **chưa thẻ nào sai**
      (từ điển đã ghi giống cho cả nhóm) nhưng sẽ nổ ngay khi user thêm `дя́дя`/`па́па`/`де́душка`.
      Đã vá bằng cờ `animate`: đồ vật đuôi -а/-я thì kết luận giống cái, **người thì im lặng**.
      Kiểm ngược trên thẻ thật: badge không đổi ca nào. (31/07/2026)
- [ ] **`soatkientruc.py` đã 578 dòng — vượt ngưỡng 400 dòng do CHÍNH `CLAUDE.md` đặt**, và **không
      có gì canh chính nó**: S10 chỉ canh file `.md`, S6 chỉ canh tên file ở gốc. Thứ đang chặn
      deploy mà sai thì hoặc chặn oan hoặc bỏ lọt, không ai biết. Liên quan trực tiếp món trên: cách
      canh nó đúng nhất là **test cho chính nó** (cho một repo giả, kỳ vọng đúng mục nào ĐỎ).
      (31/07/2026)
- [x] **Thiếu lớp chặn sớm của git → ĐÃ CÓ `commit-msg` hook.** `scripts/hook-commit-msg` +
      `scripts/caidat_hook.sh` (cài một lần mỗi máy). Chặn NGAY lúc `git commit` thay vì đợi tới
      deploy. Giữ cả S9: hook nằm ngoài repo nên không tự đi theo sang máy/AI khác, S9 thì đi cùng
      repo — hai lớp không thừa. Đã thử: commit "sua linh tinh" bị chặn. (31/07/2026)
- [x] **Trần S10 hết tuỳ tiện → đổi đơn vị sang PHÚT ĐỌC.** Trước là số dòng lấy từ "hiện tại +
      biên độ" (đúng loại con số đếm được mà `KIENTRUC.md` tự cấm). Nay đặt **ngân sách phút** —
      `CLAUDE.md` 3 phút (nạp mỗi phiên), `KIENTRUC.md`/`CACHLAM.md` 8, `SONO.md` 4, `QUYETDINH.md`
      5, `README.md` 3 — máy tự quy ra dòng (~30 dòng/phút). Con số phút thì người đặt và bảo vệ
      được; số dòng thì không. (31/07/2026)

### 🟡 Vận hành — còn lại, chưa cấp thiết

- [ ] **Bot chỉ `print`, chưa có nhật ký phân mức.** `logging.basicConfig` không tồn tại ở đâu ⇒
      không lọc được theo mức, không tách được lỗi khỏi tiếng ồn. Khác với món "log bị xoá" đã trả
      ở trên: đây là chất lượng log, không phải mất log. **Đắt** (chạm cả 3 gói) mà lợi ích chưa
      cấp thiết ⇒ để sau khi xong 61 lô. (31/07/2026)
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

- **Xoá hẳn `CHANGELOG.md` + dọn mọi con trỏ tới nó (QD-14, duyệt 02/08/2026).** File đã đóng sổ từ
  QD-06, không ai đọc, không còn nằm trong danh sách file `soatkientruc.py` S10 bắt đọc. `grep
  CHANGELOG` ra **18 file** còn nhắc tên nó — rà từng chỗ trước khi xoá: CON TRỎ CHỨC NĂNG (vd
  `README.md:35` đang trỏ sai, đáng lẽ chỉ sang `git log`) thì sửa/xoá; GHI CHÉP LỊCH SỬ (vd mục
  QD-06 kể chuyện đóng sổ) thì GIỮ NGUYÊN. Xếp SAU phiếu QD-11 đang chạy trong `VIECDANGLAM.md`.

- **Lệnh `/moi` trong bot — đọc `PHIENBAN.md` ngay trong Telegram.** User xem "có gì mới" ở đúng chỗ
  họ thực sự dùng hệ thống, khỏi phải mở repo. Việc nhỏ (đọc file + gửi text, dùng `tgbot/` sẵn có)
  nhưng CHẠM CODE BOT nên phải deploy riêng có canary. User chốt 31/07/2026: *"chức năng đó để sau"*.
