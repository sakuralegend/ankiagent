// Nút 🎤 / 🎧 mặt sau thẻ RU_Word (QD-49, 03/11/2026). anki_moitruong.dung_mat_sau() chèn
// khoá + vùng Azure từ .env rồi đẩy file này vào media Anki với tên _mic_<mã nội dung>.js
// (đổi nội dung = đổi tên ⇒ iPhone không giữ bản cũ trong bộ nhớ đệm).
// 🎤 bấm = ghi, bấm lần nữa = dừng + Azure chấm (tự dừng sau 6 s). 🎧 (hiện sau lần ghi đầu)
// = nghe lại lần vừa ghi. Điểm từng âm -> tô màu từng chữ.
// 🔴 Mọi nút tạo bằng JS PHẢI có THUỘC TÍNH onclick, KHÔNG addEventListener: AnkiMobile chỉ
// nhường cú chạm cho phần tử có onclick, còn lại coi là chạm vào thẻ ⇒ lật thẻ, trang dựng
// lại, mất nút (đã dính 3 lần liền 03/11). Test canh: MicChiDungOnclick.
// QD-49 — khoá NẰM TRONG THẺ (thay vì cổng web trên VPS): cổng web cũng phải có mật khẩu và
// mật khẩu ấy cũng phải nằm trong thẻ, lại đụng cổng 443 của VPN cùng máy. Gói F0 không
// tính tiền ⇒ lộ khoá chỉ mất lượt (5 giờ/tháng); Azure → Keys → Regenerate là vô hiệu.
// HẾT HẠN khi đổi Azure sang gói trả phí: lúc đó lộ khoá = mất tiền ⇒ phải dời ra cổng web.
window.M = (function () {
  var KEY = "__KEY__", REGION = "__REGION__", SNR_TOI_THIEU = 10, TU_DUNG_MS = 6000;
  var dang = null, mo = false;  // phiên ghi đang chạy · đang chờ hộp hỏi quyền micro
  var lanCuoi = null, dangPhat = null;  // blob: URL tiếng lần ghi gần nhất · <audio> 🎧 đang phát
  function wav16(chunks, sr) {
    var n = 0, i, j; for (i = 0; i < chunks.length; i++) n += chunks[i].length;
    var all = new Float32Array(n), o = 0;
    for (i = 0; i < chunks.length; i++) { all.set(chunks[i], o); o += chunks[i].length; }
    var ratio = sr / 16000, len = Math.floor(n / ratio), pcm = new Int16Array(len);
    for (i = 0; i < len; i++) {
      var a = Math.floor(i * ratio), b = Math.min(n, Math.floor((i + 1) * ratio)), s = 0;
      for (j = a; j < b; j++) s += all[j];
      var v = b > a ? s / (b - a) : 0; v = Math.max(-1, Math.min(1, v));
      pcm[i] = v < 0 ? v * 0x8000 : v * 0x7fff;
    }
    var buf = new ArrayBuffer(44 + len * 2), d = new DataView(buf);
    function str(p, s) { for (var k = 0; k < s.length; k++) d.setUint8(p + k, s.charCodeAt(k)); }
    str(0, "RIFF"); d.setUint32(4, 36 + len * 2, true); str(8, "WAVE"); str(12, "fmt ");
    d.setUint32(16, 16, true); d.setUint16(20, 1, true); d.setUint16(22, 1, true);
    d.setUint32(24, 16000, true); d.setUint32(28, 32000, true); d.setUint16(32, 2, true);
    d.setUint16(34, 16, true); str(36, "data"); d.setUint32(40, len * 2, true);
    for (i = 0; i < len; i++) d.setInt16(44 + i * 2, pcm[i], true);
    return buf;
  }
  // Ô hiện điểm: tìm cả trang, không giả định nằm cạnh nút (đã đơ thật 03/11 khi dời
  // 🎤 lên hàng ▶︎); mất ô thì tự đẻ ngay dưới hàng nút để lỗi luôn có chỗ hiện.
  function oKq(nut) {
    var kq = document.querySelector(".mic-kq");
    if (!kq) { kq = document.createElement("div"); kq.className = "mic-kq";
      nut.parentNode.parentNode.insertBefore(kq, nut.parentNode.nextSibling); }
    return kq;
  }
  // Điểm từng âm -> từng chữ. Azure tiếng Nga KHÔNG trả tên âm, chỉ trả điểm theo thứ tự;
  // đo 16 từ + 2 câu (03/11): số âm khớp số chữ theo luật dưới. Lệch số -> null (chỉ hiện
  // điểm chung), thà không tô còn hơn tô nhầm chữ.
  var NGUYEN_AM = "аеёиоуыэюя", HAI_AM = "яеёю";
  function toChu(ref, words) {
    var diem = [];
    (words || []).forEach(function (w) { (w.Phonemes || []).forEach(function (p) {
      diem.push((p.PronunciationAssessment || p).AccuracyScore); }); });
    var ra = [], i = 0, truoc = " ";
    for (var k = 0; k < ref.length; k++) {
      var c = ref[k], lc = c.toLowerCase(), n;
      if (lc === "ь" || lc === "ъ") n = 0;
      else if (NGUYEN_AM.indexOf(lc) >= 0)
        n = (HAI_AM.indexOf(lc) >= 0 && (truoc === " " || NGUYEN_AM.indexOf(truoc) >= 0)) ||
            truoc === "ь" || truoc === "ъ" ? 2 : 1;
      else if (/[а-яё]/i.test(c)) n = 1;
      else { n = 0; lc = " "; }
      var doan = diem.slice(i, i + n); i += n;
      ra.push({ c: c, d: doan.length ? Math.min.apply(null, doan) : null });
      truoc = lc;
    }
    return i === diem.length ? ra : null;
  }
  function mau(diem) { return diem >= 85 ? "#3fb950" : diem >= 60 ? "#d29922" : "#f85149"; }
  async function cham(nut, wav) {
    var kq = oKq(nut), ref = nut.dataset.ref;
    kq.innerHTML = "";
    var pa = btoa(unescape(encodeURIComponent(JSON.stringify({ ReferenceText: ref,
      GradingSystem: "HundredMark", Granularity: "Phoneme", Dimension: "Comprehensive",
      EnableMiscue: "True" }))));  // báo từ bỏ sót / đọc thừa — cần cho câu
    var r = await fetch("https://" + REGION + ".stt.speech.microsoft.com/speech/recognition/" +
      "conversation/cognitiveservices/v1?language=ru-RU&format=detailed", { method: "POST",
      headers: { "Ocp-Apim-Subscription-Key": KEY, "Accept": "application/json",
        "Content-Type": "audio/wav; codecs=audio/pcm; samplerate=16000", "Pronunciation-Assessment": pa },
      body: wav });
    if (r.status === 429) { kq.innerHTML = "⏳ Azure đang bận (giới hạn lượt/phút) — chờ vài giây rồi đọc lại."; return; }
    if (!r.ok) { kq.innerHTML = "❌ Azure trả lỗi " + r.status + "."; return; }
    var j = await r.json();
    if (j.RecognitionStatus !== "Success" || !j.NBest || !j.NBest[0].Words || !j.NBest[0].Words.length) {
      kq.innerHTML = "🔇 Không nghe ra chữ nào — đọc to, rõ, gần micro hơn."; return;
    }
    if ((j.SNR || 0) < SNR_TOI_THIEU) {
      kq.innerHTML = "🔈 Tiếng nhỏ hoặc ồn quá (" + Math.round(j.SNR || 0) +
        " dB) — điểm sẽ không đúng. Đọc to, gần micro hơn."; return;
    }
    // Giữ NGUYÊN mọi thứ Azure trả (user dặn 03/11: sau còn dùng cho câu) -> M.cuoi.
    M.cuoi = j;
    var nb = j.NBest[0], pa = nb.PronunciationAssessment || nb;
    var diem = Math.round(pa.AccuracyScore);
    var truoc = nut.dataset.lan ? " <span style='color:#8b949e;font-size:14px'>(lần trước " +
      nut.dataset.lan + ")</span>" : "";
    nut.dataset.lan = diem;
    // Từng TỪ (câu thì nhiều từ): bỏ sót = gạch xám · đọc thừa = ngoặc xám · còn lại tô từng chữ.
    var dong = (nb.Words || []).map(function (w) {
      var loi = (w.PronunciationAssessment || w).ErrorType || "None";
      if (loi === "Omission") return "<s style='color:#6e7681'>" + w.Word + "</s>";
      if (loi === "Insertion") return "<span style='color:#6e7681'>(" + w.Word + ")</span>";
      var chu = toChu(w.Word, [w]);
      if (!chu) return "<span style='color:" + mau((w.PronunciationAssessment || w).AccuracyScore) +
        "'>" + w.Word + "</span>";
      return chu.map(function (x) {
        return "<span style='color:" + (x.d === null ? "#8b949e" : mau(x.d)) + "'>" + x.c + "</span>"; }).join("");
    }).join(" ");
    // Đủ 4 mục Azure chấm. Với MỘT từ, "trôi chảy"/"đủ chữ" ít nghĩa (đọc sai nhấn молоко
    // thì cả hai về 0 dù đọc đủ) — vẫn hiện vì câu cần.
    function muc(ten, v) { return v === undefined || v === null ? "" : "<span style='margin:0 6px'>" + ten +
      " <b style='color:" + mau(v) + "'>" + Math.round(v) + "</b></span>"; }
    kq.innerHTML = "<span style='font-size:30px;font-weight:700;color:" + mau(diem) + "'>" + diem +
      "</span>" + truoc +
      "<div style='font-size:28px;letter-spacing:1px;margin:2px 0'>" + dong + "</div>" +
      "<div style='font-size:13px;color:#8b949e'>" + muc("Phát âm", pa.AccuracyScore) +
      muc("Trôi chảy", pa.FluencyScore) + muc("Đủ chữ", pa.CompletenessScore) +
      muc("Tổng", pa.PronScore) + muc("Ngữ điệu", pa.ProsodyScore) + "</div>" +
      "<div style='color:#8b949e;font-size:13px'>Máy nghe được: " + nb.Lexical + "</div>";
  }
  function giuLanCuoi(nut, wav) {
    if (lanCuoi) URL.revokeObjectURL(lanCuoi);
    lanCuoi = URL.createObjectURL(new Blob([wav], { type: "audio/wav" }));
    if (!document.querySelector(".mic-nghe")) {   // 🎧 chỉ hiện từ lần ghi đầu
      var b = document.createElement("span"); b.className = "mic-nghe";
      b.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" ' +
        'stroke-linecap="round"><path d="M4 15v-3a8 8 0 0 1 16 0v3"/><rect x="3" y="14" width="4" ' +
        'height="6" rx="1.5" fill="currentColor"/><rect x="17" y="14" width="4" height="6" rx="1.5" ' +
        'fill="currentColor"/></svg>';
      // PHẢI là thuộc tính onclick: AnkiMobile chỉ nhường cú chạm cho phần tử CÓ onclick, còn
      // lại coi là chạm vào thẻ -> lật/sang thẻ (03/11: addEventListener làm thẻ trượt mất).
      b.setAttribute("onclick", "M.ngheLai(this)");
      nut.parentNode.insertBefore(b, nut.nextSibling);
    }
  }
  function chayThanh(b, a) {   // thanh quét như ▶︎
    (function f() {
      if (dangPhat !== a) { b.style.setProperty("--p", "0%"); return; }
      b.style.setProperty("--p", (a.duration && isFinite(a.duration) ?
        Math.min(100, a.currentTime / a.duration * 100) : 0) + "%");
      requestAnimationFrame(f); })();
  }
  // 🎧 = <audio> + blob: URL. Đo trên iPhone 03/11 (v6 thử 3 cách, dòng ghi từng bước):
  // blob: tải✓ phát✓. Hai lần "không chạy" trước đó là do thiếu onclick, không phải do cách phát.
  function ngheLai(b) {
    if (dangPhat) { dangPhat.pause(); dangPhat = null; return; }
    if (!lanCuoi || dang) return;
    var a = new Audio(lanCuoi); dangPhat = a;
    var hong = function (ly_do) {
      if (dangPhat === a) dangPhat = null;
      var d = document.createElement("div"); d.style.cssText = "color:#f85149;font-size:13px";
      d.textContent = "❌ 🎧 không phát được: " + ly_do; oKq(b).appendChild(d);
    };
    a.onended = function () { if (dangPhat === a) dangPhat = null; };
    a.onerror = function () { hong("lỗi " + (a.error ? a.error.code : "?")); };
    var p = a.play(); if (p && p.catch) p.catch(function (e) { hong(e.name + " — " + e.message); });
    chayThanh(b, a);
  }
  async function bam(nut) {
    var kq = oKq(nut);
    if (!KEY) { kq.innerHTML = "❌ Chưa có khoá Azure (AZURE_SPEECH_KEY trong .env)."; return; }
    if (dang) { dang.dung(); return; }
    if (nut.classList.contains("cho")) return;
    if (mo) return;  // bấm lần hai lúc iPhone đang hỏi quyền
    if (dangPhat) { dangPhat.pause(); dangPhat = null; }  // đang nghe lại -> tắt
    var st = null; mo = true;
    try {
      st = await navigator.mediaDevices.getUserMedia({ audio: true });
      var ac = window.MAC;
      // Sau hộp hỏi quyền iPhone có thể để âm thanh ở trạng thái "interrupted": resume()
      // khi đó có thể không bao giờ xong -> chờ tối đa 0,5 s rồi cứ đi tiếp.
      if (ac.state !== "running") await Promise.race([ac.resume().catch(function () {}),
        new Promise(function (r) { setTimeout(r, 500); })]);
      mo = false;
      var src = ac.createMediaStreamSource(st), pr = ac.createScriptProcessor(4096, 1, 1), chunks = [];
      pr.onaudioprocess = function (e) { chunks.push(new Float32Array(e.inputBuffer.getChannelData(0))); };
      src.connect(pr); pr.connect(ac.destination);
      var hen = setTimeout(function () { if (dang) dang.dung(); }, TU_DUNG_MS);
      nut.classList.add("ghi"); kq.innerHTML = "";
      var an = ac.createAnalyser(); an.fftSize = 512; src.connect(an);
      var mau_ = new Uint8Array(an.fftSize);
      var lv = function () { if (!dang) { nut.style.setProperty("--lv", 0); return; }
        an.getByteTimeDomainData(mau_); var t = 0;
        for (var q = 0; q < mau_.length; q++) { var x = (mau_[q] - 128) / 128; t += x * x; }
        nut.style.setProperty("--lv", Math.min(1, Math.sqrt(t / mau_.length) * 4).toFixed(2));
        requestAnimationFrame(lv); };
      requestAnimationFrame(lv);  // chạy sau khi `dang` đã gán
      dang = { dung: function () {
        clearTimeout(hen); dang = null;
        pr.disconnect(); src.disconnect(); st.getTracks().forEach(function (t) { t.stop(); });
        nut.classList.remove("ghi"); nut.classList.add("cho");
        var wav = wav16(chunks, ac.sampleRate);
        giuLanCuoi(nut, wav);
        cham(nut, wav).catch(function (e) { kq.innerHTML = "❌ " + e.message; })
          .then(function () { nut.classList.remove("cho"); });
      } };
    } catch (e) {
      dang = null; mo = false; nut.classList.remove("ghi", "cho");
      try { st.getTracks().forEach(function (t) { t.stop(); }); } catch (e2) {}
      kq.innerHTML = "❌ Không mở được micro: " + e.name + " — " + e.message;
    }
  }
  return { bam: bam, ngheLai: ngheLai, toChu: toChu };
})();
