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
import re
from datetime import datetime, timedelta
import requests


from . import grammar
from .config import ANKI_CONNECT_URL, MODEL_NAME, STAGE1_DECK, STAGE2_DECK, TOPIC_DECK_PARENT
from .topics import TOPICS, TOPIC_TAG_PREFIX, topic_tag, normalize_topic
from .utils import log_warn, log_fail, strip_accents_perfectly, hl_to_bracket
from .html_builder import (
    build_examples_html,
    parse_examples_html,
    parse_gender_badge,
    parse_aspect_badge,
    parse_meaning_html,
    parse_raw_examples,
)
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
            fields = {k: v.get("value", "") for k, v in n.get("fields", {}).items()}
            duplicates.append({
                "note_id": n.get("noteId"),
                "word": fields.get("Word", ""),
                "deck": deck,
                "status_text": status_text,
                "card_ids": note_card_ids,
                # fields + tags để bot hiện LẠI TOÀN BỘ nội dung thẻ cũ (tra từ điển),
                # khỏi phải gọi notesInfo lần nữa — dữ liệu đã nằm sẵn trong tay.
                "fields": fields,
                "tags": n.get("tags", []),
            })
        return duplicates
    except Exception as e:
        log_warn(f"Không thể kiểm tra trùng lặp: {e}")
        return []


def doc_grammar_json_tat_ca():
    """Đọc ô `GrammarJSON` của MỌI thẻ -> `{WordClean: bản_ghi}`.

    🔴 THẺ LÀ NGUỒN DUY NHẤT của dữ liệu ngữ pháp (QD-11, thay QD-08 — không còn
    file cache dự phòng trên đĩa). Thẻ TỰ ĐỒNG BỘ qua AnkiWeb tới mọi máy, nên
    bot trên VPS và laptop luôn thấy cùng một dữ liệu.

    🔴 KHÔNG tự nuốt lỗi kết nối — NÉM THẲNG lên cho `grammar._lap_dem_tu_the()`
    kêu to rồi dừng. Trước đây hàm này trả `{}` khi Anki đóng/lỗi để dùng đỡ file
    cache trên đĩa; giờ không còn file đó, im lặng ở đây là mất trắng dữ liệu."""
    res = requests.post(ANKI_CONNECT_URL, json={
        "action": "findNotes", "version": 6,
        "params": {"query": f'note:"{MODEL_NAME}"'}
    }, timeout=15)
    note_ids = res.json().get("result") or []
    if not note_ids:
        return {}
    res = requests.post(ANKI_CONNECT_URL, json={
        "action": "notesInfo", "version": 6, "params": {"notes": note_ids}
    }, timeout=120)
    ra = {}
    for n in res.json().get("result") or []:
        f = n.get("fields", {})
        wc = (f.get("WordClean", {}).get("value") or "").strip()
        gj = (f.get("GrammarJSON", {}).get("value") or "").strip()
        if not wc or not gj:
            continue
        try:
            rec = json.loads(gj)
        except ValueError:
            continue                       # ô hỏng -> bỏ qua, đừng làm chết cả lượt
        if rec:
            ra[wc] = rec
    return ra


