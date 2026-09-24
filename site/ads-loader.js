/* ==========================================================================
   FinPath — ad loader
   Reads ads-config.js and places every ad slot on the page.
   You should never need to edit this file. Change ads-config.js instead.
   ========================================================================== */
(function () {
  "use strict";

  var CFG = window.FINPATH_ADS;
  if (!CFG) return;

  /* ---------- not configured yet: do nothing at all ---------- */
  var clientLooksReal = /^ca-pub-\d{10,}$/.test(CFG.client || "");
  if (!CFG.enabled || !clientLooksReal) {
    if (CFG.enabled && !clientLooksReal) {
      console.warn(
        "[ads] enabled is true but client is not a real ca-pub-… ID — ads stay off. " +
          "Set your publisher ID in ads-config.js.",
      );
    }
    return;
  }

  /* ---------- which kind of page is this? ---------- */
  function pageKind() {
    var p = location.pathname.split("/").pop() || "index.html";
    if (p === "index.html") return "home";
    if (p === "articles.html") return "index";
    if (p === "tools.html") return "tools";
    if (
      [
        "privacy-policy.html",
        "terms.html",
        "disclaimer.html",
        "404.html",
      ].indexOf(p) > -1
    )
      return "legal";
    if (
      p.indexOf(".") === -1 ||
      /^(loans|insurance|credit-debt|saving-investing)\.html$/.test(p)
    )
      return "category";
    return "article";
  }
  if (CFG.pages && CFG.pages[pageKind()] === false) return;

  /* ---------- slot resolution ----------
     Exact match on data-slot first, then a prefix match so that one
     "article-in-content" unit can serve every article page.              */
  function adSlotId(name) {
    var slots = CFG.slots || {};
    if (slots[name]) return slots[name];
    for (var key in slots) {
      if (!slots.hasOwnProperty(key)) continue;
      if (name.indexOf(key) === 0 && slots[key]) return slots[key];
    }
    return null;
  }

  var containers = [].slice
    .call(document.querySelectorAll(".ad-slot[data-slot]"))
    .map(function (el) {
      return { el: el, id: adSlotId(el.getAttribute("data-slot")) };
    })
    .filter(function (s) {
      if (!s.id || s.id === "0000000000") return false;
      if (s.el.children.length) return false; // already filled by hand
      if (s.el.dataset.filled) return false;
      return true;
    });

  if (!containers.length) return;

  /* ---------- load the AdSense script once ---------- */
  var SRC =
    "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" +
    encodeURIComponent(CFG.client) +
    (CFG.autoAds ? "&enable_page_level_ads=true" : "");

  function place() {
    containers.forEach(function (slot) {
      var ins = document.createElement("ins");
      ins.className = "adsbygoogle";
      ins.style.display = "block";
      ins.setAttribute("data-ad-client", CFG.client);
      ins.setAttribute("data-ad-slot", slot.id);
      ins.setAttribute("data-ad-format", "auto");
      ins.setAttribute("data-full-width-responsive", "true");
      if (CFG.testMode) ins.setAttribute("data-adtest", "on");
      slot.el.appendChild(ins);
      slot.el.dataset.filled = "1";
      try {
        (window.adsbygoogle = window.adsbygoogle || []).push({});
      } catch (e) {
        /* AdSense throws if the script has not finished loading; the
           onload handler below retries, so this is safe to ignore. */
      }
    });
  }

  if (window.adsbygoogle && window.adsbygoogle.loaded) {
    place();
    return;
  }

  var existing = document.querySelector('script[src*="adsbygoogle.js"]');
  if (existing) {
    existing.addEventListener("load", place);
    setTimeout(place, 1200); // safety net if load already fired
    return;
  }
  var s = document.createElement("script");
  s.async = true;
  s.src = SRC;
  s.crossOrigin = "anonymous";
  s.onload = place;
  s.onerror = function () {
    console.warn(
      "[ads] AdSense script could not be loaded — check the network, " +
        "an ad blocker, or that the domain is approved.",
    );
  };
  document.head.appendChild(s);
})();
