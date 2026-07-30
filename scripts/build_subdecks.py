# ==============================================================================
# --- DỰNG CÂY DECK KHO: RUSSIAN::<topic> và dọn thẻ về đúng deck con ---
# Cách dùng (chạy trên máy có Anki + AnkiConnect đang mở):
#   python build_subdecks.py           -> DRY-RUN: chỉ in kế hoạch, không đụng Anki
#   python build_subdecks.py --apply   -> làm thật: tạo deck, chuyển thẻ, xóa deck
#                                         cũ đã trống, sync AnkiWeb
#
# Việc script làm (theo tag topic:: trên từng note):
# 1. Tạo cây deck theo TOPICS (topics.py): slug lồng cấp "life::food" thành
#    deck RUSSIAN::life::food (Anki tự tạo deck cha RUSSIAN::life).
# 2. Đọc tag topic:: của TỪNG note (model bot) -> chuyển card về đúng deck.
#    Tag tên cũ (LEGACY_ALIASES) vẫn được hiểu, nhưng nên chạy
#    `python tag_topics.py --fix --apply` trước để tag trên thẻ cũng được đổi mới.
#    changeDeck KHÔNG ảnh hưởng tiến độ học (lịch ôn nằm trên thẻ).
# 3. Note không có tag topic:: -> báo, KHÔNG di chuyển.
# 4. Xóa deck đã TRỐNG HOÀN TOÀN: cả deck ngoài kho lẫn deck RUSSIAN::* không
#    còn trong TOPICS (vd sau khi đổi cấu trúc cây). Trừ deck mặc định của Anki
#    và deck còn thẻ lạ (không thuộc model bot).
#
# Chạy lại nhiều lần vô hại: thẻ đã đúng chỗ thì changeDeck không đổi gì.
# ==============================================================================
import argparse
import sys
from collections import Counter

import requests

# Chay duoc tu bat cu dau: file nay khong con nam o goc repo nen phai tu tro
# duong dan goc vao sys.path truoc khi import anki_tools (G3, 31/07/2026).
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from anki_tools.config import (
    ANKI_CONNECT_URL, MODEL_NAME, STAGE1_DECK, STAGE2_DECK, TOPIC_DECK_PARENT,
)
from anki_tools.topics import TOPICS, TOPIC_TAG_PREFIX, normalize_topic

# Deck không bao giờ được xóa (deck mặc định của Anki — bản Việt hóa/gốc)
PROTECTED_DECKS = {"Default", "Mặc định"}


def call(action, **params):
    r = requests.post(ANKI_CONNECT_URL, json={"action": action, "version": 6, "params": params}, timeout=120)
    j = r.json()
    if j.get("error"):
        raise SystemExit(f"AnkiConnect lỗi ({action}): {j['error']}")
    return j["result"]