def ghi_grammar_json(word_clean, rec):
    """Ghi thẳng một bản ghi ngữ pháp vào ô `GrammarJSON` của thẻ khớp
    `word_clean` — cửa DUY NHẤT của `grammar.remember()`/`fetch_grammar()` để
    persist dữ liệu (QD-11, không còn file cache dự phòng).

    Thẻ CHƯA tồn tại (đang tạo mới, `build_card_fields()` gọi trước khi
    `addNote`) thì đây là chuyện BÌNH THƯỜNG — trả `False`, không phải lỗi;
    người gọi tự đưa `rec` vào field lúc tạo note. LỖI KẾT NỐI thì NÉM THẲNG để
    nơi gọi kêu to, vì im lặng ở đây là ghi hụt dữ liệu vĩnh viễn."""
    res = requests.post(ANKI_CONNECT_URL, json={
        "action": "findNotes", "version": 6,
        "params": {"query": f'note:"{MODEL_NAME}" WordClean:"{word_clean}"'}
    }, timeout=15)
    note_ids = res.json().get("result") or []
    if not note_ids:
        return False
    payload = json.dumps(rec, ensure_ascii=False, separators=(",", ":")) if rec else ""
    for nid in note_ids:
        res = requests.post(ANKI_CONNECT_URL, json={
            "action": "updateNoteFields", "version": 6,
            "params": {"note": {"id": nid, "fields": {"GrammarJSON": payload}}}
        }, timeout=15)
        err = res.json().get("error")
        if err:
            raise RuntimeError(f"updateNoteFields (note {nid}) that bai: {err}")
    return True


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
                    # HuongDan: phân tích chẻ gốc + cách nhớ + họ hàng, do Opus 5 soạn
                    #   ĐỊNH KỲ THEO LÔ (không sinh lúc tạo thẻ) — push_to_anki không ghi
                    #   field này nên thẻ mới để trống, soạn bù sau.
                    #   (Tên cũ "Mnemonic" đã đổi 27/07/2026: hướng mnemonic bị bỏ, để
                    #   tên cũ chỉ gây nhầm. Đổi tên field KHÔNG phải schema mod — đã đo,
                    #   sync bình thường — vì số lượng và thứ tự field không đổi.)
                    # Stage: giai đoạn học. RỖNG = GĐ1 làm quen (không ô gõ),
                    #   "type" = GĐ2 gõ. Template chọn mặt thẻ theo field này —
                    #   khối điều kiện của Anki không đọc được tên deck nên bắt
                    #   buộc phải có field. Thẻ mới để trống = vào thẳng GĐ1.
                    # (Field "Image" đã bỏ 26/07/2026: 0/870 note từng dùng tới.)
                    # AspectBadge: thể động từ (HOÀN THÀNH / CHƯA HOÀN THÀNH) —
                    #   thêm 29/07/2026. Để RIÊNG một field chứ không nhét chung
                    #   vào GenderBadge: user chốt "làm hẳn 1 field mới cho dễ bảo
                    #   trì". Danh từ/tính từ để trống -> khối điều kiện trong
                    #   template làm badge biến mất, không có ô rỗng lơ lửng.
                    # ReflexiveBadge: động từ phản thân (-ся) — thêm 29/07/2026
                    #   cùng đợt với AspectBadge. Nó gỡ chỗ badge thể KHÔNG cứu
                    #   được: `учи́ть`/`учи́ться` cùng `v`, cùng chưa hoàn thành.
                    # GrammarJSON: TOÀN BỘ dữ liệu ngữ pháp cào được, dạng JSON,
                    #   ẨN (không template nào hiện). Cùng khuôn với `RawExamples`
                    #   vốn đã lưu JSON câu gốc. User chốt 29/07: *"cào rồi đặt
                    #   vào một field nào đó trong thẻ, để sau này muốn lấy để xử
                    #   lí cũng dễ"* — trước đó dữ liệu chỉ nằm ở
                    #   `data/grammar_cache.json` trên laptop nên bot trên VPS
                    #   không với tới. Để trong thẻ thì nó tự sync đi khắp nơi và
                    #   thẻ trở thành tự chứa, không phụ thuộc file ngoài.
                    #   Đo thật: 0,8 MB cho 950 thẻ (trung bình 888 B, to nhất 6 KB).
                    "inOrderFields": ["Word", "WordClean", "Meaning", "Vietnamese", "PoS", "PoSFull", "GenderBadge", "AspectBadge", "ReflexiveBadge", "ExamplesHTML", "RawExamples", "GrammarJSON", "Audio", "HuongDan", "Stage"],
                    "css": shared_css, "cardTemplates": [{"Name": "Pure Engine Typing Card v25", "Front": front_template, "Back": back_template}]
                }
            }, timeout=5)
            if res_create.json().get("error"):
                print(f"\n❌ Tạo model thất bại: {res_create.json().get('error')}")
            else:
                print("✅", end=" ")
        else:
            print("✅", end=" ")
            # Model ĐÃ CÓ SẴN thì `createModel` ở trên không chạy, nên field mới
            # phải thêm riêng. Bọc trong `if thiếu` để chạy lại nhiều lần vẫn yên:
            # `modelFieldAdd` gọi lần hai sẽ báo lỗi trùng tên.
            # 🔴 Thêm field LÀ schema mod -> Anki đòi full sync một lần. Đã nói
            # trước với user (29/07). Sau khi sync phải kiểm `journalctl` trên VPS:
            # mọi schema mod đều làm VPS kẹt "Sync status 2" mà KHÔNG báo Telegram.
            res_f = requests.post(ANKI_CONNECT_URL, json={
                "action": "modelFieldNames", "version": 6,
                "params": {"modelName": MODEL_NAME}}, timeout=5)
            dang_co = res_f.json().get("result") or []
            for ten, vi_tri in (("AspectBadge", 7), ("ReflexiveBadge", 8),
                                ("GrammarJSON", 11)):
                if ten in dang_co:
                    continue
                res_add = requests.post(ANKI_CONNECT_URL, json={
                    "action": "modelFieldAdd", "version": 6,
                    "params": {"modelName": MODEL_NAME, "fieldName": ten,
                               "index": vi_tri}}, timeout=10)
                if res_add.json().get("error"):
                    print(f"\n❌ Thêm field {ten} thất bại: {res_add.json().get('error')}")
                else:
                    print(f"\n🆕 Đã thêm field {ten} — Anki sẽ đòi FULL SYNC một lần.")

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

    # Ba badge ngữ pháp. Dựng qua grammar.* để thẻ MỚI và thẻ CŨ (scripts/backfill_badge.py)
    # luôn ra cùng một thứ — nhãn giống nay chỉ còn MỘT bảng, ở grammar.NHAN_GIONG.
    grammar_rec = data.get("grammar") or {}
    if grammar_rec:
        # ghi vào cache ngay: từ user thêm hằng ngày tự có mặt, không phải chạy
        # `cao_nguphap.py --anki` bù về sau
        grammar.remember(clean_word, grammar_rec)
    gender_badge_html = (grammar.gender_badge_html(clean_word, gender_lower, grammar_rec)
                         if pos_clean in ("n", "noun") else "")
    aspect_badge_html = grammar.aspect_badge_html(data.get("aspect", ""))
    reflexive_badge_html = grammar.reflexive_badge_html(data.get("reflexive"))
    gender_label = re.sub(r"<[^>]+>", "", gender_badge_html)

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
        "GenderBadge": gender_badge_html, "AspectBadge": aspect_badge_html,
        "ReflexiveBadge": reflexive_badge_html, "ExamplesHTML": examples_html,
        "RawExamples": json.dumps(data.get("raw_dictionary_examples", []), ensure_ascii=False),
        # separators gọn: field này thuần máy đọc, không ai mở ra ngắm.
        "GrammarJSON": (json.dumps(grammar_rec, ensure_ascii=False,
                                   separators=(",", ":")) if grammar_rec else ""),
        # BẢNG CHIA có ngay từ lúc tạo thẻ. Nó thuần dữ liệu cào được nên không
        # có lý do gì bắt user đợi tới lượt lô của từ đó mới có bảng tra cứu.
        # Phần chữ (chẻ từ / cách nhớ / họ hàng) vẫn do lô soạn sau; lúc đó
        # `nap` gọi gan_bang() gỡ bảng này ra rồi nối lại bảng mới -> không đội.
        "HuongDan": grammar.build_table(grammar_rec),
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
        "aspect_label": grammar.NHAN_THE.get(
            (data.get("aspect") or "").strip().lower(), ("", ""))[1],
        "reflexive_label": grammar.NHAN_PHAN_THAN if data.get("reflexive") else "",
        "pos_full": pos_full,
        "en_meanings": data["english_meanings"],
        "ai_degraded": ai_degraded,
    }


