# Meta Ads — Facebook, Instagram, Messenger, WhatsApp (CTWA)

Load for any Meta audit, build, optimisation or diagnosis. Thresholds are **practitioner heuristics** (adapted from the open-source projects in [CREDITS.md](../CREDITS.md)); recalibrate them to the account's own 90-day baseline. Platform facts marked **verify** change often.

---

## 1 · Evidence rules (apply before any verdict)

- **A change is real only if** it moved ≥ 15% *and* rests on ≥ 10 conversions or ≥ 500 clicks. Below 30 conversions/week, widen the noise band to ±25% vs a 4-week average.
- **No verdict below the minimum:** < 3× target CPA spent or < 10 conversions → "not enough data", not a recommendation.
- **Conversion lag:** check what share of conversions is visible by day 1. ≥ 80% → judge after 1-2 days; 50-80% → wait 3-4 days; < 50% (high-ticket, COD confirmation, lead-to-sale) → wait 7+ days. Don't cut anything inside its lag window.
- **Skip entities edited in the last 48-72 hours.** They haven't settled.
- **Group by concept, not ad ID:** the same video duplicated across ad sets is one creative.
- **Purchase counting (API/MCP):** use `omni_purchase` if present, else `purchase`; never add both.

## 2 · Diagnostic ladder (when results change)

Walk in order and stop at the first match:

| Step | Pattern | Diagnosis | Go to |
|---|---|---|---|
| 1 | Conversions down, clicks steady, and a tracking/site/checkout change happened | **Signal problem** | §4, [tracking](tracking-measurement.md) |
| 2 | < 30 conversions in 30 days, or the change rests on < 10 conversions | **Not enough data** | Gather more; consolidate |
| 3 | CPM up ≥ 20%, CTR within 15% of baseline | **Auction / season / budget pressure** (Ramadan, White Friday, competitors) | §6 seasonal bids; judge on CPA not CPM |
| 4 | CTR down ≥ 25%, CPM steady, frequency rising | **Creative fatigue** | §5 |
| 5 | CVR down ≥ 25%, CTR and CPM steady | **Landing page / offer / checkout / stock / price** | LP check; COD: confirmation step |
| 6 | One campaign takes ≥ 70% of spend with weak results | **Allocation** | §6 |
| 7 | None of the above | **Noise**, so hold | — |

Also check the **click-to-session gap**: landing page views should be ≥ 80% of link clicks and GA4 sessions ≥ 70% of LPVs. LPV < 70% of clicks → slow page / redirect problem (common on heavy Arabic-font pages and COD form pages). LPV fine but sessions < 50% → measurement (UTMs stripped by redirects).

## 3 · Structure (2026 defaults)

