import re, os, glob
from urllib.parse import urlparse
bad=[]; ext={}
for f in glob.glob('site/**/*.html', recursive=True):
    base=os.path.dirname(f); src=open(f).read()
    for href in re.findall(r'(?:href|src)="([^"]+)"', src):
        if href.startswith(('http://','https://','mailto:','#','data:','tel:')):
            if href.startswith('http'):
                ext.setdefault(urlparse(href).netloc,0); ext[urlparse(href).netloc]+=1
            continue
        path=href.split('#')[0].split('?')[0]
        if not path: continue
        tgt=os.path.normpath(os.path.join(base,path))
        if not os.path.exists(tgt): bad.append((f,href,tgt))
print("broken internal links:", len(bad))
for b in bad[:20]: print("  ",b)
print("external hosts:", {k:v for k,v in sorted(ext.items(), key=lambda x:-x[1])})
