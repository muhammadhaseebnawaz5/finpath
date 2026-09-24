import asyncio
from playwright.async_api import async_playwright
BASE = "file:///home/user/site/"

TARGETS = [
    ("index.html", "", 1440, 1000, "home-desktop"),
    ("index.html", "?ads=preview", 1440, 1000, "home-desktop-ads"),
    ("articles/how-loan-amortization-works.html", "?ads=preview", 1440, 1000, "article-desktop"),
    ("tools.html", "?ads=preview", 1440, 1000, "tools-desktop"),
    ("insurance.html", "?ads=preview", 1440, 1000, "cat-desktop"),
    ("privacy-policy.html", "", 1440, 1000, "legal-desktop"),
    ("index.html", "", 390, 844, "home-mobile"),
    ("articles/how-credit-card-minimum-payments-work.html", "", 390, 844, "article-mobile"),
]

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for path, q, w, h, name in TARGETS:
            pg = await b.new_page(viewport={"width": w, "height": h})
            errs = []
            pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
            pg.on("pageerror", lambda e: errs.append(str(e)))
            await pg.goto(BASE + path + q, wait_until="load")
            await pg.wait_for_timeout(800)
            await pg.screenshot(path=f"/home/user/shots/{name}-full.png", full_page=True)
            await pg.screenshot(path=f"/home/user/shots/{name}-top.png")
            print(f"{name:22s} JS errors: {errs[:4]}")
            await pg.close()
        await b.close()

asyncio.run(main())
