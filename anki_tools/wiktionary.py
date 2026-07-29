# -*- coding: utf-8 -*-
"""Vá lỗ hổng SỐ TỪ của OpenRussian bằng Wiktionary tiếng Nga.

## Vì sao cần nguồn thứ hai

OpenRussian dễ cào và đủ dùng cho gần hết mọi việc, nhưng **28 số từ đếm cơ bản**
(`два · четы́ре · во́семь · со́рок · сто · пятьсо́т`…) chỉ lưu đúng dạng gốc
(`formType = "ru_base"`), không có bảng biến cách. Đó là nhóm user dùng hằng
ngày và cũng là nhóm dễ sai nhất (`два/две`, `двух`, `двумя́`).

Đã cân nhắc rồi LOẠI `pymorphy3` (dự án đã có sẵn cho việc lemma): nó chia được
các dạng này nhưng **không có dấu trọng âm**, mà user chốt bảng phải *"viết từ
chính xác, đầy đủ trọng âm"*. Ghép hai nguồn để đoán chỗ nhấn là đưa trọng âm
sai lên thẻ mà user KHÔNG tự kiểm được — đúng ranh giới README §1 cấm.

## Cào cái gì

Bảng `<table class="morfotable ru">` trên `ru.wiktionary.org`. Nội dung Wiktionary
theo giấy phép CC BY-SA nên bảng dựng ra có ghi nguồn.

⚠️ **Cấu trúc bảng KHÔNG nhất quán** — đo thật trên 6 từ đã thấy 4 kiểu:
  · tên cách viết tắt 4 kiểu:  `Им./Рд./Дт./Вн./Тв./Пр.`  ·  `Им./Р./Д./В.`
    ·  `Им./Род./Дат./Вин./Твор./Предл.`  (nên phải khớp theo TIỀN TỐ)
  · `два` tách CỘT theo giống (`муж., ср.` | `жен.`), ô dùng chung thì `colspan=2`
  · `два`·`четы́ре` tách DÒNG ở cách 4 theo sống/không sống (`одуш.`/`неод.`)
  · ô nhiều biến thể ngăn bằng DẤU CÁCH, không phải dấu phẩy (`восьмью́ восемью́`)
"""
import re
import time
import urllib.parse

from .grammar import CASES, acc, bare
from .utils import log_fail, log_warn

BASE = "https://ru.wiktionary.org/wiki/"
UA = "AnkiGrammarBot/1.0 (personal Russian study flashcards)"

# Tên cách tiếng Nga -> mã. Khớp theo TIỀN TỐ vì Wiktionary viết tắt bốn kiểu.
TIEN_TO_CACH = [("им", "nom"), ("рд", "gen"), ("род", "gen"), ("р", "gen"),
                ("дт", "dat"), ("дат", "dat"), ("д", "dat"),
                ("вн", "acc"), ("вин", "acc"), ("в", "acc"),
                ("тв", "inst"), ("твор", "inst"), ("т", "inst"),
                ("пр", "prep"), ("предл", "prep"), ("п", "prep")]
# dài trước ngắn sau, kẻo "р" nuốt mất "род"
TIEN_TO_CACH.sort(key=lambda x: -len(x[0]))

SONG = {"одуш": "sống", "неод": "vật"}

# 🔴 Ô tiêu đề phải LOẠI TRƯỚC khi dò tên cách: `падеж` bắt đầu bằng "п" nên
# khớp luôn vào `пр` = cách 6, kéo cả dòng tiêu đề ("Падеж | форма") vào ô cách 6
# — và tệ hơn, nhánh nhận CỘT THEO GIỐNG không bao giờ chạy tới, nên `два` gộp
# chung `два́` với `две́` làm một. Một lỗi, hỏng hai chỗ.
TIEU_DE = ("падеж", "форма", "число")


def _sach(s):
    """Text trong ô -> chuỗi gọn; biến thể ngăn bằng dấu cách -> ngăn bằng phẩy."""
    s = re.sub(r"\s+", " ", (s or "").replace("\xa0", " ")).strip(" -—")
    if not s or s in ("*", "—", "-"):
        return ""
    return ", ".join(acc(x) for x in s.split() if x)


