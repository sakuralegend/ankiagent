# 📜 Nhật ký thay đổi (CHANGELOG)

> File này là "bộ nhớ chung" của dự án: mỗi lần sửa gì đều ghi vào đây (mới nhất ở TRÊN CÙNG),
> để phiên chat mới / người mới đọc là nắm được ngay hệ thống đã đi qua những gì.
> Quy ước mỗi mục: **ngày — commit — làm gì + vì sao**.

## 19/07/2026 (đợt 5)

- **Tách bot.py (~1.400 dòng) thành gói tgbot/ theo luồng** — user hỏi file dài
  có sao không: chạy thì không sao, nhưng khó bảo trì (6 luồng chen 1 file).
  bot.py giờ CHỈ là điểm vào ~10 dòng (systemd `python bot.py` giữ nguyên,
  không phải sửa service). Gói tgbot/: core (phiên/deck/menu/idle/format),
  commands (/start /menu /deck /thongke /don /sync + job 3h sáng), flow_add
  (thêm từ + dò trùng + đoán lemma), flow_edit (/sua + /suadeck), flow_scan
  (📷 quét ảnh), dispatch (on_word + on_callback — chỉ chia việc, không nghiệp
  vụ), app (lắp handler + khởi động). Import một chiều core <- flows <-
  dispatch <- app, không vòng. Đường dẫn last_deck.json / suadeck_resume.json
  vẫn ở gốc repo (_PROJECT_ROOT trong core.py). Kiểm bằng AST: 48/49 hàm giống
  HỆT bản cũ; hàm duy nhất khác là _idle_reset_job (chủ đích: reset phiên giờ
  dọn thêm scan_words/scan_msg của luồng quét ảnh). Các file khác đều <500
  dòng, chưa cần tách.

- **📷 Quét ảnh trang sách qua bot: OCR từ tiếng Nga -> duyệt -> thêm loạt vào inbox**
  — user chụp trang sách gửi bot, muốn gom từ mới hàng loạt thay vì gõ tay từng
  từ. NGUYÊN TẮC user chốt: bot CHỈ xử lý thô, thêm hay không LUÔN phải qua nút
  ✅ xác nhận, không tự ý. Luồng: (a) ai_client.call_claude_scan_words(): 1 request
  Gemini duy nhất/trang (ảnh base64 qua endpoint OpenAI-compatible sẵn có,
  max_tokens=3000) — OCR + đưa mọi từ về lemma, loại tên riêng, validate chỉ
  nhận Cyrillic; _send_ai_request/_call_model_once thêm tham số max_tokens.
  (b) anki_client.get_known_words(): set WordClean toàn kho để lọc từ đã có
  (None = lỗi ≠ set rỗng, tránh đề nghị thêm trùng cả kho). (c) bot.py: handler
  ảnh on_photo (filters.PHOTO) -> danh sách từ MỚI đánh số + nút "✅ Thêm cả N
  từ"/"🚫 Hủy", nhắn 'bỏ 3 7 12' để loại từ trước khi thêm; _run_scan_add chạy
  nền như /suadeck (nghỉ 3s/từ chống RPM, nút ⏹ Dừng, dò trùng lại từng từ
  trước khi thêm, sync 1 lần cuối đợt); thẻ vào RUSSIAN::0-inbox theo chế độ
  tự động. Test thật với ảnh chữ Nga tự tạo: OCR + lemma + loại tên riêng OK
  (lưu ý: lemma thi thoảng lệch kiểu цветы->цвет thay vì цветок — user duyệt
  tay là lưới an toàn).

