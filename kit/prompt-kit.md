# TOAD Prompt Kit

Everything here comes from `BRAND.md` (sections are cited as §n). Attach reference images from `assets/characters/` whenever the generator accepts them. The kit says: "Attach the references to your AI tool."

## Character lock (paste into every prompt)

> TOAD, a real photographed full-body plush frog mascot costume (not a cartoon): yellow-green lime short-pile fuzzy plush fur; wide rounded squashed frog head, clearly wider than it is tall, about one-third of body height; two large glossy white domed eyes with big black pupils and small white catchlights, the heavy sleepy plush upper lids covering the top third of each eye (never wide-open round eyes), glancing slightly sideways with a smug knowing look; one long thin crooked black stitched smile, closed mouth, no teeth, no nose; bright red short-sleeve t-shirt; mustard-yellow knee-length overall shorts with yellow suspender straps fastened by clearly visible round white buttons with red x-stitches (straps cross in an X on the back); chunky four-finger plush hands; big flat plush frog feet. The head is a rigid costume piece and the face never changes expression.

Grounding: §9 and the creator kit line "Keep the green plush texture, oversized expressive eyes, crooked smile, red shirt, and yellow overalls with suspenders. Preserve proportions across shots."
Best references: `toad-front-reference-fullbody.jpg`, `toad-face-reference-circle.jpg`, `toad-rear-reference-fullbody.jpg`, `toad-pose-reference-sheet-4-poses.jpg`, `hero-cutout-toad-bust-transparent.png`.

Negative / avoid: cartoon, 2D illustration, Pepe drawing, open mouth, teeth, tongue, moving or changing facial expression, different outfit colors, missing suspenders, blue or dark-green skin, extra fingers, text artifacts, wide-open round eyes with no lids, tall or egg-shaped head, plain buttons without the red x.

## Face check (required before any generated image is used)

Read the result next to `assets/characters/toad-face-reference-circle.jpg`. It passes only if: the upper lids cover about the top third of both eyes, the head is wider than tall, the smile is one thin crooked stitched line with a closed mouth, and the white buttons show a red x (when the bib is in frame). Note the verdict in the draft notes.

Max 2 generations per image: the first try, then one retry with the face reference first and "restore the exact face and outfit from the reference." If both fail, stop generating: composite the official cutout (`assets/characters/hero-cutout-toad-bust-transparent.png`, or the front reference cut off its backdrop) into the scene with Pillow, or make a Paper Pulse card with the official photo. Never ship a failed face.

## Templates

