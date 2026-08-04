# -*- coding: utf-8 -*-
# ==============================================================================
# --- DỰNG BẢNG HTML bảng chia (tách từ grammar.py 03/08/2026, QD-19) ---
# Bảng nằm TRONG ô Hướng dẫn, bọc trong <details> lồng: mặc định gấp lại nên
# KHÔNG tốn một pixel nào của trần "vừa một màn hình iPhone" (README §2). Phần
# chú ý cô đọng vẫn nằm ở trên, bảng chỉ để user bấm vào nghiên cứu thêm.
#
# 🔴 KHÔNG dùng <b> cho dạng từ trong bảng. `congcu.py soat` và `kiemtra.py` đối
# chiếu MỌI từ Nga in <b> với nouns.csv (từ điển chỉ chứa dạng NGUYÊN THỂ) — các
# dạng đã chia sẽ bị kêu oan hàng loạt, mà một bộ soát kêu oan mãi thì rồi chính
# mình sẽ bỏ qua cả tiếng kêu thật.
# ==============================================================================
import re

from .chu_nga import ACUTE, CASES, GIONG_TT, PASTS, PERSONS, VOWELS
from .hinh_thai import analyze


def thieu_dau(form):
    """Ô từ điển QUÊN đánh trọng âm (>=2 nguyên âm mà không có dấu, không có ё).

    Đo trên cả kho: 4/5 900 ô, đúng một từ (`ва́ренный`). Hiếm, nhưng im lặng thì
    user học thuộc trọng âm sai — mà user KHÔNG tự kiểm được (README §1). Nên ô
    đó phải tự nói ra là nó không chắc.
    """
    t = (form or "").split(",")[0].strip()
    return (len([c for c in t if c in VOWELS]) >= 2
            and ACUTE not in t and "ё" not in t.lower())


def _o(text, nong=False, nhan_bien_the=False):
    """Một ô bảng. `nhan_bien_the` = ô này là cách 5 số ít, có thể chứa dạng
    `-ою` cần dán nhãn (xem `_nhan_bien_the`).

    🔴 Soi `thieu_dau` TRƯỚC khi dán nhãn: dán xong thì chuỗi có thêm chữ Việt
    và thẻ HTML, đếm nguyên âm trên đó là ra số vô nghĩa.
    """
    lop = "gt-v" + (" gt-nong" if nong else "")
    ngo = '<span class="gt-ngo">?</span>' if text and thieu_dau(text) else ""
    if not text:
        return f'<td class="{lop}">—</td>'
    return f'<td class="{lop}">{_nhan_bien_the(text) if nhan_bien_the else text}{ngo}</td>'


# Nhãn cột. NGẮN hết mức: bảng 5 cột phải lọt bề ngang 368px của .hd-content.
NHAN_COT = {"sg": "ít", "pl": "nhiều",
            "m": "он", "f": "она́", "n": "оно́"}


# Cách 5 số ít giống cái có HAI dạng: `-ой/-ей` (đời nay) và `-ою/-ею` (văn
# chương · thơ ca · cổ). Từ điển in cả hai, ngang hàng, KHÔNG nhãn — đo 04/08:
# **139 từ** trong bộ sưu tập. Trần trụi như thế là dạy user rằng hai dạng dùng
# thay nhau được trong lời nói thường, mà không phải: viết `с ма́мою` trong tin
# nhắn nghe như đọc thơ. Nhãn ở ĐÂY chứ không sửa dữ liệu: dạng đó CÓ THẬT, chỉ
# là thiếu chú thích — sửa một chỗ là khỏi cả 139 từ, và từ mới cào về cũng khỏi.
_OU_RE = re.compile(r"^(.+?),\s*(\S+?[оеё]́?ю)$")


def _nhan_bien_the(text):
    """`'ма́мой, ма́мою'` -> dạng đời nay + dạng `-ою` có dán nhãn văn chương."""
    m = _OU_RE.match((text or "").strip())
    if not m:
        return text
    return f'{m.group(1)}<span class="gt-bt">· {m.group(2)} (văn chương)</span>'


