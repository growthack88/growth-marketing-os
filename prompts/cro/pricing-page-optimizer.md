---
title: "Pricing Page Optimizer Prompt — Plans, Anchors, Decoys & the Toggle, Audited"
author: "Mahmoud Omar"
author_url: "https://mahmoudomar.com"
category: "cro"
type: "prompt"
level: "advanced"
works_with: "Claude, ChatGPT, Gemini"
language: "EN"
last_verified: "2026-07-03"
hook: "Your pricing page isn't a menu. It's an argument about which plan to buy — and most pages argue for the wrong one."
email_subject: "The pricing-page audit: anchors, decoys, and the annual toggle"
short_pitch: "Paste your pricing page into this prompt and get a structural audit: plan architecture, anchoring and decoy logic, the annual/monthly toggle, feature-table readability, and enterprise-CTA placement — with the one test to run first."
---

# Pricing Page Optimizer Prompt

> A structural audit for pricing pages: whether the plan lineup steers anyone anywhere, whether the anchor and decoy do their jobs, whether the annual toggle is framed to win, and what the feature table is accidentally arguing.

## ⚡ What it does

The [landing page teardown](landing-page-cro-teardown.md) audits persuasion; this audits **choice architecture** — the specific machinery of pricing pages that generic CRO reviews miss: which plan the page structurally recommends (there's always one, chosen or not), what the most expensive tier anchors, whether the middle tier is a real choice or a decoy, and how the annual/monthly toggle frames the commitment. Pricing pages fail structurally more often than they fail verbally.

## 🎯 When I use it (real scenario)

Pricing pages come up in nearly every SaaS and digital-product engagement I touch, and the recurring finding is the same: pages that present plans as neutral catalog items — no recommended tier, feature tables that read as spreadsheets, toggles that whisper the annual discount. The structural questions in this prompt are the checklist that emerged from those reviews; the benchmark context (annual plans carry 10-20pp better retention, discounts cost ~32% of LTV — see the [SaaS benchmarks](../../benchmarks/growth-saas-benchmarks.md)) is what turns the recommendations from taste into math.

## 📋 The Prompt

```
You are a pricing-page specialist (choice architecture + SaaS economics). Audit my pricing page structurally. Quote the actual element for every finding.

CONTEXT:
- Product + the plan I WANT most customers on (my "hero plan"): [X]
- Plans & prices (incl. annual/monthly): [list]
- Current plan mix if known (% of new customers per plan): [X]
- Audience sophistication: [first pricing page they've seen today, or their fifth?]
- Traffic source hitting this page: [X]

PRICING PAGE CONTENT (paste everything: plan names, prices, feature lists, toggle labels, badges, CTAs, FAQ):
[PASTE]

AUDIT IN THIS ORDER:

1. THE STEER — which plan does the page structurally recommend right now
   (visual weight, badge, column order, defaults)? Does it match my hero plan?
   A page with no steer is a page that delegates pricing to anxiety.

2. ANCHOR CHECK — what's the first price the eye meets? Does the top tier make
   the hero plan feel reasonable, or does a low entry price make it feel expensive?
   Column order and mobile order BOTH.

3. DECOY LOGIC — is there a plan whose job is to make another plan obviously
   better? If every plan is "a reasonable choice for someone," none is designed.
   Identify which plan could be repriced/refeatured into a decoy.

4. THE TOGGLE — annual/monthly: which is default? Is the annual framing loss-based
   ("save X") or price-based (smaller number shown)? Is the monthly price of the
   annual plan shown (it should be)? Flag if the discount is deep enough to attract
   discount-hunters rather than commitment.

5. FEATURE TABLE FORENSICS — is it organized by what MATTERS to the buying
   decision or by database schema? Find: the 3 rows that actually differentiate,
   buried; the rows nobody understands (jargon); checkmark inflation that makes
   the cheap plan look sufficient.

6. FRICTION & TRUST AT THE MONEY MOMENT — guarantee/refund visibility, "cancel
   anytime", payment methods, and (for MENA) local pricing/currency display.

7. ENTERPRISE/TOP-TIER CTA — "Contact us" placement and what it signals.

OUTPUT:
- Structural verdict: what this page currently argues, in one sentence
- Top 5 changes ranked by impact ÷ effort, each with the exact element + replacement
- What NOT to touch
- THE ONE TEST to run first, with hypothesis and the metric that decides it
  (plan mix shift counts as a win even when total conversion is flat)
```

## 🧠 Pro tips

- Optimize plan mix, not just conversion rate — moving buyers one tier up at flat conversion is often worth more than +10% conversion into the bottom tier.
- The annual toggle is the compound-interest lever: annual mix improves retention and cash simultaneously ([ChartMogul billing data](https://chartmogul.com/reports/saas-billing-report/)) — but resist deep discounts; discounted customers churn harder and pay less forever ([Paddle/ProfitWell](https://www.paddle.com/blog/saas-discounting-strategy)).
- Three plans is a decision; five is a menu; seven is a support ticket. If you can't name each plan's intended customer in one sentence, merge plans before optimizing the page.
- Watch real sessions on the feature table (or ask support what pricing questions recur) — recurring pricing questions are rows that failed.
- Pair with the [outcome framing of the offer stack](../growth/offer-stack-builder.md): the page architecture steers WHICH plan; the copy still has to sell WHY any plan.

## 🔗 Related assets

- [Landing Page CRO Teardown](landing-page-cro-teardown.md)
- [Growth & SaaS Benchmarks](../../benchmarks/growth-saas-benchmarks.md)
- [Offer Stack Builder](../growth/offer-stack-builder.md)
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
