# ==============================================================================
# --- GẮN TAG CHỦ ĐỀ (topic::...) CHO THẺ ANKI ---
# Cách dùng (chạy trên máy có Anki + AnkiConnect đang mở):
#   python tag_topics.py            -> DRY-RUN: chỉ in thống kê + ghi file preview,
#                                      KHÔNG đụng gì vào Anki
#   python tag_topics.py --apply    -> gắn tag thật (chỉ addTags, không sửa nội dung
#                                      thẻ, không ảnh hưởng tiến độ học)
#   python tag_topics.py --missing  -> dùng AI phân loại những thẻ KHÔNG có trong
#                                      bảng tra bên dưới và chưa có tag topic::
#                                      (vd thẻ mới tạo lúc AI hỏng). Tốn quota AI,
#                                      mỗi thẻ 1 request nhỏ.
#
# An toàn:
# - Thẻ ĐÃ có tag topic:: nào đó -> luôn bỏ qua (chạy lại bao nhiêu lần cũng được).
# - Chỉ đụng note thuộc model của bot (MODEL_NAME trong config.py).
#
# Bảng WORD_TOPIC bên dưới do Claude phân loại thủ công cho ~610 từ có sẵn
# (07/2026). Từ mới thêm sau ngày đó được AI tự gắn tag ngay lúc tạo thẻ
# (xem ai_client.py / anki_client.py) nên KHÔNG cần thêm vào đây.
# Quy tắc từ dính nhiều chủ đề: chọn theo nghĩa PHỔ BIẾN nhất, mỗi từ đúng 1 tag.
# ==============================================================================
import argparse
import sys
from collections import Counter

import requests

from anki_tools.config import ANKI_CONNECT_URL, MODEL_NAME
from anki_tools.topics import TOPICS, topic_tag, TOPIC_TAG_PREFIX
from anki_tools.utils import strip_accents_perfectly

# Nhóm theo chủ đề cho dễ soát; script tự lật thành dict word -> topic.
TOPIC_WORDS = {
    "people-family": [
        "мама", "папа", "брат", "сестра", "сын", "дочь", "мать", "муж", "семья",
        "друг", "подруга", "тётя", "дядя", "няня", "малыш", "ребята", "народ",
        "девочка", "молодёжь", "родитель", "юра", "чех", "гений", "враг",
    ],
    "professions": [
        "врач", "студент", "продавец", "продавщица", "певец", "певица", "шофёр",
        "физик", "химик", "диктор", "учёный", "князь",
    ],
    "body": [
        "глаз", "ухо", "рука", "нога", "голова", "грудь", "ладонь", "нёбо",
        "коса", "сыпь", "вдох", "выдох", "слеза",
    ],
    "food": [
        "суп", "сок", "сыр", "рис", "лук", "сахар", "масло", "молоко", "мясо",
        "мёд", "хлеб", "соль", "салат", "капуста", "картошка", "картофель",
        "помидор", "шоколад", "блюдо", "колбаса", "яйцо", "огурец", "сметана",
        "груша", "вишня", "изюм", "пюре", "пиво", "чай", "борщ", "щи", "икра",
        "батон", "завтрак", "обед", "конфета", "свёкла", "рожь", "мята", "вода",
        "яблоко", "мясной", "куриный", "варенный", "вкусный", "кислый",
        "сладкий", "завтракать", "обедать", "ужинать", "пить",
    ],
    "home-objects": [
        "дом", "дома", "комната", "квартира", "зал", "стена", "окно", "потолок",
        "этаж", "стул", "стол", "шкаф", "кровать", "лампа", "полка", "зеркало",
        "ковёр", "подушка", "одеяло", "ведро", "корзина", "ваза", "мыло",
        "ложка", "чашка", "нож", "утюг", "щётка", "телефон", "телевизор",
        "дачка", "балка", "бюро", "пакет", "пол", "картина",
    ],
    "clothing": [
        "одежда", "шапка", "шарф", "шуба", "юбка", "рубашка", "платье",
        "костюм", "пальто", "сапог", "кепка", "кеды", "галстук", "плащ",
        "ткань", "сумка", "карман", "кольцо",
    ],
    "animals": [
        "кот", "кошка", "пёс", "ёж", "муха", "коза", "рыба", "белка", "голубь",
        "мышь", "лев", "окунь", "щука", "грач", "зяблик", "хек",
    ],
    "nature-plants": [
        "дуб", "сад", "ёлка", "дерево", "трава", "липа", "лён", "хвощ",
        "листва", "поле", "поляна", "остров", "болото", "земля", "небо",
        "луна", "солнце", "море", "озеро", "лес", "степь", "зерно", "луч", "юг",
    ],
    "weather": [
        "дождь", "снег", "мороз", "гроза", "ветер", "погода", "облако",
        "холод", "жар", "лёд", "солнечный", "облачный", "дождливый", "снежный",
        "ветреный", "пасмурный", "морозный", "холодный", "жаркий", "тёплый",
        "холодно", "жарко",
    ],
    "time": [
        "год", "час", "утро", "вечер", "день", "ночь", "сегодня", "вчера",
        "завтра", "позавчера", "сегодняшний", "вчерашний", "завтрашний",
        "утренний", "вечерний", "ночной", "дневной", "ранний", "поздний",
        "весенний", "летний", "осенний", "зимний", "майский", "весна", "лето",
        "осень", "зима", "весной", "осенью", "зимой", "март", "апрель", "май",
        "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь",
        "январь", "февраль", "понедельник", "вторник", "среда", "четверг",
        "пятница", "суббота", "воскресенье", "сейчас", "часто", "потом",
        "когда", "выходной", "будничный",
    ],
    "numbers": [
        "цифра", "число", "сколько", "метр", "килограмм", "дюйм", "дробь",
    ],
    "colors": [
        "цвет", "красный", "белый", "жёлтый", "чёрный", "оранжевый",
        "коричневый", "фиолетовый", "голубой", "зелёный", "розовый", "синий",
    ],
    "places-city": [
        "город", "страна", "деревня", "село", "улица", "площадь", "центр",
        "банк", "парк", "цирк", "школа", "вокзал", "музей", "магазин",
        "институт", "университет", "больница", "библиотека", "кинотеатр",
        "кино", "гараж", "завод", "рынок", "собор", "клуб", "бар", "буфет",
        "проспект", "фонтан", "москва", "россия", "индия", "франция", "киев",
        "автобус", "машина", "автомобиль", "дорога", "багаж", "вход", "выход",
    ],
    "education": [
        "класс", "урок", "книга", "буква", "слово", "тетрадь", "учебник",
        "словарь", "карандаш", "ручка", "лекция", "письмо", "газета", "журнал",
        "вопрос", "рассказ", "сказка", "стих", "роман", "зачёт", "доска",
        "физика", "химия", "бумага", "открытка", "мел",
        "читать", "писать", "учиться", "повторять",
    ],
    # actions / qualities / other: chủ yếu để fallback theo từ loại lo (xem dưới),
    # chỉ liệt kê từ cần ép riêng.
    "actions": [],
    "qualities": [],
    "other": ["можно", "карта", "угол"],
}

