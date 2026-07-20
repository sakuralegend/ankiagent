# ==============================================================================
# --- QUẢN LÝ ANKI: kiểm tra sẵn sàng, kiểm tra trùng, tạo deck, tạo model,
# đẩy note lên, in tóm tắt thẻ ---
# ⚠️ push_to_anki() đọc các khóa dict do scraper.process_pure_next_data() trả
# về (word, english_meanings, part_of_speech, pos_full, gender,
# raw_dictionary_examples). Nếu đổi tên khóa ở scraper.py, PHẢI sửa lại đây.
# ==============================================================================
import base64
import json
import os
from datetime import datetime, timedelta
import requests


from .config import ANKI_CONNECT_URL, INBOX_DECK, MODEL_NAME, TOPIC_DECK_PARENT
from .topics import TOPICS, TOPIC_TAG_PREFIX, topic_tag, normalize_topic
from .utils import log_warn, log_fail, strip_accents_perfectly, hl_to_bracket
from .html_builder import build_examples_html
from .audio import fetch_audio_bytes

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
    """Xem từ đã có thẻ TỪ VỰNG chưa. Trả về list[dict]: note_id, word, deck,
    status_text, card_ids.

    ⚠️ BẮT BUỘC lọc note:"{MODEL_NAME}". Mảng thẻ ngữ pháp (model RU_Plural, deck
    GRAMMAR::) cũng có ô WordClean, và trùng từ với kho từ vựng là chuyện BÌNH
    THƯỜNG — дом vừa là thẻ từ vựng vừa là thẻ số nhiều bất quy tắc. Không lọc
    thì bot báo "đã có thẻ" rồi từ chối thêm từ vựng (user chốt 20/07/2026)."""
    try:
        query = f'note:"{MODEL_NAME}" WordClean:"{clean_word}"'
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


def get_known_words():
    """Tập hợp WordClean (chữ thường) của MỌI note model bot — luồng quét ảnh
    dùng để lọc từ đã có thẻ trước khi hỏi user.
    Trả về set[str] (có thể rỗng), hoặc None nếu AnkiConnect lỗi (None ≠ rỗng:
    lỗi thì KHÔNG được coi là 'chưa có từ nào' kẻo đề nghị thêm trùng cả kho)."""
    try:
        res = requests.post(ANKI_CONNECT_URL, json={
            "action": "findNotes", "version": 6,
            "params": {"query": f'note:"{MODEL_NAME}"'}
        }, timeout=15)
        note_ids = res.json().get("result") or []
        if not note_ids:
            return set()
        res = requests.post(ANKI_CONNECT_URL, json={
            "action": "notesInfo", "version": 6,
            "params": {"notes": note_ids}
        }, timeout=60)
        notes = res.json().get("result") or []
        words = {
            (n.get("fields", {}).get("WordClean", {}).get("value") or "").strip().lower()
            for n in notes
        }
        words.discard("")
        return words
    except Exception as e:
        log_warn(f"Không lấy được danh sách từ đã có: {e}")
        return None


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


def store_media_file(filename, data_bytes):
    """Lưu bytes vào thư mục media của Anki (base64). Trả về True nếu thành công."""
    b64 = base64.b64encode(data_bytes).decode("ascii")
    try:
        res = requests.post(ANKI_CONNECT_URL, json={
            "action": "storeMediaFile", "version": 6,
            "params": {"filename": filename, "data": b64}
        }, timeout=20)
        if res.json().get("error"):
            log_fail(f"storeMediaFile lỗi: {res.json().get('error')}")
            return False
        return True
    except Exception as e:
        log_fail(f"storeMediaFile lỗi mạng: {e}")
        return False


def store_word_audio(clean_word):
    """Tải audio phát âm (OpenRussian -> Google TTS dự phòng khi 500) rồi lưu vào
    Anki media. Trả về (audio_field, source): '[sound:ru_audio_X.mp3]' + nguồn
    ('openrussian'/'google_tts'), hoặc ('', '') nếu cả hai nguồn đều hụt."""
    data, source = fetch_audio_bytes(clean_word)
    if not data:
        return "", ""
    filename = f"ru_audio_{clean_word}.mp3"
    if store_media_file(filename, data):
        return f"[sound:{filename}]", source
    return "", ""


def build_card_fields(word, data):
    """Dựng field thẻ (TRỪ Audio/Image) + metadata từ dữ liệu cào được. Dùng CHUNG
    cho thêm thẻ mới (push_to_anki) và làm lại thẻ (pipeline.redo_note_id) để hai
    luồng luôn tạo ra thẻ giống hệt nhau. KHÔNG đụng AnkiConnect."""
    clean_word = strip_accents_perfectly(word)
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

    examples_html, vi_meaning, simplified_examples, topic_slug = build_examples_html(
        clean_word,
        data.get("raw_dictionary_examples", []),
        data.get("english_meanings", [])
    )

    fields = {
        "Word": data["word"], "WordClean": clean_word, "Meaning": meaning_html,
        "Vietnamese": vi_meaning, "PoS": pos_clean, "PoSFull": pos_full,
        "GenderBadge": gender_badge_html, "ExamplesHTML": examples_html,
        "RawExamples": json.dumps(data.get("raw_dictionary_examples", []), ensure_ascii=False),
    }

    # Thẻ "khuyết": AI thất bại -> không ví dụ, hoặc ví dụ thô thiếu tiếng Việt.
    ai_degraded = (not simplified_examples) or not any(
        (ex.get("vi") or ex.get("vietnamese") or "").strip() for ex in simplified_examples
    )

    return {
        "fields": fields,
        "clean_word": clean_word,
        "topic_slug": topic_slug,
        "simplified_examples": simplified_examples,
        "vi_meaning": vi_meaning,
        "gender_label": gender_label,
        "pos_full": pos_full,
        "en_meanings": data["english_meanings"],
        "ai_degraded": ai_degraded,
    }


