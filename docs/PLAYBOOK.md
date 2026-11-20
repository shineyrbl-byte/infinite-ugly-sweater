# Playbook: making The Infinite Ugly Sweater in Photoshop + Nano Banana

Total generations needed: about **14 (plus a few retries)**. The free Photoshop web version allows **5 generations a day**, so plan for 4 days. With the 7-day trial you can do it in one sitting.
Prompts live in [`prompts/sweater.md`](../prompts/sweater.md) and [`prompts/card.md`](../prompts/card.md).

> Nano Banana is picked from the model menu in Photoshop's generative tools (Generate Image and Generative Fill). Where a step says "with a reference image", use the reference-image option in that panel. If your version names things differently, follow the Nano Banana resources linked on the challenge page.

## Day 1: the sweater (5 generations)

**1. Set up the file.** New document, 3000 × 3000 px, 300 ppi, RGB. Add the six palette colours (`docs/CONCEPT.md`) as swatches.

**2. Base sweater: prompt S1** (Generate Image). If it isn't right, use your second generation on S1 again rather than fixing a bad base. Rename the layer `Sweater base`.

**3. Portrait panel: prompt S2** (Generative Fill on the centre panel, with your knit reference).
Make the reference before you start:
```bash
python3 tools/knit_chart.py me.jpg --stitches 48 --palette portrait
```
Rename the result `Portrait (knitted me)`.

**4. Recursion, the signature move (no generations).**
1. Select all, **Edit > Copy Merged**, paste. Convert to a Smart Object and name it `Recursion 1`.
2. Scale it down (about 22–28%) and position it over the *chest panel of the knitted portrait*. Free Transform with a tiny rotation (1–2°) to make it look hand-placed.
3. Add a layer mask and paint away everything except the sweater's chest panel area, so only the "sweater on knitted-me" shows.
4. Double-click `Recursion 1` to open it and repeat inside it, creating `Recursion 2`. Do it once more for `Recursion 3`. Each level is now a nested Smart Object. **This is what the judges will love in the Layers screenshot.**
5. Add a **Hue/Saturation** or **Curves** adjustment clipped to each level, so the colours match exactly.

**5. Blend the smallest level: prompt S4** (Generative Fill on the innermost level).

## Day 2: ugliness details (4–5 generations)

**6. Dropped stitch: prompt S5.** Lasso a patch near the lower-left hem. Rename it `Dropped stitch (cat)`.
**7. 3D nose: prompt S6.** Then **hem text: prompt S7** (or type it and knit-ify it).
Optional spare prompts if you still have generations: lights glow, Santa on the sleeve.

**Finish the sweater.**
- A **Curves** adjustment at the top of the stack for overall contrast, and a subtle **Vignette** (Camera Raw Filter > Effects).
- Export: **File > Export > Export As > PNG**, `sweater.png`.
- **Save the layered PSD** (or cloud document). You need it for the Layers screenshot and for step 10.

## Day 3: the card (5 generations)

**8. New file**, 3500 × 2500 px (landscape). **Knitted living room: prompt C1.** Rename it `Knitted room`.

**9. Put yourself in.** Place your photo, Select Subject, mask. Then **prompt C2a** (sweater as the reference image) and **C2b** (light and shadow blending).
- Use **Match Colour** or a clipped **Color Balance** / **Curves** on your layer if the warmth doesn't match.

**10. The cat has the yarn: prompt C3.** Draw a soft **Pen tool** path for the yarn from the cat's mouth to your hem if the generation doesn't connect them.

## Day 4: the recursion and the banner (2–4 generations)

**11. The card inside the card (no generations).**
1. Copy Merged, paste as a Smart Object, name it `Card inside card`.
2. Scale it to fit the mantel frame and use **Edit > Transform > Perspective/Distort** to match the frame's angle.
3. Clip a **Curves** (slightly darker) and a soft **Gradient** (lamp glare) to it.
4. Optional: repeat once inside it for a second level.

**12. Banner: prompt C5** (or type it and use C6). **Signature:** C7 type layer.

**13. Final polish.**
- Top-of-stack **Curves** and **Color Lookup** (a warm film LUT at about 30%).
- Make sure the yarn colours in the card match the sweater: pick colours with the eyedropper from `sweater.png`.
- Export `card.png`.

## The Layers screenshot (required)
Organise both files into named groups before taking the screenshot. Judges read this panel.

**Sweater**
```
▾ 🎨 Finish
    Curves – contrast
    Vignette
▾ 🧶 Ugly details
    Hem text "I AM THE SWEATER" (Nano Banana)
    3D reindeer nose (Nano Banana)
    Dropped stitch – cat (Nano Banana)
▾ ♾️ Recursion
    Recursion 1  ▸ (Smart Object → Recursion 2 → Recursion 3)
    Blend innermost level (Nano Banana)
▾ 🙂 Portrait
    Portrait – knitted me (Nano Banana + reference)
▾ 🧥 Base
    Sweater base (Nano Banana)
```

**Card**
```
▾ 🎨 Finish   (Curves, Color Lookup)
▾ ✍️ Text     (Banner – Nano Banana, Signature – type)
▾ ♾️ Card inside card (Smart Object, perspective)
▾ 🐈 Cat with yarn (Nano Banana) + yarn path
▾ 🙂 Me       (photo + mask, sweater – Nano Banana + reference, light & shadow – Nano Banana, colour match)
▾ 🏠 Knitted room (Nano Banana)
```
Take the screenshot with the canvas and the expanded Layers panel both visible: Windows: Win+Shift+S, Mac: Cmd+Shift+4.

## If something goes wrong
| Problem | Fix |
|---|---|
| The face doesn't look like you | Use your real photo (not the knit chart) as the reference, and add "keep the same face shape, eyes and hairstyle" |
| The knit looks like a filter, not yarn | Add "visible V-shaped stockinette stitches, chunky wool, real knitting" and use the knit chart reference |
| Text is garbled | Type it in Photoshop, then knit-ify it with S4 or C6 |
| Colours drift between generations | Clip a Hue/Saturation or Curves adjustment, or pick colours from the palette swatches |
| You're out of generations | Do the no-generation steps (recursion, masks, adjustments, text) and continue tomorrow |
