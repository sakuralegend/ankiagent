# 🗄️ KHO LƯU TRỮ QUYẾT ĐỊNH — toàn văn mục đã rời sổ sống

> **File này KHÔNG tính vào ngân sách đọc, và KHÔNG ai phải đọc nó trước khi làm việc.**
> Nó chỉ có một việc: giữ lời hứa rằng `grep QD-nn` luôn ra kết quả.
>
> 🔴 **Vì sao tách (QD-29, 04/08/2026).** Số hiệu `QD-nn` là **định danh vĩnh viễn** —
> 121 chỗ trong code trỏ tới. Nhưng trước 04/08, định nghĩa của số hiệu lại nằm trong
> `QUYETDINH.md`, tức là **một file bị tính tiền thuê chỗ**. Hậu quả: một quyết định đã
> chết hẳn vẫn phải trả tiền chỗ mãi mãi, vì xoá nó đi là làm gãy con trỏ trong code.
> Tách **định danh** khỏi **chỗ lưu** thì mục chết được phép chết mà không mất gì.
>
> **Mục ở đây không phải rác.** Chúng rời sổ sống vì đã có nhà tốt hơn — hoặc một cửa
> soát thi hành (lý do sống trong lời báo lỗi), hoặc đã thành sự thật nhìn thấy trong
> cây code, hoặc lý do đã nằm nguyên trong docstring ngay chỗ dùng. Sổ sống chỉ giữ
> thứ **không có nhà nào khác**.
>
> Muốn đầy đủ hơn nữa: `git log --grep QD-nn` — toàn văn bàn bạc nằm trong thân commit
> (đo 04/08: 265 commit, thân trung bình 928 ký tự).

