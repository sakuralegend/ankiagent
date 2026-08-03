# 📌 QUYẾT ĐỊNH KỸ THUẬT (`QD-nn`)

> Mỗi mục **đúng 4 dòng**: Chọn / Thay vì / Vì (+Hết hạn nếu có). Mới nhất TRÊN CÙNG.
> Chỉ ghi khi RẼ NHÁNH (4 cửa ở `CACHLAM.md` Q5) — việc thường thì `git log` lo, đừng ghi vào đây.
> Commit thi hành quyết định thì nhắc số hiệu, ví dụ `(QD-01)`.
> **Điều kiện "Hết hạn" cấm dùng con số tuyệt đối** (mốc "61 lô" đã chết vì hàng đợi lên 64) — viết
> theo trạng thái đo được: *"khi hàng đợi hết lô `cho`"*, *"khi 0 thẻ còn tag X"*.
>
> ⚰️ **KHI NÀO MỘT MỤC CHẾT.** Đừng cân "cái nào quan trọng hơn" — không ai xếp được, nên rốt cuộc
> sẽ cắt bừa. Hỏi đúng một câu **có đáp án đúng/sai**:
> *"Có máy nào bắt được tôi nếu tôi phá luật này mà KHÔNG đọc file này không?"*
> · **Có** (cửa soát / test / hook) ⇒ nén còn **một dòng bia mộ**; lý do sống trong lời báo lỗi của chính cửa đó — nơi người đọc đang đứng khi cần biết.
> · **Không, nhưng đã thi hành xong và thành sự thật trong code** ⇒ bia mộ một dòng, `git log --grep QD-nn` giữ phần còn lại.
> · **Không, và vẫn là đánh đổi người phải tự cân lại** ⇒ **GIỮ**. Loại duy nhất đáng chiếm chỗ.

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

## QD-21 · 03/08/2026 · Mọi CON SỐ TRẦN về `soat_nguong.json` — cấu hình thật máy đọc, tài liệu chỉ trỏ
Chọn: một file JSON ở gốc (tiền lệ `soat_baseline.json`) chứa số + đúng một con trỏ `QD-nn` mỗi mục, `soatkientruc.py` đọc parse CHẶT; S12 soi cấu hình tự mâu thuẫn (trỏ file đã xoá · QD ma · khoá trùng), S13 canh trần dòng file code (400 ghi nợ theo mốc ratchet / 700 tách, bỏ qua lô dữ liệu `k*.py` `lo*.py`), S14 canh `PHIENBAN.md` (bản/mục). Chỉ con số — luật bằng chữ vẫn ở cửa code riêng.
Thay vì: số nằm rải 4 file tài liệu + hằng trong code — đo 03/08: "giữ 10 bản" nêu 4 file 0 cửa canh, "trần 2 phút" nêu 4 file mà máy thi hành 3, trần 400/700 dòng không cửa nào canh.
Vì: bản sao thì sớm muộn lệch, nguồn thì bất khả (cùng lý QD-11); ràng buộc thành dữ liệu thì máy soi được va chạm. 🔴 **Số trong các QD cũ từ nay là LỊCH SỬ — số hiệu lực duy nhất nằm ở `soat_nguong.json`.** Hết hạn: không.

## ⚰️ QD-18 · 03/08 · Tách 6 file quá trần theo khuôn "file vàng" — **ĐÃ XONG** · `git log --grep QD-18`
> Còn sống hai ý: **khuôn "file vàng"** (chạy hàm chỉ-đọc trên dữ liệu thật + so ast từng hàm, diff ≠ 0 là hoàn tác) dùng cho mọi refactor sau; `dispatch.py` cố ý KHÔNG tách (nợ + luật thay thế ghi ở `SONO.md`), `soatkientruc.py` KHÔNG tách (phá QD-02 một-file-tự-đứng).

