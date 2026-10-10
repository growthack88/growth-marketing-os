---
title: "Worked Example: Validating a Product Before Launch — Interviews, Smoke Test and Pre-Sale, Step by Step"
author: "Mahmoud Omar"
author_url: "https://mahmoudomar.com"
category: "growth"
type: "worked-example"
level: "beginner"
works_with: "Any new product, offer or market — digital or physical"
language: "EN"
last_verified: "2026-10-10"
hook: "The waitlist test came back 'in between'. The fix wasn't a better product. The ad and the page were promising different things."
email_subject: "Follow one idea from interviews to pre-sales (worked example)"
short_pitch: "A step-by-step teaching scenario: a founder validates a freelancer invoicing tool before writing code — riskiest assumption, problem interviews, a smoke-test landing page with a pass line computed from unit economics, and a refundable pre-sale. Every decision rule is written before the data."
---

# Worked Example: Validating a Product Before Launch

> 🧪 **This is a WORKED EXAMPLE: a fictional but realistic scenario built to teach the decision process.** "Daftarak" is not a real product, and its test results are invented. The benchmark cited is real and sourced. What's real here is the method: the [Pre-Launch Validation Playbook](../playbooks/pre-launch-validation-playbook.md), applied one step at a time.

## ⚡ What it does

Shows the whole [commitment ladder](../playbooks/pre-launch-validation-playbook.md) on one idea: how to pick the assumption to test first, how to turn unit economics into a pass line, what to do when a result lands "in between", and when to hand over to post-launch growth experiments. Every decision rule below was written before its test ran, in the [Experiment Log](../templates/EXPERIMENT_LOG_TEMPLATE.md).

## 🎯 The Scenario

**"Daftarak" (دفترك)** is a planned invoicing and payment-reminder tool for freelancers in Egypt. The founder's plan is a monthly subscription at EGP 150. The founder has a designer friend, a small savings budget, and a strong opinion: *"Every freelancer I know has clients who pay late. Of course they'll want this."*

Maybe. But "everyone I know" is a sample of friends, and nobody has paid anything yet.

## 📋 The Walkthrough

### Step 0 — Pick the riskiest assumption (one evening)

What must be true: (1) late payment is a real, recurring pain; (2) freelancers can be reached affordably; (3) they'll pay monthly for a tool instead of sending WhatsApp reminders by hand; (4) the founder can build it.

Assumption 4 is the founder's own skill, so it's low risk. Assumption 3 is the most likely to be wrong, and the whole business dies if it is. But you can't test willingness to pay for a problem you haven't confirmed. So the ladder starts at Step 1, with Step 4 as the real target.

### Step 1 — Problem interviews (two weeks)

**Decision rule, logged before the first call (EXP-01):** *"If most interviewees describe a late payment in the last two months AND an existing workaround → Step 2. If the pain only appears when we prompt it → stop."*

The founder interviews 12 freelancers found through design and developer groups (none of them friends) and asks only about the past: *"Tell me about the last time a client paid late. What did you do?"*

Fictional results: 9 of 12 describe a recent late payment without being prompted. Workarounds: WhatsApp reminders sent by hand, a spreadsheet, and, for three of them, paying an accountant. After the tenth call, three calls in a row add nothing new.

One phrase keeps coming back: *"العميل بيطنّش"* ("the client goes silent"). That becomes the landing page headline.

**Decision: pass → Step 2.** The pain is real and people already spend time and money on it. That still says nothing about whether they'll pay *this* founder.

### Step 2 — Smoke test: landing page + waitlist (three weeks)