def _ma_cach(nhan):
    n = re.sub(r"[^а-яё]", "", (nhan or "").lower())
    if not n or n.startswith(TIEU_DE):
        return None
    return next((ma for tt, ma in TIEN_TO_CACH if n.startswith(tt)), None)


def _doc_morfotable(bang):
    """<table class="morfotable"> -> {cột: {cách: dạng}}.

    Cột là "sg" khi bảng không tách giống, hoặc "m"/"f" khi có tách (`два`).
    """
    cot, ket, cach_hien = [], {}, None
    for tr in bang.find_all("tr"):
        o = tr.find_all(["th", "td"])
        if not o:
            continue
        dau = _sach(o[0].get_text(" ", strip=True))
        ma = _ma_cach(dau)

        if ma is None:
            # dòng tiêu đề: lấy tên cột (nếu bảng tách giống)
            phu = [_sach(x.get_text(" ", strip=True)) for x in o[1:]]
            if not cot and len(phu) >= 2 and any("жен" in p.lower() for p in phu):
                cot = ["m" if "муж" in p.lower() or "ср" in p.lower() else "f"
                       for p in phu]
            # dòng `одуш.`/`неод.` — phần tiếp của cách 4, KHÔNG phải cách mới
            nhan_song = next((v for k, v in SONG.items()
                              if re.sub(r"[^а-яё]", "", dau.lower()).startswith(k)), None)
            if nhan_song and cach_hien:
                _ghi(ket, cot, o[1:], cach_hien, nhan_song)
            continue

        cach_hien = ma
        # `Вн. | одуш. | дву́х` — ô thứ hai là nhãn sống/không sống, không phải dạng
        con = o[1:]
        nhan_song = None
        if con:
            d = re.sub(r"[^а-яё]", "", _sach(con[0].get_text(" ", strip=True)).lower())
            nhan_song = next((v for k, v in SONG.items() if d.startswith(k)), None)
            if nhan_song:
                con = con[1:]
        _ghi(ket, cot, con, ma, nhan_song)
    return ket


def _ghi(ket, cot, o, ma, nhan_song):
    """Ghi các ô của một dòng vào kết quả, xử lý colspan (ô dùng chung mọi giống)."""
    ten_cot = cot or ["sg"]
    i = 0
    for td in o:
        chu = _sach(td.get_text(" ", strip=True))
        if not chu:
            i += 1
            continue
        rong = int(td.get("colspan") or 1)
        for c in ten_cot[i:i + max(rong, 1)] or ten_cot:
            cu = ket.setdefault(c, {}).get(ma, "")
            moi = f"{chu} ({nhan_song})" if nhan_song else chu
            # cách 4 có hai dòng sống/vật -> nối lại thành một ô
            ket[c][ma] = f"{cu} · {moi}" if cu and moi not in cu else (cu or moi)
        i += rong


def fetch_numeral(word, delay=0.6):
    """Bảng biến cách của một số từ ({} nếu Wiktionary cũng không có).

    Trả về {'numDecl': {...}, 'nguon': 'wiktionary'} để bên gọi biết dạng này
    KHÔNG phải từ OpenRussian — bảng dựng ra phải ghi đúng nguồn.
    """
    import requests
    from bs4 import BeautifulSoup
    url = BASE + urllib.parse.quote(bare(word), safe="")
    try:
        res = requests.get(url, headers={"User-Agent": UA}, timeout=25)
        if res.status_code != 200:
            log_fail(f"wiktionary {word}: HTTP {res.status_code}")
            return {}
        soup = BeautifulSoup(res.text, "html.parser")
        bang = soup.find("table", class_="morfotable")
        if not bang:
            log_warn(f"wiktionary {word}: khong co bang morfotable")
            return {}
        ket = _doc_morfotable(bang)
    except Exception as e:
        log_fail(f"wiktionary {word}: {e}")
        return {}
    finally:
        if delay:
            time.sleep(delay)

    # Chỉ nhận khi ĐỦ 6 CÁCH ở ít nhất một cột. Bảng thiếu ô là bảng dạy thiếu,
    # mà user không tự biết chỗ nào thiếu -> thà không có còn hơn.
    du = {c: v for c, v in ket.items() if all(v.get(m) for m, _ in CASES)}
    return {"numDecl": du, "nguon": "wiktionary"} if du else {}
