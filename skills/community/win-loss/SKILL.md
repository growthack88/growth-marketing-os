---
name: win-loss-analysis
version: "2.0"
author: genesys-growth
last_updated: 2026-06-08
description: >
  Win/loss analysis for B2B SaaS. Analyzes sales call transcripts across
  6 dimensions (product, messaging, GTM/sales, pricing, competition,
  customer context) to extract why deals are won, lost, retained, or
  churned. Produces aggregate patterns with verbatim-quote evidence,
  frequency counts, confidence levels, and strategic recommendations.
  Includes process steps, output template, quality checklist, extraction
  patterns, and a worked 5-transcript example.
---

<!--
COMMUNITY SKILL — included under its original MIT license.
Source: https://github.com/matteotitta/genesys-skills by Matteo Titta (MIT).
License text: ../LICENSE-genesys-skills.txt
Curated into Growth Marketing OS by Mahmoud Omar (mahmoudomar.com) — this file
is NOT original work by the repo author; see /skills/community/README.md.
-->


# Win/loss analysis

Analyze sales call transcripts to extract actionable insights on why deals are won, lost, retained, or churned. Cross-reference findings with ICP, firmographics, and competitive context to produce strategic recommendations.

**Knowledge type:** `win-loss-analysis`
**Maturity on first run:** emergent → validated after team review

---

## Claude Code triggers

**Invoke when user says:**
- "Win/loss analysis"
- "Analyze sales calls"
- "Why did we win/lose"
- "Churn analysis"
- "Retention analysis"
- "Sales call insights"
- "Deal outcome patterns"
- "Customer feedback synthesis"
- "Analyze these transcripts"
- "What patterns in our sales calls"

**Do NOT invoke when:**
- User wants general transcript analysis → use a generic transcript skill
- User wants competitor research → use `competitor-research`
- User wants a single customer interview write-up → use a transcript skill
- User wants sales enablement assets → use a sales-enablement skill

---

## Input requirements

### Required

| Input | Description | Source |
|-------|-------------|--------|
| **Transcripts** | Sales call transcripts with customer name and outcome | User provides |
| **Outcome** | Win/Loss/Retention/Churn for each call | User specifies or infer |

### Optional (improve quality)

| Input | How it helps |
|-------|--------------|
| Website URL per customer | Firmographics cross-reference |
| Product/ICP document | Define in-scope product capabilities |
| Market/GTM document | Positioning and competitive landscape |
| Sales notes column | Additional context (stage, deal size) |
| Competitor names | Pre-identify competitors to watch for |

### Validation

Before proceeding: at least one transcript provided; outcome known or inferable from transcript; customer name identifiable.

If inputs are missing: ask the user for transcripts. Clarify if outcome should be inferred from transcript signals.

### Transcript intake — normalize, redact, bind to evidence

Transcripts arrive in many shapes (Gong, Fireflies, Otter, Grain, Zoom/Avoma VTT, SRT, recorder JSON, or plain pasted text). Before Phase 1, normalize whatever you're handed into one shape — speaker-attributed turns with timestamps where present. Two rules apply to every transcript before analysis:

- **Redact PII first.** Mask end-client names, emails, and account numbers before processing; keep roles, company, and deal context. (Load-bearing for regulated industries.)
- **Bind every claim to evidence.** Every extracted pattern cites a verbatim quote plus the speaker; normalized, speaker-attributed turns make that attribution reliable.

---

## Process

The analysis runs in 3 phases. Read [`references/process.md`](./references/process.md) for the full step-by-step (4 transcript-processing steps, 4 aggregation steps, 4 synthesis steps, plus per-phase checkpoints and the process flowchart).

Phase summary:

1. **Transcript processing** — classify outcome, identify speakers, extract customer context, pull verbatim quotes for the 6 dimensions
2. **Pattern aggregation** — group by outcome, count frequency, rank patterns (3+ mentions), cross-reference by ICP/competitor/persona
3. **Insight synthesis** — state pattern, provide evidence with frequency + confidence, identify opportunity, generate executive summary

---

## Core frameworks

### Analysis modes

| Mode | When to use | Output |
|------|-------------|--------|
| **Single call** | Deep analysis of one transcript | Full insight extraction per dimension |
| **Batch analysis** | Multiple transcripts (3-20 calls) | Aggregated patterns with frequency counts |
| **Comparison matrix** | Win vs. loss OR retention vs. churn | Side-by-side pattern comparison |

**Default to batch analysis mode** when multiple transcripts are provided.

### 6 analysis dimensions