## QD-19 · 03/08/2026 · Tách `grammar.py` GIỮA mùa lô — lật điều kiện chờ của `_fable_plan.md` Q5
Chọn: tách 4 mảnh lá `chu_nga` (chuẩn hoá chữ + hằng) · `boc_tudien` (normalize) · `hinh_thai` (analyze) · `bang_chia` (build_table); `grammar.py` giữ cache RAM + cào mạng + badge và làm MẶT TIỀN re-export đủ mọi tên cũ kể cả private — caller và test không đổi một dòng.
Thay vì: chờ đủ 3 điều kiện Q5 (xong 61 lô · soát xanh 14 ngày · S2=0) — lúc quyết mới đạt 0/3 (36/64 lô, kho/ còn gọi `_cache`×4).
Vì: user duyệt tách ngay trong đợt refactor 03/08; rủi ro Q5 lo ngại (caller gãy ở chỗ không ai nhớ) bị triệt bằng mặt tiền + file vàng chạy TOÀN BỘ 1023 từ thật (12 291 dòng đầu ra, diff phải = 0) + so ast từng hàm. `soat_nguphap.py` (QD-15 hẹn "gộp về mảnh của nó khi tách") vẫn để RIÊNG — nó đang có 2 caller ổn định, gộp chỉ thêm churn. Hết hạn: không.

## QD-17 · 03/08/2026 · Cửa canh thẻ hiện sai mặt: bám đuôi nhịp sync, GỌI LẠI lõi thăng cấp
Chọn: `anki_tools/soat_giaidoan.py` (mới) + tách `anki_client.thang_cap_gd2()` làm bản DUY NHẤT của ba bước thăng cấp, cả job 3h lẫn cửa canh cùng gọi. Cắm vào **đuôi `_periodic_sync` 30′**, chỉ chạy khi nhịp đó kéo về THÀNH CÔNG. Ba luật: GĐ1 + đã tốt nghiệp ⇒ **đẩy tiếp sang GĐ2 (reset lịch)** · GĐ1 + chưa tốt nghiệp ⇒ gỡ nhãn · GĐ2/kho + mất nhãn ⇒ gắn lại. Bỏ qua lệch dưới 10 phút.
Thay vì: thêm hàm vào `anki_client.py` (988 dòng, quá trần 700) · đẻ job nền mới · chỉ cảnh báo để user bấm `/don` · giữ lịch ôn cho "lành".
Vì: lệch deck↔`Stage` nổ **hai chiều** vì Anki xử xung đột sync RIÊNG cho note và RIÊNG cho card ⇒ nguyên nhân gốc **không sửa được**, chỉ dò rồi vá. 🔴 **`forgetCards` là MỤC ĐÍCH của GĐ2, không phải tác dụng phụ** — GĐ1 là chặng user bấm Again rất nhiều nên độ khó tích lại (đo: **0/84 thẻ** tự hồi phục), nên "giữ tiến độ ôn cho lành" là phá đúng thứ hệ thống dựng ra để làm. Mốc 10 phút chặn giẫm chân `thang_cap_gd2` đang chạy dở. Nghiệm thu: 976 thẻ thật ⇒ **0 kêu oan**; lệch giả 3 chiều ⇒ bắt **3/3**. Hết hạn: không.

## QD-16 · 02/08/2026 · Ghi HÀNG LOẠT lên note thì phải kéo sync về TRƯỚC, hỏng thì DỪNG
Chọn: `anki_client.sync_truoc_khi_ghi_lo()` — một cửa duy nhất, sync hỏng ⇒ không ghi gì. Gọi ở **bốn** chỗ ghi lô: hai script `backfill_*` + `congcu.py nap --apply` + `cao_nguphap._chay()`. Ở `nap` phải gọi **trước khi ĐỌC** ảnh chụp `hien_co`/`vi_co`, vì chính ảnh chụp đó quyết định "ghi hay bỏ qua". Nới đóng băng `data/huongdan/kho/` (QD-01) đủ để chèn 2 lời gọi.
Thay vì: nhắc trong tài liệu / checklist L4 (đợt 31/07 đã theo đủ L4 mà vẫn dính), hoặc để mỗi script tự gọi `sync` riêng.
Vì: đo 02/08 — **23/25 thẻ ở `1-go` hiện sai mặt**. Bot VPS thăng chúng lên GĐ2 lúc 03:00 (ghi `Stage="type"`), 9 tiếng sau laptop **chưa sync về** đã ghi lại 976 note cho ô `GrammarJSON`; ghi vào note làm `mod` mới hơn, mà sync Anki xử xung đột **"ai sửa sau thắng TRỌN note"** ⇒ bản laptop `Stage` rỗng đè bản VPS. Việc đổi deck sống sót vì nó nằm trên **THẺ**, script chỉ đụng **NOTE** — nên thẻ đúng deck, sai mặt, **không lỗi nào bật ra**. Kéo về trước là chặn được đúng cơ chế đó. Hết hạn: không.

