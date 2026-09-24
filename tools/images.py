"""Process generated images into web-ready assets.
  raw/*.png  ->  ../cover-<name>.jpg (1200x656)  +  ../thumb-<name>.jpg (800x420)
Run:  python3 tools/images.py
"""
from pathlib import Path
from PIL import Image, ImageEnhance

RAW = Path(__file__).resolve().parent.parent / "assets" / "img" / "raw"   # source PNGs (not deployed)
OUT = Path(__file__).resolve().parent.parent / "site" / "assets" / "img"  # deployed output

COVER = (1200, 656)
THUMB = (800, 420)


def crop_resize(im, size):
    tw, th = size
    w, h = im.size
    scale = max(tw / w, th / h)
    im = im.resize((max(1, round(w * scale)), max(1, round(h * scale))), Image.LANCZOS)
    w, h = im.size
    left = (w - tw) // 2
    top = int((h - th) * 0.38)          # bias slightly above centre — faces stay in frame
    return im.crop((left, top, left + tw, top + th))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    made = []
    for src in sorted(RAW.glob("*.png")):
        name = src.stem
        im = Image.open(src).convert("RGB")
        im = ImageEnhance.Color(im).enhance(1.04)
        im = ImageEnhance.Contrast(im).enhance(1.03)

        cover = crop_resize(im, COVER)
        cover.save(OUT / f"cover-{name}.jpg", "JPEG", quality=80, optimize=True, progressive=True)

        thumb = crop_resize(im, THUMB)
        thumb.save(OUT / f"thumb-{name}.jpg", "JPEG", quality=78, optimize=True, progressive=True)
        made.append((name, (OUT / f"cover-{name}.jpg").stat().st_size,
                     (OUT / f"thumb-{name}.jpg").stat().st_size))

    # social share card: 1200x630 from the hero-adjacent image
    hero_src = RAW / "loan-documents.png"
    if hero_src.exists():
        og = crop_resize(Image.open(hero_src).convert("RGB"), (1200, 630))
        og.save(OUT / "og-cover.jpg", "JPEG", quality=88, optimize=True, progressive=True)
        made.append(("og-cover.jpg", (OUT / "og-cover.jpg").stat().st_size, 0))

    for name, c, t in made:
        print(f"  {name:26s} cover {c/1024:6.1f} KB   thumb {t/1024:6.1f} KB")
    print(f"{len(made)} assets written to {OUT}")


if __name__ == "__main__":
    main()
