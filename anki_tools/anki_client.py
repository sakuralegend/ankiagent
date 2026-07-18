# ==============================================================================
# --- QUẢN LÝ ANKI: kiểm tra sẵn sàng, kiểm tra trùng, tạo deck, tạo model,
# đẩy note lên, in tóm tắt thẻ ---
# ⚠️ push_to_anki() đọc các khóa dict do scraper.process_pure_next_data() trả
# về (word, english_meanings, part_of_speech, pos_full, gender,
# raw_dictionary_examples). Nếu đổi tên khóa ở scraper.py, PHẢI sửa lại đây.
# ==============================================================================
import json
import os
import urllib.parse
from datetime import datetime, timedelta
import requests


from .config import ANKI_CONNECT_URL, MODEL_NAME, OPENRUSSIAN_AUDIO_TEMPLATE, TOPIC_DECK_PARENT
from .topics import topic_tag, normalize_topic
from .utils import log_warn, log_fail, strip_accents_perfectly, hl_to_bracket
from .html_builder import build_examples_html

_TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")


def check_anki_ready():
    """Kiểm tra AnkiConnect đã sẵn sàng chưa (không tự mở Anki)."""
    try:
        resp = requests.get(ANKI_CONNECT_URL, timeout=3)
        return resp.status_code == 200
    except Exception:
        return False


def _card_status_text(card):
    """Dịch trạng thái 1 thẻ Anki (dict trả về từ cardsInfo) sang tiếng Việt dễ hiểu."""
    queue = card.get("queue")
    ctype = card.get("type")
    interval = card.get("interval", 0)
    mod_ts = card.get("mod")

    if queue == -1:
        return "⏸️ Đã tạm ngưng (suspended)"
    if ctype == 0 or queue == 0:
        return "🆕 Mới (chưa học)"
    if queue in (1, 3):
        # Đang học / học lại (learning, relearning) - due thường tính bằng giây (epoch) hoặc số thứ tự
        return "📖 Đang học (learning)"
    if ctype == 2 or queue == 2:
        # Review: ước tính ngày due = lần ôn gần nhất (mod) + interval (ngày).
        # AnkiConnect không trả về ngày tạo collection (crt) nên đây là ước tính gần đúng.
        try:
            due_date = datetime.fromtimestamp(mod_ts) + timedelta(days=interval)
            due_str = due_date.strftime("%d/%m/%Y")
        except Exception:
            due_str = "?"
        return f"🔁 Đang ôn tập (interval {interval} ngày), ước tính đến hạn: {due_str}"
    return f"❓ Không rõ (queue={queue}, type={ctype})"


def find_duplicate_notes(clean_word):
    """Quét toàn bộ collection Anki xem từ đã tồn tại chưa.
    Trả về list[dict]: mỗi dict có note_id, word, deck, status_text, card_ids."""
    try:
        query = f'WordClean:"{clean_word}"'
        res = requests.post(ANKI_CONNECT_URL, json={
            "action": "findNotes", "version": 6,
            "params": {"query": query}
        }, timeout=5)
        result = res.json()
        if result.get("error"):
            log_warn(f"AnkiConnect lỗi khi kiểm tra trùng: {result.get('error')}")
            return []
        note_ids = result.get("result", [])
        if not note_ids:
            return []

        res_notes = requests.post(ANKI_CONNECT_URL, json={
            "action": "notesInfo", "version": 6,
            "params": {"notes": note_ids}
        }, timeout=5)
        notes_info = res_notes.json().get("result", [])

        all_card_ids = []
        for n in notes_info:
            all_card_ids.extend(n.get("cards", []))

        cards_by_id = {}
        if all_card_ids:
            res_cards = requests.post(ANKI_CONNECT_URL, json={
                "action": "cardsInfo", "version": 6,
                "params": {"cards": all_card_ids}
            }, timeout=5)
            for c in res_cards.json().get("result", []):
                cards_by_id[c["cardId"]] = c

        duplicates = []
        for n in notes_info:
            note_card_ids = n.get("cards", [])
            deck = "?"
            status_text = "❓ Không rõ"
            if note_card_ids:
                first_card = cards_by_id.get(note_card_ids[0])
                if first_card:
                    deck = first_card.get("deckName", "?")
                    status_text = _card_status_text(first_card)
            word_field = n.get("fields", {}).get("Word", {}).get("value", "")
            duplicates.append({
                "note_id": n.get("noteId"),
                "word": word_field,
                "deck": deck,
                "status_text": status_text,
                "card_ids": note_card_ids,
            })
        return duplicates
    except Exception as e:
        log_warn(f"Không thể kiểm tra trùng lặp: {e}")
        return []


