# Battlecards — Auto-update protocol

How the skill detects feedback signals and proposes updates. The body of SKILL.md points here; this file holds the operational rules.

---

## Output format wrapper

```markdown
<!--
SKILL OUTPUT: Battlecard
Generated: YYYY-MM-DD
Competitor: [Competitor Name]
Your Product: [Product Name]
Overall Confidence: High/Medium/Low
Version: 1.0
-->

# Battlecard: [Your Product] vs [Competitor]

[Full battlecard content following template in `battlecard-template.md`]

---

## Confidence Legend

| Level | Meaning |
|-------|---------|
| **High** | Primary source, verified |
| **Medium** | Secondary source, reasonable confidence |
| **Low** | Inferred or single source |
| **[UNVERIFIED]** | Claim needs verification |
```

---

## Iteration prompts (after delivery)

1. "Want me to create battlecards for additional competitors?"
2. "Should I add more objection handlers?"
3. "Want me to research specific claims further?"
4. "Should I export to Google Docs for distribution?"

---

## Feedback signal detection

| User signal | Interpretation | Action |
|-------------|----------------|--------|
| "Sales found this useful" | High quality match | Capture as reference |
| "This claim is wrong" | Accuracy issue | Log correction, update source |
| "Need more depth on [area]" | Expansion preference | Log for future battlecards |
| "Won the deal using this" | Asset effective | Capture success pattern |
| "They didn't buy it" | Asset ineffective | Analyze what didn't work |
| "Add [section]" | Template improvement | Log template update |

---

## Output as reference example

When user confirms battlecard was used successfully:

1. **Ask:** "This battlecard helped close a deal. Want me to save it as a reference example?"
2. **If approved:** Save to `references/examples/[date]-[competitor-slug].md`

---

## Pattern detection rules

**Trigger:** Same feedback received 3+ times

**Action:**
1. Surface to user: "I've noticed [pattern]. Should I update the skill?"
2. If approved: Propose specific SKILL.md edit
3. Log in changelog
