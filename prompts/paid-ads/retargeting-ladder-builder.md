---
title: "Retargeting Ladder Builder Prompt — Match the Message to How Warm They Actually Are"
author: "Mahmoud Omar"
author_url: "https://mahmoudomar.com"
category: "paid-ads"
type: "prompt"
level: "intermediate"
works_with: "Claude, ChatGPT, Gemini — output maps to Meta & TikTok audience setups"
language: "EN"
last_verified: "2026-07-02"
hook: "Showing your cart-abandoner the same ad as a cold stranger is like proposing on the first date and the wedding day with the same speech."
email_subject: "The retargeting ladder: one message per warmth level"
short_pitch: "Feed this prompt your funnel and get a complete retargeting ladder: audience tiers by engagement depth, one job per tier, matched message + format + frequency caps — instead of one 'retargeting campaign' blasting everyone."
---

# Retargeting Ladder Builder Prompt

> Build a complete retargeting ladder — audience tiers by engagement depth, each with one job, one message, matched creative format, and sane frequency caps — instead of one catch-all campaign shouting BUY at everyone warm.

## ⚡ What it does

"Retargeting" in most accounts is one audience (everyone-30-days) and one message (the discount). But a video viewer, a product-page visitor, and a cart abandoner have different objections and deserve different arguments. This prompt turns your funnel into a ladder: distinct tiers, the specific belief-job of each, the message that does that job, and the exclusion logic so tiers never overlap-bid against each other.

## 🎯 When I use it (real scenario)

This is the structure I rebuild in every e-com and digital-product account I touch, because the same money leak keeps appearing: one "retargeting" ad set where the cart abandoner who needs a shipping answer gets the same creative as someone who watched three seconds of a Reel. Laddering it — engagers, page visitors, cart, past buyers — with one job per tier is the fix that survives every platform change, because it's audience logic, not platform tricks.

## 📋 The Prompt

```
You are a paid social funnel architect. Build my retargeting ladder.

MY FUNNEL:
- Product + price + purchase consideration time: [impulse / days / weeks]
- Traffic sources feeding the pixel: [X]
- Monthly warm pool size (rough): [site visitors / engagers if known]
- The offer(s) I can use: [discount / bundle / free shipping / content / none]
- Known objections at purchase: [shipping cost, trust, price, "later"...]

BUILD THE LADDER — for EACH tier:
| Tier | Audience definition (platform-ready) | Their ONE objection/job | Message angle | Creative format | Window | Freq cap guidance | Excluded audiences |

TIERS TO COVER (merge tiers only if my warm pool is too small to split):
1. ENGAGERS — video viewers (50%+), post/profile engagers, no site visit yet
   Job: earn the click. Message: value or proof, NOT the offer.
2. BROWSERS — site visitors, no product page. Job: relevance — route to the right thing.
3. PRODUCT VIEWERS — viewed product/offer page, no ATC. Job: kill the product objection
   (proof, comparison, use case).
4. CART/CHECKOUT ABANDONERS — Job: kill the transaction objection (shipping, trust,
   payment). COD markets: "pay on delivery" reminder BEFORE any discount.
5. PAST BUYERS — Job: the next purchase (cross-sell/replenish/upgrade), NEVER the
   acquisition ad. Also: exclude them everywhere else.

THEN:
- EXCLUSION MAP: exact exclusion stack so each user sees only their tier
- BUDGET SPLIT: rough % per tier for my pool size, with reasoning
- LADDER DECAY: how the message changes within a tier over time
  (cart day 1 = reminder, day 3 = objection, day 7 = incentive or let go)
- The 2 tiers to launch FIRST if I can only manage two
```

## 🧠 Pro tips

- Small warm pool? Collapse to two tiers (engaged-not-bought / bought) — a 5-tier ladder on 2,000 visitors just fragments the learning phase.
- The discount belongs at the END of the cart tier's decay, not the start — day-1 discounts train deliberate abandonment (same rule as email recovery).
- Past-buyer exclusion is the highest-ROI five minutes in any account: paying acquisition CPMs to people who already bought is pure leak.
- Sync the ladder with your email flows: if email handles cart recovery days 1-3, let ads take days 3-10 — same argument, different channel, no double-discount.
- Audit what each tier is actually seeing monthly with the [Meta Ads Creative Diagnosis](meta-ads-creative-diagnosis.md) — ladders drift as creatives get swapped.

## 🔗 Related assets

- [Meta Ads Creative Diagnosis](meta-ads-creative-diagnosis.md)
- [Abandoned Cart Recovery Sequence](../email/abandoned-cart-recovery-sequence.md)
- [Ad Angle Matrix](ad-angle-matrix.md)
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
