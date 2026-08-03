# 📘 SỔ TAY CÁCH LÀM VIỆC — v2

> **Phạm vi:** từ nay về sau, thêm chức năng / sửa lỗi thì làm thế nào để không đẻ mớ bòng bong.
> Luật có số hiệu `L1`–`L5` để viện dẫn. User duyệt 30/07/2026 (`QD-01`).
>
> 🔴 **v2 (03/08/2026, QD-24) cắt hết phần đã thành sự thật.** Bản v1 viết khi repo **chưa có**
> `CLAUDE.md`, chưa có cửa soát, chưa có test — nên quá nửa nó là *kế hoạch*, không phải *luật*.
> Nay có 17 cửa máy (S1–S17) + `deploy.ps1` ba bậc + bộ test, những đoạn đó đã hết việc.
> Số nào không có ngày đo thì đã bị xoá theo luật của QD-23; số trần hiện hành ở `soat_nguong.json`.

---

## Q1 — Vì sao luật viết ra vẫn không tự thi hành

Bằng chứng gốc, đo 30/07/2026: chỗ nào có **luật-nằm-trong-file + máy canh** (nội dung thẻ, `CHUAN.md`)
thì 18 lô không sự cố; chỗ nào luật chỉ nằm trong đầu thì **10 wrapper AnkiConnect**, 4 hàm chuẩn hoá,
3 nơi dựng HTML. Cùng một người, hai kết quả ngược nhau ⇒ biến số không phải con người.

Người-thi-hành ở đây **không phải bạn — là AI**, và mỗi phiên là một *nhân viên mới ngày đầu*. 10 bản
wrapper không phải một người lười 10 lần; đó là 10 nhân viên mới, ai cũng chọn thứ an toàn cho phiên
của mình: chép thì chắc chạy, import thì phải đi đọc code người khác.

**Suy ra loại lời khuyên duy nhất có tác dụng ở đây:** nó phải kết tinh thành **(a) một dòng trong
file AI tự đọc**, hoặc **(b) một lệnh máy chạy được**. Mọi thứ khác là trang trí.

## Q2 — Luật (L1–L5) khác NGƯỠNG ở chỗ nào

Năm luật nằm nguyên văn trong `CLAUDE.md` — **cố ý không chép lại đây**, hai bản sao thì sớm muộn lệch.

**Vì sao không có luật thứ 6** (kiểu "file không quá X dòng"): thứ đó là **ngưỡng**, không phải luật.
Luật là thứ **vi phạm một lần đã có hại**; ngưỡng là thứ vượt qua thì **ghi nợ**. Trộn hai loại làm
luật loãng rồi người ta bỏ cả gói.

## Q3 — Thêm một chức năng

Quy trình đã thành ba playbook máy tự kích hoạt: `/ycau` → `/kehoach` → `/nghiemthu` (QD-09).
Đừng làm lại bằng tay. Hai thứ dưới đây các playbook **không** chứa:

### 3a. File cũ hay file mới?

| Tình huống | Làm gì |
|---|---|
| Sửa/mở rộng hành vi của hàm đã có | File cũ, hàm cũ |
| Chức năng mới nhưng **cùng vòng đời** với file cũ (chết cùng nhau, deploy cùng nhau, cùng một người gọi) | File cũ, hàm mới |
| File định thêm đã **quá trần ghi nợ** (`soat_nguong.json`), hoặc phải thêm import thuộc tầng khác (file đang thuần đọc-dữ-liệu bỗng phải gọi mạng) | File mới trong cùng gói |
| Script chạy tay một lần | `_va_<việc>.py` → `_daxong/` khi xong (L2) |

Quy tắc gói: chỉ bot dùng → `tgbot/` · chỉ dây chuyền kho → `data/huongdan/` · chỉ thẻ ngữ pháp →
`grammar_forms/` · **từ HAI mảng trở lên thật sự cần** → `anki_tools/`. Và chỉ khi người thứ hai
đã cần thật, đừng "để sẵn cho tương lai". Chiều import một chiều, `anki_tools` không import ngược.

### 3b. Phép thử chép-dán

Repo có cả trùng lặp tai hại (10 wrapper) lẫn trùng lặp **cố ý đúng** (kho/ giữ wrapper riêng để
thay đổi ở bot không giết lô đang chạy tối nay). Phân biệt bằng đúng một câu hỏi:

> **"Ngày mai bản GỐC sửa mà bản CHÉP không sửa theo — đó là LỖI hay là Ý ĐỒ?"**

- **LỖI** (hai bản phải luôn giống nhau, lệch là hỏng im lặng — như hai hàm chuẩn hoá `ё` ra kết quả
  khác nhau) ⇒ **cấm chép, bắt buộc import**.
