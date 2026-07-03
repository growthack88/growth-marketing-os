---
title: "UGC Brief Generator Prompt — Creator Briefs That Get Usable Footage on Take One"
author: "Mahmoud Omar"
author_url: "https://mahmoudomar.com"
category: "social"
type: "prompt"
level: "intermediate"
works_with: "Claude, ChatGPT, Gemini"
language: "Bilingual"
last_verified: "2026-07-02"
hook: "Bad UGC isn't a creator problem. It's a brief problem — you sent a mood board when they needed a script skeleton."
email_subject: "The UGC brief that stops the reshoot cycle"
short_pitch: "Generate complete UGC creator briefs from one product + one angle: shot-by-shot skeleton, spoken-language script beats, the 3 mistakes to avoid, and delivery specs — in English or Egyptian Arabic."
---

# UGC Brief Generator Prompt

> Turn a product + an angle into a complete creator brief: hook options, beat-by-beat script skeleton, shot list, do/don't rules, and delivery specs — so the first delivery is usable instead of round three.

## ⚡ What it does

The UGC failure loop is always the same: vague brief → creator improvises → footage that can't be edited into an ad → awkward revision requests → everyone unhappy. This prompt generates the brief that prevents it: structured enough that the footage cuts together (hook variants, beats with timestamps, mandatory shots), loose enough that the creator still sounds like a person and not a spokesperson.

## 🎯 When I use it (real scenario)

Born from creative production sprints where the expensive lesson was that revision rounds cost more than briefing time — a reshoot burns a week; a beat-skeleton brief costs ten minutes. The Arabic option exists because UGC in عامية has an extra failure mode: creators who slip into formal فصحى the moment a camera turns on, which reads as an infomercial. The brief now says explicitly: talk like you're voice-noting a friend — «اتكلم زي ما بتبعت voice note لصاحبك».

## 📋 The Prompt

```
You are a UGC creative director for performance ads. Write a complete creator brief.

INPUT:
- Product + what it does: [X]
- The ONE angle this video tests: [pain / dream / mechanism / proof / objection — from my angle matrix]
- Platform + placement: [Meta Reels / TikTok / Stories]
- Target length: [15s / 30s / 60s]
- Creator profile: [age range, vibe, camera experience]
- Language: [EN / Egyptian Arabic عامية / both]
- What I can send the creator: [product sample, screen access, b-roll library]

WRITE THE BRIEF:

1. THE ONE-LINER — what this video must make the viewer feel/believe (creator reads this first; everything serves it)

2. HOOKS — 3 options for the first 2 seconds, written as SPOKEN lines (not captions).
   For عامية: spoken Egyptian, English business terms kept in English, zero فصحى.

3. BEAT SKELETON — for the target length, timestamped:
   hook → context/problem → product enters (native, not presentational) → proof beat
   (the one MANDATORY shot) → payoff → soft CTA.
   Per beat: what's said (gist, not word-for-word) + what's on screen.

4. MANDATORY SHOTS (max 4) — the shots the edit cannot live without. Everything else is creator's choice.

5. DO / DON'T (max 5 each) — the actual failure modes: don't hold product like a QVC host,
   don't read a script off-screen, do shoot vertical, do leave 2s of silence before the hook
   (edit room), don't mention price if the offer changes.

6. DELIVERY SPECS — resolution, orientation, raw + no music, separate selfie-style intro take,
   filename convention, deadline.

7. USAGE RIGHTS LINE — plain-language paid-usage clause placeholder for the agreed scope.

Keep the whole brief under one page. Creators don't read page two.
```

## 🧠 Pro tips

- One angle per brief, always. "Also mention the discount and the new colors" is how good footage dies.
- Ask for the hook in 3 takes with different energy — hooks are where you'll want options in the edit, not the middle.
- The proof beat is the ad. If the brief doesn't specify exactly what proof looks like on screen (result, demo moment, before/after), you'll get a testimonial monologue instead.
- Brief creators on the [Ad Angle Matrix](../paid-ads/ad-angle-matrix.md) output directly — angle #3 from the matrix becomes the ONE-LINER of this brief. The pipeline composes.
- For عامية briefs, send the hook options as voice notes, not text — creators mimic delivery, and written Arabic pulls them toward فصحى.

## 🔗 Related assets

- [Ad Angle Matrix](../paid-ads/ad-angle-matrix.md)
- [Bilingual Hook Bank](../../swipe-files/hooks/bilingual-hook-bank.md)
- [Meta Ads Creative Diagnosis](../paid-ads/meta-ads-creative-diagnosis.md)
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
