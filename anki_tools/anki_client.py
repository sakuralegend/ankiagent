# ==============================================================================
# --- CỬA DUY NHẤT tới AnkiConnect (L1): note/deck/tag/sync + vòng đời GĐ1→GĐ2.
# Ruột đã chia (03/08/2026, QD-18) — caller CỨ import anki_client như cũ,
# mặt tiền cuối file re-export đủ tên: dựng & đẩy thẻ ở anki_the.py · thiết lập
# model/template ở anki_moitruong.py · đếm thống kê ở anki_thongke.py.
# ==============================================================================
import json
from datetime import datetime, timedelta
import requests


from .config import ANKI_CONNECT_URL, MODEL_NAME, STAGE1_DECK, STAGE2_DECK, TOPIC_DECK_PARENT
from .topics import TOPIC_TAG_PREFIX, topic_tag, normalize_topic
from .utils import log_warn, log_fail


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


def get_root_decks():
    """Tên các deck GỐC (không có '::' trong tên) — mỗi cái là một kho riêng biệt,
    vd RUSSIAN (từ vựng) và GRAMMAR (ngữ pháp). Thống kê phải tách theo các kho này
    chứ không gộp chung, vì chúng khác hẳn nhau về mục đích lẫn nhịp học."""
    return sorted(n for n in get_deck_names() if "::" not in n)



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


# ==============================================================================
# --- MẶT TIỀN (QD-18): tên cũ giữ nguyên sau khi tách file — caller không đổi.
# Ba module con KHÔNG import ngược anki_client nên không có vòng.
# ==============================================================================
from .anki_the import (store_media_file, store_word_audio, build_card_fields,   # noqa: E402,F401
                       note_to_card_info, push_to_anki, print_card_summary)
from .anki_moitruong import setup_anki_environment                              # noqa: E402,F401
from .anki_thongke import (MATURE_IVL_DAYS, CARD_STATES,                        # noqa: E402,F401
                           get_card_state_stats, get_topic_stats)
