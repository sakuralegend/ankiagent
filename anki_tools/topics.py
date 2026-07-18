# ==============================================================================
# --- ĐỊNH NGHĨA 17 CHỦ ĐỀ TỪ VỰNG (tag topic::...) ---
# Đây là NGUỒN CHÂN LÝ DUY NHẤT về danh sách chủ đề:
# - ai_client.py nhét danh sách này vào prompt để AI chọn topic khi tạo thẻ mới
# - tag_topics.py (script gắn tag hàng loạt) cũng đọc từ đây
# Muốn thêm/bớt/đổi tên chủ đề: sửa TOPICS ở đây là đủ (tag cũ trong Anki
# không tự đổi theo — phải đổi tay trong Anki Browser nếu đã gắn).
# ==============================================================================

TOPIC_TAG_PREFIX = "topic::"

# slug -> mô tả ngắn (tiếng Anh, dùng trong prompt AI; kèm ví dụ để AI chọn chuẩn)
TOPICS = {
    "people-family": "people & family: family members, relationships, groups of people (мама, брат, друг, народ)",
    "professions": "professions & occupations (врач, студент, продавец)",
    "body": "body parts & body conditions (рука, глаз, сыпь)",
    "food": "food & drink: dishes, ingredients, meals, eating/drinking verbs, taste adjectives (хлеб, пить, вкусный)",
    "home-objects": "house & household: rooms, furniture, appliances, everyday objects at home (дом, стол, лампа, телефон)",
    "clothing": "clothes, footwear, accessories, fabric (платье, сапог, ткань)",
    "animals": "animals, birds, fish, insects (кот, рыба, муха)",
    "nature-plants": "nature & plants: landscape, sky, water, trees, flowers (лес, море, дерево, солнце)",
    "weather": "weather & temperature, incl. weather adjectives/adverbs (дождь, мороз, холодный, жарко)",
    "time": "time: hours, days of week, months, seasons, time adjectives/adverbs (час, январь, зима, вчера, ранний)",
    "numbers": "numbers, quantities, units of measure (пять, цифра, метр, килограмм)",
    "colors": "colors (красный, цвет)",
    "places-city": "places & city: buildings, institutions, countries, cities, transport, roads (школа, Москва, автобус, улица)",
    "education": "education & written word: school supplies, books, press, reading/writing/studying verbs (книга, урок, читать, газета)",
    "actions": "general action verbs not covered by other topics (делать, жить, идти)",
    "qualities": "descriptive ADJECTIVES and ADVERBS only, not covered by other topics (новый, быстрый, хорошо)",
    "function-words": "grammar/function words: pronouns, particles, conjunctions, prepositions, question words, modal predicatives (я, кто, да, или, можно, здесь)",
    "abstract": "abstract nouns: feelings, concepts, events, relations (правда, счастье, работа, помощь)",
    "other": "fallback when nothing above fits: misc concrete nouns, money, sports, media (деньги, спорт, фото)",
}


def normalize_topic(value):
    """Chuẩn hóa giá trị topic AI trả về -> slug hợp lệ trong TOPICS.
    Chấp nhận cả dạng có prefix 'topic::'. Sai/thiếu -> 'other'."""
    if not isinstance(value, str):
        return "other"
    slug = value.strip().lower()
    if slug.startswith(TOPIC_TAG_PREFIX):
        slug = slug[len(TOPIC_TAG_PREFIX):]
    return slug if slug in TOPICS else "other"


def topic_tag(slug):
    """slug -> tag Anki đầy đủ, vd 'food' -> 'topic::food'."""
    return f"{TOPIC_TAG_PREFIX}{normalize_topic(slug)}"


def topics_prompt_block():
    """Danh sách chủ đề dạng text để nhét vào system prompt của AI."""
    lines = [f"- {slug}: {desc}" for slug, desc in TOPICS.items()]
    return "\n".join(lines)