## QD-15 · 02/08/2026 · Cửa canh DỮ LIỆU ngữ pháp: `anki_tools/soat_nguphap.py` đứng riêng
Chọn: file nhỏ thuần chuỗi, KHÔNG import `grammar` (tránh đẻ vòng); gọi ở `cao_nguphap.py` (dữ liệu VÀO) và `congcu.py nap` (dữ liệu LÊN THẺ). Chỉ IN RA, không tự sửa.
Vì: cửa đòi **lệch cả hai chiều cùng lúc** mới báo — đo 516 thẻ có bảng biến cách ra **0 kêu oan**, bắt đủ 2/2 chỗ hỏng thật của `ке́ды`.
✅ Điều kiện hết hạn cũ đã bị QD-19 quyết ngược: **GIỮ RIÊNG**, không còn hạn.

## ⚰️ QD-13 · 01/08 · Hook nhắc luật phải có cửa canh — **cửa S11 chạy THẬT lệnh hook mỗi lần soát, S11 LÀ bản ghi**
> Thứ S11 không tự nói được: `AGENTS.md` **cố ý không chép lại luật**, chỉ trỏ đường — hai bản sao thì sớm muộn sẽ lệch (cùng lý lẽ QD-11). Và phải chạy THẬT vì kiểu chết hay gặp là `python` không có trên PATH: cửa chỉ nhìn tên file sẽ báo XANH trên đúng cái máy hook đang chết.

## QD-12 · 01/08/2026 · Quyết định nào ĐỔI CODE thì phải để lại vết trong repo, dạng NGẮN
Chọn: ghi **một dòng** vào `QUYETDINH.md` ngay khi quyết định (mục 4 dòng vẫn dùng cho việc lớn); muốn sâu thì tra `git log`. Luật này nằm trong hook nên được bơm lại mỗi lượt.
Thay vì: chỉ ghi khi "rẽ nhánh lớn" (L5 nguyên bản) — tiêu chí đó do AI tự phán nên thực tế là không ai ghi.
Vì: đo 01/08 — **11/11 quyết định trong sổ đều đề 30–31/07**, tức toàn bộ hai tuần đầu dựng bot không có vết nào, dù chúng đổi code nhiều nhất. Vết ngắn mà có hơn vết đầy đủ mà thiếu. Ràng buộc **1 dòng** chính là thứ chặn sổ này đi lại đường `CHANGELOG.md` (2 809 dòng, QD-06): ngắn thì mới có người chịu ghi, và mới có người chịu đọc. Hết hạn: không.