def _bang_cach(ten, du_lieu, nong, tien_to=""):
    """Dựng MỘT bảng 6 cách từ {cột: {cách: dạng}}.

    Dùng chung cho danh từ (ít/nhiều), tính từ · đại từ · số từ (theo giống) —
    bốn nhóm khác nhau nhưng cùng một hình dạng, nên cùng một hàm. Cột nào cũng
    trống thì bỏ hẳn bảng, không in khung rỗng.
    """
    cot = [c for c in ("sg", "m", "f", "n", "pl")
           if c in du_lieu and any((du_lieu[c] or {}).values())]
    if not cot:
        return ""
    # một cột duy nhất thì bỏ luôn hàng tiêu đề — thừa một dòng là thừa
    dau = ""
    if len(cot) > 1:
        dau = ('<tr><td class="gt-h"></td>'
               + "".join(f'<td class="gt-h">{NHAN_COT.get(c, c)}</td>' for c in cot)
               + "</tr>")
    rows = "".join(
        f'<tr><td class="gt-k">{nhan}</td>'
        + "".join(_o(du_lieu[c].get(ma), (tien_to + c, ma) in nong or (c, ma) in nong,
                     nhan_bien_the=(ma == "inst"))
                  for c in cot)
        + "</tr>"
        for ma, nhan in CASES)
    return (f'<div class="gt-ten">{ten}</div>'
            f'<table class="gt-tbl">{dau}{rows}</table>')


def _bang_hang(ten, nhan_o, dang, nong, khoa):
    """Bảng dạng danh sách (chia ngôi, quá khứ, dạng ngắn) — 2 cột, N hàng."""
    o = [(nhan_o[i], dang[i], (khoa, i) in nong)
         for i in range(min(len(nhan_o), len(dang))) if (dang[i] or "").strip()]
    if not o:
        return ""
    rows = "".join(f'<tr><td class="gt-k">{n}</td>{_o(d, hot)}</tr>' for n, d, hot in o)
    return f'<div class="gt-ten">{ten}</div><table class="gt-tbl">{rows}</table>'


def _bang_danh_tu(rec, nong):
    return _bang_cach("Biến cách", rec.get("decl") or {}, nong)


# Nhãn sáu ô "Participles" của OpenRussian. Ngắn hết mức: bảng 2 cột phải lọt bề
# ngang 368px của `.hd-content`, mà cột nhãn đây dài hơn mọi bảng khác.
NHAN_PHAN_TU = (("activePresent", "chủ động · hiện tại"),
                ("activePast", "chủ động · quá khứ"),
                ("passivePresent", "bị động · hiện tại"),
                ("passivePast", "bị động · quá khứ"),
                ("gerundPresent", "trạng đt · hiện tại"),
                ("gerundPast", "trạng đt · quá khứ"))


def _o_phan_tu(ds):
    """Ô phân từ: các dạng cách nhau ` · `, kèm nghĩa Anh ở dòng nhỏ bên dưới.

    🔴 Soi `thieu_dau` cho TỪNG dạng, không soi trên chuỗi đã nối — nguồn có ô
    hai dạng mà chỉ dạng đầu được đánh trọng âm (`прочита́в · прочитавши`), nối
    lại rồi soi thì chuỗi "có dấu" nên cái thiếu dấu lọt im lặng.
    """
    dang = " · ".join(
        (f['f'] + '<span class="gt-ngo">?</span>') if thieu_dau(f["f"]) else f["f"]
        for f in ds)
    en = next((f["en"] for f in ds if f.get("en")), "")
    chu = f'<div class="gt-chu">{en}</div>' if en else ""
    return f'<td class="gt-v">{dang}{chu}</td>'


def _bang_phan_tu(rec):
    """Khối Participles (gồm cả Gerund) — ô nào nguồn để trống thì bỏ hẳn hàng.

    Thể hoàn thành gần như không có phân từ hiện tại, thể chưa hoàn thành gần như
    không có phân từ bị động quá khứ ⇒ in khung rỗng là dạy sai rằng "có mà chưa
    lấy về". Bảng nằm trong `<details>` gấp lại nên KHÔNG tốn pixel nào của trần
    700px (README §2) — đó là lý do lấy đủ được mà không phá chuẩn ngắn gọn.
    """
    parts = rec.get("parts") or {}
    rows = "".join(f'<tr><td class="gt-k">{nhan}</td>{_o_phan_tu(parts[k])}</tr>'
                   for k, nhan in NHAN_PHAN_TU if parts.get(k))
    if not rows:
        return ""
    return f'<div class="gt-ten">Phân từ</div><table class="gt-tbl">{rows}</table>'