- **Deck hứng RUSSIAN::0-inbox: học từ mới một chỗ, tốt nghiệp tự về deck chủ đề**
  — user tồn ~200 từ chưa học + 40-50 từ mới/ngày cần ưu tiên, muốn học gom một
  chỗ rồi thẻ thuộc rồi mới về deck chủ đề để ôn. Thiết kế: tag topic:: (AI gắn
  từ đầu) là "địa chỉ nhà", deck chỉ là chỗ ở tạm. (a) config.py thêm INBOX_DECK;
  chế độ tự động của push_to_anki đưa thẻ mới vào inbox thay vì deck chủ đề.
  (b) anki_client.move_graduated_from_inbox(): thẻ inbox đạt is:review (tốt
  nghiệp learning) -> changeDeck về RUSSIAN::<slug tag>, lịch ôn giữ nguyên.
  (c) bot: lệnh /don chạy tay + job nền 3h sáng (asyncio, không cần PTB
  job-queue), đêm có chuyển thẻ mới nhắn Telegram. (d) build_subdecks.py chừa
  thẻ inbox ra (không bốc thẻ chưa học đi). (e) setup_inbox.py (idempotent):
  ép preset Default luật user chốt "ôn HẾT thẻ cũ (hạn cũ nhất trước) rồi mới
  hiện thẻ mới" (newMix=1, reviewOrder=0 — vốn đã đúng sẵn), preset riêng
  'inbox' (newGatherPriority=2: từ THÊM GẦN NHẤT học trước để ưu tiên từ trong
  ngày, 50 từ mới/ngày), gom 187 thẻ is:new rải rác về inbox. Đã chạy + sync.

## 19/07/2026 (đợt 2)

- **Dọn note type: xóa 4 model chết + đổi tên ngắn gọn** — user thấy còn dấu
  vết nhiều lần sửa: 4 model Russian_Irregular_Plural_OLED v1→v4 (0 note) và
  2 tên dài lê thê. AnkiConnect KHÔNG có lệnh xóa/đổi tên model, nên làm bằng
  thư viện `pip anki==26.5` (khớp đúng bản desktop, tránh lệch schema): đóng
  Anki (guiExitAnki bị ngó lơ -> CloseMainWindow), backup collection.anki2
  (collection-backup-truoc-don-model-19-07.anki2 trong Anki2/User 1), xóa 4
  model chết, đổi `Russian_Premium_OLED_Type_v25`->**RU_Word** (610 note),
  `Russian_Irregular_Plural_OLED_v5`->**RU_Plural** (26 note). Gỡ luôn tag
  `Irregular_Plural_v5` (26 thẻ — lọc bằng note:"RU_Plural" là đủ). Sửa
  MODEL_NAME trong config.py. ⚠️ Xóa model = đổi schema -> Anki đòi FULL SYNC:
  PC chọn **Upload**, VPS (vnc.bat) chọn **Download**; bot dừng trong lúc
  migrate để không tự tạo lại model.

## 19/07/2026

- **Dọn 15 tag mồ côi sau tái cấu trúc** — sau đợt đổi cây 2 tầng, 15 tag tên
  cũ (topic::food, topic::other, topic::colors...) vẫn nằm trong danh sách tag
  của Anki dù không còn note nào dùng. Chạy clearUnusedTags (chỉ xóa tag 0 note,
  không đụng thẻ) + sync. Còn lại đúng 19 tag topic:: mới + Irregular_Plural_v5
  (+ 3 mục tổ tiên topic/concepts/language Anki tự giữ làm nút cây). Cùng phiên:
  xác nhận "colors 0 thẻ" là hiểu nhầm — số cạnh deck là thẻ ĐẾN HẠN hôm nay,
  không phải tổng; deck colors vẫn đủ 12 thẻ, kiểm bằng Browse
  `deck:RUSSIAN::qualities::colors`.

## 18/07/2026 (đợt 3)