- **Ý ĐỒ** (bản chép là ảnh chụp **cố tình đóng băng** để cách ly rủi ro) ⇒ được chép, trả hai đồng
  thuế: dòng đầu file ghi `# ẢNH CHỤP từ <gốc> ngày <d>, lý do, hết hạn khi <sự kiện>`, và một mục
  `QD-nn`. Ảnh chụp **không ghi hạn** chính là 12 file lô thế hệ 1 — thứ đã xoá dữ liệu thật.

## Q4 — Ngưỡng cảnh báo sớm

Vượt ngưỡng **không có nghĩa sửa ngay** — giữa việc khác mà tiện tay refactor là cách đẻ bug kinh
điển. Mặc định: ghi một dòng vào `SONO.md`. **Trả xong thì xoá dòng đó đi** (S16 canh, QD-24).

Trần dòng file · trần đọc tài liệu · trần `PHIENBAN.md` · trần dòng sổ quyết định: **số ở
`soat_nguong.json`, máy S10·S13·S14·S15 tự soi** — đừng đếm tay, đừng chép số vào đây.

Hai ngưỡng còn lại chưa có máy nào canh, phải tự nhớ:

| Ngưỡng | Con số | Vượt thì |
|---|---|---|
| Bản sao một đoạn | Lần 1 viết · lần 2 được chép **nếu qua 3b** · lần 3 **bắt buộc gom** trước khi viết bản 3 | Gom ngay trong việc đang làm |
| Tham số hàm | **>5 tham số** | Ghi nợ; lần sửa sau gom thành một dict/dataclass |

## Q5 — Khi nào BẮT BUỘC ghi quyết định

Đúng bốn cửa, ngoài ra miễn: **(1)** chọn A thay vì B mà 6 tháng sau nhìn code **không tự thấy** lý
do · **(2)** cố ý làm trái `L1`–`L4`, hoặc nhận một ảnh-chụp-chép-dán (3b) · **(3)** chạm schema
Anki · **(4)** khai tử hoặc đóng băng một thứ.

Sửa bug thường, thêm từ, chỉnh câu chữ — **không ghi**, commit message có thân là đủ.
Cách ghi (một dòng bảng, trần ký tự, luật số) nằm ở đầu `QUYETDINH.md`, S15 canh.

## Q6 — Làm việc với AI cho đúng

Sự thật nền: **mỗi phiên AI là nhân viên mới ngày đầu.** Thứ bạn muốn nó "luôn luôn làm" phải nằm
trong file nó tự đọc — `CLAUDE.md` + hook bơm lại mỗi lượt (QD-09/QD-13), không nằm trong trí nhớ
của bạn hay của phiên trước.

### 6b. Ra yêu cầu để không có wrapper thứ 11

AI mặc định chép-cho-chắc vì lệnh thường chỉ nói *đích* ("thêm nút X") mà không nói *ràng buộc đường
đi*. Ba câu này đã nằm sẵn trong `CLAUDE.md`, chỉ cần nhắc lại khi việc lớn:

- *"Trước khi viết, **liệt kê hàm/module có sẵn** nên dùng lại. Có cái gần giống thì mở rộng nó."*
- *"**Không tạo file mới, không viết hàm trùng vai** với hàm đã có, trừ khi nêu lý do và được gật."*
- *"Sửa **ít file nhất có thể**; xong việc khai: đã đổi file nào, vì sao từng file."*

### 6c. Nghiệm thu khi không đọc nổi từng dòng

Đừng cố đọc code — đọc **hình dạng của diff** và **lời khai của AI**. Ba dấu hiệu đỏ:

1. **Diff to hơn lời hứa.** Xin một chức năng mà 6–7 file đổi, hoặc có file đổi mà AI không giải
   thích ⇒ bắt khai từng file trước khi nhận.
2. **File mới / hàm mới tên na ná cái cũ** (`get_anki_data` cạnh `fetch_anki`…) ⇒ hỏi đúng một câu:
   *"vì sao không dùng cái cũ?"*. Trả lời không thuyết phục = wrapper thứ 11 đang chào đời.
3. **Chạm vùng im lặng mà không có lưới**: thấy `deleteNotes`, `updateNoteFields` hàng loạt, đổi
   model/field mà không có backup, không có bước kiểm sau ⇒ dừng, đi cửa L4.

Kèm thủ tục rẻ: cuối việc bắt AI **tự khai ba mục** — *đã đổi gì · lệnh nghiệm thu · rủi ro im lặng
nào có thể có*. Mục thứ ba quý nhất: AI biết rủi ro của code nó vừa viết, nhưng chỉ nói khi bị hỏi.

### 6d. Năm cửa DỪNG LẠI HỎI

Nguyên văn đã nằm trong `CLAUDE.md`: đổi field/model Anki · xoá-ghi đè hàng loạt thẻ thật · tạo file
`.py` mới ở gốc · viết hàm thứ hai cùng vai · đụng hạ tầng ngoài phạm vi. Cả năm đều hiếm, nên tổng
chi phí chỉ vài câu xác nhận mỗi tuần — rẻ hơn nhiều so với một lần "Sync status 2" im lặng.

