# ==============================================================================
# --- THẺ CHI PHỐI: từ nào bắt từ đứng sau nó dùng cách nào ---
#
# Chi phối (`звони́ть` + cách 3, `в` + cách 4 hay 6) KHÔNG suy được từ nghĩa hay
# từ tiếng Anh — nó là TỪ VỰNG, phải nhớ theo từng từ. Nên chữa bằng thẻ nhớ,
# không bằng bài tập điền từ.
#
# 🔴 NGƯỜI SOẠN chỉ viết 4 cột trong `data/chi_phoi.tsv`:
#        giới_từ  ·  từ_nguyên_thể  ·  cách  ·  dòng_tiếng_Việt
#    Cụm tiếng Nga và dòng đối chiếu đều do FILE NÀY sinh ra lúc nạp, lấy từ
#    bảng chia trong ô `GrammarJSON` của chính thẻ từ vựng.
#
#    Vì sao KHÔNG cho gõ tay cụm Nga vào file dữ liệu — hai lý do, cả hai đều là
#    hỏng im lặng:
#    1. Gõ tay thì máy hết đường soát. Sinh từ bảng chia thì `soat()` so lại
#       được, lệch một ký tự là ĐỎ ngay.
#    2. Dòng đối chiếu gom theo DANH TỪ, mà lô soạn theo từng nhóm nhỏ ⇒ thẻ
#       làm trước KHÔNG THỂ biết thẻ làm sau. Viết tay là nó mục ngay trong lô
#       đầu, và không có gì nhắc quay lại sửa. Sinh lại mỗi lần nạp thì không.
#
# Mọi lệnh gọi AnkiConnect đi qua `cards.py` — cửa duy nhất của mảng này (L1).
# ==============================================================================
import os
import sys

from anki_tools.anki_client import doc_grammar_json_tat_ca
from anki_tools.utils import log_fail, log_info, log_warn, strip_accents_perfectly

from . import cards
from .config import (
    BIEN_THE_GOC,
    CACH_KHOA,
    CHIPHOI_DECK_GIOITU,
    CHIPHOI_MODEL,
    CHIPHOI_TSV,
)

_GOC_REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def duong_dan_tsv():
    """Đường dẫn tuyệt đối tới file dữ liệu — không phụ thuộc thư mục đang đứng."""
    return os.path.join(_GOC_REPO, CHIPHOI_TSV.replace("/", os.sep))


def khong_dau(text):
    """Bỏ dấu nhấn + quy `ё`→`е` để so khớp. Dùng lại hàm chung của `anki_tools`.

    🔴 ĐỪNG viết hàm chuẩn hoá tiếng Nga thứ hai ở đây: repo từng đẻ ra 4 hàm
    cùng vai, và lệch nhau một ký tự là người gõ ĐÚNG bị chấm SAI mà không có
    gì báo.
    """
    return strip_accents_perfectly(text or "").replace("ё", "е").replace("Ё", "Е").strip().lower()


# ------------------------------------------------------------------ đọc dữ liệu
def doc_tsv(path=None):
    """Đọc file dữ liệu -> list dict. Bỏ dòng trống và dòng `#`.

    Trả về (danh_sách, lỗi_cú_pháp). Dòng sai số cột thì KÊU chứ không bỏ qua
    im lặng — bỏ qua là thiếu thẻ mà không ai biết.
    """
    path = path or duong_dan_tsv()
    ra, loi = [], []
    with open(path, encoding="utf-8") as f:
        for so, dong in enumerate(f, 1):
            dong = dong.rstrip("\n").rstrip("\r")
            if not dong.strip() or dong.lstrip().startswith("#"):
                continue
            cot = dong.split("\t")
            if len(cot) != 4:
                loi.append(f"dòng {so}: có {len(cot)} cột, cần đúng 4 (ngăn bằng TAB)")
                continue
            gt, lemma, cach, viet = (c.strip() for c in cot)
            if cach not in CACH_KHOA:
                loi.append(f"dòng {so}: cách {cach!r} không hợp lệ (chỉ 1–6)")
                continue
            ra.append({"so_dong": so, "gt_hien": gt, "gt_goc": BIEN_THE_GOC.get(gt, gt),
                       "lemma": lemma, "cach": cach, "viet": viet})
    return ra, loi


# ------------------------------------------------- ghép đáp án từ bảng chia
def _bang_chia(rec):
    """Bảng chia của một bản ghi, bất kể nó là danh từ, đại từ hay số từ.

    Ba loại từ dùng ba khoá khác nhau và LỒNG KHÁC NHAU trong dữ liệu
    OpenRussian: danh từ `decl.sg.<cách>`, đại từ `proDecl.m.<cách>`, số từ
    `numDecl.<cách>`. Trả về dict phẳng {cách: dạng} hoặc None.
    """
    for khoa, duong in (("decl", ("sg",)), ("proDecl", ("m",)), ("numDecl", ())):
        b = rec.get(khoa)
        if not isinstance(b, dict):
            continue
        for buoc in duong:
            b = b.get(buoc) if isinstance(b, dict) else None
        if isinstance(b, dict) and any(b.get(k) for k in CACH_KHOA.values()):
            return b
    return None


