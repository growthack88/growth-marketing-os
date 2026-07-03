---
title: "Win-Back & List Reactivation Sequence Prompt — Revive Dormant Subscribers Without Begging"
author: "Mahmoud Omar"
author_url: "https://mahmoudomar.com"
category: "email"
type: "prompt"
level: "intermediate"
works_with: "Claude, ChatGPT, Gemini — output drops into any ESP"
language: "Bilingual"
last_verified: "2026-07-03"
hook: "A third of your list stopped reading you months ago, and you're still paying your ESP for them — and paying inbox providers with your sender reputation."
email_subject: "The win-back sequence: revive, re-permission, or remove"
short_pitch: "Generate a 4-touch win-back sequence for dormant subscribers or lapsed customers: pattern-interrupt, value-led reminder, honest re-permission ask, and a clean goodbye — in English or Egyptian عامية, with the deliverability logic built in."
---

# Win-Back & List Reactivation Sequence Prompt

> Generate a complete win-back sequence — for dormant subscribers or lapsed customers — built on the honest premise: revive the revivable, re-permission the undecided, and remove the dead, because a large cold list is a liability wearing a vanity metric.

## ⚡ What it does

Most "win-back" emails are the same discount blast that trained the list to ignore the brand in the first place. This prompt builds the sequence around the actual mechanics: a pattern-interrupt that doesn't look like every other send, a value-led reason to return (not an apology tour), an explicit re-permission moment — and the part most brands skip because it feels like losing: sunsetting non-responders, which is what protects deliverability for everyone who stayed.

## 🎯 When I use it (real scenario)

List hygiene is the unglamorous half of every email program I've worked on — the audits keep finding the same thing: engagement metrics degrading not because content got worse, but because the denominator quietly filled with people who stopped reading a year ago (and inbox providers score you on exactly that). The sequence structure here is the standard I apply before any "our open rates are falling" conversation goes anywhere else; the segmentation-first rule exists because a lapsed CUSTOMER and a never-bought subscriber deserve entirely different arguments.

## 📋 The Prompt

```
You are a retention & deliverability strategist. Build my win-back / reactivation sequence.

CONTEXT:
- Who's dormant: [subscribers who stopped opening ~X months / customers who stopped buying]
- Size of dormant segment vs total list: [X / X]
- What they originally signed up for or bought: [X]
- What's genuinely NEW or better since they left: [list honestly — if nothing, say nothing]
- Incentive I can offer (if any): [X or none]
- Channel(s): [email / SMS / WhatsApp] · Language: [EN / Egyptian عامية / both]
- My ESP's sunset capability: [can I auto-suppress non-responders? Y/N]

FIRST — SEGMENT CHECK:
If my "dormant" bucket mixes lapsed customers and never-bought subscribers, split
the sequence into two tracks — their reasons for leaving differ and so must the
argument. Tell me which inputs you're using for which track.

BUILD 4 TOUCHES (per track):

TOUCH 1 — PATTERN INTERRUPT (the one that gets seen)
Subject + body that does NOT look like my usual sends. Short, personal, one
sentence of curiosity or candor. No discount. No "we miss you" template.
Goal: one open, one click, or one reply — any signal of life.

TOUCH 2 — THE REASON TO RETURN (5-7 days later)
Lead with what's NEW since they left (from my list — never invent improvements).
For lapsed customers: acknowledge the lapse without groveling. One clear CTA.

TOUCH 3 — RE-PERMISSION, HONESTLY (7 days later)
Ask the question directly: "أبطّل أبعتلك؟" / "Want to keep hearing from me?"
Two-button choice: stay (maybe with frequency/topic options) or leave cleanly.
This email's unsubscribes are a SUCCESS metric — say so in a comment for me.

TOUCH 4 — THE SUNSET (final)
The goodbye + what they'll miss + one last link. Then: suppression instructions —
non-responders move OUT of active sends (suppress or delete per my ESP answer).

FOR EACH TOUCH: subject + preview (paired, not repeating), body under 100 words,
CTA, and the metric that counts as success for THAT touch.

RULES: عامية with English business terms if Arabic — never فصحى. If an incentive
exists, it appears ONCE (touch 2 for customers, never for never-buyers — don't
pay people who never paid you). No fake "your account will be deleted" threats.
```

## 🧠 Pro tips

- Define "dormant" from engagement recency, not subscription age — and remember Apple MPP inflates opens ([email benchmarks](../../benchmarks/email-whatsapp-benchmarks.md)); use clicks as the truth signal where possible.
- Run the sequence quarterly as a system, not once as a rescue — sunset flows are hygiene, like backups.
- The re-permission email is the highest-integrity move in email marketing and it *feels* terrible. Send it anyway: a 20% smaller list with 2x engagement wins on deliverability, and deliverability compounds.
- Lapsed COD customers: WhatsApp beats email for win-back — the relationship lives on the number that confirmed their orders (script #17 in the [WhatsApp bank](../../swipe-files/whatsapp/cod-whatsapp-script-bank.md)).
- Mine the replies to touch 3 — people tell you exactly why they went quiet, and that's free [voice-of-customer data](../cro/review-mining-copy-bank.md) for the next acquisition round.

## 🔗 Related assets

- [Welcome Sequence Builder](welcome-sequence-builder.md)
- [Email & WhatsApp Benchmarks](../../benchmarks/email-whatsapp-benchmarks.md)
- [Bilingual Subject Line Bank](../../swipe-files/subject-lines/bilingual-subject-line-bank.md)
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
