---
title: "Entity Schema Builder Prompt — Person & Organization JSON-LD Graph for GEO"
author: "Mahmoud Omar"
author_url: "https://mahmoudomar.com"
category: "seo"
type: "prompt"
level: "advanced"
works_with: "Claude, ChatGPT, Gemini — output validates in Google Rich Results Test & Schema.org validator"
language: "EN"
last_verified: "2026-07-02"
hook: "AI doesn't rank pages. It resolves entities. If you're not an entity, you're a rumor."
email_subject: "Build your Person/Organization entity graph in one prompt"
short_pitch: "Generate a complete, interlinked JSON-LD entity graph — Person, Organization, products, books, sameAs profiles — from one prompt, so Google and LLMs resolve you as ONE entity instead of scattered mentions."
---

# Entity Schema Builder Prompt (Person & Organization Graph)

> Generate a complete JSON-LD entity graph — Person, Organization, creative works, and sameAs links — interconnected with stable @id references, ready to paste into your site's head.

## ⚡ What it does

Search engines and LLMs don't see your bio, your LinkedIn, your books, and your products as one thing unless you explicitly connect them. This prompt builds the connective tissue: a single JSON-LD graph where the Person node links to every property, every property links back, and sameAs ties in your social profiles — so "who is [you]?" resolves to one confident entity instead of five partial guesses.

## 🎯 When I use it (real scenario)

Built while turning my personal site into an entity hub — a deliberate GEO project where the homepage carries a Person + creative-works graph so AI engines attribute my products, books, and content to one entity. The insight that shaped the prompt: the schema itself is easy; the discipline is in the `@id` strategy (stable URIs for every entity) and in making every claim in the graph verifiable on a crawlable page. Schema that claims what the site doesn't show gets ignored.

## 📋 The Prompt

```
You are a semantic SEO specialist. Build me a complete JSON-LD entity graph for my personal/brand site. Output ONE <script type="application/ld+json"> block using @graph.

MY ENTITY:
- Person: name, role/title, one-line credential: [X]
- Primary domain (the entity hub): [X]
- Organization(s) I own/represent: [name + URL each]
- Creative works: books/guides/courses: [title + URL + type each]
- Products/apps: [name + URL + one-liner each]
- Social & authority profiles for sameAs: [LinkedIn, YouTube, X, GitHub, Wikipedia if any...]
- Languages I publish in: [X]

BUILD RULES:
1. @graph with stable @id URIs for every node (https://domain.com/#person, /#organization, /#book-slug...) — never anonymous nodes.
2. Person node: jobTitle, description, knowsAbout (5-8 topical entities), knowsLanguage, sameAs (ALL profiles), image placeholder.
3. Each Organization/Product/CreativeWork: correct schema type (SoftwareApplication for SaaS, Book/Guide for publications), url, and founder/author/publisher pointing BACK to the Person @id — the graph must be bidirectional.
4. WebSite node with publisher → Person @id.
5. NO claims that aren't verifiable on the listed URLs. If I gave you a credential you can't tie to a URL, put it in a comment for me to decide.
6. Output must validate: no trailing commas, correct @context, one block.

THEN OUTPUT:
- A placement note: which page(s) this belongs on (entity hub page vs sitewide)
- A maintenance checklist: what to update when I launch a new product
- 3 test queries to run in an LLM a few weeks later to check entity resolution ("who is [name]?", "what is [product]?", "what has [name] created?")
```

## 🧠 Pro tips

- The `@id` URIs don't need to be real pages — they're identifiers — but keep them on your domain and never change them once published. Entity identity is built on stability.
- `knowsAbout` is underrated for GEO: list the topics you want to be the answer for, as schema.org Thing entities where possible, not free text.
- Pair this with [llms.txt](llms-txt-generator.md) — schema tells machines the structure, llms.txt tells them the story. Both should make identical claims.
- Render the JSON-LD server-side or at build time. Schema injected by client-side JS after load is a gamble on which crawlers execute it.
- Recheck in Google's Rich Results Test after every edit — one trailing comma silently kills the whole graph.

## 🔗 Related assets

- [llms.txt Generator](llms-txt-generator.md)
- [GEO LLM Visibility Audit](geo-llm-visibility-audit.md)
- [Arabic LinkedIn Content Engine](../social/arabic-linkedin-content-engine.md)
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