- **Chuyển cây phẳng 19 chủ đề -> CÂY 2 TẦNG, 10 GỐC CỐ ĐỊNH** — user chỉ ra
  lỗi thiết kế: tách kiểu đợt 2 (thêm chủ đề vào tầng gốc) làm gốc phình vô hạn.
  Chốt: tầng gốc = 10 miền BẤT BIẾN (people, life, nature, places, language,
  time, numbers, actions, qualities, concepts), mỗi tầng ≤10 mục, từ nay chỉ
  thêm NHÁNH CON (vd actions::motion). Slug lồng cấp bằng :: (tag topic::life::food
  = MỘT tag, Anki hiện lồng dưới topic::life; lọc theo tag cha vẫn bắt được con).
  Kỹ thuật: topics.py thêm FALLBACK_TOPIC (concepts::misc) + LEGACY_ALIASES
  (bảng dịch slug cũ->mới, dùng cho mọi lần đổi tên sau); tag_topics --fix giờ
  dịch được cả tag của từ AI phân loại (không có trong bảng tra) qua alias;
  build_subdecks + get_topic_stats viết lại đọc tag TỪNG note phía Python
  (query tag:"cha" của Anki khớp cả tag con -> đếm đúp/chuyển sai khi lồng cấp),
  build_subdecks tự xóa cả deck RUSSIAN::* mồ côi sau đổi cấu trúc. Đã chạy:
  397 thẻ đổi tag, 609 thẻ về đúng 19 deck lá dưới 10 gốc, 15 deck phẳng cũ đã
  xóa, misc 5%, không deck nào ≥100. /thongke đọc FALLBACK_TOPIC thay 'other'.

## 18/07/2026 (đợt 2)

- **Tách 'other' thành function-words + abstract (17 -> 19 chủ đề)** — /thongke
  báo other 16% (>15%) ngay lần đầu, user hỏi cách sửa. Tách TẦNG GỐC (không
  lồng dưới other vì other là "vườn ươm": cụm nào đủ lớn thì bứng ra):
  `function-words` (35 thẻ: đại từ, trợ từ, liên từ, câu hỏi, можно/нельзя) +
  `abstract` (27 thẻ: правда, счастье, работа...). other còn 36 thẻ (5%) — hết
  cảnh báo. Kỹ thuật: tag_topics.py thêm chế độ `--fix` (đổi tag thẻ ĐÃ có tag
  cho khớp bảng tra; CHỈ đụng từ có trong bảng, từ AI phân loại giữ nguyên —
  dùng lại được cho mọi lần tách chủ đề sau) -> build_subdecks.py --apply tạo
  2 deck con mới + dọn thẻ + sync. AI prompt tự nhận 19 chủ đề qua
  topics_prompt_block(), không phải sửa prompt.

## 18/07/2026

- **Lệnh /thongke + quy tắc phát hiện khi nào cần tách deck** — user hỏi 17 chủ
  đề có bao trọn tiếng Nga lâu dài không (hiện A1, lo lên A2/B1). Kết luận đã
  bàn: 17 chủ đề bao trọn về NGỮ NGHĨA (other hứng phần dư) nhưng sẽ phình khi
  lên cấp; quy tắc đèn báo = deck con ≥100 thẻ HOẶC other >15% kho thì tách.
  Tách = thêm slug LỒNG CẤP dạng `actions::motion-verbs` vào topics.py (tag và
  deck Anki đều phân cấp bằng :: nên cây tự rẽ nhánh, không sửa code) + retag
  cụm từ cũ + chạy build_subdecks.py --apply. /thongke: đếm thẻ theo chủ đề
  (get_topic_stats trong anki_client.py), hiện bảng xếp hạng + cảnh báo 3 loại
  (deck chạm 100 / other quá 15% / thẻ chưa có tag). Ghi chú hiện trạng: other
  đang 16% (98/609) — ứng viên tách đầu tiên là function-words (đại từ, trợ từ).

## 16/07/2026 (đợt 2)