def dang_chia(rec, cach):
    """Dạng chia của từ ở `cách`, hoặc None. Nhiều biến thể thì lấy cái đầu."""
    bang = _bang_chia(rec) or {}
    o = bang.get(CACH_KHOA[cach])
    if not o:
        return None
    return o.replace("/", ",").split(",")[0].strip() or None


# ---------------------------------------------------------------- cửa soát
def soat(rows, tra_ngu_phap):
    """Soi dữ liệu trước khi nạp. Trả về list lời báo lỗi (rỗng = sạch).

    Bốn thứ máy bắt được. Thứ NĂM — dòng tiếng Việt mơ hồ kiểu "ở trường" ứng
    với cả `в шко́ле` lẫn `в шко́лу` — máy chịu, phải người đọc: đó là lý do
    quy trình bắt user duyệt từng lô.
    """
    loi = []
    thay = {}
    for r in rows:
        lem_c = khong_dau(r["lemma"])
        rec = tra_ngu_phap.get(r["lemma"]) or tra_ngu_phap.get(lem_c)
        if rec is None:
            for k, v in tra_ngu_phap.items():
                if khong_dau(k) == lem_c:
                    rec = v
                    break

        # 1. Từ chưa có trong deck từ vựng ⇒ không có bảng chia để ghép đáp án.
        if rec is None:
            loi.append(f"dòng {r['so_dong']}: '{r['lemma']}' chưa có trong deck từ vựng "
                       f"⇒ không lấy được bảng chia. Thêm từ này vào deck trước, "
                       f"hoặc đổi sang từ khác.")
            continue

        # 2. Bảng chia thiếu đúng cái cách đang cần.
        form = dang_chia(rec, r["cach"])
        if not form:
            loi.append(f"dòng {r['so_dong']}: bảng chia của '{r['lemma']}' không có "
                       f"cách {r['cach']} (từ này có thể không biến cách).")
            continue
        r["form"] = form
        # Dạng nguyên thể CÓ DẤU NHẤN để hiện mặt trước. Người soạn gõ không dấu
        # cho nhanh (`школа`), nhưng thẻ phải hiện `шко́ла` — cả deck từ vựng đều
        # có dấu nhấn, thiếu ở đây là user học sai trọng âm mà không có gì báo.
        r["lemma_acc"] = rec.get("acc") or r["lemma"]

        # 3. Hai thẻ CÙNG danh từ CÙNG cách ⇒ chắc chắn thừa một, hoặc sai một.
        khoa = (lem_c, r["cach"])
        if khoa in thay:
            loi.append(f"dòng {r['so_dong']}: trùng với dòng {thay[khoa]['so_dong']} — "
                       f"cùng '{r['lemma']}' cùng cách {r['cach']}. Một trong hai thừa.")
        else:
            thay[khoa] = r

    # 4. Cùng danh từ, khác cách, mà dòng tiếng Việt GIỐNG HỆT ⇒ đề bài không có
    #    đáp án đúng: user gõ đúng vẫn bị chấm sai rồi bấm Again, tức là HỌC
    #    NGƯỢC. Đây là kiểu hỏng đắt nhất vì không kêu tiếng nào.
    theo_lemma = {}
    for r in rows:
        theo_lemma.setdefault(khong_dau(r["lemma"]), []).append(r)
    for lem, ds in theo_lemma.items():
        for i in range(len(ds)):
            for j in range(i + 1, len(ds)):
                a, b = ds[i], ds[j]
                if a["cach"] != b["cach"] and a["viet"].lower() == b["viet"].lower():
                    loi.append(f"dòng {a['so_dong']} và {b['so_dong']}: cùng '{a['lemma']}' "
                               f"nhưng dòng tiếng Việt GIỐNG HỆT ⇒ đề bài có hai đáp án "
                               f"đúng. Viết rõ ra: 'đi vào trường' vs 'đang ở trong trường'.")
    return loi


# ------------------------------------------------------------- dựng thẻ
def dung_doi_chieu(row, cung_lemma):
    """HTML các cách KHÁC của cùng danh từ. Rỗng nếu từ này chỉ có một thẻ.

    Gom theo DANH TỪ chứ không theo giới từ: cặp đáng giá nhất bắt chéo hai giới
    từ (`на рабо́ту` đi tới ↔ `с рабо́ты` từ đó về), gom theo giới từ là mất đúng
    cặp ấy.
    """
    manh = []
    for k in cung_lemma:
        if k is row:
            continue
        manh.append(
            f'<span class="c-cum">{k["gt_hien"]} {k["form"]}</span>'
            f'<span class="c-cach">cách {k["cach"]}</span>'
            f'<span class="c-ngh">{k["viet"]}</span>'
        )
    return "".join(manh)


