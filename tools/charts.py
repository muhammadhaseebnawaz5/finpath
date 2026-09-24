"""Render branded editorial charts for the articles (no stock photos needed).
Writes JPGs into site/assets/img/.  Run: python3 tools/charts.py
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent.parent / "site" / "assets" / "img"
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
W, H = 1200, 656

INK = (26, 20, 48)
MUTED = (109, 102, 140)
LINE = (226, 222, 240)
BG = (250, 249, 254)
VIOLET = (124, 58, 237)
VIOLET_L = (196, 181, 253)
PINK = (236, 72, 153)
TEAL = (14, 165, 164)
AMBER = (245, 158, 11)
GREEN = (18, 153, 107)


def F(size, bold=False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(f"{FONT_DIR}/{name}", size)


def new_canvas():
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    for x in range(0, W, 26):
        for y in range(0, H, 26):
            d.point((x, y), fill=(238, 236, 248))
    return im, d


def header(d, kicker, title, sub=None):
    d.text((64, 46), kicker.upper(), font=F(17, True), fill=VIOLET)
    d.text((64, 76), title, font=F(40, True), fill=INK)
    if sub:
        d.text((64, 132), sub, font=F(21), fill=MUTED)


def footer(d, text):
    d.line([(64, H - 74), (W - 64, H - 74)], fill=LINE, width=2)
    d.text((64, H - 58), text, font=F(18), fill=MUTED)


def multiline(d, xy, text, font, fill, spacing=6):
    x, y = xy
    text = text.replace("\\n", "\n")          # accept both escaped and real newlines
    for line in text.split("\n"):
        d.text((x, y), line, font=font, fill=fill)
        y += font.size + spacing


def bars(d, series, top, height, bar_w=None, gap=54, show_pct=False):
    """series: list of (label, value, colour, value_text)"""
    base_y = top + height
    n = len(series)
    total_gap = gap * (n + 1)
    bar_w = bar_w or (W - 128 - total_gap) // n
    vmax = max(v for _, v, _, _ in series)
    d.line([(64, base_y), (W - 64, base_y)], fill=LINE, width=2)
    for i, (label, v, col, vtext) in enumerate(series):
        x = 64 + gap * (i + 1) + bar_w * i
        h = max(6, int(v / vmax * height))
        d.rounded_rectangle([x, base_y - h, x + bar_w, base_y], radius=10, fill=col)
        d.text((x, base_y - h - 34), vtext, font=F(24, True), fill=INK)
        multiline(d, (x, base_y + 12), label, F(19), MUTED)


def stacked(d, rows, top, row_h=52, gap=16, left=300, right=980):
    """rows: (label, interest, principal) — proportional stacked bars with clear labels."""
    base = top
    span = right - left
    vmax = max(i + p for _, i, p in rows)
    for n, (label, interest, principal) in enumerate(rows):
        y = base + n * (row_h + gap)
        d.text((64, y + row_h // 2 - 13), label, font=F(21, True), fill=INK)
        w_int = int(interest / vmax * span)
        w_tot = int((interest + principal) / vmax * span)
        d.rounded_rectangle([left, y, left + w_tot, y + row_h], radius=9, fill=VIOLET)
        d.rounded_rectangle([left, y, left + w_int, y + row_h], radius=9, fill=PINK)
        d.text((left + w_tot + 18, y + row_h // 2 - 13),
               f"${interest:,.0f} interest", font=F(19, True), fill=MUTED)


def chart_interest_gap():
    im, d = new_canvas()
    header(d, "Saving", "What $10,000 earns in a year",
           "The account you choose matters more than the product inside it.")
    series = [
        ("Legacy branch\\naccount 0.01%", 1, VIOLET_L, "$1"),
        ("Typical easy-access\\n3.00%", 305, (167, 139, 250), "$305"),
        ("Competitive account\\n4.30%", 439, VIOLET, "$439"),
        ("12-month fixed\\nterm 4.60%", 470, (91, 33, 182), "$470"),
    ]
    bars(d, series, top=196, height=250, gap=30)
    footer(d, "Illustrative rates for comparison. APY/AER shown; actual rates vary by market and change over time.")
    im.save(OUT / "chart-interest-gap.jpg", "JPEG", quality=86, optimize=True, progressive=True)


def chart_amortisation():
    im, d = new_canvas()
    header(d, "Loans", "Where a $501 monthly payment goes",
           "$25,000 at 7.5% over 60 months, split between interest and the balance.")
    # legend
    d.rounded_rectangle([64, 176, 84, 194], radius=4, fill=PINK)
    d.text((94, 172), "Interest", font=F(19, True), fill=PINK)
    d.rounded_rectangle([196, 176, 216, 194], radius=4, fill=VIOLET)
    d.text((226, 172), "Balance repaid", font=F(19, True), fill=VIOLET)
    rows = [
        ("Month 1",  156, 345),
        ("Month 12", 135, 366),
        ("Month 24", 106, 395),
        ("Month 36",  72, 429),
        ("Month 60",   2, 499),
    ]
    stacked(d, rows, top=228, row_h=54, gap=18, left=250, right=880)
    footer(d, "Interest is calculated on the outstanding balance, so it falls as the loan is repaid.")
    im.save(OUT / "chart-amortisation.jpg", "JPEG", quality=86, optimize=True, progressive=True)


def chart_minimum_payments():
    im, d = new_canvas()
    header(d, "Credit & debt", "How long does a $1,000 balance take to clear?",
           "Same balance, same 22% APR — only the monthly payment changes.")
    series = [
        ("Minimum only", 73, PINK, "73 months"),
        ("Minimum +$25", 32, AMBER, "32 months"),
        ("Minimum +$50", 16, TEAL, "16 months"),
        ("Minimum +$100", 9, GREEN, "9 months"),
    ]
    bars(d, series, top=210, height=230, gap=28)
    footer(d, "Assumes 2% or $25 minimum (whichever is greater), no new spending, no fee changes.")
    im.save(OUT / "chart-minimum-payments.jpg", "JPEG", quality=86, optimize=True, progressive=True)


def chart_fund_timeline():
    im, d = new_canvas()
    header(d, "Saving", "Building a six-month emergency fund",
           "$3,200 of essential spending a month — the target is $19,200.")
    series = [
        ("1 month buffer\\n7 weeks", 3200, VIOLET_L, "$3,200"),
        ("3 months\\n33 weeks", 9600, (167, 139, 250), "$9,600"),
        ("6 months\\n64 weeks", 19200, VIOLET, "$19,200"),
    ]
    bars(d, series, top=206, height=240, gap=30)
    footer(d, "Milestones are cumulative. Weekly amounts are illustrative — the habit matters more than the size.")
    im.save(OUT / "chart-fund-timeline.jpg", "JPEG", quality=86, optimize=True, progressive=True)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    chart_interest_gap()
    chart_amortisation()
    chart_minimum_payments()
    chart_fund_timeline()
    for f in sorted(OUT.glob("chart-*.jpg")):
        print(f"  {f.name:34s} {f.stat().st_size/1024:6.1f} KB")


if __name__ == "__main__":
    main()
