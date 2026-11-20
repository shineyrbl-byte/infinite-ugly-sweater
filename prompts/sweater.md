# Sweater prompts (Nano Banana in Photoshop)

Use these in order. Each one is a single generation. Copy a prompt exactly first, then adjust.
Tips for every prompt:
- Say what to **keep** as well as what to change ("keep the knit texture and colours exactly the same").
- One change per generation. Nano Banana edits better in small steps than in one giant prompt.
- If a result is 80% right, fix the last 20% with a small selection and Generative Fill rather than regenerating everything.

---

## S1. Base sweater (Generate Image, square 1:1)
```
Flat-lay product photo of a hand-knitted ugly Christmas sweater on a plain warm-grey background, seen straight from the front, crew neck, sleeves spread out. Chunky wool with clearly visible V-shaped stockinette stitches. Colours only: cranberry red, pine green, cream, mustard yellow and charcoal. Gloriously tacky and over-decorated: a band of cross-eyed knitted reindeer across the chest (one facing the wrong way), lopsided knitted snowflakes, a knitted string of Christmas lights with tiny real LED bulbs sewn on, white pom-pom snowballs stuck on at random, gold tinsel fringe along the cuffs and hem. In the middle of the chest, leave a large plain cream square panel, empty, framed by a red knitted border. Soft even daylight, high detail, realistic yarn fuzz.
```
**Check:** the centre panel is empty and roughly square, and the stitch texture is visible everywhere. If the panel has something in it, select it and Generative Fill: `plain cream knitted panel, same stitch texture`.

## S2. The knitted portrait (Generative Fill on the centre panel, with reference image)
Make the reference first: `python3 tools/knit_chart.py me.jpg --stitches 48 --palette portrait` and use `me_knit.png` (or your plain photo, if your version of Photoshop allows two references, use both).
```
Knitted intarsia portrait of the person in the reference image, head and shoulders, smiling, wearing this exact same ugly Christmas sweater. Knitted into the panel with the same chunky yarn, the same V-shaped stitches and only the same five colours as the rest of the sweater. It should look like real knitting, slightly blocky, like a knitting chart, not a printed photo.
```
**Check:** it still looks like you (face shape, hair, glasses if you wear them). If the likeness is off, try again with your real photo as the reference instead of the knit chart.

## S3. Recursion (Photoshop, no generation)
See PLAYBOOK step 4: the sweater goes inside the portrait's chest, three levels deep, with nested Smart Objects.

## S4. Blend the smallest level (Generative Fill on the tiny innermost sweater)
```
Keep everything the same, but make this tiny area look knitted with the same chunky V-shaped stitches and yarn colours as the surrounding sweater, so it blends in seamlessly.
```

## S5. The dropped stitch (Generative Fill, lasso a patch near the lower left hem)
```
A hole in the knitted sweater where the stitches have unravelled, with a fluffy ginger cat's paw poking through and pulling a long loose strand of cranberry-red yarn out and off the edge. Keep the surrounding knit and lighting exactly the same.
```

## S6. 3D reindeer nose (Generative Fill, small ellipse on the middle reindeer's nose)
```
A glossy red felt pom-pom nose sewn onto the knitted reindeer, sticking out in 3D and casting a small soft shadow on the wool.
```

## S7. Hem text (Generative Fill on the hem band, optional)
```
Knitted into the hem band in cream yarn on red, in blocky knitted capital letters: I AM THE SWEATER
```
If the letters come out garbled after two tries, type the words in Photoshop instead (a chunky font, then Filter > Distort > Ripple, small) and let Nano Banana knit-ify it with S4's prompt.

---

### Spare prompts if you have generations left
- **More ugliness:** `Add a small knitted Santa stuck in the chimney with only his legs showing, on the left sleeve, same yarn and stitches.`
- **Lights glow:** `Make the tiny LED bulbs on the knitted string glow softly in red, green and yellow, with a faint glow on the wool around them.`
- **Fuzz:** `Add a little stray wool fuzz and a few pilled bobbles across the sweater so it looks well-loved. Keep the design exactly the same.`
