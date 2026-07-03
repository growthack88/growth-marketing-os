# Battlecards — Process

Full 4-phase runbook for producing competitive battlecards. The body of SKILL.md keeps a compact phase summary; this file holds the step-by-step.

---

## Process flowchart

```
┌──────────────────────────────────────────────────────────────┐
│                    BATTLECARD PROCESS                          │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│ INPUT VALIDATION                                              │
│ Required:                                                    │
│ □ Competitor name(s)                                         │
│ □ Your product context (what you sell)                       │
│ Optional:                                                    │
│ □ competitor-research output                                 │
│ □ win-loss-analysis output                                   │
│ □ Competitor URLs for live research                          │
│ → If missing: Ask which competitor(s), offer to run research │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│ PHASE 1: COMPETITOR SELECTION                                 │
│ Step 1.1: Confirm competitor(s) to build battlecards for     │
│ Step 1.2: For batch: list all competitors, confirm scope     │
│ → Output: Confirmed competitor list                          │
│ ✓ Checkpoint: Competitor(s) confirmed                        │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│ PHASE 2: INTEL GATHERING                                      │
│ Step 2.1: Pull from competitor-research output (if available)│
│ Step 2.2: Pull from win-loss-analysis (if available)         │
│ Step 2.3: Web research for gaps (competitor site, G2, etc.)  │
│ Step 2.4: Cross-reference with positioning context           │
│ → Output: Intel dossier per competitor                       │
│ ✓ Checkpoint: Sufficient intel for all template sections     │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│ PHASE 3: BATTLECARD GENERATION                                │
│ Step 3.1: Fill template structure per competitor             │
│ Step 3.2: Add confidence levels to all claims                │
│ Step 3.3: Write counter-positioning and talk tracks          │
│ Step 3.4: Generate landmine questions                        │
│ → Output: Draft battlecard(s)                                │
│ ✓ Checkpoint: All sections filled, claims sourced            │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│ SELF-EVALUATION                                               │
│ □ All claims sourced with confidence levels?                 │
│ □ No invented competitor data?                               │
│ □ Scannable in 30 seconds?                                   │
│ □ Objection responses are scripted (not generic)?            │
│ □ Landmine questions are specific and tactical?              │
│ → Output: Improvement suggestions if needed                  │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│ PHASE 4: VALIDATION & DELIVERY                                │
│ Step 4.1: Verify all claims sourced                          │
│ Step 4.2: Mark confidence levels                             │
│ Step 4.3: Format for delivery (MD, Google Docs, PDF)         │
│ → Output: Final battlecard(s)                                │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│ CHAIN SUGGESTIONS                                             │
│ → If battlecard approved: Suggest sales-deck, demo-script    │
│ → If multiple competitors: Offer competitive matrix          │
│ → Export: Google Docs, PDF                                   │
└──────────────────────────────────────────────────────────────┘
```

---

## Phase 1: Competitor selection

**Purpose:** Confirm scope of battlecard work.

**Steps:**

1. **Step 1.1: Confirm competitors**
   - Single competitor → Proceed to Phase 2
   - Multiple competitors → List all, confirm which to build
   - **Output:** Confirmed competitor list

2. **Step 1.2: Batch scope** (if multiple)
   - How many battlecards needed?
   - Priority order?
   - Same depth for all or priority tiers?
   - **Output:** Scoped batch plan

**Phase 1 checkpoint:**
- [ ] Competitor(s) confirmed
- [ ] Scope defined (single or batch)

---

## Phase 2: Intel gathering

**Purpose:** Assemble all competitive intelligence.

**Steps:**

1. **Step 2.1: Pull existing research**
   - Check for competitor-research skill output
   - Extract: company facts, positioning, features, pricing, reviews
   - **Output:** Existing intel summary

2. **Step 2.2: Pull win-loss patterns**
   - Check for win-loss-analysis output
   - Extract: when we win, when we lose, common objections
   - **Output:** Win/loss patterns

3. **Step 2.3: Fill gaps with research**
   - If needed: research competitor website, G2, Crunchbase
   - Mark all new research with sources and confidence
   - **Output:** Gap-filled intel

4. **Step 2.4: Cross-reference positioning**
   - If positioning context available: pull competitive anchors
   - Align counter-positioning with strategic positioning
   - **Output:** Positioning-aligned intel

**Phase 2 checkpoint:**
- [ ] Company facts gathered (founded, funding, team, market)
- [ ] Positioning understood (their pitch, key claims)
- [ ] Win/loss patterns identified
- [ ] Feature comparison data available

---

## Phase 3: Battlecard generation

**Purpose:** Create the battlecard following template structure.

**Steps:**

1. **Step 3.1: Fill template** (see `battlecard-template.md`)
   - Quick facts table
   - When we win / when we lose
   - Their pitch / our counter-positioning
   - Feature comparison
   - **Output:** Draft battlecard

2. **Step 3.2: Confidence levels**
   - High: Primary source, verified (3+ data points)
   - Medium: Secondary source, reasonable confidence (1-2 sources)
   - Low: Inferred or single indirect mention
   - UNVERIFIED: Claim needs verification
   - **Output:** Confidence-tagged battlecard

3. **Step 3.3: Talk tracks**
   - Counter-positioning scripts (when they say X, we say Y)
   - Objection responses with proof points
   - Displacement scenario scripts
   - **Output:** Scripted responses

4. **Step 3.4: Landmine questions**
   - Questions that expose competitor weaknesses
   - Specific enough to use in discovery calls
   - Tied to your strengths
   - **Output:** Landmine question list

**Phase 3 checkpoint:**
- [ ] All template sections filled
- [ ] Confidence levels on all claims
- [ ] Talk tracks are scripted (not generic)
- [ ] Landmines are specific and tactical

---

## Phase 4: Validation & delivery

**Purpose:** Verify and deliver.

**Steps:**

1. **Step 4.1: Source verification**
   - Every factual claim has a source
   - Gaps marked as [UNVERIFIED]
   - **Output:** Verified battlecard

2. **Step 4.2: Format for delivery**
   - **Markdown:** Primary format for internal wikis and quick reference
   - **PDF:** Via document skills for print distribution
   - **Output:** Formatted battlecard

**Phase 4 checkpoint:**
- [ ] All claims sourced or marked
- [ ] Correct format for delivery

---

## Confidence level framework

| Level | Definition | Display | Action |
|-------|------------|---------|--------|
| **High** | Verified from official source or 3+ win/loss calls | No marker needed | Use freely |
| **Medium** | Secondary source or 1-2 calls | Mark with (Medium) | Use with caveat |
| **Low** | Single indirect mention or inference | Mark with (Low — verify) | Flag for verification |
| **UNVERIFIED** | No source, needs validation | Mark with [UNVERIFIED] | Do not use in sales calls |

---

## Workflow sequences

**Standard battlecard flow:**
```
competitor-research → battlecards → sales-deck (differentiation slide)
        ↑                              ↓
  win-loss-analysis              demo-script (objection handlers)
```

**Full competitive arsenal:**
```
competitor-research + win-loss-analysis + product-messaging
                              │
                              ▼
                    ┌─────────┼─────────┐
                    ▼         ▼         ▼
              battlecard  comp matrix  sales deck
                    │                     │
                    └──────────┬──────────┘
                               ▼
                    demo-script + outreach emails
```
