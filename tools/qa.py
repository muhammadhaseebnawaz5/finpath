import asyncio, glob, os, re, html
from html.parser import HTMLParser
from playwright.async_api import async_playwright

VOID={'area','base','br','col','embed','hr','img','input','link','meta','source','track','wbr','path','circle','rect','line','polyline','polygon','text','use'}
class V(HTMLParser):
    def __init__(s): super().__init__(convert_charrefs=True); s.stack=[]; s.errs=[]
    def handle_starttag(s,t,a):
        if t not in VOID: s.stack.append(t)
    def handle_endtag(s,t):
        if t in VOID: return
        if s.stack and s.stack[-1]==t: s.stack.pop()
        elif t in s.stack:
            s.errs.append(f"unclosed {'/'.join(s.stack[s.stack.index(t)+1:])}"); del s.stack[s.stack.index(t):]
        else: s.errs.append(f"stray </{t}>")

pages=sorted(glob.glob('site/**/*.html', recursive=True))
bad_struct=[]; no_alt=[]; missing_img=[]
for f in pages:
    src=open(f).read()
    p=V(); p.feed(src)
    if p.errs or p.stack: bad_struct.append((f, p.errs[:2]+p.stack[:2]))
    for tag in re.findall(r'<img[^>]*>', src):
        m=re.search(r'src="([^"]+)"', tag)
        if 'alt=' not in tag: no_alt.append((f, m.group(1) if m else '?'))
        if m and not m.group(1).startswith('http'):
            tgt=os.path.normpath(os.path.join(os.path.dirname(f), m.group(1)))
            if not os.path.exists(tgt): missing_img.append((f, m.group(1)))
print(f"pages: {len(pages)}")
print(f"HTML structure errors: {len(bad_struct)}", bad_struct[:3])
print(f"images without alt:    {len(no_alt)}", no_alt[:3])
print(f"missing image files:   {len(missing_img)}", missing_img[:3])

async def js():
    async with async_playwright() as pw:
        b=await pw.chromium.launch()
        for pg_path in ["site/index.html","site/loans.html","site/tools.html","site/articles.html",
                        "site/articles/where-to-keep-your-savings.html","site/contact.html"]:
            pg=await b.new_page(viewport={"width":1440,"height":900})
            errs=[]
            pg.on("pageerror", lambda e: errs.append(str(e)))
            pg.on("console", lambda m: errs.append("console:"+m.text[:80]) if m.type=="error" else None)
            await pg.goto("file:///home/user/"+pg_path); await pg.wait_for_timeout(500)
            imgs = await pg.evaluate("""() => {
                const all=[...document.images];
                return {total:all.length, broken:all.filter(i=>i.complete && i.naturalWidth===0).length};
            }""")
            print(f"  {pg_path:52s} js-errors={len(errs)} imgs={imgs['total']} broken={imgs['broken']} {errs[:1]}")
            await pg.close()
        await b.close()
asyncio.run(js())