def push_to_anki(word, data, deck_name, is_forced=False):
    """Đẩy note lên Anki. Trả về (success, card_info_dict) để hiển thị tóm tắt.

    deck_name=None -> chế độ TỰ ĐỘNG: thẻ vào INBOX_DECK để học gom một chỗ;
    tag topic:: (AI chọn) ghi sẵn deck chủ đề đích — thẻ tốt nghiệp learning
    thì move_graduated_from_inbox() chuyển về TOPIC_DECK_PARENT::<topic>.
    """
    built = build_card_fields(word, data)
    clean_word = built["clean_word"]
    topic_slug = built["topic_slug"]

    # Audio: bot TỰ tải (OpenRussian -> Google TTS nếu 500) rồi lưu media, thay vì
    # để AnkiConnect tự tải từ URL (không bắt được lỗi 500 để dùng phao dự phòng).
    audio_field, audio_source = store_word_audio(clean_word)

    # Th\u00eam tr\u00f9ng (force) d\u00f9ng option allowDuplicate ch\u00ednh th\u1ed1ng c\u1ee7a AnkiConnect.
    note_tags = [topic_tag(topic_slug)] if topic_slug else []

    # Chế độ tự động: thẻ mới vào inbox học trước; tag topic:: đã ghi deck đích.
    if not deck_name:
        deck_name = INBOX_DECK
        try:
            requests.post(ANKI_CONNECT_URL, json={
                "action": "createDeck", "version": 6, "params": {"deck": deck_name}
            }, timeout=5)
        except Exception as e:
            log_warn(f"Không tạo/kiểm tra được deck '{deck_name}': {e}")

    fields = dict(built["fields"])
    fields["Image"] = ""
    fields["Audio"] = audio_field

    payload = {
        "action": "addNote", "version": 6,
        "params": {
            "note": {
                "deckName": deck_name, "modelName": MODEL_NAME,
                "fields": fields,
                "options": {"allowDuplicate": is_forced},
                "tags": note_tags,
            }
        }
    }

    card_info = {
        "word": data["word"],
        "clean_word": clean_word,
        "en_meanings": built["en_meanings"],
        "vi_meaning": built["vi_meaning"],
        "pos": built["pos_full"],
        "gender": built["gender_label"],
        "deck": deck_name,
        "is_forced": is_forced,
        "simplified_examples": built["simplified_examples"],
        "ai_degraded": built["ai_degraded"],
        "topic": topic_tag(topic_slug) if topic_slug else "",
        "audio_source": audio_source,   # "openrussian" / "google_tts" / ""
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


def move_graduated_from_inbox():
    """Chuyển thẻ trong INBOX_DECK đã TỐT NGHIỆP learning (thành thẻ review,
    is:review — gồm cả thẻ lỡ lapse) về deck chủ đề theo tag topic:: của note.
    changeDeck không đụng scheduling nên lịch ôn giữ nguyên tuyệt đối.
    Trả về (moved: dict slug->số thẻ đã chuyển, tổng số) hoặc (None, 0) nếu lỗi.
    Chạy bởi job đêm của bot + lệnh /don. Idempotent: inbox sạch thì trả ({}, 0)."""
    def _call(action, **params):
        res = requests.post(ANKI_CONNECT_URL, json={
            "action": action, "version": 6, "params": params
        }, timeout=60)
        out = res.json()
        if out.get("error"):
            raise RuntimeError(f"{action}: {out['error']}")
        return out["result"]

    try:
        card_ids = _call("findCards", query=f'deck:"{INBOX_DECK}" is:review')
        if not card_ids:
            return {}, 0
        cards = _call("cardsInfo", cards=card_ids)
        note_ids = sorted({c["note"] for c in cards if isinstance(c, dict) and c.get("note")})
        notes = _call("notesInfo", notes=note_ids)
        note_slug = {}
        for n in notes:
            topic_tags = [t for t in n.get("tags", []) if t.startswith("topic::")]
            if topic_tags:
                note_slug[n["noteId"]] = normalize_topic(topic_tags[0])
        plan = {}  # slug -> [card_ids] (thẻ không có tag topic:: thì để yên trong inbox)
        for c in cards:
            slug = note_slug.get(c.get("note"))
            if slug:
                plan.setdefault(slug, []).append(c["cardId"])
        moved = {}
        for slug, cids in sorted(plan.items()):
            deck = f"{TOPIC_DECK_PARENT}::{slug}"
            _call("createDeck", deck=deck)
            _call("changeDeck", cards=cids, deck=deck)
            moved[slug] = len(cids)
        return moved, sum(moved.values())
    except Exception as e:
        log_warn(f"Không dọn được inbox: {e}")
        return None, 0


def get_topic_stats():
    """Đếm thẻ theo từng chủ đề topic:: (cho lệnh /thongke của bot).
    Đọc tag của TỪNG note rồi đếm phía Python — KHÔNG query tag:"topic::X" từng
    chủ đề, vì Anki coi tag cha khớp cả tag con (cây lồng cấp sẽ bị đếm đúp).
    Tag tên cũ (LEGACY_ALIASES) được quy về slug mới.
    Trả về (stats: dict slug->số thẻ, untagged: số note chưa có tag topic::)
    hoặc (None, 0) nếu AnkiConnect lỗi."""
    try:
        res = requests.post(ANKI_CONNECT_URL, json={
            "action": "findNotes", "version": 6,
            "params": {"query": f'note:"{MODEL_NAME}"'}
        }, timeout=15)
        note_ids = res.json().get("result") or []
        res_info = requests.post(ANKI_CONNECT_URL, json={
            "action": "notesInfo", "version": 6, "params": {"notes": note_ids}
        }, timeout=60)
        notes = res_info.json().get("result") or []

        stats = {slug: 0 for slug in TOPICS}
        untagged = 0
        for n in notes:
            tags = [t for t in n.get("tags", []) if t.startswith("topic::")]
            if not tags:
                untagged += 1
                continue
            slug = normalize_topic(tags[0])
            stats[slug] = stats.get(slug, 0) + len(n.get("cards", []))
        return stats, untagged
    except Exception as e:
        log_warn(f"Không đếm được thống kê chủ đề: {e}")
        return None, 0


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


def get_note_full(note_id):
    """Đọc note đầy đủ: {'fields': {name: value}, 'tags': [..]} hoặc None.
    Dùng cho luồng LÀM LẠI thẻ (/sua) cần cả field lẫn tag để làm mới topic."""
    try:
        res = requests.post(ANKI_CONNECT_URL, json={
            "action": "notesInfo", "version": 6,
            "params": {"notes": [note_id]}
        }, timeout=5)
        infos = res.json().get("result", [])
        if not infos:
            return None
        info = infos[0]
        return {
            "fields": {k: v.get("value", "") for k, v in info.get("fields", {}).items()},
            "tags": info.get("tags", []),
        }
    except Exception as e:
        log_warn(f"Không đọc được note {note_id}: {e}")
        return None


def update_note_fields(note_id, fields):
    """Ghi đè các field cho sẵn vào note (giữ nguyên field không truyền -> Image,
    và Audio nếu không truyền). Dùng cho luồng LÀM LẠI thẻ. True nếu thành công."""
    try:
        res = requests.post(ANKI_CONNECT_URL, json={
            "action": "updateNoteFields", "version": 6,
            "params": {"note": {"id": note_id, "fields": fields}}
        }, timeout=15)
        result = res.json()
        if result.get("error"):
            log_fail(f"Cập nhật note thất bại: {result.get('error')}")
            return False
        return True
    except Exception as e:
        log_fail(f"Lỗi cập nhật note: {e}")
        return False


def set_topic_tag(note_id, current_tags, new_slug):
    """Làm mới tag chủ đề của note: bỏ mọi tag topic:: cũ, gắn topic::<new_slug>.
    new_slug None (nhánh fallback không AI) -> chỉ gỡ tag cũ. True nếu không lỗi."""
    new_tag = topic_tag(new_slug) if new_slug else None
    old_topic_tags = [t for t in current_tags if t.startswith(TOPIC_TAG_PREFIX)]
    to_remove = [t for t in old_topic_tags if t != new_tag]
    ok = True
    try:
        if to_remove:
            res = requests.post(ANKI_CONNECT_URL, json={
                "action": "removeTags", "version": 6,
                "params": {"notes": [note_id], "tags": " ".join(to_remove)}
            }, timeout=10)
            ok = ok and not res.json().get("error")
        if new_tag and new_tag not in current_tags:
            res = requests.post(ANKI_CONNECT_URL, json={
                "action": "addTags", "version": 6,
                "params": {"notes": [note_id], "tags": new_tag}
            }, timeout=10)
            ok = ok and not res.json().get("error")
    except Exception as e:
        log_warn(f"Không cập nhật được tag chủ đề note {note_id}: {e}")
        return False
    return ok


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
    _audio_src = card_info.get("audio_source", "")
    if _audio_src == "google_tts":
        print(f"  🔊 Audio:      [Google TTS - OpenRussian lỗi]")
    elif _audio_src == "openrussian":
        print(f"  🔊 Audio:      [OpenRussian]")
    else:
        print(f"  🔊 Audio:      [KHÔNG có - cả 2 nguồn đều hụt]")

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
