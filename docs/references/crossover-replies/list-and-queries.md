# List and search queries

Primary candidate source is the owner's optional X list (`target_list_id` in `/home/box/shared/toad-config.json`, from the list URL `x.com/i/lists/<id>`):

- Operator: `list:<target_list_id>`

If no list is set, use the big visual pages in `toad-targets` instead. A good list is a mix of viral mainstream pages (pop, sports, nature, food, gadgets, meme aggregators) and some crypto accounts. Crypto-on-the-list is not a target.

## Required searches each run

`search_posts_all`, `sort_order: recency` first, relevancy only if recency is thin. Fields: `post.fields=public_metrics,created_at,conversation_id`, `expansions=author_id,attachments.media_keys`, `media.fields=type,url,preview_image_url`, `user.fields=username`.

```
list:<target_list_id> has:images -is:retweet   start_time = now-8h
list:<target_list_id> has:images -is:retweet   start_time = now-4h
list:<target_list_id> has:media -is:retweet    start_time = now-6h   (video: check media.type, judge from preview_image_url)
```

On a busy list the 8h image query usually returns a full page of 25 photo posts (next_token present). Paginate with `next_token` only if page 1 is all crypto.

When the list is mostly crypto, add optional negatives: `-crypto -bitcoin -btc -solana -memecoin`.

Engagement filtering is yours: read `public_metrics` (likes, replies, impressions) and `created_at`. `min_faves`, `filter:images`, and `within_time:` don't work.

Continuity:

```
get_users_by_username <owner_handle> → get_users_posts (latest 10)
get_users_by_username thetoadmeme_  → get_users_posts (latest 25, with tweet.fields=created_at,in_reply_to_user_id,referenced_tweets,attachments)
```

@thetoadmeme_ already posts image replies under big accounts (checked 17 Oct 2026: 15 of its last 25 posts were image replies to PopCrave, Dexerto, Polymarket, WatcherGuru, unusual_whales, DiscussingFilm, FearedBuck, Cointelegraph). Read `referenced_tweets` (type `replied_to`) and skip any parent post it already replied under. Avoid stacking on an author it hit in the last few hours.

Do not wander onto random mega-accounts outside the list / `toad-targets` pages. There is no semantic search.

## Known list flavors (not a complete roster)

Treat these as examples of who shows up. Re-check live. Do not hard-code a hall of fame.

Often usable when the post is visual and non-crypto:

- Pop / celebrity aggregators
- Nature / animal pages
- Food meme pages
- Sports / Barstool-style commentary with a still
- Gadget / Apple leak pages
- Weather maps
- Chaotic / out-of-context meme pages

Usually drop even if on the list:

- Coin-chart accounts
- "JUST IN" token / exchange / ETF posts
- Wallet, pad, or CA posts

## What to open

For every keeper, fetch the post (`get_posts_by_id`), curl the parent photo `url` (or a video's `preview_image_url`) to the box, and Read it before writing an edit prompt. Video can't be watched; say so. Then attach it with the brand-kit character references (see `remix-playbook.md`).

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
