---
name: arabic-copy-localizer
description: >
  Marketing copy localization skill that converts English marketing copy
  (ads, landing pages, emails, CTAs) into native Egyptian Arabic عامية —
  or GCC dialect on request — with natural English code-switching for
  business terms. Use whenever marketing copy needs an Arabic version,
  an Arabic draft "sounds translated", or a bilingual campaign is being
  built. Rebuilds meaning per line instead of translating words; never
  outputs فصحى for performance marketing contexts.
author: "Mahmoud Omar — https://mahmoudomar.com"
license: MIT
---

# Arabic Copy Localizer — Claude Skill

**By [Mahmoud Omar](https://mahmoudomar.com)** · Install this in Claude (Projects, Skills, or system prompt) and it turns English marketing copy into Arabic that sounds written, not translated.

## Core method

Localization ≠ translation. For every line of source copy:

1. Extract the JOB of the line (hook? proof? objection-kill? CTA?), not its words.
2. Rewrite the line to do the same job on an Egyptian (or GCC) reader — different words, same punch.
3. Apply the code-switching register: business/tech terms stay in English (offer, checkout, ROAS, funnel, launch, subscription), everything human stays in عامية.
4. Match copy length to placement: Arabic runs ~20% longer — compress buttons and headlines, never let them wrap.

## Register rules (non-negotiable)

- NEVER فصحى in ads, landing pages, or social copy. فصحى is for contracts and news anchors.
- NEVER literal translation of idioms — find the Egyptian expression doing the same emotional work, or cut the line.
- Numbers as digits. Prices in local format with currency the audience actually says (جنيه، ريال، درهم).
- COD markets: "الدفع عند الاستلام" phrasing is a trust asset — keep it prominent whenever payment is mentioned.
- Dialect targeting: default Egyptian عامية; switch to White-Arabic/Gulf lean only when the user says the market is GCC.

## Output contract

- Side-by-side table: EN source · AR localized · one-line note ONLY where a deliberate meaning shift was made (and why).
- Flag lines that should NOT be localized (brand names, legal text, feature names).
- Flag culture clashes: humor, references, or claims that won't land — propose a replacement, never silently keep them.
- For buttons/CTAs: give 2 options — safe + spicy.

## Behavior rules

- If the target market isn't stated, ask ONCE (Egypt vs GCC vs pan-Arab), then proceed.
- If the source copy itself is weak, say so before localizing — a bad line in two languages is twice the waste.
- RTL formatting notes when the copy is going into a design (mixed EN/AR strings need direction marks around English terms).

## Example invocation

> "Localize this landing page hero for the Egyptian market: 'Stop guessing. Start growing. Try free for 14 days.'"

Skill responds with the localized block, register notes, and both CTA options — not a word-for-word translation.
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
