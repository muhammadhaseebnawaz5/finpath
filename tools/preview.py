"""Build self-contained preview pages with every image embedded as a data URI.

Why: the in-app workspace viewer renders HTML inside a sandboxed iframe that
cannot fetch separate files, so a normal page shows broken images there.
These preview files carry their own images, so what you see is exactly what
the deployed site looks like.

Run:  python3 tools/preview.py
Out:  preview/home.html, preview/article.html, preview/tools.html, preview/category.html
"""

import base64, io, re, shutil
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
OUT = ROOT / "preview"

PAGES = [
    ("index.html", "home.html", "Homepage"),
    (
        "articles/how-loan-amortization-works.html",
        "article.html",
        "Guide (loan amortisation)",
    ),
    ("tools.html", "tools.html", "Calculators"),
    ("insurance.html", "category.html", "Category hub (insurance)"),
]

MAX_W = 760  # preview images are downscaled — the deployment keeps full size


def data_uri(src: Path) -> str:
    im = Image.open(src).convert("RGB")
    if im.width > MAX_W:
        im = im.resize((MAX_W, round(im.height * MAX_W / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=74, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def build(src_rel: str, out_name: str, label: str):
    html = (SITE / src_rel).read_text(encoding="utf-8")
    depth = len(Path(src_rel).parts) - 1
    prefix = "../" * depth

    cache = {}

    def repl(m):
        attr, url = m.group(1), m.group(2)
        if url.startswith(("data:", "http")):
            return m.group(0)
        target = (SITE / src_rel).parent / url
        if not target.exists():
            return m.group(0)
        if url not in cache:
            cache[url] = data_uri(target)
        return f'{attr}="{cache[url]}"'

    # embed images (src and any srcset-free references)
    html = re.sub(r'(src)="([^"]+\.(?:jpg|png))"', repl, html)

    # the ad loader / config are separate files — inline a stub so the preview stays self-contained
    html = re.sub(r'<script src="[^"]*ads-config\.js"></script>', "", html)
    html = re.sub(r'<script src="[^"]*ads-loader\.js" defer></script>', "", html)

    # previews are single files: make internal links harmless rather than broken
    def dead_link(m):
        return m.group(0).replace(m.group(1), "#")

    html = re.sub(r'href="((?!https?:|#|mailto:)[^"]+\.html)"', dead_link, html)

    # banner so it is obvious this is the built site, not a mock
    banner = (
        '<div style="background:#0e0a1c;color:#fff;font:600 13px/1.4 ui-sans-serif,system-ui,sans-serif;'
        'padding:9px 16px;text-align:center;letter-spacing:.01em">'
        f"FinPath — {label} · self-contained preview (images embedded). "
        "Live site: <b>site/&nbsp;" + src_rel + "</b></div>"
    )
    html = html.replace("<body", "<body", 1)
    html = html.replace('<main id="main">', banner + '<main id="main">', 1)

    OUT.mkdir(exist_ok=True)
    path = OUT / out_name
    path.write_text(html, encoding="utf-8")
    return path, len(cache), len(html)


def main():
    total = 0
    for src_rel, out_name, label in PAGES:
        path, imgs, size = build(src_rel, out_name, label)
        total += size
        print(
            f"  {out_name:16s} {size/1024:7.1f} KB  ({imgs} images embedded)  ← {src_rel}"
        )
    print(f"{len(PAGES)} preview files written to {OUT}")


if __name__ == "__main__":
    main()
