# ==============================================================================
# --- ĐƯA TỪ TIẾNG NGA VỀ DẠNG TỪ ĐIỂN (LEMMA) — OFFLINE, TẤT ĐỊNH ---
# Vì sao có file này (user chốt 21/07/2026): Gemini ĐỌC ảnh rất tốt nhưng phần
# "đưa về nguyên thể" thì thỉnh thoảng trượt (trả về проверяем thay vì проверять,
# дети thay vì ребёнок) -> OpenRussian không có từ đó -> thẻ không thêm được.
# Đó KHÔNG phải việc nên đoán: tiếng Nga có từ điển hình thái đầy đủ.
#
# pymorphy3 (từ điển OpenCorpora) chạy hẳn trên VPS, không mạng, không hạn mức,
# ~vài chục nghìn từ/giây. Đã đo thật trước khi chọn: 27/27 ca khó đều đúng
# (дети→ребёнок, проверяем→проверять, люди→человек, шёл→идти, лучше→хороший...).
#
# PHÂN VAI rạch ròi — mỗi bên làm đúng thứ mình giỏi:
#   • Gemini  : ĐỌC chữ trên ảnh + hiểu NGỮ CẢNH câu (biết стали trong câu này là
#               'сталь' hay 'стать' — pymorphy3 nhìn 1 từ trơ trọi thì chịu).
#   • pymorphy3: TRỌNG TÀI hình thái — từ này có thật không, dạng từ điển của nó
#               là gì. Chỉ lật kèo Gemini khi Gemini đưa ra thứ KHÔNG PHẢI lemma.
# Thiếu pymorphy3 (chưa pip install) thì mọi hàm trả None/rỗng và hệ thống chạy
# y như trước — KHÔNG được làm bot chết vì một thư viện phụ trợ.
# ==============================================================================
import threading

from .utils import log_warn

_MORPH = None
_MORPH_TRIED = False
_INIT_LOCK = threading.Lock()


def _analyzer():
    """MorphAnalyzer dùng chung (nạp từ điển ~1s, tốn ~50MB RAM nên chỉ nạp 1 lần).
    Trả về None nếu chưa cài pymorphy3 — mọi hàm dưới đây tự lùi về 'không biết'."""
    global _MORPH, _MORPH_TRIED
    if _MORPH is not None or _MORPH_TRIED:
        return _MORPH
    with _INIT_LOCK:
        if _MORPH is not None or _MORPH_TRIED:
            return _MORPH
        _MORPH_TRIED = True
        try:
            import pymorphy3
            _MORPH = pymorphy3.MorphAnalyzer()
        except Exception as e:
            log_warn(
                f"Không nạp được pymorphy3 ({e}) — bot vẫn chạy nhưng việc đưa từ về "
                "nguyên thể sẽ chỉ dựa vào AI. Cài lại: pip install -r requirements.txt"
            )
            _MORPH = None
    return _MORPH


def morph_ready():
    """Có dùng được pymorphy3 không (để bot báo trạng thái lúc khởi động)."""
    return _analyzer() is not None


def _yo_key(word):
    """Khóa so sánh bỏ qua khác biệt ё/е — OpenCorpora ghi 'ребёнок', nhiều sách và
    cả AI hay viết 'ребенок'. Hai cách viết đó là MỘT TỪ, đừng coi là bất đồng."""
    return (word or "").strip().lower().replace("ё", "е")


def possible_lemmas(word):
    """MỌI dạng từ điển mà `word` có thể quy về, xếp theo xác suất giảm dần.
    Chỉ tính các phân tích CÓ TRONG TỪ ĐIỂN (is_known): từ gõ sai cũng được
    pymorphy3 'đoán liều' theo đuôi (компютер -> компютереть) và những phỏng đoán
    kiểu đó tuyệt đối không được phép ghi đè câu trả lời của AI.
    Trả về [] nếu chưa cài pymorphy3 hoặc từ không có trong từ điển."""
    morph = _analyzer()
    if not morph or not word:
        return []
    out = []
    try:
        for p in morph.parse(word):
            if p.is_known and p.normal_form not in out:
                out.append(p.normal_form)
    except Exception as e:
        log_warn(f"pymorphy3 lỗi khi phân tích '{word}': {e}")
        return []
    return out


def guess_lemma_offline(word):
    """Dạng từ điển KHẢ DĨ NHẤT của `word`, hoặc None nếu không chắc.

    None có nghĩa "tôi không biết từ này" (gõ sai chính tả, tên riêng, từ ngoài
    từ điển) — lúc đó phải để AI xử lý, vì AI đoán được ý định người gõ."""
    lemmas = possible_lemmas(word)
    return lemmas[0] if lemmas else None


def reconcile_lemma(seen, ai_lemma):
    """TRỌNG TÀI giữa câu trả lời của AI và từ điển hình thái.

    seen     : dạng chữ đúng như nhìn thấy trên ảnh (проверяем)
    ai_lemma : dạng từ điển do AI đưa ra (có thể đã đúng, có thể chưa)

    Trả về (lemma, fixed): fixed=True nghĩa là pymorphy3 đã LẬT câu trả lời của AI.

    Bốn luật, xếp theo thứ tự:
    1. Từ điển không biết `seen` -> giữ nguyên AI (typo/tên riêng: AI giỏi hơn hẳn).
    2. Từ điển xếp CHÍNH `seen` là lemma khả dĩ NHẤT -> giữ nguyên `seen`, không cho
       "chia" sâu thêm. Đây là luật chống AI lemmatize QUÁ TAY, thêm 21/07/2026 sau
       ca thật: AI đổi 'это' (this is) thành 'этот' (this) vì đúng luật "đại từ ->
       cách 1 giống đực" trong prompt. Cả loạt từ chức năng dính chung bẫy này —
       это, всё, что, как, надо, нужно, ничего, уже... — chúng vừa là dạng biến
       cách của từ khác, vừa là mục từ điển đứng riêng (OpenRussian có đủ), và bản
       thân chúng mới là thứ người học gặp trên sách.
       ⚠️ Đánh đổi đã cân nhắc: từ đồng âm kiểu 'мой' (của tôi / rửa đi!) sẽ bị giữ
       nguyên dù AI đọc được ngữ cảnh, vì từ điển xếp nghĩa "của tôi" phổ biến hơn
       hẳn. Chấp nhận được: bot đánh dấu 🔧 và user duyệt danh sách trước khi thêm.
    3. Đáp án của AI nằm trong danh sách lemma hợp lệ của `seen` -> GIỮ AI, kể cả
       khi nó không phải phương án xác suất cao nhất. Đây là chỗ ngữ cảnh câu của
       AI thắng: 'стали' trong 'из стали' là сталь chứ không phải стать.
    4. Còn lại (AI trả về thứ không phải lemma của từ đó: проверяем, дети) -> lấy
       lemma xác suất cao nhất của từ điển."""
    seen = (seen or "").strip().lower()
    ai_lemma = (ai_lemma or "").strip().lower()
    lemmas = possible_lemmas(seen)
    if not lemmas:
        return ai_lemma or seen, False
    if _yo_key(lemmas[0]) == _yo_key(seen):
        return seen, bool(ai_lemma) and _yo_key(ai_lemma) != _yo_key(seen)
    if ai_lemma and _yo_key(ai_lemma) in {_yo_key(l) for l in lemmas}:
        return ai_lemma, False
    return lemmas[0], bool(ai_lemma) and _yo_key(ai_lemma) != _yo_key(lemmas[0])