def _bang_dong_tu(rec, nong):
    # Với thể HOÀN THÀNH, `presfut` là TƯƠNG LAI chứ không phải hiện tại — gọi
    # sai tên ở đây là dạy sai đúng thứ badge PERF/IMPF vừa dựng lên để phân biệt.
    hoan_thanh = rec.get("aspect") == "perfective"
    ten = "Tương lai đơn" if hoan_thanh else "Hiện tại"
    ra = _bang_hang(f"Chia ngôi — {ten}", PERSONS, rec.get("presfut") or [],
                    nong, "presfut")
    # Cột CÒN LẠI của khối Conjugation trên OpenRussian (trang hiện Present và
    # Future cạnh nhau). Ở đây xếp DỌC vì bề ngang chỉ có 368px.
    # 🔴 Truyền mảng THÔ, đừng lọc ô rỗng trước: `_bang_hang` bỏ ô rỗng theo CHỈ SỐ
    # để khớp nhãn ngôi; lọc trước là nhãn lệch hàng mà nhìn vẫn thấy có vẻ đúng.
    khac = rec.get("present") if hoan_thanh else rec.get("future")
    khac = khac or []
    co = [x for x in khac if x]
    if co and co != [x for x in (rec.get("presfut") or []) if x]:
        ra += _bang_hang("Hiện tại" if hoan_thanh else "Tương lai (ghép)",
                         PERSONS, khac, nong, "future")
    ra += _bang_hang("Quá khứ", PASTS, rec.get("past") or [], nong, "past")
    im = [x for x in (rec.get("imper") or []) if x]
    if im:
        ra += f'<div class="gt-phu">Mệnh lệnh: {" · ".join(im[:2])}</div>'
    ra += _bang_phan_tu(rec)
    return ra


def _bang_tinh_tu(rec, nong):
    ra = _bang_cach("Biến cách", rec.get("adjDecl") or {}, nong)
    ra += _bang_hang("Dạng ngắn", [n for _, n in GIONG_TT],
                     rec.get("shorts") or [], nong, "shorts")
    phu = []
    if rec.get("comp"):
        phu.append("hơn: " + " · ".join(rec["comp"][:3]))
    if rec.get("super"):
        phu.append("nhất: " + " · ".join(rec["super"][:2]))
    if rec.get("adverb"):
        phu.append("trạng từ: " + rec["adverb"])
    if rec.get("incomparable"):
        phu.append("KHÔNG có dạng so sánh")
    if phu:
        ra += '<div class="gt-phu">' + " · ".join(phu) + "</div>"
    return ra


def _bang_dai_tu(rec, nong):
    return _bang_cach("Biến cách", rec.get("proDecl") or {}, nong)


def _bang_so_tu(rec, nong):
    return _bang_cach("Biến cách", rec.get("numDecl") or {}, nong)


_BANG = {"noun": _bang_danh_tu, "verb": _bang_dong_tu, "adjective": _bang_tinh_tu,
         "pronoun": _bang_dai_tu, "numeral": _bang_so_tu}


_BANG_RE = re.compile(r'<details class="gt-bang">.*?</details>', re.S)


def go_bang(html):
    """GỠ bảng chia khỏi một ô Hướng dẫn — ô đó nay CHỈ chứa phần người soạn.

    Thay `attach_table()` cũ (QD-26, 04/08/2026). Trước đây bảng được nối vào
    đuôi `HuongDan` bằng cắt-dán khuôn mẫu; từ nay bảng sống ở field riêng
    `BangMay`, nên chiều duy nhất còn lại là GỠ RA.

    🔴 Vì sao đổi: cắt-dán khuôn mẫu là gốc của cả một loại lỗi im lặng. Phần máy
    nối vào sau lưng mọi cửa soát (`soat`/`dodai` chỉ đo phần agent viết) nên rác
    trong bảng sống nhiều tuần không ai bắt — 7 ca đã phải ghi vào sổ nợ. Tách
    field thì cửa máy đo được đúng phần máy.

    Vẫn phải gọi khi ghi đè `HuongDan` ở luồng LÀM LẠI THẺ (`pipeline.redo_note_id`)
    để bảng CŨ còn sót trong nội dung cũ được dọn đi, không đọng lại hai bảng.
    """
    return _BANG_RE.sub("", html or "").rstrip()