def note_to_card_info(dup):
    """Hàm NGHỊCH của build_card_fields(): note đã nằm trong Anki -> dict card_info
    ĐÚNG KHUÔN mà push_to_anki() trả về. Nhờ vậy bot hiện thẻ CŨ (tra từ điển) bằng
    đúng bộ khung hiển thị của thẻ MỚI, không phải viết hai kiểu trình bày.

    dup: 1 phần tử find_duplicate_notes() trả về (đã có sẵn fields + tags).
    Các khóa THÊM so với card_info gốc (thẻ mới chưa có): note_id, status_text,
    has_audio, image, raw_count."""
    fields = dup.get("fields") or {}
    en_meanings = parse_meaning_html(fields.get("Meaning", ""))
    topic_tags = [t for t in (dup.get("tags") or []) if t.startswith(TOPIC_TAG_PREFIX)]
    audio = fields.get("Audio", "")
    examples = parse_examples_html(fields.get("ExamplesHTML", ""))
    # Cùng định nghĩa "thẻ khuyết" như build_card_fields() -> thẻ cũ hỏng cũng
    # được cảnh báo + mời bấm nút làm lại ngay trong bảng tra từ điển.
    ai_degraded = (not examples) or not any((ex.get("vi") or "").strip() for ex in examples)
    return {
        "word": fields.get("Word", "") or dup.get("word", ""),
        "clean_word": fields.get("WordClean", ""),
        "en_meanings": en_meanings or ["(thẻ không có nghĩa tiếng Anh)"],
        "vi_meaning": fields.get("Vietnamese", "").strip(),
        "pos": fields.get("PoSFull", "") or fields.get("PoS", ""),
        "gender": parse_gender_badge(fields.get("GenderBadge", "")),
        "aspect": parse_aspect_badge(fields.get("AspectBadge", "")),
        "reflexive": parse_aspect_badge(fields.get("ReflexiveBadge", "")),
        "deck": dup.get("deck", "?"),
        "is_forced": False,
        "simplified_examples": examples,
        "ai_degraded": ai_degraded,
        "topic": topic_tags[0] if topic_tags else "",
        # Thẻ CŨ không lưu lại nguồn audio, chỉ biết có tiếng hay không
        "audio_source": "",
        "has_audio": bool(re.search(r"\[sound:[^\]]+\]", audio)),
        "image": fields.get("Image", "").strip(),
        "raw_count": len(parse_raw_examples(fields.get("RawExamples", ""))),
        "note_id": dup.get("note_id"),
        "status_text": dup.get("status_text", ""),
    }


