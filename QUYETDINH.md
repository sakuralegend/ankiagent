# 📌 QUYẾT ĐỊNH KỸ THUẬT (`QD-nn`)

> Mỗi mục **đúng 4 dòng**: Chọn / Thay vì / Vì (+Hết hạn nếu có). Mới nhất TRÊN CÙNG.
> Chỉ ghi khi RẼ NHÁNH (4 cửa ở `CACHLAM.md` Q5) — việc thường ghi `CHANGELOG.md`.
> Commit thi hành quyết định thì nhắc số hiệu, ví dụ `(QD-01)`.

---

## 📏 ĐÃ ĐO RỒI BÁC — đừng làm lại, đã tốn tiền một lần

> Mỗi dòng dưới đây là một hướng **nghe rất hợp lý**, đã có người (hoặc AI) thử, **đo bằng số liệu
> thật rồi loại bỏ**. Đây là loại lỗi đắt nhất: AI phiên sau đọc code thấy "chỗ này tối ưu được"
> rồi làm lại từ đầu. **Trước khi "tối ưu" bất cứ thứ gì trong bảng này, đọc cột Vì.**
> Muốn lật một dòng: phải ĐO LẠI ra số khác, không được lật bằng lập luận suông.

| Hướng nghe hợp lý | Phán quyết | Vì (số liệu thật) |
|---|---|---|
| ~~Bỏ `grammar_cache.json`, đọc thẳng field `GrammarJSON` trong thẻ~~ | 🔄 **ĐÃ LẬT 31/07/2026 — nay LÀ VIỆC PHẢI LÀM** | Lý do bác cũ (*"88 thẻ thiếu `present`/`future`/`parts`"*) **đã chết** sau đợt đồng bộ cùng ngày. Đo lại với Anki mở: thẻ **976** / cache **978**, thẻ thiếu khoá **0**, nội dung lệch **0**, cache chỉ dư 2 từ mồ côi chưa từng thành thẻ. **Đừng chặn việc này nữa** — xem QD-11, kế hoạch đã duyệt nằm ở `VIECDANGLAM.md` |
| Dùng `_family()` của OpenRussian để dựng mục "Họ hàng" | **BÁC** | Nó gộp `groups` (cùng gốc) với `relateds` (đồng nghĩa **khác gốc hẳn**) vào một rổ ⇒ dạy sai từ nguyên. Mục Họ hàng do người soạn tự nghĩ, cố ý không có cửa máy |
| Lọc từ theo tag trình độ A1–C2 của OpenRussian | **BÁC** | `паспорт`, `яблоко`, `сахар` bị gắn **C1**. Dùng **thứ hạng tần suất** thay thế (top 2500 danh từ ≈ A1→B2) |
| Đối chiếu chéo `nouns.csv` với `grammar_cache.json` để bắt lỗi dữ liệu | **KHÔNG ĐỦ** | Hai file **cùng thượng nguồn OpenRussian** ⇒ trùng nhau không chứng minh đúng. `фон` sai ở **cả hai**. Cửa duy nhất còn lại là người đọc bằng mắt |
| Chờ Difficulty của thẻ tự hồi phục khi trả lời Good | **BÁC** | Đo thật: `w7=0.001` ở sàn, cần **610 lần** Good mới về 50%; **0/84 thẻ** hồi phục. Chỉ Forget/Reset mới cứu |
| Gộp 4 hàm chuẩn hoá tiếng Nga làm một cho gọn | **CHƯA CẦN** | Đo 1748 từ Nga thật (31/07/2026): **0 bất đồng** ở cả hai cặp hàm cùng mục đích. Rủi ro `ё` tổ hợp có thật về lý thuyết nhưng chưa chạm dữ liệu nào ⇒ **đo lại trước khi gộp**, đừng gộp mò |
| "Lô soạn kho càng to càng lợi" | **ĐÚNG MỘT NỬA** | Đúng về token, nhưng lý do thứ hai (khối dùng chung gánh nhiều thẻ) **chết rồi** — chuẩn v3 cấm khối dùng chung, đo ra `0%`. Cỡ lô do CHẤT LƯỢNG quyết định: chốt 16–18 từ |
| Dựng "agent soát riêng" để kiểm lô sau khi soạn | **BÁC** | Lô 22 từ + agent rà lại ≈ **7,9K token/từ**, đắt hơn lô 14 từ tự soát (**7,3K**) mà chưa chắc tốt hơn: người viết biết chỗ mình lăn tăn, người rà phải dựng lại từ đầu |
| Cài bộ "spec-driven-claude-code" (hoặc kit SDLC 12 bước tương tự) vào repo | **BÁC** | Đo 31/07/2026: kit thêm **99 file / 21.852 dòng** luật (toàn repo hiện chỉ 4.033 dòng), **28 file nói C#, 36 nói .NET, 8 nói Python**; `.claude/CLAUDE.md` 616 dòng của nó **đánh nhau** với `CLAUDE.md` 4-mảng ở đây, trùng tên `/review` `/simplify` `/deploy`, và cửa TDD ≥80% khoá cứng repo 92 file .py / 1 test. Đã lấy tinh hoa thành 3 lệnh — xem QD-09 |
| Cho VPS tự động "Download from AnkiWeb" theo lịch cho an toàn | **BÁC — NGUY HIỂM** | Lệnh đó **ghi đè sạch** collection trên VPS (xoá thẻ bot vừa thêm), và không cứu được gì khi quên sync điện thoại vì dữ liệu ôn lúc đó nằm **trong điện thoại** |

