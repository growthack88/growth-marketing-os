# Auto-update protocol — feedback signals + pattern detection

Capture feedback after each win/loss run so the skill learns from real engagements.

---

## Feedback signal detection

| User signal | Interpretation | Action |
|-------------|----------------|--------|
| "This is great" / "Perfect" | High quality match | Log as positive pattern, offer reference example save |
| "Pattern is wrong/right" | Accuracy feedback | Log accuracy feedback for pattern refinement |
| "Missing [dimension]" | Incomplete analysis | Log new dimension to add |
| "This insight was useful" | Valuable pattern | Capture as reference pattern |
| "Need more depth on [area]" | Depth preference | Log depth preference for area |
| Heavy edits to analysis | Implicit correction | Analyze diff, learn pattern |
| Quick approval (<2 min) | Output was good | Reinforce patterns used |

---

## Output as reference example

When user approves win/loss analysis:
1. Ask: "Want me to save this as a reference example for future analyses?"
2. If yes: capture key elements (industry, deal size, win/loss factors, pattern validity)
3. Store pattern: `examples/example-[company]-[outcome].md`

---

## Improvement tracking

After each skill use, capture:
- [ ] Which dimensions had sufficient data?
- [ ] Was user feedback positive on pattern validity?
- [ ] Were verbatim quotes available for evidence?
- [ ] Any new win/loss signals discovered?
- [ ] What depth level was most useful?

---

## Pattern detection rules

**Trigger:** Same feedback received 3+ times
**Action:**
1. Surface to user: "I've noticed [pattern]. Should I update the skill?"
2. If approved: Propose specific SKILL.md edit
3. Log in changelog

**Common patterns to watch:**

| Pattern | Frequency trigger | Suggested update |
|---------|------------------|------------------|
| "Pattern accuracy low" | 3+ occurrences | Refine pattern detection criteria |
| "Missing [dimension]" | 3+ occurrences | Add dimension to standard analysis |
| "Need more competitor context" | 3+ occurrences | Expand competitive analysis section |
| "Quotes not relevant" | 3+ occurrences | Improve quote selection criteria |

---

## Suggested skill update format

```markdown
## Skill Update Suggestion

**Skill:** win-loss-analysis
**Date:** YYYY-MM-DD
**Trigger:** [What prompted this suggestion]

**Current behavior:**
[What the skill does now]

**Suggested change:**
[What should change]

**Rationale:**
[Why this improves the skill]

**Implementation:**
- [ ] Update dimension framework
- [ ] Modify pattern detection criteria
- [ ] Add new analysis section
- [ ] Update changelog
```