### 1. Official-style studio reference / PFP
> [CHARACTER LOCK]. Clean studio photograph, Toad [POSE: waving | arms crossed | holding a gold smiley coin | cheering with both arms up | sitting on a small wooden stool], centered with lots of breathing room, flat solid [toad green #35D391 | lime #B5DB3A | cream #F9F1D7] background, soft even lighting, soft floor shadow, sharp plush fabric detail, photoreal, [1:1 for PFP | 4:5].

Grounding: the official references use flat green or cream studio backdrops (§9). The four poses come from the pose sheet. "Lime #B5DB3A — Character backdrops" (§6). "Give the character breathing room" (§10).

### 2. "Having a day" everyday-chaos meme (photoreal scene)
> [CHARACTER LOCK]. Photoreal scene: Toad [EVERYDAY SITUATION, e.g. at a desk buried in meeting invites on a Monday | holding coffee while the laptop shows a full calendar | standing calmly while everything around him goes wrong]. The face stays deadpan and content while the situation is chaotic. Cinematic natural lighting, shallow depth of field, [16:9 or 1:1]. Leave clean empty space at the [top/bottom] for a caption added later.

Caption ideas (add as separate text): "Toad is having a day." / "Monday again?" / "This feels like a tomorrow problem." / "Currently doing his best." / "Same Toad. Different days."
Grounding: "Everyday moments work best." "Let the situation change; keep Toad recognizable." The Meme Depot examples are photoreal plush-in-scene images (selfie in a burning city, empty pool, astronaut) (§3, §13). "Add captions separately when the generator cannot render clean text."

### 3. Paper Pulse editorial poster / X header
> Editorial graphic-design poster on warm cream paper (#F9F1D7) with subtle paper grain. Huge condensed uppercase headline in a bold Anton-style typeface, deep forest green (#144137), tight leading: "[HEADLINE, e.g. TOAD IS HAVING A DAY.]", with a slightly tilted, uneven mustard-yellow (#F6BE2D) brush-stroke underline. A smaller bold sans subline: "[e.g. A little chaos. A lot of heart.]". On the right, a large photoreal cut-out of [CHARACTER LOCK, head and shoulders] with a small hand-drawn speech bubble "[e.g. Monday again?]" in a handwritten Caveat-style script. Thin forest hairline rules, a small monospace uppercase label "$TOAD / SOLANA / HAVING A DAY", generous negative space. [16:9 | 3:1 header | 4:5]

Grounding: §11 (brand board) and the OG image, plus "Cream is the canvas. Forest carries the words. The character supplies the color." and "Subtle paper grain, yellow brush marks, and handwritten notes." Exact text is best composited afterwards with the real fonts in `assets/fonts/`.

### 4. Back-view / "same Toad" shot
> [CHARACTER LOCK]. Rear view: Toad seen from behind, yellow suspenders crossing in an X over the red t-shirt, two white red-stitched buttons at the waistband, a small cream tag reading "toad" on the back of the shorts. He is looking out at [SCENE, e.g. a quiet pond at sunset | a city skyline | a wall of trading screens]. Soft light, photoreal, calm, wistful mood.

Grounding: the rear reference, the `toad-back-view-name-tag-wide-banner.jpg` banner, and the board's "Back Identity — Same Toad. Always Toad." (§11).

### 5. Short video (Seedance-style, from the official script)
> [CHARACTER LOCK]. The head is a solid, rigid costume piece, and the eyes and mouth never move. Breathing shows only as a gentle rise and fall in the shoulders and arms, like a person inside the suit. [DURATION, e.g. 15s] · 9:16 vertical · soft lighting · simple backgrounds · gentle cuts. Shot 1: [close-up setup]. Shot 2: [medium shot, the situation escalates; Toad's whole head turns slowly to camera as one rigid piece]. Shot 3: [Toad reacts with his body only]. Shot 4: slow push-in ending on the fixed crooked stitched smile.

Captions (added in edit): "[setup line]" → "[tomorrow-problem line]" → "Same Toad. Different days."
Audio: only tracks you have the rights to. Grounding: `assets/video/toad-one-more-meeting-video-prompt.txt` (§10).

## Voice / copy cheat sheet

**Voice (verbatim):** "Relatable, a little chaotic, warm, and never mean. Everyday moments work best."
**Traits:** Relatable ("He gets it."), Chaotic ("Plans are optional."), Loveable ("Always a little heart.").

**Style rules [derived from site copy]:**
- Short, punchy sentences. Use pairs and triplets ("Same Toad. Different days." / "One Toad. One token.").
- Write about everyday feelings (Mondays, meetings, overthinking, "tomorrow problems"), not charts.
- Keep pond and hop wordplay light. "the pond" = the community, "day ones" = early holders.
- Prefer lowercase "toad" in the wordmark sense and "$TOAD" for the token. The character is "Toad".
- Close with the signature line when it fits: **"Same Toad. Different days."**

**Stock lines (site-verbatim):** "Toad is having a day." · "A little chaos. A lot of heart." · "Life's a lot. Toad gets it." · "Monday again?" · "This feels like a tomorrow problem." · "Currently doing his best." · "Take your time. Toad would." · "The pond has room for you." · "No perfect days required." · "Find your people." · "We're so back." · "Cheers, pond." · "no roadmap I love you"

**Hard rules (kit and site):**
- Never mean.
- No price predictions, promises, or "guaranteed returns". $TOAD "is a meme asset, with no promise of financial returns."
- Don't present fan or bot content as an official announcement.
- When you mention buying, tell people to verify the full CA: `A13oRB9FFaiUjfi6LdCg6p9ka1u8SfGkUFs4SKvPpump` (Solana).
- Handles: X @thetoadmeme_ · TikTok @toad2066 · Telegram t.me/eltoadonsol · Meme Depot memedepot.com/d/the-toad-pepe.

**Example post shapes [inferred, built from site lines]:**
- "Monday again? Toad is having a day. $TOAD"
- "Opened the laptop for one quick thing. This feels like a tomorrow problem. Same Toad. Different days."
- "No perfect days required. The pond has room for you. 🐸"
