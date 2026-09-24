import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={"width":390,"height":844})
        errs=[]; pg.on("pageerror", lambda e: errs.append(str(e)))
        await pg.goto("file:///home/user/site/index.html"); await pg.wait_for_timeout(500)
        await pg.click(".burger"); await pg.wait_for_timeout(400)
        vis = await pg.evaluate("""() => {
          const n=document.getElementById('site-nav');
          const r=n.getBoundingClientRect();
          return {open:n.classList.contains('open'), h:Math.round(r.height), links:n.querySelectorAll('a').length,
                  ctaVisible: !!document.querySelector('.nav.open .top-cta') && getComputedStyle(document.querySelector('.nav.open .top-cta')).display};
        }""")
        print("mobile nav:", vis)
        await pg.screenshot(path="/home/user/shots/mob-nav-open.png")
        # article page: TOC built? progress bar?
        await pg.goto("file:///home/user/site/articles/emergency-fund-how-much.html"); await pg.wait_for_timeout(400)
        toc = await pg.evaluate("""() => ({tocItems: document.querySelectorAll('#toc a').length, first: (document.querySelector('#toc a')||{}).textContent})""")
        await pg.evaluate("window.scrollTo(0, 3000)"); await pg.wait_for_timeout(500)
        prog = await pg.evaluate("document.querySelector('.progress').style.width")
        act = await pg.evaluate("(document.querySelector('#toc a.active')||{}).textContent")
        print("toc:", toc, "progress:", prog, "active:", act)
        print("JS errors:", errs[:4])
        await b.close()
asyncio.run(main())
