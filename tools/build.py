# -*- coding: utf-8 -*-
"""Build the FinPath static site into /home/user/site."""

import sys, json, html
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "content"))

import framework as Fw
from framework import (
    CFG,
    shell,
    ad,
    post_card,
    sec_head,
    icon,
    tick,
    figure,
    hero_image,
    OUT,
)
from articles_a import ARTICLES_A
from articles_b import ARTICLES_B
from articles_c import ARTICLES_C

ARTICLES = ARTICLES_A + ARTICLES_B + ARTICLES_C
BY_SLUG = {a["slug"]: a for a in ARTICLES}
TODAY = "2026-09-24"

CATS = {
    "loans": {
        "name": "Loans &amp; Mortgages",
        "short": "Loans",
        "icon": "loans",
        "img": "cat-loans",
        "alt": "House keys, a model house and a loan document on a wooden table",
        "title": "Loans and mortgages, explained without the sales pitch",
        "desc": "How borrowing costs really work: amortisation, APR versus interest rate, fees, early repayment and how to compare two offers in eight minutes.",
        "intro": """
<p>A loan is a price for time. The price is set by the interest rate, the length of the term, the fees attached to setting it up, and what the lender can charge if your situation changes. Almost every expensive borrowing mistake comes from optimising one of those and ignoring the other three.</p>
<p>On this page we cover the arithmetic that loan comparison tools hide: how an instalment splits between interest and principal, why two loans quoted at the same rate can cost very different totals, when overpaying is the best guaranteed return available, and how to read an offer document before signing it.</p>
<div class="callout warn"><b>What we do not do</b><p>We do not rank lenders, quote personalised rates, or tell you which loan to take. Rates depend on your credit file, income and security, and a website cannot see any of those. What we can do is make sure you understand what you are signing.</p></div>
""",
    },
    "insurance": {
        "name": "Insurance",
        "short": "Insurance",
        "icon": "shield",
        "img": "cat-insurance",
        "alt": "A folded umbrella beside a neat stack of blank paperwork on a table",
        "title": "Insurance: working out the cover, not just the quote",
        "desc": "Life, health and protection cover explained: the DIME method, term versus permanent, riders worth paying for, and why claims get declined.",
        "intro": """
<p>Insurance is the only financial product whose usefulness is decided at the worst possible moment. That makes it unusually important to understand before you buy it, because the time to discover an exclusion is not when you need to claim.</p>
<p>Our insurance coverage focuses on the calculation — how much cover you actually need — and on the contract details that decide whether a claim is paid: disclosure, exclusions, nominees, free-look periods and complaint routes when something goes wrong.</p>
<div class="callout"><b>A useful rule of thumb</b><p>Insure the events that would be catastrophic, not the ones that would be annoying. A cracked phone screen is annoying. Losing the household's main income is catastrophic.</p></div>
""",
    },
    "credit-debt": {
        "name": "Credit &amp; Debt",
        "short": "Credit &amp; Debt",
        "icon": "card",
        "img": "cat-credit",
        "alt": "Plain unmarked bank cards fanned out on a dark surface under soft purple light",
        "title": "Credit and debt: the arithmetic behind the statements",
        "desc": "Minimum payments, APR, utilisation, balance transfers and payoff strategies — explained with worked numbers and honest trade-offs.",
        "intro": """
<p>Consumer credit is priced on risk, and the pricing is disclosed. The problem is that it is disclosed in a way that is technically accurate and practically invisible: a minimum payment percentage here, a daily accrual clause there, a promotional rate with an expiry date in the middle.</p>
<p>Here we translate those clauses into pounds, dollars and months, and cover the strategies that actually shorten debt: targeting methods, balance transfer arithmetic, and when to seek free professional help instead of another product.</p>
""",
    },
    "saving-investing": {
        "name": "Saving &amp; Investing",
        "short": "Saving",
        "icon": "chart",
        "img": "cat-saving",
        "alt": "A person smiling at a laptop in a bright home office",
        "title": "Saving and investing: getting the boring parts right",
        "desc": "Emergency funds, deposit protection, high-yield accounts, tax wrappers and CDs — compared on after-tax, after-inflation numbers.",
        "intro": """
<p>Most households do not have an investment problem. They have a cash-flow and structure problem: no buffer, money spread across accounts with no purpose, and a savings rate that gets whatever is left at the end of the month rather than whatever was decided at the start of it.</p>
<p>This section is about structure. How much buffer is enough, where to hold it, which tax wrappers apply in the US and the UK, and how to compare savings accounts on the interest that actually lands in your account rather than the rate in the advert.</p>
""",
    },
}


# --------------------------------------------------------------------------- calculators
def calc_loan(solo=True):
    return f"""<div class="tool" id="loan">
  <div class="tool-in">
    <div class="tool-form">
      <h2>Loan payment &amp; total cost</h2>
      <p style="color:var(--muted);font-size:15px">See the monthly payment, the interest you will actually pay, and how much of your first payment is interest.</p>
      <div class="field"><label for="l-amount">Amount borrowed</label><input id="l-amount" type="number" min="0" step="500" value="25000"></div>
      <div class="grid g-2" style="gap:14px">
        <div class="field"><label for="l-rate">Interest rate (% per year)</label><input id="l-rate" type="number" min="0" step="0.1" value="7.5"></div>
        <div class="field"><label for="l-term">Term (years)</label><input id="l-term" type="number" min="1" max="40" step="1" value="5"></div>
      </div>
      <div class="field"><label for="l-fee">Arrangement fee (%) <span class="hint">— 0 if none</span></label><input id="l-fee" type="number" min="0" step="0.1" value="0"></div>
      <p class="note">Estimate only. Lenders calculate interest daily or monthly depending on the agreement, and fees may be deducted rather than financed.</p>
    </div>
    <div class="tool-out">
      <h3>Your repayments</h3>
      <div class="result-hero" id="l-pay">$0</div>
      <div class="result-sub" id="l-months">per month</div>
      <div class="chart" id="l-chart" aria-hidden="true"></div>
      <ul class="result-rows">
        <li><span>Amount borrowed</span><b id="l-principal">$0</b></li>
        <li><span>Interest over the term</span><b id="l-interest">$0</b></li>
        <li><span>Fees</span><b id="l-fee-out">$0</b></li>
        <li class="tot"><span>Total cost of credit</span><b id="l-total">$0</b></li>
      </ul>
      <p class="note" id="l-split"></p>
    </div>
  </div>
</div>"""


def calc_fund(solo=True):
    return f"""<div class="tool" id="fund">
  <div class="tool-in">
    <div class="tool-form">
      <h2>Emergency fund target</h2>
      <p style="color:var(--muted);font-size:15px">Convert "I should have savings" into a specific number and a realistic timeline.</p>
      <div class="grid g-2" style="gap:14px">
        <div class="field"><label for="f-spend">Essential monthly spending</label><input id="f-spend" type="number" min="0" step="100" value="3200"></div>
        <div class="field"><label for="f-months">Months of cover</label><select id="f-months"><option>3</option><option selected>6</option><option>9</option><option>12</option></select></div>
      </div>
      <div class="grid g-2" style="gap:14px">
        <div class="field"><label for="f-have">Already saved</label><input id="f-have" type="number" min="0" step="100" value="1500"></div>
        <div class="field"><label for="f-weekly">Weekly contribution</label><input id="f-weekly" type="number" min="0" step="10" value="150"></div>
      </div>
      <p class="note">Essential spending means housing, food, utilities, transport, insurance and minimum debt payments — not your full lifestyle.</p>
    </div>
    <div class="tool-out">
      <h3>Your target</h3>
      <div class="result-hero" id="f-target">$0</div>
      <div class="result-sub" id="f-pct">0% funded</div>
      <ul class="result-rows">
        <li><span>Still to save</span><b id="f-gap">$0</b></li>
        <li class="tot"><span>Time to target</span><b id="f-time">—</b></li>
      </ul>
      <p class="note">Keep the fund in an insured account with instant access. Return is the least important feature.</p>
    </div>
  </div>
</div>"""


