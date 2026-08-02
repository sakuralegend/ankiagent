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
- [x] **`grammar_cache.json` kẹt deploy → hết hẳn file cache (QD-05 rồi QD-11).** Bài học duy nhất
      còn giá trị: số đo dùng để BÁC một hướng cũng hết hạn — "88 thẻ thiếu dữ liệu" (31/07) đo lại
      02/08 ra **0**, và chính hướng từng bị bác trở thành hướng thi hành. (chi tiết: `git log`)
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

### 🔴 Phát hiện 02/08/2026 khi chạy lô k20 (ĐÃ TRẢ 02/08/2026)

- [x] **Không cửa nào canh DỮ LIỆU NGỮ PHÁP máy nối vào thẻ → ĐÃ CÓ CỬA (QD-15). ĐÃ TRẢ 02/08/2026.**
      `кеды` bị nguồn đảo cách 5 với cách 6 (`inst=ке́де · prep=ке́дом`) ở cả số ít lẫn số nhiều;
      `soat`/`dodai` mù hoàn toàn vì chúng chỉ đo phần agent VIẾT, không đo phần `nap` NỐI vào.
      Nay `anki_tools/soat_nguphap.py` soi bản ghi **tự mâu thuẫn với luật hình thái** (khác hẳn
      hướng "đối chiếu chéo `nouns.csv`" đã bị bác — hai nguồn cùng thượng nguồn thì trùng nhau
      không chứng minh gì). Gọi ở `cao_nguphap.py` (dữ liệu VÀO — nên nợ ② *"cào lại là nguồn sai
      quay về, không ai báo"* cũng đóng: nay nó kêu to) và `congcu.py nap` (dữ liệu LÊN THẺ).
      **Đo:** 516 thẻ có bảng biến cách → **0 kêu oan**; bản ghi hỏng thật của `кеды` → bắt 2/2.
      6 test trong `tests/`, một trong số đó bắt được lỗi của chính cửa lúc viết (đuôi cách 6 phải
      tách theo số ít / số nhiều, vì `-ами` cũng kết thúc bằng `-и`).
      ⚠️ **Vẫn chỉ bắt kiểu đảo CẢ HAI CHIỀU.** Nguồn sai một chiều thì vẫn phải đọc bằng mắt.
      Bản vá gốc của `кеды` sao lưu ở `backups/_backup_grammarjson_kedy.json` (bị `.gitignore`).

### 🔴 Phát hiện + TRẢ LUÔN 02/08/2026 khi nghiệm thu cửa ngữ pháp

- [x] **8 thẻ có dòng tiếng Việt lệch giữa THẺ và FILE LÔ — `nap --tatca` từng sẽ lặng lẽ trả về
      bản cũ.** `покупать` (k14) + 7 từ ở k48: thẻ đã bỏ chữ "(chưa hoàn thành…)" cho đúng luật
      (badge `IMPF` in sẵn thứ đó ở mặt đề bài) mà `V[...]` trong repo còn giữ bản thừa. Đã sửa
      8 dòng `V[...]` cho khớp thẻ — **thẻ là bên đúng**. Nghiệm thu: `nap --tatca` chạy khan nay
      báo `doi tieng Viet 0 note` + `ghi vao 0 note` trên cả 334 từ.
      🔴 **Bài học chung, còn nguyên giá trị:** vá tay trên thẻ mà không vá file lô là đẻ ra một
      quả bom hẹn giờ — cùng HỌ với món `кеды` ở trên. Sửa nội dung thẻ thì phải hỏi **"chỗ này
      trong repo có bản của nó không"**; `nap` có in ra lúc đổi nhưng in giữa 300 dòng thì cũng
      như câm.

### 🟡 Vận hành — còn lại, chưa cấp thiết

- [ ] **Bot chỉ `print`, chưa có nhật ký phân mức.** `logging.basicConfig` không tồn tại ở đâu ⇒
      không lọc được theo mức, không tách được lỗi khỏi tiếng ồn. Khác với món "log bị xoá" đã trả
      ở trên: đây là chất lượng log, không phải mất log. **Đắt** (chạm cả 3 gói) mà lợi ích chưa
      cấp thiết ⇒ để sau khi xong 61 lô. (31/07/2026)
- [ ] **15 chỗ nuốt lỗi im lặng** (`except: pass` / `except Exception:` trống) trong 3 gói.
      **Không sửa hết ngay.** Áp luật từ nay: mọi `except` phải log, hoặc phải có comment nói vì sao
      được phép nuốt. (31/07/2026)
- [ ] **Không gì báo khi VPS chạy CODE CŨ hơn laptop.** Đo 02/08: lần deploy này kéo một cục **49
      file** vì VPS đứng ở commit 31/07 13:12 ⇒ bot chạy code cũ **3 ngày** mà không dấu hiệu nào.
      `deploy.ps1` (31/07) chỉ bắt được lúc pull HỎNG; **quên deploy** thì nó im hoàn toàn — mà quên
      mới là ca hay gặp. Hệ quả đã thấy: laptop và VPS chạy hai đời code khác nhau nhiều ngày, đúng
      môi trường đẻ ra lỗi lệch âm thầm. Hướng rẻ nhất: bot khai `git rev-parse --short HEAD` lúc
      khởi động + trong `/trangthai`, lệch thì mắt thấy ngay. CHẠM CODE BOT ⇒ deploy riêng.
      User chốt 02/08: *"tôi sẽ xử lí sau"*. (02/08/2026)

### 🟡 Code — rơi giữa hai ghế, không plan nào quản

- [x] **4 luật chuẩn hoá tiếng Nga khác nhau — ĐÃ ĐO 31/07/2026, ĐÓNG NỢ.** 1748 từ Nga thật, cả 4
      hàm, **0 bất đồng** — code vẫn khác hàm nhau (KHÔNG gộp, đúng dặn dò), chỉ là chưa có từ nào
      chạm trúng khác biệt. ⚠️ **Đo lại** nếu nạp dữ liệu từ nguồn copy-paste không rõ chuẩn hoá
      (dán thẳng từ web ngoài OpenRussian). Chi tiết: `git log`.
- [x] **Thư mục gốc vi phạm chính luật L2 — ĐÃ TRẢ 31/07/2026 (G3).** Gốc còn đúng ba file `.py`;
      thêm tên vào danh sách trắng S6 từ nay là **nới luật**, phải ghi `QUYETDINH.md` trước.

## Ý TƯỞNG (chưa làm, chờ xong 61 lô)

- **Lệnh `/moi` trong bot — đọc `PHIENBAN.md` ngay trong Telegram.** User xem "có gì mới" ở đúng chỗ
  họ thực sự dùng hệ thống, khỏi phải mở repo. Việc nhỏ (đọc file + gửi text, dùng `tgbot/` sẵn có)
  nhưng CHẠM CODE BOT nên phải deploy riêng có canary. User chốt 31/07/2026: *"chức năng đó để sau"*.