## QD-11 · 31/07/2026 · Bỏ HẲN `grammar_cache.json` — thẻ Anki là nơi DUY NHẤT · ✅ THI HÀNH 02/08/2026
Chọn: bộ nhớ đệm chỉ nằm trong RAM (lấp từ thẻ mỗi lần chạy, không file nào trên đĩa); cào xong ghi thẳng vào ô `GrammarJSON` của thẻ; Anki đóng mà lệnh cần dữ liệu ngữ pháp thì **kêu to rồi DỪNG**, cấm trả rỗng im lặng. Nới đóng băng `data/huongdan/kho/` (QD-01) đủ để sửa `cao_nguphap.py`.
Thay vì: giữ file làm bộ đệm trên đĩa (QD-08, chốt sáng cùng ngày), hoặc chỉ xoá file mà giữ code — phương án sau **vô ích**, đã đo: `_lap_dem_tu_the()` và `remember()` tự dựng lại file đủ 976 từ ngay lần chạy sau.
Vì: 🔴 **một nguồn thì không thể lệch; hai nguồn giống hệt nhau thì sớm muộn SẼ lệch, và lệch âm thầm** — đã có 89 thẻ lệch suốt nhiều tuần, tìm ra hoàn toàn tình cờ. Đo 31/07: cache **không còn giữ thứ gì thẻ không có** (thiếu khoá 0, nội dung lệch 0) ⇒ nó chỉ còn là cơ hội để lệch. Giá phải trả đo được: **0,58 giây/lần chạy** + bắt buộc mở Anki mới soạn lô — rẻ hơn hẳn một lần ghi thẻ sai mà không ai biết. Hết hạn: không.

## QD-10 · 31/07/2026 · AI TỰ commit khi việc xong, không hỏi user
Chọn: xong một việc + ba cửa L3 xanh ⇒ commit ngay (thân khai VÌ SAO, nhắc `QD-nn` nếu có); user nói "kết thúc phiên" mà cây còn bẩn thì commit nốt trước khi chào.
Thay vì: hỏi user trước mỗi lần commit (mặc định cũ), hoặc gói cả phiên thành một commit lúc kết thúc.
Vì: user hỏi *"ủa không có luật bắt phải commit mỗi khi kết thúc à"* — tra ra repo chỉ có luật commit **viết thế nào**, không có luật **khi nào**, nên việc nhớ rơi vào user, trái nguyên tắc QD-09. Đo 12 commit gần nhất: cách nhau **10–20 phút** ⇒ nhịp thật là *xong-việc-thì-commit*, gói cả phiên sẽ đẻ commit to khó lùi từng phần. Rủi ro thấp vì `commit` **không đẩy đi đâu**: code chỉ rời PC qua `deploy.ps1`, nơi 3 cửa vẫn chặn. Hết hạn: không.

## QD-09 · 31/07/2026 · Ba lệnh `/ycau` → `/kehoach` → `/nghiemthu` thay cho bộ kit SDLC 12 bước
Chọn: 3 playbook trong `.claude/commands/` + phiếu việc `VIECDANGLAM.md` ghi đè một-việc-một-lần (S10 canh trần), **AI tự kích hoạt** qua 2 lớp: dòng luật trong `CLAUDE.md` + hook `UserPromptSubmit` bơm lại 5 dòng nhắc mỗi lượt. Cửa 1 bắt buộc hỏi user bằng **AskUserQuestion trắc nghiệm**, cấm câu hỏi mở.
Thay vì: cài `spec-driven-claude-code` (99 file / 21.852 dòng / 12 bước / agent riêng), hoặc không cài gì và dựa vào Plan mode có sẵn.
Vì: repo **đã có sẵn nửa sau** (cửa soát + 3 cửa `deploy.ps1`) và chặt hơn kit; cái thiếu là **nửa trước** — chốt *làm gì / thế nào là xong* trước khi gõ code. Plan mode không để lại file nên phiên sau không thấy. Điểm quyết định là yêu cầu user: *"tôi không giỏi diễn đạt tính năng, phải có bộ lọc để hỏi tôi"* — kit giả định người dùng viết được user story. 🔴 Bản đầu làm dạng lệnh **user phải gõ**, user bác ngay (*"sao còn bắt tôi nhớ lệnh"*) ⇒ **cơ chế nào cần user nhớ thì đã hỏng từ thiết kế**. Hết hạn: không — xét lại nếu có người thứ hai viết code.

