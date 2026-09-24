# -*- coding: utf-8 -*-
"""Article set A: loans, insurance, credit cards."""

ARTICLES_A = [
    # --------------------------------------------------------------------------- 1
    {
        "slug": "how-loan-amortization-works",
        "cat": ("Loans", "loans"),
        "title": "How loan amortisation actually works (and why the first payments feel unfair)",
        "card_title": "How loan amortisation actually works",
        "dek": "A month-by-month breakdown of where every dollar and pound of an instalment goes — plus the fee traps that make two identical rates cost very different amounts.",
        "read": 9,
        "updated": "2026-08-19",
        "updated_h": "19 Aug 2026",
        "icon": "calc",
        "thumb": "",
        "img": "loan-documents",
        "alt": "A woman reviewing loan paperwork at a kitchen table with a laptop and calculator",
        "mid_img": "chart-amortisation",
        "mid_alt": "Chart showing how the interest portion of a $501 monthly payment falls from $156 in month one to $2 in month sixty",
        "mid_caption": "The same payment does less work in month 1 than in month 60. Extra payments made early are worth several times the same money paid late.",
        "keywords": "loan amortisation, EMI breakdown, APR vs interest rate, total cost of credit",
        "lede": "Most people compare loans on one number: the monthly payment. That single number hides everything that matters — how much interest you actually hand over, how slowly the balance falls, and what happens if your plans change halfway through.",
        "takeaways": [
            "Every instalment is two payments in one: interest on the balance you still owe, plus a repayment of the balance itself.",
            "On a $25,000 loan at 7.5% over five years, roughly 31% of the first payment is interest and only the last few payments are almost pure principal.",
            "Stretching the same loan from 3 years to 7 years cuts the monthly payment by about half but adds more than $4,200 of interest.",
            "The advertised interest rate is not the cost of the loan. Fees, insurance add-ons and compounding decide the real number.",
            "The legitimate ways to lower total cost: larger deposit, shorter term, extra payments, a better rate — in that order.",
        ],
        "body": """
<h2 id="two-payments">The two payments hiding inside one instalment</h2>
<p>An amortising loan works like a running tab. Each month the lender charges interest on whatever balance you still owe, takes that interest out of your payment first, and only then uses what is left to reduce the balance.</p>
<p>Early on, the balance is large, so the interest slice is large. That is the whole trick — and it is not a trick the lender invented to annoy you, it is simply how compound interest behaves when the clock runs in the lender's direction. When you save, the balance grows. When you borrow, the balance earns interest against you.</p>
<p>Because of that structure, the same payment does much less work in month one than in month fifty. This is why paying a little extra early is so much more powerful than paying the same amount late.</p>
<div class="callout"><b>The one-line mental model</b><p>Interest is rent on money you are still holding. The faster you hand the money back, the less rent you pay. Everything else in this article is a footnote to that sentence.</p></div>

<!--AD-->

<h2 id="worked-example">A worked example, month by month</h2>
<p>Take a $25,000 personal loan at 7.5% annual interest, repaid over 60 monthly instalments. The payment is <strong>$500.95</strong>. Here is how it breaks down.</p>
<table>
<caption class="sr">Amortisation schedule, first six months</caption>
<thead><tr><th>Month</th><th>Interest</th><th>Balance repaid</th><th>Balance left</th></tr></thead>
<tbody>
<tr><td>1</td><td class="num">$156.25</td><td class="num">$344.70</td><td class="num">$24,655.30</td></tr>
<tr><td>2</td><td class="num">$154.10</td><td class="num">$346.85</td><td class="num">$24,308.45</td></tr>
<tr><td>3</td><td class="num">$151.93</td><td class="num">$349.02</td><td class="num">$23,959.43</td></tr>
<tr><td>4</td><td class="num">$149.75</td><td class="num">$351.20</td><td class="num">$23,608.22</td></tr>
<tr><td>5</td><td class="num">$147.55</td><td class="num">$353.40</td><td class="num">$23,254.83</td></tr>
<tr><td>6</td><td class="num">$145.34</td><td class="num">$355.61</td><td class="num">$22,899.22</td></tr>
</tbody>
</table>
<p>After six months — $3,005.70 paid — the balance has fallen by only $2,100.80. The rest, $904.90, was interest. Over the full five years you repay <strong>$30,056.92</strong>: <strong>$5,056.92 of interest</strong> on a $25,000 loan.</p>
<p>Notice the shape: the interest slice shrinks by about $2 every month. By month 55 your payment is almost entirely principal. If you have ever felt that paying your loan was like walking up a down escalator, that is why.</p>

<h2 id="term-length">Term length: the trade you are actually making</h2>
<p>Same $25,000, same 7.5% rate, different terms:</p>
<table>
<thead><tr><th>Term</th><th>Monthly payment</th><th>Total interest</th><th>Total repaid</th></tr></thead>
<tbody>
<tr><td>3 years</td><td class="num">$777.66</td><td class="num">$2,995.60</td><td class="num">$27,995.60</td></tr>
<tr><td>4 years</td><td class="num">$604.47</td><td class="num">$4,014.68</td><td class="num">$29,014.68</td></tr>
<tr><td>5 years</td><td class="num">$500.95</td><td class="num">$5,056.92</td><td class="num">$30,056.92</td></tr>
<tr><td>7 years</td><td class="num">$383.46</td><td class="num">$7,210.38</td><td class="num">$32,210.38</td></tr>
</tbody>
</table>
<p>Going from three years to seven reduces the monthly payment by a little over half — but adds $4,214.78 of interest. Neither column is "wrong". Cash-flow-poor borrowers need the small payment; the total-cost-conscious borrower needs the short term. What is wrong is accepting a long term <em>without noticing</em> that you just bought breathing room on credit.</p>
<p>A useful habit: if the maximum term you can afford comfortably is five years, ask what the payment would be at four. Borrowers routinely find the difference is small, and the interest saved is not.</p>

<h2 id="rate-vs-cost">Why the quoted "rate" is not the cost of the loan</h2>
<p>Three loans can all say "7.5%" and cost wildly different amounts.</p>
<ul>
<li><strong>Fees financed into the loan.</strong> An arrangement fee of 2% added to the principal means you pay interest on the lender's own fee for the whole term.</li>
<li><strong>Flat-rate quoting.</strong> Some lenders quote a "flat" rate — interest charged on the full original amount for the full term, even as the balance drops. A flat 5% on a five-year loan is far more expensive than a 5% reducing-balance loan; the reducing-balance equivalent is roughly double the flat figure. Always ask which one you are being quoted.</li>
<li><strong>Add-on insurance and protection products.</strong> Payment protection tied to a loan can be the most expensive insurance you will ever buy, and it is often sold at the moment of maximum pressure. It is optional. Treat it as optional even when it is presented as standard.</li>
<li><strong>Variable versus fixed.</strong> A variable rate that starts 1% lower is a bet on the future direction of central bank policy. Sometimes that bet wins. Make it deliberately.</li>
<li><strong>Prepayment penalties.</strong> A loan that stops you from overpaying is priced to hold you for the full term.</li>
</ul>
<div class="callout warn"><b>Ask for the total cost of credit in writing</b><p>Not the payment. Not the rate. The total amount you will have paid once the last instalment clears, including fees and any insurance you did not ask for. Any lender that will not put that in writing is telling you something useful.</p></div>

<h2 id="lower-cost">The legitimate levers on total cost</h2>
<ol>
<li><strong>Bigger deposit or down payment.</strong> Every $1,000 you do not borrow is $1,000 that never accrues interest — plus its interest over the term. On the example above, $1,000 less borrowed saves roughly $202 of interest.</li>
<li><strong>Shorter term, if you can carry the payment.</strong> The single largest structural saving available to you.</li>
<li><strong>Scheduled overpayments.</strong> Adding a fixed amount every month and asking the lender to apply it to principal, not to next month's due date. Confirm in writing that overpayments reduce the term rather than just advance the next payment.</li>
<li><strong>Refinancing when your circumstances or the market improve.</strong> Only worth it when the interest saved exceeds refinancing costs — a common rule of thumb is that the break-even is reached within about two years, but run your own numbers.</li>
<li><strong>A better rate through better credit.</strong> A single missed payment can cost more in rate over five years than the payment itself was worth. Automate the minimum, always.</li>
</ol>

<h2 id="extra-payments">What actually happens when you pay extra</h2>
<p>If the schedule is front-loaded with interest, then extra money is at its most valuable at the start. Same $25,000 loan, same 7.5%, same five-year term — only the monthly payment changes:</p>
<table>
<thead><tr><th>You pay</th><th>Time to clear</th><th>Total interest</th><th>Saved</th><th>Finished sooner</th></tr></thead>
<tbody>
<tr><td>$500.95 (scheduled)</td><td>60 months</td><td class="num">$5,057</td><td class="num">—</td><td class="num">—</td></tr>
<tr><td>+$50 a month</td><td>54 months</td><td class="num">$4,492</td><td class="num">$565</td><td>6 months</td></tr>
<tr><td>+$100 a month</td><td>49 months</td><td class="num">$4,043</td><td class="num">$1,014</td><td>11 months</td></tr>
<tr><td>+$200 a month</td><td>41 months</td><td class="num">$3,373</td><td class="num">$1,684</td><td>19 months</td></tr>
<tr><td>+$300 a month</td><td>35 months</td><td class="num">$2,898</td><td class="num">$2,159</td><td>25 months</td></tr>
</tbody>
</table>
<p>The pattern is worth pausing on. An extra $100 a month — $1,200 over the year — removes about $1,014 of interest and eleven months of payments. You are not merely paying the loan off sooner; you are buying back time for roughly the same money.</p>
<p>Two conditions decide whether this works for you. The first is a penalty-free overpayment clause: some fixed-rate loans cap how much you can overpay each year, or charge an early repayment fee. The second is instruction — tell the lender in writing to apply the extra amount to the principal, not to advance your next due date. Lenders that apply overpayments to the next instalment will happily hold your money and still charge interest on the full balance.</p>
<p>Put the offers side by side and fill this in before you sign anything.</p>
<ul>
<li>Total cost of credit (all-in, including fees and any bundled insurance)</li>
<li>Representative APR / APRC, and whether the rate is fixed, variable, or fixed-then-variable</li>
<li>Term in months, and maximum term available</li>
<li>Arrangement / origination fee, and whether it is deducted or financed</li>
<li>Early repayment terms: penalty or none?</li>
<li>Late payment charges and what happens to the rate after a missed payment</li>
<li>Whether the rate is personalised — and what would make it rise</li>
<li>What the lender requires as security or guarantee</li>
</ul>
<p>Regulators publish borrower-facing explainers that are worth twenty minutes of your time: the US <a href="https://www.consumerfinance.gov/ask-cfpb/what-is-the-difference-between-a-loans-interest-rate-and-its-apr-en-733/">CFPB explains the difference between interest rate and APR</a> and keeps a <a href="https://www.consumerfinance.gov/complaint/">searchable complaint database</a>, while the UK's <a href="https://www.fca.org.uk/consumers">FCA consumer pages</a> cover credit products and how to complain, with unresolved disputes going to the <a href="https://www.financial-ombudsman.org.uk/">Financial Ombudsman Service</a>.</p>

<h2 id="faq">Questions people actually ask</h2>
<div class="faq">
<details><summary>Is it better to overpay my loan or save the money?</summary><div class="a"><p>Compare the loan's interest rate with the after-tax return you can safely earn. If the loan costs more than your savings earn, overpaying is a guaranteed, tax-free return. Keep a small cash buffer first, though — money inside a loan is hard to get back out, and the emergency fund exists to stop you re-borrowing at a worse rate.</p></div></details>
<details><summary>Why does my balance barely move for the first two years?</summary><div class="a"><p>Because interest is charged on the outstanding balance, which is at its highest at the start. The payment is calculated so that it stays constant while the mix inside it slowly shifts from interest to principal.</p></div></details>
<details><summary>Does paying twice a month save money?</summary><div class="a"><p>Only if the total paid per month is higher, or if interest is calculated on a daily rather than monthly basis and your extra payment lands early. Ask how interest is accrued before assuming it helps.</p></div></details>
<details><summary>Should I take the longest term to keep payments low and then overpay?</summary><div class="a"><p>This works only with real discipline and a loan that allows penalty-free overpayment. In practice, a shorter contractual term is a commitment device; a long term plus good intentions is a plan that often quietly becomes a long term plus nothing.</p></div></details>
<details><summary>What if I cannot pay?</summary><div class="a"><p>Contact the lender before you miss the payment, not after. Most lenders have hardship or restructure processes. In the US, non-profit credit counselling is available through <a href="https://www.nfcc.org/">NFCC</a> members; in the UK, <a href="https://www.stepchange.org/">StepChange</a> gives free debt advice and <a href="https://www.citizensadvice.org.uk/">Citizens Advice</a> covers wider consumer problems. If a complaint about a lender is unresolved, the UK Financial Ombudsman Service and, in the US, your state attorney general or the CFPB complaint system are the routes that actually move lenders.</p></div></details>
</div>
""",
        "sources": [
            (
                "Consumer Financial Protection Bureau — interest rate vs APR",
                "https://www.consumerfinance.gov/ask-cfpb/what-is-the-difference-between-a-loans-interest-rate-and-its-apr-en-733/",
            ),
            (
                "Financial Conduct Authority — consumer credit information",
                "https://www.fca.org.uk/consumers",
            ),
            (
                "Financial Ombudsman Service (UK) — resolving disputes with lenders",
                "https://www.financial-ombudsman.org.uk/",
            ),
            (
                "Consumer Financial Protection Bureau — submit a complaint",
                "https://www.consumerfinance.gov/complaint/",
            ),
        ],
        "faq": [],
        "related": [
            "how-credit-card-minimum-payments-work",
            "emergency-fund-how-much",
            "insurance-cover-how-much-do-you-need",
        ],
    },
    # --------------------------------------------------------------------------- 2
    {
        "slug": "insurance-cover-how-much-do-you-need",
        "cat": ("Insurance", "insurance"),
        "title": "How much life insurance cover do you actually need? A method you can run in ten minutes",
        "card_title": "How much life insurance cover do you need?",
        "dek": "The DIME method, the term-versus-whole-life trade-off, and the underwriting details that decide whether a claim is paid or declined.",
        "read": 10,
        "updated": "2026-07-28",
        "updated_h": "28 Jul 2026",
        "icon": "shield",
        "thumb": "t2",
        "img": "insurance-family",
        "alt": "Parents at home reviewing insurance documents while their child plays nearby",
        "mid_img": "health-insurance",
        "mid_alt": "A blank insurance card and a stethoscope on a clean desk",
        "mid_caption": "Protection cover is only as good as the disclosure you provided when you applied for it.",
        "keywords": "life insurance cover calculator, DIME method, term life vs whole life, claim denial",
        "lede": "Most life insurance arguments are about products. The more useful argument is about arithmetic: what number would keep the people who depend on you financially intact, and what is the cheapest honest way to cover it?",
        "takeaways": [
            "Cover is a calculation, not a feeling. Add debts, income replacement, mortgage and future education costs, then subtract what your family already has.",
            "Term insurance is usually the cheapest way to buy a large amount of pure protection; permanent policies bundle protection with a savings element that is often expensive.",
            "Non-disclosure of health history is the most common reason legitimate claims get refused. Disclose everything, in writing.",
            "Cheap cover that never pays is worse than no cover at all; free-look and cooling-off periods exist so you can read the policy after buying it.",
            "Revisit the number after every major life event: new mortgage, new child, new business, new income.",
        ],
        "body": """
<h2 id="what-it-can-do">What insurance can and cannot do</h2>
<p>Life insurance cannot make a death less painful or a diagnosis less frightening. It can do one narrow, valuable thing: turn an unpredictable financial shock into a predictable, monthly cost that your household can plan around.</p>
<p>That framing matters, because it tells you what to insure and what not to. Insure events that are unlikely but financially catastrophic. Do not insure events you can absorb with savings or a monthly budget. Extended warranties on a $400 appliance are not risk management; they are a margin business.</p>

<h2 id="dime">The DIME method: a cover number you can defend</h2>
<p>DIME is a simple additive model — Debt, Income, Mortgage, Education — minus what your family already has. It is not the only method, but it produces a defensible number in ten minutes, and it is easy to revisit.</p>
<table>
<thead><tr><th>Component</th><th>What goes in it</th><th>Example household</th></tr></thead>
<tbody>
<tr><td><strong>D</strong> — Debt</td><td>Credit cards, car loans, student loans, personal loans</td><td class="num">$15,000</td></tr>
<tr><td><strong>I</strong> — Income</td><td>Annual income × years your family would need to replace it</td><td class="num">$60,000 × 10 = $600,000</td></tr>
<tr><td><strong>M</strong> — Mortgage</td><td>Outstanding balance on the home loan</td><td class="num">$220,000</td></tr>
<tr><td><strong>E</strong> — Education</td><td>Estimated future schooling costs per child</td><td class="num">$80,000</td></tr>
<tr><td colspan="2"><strong>Total need</strong></td><td class="num"><strong>$915,000</strong></td></tr>
<tr><td colspan="2">Less existing cover through work or a policy you already hold</td><td class="num">−$250,000</td></tr>
<tr><td colspan="2"><strong>Cover to buy</strong></td><td class="num"><strong>$665,000</strong></td></tr>
</tbody>
</table>
<p>A sensible planning range is roughly 10% either side of that figure, since the income-replacement assumption is the softest number in the model. If your children are grown and your mortgage is nearly cleared, the number collapses to something small. If you are 32 with two children and a new mortgage, it is large.</p>
<div class="callout tip"><b>Choosing the income-replacement multiplier</b><p>Five years of income covers the transition. Ten years covers most of a childhood. Fifteen years is closer to "never work again" cover and costs accordingly. Pick the multiplier that matches what you would actually want for your family, then write down why — that sentence is what you will re-read at renewal.</p></div>

<!--AD-->

<h2 id="term-vs-permanent">Term versus permanent: the real trade-off</h2>
<table>
<thead><tr><th></th><th>Term life</th><th>Whole life / universal / endowment</th></tr></thead>
<tbody>
<tr><td>What it is</td><td>Pure protection for a fixed period</td><td>Protection plus a savings or investment component</td></tr>
<tr><td>Cost for the same cover</td><td>Lowest</td><td>Typically several times higher</td></tr>
<tr><td>Cash value</td><td>None</td><td>Builds, but usually slowly and with high early charges</td></tr>
<tr><td>Payout certainty</td><td>Pays if death occurs inside the term (or a return-of-premium variant pays at maturity)</td><td>Pays at death; cash-value surrender may not equal premiums paid</td></tr>
<tr><td>Complexity</td><td>Low</td><td>High — illustrations, guarantees, charges, surrender penalties</td></tr>
<tr><td>Best used for</td><td>Protecting dependants during working years</td><td>Specific needs such as inheritance planning, or where local tax rules make it worth the cost</td></tr>
</tbody>
</table>
<p>The honest summary: buy term for protection, and treat any savings capacity as a separate, transparent decision. If a permanent policy is genuinely cheaper for your circumstances — usually driven by tax rules or estate planning — it will survive being compared on a spreadsheet. If it only works when explained verbally by the person earning commission, that tells you something.</p>

<h2 id="pricing">What actually changes your premium</h2>
<ul>
<li><strong>Age.</strong> The single biggest factor. Every year you wait raises the price for the same cover.</li>
<li><strong>Health history.</strong> Conditions, medication, recent investigations, family history.</li>
<li><strong>Smoking status.</strong> Defined by the underwriter, not by you — nicotine tests are common and include some substitutes.</li>
<li><strong>Occupation and hobbies.</strong> Manual trades, aviation, climbing and motorsport attract loading or exclusions.</li>
<li><strong>Term length and sum insured.</strong> Longer term and larger cover cost more, but the cost per unit of cover often falls as the sum rises.</li>
<li><strong>Payment frequency.</strong> Monthly premiums often cost more than annual ones for identical cover.</li>
</ul>

<h2 id="underwriting">The part that decides whether your claim is paid</h2>
<p>Claims are rarely refused because an insurer "doesn't pay out". They are refused because the contract at the start and the situation at claim time do not match. Three practical protections:</p>
<ol>
<li><strong>Disclose everything, in writing.</strong> Every consultation, scan, prescription and test result the application asks about. If you are unsure whether something is relevant, mention it — and keep a copy of what you sent.</li>
<li><strong>Answer only what is asked, but answer it completely.</strong> Non-disclosure, not illness, is the usual finding in declined claims.</li>
<li><strong>Use the free-look period.</strong> After a policy is issued you usually have a short window to cancel for a refund of premiums. Read the exclusions section in that window. It is the only section that will matter at claim time.</li>
</ol>
<div class="callout warn"><b>Bought through a bank branch or agent?</b><p>Ask three questions in writing: what is the total premium over the full term, what is the surrender value after one, three and five years, and what commission is being paid. In the UK, unresolved complaints go to the <a href="https://www.financial-ombudsman.org.uk/">Financial Ombudsman Service</a>; in the US, to your state insurance department, reachable through <a href="https://content.naic.org/">NAIC</a>.</p></div>

<h2 id="compare-quotes">How to compare two quotes properly</h2>
<p>Quotes are designed to be hard to compare. Two policies can both say "£40 a month" and "£250,000 of cover" while being entirely different products. Line up the following on one page before you decide anything.</p>
<table>
<thead><tr><th>Check</th><th>Why it changes the answer</th></tr></thead>
<tbody>
<tr><td>Sum insured</td><td>A 20% larger payout for 12% more premium is usually good value; the reverse is not</td></tr>
<tr><td>Term and whether it is level or decreasing</td><td>Decreasing cover is cheaper because the payout shrinks in line with a repayment mortgage — it can leave a shortfall if you remortgage</td></tr>
<tr><td>Fixed premium or reviewable</td><td>Some policies can raise the premium later; level-term policies cannot</td></tr>
<tr><td>Payment frequency</td><td>Monthly premiums often cost more over a year than paying annually — compare the annual total, not the monthly figure</td></tr>
<tr><td>Underwriting timing</td><td>Full underwriting at application settles the price now; simplified or post-claim underwriting can be re-priced or declined years later</td></tr>
<tr><td>Exclusions and definitions</td><td>The section that decides the claim. Compare the definitions of suicide, hazardous pursuits and pre-existing conditions</td></tr>
<tr><td>Additional benefits</td><td>Waiver of premium, accelerated death benefit, children's cover — some are genuinely useful, others are padding</td></tr>
<tr><td>Insurer strength and complaint record</td><td>Check regulatory status and, in the UK, published complaints data from the Financial Ombudsman Service</td></tr>
<tr><td>Total premium over the full term</td><td>The only figure that shows what you have actually agreed to pay</td></tr>
</tbody>
</table>
<p>Two traps deserve a mention. "Free" cover that comes bundled with a mortgage or account is rarely free — it is priced into something else, and it usually ends when the underlying product ends. And a policy sold to you at a kitchen table with the papers filled in quickly is exactly the policy that generates declined claims later, because the medical questions were answered in a hurry and inaccurately.</p>
<ul>
<li><strong>Waiver of premium.</strong> Keeps cover alive if you cannot work. Often inexpensive and genuinely useful for a single-income household.</li>
<li><strong>Accelerated death benefit.</strong> Lets a terminally ill policyholder access part of the sum insured early. Often included at no cost; check the definition of terminal illness.</li>
<li><strong>Critical illness.</strong> A separate product with a definitions document that runs to many pages. Read the definitions of the conditions you care about, not the headline count of "covers 60 conditions".</li>
<li><strong>Return of premium.</strong> You pay substantially more so that premiums come back if you outlive the term. Compare it with simply buying cheaper term cover and saving the difference yourself.</li>
<li><strong>Accidental death only.</strong> Pays only for a subset of deaths. Useful as a cheap bolt-on, dangerous as your main cover.</li>
</ul>

<h2 id="cheap-cover">Cheap cover and expensive cover: what actually drives the price</h2>
<p>Price differences of 200% or more for the same nominal cover are normal, and they are almost never about the insurer being meaner. Four things explain most of it:</p>
<ol>
<li><strong>What is being promised.</strong> Pure protection costs the least. The moment a policy bundles savings, cash value or investment, you are paying for two products and the charges of both — which is why the same cover can cost three times more.</li>
<li><strong>How long the promise lasts.</strong> Cover to age 65 is a fraction of the cost of cover to age 90, because the insurer's probability of paying is enormously different.</li>
<li><strong>Who is being insured.</strong> Age, smoking status, occupation and health history are priced individually. A 35-year-old non-smoker with clean bloodwork pays a small fraction of what a 55-year-old smoker pays for the same sum insured.</li>
<li><strong>How it is distributed.</strong> Intermediated sales carry commission, and commission on permanent or investment-linked products is far larger than on term cover. That difference is the reason a salesperson may be reluctant to quote you term.</li>
</ol>
<p>The practical test: if a cheaper policy promises the same cash payout, in the same circumstances, for the same term, and the insurer is solvent and regulated, the cheaper one is not "worse cover" — it is simply less expensive. Buy what you need and keep the difference working for you elsewhere.</p>

<h2 id="buying">Buying without getting sold to</h2>
<ol>
<li>Decide the number first, using DIME. Write it down before you look at any product.</li>
<li>Get quotes for that exact number from at least three sources — an independent adviser, a comparison site or two, and a direct insurer.</li>
<li>Insist on the total premium over the full term, not just the first-year premium.</li>
<li>Check the insurer's solvency position and complaint volumes. In the UK, firms are regulated by the <a href="https://www.fca.org.uk/">FCA</a> and covered by the <a href="https://www.fscs.org.uk/">FSCS</a>; in the US, check AM Best or S&amp;P ratings and your state's guaranty association.</li>
<li>Name your beneficiary explicitly and keep the nomination current, especially after marriage, divorce or a birth.</li>
<li>Re-shop every few years. Level term cover bought at 30 is often cheaper than the same cover bought at 40, and if your dependants have grown up you may need less.</li>
</ol>

<h2 id="context">Buying cover in the UK and the US</h2>
<p>The two markets are structured differently, and the differences matter more than the products.</p>
<table>
<thead><tr><th></th><th>United Kingdom</th><th>United States</th></tr></thead>
<tbody>
<tr><td>Who regulates the sale</td><td>FCA-authorised firms; advisers must disclose whether they are independent or restricted, and what they charge</td><td>State insurance departments, coordinated through the NAIC; producers are licensed state by state</td></tr>
<tr><td>If the insurer fails</td><td>FSCS protection for UK policies, broadly 100% of a life or protection claim</td><td>State guaranty associations, typically covering a capped amount per insured</td></tr>
<tr><td>Cancellation right</td><td>Usually a 30-day cooling-off period, with premiums refunded</td><td>Most states mandate a free-look period, commonly 10 to 30 days</td></tr>
<tr><td>If you have a complaint</td><td>Financial Ombudsman Service — free to you and binding on the firm</td><td>Your state insurance department's consumer service, then the state ombudsman or attorney general</td></tr>
<tr><td>Shape of the market</td><td>Term cover dominant for pure protection; whole-of-life mainly for estate planning</td><td>Term plus permanent (whole life, universal, indexed), sold heavily through agents</td></tr>
</tbody>
</table>
<p>Two warnings that hold in both markets. Commission on a permanent or investment-linked policy can be several times the commission on equivalent term cover — worth remembering when you are told that term is "wasting money". And if a policy is presented as a "savings plan with free insurance", ask what the surrender value is after three years before signing anything. That single question ends most of these conversations.</p>

<h2 id="faq">Questions people actually ask</h2>
<div class="faq">
<details><summary>Do I need cover if I have no dependants?</summary><div class="a"><p>Usually not life cover — nobody's standard of living collapses if you die without dependants. The risks to prioritise are the ones you would otherwise fund yourself: health costs, income loss through illness or disability, and liability.</p></div></details>
<details><summary>Is cover through my employer enough?</summary><div class="a"><p>It is a good start and often generous, but it usually ends when the job ends — exactly when you may be between roles. Check the multiplier (often one to three times salary) and whether it converts to an individual policy.</p></div></details>
<details><summary>Can I get cover with a pre-existing condition?</summary><div class="a"><p>Often yes, with a loading, an exclusion, or both. Non-disclosure is what turns this into a claim dispute. If one insurer declines, another may not; underwriting is not identical across companies.</p></div></details>
<details><summary>Should I over-insure "just in case"?</summary><div class="a"><p>Over-insuring has a real cost — premiums that could have gone to savings, debt reduction or retirement. Under-insuring has a real cost too. The point of a method like DIME is to stop you guessing in either direction.</p></div></details>
<details><summary>How often should I review it?</summary><div class="a"><p>Every two to three years, and after any of these: mortgage, new child, marriage or divorce, significant income change, new business debt, or a diagnosis.</p></div></details>
</div>
""",
        "sources": [
            (
                "US Consumer Financial Protection Bureau — insurance and financial products",
                "https://www.consumerfinance.gov/",
            ),
            (
                "Financial Conduct Authority (UK) — insurance regulation",
                "https://www.fca.org.uk/",
            ),
            ("Financial Services Compensation Scheme (UK)", "https://www.fscs.org.uk/"),
            (
                "NAIC — state insurance departments and consumer help (US)",
                "https://content.naic.org/",
            ),
            (
                "Financial Ombudsman Service (UK) — insurance complaints",
                "https://www.financial-ombudsman.org.uk/",
            ),
        ],
        "faq": [],
        "related": [
            "how-loan-amortization-works",
            "emergency-fund-how-much",
            "where-to-keep-your-savings",
        ],
    },
    # --------------------------------------------------------------------------- 3
    {
        "slug": "how-credit-card-minimum-payments-work",
        "cat": ("Credit &amp; Debt", "credit-debt"),
        "title": "Minimum payments: what they really cost, and how to escape them faster",
        "card_title": "What credit card minimum payments really cost",
        "dek": "A $1,000 balance paid at the minimum can take over six years and cost more than the original debt. Here is the arithmetic, the policy background, and the exit route.",
        "read": 9,
        "updated": "2026-08-05",
        "updated_h": "5 Aug 2026",
        "icon": "card",
        "thumb": "t4",
        "img": "credit-card-statement",
        "alt": "A hand holding a plain card above a paper statement on a dark desk",
        "mid_img": "chart-minimum-payments",
        "mid_alt": "Chart showing a $1,000 balance taking 73 months at the minimum, 32 months with $25 extra, 16 months with $50 extra and 9 months with $100 extra",
        "mid_caption": "Same balance, same 22% APR. The only variable is how much you send each month.",
        "keywords": "credit card minimum payment, debt avalanche, snowball method, balance transfer, credit score",
        "lede": "A minimum payment is not a repayment plan. It is a threshold designed to keep your account current — and the maths behind it is why so many people pay for years and still owe roughly what they started with.",
        "takeaways": [
            "Minimums are usually a small percentage of the balance plus interest and fees, or a flat floor — whichever is greater.",
            "Paying only the minimum on a $1,000 balance at 22% APR takes about 73 months and costs roughly $819 in interest.",
            "Adding just $50 a month cuts that to about 16 months and roughly $157 in interest — a saving of around $660.",
            "Avalanche (highest rate first) usually costs the least; snowball (smallest balance first) usually feels the easiest and keeps people going.",
            "Balance transfers help only if you clear the balance before the promotional period ends and you count the transfer fee.",
        ],
        "body": """
<h2 id="how-minimums-work">How a minimum payment is calculated</h2>
<p>Card issuers use one of a few formulas, and the details are in your agreement:</p>
<ul>
<li><strong>Percentage of balance.</strong> Commonly 1–3% of the statement balance, plus any interest and late fees, plus any amount over your limit.</li>
<li><strong>Flat floor.</strong> A fixed minimum, often $25–$35 in the US or £5–£25 in the UK, used when the percentage calculation would produce something tiny.</li>
<li><strong>Interest-plus-fees.</strong> Some agreements require at least the interest charged that month, which means the balance never falls if you pay exactly that.</li>
</ul>
<p>That last point is the one to check on your own statement. If your minimum equals roughly the interest line, you are renting the balance indefinitely.</p>

<h2 id="cost">The arithmetic of paying only the minimum</h2>
<p>Take a $1,000 balance at 22% APR, assuming no new spending and no fee changes.</p>
<table>
<thead><tr><th>What you pay</th><th>Time to clear</th><th>Total interest</th><th>Total paid</th></tr></thead>
<tbody>
<tr><td>Minimum only (≈2% or $25, whichever is greater)</td><td>≈73 months</td><td class="num">≈$819</td><td class="num">≈$1,819</td></tr>
<tr><td>Minimum plus $50 a month</td><td>≈16 months</td><td class="num">≈$157</td><td class="num">≈$1,157</td></tr>
</tbody>
</table>
<p>Read the first row again. Six years of payments, and you hand over a sum approaching double the original debt. The second row takes one extra coffee a week out of the budget and removes about $660 of interest.</p>
<div class="callout"><b>Daily accrual is the hidden variable</b><p>Interest on most cards accrues daily on the balance. On a $4,000 balance at 24% APR that is roughly $2.63 a day — about $79 a month of pure interest before a single purchase. Cards that accrue daily make early repayment slightly better than the monthly arithmetic suggests, because paying earlier stops the clock sooner.</p></div>

<!--AD-->

<h2 id="why-it-works-this-way">Why the minimum is set where it is</h2>
<p>Under the US <a href="https://www.consumerfinance.gov/consumer-tools/credit-cards/answers/">Credit CARD Act of 2009</a>, issuers must include a "minimum payment warning" box on statements showing how long it takes to clear the balance at the minimum and what it would take to clear it in three years. The UK's <a href="https://www.fca.org.uk/consumers">FCA</a> rules require persistent-debt warnings where balances stay high month after month. These disclosures exist because regulators worked out the same thing you just read in the table: a repayment structure that can last six years on a small balance is a structural trap, not a feature.</p>
<p>None of this makes card issuers villains. They are lending unsecured money, and unsecured lending carries real default risk that has to be priced in. The point is simply to notice that the default path — pay the minimum and wait — is the path designed to maximise interest paid, not debt cleared.</p>

<h2 id="exit">The exit route, in order</h2>
<ol>
<li><strong>Stop adding to the balance.</strong> Paying down a card while still spending on it is filling a bath with the plug out. Switch routine spending to a debit card or cash for one month and watch the balance move.</li>
<li><strong>Fix a payment you can actually sustain.</strong> Not the largest number you could manage in a good month — the number you can pay in a bad one. Then automate it for the day after payday.</li>
<li><strong>Choose a targeting method.</strong> Avalanche means throwing every spare amount at the highest-rate balance; it minimises total interest. Snowball means attacking the smallest balance first; it produces early wins that keep behaviour on track. Both beat scattering extra money evenly.</li>
<li><strong>Consider a balance transfer — carefully.</strong> A promotional 0% period can genuinely help, but the transfer usually carries a fee of around 3–5% of the amount moved, and the standard rate resumes afterwards. Missing a payment can void the promotion and, in some agreements, restore interest retroactively. Do the arithmetic on the fee before you count the saving.</li>
<li><strong>Attack the cause, not just the symptom.</strong> If the balance grows every month, the problem is cash flow. Look at the three largest categories of spending and change one of them, permanently, rather than cutting a dozen small things for a fortnight.</li>
<li><strong>Ask for a lower rate.</strong> A single phone call to a current account holder who has paid on time for years is not always a wasted call.</li>
<li><strong>Get help early if the minimums are no longer affordable.</strong> Free, non-profit counselling exists in most countries — <a href="https://www.nfcc.org/">NFCC</a> in the US, <a href="https://www.stepchange.org/">StepChange</a> in the UK, <a href="https://www.citizensadvice.org.uk/">Citizens Advice</a> for general UK debt issues, the UK's <a href="https://www.citizensadvice.org.uk/">Citizens Advice</a> for wider consumer debt problems, and — for unresolved complaints about a lender — the Financial Ombudsman Service in the UK, or the CFPB complaint system and your state attorney general in the US. Debt settlement companies charging upfront fees deserve suspicion: in the US, advance fees for most for-profit debt relief are restricted by the FTC's Telemarketing Sales Rule.</li>
</ol>

<h2 id="several-debts">When there is more than one balance</h2>
<p>Most people do not have a single clean balance to attack. They have a card at 24%, a store card at 29%, a loan at 9% and a buy-now-pay-later plan that has quietly become a habit. Here is the arithmetic on a realistic pair, using $200 a month of extra money on top of the minimums:</p>
<table>
<thead><tr><th>Strategy</th><th>Order of attack</th><th>Time to clear</th><th>Total interest</th></tr></thead>
<tbody>
<tr><td><strong>Avalanche</strong></td><td>Highest rate first: $4,000 at 24%, then $2,000 at 9%</td><td>27 months</td><td class="num">$1,143</td></tr>
<tr><td><strong>Snowball</strong></td><td>Smallest balance first: $2,000 at 9%, then $4,000 at 24%</td><td>29 months</td><td class="num">$1,622</td></tr>
</tbody>
</table>
<p>The avalanche saves $479 and finishes two months earlier. The snowball clears the smaller balance in a fraction of the time, which is why it keeps people going — you can see an account at zero in month seven rather than month twenty-two.</p>
<p>There is no need to choose once and defend it forever. A common approach that gets both benefits: start with the smallest balance if you need the motivation, then switch to the highest rate once that first account is gone. The worked numbers above show the trade-off.</p>
<p>One warning from the same model: if the interest charged each month exceeds your minimum payment, no ordering strategy will save you. The balance grows. That is the moment to raise the payment, restructure the debt, or get free advice from a charity such as <a href="https://www.stepchange.org/">StepChange</a> in the UK or an <a href="https://www.nfcc.org/">NFCC</a> member agency in the US.</p>

<h2 id="credit-score">What does and does not affect your credit record</h2>
<ul>
<li><strong>Payment history</strong> carries the most weight. One 30-day late entry can sit on your file for years.</li>
<li><strong>Utilisation</strong> — how much of your available limit you use — matters a great deal. Keeping balances below about 30% of limits is the common benchmark; lower is better.</li>
<li><strong>Length of history</strong> rewards old accounts. Closing your oldest card can reduce your score for reasons unrelated to your behaviour.</li>
<li><strong>Hard searches</strong> from multiple applications in a short period add up. Rate-shopping through a provider's eligibility checker leaves only a soft search.</li>
<li><strong>Paying in full each month</strong> does not damage your score anywhere. If you hear otherwise, it is a myth.</li>
</ul>

<h2 id="warning-signs">Warning signs worth taking seriously</h2>
<ul>
<li>You know the minimum payment on each card but not the balances.</li>
<li>You use one card to pay another, or your balance rises for three consecutive months.</li>
<li>You avoid opening statements, or you have stopped checking the app.</li>
<li>You are paying for groceries on credit while carrying a balance from last year.</li>
</ul>
<p>Any of these is a normal human response to a tight month. It becomes expensive when it lasts. The earlier you look at the numbers, the smaller the number you have to look at.</p>

<h2 id="faq">Questions people actually ask</h2>
<div class="faq">
<details><summary>Does paying more than the minimum improve my credit score directly?</summary><div class="a"><p>Not directly — but it lowers your utilisation, which is a major scoring factor. The on-time payment is what the score rewards; the lower balance is what changes the ratio.</p></div></details>
<details><summary>Is the snowball method mathematically worse?</summary><div class="a"><p>Usually slightly, yes. But a method you finish beats a cheaper method you abandon in month four. If the smallest-balance win is what keeps you going, use it — then switch to avalanche once you have momentum.</p></div></details>
<details><summary>Are 0% balance transfers a trap?</summary><div class="a"><p>They are a tool with a fee and an expiry date. If you clear the balance inside the promotional period, they can save real money. If you do not, the standard rate applies to whatever is left, and you will have paid the transfer fee for the privilege.</p></div></details>
<details><summary>Should I close a card once I pay it off?</summary><div class="a"><p>Often not. Closing reduces your available credit (raising utilisation) and can shorten your credit history. Keep it open with a small recurring charge and a standing instruction to clear it, if you trust yourself with it. If you do not, closing is the honest choice.</p></div></details>
<details><summary>Can I negotiate the interest rate?</summary><div class="a"><p>Frequently, yes — particularly with a long clean payment record. Ask for a rate review, mention competing offers, and be prepared to move the balance if nothing changes.</p></div></details>
</div>
""",
        "sources": [
            (
                "Consumer Financial Protection Bureau — credit card rules and minimum payment warnings",
                "https://www.consumerfinance.gov/consumer-tools/credit-cards/answers/",
            ),
            (
                "Credit CARD Act of 2009 (US Congress)",
                "https://www.congress.gov/bill/111th-congress/house-bill/627",
            ),
            (
                "Financial Conduct Authority (UK) — consumer credit rules and persistent debt",
                "https://www.fca.org.uk/consumers",
            ),
            ("StepChange Debt Charity (UK)", "https://www.stepchange.org/"),
            ("National Foundation for Credit Counseling (US)", "https://www.nfcc.org/"),
            (
                "Federal Trade Commission — debt relief and credit repair scams",
                "https://consumer.ftc.gov/topics/debt-relief",
            ),
        ],
        "faq": [],
        "related": [
            "how-loan-amortization-works",
            "emergency-fund-how-much",
            "tax-efficient-saving-accounts-explained",
        ],
    },
]