| QD | Ngày | Quyết định | Vì sao (ngắn) |
|---|---|---|---|
| QD-22 | 03/08 | Tách ruột `soatkientruc.py` vào gói `soat/`, giữ tên điểm vào | Chạm trần 700 dòng. QD-02 chỉ đòi stdlib · không import module dự án · gõ được tên cũ. 🔴 Test trỏ gốc qua `khung.dat_goc()`, sai là test soi repo thật rồi xanh giả |
| QD-28 | 04/08 | `tests/test_*.py` vào `bo_qua_mau` của S13 — file test không bị trần dòng | L3 BẮT thêm test mỗi lần sửa bug, S13 PHẠT test dài ra ⇒ luật thua sẽ là luật viết test. Test là sổ một-bug-một-mục, cùng dạng `k*.py` |
| QD-27 | 04/08 | Nghĩa Việt: THẺ là chân lý. Bỏ cột `vi` ở `tudien.json`; `tiep` đọc từ thẻ; `--tatca` không phát lại `V`; `/sua` giữ bản user sửa | Đo 04/08: **353/1039** lệch. Đồng bộ ngược là việc TAY nên phiên nào cũng quên ⇒ `устать` bật lại |
| QD-26 | 04/08 | Field `BangMay` cho phần MÁY (bảng chia + cặp thể); `HuongDan` thuần phần Claude soạn | Hai chủ chung một ô ⇒ cửa soát lô đo cả phần máy, rác sống nhiều tuần (7 ca). Hết hạn: khi 0 thẻ còn bảng trong `HuongDan` |
| QD-25 | 03/08 | Luật "mọi `except` phải log hoặc khai lý do" thành cửa **S17** có ratchet, thay vì chỉ nằm trong sổ nợ | Đo 03/08: sổ ghi "15 chỗ", đếm thật ra **8** — luật bằng chữ vừa trôi vừa mang số cũ. Mốc 8 chốt vào baseline, chỉ cho GIẢM |
| QD-25 | 04/08 | Sổ nợ thành bảng: 1 nợ = 1 dòng + cột **Hết hạn**, quá hạn = ĐỎ chặn deploy `VIECDANGLAM.md` xong phiên: trống hoặc 1 đầu việc (S18-19) | Nợ 04/08 phình thành **10 dòng log** — trần TỔNG không chặn nổi mục nuốt ngân sách mục kia |
| QD-24 | 03/08 | Sổ nợ chỉ chứa nợ CHƯA trả — trả xong là XOÁ dòng, bài học dời sang nơi được đọc (S16 canh); mọi `.md` trong git đều có trần | Đo 03/08: xác nợ chiếm **67%** `SONO.md`, và làm hỏng luôn ngòi "chạm 10 mục" vì nó đếm cả xác |
| QD-23 | 03/08 | Sổ thành MỘT bảng, mỗi quyết định một dòng ≤250 ký tự; số không có ngày đo thì cấm ở lại | Đo 03/08: 40 câu chứa số, 3 câu sai ngay hôm đó; sổ phải tự đính chính "61 lô→64". Cửa S15 đếm thật |
| QD-21 | 03/08 | Mọi CON SỐ TRẦN về `soat_nguong.json`, tài liệu chỉ trỏ; S12–S14 canh | Bản sao thì sớm muộn lệch, nguồn thì bất khả. 🔴 Số trong QD cũ là LỊCH SỬ — số hiệu lực chỉ ở `soat_nguong.json` |
| ⚰️ QD-20 | 03/08 | Trần đọc đo bằng KÝ TỰ, không bằng dòng — S10 canh | Ký tự/dòng chạy từ 49 tới 140 tuỳ file ⇒ đếm dòng bỏ lọt hẳn file nặng 30 KB. Đừng "dọn" ngược về đếm dòng |
| QD-19 | 03/08 | Tách `grammar.py` thành 4 mảnh lá; `grammar.py` làm MẶT TIỀN re-export đủ tên cũ kể cả private | Caller và test không đổi một dòng. Nghiệm thu bằng "file vàng": chạy trên từ thật, diff phải = 0. `soat_nguphap.py` vẫn để RIÊNG |
| ⚰️ QD-18 | 03/08 | Tách 6 file quá trần theo khuôn "file vàng" — đã xong | Khuôn còn dùng cho mọi refactor sau: chạy hàm chỉ-đọc trên dữ liệu thật + so ast từng hàm, diff ≠ 0 là hoàn tác. `dispatch.py` cố ý KHÔNG tách |
| QD-17 | 03/08 | Cửa canh thẻ sai mặt bám đuôi nhịp sync 30′, gọi lại lõi `thang_cap_gd2()` | Chỉ chạy khi nhịp đó kéo về THÀNH CÔNG. 🔴 `forgetCards` là MỤC ĐÍCH của GĐ2, không phải tác dụng phụ — đừng "giữ tiến độ ôn cho lành" |
| QD-16 | 02/08 | Ghi hàng loạt lên note thì kéo sync về TRƯỚC; kéo hỏng thì DỪNG | Sync xử xung đột "ai sửa sau thắng TRỌN note" ⇒ bản cũ đè bản mới. Đổi deck sống sót vì nó nằm trên THẺ ⇒ thẻ đúng deck, sai mặt, không lỗi nào bật |
| ⚰️ QD-13 | 01/08 | Hook nhắc luật phải có cửa canh — S11 chạy THẬT lệnh hook mỗi lần soát | Kiểu chết hay gặp là `python` không có trên PATH: cửa chỉ nhìn tên file sẽ báo XANH trên đúng cái máy hook đang chết |
| QD-12 | 01/08 | Quyết định nào ĐỔI CODE thì ghi vết NGAY, dạng NGẮN; muốn sâu thì tra `git log` | Đo 01/08: cả hai tuần đầu dựng bot không để lại vết nào, dù đổi code nhiều nhất. NGẮN là thứ chặn sổ đi lại đường `CHANGELOG.md` |
| QD-11 | 31/07 | Bỏ hẳn `grammar_cache.json`, ô `GrammarJSON` trong thẻ là nguồn DUY NHẤT | Một nguồn thì không lệch được; hai bản giống hệt sớm muộn SẼ lệch âm thầm (89 thẻ lệch nhiều tuần). Anki đóng thì kêu to rồi DỪNG, cấm trả rỗng |
| QD-10 | 31/07 | AI TỰ commit khi việc xong + ba cửa xanh, không hỏi user | Luật cũ chỉ nói commit VIẾT THẾ NÀO, không nói KHI NÀO ⇒ việc nhớ rơi vào user. `commit` không đẩy đi đâu, cửa thật là `deploy.ps1` |
| QD-09 | 31/07 | Ba playbook `/ycau`→`/kehoach`→`/nghiemthu` + phiếu `VIECDANGLAM.md`, AI TỰ kích hoạt qua hook | Kit SDLC 12 bước quá nặng (số ở bảng trên). 🔴 Cơ chế nào bắt user nhớ lệnh là đã hỏng từ thiết kế |
| ⚰️ QD-08 · QD-05 | 31/07 | Thẻ là nguồn sự thật, cache chỉ là bộ đệm · cache ra ngoài repo | CHẾT cả hai — QD-11 thay trong cùng ngày, bỏ HẲN file cache. Giữ số vì `anki_client.py`, `KIENTRUC.md`, test và `VPS_SETUP.md` còn trỏ tới |
| QD-07 | 31/07 | `PHIENBAN.md` là file DUY NHẤT viết cho user, ngôn ngữ thường; S14 canh trần | Mọi file khác đều viết cho người làm. 🔴 Phiên soạn lô KHÔNG ghi vào đây (user bác 02/08) — mốc là DEPLOY, không phải "user cảm nhận được" |
| ⚰️ QD-06 | 31/07 | Đóng sổ `CHANGELOG.md`, lịch sử về `git log` — S9 canh "commit có thân" | Commit message gắn chặt với diff nên không nói dối được; tài liệu song song thì lệch mà không ai biết |
| ⚰️ QD-03 | 31/07 | 12 file lô thế hệ 1: tháo ngòi 31/07, **XOÁ HẲN 04/08**, sớm hơn điều kiện cũ | Điều kiện cũ (k51–k60 đủ `chuan::3`) hết nghĩa: 166/166 từ đã có nội dung TRÊN THẺ, file còn trong git, và QD-26 bỏ `attach_table` nên chúng hỏng |
| QD-02 | 31/07 | `soatkientruc.py` là điểm vào thứ 3 ở gốc, chỉ stdlib, ratchet một chiều, cắm vào `deploy.ps1` | Chỗ có máy đo thì sạch, chỗ chỉ có luật viết ra thì trôi. Ratchet chỉ cho GIẢM; nới được thì nó thành bảng ghi nợ chứ không phải cửa |
