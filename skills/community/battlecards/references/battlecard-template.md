# Battlecard template

Quick-reference competitive intelligence for sales conversations. Designed to be scanned in 30 seconds during a call.

## Structure

```markdown
# Battlecard: [Your Product] vs [Competitor]

**Last updated**: [YYYY-MM-DD]
**Confidence**: High/Medium/Low (based on source quality)

---

## Quick facts

| Attribute | [Competitor] | [Your Product] |
|-----------|--------------|----------------|
| Founded | [Year] | [Year] |
| Funding | [Amount] | [Amount] |
| Employees | [Range] | [Range] |
| Target market | [Segment] | [Segment] |
| Pricing model | [Model] | [Model] |
| Starting price | [Price] | [Price] |

---

## When we win

**Scenarios where we consistently beat [Competitor]:**

1. **[Scenario 1]**: [Brief explanation — 1 sentence]
2. **[Scenario 2]**: [Brief explanation]
3. **[Scenario 3]**: [Brief explanation]

**Proof point**: "[Verbatim customer quote about winning scenario]" — [Name], [Title], [Company]

---

## When we lose

**Scenarios where [Competitor] has advantage:**

1. **[Scenario 1]**: [Brief explanation]
2. **[Scenario 2]**: [Brief explanation]

**How to mitigate**: [Action sales can take]

---

## Their pitch (what they say)

> "[Competitor's key value prop — exact language from their site]"

**Positioning**: [How they position themselves]
**Key claims**: 
- [Claim 1]
- [Claim 2]
- [Claim 3]

---

## Counter-positioning (what we say)

**When they say**: "[Competitor claim]"
**We say**: "[Our response — specific, factual]"

**When they say**: "[Competitor claim 2]"
**We say**: "[Our response 2]"

---

## Feature comparison

| Capability | [Competitor] | [Your Product] | Winner |
|------------|--------------|----------------|--------|
| [Feature 1] | [Status/Detail] | [Status/Detail] | ✅ Us / ❌ Them / ⚖️ Tie |
| [Feature 2] | [Status/Detail] | [Status/Detail] | |
| [Feature 3] | [Status/Detail] | [Status/Detail] | |

**Our unique advantages:**
- [Advantage 1 — not available in competitor]
- [Advantage 2]

**Their unique advantages:**
- [Advantage 1 — be honest]
- [Advantage 2]

---

## Landmines to plant

Questions to ask prospect that expose competitor weaknesses:

1. "How important is [capability we have, they don't]?"
2. "Have you evaluated [limitation area] in other solutions?"
3. "What's your timeline for [thing we can do faster]?"

---

## Objection handling

**"[Competitor] is cheaper"**
> [Response with value justification]

**"[Competitor] has [feature]"**
> [Response — acknowledge if true, reframe if needed]

**"We're already using [Competitor]"**
> [Response for displacement scenario]

---

## Red flags (when to walk away)

- [Disqualification criteria 1]
- [Disqualification criteria 2]
- [Disqualification criteria 3]

---

## Sources

| Data point | Source | Accessed |
|------------|--------|----------|
| [Claim] | [URL] | [YYYY-MM-DD] |
```

## Required data sources

To build a complete battlecard, gather from:

| Section | Primary source | Skill reference |
|---------|----------------|-----------------|
| Quick facts | Competitor website, Crunchbase | competitor-research |
| When we win/lose | Sales call transcripts | win-loss-analysis |
| Their pitch | Competitor homepage, features page | competitor-research |
| Feature comparison | Both product pages, G2 | competitor-research |
| Objections | Win/loss transcripts | win-loss-analysis |

## Confidence levels

| Level | Definition | Display |
|-------|------------|---------|
| High | Verified from official source or 3+ win/loss calls | No marker needed |
| Medium | Secondary source or 1-2 calls | Mark with (Medium) |
| Low | Single indirect mention or inference | Mark with (Low — verify) |

## Design principles

1. **Scannable in 30 seconds** — Sales reps use these during calls
2. **Actionable over informational** — Every section should guide action
3. **Honest about weaknesses** — Builds credibility with sales team
4. **Updated regularly** — Stale intel damages trust

## Example: Partial battlecard

```markdown
# Battlecard: Acme CRM vs Salesforce

**Last updated**: 2025-01-15
**Confidence**: High

---

## When we win

1. **Mid-market companies ($10-50M ARR)**: Salesforce is overkill; we deploy in days not months
2. **Sales teams <50 reps**: Our per-seat pricing beats their enterprise tiers
3. **Companies without dedicated Salesforce admin**: We require zero admin overhead

**Proof point**: "We cut our CRM costs by 60% and our reps actually use it now." — Sarah Chen, VP Sales, TechStart Inc.

---

## When we lose

1. **Enterprise (500+ employees)**: They need Salesforce ecosystem integrations
2. **Heavy customization requirements**: Our flexibility has limits

**How to mitigate**: Ask early about integration requirements and customization needs to qualify out fast.

---

## Landmines to plant

1. "What's your current Salesforce admin headcount?"
2. "How long did your last CRM implementation take?"
3. "What percentage of your CRM features do reps actually use?"
```

## Workflow

1. **Gather competitor intel** — Run competitor-research skill or provide URL
2. **Pull win/loss patterns** — Reference win-loss-analysis output if available
3. **Draft battlecard** — Fill template sections
4. **Validate claims** — Ensure every fact has a source
5. **Add confidence markers** — Tag any uncertain data
6. **Format for delivery** — Markdown for internal wiki, PDF for print