def valid_deck_set():
    """Toàn bộ deck hợp lệ của kho: RUSSIAN + mọi tổ tiên của từng slug.
    Vd slug 'people::family' -> RUSSIAN::people và RUSSIAN::people::family."""
    decks = {TOPIC_DECK_PARENT, STAGE1_DECK, STAGE2_DECK}
    for slug in TOPICS:
        parts = slug.split("::")
        for i in range(1, len(parts) + 1):
            decks.add(f"{TOPIC_DECK_PARENT}::{'::'.join(parts[:i])}")
    return decks


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Dựng cây deck kho theo chủ đề")
    ap.add_argument("--apply", action="store_true", help="làm thật (mặc định: dry-run)")
    args = ap.parse_args()

    note_ids = call("findNotes", query=f'note:"{MODEL_NAME}"')
    notes = call("notesInfo", notes=note_ids)

    # --- Kế hoạch chuyển thẻ: đọc tag CHÍNH XÁC từng note (không query tag chung
    # vì Anki coi tag:cha khớp cả tag con -> đếm/chuyển sai khi cây lồng cấp) ---
    # Thẻ đang trong lộ trình học (GĐ1 làm quen + GĐ2 gõ) KHÔNG bị bốc đi —
    # việc chuyển chúng đi là của run_don() (bot /don + job đêm).
    inbox_cards = set(call("findCards", query=f'deck:"{STAGE1_DECK}"')) | \
                  set(call("findCards", query=f'deck:"{STAGE2_DECK}"'))

    plan = {}          # deck đích -> [card_ids]
    untagged = []      # từ chưa có tag topic::
    legacy_tags = Counter()  # tag tên cũ còn trên thẻ (nên chạy tag_topics --fix)
    for n in notes:
        topic_tags = [t for t in n.get("tags", []) if t.startswith(TOPIC_TAG_PREFIX)]
        word = n["fields"].get("WordClean", {}).get("value", "?")
        if not topic_tags:
            untagged.append(word)
            continue
        raw_slug = topic_tags[0][len(TOPIC_TAG_PREFIX):]
        slug = normalize_topic(raw_slug)
        if raw_slug != slug:
            legacy_tags[raw_slug] += 1
        cards = [c for c in n.get("cards", []) if c not in inbox_cards]
        if cards:
            plan.setdefault(f"{TOPIC_DECK_PARENT}::{slug}", []).extend(cards)

    print(f"Deck tổng: {TOPIC_DECK_PARENT} ({len(notes)} note)")
    if inbox_cards:
        print(f"📥 Bỏ qua {len(inbox_cards)} thẻ đang học ở {STAGE1_DECK} / {STAGE2_DECK}")
    total = 0
    for deck, cards in sorted(plan.items()):
        print(f"  {deck:40} <- {len(cards):4} thẻ")
        total += len(cards)
    print(f"  {'TỔNG':40}    {total:4} thẻ")
    if legacy_tags:
        print(f"\n⚠️ Thẻ còn TAG TÊN CŨ (deck vẫn về đúng chỗ, nhưng nên đồng bộ tag):")
        for t, c in legacy_tags.items():
            print(f"   topic::{t}: {c} thẻ")
        print("   -> chạy `python tag_topics.py --fix --apply` rồi chạy lại file này.")
    if untagged:
        print(f"\n⚠️ {len(untagged)} note CHƯA có tag topic:: (không di chuyển): {', '.join(untagged[:20])}")
        print("   -> chạy `python tag_topics.py --apply` (hoặc --missing) trước.")

    # --- Deck dự kiến xóa nếu trống: deck ngoài kho + deck RUSSIAN::* mồ côi ---
    valid = valid_deck_set()
    stale_decks = [d for d in call("deckNames")
                   if d not in PROTECTED_DECKS and d not in valid]
    print(f"\nDeck sẽ xóa NẾU trống sau khi chuyển: {', '.join(sorted(stale_decks)) or '(không có)'}")

    if not args.apply:
        print("\n(DRY-RUN — chưa làm gì. Chạy lại với --apply để làm thật.)")
        return

    # --- Làm thật ---
    for deck in sorted(valid):
        call("createDeck", deck=deck)
    print(f"✅ Đã tạo cây deck ({len(valid)} deck)")

    for deck, cards in plan.items():
        if cards:
            call("changeDeck", cards=cards, deck=deck)
            print(f"✅ {deck}: đã nhận {len(cards)} thẻ")

    deleted, kept = [], []
    # Xóa deck con sâu trước (tên dài trước) để deck cha trống đúng lượt
    for d in sorted(stale_decks, key=len, reverse=True):
        remaining = call("findCards", query=f'deck:"{d}"')
        if remaining:
            kept.append(f"{d} (còn {len(remaining)} thẻ)")
        else:
            call("deleteDecks", decks=[d], cardsToo=True)  # deck trống, cardsToo vô hại
            deleted.append(d)
    if deleted:
        print(f"🗑 Đã xóa deck trống: {', '.join(deleted)}")
    if kept:
        print(f"📌 Giữ lại (còn thẻ không thuộc model bot): {', '.join(kept)}")

    print("⏳ Sync AnkiWeb...")
    call("sync")
    print("☁️ Xong. Mở Anki sẽ thấy cây deck mới; iPhone sync là có.")


if __name__ == "__main__":
    main()
