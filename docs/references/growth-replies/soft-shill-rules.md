# Soft-shill rules for $TOAD replies

Soft-shill means a stranger should not feel sold. The comment should still work as a comment if the ticker vanished.

## Allowed

- Name $TOAD once when the parent is already about the token or the exact character
- Point at a live official photo, clip, game, or site beat without pasting the CA
- Correct a mix-up (Pepe the Frog vs the real plush suit, El Reino 3D frog vs official) in one dry line, kindly
- Attach one edited official-plush image when the parent is visual and the face *is* the joke
- Ask a short question that makes the character or product obvious

## Banned

- Contract address, unless the user explicitly asked for it in this run
- "check my bags", "small cap gem", "don't fade", "still early in the pond"
- Burned lore lines from `toad-x-post-generator/references/uniqueness.md`
- Raid language, emoji walls, identical copy under multiple posts
- Asking the author to follow the owner, @thetoadmeme_, or @thetoadmcme__
- Fake catalysts, price targets, "partnership incoming", invented Dudas quotes
- Claiming Matt Furie copied El Sapo or that the token owns the IP
- Turning an unrelated runner into TOAD
- $TOAD in coin-hunting threads ("what sub $5M coin", "looking for the next one"); reply without the ticker or skip
- More than one image reply in a pack
- More than one personal-bag mention in a pack
- Price predictions, "pump", moon, targets, financial advice, promises
- Anything that sounds like an official announcement; you are a pond member, not the project
- Mean replies, dunks on other coins, their holders, or people
- Replying to trolls, scam posts, or copycat / impostor contracts (note them in the skip list, never engage)
- Bulk tagging (more than one @ in a reply), and duplicate or near-duplicate reply text anywhere in the pack or the last 48h

## Ticker density

- Already-TOAD thread: ticker optional. Official QT already carries it.
- Adjacent thread: ticker only if the sentence dies without it.
- Not adjacent: no ticker. Hand off or skip.

## Image replies

Follow `$TOAD_KIT/docs/references/post-generator/visual-bible.md`. Always attach the character references to the generation (the box image script (`xai_image.py`) `reference_image_paths`), minimum:

- `$TOAD_KIT/kit/assets/characters/toad-front-reference-fullbody.jpg`
- `$TOAD_KIT/kit/assets/characters/toad-face-reference-circle.jpg`
- plus `toad-pose-reference-sheet-4-poses.jpg`, `toad-off-duty-sitting-on-stool.png`, or `toad-rear-reference-fullbody.jpg` from the same folder when the pose needs it
- or an official still found with `from:thetoadmeme_ has:images` (request `media.fields=type,url,preview_image_url`, curl it to the box, Read it), in addition to (not instead of) the files above

Lock: real photographed plush suit (not felt, not cartoon), lime fuzzy fur, wide squashed head, glossy white domed half-lidded eyes, thin crooked stitched smile, red tee, mustard overalls, yellow straps, red-x white buttons. Face never changes. Run the Face check in `$TOAD_KIT/kit/prompt-kit.md`. Max 2 generations; if both fail, use the official cutout composited with Pillow, or drop the image. No generated text in the image; caption afterward if needed.

Caption stays 1–2 lines. The picture does the shill. The text does not narrate the thesis.

## Reply shapes (situation first)

React to the parent's actual moment, then let Toad live in it. Patterns and the approved batch 001 posts are in `toad-x-post-generator/references/viral-hooks.md`.

- **Same-moment echo.** Mirror their situation with one concrete detail.
  Good (under a cozy saturday post): `zero plans, one blanket, maybe a snack. peak saturday 🐸`
  Bad: `once you see toad you can't unsee toad. it's a lifestyle now 🐸` (fits any thread, any coin)
- **Tomorrow-problem handoff.** Their chore becomes a tomorrow problem.
  Good (under "inbox at 400"): `that's a tomorrow problem with extra steps`
  Bad: `toad would never stress about this, $TOAD 🐸🚀` (bolted-on ticker, emoji stack)
- **Detail poke.** One thing in their image the caption missed.
  Good (under official parkour clip): `the straps held up better than my friday plans`
  Weaker: `toad doing parkour on a friday night while i was asleep by 10. respect 🐸` (fine, but narrates the clip back; cut to the turn)
- **Warm answer.** Someone asks what TOAD is.
  Good: `a plush toad having the same week as you. the pond's friendly 🐸`
  Bad: `the original pepe since 1988, check the CA` (burned lore, CA)

## Sound

Same house voice as sibling `reply-voice.md`. After avoid-ai-writing, re-loosen. Swap-test includes the ticker: if the line works for $WIF or $PEPE, it is not a TOAD reply.
