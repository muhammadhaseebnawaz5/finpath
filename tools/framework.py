"""FinPath static-site framework: config, shell, icons, reusable components."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "site"
ASSETS = ROOT / "assets"

CFG = {
    "name": "FinPath",
    "tagline": "Plain-English money guides",
    "domain": "https://www.finpath.example",
    "email": "muhammadhaseebnawaz5@gmail.com",
    "editors": "FinPath Editorial Team",
    "author_bio": (
        "FinPath's editorial team writes explainers on borrowing, insurance and "
        "household money. We read the primary sources — regulator guidance, "
        "statute, product disclosures and academic research — and translate them, "
        "without recommending specific products."
    ),
    "twitter": "@finpath",
}

CSS = (ASSETS / "css/style.css").read_text(encoding="utf-8")
JS = (ASSETS / "js/main.js").read_text(encoding="utf-8")


def brand_mark(root=""):
    return f'<img class="brand-mark" src="{root}assets/img/finpath-logo.svg" alt="FinPath">'


# --------------------------------------------------------------------------- icons
_P = {
    "loans": '<path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
    "card": '<rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20M6 15h4"/>',
    "chart": '<path d="M3 3v18h18"/><path d="m7 14 3-4 3 3 4-6"/>',
    "book": '<path d="M4 4h11a3 3 0 0 1 3 3v13H7a3 3 0 0 1-3-3z"/><path d="M8 4v16"/>',
    "calc": '<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M8 6h8M8 11h.01M12 11h.01M16 11h.01M8 15h.01M12 15h.01M16 15h.01M8 19h8"/>',
    "check": '<path d="m20 6-11 11-5-5"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "pen": '<path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 7 10 7 10-7"/>',
    "chat": '<path d="M21 12a8 8 0 0 1-8 8H8l-5 3 1.5-5A8 8 0 1 1 21 12z"/>',
    "lock": '<rect x="4" y="10" width="16" height="11" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/>',
    "scales": '<path d="M12 3v18M5 7h14M7 7l-3 7h6zM17 7l-3 7h6z"/>',
    "target": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3"/>',
    "heart": '<path d="M20.8 8.6a5 5 0 0 0-8.8-2 5 5 0 0 0-8.8 2c0 5 8.8 10.4 8.8 10.4S20.8 13.6 20.8 8.6z"/>',
    "home": '<path d="m3 10 9-7 9 7v10a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>',
    "trend": '<path d="m3 17 6-6 4 4 8-8"/><path d="M15 7h6v6"/>',
    "wallet": '<path d="M3 7a2 2 0 0 1 2-2h12v4"/><rect x="3" y="7" width="18" height="12" rx="2"/><path d="M17 13h.01"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a15 15 0 0 1 0 18 15 15 0 0 1 0-18z"/>',
    "flag": '<path d="M4 22V4h9l1 2h6v10h-8l-1-2H4"/>',
    "bulb": '<path d="M9 18h6M10 22h4"/><path d="M12 2a6 6 0 0 0-3.5 10.9c.5.4.8 1 .9 1.6l.1 1.5h5l.1-1.5c.1-.6.4-1.2.9-1.6A6 6 0 0 0 12 2z"/>',
    "receipt": '<path d="M6 2h12v20l-3-2-3 2-3-2-3 2z"/><path d="M9 7h6M9 11h6M9 15h3"/>',
}


def icon(name, cls="", size=None):
    body = _P.get(name, _P["check"])
    s = f' width="{size}" height="{size}"' if size else ""
    return (
        f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        f'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" '
        f'aria-hidden="true"{s}>{body}</svg>'
    )


def tick():
    return (
        '<span class="tick"><svg viewBox="0 0 12 12" fill="none" stroke="#fff" '
        'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
        '<path d="M1.5 6.5 4.5 9.5 10.5 2.5"/></svg></span>'
    )


# --------------------------------------------------------------------------- ad slots
def ad(slot, fmt, hint):
    """A hidden-when-empty ad container. Paste AdSense code inside the div."""
    return f"""<!-- ===== AD SLOT: {slot} =====
     Recommended unit: {fmt}
     Where: {hint}
     To go live: paste the AdSense <ins class="adsbygoogle"> snippet just below,
     inside the ad-slot div, and delete this comment. Nothing else to change. -->
<div class="ad-slot" data-slot="{slot}" data-format="{fmt}" data-hint="{hint}"></div>"""


# --------------------------------------------------------------------------- chrome
NAV = [
    ("All guides", "articles.html", "articles"),
    ("About", "about.html", "about"),
    ("Contact", "contact.html", "contact"),
]


def header(active="", root=""):
    def nav_link(label, href, key):
        active_class = ' class="active"' if key == active else ""
        return f'<a href="{root}{href}"{active_class}>{label}</a>'

    links = "".join(nav_link(label, href, key) for label, href, key in NAV)
    return f"""<a class="skip" href="#main">Skip to content</a>
<header class="top">
  <div class="wrap top-in">
    <a class="brand" href="{root}index.html">
      {brand_mark(root)}
    </a>
    <button class="burger" aria-label="Menu" aria-expanded="false" aria-controls="site-nav"><span></span><span></span><span></span></button>
    <nav class="nav" id="site-nav" aria-label="Main">
      {links}
      <div class="top-cta"><a class="btn btn-primary btn-sm" href="{root}articles.html">Read guides</a></div>
    </nav>
  </div>
