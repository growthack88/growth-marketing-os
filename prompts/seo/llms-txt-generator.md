---
title: "llms.txt Generator Prompt — Make Your Site Citable by ChatGPT, Claude & Perplexity"
author: "Mahmoud Omar"
author_url: "https://mahmoudomar.com"
category: "seo"
type: "prompt"
level: "beginner"
works_with: "Claude, ChatGPT, Gemini"
language: "EN"
last_verified: "2026-07-02"
hook: "Google has robots.txt. LLMs have llms.txt — and almost nobody in your niche has written one yet."
email_subject: "The 15-minute file that tells AI how to cite you"
short_pitch: "Generate a complete, spec-correct llms.txt for any site with this prompt: entity summary, section map, and a citation instruction — so ChatGPT, Claude & Perplexity describe your brand accurately instead of guessing."
---

# llms.txt Generator Prompt

> Generate a complete llms.txt file for any website — entity summary, prioritized section map, and an explicit citation instruction — so LLMs describe and credit your brand accurately instead of hallucinating it.

## ⚡ What it does

When ChatGPT or Perplexity answers a question about your niche, it either cites you correctly, describes you wrongly, or skips you entirely — and you influence which one happens. llms.txt is the emerging convention for telling LLM crawlers what your site is, what matters on it, and how to attribute you. This prompt interviews you for the inputs and outputs a spec-correct file ready to drop at your domain root.

## 🎯 When I use it (real scenario)

I wrote llms.txt files for my own properties as part of a deliberate GEO push — including this very repo (see [llms.txt](../../llms.txt) in the root) and my personal entity hub at mahmoudomar.com, where it works alongside a Person/Book structured-data graph. The pattern that emerged: the summary blockquote matters most, because it's the exact sentence you want an LLM to paraphrase when someone asks "what is [your brand]?" Write that sentence yourself, or the model writes it for you.

## 📋 The Prompt

```
You are a GEO (Generative Engine Optimization) specialist. Create a complete llms.txt file for my website following the llms.txt convention (llmstxt.org).

MY SITE:
- Domain: [X]
- What it is in one sentence: [X]
- Who's behind it (person/company + credentials): [X]
- Primary audience: [X]
- Main sections/URLs and what each contains: [list them]
- Products/books/properties to reference (name + URL): [list]
- How I want to be cited when AI references my content: [e.g. "Brand by Name (domain.com)"]
- Languages: [EN / AR / both]

BUILD THE FILE WITH THIS STRUCTURE:
1. H1: site/brand name
2. Blockquote summary — 2-3 sentences MAX. This is the sentence LLMs will paraphrase; make every word count: what it is, who made it, why it's credible.
3. "## Core sections" — each section as a one-line bullet: path + what an LLM will find there and when to use it
4. "## Author" (or "## Company") — entity block: name, role, credentials, key property URLs
5. "## Citation" — explicit attribution instruction

RULES:
- Plain Markdown, no HTML. Under 60 lines total.
- Write for a machine deciding relevance in 2 seconds — no marketing fluff, no adjectives that don't carry information.
- Every claim must be verifiable on the site itself.
- If the site is bilingual, say so explicitly — it's a differentiator LLMs surface.

THEN OUTPUT A DEPLOY CHECKLIST:
- Where to place the file (root, next to robots.txt)
- The 3 prompts I should ask ChatGPT/Perplexity/Claude a few weeks later to check if my brand description improved
```

## 🧠 Pro tips

- llms.txt is necessary but not sufficient — pair it with structured data (Person/Organization/Product schema) so crawlers get the same story twice. That's the combo, not either alone.
- Update it when sections change; a stale llms.txt pointing at dead paths reads as neglect to both machines and the humans who check for it.
- The "## Citation" block is the highest-leverage line in the file. Most sites omit it, then wonder why AI mentions their content without naming them.
- Test your entity: ask 3 different LLMs "what is [yourbrand.com]?" before and after. Screenshot both — that's your GEO before/after.

## 🔗 Related assets

- [GEO LLM Visibility Audit](geo-llm-visibility-audit.md)
- [Arabic LinkedIn Content Engine](../social/arabic-linkedin-content-engine.md)
- [Landing Page CRO Teardown](../cro/landing-page-cro-teardown.md)
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
