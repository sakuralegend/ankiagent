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

## 2. Nội dung — ba phần, đúng thứ tự

| Phần | Lớp CSS | Nội dung |
|---|---|---|
| **Chẻ từ** | `hd-sec` + `hd-row`(`hd-piece`/`hd-gloss`) | Từng mảnh **kèm nghĩa của mảnh**. Mảnh không mang nghĩa riêng (tiền tố thể) thì **nói thẳng là không**, đừng bịa. Từ gốc trơn thì bỏ hẳn phần chẻ, thay bằng một câu `hd-why` nói rõ "không chẻ được". |
| **Cách nhớ** | `hd-why` | Logic nối các mảnh ra nghĩa. **Bắc cầu sang tiếng Anh khi thật sự cùng gốc** (`совреме́нный` ↔ *contemporary* = *con-* + *tempus*). Chỉ ra **phụ tố mở khoá cả lớp từ** — đây là phần giá trị nhất. |
| **Họ hàng** | `hd-sec` + `hd-fam` | Từ cùng gốc / cùng phụ tố, **luôn kèm nghĩa tiếng Việt**. |

Bẫy dễ nhầm thì chèn `hd-warn` **ngay dưới phần liên quan**, không dồn xuống cuối.

**ĐƯỢC PHÉP DÀI.** User chốt: *"đừng rút gọn khó hiểu"*. Ô này thu gọn mặc định nên độ dài
không làm phiền ai.

⚠️ **Nhưng dài có trần: nhắm 6–10 KB HTML mỗi thẻ, tối đa ~12 KB.**
Đo thật: lô k01 trung bình 7,7 KB — vừa. Lô k04 lên 13,4 KB (đỉnh 16,9) vì **chồng ba khối
hệ thống lên cùng một thẻ**. Đây không phải chuyện thẩm mỹ: mục đích user nói rõ là *"thứ ĐẦU
TIÊN tôi đọc để hiểu một từ mới"* — dài quá thì user **không đọc**, và thế là hỏng đúng mục
đích mà độ dài định phục vụ. Quy tắc: **tối đa 2 khối dùng chung mỗi thẻ**, và khối thứ hai
phải thật sự liên quan tới từ đó chứ không gắn cho đủ bộ. Kiểm nhanh:

```bash
PYTHONIOENCODING=utf-8 python data/huongdan/kho/congcu.py dodai kNN
```

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

## 3. Chia lô theo HỌ TỪ, không chia đều

32/168 từ nằm cùng một hệ thống quốc tịch. Soạn cùng nhau thì lời giải thích **nhất quán và
không tự mâu thuẫn giữa các lô**. Khối hệ thống dùng chung (biến `HE`, `LUAT`, `THE`…) **lặp
ở mọi thẻ trong họ là CỐ Ý** — user chỉ nhìn một thẻ mỗi lần, gặp lại 32 lần chính là spaced
repetition cho bản thân cái hệ thống.

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

HE = (  # khối hệ thống dùng chung cho cả lô — xem §3, LẶP Ở MỌI THẺ LÀ CỐ Ý
    '<div class="hd-sec">…</div>'
    '<div class="hd-why">…</div>'
)

S = {}

S["дом"] = (
    '<div class="hd-sec">Chẻ từ</div>'
    '<div class="hd-row"><span class="hd-piece">дом-</span>'
    '<span class="hd-gloss">NHÀ</span></div>'
    '<div class="hd-sec">Cách nhớ</div>'
    '<div class="hd-why">…</div>'
    '<div class="hd-sec">Họ hàng</div>'
    '<div class="hd-fam"><b>дома́шний</b> thuộc về nhà · …</div>'
    + HE
)
```

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
