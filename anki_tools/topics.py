# ==============================================================================
# --- HAI DANH SÁCH AI DÙNG ĐỂ XẾP MỘT TỪ: CHỦ ĐỀ (`TOPICS`) và TỪ LOẠI (`TU_LOAI`) ---
# Cùng một file vì cùng một vai: đây là chỗ khai "được phép trả về những giá trị
# nào", và cả hai đều được `ai_client` nhét thẳng vào prompt. Tách đôi thì
# `ai_client` phải import hai file để làm đúng một việc.
#
# --- PHẦN 1: CHỦ ĐỀ TỪ VỰNG (tag topic::...) — CÂY 2 TẦNG, 10 GỐC ---
# Đây là NGUỒN CHÂN LÝ DUY NHẤT về danh sách chủ đề:
# - ai_client.py nhét danh sách này vào prompt để AI chọn topic khi tạo thẻ mới
# - scripts/tag_topics.py (gắn/sửa tag hàng loạt) và scripts/build_subdecks.py (dựng cây deck)
#   cũng đọc từ đây
#
# THIẾT KẾ (chốt với user 18/07/2026, giữ nguyên qua đợt 23/08/2026):
# - TẦNG GỐC CỐ ĐỊNH 10 MIỀN, KHÔNG BAO GIỜ THÊM: people, life, nature, places,
#   language, time, numbers, actions, qualities, concepts.
# - Mỗi tầng tối đa 10 mục (gốc dày nhất hiện nay là `life`, 7 nhánh).
# - Slug có thể là gốc trực tiếp ("time") hoặc nhánh ("life::food"). Tag Anki =
#   "topic::" + slug; deck Anki = TOPIC_DECK_PARENT + "::" + slug.
# - Đổi tên/tách slug: thêm dòng vào LEGACY_ALIASES rồi chạy
#   `python scripts/tag_topics.py --fix --apply` + `python scripts/build_subdecks.py --apply`.
#
# 🔴 ĐỢT 23/08/2026 — vì sao bảng này bị viết lại (QD-37):
# Bảng cũ 19 chủ đề do AI tự nghĩ mô tả. Đo độ tinh khiết (đối chiếu chuẩn ТРКИ,
# xem `data/rosedu_muc.json`): `concepts::abstract` 19% · `concepts::misc` 28% ·
# `people::family` 30% · `places::city` 33% — bốn rọ ôm 335/1212 thẻ.
# Thủ phạm KHÔNG phải AI gắn ẩu mà là chính lời mô tả:
#     concepts::misc = "fallback when nothing above fits"   -> thùng rác có giấy phép
#     places::city   = "...countries, cities, transport..." -> nuốt cả xe buýt
#     people::family = "...groups of people"                -> nuốt cả quốc tịch
# Cách chữa: chép PHẠM VI trong ngoặc của từng chủ đề ТРКИ vào mô tả, để chỗ nào
# hết phạm vi thì thấy ngay. Không mục nào còn được mang nghĩa "cái còn lại".
# ==============================================================================

TOPIC_TAG_PREFIX = "topic::"

