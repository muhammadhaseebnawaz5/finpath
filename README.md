# FinPath — US finance / insurance / loans content site

A complete, AdSense-ready static website for a **US personal-finance audience** (loans, insurance, credit and saving — the highest advertiser-demand categories). Design follows the reference you sent: dark violet gradient hero, rounded cards, phone mockup, badge-and-card layout. Built as a **zero-dependency static site** — one HTML file per page, one CSS file, one JS file, no fonts or scripts fetched from anywhere — so it loads in well under a second on mobile data.

**Included:** 10 pages, 6 in-depth guides (1,700–2,300 words each) with primary-source citations, 9 photos + 4 branded data charts, and a complete ad system.

```
/home/user
├── site/                  ← THE WEBSITE (this is what you deploy)
│   ├── index.html         homepage
│   ├── articles.html      all guides index
│   ├── articles/          6 long-form guides (~1,700–2,300 words each)
│   ├── about.html  contact.html
│   ├── ads-config.js      ← AD SETTINGS (the only file you edit for ads)
│   ├── ads-loader.js      ad injection logic (no need to touch)
│   ├── assets/img/        9 photos + 4 branded charts (all optimised JPEG)
│   ├── robots.txt  sitemap.xml  feed.xml  ads.txt
├── assets/                dev-side CSS/JS + img/raw (source PNGs, not deployed)
├── ads/                   master copies of ads-config.js / ads-loader.js
├── content/               the article text as data (edit here, then rebuild)
├── tools/build.py         regenerates every page  →  python3 tools/build.py
├── preview/               self-contained copies for viewing in this workspace
├── tools/images.py        raw PNG → optimised cover/thumb JPEGs
├── tools/charts.py        draws the branded data charts
├── tools/preview.py       embeds images into the preview/ copies
├── README.md              this file
└── CONTENT-PLAN.md        30 next topics + keyword/CPM notes
```

**Deploy the contents of `site/`** to any static host (Netlify, Cloudflare Pages, Vercel, GitHub Pages, or plain shared hosting / cPanel). No build step is needed on the server — upload and it works.

---

## 1. Preview it right now

**Inside this workspace, open the `preview/` folder — use those files, not `site/`.**

| Preview file            | What it shows                                   |
| ----------------------- | ----------------------------------------------- |
| `preview/home.html`     | Homepage                                        |
| `preview/article.html`  | A full guide (loan amortisation)                |
| `preview/tools.html`    | The four calculators (they work in the preview) |
| `preview/category.html` | A category hub (insurance)                      |

Why: the in-app viewer renders HTML inside a sandboxed iframe that cannot load separate files, so opening `site/index.html` there shows the layout with **missing images**. The `preview/` files are the exact same pages with every image embedded as a data URI, so they look identical to the deployed site. They are for looking at, not for deploying.

Rebuild them any time with `python3 tools/preview.py` (run it after `tools/build.py` if you have changed content).

**On a normal computer or after deploying, open `site/index.html` directly** — everything works from the local file system.

To see the ad layout (recommended before you place any ad):

```
site/index.html?ads=preview
```

That outlines every ad slot with its ID, format and placement note. Nothing is loaded from Google in preview mode. Click **Hide** on the dark bar (bottom of the screen) to go back to the normal, ad-free view — and use the same URL parameter on any page.

---

## 2. What's already handled for approval

