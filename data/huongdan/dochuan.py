# -*- coding: utf-8 -*-
"""Đo TỈ LỆ thẻ đạt chuẩn §2b — trên THẺ THẬT trong Anki, không phải trên file lô.

    python data/huongdan/dochuan.py

## "Đạt chuẩn mới nhất" nghĩa là gì

Chuẩn §2b (user chốt 28/07) có **hai con số cứng đo được bằng máy**:
  · vừa **một màn hình iPhone** — cao ≤ 700px (bảng chia gấp trong `<details>`
    KHÔNG tính, vì user chỉ thấy nó khi chủ động bấm vào)
  · tối đa **2 ô đỏ** (`hd-warn`)

Con số thứ ba của §2b ("không khối hệ thống dùng chung") đo theo LÔ chứ không đo
theo thẻ — một mục lặp ở ≥50% số thẻ mới là khối dùng chung — nên nó nằm ở
`congcu.py dodai`, không nằm đây.

🔴 **KHÔNG đòi thẻ phải có mục "Họ hàng".** Từ gốc trơn và hư từ (`пока́`,
`не`, `для`) không chẻ được và không có họ hàng chắc chắn; README §2 dặn thẳng
"không chắc thì bỏ mục đó". Bắt buộc có `.hd-fam` là ép agent bịa từ nguyên —
đúng thứ chuẩn này sinh ra để chặn.

Thẻ được chia làm bốn nhóm loại trừ nhau, cộng lại đúng bằng tổng số thẻ.
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(HERE, "kho"))

import congcu                                                    # noqa: E402
from anki_tools import goi_anki                                  # noqa: E402

MODEL = "RU_Word"


def ac(action, **params):
    """Vỏ mỏng quanh CỬA DUY NHẤT `anki_client` (L1) — giữ tên `ac` để ruột file
    không đổi. Trước 08/08 file này tự mở cổng AnkiConnect riêng; miễn trừ trong
    `soat_baseline.json` hẹn trả "sau 61 lô" và kho đóng 66/66 nên hạn đã tới."""
    return goi_anki(action, timeout=300, **params)


def doc_dau(tags):
    """Số hiệu chuẩn ghi trên tag `chuan::<N>` -> int, hoặc None nếu chưa có dấu.

    Đây là NGUỒN SỰ THẬT về "thẻ này đạt chuẩn nào" — nằm trên chính thẻ nên
    không lệch được với bộ sưu tập, và tra thẳng trong app Anki bằng
    `tag:chuan::3`. Xem khối comment ở `congcu.py` để biết vì sao phải có số hiệu.
    """
    so = [int(t.split("::")[1]) for t in (tags or [])
          if t.startswith(congcu.TAG_CHUAN + "::") and t.split("::")[1].isdigit()]
    return max(so) if so else None


def phan_loai(html):
    """-> ('trong'|'mn_cu'|'dat'|'vo', chi_tiet)"""
    # Bảng chia máy nối vào MỌI thẻ, kể cả thẻ chưa soạn chữ nào. Nên "rỗng"
    # phải đo trên phần NGƯỜI viết, sau khi gỡ bảng — nếu không thì 466 thẻ
    # trống trơn sẽ được đếm là "có nội dung".
    than = congcu.BANG_RE.sub("", html or "").strip()
    than = re.sub(r"<[^>]+>", "", than).strip()
    if not than:
        return "trong", None
    if "mn-" in (html or "") and "hd-" not in (html or ""):
        return "mn_cu", None
    cao = congcu.uoc_cao(html)
    do = (html or "").count("hd-warn")
    vo = []
    if cao > congcu.TRAN_CAO:
        vo.append(f"cao {cao}px")
    if do > congcu.TRAN_WARN:
        vo.append(f"{do} o do")
    return ("vo" if vo else "dat"), (cao, do, vo)


def main():
    notes = ac("notesInfo", notes=ac("findNotes", query=f'note:"{MODEL}"'))
    nhom = {"dat": [], "vo": [], "trong": [], "mn_cu": []}
    dau = {}
    for n in notes:
        f = n["fields"]
        wc = (f.get("WordClean", {}).get("value") or "").strip()
        loai, ct = phan_loai(f.get("HuongDan", {}).get("value", ""))
        nhom[loai].append((wc, ct))
        dau[wc] = doc_dau(n.get("tags"))

    tong = len(notes)
    soan = len(nhom["dat"]) + len(nhom["vo"])

    def pc(n, mau=tong):
        return f"{n * 100 / mau:5.1f}%" if mau else "  n/a"

    # ---- DẤU ĐẠT CHUẨN: câu trả lời CHÍNH cho "bao nhiêu thẻ đã đạt" ----
    # Đặt lên trên phần đo px/ô đỏ vì hai thứ đo hai câu hỏi khác nhau:
    # dấu trả lời "soạn theo chuẩn NÀO", px/ô đỏ chỉ trả lời "có quá dài không".
    # Một thẻ chuẩn cũ vẫn có thể lọt hai trần — đó đúng là chỗ đã gây loạn.
    hien = sum(1 for v in dau.values() if v == congcu.CHUAN_V)
    cu = sorted({v for v in dau.values() if v is not None and v < congcu.CHUAN_V})
    print(f"BO SUU TAP: {tong} the model {MODEL}")
    print(f"\n=== DAU DAT CHUAN (tag `{congcu.tag_chuan()}`) — chuan hien hanh v{congcu.CHUAN_V} ===")
    print(f"  DAT CHUAN HIEN HANH  {hien:4d}  {pc(hien)}   tra trong Anki: tag:{congcu.tag_chuan()}")
    for v in cu:
        n = sum(1 for x in dau.values() if x == v)
        print(f"  dat chuan CU v{v}      {n:4d}  {pc(n)}   -> phai soan lai")
    chua = sum(1 for v in dau.values() if v is None)
    print(f"  chua co dau          {chua:4d}  {pc(chua)}")
    print()
    print(f"=== DO DAI / O DO (do rieng, KHONG thay cho dau o tren) ===")
    print(f"  lot ca hai tran    {len(nhom['dat']):4d}  {pc(len(nhom['dat']))}"
          f"   <= {congcu.TRAN_CAO}px va <= {congcu.TRAN_WARN} o do")
    print(f"  da soan nhung VO   {len(nhom['vo']):4d}  {pc(len(nhom['vo']))}")
    print(f"  chua soan (trong)  {len(nhom['trong']):4d}  {pc(len(nhom['trong']))}")
    print(f"  con mnemonic cu    {len(nhom['mn_cu']):4d}  {pc(len(nhom['mn_cu']))}")
    print(f"  {'-' * 46}")
    print(f"  TONG               {sum(len(v) for v in nhom.values()):4d}")

    print(f"\nTRONG SO {soan} THE DA CO NOI DUNG: dat {pc(len(nhom['dat']), soan)}")

    if nhom["vo"]:
        ly = {}
        for wc, (cao, do, vo) in nhom["vo"]:
            for x in vo:
                ly[x.split()[-1] if "o do" in x else "cao"] = \
                    ly.get(x.split()[-1] if "o do" in x else "cao", 0) + 1
        print(f"  vo vi QUA CAO: {ly.get('cao', 0)}  |  vo vi QUA O DO: "
              f"{sum(v for k, v in ly.items() if k != 'cao')}")
        te = sorted(nhom["vo"], key=lambda x: -x[1][0])[:12]
        print("  te nhat: " + " · ".join(f"{w} {c[0]}px/{c[1]}o" for w, c in te))

    fn = os.path.join(HERE, "_dochuan.txt")
    io.open(fn, "w", encoding="utf-8").write("\n".join(
        f"{loai}\t{wc}\t{ct[0] if ct else ''}\t{ct[1] if ct else ''}"
        for loai in ("vo", "trong", "mn_cu", "dat") for wc, ct in sorted(nhom[loai])))
    print(f"\n-> chi tiet tung the: {os.path.relpath(fn)}")


if __name__ == "__main__":
    main()