# slug -> mô tả (tiếng Anh, dùng trong prompt AI). Phạm vi trong ngoặc lấy từ
# tên chủ đề ТРКИ tương ứng — ĐỪNG nới rộng khi thêm từ mới; hết phạm vi nghĩa
# là từ đó thuộc chủ đề khác.
TOPICS = {
    # ── people: con người ──
    "people::body": "appearance and body parts (внешность, части тела: рука, глаз, высокий)",
    "people::life": "stages and ages of human life (жизнь человека: детство, молодой, женатый, возраст)",
    "people::nation": "nationality, religion, how a person relates to others (национальность, религия: русский, иностранец, друг, враг)",
    "people::professions": "occupation, field of work, job status, wealth (работа, профессия, достаток: врач, зарплата, богатый)",
    "people::family": "family members and relatives (семья, родственники: мама, папа, брат, жена, бабушка). Keep pairs together — mother with father, wife with husband. Nationalities go to people::nation",
    # ── life: đời sống hằng ngày ──
    "life::food": "food, groceries, meals, cooking (еда, продукты, питание: хлеб, готовить, вкусный)",
    "life::home": "housing: furniture, household objects, appliances (жильё, мебель, предметы быта: стол, лампа, гараж)",
    "life::health": "health, illness, medicine (здоровье: болеть, лекарство, боль)",
    "life::art": "the arts: architecture, painting, cinema, literature, music, theatre (искусство: балет, барабан, альбом)",
    "life::clothing": "clothes, footwear, jewellery (одежда, обувь, украшения: платье, сапог)",
    "life::leisure": "rest, free time, interests, holidays (отдых, досуг, праздники: отпуск, игра, ёлка)",
    "life::sport": "sport (спорт: футбол, баскетбол, велосипед)",
    # ── nature: thiên nhiên ──
    "nature::animals": "animals, birds, fish, insects (животные: кот, рыба, муха)",
    "nature::plants": "plants, trees, flowers (растения: дерево, цветок, лес)",
    "nature::weather": "climate, seasons, natural phenomena, weather (климат, погода: дождь, мороз, холодно)",
    # ── places: địa điểm, di chuyển ──
    "places::geo": "geography: continents, countries, natural landmarks (география: Россия, море, гора)",
    "places::city": "where people live and public places — BUILDINGS AND INSTITUTIONS only (место жительства, общественные места: школа, магазин, улица). Vehicles belong to places::transport",
    "places::position": "place, location, distance (место, расположение, расстояние: здесь, слева, близко, вход)",
    "places::travel": "travel and tourism (путешествия, туризм: путешествие, багаж, гостиница)",
    "places::transport": "transport and journeys — VEHICLES and travelling by them (транспорт, поездки: автобус, поезд, вагон)",
    # ── language: ngôn ngữ & giao tiếp ──
    "language::grammar": "function words AND question words: pronouns, particles, conjunctions, prepositions, introductory words (союзы, предлоги, частицы, местоимения, вопросительные слова: я, кто, или, можно)",
    "language::documents": "documents and publications (документы, издания: паспорт, газета, книга)",
    "language::education": "education and science (образование и наука: урок, студент, опыт, формула)",
    "language::communication": "communication and means of communication (общение, средства коммуникации: разговор, письмо, телефон)",
    "language::etiquette": "etiquette formulas (этикет: спасибо, пожалуйста, здравствуйте)",
    # ── các gốc hiện là lá hoặc ít nhánh ──
    "time": "time: periods, parts of the day, weekdays, months, seasons, orientation in time (время: час, январь, вчера, ранний)",
    "numbers": "numbers, quantity, numerals (количество, числа, числительные: пять, много, первый)",
    "numbers::units": "units of measure — distance, time, weight, cost (единицы измерения: метр, килограмм, рубль)",
    "actions": "actions directed at somebody or something — general transitive verbs not covered by another topic (действия: делать, взять, помочь)",
    "qualities": "characteristics of objects: size, shape, weight, quality, cost, belonging (характеристика объектов: большой, круглый, дешёвый). Colours go to qualities::colors",
    "qualities::colors": "colours (цвет: красный, синий, цвет)",
    "qualities::eval": "evaluation and significance of something or somebody (оценка, значимость: важный, главный, нужно)",
    # ── concepts: khái niệm (KHÔNG còn mục nào nghĩa là "phần dư") ──
    "concepts::state": "state, power, politics (государство, власть, политика: закон, война, президент)",
    "concepts::mind": "intellect, will, desire (интеллект, воля, желание: думать, хотеть, память)",
    "concepts::emotion": "emotions, character, inner states (эмоции, характер, состояния: радость, добрый, устать)",
}

# 🔴 CỐ Ý KHÔNG CÓ `FALLBACK_TOPIC` (QD-38, 23/08/2026).
# Trước đây slug hỏng hoặc không xếp được bị ép về `concepts::misc`. Chính cái
# van im lặng đó đẻ ra rọ rác: thẻ đổ vào đấy TRÔNG NHƯ đã phân loại xong nên
# không ai đi tìm lại. Nay `normalize_topic()` trả về None -> thẻ KHÔNG được gắn
# tag -> `/thongke` đếm vào mục "chưa có tag", `build_subdecks.py` không di
# chuyển nó. Chưa xếp được thì phải NHÌN THẤY LÀ CHƯA XẾP.

