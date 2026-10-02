# TikTok Ads — Smart+, Spark Ads, creators, and the KSA/Egypt/Iraq audience

Load for any TikTok audit, build or optimisation. TikTok is strong in KSA, Egypt, Iraq and the UAE. It is creative-first: the algorithm finds the audience if the video earns attention. Thresholds are practitioner heuristics; **verify** platform minimums in TikTok Ads Manager help.

---

## 1 · Structure

- **Campaign → Ad group → Ads.** Default to consolidation: 1-2 ad groups per country per objective, broad targeting (age/gender/geo + language only when it matters), 3-6 creatives per ad group (more for Smart+).
- **Smart+ (TikTok's automated campaign)** for sales/app/lead campaigns once the pixel has conversion history; keep a manual campaign for controlled creative tests and specific audiences.
- **Learning:** ~50 conversions per ad group within 7 days to exit. Budget so the ad group can hit it: daily budget comfortably above `target CPA × 50 ÷ 7`. TikTok's own guidance has suggested much higher multiples of CPA for CPA bidding (verify the current figure). Use `scripts/ads_calc.py learning --platform tiktok --cpa X`.
- **Don't edit during learning.** Budget changes ≤ 20-30% per step; duplicate winners rather than multiplying budget.
- **Bidding:** Maximum Delivery (lowest cost) to learn; Cost Cap once CPA is stable; Value-based optimisation (VBO) for e-com with value data.
- **Optimisation event:** Complete Payment (prepaid) / confirmed-order server event (COD) / qualified lead. If volume is low, step up the funnel (Add to Cart, Initiate Checkout) rather than starving the ad group.
- **TikTok Shop / GMV Max:** only where TikTok Shop operates for the brand's market (verify availability in the GCC/Egypt).

## 2 · Tracking

TikTok Pixel + **Events API** (Shopify / Salla / Zid / WooCommerce integrations or GTM server), deduplicated via `event_id`, with hashed email/phone and `ttclid`. For COD, send confirmed and delivered orders server-side ([tracking-measurement.md](tracking-measurement.md)). TikTok's default attribution window differs from Meta's; compare like with like.

## 3 · Creative: what wins in the region

- **Native, not ads:** creator or real-person, phone-shot, Arabic in the market's dialect (Saudi/Gulf for KSA, Egyptian for Egypt, Iraqi for Iraq). Polished TV spots get scrolled.
- **Structure:** hook 0-3 s (face, bold claim, pattern interrupt, question in dialect) → value/demo 3-15 s → proof (review, before/after where allowed, unboxing) → CTA in the last 3 s with offer + delivery promise + payment options.
- **Sound on**, always; never silent video. Trending sounds from the Commercial Music Library only (licensing). Voice-over + burned-in captions in Arabic.
- **Cuts every 2-3 seconds**; text overlays for key claims.
- **9:16, 1080×1920**, keep text and faces inside the safe zone (roughly x 40-940, y 150-1470 px; avoid the right-side buttons and bottom caption area).
- **Spark Ads:** boost creator posts and the brand's organic winners; they keep social proof (likes/comments) and usually beat dark ads. Use TikTok One (Creator Marketplace) to brief creators; in KSA, creators need a Mawthooq licence for paid promotion ([mena-market-playbook.md §6](mena-market-playbook.md)).
- **Fatigue is fast:** plan refreshes every 7-14 days for strong spenders; keep 7-day frequency ≤ 3. Refresh = new hook or new angle, not a new colour grade.
- **Research:** TikTok Creative Center (top ads by country and industry, trending hashtags/songs in KSA/UAE/Egypt) and the Ad Library for competitors ([creative-system.md §6](creative-system.md)).

## 4 · Reading results

- Video metrics: 2-second and 6-second view rates, average watch time, completion rate. A low 2-s view rate means a weak hook; a good 6-s rate with low CTR means a weak offer/CTA.
- TikTok often shows low last-click ROAS but drives brand search and Meta/Google conversions. Check blended MER and brand-search trends before cutting it ([tracking-measurement.md §5](tracking-measurement.md)).
- Kill/scale calls use the same rules as Meta ([budget-scaling.md](budget-scaling.md)), applied per ad group after the learning window.

## 5 · TikTok audit checks (feed the scorecard in [audit-checklist.md](audit-checklist.md))

| # | Check | Category | Severity |
|---|---|---|---|
| T1 | Pixel + Events API live, dedup via event_id, value passed | Measurement | Critical |
| T2 | Optimisation event matches business value (Complete Payment / confirmed order / qualified lead) | Measurement | Critical |
| T3 | Ad groups can reach ~50 conversions/week (budget vs CPA) | Structure | High |
| T4 | No edits during learning; changes ≤ 20-30% per step | Bidding | High |
| T5 | Country split; dialect matches market | Structure | High (MENA) |
| T6 | ≥ 3-6 creatives per ad group, newest < 14 days old | Creative | High |
| T7 | All videos 9:16, sound on, captions, safe zones respected | Creative | High |
| T8 | Hook in first 3 s; 2-s view rate tracked | Creative | Medium |
| T9 | Spark Ads / creator content in the mix | Creative | Medium |
| T10 | 7-day frequency ≤ 3; refresh plan exists | Waste | Medium |
| T11 | Smart+ used where conversion history allows (or a stated reason) | Bidding | Low |
| T12 | Commercial-licensed music only; creator licences on file | Settings | Medium |