---

## QD-11 · 31/07/2026 · Bỏ HẲN `grammar_cache.json` — thẻ Anki là nơi DUY NHẤT · ⏳ ĐÃ DUYỆT, CHƯA THI HÀNH
> ⏳ **Code hiện tại CHƯA khớp mục này** — user duyệt xong thì hết hạn mức. Phiên sau: đọc kế hoạch 7 bước ở `VIECDANGLAM.md` rồi làm, commit nhắc `(QD-11)`. Làm xong thì xoá dòng ⏳ này.
Chọn: bộ nhớ đệm chỉ nằm trong RAM (lấp từ thẻ mỗi lần chạy, không file nào trên đĩa); cào xong ghi thẳng vào ô `GrammarJSON` của thẻ; Anki đóng mà lệnh cần dữ liệu ngữ pháp thì **kêu to rồi DỪNG**, cấm trả rỗng im lặng. Nới đóng băng `data/huongdan/kho/` (QD-01) đủ để sửa `cao_nguphap.py`.
Thay vì: giữ file làm bộ đệm trên đĩa (QD-08, chốt sáng cùng ngày), hoặc chỉ xoá file mà giữ code — phương án sau **vô ích**, đã đo: `_lap_dem_tu_the()` và `remember()` tự dựng lại file đủ 976 từ ngay lần chạy sau.
Vì: user nêu nhu cầu *"xoá cache cho đỡ nhầm lẫn, mọi nguồn chân lý đều ở thẻ Anki"*. Đo 31/07 với Anki mở: thẻ **976** / cache **978**, thẻ thiếu khoá **0**, nội dung lệch **0**, chỉ 2 từ mồ côi (user duyệt bỏ). ⇒ Cache **không còn giữ thứ gì thẻ không có**, nó chỉ còn là cơ hội để lệch. Lý lẽ quyết định: **một nguồn thì không thể lệch; hai nguồn giống hệt nhau thì sớm muộn SẼ lệch, và lệch âm thầm** — đã có 89 thẻ lệch suốt nhiều tuần, tìm ra hoàn toàn tình cờ. Giá phải trả rẻ và đo được: **0,58 giây/lần chạy** (đọc 976 thẻ qua AnkiConnect, so với 0,01s đọc file) + bắt buộc mở Anki mới soạn lô — rẻ hơn hẳn giá của một lần ghi thẻ sai mà không ai biết. QD-08 đã tự hẹn *"hết hạn: khi xong 61 lô ⇒ xét bỏ hẳn file cache"*; số liệu tới sớm hơn lịch nên thi hành sớm hơn. Hết hạn: không.

