---
name: toad-targets
description: Use when a TOAD drafts, growth-reply or crossover run needs the watch lists, ready X search queries, the official contract address and lookup query, or the don't-engage and scam-pattern rules.
---

# TOAD Targets: watch lists, queries, don't-engage

Shared reference for `toad-template-post-generator`, `toad-template-growth-replies`, `toad-template-crossover-replies` and the `toad-daily-drafts` routine. Everything here is a **starting map, not a hall of fame**: re-check every account live, and only name an account in a pack with a this-window reason (post URL, views, a question they asked).

Owner values come from `/home/box/shared/toad-config.json` (`owner_handle`, `owner_user_id`, optional `target_list_id`).

## Official TOAD (from thetoadmeme.com, mirrored in `$TOAD_KIT/kit/BRAND.md` §1–2)

- X: **@thetoadmeme_** (https://x.com/thetoadmeme_), the only official account. X Community: https://x.com/i/communities/1991148242780967304
- Site: https://thetoadmeme.com/ · Telegram: https://t.me/eltoadonsol · TikTok: @toad2066 · Meme Depot: https://memedepot.com/d/the-toad-pepe
- Chain: Solana. **Contract / mint address: `A13oRB9FFaiUjfi6LdCg6p9ka1u8SfGkUFs4SKvPpump`** (listed on thetoadmeme.com and in BRAND.md §1; re-confirmed on the live site Oct 20, 2026). DEX pair: `Nx9dcwNs3iJxM5YAxshMHE4aYJHdDyyGMhVcmaSgfu8`.
  - **Never post the CA unprompted.** If the owner asks for it in a post, include "verify the full address".
  - Always compare the **full** string. A CA that matches only the first/last few characters is a lookalike.
- **Unofficial lookalikes / impersonators (never amplify as official, never engage):** @thetoadmcme__ and @thetoadmeme_1. Treat any other handle that imitates @thetoadmeme_ (swapped letters, extra underscores or digits, "support", "airdrop", "claim") the same way.

## Crypto watch list (public accounts)

- **@thetoadmeme_** — source of truth for media. Weak reply destination (its community is already there); best as QT fuel, or reply under *people* who quote it (`get_posts_quoted_posts`). It also posts image replies under big accounts: read its `referenced_tweets` and don't stack under the same parents.
- **Public supporters** — people who have posted about TOAD themselves. Good continuity / reply targets when they're live and on a TOAD-fit topic; find them live (search `$TOAD` / `El Toad Pepe`), don't keep a fixed roster. **Never mention anyone's wallet or holdings.** Don't @ them cold with a ticker dump; skip finance-flavored posts.
- **Big CT accounts (context, rarely targets):** @blknoiz06, @gainzy222. Text replies under big CT accounts get buried; use them for mood, not as default reply targets.
- **Launchpads / chain pages (context only, never reply targets):** @Pumpfun and other launchpad, factory and chain accounts (@solana, @BNBCHAIN).
- **Owner's own orbit:** mentions and replies to the owner (`get_users_mentions <owner_user_id>`) are the reply-back pool.
- **Optional owner list:** if `target_list_id` is set, `list:<target_list_id> -is:retweet` (crypto lists) or `list:<target_list_id> has:images -is:retweet` (visual pages).

## Crossover sources (big non-crypto pages for remixes)

Pages that have produced remixable stills (re-check followers with `user.fields=public_metrics`; target 1M+ followers, under ~30 replies, under ~3 h old):

@NoContextHumans · @HumansNoContext · @nocontextfooty · @PopBase · @PopCrave · @Dexerto · @InternetH0F · @BleacherReport · @DiscussingFilm · @memechaotic · @GWR

Also useful by type (look up the official handle live): weather-service maps, sports-commentary pages with a still, gadget/Apple-leak pages, food-meme pages, nature/animal pages, out-of-context meme pages.

Usually drop even if they're big: coin-chart accounts, "JUST IN" token/exchange/ETF pages, finance-news pages (e.g. Polymarket, WatcherGuru, unusual_whales, Cointelegraph).

## Ready queries (`search_posts_all`, namespace `x`)

Always add `start_time` (UTC ISO), `sort_order`, and the fields: `post.fields=public_metrics,created_at,conversation_id,in_reply_to_user_id,referenced_tweets`, `expansions=author_id,attachments.media_keys`, `media.fields=type,url,preview_image_url`, `user.fields=username,public_metrics`. Filter engagement on `public_metrics` yourself.

**Official**
- `from:thetoadmeme_ -is:retweet` · now-48h · recency
- `from:thetoadmeme_ has:images` / `from:thetoadmeme_ has:media` · now-48h
- `@thetoadmeme_ -from:thetoadmeme_ -is:retweet` · now-12h · recency (humans talking to official)

**Community / $TOAD**
- `($TOAD OR "toad pepe" OR "el toad pepe" OR "el sapo pepe") -is:retweet -from:pumpfun` · now-12h recency, then now-24h relevancy (keep likes ≥ 15 or replies ≥ 5 for reach)
- `$TOAD (what OR "what is" OR confused OR "is this") -is:retweet` · now-12h · recency
- `$TOAD (website OR game OR telegram OR meme) -is:retweet` · now-48h · relevancy
- `($TOAD OR "toad pepe") has:images -is:retweet` · now-48h · relevancy
- Note: X search strips `$`, so `$TOAD` also matches every non-crypto "toad" post (games, insults, fandoms). Always pair it with other terms, or use the CA query.

**Contract-address query (most TOAD-specific; also where spam shows up)**
- `A13oRB9FFaiUjfi6LdCg6p9ka1u8SfGkUFs4SKvPpump -is:retweet` · now-24h · recency
- Use it to find real TOAD talk and to spot CA spam. Never reply under CA dumps.

**Adjacent character / culture**
- `(pepe OR frog OR toad) (original OR 1988 OR argentina OR "el sapo" OR mascot OR plush) -is:retweet` · now-12h · relevancy
- `("meme coin" OR memecoin) (mascot OR plush OR character OR brand) (Solana OR SOL) -is:retweet` · now-12h · relevancy
- `("what frog" OR "which pepe" OR "is this pepe") -is:retweet` · now-12h · recency

**Owner continuity**
- `get_users_posts <owner_user_id>` (latest 8–10) or `from:<owner_handle> -is:retweet` · recency
- `get_users_mentions <owner_user_id>` or `@<owner_handle> -from:<owner_handle> -is:retweet` · now-24h

**Crossover (big non-crypto pages)**
- `(from:NoContextHumans OR from:HumansNoContext OR from:nocontextfooty OR from:PopBase OR from:PopCrave OR from:Dexerto OR from:InternetH0F OR from:BleacherReport OR from:DiscussingFilm OR from:memechaotic OR from:GWR) has:images -is:retweet` · now-4h · recency (then now-8h)
- Same with `has:media` · now-6h for video posts (check `media.type`, judge from `preview_image_url`)
- Optional owner list: `list:<target_list_id> has:images -is:retweet` · now-8h, then now-4h

**Trending formats**
- `get_trends_by_woeid` with `1` (worldwide) or `23424977` (US) for what's trending; only use a trend if a big page posted a remixable still about it.
- `(meme OR template OR "everyone is posting") has:images -is:retweet lang:en` · now-12h · relevancy; keep only posts with real engagement.

**Spam negatives** (append to discovery queries when noisy): `-airdrop -presale -giveaway -"CA:" -"join us" -"free $50"`

## Don't engage (patterns)

Log these in the skip list; never reply, quote, like-bait or argue:

- **Impersonators** of @thetoadmeme_ or of the owner (lookalike handles, copied avatars/bios, "official support").
- **Fake airdrop / claim links**, "connect wallet to claim", reward or "eligibility checker" sites.
- **"DM for support" / "DM for alpha TG"**: anyone offering help, recovery, or a private group via DM; copy-paste "$TOAD 191x, $6.8K→$1.3M, DM for my private alpha TG" promos.
- **CA lookalikes / copycat tokens**: any address that isn't the full official CA, "TOAD 2.0", "real TOAD", migration or "V2" claims not posted by @thetoadmeme_.
- **TG-link / CA spam** ("$TOAD is live, join the TG") from unverified accounts.
- **Paid signal / VIP-scanner groups, referral-code spam, presale shill rings, RT+tag giveaway farming, follow-back / CTO-recruitment bait.**
- **Trolls, abusive posts, and "X is a scam/rug" accusation threads** about the project or any person. Don't argue or defend; stay neutral or skip.
- Launchpad launch cards and factory pages.
- Accounts change fast. Judge by the pattern in the post, not by a static list; new spam accounts appear daily.
