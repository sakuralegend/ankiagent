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

## 🗂️ SỔ VẮN TẮT — quyết định đổi code trước khi có sổ này (15/07 → 29/07/2026)

> Sổ số hiệu chỉ lập từ 30/07, nên hai tuần đầu **không để lại vết nào**: một AI mới đọc code
> sẽ thấy các lựa chọn này mà không biết vì sao, và rất dễ "dọn" đúng thứ được cố ý đặt vào.
> Truy lại 01/08/2026 **đúng một dòng mỗi quyết định** — muốn sâu thì `git log --grep`. (QD-12)

| Ngày | Quyết định đổi code | Vì sao, ngắn |
|---|---|---|
| 19/07 | `bot.py` chỉ còn ~10 dòng điểm vào, ruột tách vào gói `tgbot/` 4 tầng | Tầng một chiều `core ← flows ← dispatch ← app`; **`dispatch` chỉ chia việc**, cấm để logic nghiệp vụ vào đó (S3 canh) |
| 19/07 | Nới toàn cục timeout Telegram (connect 15 / read 30 / media 60) | VPS VN → `api.telegram.org` **~230ms RTT**, trần mặc định 5s làm luồng gửi ảnh chết ngay câu trả lời đầu |
| 20/07 | `/sua` = **làm lại thẻ hoàn toàn** (cào + sinh lại), xoá hẳn cơ chế "preset tinh chỉnh" cũ | Preset gần như không ai dùng; làm lại dùng chung `build_card_fields` với thêm thẻ mới nên **một chức năng một lõi** |
| 20/07 | Bot **tự tải bytes** audio rồi `storeMediaFile`, không để AnkiConnect tải hộ qua URL | OpenRussian trả 500 thì AnkiConnect ghi **nguyên câu lỗi** vào ô Audio ⇒ thẻ hỏng nhận ra bằng *thiếu `[sound:]`*, KHÔNG phải ô rỗng |
| 20/07 | Thẻ ngữ pháp tách hẳn thành mảng `grammar_forms/`, phụ thuộc **một chiều** vào `anki_tools` | User: *"ít ảnh hưởng đến deck RUSSIAN đang chạy ngon"* — ưu tiên tuyệt đối là không làm hỏng thứ đang chạy |
| 21/07 | **pymorphy3 offline làm trọng tài** đưa từ Nga về dạng từ điển; AI chỉ lo đọc ảnh | Lemma là việc **tất định**, không nên đoán bằng AI. `reconcile_lemma` có 4 luật giữ phần AI đúng — 🔴 đừng "đơn giản hoá" thành *từ điển luôn thắng* |
| 21/07 | Gõ từ **đã có thẻ** ⇒ trả nguyên mục từ điển, không báo "trùng" suông | Kéo theo ràng buộc vĩnh viễn: mỗi hàm dựng HTML phải có **hàm nghịch** đọc ngược; đổi cấu trúc HTML mà quên sửa hàm nghịch ⇒ bảng tra hiện **trống rỗng** |
| 22/07 | Bỏ deck lọc "phòng tập", cày thẳng trong inbox bằng **undo** | Deck lọc rút thẻ khỏi inbox nên hai bên lệch nhau; undo hoàn nguyên trọn vẹn cả revlog lẫn lịch |
| 22/07 | Gợi ý (hint) dựng bằng **JS trong mặt trước thẻ**, KHÔNG thêm card template | Chỉ card template mới nhân đôi số thẻ — thêm template là tự nhân đôi cả bộ sưu tập |
| 26/07 | Gỡ sạch trần thẻ mới (`new/perDay = 9999` cả 3 preset) | User: *"học đến bao giờ hết thì thôi"*. 🔴 Hằng số nguồn ở **`scripts/setup_inbox.py`** — script này **ghi đè GUI mỗi lần chạy**, chỉnh tay trong Anki là vô ích |
| 29/07 | Gom 3 luồng chạy nền của bot về một hàm `core.chay_hang_loat()` | Ba bản sao lệch nhau âm thầm; nguyên tắc user chốt: **một chức năng một script**, trùng thì tách tầng chứ đừng đồng bộ tay |

---

## QD-15 · 02/08/2026 · Cửa canh DỮ LIỆU ngữ pháp: file mới nhỏ, không nhét thêm vào `grammar.py`
Chọn: `anki_tools/soat_nguphap.py` (~95 dòng, thuần chuỗi, KHÔNG import `grammar` nên không đẻ vòng); gọi ở `cao_nguphap.py` (lúc dữ liệu VÀO) và `congcu.py nap` (lúc dữ liệu LÊN THẺ). Chỉ IN RA, không tự sửa.
Thay vì: thêm hàm vào `grammar.py`, hay nhét vào `congcu.py soat` như phiếu việc gợi ý.
Vì: `grammar.py` đã **1309 dòng** (gấp đôi trần 700) và `_fable_plan.md` chốt dứt khoát *"việc mới liên quan grammar → file mới import grammar, KHÔNG thêm hàm vào file này nữa"*; còn `soat` là lệnh **agent** chạy mà agent cố ý không đụng Anki — trong khi dữ liệu cần soi nằm trong thẻ. Cửa đòi **lệch cả hai chiều cùng lúc** mới báo: đo 516 thẻ có bảng biến cách ra **0 kêu oan**, và bắt đủ 2/2 chỗ của bản ghi hỏng thật `ке́ды`. Hết hạn: khi tách `grammar.py` thì gộp về đúng mảnh của nó.

