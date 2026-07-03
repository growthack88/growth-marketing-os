# 🚀 How to Use Growth Marketing OS

**By [Mahmoud Omar](https://mahmoudomar.com)** · Pick your level. Each path takes you from "browsing" to "getting results" in under 30 minutes.

---

## 🟢 Beginner Path — "I use ChatGPT/Claude sometimes, I'm not technical"

**Goal: get one real result today. No tools, no setup, no code.**

### Step 1 — Grab your first prompt (5 min)
1. Open [`prompts/`](prompts/) and pick the folder matching your current problem (running ads? → [`paid-ads/`](prompts/paid-ads/) · want AI to know your brand? → [`seo/`](prompts/seo/)).
2. Open any file. Scroll to **📋 The Asset** — everything inside the code block is the prompt.
3. Click the copy icon on the code block.

### Step 2 — Run it (5 min)
1. Paste into Claude, ChatGPT, or Gemini — free versions work.
2. Replace every `[bracket]` with your real info. **Don't skip brackets** — the prompt quality depends on your inputs.
3. Send. Read the output. Ask follow-up questions — the prompt sets up the conversation, it doesn't end it.

### Step 3 — Build your habit (ongoing)
- ⭐ **Star the repo** so you can find it again (top-right button).
- Read the **🎯 When I use it** section of each asset — that's where the real education is: it teaches you *when* to reach for which weapon.
- Start with these 3:
  1. [Meta Ads Creative Diagnosis](prompts/paid-ads/meta-ads-creative-diagnosis.md) — if you spend anything on ads
  2. [GEO LLM Visibility Audit](prompts/seo/geo-llm-visibility-audit.md) — check if AI knows your brand
  3. [Bilingual Hook Bank](swipe-files/hooks/bilingual-hook-bank.md) — steal openers for posts & ads (EN + AR)
- Before you panic about any metric, check it against the [`benchmarks/`](benchmarks/) — every number there cites a real study, and the most common finding is that your "bad" number is normal.
- Want to see how the assets fit together on a real problem? Read one [worked example](worked-examples/) — they walk a full campaign decision start to finish.

**Rules for beginners:**
- One prompt at a time. Get a result, then move on.
- If the output feels generic → your `[brackets]` were too vague. Add real numbers, real context, real market.
- You never need to read the whole repo. It's a toolbox, not a book.

---

## 🟡 Intermediate Path — "I run campaigns/funnels and use AI weekly"

**Goal: stop using prompts one-by-one — install systems.**

### Step 1 — Install the agents & skills (15 min)
- Take the [Growth Strategist Agent](agents/growth-strategist-agent.md) system prompt and set it up **once** as:
  - a Claude **Project** (paste into project instructions), or
  - a ChatGPT **Custom GPT** (paste into instructions), or
  - your API system prompt.
- Add the [Funnel Decomposition Skill](skills/funnel-decomposition/SKILL.md) the same way. Now every conversation starts at senior-strategist level instead of from zero.
- Level it up: install the [Benchmark Analyst](skills/benchmark-analyst/SKILL.md) with the [`benchmarks/`](benchmarks/) files as knowledge — "is this number good?" gets a sourced answer. Running COD? Add the [COD Operations Analyst](skills/cod-operations-analyst/SKILL.md). The [community skills](skills/community/) (A/B testing, churn, positioning, ICP) install the same way.

### Step 2 — Feed it real data (this is the multiplier)
Exports beat descriptions. Drop into the conversation:
- Meta Ads: last 14 + previous 14 days (CTR, CPC, frequency, ROAS)
- Shopify/GA4: sessions → ATC → checkout → purchase by week
- Email: sends, opens, clicks, revenue per campaign

The same prompt with real numbers is 10x sharper than with adjectives.

### Step 3 — Automate the boring layer (30-60 min)
- Import workflows from [`workflows/`](workflows/) into your n8n or Make.
- Start with [Repo-to-Content Flywheel](workflows/n8n/repo-to-content-flywheel.md) if you create content — or use its node map as a pattern for your own repo/Notion → posts pipeline.

### Step 4 — Localize (MENA advantage)
Every bilingual asset has native Egyptian Arabic versions — not translations. Use the AR versions as-is for MENA audiences, and follow the code-switching style (English terms, Arabic flow) when creating your own.

**Rules for intermediates:**
- Systems > prompts. If you've pasted the same prompt 3 times, turn it into a Project/GPT/skill.
- Track before/after: CPA, CTR, time saved. Assets you can't measure, you can't trust.
- Contribute back — battle-tested improvements get merged with credit ([CONTRIBUTING.md](CONTRIBUTING.md)).

---

## 🔴 Advanced Path — "I build automations, agents, or run a team"

- Wire the repo into your stack: every asset's **YAML frontmatter** (`category`, `type`, `hook`, `email_subject`, `short_pitch`) is machine-readable by design — parse it with n8n/scripts to build internal libraries, Slack bots, or content pipelines.
- Deploy [`agents/`](agents/) as system prompts across your team's workspaces so everyone operates from the same playbook.
- Fork the [flywheel workflow](workflows/n8n/repo-to-content-flywheel.md) and point it at your own asset repo.
- MCP recipes in [`mcps/`](mcps/) connect AI assistants directly to your marketing stack.
- Load the [`benchmarks/`](benchmarks/) files as knowledge for any advisor agent you build — labeled, sourced numbers stop models from hallucinating their own.
- The [`resources/`](resources/) folder and [`skills/community/`](skills/community/) carry the best openly-licensed community assets, vendored with attribution — one clone gets your team the whole toolkit.

---

## ❓ FAQ

**Is this free?** Yes — MIT license. Use it in client work, courses, agencies. Attribution to [Mahmoud Omar](https://mahmoudomar.com) appreciated.

**Which AI tool do I need?** Any — Claude, ChatGPT, Gemini all work. Assets note their best fit in `works_with`.

**English or Arabic?** Both. Check the `language` field in each file's frontmatter. Bilingual assets carry native AR versions.

**How often do new assets drop?** Weekly. Star + watch the repo, or get them first via [mahmoudomar.com](https://mahmoudomar.com) and [YouTube — Growth Hack Academy](https://www.youtube.com/@GrowthHackAcademy?sub_confirmation=1).
