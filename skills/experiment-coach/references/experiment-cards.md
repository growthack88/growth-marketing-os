# Experiment card library (32 cards)

Ready starting points. A card is a **pattern**, not a promise. These cards deliberately carry **no expected lifts**: any lift number would be invented. The user's own baseline and a written decision rule decide.

**Business types:** E = e-commerce (incl. COD) · S = SaaS / app · D = digital product / course / community · X = services / B2B.
**Traffic:** *none* = a pre-launch method (no A/B traffic needed) · *A/B* = size it with `calc ab` before committing.

How to use: pick the funnel stage that is the bottleneck (don't pick by excitement), choose 3–5 cards that fit the business type, fill in the hypothesis with the user's evidence, then rank them with ICE (impact, confidence, ease), writing one sentence of reasoning per score. Every card that runs gets a decision rule and a log entry.

Hypothesis template: **If we [change] for [segment], [primary metric] will improve because [evidence: interview quote, data, objection].**

---

## Pre-launch (P)

**P1 · Problem interviews** · all · traffic: none
Method: 8–15 interviews about the last incident (see interviews.md). Metric: count with an unprompted recent incident and a workaround. Watch-out: friends and leading questions.

**P2 · Smoke test (page + waitlist)** · all · traffic: none (paid strangers)
Method: one honest page and a paid audience. Metric: visitor → sign-up vs. the economics pass line. Guardrail: sign-up quality (thank-you-page answers). Watch-out: message mismatch.

**P3 · Promise test on ads** · all · traffic: none
Method: 3–5 ads, each with a different promise from the interview language, all pointing to matching page variants. Metric: cost per sign-up per promise. Watch-out: judging on CTR alone (clicks ≠ intent).

**P4 · Fake door (plan or feature)** · S, D · traffic: existing users
Method: a new option where the real choice happens, with an honest "not live yet" after the click. Metric: views → clicks → emails, vs. a similar existing option. Watch-out: hiding the "not live" message.

**P5 · Refundable pre-sale** · all · traffic: waitlist first
Method: founding price or deposit, a delivery date, and a full-refund promise. Metric: paid count vs. break-even pre-sales. Watch-out: COD "orders" counted as commitment.

**P6 · Concierge MVP** · S, D, X · traffic: none
Method: deliver the outcome by hand to the first 5–10 paying customers before building. Metric: completed deliveries, repeat use, willingness to keep paying. Watch-out: free pilots that teach nothing about price.

**P7 · Price-point pre-sale split** · S, D · traffic: waitlist split at random
Method: two prices sent to two random halves of the waitlist at the same time. Metric: paid share and revenue per invitee. Guardrail: refund requests. Watch-out: small lists can't separate close prices. Report it as directional.

**P8 · Demo video test** · S, D · traffic: none (page visitors)
Method: add a short demo to the smoke-test page as a separate test after the first pass. Metric: sign-up rate, video completion. Watch-out: changing the copy at the same time.

## Acquisition (A)

**A1 · Channel probe** · all · traffic: small fixed budget per channel
Method: same offer and page, equal small budgets on 2–3 channels for the same period. Metric: cost per *qualified* sign-up or lead. Watch-out: comparing channels with different offers.

**A2 · Hook / angle test** · E, D · traffic: A/B (ad platform split)
Method: one variable, the opening angle. Metric: cost per purchase or lead (not CTR). Watch-out: winners that attract cheap but low-quality buyers.

**A3 · Lead magnet vs. direct offer** · D, X, S · traffic: A/B
Method: a free resource that pre-sells the paid product vs. a direct offer. Metric: cost per paying customer after N days. Watch-out: counting leads, not customers.

**A4 · Click-to-WhatsApp vs. landing-page form** · E, X · traffic: A/B
Method: the same ad, sending people either to a WhatsApp chat or to a form. Metric: cost per qualified conversation or order. Guardrail: response time and team capacity. Watch-out: no one staffing the chat at peak hours.

**A5 · Dialect vs. MSA creative** · all (Arab markets) · traffic: A/B
Method: the same offer, Egyptian/Gulf dialect vs. MSA (or vs. English). Metric: cost per conversion by country. Watch-out: mixing countries in one ad set.

**A6 · Creator/UGC vs. brand creative** · E, D · traffic: A/B
Method: the same message, delivered by a creator vs. brand-produced. Metric: cost per purchase. Watch-out: one creator ≠ the format. Test 2–3.

## Activation (V)

**V1 · Shorter sign-up** · S, D, X · traffic: A/B
Method: remove non-essential fields or steps. Metric: sign-up completion → activation (not just completion). Guardrail: lead quality.

**V2 · Path to the aha moment** · S · traffic: A/B
Method: an onboarding checklist that drives the one action correlated with retention. Metric: share reaching the aha action within N days. Watch-out: picking an aha action without checking it predicts retention.

**V3 · Templates or sample data on first run** · S · traffic: A/B
Method: start new users from a filled example instead of an empty state. Metric: first meaningful action within the session. Watch-out: users never replacing the sample.

**V4 · First-order incentive vs. free shipping** · E · traffic: A/B
Method: a discount vs. free shipping of equal cost. Metric: first-order conversion and contribution margin. Guardrail: margin per order.

**V5 · COD confirmation script** · E (COD) · traffic: A/B on orders
Method: a structured WhatsApp/call confirmation script vs. the current one. Metric: **delivered** orders ÷ placed orders. Guardrail: confirmation cost per order. Watch-out: measuring confirmations, not deliveries.

**V6 · Human onboarding call** · S, X · traffic: random half of new sign-ups
Method: offer a 15-minute setup call. Metric: activation and paid conversion. Guardrail: team hours per conversion.

## Retention (R)

**R1 · Usage-triggered reminder** · S, D · traffic: A/B (holdout)
Method: a message when a user stalls before the next key action. Metric: return within N days vs. a holdout. Watch-out: no holdout = no learning.

**R2 · Win-back sequence** · E, S, D · traffic: holdout
Method: a sequence for dormant users or customers. Metric: reactivation vs. a holdout group. Guardrail: unsubscribe/complaint rate.

**R3 · Replenishment timing** · E · traffic: holdout
Method: a reminder timed to the product's real usage cycle (measured from repeat-order gaps). Metric: repeat-purchase rate. Watch-out: guessing the cycle instead of measuring it.

**R4 · Pause option or save offer in cancel flow** · S · traffic: A/B
Method: offer pause or a downgrade before cancel. Metric: retained accounts after 60–90 days (not just at the cancel screen). Guardrail: support complaints.

## Referral (F)

**F1 · Two-sided referral at a success moment** · S, E · traffic: A/B
Method: ask right after the user gets value, with a reward for both sides. Metric: referred paying customers per active user. Watch-out: rewards that attract fraud. Add a qualification rule.

**F2 · Share prompt after an outcome** · S, D · traffic: A/B
Method: a prompt to share a result (certificate, report, before/after). Metric: share rate → visits → sign-ups. Watch-out: counting shares that bring no one.

## Revenue (M)

**M1 · Annual plan default** · S · traffic: A/B
Method: show annual billing first or preselected, with honest savings shown. Metric: revenue per visitor, annual share. Guardrail: refunds and chargebacks.

**M2 · Bundle / offer stack** · E, D · traffic: A/B
Method: a bundle that solves the whole job vs. single items. Metric: revenue per visitor and margin. Watch-out: AOV up but conversion down. Judge on revenue per visitor.

**M3 · Free-shipping threshold** · E · traffic: A/B
Method: set the threshold from the current order-value distribution. Metric: contribution margin per visitor. Guardrail: conversion rate.

**M4 · Prepaid incentive vs. COD** · E (COD markets) · traffic: A/B
Method: a small incentive for paying upfront. Metric: delivered revenue per visitor and prepaid share. Guardrail: total conversion. Watch-out: an incentive that costs more than the returns it prevents. Compute it with the store's own RTO cost.

**M5 · Founding-price ladder** · D, S · traffic: none (launch mechanic)
Method: a public price ladder with real dates or caps. Metric: paid count per stage. Watch-out: extending "final" deadlines (it kills trust).

**M6 · Pricing-page anchor / decoy** · S · traffic: A/B
Method: change the plan order, add a high anchor, or add a decoy plan. Metric: revenue per visitor, plan mix. Guardrail: support load from confused buyers.

---

Repo prompts that pair with these cards (when the user has Growth Marketing OS): Growth Experiment Designer (ranking), Offer Stack Builder (M2), Pricing Page Optimizer (M6), Referral Program Designer (F1), Win-Back Sequence (R2), COD WhatsApp Script Bank (V5), Ad Angle Matrix (A2), Campaign Postmortem (after every card).