def change_note_deck(card_ids, deck_name):
    """Chuyển các card_ids sang deck_name. Trả về True nếu thành công."""
    try:
        res = requests.post(ANKI_CONNECT_URL, json={
            "action": "changeDeck", "version": 6,
            "params": {"cards": card_ids, "deck": deck_name}
        }, timeout=5)
        result = res.json()
        if result.get("error"):
            log_fail(f"Không thể chuyển deck: {result.get('error')}")
            return False
        return True
    except Exception as e:
        log_fail(f"Lỗi chuyển deck: {e}")
        return False


def delete_notes(note_ids):
    """Xóa các note theo note_ids. Trả về True nếu thành công."""
    try:
        res = requests.post(ANKI_CONNECT_URL, json={
            "action": "deleteNotes", "version": 6,
            "params": {"notes": note_ids}
        }, timeout=5)
        result = res.json()
        if result.get("error"):
            log_fail(f"Không thể xóa note: {result.get('error')}")
            return False
        return True
    except Exception as e:
        log_fail(f"Lỗi xóa note: {e}")
        return False



def get_deck_names():
    """Lấy danh sách tên toàn bộ deck trong collection (cho bảng chọn deck của bot)."""
    try:
        res = requests.post(ANKI_CONNECT_URL, json={"action": "deckNames", "version": 6}, timeout=5)
        return res.json().get("result", []) or []
    except Exception as e:
        log_warn(f"Không lấy được danh sách deck: {e}")
        return []


def get_deck_note_ids(deck_name):
    """Lấy note_id của TOÀN BỘ note (model của bot) trong 1 deck, gồm cả subdeck.
    Dùng cho luồng /suadeck (sửa hàng loạt). Trả về list note_ids ([] nếu lỗi/trống)."""
    try:
        safe_deck = deck_name.replace('"', '\\"')
        query = f'deck:"{safe_deck}" note:"{MODEL_NAME}"'
        res = requests.post(ANKI_CONNECT_URL, json={
            "action": "findNotes", "version": 6,
            "params": {"query": query}
        }, timeout=10)
        result = res.json()
        if result.get("error"):
            log_warn(f"AnkiConnect lỗi khi liệt kê thẻ deck '{deck_name}': {result.get('error')}")
            return []
        return result.get("result", []) or []
    except Exception as e:
        log_warn(f"Không liệt kê được thẻ của deck '{deck_name}': {e}")
        return []


def ensure_deck_exists(deck_name):
    """Kiểm tra deck đã tồn tại chưa, tạo mới nếu chưa có. Trả về True nếu OK."""
    try:
        res_names = requests.post(ANKI_CONNECT_URL, json={"action": "deckNames", "version": 6}, timeout=5)
        existing_decks = res_names.json().get("result", [])
        if deck_name in existing_decks:
            print(f"📚 Bộ bài: '{deck_name}' (đã có sẵn)")
            return True
        res_c = requests.post(ANKI_CONNECT_URL, json={"action": "createDeck", "version": 6, "params": {"deck": deck_name}}, timeout=5)
        if res_c.json().get("error"):
            log_fail(f"Không thể tạo bộ bài: {res_c.json().get('error')}")
            return False
        print(f"📚 Đã tạo bộ bài mới: '{deck_name}'")
        return True
    except Exception as e:
        log_fail(f"Lỗi kiểm tra/tạo bộ bài: {e}")
        return False


