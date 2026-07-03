# Quality — pre-delivery checklist + worked example

Run these gates before handing the win/loss report to the user. Then check the worked example to calibrate "good."

---

## Pre-delivery checklist

### Evidence quality
- [ ] Every insight traces to verbatim quote with speaker attribution
- [ ] Frequency counts provided (X of Y calls)
- [ ] Confidence levels assigned to all patterns
- [ ] No invented patterns — all findings grounded in transcript text

### Analysis quality
- [ ] All 6 dimensions addressed or marked "Not discussed"
- [ ] Cross-references analyzed when context docs provided
- [ ] Win/loss reasons limited to 1-3 per dimension (prioritized)
- [ ] Actionable opportunities provided for each dimension

### Format quality
- [ ] Output header with date and font specification
- [ ] Executive summary is actionable
- [ ] Data gaps documented with suggested follow-ups

---

## What good looks like — Batch analysis (8 calls)

**Input context:**
```
8 sales call transcripts
5 wins, 3 losses
Product: B2B SaaS analytics platform
```

**Expected output excerpt:**
```markdown
## Executive Summary

Across 8 analyzed calls (5 wins, 3 losses), product-market fit is strong for mid-market teams seeking self-serve analytics. Wins consistently cite "ease of setup" and "no SQL required" (4 of 5 wins). Losses cluster around enterprise requirements — missing SSO and audit logs mentioned in all 3 losses. Pricing was not a factor in any loss.

**Strategic recommendations:**
1. Prioritize enterprise security features (SSO, audit logs) to unlock enterprise segment
2. Double down on "no SQL required" messaging — strongest resonance
3. Train sales on handling "security review" objection with roadmap response

---

### 1. Product

**Pattern:** Ease of setup and self-serve capability drive wins; missing enterprise security features drive losses.

**Evidence (Wins):**
> "We were up and running in 2 hours. No SQL, no engineering dependency. That's exactly what we needed."
> — Champion (Head of RevOps), Acme Corp, Win

**Evidence (Losses):**
> "Your product is great, but without SSO and audit logs, we can't get through security review."
> — Economic Buyer (VP Engineering), TechCo, Loss

**Frequency:** Setup ease: 4 of 5 wins | Security gaps: 3 of 3 losses
**Confidence:** High

**Opportunity:** Add SSO and audit logs to roadmap; create "enterprise security" FAQ for sales to handle objection.
```

**Why this works:** executive summary is actionable; every insight has verbatim quote with attribution; frequency and confidence explicitly stated; clear opportunity recommendation.

---

## Anti-examples (what to avoid)

| Bad pattern | Why it's bad | Better approach |
|-------------|--------------|-----------------|
| "Customers like the product" | No verbatim evidence | Quote specific words with attribution |
| "Pricing is an issue" (1 call) | Single mention labeled as pattern | Label as "Single mention — pattern unconfirmed" |
| Paraphrased quotes | Violates verbatim rule | Use exact words from transcript |
| No frequency counts | Can't assess pattern strength | Always include "X of Y calls" |