def calc_ins(solo=True):
    return f"""<div class="tool" id="insurance-cover">
  <div class="tool-in">
    <div class="tool-form">
      <h2>Life insurance cover estimator</h2>
      <p style="color:var(--muted);font-size:15px">A DIME-style estimate: debts, income replacement, mortgage and education, minus what you already have.</p>
      <div class="grid g-2" style="gap:14px">
        <div class="field"><label for="i-debt">Debts (cards, car, personal loans)</label><input id="i-debt" type="number" min="0" step="1000" value="15000"></div>
        <div class="field"><label for="i-mortgage">Mortgage balance</label><input id="i-mortgage" type="number" min="0" step="1000" value="220000"></div>
      </div>
      <div class="grid g-2" style="gap:14px">
        <div class="field"><label for="i-income">Annual income</label><input id="i-income" type="number" min="0" step="1000" value="60000"></div>
        <div class="field"><label for="i-years">Years of income to replace</label><input id="i-years" type="number" min="0" max="30" step="1" value="10"></div>
      </div>
      <div class="grid g-2" style="gap:14px">
        <div class="field"><label for="i-edu">Future education costs</label><input id="i-edu" type="number" min="0" step="1000" value="80000"></div>
        <div class="field"><label for="i-existing">Existing cover (work + policies)</label><input id="i-existing" type="number" min="0" step="1000" value="250000"></div>
      </div>
      <div class="field"><label for="i-savings">Savings and investments available</label><input id="i-savings" type="number" min="0" step="1000" value="0"></div>
    </div>
    <div class="tool-out">
      <h3>Estimated cover needed</h3>
      <div class="result-hero" id="i-gap">$0</div>
      <div class="result-sub">Planning range <span id="i-range">$0 – $0</span></div>
      <ul class="result-rows">
        <li><span>Total need identified</span><b id="i-need">$0</b></li>
        <li><span>Income replacement portion</span><b id="i-income-part">$0</b></li>
      </ul>
      <p class="note">Educational estimate only — not advice, not a quote. Underwriting and pricing depend on your health, age and occupation.</p>
    </div>
  </div>
</div>"""


def calc_debt(solo=True):
    return f"""<div class="tool" id="debt">
  <div class="tool-in">
    <div class="tool-form">
      <h2>Debt payoff: avalanche vs snowball</h2>
      <p style="color:var(--muted);font-size:15px">Enter up to three balances. The model assumes minimum payments of 2% or 25 (whichever is greater) plus your extra amount each month.</p>
      <div class="grid g-3" style="gap:12px">
        <div class="field"><label for="d-b1">Balance 1</label><input id="d-b1" type="number" min="0" step="100" value="4000"></div>
        <div class="field"><label for="d-b2">Balance 2</label><input id="d-b2" type="number" min="0" step="100" value="2000"></div>
        <div class="field"><label for="d-b3">Balance 3</label><input id="d-b3" type="number" min="0" step="100" value="0"></div>
      </div>
      <div class="grid g-3" style="gap:12px">
        <div class="field"><label for="d-a1">APR 1 (%)</label><input id="d-a1" type="number" min="0" step="0.1" value="24"></div>
        <div class="field"><label for="d-a2">APR 2 (%)</label><input id="d-a2" type="number" min="0" step="0.1" value="9"></div>
        <div class="field"><label for="d-a3">APR 3 (%)</label><input id="d-a3" type="number" min="0" step="0.1" value="18"></div>
      </div>
      <div class="field"><label for="d-extra">Extra per month on top of minimums</label><input id="d-extra" type="number" min="0" step="25" value="200"></div>
      <p class="note">Simplified model for comparison. Your statement's minimum may be calculated differently, and interest accrues daily on most cards.</p>
    </div>
    <div class="tool-out">
      <h3>Two targeting strategies</h3>
      <ul class="result-rows">
        <li><span><strong>Avalanche</strong><br><small style="opacity:.7">highest rate first</small></span><b id="d-ava">—</b></li>
        <li><span><strong>Snowball</strong><br><small style="opacity:.7">smallest balance first</small></span><b id="d-snow">—</b></li>
      </ul>
      <p class="note" id="d-save">—</p>
    </div>
  </div>
</div>"""


CALCS = {"loan": calc_loan, "fund": calc_fund, "ins": calc_ins, "debt": calc_debt}


# --------------------------------------------------------------------------- shared blocks
def mini_chart(kind):
    """Small inline SVG charts — used in the 'how the numbers work' panels."""
    if kind == "split":
        rows = [("Month 1", 31), ("Month 24", 21), ("Month 60", 1)]
        y = 14
        out = [
            '<svg viewBox="0 0 340 116" class="mini" role="img" aria-label="Chart: the interest share of a loan payment falls from 31% in month one to almost nothing by month sixty">'
        ]
        for label, pct in rows:
            out.append(
                f'<text x="0" y="{y+13}" font-size="12" fill="#6d6690">{label}</text>'
            )
            out.append(
                f'<rect x="64" y="{y}" width="232" height="18" rx="5" fill="#7c3aed"/>'
            )
            out.append(
                f'<rect x="64" y="{y}" width="{round(232*pct/100)}" height="18" rx="5" fill="#ec4899"/>'
            )
            out.append(
                f'<text x="304" y="{y+13}" font-size="11.5" fill="#6d6690">{pct}%</text>'
            )
            y += 34
        out.append("</svg>")
        return "".join(out)
    if kind == "buffer":
        bars = [("1 month", 3200, 44), ("3 months", 9600, 84), ("6 months", 19200, 118)]
        out = [
            '<svg viewBox="0 0 330 176" class="mini" role="img" aria-label="Chart: an emergency fund growing from a one-month buffer of 3,200 dollars to a six-month target of 19,200 dollars">'
        ]
        x = 22
        base = 148
        for label, val, h in bars:
            fill = "#c4b5fd" if h < 100 else "#7c3aed"
            out.append(
                f'<rect x="{x}" y="{base-h}" width="56" height="{h}" rx="6" fill="{fill}"/>'
            )
            out.append(
                f'<text x="{x+28}" y="{base-h-9}" font-size="12" font-weight="700" fill="#1a1430" text-anchor="middle">${val:,}</text>'
            )
            out.append(
                f'<text x="{x+28}" y="{base+16}" font-size="10.5" fill="#6d6690" text-anchor="middle">{label}</text>'
            )
            x += 96
        out.append(
            f'<line x1="10" y1="{base}" x2="320" y2="{base}" stroke="#e7e3f3" stroke-width="2"/>'
        )
        out.append("</svg>")
        return "".join(out)
    # minimum payments
    out = [
        '<svg viewBox="0 0 340 132" class="mini" role="img" aria-label="Chart: a 1,000 dollar balance takes 73 months to clear at the minimum, but 16 months with 50 dollars extra a month">'
    ]
    data = [("Minimum only", 73, "#ec4899"), ("Minimum +$50", 16, "#0ea5a4")]
    y = 22
    for label, months, colour in data:
        w = round(120 * months / 73)
        out.append(
            f'<text x="0" y="{y+13}" font-size="12" fill="#6d6690">{label}</text>'
        )
        out.append(
            f'<rect x="112" y="{y}" width="{w}" height="18" rx="5" fill="{colour}"/>'
        )
        out.append(
            f'<text x="{112 + w + 10}" y="{y+13}" font-size="11.5" font-weight="600" fill="#4b4468">{months} months</text>'
        )
        y += 44
    out.append(
        f'<text x="0" y="124" font-size="11" fill="#8b84a8">Same $1,000 balance, same 22% APR, no new spending</text>'
    )
    out.append("</svg>")
    return "".join(out)


def numbers_section():
    """Three at-a-glance panels with live SVG charts — mirrors the reference layout."""
    panels = [
        (
            "calc",
            "Where your instalment goes",
            "Interest is charged on the outstanding balance, so the interest slice of a fixed payment falls every month — which is why overpaying early is worth so much more than overpaying later.",
            "split",
            "Read the amortisation guide",
            "articles/how-loan-amortization-works.html",
        ),
        (
            "wallet",
            "Your buffer, staged",
            "A one-month buffer changes behaviour; a six-month fund changes outcomes. Stage it rather than aiming at the distant number and losing momentum.",
            "buffer",
            "Size your emergency fund",
            "articles/emergency-fund-how-much.html",
        ),
        (
            "card",
            "The minimum-payment trap",
            "A $1,000 balance at 22% takes 73 months to clear at the minimum. Adding $50 a month cuts that to 16 months and removes most of the interest.",
            "min",
            "See the payoff maths",
            "articles/how-credit-card-minimum-payments-work.html",
        ),
    ]
    cards = ""
    for icon_name, title, text, kind, link_text, href in panels:
        cards += f"""<div class="card num-card">
  <div class="num-head"><span class="num-ic">{icon(icon_name, size=20)}</span><h3>{title}</h3></div>
  <div class="mini-wrap">{mini_chart(kind)}</div>
  <p>{text}</p>
  <a class="more" href="{href}">{link_text} →</a>
</div>"""
    return f"""<section class="section">
  <div class="wrap">
    {sec_head("At a glance", "How the numbers actually work",
              "Three charts that explain most of what this site is about. Every figure is worked through in the full guides.")}
    <div class="grid g-3">{cards}</div>
  </div>
</section>"""