def _read_template(filename):
    with open(os.path.join(_TEMPLATES_DIR, filename), "r", encoding="utf-8") as f:
        return f.read()


def setup_anki_environment():
    # Từ khi gỡ nút AI Refine khỏi thẻ, back_template.html là HTML tĩnh thuần,
    # không còn placeholder nào cần tiêm (API key không còn bị nhúng vào thẻ).
    shared_css = _read_template("card.css")
    front_template = _read_template("front_template.html")
    back_template = _read_template("back_template.html")

    print("--- ⚙️ Thiết lập môi trường Anki...", end=" ", flush=True)
    try:
        res = requests.post(ANKI_CONNECT_URL, json={"action": "modelNames", "version": 6}, timeout=5)
        existing_models = res.json().get("result", [])

        if MODEL_NAME not in existing_models:
            res_create = requests.post(ANKI_CONNECT_URL, json={
                "action": "createModel", "version": 6,
                "params": {
                    "modelName": MODEL_NAME,
                    "inOrderFields": ["Word", "WordClean", "Meaning", "Vietnamese", "PoS", "PoSFull", "GenderBadge", "ExamplesHTML", "Image", "RawExamples", "Audio"],
                    "css": shared_css, "cardTemplates": [{"Name": "Pure Engine Typing Card v25", "Front": front_template, "Back": back_template}]
                }
            }, timeout=5)
            if res_create.json().get("error"):
                print(f"\n❌ Tạo model thất bại: {res_create.json().get('error')}")
            else:
                print("✅", end=" ")
        else:
            print("✅", end=" ")

        res_style = requests.post(ANKI_CONNECT_URL, json={"action": "updateModelStyling", "version": 6, "params": {"model": {"name": MODEL_NAME, "css": shared_css}}}, timeout=5)
        if res_style.json().get("error"):
            print(f"\n❌ CSS thất bại: {res_style.json().get('error')}")

        res_tmpl = requests.post(ANKI_CONNECT_URL, json={"action": "updateModelTemplates", "version": 6, "params": {
            "model": {"name": MODEL_NAME, "templates": {"Pure Engine Typing Card v25": {"Front": front_template, "Back": back_template}}}
        }}, timeout=5)
        if res_tmpl.json().get("error"):
            print(f"\n❌ Templates thất bại: {res_tmpl.json().get('error')}")

        print("Hoàn tất. ---")
    except Exception as e:
        print(f"\n❌ Không kết nối được AnkiConnect: {e}")


