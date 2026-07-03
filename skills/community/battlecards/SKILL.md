---
name: battlecards
version: '1.0'
last_updated: 2026-02-06
author: marketing-team
description: Creates competitive battlecards for sales deal conversations. Produces win themes, landmines to plant, objection
  handlers, and competitive positioning per competitor. Outputs a structured markdown battlecard with quick-reference sections
  for live sales calls. Depends on competitor-research for competitive intelligence and consumes product-messaging, win-loss-analysis,
  and positioning for framing. Feeds into sales-deck, outreach-emails, and demo-script. Triggered by "battlecard", "competitive
  intel", "win against [competitor]", or "how do we beat [competitor]".
goal: Creates competitive battlecards for sales deal conversations.
outcome: Creates competitive battlecards for sales deal conversations. Produces win themes, landmines to plant, objection
  handlers, and competitive positioning per competitor. Outputs a structured markdown battlecard with quick-reference sections
  for live sales calls. Depends on competitor-research for...
primitive: sales-enablement
ontology_type: battlecard
review_gate: 2
inputs:
  required: []
  recommended:
  - competitor-research
  - product-messaging
  - win-loss-analysis
  - positioning
outputs:
- type: battlecard
  feeds_into:
  - sales-deck
  - outreach-emails
  - demo-script
depends_on: []
feeds_into:
- demo-script
- outreach-emails
- sales-deck
owned_by_agent: sales
mcps_used: []
push_targets:
- gdrive
triggers:
  slash_commands: []
  natural_language: []
status: draft
locked_by: null
locked_date: null
lock_version: null
sources_count: 0
context: fork
effort: high
---

<!--
COMMUNITY SKILL — included under its original MIT license.
Source: https://github.com/matteotitta/genesys-skills by Matteo Titta (MIT).
License text: ../LICENSE-genesys-skills.txt
Curated into Growth Marketing OS by Mahmoud Omar (mahmoudomar.com) — this file
is NOT original work by the repo author; see /skills/community/README.md.
-->


# Battlecards

Quick-reference competitive intelligence battlecards for live sales conversations. Designed to be scanned in 30 seconds during a call. Supports batch generation for multiple competitors with confidence-level sourcing on every claim.

The body of this file holds decision-grade context (when to invoke, inputs, structure, anti-hallucination guardrails, gotchas). Step-by-step process, output template, quality gates, and feedback loops live in `references/`.

---

## Claude Code triggers

**Invoke this skill when user says:**
- "Create battlecard for [competitor]"
- "Competitive battlecard"
- "How to win against [competitor]"
- "Competitive intel for sales"
- "Battlecards for [product]"
- "Sales battlecard"
- "Counter-positioning against [competitor]"
- "Competitive one-pager" (if focus is on win/lose scenarios)

**Do NOT invoke when:**
- User wants deep competitor research → Use `/competitor-research` skill
- User wants sales deck → Use `/sales-deck` skill
- User wants demo script → Use `/demo-script` skill
- User wants competitive feature comparison only → Use `/competitor-research` skill

---

## Input requirements

### Required inputs

| Input | Description | Source |
|-------|-------------|--------|
| **Competitor name(s)** | Which competitor(s) to create battlecards for | User specifies |
| **Your product context** | What you sell, key capabilities | User, product-messaging, or URL |

### Optional inputs (improve quality)

| Input | How it helps |
|-------|--------------|
| competitor-research output | Pre-researched intel (funding, features, positioning) |
| win-loss-analysis output | When we win/lose patterns with evidence |
| Product messaging | Counter-positioning based on your value props |
| Positioning context | Strategic anchors for competitive framing |
| Competitor URLs | For live research if no prior research exists |
| Sales call transcripts | Real objections and competitive mentions |

### Input validation checklist

Before proceeding, verify:
- [ ] Competitor(s) confirmed
- [ ] Your product's key differentiators known
- [ ] At least one intel source available (research, URL, or docs)

**If inputs are missing:** Ask which competitor(s). Offer to run competitor-research first if no intel available.

---

## Process at a glance

| Phase | Purpose | Output |
|-------|---------|--------|
| 1. Competitor selection | Confirm scope (single vs batch) | Confirmed competitor list |
| 2. Intel gathering | Pull from research + win-loss + web research | Intel dossier per competitor |
| 3. Battlecard generation | Fill template, add confidence levels, write talk tracks + landmines | Draft battlecard(s) |
| 4. Validation & delivery | Verify sources, format for delivery | Final battlecard(s) |

