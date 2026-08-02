# -*- coding: utf-8 -*-
"""Soi DỮ LIỆU NGỮ PHÁP tự mâu thuẫn — lớp lỗi mà `soat`/`dodai` mù hoàn toàn.

Vì sao có file này (SONO.md 02/08/2026): hai bộ soát của dây chuyền kho chỉ đo
phần **agent VIẾT**. Bảng biến cách thì do MÁY nối vào lúc ghi thẻ (`gan_bang`),
nên dữ liệu nguồn sai chảy thẳng ra mặt thẻ mà không cửa nào thấy. Đã dính thật:
`ке́ды` bị OpenRussian **đảo cách 5 với cách 6** ở cả số ít lẫn số nhiều
(`inst=ке́де · prep=ке́дом`), user học thuộc dạng sai mà không tự kiểm được.

🔴 KHÁC HẲN hướng đã bị BÁC ở bảng "ĐÃ ĐO RỒI BÁC" (đối chiếu `nouns.csv` với dữ
liệu cào). Hướng đó chết vì hai nguồn CÙNG thượng nguồn OpenRussian ⇒ trùng nhau
không chứng minh gì. Ở đây không so hai nguồn: chỉ soi bản ghi có **tự mâu thuẫn
với luật hình thái tiếng Nga** hay không — một nguồn tự nó cũng phải nhất quán.

Vì sao ở `anki_tools/` mà không nằm trong `grammar.py`: file đó đã 1309 dòng,
gấp đôi trần 700 của repo, và `_fable_plan.md` chốt dứt khoát *"việc mới liên
quan grammar → file mới import grammar, KHÔNG thêm hàm vào file này nữa"*.
File này **không import `grammar`** (thuần chuỗi) nên không đẻ vòng import. (QD-15)

Cố ý KHÔNG tự sửa dữ liệu, chỉ in ra: sửa mù theo suy đoán thì lần sau nó lặng lẽ
đảo lại một bảng đang đúng — đúng loại hỏng im lặng đang muốn chặn.
"""
ACUTE = "́"
ZWSP = "​"

# 🔴 PHẢI TÁCH THEO SỐ, đừng gộp một rổ. Gộp thì `-ами` (cách 5 số nhiều) cũng
# kết thúc bằng `-и` — đuôi hợp lệ của cách 6 số ít — nên bảng bị đảo của `ке́ды`
# ở phần số nhiều LỌT SẠCH. Chính bộ test bắt được lỗi này ngay lần chạy đầu.
DUOI_CACH_5 = {
    # Số ít: -ом/-ем/-ём (đực·trung), -ой/-ей/-ёй + biến thể văn chương -ою/-ею
    # (cái, biến cách I), -ью (cái, biến cách III), -ым/-им (danh từ biến như
    # tính từ: моро́женым).
    "sg": ("ом", "ём", "ем", "ой", "ёй", "ей", "ою", "ею", "ью", "ым", "им"),
    # Số nhiều: -ами/-ями, và -ьми của nhóm bất quy tắc (людьми́, детьми́).
    "pl": ("ами", "ями", "ьми"),
}
DUOI_CACH_6 = {
    # Số ít: -е, -и/-ии (cái III và nhóm -ия/-ие), và -у/-ю của **cách vị trí**
    # (второй предложный: в лесу́, в году́ — dạng THẬT, đừng coi là lỗi).
    "sg": ("е", "и", "у", "ю"),
    "pl": ("ах", "ях"),
}


def _dang(o):
    """Ô từ điển -> dạng trần để soi đuôi.

    Ba thứ phải gọt trước khi so, nếu không cửa sẽ kêu oan hàng loạt:
      · ô nhiều biến thể `ке́дов, кед` -> lấy biến thể ĐẦU;
      · ô cách 6 hay có sẵn giới từ `в году́` -> lấy chữ CUỐI;
      · dấu trọng âm và zero-width -> bỏ, chúng không phải phần đuôi.
    """
    t = (o or "").split(",")[0].strip()
    if not t:
        return ""
    return t.split()[-1].replace(ACUTE, "").replace(ZWSP, "").replace("'", "").lower()


def _lac_cho(dang, duoi_dung, duoi_kia):
    """Dạng này KHÔNG mang đuôi của cách nó đang đứng, mà mang đuôi của cách kia.

    Phải hỏi ĐỦ HAI VẾ. Chỉ hỏi vế sau thì `людьми́` (cách 5 đúng) bị coi là khả
    nghi vì nó cũng kết thúc bằng `-и` — đuôi hợp lệ của cách 6.
    """
    return bool(dang) and not dang.endswith(duoi_dung) and dang.endswith(duoi_kia)


def dao_cach_5_6(rec):
    """-> [(số, ô cách 5, ô cách 6)] các khối bị ĐẢO cách 5 với cách 6.

    🔴 Đòi LỆCH CẢ HAI CHIỀU CÙNG LÚC mới báo. Một chiều lệch thì thường là biến
    thể thật hoặc nhóm bất quy tắc; hai chiều đổi chỗ cho nhau thì không có cách
    đọc nào khác ngoài "nguồn xếp nhầm cột". Đo trên 516 thẻ có bảng biến cách:
    **0 chỗ kêu oan**, và đem bản ghi hỏng của `ке́ды` ra thử thì bắt đủ 2 chỗ.

    Đánh đổi đã chọn: nguồn sai MỘT chiều vẫn lọt cửa này. Đổi lại cửa không bao
    giờ kêu oan — mà cửa kêu oan là cửa rồi cũng bị bỏ qua (README huongdan).
    """
    ra = []
    for so in ("sg", "pl"):
        o = ((rec or {}).get("decl") or {}).get(so) or {}
        c5, c6 = _dang(o.get("inst")), _dang(o.get("prep"))
        if (_lac_cho(c5, DUOI_CACH_5[so], DUOI_CACH_6[so])
                and _lac_cho(c6, DUOI_CACH_6[so], DUOI_CACH_5[so])):
            ra.append((so, o.get("inst"), o.get("prep")))
    return ra


def keu_neu_dao(bang, nhan=""):
    """Quét một bảng {từ: bản ghi} và KÊU TO. -> số chỗ bị báo.

    In ra chứ không ném lỗi: những lệnh gọi hàm này (`cao_nguphap`, `nap`) đang
    làm việc dài hàng trăm từ, chết giữa chừng vì một từ thì hại hơn là lợi.
    """
    loi = [(w, so, a, b) for w, rec in sorted((bang or {}).items())
           for so, a, b in dao_cach_5_6(rec)]
    if not loi:
        return 0
    print(f"\n🔴 DU LIEU NGU PHAP NGHI BI DAO CACH 5 <-> CACH 6"
          f"{(' (' + nhan + ')') if nhan else ''}: {len(loi)} cho")
    for w, so, a, b in loi:
        print(f"   {w:16s} {'so it' if so == 'sg' else 'so nhieu':9s} "
              f"cach5={a!r}  cach6={b!r}   <- nghi doi cho nhau")
    print("   -> Kiem tay roi va thang GrammarJSON cua the (sao luu truoc).\n")
    return len(loi)