def push_to_anki(word, data, deck_name, is_forced=False):
    """Đẩy note lên Anki. Trả về (success, card_info_dict) để hiển thị tóm tắt.

    deck_name=None -> chế độ TỰ ĐỘNG: thẻ vào STAGE1_DECK (giai đoạn LÀM QUEN);
    tag topic:: (AI chọn) ghi sẵn deck chủ đề đích. Thẻ đi tiếp theo lộ trình
    hai giai đoạn do run_don() điều khiển: 0-quen -> 1-go -> <kho>::<topic>.
    Field Stage để TRỐNG (không ghi) nên thẻ mới luôn bắt đầu ở GĐ1.
    """
    built = build_card_fields(word, data)
    clean_word = built["clean_word"]
    topic_slug = built["topic_slug"]

    # Audio: bot TỰ tải (OpenRussian -> Google TTS nếu 500) rồi lưu media, thay vì
    # để AnkiConnect tự tải từ URL (không bắt được lỗi 500 để dùng phao dự phòng).
    audio_field, audio_source = store_word_audio(clean_word)

    # Th\u00eam tr\u00f9ng (force) d\u00f9ng option allowDuplicate ch\u00ednh th\u1ed1ng c\u1ee7a AnkiConnect.
    note_tags = [topic_tag(topic_slug)] if topic_slug else []

    # Chế độ tự động: thẻ mới vào deck LÀM QUEN; tag topic:: đã ghi deck đích.
    if not deck_name:
        deck_name = STAGE1_DECK
        try:
            requests.post(ANKI_CONNECT_URL, json={
                "action": "createDeck", "version": 6, "params": {"deck": deck_name}
            }, timeout=5)
        except Exception as e:
            log_warn(f"Không tạo/kiểm tra được deck '{deck_name}': {e}")

    fields = dict(built["fields"])
    fields["Audio"] = audio_field
    # KHÔNG ghi "Stage": để trống nghĩa là thẻ bắt đầu ở GĐ1 (làm quen).
    # KHÔNG còn "Image": field đã bị xoá khỏi note type 26/07/2026 — ghi vào một
    # field không tồn tại thì AnkiConnect từ chối cả note.

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
        "aspect": built["aspect_label"],
        "reflexive": built["reflexive_label"],
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


