---
title: "Repo-to-Content Flywheel — n8n Workflow That Turns Every Commit Into Posts & Emails"
author: "Mahmoud Omar"
author_url: "https://mahmoudomar.com"
category: "growth"
type: "workflow"
level: "advanced"
works_with: "n8n, GitHub API, Claude API, LinkedIn, Email (any ESP)"
language: "EN"
last_verified: "2026-07-02"
hook: "I don't create content. I commit assets — the machine creates the content."
email_subject: "One commit = a LinkedIn post + an X thread + a newsletter entry"
short_pitch: "The n8n blueprint powering this repo: every new asset file auto-generates a LinkedIn post draft, an X thread, and a newsletter block from its frontmatter."
---

# Repo-to-Content Flywheel (n8n)

> The automation that powers this repo's distribution: one committed asset file → LinkedIn post draft + X thread + newsletter block, generated from the file's frontmatter.

## ⚡ What it does

Every asset in Growth Marketing OS carries `hook`, `email_subject`, and `short_pitch` fields in its frontmatter. This workflow watches the repo, and on every new asset: parses the frontmatter, sends the asset to Claude with a style guide, and drops ready-to-review drafts into a queue. Publish 3 assets/week = 9+ content pieces/week on autopilot.

## 🎯 When I use it (real scenario)

This exact flywheel distributes this repository. The frontmatter you see in every file here isn't decoration — it's machine fuel.

## 📋 The Workflow (node map)

```
1. TRIGGER — GitHub Trigger node
   Event: push to main · Filter: paths matching *.md, exclude README/_brand/templates

2. FETCH — HTTP Request node
   GET raw file content via GitHub API for each added file

3. PARSE — Code node
   Extract YAML frontmatter (title, hook, email_subject, short_pitch, category)
   + first 2 sections of body ("What it does" + "When I use it")

4. GENERATE — 3 parallel LLM nodes (Claude API)
   a) LinkedIn post: input = hook + body extract + personal style guide → 150-220 word post, hook as line 1, CTA to repo
   b) X thread: input = short_pitch + asset block → 4-6 tweet thread, last tweet = repo link
   c) Newsletter block: input = email_subject + body extract → 120-word teaser + link

5. QUEUE — Notion/Airtable node
   One row per draft: asset · channel · draft · status=Review

6. NOTIFY — Telegram/Slack node
   "3 drafts ready for review: [asset title]"

Human reviews → schedules. Never auto-publish; the review pass is where the voice stays real.
```

Importable JSON: `repo-to-content-flywheel.json` (same folder).

## 🧠 Pro tips

- Feed the LLM nodes YOUR writing style guide as a system prompt — otherwise you get generic AI voice and the whole flywheel is worthless.
- Add a weekly cron branch: pick the top-starred asset of the week → auto-draft a "most popular this week" post.
- Keep generation and publishing decoupled. Drafts are cheap; trust is expensive.

## 🔗 Related assets

- [Master Asset Template](../../templates/ASSET_TEMPLATE.md)
- [Growth Strategist Agent](../../agents/growth-strategist-agent.md)
<!-- MO-BRAND-FOOTER v1 — paste at the bottom of every asset file -->

---

## 🦆 Built by Mahmoud Omar

**Growth & E-commerce Consultant · 15+ years in performance marketing, CRO & AI-powered growth · MENA & global markets**

| Asset | Link |
|---|---|
| 🌍 Personal Site | [mahmoudomar.com](https://mahmoudomar.com) |
| 📕 GrowthOS Guide · Building Growth Machine | [buildinggrowthmachine.com](https://buildinggrowthmachine.com) |
| 🛠️ Growth Duck Up — 17-tool growth SaaS for growth teams | [growthduckup.com](https://growthduckup.com) |
| 🎓 Growth Hack Academy | [growthhackacademy.com](https://growthhackacademy.com) |
| 🚀 StartupKit Pro — Startup OS for MENA founders | [startupkit.pro](https://startupkit.pro) |
| 🍅 DuckDoro — calm productivity app | [duckdoro.com](https://duckdoro.com) |
| 🎥 YouTube (40K+ marketers) | [Subscribe → Growth Hack Academy](https://www.youtube.com/@GrowthHackAcademy?sub_confirmation=1) |

⭐ **Saved you time? [Star the repo](https://github.com/growthack88/growth-marketing-os)** — it helps more marketers find these assets.

> All assets are original work by [Mahmoud Omar](https://mahmoudomar.com), battle-tested on real accounts. Free to use with attribution. Not AI-generated filler.
