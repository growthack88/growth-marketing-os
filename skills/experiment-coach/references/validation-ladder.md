# Validation ladder (compact)

The full version with Arabic text is in the [Pre-Launch Validation Playbook](https://github.com/growthack88/growth-marketing-os/blob/main/playbooks/pre-launch-validation-playbook.md). Each step asks for more commitment than the one before and runs only if the previous step passed.

| Step | Proves | Commitment asked | Typical cost | Primary metric |
|---|---|---|---|---|
| 0 · Riskiest assumption | What to test first | none | an evening | — |
| 1 · Problem interviews | The problem is real and already costs them | time | 1–2 weeks | share describing a recent incident + a workaround |
| 2 · Smoke test (page + waitlist) | Strangers want the promise | email | small ad budget | visitor → sign-up rate |
| 3 · Fake door | Real users choose it in context | a click (+ email) | low | views → clicks on the new option |
| 4 · Pre-sale | They'll pay | money (refundable) | refunds if you don't ship | waitlist → paid, total paid vs break-even |

## 0 · Riskiest assumption

List what must be true: problem exists · painful enough · reachable · will pay this price · can deliver. Score each on two things: *how likely it is to be wrong* and *whether being wrong kills the plan*. Test the one that scores high on both. If it can't be tested yet, test the earliest assumption it depends on. Usually that's the problem, which is Step 1.

Optional warm-up: synthetic audiences (GrowthLab, MiroFish, LLM persona panels). Use the output for questions and objections only. It never counts as a pass.

## 1 · Problem interviews

- Recruit people matching the target customer, **not** friends or family. Sources: niche Facebook/WhatsApp/Telegram groups, LinkedIn, existing customers of adjacent products, a small screener ad.
- Ask about the past (last incident, what they did, what it cost, what they tried). Never ask "would you buy?"
- Stop when three interviews in a row add nothing new.
- **Rule template:** "If most interviewees describe a recent incident without being prompted AND an existing workaround → Step 2. If the pain only appears when prompted → stop or re-target."

## 2 · Smoke test

- One page: the promise in customers' words, who it's for, what they get, an honest "launching soon", one form.
- Traffic from **strangers** in the real target audience (paid social/search), not followers.
- Pass line = CPC ÷ affordable cost per sign-up ([calculations §1](calculations.md)). Sanity-check it against the sourced landing-page median in [benchmarks-used](benchmarks-used.md). That's a reference point, not a target.
- Sample: [calculations §2](calculations.md). Budget = visitors × measured CPC.
- Check **message match** first: ad, headline and form must promise the same thing.

## 3 · Fake door

- Needs an existing product, site or audience. Put the new option where a real decision happens (pricing plan, in-product button, menu).
- After the click, show an honest "not live yet, want early access?" message plus an email field.
- Compare to a similar existing option **on the same page**, not to an internet average.

## 4 · Pre-sale

- Founding price or refundable deposit, a delivery date, and a full-refund promise if you miss it.
- Waitlist first, then the same paid audience.
- Pass line = pre-sales needed to cover the build/stock cost ([calculations §6](calculations.md)).
- In COD markets, take a prepaid deposit; a COD order is a "maybe" ([mena-notes](mena-notes.md)).
- If it falls short, call the people who signed up but didn't pay. Their reasons are the next Step 1.

## After launch

Switch from the ladder to experiments: find the bottleneck (funnel decomposition), rank ideas against it ([experiment-cards](experiment-cards.md) + ICE with written reasoning), and A/B test only when traffic can reach the sample within ~6 weeks ([calculations §4](calculations.md)). Keep one log for the whole journey.
