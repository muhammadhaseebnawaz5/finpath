# CoinPath — 30-topic content plan (US / UK personal finance)

How this list was put together: ranked by **advertiser demand** (what banks, insurers, lenders and fintechs actually bid on) × **search intent** (people looking for an answer they will act on) × **how easy it is to write something genuinely original**. High-CPM keywords only earn if the article ranks — and AdSense approval itself depends on original, substantial writing, not keyword selection.

**CPM tiers** (display/AdSense, indicative, varies by country and season):
- **Tier 1 (highest):** insurance quotes, mortgage/refinance, credit cards, loans, investing platforms
- **Tier 2:** banking, savings products, tax-advantaged accounts, credit-score services
- **Tier 3:** budgeting and money psychology — publish these anyway; they build the topical authority that makes Tier 1 pages rank

---

## Phase 1 — deepen what already exists (weeks 1–4)
These support the six published guides and build internal links immediately.

| # | Working title | Main keyword | Tier | Why |
|---|---|---|---|---|
| 1 | Refinancing a loan: break-even maths, fees and the traps | refinance break even | T1 | Continues `how-loan-amortization-works`; refinance carries some of the most expensive clicks in the category |
| 2 | Fixed vs variable rates: what you are actually betting on | fixed vs variable rate | T1 | Evergreen; natural internal link from the amortisation guide |
| 3 | How lenders underwrite you: income, DTI, credit file, collateral | debt to income ratio | T2 | Explains *why* a rate was quoted — what people search after a rejection |
| 4 | Mortgage overpayments: the four ways lenders apply them | mortgage overpayment | T1 | High commercial intent; the "principal vs next due date" detail is genuinely useful |
| 5 | Co-signing and guarantors: what you are signing up to | cosigner meaning | T2 | High search volume, almost no honest content |
| 6 | Payment protection and loan insurance: is it worth it? | payment protection insurance | T1 | Close cousin of the cover guide; strong advertiser demand |

## Phase 2 — the insurance cluster (weeks 5–8)
Insurance is the highest-CPM vertical in personal finance. Aim for 6–8 pages that interlink and all point back to `insurance-cover-how-much-do-you-need`.

| # | Working title | Main keyword | Tier |
|---|---|---|---|
| 7 | Health insurance basics: deductibles, co-insurance, out-of-pocket maximums | out of pocket maximum | **T1** |
| 8 | Critical illness cover: reading the definitions that decide payout | critical illness definitions | T1 |
| 9 | Income protection vs life insurance: insuring your ability to earn | income protection insurance | T1 |
| 10 | Home and contents insurance: what is usually excluded | home insurance exclusions | T1 |
| 11 | Car insurance: comprehensive vs third party, and the no-claims maths | third party vs comprehensive | T1 |
| 12 | Travel insurance: pre-existing conditions and medical evacuation limits | travel insurance pre-existing | T1 |
| 13 | Group cover through your employer — and what happens when you leave | group life insurance | T2 |
| 14 | How to file a claim without losing money to paperwork | insurance claim process | T2 |

## Phase 3 — credit, debt and tax wrappers (weeks 9–12)

| # | Working title | Main keyword | Tier |
|---|---|---|---|
| 15 | Credit utilisation: why 30% is the wrong number to aim at | credit utilisation | T2 |
| 16 | Reading your credit report line by line | how to read credit report | T1 (credit-score services bid hard) |
| 17 | Debt consolidation loans: when they help and when they hide the problem | debt consolidation loan | **T1** |
| 18 | Snowball vs avalanche, with a spreadsheet you can copy | debt snowball vs avalanche | T1 |
| 19 | Escaping high-cost short-term credit | payday loan alternatives | T1 (keep it strictly educational) |
| 20 | 401(k) vs IRA vs Roth: order of operations for US savers | roth vs traditional | T1 |
| 21 | Pension or ISA? A UK decision framework | pension vs isa | T1 |
| 22 | Inflation and real returns: the number that decides if saving works | real return calculation | T2 |
| 23 | Index funds vs managed funds: what the fee difference costs | index fund fees | T1 |

## Phase 4 — acquisition and household money (weeks 13–16)

| # | Working title | Main keyword | Tier |
|---|---|---|---|
| 24 | Mortgage pre-approval: what it does and does not lock in | mortgage pre approval | **T1** |
| 25 | First-time buyer schemes explained (US and UK, side by side) | first time buyer scheme | T1 |
| 26 | Student loans: repayment plans and whether to overpay | student loan repayment | T1 |
| 27 | Remittances and multi-currency accounts: cutting the hidden fee | best way to send money abroad | T1 (transfer services pay well) |
| 28 | Salary sacrifice, 401(k) match and the raise you never see | salary sacrifice explained | T2 |
| 29 | What to do with a windfall: a written order of operations | what to do with a windfall | T2 |
| 30 | Side income and tax: freelancers, gig work and the first return | freelancer tax basics | T1 (huge, growing audience) |

---

## Publishing rhythm and internal-linking rules

- **2 quality pages a week beats 10 thin ones.** Thin, near-duplicate pages are the number one reason sites fail review or get dropped later.
- Every new article links **out** to at least two existing guides and gets linked **back** from one, with descriptive anchor text. `tools/build.py` generates the related-guides module — just add the new slug to a neighbouring article's `related` list and rebuild.
- Every article: worked numbers, one table, one FAQ block (schema auto-generated), primary-source links, a dated review. That structure is also what makes a page read as unmistakably human-written to a reviewer.
- Update cadence: re-check rates, fees, limits and tax figures every quarter; change the review date whenever a number changes. A visible "Updated" date on genuinely updated content is one of the cheapest ranking wins available.
- **Never publish:** "top 10 best loans in X", "best credit card for X", guaranteed-return claims, or anything that reads like advice for a named person. Keep it educational — that is also what keeps you inside AdSense policy.
- **Images:** every new article needs one photo (from `assets/img/raw/` + `tools/images.py`) or a chart (`tools/charts.py`). Add `img`, `alt` and optionally `mid_img`, `mid_alt`, `mid_caption` to the article dict and the layout does the rest.

## Metrics to watch after approval
- **RPV** (revenue per 1,000 pageviews) by page type — if article pages beat the homepage, shift internal linking toward articles.
- **Viewability** in AdSense (target 50%+ on the in-article unit). Below that, the unit is too far down the page — move it after section one.
- **Scroll depth** at 50% / 90%. Under 40% at halfway means the intro is too long, not that the article is too long.
- **Queries in Search Console.** Pages ranking for "how much", "explained" and "vs" are your best templates — write more of those shapes.