# Tên slug CŨ -> MỚI. scripts/tag_topics.py --fix dựa vào đây để dịch tag cũ trên
# thẻ sang tên mới; normalize_topic() cũng dùng để "đỡ" nếu AI lỡ trả tên cũ.
LEGACY_ALIASES = {
    # đợt cây phẳng 19 chủ đề -> cây 2 tầng 10 gốc (18/07/2026)
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
    # đợt thay bảng chủ đề bằng chuẩn ТРКИ (23/08/2026, QD-37).
    # `life::home`, `language::grammar`, `life::food`... giữ NGUYÊN TÊN nên không
    # cần dòng nào ở đây — normalize_topic() tìm thấy thẳng trong TOPICS.
    # 🔴 Các slug cũ bị XOÁ mà KHÔNG có tên mới tương đương — CỐ Ý không đưa vào
    # đây: `concepts::abstract`, `concepts::misc`, `other` là rọ rác (từ trong đó
    # rải ra ~20 chủ đề khác nhau), còn `places::city` và `people::family` cũ có
    # phạm vi RỘNG HƠN tên mới cùng chữ. Dịch máy chúng là chép nguyên mớ lộn xộn
    # sang cây mới. Chúng đi đường bảng tra ros-edu, thiếu nữa thì đi đường AI.
}

# 🔴 CỐ Ý KHÔNG CÓ bảng "id chủ đề ТРКИ -> slug" (user chốt 23/08/2026).
# Đã dựng thử rồi BỎ, vì đo ra nhãn TỪNG TỪ của nguồn sai có hệ thống — 6/16 cặp
# từ đối nhau bị tách sang hai chủ đề khác nhau:
#     папа·отец -> "Семья"          nhưng мама·мать -> "Жизнь человека"
#     жена      -> "Семья"          nhưng муж       -> "Жизнь человека"
#     вопрос    -> "Вопросительные слова" (nó là DANH TỪ, không phải từ để hỏi)
#     белый·красный -> gộp vào "Характеристика объектов", làm rỗng `qualities::colors`
# Lấy CẤU TRÚC cây của họ (rõ, có phạm vi trong ngoặc) là đúng; lấy nhãn từng từ
# của họ là chép nguyên lỗi sang. Nên: danh sách từ + TRÌNH ĐỘ lấy từ
# `data/rosedu_muc.json`, còn chủ đề thì AI tự xếp theo đúng bảng TOPICS ở trên.


def normalize_topic(value):
    """Chuẩn hóa giá trị topic AI trả về -> slug hợp lệ trong TOPICS.
    Chấp nhận cả dạng có prefix 'topic::' lẫn tên cũ trong LEGACY_ALIASES.

    🔴 Trả về **None** khi không xếp được — KHÔNG ép về chủ đề nào (QD-38).
    Người gọi PHẢI xử lý None: thẻ đó chưa có chủ đề, và phải nhìn thấy được là
    chưa có, chứ không được lặng lẽ đổ vào một rọ."""
    if not isinstance(value, str):
        return None
    slug = value.strip().lower()
    if slug.startswith(TOPIC_TAG_PREFIX):
        slug = slug[len(TOPIC_TAG_PREFIX):]
    slug = LEGACY_ALIASES.get(slug, slug)
    return slug if slug in TOPICS else None


def topic_tag(slug):
    """slug -> tag Anki đầy đủ, vd 'life::food' -> 'topic::life::food'.
    None nếu slug không xếp được — người gọi phải lọc, ĐỪNG ghép chuỗi thẳng
    (ghép thẳng sẽ đẻ ra tag 'topic::None' trông như tag thật)."""
    ok = normalize_topic(slug)
    return f"{TOPIC_TAG_PREFIX}{ok}" if ok else None


def topics_prompt_block():
    """Danh sách chủ đề dạng text để nhét vào system prompt của AI."""
    lines = [f"- {slug}: {desc}" for slug, desc in TOPICS.items()]
    return "\n".join(lines)