def tools_teaser():
    return f"""<section class="section alt">
  <div class="wrap">
    {sec_head("Free calculators", "Run the numbers before anyone quotes you a rate",
              "Four calculators, no sign-up, no email gate. Useful on their own and updated whenever the underlying rules change.")}
    <div class="grid g-2" style="gap:26px">
      <div class="card"><div class="cat-card" style="padding:0;border:0;box-shadow:none">
        <div class="ic">{icon('calc')}</div><h3>Loan payment &amp; total cost</h3>
        <p>Monthly payment, total interest, fees financed — and the share of your first payment that is pure interest.</p>
        <a class="btn btn-ghost btn-sm" href="articles.html">Read the guide</a></div></div>
      <div class="card"><div class="cat-card" style="padding:0;border:0;box-shadow:none">
        <div class="ic">{icon('wallet')}</div><h3>Emergency fund target</h3>
        <p>Turn "I should have savings" into a number and a weekly plan with a realistic timeline.</p>
        <a class="btn btn-ghost btn-sm" href="articles.html">Read the guide</a></div></div>
      <div class="card"><div class="cat-card" style="padding:0;border:0;box-shadow:none">
        <div class="ic">{icon('shield')}</div><h3>Life cover estimator</h3>
        <p>The DIME method, run for you: debts plus income replacement plus mortgage plus education, minus what you hold.</p>
        <a class="btn btn-ghost btn-sm" href="articles.html">Read the guide</a></div></div>
      <div class="card"><div class="cat-card" style="padding:0;border:0;box-shadow:none">
        <div class="ic">{icon('chart')}</div><h3>Avalanche vs snowball</h3>
        <p>Two payoff strategies, same debts, side by side: months to clear and total interest under each.</p>
        <a class="btn btn-ghost btn-sm" href="articles.html">Read the guide</a></div></div>
    </div>
  </div>
</section>"""


def newsletter():
    return f"""<div class="news" id="newsletter">
  <h2>The monthly numbers email</h2>
  <p>One email a month: what changed in rates, fees and rules, a worked example, and one habit worth building. No product pitches, no affiliates, unsubscribe in one click.</p>
  <form class="news-form" data-news method="post" action="#">
    <label class="sr" for="nl-email">Email address</label>
    <input id="nl-email" type="email" name="email" placeholder="you@example.com" required>
    <button class="btn btn-primary" type="submit">Subscribe</button>
  </form>
  <div class="form-msg">Thanks — check your inbox for the confirmation link.</div>
  <p class="fine">We store your address only to send the newsletter. A working newsletter needs a real provider before launch — see the README.</p>
</div>"""


def home_faq():
    qs = [
        (
            "Is this website financial advice?",
            "No. Every page here is general educational information. It does not take your income, debts, tax position or goals into account, which is exactly what proper advice requires. For decisions with real consequences, speak to a regulated adviser in your country.",
        ),
        (
            "How do you make money?",
            "Display advertising. Ads are clearly separated from editorial content, never placed inside the text flow of a sentence, and we do not accept payment to recommend a lender, insurer or product. That independence is the reason the site exists.",
        ),
        (
            "Do you recommend specific loans, cards or policies?",
            "No, and that is deliberate. Product recommendations require knowing your circumstances and, in most countries, a licence we deliberately do not hold. We explain how products work and how to compare them, then leave the selection to you.",
        ),
        (
            "How current is the information?",
            "Every guide carries a last-updated date. Rates, contribution limits and tax rules change, so we link to the primary source for each factual claim — regulator, tax authority or statute — and you can verify anything we write in a couple of clicks.",
        ),
        (
            "Can I suggest a correction or a topic?",
            "Yes, and corrections are welcome. Use the contact page; where a correction changes a published figure we update the guide and note the change at the foot of the page.",
        ),
    ]
    items = "".join(
        f"<details><summary>{q}</summary><div class='a'><p>{a}</p></div></details>"
        for q, a in qs
    )
    return f"""<section class="section">
  <div class="wrap-n wrap">
    {sec_head("Common questions", "About FinPath", "", center=True)}
    <div class="faq">{items}</div>
  </div>
</section>"""


# --------------------------------------------------------------------------- home
def build_home():
    feat = [
        BY_SLUG["how-loan-amortization-works"],
        BY_SLUG["insurance-cover-how-much-do-you-need"],
        BY_SLUG["how-credit-card-minimum-payments-work"],
    ]
    cards = "".join(post_card(p, root="", large=(i == 0)) for i, p in enumerate(feat))
    # in-feed ad sits inside the article grid as a card-like unit
    infeed = ad(
        "home-in-feed",
        "In-feed / in-article responsive unit",
        "Placed between article cards on the homepage, styled to match the card width so it blends with the list rather than interrupting it.",
    )
    recent = "".join(post_card(p, root="") for p in ARTICLES)
    cats_html = ""
    for key, c in CATS.items():
        subs = [a for a in ARTICLES if a["cat"][1] == key]
        cats_html += f"""<div class="card cat-card">
  <div class="ic">{icon(c['icon'])}</div>
  <h3>{c['name']}</h3>
  <p>{c['desc']}</p>
  <div class="more"><a href="articles.html#{key}" style="color:inherit">Browse {len(subs)} guide{'s' if len(subs)!=1 else ''} →</a></div>
</div>"""

    body = f"""
<section class="hero">
  <div class="wrap hero-in">
    <div>
      <h1>Understand the money <em>before</em> you sign for it</h1>
      <p class="lede">FinPath explains borrowing, insurance and household savings in plain language — with the arithmetic shown, the fine print translated, and no products to sell you.</p>
      <div class="hero-btns">
        <a class="btn btn-primary" href="articles.html">Start with the guides</a>
        <a class="btn btn-ghost on-dark" href="articles.html">Read the guides</a>
      </div>
      <ul class="hero-facts">
        <li>{tick()} No product recommendations</li>
        <li>{tick()} Primary sources linked</li>
        <li>{tick()} Last-updated dates on every guide</li>
      </ul>
    </div>
    <div class="hero-visual" aria-hidden="true">
      <span class="orb a"></span><span class="orb b"></span>
      <div class="phone">
        <div class="screen">
          <div class="s-head">
            <div class="s-av">TA</div>
            <div><b>Good morning</b><span>Here is your month at a glance</span></div>
            <div class="s-bell">◔</div>
          </div>
          <div class="s-balance">
            <div class="lbl">Loan balance tracked</div>
            <div class="amt">$27,918.00</div>
            <div class="s-chip"><span>Interest this month: $156</span><span>31% of payment</span></div>
          </div>
          <div class="s-actions">
            <div><i>＋</i>Repay</div><div><i>⇄</i>Compare</div><div><i>↻</i>Refinance</div><div><i>▣</i>Plan</div>
          </div>
          <div class="s-bar">
            <div class="top"><b>Balance over time</b><span>60 months</span></div>
            <div class="bars">
              <b style="height:52px"></b><b style="height:47px"></b><b style="height:41px"></b>
              <b style="height:34px"></b><b style="height:26px"></b><b style="height:17px"></b><b style="height:9px"></b>
            </div>
          </div>
          <div class="s-list">
            <div class="s-row"><span class="ic">◱</span><div><b>Emergency fund</b><small>6 months target</small></div><span class="amt g">$19,200</span></div>
            <div class="s-row"><span class="ic">▦</span><div><b>Card balance</b><small>73 months at minimum</small></div><span class="amt r">$1,000</span></div>
            <div class="s-row"><span class="ic">◈</span><div><b>Cover needed</b><small>DIME estimate</small></div><span class="amt">$665,000</span></div>
          </div>
        </div>
        <div class="float-card one">Interest saved by<br>overpaying $100/mo<b>$1,240</b></div>
        <div class="float-card two">Real return after tax<br>and inflation<b>+1.75%</b></div>
      </div>
    </div>
  </div>
</section>

<div class="trust">
  <div class="wrap trust-in">
    <span>{icon('check', size=16)} Educational only — never a recommendation</span>
    <span>{icon('check', size=16)} Primary sources cited</span>
    <span>{icon('check', size=16)} No paid placements</span>
    <span>{icon('check', size=16)} Corrections published</span>
  </div>
</div>

{ad("home-top", "Responsive display — 970×250 / 336×280 above the fold is best avoided", "Sits below the hero, before the topic grid. One unit here is plenty; stacking a second banner above the fold both annoys readers and depresses click quality.")}

<section class="section">
  <div class="wrap">
    {sec_head("Browse by topic", "Four areas where the fine print costs the most",
              "Each section explains the mechanics, the traps, and the questions to ask before you commit to anything.")}
    <div class="grid g-4">{cats_html}</div>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    {sec_head("Start here", "The guides most readers open first",
              "Written for someone who has a decision to make in the next few weeks, not for someone browsing.")}
    <div class="grid g-3">{cards}</div>
    {infeed}
  </div>
</section>

{numbers_section()}

<section class="section">
  <div class="wrap">
    {sec_head("All guides", "Everything we publish, newest first")}
    <div class="grid g-3">{recent}</div>
  </div>
</section>

<section class="section alt">
  <div class="wrap">{newsletter()}</div>
</section>

{home_faq()}

{ad("home-bottom", "Footer / anchor responsive unit", "Optional. A mobile anchor unit performs well but should stay dismissible and non-intrusive to comply with ad-experience policies.")}
"""

    schema = [
        {
            "@context": "https://schema.org",
            "@type": "WebSite",
            "name": CFG["name"],
            "url": CFG["domain"],
            "inLanguage": "en",
            "description": "Independent educational guides on loans, insurance, credit and saving.",
            "publisher": {"@type": "Organization", "name": CFG["name"]},
        },
        {
            "@context": "https://schema.org",
            "@type": "Organization",
            "name": CFG["name"],
            "url": CFG["domain"],
            "description": "FinPath publishes plain-English educational explainers on borrowing, insurance, credit and household money. It does not sell or recommend financial products.",
            "email": CFG["email"],
        },
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": "Is this website financial advice?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "No. Every page is general educational information and does not take your income, debts, tax position or goals into account.",
                    },
                },
                {
                    "@type": "Question",
                    "name": "Do you recommend specific loans, cards or policies?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "No. We explain how products work and how to compare them, but we do not recommend specific products.",
                    },
                },
                {
                    "@type": "Question",
                    "name": "How do you make money?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Display advertising, clearly separated from editorial content. We do not accept payment to recommend a product.",
                    },
                },
            ],
        },
    ]
    return shell(
        title=f"{CFG['name']} — plain-English guides to loans, insurance, credit and saving",
        desc="Independent, educational explainers on loan amortisation, insurance cover, credit card minimum payments and emergency funds. Worked examples, primary sources, no product recommendations.",
        body=body,
        slug="index.html",
        active="",
        schema=schema,
    )