def cap_the_html(rec):
    """Dòng CẶP THỂ của động từ ('' nếu không phải động từ / không có cặp).

    Dữ liệu đã nằm sẵn trong `GrammarJSON` từ lâu (`partners`, bóc ở
    `boc_tudien.normalize`) nhưng chưa từng được hiện ra — đo 04/08: **112/116**
    động từ trong bộ sưu tập đã có, cả kho ở bản ghi v4 ⇒ không phải cào lại một
    từ nào.

    🔴 CHỈ LẤY `partners[0]`, không liệt kê hết. Từ điển trả 1–3 mục và chỉ mục
    đầu là cặp thể chuẩn (`aspectPartner` của OpenRussian trỏ đúng vào nó, đã đối
    chiếu); các mục sau là từ GẦN NGHĨA khác hẳn về sắc thái — `сказа́ть` kéo theo
    `ска́зывать` (kể lể, gần như không dùng), `чита́ть` kéo theo `почита́ть` (đọc
    một lúc cho vui). In hết là dạy sai ba từ để được một từ đúng. User chốt
    04/08: *"chỉ cặp chuẩn, hai từ"*.
    """
    if rec.get("pos") != "verb":
        return ""
    ban = next((p for p in (rec.get("partners") or []) if p), "")
    if not ban:
        return ""
    minh = rec.get("acc") or rec.get("wc") or ""
    nhan = {"perfective": ("hoàn thành", "chưa hoàn thành"),
            "imperfective": ("chưa hoàn thành", "hoàn thành")}.get(rec.get("aspect"))
    if not nhan:
        return ""                   # thể `both` / thiếu thể: nói cặp là nói bừa
    return ('<div class="gt-ten">Cặp thể</div>'
            f'<div class="gt-cap">{minh} <span class="gt-cap-n">({nhan[0]})</span>'
            f' ↔ {ban} <span class="gt-cap-n">({nhan[1]})</span></div>')


def khoi_may(rec, phan_tich=None):
    """TOÀN BỘ nội dung field `BangMay` = cặp thể + bảng chia ('' nếu không có gì).

    Đây là thứ DUY NHẤT được ghi vào `BangMay`, và `BangMay` là thứ DUY NHẤT máy
    ghi lên mặt thẻ — ô `HuongDan` từ nay thuần phần người soạn (QD-26).
    """
    if not rec:
        return ""
    cap = cap_the_html(rec)
    bang = build_table(rec, phan_tich)
    return (cap + bang) if (cap or bang) else ""


def build_table(rec, phan_tich=None):
    """HTML bảng chia ĐẦY ĐỦ ('' nếu từ này không biến cách / không có dữ liệu).

    🔴 MỌI từ có biến cách đều được bảng, không chỉ từ bất thường — user đổi
    quyết định 29/07: *"toàn bộ từ sẽ có bảng toàn bộ cách chia, làm sao thu gọn
    nhất có thể; cái này để tiện tra cứu về sau"*. Bộ phát hiện bất thường
    (`analyze`) đổi vai: nó không còn quyết định CÓ bảng hay không, mà chỉ (a) tô
    sáng ô biến đổi và (b) nhắc người soạn lô viết câu chú ý ở trên — đọc câu đó
    là hiểu cả bảng, bảng chỉ để tra cứu chi tiết.

    🔴 KHÔNG còn bọc `<details>` riêng (QD-26, 04/08/2026). Trước đây bảng nằm
    TRONG ô Hướng dẫn nên phải tự gấp lại; nay nó sống ở field `BangMay`, mà cả
    field đó đã là một ô thu gọn ⇒ bọc thêm lần nữa là bắt user bấm HAI lần mới
    thấy bảng. Trần "vừa một màn hình iPhone" vẫn giữ nguyên: ô ngoài đóng sẵn.
    """
    if not rec:
        return ""
    nong = (phan_tich or analyze(rec))["nong"]
    than = _BANG.get(rec.get("pos"))
    ruot = than(rec, nong) if than else ""
    if not ruot.strip():
        return ""

    if rec.get("declInfo"):
        # Chú giải NGƯỜI THẬT viết trong từ điển ("The forms with н- are used if
        # after a preposition") — quý hơn mọi thứ suy ra được, và đúng loại mà
        # agent tự nghĩ hay nói sai. Giữ nguyên văn, ghi rõ là của từ điển.
        ruot += f'<div class="gt-chu">📖 {rec["declInfo"]}</div>'

    ngo = ('<div class="gt-nguon">⚠️ Ô có dấu <b>?</b>: từ điển KHÔNG ghi trọng âm '
           '— chưa kiểm được, đừng học thuộc chỗ nhấn ở đó.</div>'
           if 'class="gt-ngo"' in ruot else "")
    nguon = "Wiktionary tiếng Nga" if rec.get("nguon") == "wiktionary" else "OpenRussian"
    return (f'<div class="gt-body">{ruot}{ngo}'
            f'<div class="gt-nguon">Nguồn: {nguon} — máy dựng, không qua AI. '
            'Ô sáng = chỗ biến đổi.</div>'
            '</div>')
