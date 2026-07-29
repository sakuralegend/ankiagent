# Ô "Hướng dẫn" — công thức soạn nội dung

> Đọc file này TRƯỚC khi soạn thêm lô mới. Nó giữ đủ để một phiên chat mới soạn ra
> nội dung **cùng chất lượng** với 168 thẻ đã làm, không phải dò lại từ đầu.

## 1. Mục đích — thứ quyết định mọi lựa chọn khác

User (đang tự học tiếng Nga từ số 0, có tiếng Anh B2/IELTS 6.5) nói rõ:

> *"Phần hướng dẫn này là thứ ĐẦU TIÊN tôi đọc để hiểu một từ mới, tránh học vẹt đi vào
> vết xe đổ lần trước. Học để thật sự hiểu, thật sự nhớ."*

Và:

> *"Tôi mới học nên chưa thể biết nên nhét nội dung gì vào… tôi không đủ kiến thức để kiểm tra
> được độ tin cậy. Rất cần bạn đóng vai một người thầy, chỉ cho tôi những gì tinh tuý nhất của
> từ đó, mà nó cần thiết cho việc học lâu dài về sau."*

⇒ **Không được đẩy việc thẩm định sang user.** Phần nào máy soát được thì bắt buộc để máy soát
(xem §5). Phần nào không soát được thì **nói rõ mức tin ngay trên thẻ**.

## 2. Nội dung — ba mục, đúng thứ tự, và NGẮN

### 🧭 Nguyên tắc gốc — đọc câu này trước, mọi con số bên dưới chỉ là cách thi hành nó

> *"Tôi muốn **mỗi từ chỉ tiết lộ một ít kiến thức liên quan TRỰC TIẾP đến nó** thôi, đừng bê
> cả họ kiến thức như sách giáo khoa vào."*

**Phép thử một câu:** *câu này có giúp nhớ ĐÚNG TỪ NÀY không, hay chỉ là kiến thức đúng nói
chung?* Loại thứ hai bỏ đi. **Đúng không phải lý do để cho vào thẻ.**

### Ba mục cốt lõi — đây là thứ user gọi là quan trọng nhất

| Mục | Lớp CSS | Nội dung |
|---|---|---|
| **Chẻ từ** | `hd-sec` + `hd-row`(`hd-piece`/`hd-gloss`) | Từng mảnh **kèm nghĩa của mảnh**. Mảnh không mang nghĩa riêng (tiền tố thể) thì **nói thẳng là không**, đừng bịa. Từ gốc trơn thì bỏ hẳn phần chẻ, thay bằng một câu `hd-why` nói rõ "không chẻ được". |
| **Cách nhớ** | `hd-why` | **Chủ yếu suy thẳng ra TỪ các mảnh vừa chẻ.** Bắc cầu sang tiếng Anh khi thật sự cùng gốc (`совреме́нный` ↔ *contemporary*). |
| **Họ hàng** | `hd-sec` + `hd-fam` | Từ cùng gốc / cùng phụ tố, **luôn kèm nghĩa tiếng Việt**. |

🆕 **`congcu.py tiep` in sẵn hai khối từ điển (29/07)** — đọc trước khi tự nghĩ:

| Khối in ra | Dùng vào đâu |
|---|---|
| `BAT THUONG` — chỗ bảng chia lệch quy tắc | viết **một câu chú ý** phía trên bảng: đọc câu đó là hiểu cả bảng |
| `CUM CO DINH` / `CACH DUNG` | ứng viên ô đỏ (`к сожале́нию` của bản mẫu chính từ đây ra) |

🔴 **Đừng chép nguyên văn** — đây là văn từ điển thô (tiếng Anh, có mục là ghi chú
nội bộ kiểu *"This page needs fixing"*). Máy chỉ trỏ chỗ, câu chú ý là bạn viết.