def ten_deck(gt_goc, rows_cua_gt, nghia):
    """`GRAMMAR::chi phối::giới từ::в — cách 4/6 — trong, ở trong, vào`

    Tên deck ghi CẢ CÁCH LẪN NGHĨA vì cuộn danh sách deck trên iPhone cũng là
    một lượt ôn, và 14 dòng chữ Nga trơn thì trông giống hệt nhau.
    """
    cac_cach = sorted({r["cach"] for r in rows_cua_gt})
    phan_cach = "cách " + "/".join(cac_cach)
    phan_nghia = (nghia or "").replace("::", " ").replace('"', "").strip()
    if len(phan_nghia) > 30:
        phan_nghia = phan_nghia[:30].rsplit(",", 1)[0].rstrip(" ,") + "…"
    ten = f"{gt_goc} — {phan_cach}" + (f" — {phan_nghia}" if phan_nghia else "")
    return f"{CHIPHOI_DECK_GIOITU}::{ten}"


def dung_the(rows, nghia_gt):
    """rows (đã qua `soat`) -> list (deck, fields, tags)."""
    theo_lemma = {}
    for r in rows:
        theo_lemma.setdefault(khong_dau(r["lemma"]), []).append(r)
    theo_gt = {}
    for r in rows:
        theo_gt.setdefault(r["gt_goc"], []).append(r)

    ra = []
    for r in rows:
        cum = f'{r["gt_hien"]} {r["form"]}'
        fields = {
            "Khoa": f'{r["gt_hien"]}|{khong_dau(r["lemma"])}|{r["cach"]}',
            "GioiTu": r["gt_goc"],
            "Lemma": r.get("lemma_acc") or r["lemma"],
            "Cum": cum,
            "CumClean": strip_accents_perfectly(cum),
            "Cach": f'cách {r["cach"]}',
            "Vietnamese": r["viet"],
            "DoiChieu": dung_doi_chieu(r, theo_lemma[khong_dau(r["lemma"])]),
            "Nguon": "bảng",
        }
        deck = ten_deck(r["gt_goc"], theo_gt[r["gt_goc"]], nghia_gt.get(r["gt_goc"], ""))
        ra.append((deck, fields, [f'cach::{r["cach"]}', "chiphoi::giới-từ"]))
    return ra


# ------------------------------------------------------------------ nạp
def nap(apply=False):
    """Soát rồi (nếu `apply`) ghi thẻ vào Anki. Trả về mã thoát cho `sys.exit`."""
    rows, loi_cu_phap = doc_tsv()
    if loi_cu_phap:
        for l in loi_cu_phap:
            log_fail(l)
        return 1
    log_info(f"Đọc {len(rows)} dòng từ {CHIPHOI_TSV}")

    try:
        tra = doc_grammar_json_tat_ca()
    except Exception as e:
        log_fail(f"Không đọc được dữ liệu ngữ pháp từ Anki: {e}. Mở Anki rồi chạy lại.")
        return 1

    loi = soat(rows, tra)
    if loi:
        for l in loi:
            log_fail(l)
        log_fail(f"{len(loi)} lỗi — KHÔNG nạp gì cả. Sửa `{CHIPHOI_TSV}` rồi chạy lại.")
        return 1

    nghia_gt = cards.doc_nghia_tu_vung(sorted({r["gt_goc"] for r in rows}))
    the = dung_the(rows, nghia_gt)

    if not apply:
        print(f"\n✅ {len(the)} thẻ hợp lệ, đáp án đều ghép được từ bảng chia.\n")
        deck_hien = None
        for deck, f, tags in the:
            if deck != deck_hien:
                deck_hien = deck
                print(f"  📚 {deck}")
            print(f"      {f['Cum']:<22} {f['Cach']:<8} {f['Vietnamese']}")
        print(f"\n(chạy lại kèm `--apply` để ghi {len(the)} thẻ vào Anki)")
        return 0

    them = bo_qua = hong = 0
    for deck, f, tags in the:
        cu = cards.anki("findNotes",
                        query=f'note:"{CHIPHOI_MODEL}" Khoa:"{f["Khoa"]}"') or []
        if cu:
            cards.update_note(cu[0], f)      # giữ note_id ⇒ tiến trình học không mất
            bo_qua += 1
            continue
        note_id, err = cards.add_note(f, deck=deck, tags=tags, model=CHIPHOI_MODEL)
        if note_id:
            them += 1
        else:
            hong += 1
            log_warn(f"{f['Cum']}: {err}")
    log_info(f"Xong — thêm mới {them} · cập nhật {bo_qua} · hỏng {hong}")
    return 0 if not hong else 1


if __name__ == "__main__":
    sys.exit(nap(apply="--apply" in sys.argv))