# ==============================================================================
# --- PHẦN 2: TỪ LOẠI (ô `PoS` mặt trước / `PoSFull` mặt sau thẻ) ---
#
# 🔴 VÌ SAO CÓ BẢNG NÀY (01/09/2026, QD-41). OpenRussian trả thẳng chữ `"other"`
# cho 93/1290 thẻ — trạng từ, giới từ, liên từ, trợ từ dồn chung một rọ. Badge in
# ra chữ `oth`, tức là **mặt thẻ có một ô mà không dạy gì**; 12 file lô kho đã
# phải viết tay câu "PoS = oth nên badge vô dụng, phải tự ghi từ loại".
#
# Đã ĐO ba đường trước khi chọn (01/09/2026):
#  · Hỏi lại OpenRussian: VÔ ÍCH. 74/93 vẫn trả "other", và nó trả SAI 2 từ —
#    `тут` ("ở đây") và `справа` ("bên phải") nó bảo là DANH TỪ.
#  · Chép bảng tra viết tay 93 từ vào repo: chạy được, nhưng chỉ cứu 93 từ đã
#    biết; từ mới gõ vào ngày mai lại ra "other".
#  · AI xếp (đường đã chọn): đo trên đúng 93 từ đó, khớp 89/93 với bảng xếp tay.
#    4 chỗ lệch đều là từ mang HAI từ loại (`всё` đại từ/trạng từ, `пока`
#    thán từ/liên từ) — chỗ mà bản thân các nhà ngữ pháp cũng chia hai phe.
#
# 🔴 KHÔNG có mã "other"/"unknown" trong bảng này, CỐ Ý — cùng lý lẽ với QD-38:
# một rọ chứa "phần còn lại" làm thẻ TRÔNG NHƯ đã phân loại xong nên không ai đi
# tìm lại. `normalize_pos()` trả None; ô PoS để TRỐNG thì nhìn là thấy ngay.
# ==============================================================================

# mã ngắn (mặt TRƯỚC thẻ) -> (tên đầy đủ mặt SAU, mô tả cho prompt AI).
# 🔴 Tên đầy đủ phải GIỮ NGUYÊN VĂN: 1197 thẻ có sẵn đang ghi đúng 6 chữ
# noun/verb/adjective/adverb/numeral/pronoun (đo 01/09/2026). Đổi chữ ở đây mà
# không chạy lại `scripts/backfill_badge.py` là kho lẫn hai cách gọi cùng một thứ.
TU_LOAI = {
    "n": ("noun", "noun (существительное)"),
    "v": ("verb", "verb (глагол)"),
    "adj": ("adjective", "adjective (прилагательное)"),
    "adv": ("adverb", "adverb (наречие) — including pronominal adverbs: там, где, когда, почему"),
    "num": ("numeral", "numeral (числительное)"),
    "pron": ("pronoun", "pronoun (местоимение) — это, все, ничего, я, кто"),
    "prep": ("preposition", "preposition (предлог) — в, на, до, для, через"),
    "conj": ("conjunction", "conjunction (союз) — и, но, или, чтобы, хотя"),
    "part": ("particle", "particle (частица) — не, ни, вот, пусть, да, нет, только"),
    "pred": ("predicative", "impersonal predicative (предикатив, категория состояния) — нельзя, надо, жаль"),
    "interj": ("interjection", "interjection (междометие) — ой, ах, здравствуйте"),
}

# Tên OpenRussian trả về / tên cũ -> mã ngắn. Nguồn viết đủ chữ ("preposition"),
# thẻ lưu mã ngắn ("prep"), nên phải dịch. Nhận cả hai chiều để người gọi khỏi
# phải nhớ mình đang cầm loại nào.
_POS_ALIASES = {ten_du: ma for ma, (ten_du, _mo_ta) in TU_LOAI.items()}
_POS_ALIASES.update({
    "particuple": "adj",     # OpenRussian gõ nhầm "participle" ở vài mục
    "participle": "adj",
    "numeral": "num", "number": "num",
    "conjunction": "conj", "preposition": "prep", "interjection": "interj",
    "predicative": "pred", "particle": "part",
})


def normalize_pos(value):
    """Chuẩn hoá từ loại (mã ngắn HOẶC tên đầy đủ) -> mã ngắn trong TU_LOAI.

    🔴 Trả về **None** khi không xếp được — KHÔNG ép về "other" (xem khối comment
    trên). Người gọi phải để ô PoS TRỐNG, đừng ghép chuỗi thẳng."""
    if not isinstance(value, str):
        return None
    ma = value.strip().lower()
    ma = _POS_ALIASES.get(ma, ma)
    return ma if ma in TU_LOAI else None


def pos_full(value):
    """mã ngắn -> tên đầy đủ cho ô `PoSFull` ('adv' -> 'adverb'). None nếu không xếp được."""
    ma = normalize_pos(value)
    return TU_LOAI[ma][0] if ma else None


def pos_prompt_block():
    """Danh sách từ loại dạng text để nhét vào system prompt của AI."""
    return "\n".join(f"- {ma}: {mo_ta}" for ma, (_ten, mo_ta) in TU_LOAI.items())