- **Cây deck kho RUSSIAN::<topic> + chế độ thêm từ TỰ ĐỘNG** — user muốn deck
  tổng làm kho, học theo deck con chủ đề, tiến độ cộng dồn lên kho (KHÔNG dùng
  Filtered Deck vì học xong thẻ biến mất). Tên kho tiếng Anh "RUSSIAN" theo yêu
  cầu user (dễ gõ hơn Cyrillic), đổi được qua env TOPIC_DECK_PARENT (config.py).
  (1) `build_subdecks.py`: tạo RUSSIAN + 17 deck con, chuyển 609 thẻ về đúng
  deck con theo tag topic:: (changeDeck không ảnh hưởng lịch ôn — đã kiểm tra
  interval giữ nguyên), xóa 10 deck cũ đã trống, GIỮ deck Irregular (26 thẻ
  không thuộc model bot), sync. Dry-run mặc định, --apply làm thật, chạy lại
  vô hại. Lưu ý: 610 note -> 609 vì 1 note hỏng (không có card, deck "?") đã
  biến mất trước đó.
  (2) Chế độ TỰ ĐỘNG: deck_name=None xuyên suốt pipeline -> push_to_anki tự
  đặt thẻ vào RUSSIAN::<topic AI chọn> (không có topic -> ::other), createDeck
  idempotent trước khi add. Bot: không bắt chọn deck nữa (None = tự động, là
  mặc định + sau idle reset); bảng chọn deck thêm nút "🤖 Tự động theo chủ đề";
  chặn "📦 Chuyển deck" trong luồng từ trùng khi đang tự động (không có deck
  hiện tại). CLI main.py: Enter bỏ trống tên deck = tự động.
  Giới hạn bài/ngày KHÔNG cần chỉnh 9999 như các hướng dẫn cũ: Anki >= 23.10
  dùng v3 scheduler, bấm thẳng deck con thì giới hạn của deck mẹ được BỎ QUA.

## 16/07/2026

- **Nút "🕘 Deck gần nhất" trong bảng chọn deck của bot** — đỡ phải bấm
  Deck có sẵn → chọn lại sau mỗi lần phiên reset (nghỉ >3 phút). Deck vừa chọn
  (mọi ngả: nút danh sách, /deck <tên>, gõ tên deck mới) đều đi qua hàm chung
  `_set_deck()` → ghi `last_deck.json` (gitignore) nên nhớ được cả khi bot
  restart trên VPS. Bấm nút: kiểm tra deck còn tồn tại (KHÔNG dùng
  ensure_deck_exists để khỏi tự tạo lại deck user đã xóa; deck chết → quên file
  + mời chọn lại). Callback cố định `deck:last` vì tên deck Cyrillic có thể
  vượt 64 byte callback_data.
- **Bỏ tag kỹ thuật OpenRussian_*_v25** — user chê rác. Không code nào tra thẻ
  theo 2 tag này (nhận diện thẻ của bot luôn qua model name
  `Russian_Premium_OLED_Type_v25`), nên: gỡ khỏi 610 thẻ (removeTags: 229 thẻ
  AI_OLED + 381 thẻ Pure) + clearUnusedTags; `push_to_anki` không gắn nữa —
  thẻ mới giờ CHỈ có tag `topic::...`.
- **Tag chủ đề cho toàn bộ từ vựng (topic::...)** — 17 chủ đề (people-family,
  professions, body, food, home-objects, clothing, animals, nature-plants,
  weather, time, numbers, colors, places-city, education, actions, qualities
  [CHỈ tính từ+trạng từ], other [không nhét được vào đâu]), user chốt qua thảo
  luận. Danh sách chủ đề định nghĩa MỘT nơi: `anki_tools/topics.py`.
  (1) 610 thẻ có sẵn: gắn bằng `tag_topics.py` (bảng tra thủ công, addTags —
  không đụng nội dung/tiến độ học; idempotent: thẻ đã có topic:: thì bỏ qua;
  dry-run mặc định, `--apply` mới gắn thật). Đã chạy, đủ 610/610.
  (2) Từ mới: AI chọn topic trong CÙNG request sinh ví dụ (thêm trường "topic"
  vào JSON schema + few-shot của `_CORE_SYSTEM_PROMPT`; validate ép về "other"
  nếu sai/thiếu — KHÔNG làm hỏng kết quả; nhánh fallback không AI → không gắn
  tag, gắn bù bằng `python tag_topics.py --missing` [AI phân loại từng thẻ lẻ,
  hàm `call_claude_topic`]). Chuỗi truyền: build_examples_html trả thêm
  topic_slug → push_to_anki gắn tags + đưa vào card_info["topic"] → CLI và bot
  Telegram hiện dòng "📂 topic::...". Quy tắc phân loại: mỗi từ đúng 1 tag,
  theo nghĩa phổ biến nhất (mùa→time, động từ ăn uống→food, tính từ thời
  tiết→weather, màu→colors).