# --------------------------------------------------------------------------- category pages
CAT_FAQ = {
    "loans": [
        (
            "Should I choose the lowest monthly payment?",
            "Only if cash flow genuinely requires it. A lower payment usually means a longer term, which increases total interest. Compare the total cost of credit, not just the instalment.",
        ),
        (
            "What is a good interest rate?",
            "It depends entirely on your market, the loan type, the term and your credit profile. The useful comparison is between offers available to you, using the total cost of credit as the deciding number.",
        ),
        (
            "Can I pay a loan off early?",
            "Check the agreement for an early repayment charge. Many loans allow penalty-free overpayment; some do not, and a few restrict how much you may overpay each year.",
        ),
    ],
    "insurance": [
        (
            "How much cover is enough?",
            "Start with the DIME arithmetic: debts plus income replacement plus mortgage plus future education, minus existing cover and savings. Then adjust for what your family would actually need.",
        ),
        (
            "Is cheap insurance bad insurance?",
            "Not necessarily — price differences often reflect term length, underwriting and distribution costs rather than a weaker promise. What matters is the insurer's ability to pay and the exclusions in the contract.",
        ),
        (
            "What makes a claim fail?",
            "Most commonly, information that was not disclosed at application, or an exclusion that was in the policy but not read. Keep a copy of everything you submit.",
        ),
    ],
    "credit-debt": [
        (
            "Does carrying a balance build credit?",
            "No. On-time payments build your record; interest costs you money. Paying in full each month is the best of both outcomes.",
        ),
        (
            "Which debt should I clear first?",
            "Highest interest rate first costs the least. Smallest balance first is easier to persist with. Both work; scattering extra money evenly across accounts works least well.",
        ),
        (
            "Will closing cards hurt me?",
            "It can, by reducing available credit and shortening your history. Close accounts only when the risk of overspending outweighs the scoring effect.",
        ),
    ],
    "saving-investing": [
        (
            "How much should I keep in cash?",
            "Enough to cover essential spending for the number of months your income risk justifies: three months for stable dual incomes, six to twelve where income is variable or a single income supports a household.",
        ),
        (
            "What is a real return?",
            "The return after tax and inflation. It is the only figure that shows whether your purchasing power is growing or shrinking.",
        ),
        (
            "Should I invest money that I might need next year?",
            "No. Money with a short horizon belongs in an insured, accessible account. Volatility is only tolerable when you have time to wait it out.",
        ),
    ],
}


def build_category(key):
    c = CATS[key]
    arts = [a for a in ARTICLES if a["cat"][1] == key]
    cards = "".join(post_card(a, root="") for a in arts)
    extra = ""
    if key == "loans":
        extra = f'<section class="section alt"><div class="wrap">{sec_head("Calculator","Run your own numbers")}{calc_loan()}</div></section>'
    if key == "saving-investing":
        extra = f'<section class="section alt"><div class="wrap">{sec_head("Calculator","Size your buffer")}{calc_fund()}</div></section>'
    if key == "insurance":
        extra = f'<section class="section alt"><div class="wrap">{sec_head("Calculator","Estimate the cover you need")}{calc_ins()}</div></section>'
    if key == "credit-debt":
        extra = f'<section class="section alt"><div class="wrap">{sec_head("Calculator","Compare payoff strategies")}{calc_debt()}</div></section>'
    faqs = "".join(
        f"<details><summary>{q}</summary><div class='a'><p>{a}</p></div></details>"
        for q, a in CAT_FAQ[key]
    )
    body = f"""
<div class="page-head"><div class="wrap">
  <div class="crumbs"><a href="index.html">Home</a> › <span>{c['name']}</span></div>
  <h1>{c['title']}</h1>
  <p class="lede">{c['desc']}</p>
</div></div>

{hero_image(c['img'], c['alt'])}

{ad(f'{key}-top', "Responsive display unit", "Below the page heading, above the first block of real content. Keeps the top of the page useful and the ad clearly separated from navigation.")}

<section class="section">
  <div class="wrap" style="max-width:860px">
    <div class="prose" style="max-width:none">
      <div class="eyebrow">Overview</div>
      {c['intro']}
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    {sec_head("Guides", f"{c['name']} — what we have published so far")}
    <div class="grid g-3">{cards}</div>
    <div style="margin-top:30px" class="card">
      <h3>What is coming next</h3>
      <p style="color:var(--muted);margin:0">We add guides when a reader question repeats often enough to be worth answering properly, and we revise existing ones whenever a rule, rate or fee changes. If a page here looks out of date, tell us through the <a href="contact.html">contact page</a> — corrections are published, not silently patched.</p>
    </div>
  </div>
</section>

{ad(f'{key}-in-content', "In-article / in-feed responsive", "Placed between content blocks, never inside a sentence or directly above a link list.")}

{extra}

<section class="section">
  <div class="wrap-n wrap">
    {sec_head("Quick answers", f"{c['name']}: questions we get asked most", "", center=True)}
    <div class="faq">{faqs}</div>
  </div>
</section>
"""
    schema = [
        {
            "@context": "https://schema.org",
            "@type": "CollectionPage",
            "name": c["title"],
            "description": c["desc"],
            "url": f"{CFG['domain']}/{key}.html",
            "inLanguage": "en",
            "isPartOf": {"@type": "WebSite", "name": CFG["name"], "url": CFG["domain"]},
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": 1,
                    "name": "Home",
                    "item": CFG["domain"] + "/",
                },
                {"@type": "ListItem", "position": 2, "name": c["short"]},
            ],
        },
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": q,
                    "acceptedAnswer": {"@type": "Answer", "text": a},
                }
                for q, a in CAT_FAQ[key]
            ],
        },
    ]
    title = f"{c['short']} — guides and explanations | {CFG['name']}"
    return shell(
        title=title,
        desc=c["desc"],
        body=body,
        slug=f"{key}.html",
        active=key,
        schema=schema,
    )


