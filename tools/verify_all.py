import asyncio
from playwright.async_api import async_playwright
FILES=["home.html","article.html","tools.html","category.html"]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for f in FILES:
            pg=await b.new_page(viewport={"width":1440,"height":950})
            errs=[]
            pg.on("pageerror", lambda e: errs.append(str(e)))
            await pg.goto(f"file:///home/user/preview/{f}"); await pg.wait_for_timeout(700)
            r = await pg.evaluate("""() => ({
                imgs: document.images.length,
                broken: [...document.images].filter(i=>i.complete&&i.naturalWidth===0).length,
                h: document.body.scrollHeight,
                calc: !!document.querySelector('#loan'),
                loan: (document.getElementById('l-pay')||{}).textContent
            })""")
            print(f"  {f:15s} height={r['h']:5d} imgs={r['imgs']} broken={r['broken']} calculator={r['calc']} loan-pay={r['loan']} js-errors={len(errs)}")
            await pg.close()
        # mobile check on the homepage preview
        pg=await b.new_page(viewport={"width":390,"height":844})
        await pg.goto("file:///home/user/preview/home.html"); await pg.wait_for_timeout(600)
        m=await pg.evaluate("()=>({w:document.documentElement.scrollWidth,broken:[...document.images].filter(i=>i.complete&&i.naturalWidth===0).length})")
        print(f"  mobile 390px   scrollWidth={m['w']} (no h-scroll if ≤390) broken={m['broken']}")
        await pg.screenshot(path="/home/user/shots/mobile-check.png", full_page=False)
        await b.close()
asyncio.run(main())
