---
description: Chốt YÊU CẦU trước khi viết code — hỏi user bằng trắc nghiệm cho tới khi rõ
argument-hint: [mô tả sơ sài cũng được, kiểu "bot nên nhắc tôi ôn"]
---

# /ycau — cửa số 1: làm rõ user MUỐN GÌ, trước khi đụng code

User đã nói ra ý tưởng ở dạng thô nhất: **$ARGUMENTS**

## Sự thật nền — đọc trước, đây là lý do lệnh này tồn tại

User **không phải lập trình viên** và tự nhận *"tôi không giỏi diễn đạt tính năng"*. Vậy nên
**diễn đạt cho rõ là việc của BẠN, không phải của user.** Một câu mô tả thô KHÔNG phải là user
làm ẩu — đó là đầu vào hợp lệ và đúng như dự kiến của lệnh này.

🔴 **CẤM tuyệt đối trong lệnh này:** viết code, sửa file code, chạy lệnh đổi dữ liệu.
Lệnh này chỉ đẻ ra **một phiếu việc**. Không hơn.

## Bước 1 — TỰ ĐI ĐO trước khi hỏi (bắt buộc, đừng bỏ)

Hỏi user cái mà bạn tự tra được là hành vi bị cấm ở `CLAUDE.md` mục 1. Trước khi mở miệng hỏi:

1. Đọc `QUYETDINH.md` — **nhất là bảng "📏 ĐÃ ĐO RỒI BÁC" ở đầu file**. Ý tưởng của user
   trùng một dòng đã bị BÁC? → nói ra NGAY, kèm số liệu ở cột *Vì*, đừng đi tiếp.
2. Đọc `SONO.md` — việc này đụng file nào đang mang nợ?
3. Grep tìm **chức năng gần giống đã có**. Rất hay gặp: thứ user xin đã tồn tại, chỉ khác tên.
4. Việc đụng từ hai mảng trở lên → đọc `KIENTRUC.md`.
5. Đối chiếu `CACHLAM.md` Q7 (ba phép thử nói KHÔNG): nó phục vụ **buổi học tuần này** hay chỉ
   là "sẽ hay"? Giá **nuôi** nó (VPS 24/7, hỏng thì mất buổi học) là bao nhiêu? Nó có đáng
   **hơn 2 lô soạn kho** không?

## Bước 2 — HỎI USER bằng trắc nghiệm (đây là phần quan trọng nhất)

Dùng công cụ **AskUserQuestion** — nút bấm, không phải câu hỏi mở. Tối đa 4 câu một lượt,
mỗi câu 2–4 lựa chọn **cụ thể**, phương án bạn khuyên đặt đầu tiên kèm chữ *(đề xuất)*.

**Luật ra câu hỏi:**

- ❌ Đừng hỏi *"bác muốn thiết kế thế nào?"* / *"nên dùng cấu trúc nào?"* — user **DUYỆT**,
  không **THIẾT KẾ**. Bạn phải tự nghĩ ra các phương án rồi mới đưa ra bấm.
- ❌ Đừng dùng thuật ngữ trong câu hỏi. "field", "cache", "hook" → dịch sang việc user thấy được.
- ✅ Hỏi bằng **cảnh cụ thể**: *"Lúc bác đang ôn giữa chừng mà đến giờ nhắc, bot nên: (a) nhắn
  luôn, (b) đợi bác ôn xong, (c) không nhắn nếu hôm nay đã ôn rồi."*
- ✅ Mỗi lựa chọn nói rõ **được gì / mất gì**, bằng ngôn ngữ thường.

**Bốn nhóm phải hỏi cho ra** (gộp lại còn 3–4 câu, đừng hỏi rời rạc thành 10 lượt):

| Nhóm | Cần moi ra điều gì |
|---|---|
| **Cảnh dùng** | Bác dùng nó lúc nào, trên điện thoại hay máy tính, bao lâu một lần |
| **Nhìn thấy gì đổi** | Sau khi xong, cái gì trên màn hình khác đi so với bây giờ |
| **Thế nào là ĐÚNG** | Một cảnh cụ thể mà nếu chạy ra kết quả đó thì coi như xong |
| **Ranh giới** | Cái gần giống mà **cố ý KHÔNG làm** lần này (chống phình việc) |

Chưa rõ thì **hỏi tiếp một lượt nữa**. Thà hỏi 2 lượt còn hơn code sai rồi sửa 2 ngày.

## Bước 3 — Viết phiếu việc `VIECDANGLAM.md`

**GHI ĐÈ** file (đừng nối thêm — file này luôn chỉ chứa MỘT việc đang làm; nối thêm là con
đường đã giết `CHANGELOG.md`, xem QD-06). Trần: ngân sách đọc trong `soat_nguong.json`, cửa S10
canh bằng KÝ TỰ (QD-20).

```markdown
# 🎯 VIỆC ĐANG LÀM — <tên việc bằng ngôn ngữ thường>
> Phiếu này bị GHI ĐÈ ở việc kế tiếp. Xong việc thì xoá nội dung, để lại đúng dòng tiêu đề.

## Một câu
Chức năng này để ___, dùng khi ___.

## User đã chốt (từ câu hỏi trắc nghiệm)
- <điều đã chốt 1>
- <điều đã chốt 2>

## Coi là XONG khi
- [ ] <cảnh cụ thể nhìn được bằng mắt: thẻ hiện thế này / bot trả lời thế kia>

## CỐ Ý KHÔNG LÀM lần này
- <thứ gần giống bị cắt khỏi phạm vi>

## Đã đo trước khi nhận việc
- Trùng bảng "ĐÃ ĐO RỒI BÁC"? <có/không + dòng nào>
- Chức năng gần giống đã có? <tên hàm/file, hoặc "không có">
```

## Bước 4 — Đi thẳng sang cửa 2, ĐỪNG bắt user gõ gì

Tóm hai câu ngôn ngữ thường (**tôi hiểu bác muốn gì · tôi CỐ Ý không làm gì**), rồi **tự động đọc
`.claude/commands/kehoach.md` và làm tiếp ngay**. User chỉ dừng lại đúng **MỘT lần** để duyệt kế
hoạch — đừng bắt họ nhớ tên lệnh nào, đừng hỏi *"bác có muốn tôi lập kế hoạch không?"*.
