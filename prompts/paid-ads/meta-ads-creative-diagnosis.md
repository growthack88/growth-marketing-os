---
title: "Meta Ads Creative Diagnosis Prompt — Find Why Your Ads Stopped Converting"
author: "Mahmoud Omar"
author_url: "https://mahmoudomar.com"
category: "paid-ads"
type: "prompt"
level: "intermediate"
works_with: "Claude, ChatGPT, Gemini"
language: "EN"
last_verified: "2026-07-02"
hook: "Your ad isn't fatigued. Your diagnosis is lazy."
email_subject: "The 5-minute prompt that saved a $12K/mo ad account"
short_pitch: "Paste your Meta ads metrics into this prompt and get a layer-by-layer diagnosis: creative vs. audience vs. offer vs. landing page — with a fix priority list."
---

# Meta Ads Creative Diagnosis Prompt

> Paste your ad metrics + creative description and get a structured diagnosis of exactly which layer is broken — hook, creative, audience, offer, or landing page — with a prioritized fix list.

## ⚡ What it does

Most media buyers see ROAS drop and immediately swap creatives. Wrong move 60% of the time. This prompt forces the AI to decompose performance layer by layer (CTR → CPC → LP view rate → ATC → purchase) and tell you WHERE the leak actually is before you touch anything.

## 🎯 When I use it (real scenario)

E-com account, GCC market, ROAS fell from 3.1 to 1.7 in 10 days. Team wanted new creatives. Ran this diagnosis: CTR was stable, hook was fine — checkout conversion had collapsed after a shipping-fee change. New creatives would have burned two weeks and $4K for nothing. Fixed the offer layer, ROAS back to 2.8 in one week.

## 📋 The Prompt

```
You are a senior Meta Ads performance analyst. Diagnose my campaign using funnel decomposition — do NOT jump to conclusions.

MY DATA (last 14 days vs previous 14 days):
- Spend: [X] vs [X]
- Impressions: [X] vs [X]
- CTR (link): [X]% vs [X]%
- CPC: [X] vs [X]
- Landing page views / clicks ratio: [X]% vs [X]%
- Add to cart: [X] vs [X]
- Purchases: [X] vs [X]
- ROAS: [X] vs [X]
- Frequency: [X] vs [X]
- Creative: [describe format, hook, offer shown]
- Recent changes: [pricing, LP, shipping, targeting, budget changes]

ANALYZE IN THIS ORDER:
1. ATTENTION LAYER: Is CTR/hook the problem? (compare CTR + frequency trends)
2. TRAFFIC QUALITY LAYER: Is the click-to-LP-view ratio degrading? (technical/speed/audience issue)
3. INTEREST LAYER: LP view → ATC. (offer-message match problem)
4. CONVERSION LAYER: ATC → Purchase. (pricing, shipping, checkout friction)
5. SATURATION LAYER: frequency + CPM trends. (audience fatigue vs auction pressure)

OUTPUT FORMAT:
- Primary broken layer + confidence level
- Evidence for that conclusion
- What is NOT the problem (so I don't waste money fixing it)
- Top 3 fixes ranked by expected impact vs effort
- One test to validate the diagnosis in 72 hours
```

## 🧠 Pro tips

- Feed it 14-day windows minimum — 3-day windows produce noise, not diagnosis.
- If frequency > 4 AND CTR dropped > 25%, only then is it actually creative fatigue.
- Run it monthly even when things are fine — you'll build a baseline the AI can compare against.
- Works identically for TikTok Ads — just rename the metrics.

## 🔗 Related assets

- [Funnel Decomposition Skill](../../skills/funnel-decomposition/SKILL.md)
- [Bilingual Hook Bank](../../swipe-files/hooks/bilingual-hook-bank.md)
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
