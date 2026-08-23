# ==============================================================================
# --- GẮN TAG CHỦ ĐỀ (topic::...) CHO THẺ ANKI ---
# Cách dùng (chạy trên máy có Anki + AnkiConnect đang mở):
#   python tag_topics.py           -> NHÁP: chỉ in kế hoạch, KHÔNG đụng gì vào Anki
#   python tag_topics.py --apply   -> gắn tag thật (chỉ tag, không sửa nội dung thẻ,
#                                     không ảnh hưởng tiến độ học)
#   python tag_topics.py --fix     -> xếp lại CẢ thẻ ĐÃ có tag (dùng khi đổi cây chủ đề)
#
# AI XẾP, KHÔNG PHẢI BẢNG TRA (user chốt 23/08/2026, QD-37).
# Trước đây chỗ này có dict `TOPIC_WORDS` ~100 dòng chép tay cho ~610 từ. Đã thử
# thay bằng nhãn sẵn của ros-edu.ru rồi BỎ: đo ra nhãn từng từ của họ sai có hệ
# thống — 6/16 cặp từ đối nhau bị tách sang hai chủ đề khác nhau (`папа` ở "Семья"
# mà `мама` ở "Жизнь человека"; `жена` một chỗ, `муж` chỗ khác; `вопрос` bị xếp
# vào "từ để hỏi" dù nó là danh từ; màu sắc bị dồn hết vào "đặc điểm đồ vật", làm
# rỗng nhánh `qualities::colors` đang chạy tốt).
# Từ ros-edu chỉ lấy DANH SÁCH TỪ + TRÌNH ĐỘ (`data/rosedu_muc.json`) — phần đó
# là chuẩn ТРКИ đã xuất bản, tin được. Chủ đề thì AI xếp theo `anki_tools/topics.py`.
#
# An toàn:
# - Không có --fix: thẻ ĐÃ có tag topic:: -> bỏ qua (chạy lại bao nhiêu lần cũng được).
# - Chỉ đụng note thuộc model của bot (MODEL_NAME trong config.py).
# - Từ AI không xếp được -> ĐỂ TRỐNG tag, in ra danh sách. KHÔNG ép vào rọ (QD-38).
# ==============================================================================
import argparse
import json
import os
import sys
from collections import Counter

import requests

# Chay duoc tu bat cu dau: file nay khong con nam o goc repo nen phai tu tro
# duong dan goc vao sys.path truoc khi import anki_tools (G3, 31/07/2026).
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from anki_tools.config import ANKI_CONNECT_URL, MODEL_NAME
from anki_tools.topics import TOPICS, topic_tag, TOPIC_TAG_PREFIX, LEGACY_ALIASES
from anki_tools.utils import strip_accents_perfectly

# Số từ gửi AI mỗi lượt. 25 là chỗ cân: danh sách 35 chủ đề (~2K token) là phần
# cố định của mỗi request, chia cho 25 từ thì rẻ; to hơn nữa thì model bắt đầu
# trả thiếu mục và phải gọi lại, mất luôn cái vừa tiết kiệm.
CO_LO = 25

BAN_CHUP = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "data", "rosedu_muc.json")


def doc_muc_trki():
    """-> dict {từ không dấu nhấn: 1=A1 2=A2 3=B1 4=B2}. {} nếu chưa có bản chụp.

    CHỈ dùng để in kèm cho dễ soát (biết từ nào là từ vỡ lòng), KHÔNG dùng để
    quyết định chủ đề — xem ghi chú đầu file."""
    try:
        with open(BAN_CHUP, encoding="utf-8") as f:
            d = json.load(f)
    except (OSError, ValueError):
        return {}
    muc = {}
    for w, m, _cats in d["tu"]:
        key = strip_accents_perfectly(w).strip().lower()
        if key:
            muc[key] = min(m, muc.get(key, 9))
    return muc


WORD_MUC = doc_muc_trki()
TEN_MUC = {1: "A1", 2: "A2", 3: "B1", 4: "B2"}


def call(action, **params):
    r = requests.post(ANKI_CONNECT_URL, json={"action": action, "version": 6, "params": params}, timeout=60)
    j = r.json()
    if j.get("error"):
        raise SystemExit(f"AnkiConnect lỗi ({action}): {j['error']}")
    return j["result"]


