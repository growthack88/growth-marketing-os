---
title: "SaaS & Growth Benchmarks 2026 — Trial Conversion, Activation, Churn, NRR & Unit Economics (Sourced)"
author: "Mahmoud Omar"
author_url: "https://mahmoudomar.com"
category: "growth"
type: "benchmark"
level: "intermediate"
works_with: "Any SaaS / subscription / digital product — reference data for planning & audits"
language: "EN"
last_verified: "2026-07-03"
hook: "Your conversion rate isn't 'bad'. It's bad FOR YOUR MODEL — an opt-in trial at 5% is healthy, a credit-card trial at 5% is a fire."
email_subject: "The SaaS benchmarks that actually have sources (2026 edition)"
short_pitch: "Sourced 2024-2026 SaaS benchmarks in one file: trial→paid by model, activation, churn by segment, NRR, CAC payback, LTV:CAC — every number cited (Growth Unhinged, RevenueCat, ChartMogul, SaaS Capital), every gap admitted."
---

# SaaS & Growth Benchmarks (2026, Sourced)

> Reference benchmarks for SaaS and subscription growth — trial conversion by model, activation, churn by segment, NRR, and unit economics. Every figure carries its source and year; where no reliable public data exists, it says so instead of making one up.

## ⚡ What it does

Half the "benchmarks" quoted in growth meetings are folklore — a number someone saw in a thread, detached from its model, segment, and year. This file is the antidote: the current sourced numbers, organized by the question you're actually asking ("is my trial conversion normal FOR MY MODEL?"), with data-quality flags so you know which figures are billing-data solid and which are survey-soft.

## 🎯 When I use it (real scenario)

Benchmarks enter my work at exactly two moments: triage (is this metric the bottleneck, or does it just feel bad?) and target-setting sanity checks (is the goal ambitious or delusional?). The rule I hold clients to, and the rule for using this file: **a benchmark is a threshold for attention, never a target** — chasing someone else's median with your funnel's context is how teams optimize the wrong thing confidently. Feed these to the [Growth Strategist Agent](../agents/growth-strategist-agent.md) as knowledge and it stops hallucinating its own.

## 📋 The Benchmarks

### 1 · Free → Paid Conversion (by model — the model IS the benchmark)

