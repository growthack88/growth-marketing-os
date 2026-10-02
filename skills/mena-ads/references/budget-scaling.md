# Budget, Scaling & Diagnosis — the decision rules

Load for `plan`, `optimize` and `diagnose`. These rules are practitioner heuristics distilled from the projects in [CREDITS.md](../CREDITS.md) and adapted for MENA economics. The account's own history beats them; recalibrate after 90 days.

---

## 1 · Start from economics, not from a budget

1. **Break-even first.** `Break-even ROAS = 1 ÷ contribution margin %` (for COD, use the delivered-order version):
   `python3 scripts/ads_calc.py breakeven --price P --cogs C --shipping S --fees F --confirm C% --deliver D% --return-cost R`
2. **Target = break-even with a margin buffer.** Default working target CPA = break-even CPA ÷ 1.2 (the calculator prints it). Profitable: ROAS ≥ 1.2× break-even · marginal: 1.0-1.2× · losing: < 1.0×. If cost data is missing, print the break-even ROAS formula rather than inventing a margin.
3. **Budget must let each ad set/ad group learn** (~50 optimisation events/week; Google tCPA ~30/month). If it can't, consolidate or optimise for a higher-volume event. Don't split a small budget across five platforms.
4. **VAT:** state whether budgets and targets include VAT (`ads_calc.py vat`).

## 2 · Allocation

**Monthly split of a stable account:** ~70% proven campaigns · ~20% scaling/iteration of winners · ~10% experiments (new platform, angle, audience). New accounts lean the other way: weeks 1-4 ≈ 40/40/20, weeks 5-8 ≈ 60/25/15, then 70/20/10.

**Platform selection by goal and market** (starting hypotheses; `ads_calc.py split` prints them):

| Goal | Egypt | KSA | UAE | Smaller GCC |
|---|---|---|---|---|
| E-com sales | Meta-led + TikTok + Google | Meta + Snapchat + TikTok + Google | Meta + Google (PMax/Shopping) + TikTok | Meta/Instagram + Snapchat + Google |
| Lead-gen | Meta (forms/CTWA) + Google | Google + Meta + Snapchat | Google + Meta (+ LinkedIn if B2B) | Google + Meta |
| B2B | LinkedIn + Google + Meta retargeting | same | same | same |
| App | Meta + Google App + TikTok | + Snapchat + Apple Search Ads | + Apple Search Ads | + Snapchat |

**Minimum sensible monthly test per new platform:** enough for ~50 conversions on the platform's optimisation event in the first month, or the platform's practical floor (roughly: Meta/TikTok/Snapchat a few hundred USD-equivalent, Google Search ~$1k, LinkedIn ~$2-3k). Below that, test on a higher-funnel event or skip the platform.

**Funnel split (prospecting / consideration / conversion):** ~30/25/45 for sales and lead-gen, more top-funnel for awareness or new brands, adjusted for warm-pool size (small warm pools → less retargeting).

**Re-weight every 2-4 weeks toward the best marginal real CPA** (the cost of the *next* conversion, not the average). Never re-weight by CPM or CTR.

## 3 · Scale / hold / reduce / pause

Per campaign or ad set, after the conversion-lag window, compared to target CPA (or ROAS):

| Call | Rule | Action |
|---|---|---|
| **Not enough data** | < 3× target CPA spent or < 10 conversions | Wait; don't edit |
| **Scale** | ≥ 15% better than target for ≥ 7 days (14 is safer for high-ticket/long-lag offers), ≥ 30 conversions, out of learning, no edit in 72 h | +15-20% per step, one step per 72 h (vertical); or duplicate into a new campaign (horizontal); or open a new geo/audience |
| **Hold** | Within ±15% of target | Keep spending; add creative/angles |
| **Hold + fix** | 15-25% over target | Keep the budget; fix the weakest layer (§4); re-check in 3-5 days |
| **Reduce / fix** | 25-100% over target with ≥ 30 conversions | −20%; diagnose the funnel layer (§4) before cutting further |
| **Pause** | 3× target CPA spent with 0 conversions, or > 2× target with ≥ 20 conversions | Pause; never delete |

Guardrails:
- **Rollback:** CPA > 20% over target for 3 consecutive days after a change → revert.
- One change at a time per campaign (not bids + budget + creative together).
- Never +100% or −50% in one step. Expect a short CPA bump after any increase; judge after 3-5 days.
- **Saturation signals** (time to expand horizontally, not vertically): Google impression share > 80%; Meta 7-day prospecting frequency > 3-4; TikTok/Snap frequency > 3; small GCC markets reach saturation first.
- Google-specific scaling (budget vs rank pressure, PMax caps): [google.md](google.md).
- `python3 scripts/ads_calc.py verdict --spend S --conversions N --target-cpa T --days D [--frequency F --ctr-drop X]` returns the same call.

## 4 · Diagnosis: "why did results drop?"

Work top-down, one layer at a time, with numbers for the current vs previous period:

| Layer | Metric | If broken, likely cause |
|---|---|---|
| 0 · Signal | Platform vs backend conversions; recent tracking/site changes | Tracking broke → fix before anything else |
| 1 · Delivery/auction | Spend, CPM, impression share | Season (Ramadan, White Friday), competitors, budget/bid caps, payment failures, policy rejections |
| 2 · Attention | Hook rate, CTR | Creative fatigue, weak angle, wrong audience |
| 3 · Click quality | CPC, LPV ÷ clicks, bounce, sessions | Slow page, broken redirect, accidental clicks (placements) |
| 4 · Conversion | CVR, AOV, checkout drop-off | Offer, price, stock, shipping fee surprise, payment options, form friction |
| 5 · Post-conversion (MENA) | Confirmation %, delivery %, lead qualification % | COD operations, junk leads, call-centre speed |
| 6 · Measurement window | Conversion lag, attribution window | Data not in yet; window changed |

Rules:
- **Find the first broken layer and stop.** Fixing layer 4 when layer 1 broke wastes a week.
- Separate **auction** (CPM up, CTR steady) from **fatigue** (CTR down, CPM steady, frequency up) from **landing page** (CTR steady, CVR down). They need different fixes.
- Check the **calendar** (Ramadan, Eid, salary week, national days, summer travel) and **the change log** before blaming the algorithm.
- Output: hypothesis table (cause · evidence · likelihood · test) → most likely cause → ranked fixes → expected recovery time (as an estimate).

## 5 · Weekly operating rhythm (60 minutes)

1. Backend vs platform reconciliation (10 min) — COD: confirmation + delivery rates.
2. Spend pacing vs plan; payment issues; rejected ads (5 min).
3. Run scale/hold/reduce/pause on every ad set/campaign with enough data (15 min).
4. Fatigue scan: frequency, CTR trend, hook rate by concept (10 min).
5. Google search terms + negatives (10 min).
6. Launch the week's creative tests; log hypotheses (5 min).
7. Write the 5-line update (5 min): what changed, why, what we're doing, what needs approval, what we're deliberately not changing yet.
