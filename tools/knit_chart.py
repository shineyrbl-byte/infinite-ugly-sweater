#!/usr/bin/env python3
"""
knit_chart.py: turn a photo into a knitted-intarsia image (and a printable knitting chart).

Use the knitted image as a *reference image* for Nano Banana in Photoshop, so the portrait
on the sweater looks like real knitting: a grid of V-shaped stitches in a few yarn colours,
not a smooth photo with a "wool" filter.

    python3 tools/knit_chart.py me.jpg                 # writes me_knit.png and me_chart.png
    python3 tools/knit_chart.py me.jpg --stitches 60 --palette sweater

Each stitch is drawn as two slanted loops (the "V" of stockinette knitting) with simple
shading, so it reads as yarn even at small sizes.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageOps

PALETTES = {
    # The sweater's own yarn colours (see docs/CONCEPT.md)
    "sweater": ["#B3202B", "#1F5B3A", "#F3E9D2", "#E0A526", "#2B2A2E", "#E7B8A1"],
    # A softer palette for faces: cream, two skin tones, hair, red
    "portrait": ["#F3E9D2", "#E7B8A1", "#B9785A", "#5A3A2E", "#2B2A2E", "#B3202B"],
}

STITCH_W = 20  # pixels per stitch in the output image
STITCH_H = 16  # stitches are wider than tall, like real knitting


def hex_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]


def shade(rgb: tuple[int, int, int], f: float) -> tuple[int, int, int]:
    return tuple(max(0, min(255, int(c * f))) for c in rgb)  # type: ignore[return-value]


def quantize(img: Image.Image, stitches: int, palette: list[str]) -> Image.Image:
    """Resize to the stitch grid and map every pixel to the nearest yarn colour."""
    w, h = img.size
    rows = max(1, round(stitches * (h / w) * (STITCH_W / STITCH_H)))
    small = ImageOps.autocontrast(img.convert("RGB")).resize((stitches, rows), Image.Resampling.LANCZOS)
    pal_img = Image.new("P", (1, 1))
    flat = [c for hx in palette for c in hex_rgb(hx)]
    pal_img.putpalette(flat + flat[-3:] * (256 - len(palette)))
    return small.quantize(palette=pal_img, dither=Image.Dither.NONE).convert("RGB")


def draw_knit(grid: Image.Image) -> Image.Image:
    """Render each grid cell as a knitted V stitch."""
    cols, rows = grid.size
    out = Image.new("RGB", (cols * STITCH_W, rows * STITCH_H), (40, 36, 40))
    d = ImageDraw.Draw(out)
    px = grid.load()
    half = STITCH_W // 2
    for y in range(rows):
        for x in range(cols):
            c = px[x, y]
            x0, y0 = x * STITCH_W, y * STITCH_H
            dark, light = shade(c, 0.62), shade(c, 1.18)
            # left loop leans right, right loop leans left: together they make a V
            left = [(x0 + 1, y0 - 2), (x0 + half, y0 + STITCH_H * 0.55), (x0 + half, y0 + STITCH_H + 3), (x0 + 1, y0 + STITCH_H * 0.45)]
            right = [(x0 + STITCH_W - 1, y0 - 2), (x0 + half, y0 + STITCH_H * 0.55), (x0 + half, y0 + STITCH_H + 3), (x0 + STITCH_W - 1, y0 + STITCH_H * 0.45)]
            d.polygon(left, fill=c, outline=dark)
            d.polygon(right, fill=shade(c, 0.9), outline=dark)
            # a highlight along each loop sells the yarn
            d.line([(x0 + 3, y0 + 1), (x0 + half - 1, y0 + STITCH_H * 0.6)], fill=light, width=2)
            d.line([(x0 + STITCH_W - 3, y0 + 1), (x0 + half + 1, y0 + STITCH_H * 0.6)], fill=shade(c, 1.08), width=2)
    # a touch of blur so it reads as fuzzy wool rather than vector art
    return out.filter(ImageFilter.GaussianBlur(0.6))


def draw_chart(grid: Image.Image, palette: list[str]) -> Image.Image:
    """A classic knitting chart: one square per stitch with a grid every 10 stitches."""
    cols, rows = grid.size
    cell = 14
    pad = 30
    out = Image.new("RGB", (cols * cell + pad * 2, rows * cell + pad * 2), "white")
    d = ImageDraw.Draw(out)
    px = grid.load()
    for y in range(rows):
        for x in range(cols):
            x0, y0 = pad + x * cell, pad + y * cell
            d.rectangle([x0, y0, x0 + cell, y0 + cell], fill=px[x, y], outline=(200, 200, 200))
    for x in range(0, cols + 1, 10):
        d.line([(pad + x * cell, pad), (pad + x * cell, pad + rows * cell)], fill=(60, 60, 60), width=2)
    for y in range(0, rows + 1, 10):
        d.line([(pad, pad + y * cell), (pad + cols * cell, pad + y * cell)], fill=(60, 60, 60), width=2)
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Turn a photo into a knitted intarsia image and knitting chart.")
    ap.add_argument("image", type=Path)
    ap.add_argument("--stitches", type=int, default=48, help="stitches across (default 48)")
    ap.add_argument("--palette", choices=sorted(PALETTES), default="portrait")
    ap.add_argument("--out", type=Path, default=None, help="output folder (default: next to the image)")
    args = ap.parse_args(argv)

    if not args.image.exists():
        print(f"No such file: {args.image}", file=sys.stderr)
        return 1
    palette = PALETTES[args.palette]
    grid = quantize(Image.open(args.image), max(8, min(200, args.stitches)), palette)
    out_dir = args.out or args.image.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    knit_path = out_dir / f"{args.image.stem}_knit.png"
    chart_path = out_dir / f"{args.image.stem}_chart.png"
    draw_knit(grid).save(knit_path)
    draw_chart(grid, palette).save(chart_path)
    print(f"{knit_path}  ({grid.size[0]}×{grid.size[1]} stitches)\n{chart_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
