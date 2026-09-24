import asyncio, json, shutil, re
from pathlib import Path
from playwright.async_api import async_playwright

CFG = Path('site/ads-config.js'); BACKUP = CFG.read_text()
# turn ads on with a fake-but-valid-looking pub id and route the Google script to a local stub
test = BACKUP.replace('enabled: false', 'enabled: true').replace('ca-pub-XXXXXXXXXXXXXXXX', 'ca-pub-1234567890123456')
test = test.replace('"home-top":                        "0000000000"', '"home-top":                        "1111111111"')
test = test.replace('"home-in-feed":                    "0000000000"', '"home-in-feed":                    "2222222222"')
test = test.replace('"article-in-content":              "0000000000"', '"article-in-content":              "3333333333"')
CFG.write_text(test)

STUB = Path('site/adsbygoogle-stub.js')
STUB.write_text("window.adsbygoogle = window.adsbygoogle || []; window.adsbygoogle.loaded = true;")

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width":1440,"height":900})
        warns=[]
        pg.on("console", lambda m: warns.append(m.text[:110]) if m.type in ("warning","error") else None)
        await pg.route("**/pagead2.googlesyndication.com/**", lambda r: r.fulfill(
            status=200, content_type="application/javascript", body="window.adsbygoogle=window.adsbygoogle||[];window.adsbygoogle.loaded=true;"))
        await pg.goto("file:///home/user/site/index.html"); await pg.wait_for_timeout(900)
        res = await pg.evaluate("""() => {
            const ins = [...document.querySelectorAll('.ad-slot ins.adsbygoogle')];
            return ins.map(i => ({slot: i.dataset.adSlot, fmt: i.dataset.adFormat, test: i.dataset.adtest,
                                  parent: i.closest('.ad-slot').dataset.slot}));
        }""")
        print("HOME ads injected:")
        for r in res: print("   ", r)
        await pg.goto("file:///home/user/site/articles/how-loan-amortization-works.html"); await pg.wait_for_timeout(600)
        res2 = await pg.evaluate("""() => {
            const ins = [...document.querySelectorAll('.ad-slot ins.adsbygoogle')];
            return ins.map(i => i.dataset.adSlot + ' <- ' + i.closest('.ad-slot').dataset.slot);
        }""")
        print("ARTICLE ads injected:"); [print("   ", r) for r in res2]
        print("console:", warns[:4])
        await b.close()

asyncio.run(main())