# --------------------------------------------------------------------------- articles index + tools
def build_articles_index():
    cards = "".join(post_card(a, root="") for a in ARTICLES)
    body = f"""
<div class="page-head"><div class="wrap">
  <div class="crumbs"><a href="index.html">Home</a> › <span>All guides</span></div>
  <h1>Every guide on FinPath</h1>
  <p class="lede">Six long-form explainers, each written to be useful on its own, each linking to the primary sources behind every number. New guides are added monthly and existing ones are revised when rules change.</p>
</div></div>
{ad('articles-top', "Responsive display unit", "Below the heading on the index page.")}
<section class="section">
  <div class="wrap">
    <div class="grid g-3">{cards}</div>
    <div style="margin-top:34px" class="news">{''}</div>
  </div>
</section>
<section class="section alt">
  <div class="wrap">
    {sec_head("How we work", "What every guide has in common",
              "Consistent structure is what makes a library useful — and what makes it clear that the content is original rather than scraped.")}
    <div class="grid g-3">
      <div class="card"><div class="ic" style="width:44px;height:44px;border-radius:13px;display:grid;place-items:center;background:var(--violet-soft);color:var(--violet);margin-bottom:14px">{icon('search')}</div>
        <h3>A stated question</h3><p>Each guide answers one question a reader actually has, in the first two paragraphs, before any background.</p></div>
      <div class="card"><div class="ic" style="width:44px;height:44px;border-radius:13px;display:grid;place-items:center;background:var(--violet-soft);color:var(--violet);margin-bottom:14px">{icon('calc')}</div>
        <h3>Worked arithmetic</h3><p>Real numbers, shown step by step, so you can check the maths and re-run it with your own figures.</p></div>
      <div class="card"><div class="ic" style="width:44px;height:44px;border-radius:13px;display:grid;place-items:center;background:var(--violet-soft);color:var(--violet);margin-bottom:14px">{icon('lock')}</div>
        <h3>Primary sources</h3><p>Regulators, tax authorities and statutes are linked directly. No claim rests on "experts say".</p></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">{newsletter()}</div>
</section>
"""
    return shell(
        title=f"All guides | {CFG['name']}",
        desc="Browse every FinPath guide: loan amortisation, insurance cover, credit card minimums, emergency funds, tax wrappers and national savings.",
        body=body,
        slug="articles.html",
        active="articles",
    )


def build_tools():
    cur = """<div class="field" style="max-width:220px"><label for="cur">Currency symbol</label>
    <select id="cur"><option value="$">$ — Dollar</option><option value="£">£ — Pound</option><option value="€">€ — Euro</option>
    <option value="C$">C$ — Canadian Dollar</option><option value="A$">A$ — Australian Dollar</option><option value="AED ">AED — Dirham</option>
    <option value="₹">₹ — Indian Rupee</option></select></div>"""
    body = f"""
<div class="page-head"><div class="wrap">
  <div class="crumbs"><a href="index.html">Home</a> › <span>Tools</span></div>
  <h1>Four calculators, no sign-up</h1>
  <p class="lede">These run entirely in your browser — nothing you type is sent anywhere, stored or shared. They are estimates for planning, not quotes or advice.</p>
</div></div>
{ad('tools-top', "Responsive display unit", "Below the heading. Tools pages hold attention well, so a single unit here performs better than two stacked.")}
<section class="section">
  <div class="wrap">
    <div class="wrap-n" style="padding-left:0;padding-right:0;margin-bottom:26px">{cur}</div>
    {calc_loan()}
    <div style="height:34px"></div>
    {calc_fund()}
    <div style="height:34px"></div>
    {calc_ins()}
    <div style="height:34px"></div>
    {calc_debt()}
    <p class="note" style="margin-top:26px">Estimates only. Lenders, insurers and savings providers calculate interest, fees and charges according to their own agreements and local rules. Nothing here is a quote, an offer, or advice.</p>
  </div>
</section>
{ad('tools-bottom', "In-content responsive unit", "Between the last calculator and the reading list.")}
<section class="section alt">
  <div class="wrap">
    {sec_head("Read the method", "The guides behind these calculators")}
    <div class="grid g-3">{''.join(post_card(a, root='') for a in ARTICLES[:3])}</div>
  </div>
</section>
<section class="section">
  <div class="wrap">{newsletter()}</div>
</section>
"""
    return shell(
        title=f"Free financial calculators | {CFG['name']}",
        desc="Loan payment and total cost, emergency fund, life insurance cover and debt payoff calculators. Free, no sign-up, nothing stored.",
        body=body,
        slug="tools.html",
        active="",
    )


# --------------------------------------------------------------------------- article page
def build_article(a):
    body_html = a["body"]
    ad_article = ad(
        f"article-in-content-{a['slug'][:18]}",
        "In-article responsive unit",
        "Placed immediately after the first substantive section, where the reader has started reading but has not yet reached the end. This is the highest-performing placement on a text page.",
    )
    if "<!--AD-->" in body_html:
        body_html = body_html.replace("<!--AD-->", ad_article, 1)
    else:
        body_html = ad_article + body_html
    bottom_ad = ad(
        f"article-bottom-{a['slug'][:18]}",
        "Multiplex / matched content unit",
        "At the end of the article, before the author box. Readers who finish a piece are the most engaged audience you have.",
    )
    mid_figure = ""
    if a.get("mid_img"):
        mid_figure = figure(
            a["mid_img"], a.get("mid_alt", ""), a.get("mid_caption", ""), root="../"
        )

    if '<h2 id="faq"' in body_html:
        body_html = body_html.replace('<h2 id="faq"', bottom_ad + '\n<h2 id="faq"', 1)
    else:
        body_html += bottom_ad

    takeaways = "".join(f"<li>{t}</li>" for t in a["takeaways"])
    sources = "".join(
        f'<li>{html.escape(s[0])} — <a href="{s[1]}" rel="noopener nofollow">{html.escape(s[1].replace("https://","").rstrip("/"))}</a></li>'
        for s in a["sources"]
    )
    rel = [BY_SLUG[s] for s in a["related"] if s in BY_SLUG][:3]
    related = "".join(post_card(r, root="../") for r in rel)
    sidebar_ad = ad(
        f"article-sidebar-{a['slug'][:18]}",
        "300×250 and 300×600 responsive unit",
        "Sticky sidebar unit. Desktop only — it disappears on small screens along with the sidebar column.",
    )
    cat_key = a["cat"][1]
    cat_name = CATS[cat_key]["name"]

    body = f"""
<div class="progress" aria-hidden="true"></div>
<div class="page-head">
  <div class="wrap">
    <div class="crumbs"><a href="../index.html">Home</a> › <a href="../articles.html#{cat_key}">{cat_name}</a> › <span>{a['cat'][0]}</span></div>
    <h1>{a['title']}</h1>
    <p class="lede">{a['lede']}</p>
    <div class="article-meta">
      <span class="who"><img class="meta-logo" src="../assets/img/finpath-logo.svg" alt="FinPath logo">{CFG['editors']}</span>
      <span>·</span><span>{a['read']} min read</span>
    </div>
  </div>
</div>
{hero_image(a["img"], a.get("alt", a["card_title"]), root="../") if a.get("img") else ""}

<div class="wrap layout">
  <article class="prose">
    <div class="takeaways">
      <h2>Key points</h2>
      <ul>{takeaways}</ul>
    </div>
    {body_html}
    {mid_figure}

    <h2 id="sources">Sources and further reading</h2>
    <p class="src">Every factual claim in this guide is drawn from the sources below. We link to the regulator, tax authority or statute rather than to commentary about them.</p>
    <ul class="src">{sources}</ul>

    <div class="callout warn"><b>Not financial advice</b><p>This guide is general information for educational purposes. It does not consider your income, debts, tax position or objectives and is not a recommendation of any product, lender or insurer. Confirm current rules, rates and limits with the provider, your tax authority or a regulated professional before acting.</p></div>

    <div class="share">
      <strong>Found this useful?</strong>
      <a href="#newsletter">Get the monthly email</a><span>·</span>
      <a href="../contact.html">Report a correction</a><span>·</span>
      <a href="../articles.html#{cat_key}">More {a['cat'][0].lower()} guides</a>
    </div>
  </article>

  <aside class="side">
    <div class="side-box">
      <h4>On this page</h4>
      <ul class="toc" id="toc"></ul>
    </div>
    {sidebar_ad}
    <div class="side-box">
      <h4>Keep reading</h4>
      {''.join(f'<a class="side-link" href="{r["slug"]}.html">{r["card_title"]}</a>' for r in rel)}
      <a class="side-link" href="../articles.html">All money guides</a>
    </div>
    <div class="side-box">
      <h4>Written by</h4>
      <p style="font-size:14.5px;color:var(--muted);margin:0">{CFG['author_bio']}</p>
      <p style="font-size:14px;margin:12px 0 0"><a href="../about.html">How we work →</a></p>
    </div>
  </aside>
</div>

<div class="wrap" style="padding-bottom:40px"><div class="author-box">
  <img class="av author-logo" src="../assets/img/finpath-logo.svg" alt="FinPath logo">
  <div>
    <h4>{CFG['editors']}</h4>
    <p>{CFG['author_bio']} Questions, corrections and topic requests: <a href="../contact.html">contact page</a>.</p>
  </div>
</div></div>

<section class="section alt">
  <div class="wrap">
    {sec_head("Keep reading", "Related guides")}
    <div class="grid g-3">{related}</div>
  </div>
</section>
  <section class="section"><div class="wrap">{newsletter()}</div></section>
"""

    schema = [
        {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": a["title"],
            "description": a["dek"],
            "inLanguage": "en",
            "articleSection": a["cat"][0],
            "datePublished": a["updated"],
            "dateModified": a["updated"],
            "keywords": a["keywords"],
            "author": {
                "@type": "Organization",
                "name": CFG["editors"],
                "url": CFG["domain"],
            },
            "publisher": {
                "@type": "Organization",
                "name": CFG["name"],
                "url": CFG["domain"],
            },
            "mainEntityOfPage": {
                "@type": "WebPage",
                "@id": f"{CFG['domain']}/articles/{a['slug']}.html",
            },
            "isAccessibleForFree": True,
            "wordCount": 2100,
            "image": {
                "@type": "ImageObject",
                "url": f"{CFG['domain']}/assets/img/cover-{a.get('img','og-cover')}.jpg",
                "width": 1200,
                "height": 656,
            },
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": 1,
                    "name": "Home",
                    "item": CFG["domain"] + "/",
                },
                {
                    "@type": "ListItem",
                    "position": 2,
                    "name": CATS[cat_key]["short"],
                    "item": f"{CFG['domain']}/articles.html#{cat_key}",
                },
                {"@type": "ListItem", "position": 3, "name": a["card_title"]},
            ],
        },
    ]
    return shell(
        title=f"{a['title']} | {CFG['name']}",
        desc=a["dek"],
        body=body,
        slug=f"articles/{a['slug']}.html",
        active=cat_key,
        root="../",
        schema=schema,
    )