🔴 **Mục "Họ hàng" KHÔNG có dữ liệu máy, và đó là chủ ý** (user chốt 29/07): danh
sách họ từ của OpenRussian trộn từ **cùng gốc** với từ **đồng nghĩa khác gốc**
(`ги́бкий` → `мя́гкий`, `бога́тый`), nên đưa ra là mời gọi đúng loại lỗi cần tránh.
Bạn tự nghĩ như trước — nhưng **chỉ viết khi chắc**; hai lỗi đã bắt được là
`о́блако`↔`во́лос` và `целова́ть`↔`цель` (nhìn giống gốc mà không cùng gốc). Không
chắc thì bỏ mục đó, đừng đoán.

### 🔴 Ba con số cứng

1. **VỪA ĐÚNG MỘT MÀN HÌNH iPHONE — trần 700px, nhắm dưới 600px.** User chốt:
   *"toàn bộ nội dung đó chỉ được hiện trên 1 mặt màn hình iPhone thôi"* (máy thật:
   **iPhone 16 Pro Max, 440×956**). Quá 700px là phải cuộn = vỡ yêu cầu.
2. **TỐI ĐA 2 ô đỏ (`hd-warn`) mỗi thẻ** — chọn hai cái hay nhất, bỏ hết phần còn lại.
3. **MẶC ĐỊNH KHÔNG CÓ KHỐI HỆ THỐNG** (§3). Cần lắm thì trải đầy đủ ở **đúng một thẻ** của lô,
   thẻ khác dẫn chiếu một dòng.

```bash
PYTHONIOENCODING=utf-8 python data/huongdan/kho/congcu.py dodai kNN   # cao px + ô đỏ + %khối chung
```

⚠️ **Đừng canh theo BYTE — byte là đại lượng sai.** Một bảng 6 dòng và một đoạn văn cùng số byte
chiếm chiều cao khác nhau tới ba lần. `dodai` ước lượng **chiều cao dựng hình** từ đúng
font-size/line-height/padding trong `card.css`. Đối chiếu thật:

| | `сожаление` (user khen) | `гиря` (k15, ngắn nhất lô) | `реплика` (k04) |
|---|---|---|---|
| Byte | 1 173 | 2 827 | 16 874 |
| **Chiều cao** | **516px = 0,7 màn** | 1 112px = **1,6 màn** | 6 305px = **9 màn** |

Cỡ chữ tham khảo: một thẻ vừa màn hình thường rơi vào **1,2–1,6 KB HTML** — nhưng đó là *hệ quả*,
không phải mục tiêu. Mục tiêu là con số px.

### Cắt cái gì để xuống được cỡ đó

- ✂️ **Biến cách / số nhiều theo ĐÚNG QUY TẮC thì BỎ HẲN.** Chỉ liệt kê khi **bất thường** —
  nguyên âm chạy (`лёд → льда`), số nhiều bất quy tắc, giống lệch với đuôi.
  *"Đặc biệt thì liệt kê đủ, còn theo quy tắc thì thôi."*
- ✂️ Bỏ sắc thái phụ, ví dụ câu thứ hai trở đi, mẹo phát âm không mở khoá lớp từ nào.

⚠️ **Ngắn KHÔNG phải là cụt** — user vẫn giữ *"đừng rút gọn khó hiểu"*.

### 📐 Bản mẫu: `сожаление` — 1 173 byte, và user chấm là "vừa súc tích vừa đủ ý"

**Chép cái TỈ LỆ này, đừng chép độ dài suông:**

- **Chẻ từ**: 3 mảnh, mỗi mảnh một dòng ngắn (`со-` cùng · `-жал-` thương xót · `-ение` → danh từ)
- **Cách nhớ**: một câu nghĩa đen nối các mảnh + **một dẫn chiếu sang từ đã học** (`совреме́нный`)
- **2 ô đỏ đắt giá**: từ cùng gốc user dùng hằng ngày (`пожа́луйста`) · cụm phải thuộc (`к сожале́нию`)
- **Họ hàng**: đúng một dòng, 5 từ