def push_to_anki(word, data, deck_name, is_forced=False):
    """Đẩy note lên Anki. Trả về (success, card_info_dict) để hiển thị tóm tắt.

    deck_name=None -> chế độ TỰ ĐỘNG: thẻ vào deck con theo chủ đề AI chọn
    (TOPIC_DECK_PARENT::<topic>, vd Русский::food; AI không chọn được -> ::other).
    """
    clean_word = strip_accents_perfectly(word)
    audio_url = OPENRUSSIAN_AUDIO_TEMPLATE.format(word=urllib.parse.quote(clean_word))
    audio_filename = f"ru_audio_{clean_word}.mp3"

    pos_clean = data["part_of_speech"].lower().strip()
    pos_full = data["pos_full"]
    gender_lower = str(data["gender"]).lower().strip()

    gender_label = ""
    if pos_clean in ["n", "noun"] and gender_lower != "none":
        if gender_lower in ["m", "masculine"]: gender_label = "Masculine ♂"
        elif gender_lower in ["f", "feminine"]: gender_label = "Feminine ♀"
        elif gender_lower in ["n", "neuter"]: gender_label = "Neuter ⚧"
        elif gender_lower in ["pl", "plural"]: gender_label = "Plural 👥"

    gender_badge_html = f'<div class="badge {gender_lower}">{gender_label}</div>' if gender_label else ""

    meaning_html = '<ol class="meaning-list">'
    for m in data["english_meanings"]: meaning_html += f"<li>{m}</li>"
    meaning_html += "</ol>"

    # Th\u00eam tr\u00f9ng (force): d\u00f9ng option allowDuplicate ch\u00ednh th\u1ed1ng c\u1ee7a AnkiConnect.
    # (M\u00e1nh c\u0169 g\u1eafn k\u00fd t\u1ef1 v\u00f4 h\u00ecnh \u200b v\u00e0o Word \u0111\u00e3 b\u1ecb Anki >= 25.x t\u1ef1 x\u00f3a khi
    # l\u01b0u note -> v\u1eabn b\u1ecb ch\u1eb7n tr\u00f9ng, n\u00ean b\u1ecf.)
    word_field_value = data["word"]

    examples_html, vi_meaning, simplified_examples, topic_slug = build_examples_html(
        clean_word,
        data.get("raw_dictionary_examples", []),
        data.get("english_meanings", [])
    )

    # Tag chủ đề (topic::food, topic::animals...) do AI chọn trong CÙNG request
    # sinh ví dụ. Nhánh fallback không AI -> không có topic, gắn bù sau bằng
    # `python tag_topics.py --missing`.
    # (Tag kỹ thuật OpenRussian_*_v25 cũ đã bỏ 16/07/2026: không code nào tra
    # theo nó — nhận diện thẻ của bot luôn đi qua model name.)
    note_tags = [topic_tag(topic_slug)] if topic_slug else []

    # Chế độ tự động: deck đích chỉ biết được SAU khi AI chọn topic -> tính ở đây.
    # createDeck idempotent (deck có rồi thì thôi), gọi thẳng để không in log mỗi thẻ.
    if not deck_name:
        deck_name = f"{TOPIC_DECK_PARENT}::{normalize_topic(topic_slug)}"
        try:
            requests.post(ANKI_CONNECT_URL, json={
                "action": "createDeck", "version": 6, "params": {"deck": deck_name}
            }, timeout=5)
        except Exception as e:
            log_warn(f"Không tạo/kiểm tra được deck '{deck_name}': {e}")

    payload = {
        "action": "addNote", "version": 6,
        "params": {
            "note": {
                "deckName": deck_name, "modelName": MODEL_NAME,
                "fields": {
                    "Word": word_field_value, "WordClean": clean_word, "Meaning": meaning_html,
                    "Vietnamese": vi_meaning, "PoS": pos_clean, "PoSFull": pos_full,
                    "GenderBadge": gender_badge_html, "ExamplesHTML": examples_html, "Image": "",
                    "RawExamples": json.dumps(data.get("raw_dictionary_examples", []), ensure_ascii=False)
                },
                "options": {"allowDuplicate": is_forced},
                "tags": note_tags,
                "audio": [{"url": audio_url, "filename": audio_filename, "fields": ["Audio"]}]
            }
        }
    }

    # Thẻ "khuyết": AI thất bại hoàn toàn -> không có ví dụ, hoặc chỉ còn ví dụ
    # thô không có tiếng Việt. Bot dựa vào cờ này để CẢNH BÁO thay vì im lặng.
    ai_degraded = (not simplified_examples) or not any(
        (ex.get("vi") or ex.get("vietnamese") or "").strip() for ex in simplified_examples
    )

    card_info = {
        "word": data["word"],
        "clean_word": clean_word,
        "en_meanings": data["english_meanings"],
        "vi_meaning": vi_meaning,
        "pos": pos_full,
        "gender": gender_label,
        "deck": deck_name,
        "is_forced": is_forced,
        "simplified_examples": simplified_examples,
        "ai_degraded": ai_degraded,
        "topic": topic_tag(topic_slug) if topic_slug else "",
    }

    try:
        res = requests.post(ANKI_CONNECT_URL, json=payload, timeout=10)
        result = res.json()
        if result.get("error"):
            log_fail(f"AnkiConnect từ chối thêm note: {result.get('error')}")
            card_info["error"] = str(result.get("error"))
            return False, card_info
        return True, card_info
    except Exception as e:
        log_fail(f"Không kết nối được AnkiConnect: {e}")
        card_info["error"] = str(e)
        return False, card_info