# --------------------------------------------------------------------------- static pages
def build_about():
    body = f"""
<div class="page-head"><div class="wrap">
  <div class="crumbs"><a href="index.html">Home</a> › <span>About</span></div>
  <h1>About FinPath</h1>
  <p class="lede">An independent, advertising-supported publication about borrowing, insurance and household money — written for readers rather than for sales targets.</p>
</div></div>
{hero_image("about-desk", "An editor's research desk with reports, a laptop and a notebook")}
<section class="section">
  <div class="wrap" style="max-width:820px">
    <div class="prose">
      <h2 id="why">Why this site exists</h2>
      <p>Most financial information written for consumers is produced by organisations that profit when you buy something. That does not make it wrong — but it does mean the questions that matter to a borrower are often missing: what happens on early repayment, what the fee actually totals, how long a debt takes to clear at the minimum, what a claim looks like when it is declined.</p>
      <p>FinPath exists to answer those questions properly. We read the primary sources — legislation, regulator rules, tax authority guidance, product disclosure documents — and translate them into plain language with worked arithmetic. Where we cannot verify something, we say so or leave it out.</p>

      <h2 id="how">How we work</h2>
      <ul>
        <li><strong>Written by humans, for a specific reader.</strong> Each guide starts from a question people actually ask, and every number in it is explained rather than asserted.</li>
        <li><strong>Primary sources, linked.</strong> Regulators, tax authorities, statutes and central banks — not other blogs.</li>
        <li><strong>Dated reviews.</strong> Every guide carries a last-updated date. Rates, limits and rules move; stale pages are a disservice.</li>
        <li><strong>No product recommendations.</strong> We explain how products work and how to compare them. We do not tell you which one to buy, because doing that responsibly requires knowing your circumstances and, in most jurisdictions, a licence we do not hold.</li>
        <li><strong>Corrections published.</strong> If we get something wrong, we fix it and say what changed.</li>
      </ul>

      <h2 id="money">How we make money</h2>
      <p>Through display advertising. Ads are labelled and separated from editorial content, they are never disguised as navigation or as part of an article, and we never place an ad inside a sentence or design a button that pretends to be an ad. Advertisers have no influence over what we cover or what we write — the ad inventory is bought programmatically, which means the businesses advertising here have not seen our content and we have not agreed anything with them.</p>
      <p>We do not accept sponsored articles, paid links, affiliate commissions or payments to appear in a comparison. If that ever changes, the disclosure will be at the top of the page it applies to.</p>

      <h2 id="who">Who writes it</h2>
      <p>{CFG['author_bio']} We are not a licensed adviser and we do not pretend to be one. What we are is a research desk that has read the disclosure documents so you do not have to read all of them.</p>

      <h2 id="contact">Getting in touch</h2>
      <p>Corrections, questions and topic requests are all welcome — <a href="contact.html">contact us</a> or email <a href="mailto:{CFG['email']}">{CFG['email']}</a>.</p>
    </div>
  </div>
</section>
"""
    return shell(
        title=f"About {CFG['name']} — who writes this and how it is funded",
        desc="FinPath is an independent, ad-supported publisher of educational money guides. No product recommendations, primary sources only, published corrections.",
        body=body,
        slug="about.html",
        active="about",
    )


def build_editorial():
    body = f"""
<div class="page-head"><div class="wrap">
  <div class="crumbs"><a href="index.html">Home</a> › <span>Editorial standards</span></div>
  <h1>Editorial standards</h1>
  <p class="lede">The rules we hold ourselves to, written down so you can hold us to them.</p>
</div></div>
<section class="section"><div class="wrap" style="max-width:820px"><div class="prose">
  <h2 id="accuracy">Accuracy and sourcing</h2>
  <ul>
    <li>Every factual claim about a rule, rate, fee, limit or legal requirement is linked to a primary source: the regulator, the tax authority, the statute or the provider's own disclosure document.</li>
    <li>We distinguish clearly between what is required by law, what is market practice, and what is our own arithmetic.</li>
    <li>Estimates and examples are labelled as estimates, and we show the assumptions behind them.</li>
    <li>Where credible sources disagree, we say so rather than picking the more convenient figure.</li>
  </ul>

  <h2 id="independence">Independence</h2>
  <ul>
    <li>No advertiser, lender, insurer or affiliate programme has any input into what we publish.</li>
    <li>We do not accept payment for coverage, for reviews, for "best of" placements or for links.</li>
    <li>Advertising is served programmatically and clearly separated from editorial content.</li>
    <li>Nothing on this site is a personalised recommendation of a financial product.</li>
  </ul>

  <h2 id="writing">How articles are produced</h2>
  <ol>
    <li><strong>Question first.</strong> We start from a question readers actually ask, and answer it in the opening paragraphs.</li>
    <li><strong>Research from source.</strong> Primary documents are read directly. We do not build articles from other websites' summaries.</li>
    <li><strong>Worked numbers.</strong> Where a concept is arithmetic, we show the arithmetic with a realistic example that a reader can reproduce.</li>
    <li><strong>Review.</strong> Each article is checked for accuracy, for clarity to a non-specialist reader, and for anything that could be read as a recommendation.</li>
    <li><strong>Review dates.</strong> Articles are revisited when the underlying rules change, and the last-updated date changes whenever the content does.</li>
  </ol>

  <h2 id="corrections">Corrections</h2>
  <p>If you believe something here is wrong, email <a href="mailto:{CFG['email']}">{CFG['email']}</a> or use the <a href="contact.html">contact page</a>, ideally with a link to the source you are relying on. We aim to assess corrections within a few working days. Where a correction changes a figure or a conclusion, we update the article, change the review date, and add a note describing what changed. We do not quietly delete content.</p>

  <h2 id="limits">What we are not</h2>
  <p>We are not a licensed financial adviser, insurance broker, tax adviser or lawyer, and this site does not provide advice, a recommendation or an offer. We do not know your income, debts, tax status, health or objectives — and without those, any recommendation would be guesswork. For decisions with real consequences, consult a regulated professional in your country.</p>
</div></div></section>
"""
    return shell(
        title=f"Editorial standards | {CFG['name']}",
        desc="Our sourcing rules, independence policy, review process and corrections policy — published so readers can verify how FinPath content is produced.",
        body=body,
        slug="editorial-standards.html",
        active="about",
    )