- **Consolidate.** An ad set needs ~50 optimisation events/week to learn. Max useful ad sets ≈ weekly conversions ÷ 50. More than that = fragmentation; merge (only if the merged ad set clears 50/week).
- **Learning health:** ≥ 50 events/week supports learning · 25-50 thin · < 25 or more than one reset/week can't learn. Keep "Learning limited" < 30% of ad sets.
- **Account shape for e-com:** 1 Advantage+ Sales campaign (broad, the main volume engine) + 1 manual sales campaign for tests/specific audiences + retargeting only if the warm pool is big enough to justify it (Advantage+ already retargets). Split by **country** (Egypt ≠ KSA ≠ UAE).
- **Advantage+ Sales readiness:** CAPI live, pixel with history, ~50+ purchases/week. States: healthy & scaling (within 15% of target, 50+/week) · constrained (≥ 70% of spend on one product or creative) · unstable (< 50/week, low EMQ, unverified dedup) · misleading (conversions don't match business quality, e.g. COD refusals, junk leads) · unclear (< 14 days of data).
- **CBO vs ABO:** CBO/Advantage campaign budget for scaling (generally ≥ ~$100-300/day equivalent); ABO for controlled creative tests with small budgets.
- **Budget floor per ad set:** daily budget ≥ ~5× target CPA (warning 2-5×; < 2× can't learn). Use `scripts/ads_calc.py learning --platform meta --cpa X`. If the budget can't reach it, optimise for a higher-volume event (Add to Cart, Initiate Checkout, ConfirmedOrder) or consolidate.
- **Audiences:** broad + Advantage+ audience is the default; your audience inputs are suggestions. Hard limits remain location, minimum age, language and custom-audience exclusions. Exclude purchasers (and COD refusers) from prospecting. Lookalike seeds: ≥ 1,000 people from **one country**, refreshed within 30 days, value-based (delivered buyers). Nested lookalikes from the same seed compete with each other.
- **Overlap:** < 20% clean · 20-30% tidy up · > 30% consolidate.
- **Special Ad Categories:** housing (most real-estate ads), employment, credit, financial products and services, social issues/elections restrict targeting; declare them or the account gets restricted. Real estate is a large category in UAE/KSA/Egypt; plan for broad targeting there.
- **Attribution (verify):** Meta removed the 7-day-view and 28-day-view windows in January 2026; the standard setting is **7-day click + 1-day view** (1-day engaged-view for video). State the window in every report; compare click-only when view-through is > 25% of conversions.

## 4 · Signal quality (Pixel + CAPI)

| Status | Criteria | Meaning |
|---|---|---|
| **Ready to scale** | EMQ (Purchase) ≥ 6, ideally ≥ 8 · dedup verified (same `event_id` browser + server; 60-90% browser/server overlap is healthy) · ~50 events/week/ad set · optimised event reflects real value | Scale on platform data |
| **Needs review** | EMQ 4-6, single source only, dedup unverified, or 20-50 events/week | Fix before scaling |
| **Not ready** | EMQ < 4, both sources without dedup, < 20 events/week, or the optimised event ≠ business value (placed COD orders, raw leads) | Fix signal first; numbers are unreliable |

Plus: domain verified; Aggregated Event Measurement priorities set (Purchase → InitiateCheckout → AddToCart → ViewContent → Lead…); standard events over custom where possible; value + correct currency. iOS: if Meta's reported iOS share is > 10 points below the site's iOS share, the gap is material; never exclude iOS based on reported data alone.

**Attribution reality check:** Meta conversions ÷ backend conversions. 1.0-1.3× usable · 1.3-2.0× plan on the stricter (backend) number · > 2.0× or no backend count → don't scale on Meta numbers. A retargeting ROAS many times the account average usually means credit is being claimed, not created.

## 5 · Creative and fatigue

- **Volume:** ≥ 10 distinct creatives live in the account; 5-8 per ad set for standard campaigns, more for Advantage+ Sales. Meta's retrieval system rewards **genuinely different** concepts (different angle, format, person, setting), not 10 versions of one video. At least 3 formats (video, static, carousel/collection) and a 9:16 version of everything.
- **Fatigue statuses (per concept):**

| Status | Rule |
|---|---|
| Winner | CPA ≤ target and CTR within 20% of its own baseline, whatever the frequency |
| Watchlist | 2 of: frequency up ≥ 50%, CTR down ≥ 30%, CPA up ≥ 20% (with CPM within ±15%), or a decline < 7 days old |
| Tired winner | Was at target 14+ days, then all three signals above |
| Replace | Tired for 14+ days → launch new angle (not a re-edit of the same one) |
| Kill | Spent 3× target CPA without ever getting within 20% of target |

  Quick screen when you only have totals: prospecting frequency > 3 (7-day) with CTR down > 20% over 14 days → fatigue risk. CPM rising with steady CTR is the auction, not fatigue.
- **Video metrics:** hook rate (3-s views ÷ impressions): < 25% weak · 25-35% OK · ≥ 35-40% strong. Hold rate (ThruPlays ÷ 3-s views): aim for the account average + 25% on winners. CTR (link) ≥ 1% healthy for prospecting; good hook + poor hold → fix the middle; poor hook → new first 3 seconds; good hook + hold but CTR < 0.65% → weak offer/CTA.
- **Copy (Flexible/Advantage+ creative):** 4 primary texts (≤ 125 characters visible; hooks from different archetypes: relatability, confession, contrast, curiosity, bold claim, imperative) + 3 headlines (≤ 40 characters). Structure: hook → proof → CTA, ≤ 3 emojis. Arabic: dialect per market, see [creative-system.md](creative-system.md).
- **Never pause the top-converting ad of an ad set** to "rotate"; add new ones next to it.
- Creative system, angle matrix, UGC briefs and Arabic copy rules: [creative-system.md](creative-system.md).

## 6 · Budget decisions

| Call | Rule (per campaign/ad set, after the lag window) | Action |
|---|---|---|
| **Scale** | CPA ≥ 15% better than target for ≥ 7 days (14 for high-ticket/long-lag), ≥ 30 conversions, out of learning, no edit in 72 h | +15-20% per step, one change per 72 h; or duplicate into a new CBO/Advantage+ campaign (horizontal) |
| **Hold** | Within ±15% of target, or < 30 conversions | Leave it; add creative |
| **Hold + fix** | 15-25% over target | Keep budget; fix the diagnosed layer (§2) |
| **Reduce** | CPA 25-100% over target with ≥ 30 conversions | −20% and fix the diagnosed layer |
| **Pause** | 3× target CPA spent with 0 conversions, or CPA > 2× target with ≥ 20 conversions | Pause (don't delete) |

- **Rollback:** CPA > 20% over target for 3 days in a row after a change → revert.
- Never scale and restructure at the same time. Never +100% / −50% in one step.
- Budget utilisation ≥ 85% of daily budget; under-delivery means bid/cost caps are too tight or audience too narrow.
- Bid caps/cost caps: never below historical CPA; raise them **before** Ramadan/White Friday when CPMs climb.
- Run `scripts/ads_calc.py verdict ...` for a consistent call.

## 7 · Placements

Give a placement a verdict only with ≥ 5% of spend or ≥ 10 conversions. Test excluding it only if: CPA > 2× account CPA at ≥ 10 conversions (after trying placement-specific creative), or ≥ 10% of spend with 0 conversions, or its share of results < ⅓ of its share of spend across two windows. Audience Network and in-app placements often produce junk leads in the region; watch lead quality, not CPL.

## 8 · Click-to-WhatsApp (CTWA) and Messenger

- Use for high-consideration, high-ticket, trust-sensitive, or local-service offers, and for audiences who prefer chatting to checkout (most of the region).
- Objective: Sales or Leads with conversion location = WhatsApp (or Engagement → conversations while learning). Set up the WhatsApp Business Platform/API with a CRM for volume.
- Pre-filled greeting + 3-4 quick-reply buttons (product, city, size, "talk to an agent").
- **Measure past the conversation:** send `LeadSubmitted` / `Purchase` back via the Conversions API for Business Messaging; report cost per sale, not cost per conversation. Reply time < 5 minutes is part of the funnel; check staffing before scaling.

## 9 · Meta audit checks (feed the scorecard in [audit-checklist.md](audit-checklist.md))

| # | Check | Category | Severity |
|---|---|---|---|
| M-01 | Pixel + CAPI live, dedup verified | Measurement | Critical |
| M-02 | EMQ (Purchase/Lead) ≥ 6 (pass ≥ 8; fail < 4) | Measurement | Critical |
| M-03 | Optimised event = business value (not raw leads / placed COD orders when better events exist) | Measurement | Critical |
| M-04 | Meta conversions 1.0-1.3× backend | Measurement | High |
| M-05 | Domain verified, AEM priorities set, value + currency correct | Measurement | High |
| M-06 | Ad sets ≤ weekly conversions ÷ 50 (no fragmentation); Learning limited < 30% | Structure | High |
| M-07 | Daily budget ≥ 5× target CPA per ad set (fail < 2×) | Structure | High |
| M-08 | Country split; no mixed Egypt + GCC ad sets | Structure | High (MENA) |
| M-09 | Special Ad Category declared where needed | Structure | Critical (if applicable) |
| M-10 | Purchasers / converted leads / refusers excluded from prospecting | Audience | High |
| M-11 | Overlap < 30%; lookalike seeds ≥ 1,000, one country, < 90 days old | Audience | Medium |
| M-12 | ≥ 10 distinct creatives in account; ≥ 3 formats; 9:16 versions | Creative | High |
| M-13 | New concept launched in the last 30 days (fail > 60) | Creative | High |
| M-14 | No fatigued winners left unreplaced (watchlist/tired statuses handled) | Creative | High |
| M-15 | Hook rate ≥ 25% on main videos; CTR (link) ≥ 1% prospecting | Creative | Medium |
| M-16 | Creative in market dialect; RTL QA; price + delivery + payment options shown | Creative | Medium (MENA) |
| M-17 | Prospecting frequency < 3 (warn 3-5), retargeting < 8 | Waste | Medium |
| M-18 | Placements reviewed; no junk-lead placements unchecked | Waste | Medium |
| M-19 | UTMs on every ad; click-to-session gap healthy | Measurement | Medium |
| M-20 | CTWA campaigns measured on sales/qualified leads, not conversations | Measurement | High (if CTWA) |
| M-21 | At least one structured test running (concept or iteration) | Creative | Low |
| M-22 | Bid/cost caps not below historical CPA; budget utilisation ≥ 85% | Structure | Medium |
