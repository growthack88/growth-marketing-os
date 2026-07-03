---
title: "Referral Program Designer Prompt — Loops Built on Moments, Not Wishful Math"
author: "Mahmoud Omar"
author_url: "https://mahmoudomar.com"
category: "growth"
type: "prompt"
level: "advanced"
works_with: "Claude, ChatGPT, Gemini"
language: "EN"
last_verified: "2026-07-03"
hook: "Every founder wants 'a Dropbox referral program'. Dropbox's viral coefficient peaked around 0.5 — even the legend didn't do what the legend says."
email_subject: "Design a referral program on real math (not the Dropbox myth)"
short_pitch: "Feed this prompt your product and get a complete referral program design: the trigger moment, two-sided incentive matched to your unit economics, fraud guards, and honest projections — with the viral-coefficient math done truthfully."
---

# Referral Program Designer Prompt

> Design a referral program as an engineered loop: the moment worth asking at, incentives priced against your real unit economics, fraud guards from day one — and projections computed honestly, because sustained K>1 virality is essentially a myth.

## ⚡ What it does

Referral programs fail in two standard ways: bolted-on (a "refer a friend" link in the footer, asked of everyone at no particular moment) and over-promised (modeled at viral coefficients no product sustains). This prompt designs the real thing — trigger moment, incentive structure, delivery mechanics, fraud economics — and forces the projection math to use published reality: referred customers are worth more (+16% LTV, 18% lower churn per the canonical Wharton study), but referral is an amplifier on retention, not a substitute for acquisition.

## 🎯 When I use it (real scenario)

Referral comes up in every growth-model conversation (it's the loop everyone wants in the [Growth Strategist](../../agents/growth-strategist-agent.md) sessions), and the design questions are always the same three: WHEN do we ask (the moment of maximum delivered value, never signup), WHAT do we pay (both sides, priced against margin, in product-currency where possible), and HOW does it not get gamed (COD markets and coupon communities find every hole). This prompt is those three questions industrialized, with the fantasy-math firewall built in.

## 📋 The Prompt

```
You are a growth engineer designing a referral program. Design the LOOP, then check the MATH, then break your own design as a fraud analyst.

MY PRODUCT:
- What it is + price/AOV + gross margin: [X]
- The moment users experience clear value (be specific — an event, not a vibe): [X]
- Current retention/repeat behavior: [X]
- Payment context: [prepaid / COD / subscription] · Market: [X]
- What I can afford to give away per acquired customer (my current CAC for reference): [X]

DESIGN:

1. THE TRIGGER MOMENT
   Pick the exact event to ask after (first result achieved / delivery confirmed &
   product loved / milestone hit). Justify it. Add one secondary moment.
   Rule: never at signup, never at checkout — nobody refers before value lands.

2. INCENTIVE ARCHITECTURE (two-sided by default)
   - Referrer reward + new-user reward, each: what, when paid, and WHY this currency
     (product credit > cash for retention; cash > credit for low-frequency purchases).
   - Price it: both rewards together must cost meaningfully less than my CAC,
     after expected fraud/breakage. Show the math.
   - The ASK copy: 2 versions of the referral message the USER sends (the real ad
     is their message, not my UI) — natural, screenshot-able, in [language].

3. MECHANICS
   Share mechanism fitted to my market (link / code / WhatsApp-first for MENA),
   reward delivery timing (after the referred user's QUALIFYING event, not signup),
   and the qualifying event definition (for COD: delivered & paid, NOT ordered).

4. FRAUD & ABUSE PASS (attack your own design)
   Self-referral, disposable emails/numbers, coupon-site leakage, COD fake orders,
   reward farming. For each: the guard, and what the guard costs in honest-user friction.

5. HONEST PROJECTIONS
   Compute with participation and conversion assumptions LABELED as assumptions:
   - % of active users who share (single digits is normal), invites per sharer,
     invite→customer conversion → implied K factor.
   - State plainly: if K < 1 (it will be), referral is a CAC-reducing amplifier,
     not an engine. Project it as % of new customers (10-30% at maturity is a
     strong program), never as exponential growth.
   Context anchors: referred customers show +16% LTV and 18% lower churn
   (Wharton/Van den Bulte study); Dropbox at PEAK ran ~35% of signups from
   referrals with K≈0.35-0.7 — that's the ceiling story, not the base case.

6. THE MVP TEST
   Smallest honest version (manual codes + spreadsheet is fine), the 2 metrics
   that decide (sharer participation rate first — if <2% share, fix the moment
   or the product before touching the reward), and the 30-day decision rule.
```

## 🧠 Pro tips

- Participation rate is the diagnostic, not conversion: low sharing = the product moment isn't worth talking about yet — a bigger reward can't fix pride that isn't there.
- Product-credit rewards quietly double as retention: a user holding 200 EGP of credit comes back. Cash rewards leak; credit compounds.
- COD markets: qualify rewards on *delivered* orders and cap monthly redemptions per account — the fraud pass isn't paranoia, it's arithmetic (see the [COD Profit Funnel](../../frameworks/cod-profit-funnel.md) on what fake orders cost).
- WhatsApp-first sharing in MENA: pre-filled message beats share-link-to-nowhere; write the message in عامية and make it something a person would actually forward ([CTA bank #20](../../swipe-files/ctas/arabic-cta-bank.md) energy).
- Treat the program as an experiment with a kill rule ([Experiment Designer](growth-experiment-designer.md)) — a referral program that pays out without moving CAC-blended math is a loyalty discount wearing a growth costume.

## 🔗 Related assets

- [Growth Experiment Designer](growth-experiment-designer.md)
- [Growth & SaaS Benchmarks](../../benchmarks/growth-saas-benchmarks.md)
- [The COD Profit Funnel](../../frameworks/cod-profit-funnel.md)
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
