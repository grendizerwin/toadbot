# Ready X & Web Search Strings

All calls: `search_posts_all` with `start_time`, `sort_order`, and the fields in the rules block below. "now-24h" = UTC ISO timestamp 24 hours ago.

## Official
- `from:thetoadmeme_ -is:retweet` · start_time now-48h · recency
- `from:thetoadmeme_ has:images` · start_time now-48h · recency
- `from:thetoadmeme_ has:media` · for clips (check `media.type == video`)
- Or `get_users_by_username thetoadmeme_` → `get_users_posts` (includes its image replies under big accounts)

## Community
- `($TOAD OR "toad pepe" OR "el toad pepe" OR "el sapo pepe") -is:retweet` · start_time now-24h · recency, then relevancy
- `$TOAD (website OR game OR telegram OR meme) -is:retweet` · start_time now-48h · relevancy
- Keep posts with real engagement by reading `public_metrics` (e.g. likes ≥ 5 or replies ≥ 3); drop reply-guy sludge.

## Media check
- `($TOAD OR "toad pepe") has:images -is:retweet` · start_time now-48h · relevancy
- Quotes of a strong official post: `get_posts_quoted_posts(<post id>)`

## Continuity
- `get_users_by_username <owner_handle>` → `get_users_posts` (latest 8)

## Price sanity (context only, never in a caption)
- DexScreener / Jupiter / GeckoTerminal for the CA (`A13oRB9FFaiUjfi6LdCg6p9ka1u8SfGkUFs4SKvPpump`).
- For your own read of the room. Never put price, MC, or targets in a caption.

## Skip
- Copycat contracts, impostor handles (`thetoadmeme_1`, `thetoadmcme__`), scam or troll threads: note them, never engage.

## Image references
- Official media: request `media.fields=type,url,preview_image_url`, curl to the box, Read
- Brand kit references listed in visual-bible.md (`$TOAD_KIT/kit/assets/characters/...`)

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