def _ac(action, timeout=60, **params):
    """Gọi AnkiConnect, NÉM lỗi thay vì nuốt — người gọi tự bắt và báo cáo."""
    res = requests.post(ANKI_CONNECT_URL, json={
        "action": action, "version": 6, "params": params
    }, timeout=timeout)
    out = res.json()
    if out.get("error"):
        raise RuntimeError(f"{action}: {out['error']}")
    return out["result"]


def promote_stage1_to_stage2():
    """GĐ1 -> GĐ2: thẻ trong STAGE1_DECK đã RỜI LEARNING (is:review, tức ~2 lượt
    Good trong ~15 phút) thì coi như "đã làm quen xong":
        1. Stage = "type"     -> template đổi sang mặt gõ
        2. forgetCards        -> thành THẺ MỚI TINH, chạy lại learning steps
        3. changeDeck -> STAGE2_DECK

    ⚠️ Ba việc phải đi CÙNG NHAU. Lệch deck với field là thẻ hiện sai mặt (nằm ở
    deck gõ mà mặt trước vẫn là thẻ làm quen, hoặc ngược lại).

    forgetCards là CỐ Ý chứ không phải tiện tay: user muốn GĐ2 là một thẻ mới
    hoàn toàn, và nó cũng xoá luôn D tích luỹ ở GĐ1 (Good không kéo D xuống —
    đã đo 0/84 thẻ tự hồi phục, chỉ Forget mới cứu được).

    Chỉ lọc theo deck GỐC là chưa đủ nếu sau này user dựng lại deck lọc: Anki
    khớp `deck:X` cho cả thẻ đang bị kéo vào deck lọc. Nên loại luôn thẻ đang
    nằm ở deck khác với deck gốc.

    Trả về số thẻ đã đẩy sang GĐ2. Idempotent: không có gì thì trả 0."""
    card_ids = _ac("findCards", query=f'deck:"{STAGE1_DECK}" is:review -is:suspended')
    if not card_ids:
        return 0
    cards = _ac("cardsInfo", timeout=120, cards=card_ids)
    # deckName là deck ĐANG chứa thẻ; khác STAGE1_DECK nghĩa là thẻ đang bị kéo
    # vào một deck lọc -> bỏ qua, đừng forgetCards phá lịch của nó.
    at_home = [c for c in cards
               if isinstance(c, dict) and c.get("deckName") == STAGE1_DECK]
    if not at_home:
        return 0
    return thang_cap_gd2([c["cardId"] for c in at_home],
                         sorted({c["note"] for c in at_home if c.get("note")}))


def thang_cap_gd2(card_ids, note_ids):
    """BA BƯỚC THĂNG CẤP GĐ1 -> GĐ2, tách riêng vì có HAI người gọi.

    🔴 Đây là bản DUY NHẤT của ba bước này. `promote_stage1_to_stage2()` gọi nó
    (đường thường lệ, mỗi đêm 3h), và `soat_giaidoan.py` cũng gọi nó khi vá thẻ
    bị đồng bộ đá ngược về GĐ1 (QD-17). Cố ý KHÔNG để cửa canh tự dựng ba bước
    riêng: hai bản sao của cùng một luật thì sớm muộn sẽ lệch nhau ÂM THẦM —
    đúng bệnh đã đẻ ra 10 wrapper AnkiConnect và giết `CHANGELOG.md`.

    Ba bước PHẢI đi cùng nhau; lệch deck với field là thẻ hiện sai mặt.
    `forgetCards` là MỤC ĐÍCH chứ không phải tác dụng phụ — xem docstring của
    `promote_stage1_to_stage2()`.

    Trả về số thẻ đã đẩy. Idempotent: danh sách rỗng thì trả 0, không gọi gì."""
    if not card_ids:
        return 0
    for nid in note_ids:
        _ac("updateNoteFields", note={"id": nid, "fields": {"Stage": "type"}})
    _ac("forgetCards", timeout=120, cards=card_ids)
    _ac("createDeck", deck=STAGE2_DECK)
    _ac("changeDeck", timeout=120, cards=card_ids, deck=STAGE2_DECK)
    return len(card_ids)


