# ==============================================================================
# --- ĐỊNH NGHĨA CHỦ ĐỀ TỪ VỰNG (tag topic::...) — CÂY 2 TẦNG, 10 GỐC ---
# Đây là NGUỒN CHÂN LÝ DUY NHẤT về danh sách chủ đề:
# - ai_client.py nhét danh sách này vào prompt để AI chọn topic khi tạo thẻ mới
# - scripts/tag_topics.py (gắn/sửa tag hàng loạt) và scripts/build_subdecks.py (dựng cây deck)
#   cũng đọc từ đây
#
# THIẾT KẾ (chốt với user 18/07/2026):
# - TẦNG GỐC CỐ ĐỊNH 10 MIỀN, KHÔNG BAO GIỜ THÊM: people, life, nature, places,
#   language, time, numbers, actions, qualities, concepts.
# - Mỗi tầng tối đa 10 mục. Khi /thongke cảnh báo (nhánh ≥100 thẻ) -> chỉ THÊM
#   NHÁNH CON dạng "cha::con" (vd "actions::motion"), tuyệt đối không thêm gốc.
# - Slug có thể là gốc trực tiếp ("time") hoặc nhánh ("life::food"). Tag Anki =
#   "topic::" + slug; deck Anki = TOPIC_DECK_PARENT + "::" + slug. Cả tag lẫn
#   deck đều phân cấp bằng "::" nên cây tự rẽ nhánh, thẻ luôn chỉ có 1 tag.
# - Đổi tên/tách slug: thêm dòng vào LEGACY_ALIASES rồi chạy
#   `python scripts/tag_topics.py --fix --apply` + `python scripts/build_subdecks.py --apply`.
# ==============================================================================

TOPIC_TAG_PREFIX = "topic::"

# slug -> mô tả ngắn (tiếng Anh, dùng trong prompt AI; kèm ví dụ để AI chọn chuẩn)
TOPICS = {
    # ── people: con người ──
    "people::family": "family members, relationships, groups of people (мама, брат, друг, народ)",
    "people::professions": "professions & occupations (врач, студент, продавец)",
    "people::body": "body parts & body conditions (рука, глаз, сыпь)",
    # ── life: đời sống hằng ngày ──
    "life::food": "food & drink: dishes, ingredients, meals, eating/drinking verbs, taste adjectives (хлеб, пить, вкусный)",
    "life::home": "house & household: rooms, furniture, appliances, everyday objects at home (дом, стол, лампа, телефон)",
    "life::clothing": "clothes, footwear, accessories, fabric (платье, сапог, ткань)",
    # ── nature: thiên nhiên ──
    "nature::animals": "animals, birds, fish, insects (кот, рыба, муха)",
    "nature::plants": "nature & plants: landscape, sky, water, trees, flowers (лес, море, дерево, солнце)",
    "nature::weather": "weather & temperature, incl. weather adjectives/adverbs (дождь, мороз, холодный, жарко)",
    # ── places: địa điểm, di chuyển ──
    "places::city": "places & city: buildings, institutions, countries, cities, transport, roads (школа, Москва, автобус, улица)",
    # ── language: ngôn ngữ & học tập ──
    "language::education": "education & written word: school supplies, books, press, reading/writing/studying verbs (книга, урок, читать, газета)",
    "language::grammar": "grammar/function words: pronouns, particles, conjunctions, prepositions, question words, modal predicatives (я, кто, да, или, можно, здесь)",
    # ── các gốc hiện là lá (sẽ rẽ nhánh sau khi phình) ──
    "time": "time: hours, days of week, months, seasons, time adjectives/adverbs (час, январь, зима, вчера, ранний)",
    "numbers": "numbers, quantities, units of measure (пять, цифра, метр, килограмм)",
    "actions": "general action verbs not covered by other topics (делать, жить, идти)",
    "qualities": "descriptive ADJECTIVES and ADVERBS only, not covered by other topics (новый, быстрый, хорошо)",
    "qualities::colors": "colors (красный, цвет)",
    # ── concepts: khái niệm & phần dư ──
    "concepts::abstract": "abstract nouns: feelings, concepts, events, relations (правда, счастье, работа, помощь)",
    "concepts::misc": "fallback when nothing above fits: misc concrete nouns, money, sports, media (деньги, спорт, фото)",
}

# Slug mặc định khi AI trả sai/thiếu hoặc không xếp được vào đâu
FALLBACK_TOPIC = "concepts::misc"

# Tên slug CŨ -> MỚI. Dùng khi đổi tên/tách chủ đề: scripts/tag_topics.py --fix dựa vào
# đây để dịch tag cũ trên thẻ (kể cả thẻ do AI phân loại) sang tên mới;
# normalize_topic() cũng dùng để "đỡ" nếu AI lỡ trả tên cũ.
LEGACY_ALIASES = {
    # đợt chuyển cây phẳng 19 chủ đề -> cây 2 tầng 10 gốc (18/07/2026)
    "people-family": "people::family",
    "professions": "people::professions",
    "body": "people::body",
    "food": "life::food",
    "home-objects": "life::home",
    "clothing": "life::clothing",
    "animals": "nature::animals",
    "nature-plants": "nature::plants",
    "weather": "nature::weather",
    "places-city": "places::city",
    "education": "language::education",
    "function-words": "language::grammar",
    "colors": "qualities::colors",
    "abstract": "concepts::abstract",
    "other": "concepts::misc",
}


def normalize_topic(value):
    """Chuẩn hóa giá trị topic AI trả về -> slug hợp lệ trong TOPICS.
    Chấp nhận cả dạng có prefix 'topic::' lẫn tên cũ trong LEGACY_ALIASES.
    Sai/thiếu -> FALLBACK_TOPIC."""
    if not isinstance(value, str):
        return FALLBACK_TOPIC
    slug = value.strip().lower()
    if slug.startswith(TOPIC_TAG_PREFIX):
        slug = slug[len(TOPIC_TAG_PREFIX):]
    slug = LEGACY_ALIASES.get(slug, slug)
    return slug if slug in TOPICS else FALLBACK_TOPIC


def topic_tag(slug):
    """slug -> tag Anki đầy đủ, vd 'life::food' -> 'topic::life::food'."""
    return f"{TOPIC_TAG_PREFIX}{normalize_topic(slug)}"


def topics_prompt_block():
    """Danh sách chủ đề dạng text để nhét vào system prompt của AI."""
    lines = [f"- {slug}: {desc}" for slug, desc in TOPICS.items()]
    return "\n".join(lines)
