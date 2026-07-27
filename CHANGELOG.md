# 📜 Nhật ký thay đổi (CHANGELOG)

> File này là "bộ nhớ chung" của dự án: mỗi lần sửa gì đều ghi vào đây (mới nhất ở TRÊN CÙNG),
> để phiên chat mới / người mới đọc là nắm được ngay hệ thống đã đi qua những gì.
> Quy ước mỗi mục: **ngày — commit — làm gì + vì sao**.

## 27/07/2026 (chiều) — DÂY CHUYỀN SOẠN KHO 703 TỪ

- **`c8d47fe` — dựng dây chuyền soạn ô "Hướng dẫn" cho 703 từ deck kho**, chia **56 lô**.
  Thẻ trong Anki **chưa bị đụng** — user yêu cầu *"để riêng ra một chỗ, lúc nào xong toàn bộ
  tôi sẽ nhờ bạn đẩy vào một thể"*.
- 🔴 **MỖI LÔ CHẠY TRONG MỘT CONTEXT TRẮNG** — user chỉ ra đúng chỗ đau: *"đừng để những lượt
  làm này gối lên nhau… thứ tôi ưu tiên nhất là chất lượng"*. Soạn nhiều lô liên tiếp trong
  cùng một context làm chất lượng **nhạt dần** (bắt đầu chép khuôn lô trước thay vì nghĩ lại
  cho từ mới), mà nhạt dần thì **chính người soạn khó tự thấy** — kiểu xuống cấp nguy hiểm
  nhất, vì user không kiểm được. Chữa bằng cách giao mỗi lô cho một agent phụ khởi động lạnh,
  đọc `README.md` §7 rồi soạn. Luồng chính **không soạn**, chỉ **soát và ghi nhận**.
- **Trạng thái nằm TRÊN ĐĨA, không nằm trong context**: `kho/hangdoi.json` (56 lô + trạng thái)
  và `kho/tudien.json` (ảnh chụp đông lạnh 703 từ). Hết hạn mức 5h thì phiên sau chỉ cần
  `congcu.py trangthai` là biết chạy tiếp từ đâu, không phải dò lại.
- **`kho/congcu.py`** — `tiep <id>` (in đề bài) · `soat [id]` (soát KHÔNG cần Anki) ·
  `trangthai` · `xong <id>` (chỉ luồng chính gọi) · `nap --apply` (đẩy vào Anki, một lần cuối).
  Lô soạn xong là file **dữ liệu thuần** `S = {...}`, không boilerplate, không tự gọi Anki —
  **lô không được tự đánh dấu mình xong**, nếu không bộ soát mất hết ý nghĩa.
- **Chia lô theo họ từ bằng cách sắp xếp TỪ VIẾT NGƯỢC** — tiếng Nga phái sinh bằng hậu tố,
  nên xếp ngược thì `-ение`, `-ость`, `-ский`, `-тель` tự động nằm liền nhau.
- ➕ **Bộ soát thêm hai cửa**, cả hai bắt được lỗi thật ngay lô đầu:
  - **CẤU TRÚC HTML** — bắt `<u>…</b>` lệch ở thẻ `дава́ть`. HTML hỏng thì thẻ hiện sai trên iPhone.
  - **TỪ NGA IN ĐẬM THIẾU DẤU TRỌNG ÂM** — bịt lỗ hổng của bộ soát cũ: nó chỉ đối chiếu được
    từ **có sẵn dấu**, nên **bỏ dấu là né được**. Giờ từ ≥2 nguyên âm mà không dấu sẽ bị báo.
- Lô k01 (15 động từ) xong, đã soát sạch cả ba cửa. Nội dung dạy 3 hệ thống trục: cặp thể +
  4 kiểu dựng cặp · hai lớp chia + biến âm ngôi `я` chỉ ở lớp 2 · động từ chuyển động một
  chiều/nhiều chiều + bảng tiền tố hướng.

## 27/07/2026

- **XONG Ô "HƯỚNG DẪN" CHO TOÀN BỘ 168 TỪ trong hai deck đang học** (lô 1→12). Đây là thứ user
  đọc ĐẦU TIÊN khi gặp từ mới — mục tiêu user nói rõ: *"học để thật sự hiểu, thật sự nhớ, tránh
  học vẹt đi vào vết xe đổ lần trước"*.
  - **Chia lô theo HỌ TỪ, không chia đều.** 32/168 từ nằm cùng hệ thống quốc tịch; soạn cùng
    nhau thì giải thích nhất quán. Khối hệ thống dùng chung **lặp ở mọi thẻ trong họ là CỐ Ý** —
    user chỉ nhìn một thẻ mỗi lần, gặp lại 32 lần chính là spaced repetition cho cái hệ thống.
  - 📄 **Công thức đầy đủ ở `data/huongdan/README.md`** — đặc tả nội dung, 7 tiêu chí "cái tinh
    tuý nên ưu tiên", quy trình 6 bước, bẫy đã dính, và bảng 12 hệ thống đã dạy. Đọc file đó
    trước khi soạn lô mới, đừng dò lại từ đầu.
- **BỘ SOÁT `kiemtra.py` đã bắt 11 lỗi thật qua 12 lô** — user tự nói *"tôi không đủ kiến thức
  để kiểm tra được độ tin cậy"*, nên phần nào máy soát được thì bắt buộc để máy soát.
  - Bắt được cả loại lỗi **đọc bằng mắt không ra**: `коре́янка`→`корея́нка`, `славя́нин`→`славяни́н`,
    `выходны́е`, `морози́льник`; từ **không tồn tại** `ра́дый`; sai dạng `мо́лодый`→`молодо́й`.
  - 🔴 **Hai lần nó lộ ra LỜI GIẢI THÍCH sai, không chỉ con số**: (1) tôi viết "trọng âm dịch
    giữa `-ик`/`-ика`" — thực ra đứng yên ở cả 4 cặp, suýt dạy user một luật ngược; (2) `ви́на`
    không phải cách 2 của `вино́` mà là số nhiều — cách 2 lại trùng khít `вина́` "lỗi lầm".
  - Đã mở rộng từ chỗ **chỉ soát khối Họ hàng** ra **toàn field** (bản đầu bỏ lọt mọi từ trong
    phần Cách nhớ và ô cảnh báo), thêm `MIEN_TRU` cho từ đồng tự — một bộ soát kêu nhầm mãi thì
    rồi chính mình sẽ bỏ qua cả tiếng kêu thật.
  - ⚠️ **Giới hạn phải nhớ:** `nouns.csv` chỉ có DANH TỪ. Động từ/tính từ rơi vào danh sách
    "phải đọc bằng mắt" — đó là **chưa kiểm được**, KHÔNG phải "đúng".

- **BỘ SOÁT `data/huongdan/kiemtra.py` — để MÁY kiểm tôi, đừng bắt user tin.** User nói thẳng:
  *"tôi không đủ kiến thức để có thể kiểm tra được độ tin cậy"*. Nên phần nào máy soát được thì
  phải để máy soát. Script đối chiếu mọi từ Nga in đậm trong khối `.hd-fam` với
  **`data/nouns.csv` (26.856 danh từ có sẵn trọng âm chuẩn)**: từ đó có thật không, và trọng âm
  đặt đúng chỗ chưa.
  - 🟢 **Bắt lỗi thật ngay lô đầu**: tôi viết `коре́янка`, đúng phải là `корея́нка`. Tự mâu thuẫn
    với chính `китая́нка` cùng lô mà không tự thấy.
  - ⚠️ **Giới hạn phải nói rõ**: `nouns.csv` chỉ có DANH TỪ. Động từ/tính từ script báo
    "không tra được" — **KHÔNG phải "đúng"**. Đừng đọc nhầm cái im lặng đó thành xác nhận.
  - ⚠️ Bẫy của chính bộ soát: từ điển **không ghi trọng âm cho nhiều tên riêng** (`Аме́рика`,
    `Кита́й`, `Коре́я` lưu trần) ⇒ báo nhầm hàng loạt. Đã lọc: mục không có dấu thì không so.
- **Hướng dẫn lô 1 + lô 2 — trọn họ QUỐC TỊCH (32 từ).** Lô 1: 17 danh từ chỉ người. Lô 2: 9
  tính từ `-ский` + 6 trạng từ `по-…-ски`. Gom theo HỌ chứ không chia đều — 32/168 từ đang học
  nằm trong cùng một hệ thống, soạn cùng nhau thì lời giải thích nhất quán.
  - Trọng tâm lô 2 không phải từng từ mà là **`ру́сский язы́к` (tính từ) vs `говори́ть по-ру́сски`
    (trạng từ)** — lỗi người mới mắc suốt.
  - Khối hệ thống lặp ở MỌI thẻ là cố ý: user chỉ nhìn một thẻ mỗi lần, gặp lại 32 lần chính là
    spaced repetition cho bản thân cái hệ thống.
  - Còn **237 thẻ** nội dung kiểu cũ, **134 từ** trong hai deck học chưa soạn.

- **SỬA THỨ TỰ KHỞI ĐỘNG BOT: sync KÉO VỀ trước, rồi mới đẩy template.** Bản cũ làm ngược.
  Hôm đổi tên field trên laptop, VPS khởi động lại và đẩy template có `{{HuongDan}}` vào
  collection của nó vẫn còn tên `Mnemonic` → `❌ Templates thất bại: Field 'HuongDan' not found`.
  - 🔴 **Hậu quả nặng hơn cái lỗi**: lần đẩy hỏng đó **vẫn chạm vào note type**, làm bản của VPS
    "mới hơn" bản laptop, nên **mọi lần sync sau đều GIỮ BẢN CŨ** dù laptop đã đúng. Sync báo
    "OK" đều đặn mà tên field không bao giờ về. Phải ssh vào đổi tên tay trên VPS rồi mới hết.
  - 🔑 Rút ra: **sync báo OK không có nghĩa là hai bên giống nhau.** Sau mỗi lần đổi note type
    phải đối chiếu thật `modelFieldNames` + `modelTemplates` ở CẢ HAI máy, đừng tin chữ "OK".
  - Lại một lần nữa lỗi chỉ lộ ra trong `journalctl`, không có tin Telegram nào.

- **BỎ HẲN HƯỚNG MNEMONIC, Ô "HƯỚNG DẪN" CHUYỂN SANG PHÂN TÍCH GỐC TỪ.** User đánh giá sau buổi
  học 26/07: hai thứ đáng giá nhất là **giai đoạn 1** và **đoạn phân tích gốc từ** — *"đã khiến
  tôi hiểu được một từ được ghép từ nhiều mảnh, mỗi mảnh có ý nghĩa riêng"*. Ngược lại mnemonic
  *"chất lượng chưa cao"* ⇒ bỏ luôn, bỏ cả phiên âm.
  - Nội dung mới ba phần: **Chẻ từ** (từng mảnh + nghĩa của mảnh) → **Cách nhớ** (logic nối các
    mảnh ra nghĩa, bắc cầu sang tiếng Anh khi cùng gốc Latin) → **Họ hàng** (từ cùng gốc/cùng
    phụ tố, có nghĩa kèm). Bẫy dễ nhầm gốc thì chèn `.hd-warn` ngay dưới phần liên quan.
  - **Ô Hướng dẫn giờ THU GỌN mặc định**, bấm mới mở — dùng lại đúng `<details>/<summary>` của
    khối ví dụ, **HTML thuần không JavaScript** (JS ở mặt sau thẻ hay chết lặng trên AnkiMobile).
    Nhờ gấp lại được nên nội dung mới được phép dài: user chốt *"đừng rút gọn khó hiểu"*.
  - **Đổi tên field `Mnemonic` → `HuongDan`** cho khỏi nhầm. 🟢 **Đo được: đổi tên field KHÔNG
    phải schema mod** — sync ngay sau đó sạch, không đòi full sync — vì số lượng và thứ tự field
    không đổi (khác hẳn thêm/xoá field). Đây là điều trước nay vẫn tưởng là phải full sync.
  - **Lớp CSS `mn-` → `hd-`**; khối `mn-read/mn-story/mn-tip` giữ tạm vì **269 note chưa soạn lại
    vẫn còn các div ấy trong nội dung field**. Nhìn tiền tố là biết cái nào còn sống. Xoá khối
    di sản khi soạn xong lô cuối.
  - Xoá `data/mnemonics/` (git vẫn giữ lịch sử). Tag Anki vốn không có tag nào dính mnemonic.
  - Đã áp mẫu cho **положи́тельный** và **перево́дчик** để user duyệt trước khi chạy cả lô.

## 26/07/2026

- **SỬA NÚT 🧹 Dọn trong menu — nó chạy LOGIC CŨ và crash.** Phát hiện nhờ đọc journal VPS:
  `17:00:24 TypeError: _don_report() takes 1 positional argument but 2 were given`.
  Nút bấm gọi thẳng `move_graduated_from_inbox()` nên **bỏ cả bước sync-kéo-về lẫn bước
  GĐ1→GĐ2**, rồi chết ở dòng báo cáo. Lệnh gõ `/don` vẫn đúng, chỉ nút hỏng.
  → `dispatch.py` giờ gọi chung `run_don()`, không dựng lại logic dọn ở đó nữa.
  - 🔑 **Bài học**: đổi chữ ký một hàm dùng chung thì phải **grep MỌI call site**, không chỉ
    chỗ mình vừa sửa. **Lệnh gõ và nút bấm là HAI đường code khác nhau** — sửa một bên không
    tự sửa bên kia. Đây là lỗi cùng họ với vụ `flow_scan.py` còn import `INBOX_DECK` đã xoá.
  - 🔑 **Job nền `_guard()` nuốt exception nên Telegram im lặng** — nút hỏng suốt 6 tiếng mà
    không có cảnh báo nào. Chỗ duy nhất lộ ra là `journalctl -u anki-bot`. Sau mỗi đợt sửa
    lớn, **đọc journal chứ đừng chỉ hỏi `systemctl is-active`**.
  - Đã quét lại toàn bộ: 3 chỗ gọi `_don_report` đều 1 tham số, 3 chỗ gọi `run_don`, và
    import thử **cả 12 module** y như lúc bot khởi động — tất cả sạch.