def move_graduated_from_inbox():
    """GĐ2 -> kho: thẻ trong STAGE2_DECK đã TỐT NGHIỆP learning (is:review — gồm
    cả thẻ lỡ lapse) về deck chủ đề theo tag topic:: của note.
    changeDeck không đụng scheduling nên lịch ôn giữ nguyên tuyệt đối.
    Trả về (moved: dict slug->số thẻ đã chuyển, tổng số) hoặc (None, 0) nếu lỗi.
    Idempotent: deck sạch thì trả ({}, 0)."""
    def _call(action, **params):
        return _ac(action, **params)

    try:
        card_ids = _call("findCards", query=f'deck:"{STAGE2_DECK}" is:review')
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


# --- Đếm thẻ theo TRẠNG THÁI HỌC (bản Telegram của màn "Card Counts" trong Anki) ---
# Mốc 21 ngày là hằng số của chính Anki để tách thẻ "trẻ" khỏi thẻ "trưởng thành".
MATURE_IVL_DAYS = 21

# Thẻ TẠM NGƯNG/TẠM ẨN phải được tách ra TRƯỚC rồi phần còn lại mới chia theo trạng
# thái học — đúng thứ tự Anki làm, nhờ vậy các nhóm không chồng lấn nhau.
_ACTIVE = "-is:suspended -is:buried"

# (slug, nhãn hiển thị, truy vấn Anki). Thứ tự này cũng là thứ tự hiện trong báo cáo:
# đi theo vòng đời một tấm thẻ — mới -> đang học -> trẻ -> trưởng thành.
CARD_STATES = [
    ("new", "🆕 Mới (chưa học)", f"is:new {_ACTIVE}"),
    ("learning", "📖 Đang học", f"is:learn {_ACTIVE}"),
    ("young", f"🌱 Trẻ (dưới {MATURE_IVL_DAYS} ngày)",
     f"is:review prop:ivl<{MATURE_IVL_DAYS} {_ACTIVE}"),
    ("mature", f"🌳 Trưởng thành (từ {MATURE_IVL_DAYS} ngày)",
     f"is:review prop:ivl>={MATURE_IVL_DAYS} {_ACTIVE}"),
    ("suspended", "⏸ Tạm ngưng", "is:suspended"),
    ("buried", "🫥 Tạm ẩn", f"is:buried -is:suspended"),
]


def get_card_state_stats(deck=None):
    """Đếm thẻ theo trạng thái học, chia nhóm y như màn "Card Counts" của Anki.
    deck=None -> cả collection; deck="RUSSIAN" -> deck đó và mọi deck con của nó.
    Trả về (counts: dict slug->số thẻ, total) hoặc (None, 0) nếu AnkiConnect lỗi.

    Lọc theo DECK chứ không theo model (user chốt 22/07/2026: "đừng lẫn 2 deck lớn
    vào nhau"). Lọc theo model thì mảng ngữ pháp GRAMMAR:: — vốn dùng model RU_Plural
    riêng — sẽ biến mất khỏi báo cáo mà không ai hay.

    CỐ Ý đếm bằng findCards (chỉ trả về danh sách id) thay vì cardsInfo: cardsInfo
    kèm theo cả HTML mặt trước/sau ĐÃ DỰNG của từng thẻ — với ~700 thẻ là vài MB
    tải về chỉ để đọc hai con số queue/type.

    Nhóm "Đang học" gộp cả thẻ học lại (lapse). Anki tách riêng Relearning, nhưng đã
    đo trên chính collection này: `is:learn` và `is:review` KHÔNG giao nhau nên không
    có cách tách bằng truy vấn — mà bốn nhóm chính mới là thứ cần nhìn hằng ngày."""
    # Thoát dấu " trong tên deck y như get_deck_note_ids() — tên deck do user đặt
    safe_deck = (deck or "").replace('"', '\\"')
    scope = f'deck:"{safe_deck}"' if deck else ""

    def count(query):
        res = requests.post(ANKI_CONNECT_URL, json={
            "action": "findCards", "version": 6,
            "params": {"query": f"{scope} {query}".strip()}
        }, timeout=20)
        out = res.json()
        if out.get("error"):
            raise RuntimeError(out["error"])
        return len(out.get("result") or [])

    try:
        counts = {slug: count(query) for slug, _, query in CARD_STATES}
        total = count("")
    except Exception as e:
        log_warn(f"Không đếm được trạng thái thẻ của deck '{deck or 'toàn bộ'}': {e}")
        return None, 0
    return counts, total