</header>"""


def footer(root=""):
    return f"""<footer class="foot">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-about">
        <a class="brand" href="{root}index.html">{brand_mark(root)}</a>
        <p>Independent, advertising-supported explainers on borrowing, insurance, credit and household money. We don't sell or recommend financial products.</p>
      </div>
      <div>
        <h4>Topics</h4>
        <ul>
          <li><a href="{root}articles.html">All money guides</a></li>
          <li><a href="{root}articles.html#loans">Loans &amp; mortgages</a></li>
          <li><a href="{root}articles.html#insurance">Insurance</a></li>
          <li><a href="{root}articles.html#credit-debt">Credit &amp; debt</a></li>
          <li><a href="{root}articles.html#saving">Saving &amp; investing</a></li>
        </ul>
      </div>
      <div>
        <h4>About us</h4>
        <ul>
          <li><a href="{root}about.html">Who we are</a></li>
          <li><a href="{root}contact.html">Contact &amp; corrections</a></li>
          <li><a href="{root}feed.xml">RSS feed</a></li>
        </ul>
      </div>
    </div>
    <div class="disclaimer-box">
      <strong>Important:</strong> {CFG['name']} publishes general educational information only. It is not financial, insurance, tax or legal advice, and it is not a recommendation of any product, lender or insurer. Rates, limits and rules change — always confirm details with the provider or a qualified professional before you act.
    </div>
    <div class="foot-bottom">
      <span>© <span data-year>2026</span> {CFG['name']}. All rights reserved.</span>
      <span>Made for readers, not for sales targets.</span>
    </div>
  </div>
</footer>"""


def shell(
    *,
    title,
    desc,
    body,
    slug,
    active="",
    root="",
    schema=None,
    body_class="",
    canonical=None,
):
    canon = (
        canonical
        if canonical
        else (
            f"{CFG['domain']}/" if slug == "index.html" else f"{CFG['domain']}/{slug}"
        )
    )
    ld = "".join(
        f'\n<script type="application/ld+json">{json.dumps(s, separators=(",", ":"))}</script>'
        for s in (schema or [])
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#1a0f33">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{CFG['name']}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{CFG['domain']}/assets/img/og-cover.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="{CFG['twitter']}">
<link rel="icon" href="{root}assets/img/finpath-logo.svg">
<link rel="alternate" type="application/rss+xml" title="{CFG['name']} feed" href="{root}feed.xml">
<!-- ============================================================
     ADSENSE: replace the line below with your own publisher ID.
     Get it from AdSense -> Account -> Account information.
     ============================================================ -->
<meta name="google-adsense-account" content="ca-pub-XXXXXXXXXXXXXXXX">{ld}
<style>{CSS}</style>
</head>
<body{(' class="' + body_class + '"') if body_class else ""}>
{header(active, root)}
<main id="main">
{body}
</main>
{footer(root)}
<script>{JS}</script>
<script src="{root}ads-config.js"></script>
<script src="{root}ads-loader.js" defer></script>
</body>
</html>"""


def img_src(img, root=""):
    """Charts ship as chart-*.jpg, photos as cover-*.jpg."""
    return (
        f"{root}assets/img/{img}.jpg"
        if img.startswith("chart-")
        else f"{root}assets/img/cover-{img}.jpg"
    )


def figure(img, alt, caption="", root="", lazy=True):
    """Inline article figure."""
    return f"""<figure class="fig">
  <img src="{img_src(img, root)}" width="1200" height="656"
       {'loading="lazy"' if lazy else ''} decoding="async" alt="{alt}">
  {f'<figcaption>{caption}</figcaption>' if caption else ''}
</figure>"""


def hero_image(img, alt, root="", caption=""):
    return f"""<div class="wrap cat-hero">
  <img src="{img_src(img, root)}" width="1200" height="656"
       loading="eager" fetchpriority="high" decoding="async" alt="{alt}">
  {f'<p class="cap">{caption}</p>' if caption else ''}
</div>"""


def post_card(p, root="", large=False):
    cls = "card post post-lg" if large else "card post"
    img = p.get("img")
    if img:
        thumb = (
            f'<img class="thumb-img" src="{root}assets/img/thumb-{img}.jpg" '
            f'width="800" height="420" loading="lazy" decoding="async" '
            f'alt="{p.get("alt", p["card_title"])}">'
        )
    else:
        thumb = (
            f'<div class="thumb {p.get("thumb","")}">{icon(p.get("icon","book"))}</div>'
        )
    return f"""<a class="{cls}" href="{root}articles/{p['slug']}.html">
  {thumb}
  <div class="post-body">
    <div class="kicker">{p['cat'][0]}</div>
    <h3>{p['card_title']}</h3>
    <p>{p['dek']}</p>
    <div class="meta"><span>{p['read']} min read</span></div>
  </div>
</a>"""


def sec_head(eyebrow, h2, p="", center=False):
    return f"""<div class="sec-head{' center' if center else ''}">
  <div class="eyebrow">{eyebrow}</div>
  <h2>{h2}</h2>
  {f'<p>{p}</p>' if p else ''}
</div>"""
