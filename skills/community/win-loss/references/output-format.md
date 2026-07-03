# Output format — win/loss report template

The skill produces a single win/loss report markdown file. Use this template verbatim, filling bracketed placeholders.

---

```markdown
<!--
SKILL OUTPUT: Win/Loss Analysis
Generated: YYYY-MM-DD
Font: Inter (for rendering)
Version: 2.0
-->

# Win/loss analysis report

**Analysis date:** [YYYY-MM-DD]
**Transcripts analyzed:** [N]
**Outcome breakdown:** [X wins / Y losses] or [X retained / Y churned]

---

## Executive Summary

[3-5 sentences on key findings and strategic recommendations]

---

## Win/Loss Reasons Matrix

| Dimension | Win Reasons | Loss Reasons | Evidence (calls) |
|-----------|-------------|--------------|------------------|
| Product | [1-3 reasons] | [1-3 reasons] | [X of Y calls] |
| Messaging | [1-3 reasons] | [1-3 reasons] | [X of Y calls] |
| GTM/Sales | [1-3 reasons] | [1-3 reasons] | [X of Y calls] |
| Pricing | [1-3 reasons] | [1-3 reasons] | [X of Y calls] |
| Competition | [1-3 reasons] | [1-3 reasons] | [X of Y calls] |
| Customer context | [1-3 reasons] | [1-3 reasons] | [X of Y calls] |

---

## Insights by Dimension

### 1. Product

**Pattern:** [One-sentence summary]

**Evidence:**
> "[Verbatim quote]"
> — [Speaker role], [Customer name], [Outcome]

**Frequency:** [X of Y calls] | **Confidence:** High/Medium/Low

**Opportunity:** [Actionable recommendation]

---

### 2. Messaging

**Pattern:** [One-sentence summary]

**Evidence:**
> "[Verbatim quote]"
> — [Speaker role], [Customer name], [Outcome]

**Frequency:** [X of Y calls] | **Confidence:** High/Medium/Low

**Opportunity:** [Actionable recommendation]

---

[Continue for all 6 dimensions]

---

## Cross-Reference Analysis

### By ICP Segment

| Segment | Win Rate | Top Win Reason | Top Loss Reason |
|---------|----------|----------------|-----------------|
| [Segment 1] | [X/Y] | [Reason] | [Reason] |

### By Competitor

| Competitor | Head-to-Head | Why We Win | Why We Lose |
|------------|--------------|------------|-------------|
| [Competitor 1] | [X wins / Y losses] | [Reasons] | [Reasons] |

### By Persona

| Persona | Win Rate | Key Patterns |
|---------|----------|--------------|
| [Persona 1] | [X/Y] | [Patterns] |

---

## Verbatim Evidence Library

### Win Quotes by Dimension

**Product:**
> "[Quote]" — [Speaker], [Customer], [Outcome]

**Messaging:**
> "[Quote]" — [Speaker], [Customer], [Outcome]

[Continue for all dimensions]

### Loss Quotes by Dimension

[Same structure]

---

## Data Gaps

| Gap | Impact | Suggested Follow-up |
|-----|--------|---------------------|
| [What's missing] | [Impact] | [How to fill] |

---

## Iteration Prompts

After reviewing this analysis, consider:
1. "Should I create competitive battlecards from these insights?"
2. "Want me to update product messaging based on win patterns?"
3. "Should I analyze additional transcripts?"
```

---

## Iteration prompts library

### Refinement
1. "Should I dig deeper on any dimension?"
2. "Want me to re-analyze with different outcome groupings?"
3. "Should I expand the cross-reference analysis?"

### Expansion
1. "Ready to create competitive battlecards from these insights?"
2. "Should I update product messaging based on win patterns?"
3. "Want me to generate objection handlers from loss reasons?"

### Quality
1. "Any patterns that seem off based on your experience?"
2. "Should I verify any insights with additional context?"
3. "Want me to look for additional patterns in the data?"
