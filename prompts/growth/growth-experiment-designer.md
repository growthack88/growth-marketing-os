---
title: "Growth Experiment Designer Prompt — From 'Let's Try Stuff' to a Ranked Testing Backlog"
author: "Mahmoud Omar"
author_url: "https://mahmoudomar.com"
category: "growth"
type: "prompt"
level: "intermediate"
works_with: "Claude, ChatGPT, Gemini"
language: "EN"
last_verified: "2026-07-03"
hook: "Most growth 'experiments' are just changes with optimism attached. No hypothesis, no decision rule, no memory."
email_subject: "Turn your idea pile into a ranked experiment backlog"
short_pitch: "Feed this prompt your growth ideas + one bottleneck and get real experiments back: falsifiable hypotheses, minimum viable test designs, ICE scores with stated reasoning, decision rules, and a kill-criteria line for each."
---

# Growth Experiment Designer Prompt

> Convert a pile of growth ideas into a ranked experiment backlog: every idea becomes a falsifiable hypothesis with a minimum viable test, an honest ICE score, a decision rule, and a pre-committed kill line.

## ⚡ What it does

The difference between a growth team and a busy team is experiment design: a hypothesis stated before the test, a sample size that can actually answer the question, and a decision rule written down while everyone is still objective. This prompt does that conversion at backlog scale — it takes raw ideas ("we should try TikTok", "maybe a referral program"), rebuilds each as a real experiment, ranks them against your actual bottleneck, and refuses to let untestable ideas pretend to be experiments.

## 🎯 When I use it (real scenario)

This is the working session I run when a backlog has turned into a wish list — my own products included. The pattern it fixes is always the same: ideas ranked by excitement instead of by bottleneck relevance, and "tests" that run for two weeks and end in a shrug because nobody defined what result would mean what decision. Designing the decision rule BEFORE the test is the whole discipline — everything else in the prompt exists to force that.

## 📋 The Prompt

```
You are a growth experimentation lead. Convert my idea pile into a ranked experiment backlog. Be ruthless: ideas that can't produce a decision are not experiments.

CONTEXT:
- Product + current growth model in one paragraph: [X]
- THE BOTTLENECK right now (acquisition / activation / retention / monetization + evidence): [X]
- Monthly traffic/user volume available for testing: [X]
- Resources: [who can build/run tests, budget]
- Past experiments already run (so you don't re-suggest my graveyard): [list or "none logged"]

MY IDEA PILE:
[paste raw ideas, any format]

FOR EACH IDEA, BUILD:
1. HYPOTHESIS — "We believe [specific change] will move [metric] by [estimated range]
   because [insight/evidence]." If no honest 'because' exists, mark the idea
   NOT AN EXPERIMENT and move it to a "needs research first" list.
2. MINIMUM VIABLE TEST — the smallest/cheapest version that gives a real answer
   (fake-door, concierge, geo-split, subset rollout). Shrink scope, not rigor.
3. SAMPLE & DURATION check — with MY volume, can this reach a readable result in
   ≤4 weeks? If not: flag it and either redesign for a bigger effect size or park it.
4. DECISION RULE — written NOW: "if [metric] ≥ [X] → scale; between [X-Y] → iterate
   once on [variable]; below [Y] → kill." No test ships without one.
5. ICE SCORE — Impact (on THE bottleneck, not any metric) / Confidence (evidence-based:
   customer data > competitor precedent > opinion) / Ease. Show reasoning per digit —
   unexplained scores are vibes in a spreadsheet.

THEN OUTPUT:
- THE RANKED BACKLOG (table) with the top 3 marked "this sprint"
- CONFLICTS: which experiments contaminate each other if run simultaneously
- THE MISSING EXPERIMENT: given my bottleneck, the highest-leverage test NOT in
  my idea pile — and why I'm probably avoiding it
```

## 🧠 Pro tips

- One bottleneck per backlog. Ideas targeting other funnel stages go to the parking lot, however exciting — that's the ONE BOTTLENECK principle doing its job.
- Low-volume products can't run classic A/B tests — use sequential before/after with a guardrail metric, or bigger-swing tests (effect sizes worth detecting). The prompt's step 3 catches this; listen to it.
- "Confidence" is where backlogs get honest: an idea backed by review-mining evidence outranks a tactic from a viral thread, even at equal impact.
- Close the loop: every completed experiment goes through the [Campaign Postmortem](../paid-ads/campaign-postmortem.md) and its log entry feeds the next backlog session's "graveyard" input. That loop IS the growth process.
- Rerun the session monthly, not when the backlog is empty — backlogs rot as the bottleneck moves.

## 🔗 Related assets

- [Growth Strategist Agent](../../agents/growth-strategist-agent.md)
- [Campaign Postmortem](../paid-ads/campaign-postmortem.md)
- [Funnel Decomposition Skill](../../skills/funnel-decomposition/SKILL.md)
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