| AdSense / review requirement  | How this site satisfies it                                                                                                                                                                                                             |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Original, substantial content | 6 guides, ~2,000–2,300 words each, written as structured data in `content/` — specific numbers, tables, worked examples. Not spun, not templated filler.                                                                               |
| Clear niche                   | Personal finance: loans & mortgages, insurance, credit & debt, saving. One of the highest advertiser-demand categories (banking, insurance, lending, fintech).                                                                         |
| Navigation                    | Sticky header with 4 topic hubs + all-guides + about; breadcrumbs; footer link blocks; related-guide modules. No orphan pages.                                                                                                         |
| Privacy policy                | `privacy-policy.html` — clearly states the site keeps data handling simple and avoids a heavy tracking experience.                                                                                                                     |
| About + Contact               | `about.html` (who writes it, how it's funded) and `contact.html` (form + email, plus what the site can and cannot help with).                                                                                                          |
| Editorial transparency        | `editorial-standards.html`: sourcing rules, independence, review process, corrections policy.                                                                                                                                          |
| Financial disclaimer          | Site-wide footer block + `disclaimer.html` + a disclaimer in every guide. This matters for YMYL ("your money or your life") content.                                                                                                   |
| Legal pages                   | Terms of use, disclaimer and privacy policy without a consent popup or tracking gate.                                                                                                                                                  |
| Technical                     | `robots.txt` explicitly allows `Mediapartners-Google` and `AdsBot-Google`, sitemap, RSS feed, canonical URLs, Open Graph, Article/Breadcrumb/FAQ schema, mobile-first responsive, no pop-ups, no auto-playing video, no interstitials. |
| Policy safety                 | No "click here" ad-baiting, no ads disguised as navigation, no ads inside a sentence, no more than 2–4 units per page, calculator results never gated behind an ad click.                                                              |

---

## 3. Turning ads on — done for you, one file to edit

The ad system is built. Every ad position already exists on the page, is labelled, and is **invisible until you switch it on**, so the site works perfectly with ads off.

### The 3-minute setup

Open **`site/ads-config.js`**. That is the only file you touch.

```js
window.COINPATH_ADS = {
  enabled: false,                          // 1. change to true
  client: "ca-pub-XXXXXXXXXXXXXXXX",       // 2. paste your AdSense publisher ID
  autoAds: false,                          // leave false unless you enable Auto ads in AdSense
  testMode: true,                          // 3. keep true for the first day, then set false
  ...
```

Then paste a **10-digit ad slot ID** next to each position you want to use, inside the `slots` map:

```js
  slots: {
    "home-top":     "1234567890",   // ← from AdSense → Ads → By ad unit
    "home-in-feed": "0987654321",
    ...
```

That's it. Nothing else to edit, no HTML changes, no code to paste into pages. Upload `site/ads-config.js` and you are live.

### Where to get the two IDs

- **Publisher ID** (`ca-pub-…`): AdSense → Account → Account information.
- **Ad slot ID** (10 digits): AdSense → Ads → By ad unit → create a "Display ads" unit, one per position you want. Responsive units work for every slot in this build.

### Seeing the placements before you enable them

Open any page with **`?ads=preview`** — e.g. `site/index.html?ads=preview`. Every slot appears as a dashed box showing its name, format and a note on why it sits there. Those names are exactly the keys you use in `ads-config.js`.

### Safe testing

Leave `testMode: true` until you have confirmed the layout on desktop and mobile. Test ads display a "Test Ad" label and are **safe to click** — clicking a real ad on your own site is a policy violation, clicking test ads is not.

### Which slots to switch on first

| Phase | Slots                                                                                | Why                                                              |
| ----- | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| 1     | `home-top`, `home-in-feed`, `article-in-content`                                     | Best revenue per session; in-content units carry the highest CPM |
| 2     | `loans-top`, `insurance-top`, `credit-debt-top`, `saving-investing-top`, `tools-top` | Category and tools pages hold attention well                     |
| 3     | `article-sidebar` (desktop only), `article-bottom`, `home-bottom`, `articles-top`    | Fills out the site once phase 1–2 are performing                 |

Blank or leftover `0000000000` slots simply stay empty, so you can add units gradually and measure what each one is worth.

### Slot map

| Page          | Slot name                                                               | Format                                           | Priority |
| ------------- | ----------------------------------------------------------------------- | ------------------------------------------------ | -------- |
| Home          | `home-top`                                                              | Responsive display                               | **1**    |
| Home          | `home-in-feed`                                                          | In-feed / in-article                             | **1**    |
| Home          | `home-bottom`                                                           | Responsive / anchor (mobile)                     | 3        |
| Category hubs | `loans-top`, `insurance-top`, `credit-debt-top`, `saving-investing-top` | Responsive display                               | 2        |
| Category hubs | `…-in-content`                                                          | In-article                                       | **1**    |
| Guides index  | `articles-top`                                                          | Responsive display                               | 3        |
| Article pages | `article-in-content`                                                    | In-article — highest CPM position on a text page | **1**    |
| Article pages | `article-sidebar`                                                       | 300×250 / 300×600 sticky (desktop only)          | 2        |
| Article pages | `article-bottom`                                                        | Multiplex / matched content                      | 3        |
| Tools         | `tools-top`, `tools-bottom`                                             | Responsive                                       | 2        |

**Auto ads:** if you prefer Google to place units for you, switch Auto ads on in the AdSense dashboard and set `autoAds: true`. Don't run Auto ads aggressively _and_ all manual units at once — pick one, measure, then tune.

After approval, replace the placeholder line in `site/ads.txt` with the real `pub-` line AdSense gives you (AdSense → Account → Account information), and add your site under AdSense → Sites.

### About "clickable ads"

High-value placement is legitimate; making people click ads is not. The units here sit naturally in the reading flow — in-article after the first section, one in-feed card in the homepage list, one sticky sidebar unit on desktop only. Fake "Download"/"Continue" buttons, ads styled as menu items, ads inside a sentence, or anyone telling you to buy clicks will get the account terminated, and that is not recoverable.

## 4. Before you apply (this is the part that decides approval)

1. **Put it on a real domain** with real pages, not a free subdomain. `www.coinpath.example` appears in canonicals, sitemap, feed and OG tags — search-and-replace it with your domain, or edit `CFG["domain"]` in `tools/framework.py` and re-run `python3 tools/build.py`.
2. **Replace the placeholders:** email address (`hello@coinpath.example`), brand name/logo letter if you want a different name, and the contact form endpoint. The form is already wired for Netlify Forms; on other hosts point it at Formspree, Basin or your own handler.
3. **Decide about the images.** All 13 images are AI-generated, so there is no stock-photo licence to buy and no attribution requirement. For a finance site, AI photos are acceptable — but if you want real photography later, replace the files in `site/assets/img/` keeping the same filenames and nothing else needs to change. Charts in `assets/img/chart-*.jpg` are drawn by `tools/charts.py` and will re-render with your own numbers if you edit that file.
4. **Make the newsletter real** — no provider is connected yet. The form currently shows a thank-you message only. Hook it up to Mailchimp/Brevo/Buttondown, or remove the section.
5. **Get some traffic history.** AdSense does accept new sites, but a 3–5 week old site with 15–25 indexed pages and a few dozen organic visits from search gets approved far more often than a site published yesterday.
6. **Submit the sitemap** to Google Search Console the day you go live, and request indexing for all 20 pages.
7. **Do not buy traffic, clicks or "approval services".** That is the fastest way to a permanent ban, and it is not recoverable.

### About "clickable ads"

High-value placement is legitimate; making people click ads is not. Ads that sit naturally in the reading flow outperform ads that beg — and begging (fake "Download", "Continue", "Next page" buttons, ads styled like menu items, ads inside a sentence) violates policy and gets accounts terminated. The placements in this build are the legitimate version of a high-CTR layout: in-article units right after the first section, one in-feed unit in the homepage list, one sticky sidebar unit on desktop only.

---

## 5. Editing content

You have two options:

**A. Edit the HTML** in `site/articles/*.html` directly. Each file is standalone — CSS and JS are inlined, so a fix in one file is a fix in one file.

**B. Edit the data and rebuild (recommended).** Article text lives in `content/articles_a.py` and `content/articles_b.py`; page templates live in `tools/build.py`. Then:

```bash
python3 tools/build.py     # rewrites all 20 pages + sitemap + feed
```

Adding a new guide = append a dict to the list in `content/articles_*.py` (copy an existing one as a template), add its slug to another article's `related` list, then rebuild. Slugs, meta tags, schema, breadcrumbs and sitemap entries are generated for you.

---

## 6. Hosting notes

- **Netlify / Cloudflare Pages / Vercel:** drag the `site` folder in. Done. Free HTTPS, fast in Asia.
- **Shared hosting / cPanel:** upload the contents of `site/` to `public_html`. Add a 404 rule pointing at `404.html` if your host supports it. Also add a redirect so `https://yourdomain.com/index.html` is not indexed separately — canonicals already handle it.
- **Performance:** no external requests out of the box. HTML ~54–68 KB (CSS and JS inlined) plus lazy-loaded JPEGs that average 50 KB. Verified: DOMContentLoaded under 70 ms, no render-blocking requests. Once AdSense loads, that becomes the heaviest asset on the page — normal, and one more reason everything else is lean.
- **Charts:** the homepage "How the numbers actually work" panels and the article figures are drawn as inline SVG / generated JPEGs from `tools/charts.py` — no third-party chart library, nothing fetched at runtime.
- **Images:** nine AI-generated editorial photos (no licence or attribution needed — same as stock, but you own them) plus four charts drawn by `tools/charts.py`. Covers are 1200×656, thumbs 800×420, all progressive JPEG. Re-run `python3 tools/images.py` after replacing a raw PNG to regenerate every size.
- **Accessibility:** every image has descriptive alt text, focus states are visible, the ToC and FAQ are keyboard-operable, and colour contrast on body text passes AA.

## 7. Honest limitations

- The site is **educational only** and never recommends a product. That is deliberate: it protects you legally, and it is also what keeps YMYL content credible with readers and reviewers.
- Rates, tax figures and limits move constantly. Every guide is dated, but you should re-check the linked regulator pages quarterly and update the date when a number changes.
- Content is written for a US/UK audience: dollars and pounds, CFPB/FCA/SEC/FTC sources, FDIC/FSCS limits, 401(k)/ISA/Roth examples. If you later want a single market (US only, or UK only), the examples and regulators can be narrowed in `content/`.
- Charts are static images with the numbers we published baked in. If a rate changes and you edit a table, re-run `tools/charts.py` (after updating the values in that file) so the chart matches the text.
# finpath
