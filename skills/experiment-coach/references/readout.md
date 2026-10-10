# Readouts, verdicts and postmortems

## 1 · Before reading any result

1. **Find the rule.** What were the pre-written primary metric, pass line, fail line, sample and date? If there was none, label the readout *exploratory*, give a cautious read, and write the rule for a rerun.
2. **Sample reached?** If not, the answer is "keep running" (or "stop for cost", if the cap was hit). Don't judge early.
3. **Data is trustworthy?** Check the event fired once per conversion, there were no tracking changes mid-test, bot/spam sign-ups were removed, and for A/B tests the traffic split passes the SRM check ([calculations §7](calculations.md)).
4. **Same conditions?** For A/B tests, were both arms running at the same time to the same audience? If not, the result is directional.

## 2 · Pre-launch readouts (ladder steps)

Compare the observed metric to the pre-written lines:
- **≥ pass** → move to the next step. Note what to carry forward (winning promise, segment, phrases).
- **< fail** → stop or re-target. Say what *was* learned. A clean "no" is a result.
- **In between** → name the **one** most likely cause and the one change to make. Rerun once.

Common in-between causes to check first, cheapest first:
1. Message mismatch: the ad promised something the page didn't deliver.
2. Wrong audience: the segment that passed interviews wasn't the one targeted.
3. Friction: a long form, slow page, or missing payment method.
4. Offer or price: only once 1–3 are ruled out.

Show the uncertainty: give the observed rate with a ± range ([calculations §2](calculations.md)) so the user can see when the result is close to a line.

## 3 · A/B readouts

Report in this order:
1. Verdict (ship B / keep A / no reliable difference / test invalid).
2. The primary metric for A and B, the difference in points and relative %, the 95% CI, and the p-value.
3. Guardrail metrics: if a guardrail got worse, don't ship even if the primary metric won.
4. Validity notes: sample reached, SRM, test length covering full weeks, novelty effects.

Rules: never stop the moment p dips under 0.05 (peeking inflates false wins). Don't slice into segments after the fact to find a winner. Segment findings are hypotheses for the next test. "No difference" means the change didn't matter at this size. Keep the simpler or cheaper version.

## 4 · Writing the verdict

```
VERDICT: [continue to Step N / rerun with one change: X / stop / ship B / keep A / invalid — fix Y]
WHY: [metric] was [value ± range] vs pass [x] / fail [y], on [n] after [days].
CARRY FORWARD: [what the next test inherits]
NEXT TEST: [one line + its decision rule]
```

## 5 · Postmortem (`postmortem`)

1. **What we expected** (the hypothesis and rule, copied from the log, not rewritten).
2. **What happened** (numbers, sample, cost, dates).
3. **Why we think it happened**, labelled *measured* or *hypothesis*.
4. **What we'd do differently** in the test design (not just the idea).
5. **What the next test inherits**: one sentence that goes into the log's "Learning" line.
6. **Decision** taken and its date.

Keep the losers. A stopped idea with a logged reason saves the next team weeks.