WORD_TOPIC = {}
for _topic, _words in TOPIC_WORDS.items():
    for _w in _words:
        if _w in WORD_TOPIC:
            raise SystemExit(f"Từ '{_w}' bị khai báo ở 2 chủ đề: {WORD_TOPIC[_w]} và {_topic}")
        WORD_TOPIC[_w] = _topic

# Từ không có trong bảng tra -> đoán theo từ loại (field PoS của thẻ)
POS_FALLBACK = {"num": "numbers", "v": "actions", "adj": "qualities", "adv": "qualities"}
# pron / oth / n còn lại -> other
DEFAULT_TOPIC = "other"


def call(action, **params):
    r = requests.post(ANKI_CONNECT_URL, json={"action": action, "version": 6, "params": params}, timeout=60)
    j = r.json()
    if j.get("error"):
        raise SystemExit(f"AnkiConnect lỗi ({action}): {j['error']}")
    return j["result"]


def classify(word_clean, pos):
    """Trả về (topic_slug, nguồn) — nguồn: 'map' (bảng tra) hoặc 'pos' (fallback từ loại)."""
    w = word_clean.strip().lower()
    if w in WORD_TOPIC:
        return WORD_TOPIC[w], "map"
    return POS_FALLBACK.get(pos.strip().lower(), DEFAULT_TOPIC), "pos"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Gắn tag chủ đề topic:: cho thẻ Anki")
    ap.add_argument("--apply", action="store_true", help="gắn tag thật (mặc định: dry-run)")
    ap.add_argument("--missing", action="store_true",
                    help="dùng AI phân loại thẻ không có trong bảng tra (tốn quota)")
    args = ap.parse_args()

    note_ids = call("findNotes", query=f'note:"{MODEL_NAME}"')
    notes = call("notesInfo", notes=note_ids)
    print(f"Tổng số note: {len(notes)}")

    plan = {}          # topic_slug -> [note_ids]
    fallback_words = []  # từ phải đoán theo PoS (để soát mắt)
    skipped = 0
    for n in notes:
        if any(t.startswith(TOPIC_TAG_PREFIX) for t in n.get("tags", [])):
            skipped += 1
            continue
        f = n["fields"]
        word = f.get("WordClean", {}).get("value", "") or strip_accents_perfectly(
            f.get("Word", {}).get("value", ""))
        pos = f.get("PoS", {}).get("value", "")

        if args.missing and word.strip().lower() not in WORD_TOPIC:
            from anki_tools.ai_client import call_claude_topic
            en = f.get("Meaning", {}).get("value", "")
            slug = call_claude_topic(word, [en[:200]])
            source = "ai"
            if not slug:
                print(f"  ⚠️ AI không phân loại được '{word}' -> bỏ qua")
                continue
        else:
            slug, source = classify(word, pos)
            if source == "pos":
                fallback_words.append(f"{word} ({pos or '?'}) -> {slug}")

        plan.setdefault(slug, []).append(n["noteId"])

    print(f"Bỏ qua (đã có tag topic::): {skipped}")
    print("\nKế hoạch gắn tag:")
    total = 0
    for slug in TOPICS:
        ids = plan.get(slug, [])
        if ids:
            print(f"  {topic_tag(slug):28} {len(ids):4} thẻ")
            total += len(ids)
    print(f"  {'TỔNG':28} {total:4} thẻ")

    if fallback_words:
        print(f"\nTừ KHÔNG có trong bảng tra, đoán theo từ loại ({len(fallback_words)}):")
        for line in fallback_words:
            print("  ", line)

    if not args.apply:
        print("\n(DRY-RUN — chưa gắn gì. Chạy lại với --apply để gắn thật.)")
        return

    for slug, ids in plan.items():
        call("addTags", notes=ids, tags=topic_tag(slug))
        print(f"✅ Đã gắn {topic_tag(slug)} cho {len(ids)} thẻ")
    print("\nXong. Kiểm tra lại trong Anki Browser (cây Tags bên trái).")


if __name__ == "__main__":
    main()