## Q7 — Nói KHÔNG và cắt phạm vi

Ba phép thử trước khi thêm bất cứ thứ gì, hỏi đúng thứ tự:

1. **Nó phục vụ buổi học tuần này, hay nó "sẽ hay"?** "Sẽ hay" ⇒ không làm. Bộ lọc này tồn tại vì
   sản phẩm là công cụ học *đang dùng hằng ngày* — mọi giờ xây thứ "sẽ hay" là giờ không soạn kho.
2. **Giá NUÔI, không chỉ giá xây.** Nó có chạy trên VPS 24/7 không? Hỏng nó có mất buổi học không?
   Có ⇒ nó là *hạ tầng*, mà hạ tầng thì trả tiền nuôi mãi mãi: log, restart, backup, thêm một chỗ
   nữa để sync kẹt. Tính giá đó **trước** khi gật.
3. **Chi phí cơ hội tính bằng lô.** Ngân sách AI là ràng buộc thật, và chủ nợ là **hàng đợi kho chưa
   soạn xong** (đo bằng `congcu.py trangthai`, đừng chép con số vào đây). Câu hỏi đúng không phải
   "feature này có đáng không" mà **"nó đáng hơn 2 lô soạn kho không?"**

**Một dòng đọc ngược từ chính dự án:** thứ đã cứu bạn không phải chức năng thứ 20 của bot, mà mấy
cái luật nhỏ tự đặt. Phân vân xây gì tiếp thì xây thêm *luật/cửa soát* thường lãi hơn *chức năng*.

## Q8 — Thứ KHÔNG nên áp dụng ở quy mô này

| Thực hành | Vì sao ở đây nó hại | Ngưỡng xét lại |
|---|---|---|
| CI/CD | `deploy.ps1` đã chạy đủ ba cửa trước khi push; CI chỉ thêm thời gian chờ, và nó cứu lỗi phối hợp nhiều người — ở đây không có ai để phối hợp | Có cộng tác viên thứ hai |
| Code review nghi thức | Không có người thứ hai; giả vờ review từng dòng code AI là kịch. Nghiệm thu 6c **chính là** review đúng dạng: review hình dạng | Không bao giờ, ở quy mô một người |
| Nhánh git phức tạp (gitflow, PR) | Chi phí nhánh trả cho nhiều người song song — không tồn tại ở đây. Làm thẳng trên `main` | Việc lớn kéo dài >1 ngày mà bot phải sống ⇒ một nhánh tạm, xong merge rồi xoá |
| Type hint toàn bộ | Không có `mypy` nào chạy để hưởng. Chỉ hint **chữ ký public của `anki_tools`** — ranh giới các mảng gặp nhau | Lỗi kiểu-dữ-liệu qua ranh giới gói xảy ra lần 2 ⇒ bật mypy riêng cho `anki_tools/` |
| Dependency injection, kiến trúc lớp | DI trả giá dễ-thay-thế để phục vụ test double; bộ test ở đây cố ý HẸP, chỉ test chỗ đã hỏng thật | Không, ở quy mô này |
| Microservice / tách repo | 4 mảng gặp nhau ở bộ sưu tập Anki; tách repo biến một lần sửa xuyên mảng thành 2 PR + 2 deploy | Không, chừng nào còn một người |
| Đuổi độ phủ test | Test ở đây cố ý HẸP: **chỉ test chỗ ĐÃ HỎNG THẬT một lần**. Đuổi độ phủ trên code AI viết đẻ ra test dối, mà lỗi thật của dự án nằm ở **dữ liệu** | Một hàm hỏng lần thứ 2 cùng kiểu ⇒ viết test cho đúng hàm đó, không hơn |

Mẫu số chung: các món trên đều **trả chi phí mỗi-lần-sửa để mua an toàn phối-hợp-nhiều-người**. Dự
án này ngược lại: một người, ngân sách theo lượt, rủi ro nằm ở *hỏng im lặng trên dữ liệu*.

## 🎯 Nếu chỉ nhớ ba câu

1. **Luật không nằm trong file AI đọc được, hoặc không có máy đo được — là luật trang trí.**
   (`CHUAN.md` sống khoẻ; "MỘT chức năng MỘT script" chết non, dù cả hai đều đúng.)
2. **Mỗi phiên AI là nhân viên mới ngày đầu** — `CLAUDE.md` + hook là sổ tay onboarding, viết một
   lần, mọi phiên tự tuân.
3. **Sợ nhất không phải code chết to tiếng, mà là dữ liệu hỏng im lặng** — mọi việc chạm vùng im
   lặng phải đứng một mình, có backup, có một vòng kiểm sau.
