/* ==========================================================================
   FinPath — site scripts
   No dependencies, ~6KB, runs after first paint concerns are minimal.
   ========================================================================== */
(function () {
  "use strict";
  var $ = function (s, r) {
    return (r || document).querySelector(s);
  };
  var $$ = function (s, r) {
    return Array.prototype.slice.call((r || document).querySelectorAll(s));
  };

  /* ---------- footer year ---------- */
  $$("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  /* ---------- mobile nav ---------- */
  var burger = $(".burger"),
    nav = $("#site-nav");
  if (burger && nav) {
    burger.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  /* ---------- reading progress (article pages) ---------- */
  var bar = $(".progress"),
    prose = $(".prose");
  if (bar && prose) {
    var onScroll = function () {
      var r = prose.getBoundingClientRect();
      var total = r.height - window.innerHeight + 120;
      var done = Math.min(Math.max(-r.top + 100, 0), Math.max(total, 1));
      bar.style.width = (done / Math.max(total, 1)) * 100 + "%";
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  /* ---------- table of contents: build + scroll-spy ---------- */
  var toc = $("#toc");
  if (toc && prose) {
    var heads = $$("h2[id]", prose);
    heads.forEach(function (h) {
      var li = document.createElement("li");
      var a = document.createElement("a");
      a.href = "#" + h.id;
      a.textContent = h.textContent.replace(/\s*\(.*?\)\s*$/, "");
      li.appendChild(a);
      toc.appendChild(li);
    });
    if (!heads.length) {
      var box = toc.closest(".side-box");
      if (box) box.style.display = "none";
    }
    var links = $$("a", toc);
    var spy = function () {
      var best = null,
        bestTop = -Infinity;
      heads.forEach(function (h) {
        var t = h.getBoundingClientRect().top;
        if (t < 140 && t > bestTop) {
          bestTop = t;
          best = h.id;
        }
      });
      links.forEach(function (a) {
        a.classList.toggle("active", a.getAttribute("href") === "#" + best);
      });
    };
    window.addEventListener("scroll", spy, { passive: true });
    spy();
  }

  /* ---------- calculators ---------- */
  var CUR = "$";
  try {
    CUR = localStorage.getItem("finpath_cur") || "$";
  } catch (e) {}
  var rerun = [];
  var money = function (n, cur) {
    var c = cur || CUR;
    return (
      c + Number(n).toLocaleString(undefined, { maximumFractionDigits: 0 })
    );
  };
  var curSel = $("#cur");
  if (curSel) {
    curSel.value = CUR;
    curSel.addEventListener("change", function () {
      CUR = curSel.value;
      try {
        localStorage.setItem("finpath_cur", CUR);
      } catch (e) {}
      rerun.forEach(function (f) {
        f();
      });
    });
  }

  // 1) Loan / EMI
  var loan = $("#loan");
  if (loan) {
    var runLoan = function () {
      var P = +$("#l-amount").value || 0,
        annual = +$("#l-rate").value || 0,
        years = +$("#l-term").value || 1,
        fee = +$("#l-fee").value || 0;
      var r = annual / 100 / 12,
        n = Math.round(years * 12);
      var pay = r > 0 ? (P * r) / (1 - Math.pow(1 + r, -n)) : P / n;
      var total = pay * n,
        interest = total - P,
        feeAmt = (P * fee) / 100;
      $("#l-pay").textContent = money(pay);
      $("#l-interest").textContent = money(interest);
      $("#l-principal").textContent = money(P);
      $("#l-total").textContent = money(total + feeAmt);
      $("#l-fee-out").textContent = money(feeAmt);
      $("#l-months").textContent = n + " months";
      // simple amortisation sparkline: balance by year
      var chart = $("#l-chart");
      if (chart) {
        chart.innerHTML = "";
        var perYear = Math.max(1, Math.round(n / 8)),
          bal = P,
          i;
        for (i = 0; i < n; i++) {
          bal = bal + bal * r - pay;
          if (bal < 0) bal = 0;
          if (i % perYear === 0) {
            var b = document.createElement("b");
            b.style.height = Math.max(6, (bal / P) * 88) + "px";
            chart.appendChild(b);
          }
        }
      }
      var firstI = P * r;
      var split = $("#l-split");
      if (split) {
        if (P <= 0) {
          split.textContent = "Enter an amount to see where your money goes.";
        } else if (firstI <= 0) {
          split.textContent =
            "With no interest, every payment goes straight to the balance.";
        } else {
          split.textContent =
            Math.round((firstI / pay) * 100) +
            "% of your first payment is interest — " +
            money(firstI) +
            " of " +
            money(pay) +
            ".";
        }
      }
    };
    ["#l-amount", "#l-rate", "#l-term", "#l-fee"].forEach(function (id) {
      var el = $(id);
      if (el) el.addEventListener("input", runLoan);
    });
    runLoan();
    rerun.push(runLoan);
  }

  // 2) Emergency fund
  var ef = $("#fund");
  if (ef) {
    var runFund = function () {
      var spend = +$("#f-spend").value || 0,
        months = +$("#f-months").value || 0,
        saved = +$("#f-have").value || 0,
        weekly = +$("#f-weekly").value || 0;
      var target = spend * months,
        gap = Math.max(target - saved, 0);
      $("#f-target").textContent = money(target);
      $("#f-gap").textContent = money(gap);
      $("#f-pct").textContent =
        (target > 0 ? Math.min(100, Math.round((saved / target) * 100)) : 0) +
        "% funded";
      var weeks = weekly > 0 ? Math.ceil(gap / weekly) : 0;
      $("#f-time").textContent =
        gap === 0
          ? "Fully funded — move to the next goal"
          : weekly > 0
            ? weeks + " weeks (about " + Math.ceil(weeks / 4.33) + " months)"
            : "Add a weekly amount to see a timeline";
    };
    ["#f-spend", "#f-months", "#f-have", "#f-weekly"].forEach(function (id) {
      var el = $(id);
      if (el) el.addEventListener("input", runFund);
    });
    runFund();
    rerun.push(runFund);
  }

  // 3) Insurance cover (DIME method)
  var ins = $("#insurance-cover");
  if (ins) {
    var runIns = function () {
      var debt = +$("#i-debt").value || 0,
        income = +$("#i-income").value || 0,
        years = +$("#i-years").value || 0,
        mortgage = +$("#i-mortgage").value || 0,
        edu = +$("#i-edu").value || 0,
        existing = +$("#i-existing").value || 0,
        savings = +$("#i-savings").value || 0;
      var need = debt + income * years + mortgage + edu;
      var gap = Math.max(need - existing - savings, 0);
      $("#i-need").textContent = money(need);
      $("#i-gap").textContent = money(gap);
      $("#i-income-part").textContent = money(income * years);
      $("#i-range").textContent =
        money(Math.round(gap * 0.9)) + " – " + money(Math.round(gap * 1.1));
    };
    [
      "#i-debt",
      "#i-income",
      "#i-years",
      "#i-mortgage",
      "#i-edu",
      "#i-existing",
      "#i-savings",
    ].forEach(function (id) {
      var el = $(id);
      if (el) el.addEventListener("input", runIns);
    });
    runIns();
    rerun.push(runIns);
  }

  // 4) Debt payoff comparison
  var debt = $("#debt");
  if (debt) {
    var simulate = function (balances, aprs, extra, mode) {
      // returns months and total interest
      var bals = balances.slice(),
        months = 0,
        interest = 0,
        i;
      var order = bals.map(function (_, i) {
        return i;
      });
      while (
        bals.some(function (v) {
          return v > 0.5;
        }) &&
        months < 600
      ) {
        months++;
        var pool = extra;
        for (i = 0; i < bals.length; i++) {
          if (bals[i] <= 0) continue;
          var add = bals[i] * (aprs[i] / 100 / 12);
          bals[i] += add;
          interest += add;
        }
        // minimum payments (assume 2% or 25, whichever larger)
        var minTotal = 0;
        for (i = 0; i < bals.length; i++) {
          if (bals[i] <= 0) continue;
          var min = Math.min(bals[i], Math.max(bals[i] * 0.02, 25));
          bals[i] -= min;
          minTotal += min;
        }
        // sort order
        order = order.slice().sort(function (a, b) {
          if (mode === "avalanche") return aprs[b] - aprs[a];
          return balances[a] - balances[b] || bals[a] - bals[b];
        });
        var left = Math.max(extra, 0);
        for (i = 0; i < order.length && left > 0; i++) {
          var idx = order[i];
          if (bals[idx] <= 0) continue;
          var pay = Math.min(left, bals[idx]);
          bals[idx] -= pay;
          left -= pay;
        }
      }
      return {
        months: months,
        interest: Math.max(interest, 0),
        stuck: months >= 600,
      };
    };
    var runDebt = function () {
      var b1 = +$("#d-b1").value || 0,
        a1 = +$("#d-a1").value || 0,
        b2 = +$("#d-b2").value || 0,
        a2 = +$("#d-a2").value || 0,
        b3 = +$("#d-b3").value || 0,
        a3 = +$("#d-a3").value || 0,
        extra = +$("#d-extra").value || 0;
      var bal = [b1, b2, b3].filter(function (v, i) {
        return [b1, b2, b3][i] > 0;
      });
      var ap = [a1, a2, a3].slice(0, bal.length);
      bal = [b1, b2, b3].filter(function (v) {
        return v > 0;
      });
      ap = [];
      if (b1 > 0) ap.push(a1);
      if (b2 > 0) ap.push(a2);
      if (b3 > 0) ap.push(a3);
      if (!bal.length) {
        $("#d-ava").textContent = "—";
        $("#d-snow").textContent = "—";
        $("#d-save").textContent = "Enter at least one balance";
        return;
      }
      var av = simulate(bal, ap, extra, "avalanche");
      var sn = simulate(bal, ap, extra, "snowball");
      var label = function (x) {
        return x.stuck
          ? "Never clears (50-year cap)"
          : x.months + " months · " + money(x.interest) + " interest";
      };
      $("#d-ava").textContent = label(av);
      $("#d-snow").textContent = label(sn);
      if (av.stuck || sn.stuck) {
        $("#d-save").textContent =
          "Warning: with these numbers the interest charged each month is larger than the " +
          "minimum payment, so the balance grows instead of shrinking. Raising the extra monthly amount is the only way out — " +
          "this is exactly how a minimum-payment trap works.";
        return;
      }
      var diff = Math.abs(av.interest - sn.interest);
      $("#d-save").textContent =
        diff < 1
          ? "Both methods land at almost the same cost with these numbers."
          : "Avalanche saves about " +
            money(diff) +
            " in interest" +
            (sn.months < av.months
              ? ", but snowball finishes " +
                (av.months - sn.months) +
                " month(s) sooner."
              : ".");
    };
    $$("#debt input").forEach(function (el) {
      el.addEventListener("input", runDebt);
    });
    runDebt();
    rerun.push(runDebt);
  }

  /* ---------- newsletter (demo only — wire to your provider) ---------- */
  $$("form[data-news]").forEach(function (f) {
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      var msg = $(".form-msg", f.parentNode);
      if (msg) {
        msg.classList.add("show");
      }
      f.reset();
    });
  });

  /* ---------- ad placement preview ----------
     Real AdSense code goes inside the .ad-slot divs; those stay display:none-free
     once you replace them. Add ?ads=preview to the URL (or use the toggle) to see
     exactly where ads will appear without loading anything from Google.        */
  function adPreview(on) {
    $$(".ad-slot").forEach(function (s) {
      var empty = s.children.length === 0;
      s.classList.toggle("dev", !!on && empty);
      if (on && empty && !s.dataset.built) {
        s.dataset.built = "1";
        s.innerHTML =
          '<div class="tag">Ad preview &middot; not loaded</div>' +
          '<div class="size">' +
          (s.getAttribute("data-format") || "Responsive unit") +
          "</div>" +
          '<div class="hint">slot: #' +
          (s.getAttribute("data-slot") || "") +
          "</div>" +
          '<div class="note">' +
          (s.getAttribute("data-hint") || "") +
          "</div>";
      }
    });
    var old = $("#ad-devbar");
    if (old) old.parentNode.removeChild(old);
    if (on) {
      var bar = document.createElement("div");
      bar.className = "ad-devbar";
      bar.id = "ad-devbar";
      bar.innerHTML =
        '<b>Ad preview</b><button type="button" data-off>Hide</button>';
      document.body.appendChild(bar);
      $("[data-off]", bar).addEventListener("click", function () {
        try {
          localStorage.setItem("coinpath_ads", "0");
        } catch (e) {}
        adPreview(false);
      });
    }
  }
  var q = location.search;
  var adOn = /(\?|&)ads=preview/.test(q);
  try {
    if (localStorage.getItem("coinpath_ads") === "1") adOn = true;
  } catch (e) {}
  if (adOn) {
    try {
      localStorage.setItem("coinpath_ads", "1");
    } catch (e) {}
  }
  if ($$(".ad-slot").length) adPreview(adOn);
  window.CoinPathAds = {
    show: function () {
      try {
        localStorage.setItem("coinpath_ads", "1");
      } catch (e) {}
      adPreview(true);
    },
  };
})();
