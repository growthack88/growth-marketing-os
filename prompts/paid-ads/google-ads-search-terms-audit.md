---
title: "Google Ads Search Terms Audit Prompt — Find Where Your Budget Is Leaking"
author: "Mahmoud Omar"
author_url: "https://mahmoudomar.com"
category: "paid-ads"
type: "prompt"
level: "intermediate"
works_with: "Claude, ChatGPT, Gemini"
language: "EN"
last_verified: "2026-07-02"
hook: "Your Google Ads account isn't underperforming. It's leaking — and the search terms report knows exactly where."
email_subject: "The 10-minute audit that turns 5,000 search terms into a negatives list"
short_pitch: "Export your search terms report, paste it into this prompt, and get a full leak audit: irrelevant queries flagged, negative keyword list built, and high-intent terms you should be bidding on exact — in minutes, not hours."
---

# Google Ads Search Terms Audit Prompt

> Paste your search terms report and get a structured leak audit: wasted-spend buckets, a ready-to-upload negative keyword list, and the high-intent queries you should promote to exact match.

## ⚡ What it does

Broad match and Performance Max quietly bleed budget into queries that will never convert — and nobody has time to read a 5,000-row search terms report line by line. This prompt turns the raw export into four clean buckets (irrelevant, competitor, research-intent, high-intent unbid) and outputs actions you can apply the same day: negatives to add, exact-match candidates to split out, and match-type fixes.

## 🎯 When I use it (real scenario)

This is the first thing I run when auditing or taking over any Google Ads account — before touching bids, budgets, or creatives. The classic pattern: broad match campaigns matching against queries that are one or two words away from the product but a universe away in intent. The audit compresses what used to be an afternoon of spreadsheet filtering into one prompt run, and the negatives list alone usually pays for the time on day one.

## 📋 The Prompt

```
You are a senior Google Ads auditor. I'm pasting my Search Terms Report export below. Audit it for budget leaks — be ruthless and specific.

CONTEXT:
- Business: [what you sell, target market, geography]
- Goal conversion: [purchase / lead / signup]
- Target CPA or ROAS: [X]
- Campaign types in the report: [Search / PMax / Shopping]

SEARCH TERMS DATA (term, impressions, clicks, cost, conversions):
[PASTE EXPORT ROWS HERE — CSV or table format]

CLASSIFY EVERY TERM WITH SPEND INTO EXACTLY ONE BUCKET:
1. IRRELEVANT — wrong product, wrong audience, wrong intent entirely
2. COMPETITOR — competitor brand names (decide: block or bid deliberately)
3. RESEARCH-INTENT — "how to", "what is", comparisons with zero purchase signals
4. HIGH-INTENT UNBID — converting or clearly commercial terms I'm reaching only via broad/PMax and should control with exact match

THEN OUTPUT:
A. Total estimated wasted spend (buckets 1 + 3, and 2 if blocking) as % of the pasted spend
B. NEGATIVE KEYWORD LIST — ready to upload: term, suggested match type (exact/phrase), campaign vs account level
C. EXACT-MATCH PROMOTION LIST — bucket 4 terms worth their own ad groups, with suggested starting bids relative to current CPC
D. PATTERN DIAGNOSIS — the 3 recurring leak patterns (e.g. one broad keyword responsible for most junk) so I fix causes, not symptoms
E. One structural recommendation: what this report says about my match-type strategy overall
```

## 🧠 Pro tips

- Export at least 30 days of data; filter to terms with cost > 0 before pasting to stay inside context limits on big accounts.
- Run buckets 1-3 as account-level negative lists, not campaign-level — leaks come back through new campaigns.
- For PMax you can't see everything, but auditing what Google does show you is still the fastest brand-safety and waste check available.
- Re-run monthly. Broad match drifts — a clean account in January is a leaky one by March.
- Pair with the [Meta Ads Creative Diagnosis](meta-ads-creative-diagnosis.md) mindset: fix the leak layer before you touch anything else.

## 🔗 Related assets

- [Meta Ads Creative Diagnosis](meta-ads-creative-diagnosis.md)
- [Funnel Decomposition Skill](../../skills/funnel-decomposition/SKILL.md)
- [Landing Page CRO Teardown](../cro/landing-page-cro-teardown.md)
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