## QD-02 · 31/07/2026 · `soatkientruc.py` là điểm vào thứ 3 ở gốc + ratchet + cửa trong `deploy.ps1`
Chọn: một file `soatkientruc.py` ở thư mục gốc (stdlib, `ast`+regex, KHÔNG import module dự án), baseline ratchet một chiều trong `soat_baseline.json`, cắm làm bậc 1 của `deploy.ps1` trước `git push`.
Thay vì: để luật kiến trúc nằm trong `CACHLAM.md`/`CLAUDE.md` và trông vào tự giác; hoặc dựng pytest/CI/pre-commit.
Vì: chỗ nào có máy đo (dây chuyền kho, tag `chuan::N`) thì sạch, chỗ nào chỉ có luật viết ra thì trôi — 10 wrapper ra đời SAU khi phát biểu "MỘT chức năng MỘT script". Đặt ở gốc là **ngoại lệ L2 có chủ ý** (L2: gốc chỉ chứa điểm vào đang sống): nó phải nằm nơi `python soatkientruc.py` gõ được không cần nhớ đường dẫn, và chính nó là thứ canh L2. Ratchet chỉ cho GIẢM ⇒ nợ không mọc lại; nới được thì nó thành bảng ghi nợ chứ không phải cửa. Hết hạn: không — thay bằng CI chỉ khi dự án có người thứ hai viết code.

## ⚰️ QD-08 · 31/07 · Thẻ Anki là nguồn sự thật, cache chỉ là bộ đệm — **CHẾT**, QD-11 thay cùng ngày · `git log --grep QD-08`
> Phần "**thẻ là nguồn sự thật**" vẫn sống, nhưng nó nay là nền của QD-11 — đọc ở đó.

## QD-07 · 31/07/2026 · `PHIENBAN.md` — file duy nhất viết cho USER, tách hẳn khỏi tài liệu kỹ thuật
Chọn: một file ngắn kiểu release notes app (`vX.Y.Z`, ngôn ngữ thường; trần bản/mục nay ở `soat_nguong.json`, cửa S14 canh); chỉ ghi thứ **user cảm nhận được**.
Thay vì: để user tự đọc `git log`/`CHANGELOG.md`/`KIENTRUC.md` — hoặc không có gì cho user cả (hiện trạng trước đó).
Vì: user chỉ ra rằng **mọi file trong repo đều viết cho người làm**, không sót file nào cho người dùng — *"để tôi hiểu thì chỉ cần kiểu v2.3.3 xong vài gạch đầu dòng"*. QD-06 đóng sổ CHANGELOG vì nó TRÙNG git log ở tầng kỹ thuật; món này KHÔNG trùng vì khác đối tượng, khác ngôn ngữ, khác thứ được chọn để ghi. Chống phình ngay từ đầu bằng ba khoá: trần 2 phút đọc (S10), tối đa 5 mục/bản, giữ 10 bản. Hết hạn: không.
🔴 **Phiên soạn lô KHÔNG ghi vào đây — user bác 02/08/2026, một mục tự ghi đã phải gỡ.** Mốc là DEPLOY, không phải "user cảm nhận được": soạn lô chạy đều mỗi phiên, ghi vào là file chết đúng đường `CHANGELOG.md`. Đừng đề xuất lại.

## ⚰️ QD-14 · 02/08 · Xoá hẳn `CHANGELOG.md` khỏi cây làm việc — **ĐÃ THI HÀNH XONG**, file không còn tồn tại · `git log --grep QD-14`

## ⚰️ QD-06 · 31/07 · Đóng sổ `CHANGELOG.md`, lịch sử về `git log` — **cửa S9 canh "commit có thân", S9 LÀ bản ghi** (file đã xoá hẳn, QD-14)
> Lý lẽ đáng nhớ ngoài phạm vi ca này: **commit message gắn chặt với diff nên không nói dối được**; tài liệu viết một đằng sửa một nẻo thì không ai biết — đúng con đường đã giết `README.md` cũ.

