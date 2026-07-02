---
title: "Landing Page CRO Teardown Prompt — Find the Conversion Leak Before You Redesign"
author: "Mahmoud Omar"
author_url: "https://mahmoudomar.com"
category: "cro"
type: "prompt"
level: "intermediate"
works_with: "Claude, ChatGPT, Gemini"
language: "EN"
last_verified: "2026-07-02"
hook: "Nobody redesigns their way out of a message-match problem."
email_subject: "The CRO teardown prompt I run before touching any landing page"
short_pitch: "Paste your landing page copy + traffic source into this prompt and get a 6-layer CRO teardown: message match, above-fold clarity, offer, friction, trust, mobile — with fixes ranked by impact vs effort."
---

# Landing Page CRO Teardown Prompt

> Paste your landing page content and traffic context, get a 6-layer conversion teardown with fixes ranked by impact vs effort — so you change the thing that's actually leaking, not the thing that's easiest to redesign.

## ⚡ What it does

Most landing page "optimization" is redesign theater: new hero, new colors, same conversion rate. This prompt forces a structured teardown across the six layers where conversions actually die — message match with the ad, above-fold clarity, offer strength, friction, trust, and mobile experience — and returns a prioritized fix list instead of a vague critique.

## 🎯 When I use it (real scenario)

I ran versions of this teardown across the StartupKit Pro upgrade funnel while rebuilding its trial and pricing flow — page by page: landing, pricing, paywall. The recurring finding wasn't visual at all; it was message match and offer framing (features listed where outcomes should be, CTAs asking for commitment before showing value). Same story on Arabic RTL offer pages for an e-commerce book store: the teardown catches what a design eye skips, because it audits against the traffic source, not against taste.

## 📋 The Prompt

```
You are a senior CRO consultant. Tear down my landing page layer by layer. Do NOT give generic advice — every finding must quote the actual copy or element it refers to.

CONTEXT:
- Traffic source + the exact ad/post/email that sends people here: [paste the ad copy or describe]
- Audience temperature: [cold / warm / hot]
- Conversion goal on this page: [buy / trial / lead / book a call]
- Price point & offer: [X]
- Current conversion rate (if known): [X]%
- Device split (if known): [X]% mobile

LANDING PAGE CONTENT (full copy, in order, top to bottom — include headlines, subheads, CTAs, form fields, badges):
[PASTE PAGE CONTENT HERE]

TEAR DOWN IN THIS ORDER:
1. MESSAGE MATCH — does the page continue the exact promise of the ad? Score /10. Quote the ad line vs the H1.
2. ABOVE-FOLD CLARITY — 5-second test: what do I get, why you, what do I do next? Flag anything that needs scrolling to understand.
3. OFFER LAYER — is the offer stated as an outcome or a feature list? Is the value obvious vs the price? What's missing: guarantee, urgency, risk-reversal?
4. FRICTION LAYER — every field, click, and decision between arrival and conversion. Count them. Flag each one that isn't earning its cost.
5. TRUST LAYER — proof elements: are they specific (numbers, names, faces) or decorative? Where is proof missing next to a commitment point?
6. MOBILE LAYER — what breaks or gets buried on a small screen: CTA visibility, form length, load-heavy elements.

OUTPUT FORMAT:
- Layer scores (/10 each) + the single weakest layer
- Top 5 fixes ranked by expected impact vs implementation effort — each with the exact element to change and the suggested replacement copy
- 3 things that are working — do NOT touch these
- One A/B test to run first, with the hypothesis stated in one sentence
```

## 🧠 Pro tips

- Always paste the ad WITH the page. A teardown without the traffic source is a design review, not CRO.
- Run it separately for cold and warm traffic pages — the right page for a retargeting click fails a cold click, and vice versa.
- For RTL/Arabic pages, add one line to the prompt: "The page is Arabic RTL — audit CTA button copy for dialect (عامية vs فصحى) and RTL layout breaks."
- Rerun after implementing the top fix, not all five — otherwise you learn nothing about what moved the number.

## 🔗 Related assets

- [Meta Ads Creative Diagnosis](../paid-ads/meta-ads-creative-diagnosis.md)
- [Funnel Decomposition Skill](../../skills/funnel-decomposition/SKILL.md)
- [Arabic CTA Bank](../../swipe-files/ctas/arabic-cta-bank.md)
<!-- MO-BRAND-FOOTER v1 — paste at the bottom of every asset file -->

---

## 🦆 Built by Mahmoud Omar

**Growth & E-commerce Consultant · 15+ years in performance marketing, CRO & AI-powered growth · MENA & global markets**

| Asset | Link |
|---|---|
| 🌍 Personal Site | [mahmoudomar.com](https://mahmoudomar.com) |
| 📕 Book · Growth Systems | [buildinggrowthmachine.com](https://buildinggrowthmachine.com) |
| 📗 Book · Growth Duck Up | [growthduckup.com](https://growthduckup.com) |
| 🎓 Growth Hack Academy | [growthhackacademy.com](https://growthhackacademy.com) |
| 🚀 StartupKit Pro — Startup OS for MENA founders | [startupkit.pro](https://startupkit.pro) |
| 🍅 DuckDoro — calm productivity app | [duckdoro.com](https://duckdoro.com) |
| 🎥 YouTube (40K+ marketers) | [Subscribe → Growth Hack Academy](https://www.youtube.com/@GrowthHackAcademy?sub_confirmation=1) |

⭐ **Saved you time? [Star the repo](https://github.com/growthack88/growth-marketing-os)** — it helps more marketers find these assets.

> All assets are original work by [Mahmoud Omar](https://mahmoudomar.com), battle-tested on real accounts. Free to use with attribution. Not AI-generated filler.
