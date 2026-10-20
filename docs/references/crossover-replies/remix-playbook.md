# Remix playbook

The comment wins when a stranger sees *their* post back, with the official toad inside it.

## Always

1. Curl the parent media to the box (`url` for photos, `preview_image_url` for a video frame) and Read it. Video itself can't be watched; say so
2. Call `xai_image.py` with `--ref` = the parent image **plus** the character references (always both):
   - `$TOAD_KIT/kit/assets/characters/toad-front-reference-fullbody.jpg`
   - `$TOAD_KIT/kit/assets/characters/toad-face-reference-circle.jpg`
   - add `toad-pose-reference-sheet-4-poses.jpg`, `toad-off-duty-sitting-on-stool.png`, `toad-rear-reference-fullbody.jpg`, or `hero-cutout-toad-bust-transparent.png` (same folder) when the pose or a cutout helps
   - an official still from `from:thetoadmeme_ has:images` can be added, never as the only reference
3. Prompt = Character lock from `$TOAD_KIT/kit/prompt-kit.md` + the edit pattern below
4. Run the Face check in `$TOAD_KIT/kit/prompt-kit.md` (Read the result next to `$TOAD_KIT/kit/assets/characters/toad-face-reference-circle.jpg`), then check the lock: real photographed plush suit (not felt, not cartoon), lime fuzzy fur, wide squashed head, glossy white domed half-lidded eyes, thin crooked stitched smile, red tee, mustard overalls, yellow straps, red-x white buttons, four-finger hands. Face never changes; the situation is the joke
5. Show the result in the same answer

## Joke classes that match the tests

Pick one class per target. Do not repeat a class already used by the owner in 48h.

- **Swap comparison** — parent is old vs new / leaked vs current. Old object on OLD, official plush on NEW. Don't mock another coin's mascot or its holders; if Pepe appears on OLD it must read as a gentle chronology joke, not a dunk
- **Drop-in scene** — parent is a real place (aisle, field, stadium, kitchen). Stand the plush in the same room, same camera angle
- **Graphic occupancy** — parent is a map, chart-that-is-not-crypto, poster, or labeled graphic. Sit the plush on the graphic and keep their labels
- **Object replacement** — parent hero object becomes the plush, rest of layout stays
- **Everyday stand-in** — parent is a relatable moment (queue, desk, rainy commute, couch, monday traffic). Toad is the calm one living it, same camera angle

## Edit prompt pattern

[CHARACTER LOCK]. Use the first attached image as the scene: keep its layout, background, props, lighting, and any text exactly. Insert the plush Toad from the character references: same glossy white domed half-lidded eyes, same thin crooked stitched smile with closed mouth, same lime fuzzy plush, red tee, mustard overalls, yellow straps, red-x white buttons. Only change: [insert Toad at X / replace object Y]. Photoreal plush suit in their scene, matching their light. No new text, no ticker, no CA, no logos, no watermark. Not Pepe, not a cartoon, not felt.

If the parent has text you need to keep and the generator garbles it, generate without text and restore it afterward with Pillow (fonts and recipe in `toad-x-post-generator/references/visual-bible.md`).

## Rights

- Never keep a third party's logo or brand mark in a way that implies endorsement or partnership. If the logo is the joke, keep it small and as-is in their layout; never add one.
- Never remix photos of private individuals (non-public people, bystanders, someone's kid or family). Public figures in a newsworthy context only, and never demeaning.
- Skip authors who've asked not to be edited or remixed (check bio and recent posts).

## Fail the image if

- Face drifted to Pepe, orange-eyed 3D kids-TV frog, felt puppet, oval cartoon eyes, open mouth, or a biological toad
- Layout no longer reads as *their* post
- Burned-in `$TOAD`, CA, or "buy now"
- Extra watermarks, extra logos claiming brand partnership, or anything that looks like an official announcement
- The joke needs a paragraph of caption to land

Max 2 generations: one identity-lock retry, then composite the official cutout (`hero-cutout-toad-bust-transparent.png`) or the front reference into their photo with Pillow, or drop. Do not ship a wrong face.

## Caption

- Empty is valid
- Else 1–8 words that only work on that picture, lowercase, warm, never mean
- No hashtags unless the parent already made the hashtag the joke (weather frog style) and it is not a ticker tag

Good / bad:
- Grocery-aisle photo → good: `unc toad on a tuesday` · bad: `$TOAD to the moon 🐸🚀`
- Rainy weather map → good: `tomorrow problem confirmed` · bad: `toad says buy the dip`
- Phone-leak "old vs new" → good: `get a new model` · bad: `pepe is dead, toad is king` (dunk)
- Monday traffic photo → good: `monday again?` · bad: `join the pond at thetoadmeme.com` (pitch)