## 15/07/2026

- **Đổi phông viết tay sang Propisi Regular** (theo yêu cầu user sau khi dùng thử
  Marck Script) — Propisi (ParaGraph 1997) là font làm ĐÚNG theo mẫu chữ vở tập
  viết trường Nga, chuẩn hơn Marck Script. `_propisi.ttf` (41KB, đủ bảng chữ
  Cyrillic hoa+thường, đã kiểm bằng fontTools) nạp vào collection.media;
  `.cursive-word` dùng "Propisi" với "MarckScript" làm dự phòng, cỡ 34px.
  Nguồn font: wfonts.com/font/propisi (free).
- **Phông chữ viết tay Nga trên thẻ (Marck Script)** — dòng chữ nghiêng ở mặt sau
  thẻ vốn để luyện đọc chữ viết tay Nga nhưng phông hệ thống nghiêng không ra dạng
  viết tay. Đổi sang Marck Script (giống chữ vở tập viết пропись: т→m, д→g), user
  chọn qua trang preview 3 phông (Marck/Bad Script/Caveat). Font nhúng vào Anki:
  file `_marckscript.ttf` trong collection.media (storeMediaFile) → tự sync mọi
  thiết bị, offline OK. Dòng viết tay đổi từ {{Word}} → {{WordClean}} (bỏ dấu
  trọng âm — Marck Script không có ký tự dấu ghép ◌́ nên bị vỡ phông), cỡ chữ
  18→32px, bỏ font-style italic.
- **Vá lỗi RPM cho /suadeck + tính năng Sửa tiếp** — đợt sửa deck Матрёшка (309 thẻ)
  bị 44 lỗi vì model lite trả lời nhanh → vòng lặp bắn >15 lượt/phút (trần RPM
  free là 15); code cũ coi mọi 429 là hết quota ngày nên nhảy sang model dự phòng
  (quota bé) rồi chết. Fix: (1) 429 KHÔNG có chữ "PerDay" = giới hạn mỗi phút →
  chờ đúng retryDelay Google gợi ý (tối đa 2 lần) rồi thử lại CHÍNH model đó;
  (2) batch nghỉ 3s giữa 2 thẻ (~10 lượt/phút < 15); (3) batch dừng/lỗi → lưu
  danh sách thẻ còn dở vào `suadeck_resume.json` (gitignore) → /suadeck lần sau
  hỏi "▶️ Sửa tiếp N thẻ". Đợt Матрёшка được cứu bằng script quét mod-time trên
  VPS: xác nhận đúng 200 thẻ đã sửa, 109 thẻ dở đã vào danh sách Sửa tiếp.
- **/suadeck — sửa TOÀN BỘ thẻ trong 1 deck** (tính năng ít dùng nên là lệnh riêng
  trong danh sách "/", KHÔNG chiếm chỗ menu chính). Luồng toàn nút: chọn deck →
  kiểu sửa (1/2/3/tự viết) → màn xác nhận (số thẻ, ước tính thời gian, cảnh báo
  nếu >450 thẻ vì quota Gemini 500/ngày) → chạy nền. Tiến độ = ĐÚNG 1 tin nhắn
  tự cập nhật tại chỗ (thẻ i/N, vừa xong từ nào ✅/❌, đếm xong/lỗi) + nút ⏹ Dừng.
  Xong/dừng: sync AnkiWeb 1 lần, tổng kết liệt kê ≤10 từ lỗi (thẻ lỗi giữ nguyên
  nhờ OUTPUT CONTRACT + validate). Kỹ thuật: `get_deck_note_ids()` (anki_client),
  tách lõi `refine_note_id()` từ `refine_note()` (pipeline), batch chạy
  `asyncio.create_task` vì PTB xử lý update tuần tự (không thì nút Dừng chết),
  guard `sd_running` chống chạy 2 đợt, idle timer được đẩy mỗi thẻ.