def build_contact():
    body = f"""
<div class="page-head"><div class="wrap">
  <div class="crumbs"><a href="index.html">Home</a> › <span>Contact</span></div>
  <h1>Contact and corrections</h1>
  <p class="lede">Tell us what is wrong, what is missing, or what you could not find an answer to. Reader questions are the main source of new guides.</p>
</div></div>
<section class="section"><div class="wrap" style="padding-top:0">
  <div class="prose">
    <h2 id="email">Email</h2>
    <p>General and editorial: <a href="mailto:{CFG['email']}">{CFG['email']}</a><br>
    Corrections: same address, please include "correction" in the subject and a link to your source.</p>
    <h2 id="what">What we can help with</h2>
    <ul>
      <li>Corrections to published figures, links or explanations.</li>
      <li>Requests for a topic to be covered.</li>
      <li>Questions about how a guide was researched or reviewed.</li>
      <li>Accessibility problems with the site.</li>
    </ul>
    <h2 id="limits">What we cannot do</h2>
    <ul>
      <li><strong>Give personal advice.</strong> We cannot tell you what to do with your money, which product to buy, or whether a specific offer is right for you.</li>
      <li><strong>Act on your behalf.</strong> We cannot contact your bank, insurer or lender, or intervene in a dispute. For unresolved complaints use the official routes: the <a href="https://www.financial-ombudsman.org.uk/">Financial Ombudsman Service</a> in the UK, or your state insurance department via <a href="https://content.naic.org/">NAIC</a> and the <a href="https://www.consumerfinance.gov/complaint/">CFPB complaint system</a> in the US.</li>
      <li><strong>Provide legal or tax advice.</strong> Consult a qualified professional in your jurisdiction.</li>
    </ul>
    <h2 id="form">Send a message</h2>
    <form name="contact" method="POST" data-netlify="true" action="contact.html" style="max-width:560px">
      <input type="hidden" name="form-name" value="contact">
      <div class="field"><label for="c-name">Your name</label><input id="c-name" name="name" type="text" required></div>
      <div class="field"><label for="c-email">Email</label><input id="c-email" name="email" type="email" required></div>
      <div class="field"><label for="c-subject">Subject</label>
        <select id="c-subject" name="subject">
          <option>Correction</option><option>Topic request</option><option>Editorial question</option><option>Accessibility</option><option>Other</option>
        </select></div>
      <div class="field"><label for="c-msg">Message</label><textarea id="c-msg" name="message" rows="6" required style="width:100%;font:inherit;padding:12px 14px;border-radius:10px;border:1px solid var(--line-2)"></textarea></div>
      <button class="btn btn-primary" type="submit">Send message</button>
      <p class="note" style="margin-top:14px">This form is ready for Netlify Forms. If you host elsewhere, point it at Formspree, Basin or your own endpoint — see the README. We do not sell or share contact details.</p>
    </form>
  </div>
</div></section>
"""
    return shell(
        title=f"Contact and corrections | {CFG['name']}",
        desc="Contact FinPath for corrections, topic requests or editorial questions. We cannot provide personal financial advice.",
        body=body,
        slug="contact.html",
        active="about",
    )


def legal_page(slug, h1, lede, sections, title=None):
    inner = "".join(f'<h2 id="s{i+1}">{h}</h2>{b}' for i, (h, b) in enumerate(sections))
    body = f"""
<div class="page-head"><div class="wrap">
  <div class="crumbs"><a href="index.html">Home</a> › <span>{h1}</span></div>
  <h1>{h1}</h1>
  <p class="lede">{lede}</p>
  <div class="article-meta"><span>Applies to this website only</span></div>
</div></div>
<section class="section"><div class="wrap" style="max-width:820px"><div class="prose">{inner}</div></div></section>
"""
    return shell(
        title=title or f"{h1} | {CFG['name']}", desc=lede, body=body, slug=slug
    )


def build_privacy():
    secs = [
        (
            "Who we are",
            f"<p>{CFG['name']} is an independent publisher of educational money guides. You can reach us at <a href=\"mailto:{CFG['email']}\">{CFG['email']}</a>. This policy explains what data this website collects and why.</p>",
        ),
        (
            "The short version",
            "<p>We do not ask you to create an account, we do not sell personal information, and the calculators on this site run entirely in your browser — the numbers you type are never sent to us or stored on a server.</p>",
        ),
        (
            "Information we collect",
            """
<ul>
<li><strong>Server logs.</strong> Like most websites, our host records technical data such as IP address, browser type, pages requested and timestamps. This is used for security, debugging and aggregate traffic measurement.</li>
<li><strong>Email address.</strong> Only if you subscribe to the newsletter or write to us. We use it to send the newsletter or to reply.</li>
<li><strong>Contact form content.</strong> If you submit the contact form, we receive the details you provide in order to respond.</li>
</ul>""",
        ),
        (
            "Advertising and data use",
            """
    <p>This site is supported by advertising, but we keep the experience simple and do not use behavioural ad targeting or a tracking wall to gate access to content.</p>
    <p>We may still use standard website hosting data and basic analytics needed to operate and secure the site. We do not sell personal information.</p>""",
        ),
        (
            "Legal bases and your rights",
            """
    <p>Depending on where you live, you may have the right to access, correct, delete or restrict the processing of your personal data. To exercise any of these rights, email <a href="mailto:%s">%s</a>. We will respond within the period required by applicable law.</p>
    <p>We aim to follow reasonable privacy standards for every visitor, regardless of location, while keeping the site lightweight and free of unnecessary friction.</p>"""
            % (CFG["email"], CFG["email"]),
        ),
        (
            "Data retention and security",
            "<p>Server logs are retained only as long as needed for security and analytical purposes. Newsletter addresses are kept until you unsubscribe. We use HTTPS, keep software updated, and limit access to subscriber data to those who need it to send the email.</p>",
        ),
        (
            "Children",
            "<p>This site is intended for adults managing their own finances. It is not directed at children, and we do not knowingly collect personal information from children.</p>",
        ),
        (
            "Changes to this policy",
            "<p>When this policy changes materially, we update the date at the top of the page and, where appropriate, note the change on the relevant page. Continued use of the site after an update means you accept the revised version.</p>",
        ),
    ]
    return legal_page(
        "privacy-policy.html",
        "Privacy policy",
        "What this website collects, why, and how we keep the experience simple and respectful of your time.",
        secs,
    )


def build_terms():
    secs = [
        (
            "Agreement",
            f"<p>By using {CFG['name']} you agree to these terms. If you do not agree with them, please do not use the site.</p>",
        ),
        (
            "Educational purpose only",
            "<p>All content is general information published for educational purposes. It is not financial, investment, insurance, tax or legal advice, and it is not an offer or solicitation to buy any product or service. Nothing here takes account of your personal circumstances, and no adviser-client or fiduciary relationship is created by your use of the site.</p>",
        ),
        (
            "Accuracy and currency",
            "<p>We take care to cite primary sources and to date our reviews, but rules, rates, fees and product terms change frequently and vary by jurisdiction. We make no warranty that any content is accurate, complete or current on the day you read it. Always verify details with the provider, regulator or a qualified professional before acting.</p>",
        ),
        (
            "No liability",
            "<p>To the fullest extent permitted by law, we are not liable for any loss or damage arising from your use of, or reliance on, the content of this website, including decisions taken about financial products. This does not exclude liability that cannot lawfully be excluded.</p>",
        ),
        (
            "Third-party links and advertising",
            "<p>The site links to third-party websites, including regulators, tax authorities and product disclosure pages, and displays third-party advertising. We do not control external sites and are not responsible for their content, availability or data practices. Advertising is clearly separated from editorial content and is not an endorsement.</p>",
        ),
        (
            "Acceptable use",
            "<p>You agree not to scrape, republish or resell content in bulk, to attempt to interfere with the operation of the site, or to use it in a way that breaks applicable law. Short quotations with attribution and a link are welcome.</p>",
        ),
        (
            "Intellectual property",
            "<p>Text, layout, graphics and code on this site are owned by us or used under licence, unless stated otherwise. Third-party trademarks remain the property of their owners.</p>",
        ),
        (
            "Changes",
            "<p>We may update these terms. The version published on this page at the time of your visit applies.</p>",
        ),
    ]
    return legal_page(
        "terms.html",
        "Terms of use",
        "The basis on which this website and its content are provided.",
        secs,
    )