## QD-10 · 31/07/2026 · AI TỰ commit khi việc xong, không hỏi user
Chọn: xong một việc + ba cửa L3 xanh ⇒ commit ngay (thân khai VÌ SAO, nhắc `QD-nn` nếu có); user nói "kết thúc phiên" mà cây còn bẩn thì commit nốt trước khi chào.
Thay vì: hỏi user trước mỗi lần commit (mặc định cũ), hoặc gói cả phiên thành một commit lúc kết thúc.
Vì: user hỏi *"ủa không có luật bắt phải commit mỗi khi kết thúc à"* — tra ra repo chỉ có luật commit **viết thế nào**, không có luật **khi nào**, nên việc nhớ rơi vào user, trái nguyên tắc QD-09. Đo 12 commit gần nhất: cách nhau **10–20 phút** ⇒ nhịp thật là *xong-việc-thì-commit*, gói cả phiên sẽ đẻ commit to khó lùi từng phần. Rủi ro thấp vì `commit` **không đẩy đi đâu**: code chỉ rời PC qua `deploy.ps1`, nơi 3 cửa vẫn chặn. Hết hạn: không.

## QD-09 · 31/07/2026 · Ba lệnh `/ycau` → `/kehoach` → `/nghiemthu` thay cho bộ kit SDLC 12 bước
Chọn: 3 playbook trong `.claude/commands/` + phiếu việc `VIECDANGLAM.md` ghi đè một-việc-một-lần (S10 canh trần), **AI tự kích hoạt** qua 2 lớp: dòng luật trong `CLAUDE.md` + hook `UserPromptSubmit` bơm lại 5 dòng nhắc mỗi lượt. Cửa 1 bắt buộc hỏi user bằng **AskUserQuestion trắc nghiệm**, cấm câu hỏi mở.
Thay vì: cài `spec-driven-claude-code` (99 file / 21.852 dòng / 12 bước / agent riêng), hoặc không cài gì và dựa vào Plan mode có sẵn.
Vì: repo **đã có sẵn nửa sau** của kit đó và làm chặt hơn (S1–S10 + 3 cửa trong `deploy.ps1` + `QUYETDINH.md`); cái thiếu là **nửa trước** — chốt *làm gì / thế nào là xong* trước khi gõ code. Kit trả giá bằng hai quyển luật mâu thuẫn, trùng tên lệnh, và cửa TDD ≥80% khoá cứng — mà `CACHLAM.md` Q8 đã BÁC coverage cao ở quy mô này. Plan mode thì không để lại file nên phiên AI sau không thấy. Điểm quyết định là yêu cầu của user: *"tôi không giỏi diễn đạt tính năng, phải có bộ lọc để hỏi tôi"* — bộ kit không có bước đó, nó giả định người dùng viết được user story. Bản đầu làm dạng slash command **user phải gõ**; user bác ngay (*"sao còn bắt tôi phải nhớ lệnh"*) ⇒ đổi sang AI tự kích hoạt, vì cơ chế nào cần user nhớ thì đã hỏng từ thiết kế — đúng bài học Q6a. Hết hạn: không — xét lại nếu có người thứ hai viết code.

## QD-02 · 31/07/2026 · `soatkientruc.py` là điểm vào thứ 3 ở gốc + ratchet + cửa trong `deploy.ps1`
Chọn: một file `soatkientruc.py` ở thư mục gốc (stdlib, `ast`+regex, KHÔNG import module dự án), baseline ratchet một chiều trong `soat_baseline.json`, cắm làm bậc 1 của `deploy.ps1` trước `git push`.
Thay vì: để luật kiến trúc nằm trong `CACHLAM.md`/`CLAUDE.md` và trông vào tự giác; hoặc dựng pytest/CI/pre-commit.
Vì: chỗ nào có máy đo (dây chuyền kho, tag `chuan::N`) thì sạch, chỗ nào chỉ có luật viết ra thì trôi — 10 wrapper ra đời SAU khi phát biểu "MỘT chức năng MỘT script". Đặt ở gốc là **ngoại lệ L2 có chủ ý** (L2: gốc chỉ chứa điểm vào đang sống): nó phải nằm nơi `python soatkientruc.py` gõ được không cần nhớ đường dẫn, và chính nó là thứ canh L2. Ratchet chỉ cho GIẢM ⇒ nợ không mọc lại; nới được thì nó thành bảng ghi nợ chứ không phải cửa. Hết hạn: không — thay bằng CI chỉ khi dự án có người thứ hai viết code.