- **GỠ SẠCH TRẦN THẺ MỚI** (user: *"tôi sẽ học đến bao giờ hết thì thôi"*). Cả ba preset về
  `new/perDay = 9999` (mức cao nhất Anki nhận = không trần): `russian-parent-70` (cha, 140→9999),
  `stage1-quen` (70→9999), `inbox` (70→9999). `rev/perDay` vốn đã 9999 từ trước.
  Hiệu lực ngay: `getDeckStats.new_count` của `0-quen` từ **0 → 197** (suất 70 hôm nay đã tiêu hết).
  - ⚠️ **Sửa luôn `setup_inbox.py`**, nếu không nó dựng lại trần 70/140 ở lần chạy sau mà không
    ai biết — `ensure_preset()` ghi `perDay` **vô điều kiện** mỗi lần chạy. Hằng số nguồn duy nhất
    là `STAGE_NEW_PER_DAY` / `PARENT_NEW_PER_DAY`; **đừng chỉnh trần bằng tay trong GUI Anki.**
    (`PARENT_NEW_PER_DAY` không còn = `STAGE × 2` vì 19998 vượt mức Anki nhận.)
  - ⚠️ **Tên preset `russian-parent-70` giờ là tên SAI** — không còn giới hạn 70. Cố ý giữ tên vì
    user nhìn nó trong GUI. Đừng suy hạn mức từ tên preset, đọc `new.perDay`.
  - Đã báo trước cho user cái giá: gỡ trần ở `1-go` nghĩa là cày hết GĐ1 trong một buổi thì hôm
    sau toàn bộ chỗ đó đổ sang dạng **gõ** cùng lúc, và thẻ gõ đẻ nợ ôn tập kéo dài nhiều tuần
    chứ không tan sau 15 phút như GĐ1. User chấp nhận.
- **ĐẨY TOÀN BỘ 89 THẺ `1-go` NGƯỢC VỀ `0-quen`, xoá sạch dữ liệu học** (user yêu cầu sau khi
  học thử GĐ1: *"tôi thấy học kiểu này hiệu quả đấy"* — muốn học lại từ đầu theo lộ trình mới).
  Làm y hệt `promote_stage1_to_stage2()` nhưng ngược chiều, **ba việc phải đi cùng nhau**:
  `Stage=""` → `forgetCards` → `changeDeck` sang `0-quen`. Sao lưu trước bằng `exportPackage`
  deck `RUSSIAN` kèm `includeSched=True` → `backups/truoc-reset-1go_2026-07-26_1646.apkg` (40,5 MB).
  Sau: `1-go` 0 thẻ, `0-quen` 271 thẻ (201 mới), tổng vẫn **870**, 0 thẻ lệch deck ↔ field.
  Hàng đợi thẻ mới ở `0-quen` là 201 ở mức 70/ngày ⇒ ~3 ngày mới tiêu hết.
- 🟢 **TRẢ LỜI CÂU HỎI CÒN TREO: `forgetCards` CÓ xoá sạch FSRS Difficulty + Stability.**
  Đợt reset trên là cơ hội đo thật. Bằng chứng (chính `0-quen` ngay sau khi reset):
  `is:new prop:d>0` = **0**, `is:new prop:s>0` = **0**, trong khi `-is:new prop:d>0` = **70**
  (70 thẻ GĐ1 đang học dở hôm nay vẫn giữ D). ⇒ bước GĐ1→GĐ2 tiện thể rửa sạch D tích luỹ,
  điều mà bấm Good **không** làm được (xem mục 25/07).
  ⚠️ **Cách đo**: `cardsInfo` trả `difficulty`/`stability`/`fsrsMemoryState` = `None` cho MỌI thẻ —
  đừng tin đó là "D đã bị xoá", nó chỉ là AnkiConnect không xuất trường này. Phải hỏi bằng
  **search `prop:d>0` / `prop:s>0`**, đó mới là số Anki tính thật.
- **LỘ TRÌNH HỌC HAI GIAI ĐOẠN: tách `0-inbox` thành `0-quen` (làm quen) + `1-go` (gõ).**
  Vấn đề: thẻ mới toanh bắt SẢN XUẤT tiếng Nga từ con số 0 ngay lần gặp đầu — nhiệm vụ khó nhất
  có thể. Nguyên tắc thiết kế (user diễn đạt, gọn hơn mọi lý lẽ khác): **mỗi giai đoạn đo ĐÚNG MỘT
  thứ** — GĐ1 đo nhận diện + âm điệu + nghĩa, GĐ2 đo chính tả.
  Vòng đời mới: `0-quen` (Stage rỗng, mặt trước chỉ chữ Nga, KHÔNG ô gõ) → rời learning →
  `Stage="type"` + `forgetCards` + chuyển sang `1-go` (thẻ MỚI TINH, có ô gõ + gợi ý chữ cái) →
  rời learning lần nữa → về `RUSSIAN::<topic>` như cũ.
  - **Field `Stage` thay cho `Image`** (Image chết: 0/870 note có dữ liệu). Phải dùng FIELD chứ
    không dùng deck vì khối điều kiện `{{#...}}` của Anki **chỉ đọc được field**.
  - **Đã kiểm chứng trước khi làm**: `{{type:}}` đặt BÊN TRONG khối điều kiện vẫn bật được ô gõ →
    **một** card template phục vụ cả hai giai đoạn, số thẻ giữ nguyên **870**. Nếu phải tách 2
    card template thì 870 → 1740 và không nên làm.
  - ⚠️ **BẪY ĐÃ DÍNH khi viết template**: comment HTML chứa chuỗi literal `[[type:...]]` khiến
    thẻ GĐ1 MỌC Ô GÕ. Anki thay thế trên **văn bản thô** trước khi thành HTML nên comment không
    che được. Tuyệt đối không viết ký hiệu ô gõ vào comment. Phát hiện nhờ so `question` render
    thật, không tin template đọc bằng mắt.
  - Hai deck riêng (không phải một deck hạn mức gấp đôi) vì Anki rút thẻ mới **theo vị trí** —
    một deck gộp có thể lĩnh trọn suất cho GĐ1, không còn suất nào cho GĐ2. Preset `inbox` giữ
    cho `1-go`, clone thành `stage1-quen` cho `0-quen`, mỗi bên 70/ngày.
  - ⚠️ **Trần deck CHA `RUSSIAN` nâng 70 → 140** vì mỗi từ đi qua hàng đợi "thẻ mới" HAI lượt.
    Đúng bài học 21/07: trần cha kẹp cả cây. Đã đo lại bằng `getDeckStats`: RUSSIAN=70 = tổng hai
    con → cha không còn kẹp.
  - Di trú: `Stage="type"` cho **688** note đã học, để trống cho **182** thẻ chưa học. Quên bước
    này thì cả 870 thẻ rơi về GĐ1, kể cả 599 thẻ đã thuộc ở deck chủ đề.
  - `renameDeck` **không có** trong AnkiConnect → đổi tên deck bằng cách tạo deck mới + chuyển
    thẻ + xoá deck cũ.
  - Code: `config.py` bỏ `INBOX_DECK`, thêm `STAGE1_DECK`/`STAGE2_DECK`; `anki_client` thêm
    `promote_stage1_to_stage2()`; `push_to_anki` bỏ ghi `fields["Image"]` (ghi vào field không
    tồn tại là AnkiConnect từ chối CẢ note); `setup_inbox.py` dựng cả hai preset + trần cha.
    ⚠️ Chỗ suýt sót: `tgbot/flow_scan.py` còn import `INBOX_DECK` — bot sẽ **crash lúc khởi
    động**. Bài học: sau khi đổi hằng số trong config, phải nạp thử **toàn bộ** module như lúc
    bot khởi động, không chỉ module vừa sửa.

- **`/don` gộp TẤT CẢ TRONG MỘT: sync về → dọn GĐ1→GĐ2 → dọn GĐ2→kho → sync lên.**
  User: *"việc sync cũng khá cồng kềnh, tích hợp /don tất cả trong một để học xong tôi làm thủ
  công cho nhanh"*. Lỗ hổng bản cũ: **chỉ sync SAU** khi dọn → VPS xử lý trên ảnh chụp cũ, và
  đúng những thẻ user vừa học xong trên iPhone lại là thẻ bị bỏ sót. Nay **luôn sync KÉO VỀ
  trước**. Sync đầu hỏng thì vẫn dọn tiếp (idempotent, cùng lắm chuyển ít thẻ hơn) nhưng **báo
  ra** để user không tưởng xong. Thân tách thành `run_don()` dùng chung cho `/don` và job 3h.

- **CẢNH BÁO BẤT THƯỜNG QUA TELEGRAM (`tgbot/alerts.py`) — bịt lỗ "hỏng im lặng".**
  User: *"những gì bất thường thì đều phải nhắn"*. Đây là hệ quả trực tiếp của việc VPS kẹt sync
  2 ngày mà không ai biết: `trigger_sync` chỉ `log_warn` ra journal rồi trả `False`.
  ⚠️ **Nguyên tắc: cảnh báo phải CÓ TIẾT CHẾ.** Nhắn mỗi 30 phút suốt hai ngày thì user sẽ tắt
  thông báo của bot, và lần hỏng THẬT tiếp theo lại không ai thấy — tệ hơn cả không cảnh báo. Nên:
  bỏ qua lỗi thoáng qua (báo sau **2 nhịp liên tiếp**), đang hỏng thì nhắc lại **6 tiếng/lần**,
  hết hỏng thì báo **một** tin "đã bình thường" rồi im.
  Đã phủ: sync định kỳ, job nền ném exception (`_guard`, báo ngay lần đầu vì luôn bất thường),
  backup đêm thất bại, job dọn 3h chạy không trọn.
  `sync_error_hint()` dịch lỗi thô thành VIỆC CẦN LÀM — "Sync status 2" ra đúng ba bước
  Upload/Download, vì lỗi đó **không tự khỏi**, phải có người bấm tay.
  `anki_client.sync_now()` trả `(ok, err)`; `trigger_sync()` giữ nguyên làm vỏ mỏng cho code cũ.
  Đã test logic tiết chế bằng bot giả: nhịp 1 im, nhịp 2 nhắn, nhịp 3-5 im, qua 6 tiếng nhắc lại,
  khỏi thì nhắn một tin, vẫn khoẻ thì im.

- **VNC vào VPS bị CẮT XÉN màn hình: màn hình ảo 1024×768 → 1600×900.**
  User: *"mở qua vnc.bat, màn hình VPS nhiều lúc toàn bị cắt xén"*. Nguyên nhân không phải
  TightVNC: container **KHÔNG chạy Xvfb** mà dùng thẳng plugin VNC của Qt (`QT_QPA_PLATFORM=vnc`),
  nên "màn hình" chỉ là một khung Qt dựng sẵn, mặc định của image là **1024×768** — nhỏ hơn cửa
  sổ Anki + các hộp thoại của nó.
  **Cách đo (dùng lại được):** bắt tay RFB rồi đọc `ServerInit` trả `width/height` — số thật,
  không phải ước lượng bằng mắt trong VNC viewer. Container không có `xdpyinfo` và cũng không có
  X server để hỏi.
  Sửa: `docker-compose.yml` thêm `QT_QPA_PLATFORM=vnc:size=1600x900`.
  ⚠️ **Thử trên container NHÁP trước** (image y hệt, port 5901, /data riêng) để nếu Qt không nhận
  tham số thì Anki thật không chết kéo theo bot. Container nháp báo đúng 1600×900 mới áp vào thật.
  Trước khi `docker compose up -d` thì gọi `sync` một phát cho chắc. Sau khi dựng lại: đo lại RFB
  = 1600×900, AnkiConnect trả 870 thẻ, bot vẫn `active`.

- **VPS ĐANG KẸT SYNC TỪ 25/07 — phát hiện khi kiểm tra trước lúc làm.** `journalctl` cho thấy
  `Sync status 2` lặp lại mỗi 30 phút suốt hai ngày. Nguyên nhân: thêm field `Mnemonic` (25/07)
  là schema mod, laptop đã Upload nhưng **VPS chưa bao giờ Download**. `trigger_sync()` chỉ
  `log_warn` rồi trả False — **không cảnh báo tới Telegram**, nên hỏng im lặng.
  Xác nhận VPS chỉ là bản tụt hậu, an toàn để Download: RU_Word trên VPS có **11 field, không có
  Mnemonic**; **0 note** có Mnemonic; **0 note** thêm trong 2 ngày; 870 thẻ = bằng laptop.
  → Rút gọn được quy trình: làm hết thay đổi trên laptop rồi Upload MỘT lần, VPS Download MỘT
  lần (thay vì gỡ kẹt trước rồi lại Download lần hai).
  **Việc nên làm sau:** cho `trigger_sync` báo Telegram khi lỗi lặp lại, đừng để hỏng im lặng.

- **Sửa 51 mnemonic vốn chỉ là "giải thích nghĩa bằng hình ảnh", không có cầu âm thanh.**
  User bắt lỗi bằng ví dụ cụ thể: *"прошедший bạn giải thích là đoàn tàu vừa đi qua, chỉ còn khói.
  Mnemonic ở chỗ nào vậy? Tôi nghĩ mnemonic phải có những từ âm tiết ở trong câu chuyện ngắn chứ"*.
  Đúng — một câu chuyện minh hoạ **nghĩa** không phải mnemonic; mnemonic phải bắc cầu từ **âm đọc**
  sang nghĩa. Đã rà cả 271 và viết lại 51 câu hỏng, mỗi câu giờ có cụm tiếng Việt đọc gần giống:
  прошедший → “**bờ-ra… XIẾT**”, положительный → “**bỏ lại… giỏ**”, письменно → “**bịt miệng**”,
  воскресение → “**vọt khỏi**”, себя → “**xi… BIA**”, почему → “**vì chi mà?**”, жительство →
  “**ghi tên**”, помощь → “**bơm mạch**”, земля → “**giẫm… lia**”, жена → “**giữ nhà**”…
  ⚠️ **Từ mượn quốc tế KHÔNG nằm trong danh sách sửa** vì chính từ tiếng Anh đã là cầu âm thanh
  (economist ↔ экономист) — đó vẫn là mnemonic hợp lệ với user B2.
  Bản vá nằm ở khối `S.update({...})` cuối `data/mnemonics/stories01_inbox_2026-07-25.py`.

## 25/07/2026

