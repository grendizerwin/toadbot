# Official $TOAD Visual Bible

Source of truth: `$TOAD_KIT/kit/BRAND.md` (§9 character, §10 guidelines, §11 Paper Pulse board, §12 do's/don'ts) and the "Character lock" in `$TOAD_KIT/kit/prompt-kit.md`. If anything here disagrees with BRAND.md, BRAND.md wins.

## What Toad is

A **real photographed full-body plush mascot suit**. Not a cartoon, not felt, not a small toy, not Pepe.

- **Fur:** yellow-green lime short-pile fuzzy plush (close to #B5DB3A, olive shading), visible nap. Same plush on arms, hands, legs, feet.
- **Head:** wide, rounded, squashed frog head, wider than tall, about 1/3 of body height. Rigid costume piece. No neck, no warts.
- **Eyes:** two large **glossy white domed eyes**, big black pupils with a small white catchlight, **heavy sleepy plush upper lids cover the top third of each eye** (never wide-open round eyes). Glancing slightly sideways. Smug, knowing, deadpan. Slightly asymmetric.
- **Mouth:** one long **thin crooked black stitched smile**. Closed. No teeth, no tongue, no nose, no ears.
- **Outfit:** bright **red short-sleeve tee**; **mustard knee-length overall shorts** with **yellow straps**; round **white buttons stitched with a red x**. From behind the straps cross in an X; a small cream "toad" tag sits on the back of the shorts.
- **Hands/feet:** chunky **four-finger** plush hands; big flat plush frog feet.
- **Scale:** adult-human proportions (a person in a suit), not tabletop-toy size unless the joke is scale.
- **Face never changes.** Emotion comes from body pose, props, and setting. The joke is the situation around him.

## Never generate

- Pepe the Frog / Matt Furie style, any 2D or flat cartoon, children's-book toad
- Felt puppet look, small stuffed toy, Muppet with an open mouth
- El Reino Infantil / La Granja de Zenón 3D frog (orange irises, purple "PP" shirt)
- Generic crypto frog (cigar, laser eyes), biological toad, sombrero "El Toad" knockoff
- Open mouth, teeth, tongue, changing expression, oval cartoon eyes, missing overalls or straps, wrong colors, extra fingers, garbled text

## Reference files (verified on disk; attach to EVERY image or video generation)

Character (`$TOAD_KIT/kit/assets/characters/`):
- `toad-front-reference-fullbody.jpg` — front full body, green backdrop (default identity lock)
- `toad-face-reference-circle.jpg` — face and eyes lock
- `toad-rear-reference-fullbody.jpg` — back, crossed straps, two buttons
- `toad-pose-reference-sheet-4-poses.jpg` — waving, arms crossed, holding coin, cheering
- `hero-cutout-toad-bust-transparent.png` — transparent bust, best for compositing
- `toad-portrait-bust-green-bg.png` — head and shoulders on green
- `toad-off-duty-sitting-on-stool.png` — seated on a wooden stool
- `toad-back-view-name-tag-wide-banner.jpg` — rear view with "toad" tag

Creator kit duplicates (`$TOAD_KIT/kit/assets/creator-kit/`): `toad-front-reference.jpg`, `toad-face-reference.jpg`, `toad-rear-reference.jpg`, `toad-pose-reference.jpg`, `toad-video-prompt.txt`, `toad-creator-guidelines.txt`.

Layout: `$TOAD_KIT/kit/assets/paper-pulse-reference.png`, `assets/social/toad-social-og-image-having-a-day.png`, `assets/backgrounds/paper-grain-noise-texture.svg`.
Community scene examples (style only, not identity): browse Meme Depot (https://memedepot.com/d/the-toad-pepe); those images are not redistributed in this kit.
Video: `$TOAD_KIT/kit/assets/video/toad-one-more-meeting-video-prompt.txt`, `toad-one-more-meeting.mp4`.

The old `assets/official-*.jpg` files do not exist. Do not cite them.

Minimum attach set: front + face. Add rear for back shots, pose sheet for poses, stool for seated scenes. Add the source image when remixing someone's post.

## Image workflow

1. Pick the scene first (see `viral-hooks.md`): one everyday situation, one prop that carries the joke.
2. Call `xai_image.py` with `--ref` = the attach set above (absolute paths) and a prompt that starts with the Character lock from prompt-kit.md, then:
   > Only change: [scene / pose / prop]. Photoreal photograph of the real plush suit in a real place, natural light, sharp fabric detail. Face exactly as reference: half-lidded glossy white domed eyes, thin crooked stitched smile, closed mouth. No text, no logos, no watermark. Leave clean space at the [top/bottom] for a caption.
3. Run the **Face check** in `prompt-kit.md`: Read the result next to `$TOAD_KIT/kit/assets/characters/toad-face-reference-circle.jpg` (lids over the top third of the eyes, head wider than tall, thin crooked closed smile, red-x buttons), plus red tee, mustard overalls, yellow straps, four fingers, plush not felt. Max 2 generations: if the first drifts, rerun once with the face reference first and "restore the exact face and outfit from the reference." If that fails too, stop generating and fall back to the official cutout composited with Pillow, or a Paper Pulse card.
4. Never burn generated text into the image. Render text-free, then caption afterward (below).

## Captions on images (Paper Pulse)

Use Pillow (installed; ImageMagick is not). Pillow loads the brand fonts directly from `$TOAD_KIT/kit/assets/fonts/`:
- Display: `anton-latin-400-normal-Byf51wtH.woff2`
- Body: `dm-sans-latin-wght-normal-Xz1IZZA0.woff2`
- Labels: `ibm-plex-mono-latin-400-normal-DMJ8VG8y.woff2`
- Handwritten: `caveat-latin-700-normal-D8_1Nw6V.woff2`

Script: `python3 $TOAD_KIT/bin/compose.py <photo> <out.jpg> "<HEADLINE>" "<caveat note>" "<LEFT LABEL>" "<RIGHT LABEL>"` (from batch 001, now loading the brand fonts above directly). Output: cream paper with grain, Plex Mono labels, Anton headline with a tilted yellow brush underline, photo in an 8px rounded forest frame, Caveat note with a small red heart, "SAME TOAD. DIFFERENT DAYS." footer.

Rules: cream #F9F1D7 canvas, forest #144137 text, yellow #F6BE2D brush marks, red #E02B2F only as a tiny accent, green #35D391 / lime #B5DB3A backdrops. One headline. Short caption in safe areas, lots of breathing room. Forest text on cream, yellow, lime, or green only.

## Video

- 9:16 vertical, under 15s, soft light, simple backgrounds, gentle cuts. Model it on `toad-one-more-meeting-video-prompt.txt`.
- GenerateVideo with `reference_image_paths` = front + face (+ rear if he turns away). Cite them as <IMAGE_0>, <IMAGE_1>.
- The head is one rigid piece: eyes and mouth never move. Only shoulders and arms breathe; the body does the acting. End on the fixed crooked smile.
- No text in the generation. Captions are added in edit. Audio only if you have the rights.

## Scenes that fit (everyday moments)

Sofa at night with the remote, desk at 8:59 on a monday, coffee in both hands, the "one quick thing" laptop, alarm on the nightstand, laundry chair, grocery queue, rainy bus stop, pond dock at golden hour, saturday blanket fort, group-chat phone glow. One situation per image. Toad stays calm while the situation does the work.
