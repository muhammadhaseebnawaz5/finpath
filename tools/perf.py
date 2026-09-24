import asyncio, time
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={"width":1280,"height":800})
        for url in ["index.html","articles/how-loan-amortization-works.html","tools.html"]:
            t=time.time()
            await pg.goto("file:///home/user/site/"+url, wait_until="load")
            load=(time.time()-t)*1000
            m=await pg.evaluate("""() => {
              const r=performance.getEntriesByType('resource');
              const nav=performance.getEntriesByType('navigation')[0];
              return {requests:r.length, transfer:r.reduce((a,x)=>a+(x.transferSize||0),0),
                      dom:Math.round(nav.domContentLoadedEventEnd), load:Math.round(nav.loadEventEnd),
                      html:Math.round(nav.transferSize||0)};
            }""")
            print(f"{url:44s} wall={load:6.0f}ms  DOMContentLoaded={m['dom']}ms  externalRequests={m['requests']}  resources={m['transfer']}B")
        await b.close()
asyncio.run(main())
