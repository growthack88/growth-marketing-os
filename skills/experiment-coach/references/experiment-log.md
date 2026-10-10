# Experiment log, plan formats and GrowthLab

## 1 · Log entry (Markdown) — the default output of `plan` and `log`

This matches the repo's [Experiment Log template](https://github.com/growthack88/growth-marketing-os/blob/main/templates/EXPERIMENT_LOG_TEMPLATE.md). Fill in **Before** before the test runs; never edit it afterwards. Fill in **After** at the sample or date.

```markdown
### EXP-[number] · [short name]

**Before**
- Date started:
- Owner:
- Stage: pre-launch step [0–4] · or post-launch
- Riskiest assumption this tests:
- Hypothesis: We believe [audience] will [behavior] because [reason].
- Test: [method] — what exactly runs where
- Primary metric (one only):
- Guardrail metric:
- Sample needed: [n] — how calculated
- Budget / time cap:
- Decision rule:
  - Pass: if [metric] ≥ [line] after [sample] by [date] → [action]
  - Fail: if [metric] < [line] → [action]
  - In between: [the ONE change], rerun once
- Where the lines came from: [economics calc / sourced benchmark + source / previous test]

**After**
- Date ended:
- Result: [value, sample reached, cost]
- Decision: pass / fail / rerun → what we did next
- What surprised us:
- Learning in one sentence:
- Links:
```

Arabic users get the same block with Arabic labels (تجربة-[رقم]، قبل، بعد، الفرضية، المؤشر الأساسي، قاعدة القرار…).

## 2 · Experiment plan JSON (GrowthLab format, v1.0)

Growth Marketing OS publishes a JSON format for experiment plans, shared with **GrowthLab**, a separate simulation app. Its schema lives in the repo at `integrations/growthlab/experiment-plan.schema.json`. Write JSON only when the user asks for it (for GrowthLab, a tracker, or an automation). Otherwise use the Markdown entry.

Required fields: `schema_version` ("1.0"), `title`, `hypothesis`, `segment`, `channel`, `steps` (array of strings), `target_metric` (a metric **name**, never a value), `success_criterion`, `stop_criterion`, `validation_status`, `status`.

Useful optional fields: `id`, `kind` ("factor" | "objection" | "manual"), `riskiest_assumption`, `message_or_offer`, `changed_factor` ("message" | "offer" | "price" | "channel" | "positioning" | "incentive" | "intervention" | null), `control`, `variant`, `evidence` (array of `{persona_name, text, source_kind, …}`), `locale` ("en" | "ar"), `template`, `next_steps` (array of `{asset, url, use}`), `notes`, `created_at`, `updated_at`. No other fields are allowed.

Rules when writing it from a chat:
- `kind: "manual"`.
- `status: "draft"` until the test starts, then "planned" / "running", and finally "won" / "lost" / "inconclusive" / "stopped".
- Thresholds go in `success_criterion` / `stop_criterion` as the user's own lines, or as `[set before launch]` if not decided yet. **Never** put invented percentages in the hypothesis.
- `validation_status`: the v1.0 enum has `unvalidated_simulation_signal`, `validated_in_market` and `invalidated_in_market`. Use `validated_in_market` / `invalidated_in_market` after a real test. For an untested plan that **didn't** come from a simulation, there's no exact value in v1.0. Tell the user, use `unvalidated_simulation_signal` only if they still need schema-valid JSON, and say so in `notes` ("untested hand-written plan; not a simulation signal").

Minimal example:

```json
{
  "schema_version": "1.0",
  "kind": "manual",
  "title": "Smoke test: payment-reminder promise for Egyptian freelancers",
  "riskiest_assumption": "Freelancers will sign up for automated payment reminders",
  "hypothesis": "We believe freelancers in Egypt who chase late payments on WhatsApp will join a waitlist for automated reminders, because interviewees described recent late payments and manual workarounds.",
  "segment": "Freelance designers and developers, Egypt",
  "channel": "Meta ads to a landing page",
  "message_or_offer": "Client gone silent? We remind them for you.",
  "steps": ["Pilot spend to measure CPC", "Run the page to the computed sample", "Read out against the rule"],
  "target_metric": "Visitor-to-waitlist sign-up rate",
  "success_criterion": "≥ [pass line from passline calc] after [n] visitors by [date]",
  "stop_criterion": "< [fail line] after [n] visitors, or the budget cap is reached",
  "validation_status": "unvalidated_simulation_signal",
  "status": "draft",
  "locale": "en",
  "notes": "Untested hand-written plan; not a simulation signal (schema v1.0 has no separate value)."
}
```

## 3 · Importing a GrowthLab export (`import`)

GrowthLab runs launches, messages, offers and prices past **synthetic personas** and exports experiment drafts, as JSON in the format above or as a pre-filled Markdown log entry. When the user pastes one:

1. **Label it.** Everything in `evidence` is synthetic: simulated reactions, not market data. Say so once, plainly. Counts like "0 vs 12 simulated objections" describe the simulation only. Never convert them into expected conversion rates.
2. **Keep what's useful:** the changed factor, the control and variant wording, and the objections, which become interview questions and page copy to test.
3. **Place it on the ladder.** Usually it feeds Step 1 (ask real people about the objections) or Step 2 (test the winning message on real strangers). It never replaces a step.
4. **Fill the blanks GrowthLab leaves on purpose:** pass/fail lines from the user's economics, sample size, budget, dates, guardrail.
5. **Return** a completed log entry, and the updated JSON if they want it (set `status` and keep `kind` as exported).
6. After the real test, set `validation_status` to `validated_in_market` or `invalidated_in_market`.
