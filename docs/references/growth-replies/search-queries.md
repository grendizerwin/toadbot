# Search queries for TOAD growth scans

All calls: `search_posts_all` with `start_time` (UTC ISO, e.g. now-6h or now-12h), `sort_order`, and the fields in the rules block below. Filter engagement on `public_metrics` yourself; tighten if junk, loosen if the window is quiet.

## Continuity (always)

- `get_users_by_username <owner_handle>` → `get_users_posts` (latest 8–10)
- `get_users_by_username thetoadmeme_` → `get_users_posts` (latest 8)
- `from:thetoadmeme_ has:images` / `has:media` when an image reply is possible

## Already-TOAD (people, not pads)

- `($TOAD OR "toad pepe" OR "el toad pepe" OR "el sapo pepe") -is:retweet -from:pumpfun` · start_time now-12h · recency
- Same query · start_time now-24h · relevancy (proof of reach; keep likes ≥ 15 or replies ≥ 5 from `public_metrics`)
- `$TOAD (what OR "what is" OR confused OR "is this") -is:retweet` · start_time now-12h · recency
- Quoters of a strong official post: `get_posts_quoted_posts(<official post id>)`; reply under the *quoter*

Recency for velocity, relevancy for proof of reach.

## Adjacent character / culture

- `(pepe OR frog OR toad) (original OR 1988 OR argentina OR "el sapo" OR mascot OR plush) -is:retweet` · start_time now-12h · relevancy
- `("meme coin" OR memecoin) (mascot OR plush OR character OR brand) (Solana OR SOL) -is:retweet` · start_time now-12h · relevancy
- `("what frog" OR "which pepe" OR "is this pepe") -is:retweet` · start_time now-12h · recency

Drop hits about a different live frog token with no comparison hook.

## Official amplification (humans only)

- `@thetoadmeme_ -from:thetoadmeme_ -is:retweet` · start_time now-12h · recency
- `get_posts_quoted_posts` on today's official media; don't default to commenting under official.

## Relevancy sweeps (replace the old "semantic" prompts; there is no semantic search)

- `("toad pepe" OR "el toad pepe" OR "el sapo pepe") (what OR who OR explain) -is:retweet` · relevancy
- `(pepe frog) (toad OR argentina OR 1988 OR older) -is:retweet` · relevancy
- `(solana) (mascot OR plush) (memecoin OR "meme coin") -is:retweet` · relevancy

## Price / fact check (web, not reply targets, never quoted in replies)

- DexScreener / Jupiter / Gecko for `A13oRB9FFaiUjfi6LdCg6p9ka1u8SfGkUFs4SKvPpump`
- Official site / game mentions only if a live post references them

## Do not query as destinations

- `from:pumpfun` / other factory pages
- Bare `$TOAD` with no engagement filter (reply-guy sludge)
- `from:elonmusk` as a default hunt
- Impostor / lookalike handles (`thetoadmeme_1`, `thetoadmcme__`) as official
- Copycat contracts, scam or troll threads (log in the skip list, never reply)

## X connector rules (tested 17 Oct 2026)

- Tool: `search_posts_all` (namespace `x`). Time window = `start_time` in UTC ISO (`date -u -d '-6 hours' +%Y-%m-%dT%H:%M:%SZ`). `within_time:` makes the whole call fail.
- `min_faves:`, `min_replies:`, `filter:images`, `filter:videos` are silently dropped. Use `has:images` (photos) or `has:media` (photos + video), add `-is:retweet`, and filter on `public_metrics` yourself.
- Always request `post.fields=public_metrics,created_at,conversation_id`, `expansions=author_id,attachments.media_keys`, `media.fields=type,url,preview_image_url`, `user.fields=username`.
- "Latest" = `sort_order: recency`; "Top" = `sort_order: relevancy`. There is no semantic search; use a keyword query sorted by relevancy.
- Quotes of a post: `get_posts_quoted_posts(<post id>)` (`quoted_tweet_id:` doesn't exist).
- Thread fetch: `get_posts_by_id(<id>)` + `search_posts_all "conversation_id:<id>"` sorted by recency.
- Account activity: `get_users_by_username` → `get_users_posts(<numeric id>)`. `search_users` returns 403.
- Viewing media: curl the `url` (photo) or `preview_image_url` (video frame) to the box and Read it. Video can't be watched; say so and judge from the preview frame.
- Budget: 30 calls/min, 1000/day, max 25 results per call. Batch, don't spray.
- Posting: the X connector has no post tool. Only a draft the user explicitly approved goes out, once, through the box browser. Scheduled runs deliver drafts only.