def get_root_decks():
    """Tên các deck GỐC (không có '::' trong tên) — mỗi cái là một kho riêng biệt,
    vd RUSSIAN (từ vựng) và GRAMMAR (ngữ pháp). Thống kê phải tách theo các kho này
    chứ không gộp chung, vì chúng khác hẳn nhau về mục đích lẫn nhịp học."""
    return sorted(n for n in get_deck_names() if "::" not in n)


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


def sync_now():
    """Sync với AnkiWeb. Trả về (ok: bool, err: str) — err rỗng khi thành công.

    Dùng bản này khi cần BIẾT LÝ DO hỏng để cảnh báo cho ra hồn. Lý do quan trọng
    nhất là "Sync status 2" = AnkiWeb đòi full sync (thường do vừa đổi schema:
    thêm/xoá field, đổi note type). Lúc đó sync sẽ hỏng MÃI MÃI cho tới khi có
    người vào bấm tay — đúng cái đã làm VPS kẹt im lặng suốt 2 ngày (25-26/07)."""
    try:
        res = requests.post(ANKI_CONNECT_URL, json={"action": "sync", "version": 6}, timeout=60)
        result = res.json()
        if result.get("error"):
            err = str(result["error"])
            log_warn(f"Sync AnkiWeb lỗi: {err}")
            return False, err
        return True, ""
    except Exception as e:
        log_warn(f"Không gọi được sync: {e}")
        return False, str(e)


def trigger_sync():
    """Yêu cầu Anki sync với AnkiWeb (đẩy thẻ mới lên để điện thoại kéo về).
    Trả về True nếu lệnh được chấp nhận. Không chặn quá lâu: sync chạy nền trong Anki."""
    return sync_now()[0]


def sync_truoc_khi_ghi_lo(ten_viec="ghi lô"):
    """🔴 GỌI TRƯỚC MỌI ĐỢT GHI HÀNG LOẠT LÊN NOTE. Trả True nếu được phép ghi.

    Bẫy đã trả học phí 31/07/2026 — 23 thẻ hỏng IM LẶNG: script trên laptop ghi lại
    976 note lúc 12:40, trong khi laptop CHƯA kéo về đợt dọn 03:00 của bot trên VPS.
    Ghi vào note làm `mod` của nó mới hơn, mà sync của Anki xử xung đột theo "ai sửa
    sau thắng, thắng TRỌN note" ⇒ bản laptop (Stage rỗng) đè bản VPS (Stage="type")
    ⇒ 23 thẻ vừa được thăng lên GĐ2 nằm ở deck gõ mà hiện mặt làm quen. Đổi deck
    KHÔNG bị vì đó là thay đổi trên THẺ, script chỉ đụng NOTE.

    Kéo về trước rồi mới ghi thì bản ghi đè lên đúng bản mới nhất, không mất gì."""
    ok, err = sync_now()
    if not ok:
        log_fail(f"{ten_viec}: KHÔNG kéo được AnkiWeb về ({err}). DỪNG, chưa ghi gì — "
                 f"ghi lúc này là ghi đè lên bản chép cũ, thay đổi từ máy khác "
                 f"(bot trên VPS, điện thoại) sẽ bị nuốt im lặng.")
    return ok


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
    phu = [x for x in (gender, card_info.get("aspect")) if x]
    print(f"  🏷️  Từ loại:    {pos}" + (f" ({', '.join(phu)})" if phu else ""))
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
