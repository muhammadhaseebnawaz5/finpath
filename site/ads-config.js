/* ==========================================================================
   FinPath — AD SETTINGS
   --------------------------------------------------------------------------
   This is the ONLY file you need to edit to turn advertising on.
   Nothing loads from Google until you set  enabled: true  below.

   STEPS
   1. Get your publisher ID: AdSense → Account → Account information
      It looks like  ca-pub-1234567890123456
   2. Paste it as  client  below.
   3. In AdSense → Ads → By ad unit, create a "Display ads" unit for every
      position you want to use. Each unit gets a 10-digit ad slot ID.
      Paste each ID into the  slots  map below, next to the matching name.
      (The names are printed on every page when you open a URL with
       ?ads=preview — that shows you exactly where each one sits.)
   4. Set  enabled: true  and re-upload these three files:
      ads-config.js, ads-loader.js, and every .html page (the pages only
      need re-uploading if you changed which slots exist).

   NOTE ON AUTO ADS
   AdSense → Ads → By site → Auto ads. Google then places units for you.
   If you enable Auto ads in the dashboard, no slot IDs are needed — the
   loader already loads the AdSense script, which is all Auto ads require.
   Running Auto ads AND the manual units below on the same page is allowed
   but usually earns less than picking one and doing it well.

   TESTING
   Set  testMode: true  to request AdSense test ads. Those are safe to click
   and will not put your account at risk. Always use testMode first.
   ========================================================================== */

window.FINPATH_ADS = {
  /* master switch — false means the site loads no ad script at all */
  enabled: false,

  /* your AdSense publisher ID */
  client: "ca-pub-XXXXXXXXXXXXXXXX",

  /* true only after you have switched Auto ads on in the AdSense dashboard */
  autoAds: false,

  /* true = AdSense test ads (safe to click, shows "Test Ad") */
  testMode: true,

  /* Which page types to serve ads on. Turn individual pages off any time. */
  pages: {
    home: true,
    category: true,
    article: true,
    tools: true,
    index: true,
    legal: false, // off by default: policy pages earn little and add clutter
  },

  /* ------------------------------------------------------------------------
     Ad unit IDs. Replace each "0000000000" with the real ad slot ID.
     A slot left as 0000000000 (or deleted) simply stays empty on the page,
     so you can turn positions on one at a time and watch the revenue move.

     Suggested order to switch on:
       phase 1 — home-top, home-in-feed, article-in-content
       phase 2 — category-in-content, tools-top
       phase 3 — sidebar and bottom units
     ------------------------------------------------------------------------ */
  slots: {
    "home-top": "0000000000",
    "home-in-feed": "0000000000",
    "home-bottom": "0000000000",

    "loans-top": "0000000000",
    "loans-in-content": "0000000000",
    "insurance-top": "0000000000",
    "insurance-in-content": "0000000000",
    "credit-debt-top": "0000000000",
    "credit-debt-in-content": "0000000000",
    "saving-investing-top": "0000000000",
    "saving-investing-in-content": "0000000000",

    "tools-top": "0000000000",
    "tools-bottom": "0000000000",
    "articles-top": "0000000000",

    /* article pages: one shared unit is fine — AdSense rotates creatives.
       If you prefer a unique unit per article, add the exact slot names
       shown by ?ads=preview (they end with the article slug, shortened). */
    "article-in-content": "0000000000",
    "article-sidebar": "0000000000",
    "article-bottom": "0000000000",
  },
};