Bẫy dễ nhầm thì chèn `hd-warn` **ngay dưới phần liên quan**, không dồn xuống cuối.

<details><summary>Vì sao chuẩn đổi (28/07) — đọc nếu định nới lại cho dài</summary>

Trước đây mục này ghi *"ĐƯỢC PHÉP DÀI, nhắm 6–10 KB"*. User học hết số thẻ đã soạn rồi kết luận
ngược: *"tham quá khiến thẻ dài tôi đọc xong không nhớ gì"*. Công cụ khi đó **chỉ đo byte, không
đếm ô đỏ và không đếm khối lặp**, nên tôi tưởng đã đạt trong khi trượt rất xa:

| | `сожаление` | k12 (lô gọn nhất) | k04 |
|---|---|---|---|
| Byte | **1 173** | 3 583 | 13 403 |
| Ô đỏ / thẻ | **2** | 4,3 | 10,5 |
| % là khối lặp | **0%** | 0% | **80%** |

⇒ **Trần byte một mình không đủ.** `dodai` nay đo cả ba.
</details>

### Cái "tinh tuý" nên ưu tiên, theo thứ tự giá trị đường dài

1. **Luật SUY RA ĐƯỢC vs chỗ BUỘC PHẢI THUỘC** — tách bạch hai loại này tiết kiệm công nhất.
2. **Phụ tố mở khoá cả lớp từ** (`-тельный`, `-ость`, `-ение`, `-альный`, `-ик/-ика`).
3. **Phép biến âm lặp khắp nơi** (`г/к/х → ж/ч/ш`, `з→ж`, `ц+ск→цк`, `ст→щ`).
4. **Trọng âm dịch khi thêm hậu tố** (`не́мец → неме́цкий`), và **nguyên âm chạy** (`лёд → льда`).
5. **Cặp dễ lẫn về CÁCH DÙNG** (`ру́сский язы́к` tính từ vs `говори́ть по-ру́сски` trạng từ;
   `слы́шать` vs `слу́шать`; `ви́деть` vs `смотре́ть`).
6. **Cách mà động từ/giới từ đòi** — học động từ là phải học luôn cái cách nó kéo theo.
7. **Sắc thái dùng thật** (`приве́т` chỉ với người ngang hàng; `норма́льно` là câu trả lời tích cực).

### KHÔNG làm

- ❌ Mnemonic / chuyện bắc cầu âm thanh — **user đã bỏ hẳn hướng này**, đánh giá thất bại.
- ❌ Phiên âm — user học shadowing nhanh hơn.
- ❌ Bịa cấu trúc cho từ gốc trơn hoặc từ mượn.
- ❌ Khẳng định chắc nịch một từ nguyên còn tranh cãi. Dùng `hd-warn` mở đầu bằng
  `⚠️ Mức tin:` rồi nói rõ đó là từ nguyên, không phải luật suy ra được.

## 2c. Việc thứ hai của mỗi lô: SỬA FIELD `Vietnamese`

User chốt 28/07: *"phần dịch tiếng Việt đôi khi chưa được thoát ý, ví dụ phải chỉ ra đó là thể
hoàn thành hay chưa hoàn thành thì tôi mới viết đúng được"*.

🔴 **Dòng tiếng Việt là ĐỀ BÀI của deck `1-go`** — user nhìn nó rồi **gõ** từ Nga. Mơ hồ ở đây
không phải lỗi thẩm mỹ mà là **đề bài không có đáp án đúng**: `nói` không phân biệt được
`сказа́ть` (hoàn thành) với `говори́ть` (chưa hoàn thành), nên user gõ kiểu gì cũng có thể sai.

**Tiêu chí:** *"tạo nghĩa tiếng Việt sát nhất, sao cho **chỉ có 1 đáp án đúng** thôi"* — user
không biết trước sẽ học từ nào, nên không thể trông vào việc họ đoán ý.