**The pass line comes from economics, not hope:**
1. A small pilot spend measures the founder's own cost per click: about EGP 3. (There are no reliable public MENA CPC benchmarks; see the note in [Paid Ads benchmarks §4](../benchmarks/paid-ads-benchmarks.md). So you measure your own.)
2. The founder wants to earn back acquisition cost within 3 months: 3 × EGP 150 = EGP 450 per paying customer. They *guess* that 1 in 10 waitlist sign-ups will pay, a number Step 4 will replace. So the most they can spend per sign-up is EGP 45.
3. Required sign-up rate = EGP 3 ÷ EGP 45 ≈ **6.7%**.
4. Sanity check: the median landing page converts at **6.6%** for campaign/lead conversions ([Unbounce, Q4 2024](https://unbounce.com/average-conversion-rates-landing-pages/), via [CRO & E-commerce benchmarks §4](../benchmarks/cro-ecommerce-benchmarks.md)). The required rate is ambitious but not fantasy.

**Sample size:** expecting around 7% and wanting ± 2 points: 4 × 0.07 × 0.93 ÷ 0.02² ≈ 650 visitors, so about EGP 2,000 in ads.

**Decision rule (EXP-02):** *"Pass if ≥ 6.7% after 650+ visitors. Fail if < 3.5%. In between: change one thing and rerun once."*

**Run 1 (fictional):** 700 visitors, 29 sign-ups = **4.1%**. In between.

The tempting move is to redesign the whole page, change the price and try a new audience all at once. Instead the founder runs the [Landing Page CRO Teardown](../prompts/cro/landing-page-cro-teardown.md) and finds a message-match problem. The ad said *"free invoices in 30 seconds"*, but the page sold *payment reminders*. People clicked for one promise and landed on another. Run 1 tested the ad copy, not demand.

**The one change:** the ad now uses the page's promise and the interview phrase, "العميل بيطنّش؟ دفترك يفكّره بدالك" ("Client gone silent? Daftarak reminds them for you").

**Run 2 (fictional):** 720 visitors, 54 sign-ups = **7.5%**. Pass. The waitlist now has 83 people.

### Step 3 — Fake door (skipped, on purpose)

A fake door needs an existing product or site where real users make real choices. Daftarak has neither, so the founder goes straight to Step 4. After launch, the same founder will use a fake door to test a "client portal" add-on before building it.

### Step 4 — Pre-sale (two weeks)

**The offer** (shaped with the [Offer Stack Builder](../prompts/growth/offer-stack-builder.md) and the [Lifetime Deal Launch Playbook](../playbooks/lifetime-deal-launch-playbook.md)): a founding-member year at a one-time price, a delivery date 8 weeks out, and a full refund if it ships late.

**Decision rule (EXP-03):** the founder's cost estimate for the first version says 15 founding members justify building. *"Pass if ≥ 15 paid within 14 days. Fail if < 6 → back to Step 1 with the non-payers. In between: one change, rerun once."*

**Run 1 (fictional):** 7 paid. In between.

The founder calls 10 people who signed up but didn't pay. Two reasons come up again and again: *"I don't have a card that works online"* and *"I want to see it first."* A cash-on-delivery order wouldn't solve this. As the [COD Profit Funnel](../frameworks/cod-profit-funnel.md) shows, a COD order is a "maybe" until delivery, and validation needs money that has actually moved.

**The one change:** one extra payment link next to the card option that accepts instant bank transfer and mobile wallets. It targets the most common objection, *payment friction*. The "see it first" request waits for its own test, a demo video, so the rerun has only one change in it.

**Run 2 (fictional):** 16 paid in total. **Pass → build.**

### After launch — switching to growth experiments

With a founding cohort using the product, the questions change from "does anyone want this?" to "where does growth stall?" The founder:
- feeds the idea pile into the [Growth Experiment Designer](../prompts/growth/growth-experiment-designer.md) to get a ranked backlog with kill lines;
- runs the demo-video idea as its own test, with its own decision rule;
- waits to use the [A/B Testing skill](../skills/community/ab-testing/SKILL.md) until site traffic can reach a meaningful sample within a few weeks — at Daftarak's early volume, a split test would take months to say anything;
- closes each test and campaign with the [Campaign Postmortem](../prompts/paid-ads/campaign-postmortem.md), in the same experiment log that started at EXP-01.

## 🧠 The transferable lessons

1. **Test the riskiest assumption you can test right now,** not the one that's easiest or most fun to test.
2. **Pass lines come from your economics.** The benchmark is a sanity check, not the goal.
3. **"In between" is the most useful result,** as long as you change one thing. Here it exposed a message mismatch and a payment problem, not a weak idea.
4. **The people who almost said yes are your best researchers.** Ten calls with sign-ups who didn't pay explained more than the conversion rate did.
5. **In MENA, how people pay is part of the product.** A pre-sale that only takes cards tests access to cards as much as it tests demand.

## 🔗 Related assets

- [Pre-Launch Validation Playbook](../playbooks/pre-launch-validation-playbook.md): the ladder used here
- [Experiment Log template](../templates/EXPERIMENT_LOG_TEMPLATE.md): where EXP-01 to EXP-03 live
- [Growth Experiment Designer](../prompts/growth/growth-experiment-designer.md): what comes after launch
- [SaaS Trial Conversion Turnaround](saas-trial-conversion-turnaround.md): the next problem most products hit — activation

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
