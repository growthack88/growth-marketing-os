# Ads Audit — scored health check (0-100, A-F)

The `audit` command. It produces a health score you can track month over month, a list of findings ranked by money at stake, and a 30-day fix plan. Scoring method adapted from [claude-ads](https://github.com/AgriciDaniel/claude-ads) (MIT); the MENA checks are original. See [CREDITS.md](../CREDITS.md).

---

## 1 · Process

1. **Intake** (SKILL.md Step 0). Confirm the business model, markets, target, and date range (default: last 30 days vs previous 30).
2. **Tracking first.** Run the [tracking checks](tracking-measurement.md). If Purchase/Lead counts are off by > 20% vs the backend, say so on line one: every number after that is provisional.
3. **Score each platform** with its check list: [meta.md](meta.md) · [google.md](google.md#7--google-audit-checks-feed-the-scorecard-in-audit-checklistmd) · [tiktok.md](tiktok.md) · [snapchat.md](snapchat.md#6--snapchat-audit-checks-feed-into-the-main-audit-scorecard) · [other-platforms.md](other-platforms.md), plus the cross-platform and MENA checks below.
4. **Quantify waste** in money (spend on Q4/Q5 search terms, fatigued ads, wrong placements, out-of-market clicks, past-buyer prospecting, junk leads).
5. **Write the report** in the format in §5.

## 2 · Scoring

Each check gets: **Pass** (1) · **Warning** (0.5) · **Fail** (0) · **Unknown** (no data, excluded from the score but counted in coverage) · **N/A** (excluded).

Severity weights: **Critical 5 · High 3 · Medium 1.5 · Low 0.5**.

```
Category score  = 100 × Σ(result × severity) ÷ Σ(severity of known checks)
Platform score  = Σ(category score × category weight) ÷ 100
Coverage        = known checks' severity ÷ all applicable checks' severity
Account score   = platform scores weighted by each platform's share of spend
```

**Category weights (sum to 100):**

| Platform | Measurement | Structure/Bidding | Audience/Keywords | Creative | Waste/Settings |
|---|---|---|---|---|---|
| Meta | 30 | 20 | 15 | 30 | 5 |
| Google | 25 | 15 | 15 | 15 | 30 (waste 20 + settings 10) |
| TikTok | 25 | 20 | 10 | 35 | 10 |
| Snapchat | 25 | 20 | 10 | 35 | 10 |
| LinkedIn | 25 | 15 | 30 | 20 | 10 |

**Grades:** A 90-100 · B 75-89 · C 60-74 · D 40-59 · F < 40.

**Coverage rule:** coverage ≥ 80% → graded. 60-79% → "provisional grade". < 60% → no grade; report findings plus the data needed to finish. Never score missing data as a fail; mark it Unknown and ask for it.

## 3 · Cross-platform checks (apply to every account)

| # | Check | Severity |
|---|---|---|
| X1 | Optimisation event = business outcome (delivered/confirmed order for COD, purchase for prepaid, qualified lead for lead-gen) | Critical |
| X2 | Platform conversions within ±20% of backend for the same period | Critical |
| X3 | Server-side tracking (CAPI / Events API / Enhanced Conversions) live and deduplicated | Critical |
| X4 | Conversion value and currency correct | Critical |
| X5 | UTMs on every ad; backend can attribute orders to campaigns | High |
| X6 | Target CPA/ROAS defined and grounded in unit economics (break-even computed) | High |
| X7 | Blended MER tracked (total revenue ÷ total ad spend) alongside platform ROAS | Medium |
| X8 | Past buyers / existing leads excluded from prospecting | High |
| X9 | Landing page: loads < 3 s on mobile, message matches the ad, price + delivery + payment options visible | High |
| X10 | Naming convention consistent and readable | Low |
| X11 | Testing roadmap exists (what's being tested this month and why) | Medium |
| X12 | ~70/20/10 budget split (proven / scaling / experiments) or a stated alternative | Medium |

## 4 · MENA checks (apply when any Arab market is targeted)

| # | Check | Severity |
|---|---|---|
| M1 | Campaigns split by country (no blended "MENA/GCC" ad sets mixing Egypt with the Gulf) | High |
| M2 | Creative in the market's dialect (Egyptian / Gulf / Levantine / Darija), RTL rendering QA'd | High |
| M3 | COD: confirmation and delivery rates tracked per campaign; real ROAS reported | Critical (COD) |
| M4 | COD: confirmed/delivered events sent back server-side; refusers excluded; delivered buyers seed lookalikes | High (COD) |
| M5 | Snapchat in the plan for KSA/GCC consumer brands (or a stated reason it isn't) | Medium |
| M6 | Click-to-WhatsApp measured past "conversations" (sales or qualified leads sent back) | High (if CTWA) |
| M7 | Seasonal calendar loaded for the next 60 days (Ramadan, Eid, White Friday, national days) | Medium |
| M8 | Price in local currency, VAT stated where required, delivery time and payment options (BNPL/COD/Apple Pay) in ads or landing page | Medium |
| M9 | Regulated categories compliant (health claims, finance, real estate special category, influencer licences: Mawthooq / UAE Media Council) | Critical (if applicable) |
| M10 | Google: Arabic + English language targeting and Arabic spelling variants covered | High (if Google) |
| M11 | Ad account billing stable (no failed-payment pauses in 30 days; backup payment method) | Medium |
| M12 | GCC expat segments treated as separate audiences with their own creative where relevant | Low |

## 5 · Report format

```
# Ads Audit: [Brand] · [Markets] · [Date range]

Health: [score]/100 ([grade]) · Coverage: [x]% · Monthly spend: [amount, currency]
One-line verdict: [the single biggest problem and what it costs]

## Scorecard
| Platform | Score | Grade | Share of spend | Biggest issue |

## Top findings (ranked by money at stake)
| # | Finding | Evidence (numbers) | Est. monthly impact | Fix | Effort |

## Waste found
[itemised, with amounts]

## 30-day plan
⚡ Week 1 (do today): ...
🧪 Weeks 2-3 (tests, with hypothesis + success metric): ...
🛑 Stop / reduce: ...
📈 Week 4: scale what passed, re-score.

## What I couldn't check (data needed)
```

Write the report in the user's language. In Arabic reports, keep metric names in English (ROAS, CPA, CTR) and numbers in Western digits unless the client prefers Arabic-Indic digits.