- **Giao diện "bấm trước, gõ sau" (đỡ đổi bàn phím Nga↔Latin)** — user dùng bàn phím
  tiếng Nga liên tục nên gõ lệnh kiểu `/sua <từ>` rất bất tiện. Đổi logic:
  `/sua` (hoặc nút ✏️ Sửa thẻ) → bot hỏi "gõ từ cần sửa" → gõ từ → nút chọn kiểu sửa;
  nút "Tự viết yêu cầu" → bot hỏi → gõ thẳng yêu cầu (không cần gõ lại lệnh/từ).
  **Xóa lệnh `c` đổi deck** — đổi deck chỉ qua `/deck` hoặc nút 📚.
  Kỹ thuật: trạng thái chờ `user_data["awaiting"]` = `sua_word` / `sua_custom`,
  idle reset có dọn. Đường tắt `/deck <tên>`, `/sua <từ> [yêu cầu]` vẫn chạy ngầm.
- **vnc.bat** — double-click là xem màn hình Anki trên VPS: tự mở đường hầm SSH
  (cổng 15900, không hỏi pass nhờ SSH key) rồi bật TightVNC Viewer
  (`C:\Program Files\TightVNC\tvnviewer.exe`). Đóng cửa sổ SSH thu nhỏ = ngắt VNC.
- **Quyết định: KHÔNG cập nhật Anki trên VPS** dù có thông báo bản mới — hệ đang
  chạy ổn, addon AnkiConnect từng phải vá tay, bản trong Docker image chỉ đổi khi
  chủ động `docker compose pull`. Chỉ cập nhật khi AnkiWeb từ chối sync vì
  "client quá cũ" (lúc đó làm cùng Claude để có đường lùi).

- **Reset 3 phút gọn hơn + menu liền** — tin nhắn reset giờ chỉ báo "đã reset phiên"
  (nói rõ chỉ quên deck đang chọn, thẻ trong Anki không mất gì) và kèm luôn menu nút bấm
  y hệt `/menu` trong cùng 1 tin, để lần vào tới bấm chọn ngay.
- **Từ không có trên OpenRussian → AI đoán từ nguyên mẫu** — gõ từ biến cách
  (vd `дома`) hoặc sai chính tả (vd `хорошшо`): bot nhờ Gemini đoán dạng từ điển
  (lemma) + giải thích ngắn tiếng Việt, hiện nút `✅ Thêm '<từ>'` (kèm 0–2 phương án
  phụ nếu mơ hồ) và `🚫 Hủy`. Bấm xác nhận thì mới cào OpenRussian bằng từ đó —
  AI chỉ đoán, KHÔNG tự quyết. Kỹ thuật: `pipeline.process_word` trả cờ
  `not_found`; `ai_client.call_claude_lemma()`; nút dùng chỉ số
  (`lemma:i`, danh sách trong `user_data["lemma_choices"]`) để né giới hạn
  64 byte callback_data.
- **Thêm CHANGELOG.md này** — quy trình mới: mỗi lần sửa code phải cập nhật
  CHANGELOG + memory của Claude, để không phải kể lại ngữ cảnh ở phiên chat mới.

## 14/07/2026 — ngày chuyển toàn bộ hệ thống lên VPS

- `6e5040a` — Cập nhật docs: deploy.bat, /deck mở bảng chọn, nút Tự sửa/Bỏ qua.
- `9000213` — **deploy.bat**: double-click là deploy, khỏi mở PowerShell.
  Kèm theo (ngoài git): tạo SSH key trên PC + chép lên VPS → deploy không hỏi mật khẩu.
