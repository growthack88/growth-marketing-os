# Google Ads — Search, Shopping, PMax, Demand Gen, YouTube

Load for any Google Ads audit, build, or optimisation. Thresholds below are **practitioner defaults** (adapted from the open-source projects in [CREDITS.md](../CREDITS.md)), not Google policy. The account's own 90-day baseline beats any of them.

---

## 1 · Data rules before any judgement

- Pull **campaign → ad group → keyword/search term** data for the last 30 days plus the previous 30. For Shopping, use 14 days if the account has ≥ 100 purchases/month, otherwise 30.
- **Minimum evidence:** don't judge Smart Bidding performance below ~30 conversions in 30 days (Search) or ~50 (PMax/Shopping). Don't make segment calls (device, location, hour) below ~50 clicks and 5 conversions per segment.
- **Check the change history first.** Anything edited in the last 7 days is still settling; don't stack a new change on it.
- **Only real levers:** campaign budgets, bid strategy/targets, keywords/negatives, assets, audiences/signals, schedules and locations, and pause/enable. Never "move budget to a search term" or "to a device"; no such lever exists.
- **Never change bids and budget on the same campaign at the same time.** One variable at a time, max ±20% per step, wait at least 7 days.
- API pitfalls (MCP/API mode): costs are in micros (÷ 1,000,000); always filter `status = 'ENABLED'`; don't sum conversions across different attribution windows.

## 2 · Search: the weekly decision system

**Search-term classes (per term, last 30 days, vs target CPA/ROAS):**

| Class | Rule | Action |
|---|---|---|
| Q1 Profitable | ≥ 2 conversions at or better than target | Isolate to exact match in its own ad group / campaign; protect it |
| Q2 Promising | 0 conv, cost < 0.5× target CPA | Keep, let data accumulate |
| Q3 Unproven | 0 conv, cost 0.5-1× target CPA | Watch; check relevance and landing page |
| Q4 Losing | cost ≥ 1× target CPA with 0 conv, or CPA ≥ 1.5× target, or ROAS ≤ 0.7× target | Cap: lower bid, move to exact with a lower target, or negate |
| Q5 Invalid | Intent mismatch: free, cheap (for premium), DIY, how to, jobs/وظائف, salary/مرتب, course/كورس, PDF, meaning/معنى, used/مستعمل, repair/تصليح | Negate always |

