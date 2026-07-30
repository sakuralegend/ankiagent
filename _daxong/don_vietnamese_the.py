# -*- coding: utf-8 -*-
"""Gỡ phần ghi THỂ ĐỘNG TỪ khỏi field `Vietnamese` — badge đã in sẵn rồi.

    python don_vietnamese_the.py            # CHẠY KHAN, in từng dòng cũ -> mới
    python don_vietnamese_the.py --apply    # ghi thật

## Vì sao có file này

README §2c từng bắt buộc viết tay *"(HOÀN THÀNH — một lần, xong việc)"* vào dòng
tiếng Việt của mọi động từ, vì **không field nào chứa thể** nên đề bài `nói` không
phân biệt được `сказа́ть` với `говори́ть`. Từ 29/07/2026 có field `AspectBadge`
in ngay cạnh badge từ loại ⇒ dòng tiếng Việt đang nói lại đúng thứ user đang
nhìn thấy — chính lỗi user đã bắt trước đây với từ loại (*"cái từ loại không cần
ghi đâu, vì thẻ của tôi đã có field đó rồi"*).

## Vì sao là BẢNG CHỈ ĐỊNH TAY chứ không phải regex

🔴 Thẻ `вы́полнить` có `Vietnamese = "hoàn thành, thực hiện"` — đó là **NGHĨA của
từ**, không phải ghi chú thể. Mọi regex bắt chữ "hoàn thành" đều xoá mất nghĩa
của thẻ này. README cũng đã dặn đúng chuyện đó: *"agent tự phán đoán chứ đừng
dựng cửa máy"*.

Và phần trong ngoặc KHÔNG phải lúc nào cũng chỉ là thể — nhiều chỗ còn gánh nét
phân biệt mà badge KHÔNG cứu được, phải giữ lại:
  · `учи́ться`  "phản thân, KHÔNG phải dạy"  — tách khỏi `учи́ть`
  · `ви́деть`   "mắt bắt được, không chủ ý"  — tách khỏi `смотре́ть`
  · `гуля́ть`   "dạo ngoài trời…"            — tách khỏi `ходи́ть`
  · `звони́ть`  "không tiền tố"              — tách khỏi `позвони́ть`
"""
import json
import re
import sys
import urllib.request

# Chay duoc tu bat cu dau: file nay khong con nam o goc repo nen phai tu tro
# duong dan goc vao sys.path truoc khi import anki_tools (G3, 31/07/2026).
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from anki_tools.config import ANKI_CONNECT_URL, MODEL_NAME

# {WordClean: dòng tiếng Việt MỚI}. Soạn tay sau khi đọc cả 88 động từ.
# Nguyên tắc: bỏ phần nói về THỂ, giữ nguyên mọi nét phân biệt khác.
MOI = {
    # --- ngoặc CHỈ chứa thể -> bỏ cả ngoặc ---
    "танцевать":  "nhảy múa, khiêu vũ",
    "рисовать":   "vẽ, phác hoạ",
    "целовать":   "hôn",
    "понимать":   "hiểu",
    "думать":     "nghĩ, suy nghĩ, cho rằng",
    "повторять":  "lặp lại, ôn tập",
    "жить":       "sống, sinh sống ở đâu",
    "завтракать": "ăn sáng",
    "обедать":    "ăn trưa",
    "ужинать":    "ăn tối",
    "проверять":  "kiểm tra, rà soát",
    "поставить":  "đặt, dựng",
    "посмотреть": "xem, nhìn",
    "объявить":   "tuyên bố, công bố cho mọi người biết",
    "сказать":    "nói ra, bảo một câu",
    "спросить":   "hỏi một câu",
    # `(xong)` cũng là ký hiệu thể, chỉ viết ngắn hơn
    "прочитать":  "đọc",
    "написать":   "viết, nhắn tin",
    # --- ngoặc còn gánh nét phân biệt khác -> CHỈ cắt phần thể ---
    "учиться":    'học, đi học (phản thân, KHÔNG phải "dạy")',
    "играть":     "chơi (thể thao, trò chơi, nhạc cụ)",
    "видеть":     "nhìn thấy, trông thấy (mắt bắt được, không chủ ý)",
    "гулять":     "đi dạo chơi (dạo ngoài trời, không nhằm tới đâu)",
    "звонить":    "gọi điện thoại (không tiền tố)",
    "спрягаться": "được chia (nói về động từ) — dạng phản thân -ся",
}

# Thẻ có chữ "hoàn thành" nhưng ĐÓ LÀ NGHĨA — tuyệt đối không đụng.
KHONG_DUNG = {"выполнить": "'hoàn thành, thực hiện' là NGHĨA của từ, không phải thể"}


def ac(action, **params):
    req = urllib.request.Request(
        ANKI_CONNECT_URL,
        json.dumps({"action": action, "version": 6, "params": params}).encode())
    out = json.load(urllib.request.urlopen(req, timeout=120))
    if out.get("error"):
        raise RuntimeError(f"{action}: {out['error']}")
    return out["result"]


def main():
    apply = "--apply" in sys.argv
    notes = ac("notesInfo", notes=ac("findNotes", query=f'note:"{MODEL_NAME}"'))
    theo_tu = {}
    for n in notes:
        wc = (n["fields"].get("WordClean", {}).get("value") or "").strip()
        # thẻ trùng do ký tự zero-width -> ghi vào CẢ HAI, đừng bỏ sót một cái
        theo_tu.setdefault(wc.replace("​", "").lower(), []).append(n)

    doi, thieu, da_dat = [], [], 0
    for wc, moi in MOI.items():
        ns = theo_tu.get(wc)
        if not ns:
            thieu.append(wc)
            continue
        for n in ns:
            cu = n["fields"]["Vietnamese"]["value"]
            if cu.strip() == moi:
                da_dat += 1
                continue
            if not n["fields"].get("AspectBadge", {}).get("value", "").strip():
                # Không có badge mà đã gỡ chữ thể khỏi đề bài = user mất hẳn
                # thông tin. Thà không sửa còn hơn.
                thieu.append(f"{wc} (CHUA CO BADGE — bo qua)")
                continue
            doi.append((n["noteId"], wc, cu, moi))

    print(f"{len(notes)} thẻ | sẽ đổi {len(doi)} | đã đạt sẵn {da_dat}")
    print("\n=== ĐỀ BÀI deck 1-go SẼ ĐỔI (đọc kỹ: đây là dòng bạn nhìn rồi gõ) ===")
    for _, wc, cu, moi in doi:
        print(f"  {wc:14s} {cu}")
        print(f"  {'':14s}   -> {moi}")
    for wc, ly in KHONG_DUNG.items():
        print(f"\n  ⛔ KHÔNG đụng {wc}: {ly}")
    if thieu:
        print("\n  ⚠️ không xử lý: " + " · ".join(thieu))

    if not apply:
        print("\n(CHẠY KHAN — thêm --apply để ghi thật)")
        return
    for nid, _, _, moi in doi:
        ac("updateNoteFields", note={"id": nid, "fields": {"Vietnamese": moi}})
    print(f"\n✅ Đã ghi {len(doi)} thẻ.")


if __name__ == "__main__":
    main()