- **Đổi tên nhãn field thành "Hướng dẫn" + ĐƯA MNEMONIC LÊN ĐẦU, từ nào cũng phải có.**
  User phản hồi sau khi dùng thử lô đầu: phần chẻ gốc "rất đúng" nhưng **thứ quan trọng nhất là
  mnemonic thì lại thiếu** ở phần lớn thẻ (từ mượn tiếng Anh và từ có gốc rõ ràng bị bỏ trống mẹo).
  ⇒ Đảo lại thứ tự ưu tiên: **mnemonic là bắt buộc và luôn đứng đầu**, phân tích gốc từ tụt xuống
  làm phần bổ trợ. Trong field giờ có 4 tầng theo đúng thứ tự:
  `mn-read` (phiên âm) → **`mn-story` (mnemonic, bắt buộc)** → thân bài chẻ gốc (`mn-content`) →
  `mn-tip` (dòng cách nhớ).
  - `card.css`: thêm `.mn-story` (16px, #f2cc60, đậm, có `::before` là 🎬) và **hạ tông `.mn-content`**
    (15px #e3b341 → 14px #b9975b) để phần phân tích không tranh mắt với mnemonic.
  - `back_template.html`: nhãn `Thầy nhắc` → **`Hướng dẫn`**.
  - Nội dung 271 mnemonic soạn tay ở `data/mnemonics/stories01_inbox_2026-07-25.py` (bổ sung cho
    `batch01_…py`; key = từ đã bỏ dấu trọng âm U+0301 và ký tự zero-width U+200B — thẻ `лес` có
    kèm U+200B, `Китай` viết hoa, hai bẫy này làm lệch khớp nếu không chuẩn hoá).
  - Dọn trùng: **34 thẻ** vốn đã có mẹo âm thanh nằm ở thân bài (kiểu `<b>"CẠO TÓC-ka"</b> — …`)
    thì **xoá thân bài**, giữ mnemonic mới; các thân bài mang thông tin thật (gốc `врать` của врач,
    cặp vần лёд–лес, `не + который`…) thì giữ nguyên.
  - **271/271 thẻ inbox đều có `mn-story`.** Không cần full sync cho bước này (chỉ sửa nội dung note
    + template/CSS), nhưng full sync của lần THÊM FIELD vẫn đang treo — xem mục dưới.

- **Thêm field `Mnemonic` ("Thầy nhắc" → nay là "Hướng dẫn") vào note type RU_Word — nội dung do Opus 5 soạn ĐỊNH KỲ,
  KHÔNG sinh lúc tạo thẻ.** User thử mnemonic bằng `gemini-3.5-flash` (free) thấy ~50% là rác ở
  nhánh âm thanh (bịa âm vô nghĩa "sa chà", "cà khịa") + phiên âm sai (о không nhấn phải đọc "a").
  Đối chứng cùng 8 từ: nhánh **chẻ gốc** hai bên hoà, nhánh **âm thanh** thì model nhỏ thua rõ.
  ⇒ Chốt: mảng mnemonic tách khỏi Gemini, do Opus 5 làm theo lô; Gemini giữ nguyên việc sinh ví
  dụ + topic + quét ảnh (miễn phí, đang chạy tốt).
  **Ý user quan trọng:** đây KHÔNG phải "mẹo nhớ" mà là **lời thầy hướng dẫn** — mỗi từ một cách:
  từ mượn quốc tế thì chỉ mặt từ tiếng Anh tương ứng (user B2/IELTS 6.5), từ có gốc Nga thì chẻ
  gốc, từ khó quá mới dùng mẹo âm thanh. Cấu trúc field 3 phần: `mn-read` (phiên âm có trọng âm)
  → thân bài → `mn-tip` (dòng "cách nhớ", tách bằng gạch đứt).
  Đã làm: `modelFieldAdd` Mnemonic; `back_template.html` chèn khối `{{#Mnemonic}}` **sau Vietnamese,
  trước Context Examples**; `card.css` thêm `.mnemonic-box/.mn-label/.mn-read/.mn-content/.mn-tip`
  (tông hổ phách #d29922, khác xanh lá của ô Tiếng Việt); `createModel.inOrderFields` thêm Mnemonic.
  **Đã ghi đủ 271/271 thẻ trong `RUSSIAN::0-inbox`.**
  ⚠️ Thêm field = **schema mod = Anki đòi FULL SYNC**. Đã `/backup` trước (47 MB, 3 deck, 0 lỗi,
  `backups/2026-07-25_2315`). AnkiConnect KHÔNG trả lời được hộp thoại Upload/Download nên **không
  gọi sync bằng script** — user phải bấm trong GUI và chọn **Upload**, sau đó iPhone sync để tải về.
  ✅ `update_note_fields()` truyền dict MỘT PHẦN nên `/sua` và luồng làm lại thẻ **không xoá** Mnemonic.

- **Bác bỏ lập luận "cày Again vô hại vì FSRS có mean reversion" — bằng số của chính collection.**
  User mang về bản tổng hợp (AI khác) nói "5–8 lần Good là D về mức bình thường, không có vết
  sẹo vĩnh viễn". Kiểm: `fsrsParams6` cho **`w7 = 0.001` — SÀN CỨNG của FSRS**, tức optimizer
  nhìn 8476 lượt ôn rồi kết luận "thẻ khó ở người này không bao giờ thành dễ". Thêm nữa
  `ΔD = −w6×(rating−3)` ⇒ **Good (rating=3) không giảm D chút nào**. Mô phỏng từ D=92%:
  5 lần Good → 91.5%, 8 lần → 91.3%, **610 lần mới về 50%**.
  Thực nghiệm (nhóm đối chứng ghép theo tiền sử): **84 thẻ từng Again ≥3 lần và hiện có chuỗi
  Good ≥5 → 68 thẻ vẫn D 90–100%, 16 thẻ 70–90%, 0 thẻ dưới 70%.** Số Again trung vị theo nhóm
  D: 0 / 0 / 1 / 2 / **8**.
  Giá thật của D cao (qua số hạng `(11−D)` trong công thức tăng S): bấm Good trên thẻ S=10 ngày
  → D=30% lên 35 ngày, D=92% chỉ lên 16 ngày; sau 6 lượt Good nữa là **11,5 năm vs 120 ngày**.
  ⇒ Kết luận: thẻ cứu được nhưng **không cứu bằng Good, chỉ bằng Forget/Reset**, và phải sửa
  luật chấm trước rồi mới reset. Lưu ý công bằng: `w7` là tham số per-user.
  ⚠️ Bẫy API phát hiện khi làm: `getReviewsOfCards` truyền id dạng **string trả về rỗng, không
  báo lỗi** — phải truyền int; luôn in tổng số lượt lấy được trước khi tin kết quả.

- **Độ dài từ mới là biến số lớn nhất của D — user chẩn đoán đúng.** User giải thích "thẻ đầu
  toàn từ đơn âm tiết nên thuộc nhanh, giờ tới từ 3–4 âm tiết nên thẻ nào cũng kịch độ khó".
  Đo D theo số âm tiết (đếm nguyên âm Nga trong `WordClean`): **1 âm tiết → D 40% | 2 → 88% |
  3 → 96% | 4 → 96% | 5+ → 96%**, đơn điệu tuyệt đối ⇒ phần lớn D cao là **độ khó ngôn ngữ
  thật**, không phải lỗi cách chấm. Các lần đo trước chưa tính tới biến này.
  **Thời gian 14 ngày (14,9h): học thẻ mới 6,9h (46%) | ôn tập 5,1h (34%) | học lại 2,9h (19%)**;
  mỗi lượt ôn 8,0s vs thẻ mới 7,0s ⇒ **ôn tập không phải gánh nặng, số lượt thẻ mới mới là**
  (user nói đúng). Số lượt learning trung vị để tốt nghiệp 1 thẻ = **4** (tối thiểu lý thuyết 2).
  📌 **User quyết: học tiếp theo cách của mình ~2 tuần rồi thống kê lại.** Đã lưu mốc so sánh
  `data/anki_baseline_2026-07-25.json` (kèm cardId tại mốc để nhận ra thẻ mới). Lần đo sau phải
  **so từ 3 âm tiết với từ 3 âm tiết** mới tách được "từ khó thật" khỏi "cách chấm".

- **KHÔNG sửa tay `w7` — và thu hẹp lại kết luận "D là hóa thạch" của mục dưới.** User hỏi
  "sao không sửa `w7` cho phù hợp hơn". Đo tỉ lệ nhớ THẬT trên lượt review có lịch (type=1),
  mục tiêu DR=90%: **D<90% đạt 93.4% (chuẩn) | D≥90% chỉ 61.1% (hụt 29 điểm) | toàn bộ 70.2%**.
  ⇒ Thẻ D≥90% đang được cho khoảng cách **quá DÀI chứ không phải quá ngắn**; nâng `w7` sẽ hạ D,
  giãn lịch thêm, tụt dưới 61%. D không phải nhiệt kế hỏng — 61% mới là cơn sốt.
  Tách 325 thẻ D≥90% ra thấy hai loài: **nhóm A (68 thẻ, 5 lượt cuối toàn đúng) — 3 lượt gần
  nhất 204/204 = 100%** ⇒ hóa thạch thật, nên reset; **nhóm B (257 thẻ) — 3 lượt gần nhất chỉ
  69.1%** ⇒ D≥90% là ĐÚNG với chúng, không được reset/hạ D. Mục dưới nói "D là hóa thạch" cho
  cả 325 thẻ là **quá rộng, đã sửa**.
  Ba lý do bỏ hướng `w7`: (1) đặt w7=0.05 thì số thẻ D≥90% tụt **348 → 10**, xóa nhãn khó của
  257 thẻ đang thật sự khó; (2) `w7` là **kết luận** optimizer rút từ 8476 lượt ôn, không phải
  tuỳ chọn; (3) **bấm Optimize một lần là mất**, muốn giữ thì phải bỏ Optimize vĩnh viễn.
  ⇒ Việc đúng: Forget/Reset **chỉ nhóm A**, tính lại danh sách tại thời điểm reset (nhóm B sẽ
  dần chuyển sang A nhờ luật chấm mới), để yên `w7`.

- **Đo tiếp: user ĐÚNG về việc mình học được, và đó chính là lý do phải reset.** User lập luận
  "tôi Again nhiều chỉ vì chưa liên kết được từ với nghĩa; liên kết rồi thì không sai nữa; bấm
  Good 10–20 lần là thẻ về bình thường". Kiểm từng vế:
  - **Vế học: ĐÚNG.** Trên chính 325 thẻ D≥90%, tỉ lệ đúng theo thứ tự lần review:
    **40% → 45% → 65% → 70% → 78% → 81% → 82% (lần 8+)**. Và 550 thẻ đạt mốc đúng 2 lần trên
    hai ngày khác nhau thì **396 thẻ (72%) không bao giờ Again nữa**.
  - **Vế sửa D: SAI.** Từ D=92%, bấm Good 10 lần → 91.08%, **20 lần → 90.18%** (mua được 1.8
    điểm). Vì `ΔD = −w6×(rating−3)` mà Good có rating=3 ⇒ số hạng bằng **0**.
  ⇒ Ghép lại: user đã thuộc thật (82%) nhưng D kẹt 92% ⇒ **D là hóa thạch của thời cày cũ,
  không còn mô tả trí nhớ hiện tại**. Tiêu chí reset nhắm gọn: **D≥90% nhưng mấy lượt gần nhất
  đúng**; làm theo lô để không vỡ hạn ngạch 70 từ mới/ngày; vẫn chờ ~2 tuần xác nhận kỷ luật
  chấm mới rồi mới reset (reset trước thì D leo lại, mất trắng).
  **Tải ôn tập thực đo:** 309 → **479 lượt/ngày** trong một tuần (+55%) ở 870 thẻ (~1,3 giờ/ngày
  ở 9,6 s/lượt); ngoại suy 3000 thẻ ≈ **1650 lượt/ngày, >4 giờ/ngày**. D thấp cho ×3.5/lượt
  (dày rồi thưa dần — đúng ý user), D=92% cho ×1.6 (**dày mãi mãi**).

- **Relearning cũng phải 2 bậc `1m 15m` — luật tốt nghiệp thống nhất cho cả thẻ mới lẫn thẻ quên.**
  User muốn một luật duy nhất: thẻ chỉ được rời learning/relearning khi có **2 lượt Good
  liên tiếp cách nhau ≥15 phút**. Trước đó relearn chỉ có 1 bậc `10m` → thẻ quên bấm Good
  một phát là quay lại lịch ôn ngay, lỏng hơn hẳn thẻ mới. Đã đặt `lapse.delays = [1, 15]`
  và `new.delays = [1, 15]` cho CẢ 3 preset (`inbox`, `russian-parent-70`, `Default`) qua
  saveDeckConfig — Default quan trọng vì thẻ tốt nghiệp nằm ở topic deck, quên là quên ở đó.
  Ghi chú cơ chế (scheduler v3): trong learning/relearning chỉ **Good mới tiến bậc**;
  **Hard đứng yên tại bậc hiện tại** (bấm Hard mãi không bao giờ tốt nghiệp), Again về bậc 1,
  Easy nhảy cóc tốt nghiệp luôn (thẻ mới đừng bấm — bay 1,4 tháng). Verify + sync xong.
  Đã ĐO trên thẻ thật đang ở bậc cuối (`cardsInfo.nextReviews`, `left=1`):
  **Again 1m / Hard 15m (giẫm chân) / Good 1d (tốt nghiệp) / Easy 2d** — xác nhận Hard không
  tiến bậc. ⚠️ Hệ quả: bấm Hard mãi ⇒ thẻ lặp 15 phút vô hạn trong ngày, chỉ Good mới thoát.
  Luật thao tác: **quên thật ⇒ Again thẳng** (bậc `1m` chính là lượt gõ lại, khỏi undo);
  **nhớ ra mà sai 1–2 ký tự ⇒ undo gõ lại rồi Hard**. Undo cứu lỗi chính tả, không cứu lỗi quên.

## 22/07/2026

- **Chỉnh deck options: bỏ bậc học `1m`, chặn cày Again trong cùng buổi.** User hỏi ý kiến
  về việc retention tụt còn ~70% và độ khó trung vị 92%. Kéo số liệu thật qua AnkiConnect
  (841 thẻ RU_Word, 6833 lượt ôn, 18.2 giờ) thì thủ phạm KHÔNG phải FSRS — FSRS đã bật, đã
  optimize sẵn (21 tham số), desiredRetention đang 0.9 (Gemini khuyên hạ 0.88 là đi NGƯỢC:
  DR thấp = khoảng cách dài hơn = retention còn tụt nữa).
  Thủ phạm là **bậc learning `1m`**: thẻ sai quay lại sau 1 phút nên user gõ lại 5–10 lần
  tại chỗ. Ba con số kết tội:
    1. lượt lặp thứ 3 trở đi của cùng thẻ cùng ngày = 3283 lượt = **9.0/18.2 giờ (50%)**;
    2. tỉ lệ Again TĂNG dần theo lần lặp trong ngày (45→51→59→62→65→69→71%) — cày không
       giúp nhớ hơn, nếu giúp thì đường này phải đi xuống;
    3. thẻ hôm tốt nghiệp bị cày ≥4 lượt chỉ sống sót lần review thật đầu tiên **47.5%**,
       thẻ không bị cày sống **82.3%** → "tốt nghiệp giả" là có thật, đo được.
  Cũng phát hiện preset `Default` (29 deck chủ đề) để **new/day = 999** — hiện vô hại vì
  0 thẻ mới nằm ngoài inbox, nhưng là mìn: thẻ mới lọt vào deck chủ đề qua `/deck` sẽ bỏ
  qua trần 50 của inbox.
  Đã đổi (qua `saveDeckConfig`, có sao lưu bản cũ, đọc lại xác nhận):
    - learning steps: `Default 1m 15m` / `inbox 1m 10m` → **`15m`** (cả hai)
    - new/day: Default `999` → **20**; inbox giữ **50**
    - max reviews/day: `9999` → **500** (lưới an toàn) — relearn `10m` và DR `0.9` giữ nguyên
  Đổi lúc 0 thẻ đang ở trạng thái learning nên không gián đoạn thẻ nào.
  ⚠️ Còn 1 việc PHẢI làm tay trong GUI (AnkiConnect không đụng tới được):
  Tools → Preferences → Review → **Learn ahead limit = 0 phút**.
- **SỬA LỖI DO TÔI GÂY RA: trần thẻ mới của deck CHA `RUSSIAN` kẹp cả cây xuống 20/ngày.**
  User tự phát hiện: "deck tổng để 20 mà tôi muốn học 70, có nhầm không?" — đúng, và là lỗi
  của tôi. Sáng nay tôi hạ preset `Default` (deck cha RUSSIAN dùng preset này) 999 → 20 gọi
  là "lưới an toàn". Nhưng **Anki scheduler v3 áp giới hạn thẻ mới của deck CHA lên tổng các
  con** — nên RUSSIAN=20 kẹp inbox (70) xuống 20, dù học thẳng deck con. Trước khi tôi đụng
  vào (999) thì trần cha quá cao nên vô hại; chính thay đổi sáng nay bịt cổ chai.
  Đo bằng `getDeckStats.new_count` (đã áp mọi trần): trước sửa RUSSIAN=6 còn 0-inbox=56
  (chênh 50 = đúng chỗ trần cha bám); sau sửa **RUSSIAN=56 = 0-inbox=56**. Bằng chứng trần
  thật sự bám chứ không phải lý thuyết.
  Cách sửa (phẫu thuật, không đụng topic decks/GRAMMAR): `cloneDeckConfigId` từ Default →
  preset mới `russian-parent-70`, `setDeckConfigId` gán CHỈ deck cha RUSSIAN vào đó,
  new/day=70. Topic decks giữ Default=20 (vô hại vì ~0 thẻ mới), GRAMMAR không bị đụng.
  → Bài học: **trần điều tiết thẻ mới cả cây là ở DECK CHA, không phải deck con.** Muốn giới
  hạn tổng/ngày thì đặt ở cha; đặt ở con mà quên cha thì con bị cha kẹp.

- **User BỎ filtered deck, drill THẲNG trong inbox bằng undo; inbox steps về `1m 15m`.**
  User thấy filtered deck lệch inbox: thẻ trong filtered deck bị RÚT khỏi inbox nên sáng
  thêm từ mới mà chưa Rebuild thì filtered deck vẫn ôm bộ cũ, hai bên lệch nhau (đã xác nhận:
  `0-inbox-luyen` vẫn giữ 4 thẻ — đúng chỗ gây cảm giác "không đồng bộ"). Cách mới của user:
  gõ sai → **undo** (gán cử chỉ vuốt trên iPhone) → gõ tới khi đúng → bấm nút. Undo hoàn
  nguyên trọn vẹn revlog + scheduler nên không bẩn D — tương đương filtered deck nhưng gọn
  một chỗ. Hợp lý, tôi ủng hộ (đảo lại việc tôi cố giữ hai-deck).
  Đặt lại inbox learning steps `15m` → **`1m 15m`** theo yêu cầu (42 thẻ đang learning lúc
  đổi; v3 tự xử, không gián đoạn).
  ⚠️ **Chi tiết quyết định thành–bại đã dặn user: sau undo-drill tới khi gõ đúng, bấm GOOD
  chứ KHÔNG bấm Again.** Trong learning, Again ghi ease=1 → ĐẨY D LÊN (đúng cái đã sửa cả
  ngày); Good → 15m, D sạch. Vòng undo CHÍNH LÀ luyện ngắn hạn, không cần Again. Bậc `1m`
  chỉ kích hoạt khi bấm Again → nếu luôn Good thì `1m 15m` chạy y hệt `15m`. User hiểu
  "again = drill thêm" là sai; Again = "bỏ thẻ ra mai tính".
  Pre-sync (điểm user hỏi): user chọn KHÔNG cần — thêm thẻ vốn là merge, không ghi đè lịch.
  Sẽ đo lại phân bố D sau 2–3 tuần: kỷ luật undo giữ thì D thấp, trượt (quen tay Again) thì
  `1m` khuếch đại flood và sẽ lộ ra.

- **Nâng inbox `new/day` 50 → 70 và BỎ trần ôn tập (500 → 9999).** User học 0→A1 trong 2
  tháng, lớp 4 buổi/tuần mỗi buổi 60–70 từ; mục tiêu của user là **cày hết bài của ngày hôm
  đó**, còn ~150 từ nợ cũ thì dành 3 ngày nghỉ trong tuần để trả dần.
  Trần 50 phá đúng mục tiêu đó: hôm nay thêm 80 từ mà chỉ học 50, 30 từ thừa bị đẩy vào hàng
  chờ — và vì inbox gom `Highest position` nên buổi học sau chúng bị bài mới hơn chen lên
  trước, chỉ được đụng vào ngày nghỉ, trộn lẫn với nợ cũ. Đặt 70 thì cơ chế mới-nhất-trước
  tự tách bạch đúng ý user: ngày có lớp bài mới luôn nằm trên cùng → học trọn bài; ngày nghỉ
  không có gì thêm → nhóm cũ nhất trồi lên → trả nợ. Không phải đổi search hay thứ tự gì.
  Ước tính: thêm ~260 từ/tuần, học được ~490/tuần → ròng −230/tuần, 238 thẻ tồn hết trong
  1–1.5 tuần.
  **Bỏ trần ôn tập vì trần ôn chỉ sinh ra NỢ ôn tập** — thẻ đến hạn không biến mất, nó dồn
  sang hôm sau rồi cuộn tuyết. Trần 500 hợp lý lúc 50% số lượt của user là cày lãng phí,
  nhưng nay đã dẹp việc cày và user đang chạy deadline nên nó chỉ còn giấu việc đi. Muốn
  giảm tải thì vặn `new/day` hoặc DR, đừng chặn review.
  ⚠️ Kéo theo: **limit của deck lọc `0-inbox-luyen` phải nâng 50 → 70** cho khớp, không thì
  phòng tập chỉ phủ 50/70 từ mà kỳ thi hỏi cả 70.

- **Lộ trình cuối: deck lọc `0-inbox-luyen` làm BUỔI LÀM QUEN, inbox làm BÀI THI — đã kiểm
  chứng bằng số liệu thật.** User tự nghĩ ra và nó đúng hướng (chính là "tách bước làm quen
  khỏi bước kiểm tra"): ôn thẻ cũ → cày 50 từ mới trong deck lọc kiểu cũ (sai rồi sửa tới
  khi đúng) → sang inbox thi thật.
  Cấu hình deck lọc: search `deck:RUSSIAN::0-inbox is:new`, limit 50,
  **Selected by = `Latest added first`**, **Reschedule TẮT**, delay Again 1m/Hard 5m/Good 10m.
  ⚠️ **Phải đọc `newGatherPriority` của deck inbox TRƯỚC khi chọn thứ tự cho deck lọc.**
  User hỏi đúng câu quan trọng nhất: "inbox có 238 thẻ mới, mỗi ngày chỉ lôi 50 ra — làm sao
  biết deck lọc lôi ĐÚNG 50 thẻ đó?" Inbox của user để `newGatherPriority = 2` =
  **Highest position (MỚI thêm nhất trước)**, cố ý đặt (mặc định Anki là 0) vì user muốn học
  từ của bài gần nhất trước. Nên `Latest added first` — thiết lập BAN ĐẦU của user — mới
  đúng; đã đo ở limit 50 nó trùng `Highest position` **50/50** (top 80 thì lệch 5).
  **Tôi đã hướng dẫn SAI ở đây và phải ghi lại để không lặp:** tôi bảo user đổi sang
  `Order due` (sắp position THẤP→CAO = lấy 50 từ CŨ NHẤT, ngược hoàn toàn), rồi tự chạy
  kiểm và reo "khớp 50/50 ✅" — nhưng đó là khớp với danh sách kỳ vọng do chính tôi tính
  sai. **Phép kiểm chỉ chứng minh deck lọc chạy đúng lệnh, không chứng minh lệnh đúng.**
  User phát hiện ra ("tôi tưởng tôi muốn học những từ mới thêm vào đầu tiên"). Kiểm một hệ
  thống thì phải kiểm cả tiêu chí kỳ vọng, đừng chỉ kiểm việc thực thi.
  Bài học đo lường thứ hai: KHÔNG đọc được số thứ tự thật khi thẻ còn trong deck lọc — `due`
  bị **ghi đè** (thành −99xxx hoặc timestamp lần hiện lại) và `cardsInfo` KHÔNG trả
  `odue`/`odid`. Cũng không được dùng noteId thay cột position (đã kiểm trên 189 thẻ inbox:
  sort theo `due` ≠ sort theo noteId). Quy trình đúng, bắt buộc theo thứ tự: Empty → thẻ về
  nhà, `due` khôi phục → chụp `due` toàn bộ thẻ mới, tính 50 thẻ position CAO nhất và ghi id
  → Rebuild → đối chiếu id. Muốn tuyệt đối chính xác thì search bằng `prop:pos>=<ngưỡng>`
  (đo được ngưỡng = 1771714), nhưng ngưỡng đổi mỗi ngày nên `Latest added first` tiện hơn.
  Đã chụp trạng thái trước rồi so sau khi user cày thử 10 lượt (9 Again + 1 Good):
    - **10/10 lượt ghi vào revlog dưới dạng `FILTERED/cram` (type=3), 0 lượt learn/review**
      → không chạm D, S hay lịch ôn;
    - 50 thẻ vẫn `type=0` (MỚI), `reps=0`; inbox vẫn đủ 242 thẻ mới;
    - thẻ bấm Good thì RỜI deck lọc về nhà `RUSSIAN::0-inbox`, vẫn nguyên trạng thái mới.
      → quy ước nút trong phòng tập: Again/Hard = giữ lại cày tiếp, Good = xong, tống ra.
  Đo được luôn hai thứ trước đó phải phỏng đoán:
    - **`{{Deck}}` trả về deck GỐC chứ không phải tên deck lọc** (thẻ nằm trong
      `Filtered Deck 13:04` vẫn render ra `RUSSIAN::life::home`) → hint tự hiện đúng trong
      buổi cày, KHÔNG cần mẹo đặt tên deck lọc chứa chuỗi `0-inbox`.
    - Thẻ trong deck lọc mang `queue=2` nhưng `type=0` — nhìn `type` mới đúng, đừng hoảng.
  ⚠️ Bẫy đã cảnh báo user: cày xong THI NGAY trong cùng buổi thì bài thi đo lại chính buổi
  cày, và nguy hơn kiểu cũ — vì FSRS không thấy buổi cày nên tưởng user nhớ ngay lần đầu và
  giao ~8.4 ngày (kiểu cũ giao ~1 ngày vì thấy hết các lượt Again). Chữa: cày tối, thi sáng
  hôm sau; hoặc thi cùng buổi thì chấm cao nhất là Hard, để dành Good cho hôm sau.
  Ghi chú UI: số hiện trên deck lọc là "số thẻ học được NGAY BÂY GIỜ", không phải số thẻ
  còn lại — bấm Again 9 thẻ thì 9 thẻ đó vào hàng đợi 1 phút nên 49 tụt xuống 40, hết phút
  tự bò lên. User tưởng mất thẻ.

- **RÚT LẠI đề xuất reset 64 thẻ "D cao nhưng chưa quên lần nào" — nguyên nhân thật là
  LUẬT CHẤM ĐIỂM, không phải việc cày.** Đã định `Forget` 64 thẻ D≥90% + lapses=0 (toàn từ
  vỡ lòng: зелёный, март, суббота, весна, больница — 965 lượt ôn, 15.1 lượt/thẻ, không thẻ
  nào thoát mốc 2 ngày). User khai thêm hai điều làm đảo kết luận: mấy từ đó **mới học 1–2
  ngày**, và user **chấm "sai 1 ký tự = Again"**.
  Đo lại để kiểm lời khai, và nó khớp: thời gian trung vị trước khi bấm **Again 7.6s vs
  Good 7.0s — gần bằng nhau**, chỉ **3.0%** lượt Again bấm dưới 3 giây. Tức 97% lượt Again
  là user ĐÃ GÕ TRỌN một từ rồi trượt ở vài ký tự — không phải quên từ. (Nếu quên thật thì
  lượt Again phải nhanh: không gõ gì, bấm luôn.)
  Vậy 3835 lượt Again phần lớn là **trượt đuôi `-ый/-ий/-ой`, `ё/е`** chứ không phải thất
  bại trí nhớ; bài kiểm tra gõ đang trộn "biết từ" với "biết chính tả" vào một điểm số rồi
  đổ hết vào D. Việc cày chỉ là hệ quả: chấm gắt → Again ngập → thấy buộc phải cày.
  → **Không reset lúc này**: chữa triệu chứng trong khi nguyên nhân còn sống thì D leo lại
  90% trong một tuần. Thứ tự đúng: đổi luật chấm → 2–3 tuần dữ liệu sạch → Optimize (D
  được tính lại từ lịch sử đã phân biệt được "sai đuôi" với "không biết từ") → ĐO LẠI rồi
  mới reset thẻ nào còn ≥90%.
  Luật chấm mới: không nhớ nổi = **Again**; nhớ ra từ nhưng sai 1–2 ký tự, hoặc đúng mà
  phải nghĩ lâu = **Hard**; đúng trôi chảy = **Good**; bật ra ngay = **Easy**.
  Nút bấm là báo cáo về TRÍ NHỚ, không phải điểm cho ngón tay — chỗ học chính tả là bảng
  diff đỏ/xanh ở màn đáp án, nó hiện y hệt dù bấm nút nào. User đang dùng hệ 4 nút như hệ
  2 nút (Again 56.1% / Hard 2.4% / Good 41.4% / Easy 0.1%).

- **Chỗ "cày cho đã" mà không phá lịch: filtered deck tắt reschedule.** User nói thẳng lý
  do bấm Again khi sai 1 ký tự: *muốn gõ lại NGAY để có cảm giác mình đang thuộc*. Nhu cầu
  đó thật và cần cho việc học cả ngày, nên đừng dẹp — chuyển nó sang đúng quầy:
  Tools → Create Filtered Deck, search `note:RU_Word rated:1:1` (đúng những từ bấm Again
  hôm nay), **BỎ TÍCH "Reschedule cards based on my answers in this deck"**, Build; hằng
  ngày chỉ cần Rebuild. Gõ lại bao nhiêu lần cũng được mà D/S/lịch ôn không suy suyển.
  Deck thường = kỳ thi (chấm trung thực), filtered deck = phòng tập (cày thoải mái).
  ⚠️ AnkiConnect KHÔNG tạo được filtered deck (`apiReflect` chỉ có `forgetCards`, không có
  action nào cho filtered/cram) — chỗ này bắt buộc user tự bấm trong GUI.
  Hai cái bẫy đã vấp khi dựng: (1) `rated:1:1` = "bấm Again trong 1 ngày qua" nên **rỗng
  nếu hôm đó chưa ôn** → Anki báo "no cards matched" dù cú pháp đúng; dùng `rated:3:1`
  (158 thẻ, luôn có nội dung) rồi đặt Limit ~40. (2) Hộp thoại Create Filtered Deck **điền
  sẵn deck đang chọn** vào ô search — thêm câu vào sau thay vì xóa trắng thì dính
  `deck:"Mặc định"` (deck rỗng, 0 thẻ) và cũng ra 0. Cách chẩn: thử câu đơn giản nhất
  (`note:RU_Word` = 833 thẻ) trước; nếu ngay câu đó đã 0 thì lỗi không nằm ở search.
  Ghi chú phụ: sau khi bỏ bậc `1m`, bấm Again KHÔNG còn cho gõ lại tức thì nữa (thẻ mới
  15 phút, relearn 10 phút, learn-ahead 0 chặn kéo sớm) — nên Again giờ chỉ còn là trả giá
  gấp đôi (+2 đơn vị D, tính lapse) cho một thứ không còn bán.

- **Hint chữ cái đầu trên mặt trước, tự rụng khi thẻ tốt nghiệp.** Xử nguyên nhân GỐC của
  mục trên: tỉ lệ Again ở lượt gặp ĐẦU TIÊN trong ngày đã là **45%** (chưa cày gì cả),
  vì thẻ chỉ có chiều sản sinh (nghĩa → gõ tiếng Nga) còn audio nằm ở mặt SAU. User:
  *"tiếng Nga có những từ không có tí liên kết nào"* — bấm Again nhiều lượt chỉ để moi ra
  1–2 chữ cái đầu. Chốt: hiện **mỗi chữ cái đầu**, không kèm số chữ cái.
  Cách làm chọn để KHÔNG đụng bot dòng nào và KHÔNG làm nở số thẻ:
    - dựng bằng **JS ngay trong `front_template.html`**, đọc `{{WordClean}}` đã có sẵn
      → không thêm field (thêm field sẽ bắt Anki đòi full sync), không sửa
      `push_to_anki` / `/sua` / parser đọc ngược HTML;
    - **không thêm card template** → 1 note vẫn = 1 thẻ. Đây là chỗ user lo "vài nghìn từ
      thì số thẻ mất kiểm soát": nỗi lo đó chỉ đúng với việc thêm card template thứ hai
      (3000 từ → 6000 thẻ), còn sửa cách hiển thị của thẻ đang có thì số thẻ đứng yên;
    - hint **chỉ hiện khi `{{Deck}}` còn chứa `0-inbox`**. Job đêm/`/don` vốn đã chuyển thẻ
      tốt nghiệp sang `RUSSIAN::<topic>`, nên bánh xe phụ tự rụng đúng lúc — tái dùng
      ranh giới inbox/topic có sẵn, không đẻ thêm cơ chế.
  An toàn: `display:none` đặt SẴN trong HTML chứ không do JS gắn → JS lỗi hay thiết bị
  chặn script thì hint không hiện, chứ không bao giờ lộ đáp án. Bản Anki nào không thay
  được `{{Deck}}` cũng rơi vào nhánh không-hiện-hint (hỏng theo hướng an toàn).
  Đã đo thật sau khi đẩy template, không tin suông: thẻ `RUSSIAN::0-inbox` (домашний) →
  hiện hint 'д'; thẻ `RUSSIAN::qualities` (много) → không hiện; cả hai đều xác nhận đáp án
  không lọt ra vùng hiển thị được.

- **Xác nhận relearning steps KHÔNG có lỗi** (user hỏi kiểm lại): `lapse.delays = [10m]`
  một bậc — đúng chuẩn FSRS, giữ nguyên. `lapse.mult = 0.0` vô hại vì FSRS bật thì Anki bỏ
  qua ô "New interval" và tự tính độ bền sau khi quên. Leech = 8 lần quên, hành động
  *Tag Only* (không tạm ngưng) — chưa thẻ nào thành leech, cao nhất mới 7 lapse.
  Tức toàn bộ 925 lượt relearn không phải chỗ rò rỉ; bậc học lỗi chỉ nằm ở khâu thẻ mới.

- **/thongke hiện thêm TRẠNG THÁI HỌC, tách riêng từng kho** (mới / đang học / trẻ /
  trưởng thành kèm %, như màn "Card Counts" của Anki). Mốc 21 ngày để tách "trẻ" khỏi
  "trưởng thành" là hằng số của chính Anki.
  ⚠️ Bản đầu lọc theo `note:"RU_Word"` — user nhắc kịp "đừng lẫn 2 deck lớn vào nhau",
  và hóa ra lọc theo model còn có lỗi NẶNG HƠN: mảng ngữ pháp GRAMMAR:: dùng model
  RU_Plural riêng nên biến mất hoàn toàn khỏi báo cáo mà không ai hay. Sửa: lọc theo
  DECK GỐC (`get_root_decks()` = tên không chứa '::'), mỗi kho một khối riêng, deck
  rỗng (vd 'Mặc định') thì bỏ qua chứ không hiện hàng số 0.
  Đo trước khi viết truy vấn, không đoán cú pháp Anki: trên chính collection này
  `is:new + is:learn + is:review = 163+4+574 = 741` = đúng tổng và không giao nhau,
  nên chia nhóm theo lối đó là kín. Thẻ TẠM NGƯNG/TẠM ẨN tách ra TRƯỚC (đúng thứ tự
  Anki làm) rồi phần còn lại mới chia — nếu không, 8 thẻ tạm ngưng sẽ bị đếm hai lần.
  Kết quả thật: RUSSIAN 159+0+453+121+8 = 741 ✓, GRAMMAR 94+4+26+0 = 124 ✓.
  Vẫn có dòng "❓ Khác" phòng khi bản Anki khác phân loại lệch đi — thà hiện ra còn
  hơn để tổng không khớp mà người đọc không biết.
  Đếm bằng `findCards` (chỉ trả về id) chứ KHÔNG dùng `cardsInfo`: cardsInfo kèm cả
  HTML mặt trước/sau đã dựng của từng thẻ — vài MB tải về chỉ để đọc queue/type.
  Các kho đếm song song bằng asyncio.gather -> cả báo cáo chạy 0.7s.

## 21/07/2026 (đợt 4)

- **Quét ảnh báo `этот ← это` là "từ MỚI" dù `это` đã có thẻ** — user báo ngay sau khi
  deploy đợt 3. Tin nhắn tự tố cáo thủ phạm: KHÔNG có dấu 🔧 nghĩa là pymorphy3 không
  hề sửa gì, chính GEMINI đổi `это`->`этот`, và trọng tài cố tình nhường nó (luật "đáp
  án AI nằm trong danh sách lemma hợp lệ thì giữ AI" — `этот` đúng là một lemma hợp lệ
  của `это`). Nguyên nhân gốc: prompt đợt 3 dạy "đại từ -> cách 1", AI áp dụng đúng luật
  nhưng QUÁ TAY. Kiểm bằng dữ liệu thật: collection có thẻ `это`
  (RUSSIAN::language::grammar), không có `этот`; OpenRussian có cả hai (`это`="this is",
  `этот`="this") nên bấm ✅ vẫn tạo được thẻ — tức là không lỗi to, mà là NHIỄU: từ mình
  đang học quay lại đội lốt từ mới.
  Sửa HAI TẦNG, tầng nào cũng chặn được một lớp lỗi khác nhau:
  (1) `reconcile_lemma()` thêm luật: từ điển xếp CHÍNH dạng thấy trên ảnh là lemma khả
  dĩ nhất -> giữ nguyên nó, không cho AI chia sâu thêm. Đo trước khi viết, luật tách
  sạch 21/21 từ chức năng (это, всё, что, как, надо, нужно, ничего, уже, тут...) mà
  KHÔNG đụng 18/18 dạng biến cách thật (дети, проверяем, шла, яйца, сестёр...), vì với
  chúng lemma xác suất cao nhất khác hẳn dạng trên trang. Đánh đổi đã cân nhắc: từ đồng
  âm kiểu `мой` (của tôi / rửa đi) sẽ theo từ điển thay vì ngữ cảnh AI — chấp nhận được
  vì có dấu 🔧 và user vẫn duyệt danh sách trước khi thêm.
  (2) Bộ lọc "đã có thẻ" giờ xét CẢ dạng nguyên thể LẪN dạng in trên trang
  (`_already_has_card`). Đây mới là tầng chặn tổng quát: bước đưa về nguyên thể còn có
  thể đổi từ sang mục từ điển khác hợp lệ ở những cặp khác, chỉ so mỗi lemma là còn
  nguyên cái bẫy.
  ⚠️ Test suýt báo oan `лучше`: kết quả ra `лучше` thay vì `хороший`. Soi ra KHÔNG phải
  hồi quy — `possible_lemmas('лучше')=['хороший','лучше']` nên luật mới không thể bắn;
  đó là luật CŨ (AI trả lời hợp lệ thì giữ AI) và cả hai đều là mục từ điển thật.

## 21/07/2026 (đợt 3)

- **Gõ từ ĐÃ CÓ thẻ → bot trả về nguyên mục TỪ ĐIỂN, không báo "bị trùng" suông nữa.**
  Thẻ cũ đã chứa sẵn nghĩa Anh/Việt, từ loại, giống, 3 ví dụ song ngữ, audio — báo mỗi
  câu "đã tồn tại" là vứt hết đi rồi bắt user tự mở app Anki tra lại. Nay bot đọc ngược
  nội dung note ra đúng bố cục lúc thêm thẻ mới, kèm trạng thái học + deck + có audio hay
  chưa; nút cũ (chuyển deck / xóa+thêm lại / vẫn thêm trùng) giữ nguyên, thêm nút 🔄 Làm
  lại thẻ. Nhiều note trùng thì bấm `Note [1] [2]` xem từng cái.
  Cách làm: thẻ chỉ lưu HTML nên phải viết hàm NGHỊCH của lúc dựng thẻ —
  `html_builder.parse_examples_html/parse_meaning_html/...` (đặt ngay dưới hàm dựng để
  sửa cấu trúc HTML là thấy ngay phải sửa cả hai) + `anki_client.note_to_card_info()`
  dựng lại đúng dict `card_info`, nhờ vậy dùng CHUNG `_card_body_lines()` với thẻ mới,
  hai nơi không thể trình bày lệch nhau. `find_duplicate_notes()` trả kèm fields+tags
  (đã có sẵn trong tay, khỏi gọi notesInfo lần hai).
  ⚠️ Bug regex đã dính và test bắt được: `</?(?!hl\b)[a-zA-Z!/]...` vẫn nuốt `</hl>`
  (regex coi "/" là ký tự đầu tên thẻ) -> câu ví dụ hiện ra "Trời [đẹp quá, đi dạo
  không?". Phải đưa dấu / vào TRONG lookahead: `<(?!/?hl\b)/?[a-zA-Z!]...`.
  Nút 🔄 Làm lại thẻ CỐ Ý chỉ hiện khi có đúng 1 note: `redo_note()` chọn note mới nhất
  theo từ, nhiều note trùng thì nút sẽ sửa nhầm cái đang xem.

- **Quét ảnh: Gemini ĐỌC, pymorphy3 CHỐT dạng từ điển** (user chốt phương án sau khi
  hỏi). Lỗi thật đang gặp: AI trả về `проверяем` (chưa chia về nguyên thể) và `дети`
  (thay vì `ребёнок`) -> OpenRussian không có -> thẻ không thêm được. Đó KHÔNG phải
  việc nên đoán: tiếng Nga có từ điển hình thái đầy đủ, dùng đúng công cụ là hết sai.
  `anki_tools/lemma.py` bọc **pymorphy3** (từ điển OpenCorpora, chạy offline trên VPS,
  không mạng/không hạn mức). ĐÃ ĐO THẬT trước khi chọn, không tin lời quảng cáo: 27/27
  ca khó đều đúng (дети→ребёнок, проверяем→проверять, люди→человек, шёл→идти,
  лучше→хороший, бегущий→бежать...).
  PHÂN VAI là chỗ quan trọng nhất — `reconcile_lemma()` có 3 luật, KHÔNG để từ điển
  đè AI vô tội vạ: (1) từ điển không biết từ đó (gõ sai/tên riêng) -> giữ AI, vì
  pymorphy đoán liều theo đuôi rất bậy (компютер -> "компютереть", nhận ra nhờ cờ
  `is_known`); (2) đáp án AI nằm trong danh sách lemma hợp lệ -> GIỮ AI kể cả khi không
  phải phương án xác suất cao nhất, vì AI có ngữ cảnh câu còn pymorphy nhìn từ trơ trọi
  (стали trong "из стали" là сталь, không phải стать); (3) còn lại mới lật. So sánh
  bỏ qua khác biệt ё/е.
  Prompt quét ảnh viết lại: tách bạch BƯỚC ĐỌC (bắt quét từng dòng, gồm cả tiêu đề, số
  bài tập, chú thích, bảng biểu, chữ bị gạch nối xuống dòng — chỗ AI hay lướt) khỏi BƯỚC
  đưa về nguyên thể; bắt trả về CẶP `{seen, lemma}` chứ không chỉ lemma (model buộc phải
  nghĩ "từ này từ đâu ra", và bot có dạng gốc để đối chiếu + hiện cho user duyệt); nêu
  đích danh nhóm suppletive hay trượt. Lượt quét ảnh được nâng `reasoning_effort`
  minimal->low, `max_tokens` 3000->6000, timeout 60s->180s (đọc kỹ cả trang thì lâu hơn,
  đứt giữa chừng là mất trắng công đọc).
  Danh sách duyệt giờ hiện `проверять ← проверяем 🔧` (🔧 = từ điển đã sửa lại AI), và
  có trần độ dài: trang dày ra hàng trăm từ thì tin nhắn vượt 4096 ký tự và Telegram
  TỪ CHỐI cả tin — user không thấy gì để duyệt.

- **Nhận ảnh gửi dạng FILE (document), không chỉ ảnh nén.** Telegram ép ảnh thường về
  ~1280px; sách chữ nhỏ mất nét là AI đọc sót từ — đây nhiều khả năng là nguyên nhân
  "bỏ lọt vài từ" chứ không chỉ tại prompt. Gửi dạng file thì ảnh nguyên vẹn.
  Chặn sớm ở 8MB kèm lời khuyên rõ ràng (base64 phình thêm ~33%).
  Kéo theo: phải NHẬN DẠNG định dạng ảnh bằng magic bytes (`image_mime_type()`) thay vì
  khai cứng `image/jpeg` — ảnh nén Telegram luôn là JPEG nên trước đây khai bừa cũng
  đúng, còn file thì có thể là PNG (ảnh chụp màn hình) hoặc HEIC (iPhone gửi nguyên
  bản, Gemini KHÔNG đọc được) -> báo thẳng "gửi lại dạng ảnh thường" thay vì để AI trả
  lỗi khó hiểu.

- **Gõ tay từ biến cách: hỏi từ điển TRƯỚC, AI sau.** `дома` -> `_suggest_lemma()` hỏi
  pymorphy3 ngay (tức thì, 0 lượt AI, chắc chắn đúng); chỉ khi từ điển bó tay — tức là
  gõ SAI CHÍNH TẢ, thứ từ điển không xử lý được nhưng AI thì có — mới gọi AI đoán.
  Vẫn phải bấm nút xác nhận như cũ, bot không tự thêm.
  Thiếu pymorphy3 (chưa `pip install`) thì mọi hàm trả None và hệ thống chạy y như
  trước — một thư viện phụ trợ không được phép làm chết bot.

## 21/07/2026 (đợt 2)

- **Backup HỎNG HOÀN TOÀN trên VPS — sửa 2 nhịp.** Chạy thử thật trên VPS (thay vì
  tin là nó giống PC) mới lòi ra: backup không tạo nổi file nào.
  (1) `exportPackage` bảo **ANKI** tự ghi file nên đường dẫn được hiểu theo GÓC NHÌN
  CỦA ANKI. Trên VPS Anki nằm TRONG CONTAINER, không thấy `/root/ankiagent/backups`
  của host -> Permission denied. Trên PC không lộ vì Anki chạy trực tiếp. Sửa:
  `resolve_dirs()` tự nhận biết qua `getMediaDirPath` — media nằm dưới `/data` nghĩa
  là đang trong container, khi đó bảo Anki ghi `/data/backups` còn bot đọc/dọn ở
  `<project>/anki-data/backups` (docker-compose mount anki-data -> /data).
  (2) Đường dẫn đúng rồi vẫn Permission denied: bot chạy bằng **root** (host) tạo thư
  mục 755 root:root, còn Anki trong container chạy bằng **uid 1000** nên không ghi
  nổi. Sửa: `_makedirs_shared()` chmod 777 thư mục backup (đúng cách VPS_SETUP.md đã
  bảo làm với chính anki-data).
  Kết quả: backup chạy được trên VPS, 36MB/bản, đĩa còn 8GB/16GB nên 7 bản (~250MB)
  thoải mái. BÀI HỌC: thứ gì chạy được trên PC chưa chắc chạy trên VPS — Anki ở hai
  nơi có tư cách khác hẳn nhau (chạy trực tiếp vs trong container, root vs uid 1000).

- **Job nền không bao giờ chết nữa + dẹp PTBUserWarning** — soi log sau deploy thì
  lộ ra một điểm yếu CÓ SẴN TỪ TRƯỚC: `_nightly_don` không bọc try/except quanh
  thân vòng lặp. Task asyncio mà ném exception thì CHẾT HẲN VÀ IM LẶNG — nghĩa là
  chỉ cần AnkiConnect lỗi đúng một đêm là job dọn inbox ngừng chạy vĩnh viễn cho
  tới lần restart bot, không có dấu hiệu nào báo ra. Sửa: thêm `_guard()` bọc mọi
  job (nuốt lỗi, log, nghỉ 60s rồi chạy tiếp; riêng CancelledError vẫn cho ném để
  tắt bot bình thường) + `_sleep_until()` dùng chung, bỏ phần tính giờ lặp 2 lần.
  Đã kiểm chứng: job ném lỗi 6 lần liên tiếp vẫn tiếp tục chạy.
  Đồng thời `app.create_task` -> `asyncio.create_task` (`_spawn` trong app.py, có
  giữ tham chiếu vì asyncio chỉ giữ weak ref): PTB cảnh báo mỗi lần khởi động vì
  Application chưa "running" lúc _post_init — 3 job = 3 dòng rác trong log, dễ che
  lỗi thật. KHÔNG dùng JobQueue của PTB vì nó đòi thêm gói apscheduler (đã kiểm:
  `app.job_queue` là None trên VPS) — không đáng cài dependency mới chỉ để dẹp
  cảnh báo.

## 21/07/2026

- **Sao lưu tự động + sync định kỳ trên VPS** — user hỏi "có nên đặt VPS luôn
  sync theo chiều DOWNLOAD về từ AnkiWeb không, phòng khi quên sync điện thoại".
  ĐÃ TỪ CHỐI phương án đó, lý do:
  (1) Nó không cứu được thứ user đang lo. Quên sync điện thoại thì thứ mất là
  TIẾN TRÌNH ÔN nằm trong điện thoại — AnkiWeb cũng chưa có, nên VPS tải về bao
  nhiêu lần cũng không kéo được. Máy đang không sync là điện thoại, không phải VPS.
  (2) Nó tạo rủi ro MỚI: "Download from AnkiWeb" không phải tải thêm mà GHI ĐÈ
  sạch collection VPS — chạy tự động định kỳ là tự đặt bom, mất thẻ bot vừa thêm
  chưa kịp đẩy lên. (AnkiConnect cũng chỉ có mỗi lệnh `sync` hai chiều, không có
  lệnh tải-về-một-chiều; muốn ép phải vào VNC bấm tay.)
  LÀM THAY: (a) `_periodic_sync()` — sync HAI CHIỀU mỗi 30 phút, không ghi đè bên
  nào, giữ VPS <-> AnkiWeb không lệch xa. (b) `anki_tools/backup.py` +
  `_nightly_backup()` 3h30 sáng + lệnh `/backup` + nút 💾: xuất từng deck GỐC ra
  .apkg kèm includeSched (giữ lịch ôn), giữ 7 bản gần nhất (~36MB/bản -> ~250MB),
  tự xóa bản cũ. Backup thành công thì im lặng, THẤT BẠI mới nhắn Telegram.
  ⚠️ exportPackage KHÔNG nhận deck rỗng để xuất cả collection (đã thử: trả False)
  nên phải liệt kê deck gốc xuất từng cái. CỐ Ý đi qua HTTP thay vì copy thẳng
  collection.anki2: bot chạy trên host còn Anki trong container, đường dẫn khác nhau.
  Lý do sâu xa cần backup: cái nguy hiểm nhất với Anki không phải quên sync, mà
  là một lần full sync chọn nhầm chiều — nó ghi đè cả bản AnkiWeb, không lùi được.

## 20/07/2026 (đợt 2)

- **Mảng THẺ NGỮ PHÁP tách riêng: `grammar_forms/` + deck `GRAMMAR::plural-irregular`
  + lối tắt bot `/dacbiet`** — user muốn học danh từ có số nhiều BẤT QUY TẮC, và
  yêu cầu làm sao "ít ảnh hưởng đến deck RUSSIAN đang chạy ngon, tách bạch để sau
  dễ bảo trì" (còn định thêm các loại biến cách khác).
  (A) DANH SÁCH TỪ (`grammar_forms/irregular_plurals.py` -> `data/irregular_plurals.tsv`,
  125 từ): KHÔNG chép từ giáo trình mà SUY RA từ dữ liệu OpenRussian — dự đoán số
  nhiều chuẩn theo quy tắc rồi so với số nhiều thật, lệch = bất quy tắc. Thân từ
  suy từ GENITIVE số ít nên nguyên âm chạy (отец/отцы) không bị coi nhầm. Nguồn:
  dump `Badestrand/russian-dictionary` (27k danh từ, gitignore vì ~8MB), xét 2500
  từ thông dụng nhất, đối chiếu chéo với web OpenRussian để loại dòng dump cũ/sai
  (год→лета, дядя→дядья, воронко), lọc tính từ danh từ hóa (лёгкое, остальное).
  ⚠️ ĐÃ THỬ VÀ PHẢI BỎ cách lọc theo tag level của OpenRussian: паспорт/яблоко/
  сахар/юг bị gắn C1, село/повар C2 — lọc kiểu đó mất 63/133 từ toàn từ lõi.
  Thứ hạng tần suất mới đáng tin; cột level vẫn ghi ra TSV để tham khảo.
  (B) KIẾN TRÚC TÁCH BẠCH: package `grammar_forms/` (config/scraper/ai/cards/
  pipeline/templates/setup/backfill) phụ thuộc MỘT CHIỀU vào anki_tools (chỉ mượn
  utils, audio.fetch_audio_bytes, store_media_file, hạ tầng gọi AI). KHÔNG sửa
  một dòng nào trong scraper.py/pipeline.py/ai_client.py/html_builder.py — xóa cả
  thư mục grammar_forms đi thì deck từ vựng vẫn chạy nguyên vẹn.
  (C) THẺ: model `RU_Plural` thêm 3 ô `ExamplesHTML`/`KindLabel`/`RawExamples`
  (modelFieldAdd — thẻ cũ chỉ nhận ô rỗng, không mất tiến trình học). Mặt trước:
  số ít + nghĩa EN/VI + audio, gõ đáp án `type:PluralClean`, CỐ Ý không có ví dụ
  (ví dụ chứa sẵn dạng số nhiều = lộ đáp án). Mặt sau: số nhiều (xanh lá) + audio
  + nhãn KIỂU bất quy tắc + 3 ví dụ. Prompt riêng ép AI dùng ĐÚNG nominative số
  nhiều, có HẬU KIỂM regex bắt làm lại (AI hay trả "много друзей" = genitive).
  (D) Deck cũ `Irregular` -> `GRAMMAR::plural-irregular`: AnkiConnect không có
  lệnh đổi tên nên createDeck + changeDeck (không đụng lịch ôn) + deleteDecks vỏ
  rỗng. 26 thẻ cũ được vá đủ ví dụ + PluralAudio (trước đó RỖNG cả 26) qua
  `python -m grammar_forms.backfill fix`, giữ nguyên note_id. Gắn tag
  `grammar::plural-irregular` cho toàn bộ.
  (E) BOT: `/dacbiet` + nút ⭐ trong /menu -> flow_special.py (thêm 1 từ / thêm
  loạt từ danh sách / vá thẻ cũ, có duyệt trước + nút ⏹ Dừng). Chỗ sửa ở tgbot cũ
  gói gọn 1-2 dòng mỗi file (dispatch, app, core).
  ⚠️ Thêm field = ĐỔI SCHEMA -> AnkiWeb đòi FULL SYNC một lần (sync thường báo
  "Sync status 2"). Phải mở Anki desktop bấm Sync rồi chọn **Upload to AnkiWeb**.
  (F) SỬA NGAY SAU KHI USER MỞ THỬ THẺ: (1) nghĩa tiếng Anh hiện "N/A" ở MỌI thẻ
  — `grammar_forms/scraper.py` đọc nhầm khóa `translations[].tl`, đúng phải là
  `tls` (một LIST nghĩa). (2) `.hl` trong ví dụ đang tô xanh lá, user muốn giữ
  nguyên thiết kế của thẻ từ vựng -> trả về xanh dương #58a6ff như card.css.
  `backfill._needs_fix()` nhận thêm dấu hiệu "Meaning chứa N/A" để vá lại được
  27 thẻ đã lỡ tạo bằng bản lỗi.
  (G) TRÙNG TỪ GIỮA HAI MẢNG (user báo): `find_duplicate_notes()` dò theo
  `WordClean:"..."` KHÔNG lọc model — mà RU_Plural cũng có ô WordClean, nên thêm
  từ vựng `дом` sẽ bị báo "đã có thẻ" nhầm với thẻ ngữ pháp. Sửa: query thêm
  `note:"{MODEL_NAME}"`. Một từ có CẢ hai loại thẻ là chuyện bình thường, không
  phải trùng. (Các hàm khác — get_known_words, get_topic_stats, get_deck_note_ids
  — vốn đã lọc model nên không dính.)
  (H) LÀM LẠI THẺ NGỮ PHÁP: `grammar_forms.pipeline.redo_word()` + nút 🔄 trong
  /dacbiet (logic giống /sua: dựng lại từ đầu, ghi đè cùng note_id nên tiến trình
  học giữ nguyên). CỐ Ý tách khỏi /sua thay vì gộp: một từ có thể có cả hai loại
  thẻ, gộp chung thì không biết user muốn sửa thẻ nào.

- **Menu bot gọn lại còn 2 tầng** — user thấy "nhiều chức năng nên nhìn hơi rối",
  và cho biết dùng nhiều nhất vẫn là gõ từ vào inbox + AI gắn nhãn, phần còn lại
  chỉ đụng lúc fix lỗi. Nguyên tắc áp dụng: việc dùng hằng ngày KHÔNG cần nút nào
  cả, nên mặt tiền phải nhường đường cho nó thay vì trưng thêm nút.
  Tầng 1 (/menu) còn 3 nút: 📚 Đổi deck │ ⭐ Ngữ pháp │ 🛠 Sửa chữa & công cụ.
  Tầng 2 (sau 🛠): 🔄 Làm lại 1 thẻ │ 📚 Cả deck │ 📊 Thống kê │ 🧹 Dọn inbox │
  ☁️ Sync │ ❓ Hướng dẫn │ ◀️ Quay lại. Danh sách lệnh "/" rút từ 9 xuống 4
  (/menu /dacbiet /deck /help) — các lệnh kia vẫn chạy khi gõ tay, chỉ không
  chiếm chỗ bảng gợi ý. HELP_TEXT chia đôi: "DÙNG HẰNG NGÀY" / "KHI CẦN SỬA".
  Tách `commands.thongke_report()` khỏi `cmd_thongke` để nút 📊 và lệnh /thongke
  dùng chung một logic.

- **Đã thêm đủ 124 thẻ số nhiều bất quy tắc.** Chạy `backfill add` cho 98 từ còn
  lại: 97 ✅, 1 ❌ (`сахар`). Hóa ra `сахар` là danh từ KHÔNG ĐẾM ĐƯỢC — web
  OpenRussian không có dạng số nhiều, chỉ dump cũ mới ghi bừa `сахара'`. Bổ sung
  luật vào `irregular_plurals.enrich_levels()`: web cào được mà ô plural RỖNG thì
  loại khỏi danh sách (meta rỗng hẳn = cào lỗi mạng thì vẫn giữ). Danh sách còn
  124 từ, khớp đúng số thẻ. Toàn deck đã kiểm: 0 thẻ thiếu ví dụ / thiếu audio /
  nghĩa N/A / thiếu nhãn kiểu.

## 20/07/2026

- **Audio dự phòng Google Cloud TTS + /sua = "làm lại thẻ" (bỏ preset 1/2/3)** —
  hai việc user chốt.
  (A) ÂM THANH: OpenRussian thỉnh thoảng trả 500 -> AnkiConnect (tải hộ qua URL)
  KHÔNG bắt được lỗi, còn GHI NGUYÊN câu "…download failed with return code 500"
  vào ô Audio (3 thẻ dính: дачка, варенный, коммуникативный). Sửa: bot TỰ tải
  bytes (anki_tools/audio.py: OpenRussian trước, hụt thì Google Cloud TTS giọng
  ru-RU-Standard-A) rồi storeMediaFile + set field Audio '[sound:...]'. push_to_anki
  bỏ mảng audio-url, tách build_card_fields() dùng chung. ⚠️ Key TTS phải là API
  key Google Cloud (bật Cloud Text-to-Speech API) — key Gemini AI Studio KHÔNG
  gọi được; biến GOOGLE_TTS_API_KEY trong .env, trống thì bỏ qua phao. Free 4tr
  ký tự/tháng. fix_audio.py (mới): vá thẻ đang thiếu tiếng (nhận diện = ô Audio
  thiếu tag [sound:], gồm cả thẻ mang text lỗi cũ); dry-run mặc định / --apply.
  (B) /sua: bỏ hẳn refine preset 1/2/3 + tự-viết (gần như không dùng). Giờ /sua =
  LÀM LẠI thẻ: cào lại OpenRussian + AI sinh lại nghĩa/ví dụ GIỐNG thẻ mới, ghi
  đè cùng note_id nên TIẾN TRÌNH HỌC giữ nguyên; làm mới cả tag chủ đề; vá audio
  nếu thẻ đang thiếu. /suadeck cũng thành "làm lại cả deck" (giữ nút Dừng/resume).
  pipeline: refine_note* -> redo_note*; anki_client thêm store_media_file/
  store_word_audio/build_card_fields/get_note_full/update_note_fields/set_topic_tag;
  xóa code refine chết (call_claude_refine, REFINE_PRESETS, update_note_refined).

## 19/07/2026 (đợt 6)

- **Fix kẹt "Đang tải ảnh về": nới trần chờ HTTP Telegram + retry tải ảnh** —
  user gửi ảnh bị kẹt 3 phút. Log VPS: telegram.error.TimedOut ngay ở
  reply_text đầu tiên của on_photo (handler chết trước khi quét). Nguyên nhân:
  VPS (VN) -> api.telegram.org ~230ms RTT, trần chờ mặc định của PTB chỉ 5s,
  mạng chững một nhịp là gãy. Sửa: (a) app.py nới toàn cục connect 15s / read
  30s / write 30s / media_write 60s / pool 15s; (b) on_photo bọc TimedOut cho
  tin trạng thái đầu (thử lại 1 lần) + vòng tải ảnh retry 1 lần (nghỉ 3s).
  Bài học: bot chạy VPS xa server Telegram thì MỌI handler gửi tin đều có thể
  dính TimedOut — trần 5s mặc định quá mỏng.

- **Tách bot.py (~1.400 dòng) thành gói tgbot/ theo luồng** — user hỏi file dài
  có sao không: chạy thì không sao, nhưng khó bảo trì (6 luồng chen 1 file).
  bot.py giờ CHỈ là điểm vào ~10 dòng (systemd `python bot.py` giữ nguyên,
  không phải sửa service). Gói tgbot/: core (phiên/deck/menu/idle/format),
  commands (/start /menu /deck /thongke /don /sync + job 3h sáng), flow_add
  (thêm từ + dò trùng + đoán lemma), flow_edit (/sua + /suadeck), flow_scan
  (📷 quét ảnh), dispatch (on_word + on_callback — chỉ chia việc, không nghiệp
  vụ), app (lắp handler + khởi động). Import một chiều core <- flows <-
  dispatch <- app, không vòng. Đường dẫn last_deck.json / suadeck_resume.json
  vẫn ở gốc repo (_PROJECT_ROOT trong core.py). Kiểm bằng AST: 48/49 hàm giống
  HỆT bản cũ; hàm duy nhất khác là _idle_reset_job (chủ đích: reset phiên giờ
  dọn thêm scan_words/scan_msg của luồng quét ảnh). Các file khác đều <500
  dòng, chưa cần tách.

- **📷 Quét ảnh trang sách qua bot: OCR từ tiếng Nga -> duyệt -> thêm loạt vào inbox**
  — user chụp trang sách gửi bot, muốn gom từ mới hàng loạt thay vì gõ tay từng
  từ. NGUYÊN TẮC user chốt: bot CHỈ xử lý thô, thêm hay không LUÔN phải qua nút
  ✅ xác nhận, không tự ý. Luồng: (a) ai_client.call_claude_scan_words(): 1 request
  Gemini duy nhất/trang (ảnh base64 qua endpoint OpenAI-compatible sẵn có,
  max_tokens=3000) — OCR + đưa mọi từ về lemma, loại tên riêng, validate chỉ
  nhận Cyrillic; _send_ai_request/_call_model_once thêm tham số max_tokens.
  (b) anki_client.get_known_words(): set WordClean toàn kho để lọc từ đã có
  (None = lỗi ≠ set rỗng, tránh đề nghị thêm trùng cả kho). (c) bot.py: handler
  ảnh on_photo (filters.PHOTO) -> danh sách từ MỚI đánh số + nút "✅ Thêm cả N
  từ"/"🚫 Hủy", nhắn 'bỏ 3 7 12' để loại từ trước khi thêm; _run_scan_add chạy
  nền như /suadeck (nghỉ 3s/từ chống RPM, nút ⏹ Dừng, dò trùng lại từng từ
  trước khi thêm, sync 1 lần cuối đợt); thẻ vào RUSSIAN::0-inbox theo chế độ
  tự động. Test thật với ảnh chữ Nga tự tạo: OCR + lemma + loại tên riêng OK
  (lưu ý: lemma thi thoảng lệch kiểu цветы->цвет thay vì цветок — user duyệt
  tay là lưới an toàn).

- **Deck hứng RUSSIAN::0-inbox: học từ mới một chỗ, tốt nghiệp tự về deck chủ đề**
  — user tồn ~200 từ chưa học + 40-50 từ mới/ngày cần ưu tiên, muốn học gom một
  chỗ rồi thẻ thuộc rồi mới về deck chủ đề để ôn. Thiết kế: tag topic:: (AI gắn
  từ đầu) là "địa chỉ nhà", deck chỉ là chỗ ở tạm. (a) config.py thêm INBOX_DECK;
  chế độ tự động của push_to_anki đưa thẻ mới vào inbox thay vì deck chủ đề.
  (b) anki_client.move_graduated_from_inbox(): thẻ inbox đạt is:review (tốt
  nghiệp learning) -> changeDeck về RUSSIAN::<slug tag>, lịch ôn giữ nguyên.
  (c) bot: lệnh /don chạy tay + job nền 3h sáng (asyncio, không cần PTB
  job-queue), đêm có chuyển thẻ mới nhắn Telegram. (d) build_subdecks.py chừa
  thẻ inbox ra (không bốc thẻ chưa học đi). (e) setup_inbox.py (idempotent):
  ép preset Default luật user chốt "ôn HẾT thẻ cũ (hạn cũ nhất trước) rồi mới
  hiện thẻ mới" (newMix=1, reviewOrder=0 — vốn đã đúng sẵn), preset riêng
  'inbox' (newGatherPriority=2: từ THÊM GẦN NHẤT học trước để ưu tiên từ trong
  ngày, 50 từ mới/ngày), gom 187 thẻ is:new rải rác về inbox. Đã chạy + sync.

## 19/07/2026 (đợt 2)

- **Dọn note type: xóa 4 model chết + đổi tên ngắn gọn** — user thấy còn dấu
  vết nhiều lần sửa: 4 model Russian_Irregular_Plural_OLED v1→v4 (0 note) và
  2 tên dài lê thê. AnkiConnect KHÔNG có lệnh xóa/đổi tên model, nên làm bằng
  thư viện `pip anki==26.5` (khớp đúng bản desktop, tránh lệch schema): đóng
  Anki (guiExitAnki bị ngó lơ -> CloseMainWindow), backup collection.anki2
  (collection-backup-truoc-don-model-19-07.anki2 trong Anki2/User 1), xóa 4
  model chết, đổi `Russian_Premium_OLED_Type_v25`->**RU_Word** (610 note),
  `Russian_Irregular_Plural_OLED_v5`->**RU_Plural** (26 note). Gỡ luôn tag
  `Irregular_Plural_v5` (26 thẻ — lọc bằng note:"RU_Plural" là đủ). Sửa
  MODEL_NAME trong config.py. ⚠️ Xóa model = đổi schema -> Anki đòi FULL SYNC:
  PC chọn **Upload**, VPS (vnc.bat) chọn **Download**; bot dừng trong lúc
  migrate để không tự tạo lại model.

## 19/07/2026

- **Dọn 15 tag mồ côi sau tái cấu trúc** — sau đợt đổi cây 2 tầng, 15 tag tên
  cũ (topic::food, topic::other, topic::colors...) vẫn nằm trong danh sách tag
  của Anki dù không còn note nào dùng. Chạy clearUnusedTags (chỉ xóa tag 0 note,
  không đụng thẻ) + sync. Còn lại đúng 19 tag topic:: mới + Irregular_Plural_v5
  (+ 3 mục tổ tiên topic/concepts/language Anki tự giữ làm nút cây). Cùng phiên:
  xác nhận "colors 0 thẻ" là hiểu nhầm — số cạnh deck là thẻ ĐẾN HẠN hôm nay,
  không phải tổng; deck colors vẫn đủ 12 thẻ, kiểm bằng Browse
  `deck:RUSSIAN::qualities::colors`.

## 18/07/2026 (đợt 3)

- **Chuyển cây phẳng 19 chủ đề -> CÂY 2 TẦNG, 10 GỐC CỐ ĐỊNH** — user chỉ ra
  lỗi thiết kế: tách kiểu đợt 2 (thêm chủ đề vào tầng gốc) làm gốc phình vô hạn.
  Chốt: tầng gốc = 10 miền BẤT BIẾN (people, life, nature, places, language,
  time, numbers, actions, qualities, concepts), mỗi tầng ≤10 mục, từ nay chỉ
  thêm NHÁNH CON (vd actions::motion). Slug lồng cấp bằng :: (tag topic::life::food
  = MỘT tag, Anki hiện lồng dưới topic::life; lọc theo tag cha vẫn bắt được con).
  Kỹ thuật: topics.py thêm FALLBACK_TOPIC (concepts::misc) + LEGACY_ALIASES
  (bảng dịch slug cũ->mới, dùng cho mọi lần đổi tên sau); tag_topics --fix giờ
  dịch được cả tag của từ AI phân loại (không có trong bảng tra) qua alias;
  build_subdecks + get_topic_stats viết lại đọc tag TỪNG note phía Python
  (query tag:"cha" của Anki khớp cả tag con -> đếm đúp/chuyển sai khi lồng cấp),
  build_subdecks tự xóa cả deck RUSSIAN::* mồ côi sau đổi cấu trúc. Đã chạy:
  397 thẻ đổi tag, 609 thẻ về đúng 19 deck lá dưới 10 gốc, 15 deck phẳng cũ đã
  xóa, misc 5%, không deck nào ≥100. /thongke đọc FALLBACK_TOPIC thay 'other'.

## 18/07/2026 (đợt 2)

- **Tách 'other' thành function-words + abstract (17 -> 19 chủ đề)** — /thongke
  báo other 16% (>15%) ngay lần đầu, user hỏi cách sửa. Tách TẦNG GỐC (không
  lồng dưới other vì other là "vườn ươm": cụm nào đủ lớn thì bứng ra):
  `function-words` (35 thẻ: đại từ, trợ từ, liên từ, câu hỏi, можно/нельзя) +
  `abstract` (27 thẻ: правда, счастье, работа...). other còn 36 thẻ (5%) — hết
  cảnh báo. Kỹ thuật: tag_topics.py thêm chế độ `--fix` (đổi tag thẻ ĐÃ có tag
  cho khớp bảng tra; CHỈ đụng từ có trong bảng, từ AI phân loại giữ nguyên —
  dùng lại được cho mọi lần tách chủ đề sau) -> build_subdecks.py --apply tạo
  2 deck con mới + dọn thẻ + sync. AI prompt tự nhận 19 chủ đề qua
  topics_prompt_block(), không phải sửa prompt.

## 18/07/2026

- **Lệnh /thongke + quy tắc phát hiện khi nào cần tách deck** — user hỏi 17 chủ
  đề có bao trọn tiếng Nga lâu dài không (hiện A1, lo lên A2/B1). Kết luận đã
  bàn: 17 chủ đề bao trọn về NGỮ NGHĨA (other hứng phần dư) nhưng sẽ phình khi
  lên cấp; quy tắc đèn báo = deck con ≥100 thẻ HOẶC other >15% kho thì tách.
  Tách = thêm slug LỒNG CẤP dạng `actions::motion-verbs` vào topics.py (tag và
  deck Anki đều phân cấp bằng :: nên cây tự rẽ nhánh, không sửa code) + retag
  cụm từ cũ + chạy build_subdecks.py --apply. /thongke: đếm thẻ theo chủ đề
  (get_topic_stats trong anki_client.py), hiện bảng xếp hạng + cảnh báo 3 loại
  (deck chạm 100 / other quá 15% / thẻ chưa có tag). Ghi chú hiện trạng: other
  đang 16% (98/609) — ứng viên tách đầu tiên là function-words (đại từ, trợ từ).

## 16/07/2026 (đợt 2)

- **Cây deck kho RUSSIAN::<topic> + chế độ thêm từ TỰ ĐỘNG** — user muốn deck
  tổng làm kho, học theo deck con chủ đề, tiến độ cộng dồn lên kho (KHÔNG dùng
  Filtered Deck vì học xong thẻ biến mất). Tên kho tiếng Anh "RUSSIAN" theo yêu
  cầu user (dễ gõ hơn Cyrillic), đổi được qua env TOPIC_DECK_PARENT (config.py).
  (1) `build_subdecks.py`: tạo RUSSIAN + 17 deck con, chuyển 609 thẻ về đúng
  deck con theo tag topic:: (changeDeck không ảnh hưởng lịch ôn — đã kiểm tra
  interval giữ nguyên), xóa 10 deck cũ đã trống, GIỮ deck Irregular (26 thẻ
  không thuộc model bot), sync. Dry-run mặc định, --apply làm thật, chạy lại
  vô hại. Lưu ý: 610 note -> 609 vì 1 note hỏng (không có card, deck "?") đã
  biến mất trước đó.
  (2) Chế độ TỰ ĐỘNG: deck_name=None xuyên suốt pipeline -> push_to_anki tự
  đặt thẻ vào RUSSIAN::<topic AI chọn> (không có topic -> ::other), createDeck
  idempotent trước khi add. Bot: không bắt chọn deck nữa (None = tự động, là
  mặc định + sau idle reset); bảng chọn deck thêm nút "🤖 Tự động theo chủ đề";
  chặn "📦 Chuyển deck" trong luồng từ trùng khi đang tự động (không có deck
  hiện tại). CLI main.py: Enter bỏ trống tên deck = tự động.
  Giới hạn bài/ngày KHÔNG cần chỉnh 9999 như các hướng dẫn cũ: Anki >= 23.10
  dùng v3 scheduler, bấm thẳng deck con thì giới hạn của deck mẹ được BỎ QUA.

## 16/07/2026

- **Nút "🕘 Deck gần nhất" trong bảng chọn deck của bot** — đỡ phải bấm
  Deck có sẵn → chọn lại sau mỗi lần phiên reset (nghỉ >3 phút). Deck vừa chọn
  (mọi ngả: nút danh sách, /deck <tên>, gõ tên deck mới) đều đi qua hàm chung
  `_set_deck()` → ghi `last_deck.json` (gitignore) nên nhớ được cả khi bot
  restart trên VPS. Bấm nút: kiểm tra deck còn tồn tại (KHÔNG dùng
  ensure_deck_exists để khỏi tự tạo lại deck user đã xóa; deck chết → quên file
  + mời chọn lại). Callback cố định `deck:last` vì tên deck Cyrillic có thể
  vượt 64 byte callback_data.
- **Bỏ tag kỹ thuật OpenRussian_*_v25** — user chê rác. Không code nào tra thẻ
  theo 2 tag này (nhận diện thẻ của bot luôn qua model name
  `Russian_Premium_OLED_Type_v25`), nên: gỡ khỏi 610 thẻ (removeTags: 229 thẻ
  AI_OLED + 381 thẻ Pure) + clearUnusedTags; `push_to_anki` không gắn nữa —
  thẻ mới giờ CHỈ có tag `topic::...`.
- **Tag chủ đề cho toàn bộ từ vựng (topic::...)** — 17 chủ đề (people-family,
  professions, body, food, home-objects, clothing, animals, nature-plants,
  weather, time, numbers, colors, places-city, education, actions, qualities
  [CHỈ tính từ+trạng từ], other [không nhét được vào đâu]), user chốt qua thảo
  luận. Danh sách chủ đề định nghĩa MỘT nơi: `anki_tools/topics.py`.
  (1) 610 thẻ có sẵn: gắn bằng `tag_topics.py` (bảng tra thủ công, addTags —
  không đụng nội dung/tiến độ học; idempotent: thẻ đã có topic:: thì bỏ qua;
  dry-run mặc định, `--apply` mới gắn thật). Đã chạy, đủ 610/610.
  (2) Từ mới: AI chọn topic trong CÙNG request sinh ví dụ (thêm trường "topic"
  vào JSON schema + few-shot của `_CORE_SYSTEM_PROMPT`; validate ép về "other"
  nếu sai/thiếu — KHÔNG làm hỏng kết quả; nhánh fallback không AI → không gắn
  tag, gắn bù bằng `python tag_topics.py --missing` [AI phân loại từng thẻ lẻ,
  hàm `call_claude_topic`]). Chuỗi truyền: build_examples_html trả thêm
  topic_slug → push_to_anki gắn tags + đưa vào card_info["topic"] → CLI và bot
  Telegram hiện dòng "📂 topic::...". Quy tắc phân loại: mỗi từ đúng 1 tag,
  theo nghĩa phổ biến nhất (mùa→time, động từ ăn uống→food, tính từ thời
  tiết→weather, màu→colors).

## 15/07/2026

- **Đổi phông viết tay sang Propisi Regular** (theo yêu cầu user sau khi dùng thử
  Marck Script) — Propisi (ParaGraph 1997) là font làm ĐÚNG theo mẫu chữ vở tập
  viết trường Nga, chuẩn hơn Marck Script. `_propisi.ttf` (41KB, đủ bảng chữ
  Cyrillic hoa+thường, đã kiểm bằng fontTools) nạp vào collection.media;
  `.cursive-word` dùng "Propisi" với "MarckScript" làm dự phòng, cỡ 34px.
  Nguồn font: wfonts.com/font/propisi (free).
- **Phông chữ viết tay Nga trên thẻ (Marck Script)** — dòng chữ nghiêng ở mặt sau
  thẻ vốn để luyện đọc chữ viết tay Nga nhưng phông hệ thống nghiêng không ra dạng
  viết tay. Đổi sang Marck Script (giống chữ vở tập viết пропись: т→m, д→g), user
  chọn qua trang preview 3 phông (Marck/Bad Script/Caveat). Font nhúng vào Anki:
  file `_marckscript.ttf` trong collection.media (storeMediaFile) → tự sync mọi
  thiết bị, offline OK. Dòng viết tay đổi từ {{Word}} → {{WordClean}} (bỏ dấu
  trọng âm — Marck Script không có ký tự dấu ghép ◌́ nên bị vỡ phông), cỡ chữ
  18→32px, bỏ font-style italic.
- **Vá lỗi RPM cho /suadeck + tính năng Sửa tiếp** — đợt sửa deck Матрёшка (309 thẻ)
  bị 44 lỗi vì model lite trả lời nhanh → vòng lặp bắn >15 lượt/phút (trần RPM
  free là 15); code cũ coi mọi 429 là hết quota ngày nên nhảy sang model dự phòng
  (quota bé) rồi chết. Fix: (1) 429 KHÔNG có chữ "PerDay" = giới hạn mỗi phút →
  chờ đúng retryDelay Google gợi ý (tối đa 2 lần) rồi thử lại CHÍNH model đó;
  (2) batch nghỉ 3s giữa 2 thẻ (~10 lượt/phút < 15); (3) batch dừng/lỗi → lưu
  danh sách thẻ còn dở vào `suadeck_resume.json` (gitignore) → /suadeck lần sau
  hỏi "▶️ Sửa tiếp N thẻ". Đợt Матрёшка được cứu bằng script quét mod-time trên
  VPS: xác nhận đúng 200 thẻ đã sửa, 109 thẻ dở đã vào danh sách Sửa tiếp.
- **/suadeck — sửa TOÀN BỘ thẻ trong 1 deck** (tính năng ít dùng nên là lệnh riêng
  trong danh sách "/", KHÔNG chiếm chỗ menu chính). Luồng toàn nút: chọn deck →
  kiểu sửa (1/2/3/tự viết) → màn xác nhận (số thẻ, ước tính thời gian, cảnh báo
  nếu >450 thẻ vì quota Gemini 500/ngày) → chạy nền. Tiến độ = ĐÚNG 1 tin nhắn
  tự cập nhật tại chỗ (thẻ i/N, vừa xong từ nào ✅/❌, đếm xong/lỗi) + nút ⏹ Dừng.
  Xong/dừng: sync AnkiWeb 1 lần, tổng kết liệt kê ≤10 từ lỗi (thẻ lỗi giữ nguyên
  nhờ OUTPUT CONTRACT + validate). Kỹ thuật: `get_deck_note_ids()` (anki_client),
  tách lõi `refine_note_id()` từ `refine_note()` (pipeline), batch chạy
  `asyncio.create_task` vì PTB xử lý update tuần tự (không thì nút Dừng chết),
  guard `sd_running` chống chạy 2 đợt, idle timer được đẩy mỗi thẻ.
- **Giao diện "bấm trước, gõ sau" (đỡ đổi bàn phím Nga↔Latin)** — user dùng bàn phím
  tiếng Nga liên tục nên gõ lệnh kiểu `/sua <từ>` rất bất tiện. Đổi logic:
  `/sua` (hoặc nút ✏️ Sửa thẻ) → bot hỏi "gõ từ cần sửa" → gõ từ → nút chọn kiểu sửa;
  nút "Tự viết yêu cầu" → bot hỏi → gõ thẳng yêu cầu (không cần gõ lại lệnh/từ).
  **Xóa lệnh `c` đổi deck** — đổi deck chỉ qua `/deck` hoặc nút 📚.
  Kỹ thuật: trạng thái chờ `user_data["awaiting"]` = `sua_word` / `sua_custom`,
  idle reset có dọn. Đường tắt `/deck <tên>`, `/sua <từ> [yêu cầu]` vẫn chạy ngầm.
- **vnc.bat** — double-click là xem màn hình Anki trên VPS: tự mở đường hầm SSH
  (cổng 15900, không hỏi pass nhờ SSH key) rồi bật TightVNC Viewer
  (`C:\Program Files\TightVNC\tvnviewer.exe`). Đóng cửa sổ SSH thu nhỏ = ngắt VNC.
- **Quyết định: KHÔNG cập nhật Anki trên VPS** dù có thông báo bản mới — hệ đang
  chạy ổn, addon AnkiConnect từng phải vá tay, bản trong Docker image chỉ đổi khi
  chủ động `docker compose pull`. Chỉ cập nhật khi AnkiWeb từ chối sync vì
  "client quá cũ" (lúc đó làm cùng Claude để có đường lùi).

- **Reset 3 phút gọn hơn + menu liền** — tin nhắn reset giờ chỉ báo "đã reset phiên"
  (nói rõ chỉ quên deck đang chọn, thẻ trong Anki không mất gì) và kèm luôn menu nút bấm
  y hệt `/menu` trong cùng 1 tin, để lần vào tới bấm chọn ngay.
- **Từ không có trên OpenRussian → AI đoán từ nguyên mẫu** — gõ từ biến cách
  (vd `дома`) hoặc sai chính tả (vd `хорошшо`): bot nhờ Gemini đoán dạng từ điển
  (lemma) + giải thích ngắn tiếng Việt, hiện nút `✅ Thêm '<từ>'` (kèm 0–2 phương án
  phụ nếu mơ hồ) và `🚫 Hủy`. Bấm xác nhận thì mới cào OpenRussian bằng từ đó —
  AI chỉ đoán, KHÔNG tự quyết. Kỹ thuật: `pipeline.process_word` trả cờ
  `not_found`; `ai_client.call_claude_lemma()`; nút dùng chỉ số
  (`lemma:i`, danh sách trong `user_data["lemma_choices"]`) để né giới hạn
  64 byte callback_data.
- **Thêm CHANGELOG.md này** — quy trình mới: mỗi lần sửa code phải cập nhật
  CHANGELOG + memory của Claude, để không phải kể lại ngữ cảnh ở phiên chat mới.

## 14/07/2026 — ngày chuyển toàn bộ hệ thống lên VPS

- `6e5040a` — Cập nhật docs: deploy.bat, /deck mở bảng chọn, nút Tự sửa/Bỏ qua.
- `9000213` — **deploy.bat**: double-click là deploy, khỏi mở PowerShell.
  Kèm theo (ngoài git): tạo SSH key trên PC + chép lên VPS → deploy không hỏi mật khẩu.
- `19aad56` — Thẻ AI bị khuyết (thiếu ví dụ): 2 nút bấm liền **🔧 Tự sửa** (chạy
  preset 2 đổi ví dụ) / **⏭ Bỏ qua**; `/deck` không tham số mở bảng chọn deck.
- `c718d70` — **Chọn deck bằng nút bấm**: [📂 Deck có sẵn (liệt kê hết, tối đa 24)]
  [➕ Tạo deck mới (gõ tên)]; gõ `c` mở cùng bảng này, deck cũ giữ đến khi chọn xong.
- `603e283` — Báo rõ thẻ khuyết khi AI thất bại (cờ `ai_degraded` + cảnh báo),
  thêm dòng 🇬🇧 vào tin nhắn tổng kết, AI freestyle retry 2 lần.
- `7e04cc7` — **CHÍNH SÁCH SYNC** (sau sự cố mất deck 00 do chọn Upload trên iPhone):
  sync AnkiWeb NGAY sau MỌI hành động sửa đổi + báo rõ khi sync thất bại.
  Quy tắc trên iPhone: LUÔN chọn "Download from AnkiWeb".
- `f94ed83` — Nâng cấp lớn bot: `/sua` có OUTPUT CONTRACT cứng (không thể trả thiếu
  ví dụ) + validate + retry; preset 1 Ngắn hơn / 2 Đổi ví dụ / 3 Dài hơn; bỏ deck
  mặc định (hỏi deck đầu phiên như CLI); idle reset 3 phút; /menu; viết lại README.
- `fdea689` — Thêm trùng dùng `options.allowDuplicate` chính thống (mánh ký tự vô
  hình ZWSP bị Anki ≥25.x tự xóa nên hỏng).
- `83a1271` — Hết quota không chết: chuỗi model dự phòng khi 429
  (chính: `gemini-3.1-flash-lite` 500 lượt/ngày); ping API bằng GET /models không đốt quota.
- `e403a94` — Sửa báo động giả "AI chưa phản hồi" (parse lỗi Google bọc trong list).
- `88613d7` — setup_vps.sh tự cài addon AnkiConnect vào volume (addon gốc là symlink
  bị volume che mất) + set webBindAddress.
- `aea5733` — Vá lỗi quyền thư mục anki-data (chmod 777) + hướng dẫn VNC qua tunnel cổng 15900.
- `ff38068` — Gỡ nút AI Refine + toàn bộ JS khỏi thẻ Anki → thẻ tĩnh, key không còn
  nhúng vào thẻ, prompt chỉ còn 1 nơi (`ai_client.py`). Sửa thẻ = `/sua` qua bot.
- `066f291` — Commit đầu: chuyển hệ thống lên VPS — bot Telegram + pipeline dùng
  chung CLI/bot + secrets tách ra `.env` + docker-compose (headless-anki) +
  setup_vps.sh + systemd + deploy.ps1 + VPS_SETUP.md.

## Hạ tầng cố định (để khỏi tìm lại)

- VPS: FPT `161.248.146.56` (1 vCPU/2GB/16GB + swap 2GB), code tại `/root/ankiagent`,
  bot chạy bằng systemd `anki-bot`, Anki headless trong Docker container tên `anki`
  (image `thisisnttheway/headless-anki`), AnkiConnect `127.0.0.1:8765`, VNC `127.0.0.1:5900`
  (cả 2 KHÔNG mở ra internet).
- GitHub: `sakuralegend/ankiagent` (private, VPS đọc qua deploy key).
- Deploy: double-click `deploy.bat` (hoặc `.\deploy.ps1`) — push → VPS pull → restart bot.
- Secrets: chỉ trong `.env` (PC + VPS, không có trong git). Đổi `.env` thì phải
  `scp .env root@161.248.146.56:/root/ankiagent/.env` + restart bot.