## QD-20 · 03/08/2026 · Trần đọc đo bằng KÝ TỰ, không bằng dòng
Chọn: `S10` đổi `DONG_MOI_PHUT=30` → `KY_TU_MOI_PHUT=1400`; ngân sách phút đặt lại từ kích thước THẬT 03/08 (ratchet chốt-từ-hiện-trạng như `soat_baseline.json`); thêm `TIEPTUC.md` + `data/huongdan/README.md` vào danh sách bị canh; 4 test mới, trong đó **một test tái hiện đúng ca bản cũ bỏ lọt**.
Thay vì: giữ đếm dòng, hoặc đặt ngân sách theo mức "đáng ra phải thế" (sẽ đỏ 8 file, chặn deploy trong khi việc chính là chạy lô).
Vì: đo 03/08 — **ký tự/dòng chạy từ 49 tới 140** giữa các file nên đếm dòng không đo được gì thật: `QUYETDINH.md` báo 149/150 dòng "còn chỗ" trong khi nặng 30 KB, dòng dài nhất **1090 ký tự**, tức vượt ngân sách gấp ba mà cửa vẫn XANH. Và hai file to nhất repo (60 249 ký tự = **44% toàn bộ tài liệu**) chưa hề bị canh, trong khi `PHIENBAN.md` 3 652 ký tự thì bị chặn. Tốc độ 1400 kt/phút không bịa: nó là tốc độ hàm ý của đúng hai file chưa ai kêu dài (KIENTRUC 1417 · README 1438). Hết hạn: không.

## ⚰️ QD-05 · 31/07 · Cache ngữ pháp ra ngoài repo — **CHẾT**, QD-11 thay cùng ngày (bỏ hẳn file cache) · `git log --grep QD-05`

## QD-04 · 31/07/2026 · Cảnh báo "bot chết" đi đường ĐỘC LẬP, cố ý không qua `tgbot/alerts.py`
Chọn: `scripts/canhbao_bot_chet.sh` gọi thẳng Telegram API bằng `curl`; systemd `OnFailure=` + cron 15 phút; chống spam bằng mốc trạng thái nên chỉ nhắn khi trạng thái ĐỔI.
Thay vì: dùng `alerts.py` như mọi cảnh báo khác (luật thường lệ trong `CLAUDE.md`).
Vì: `alerts.py` gửi tin **qua chính bot** ⇒ bot chết thì lời cảnh báo chết theo, im lặng tuyệt đối — đúng thứ cần diệt. Đường báo phải không nạp một dòng code Python nào của dự án mới sống sót được khi dự án hỏng. Hết hạn: không.

## ⚰️ QD-03 · 31/07 · Tháo ngòi 12 file lô thế hệ 1 bằng `raise SystemExit` thay vì xoá — **cửa S7 canh, S7 LÀ bản ghi**
> ⏳ **Còn nợ:** khi 168 thẻ của k51–k60 mang đủ tag `chuan::3` thì **xoá hẳn 12 file**, git giữ lịch sử. Chạy nhầm chúng sẽ XOÁ bảng chia thẻ thật **không một tiếng kêu** — đã xảy ra 29/07.

## QD-01 · 30/07/2026 · Nhận hệ CACHLAM v1 + CLAUDE.md
Chọn: luật L1–L5 thi hành qua `CLAUDE.md` (AI tự đọc mỗi phiên) + lệnh grep; wrapper riêng của `data/huongdan/kho/` được đóng băng làm ngoại lệ L1 hợp lệ.
Thay vì: nguyên tắc chỉ nằm trong trí nhớ/memory phiên chat (đã chứng minh không tự thi hành — 10 wrapper ra đời SAU khi phát biểu "MỘT chức năng MỘT script").
Vì: chỗ có luật-trong-file + máy canh (CHUAN.md) không loạn, chỗ luật-trong-đầu loạn sau 3 tuần.
🔴 **Hết hạn ngoại lệ `kho/`: khi hàng đợi hết lô `cho`** (đo: `congcu.py trangthai`). Mốc cũ ghi "khi xong **61 lô**" — SAI, hàng đợi nay **64 lô** và còn đổi mỗi lần user thêm từ mới, nên **đừng bao giờ đặt điều kiện bằng con số tuyệt đối**. Trên thực tế đóng băng này đã bị nới ba lần (QD-11, QD-16, QD-19) ⇒ nó **gần như đã chết**, giữ lại chỉ để chặn viết wrapper mới.
