# Devpost submission: Deck the Pixels 2026

Written in first person. **Edit anything that doesn't match what you actually did.** The answers must describe your real process, so update the numbers of generations, any prompts you changed, and the tools you used.

## Project name
The Infinite Ugly Sweater

## Tagline
An ugly sweater with me on it, wearing the ugly sweater, wearing the ugly sweater, forever. And a card where the whole room is knitted.

## Images to upload
1. `sweater.png`: the sweater design
2. `card.png`: the finished holiday card
3. `layers.png`: Photoshop with the Layers panel visible

## How I used Nano Banana and Photoshop: the sweater

```
I wanted an ugly sweater that's ugly in every direction at once, and that contains itself.

Nano Banana:
- I generated the base sweater as a flat-lay photo with a strict five-colour yarn palette, every cliché I could think of (cross-eyed reindeer, one facing the wrong way, lopsided snowflakes, sewn-on LED lights, pom-poms, tinsel fringe), and an empty panel in the middle.
- I filled the panel with Generative Fill using a reference image of myself. To make it look like real knitting rather than a photo with a wool filter, I first turned my photo into a knitting chart (a grid of V-shaped stitches in the sweater's own colours) with a small script I wrote, and used that as the reference. Nano Banana kept my likeness while matching the stitches.
- I used small, targeted Generative Fill edits for the details: a dropped stitch where a ginger cat is unravelling the sweater, a glossy 3D felt nose on one reindeer, and "I AM THE SWEATER" knitted into the hem.

Photoshop:
- The recursion is built from nested Smart Objects: the sweater is placed inside the knitted portrait's chest, three levels deep, each masked to the panel and slightly rotated so it looks hand-placed. Then I used Nano Banana to re-knit the tiniest level so it blends into the stitches.
- Clipped Curves and Hue/Saturation layers keep every level and every AI edit on the same palette. A final Curves and vignette tie it together.
```

## How I used Nano Banana and Photoshop: the holiday card

```
The card continues the joke: I'm standing in a living room where everything is knitted, and the photo on the mantel is the card itself.

Nano Banana:
- I generated the room with everything knitted from the same yarn colours: the tree, the presents, the fireplace and its flames, the armchair, the cat and the snow outside the window. I fixed anything that looked plastic with Generative Fill.
- I placed my own photo, then used Generative Fill with my finished sweater as the reference image to dress me in it, portrait panel and all. A second pass matched the lamp light and added a contact shadow on the knitted rug.
- The ginger cat from the sweater's dropped stitch is back, now holding the yarn that leads to my hem.
- The knitted bunting reading "WISHING YOU AN INFINITELY COZY HOLIDAY" was generated with Nano Banana's text rendering.

Photoshop:
- Select Subject and layer masks to cut myself out and blend me in, plus Match Colour and clipped Curves to match the room's warmth.
- The card inside the card: I placed the finished card as a Smart Object in the mantel frame and used Perspective and Distort to fit the frame's angle, with a darker Curves and a soft glare gradient on top.
- A final Color Lookup and Curves pass, with colours eyedropped from the sweater so the two images read as one piece.
```

## Anything else (optional)
```
Everything visible in both images was made in Photoshop with Nano Banana, plus my own photo. The only outside step was a small open-source script I wrote to turn my photo into a knitting-chart image, which I used purely as a reference image for Nano Banana: https://github.com/shineyrbl-byte/infinite-ugly-sweater
```