## QD-13 · 01/08/2026 · Cơ chế nhắc luật phải CÓ CỬA CANH, và phải có đường vào cho AI ngoài Claude Code
Chọn: cửa `S11` trong `soatkientruc.py` chạy THẬT lệnh hook mỗi lần soát (không chỉ kiểm file tồn tại) và **chặn deploy** khi hook không in ra gì / exit khác 0 / file mất; kèm `AGENTS.md` 6 dòng **chỉ trỏ đường**, cố ý không chép lại luật.
Thay vì: tin rằng hook luôn chạy (đo 01/08: S1→S10 **mù hoàn toàn** với chuyện này), hoặc chép luật vào `AGENTS.md` cho AI khác đọc thẳng.
Vì: hook chết là chết **im lặng** — không lỗi nào hiện ra, chỉ là các lượt sau AI dần quên luật, đúng cơ chế đã đẻ ra 10 wrapper. Phải chạy thật vì kiểu chết hay gặp nhất là `python` không có trên PATH (Linux/macOS thường chỉ có `python3`), mà cửa chỉ nhìn tên file sẽ báo XANH trên đúng cái máy hook đang chết. `AGENTS.md` không chép luật vì **hai bản sao thì sớm muộn sẽ lệch** — cùng lý lẽ đã dùng ở QD-11. Hết hạn: không.

## QD-12 · 01/08/2026 · Quyết định nào ĐỔI CODE thì phải để lại vết trong repo, dạng NGẮN
Chọn: ghi **một dòng** vào `QUYETDINH.md` ngay khi quyết định (mục 4 dòng vẫn dùng cho việc lớn); muốn sâu thì tra `git log`. Luật này nằm trong hook nên được bơm lại mỗi lượt.
Thay vì: chỉ ghi khi "rẽ nhánh lớn" (L5 nguyên bản) — tiêu chí đó do AI tự phán nên thực tế là không ai ghi.
Vì: đo 01/08 — **11/11 quyết định trong sổ đều đề 30–31/07**, tức toàn bộ hai tuần đầu dựng bot không có vết nào, dù chúng đổi code nhiều nhất. Vết ngắn mà có hơn vết đầy đủ mà thiếu. Ràng buộc **1 dòng** chính là thứ chặn sổ này đi lại đường `CHANGELOG.md` (2 809 dòng, QD-06): ngắn thì mới có người chịu ghi, và mới có người chịu đọc. Hết hạn: không.

## QD-11 · 31/07/2026 · Bỏ HẲN `grammar_cache.json` — thẻ Anki là nơi DUY NHẤT · ✅ THI HÀNH 02/08/2026
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
🔴 **Phiên soạn lô KHÔNG được ghi vào đây — user bác 02/08/2026.** Tôi đã tự ghi một mục `v1.1.0` cho phiên 5 lô (74 thẻ đổi mặt, lập luận: `nap` sync thẳng sang điện thoại nên user thấy được, dù không qua `deploy.ps1`). **User bảo gỡ.** Mốc là DEPLOY, không phải "user cảm nhận được" — soạn lô là việc chạy đều mỗi phiên, ghi vào đây thì 61 lô đẻ ra hàng chục mục và file chết đúng đường `CHANGELOG.md`. Đừng đề xuất lại.

## QD-14 · 02/08/2026 · Xoá hẳn `CHANGELOG.md` + dọn mọi con trỏ tới nó · ✅ THI HÀNH 02/08/2026
Chọn: xoá hẳn file `CHANGELOG.md` khỏi cây làm việc (không giữ làm lưu trữ nữa) + rà 18 file còn nhắc chữ `CHANGELOG` (`grep CHANGELOG`), sửa/xoá chỗ nào là CON TRỎ CHỨC NĂNG (vd `README.md:35` đang trỏ sai — đã đổi sang `git log` từ QD-06), GIỮ NGUYÊN chỗ nào là GHI CHÉP LỊCH SỬ (vd mục QD-06 ngay dưới, kể lại quyết định đóng sổ).
Thay vì: giữ nguyên file làm lưu trữ như QD-06 từng chốt.
Vì: user chỉ ra file "chẳng để làm gì" — đúng, `soatkientruc.py` S10 đã bỏ nó khỏi danh sách file bắt đọc từ lúc đóng sổ, không ai còn tra tới. Giữ 2809 dòng làm lưu trữ không người đọc chỉ còn là rác cùng loại đã giết chính nó (QD-06). git vẫn giữ trọn nội dung trong lịch sử commit — xoá khỏi cây làm việc không mất gì. Hết hạn: không.

## QD-06 · 31/07/2026 · Đóng sổ `CHANGELOG.md`, lịch sử chuyển sang `git log`
> ⬆️ Phần "giữ nguyên phần cũ làm lưu trữ" BỊ QD-14 THAY THẾ (02/08/2026) — nay xoá hẳn, không giữ nữa.
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