Full step-by-step (with checkpoints, confidence framework, workflow sequences, GDrive export commands) in [`references/process.md`](references/process.md).

---

## Battlecard structure (decision-grade)

Every battlecard contains these sections — in this order, no exceptions:

1. **Quick facts** — Founded, funding, employees, target market, pricing model, starting price (side-by-side table)
2. **When we win** — 3 specific scenarios + verbatim customer proof point
3. **When we lose** — 2+ honest losing scenarios + mitigation actions
4. **Their pitch** — Verbatim competitor language + key claims
5. **Counter-positioning** — Scripted "when they say X, we say Y" responses
6. **Feature comparison** — Honest table with winner-per-row
7. **Landmines to plant** — 3+ discovery questions that expose competitor weaknesses
8. **Objection handling** — Common objections with proof-pointed responses
9. **Red flags** — When to walk away (qualification-out criteria)
10. **Sources** — Every claim with URL + access date + confidence

Full template with field-level guidance in [`references/battlecard-template.md`](references/battlecard-template.md). Output wrapper format and iteration prompts in [`references/auto-update.md`](references/auto-update.md).

---

## Anti-hallucination guardrails

**Critical for sales credibility:**

1. **Never invent competitor claims.** Only use verified data with sources.
2. **Never fabricate customer quotes.** Verbatim only or mark "[PLACEHOLDER: need customer quote]".
3. **Never guess competitor pricing.** Use verified data or mark "[CONFIRM: pricing]".
4. **Mark confidence levels** on all competitive intel (High/Medium/Low/UNVERIFIED).
5. **Cite sources** for all factual claims with access dates.
6. **Acknowledge gaps** rather than fill with plausible content.
7. **Be honest about weaknesses.** "When we lose" builds credibility with sales team.

---

## Gotchas

- **Fabricated competitor pricing**: Invents pricing tiers when pricing page is gated or not found → Mark pricing as [UNAVAILABLE] and note where to find it (sales call, demo request). Never guess.
- **Generic objection handlers**: Produces "we're more reliable" instead of specific counter-arguments → Every objection handler must reference a concrete differentiator or proof point.
- **Missing landmines**: Only covers strengths, forgets to include questions that expose competitor weaknesses → Landmines are the most valuable section for sales reps. 3-5 questions per competitor minimum.
- **Stale competitive data**: Uses old competitor positioning without checking current website → Always scrape competitor website at time of battlecard creation. Note access date.

---

## Integration with other skills

### Upstream skills (provide inputs)

| Skill | What it provides | Required? |
|-------|------------------|-----------|
| **competitor-research** | Company facts, positioning, features, pricing | Recommended |
| **win-loss-analysis** | Win/loss patterns, objections, proof points | Recommended |
| **product-messaging** | Your value props for counter-positioning | Recommended |
| **positioning** | Strategic competitive anchors | Optional |

### Downstream skills (consume outputs)

| Skill | How it uses battlecards |
|-------|-------------------------|
| **sales-deck** | Differentiation slide content |
| **demo-script** | Objection handling during demos |
| **outreach-emails** | Competitive displacement email content |

---

## Reference files

| File | Purpose |
|------|---------|
| [`references/process.md`](references/process.md) | 4-phase runbook + flowchart + confidence framework + workflow sequences |
| [`references/battlecard-template.md`](references/battlecard-template.md) | Complete battlecard structure with field-level examples |
| [`references/quality.md`](references/quality.md) | Pre-delivery checklist + self-evaluation protocol + anti-examples |
| [`references/auto-update.md`](references/auto-update.md) | Output wrapper, iteration prompts, feedback signal detection, pattern rules |

---

## MCP data integration

**Level:** 2 — PM Execution (inherits upstream, no unique pulls)

**Inherits from:** competitor-research, win-loss-analysis, product-messaging

**Pulls fresh:** NONE — all data comes from upstream. Battlecards synthesize existing competitor research and win-loss patterns.

**Fallback (no MCP):** Use competitor-research and win-loss-analysis outputs directly. If upstream skills haven't run, trigger them first before running battlecards.

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-06 | Initial skill creation. Extracted from sales-enablement with dedicated process, confidence framework, batch support, and Google Docs/PDF export |
| 1.1 | 2026-05-01 | Slim refactor: extracted process, quality, and auto-update protocol to references/ (Phase 4.5.1.C) |
