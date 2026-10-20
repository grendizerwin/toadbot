# Scoring TOAD reply windows

Score **visibility + adjacency + add**. Fame of the author is last.

## Hard fail

Drop immediately if:

- Conversation older than ~12 hours and engagement is flat
- 400+ replies on a finished post
- Author is a launchpad / factory / official protocol page or the post is their launch card
- Author is a known reply-guy farm or engagement pod
- Thread is a giveaway, follow-train, or identical-emoji raid
- Only possible line is "🐸 $TOAD" or a burned 1988 slogan
- Parent is off-adjacent (see `adjacent-surfaces.md`)
- the owner already replied unless a new fact appeared
- Same target account used in the last 24–48 hours
- Troll bait, scam, copycat / impostor contract, or a thread where the only angle is mocking a coin or person
- Your draft matches or near-matches another reply in this pack or the last 48h

Mega-accounts only pass with a specific fact the existing replies lack. That is rare.

## Visibility (need two)

- Roughly 2k–250k views and 5–80 replies
- Less than 6 hours old, or replies still arriving
- You would be among the first *useful* comments

Tiny posts (<200 views) pass only if the author is a real person who replies and the adjacency is perfect (they asked what TOAD is).

## Adjacency (need one strong)

- Parent already names TOAD / El Toad Pepe / El Sapo Pepe / official plush / @thetoadmeme_
- Parent is a character mix-up you can correct with one observed detail
- Parent is mascot / brand-not-chart and you have a live official visual
- A human QT of official media
- A real question about the token or the 1988 / Argentine character

No strong adjacency = do not ship as a TOAD reply.

## Add (need one clause)

You must name the add:

- Answer the question they asked
- Poke one detail in their image the caption missed
- Drop one confirmed live fact (game, clip, number) the thread does not have
- Dry joke that dies if you swap the character (a brand phrase like "tomorrow problem" or "the pond" tied to their situation counts)

"I like this coin" is not an add.

## Score 1–5

- **5** — Rising, mid-size, already-TOAD or tight adjacent, clear add, human author
- **4** — Rising or mid-size, adjacent, clear add
- **3** — Adjacent but competition rising, or visibility only okay. Optional third only
- **2** — Weak visibility or weak bridge. Skip unless pack is empty
- **1** — Off-adjacent, buried, pad, raid, or hard shill. Skip

## Pack diversity

- Different authors and conversations (max 3 replies: up to 2 text reply-backs, 0–1 image)
- Mix already-TOAD with adjacent. Do not ship three comments inside the official reply section
- At most one image reply
- At most one ticker-heavy line
- Prefer people who historically reply

After picking a target, fetch the thread: `get_posts_by_id(<id>)` plus `search_posts_all "conversation_id:<id>"` sorted by recency. If your line is already there, rewrite or drop.