## QD-08 · 31/07/2026 · THẺ ANKI là nguồn sự thật của dữ liệu ngữ pháp; `grammar_cache.json` chỉ còn là BỘ NHỚ ĐỆM
> ⬆️ **BỊ QD-11 THAY THẾ cùng ngày** (bỏ hẳn file cache). Phần "thẻ là nguồn sự thật" vẫn đúng và vẫn là nền của QD-11; chỉ phần "giữ file làm bộ đệm trên đĩa" là hết hiệu lực.
Chọn: `get_cached()` tìm theo thứ tự **đệm → thẻ Anki**; thiếu ở đệm thì tự lấp từ ô `GrammarJSON` (chỉ THÊM khoá thiếu, không đè bản đang có); Anki đóng thì im lặng dùng đệm nên lệnh soát lô vẫn chạy offline.
Thay vì: giữ file cache làm kho riêng của từng máy (cũ), hoặc bỏ hẳn cache ngay (phải sửa `kho/cao_nguphap.py` — đang đóng băng theo QD-01, còn 43 lô).
Vì: user chỉ ra bot cào từ mới **trên VPS** nên ghi vào cache của VPS — laptop không bao giờ nhận, `remember()` không đạt mục đích, và phải cào lại lần hai cùng một từ; QD-05 còn làm đứt hẳn đường về. Thẻ thì **tự đồng bộ qua AnkiWeb tới mọi máy** nên nó mới là kênh đúng. Đo chứng minh: xoá sạch file cache, nó **tự dựng lại 976 từ từ thẻ**, `дом` vẫn đủ bảng chia. Lý do cũ để bác hướng này ("88 thẻ thiếu `present`/`future`/`parts`") đã bị chính việc đồng bộ hôm nay xoá bỏ. Hết hạn: khi xong 61 lô, `kho/` hết đóng băng ⇒ xét bỏ hẳn file cache.

## QD-07 · 31/07/2026 · `PHIENBAN.md` — file duy nhất viết cho USER, tách hẳn khỏi tài liệu kỹ thuật
Chọn: một file ngắn kiểu release notes app (`vX.Y.Z` + ≤5 gạch đầu dòng, ngôn ngữ thường, giữ 10 bản gần nhất); chỉ ghi thứ **user cảm nhận được**.
Thay vì: để user tự đọc `git log`/`CHANGELOG.md`/`KIENTRUC.md` — hoặc không có gì cho user cả (hiện trạng trước đó).
Vì: user chỉ ra rằng **mọi file trong repo đều viết cho người làm**, không sót file nào cho người dùng — *"để tôi hiểu thì chỉ cần kiểu v2.3.3 xong vài gạch đầu dòng"*. QD-06 đóng sổ CHANGELOG vì nó TRÙNG git log ở tầng kỹ thuật; món này KHÔNG trùng vì khác đối tượng, khác ngôn ngữ, khác thứ được chọn để ghi. Chống phình ngay từ đầu bằng ba khoá: trần 2 phút đọc (S10), tối đa 5 mục/bản, giữ 10 bản. Hết hạn: không.

## QD-06 · 31/07/2026 · Đóng sổ `CHANGELOG.md`, lịch sử chuyển sang `git log`
Chọn: `CHANGELOG.md` ngừng ghi (giữ nguyên phần cũ làm lưu trữ); commit message đụng code bắt buộc có phần thân khai VÌ SAO; S9 đổi từ canh "có sửa CHANGELOG" sang canh "message có thân".
Thay vì: tiếp tục ghi song song cả hai (`_fable_plan.md` từng chốt "không bao giờ nén CHANGELOG" — vẫn đúng, nhưng nó nói về **nén file cũ**, không nói phải **ghi tiếp mãi**).
Vì: đo 31/07 — **không script nào đọc** file này (5 chỗ nhắc tên chỉ là chú thích), user nói thẳng *"tôi chẳng thèm đọc"*, và cùng một việc bị viết **hai lần** (17.167 ký tự vào CHANGELOG + 10.241 vào commit message cùng ngày). Quyết định bởi một lý lẽ: **commit message gắn chặt với diff nên không nói dối được**, còn CHANGELOG viết một đằng sửa một nẻo vẫn không ai biết — đúng con đường đã giết `README.md`. Nhu cầu "đính chính về sau" (thứ commit không làm được) đã có `QUYETDINH.md`/`SONO.md` lo. Hết hạn: không.