**Red List (fast waste finder):** take the campaigns making up 80% of spend, then the terms making up 80% of each. Flag a term if (spend ≥ 5% of campaign AND CTR ≥ 40% below the campaign's) or (spend ≥ 8% AND CVR ≥ 40% below, zero included). If ≥ 3 flagged terms share a word, add one phrase-match negative for the root instead of many exacts.

**Pressure matrix (impression share):**

| Situation | Signal | Action |
|---|---|---|
| Budget-limited winner | Lost IS (budget) ≥ 20% and CPA ≤ target | Budget +10-20% |
| Rank-limited | Lost IS (rank) ≥ 20-30%, or top-of-page < 60% | Improve ad relevance / landing page / QS first; bids +5-10% only if competition is the cause |
| Saturated | IS ≥ 80% and CPA ≤ target | Healthy; growth must come from new keywords/campaigns |
| Expensive and visible | IS ≥ 75% and CPA > target | Hold or trim bids; no budget increase while CPA > 1.2× target |
| Brand campaign | Brand IS < 85% | Fix it first: cheapest conversions in the account |

**CPC inflation:** three causes: competition, match-type leakage (broad pulling junk), ad relevance. Only competition justifies higher bids. Scale only while week-over-week CPC growth stays below CVR growth.

**Fixed weekly order:** prune (negatives) → reclassify terms → recompute CPA/ROAS → bids/budgets → relevance (ads, assets, landing pages).

## 3 · Search build defaults

- Structure by intent theme, not by keyword: Brand · Generic-high-intent · Competitor (only if CPA ≤ 1.2× target) · DSA/broad catch-all (only with Smart Bidding and strong negatives).
- **No broad match without Smart Bidding** and a conversion goal with volume.
- **RSAs:** ≥ 8 headlines (12-15 ideal), 4 descriptions, pin only for legal/brand reasons; Ad Strength Good+; ≥ 4 sitelinks, callouts, structured snippets, call and image assets; price/promotion assets in sale seasons.
- **Bid strategy by goal:** volume → Maximise Conversions; a cost target → tCPA (once ~30 conv/30 days); revenue → Maximise Conversion Value; a return target → tROAS (once ~50 conv/30 days). New account without tracking → Maximise Clicks with a CPC cap, only until tracking works.
- **Negatives list** shared across campaigns from day one (Q5 terms in Arabic + English + Franco spellings).
- Quality Score: aim for ≥ 7 on top-spend keywords; fewer than 10% of keywords at QS ≤ 3.

### MENA specifics for Search
- **Languages:** target Arabic **and** English for Arabic campaigns (many users run Google in English). Build separate ad groups for Arabic queries, English queries, and Franco/Arabizi queries, each with ads in the query's language.
- **Spelling variants:** ة/ه, ى/ي, أ/إ/ا, with and without ال, plus common typos. Add them as keywords and as negatives where relevant.
- **Location:** use "Presence: people in or regularly in your targeted locations", not "interest", or you'll pay for clicks from outside the market (common with GCC targeting from Egypt/India).
- **Call assets and WhatsApp:** many MENA searchers would rather call or message; use call assets with business hours and test a WhatsApp click path on the landing page.
- **Ramadan:** search volume shifts to late night; check hour-of-day before adding schedules; don't cut daytime blindly.

## 4 · Performance Max

- **Maturity gate:** don't judge before 30 days (ideally 60) or ~50 conversions.
- **Kill rule:** ROAS < 0.3× target after spend ≥ 3× AOV → pause or rebuild.
- **PMax vs Search ROAS ratio:** < 0.5 poor · 0.5-0.9 below par · ≥ 0.9 healthy.
- **Brand cannibalisation:** if brand terms make up > ~15% of PMax conversions, add brand exclusions (brand lists) and let the brand Search campaign own them.
- **Scaling:** profitable for 14-30 days → budget +20% (up to +50% for mature PMax) every 14-30 days; stop if CPA > 1.2× target or ROAS < 0.8× target. Cap at 2-3× the starting budget until 90 days of profitability.
- **Assets:** 5-10 images, 5 videos (make your own vertical + horizontal; don't let Google auto-generate), 5 headlines, 5 long headlines, Arabic and English asset groups where both audiences matter. Asset labels: Best → make variations · Low → replace · Pending → wait 14+ days.
- **Structure:** several focused PMax campaigns, each with a single asset group (by margin tier or category), outperform one PMax with many groups. PMax at ~10-25% of account spend is a common sweet spot when Search is strong.
- **Audience signals:** customer lists (delivered buyers), site visitors, and custom segments built from high-intent Arabic and English search terms.
- **Exclusions:** device or location with CPA > 1.5-2× the account average → consider excluding; exclude placements in mobile-app inventory if junk leads appear.

## 5 · Shopping (Standard + feed)

- **Feed gate:** ≥ 80% of products approved and conversion tracking live, or nothing else matters. Titles front-load brand + product type + key attribute; include the Arabic title in a separate feed/label where you target Arabic shoppers.
- **Per product:** KILL if cost ≥ 2× AOV with 0 conversions · DOWNGRADE if ROAS < 0.7× target and cost ≥ 0.5× AOV · PROMOTE if ≥ 2 conversions and ROAS ≥ target.
- Keep ≤ 3 product-group tiers (heroes / steady / zombies); custom labels for margin, price band, season.
- **Campaign kill:** ROAS < 0.6× target after spend ≥ 2× AOV.

## 6 · Demand Gen and YouTube

See [other-platforms.md](other-platforms.md#youtube-via-google-ads). Judge on view-through conversions plus brand-search lift, not last-click alone.

## 7 · Google audit checks (feed the scorecard in [audit-checklist.md](audit-checklist.md))

| # | Check | Category | Severity |
|---|---|---|---|
| G1 | Primary conversion action = the real business goal (purchase / qualified lead / delivered order), secondary goals not counted in bidding | Measurement | Critical |
| G2 | Enhanced Conversions live; offline conversions imported for lead-gen / COD | Measurement | Critical |
| G3 | Google tag + Consent Mode v2 where required; GA4 linked; auto-tagging on | Measurement | High |
| G4 | Search terms reviewed in the last 14 days; irrelevant spend < 5% | Waste | Critical |
| G5 | Shared negative lists (incl. Arabic/English/Franco Q5 terms) applied | Waste | High |
| G6 | Location setting = Presence, not interest | Waste | High |
| G7 | Display/Search Partners off on Search unless proven | Waste | Medium |
| G8 | Brand split from non-brand; brand IS ≥ 85% | Structure | High |
| G9 | No broad match without Smart Bidding | Structure | High |
| G10 | Bid strategy matches volume (tCPA ≥ 30 conv/30d; tROAS ≥ 50) and target within 30% of actual | Bidding | High |
| G11 | Campaigns not budget-limited while CPA ≤ target (lost IS budget < 20%) | Bidding | Medium |
| G12 | RSAs: ≥ 8 headlines, Ad Strength Good+, every ad group has ≥ 1 RSA | Creative | High |
| G13 | ≥ 4 sitelinks + callouts + structured snippets + call/image assets | Creative | Medium |
| G14 | QS ≥ 7 on top-spend keywords; < 10% at QS ≤ 3 | Keywords | Medium |
| G15 | Arabic + English languages targeted for Arabic campaigns; spelling variants covered | Keywords | High (MENA) |
| G16 | PMax brand exclusions in place; PMax not cannibalising brand Search | Structure | High |
| G17 | PMax has own-made video + ≥ 5 images per asset group | Creative | Medium |
| G18 | Merchant Center feed ≥ 80% approved, no critical errors | Settings | Critical (e-com) |
| G19 | Ad schedule / hour-of-day reviewed for Ramadan and weekends (Fri-Sat vs Sat-Sun) | Settings | Low |
| G20 | Conversion value passed with correct currency (EGP/SAR/AED vs account currency) | Measurement | Critical |
