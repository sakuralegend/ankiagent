# 💳 SỔ NỢ KỸ THUẬT

> Ghi khi vượt ngưỡng ở `CACHLAM.md` Q4 — KHÔNG sửa ngay giữa việc khác.
> Trả nợ khi: sắp sửa tiếp đúng file đó, hoặc sổ chạm 10 mục (dành một phiên riêng chỉ trả nợ).
> Định dạng: `- [ ] <file/hàm>: <ngưỡng nào vỡ> (ngày ghi)`

## Nợ

### 🔴 Vận hành — hỏng thì mất dữ liệu hoặc mất nhiều giờ truy lỗi (ĐÃ TRẢ 31/07/2026)

- [x] **Sao lưu chưa từng khôi phục thử.** Đã khôi phục thật vào profile Anki RỖNG: 950/950 note
      đúng. Các bước ghi ở `VPS_SETUP.md` mục "Khôi phục thử một bản `.apkg`". (31/07/2026)
- [x] **`requirements.txt` không ghim phiên bản.** Đã `pip freeze` trên VPS lấy đúng bản đang chạy
      thật, ghim `==` cho cả 6 gói. Nâng cấp từ nay là hành động có chủ đích. (31/07/2026)

### 🟡 Vận hành — ĐÃ TRẢ 31/07/2026 (user duyệt cả ba)

- [x] **Không ai báo khi BOT chết → ĐÃ CÓ CHUÔNG (QD-04).** `scripts/canhbao_bot_chet.sh` gọi thẳng
      Telegram bằng `curl`, **không nạp dòng code Python nào của dự án** — đó là cả điểm của nó.
- [x] **`grammar_cache.json` kẹt deploy → hết hẳn file cache (QD-05 rồi QD-11).** Bài học duy nhất
      còn giá trị: **số đo dùng để BÁC một hướng cũng hết hạn** — "88 thẻ thiếu" (31/07) đo lại 02/08
      ra **0**, và chính hướng từng bị bác trở thành hướng thi hành.
- [x] **Log xoay vòng mất dấu → ĐÃ ĐẶT TRẦN** `SystemMaxUse=500M` + `MaxRetentionSec=3month`.

### 🔴 Tự soi 31/07/2026 — AI tự tìm ra, user KHÔNG phải người phát hiện

- [x] **DỰ ÁN KHÔNG CÓ TEST NÀO → ĐÃ CÓ `tests/`, và nó BẮT ĐƯỢC BUG THẬT NGAY LẦN CHẠY ĐẦU.**
      20 test bằng `unittest` (stdlib, không thêm phụ thuộc), chạy offline ~0,1 giây, cắm vào
      `deploy.ps1`. Nguyên tắc cố ý HẸP: **chỉ test chỗ ĐÃ HỎNG THẬT một lần**, không đuổi độ phủ.
      **Thu hoạch ngay:** `suy_giong()` phán `дя́дя` (giống ĐỰC, biến cách như giống cái) là `'f'`.
      Đã vá bằng cờ `animate`: đồ vật đuôi -а/-я thì kết luận giống cái, **người thì im lặng**.
      (31/07/2026)
- [x] **`soatkientruc.py` không ai canh → ĐÃ CÓ `tests/test_soatkientruc.py` (03/08/2026).**
      Repo giả trong thư mục tạm, kỳ vọng đúng mục nào ĐỎ/im. KHÔNG tách file (phá QD-02 —
      user duyệt 03/08). ⚠️ Vẫn "đừng thêm mục soát mới mà không thêm test tương ứng".
      🔴 **NAY ĐÚNG 700/700 DÒNG — hết chỗ.** Đã tháo `PHUT_DOC` ra `soat_nguong.json` + nén chú
      thích trùng QD (QD-21) mới nhét vừa S12–S14; muốn thêm cửa nữa là phải bàn lại QD-02.
- [x] **Thiếu lớp chặn sớm của git → ĐÃ CÓ `commit-msg` hook.** `scripts/hook-commit-msg` +
      `scripts/caidat_hook.sh` (cài một lần mỗi máy). Chặn NGAY lúc `git commit` thay vì đợi tới
      deploy. Giữ cả S9: hook nằm ngoài repo nên không tự đi theo sang máy/AI khác, S9 thì đi cùng
      repo — hai lớp không thừa. Đã thử: commit "sua linh tinh" bị chặn. (31/07/2026)