def xep_bang_ai(can_xep):
    """can_xep: list (note_id, từ, nghĩa Anh) -> dict {note_id: slug hoặc None}."""
    from anki_tools.ai_client import call_claude_topic
    ra = {}
    for i in range(0, len(can_xep), CO_LO):
        lo = can_xep[i:i + CO_LO]
        print(f"   AI lượt {i // CO_LO + 1}/{-(-len(can_xep) // CO_LO)} "
              f"({len(lo)} từ)...", flush=True)
        ket = call_claude_topic([(w, en) for _nid, w, en in lo])
        for nid, w, _en in lo:
            ra[nid] = ket.get(w)
    return ra


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Gắn tag chủ đề topic:: cho thẻ Anki")
    ap.add_argument("--apply", action="store_true", help="gắn tag thật (mặc định: nháp)")
    ap.add_argument("--fix", action="store_true",
                    help="xếp lại CẢ thẻ đã có tag (dùng khi đổi cây chủ đề). "
                         "Không có cờ này thì chỉ đụng thẻ chưa có tag.")
    args = ap.parse_args()

    note_ids = call("findNotes", query=f'note:"{MODEL_NAME}"')
    notes = call("notesInfo", notes=note_ids)
    print(f"Tổng số note: {len(notes)}")

    can_xep = []     # (note_id, từ, nghĩa Anh) — sẽ hỏi AI
    tag_cu = {}      # note_id -> [tag topic:: đang có]
    bo_qua = 0
    for n in notes:
        f = n["fields"]
        word = f.get("WordClean", {}).get("value", "") or strip_accents_perfectly(
            f.get("Word", {}).get("value", ""))
        hien_co = [t for t in n.get("tags", []) if t.startswith(TOPIC_TAG_PREFIX)]
        if hien_co and not args.fix:
            bo_qua += 1
            continue
        tag_cu[n["noteId"]] = hien_co
        en = f.get("Meaning", {}).get("value", "")
        can_xep.append((n["noteId"], word.strip().lower(), en[:200]))

    print(f"Bỏ qua (đã có tag, không có --fix): {bo_qua}")
    if not can_xep:
        print("Không có thẻ nào cần xếp.")
        return
    so_lo = -(-len(can_xep) // CO_LO)
    print(f"Cần xếp: {len(can_xep)} thẻ -> {so_lo} lượt gọi AI\n")

    if not args.apply:
        print("(NHÁP — chưa gọi AI, chưa gắn gì. Chạy lại với --apply để làm thật.)")
        print("Mẫu 15 thẻ sẽ đem đi xếp:")
        for nid, w, _en in can_xep[:15]:
            muc = TEN_MUC.get(WORD_MUC.get(w), "—")
            print(f"   [{muc}] {w:18s} đang: {', '.join(tag_cu[nid]) or '(chưa có)'}")
        return

    ket = xep_bang_ai(can_xep)

    doi, giu, mo_coi = {}, 0, []
    for nid, w, _en in can_xep:
        slug = ket.get(nid)
        if not slug:
            mo_coi.append(f"{w} (đang: {', '.join(tag_cu[nid]) or 'chưa có'})")
            continue
        if tag_cu[nid] == [topic_tag(slug)]:
            giu += 1
            continue
        doi[nid] = slug

    print(f"\nGiữ nguyên: {giu} | Đổi tag: {len(doi)} | Chưa xếp được: {len(mo_coi)}")
    dem = Counter(doi.values())
    for slug, n in dem.most_common():
        print(f"   {topic_tag(slug):32} +{n}")

    # 🔴 PHẢI IN, kể cả rỗng (QD-38). Đây là con số thay cho cái rọ rác cũ: trước
    # đây chúng lặng lẽ vào `concepts::misc` và trông như đã phân loại xong.
    print(f"\nCHƯA XẾP ĐƯỢC (để trống tag, /thongke sẽ đếm): {len(mo_coi)}")
    for line in mo_coi:
        print("  ", line)

    for nid, slug in doi.items():
        cu = [t for t in tag_cu[nid] if t != topic_tag(slug)]
        if cu:
            call("removeTags", notes=[nid], tags=" ".join(cu))
        call("addTags", notes=[nid], tags=topic_tag(slug))
    print(f"\n✅ Đã gắn tag cho {len(doi)} thẻ.")

    # Tag cũ trỏ chủ đề đã bị xoá thì phải GỠ, không thì `build_subdecks` thấy thẻ
    # "có tag" mà tag chết, rồi bỏ lại đúng chỗ cũ — im lặng y như trước.
    go = [nid for nid, w, _en in can_xep
          if not ket.get(nid) and tag_cu[nid]
          and any(t[len(TOPIC_TAG_PREFIX):] not in TOPICS for t in tag_cu[nid])]
    for nid in go:
        call("removeTags", notes=[nid], tags=" ".join(tag_cu[nid]))
    if go:
        print(f"🧹 Đã gỡ tag CHẾT khỏi {len(go)} thẻ (chủ đề không còn tồn tại).")
    print(f"\nBước tiếp: python scripts/build_subdecks.py  (nháp) rồi --apply")


if __name__ == "__main__":
    main()
