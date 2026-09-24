import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={"width":1440,"height":1000})
        errs=[]; pg.on("pageerror", lambda e: errs.append(str(e)))
        await pg.goto("file:///home/user/preview/home.html"); await pg.wait_for_timeout(800)
        h = await pg.evaluate("document.body.scrollHeight")
        broken = await pg.evaluate("[...document.images].filter(i=>i.complete&&i.naturalWidth===0).length")
        # crop around the new numbers section
        el = await pg.query_selector("text=How the numbers actually work")
        box = await el.bounding_box()
        await pg.screenshot(path="/home/user/shots/preview-full.png", full_page=True)
        print("section y:", box["y"])
        print("home preview: height", h, "broken images:", broken, "js errors:", errs[:2])
        await pg.screenshot(path="/home/user/shots/preview-full.png", full_page=True)
        await b.close()
asyncio.run(main())
