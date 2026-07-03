# Process — full step-by-step (3 phases)

The win-loss analysis runs in 3 phases: transcript processing → pattern aggregation → insight synthesis. Read this when running the skill end-to-end.

---

## Phase 1: Transcript processing

**Purpose:** Classify and extract raw data from each transcript.

**Steps:**

1. **Step 1.1: Classify outcome**
   - Win: "We're moving forward," pricing confirmed, implementation scheduled
   - Loss: "Going with [competitor]," "Not right now," "Budget cut"
   - Retention: Renewal discussion, expansion, upsell
   - Churn: Cancellation, downgrade, "not getting value"
   - **Output:** Outcome classification per transcript

2. **Step 1.2: Identify speakers**
   - Tag prospect vs. sales rep vs. champion
   - Distinguish roles for attribution
   - **Output:** Speaker map

3. **Step 1.3: Extract customer context**
   - Company name and URL
   - Inferred firmographics (size, industry if mentioned)
   - Role/persona of primary contact
   - Deal context (stage, competitors mentioned)
   - **Output:** Customer context per transcript

4. **Step 1.4: Extract verbatim quotes**
   - Pull quotes for each of 6 dimensions
   - Tag speaker and timestamp
   - Note signal type (win/loss indicator)
   - **Output:** Quote library

**Phase 1 checkpoint:** all transcripts classified by outcome; speakers identified; quotes extracted with attribution.

---

## Phase 2: Pattern aggregation

**Purpose:** Identify patterns across multiple transcripts.

**Steps:**

1. **Step 2.1: Group by outcome** — wins vs. losses OR retention vs. churn → grouped transcripts
2. **Step 2.2: Count frequency per insight** — e.g., "Pricing mentioned as issue: 5 of 8 losses" → frequency counts
3. **Step 2.3: Identify top patterns** — sort by frequency; prioritize patterns with 3+ mentions → ranked patterns
4. **Step 2.4: Cross-reference with context** — ICP segment / competitor / persona correlation → cross-reference analysis

**Phase 2 checkpoint:** patterns grouped by outcome; frequency counts calculated; cross-references analyzed.

---

## Phase 3: Insight synthesis

**Purpose:** Convert patterns into actionable insights.

**Steps:**

1. **Step 3.1: State each pattern** — 1-2 sentence summary
2. **Step 3.2: Provide evidence** — verbatim quotes with attribution; frequency and confidence level
3. **Step 3.3: Identify opportunities** — what could change the outcome? actionable recommendation
4. **Step 3.4: Generate executive summary** — key findings + strategic recommendations

**Phase 3 checkpoint:** all patterns have evidence; opportunities identified per dimension; executive summary complete.

---

## Process flowchart

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   INPUT     │───▶│ TRANSCRIPT  │───▶│   PATTERN   │───▶│   INSIGHT   │───▶│   REVIEW    │
│ VALIDATION  │    │ PROCESSING  │    │ AGGREGATION │    │  SYNTHESIS  │    │   & CHAIN   │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

**Self-evaluation gate** (before review): every insight traces to verbatim quote with speaker attribution; frequency counts provided (X of Y calls); no invented patterns (single mentions labeled "pattern unconfirmed"); all 6 dimensions addressed or marked "Not discussed in transcripts".

**Review gate:** Level 2 (Spot Check). Chain into `sales-enablement` (battlecards from insights), `product-messaging` (update based on wins), `competitor-research` (cross-ref mentions).