Primary source: **Growth Unhinged "Free-to-Paid Conversion Report" (Kyle Poyar, Jan 2026** — 200 B2B self-serve products, ChartMogul + ProductLed data partners). [Source](https://www.growthunhinged.com/p/free-to-paid-conversion-report)

| Model | GOOD | GREAT |
|---|---|---|
| Freemium (self-serve) | 3–5% | 8–12% |
| Free trial, opt-in (no card) | 4–6% | 10–15% |
| Free trial, opt-out (card required) | 25–35% | 50–60% |
| Reverse trial | 4–6% | 8–12% ⚠️ small subsample (~14 products) — treat as directional |
| AI-native / hybrid | 6–8% | 15–20% |
| Overall median, all models | 8% | — |

Supporting (ChartMogul billing data, 2026): opt-in trials avg **8.9%**, card-required trials avg **31.4%**. Context stats: 57% of self-serve B2B leads with a free trial, only 20% of trials require a card, 62% run 14 days. ([Growth Unhinged, 2026](https://www.growthunhinged.com/p/free-to-paid-conversion-report))

Consumer apps (**RevenueCat State of Subscription Apps 2025** — real transactions, 115k+ apps): hard paywall median download→paid **12.1%** vs freemium **2.2%**; 17–32-day trials convert **45.7%** trial→paid vs **25.5%** for <4-day trials. ([Source](https://www.revenuecat.com/state-of-subscription-apps-2025/))

### 2 · Activation & Early Retention

| Metric | Value | Source / Year |
|---|---|---|
| Avg SaaS activation rate (aha/setup moment) | 36% avg, 30% median | [Lenny Rachitsky + Yuriy Timen survey, 500+ products, 2022](https://www.lennysnewsletter.com/p/what-is-a-good-activation-rate) ⚠️ pre-AI-era vintage |
| B2B enterprise activation: median / good / great | 33% / 40% / 65% | same |
| Avg week-1 retention (active usage, all signups) | 28% (fell ~50% YoY) | [Mixpanel Benchmarks Report 2024](https://mixpanel.com/blog/2024-mixpanel-benchmarks-report/) (7,700 companies) |
| Day-7 retention, top-25% products | ≥7% | [Amplitude Product Benchmark Report 2025](https://info.amplitude.com/rs/138-CDN-550/images/the-product-benchmark-report.pdf) (2,600+ companies) |
| D7 → long-term link | 69% of top D7 performers are also top 3-month performers | Amplitude, 2025 |

⚠️ Definitions differ: Mixpanel/Amplitude "retention" = active usage of ALL signups (single digits–28%); Lenny "activation" = % reaching a defined aha moment (~30-36%). Never compare across the two.

### 3 · Churn & NRR (by segment — segment first, then judge)

| Metric | Value | Source / Year |
|---|---|---|
| Median NRR: Enterprise / Mid-market / SMB | ~118% / 108% / 97% | [SaaS Capital Retention Survey 2025](https://www.saas-capital.com/blog-posts/what-is-a-good-retention-rate-for-a-private-saas-company/) |
| Median GRR, private B2B SaaS | ~88% | [Benchmarkit 2025](https://www.benchmarkit.ai/2025benchmarks) |
| Monthly logo churn, ARPA <$25/mo | 6.1% median | [ChartMogul billing data](https://chartmogul.com/saas-metrics/customer-churn/) |
| Monthly logo churn, ARPA >$500/mo | 2.2% median | same |
| Best-in-class target | <2%/mo (<1% at high ARPA) | same |
| Consumer apps monthly churn (low/mid/high price) | 1.4% / 2.0% / 2.8% median | [RevenueCat 2026](https://www.revenuecat.com/state-of-subscription-apps/) |
| Consumer Year-1 retention: monthly plans | 12–23% by price tier | RevenueCat 2025 |
| Consumer Year-1 retention: annual plans | 48–54%; ~27-28% renew into year 2 | RevenueCat 2025/2026 |
| Annual subscribers canceling within first month | 30% | RevenueCat 2025 |

### 4 · Unit Economics

| Metric | Value | Source / Year |
|---|---|---|
| Median CAC payback | 18 months (2024, up from 14) | [Benchmarkit 2025](https://www.benchmarkit.ai/2025benchmarks) |
| CAC payback by ACV: <$5K / $50–100K | ~11 mo / ~22 mo | same |
| Median LTV:CAC | 3.6:1 | same |
| Top-quartile LTV:CAC | 4:1–6:1, payback <12 mo | [Bessemer State of the Cloud 2026 (via SaaS Hero)](https://www.saashero.net/strategy/b2b-saas-ltv-cac-benchmarks/) |
| Rule of 40: public SaaS median | 28% (only ~20% clear 40) | [Aleph public-SaaS analysis, Q4 2025](https://www.getaleph.com/answers/rule-of-40-saas-2026) |
| Median ARR growth $1–5M B2B SaaS vs AI-native | 40% vs 110% | [High Alpha 2025 SaaS Benchmarks](https://www.highalpha.com/saas-benchmarks) |

### 5 · Pricing Mix & Discounts

| Metric | Value | Source / Year |
|---|---|---|
| Annual-plan share of ARR (≥$1K ARPA segment) | 55% annual / 34% monthly | [ChartMogul SaaS Billing Report](https://chartmogul.com/reports/saas-billing-report/) |
| NRR gap, annual vs monthly plans | +10–20pp for annual | same |
| Discount-acquired customers | ~32.4% lower LTV, higher churn | [ProfitWell/Paddle study, 6,000+ companies](https://www.paddle.com/blog/saas-discounting-strategy) |
| Consumer plan mix by category | health/fitness 68% annual; productivity 77% monthly | RevenueCat 2026 |

### 6 · Honest gaps (no reliable public benchmark found)

- Median referral-program share of signups, 2024-2026 (vendor content still recycles Dropbox 2010 and the Wharton 2011 study — referred customers +16% LTV, 18% lower churn — with no modern large-sample replication)
- Lifetime-deal cohort economics (LTV, support cost per LTD user) — AppSumo publishes no aggregates; independent analysis of 770+ deals suggests ~$5,900 avg gross per deal ([Pirciu, Medium](https://medium.com/@danielpirciu/how-much-revenue-an-appsumo-deal-is-making-d7281b6d0ed3)), platform reported under pressure ([PPC Land](https://ppc.land/appsumos-revenue-crashes-50-as-lifetime-deal-model-faces-existential-crisis/))
- Sustained viral coefficient K>1 — essentially unheard of in SaaS; Dropbox peaked at K≈0.35–0.7

## 🧠 How to use benchmarks (the part everyone skips)

- **Threshold, not target.** Below "good" → investigate that stage; above it → your bottleneck is elsewhere. Never make "reach the median" a roadmap item.
- **Match the model before the number.** The single most common benchmark abuse: judging an opt-in trial against opt-out numbers (a 6x definitional difference).
- **Billing data > surveys.** RevenueCat/ChartMogul figures come from real transactions; survey medians (High Alpha, SaaS Capital) skew toward healthier companies that bother responding.
- **Check the vintage.** Activation benchmarks are 2022-era; AI-native products are re-basing every curve (110% vs 40% median growth).
- Feed this file to your [Growth Strategist GPT](../gpts/growth-strategist-gpt.md) as a knowledge file — labeled proxies beat hallucinated ones.

## 🔗 Related assets

- [Growth Strategist Agent](../agents/growth-strategist-agent.md)
- [Growth Experiment Designer](../prompts/growth/growth-experiment-designer.md)
- [Lifetime Deal Launch Playbook](../playbooks/lifetime-deal-launch-playbook.md)
<!-- MO-BRAND-FOOTER v1 — paste at the bottom of every asset file -->

---

## 🦆 Built by Mahmoud Omar

**Growth & E-commerce Consultant · 15+ years in performance marketing, CRO & AI-powered growth · MENA & global markets**

| Asset | Link |
|---|---|
| 🌍 Personal Site | [mahmoudomar.com](https://mahmoudomar.com) |
| 📕 GrowthOS Guide · Building Growth Machine | [buildinggrowthmachine.com](https://buildinggrowthmachine.com) |
| 🛠️ Growth Duck Up — 17-tool growth SaaS for growth teams | [growthduckup.com](https://growthduckup.com) |
| 🎓 Growth Hack Academy | [growthhackacademy.com](https://growthhackacademy.com) |
| 🚀 StartupKit Pro — Startup OS for MENA founders | [startupkit.pro](https://startupkit.pro) |
| 🍅 DuckDoro — calm productivity app | [duckdoro.com](https://duckdoro.com) |
| 🎥 YouTube (40K+ marketers) | [Subscribe → Growth Hack Academy](https://www.youtube.com/@GrowthHackAcademy?sub_confirmation=1) |

⭐ **Saved you time? [Star the repo](https://github.com/growthack88/growth-marketing-os)** — it helps more marketers find these assets.

> All assets are original work by [Mahmoud Omar](https://mahmoudomar.com), battle-tested on real accounts. Free to use with attribution. Not AI-generated filler.