def build_disclaimer():
    secs = [
        (
            "This is not financial advice",
            f"<p>{CFG['name']} publishes general educational information about financial products and household money management. We are not a licensed financial adviser, insurance broker, tax adviser, accountant or law firm, and we do not provide personalised advice. Reading this site does not create an advisory relationship of any kind.</p>",
        ),
        (
            "No product recommendations or endorsements",
            "<p>We do not recommend, rank or endorse specific loans, credit cards, insurance policies, savings schemes or investments, and we do not receive payment for coverage. Any product, provider or scheme mentioned is used to illustrate how a category of product works. Advertisements appearing on this site are served programmatically, are labelled, and are not endorsements by us.</p>",
        ),
        (
            "Estimates and calculators",
            "<p>The calculators on this site produce estimates based on simplified models and the figures you enter. They do not include the specific terms, daily interest conventions, fees, charges or taxes that a provider would apply, and they are not quotes, offers or guarantees. Real results will differ.</p>",
        ),
        (
            "Rates, rules and figures change",
            "<p>Interest rates, tax rates, contribution limits, insurance terms and regulatory requirements change frequently and differ between countries. Figures in our guides are illustrative and were correct to the best of our knowledge at the review date shown on the page. Verify anything time-sensitive with the provider or the relevant authority before making a decision.</p>",
        ),
        (
            "Higher-rate debt and risk warnings",
            "<p>Borrowing costs money and can become unaffordable if your circumstances change. Investments can fall as well as rise, and the value of an investment is not guaranteed; past performance does not indicate future results. Insurance products may not pay out if the terms and conditions, disclosure requirements or exclusions are not met. Where a product carries specific risk warnings in your jurisdiction, those warnings apply in addition to anything stated here.</p>",
        ),
        (
            "Seek regulated advice",
            "<p>For decisions about your own situation, consult a professional regulated in your country — a licensed financial adviser, a registered insurance broker, or a qualified tax practitioner. If you are struggling with debt, free and confidential help is available in most countries, and getting it early is almost always cheaper than getting it late.</p>",
        ),
        (
            "Complaints and disputes",
            '<p>We cannot act on your behalf with any bank, insurer or lender. If you have an unresolved complaint, use the official channel in your jurisdiction: the <a href="https://www.financial-ombudsman.org.uk/">Financial Ombudsman Service</a> in the United Kingdom, or your state insurance department via <a href="https://content.naic.org/">NAIC</a> and the <a href="https://www.consumerfinance.gov/complaint/">Consumer Financial Protection Bureau</a> in the United States.</p>',
        ),
    ]
    return legal_page(
        "disclaimer.html",
        "Financial disclaimer",
        "What our content is, what it is not, and the limits of the estimates on this site.",
        secs,
    )


def build_404():
    body = f"""
<section class="section" style="padding:90px 0">
  <div class="wrap" style="max-width:720px;text-align:center">
    <div class="eyebrow" style="justify-content:center">Error 404</div>
    <h1 style="font-size:clamp(2rem,4vw,3rem)">That page has moved or never existed</h1>
    <p style="color:var(--muted);font-size:18px">Try one of the guides below, or use the navigation above. If you followed a link from another site and expected something specific, tell us and we will point you to the right place.</p>
    <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin:26px 0 40px">
      <a class="btn btn-primary" href="index.html">Go to the homepage</a>
      <a class="btn btn-ghost" href="articles.html">Browse all guides</a>
    </div>
    <div class="grid g-3">{''.join(post_card(a, root='') for a in ARTICLES[:3])}</div>
  </div>
</section>
"""
    return shell(
        title=f"Page not found | {CFG['name']}",
        desc="The page you requested could not be found. Browse FinPath guides on loans, insurance, credit and saving instead.",
        body=body,
        slug="404.html",
    )


# --------------------------------------------------------------------------- extras
def copy_ads_files():
    """ads-config.js / ads-loader.js live in /ads so a rebuild never loses them."""
    import shutil

    src_dir = ROOT / "ads"
    for name in ("ads-config.js", "ads-loader.js"):
        src = src_dir / name
        if src.exists():
            shutil.copy2(src, OUT / name)
        else:
            print(f"  ! missing {src}")


def copy_brand_asset():
    """Copy the shared FinPath wordmark into the generated site's asset tree."""
    import shutil

    src = ROOT / "assets" / "img" / "finpath-logo.svg"
    dest = OUT / "assets" / "img" / "finpath-logo.svg"
    if src.exists():
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
    else:
        print(f"  ! missing {src}")


def copy_feed_stylesheet():
    """Copy the browser-friendly RSS stylesheet into the generated site."""
    import shutil

    src = ROOT / "assets" / "feed.xsl"
    dest = OUT / "feed.xsl"
    if src.exists():
        shutil.copy2(src, dest)
    else:
        print(f"  ! missing {src}")


def build_extras(keep=None):
    urls = [(f"{CFG['domain']}/", TODAY, "1.0", "daily")]
    urls.append((f"{CFG['domain']}/articles.html", TODAY, "0.8", "weekly"))
    for a in ARTICLES:
        urls.append(
            (
                f"{CFG['domain']}/articles/{a['slug']}.html",
                a["updated"],
                "0.8",
                "monthly",
            )
        )
    for p in ["about.html", "contact.html"]:
        urls.append((f"{CFG['domain']}/{p}", TODAY, "0.5", "yearly"))
    sm = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for u, lm, pr, cf in urls:
        sm.append(
            f"  <url><loc>{u}</loc><lastmod>{lm}</lastmod><priority>{pr}</priority><changefreq>{cf}</changefreq></url>"
        )
    sm.append("</urlset>")
    (OUT / "sitemap.xml").write_text("\n".join(sm), encoding="utf-8")
    if keep is not None:
        keep.add("sitemap.xml")

    (OUT / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\n"
        "User-agent: Mediapartners-Google\nAllow: /\n\n"
        "User-agent: AdsBot-Google\nAllow: /\n\n"
        f"Sitemap: {CFG['domain']}/sitemap.xml\n",
        encoding="utf-8",
    )

    items = []
    for a in ARTICLES:
        items.append(f"""  <item>
    <title>{html.escape(a['card_title'])}</title>
    <link>{CFG['domain']}/articles/{a['slug']}.html</link>
    <guid isPermaLink="true">{CFG['domain']}/articles/{a['slug']}.html</guid>
    <description>{html.escape(a['dek'])}</description>
    <category>{html.escape(a['cat'][0])}</category>
    <pubDate>{a['updated']}T09:00:00+00:00</pubDate>
  </item>""")
    feed = f"""<?xml version="1.0" encoding="UTF-8"?>
  <?xml-stylesheet type="text/xsl" href="feed.xsl"?>
<rss version="2.0"><channel>
  <title>{CFG['name']} — {CFG['tagline']}</title>
  <link>{CFG['domain']}</link>
  <description>Independent educational guides on loans, insurance, credit and saving.</description>
  <language>en</language>
  <lastBuildDate>{TODAY}T09:00:00+00:00</lastBuildDate>
{chr(10).join(items)}
</channel></rss>"""
    (OUT / "feed.xml").write_text(feed, encoding="utf-8")
    if keep is not None:
        keep.add("feed.xml")

    (OUT / "ads.txt").write_text(
        "# After AdSense approval, replace the placeholder below with the line AdSense gives you\n"
        "# (AdSense → Account → Account information). It looks like:\n"
        "# google.com, pub-0000000000000000, DIRECT, f08c47fec0942fa0\n"
        "google.com, pub-XXXXXXXXXXXXXX, DIRECT, f08c47fec0942fa0\n",
        encoding="utf-8",
    )


# --------------------------------------------------------------------------- build
def prune_output(keep):
    """Delete generated HTML/XML that is no longer produced (renamed or removed pages)."""
    removed = []
    for path in list(OUT.rglob("*.html")) + list(OUT.rglob("*.xml")):
        rel = str(path.relative_to(OUT)).replace("\\", "/")
        if rel not in keep:
            path.unlink()
            removed.append(rel)
    return removed


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "articles").mkdir(exist_ok=True)
    written = []
    keep = set()

    def put(name, content):
        p = OUT / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
        written.append((name, len(content)))
        keep.add(name)

    put("index.html", build_home())
    put("articles.html", build_articles_index())
    for a in ARTICLES:
        put(f"articles/{a['slug']}.html", build_article(a))
    put("about.html", build_about())
    put("contact.html", build_contact())
    build_extras(keep)
    copy_ads_files()
    copy_brand_asset()
    copy_feed_stylesheet()

    removed = prune_output(keep)
    for r in removed:
        print(f"  pruned stale page: {r}")

    print(f"Built {len(written)} HTML pages into {OUT}")
    for n, s in written:
        print(f"  {n:48s} {s/1024:7.1f} KB")


if __name__ == "__main__":
    main()