| # | Dimension | Win signals | Loss signals |
|---|-----------|-------------|--------------|
| 1 | **Product** | "Exactly what we need," feature praised | "Missing [feature]," "Doesn't do [X]" |
| 2 | **Messaging** | "Now I understand why this matters" | "What does it actually do?" |
| 3 | **GTM/Sales** | "You really understand our problem" | "Demo didn't address our needs" |
| 4 | **Pricing** | "Fair price," "good value" | "Too expensive," "over budget" |
| 5 | **Competition** | "Chose you over [competitor]" | "Going with [competitor]" |
| 6 | **Customer context** | "Need this now," deadline-driven | "No rush," "maybe next year" |

### Confidence scoring

| Level | Definition | When to apply |
|-------|------------|---------------|
| **High** | 3+ calls with consistent pattern | Clear recurring theme |
| **Medium** | 2 calls or inferred from strong signals | Emerging pattern |
| **Low** | Single mention or indirect reference | Possible outlier |

### Outcome classification

| Outcome | Definition | Key signals |
|---------|------------|-------------|
| **Win** | Deal closed, contract signed | "We're moving forward," pricing confirmed |
| **Loss** | Deal lost to competitor or no-decision | "Going with [competitor]," "Not right now" |
| **Retention** | Existing customer renewing/expanding | Renewal discussion, expansion |
| **Churn** | Existing customer leaving/reducing | Cancellation, "not getting value" |

---

## Output

Produce a single win/loss report markdown file. Template + iteration prompts library: [`references/output-format.md`](./references/output-format.md).

Pre-delivery quality checklist + worked example + anti-examples: [`references/quality.md`](./references/quality.md).

Auto-update protocol (feedback signals, pattern detection, skill-update template): [`references/auto-update.md`](./references/auto-update.md).

---

## Anti-hallucination guardrails

1. **Quote verbatim.** All insights must trace to specific transcript quotes.
2. **Never invent patterns.** If a pattern appears in only one call, label it "Single mention — pattern unconfirmed."
3. **State frequency.** Always note how many calls support each finding (e.g., "4 of 7 calls").
4. **Acknowledge gaps.** If a dimension has no data, mark "Not discussed in transcripts."
5. **Distinguish roles.** Tag who said what — prospect vs. sales rep vs. champion.

---

## Gotchas

- **Correlation as causation.** Reports "deals with longer sales cycles were lost" as if cycle length caused the loss → always distinguish patterns from causes. Use "associated with" not "caused by".
- **Small sample bias.** Draws conclusions from 2-3 deals instead of waiting for sufficient data → flag sample size prominently. Minimum 5 wins and 5 losses for reliable patterns.
- **Missing verbatim quotes.** Summarizes what buyers said instead of extracting exact quotes → verbatim quotes are the primary deliverable. Summaries are secondary.
- **Single-dimension analysis.** Only looks at win/loss by competitor, missing dimensions like deal size, ICP segment, or sales cycle stage → cross-tabulate across at least 3 dimensions.
- **Conflates product feedback with sales insights.** Mixes "they wanted feature X" with "they didn't trust our team" → separate product gaps from sales execution issues. They feed into different downstream work.

---

## Integration with other skills

| Skill | Relationship | Usage |
|-------|--------------|-------|
| **transcript analysis** | Related | Use for general transcripts, not sales calls |
| **sales enablement** | Downstream | Feed insights into battlecards and objection handlers |
| **product messaging** | Downstream | Update messaging based on win patterns |
| **competitor research** | Related | Cross-reference competitor mentions |

---

## Reference files

| File | Purpose |
|------|---------|
| [`references/process.md`](./references/process.md) | Full 3-phase step-by-step + flowchart |
| [`references/output-format.md`](./references/output-format.md) | Win/loss report template + iteration prompts |
| [`references/quality.md`](./references/quality.md) | Pre-delivery checklist + worked example + anti-examples |
| [`references/auto-update.md`](./references/auto-update.md) | Feedback signal detection + pattern rules |
| [`references/extraction-patterns.md`](./references/extraction-patterns.md) | Signal patterns for each dimension |
| [`references/output-template.md`](./references/output-template.md) | Legacy report template (kept for reference) |
| [`references/example-analysis.md`](./references/example-analysis.md) | Worked example with 5 transcripts |

---

## Data integration

**Level:** 0 — Context (heavy pulls)

If you run win/loss inside a connected environment, pull transcripts and deal context fresh:

| Source | What to pull | When |
|--------|-------------|------|
| **Meeting recorder** (Granola, Gong, Fireflies, etc.) | Sales call transcripts and deal discussions | Always |
| **Team chat** (Slack, etc.) | Deal discussion threads and competitive intel | Always |

**Fallback (no integrations):** user-provided call transcripts or recordings; manual deal review notes.

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 2.0 | 2026-01-16 | Refactored to v2.0 template: structured phases, evidence-ready insights, iteration prompts, auto-update rules |
| 1.0 | Previous | Initial skill creation with 6 dimensions |
