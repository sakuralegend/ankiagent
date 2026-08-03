# 🎯 VIỆC ĐANG LÀM
> Phiếu này bị GHI ĐÈ ở việc kế tiếp. Xong việc thì xoá nội dung, để lại đúng dòng tiêu đề.

## Việc: tách các file quá dài (refactor thuần, hành vi không đổi một ký tự)

**8 file vượt trần dòng** (CLAUDE.md: >400 đừng thêm, >700 phải tách):
`grammar.py` 1309 · `anki_client.py` 1006 · `kho/congcu.py` 912 · `soatkientruc.py` 673 ·
`ai_client.py` 502 · `tgbot/core.py` 437 · `tgbot/commands.py` 434 · `tgbot/dispatch.py` 430.

**Luật cứng user đặt:** refactor thuần (thấy bug thì ghi SONO, không sửa) · lưới file vàng dựng
TRƯỚC mỗi file (chạy hàm chỉ-đọc trên dữ liệu thật, tách xong diff từng ký tự, khác 0 = hoàn tác) ·
một file một commit, hết mỗi đợt DỪNG chờ duyệt · 3 cửa nghiệm thu xanh mỗi commit · tổng dòng
không được phình · không đụng kNN_*.py, lo*_*.py.

**Thứ tự:** đợt 1 `dispatch → commands → core` · đợt 2 `ai_client → congcu` ·
đợt 3 `anki_client → grammar` · cuối `soatkientruc` (viết test cho nó TRƯỚC — nợ SONO 31/07).

**Đã đo 03/08 trước khi trình kế hoạch:**
- 3 cửa nền đều XANH (soát sạch, import sạch, 38 test OK). Anki PC đang mở → chạy được file vàng.
- Kho đang giữa mùa: **36/64 lô** — mọi lô còn lại đi qua `grammar.py` (lệnh `nap` nối bảng chia).
  `_fable_plan.md` Q5 từng chốt KHÔNG tách grammar.py tới khi đủ 3 điều kiện; nay mới đạt 0/3
  (còn 28 lô · chưa đo 14 ngày xanh · caller kho/ vẫn gọi tên private `_cache`×4, `_BANG_RE`×1).
  → Cách tách phải là "mặt tiền giữ nguyên tên": `grammar.py` vẫn tồn tại, vẫn mang đủ mọi tên
  cũ (kể cả tên private đang bị mượn), chỉ chuyển ruột sang file con — caller không đổi dòng nào.
- `dispatch.py` 430 dòng nhưng chỉ có 2 hàm; hàm `on_callback` ~320 dòng — tách nó KHÔNG thể là
  "di chuyển nguyên hàm", phải cắt ruột hàm → rủi ro cao hơn 7 file kia, đáng cân nhắc bỏ qua.
- `soatkientruc.py` 673 dòng — DƯỚI mức 700 buộc tách; QD-02 chốt nó là MỘT file stdlib không
  import module dự án → tách là phá QD-02. Test cho chính nó thì vẫn viết (nợ SONO).

## Kế hoạch (ĐÃ DUYỆT 03/08, user chọn qua trắc nghiệm)

**Phạm vi chốt:** 6 file tách — đợt 1 `commands` `core` · đợt 2 `ai_client` `congcu` ·
đợt 3 `anki_client` `grammar` (trình lại QD riêng ở đầu đợt) · cuối: `soatkientruc` KHÔNG tách
(673<700, tách phá QD-02), chỉ viết test cho nó. `dispatch.py` BỎ QUA, ghi SONO.md:
cấm thêm nhánh nút mới vào `on_callback`, nhánh mới đặt file riêng cùng tầng.

Mỗi file: ① dựng file vàng (chỉ đọc, dữ liệu thật, để ngoài repo) → ② tách kiểu di-chuyển-nguyên-
hàm, file gốc thành mặt tiền giữ đủ tên cũ → ③ chạy lại file vàng, diff = 0 → ④ máy so thêm ruột
từng hàm trước–sau (chỉ đổi chỗ, không đổi ruột) → ⑤ 3 cửa xanh → ⑥ commit (thân khai VÌ SAO).
Đợt nào đụng code bot thì đề xuất deploy riêng có canary khi user duyệt đợt đó.
Lệnh nghiệm thu: `python soatkientruc.py` · `python -c "import bot, main"` ·
`python -m unittest discover -s tests` · diff file vàng = 0 · tổng `wc -l` không tăng.
QD phải ghi: mỗi file tách = 1 dòng SỔ VẮN TẮT (QD-12); riêng grammar.py soạn mục QD đầy đủ
(lật điều kiện _fable_plan Q5 giữa mùa lô) trình ở đầu đợt 3.
