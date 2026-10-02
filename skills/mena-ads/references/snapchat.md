# Snapchat Ads — the GCC channel generic playbooks skip

Load for any KSA or GCC consumer account, and for any account that asks about Snapchat. In Saudi Arabia, Snapchat is often a top-two channel by reach for under-35s; leaving it out of a Saudi consumer plan is a planning error, not a choice. Platform specs and minimums change; **verify** in Snap's Business Help Center.

---

## 1 · When Snapchat earns budget

| Use it when | Be careful when |
|---|---|
| KSA / Kuwait / UAE / Qatar consumer brand, audience under ~40 | Pure B2B or 45+ audience |
| Fashion, beauty, F&B, delivery apps, telecom, gaming, events, retail, auto launches | Long, text-heavy explanations (sound-on, fast-swiping format) |
| You can produce vertical, native, person-to-camera video in the local dialect | You only have polished landscape TV assets |
| App installs and app re-engagement (strong in GCC) | Tracking has no Snap Pixel/CAPI yet — fix that first |

## 2 · Account structure

- **Campaign → Ad Squad → Ads.** Keep it consolidated: 1-3 ad squads per objective per country, 3-6 creatives each.
- **Separate countries** (KSA vs UAE vs Kuwait): different CPMs and dialects.
- **Objectives:** Awareness & Engagement, Traffic, App promotion, Leads, Sales (Pixel purchases / catalogue). Use Sales with Pixel + CAPI purchase optimisation once the pixel has volume; start on a higher-funnel event (Add to Cart / Page View) if it doesn't.
- **Bidding:** Auto-bid while learning; Target Cost once CPA is stable; Max Bid only with a reason. Give goal-based bidding roughly 50 conversions per ad squad per week before judging (verify current guidance).
- **Audiences:** broad + age/gender/geo works best once the pixel has data. Snap Lifestyle Categories and lookalikes (from delivered/purchaser lists) for prospecting; pixel and engagement retargeting for warm audiences.
- **Placements:** automatic (between content, Discover, Spotlight) unless brand-safety constraints say otherwise.

## 3 · Formats

| Format | Use for |
|---|---|
| **Single Image/Video Snap Ad** (9:16, full screen, sound on) | The workhorse for sales and traffic |
| **Collection Ad** (video + 4 product tiles) | E-commerce catalogues, fashion, beauty |
| **Dynamic Product Ads** (catalogue) | Retargeting and broad catalogue sales |
| **Story Ads** (tile in Discover) | Multi-creative storytelling, consideration |
| **Commercials** (non-skippable up to 6 s) | Awareness, launches |
| **Sponsored AR Lenses / Filters** | Ramadan, Eid, National Day, launches: earned reach and brand moments, not CPA |
| **Lead Ads** (in-app form) | Lead-gen; add a qualifying question, since junk-lead risk is high |

## 4 · Creative rules that win on Snap in the GCC

1. **Hook in the first 1-2 seconds**: face, product, or a bold claim. Snap viewers swipe faster than on any other platform.
2. **Native, not polished:** selfie-style, creator or staff talking to camera in Saudi/Gulf dialect beats studio ads. Shoot on a phone.
3. **Sound on:** Snap is a sound-on platform. Voice-over plus captions (captions for the sound-off minority).
4. **Show the product and the price/offer by second 3**, with delivery promise ("توصيل خلال ٢٤ ساعة") and payment options (Tabby/Tamara, Apple Pay, COD).
5. **Vertical safe zones:** keep text out of the top ~150 px and bottom ~250 px (UI overlays).
6. **3-10 seconds for performance**, longer only for storytelling.
7. **Refresh fast:** young audiences + high frequency = fatigue in 1-2 weeks for strong spenders. Plan 4-6 new creatives per ad squad per month.
8. **Creators:** Snap Stars and local creators drive trust in KSA. Creators doing paid ads need a Mawthooq licence (see [mena-market-playbook.md](mena-market-playbook.md) §6).

## 5 · Tracking

- Snap Pixel + **Conversions API** (via Shopify/Salla/Zid apps, GTM server, or direct). Pass hashed email/phone and the click ID; deduplicate with an event ID.
- For COD: send confirmed and delivered orders server-side (see [tracking-measurement.md](tracking-measurement.md)).
- Snap's default attribution window differs from Meta's. State the window when comparing platforms.

## 6 · Snapchat audit checks (feed into the main audit scorecard)

| # | Check | Severity |
|---|---|---|
| S1 | Pixel + CAPI live, purchases deduplicated, value passed | Critical |
| S2 | Countries split; creative in local dialect | High |
| S3 | ≥ 3 active creatives per ad squad, < 3 weeks old | High |
| S4 | Optimisation event matches the goal (no Swipe-Up optimisation on a sales campaign that has pixel volume) | High |
| S5 | Ad squads not fragmented (each can reach ~50 conversions/week) | High |
| S6 | Creatives 9:16, sound on, hook ≤ 2 s, safe zones respected | Medium |
| S7 | Catalogue connected + Dynamic Product Ads running for e-commerce | Medium |
| S8 | Frequency monitored; refresh plan exists | Medium |
| S9 | Seasonal Lens/Filter or Commercial planned for Ramadan / National Day (brands with awareness budget) | Low |