- `19aad56` — Thẻ AI bị khuyết (thiếu ví dụ): 2 nút bấm liền **🔧 Tự sửa** (chạy
  preset 2 đổi ví dụ) / **⏭ Bỏ qua**; `/deck` không tham số mở bảng chọn deck.
- `c718d70` — **Chọn deck bằng nút bấm**: [📂 Deck có sẵn (liệt kê hết, tối đa 24)]
  [➕ Tạo deck mới (gõ tên)]; gõ `c` mở cùng bảng này, deck cũ giữ đến khi chọn xong.
- `603e283` — Báo rõ thẻ khuyết khi AI thất bại (cờ `ai_degraded` + cảnh báo),
  thêm dòng 🇬🇧 vào tin nhắn tổng kết, AI freestyle retry 2 lần.
- `7e04cc7` — **CHÍNH SÁCH SYNC** (sau sự cố mất deck 00 do chọn Upload trên iPhone):
  sync AnkiWeb NGAY sau MỌI hành động sửa đổi + báo rõ khi sync thất bại.
  Quy tắc trên iPhone: LUÔN chọn "Download from AnkiWeb".
- `f94ed83` — Nâng cấp lớn bot: `/sua` có OUTPUT CONTRACT cứng (không thể trả thiếu
  ví dụ) + validate + retry; preset 1 Ngắn hơn / 2 Đổi ví dụ / 3 Dài hơn; bỏ deck
  mặc định (hỏi deck đầu phiên như CLI); idle reset 3 phút; /menu; viết lại README.
- `fdea689` — Thêm trùng dùng `options.allowDuplicate` chính thống (mánh ký tự vô
  hình ZWSP bị Anki ≥25.x tự xóa nên hỏng).
- `83a1271` — Hết quota không chết: chuỗi model dự phòng khi 429
  (chính: `gemini-3.1-flash-lite` 500 lượt/ngày); ping API bằng GET /models không đốt quota.
- `e403a94` — Sửa báo động giả "AI chưa phản hồi" (parse lỗi Google bọc trong list).
- `88613d7` — setup_vps.sh tự cài addon AnkiConnect vào volume (addon gốc là symlink
  bị volume che mất) + set webBindAddress.
- `aea5733` — Vá lỗi quyền thư mục anki-data (chmod 777) + hướng dẫn VNC qua tunnel cổng 15900.
- `ff38068` — Gỡ nút AI Refine + toàn bộ JS khỏi thẻ Anki → thẻ tĩnh, key không còn
  nhúng vào thẻ, prompt chỉ còn 1 nơi (`ai_client.py`). Sửa thẻ = `/sua` qua bot.
- `066f291` — Commit đầu: chuyển hệ thống lên VPS — bot Telegram + pipeline dùng
  chung CLI/bot + secrets tách ra `.env` + docker-compose (headless-anki) +
  setup_vps.sh + systemd + deploy.ps1 + VPS_SETUP.md.

## Hạ tầng cố định (để khỏi tìm lại)

- VPS: FPT `161.248.146.56` (1 vCPU/2GB/16GB + swap 2GB), code tại `/root/ankiagent`,
  bot chạy bằng systemd `anki-bot`, Anki headless trong Docker container tên `anki`
  (image `thisisnttheway/headless-anki`), AnkiConnect `127.0.0.1:8765`, VNC `127.0.0.1:5900`
  (cả 2 KHÔNG mở ra internet).
- GitHub: `sakuralegend/ankiagent` (private, VPS đọc qua deploy key).
- Deploy: double-click `deploy.bat` (hoặc `.\deploy.ps1`) — push → VPS pull → restart bot.
- Secrets: chỉ trong `.env` (PC + VPS, không có trong git). Đổi `.env` thì phải
  `scp .env root@161.248.146.56:/root/ankiagent/.env` + restart bot.