🧠 **Dùng chính đầu óc của bạn, đừng chờ công cụ.** User nói rõ: *"nó phải tự biết từ này dễ
nhầm với từ nào chứ"*. Không có bước bắt buộc nào phải chạy — bạn biết `сказа́ть` đụng
`говори́ть`, `бли́зкий` đụng `бли́зко`, thì xử lý luôn.

**Cách làm:** trong file lô, khai thêm dict `V` bên cạnh `S`, **chỉ những từ cần làm rõ**:

```python
V = {
    "сказать":  "nói, bảo (HOÀN THÀNH — một lần, xong việc)",
    "говорить": "nói, trò chuyện (chưa hoàn thành — đang/thường xuyên)",
}
```

🔴 **ĐỪNG GHI TỪ LOẠI — mặt đề bài đã có badge rồi** (user chốt 28/07: *"cái từ loại không cần
ghi đâu, vì thẻ của tôi đã có field đó rồi"*). Front của card gõ in sẵn `{{PoS}}` và
`{{GenderBadge}}`, nên viết thêm "(TÍNH TỪ)" · "(DANH TỪ)" · "— ĐỘNG TỪ" · "(giống cái)" là
**lặp lại thứ user đang nhìn thấy**, chỉ tổ làm đề bài dài ra.

| Badge in sẵn | Không cần ghi lại |
|---|---|
| `n` `v` `adj` `adv` `pron` + `M`/`Fe`/`Nt` | từ loại, giống |

⚠️ **Ngoại lệ `oth`**: từ nào có `PoS = oth` thì badge chỉ hiện "oth" — vô dụng. Với chúng
(`по-ру́сски`, `за`, `про`, `то́лько`…) **vẫn phải ghi** "trạng từ" / "giới từ, đi với cách 4".
Kiểm bằng `notesInfo` chứ đừng đoán.

⚠️ **THỂ động từ thì KHÔNG có field nào chứa** — badge chỉ nói `v`. Nên *hoàn thành / chưa hoàn
thành* **vẫn phải ghi**, đây mới là thứ user cần. Tương tự: dạng phản thân `-ся`, so sánh hơn,
từ chỉ dùng số nhiều — đều không nằm trong field nào.

⇒ Hệ quả cho **hai lớp dưới**: cặp *tính từ vs trạng từ* (`бли́зкий`/`бли́зко`) và cặp *động từ ↔
danh từ cùng gốc* (`за́втракать`/`за́втрак`) **badge đã tự tách rồi** — chỉ cần lo phần nghĩa.

Các lớp hay đụng nhất — gặp là xử lý, khỏi cân nhắc:
1. **Cặp thể động từ** — luôn ghi *hoàn thành* / *chưa hoàn thành*. **Đây là lớp quan trọng nhất**
   vì không badge nào đỡ.
2. **Đồng nghĩa gần** (`ви́деть`/`смотре́ть` đều "nhìn") — thêm nét phân biệt.
3. **Cùng từ loại, nghĩa Việt trùng** (`бу́дничный` "bình thường" đụng `обы́чный`) — badge không
   cứu được, phải tách bằng nghĩa.
4. **Cặp có tiền tố ↔ không tiền tố** và **phản thân ↔ không** (`учи́ть`/`учи́ться`) — cùng `v`,
   badge không tách được.

⚠️ `nap` in từng dòng `cũ -> mới` để soát bằng mắt trước khi ghi — đổi đề bài của thẻ user đang
học thì phải thấy được, không làm lặng lẽ.

<sub>Có `congcu.py vacham` soi toàn bộ 908 thẻ tìm nghĩa Việt trùng nhau (đo 28/07: **186 nghĩa
trùng, dính 414 lượt từ** — `ổn` ứng với 5 từ Nga). **Tuỳ chọn, không phải cửa bắt buộc** —
dùng khi luồng chính muốn kiểm lại, đừng bắt agent chạy.</sub>

## 3. Chia lô theo HỌ TỪ, không chia đều

32/168 từ nằm cùng một hệ thống quốc tịch. Soạn cùng nhau thì lời giải thích **nhất quán và
không tự mâu thuẫn giữa các lô**.

### 🔴 Khối hệ thống dùng chung: MẶC ĐỊNH LÀ KHÔNG CÓ

1. **Lô 0% khối chung (k09, k10, k12, k49) là CHUẨN, không phải ngoại lệ.** Khối dùng chung phải
   tự chứng minh mình đáng có; nó không phải mục cần điền cho đủ bộ.
2. **Cần lắm thì trải đầy đủ ở ĐÚNG MỘT thẻ của lô** — thẻ mà hệ thống đó là trọng tâm thật
   (bảng biến cách đại từ đặt ở `он`, không rải khắp 14 thẻ).
3. **Thẻ còn lại: một dòng dẫn chiếu, hoặc không nói gì.**
   `<div class="hd-why">Bảng biến cách đầy đủ nằm ở thẻ <b>он</b>.</div>`
4. **Cấm bảng/danh sách trọn lớp từ trên thẻ không thuộc trọng tâm của lớp đó.** Kiến thức chung
   phải **hoà vào "Cách nhớ" bằng một câu nói về CHÍNH TỪ NÀY**:
   ✅ *"đuôi `-ение` cho biết đây là danh từ giống trung"* — ❌ cả bảng ba giống.
5. **Không bao giờ đánh số "Hệ thống 1 / 2 / 3"** trên một thẻ. Viết tới số 2 là đã sai.

`congcu.py dodai` in cột **`khoi dung chung: N% do dai the`** — kêu khi vượt 15%.

<details><summary>Vì sao đổi (28/07) — đọc nếu định khôi phục cách cũ</summary>

Mục này trước đây khẳng định *"khối hệ thống lặp ở mọi thẻ trong họ là CỐ Ý — user chỉ nhìn một
thẻ mỗi lần, gặp lại 32 lần chính là spaced repetition cho bản thân cái hệ thống"*. Lập luận
nghe hợp lý, **user cũng đã đồng ý lúc đó**, nhưng sai khi dùng thật:

| Lô | k04 | k08 | k07 | k05 | k01 | k16 | k02 | k09·k10·k12·k49 |
|---|---|---|---|---|---|---|---|---|
| % độ dài thẻ là khối lặp | **80%** | 73% | 68% | 62% | 60% | 56% | 52% | **0%** |

Ở k04, **4/5 thẻ là khối lặp**, phần nói về chính từ đó chỉ còn 1/5. Cái "spaced repetition cho
hệ thống" đẩy chính cái từ ra rìa và làm mọi thẻ trong lô **trông giống hệt nhau** nên mắt lướt
qua. User: *"tôi thấy nó chiếm quá nhiều diện tích rồi… đừng bê cả họ kiến thức như sách giáo
khoa vào"*.
</details>

## 4. Quy trình chạy một lô — không được bỏ bước nào

```bash
# 1. Viết data/huongdan/loNN_<ten>_<ngay>.py  (chép khuôn từ một lô cũ)
# 2. CHẠY KHAN trước — bắt key sai mà chưa ghi gì vào thẻ
python data/huongdan/loNN_....py
# 3. Ghi thật
python data/huongdan/loNN_....py --apply
# 4. SOÁT — bắt buộc, và phải ĐỌC danh sách "phai doc bang mat"
python data/huongdan/kiemtra.py
# 5. Sửa lỗi -> chạy lại --apply -> soát lại tới khi "khong co"
# 6. git commit + push
```

### Bẫy đã dính, đừng dính lại

- 🔴 **Key phải khớp `WordClean` chính xác, kể cả chữ `ё`** — `весёлый` không phải `веселый`.
  Chạy khan bắt được ngay.
- 🔴 **Bash tool là Git Bash, KHÔNG phải PowerShell.** Đừng dùng here-string `@'…'@` cho
  commit message — nó tạo commit tên `@`. Dùng heredoc `git commit -F - <<'EOF'`.
- 🔴 **Xuống dòng giữa chuỗi Python** trong file lô = SyntaxError. Chạy khan bắt được.
- 🔴 `cardsInfo.answer` **kèm cả khối `<style>`** — đếm chuỗi trong đó sẽ ra số lớn hơn thật.
  Muốn đếm phần thân thì `answer.split('</style>')[-1]`.

## 5. Bộ soát `kiemtra.py` — vì user không tự kiểm được

Đối chiếu **mọi từ Nga in đậm trong toàn field** với `data/nouns.csv`
(26.856 danh từ **có trọng âm chuẩn**): từ đó có thật không, trọng âm đúng chỗ chưa.

**Nó đã bắt 11 lỗi thật qua 12 lô**, trong đó có lỗi mà đọc bằng mắt không ra:

| Loại | Ví dụ |
|---|---|
| Trọng âm sai | `коре́янка`→`корея́нка` · `славя́нин`→`славяни́н` · `выходны́е` · `морози́льник` |
| Từ **không tồn tại** | `ра́дый` (đúng: `рад`) |
| Sai dạng từ | `мо́лодый` (đúng: `молодо́й`) |
| **Lời giải thích SAI** | tôi viết "trọng âm dịch giữa `-ик`/`-ика`" — thực ra nó đứng yên ở cả 4 cặp |
| **Lời giải thích SAI** | `ви́на` không phải cách 2 của `вино́` mà là số nhiều |

⚠️ **Giới hạn phải nói rõ, đừng đọc nhầm cái im lặng thành xác nhận:**
`nouns.csv` **chỉ có DANH TỪ**. Động từ, tính từ, trạng từ đều rơi vào danh sách
"phai doc bang mat" — đó là **chưa kiểm được**, KHÔNG phải "đúng". Lô động từ (lô 7) là lô
bộ soát đỡ được ít nhất.

🔴 **Danh sách "phai doc bang mat" KHÔNG phải rác — phải đọc.** Chính nó lộ ra `ра́дый` và
`мо́лодый`. Thấy tính từ/động từ trông lạ thì kiểm tay.

`MIEN_TRU` trong `kiemtra.py` là danh sách miễn trừ **từ đồng tự** (máy không phân biệt được),
mỗi mục phải ghi lý do — một bộ soát kêu nhầm mãi thì rồi chính mình sẽ bỏ qua cả tiếng kêu thật.

## 6. Trạng thái (27/07/2026)

| | |
|---|---|
| **Hai deck học (`0-quen` + `1-go`)** | **168/168 XONG** — lô 1→12 |
| Deck kho `RUSSIAN::<topic>` | **599 thẻ chưa có gì** |
| Thẻ còn nội dung mnemonic cũ | 103 (nằm trong deck kho) |
| Tổng `RU_Word` | 870 |

### Hệ thống đã dạy — lô sau đừng lặp lại, hãy DẪN CHIẾU

| Lô | Hệ thống |
|---|---|
| 1–2 | Bộ bốn quốc tịch `-ец/-ка/-ский/по-…-ски`; tính từ vs trạng từ |
| 3 | Luật dấu cứng `ъ`; gốc `езд` (đi xe), `ём/ня/ним` (lấy) |
| 4 | Danh từ → tính từ bằng `-н-`; biến âm `г/к/х → ж/ч/ш` |
| 5 | `-альный` (kho từ quốc tế), `-тельный`, `-ость`; tiền tố `со-`, `ино-` |
| 6 | `ЧА ЩА` viết А / `ЧУ ЩУ` viết У / `ЖИ ШИ` viết И; nguồn gốc chữ `щ` |
| 7 | **Cặp thể** (вид); **hai lớp chia**; biến âm ngôi "tôi"; `-овать → -ую` |
| 8 | So sánh hơn; **dạng ngắn**; **tính từ hoá danh từ** |
| 9 | **Luật giống** theo chữ cuối; từ mượn quốc tế; hậu tố nhỏ `-ка/-ик` |
| 10 | `-ение/-ание` (→ giống trung); `-ик` người vs `-ика` ngành; gốc `род`, `чёт` |
| 11 | Giống cái đuôi `-ь` (biến cách 3); **nguyên âm chạy**; 5 từ họ hàng Ấn–Âu |
| 12 | Tính từ → trạng từ bằng `-о`; **cách 5 làm trạng từ thời gian**; giới từ 2 cách |

### Lô kế tiếp nên làm gì

703 thẻ deck kho — xem §7, đã có dây chuyền riêng. Vẫn **gom theo họ**, không chia đều.
Nếu gặp từ đã dùng làm "họ hàng" ở lô cũ, giữ **cùng một cách giải thích** — nhất quán quan
trọng hơn mới lạ.

---

# §7. Dây chuyền soạn KHO (703 từ) — đọc kỹ nếu bạn được giao một lô `kNN`

## Vì sao dây chuyền này tồn tại

703 từ không soạn hết trong một phiên. Và quan trọng hơn: **soạn nhiều lô liên tiếp trong
cùng một context làm chất lượng nhạt dần** — người soạn bắt đầu chép khuôn lô trước thay vì
nghĩ lại cho từ mới, mà nhạt dần thì chính người soạn khó tự thấy. User đã chỉ đúng chỗ này
và chọn cách chữa: **mỗi lô chạy trong một context trắng tinh.**

⇒ Nếu bạn đang đọc dòng này với tư cách người soạn một lô: bạn **không biết gì** về các lô
khác, và **đó là cố ý**. Mọi thứ bạn cần nằm trong file. Đừng đoán, đừng phỏng theo trí nhớ.

## Ngân sách — đọc trước khi mở lô

Đo thật phiên 27/07/2026 (8 lô, 99 từ): **chi phí tính theo LÔ, không theo từ.**

| Cỡ lô | Token/lô | **Token/từ** |
|---|---|---|
| 15 từ | 116–165K | 7,8–11,0K |
| 6 từ | 125K | 20,9K |
| 4 từ | 107K | **26,7K** — đắt gấp 3,4 lần |

Phần cố định (đọc spec, xem mẫu, tra từ điển, chạy soát) áp đảo. ⇒ **Không bao giờ chạy lô
dưới 10 từ**; hàng đợi lệch thì chạy `chialai.py` chia lại cho đều (13–18 từ/lô).

🔴 **Mỗi phiên 4 lô (~76 từ) ở chuẩn §2.** Đo thật 28/07: chi phí ≈ **53K cố định mỗi lô +
1,6K mỗi từ**. Phần cố định chiếm ~62% một lô ⇒ **lô to rẻ hơn rõ rệt trên mỗi từ, đừng cắt
nhỏ lô**. (Ở chuẩn cũ dài gấp 4–5 lần thì chỉ chạy được 2 lô ≈ 40 từ. Và 8 lô một phiên đã
từng đốt trọn cửa sổ 5h + $25 credit — trần thật, đã trả giá để biết.)

🔴 **ĐỪNG đọc `MAU.py` hay `k01_actions.py` để xem mẫu.** Cả hai soạn theo **chuẩn cũ dài gấp
4–5 lần** (nhiều ô đỏ, khối hệ thống lặp) — chép theo là hỏng đúng thứ vừa sửa. Bản mẫu đúng là
**`сожаление` ở §2**, đã trích sẵn đủ tỉ lệ; không cần mở file nào khác.

## Quy trình một lô — đúng 5 bước

```bash
# 1. LẤY ĐỀ BÀI (thay k07 bằng id lô của bạn)
python data/huongdan/kho/congcu.py tiep k07
#    -> in ra 15 dòng: WordClean, dạng có trọng âm, từ loại, nghĩa Anh + Việt
#    -> dòng nào có [DE GHI DE noi dung mnemonic cu] là thẻ còn rác cũ, cứ ghi đè

# 2. SOẠN — tạo data/huongdan/kho/k07_<topic>.py
#    File CHỈ CHỨA `S = {...}`. KHÔNG import, KHÔNG main(), KHÔNG gọi Anki.
#    Việc đẩy vào Anki là của lệnh `nap`, chạy một lần duy nhất ở cuối, khi user cho phép.

# 3. TỰ SOÁT
python data/huongdan/kho/congcu.py soat k07

# 4. SỬA cho tới khi CẢ BA mục đầu đều báo "(khong co)":
#      · CAU TRUC HTML                        (thẻ mở/đóng lệch, thiếu .hd-sec/.hd-fam)
#      · TU NGA IN DAM MA THIEU DAU TRONG AM  (xem vạch đỏ bên dưới)
#      · TRONG AM LECH so voi tu dien
#    rồi ĐỌC BẰNG MẮT danh sách "PHAI DOC BANG MAT" (§5 — chính nó bắt được từ bịa)

# 5. DỪNG. Không đánh dấu xong, không commit, không đụng hangdoi.json.
#    Luồng chính sẽ soát lại rồi mới ghi nhận. Lô tự chấm điểm mình thì bộ soát vô nghĩa.
```

## Khuôn file (chép nguyên, đổi phần nội dung)

```python
# -*- coding: utf-8 -*-
"""k07 — <topic>: <một câu nói hệ thống trục của lô này>."""

# 🔴 KHÔNG dựng biến khối dùng chung (HE/LUAT/THE…) rồi cộng vào mọi thẻ.
# Đó là cách cũ, đã bỏ 28/07 — xem §3. Nó nuốt tới 80% độ dài thẻ ở k04.

S = {}

S["дом"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дом-</span>'
    '<span class="hd-gloss">NHÀ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">…</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дома́шний</b> thuộc về nhà · …</div>'
)
```

**Cả thẻ nhắm 1,2–2,2 KB, tối đa 2 ô `hd-warn`.** Xem bản mẫu `сожаление` ở §2.

**Khoá `S[...]` phải khớp `WordClean` CHÍNH XÁC** — kể cả `ё` (`весёлый` ≠ `веселый`).
Cứ chép nguyên chuỗi mà lệnh `tiep` in ra.

## Vạch đỏ — vi phạm là hỏng cả thẻ

- **Từ Nga in `<b>` thì BẮT BUỘC có dấu trọng âm** (`дома́шний`, không phải `домашний`).
  Bộ soát chỉ đối chiếu được từ nào bạn đánh dấu; bỏ dấu = né bộ soát, không phải "an toàn".
- **Không bịa cấu trúc** cho từ gốc trơn hay từ mượn. Không chẻ được thì nói thẳng là không.
- **Không chắc thì hạ mức tin**, đừng khẳng định: `<div class="hd-warn">⚠️ Mức tin: đây là từ
  nguyên, không phải luật suy ra được…</div>`. User **không tự kiểm được** (§1) — nói quá là
  hại thật, không phải chuyện văn phong.
- **Không mnemonic, không phiên âm.** User đã bỏ hẳn hai hướng này.
- Từ loại quyết định trọng tâm: **danh từ** → giống + số nhiều bất thường; **động từ** →
  cặp thể + lớp chia + cách nó đòi; **tính từ** → dạng ngắn + trạng từ `-о` tương ứng;
  **số từ** → cách mà nó bắt danh từ theo sau (2–4 khác 5+, đây là chỗ khó nhất của số từ).

## Trạng thái

`python data/huongdan/kho/congcu.py trangthai` — còn bao nhiêu lô, bao nhiêu từ.
Toàn bộ tiến độ nằm ở `kho/hangdoi.json`; `kho/tudien.json` là ảnh chụp 703 từ (đông lạnh,
đừng sửa). Thẻ trong Anki **không bị đụng** cho tới khi user bảo chạy `nap --apply`.
