# 🎯 VIỆC ĐANG LÀM

> Phiếu bị GHI ĐÈ ở việc kế tiếp. Xong phiên: để TRỐNG hoặc chừa đúng MỘT đầu
> việc (cửa **S19**, QD-25). Việc chưa tới lượt ⇒ `SONO.md` kèm HẠN XOÁ.

**Hai bug bắt được lúc nạp thô A1–A2 (16/10/2026)** — sửa ngay sau commit nạp, mỗi cái 1 test (L3):
1. `anki_client.get_known_words()` trả `set()` RỖNG thay vì `None` khi AnkiConnect báo
   lỗi (`result` là None lúc Anki đang sync: "Collection lifecycle operation is active")
   — vi phạm hợp đồng "None ≠ rỗng" trong chính docstring của nó. Soát luôn
   `doc_grammar_json_tat_ca` cùng kiểu.
2. 🔑 `audio.py:55` `log_fail(f"Google TTS lỗi mạng: {e}")` in NGUYÊN URL có
   `?key=<GOOGLE_TTS_API_KEY>` ra log (thấy khi mạng rớt 15/10) — cắt query khỏi `e`.
