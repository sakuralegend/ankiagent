# 🎯 VIỆC ĐANG LÀM
> Phiếu bị GHI ĐÈ ở việc kế tiếp. Xong việc thì để trống, chừa đúng dòng tiêu đề.

## ▶ Thêm từ tới HẾT B1 rồi dừng (user chốt 20/11/2026)
B1 = 795 từ đầu `data/sach_b2.json`. Mỗi bước xong ⇒ sửa mục này + commit (user dặn lưu tiến trình).
- Đợt B2 #3 = k126–k135, 200 từ: ✅ chốt lô · ✅ tạo thẻ · ✅ soạn HD (10 lô xanh, commit a3fc317) · ✅ dolo.tsv đủ 10 dòng · **☐ BƯỚC KẾ: `congcu.py xong` + `nap` 10 lô** → đo lại va chạm trên thẻ thật → `kiemtra.py` → 3 cửa → commit. Bước kế KHÔNG gọi agent, không tốn AI.
- Chờ user quyết (agent báo lên, thẻ cũ đã nạp nên agent không được sửa): `дочка`↔`дочь` (đều "con gái") · `велик`↔`велосипед` (đều "xe đạp") · `прощать`↔`извинять` "tha thứ" (đề xuất sửa извинять) · `организовать`↔`провести` "tổ chức" (đề xuất bỏ ở провести) · `узнавать`↔`понимать` "nhận ra" · `куда-то`/`куда-нибудь`, `где-нибудь`↔`где-то`: quyết chung với `что-то`/`что-нибудь` · `наоборот` phải thêm chữ vì trùng обратно/напротив · `монета`↔`копейка` (đề xuất копейка chỉ còn "cô-pếch").
- Sau đợt này còn **292 từ B1** (`туман`…`русско-английский`, đo 20/11). Lần sau:
  `xephangdoi.py chon N` với N = số B1 còn lại (đo lại trước, đừng tin số này) — **đừng
  lấy quá**, hết B1 là DỪNG, chưa sang B2.

## ⏸ Kế hoạch "thêm từ một mạch" — user CHƯA duyệt, đang nghĩ (18/11/2026)
Đợt B2 #1 (k111–k115, 101 từ, toàn Opus) XONG 18/11. Lần đó dừng nhiều ở luồng chính; đề
xuất để lần sau user chỉ nói "thêm N từ" là chạy một mạch:
- lệnh `xephangdoi.py giao`: in bối cảnh từng lô (va chạm lọc đủ 3 badge + lô nào lo gỡ +
  họ từ đã có thẻ) — đợt #1 phải viết tay 2 đoạn dò này;
- lệnh `xong` gộp: soát → dodai → xong → nap → chờ mở khoá → kiemtra, dừng đúng lô trượt
  (`kiemtra.py` cũng vấp "Collection lifecycle" ngay sau `nap` sync — chưa sửa);
- viết lại `lo.md` §1 theo đường mới, ngắn hơn.
**Đã chốt 18/11:** từ đồng tự sách B2 ⇒ Opus tự chọn nghĩa đúng trình độ, báo lại cuối đợt;
bot Telegram vẫn hỏi user như cũ. Trùng trọn dòng còn chờ user: `что-то`↔`что-нибудь` (cũ),
`от`↔`из`/`с` (cũ).