def trigger_sync():
    """Yêu cầu Anki sync với AnkiWeb (đẩy thẻ mới lên để điện thoại kéo về).
    Trả về True nếu lệnh được chấp nhận. Không chặn quá lâu: sync chạy nền trong Anki."""
    try:
        res = requests.post(ANKI_CONNECT_URL, json={"action": "sync", "version": 6}, timeout=60)
        result = res.json()
        if result.get("error"):
            log_warn(f"Sync AnkiWeb lỗi: {result.get('error')}")
            return False
        return True
    except Exception as e:
        log_warn(f"Không gọi được sync: {e}")
        return False


def get_note_fields(note_id):
    """Lấy fields hiện tại của 1 note (dùng cho luồng sửa thẻ /sua).
    Trả về dict {field_name: value} hoặc None."""
    try:
        res = requests.post(ANKI_CONNECT_URL, json={
            "action": "notesInfo", "version": 6,
            "params": {"notes": [note_id]}
        }, timeout=5)
        infos = res.json().get("result", [])
        if not infos:
            return None
        return {k: v.get("value", "") for k, v in infos[0].get("fields", {}).items()}
    except Exception as e:
        log_warn(f"Không đọc được note {note_id}: {e}")
        return None


def update_note_refined(note_id, vi_meaning, examples_html):
    """Ghi đè nghĩa tiếng Việt + khối ví dụ mới vào note (luồng sửa thẻ /sua).
    Trả về True nếu thành công."""
    try:
        res = requests.post(ANKI_CONNECT_URL, json={
            "action": "updateNoteFields", "version": 6,
            "params": {"note": {"id": note_id, "fields": {
                "Vietnamese": vi_meaning,
                "ExamplesHTML": examples_html,
            }}}
        }, timeout=10)
        result = res.json()
        if result.get("error"):
            log_fail(f"Cập nhật note thất bại: {result.get('error')}")
            return False
        return True
    except Exception as e:
        log_fail(f"Lỗi cập nhật note: {e}")
        return False


def print_card_summary(card_info, elapsed):
    """In tóm tắt thẻ vừa tạo - đơn giản, không bảng kẻ."""
    w = hl_to_bracket(card_info["word"])
    vi = card_info["vi_meaning"]
    en = ", ".join(card_info["en_meanings"])
    pos = card_info["pos"]
    gender = card_info["gender"]
    deck = card_info["deck"]
    forced = " ⚠️ FORCE" if card_info["is_forced"] else ""
    examples = card_info.get("simplified_examples", [])

    print(f"\n  ═══ 📇 THẺ MỚI{forced}: {w} ═══")
    print(f"  🇷🇺 Từ:         {w}")
    print(f"  🇬🇧 Nghĩa:      {en}")
    print(f"  🇻🇳 Tiếng Việt:  {vi}")
    if gender:
        print(f"  🏷️  Từ loại:    {pos} ({gender})")
    else:
        print(f"  🏷️  Từ loại:    {pos}")
    if card_info.get("topic"):
        print(f"  📂 Chủ đề:     {card_info['topic']}")
    print(f"  🔊 Audio:      [đã đính kèm]")

    if examples:
        print(f"  ─────────────────────────────────────")
        for i, ex in enumerate(examples[:3]):
            ru = hl_to_bracket(ex.get("ru", ""))
            en_ex = hl_to_bracket(ex.get("en", ""))
            vi_ex = hl_to_bracket(ex.get("vi") or ex.get("vietnamese") or "")
            print(f"  💡 Ví dụ {i+1}:")
            print(f"     RU: {ru}")
            print(f"     EN: {en_ex}")
            if vi_ex:
                print(f"     VI: {vi_ex}")

    if card_info.get("ai_degraded"):
        print(f"  ⚠️  AI không tạo được ví dụ/nghĩa Việt - thẻ THIẾU nội dung, nên sửa lại sau.")

    print(f"  ─────────────────────────────────────")
    print(f"  📦 Bộ bài: {deck} │ ⏱️ {elapsed:.1f}s\n")
