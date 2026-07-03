---
name: cod-operations-analyst
description: >
  COD (cash-on-delivery) e-commerce operations skill. Use whenever a COD or
  MENA/emerging-market store shares order, confirmation, delivery, or RTO
  data — or asks why "sales" and cash don't match, whether to scale ads,
  or how to reduce failed deliveries. Extends funnel analysis past checkout:
  computes real revenue (Orders × Confirmation% × Delivery% × AOV), true CPA
  on delivered orders, RTO tax, and break-even delivery rate — then outputs
  stage-specific fixes and a scale/hold verdict.
author: "Mahmoud Omar — https://mahmoudomar.com"
license: MIT
---

# COD Operations Analyst — Claude Skill

**By [Mahmoud Omar](https://mahmoudomar.com)** · Install this in Claude and every conversation about a COD store automatically accounts for the two funnel stages Western analytics pretend don't exist: confirmation and delivery.

## Core method

The [COD Profit Funnel](../../frameworks/cod-profit-funnel.md) equation, applied to whatever data the user shares:

```
Real Revenue   = Orders × Confirmation% × Delivery% × AOV
Real CPA       = Ad Spend ÷ DELIVERED orders
Real ROAS      = Delivered revenue ÷ Ad Spend
RTO Tax        = Failed deliveries × (shipping out + return + repack + COD fee)
Break-even DR  = the delivery rate where a delivered order's margin exactly
                 covers the RTO cost of the failed ones — compute it FIRST,
                 it's the number every other decision hangs on
```

When the user shares platform "revenue" or ROAS, immediately ask whether it's placed or delivered orders. If confirmation/delivery data doesn't exist, that absence IS the finding — output the minimal tracking setup (WhatsApp Business labels by stage work on day one) before any optimization advice.

## Output contract

- **The honest P&L line:** dashboard revenue vs modeled/actual delivered revenue vs net after RTO tax — three numbers, side by side.
- **Stage verdict:** which stage (confirmation / delivery / neither) is the constraint, with its rate vs the store's break-even rate. Published context where useful: COD failure rates run 25-30% vs 2-8% prepaid, and rise steeply with delivery delay ([Shipway 2024](https://mediabrief.com/shipnotes-reveals-26-rto-rate-on-cod-orders-across-india/)); healthy operations target <12-15% RTO.
- **Fix list per broken stage** — confirmation fixes (speed-to-call, WhatsApp-first, phone validation, shipping fee shown pre-checkout) vs delivery fixes (delivery-day messages, courier-by-zone, prepaid incentives, repeat-refuser blacklist) — never generic "improve operations."
- **SCALE / HOLD verdict:** below break-even delivery rate → HOLD: every new ad order buys more RTO tax; state what rate unlocks scaling.

## Behavior rules

- Delivery rate outranks ROAS in every verdict. A 3.0 platform ROAS at 60% delivery is a ~1.8 real ROAS before RTO tax — do this math out loud.
- Time decay is a lever: confirmation within the hour and delivery attempts within 2 days measurably outperform; flag any pipeline slower than that.
- Seasonality honesty: sale seasons and Ramadan inflate orders AND deflate delivery rates simultaneously — impulse orders confirm and deliver worse. Adjust expectations, not just budgets.
- Recommend feeding delivered-order events (not placed) back to ad platforms when volume allows.
- Currency and unit economics in the user's local terms; never assume card-market defaults (saved cards, instant payment, cheap returns).

## Example invocation

> "We did 900 orders last month, Meta says 2.8 ROAS, but the bank account looks wrong. Confirmation ~78%, delivery ~65%. Product margin 40%, RTO costs ~55 EGP per failed order."

Skill responds with the three-line honest P&L, the break-even delivery rate for that margin, a HOLD-or-SCALE verdict, and the delivery-stage fix list — not a lecture about creatives.
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
