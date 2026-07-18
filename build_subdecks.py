# ==============================================================================
# --- DỰNG CÂY DECK KHO: RUSSIAN::<topic> và dọn thẻ về đúng deck con ---
# Cách dùng (chạy trên máy có Anki + AnkiConnect đang mở):
#   python build_subdecks.py           -> DRY-RUN: chỉ in kế hoạch, không đụng Anki
#   python build_subdecks.py --apply   -> làm thật: tạo deck, chuyển thẻ, xóa deck
#                                         cũ đã trống, sync AnkiWeb
#
# Việc script làm (theo tag topic:: đã gắn bằng tag_topics.py):
# 1. Tạo deck tổng TOPIC_DECK_PARENT (config.py) + 17 deck con <kho>::<slug>.
# 2. Chuyển TOÀN BỘ card của note (model bot) có tag topic::X về <kho>::X.
#    changeDeck KHÔNG ảnh hưởng tiến độ học (lịch ôn nằm trên thẻ, không trên deck).
# 3. Note không có tag topic:: -> báo, KHÔNG di chuyển (gắn tag trước bằng
#    tag_topics.py rồi chạy lại).
# 4. Xóa các deck cũ đã TRỐNG HOÀN TOÀN (trừ deck mặc định của Anki và cây kho).
#    Deck còn thẻ lạ (không thuộc model bot) sẽ được giữ nguyên.
#
# Chạy lại nhiều lần vô hại: thẻ đã đúng chỗ thì changeDeck không đổi gì.
# ==============================================================================
import argparse
import sys

import requests

from anki_tools.config import ANKI_CONNECT_URL, MODEL_NAME, TOPIC_DECK_PARENT
from anki_tools.topics import TOPICS

# Deck không bao giờ được xóa (deck mặc định của Anki — bản Việt hóa/gốc)
PROTECTED_DECKS = {"Default", "Mặc định"}


def call(action, **params):
    r = requests.post(ANKI_CONNECT_URL, json={"action": action, "version": 6, "params": params}, timeout=60)
    j = r.json()
    if j.get("error"):
        raise SystemExit(f"AnkiConnect lỗi ({action}): {j['error']}")
    return j["result"]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Dựng cây deck kho theo chủ đề")
    ap.add_argument("--apply", action="store_true", help="làm thật (mặc định: dry-run)")
    args = ap.parse_args()

    # --- Kế hoạch chuyển thẻ theo tag ---
    plan = {}      # deck con -> list card_ids
    untagged = []  # từ chưa có tag topic::
    for slug in TOPICS:
        note_ids = call("findNotes", query=f'note:"{MODEL_NAME}" tag:"topic::{slug}"')
        if not note_ids:
            continue
        card_ids = call("findCards", query=f'note:"{MODEL_NAME}" tag:"topic::{slug}"')
        plan[f"{TOPIC_DECK_PARENT}::{slug}"] = card_ids

    untagged_ids = call("findNotes", query=f'note:"{MODEL_NAME}" -tag:topic::*')
    if untagged_ids:
        infos = call("notesInfo", notes=untagged_ids)
        untagged = [i["fields"].get("WordClean", {}).get("value", "?") for i in infos]

    print(f"Deck tổng: {TOPIC_DECK_PARENT}")
    total = 0
    for deck, cards in sorted(plan.items()):
        print(f"  {deck:35} <- {len(cards):4} thẻ")
        total += len(cards)
    print(f"  {'TỔNG':35}    {total:4} thẻ")
    if untagged:
        print(f"\n⚠️ {len(untagged)} note CHƯA có tag topic:: (không di chuyển): {', '.join(untagged[:20])}")
        print("   -> chạy `python tag_topics.py --apply` (hoặc --missing) trước rồi chạy lại file này.")

    # --- Deck cũ dự kiến xóa nếu trống sau khi chuyển ---
    old_decks = [d for d in call("deckNames")
                 if d not in PROTECTED_DECKS
                 and d != TOPIC_DECK_PARENT
                 and not d.startswith(f"{TOPIC_DECK_PARENT}::")]
    print(f"\nDeck cũ sẽ xóa NẾU trống sau khi chuyển: {', '.join(old_decks) or '(không có)'}")

    if not args.apply:
        print("\n(DRY-RUN — chưa làm gì. Chạy lại với --apply để làm thật.)")
        return

    # --- Làm thật ---
    call("createDeck", deck=TOPIC_DECK_PARENT)
    for slug in TOPICS:
        call("createDeck", deck=f"{TOPIC_DECK_PARENT}::{slug}")
    print(f"✅ Đã tạo cây deck {TOPIC_DECK_PARENT} + {len(TOPICS)} deck con")

    for deck, cards in plan.items():
        if cards:
            call("changeDeck", cards=cards, deck=deck)
            print(f"✅ {deck}: đã nhận {len(cards)} thẻ")

    deleted, kept = [], []
    for d in old_decks:
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