## QD-05 · 31/07/2026 · Cache ngữ pháp của bot nằm NGOÀI repo (biến `ANKI_GRAMMAR_CACHE`)
> ⬆️ **BỊ QD-11 THAY THẾ cùng ngày.** Không còn file cache thì không còn chỗ nào để tách, biến `ANKI_GRAMMAR_CACHE` bị gỡ. Câu *"hướng đọc từ thẻ đã ĐO và BÁC — 88 thẻ thiếu"* dưới đây **KHÔNG CÒN ĐÚNG**, đo lại ra 0.
Chọn: `grammar.CACHE_PATH` đọc biến môi trường, mặc định giữ chỗ cũ; VPS trỏ `/root/anki-cache/`.
Thay vì: bỏ file khỏi git (mất bản sao lưu công cào), hoặc bỏ hẳn cache để đọc field `GrammarJSON` trong thẻ (`TIEPTUC.md` từng đề xuất).
Vì: một file vừa do git quản vừa bị runtime ghi thì `git pull` bỏ cuộc mỗi lần deploy — đã xảy ra thật 31/07. **Hướng "đọc từ thẻ" đã ĐO và BÁC**: cache bao trùm thẻ, 88 thẻ thiếu hẳn `present`/`future`/`parts`. Cache là ảnh chụp cào lại được nhưng đắt, nên vẫn giữ trong git cho PC. Hết hạn: khi nào bot không còn tự cào (không thấy trước).

## QD-04 · 31/07/2026 · Cảnh báo "bot chết" đi đường ĐỘC LẬP, cố ý không qua `tgbot/alerts.py`
Chọn: `scripts/canhbao_bot_chet.sh` gọi thẳng Telegram API bằng `curl`; systemd `OnFailure=` + cron 15 phút; chống spam bằng mốc trạng thái nên chỉ nhắn khi trạng thái ĐỔI.
Thay vì: dùng `alerts.py` như mọi cảnh báo khác (luật thường lệ trong `CLAUDE.md`).
Vì: `alerts.py` gửi tin **qua chính bot** ⇒ bot chết thì lời cảnh báo chết theo, im lặng tuyệt đối — đúng thứ cần diệt. Đường báo phải không nạp một dòng code Python nào của dự án mới sống sót được khi dự án hỏng. Hết hạn: không.

## QD-03 · 31/07/2026 · Tháo ngòi 12 file lô thế hệ 1 thay vì xoá
Chọn: chèn `raise SystemExit(...)` ngay sau docstring của `lo01…lo12_*.py` — file còn đọc được, chỉ không chạy lại được nữa.
Thay vì: xoá hẳn 12 file.
Vì: chúng vẫn là bản tham chiếu nội dung của 168 thẻ đang phủ dở bởi k51–k60; chạy nhầm lại sẽ XOÁ bảng chia thẻ thật không một tiếng kêu — đã từng xảy ra 29/07/2026. Hết hạn: khi 168 thẻ đó mang tag `chuan::3` hết (đo bằng `findNotes`) → xoá hẳn, git giữ lịch sử.

## QD-01 · 30/07/2026 · Nhận hệ CACHLAM v1 + CLAUDE.md
Chọn: luật L1–L5 thi hành qua `CLAUDE.md` (AI tự đọc mỗi phiên) + lệnh grep; wrapper riêng của `data/huongdan/kho/` được đóng băng làm ngoại lệ L1 hợp lệ.
Thay vì: nguyên tắc chỉ nằm trong trí nhớ/memory phiên chat (đã chứng minh không tự thi hành — 10 wrapper ra đời SAU khi phát biểu "MỘT chức năng MỘT script").
Vì: chỗ có luật-trong-file + máy canh (CHUAN.md) không loạn, chỗ luật-trong-đầu loạn sau 3 tuần. Hết hạn ngoại lệ kho/: khi xong 61 lô.
