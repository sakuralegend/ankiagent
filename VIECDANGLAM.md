# 🎯 VIỆC ĐANG LÀM — Bỏ HẲN file cache ngữ pháp, thẻ Anki là nơi duy nhất
> Phiếu việc dùng một lần: cửa 1 GHI ĐÈ, cửa 3 xoá. Trần 60 dòng (S10).

## Một câu
Gỡ hẳn cái máy đẻ ra `data/grammar_cache.json`, để dữ liệu ngữ pháp chỉ còn nằm **một chỗ duy
nhất là thẻ Anki** — dùng khi user không muốn phải đoán "bản nào mới đúng" nữa.

## User đã chốt (từ câu hỏi trắc nghiệm)
- **Gỡ hẳn máy đẻ file**, không phải chỉ xoá file (xoá suông thì code tự dựng lại → vô ích).
- Chấp nhận đổi lại: **bắt buộc mở Anki** mới soạn lô được; mỗi lần chạy chậm thêm 0,58 giây.
- Chấp nhận **nới luật đóng băng** `data/huongdan/kho/` để sửa `cao_nguphap.py` (QD-01).
- 2 từ mồ côi `возвращаться` · `китайски` (có trong cache, chưa từng thành thẻ): **bỏ luôn**.
- `data/openrussian_cache.json` (cache thứ hai, phục vụ thẻ ngữ pháp): **KHÔNG đụng lần này**.

## Coi là XONG khi
- [ ] `data/grammar_cache.json` biến mất, và **chạy lại mọi lệnh nó không mọc lại**.
- [ ] Mở Anki, chạy `python data/huongdan/kho/congcu.py bang <từ>` → vẫn ra đủ bảng chia.
- [ ] **Đóng Anki** rồi chạy lệnh soạn lô → nó **KÊU TO rồi dừng**, tuyệt đối không âm thầm
      ghi thẻ thiếu bảng chia (đây là rủi ro hỏng-im-lặng lớn nhất của việc này).
- [ ] Cào một từ mới bằng bot → dữ liệu ngữ pháp nằm trong ô `GrammarJSON` của thẻ, không đâu khác.
- [ ] 3 cửa nghiệm thu L3 xanh.

## CỐ Ý KHÔNG LÀM lần này
- Không đụng `data/openrussian_cache.json` và `grammar_forms/` (mảng khác, chưa đo).
- Không gộp/đổi tên field Anki nào — **không chạm vùng im lặng schema mod**.
- Không dọn `CHANGELOG.md` (đã đóng sổ, QD-06).

## Đã đo trước khi nhận việc
- **Trùng bảng "ĐÃ ĐO RỒI BÁC"?** CÓ — dòng 18 (`Bỏ grammar_cache.json, đọc thẳng GrammarJSON`,
  phán quyết **BÁC**). Nhưng lý do bác ("88 thẻ thiếu present/future/parts") **đã chết**: đo lại
  31/07/2026 với Anki mở → thẻ **976** / cache **978**, thẻ thiếu khoá **0**, nội dung lệch **0**,
  chỉ 2 từ mồ côi. QD-08 đã tự ghi "hết hạn ⇒ xét bỏ hẳn file cache". ⇒ **Đủ tư cách lật**
  (lật bằng số liệu mới, không bằng lập luận suông).
- **Chức năng gần giống đã có?** CÓ, dùng lại chứ không viết mới:
  `scripts/backfill_grammar_json.py` (ghi dữ liệu ngữ pháp vào thẻ) ·
  `anki_client.doc_grammar_json_tat_ca()` (đọc ngược từ thẻ) · `grammar._lap_dem_tu_the()`.
- **File đang mang nợ?** `anki_tools/grammar.py` **1329 dòng** (>700). Việc này chỉ **BỚT** code
  khỏi nó, không thêm ⇒ không làm nợ nặng thêm.
- **Đụng mấy mảng?** 3 (`anki_tools` · `data/huongdan` · `scripts`) ⇒ đã đọc `KIENTRUC.md`.

## Kế hoạch (user ĐÃ DUYỆT 31/07/2026) — phiên sau chạy thẳng, KHÔNG hỏi lại
1. `grammar.py`: xoá `CACHE_PATH` · `_load_cache()` · `_save_cache()`; `_cache()` thành dict RAM
   lấp từ thẻ (`_lap_dem_tu_the`), bỏ mọi lệnh ghi đĩa ở `fetch_grammar():526` và `:572`.
2. `grammar.remember()`: ghi RAM **+ ghi thẳng ô `GrammarJSON` của thẻ**; Anki đóng thì KÊU.
3. `anki_client.py`: thêm cửa ghi `GrammarJSON` (L1 — cấm tự mở kết nối `:8765` chỗ khác).
4. 🔴 `get_cached():576`: đọc thẻ không được ⇒ **KÊU TO + DỪNG**, cấm trả rỗng im lặng.
5. `kho/cao_nguphap.py` (nới đóng băng QD-01): bỏ `_save_cache` ở `:73` và `:110`, sửa docstring.
6. `huongdan/kiemtra.py:63`: xoá hẳn `soat_the_khop_cache()` — hết hai bản thì hết chỗ lệch.
7. Dọn: xoá `data/grammar_cache.json` khỏi git · gỡ `ANKI_GRAMMAR_CACHE` ở `anki-bot.service:25`
   + `setup_vps.sh:90` · sửa `KIENTRUC.md:112,200` · `deploy.ps1:43` · `tests/test_bug_da_tra_hoc_phi.py:176,198`.

**Lệnh nghiệm thu**: `python soatkientruc.py` · `python -c "import bot, main"` ·
`python -m unittest discover -s tests` · `python data/huongdan/kiemtra.py` ·
**thử ĐÓNG Anki chạy lại → phải kêu to, đây là mục dễ trượt nhất**.
**Lùi lại**: chưa deploy → `git reset --hard HEAD`; đã deploy → `git revert` + `deploy.ps1`.
**Quyết định kèm theo**: QD-11 (đã ghi, đang chờ thi hành). Commit phải nhắc `(QD-11)`.