- [x] **Trần S10 đo sai hai lần, nay mới đúng (31/07 → 03/08, QD-20).** Bản 1 đếm dòng lấy từ
      "hiện tại + biên độ" — con số tuỳ tiện. Bản 2 đổi sang **ngân sách phút**, đúng ý niệm nhưng
      vẫn quy ra **dòng**. Bản 3 (03/08) quy ra **KÝ TỰ**: đo ra ký tự/dòng chạy từ 49 tới 140 giữa
      các file, nên đếm dòng bỏ lọt hẳn `QUYETDINH.md` (149/150 dòng "còn chỗ" mà nặng 30 KB, dòng
      dài nhất 1090 ký tự). Ngân sách hiện hành nằm trong `PHUT_DOC`, có ghi số đo cạnh từng dòng.
      🔴 Bài học: **đơn vị đo sai thì cửa soát vẫn XANH trong khi thứ nó canh đã hỏng.**

### 🔴 Phát hiện + TRẢ LUÔN 02/08/2026 (chi tiết: `git log`)

- [x] **Không cửa nào canh DỮ LIỆU NGỮ PHÁP máy nối vào thẻ → ĐÃ CÓ CỬA (QD-15).**
      `anki_tools/soat_nguphap.py` soi bản ghi tự mâu thuẫn với luật hình thái, gọi ở
      `cao_nguphap.py` (dữ liệu VÀO) và `congcu.py nap` (dữ liệu LÊN THẺ). Đo: 516 thẻ → 0 kêu oan.
      ⚠️ **Vẫn chỉ bắt kiểu đảo CẢ HAI CHIỀU.** Nguồn sai một chiều thì vẫn phải đọc bằng mắt.
- [x] **8 thẻ có dòng tiếng Việt lệch giữa THẺ và FILE LÔ** — `nap --tatca` từng sẽ lặng lẽ trả về
      bản cũ. Đã sửa 8 dòng `V[...]` cho khớp thẻ (**thẻ là bên đúng**).
      🔴 **Bài học còn nguyên giá trị:** vá tay trên thẻ mà không vá file lô là quả bom hẹn giờ.
      Sửa nội dung thẻ thì phải hỏi **"chỗ này trong repo có bản của nó không"**; `nap` có in ra
      lúc đổi nhưng in giữa 300 dòng thì cũng như câm.

### 🔴 Phát hiện + TRẢ LUÔN 03/08/2026 — chiều NGƯỢC của QD-16

- [x] **Không gì canh thẻ LỆCH deck ↔ nhãn `Stage` → ĐÃ CÓ CỬA CANH (QD-17).**
      ⚠️ **Chỉ dò rồi vá lại, KHÔNG chặn được nguyên nhân gốc** (Anki xử xung đột sync RIÊNG cho
      note và RIÊNG cho thẻ) — thẻ vẫn có thể sai mặt tối đa ~40 phút. Muốn hết hẳn thì phải để
      thiết bị sync xong rồi mới học.

### 🟡 Vận hành — còn lại, chưa cấp thiết

- [ ] **`tgbot/dispatch.py` 430 dòng, vượt trần 400 — user duyệt 03/08: KHÔNG tách.** `on_callback`
      ~320 dòng là một chuỗi nhánh nút; tách buộc cắt ruột hàm, lưới an toàn không phủ kín, mà bot
      là nơi lỗi chết im lặng. Đổi lại luật: **cấm thêm nhánh nút mới vào `on_callback`** — nhánh
      mới viết hàm ở file riêng cùng tầng rồi gọi một dòng từ `on_callback`. (03/08/2026)
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

- [x] **4 luật chuẩn hoá tiếng Nga khác nhau — ĐÃ ĐO 31/07, ĐÓNG NỢ.** 1748 từ thật, **0 bất đồng**;
      KHÔNG gộp (đúng dặn dò). ⚠️ **Đo lại** nếu nạp dữ liệu dán thẳng từ web ngoài OpenRussian.
- [x] **Gốc vi phạm luật L2 — ĐÃ TRẢ 31/07.** Cửa S6 canh, **S6 là bản ghi**.

## Ý TƯỞNG (chờ hết hàng đợi kho)

- **Lệnh `/moi` trong bot — đọc `PHIENBAN.md` ngay trong Telegram.** User xem "có gì mới" ở đúng chỗ
  họ thực sự dùng hệ thống, khỏi phải mở repo. Việc nhỏ (đọc file + gửi text, dùng `tgbot/` sẵn có)
  nhưng CHẠM CODE BOT nên phải deploy riêng có canary. User chốt 31/07/2026: *"chức năng đó để sau"*.
