---
title: "Case Study Writer Prompt — Interview Yourself Into a Case Study People Believe"
author: "Mahmoud Omar"
author_url: "https://mahmoudomar.com"
category: "content"
type: "prompt"
level: "beginner"
works_with: "Claude, ChatGPT, Gemini"
language: "Bilingual"
last_verified: "2026-07-03"
hook: "Nobody believes 'we 10x'd revenue'. Everybody believes 'we went from 41% to 26% checkout completion, and here's the shipping fee that did it.'"
email_subject: "Turn a finished campaign into a case study (interview format)"
short_pitch: "This prompt interviews you about a real campaign — baseline, intervention, numbers, external factors — then writes the case study with credibility architecture built in: equal comparison windows, the confession section, and 'where this won't work'."
---

# Case Study Writer Prompt

> Turns a real campaign into a written case study via structured interview: it extracts the facts (baseline, the move, the windows, the confounders), then writes the story with the credibility features most case studies skip — what failed first, what else was happening, and where the tactic won't transfer.

## ⚡ What it does

Case studies fail at credibility, not writing: percentage claims with no baseline, cherry-picked windows, wins with no confessed context. This prompt inverts the process — interview first, prose second. It refuses to write until it has the numbers and their windows, it asks the awkward questions (what else changed? what did the season do?), and it structurally includes the two sections that make readers trust the rest: "what wasn't working" and "where this won't work."

## 🎯 When I use it (real scenario)

This prompt exists because the hardest part of documenting real work isn't confidentiality — it's extraction. After a campaign, the facts live scattered across dashboards, chats, and memory, and the person who ran it is the worst judge of what's obvious. The interview format is how case studies get out of practitioners' heads (including mine — it's the companion to this repo's own [case-study template](../../templates/CASE_STUDY_TEMPLATE.md), which defines the output anatomy this prompt writes into).

## 📋 The Prompt

```
You are a case study editor with a fact-checker's temperament. INTERVIEW me about a real campaign, then write the case study. Do not write a word of prose until the interview is complete.

PHASE 1 — THE INTERVIEW (ask in batches of 3-4, adapt to my answers):

BASELINE & CONTEXT
- What was the business/campaign, market, and channel? (anonymization level: [none/partial/full])
- The starting numbers, with dates: what metric, what value, over what window?
- What had been tried before this, and what happened?

THE MOVE
- What exactly changed — and just as important, what deliberately did NOT change?
- Timeline: when did the change ship, when did you measure?
- What tools/process did you use?

THE NUMBERS (be strict with me here)
- After numbers — SAME metric, SAME window length as the baseline. If my windows
  don't match, make me fix them or state the mismatch in the case study.
- The guardrail metric: what could have gotten worse but didn't (or did)?
- What ELSE was happening — seasonality, price changes, other campaigns, market
  events? (This goes IN the case study, not under the rug.)

THE HONESTY LAYER
- What partially failed or surprised you?
- Where would this move NOT work — what conditions did it depend on?

PHASE 2 — WRITE (only after the interview):
Structure: result-first title (real numbers in it) → situation & baseline →
what wasn't working → the move (replicable detail) → the numbers table
(before/after/window/guardrail) → what else was happening → what made it work
& where it won't → takeaways (max 3).

RULES:
- Every number I gave appears with its window. No number I didn't give appears at all.
- If a claim came from my memory rather than data, mark it "(recalled, not logged)".
- Anonymize per my instruction but keep the CONTEXT concrete (market, scale band,
  category) — anonymous ≠ vague.
- Voice: practitioner writing to practitioners. No "unlock", no "game-changer".
- If Arabic output: عامية register with English business terms, never فصحى.

Begin the interview.
```

## 🧠 Pro tips

- Run this within two weeks of the campaign closing — case studies written a quarter later are dashboard archaeology plus optimism.
- The "what deliberately did NOT change" question is the credibility engine: isolating the variable is what separates a case study from a coincidence report.
- Keep a "case study raw material" note during every campaign (screenshots with dates, decision moments) — the interview goes from an hour to fifteen minutes.
- The "where this won't work" section is counterintuitively your best sales asset: readers who see their situation excluded trust the inclusion claims; and per the [LLM citation data](../../benchmarks/seo-geo-benchmarks.md), third-party-credible, claim-dense content is exactly what AI engines quote.
- Pair the output with the [Content Repurposing Matrix](content-repurposing-matrix.md) — one honest case study is a month of proof-angle posts.

## 🔗 Related assets

- [Case Study Template](../../templates/CASE_STUDY_TEMPLATE.md)
- [Campaign Postmortem](../paid-ads/campaign-postmortem.md)
- [Content Repurposing Matrix](content-repurposing-matrix.md)
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
