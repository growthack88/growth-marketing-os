<div align="center">

<img src="_brand/social-preview.png" alt="Growth Marketing OS — the open-source growth stack by Mahmoud Omar: AI prompts, agents, skills, playbooks and sourced benchmarks in English and Arabic" width="100%">

# Growth Marketing OS

**An open-source library of AI marketing assets — prompts, Claude skills, agents, playbooks and sourced benchmarks — in English and العربية.**
Built and used by [Mahmoud Omar](https://mahmoudomar.com) on real e-commerce, SaaS and lead-gen accounts across Egypt, the GCC and global markets.

<p dir="rtl">مكتبة مفتوحة المصدر لأدوات التسويق بالذكاء الاصطناعي: برومبتات، Skills، وكلاء، Playbooks وأرقام مرجعية موثّقة، بالعربي والإنجليزي.</p>

[How to use](HOW-TO-USE.md) · [Asset catalog](#asset-catalog) · [MENA Ads plugin](#featured-mena-ads-command-center) · [Contributing](CONTRIBUTING.md) · [MIT License](LICENSE)

</div>

---

## Contents

- [What's inside](#whats-inside)
- [Start here](#start-here)
- [Featured: MENA Ads Command Center](#featured-mena-ads-command-center)
- [Asset catalog](#asset-catalog)
- [Repository map](#repository-map)
- [How every asset is built](#how-every-asset-is-built)
- [What's still missing](#whats-still-missing)
- [Contributing](#contributing)
- [License and attribution](#license-and-attribution)
- [About the author](#about-the-author)

## What's inside

**56 original assets**, plus **13 openly licensed community resources** curated in with full attribution.

| Type | Count | Best for |
|---|---:|---|
| [Prompts](prompts/) | 25 | One task, one answer — paste into Claude, ChatGPT or Gemini |
| [Skills](skills/) | 7 original + 11 community | Repeatable workflows your AI assistant runs on demand |
| [Agents](agents/) and [GPTs](gpts/) | 2 + 2 | A standing advisor set up once as a system prompt, Project or Custom GPT |
| [Benchmarks](benchmarks/) | 7 | "Is this number good?" — every figure cited to a named study |
| [Swipe files](swipe-files/) | 4 | Hooks, subject lines, CTAs and WhatsApp scripts in EN + AR |
| [Playbooks](playbooks/) and [frameworks](frameworks/) | 2 + 2 | Step-by-step launches and the mental models behind them |
| [Worked examples](worked-examples/) | 3 | Full decision walkthroughs (fictional scenarios, real benchmark data) |
| [MCP recipes](mcps/) and [workflows](workflows/) | 1 + 1 | Connecting AI to your store and your content pipeline |
| [Community resources](resources/) | 2 | Vendored tool directory and prompt collection (MIT / CC0) |

## Start here

| If you want to… | Open this |
|---|---|
| Get one result in 10 minutes, no setup | [Beginner path](HOW-TO-USE.md#-beginner-path--i-use-chatgptclaude-sometimes-im-not-technical) → [Meta Ads Creative Diagnosis](prompts/paid-ads/meta-ads-creative-diagnosis.md) |
| Find out why sales dropped | [Funnel Decomposition Analyst](skills/funnel-decomposition/SKILL.md) |
| Check if a metric is actually bad | [Benchmarks](benchmarks/) + [Benchmark Analyst skill](skills/benchmark-analyst/SKILL.md) |
| Audit or scale paid ads in the Arab world | [MENA Ads Command Center](skills/mena-ads/README.md) |
| See if ChatGPT, Claude and Gemini recommend your brand | [GEO LLM Visibility Audit](prompts/seo/geo-llm-visibility-audit.md) |
| Write Arabic copy that doesn't read like a translation | [Arabic Copy Localizer](skills/arabic-copy-localizer/SKILL.md) + [Bilingual Hook Bank](swipe-files/hooks/bilingual-hook-bank.md) |
| Run a cash-on-delivery store profitably | [COD Profit Funnel](frameworks/cod-profit-funnel.md) + [COD Operations Analyst](skills/cod-operations-analyst/SKILL.md) |
| Install systems instead of one-off prompts | [Intermediate path](HOW-TO-USE.md#-intermediate-path--i-run-campaignsfunnels-and-use-ai-weekly) |
| Wire assets into your own stack | [Advanced path](HOW-TO-USE.md#-advanced-path--i-build-automations-agents-or-run-a-team) |

## Featured: MENA Ads Command Center

A complete paid-ads skill for the Arab world (**مركز قيادة الإعلانات**): scored account audits, media plans, scale/kill decisions, Arabic ad copy by dialect, delivered-order ROAS for COD, Snapchat and Click-to-WhatsApp playbooks, and Ramadan planning across Meta, Google, TikTok, Snapchat, LinkedIn and X.

Install in Claude Code:

```
/plugin marketplace add growthack88/growth-marketing-os
/plugin install mena-ads@growth-marketing-os
```

Using ChatGPT, Gemini, Cursor or Codex? → [Install guide for every AI](skills/mena-ads/README.md#install-pick-your-ai) · [ChatGPT / Gemini config](gpts/mena-ads-gpt.md)

## Asset catalog

Level: 🟢 beginner · 🟡 intermediate · 🔴 advanced. Language: EN, or EN + AR for assets with native Arabic versions.

<details open>
<summary><b>Prompts — paid ads</b> (6)</summary>

| Prompt | Use it when | Level | Lang |
|---|---|:---:|:---:|
| [Meta Ads Creative Diagnosis](prompts/paid-ads/meta-ads-creative-diagnosis.md) | Your Meta ads stopped converting and you need to know why | 🟡 | EN |
| [Ad Angle Matrix](prompts/paid-ads/ad-angle-matrix.md) | You need 12 distinct angles from one product, mapped to awareness levels | 🟡 | EN |
| [Competitor Ads Teardown](prompts/paid-ads/competitor-ads-teardown.md) | You want the strategy behind a competitor's Ad Library | 🟡 | EN |
| [Google Ads Search Terms Audit](prompts/paid-ads/google-ads-search-terms-audit.md) | Search budget is leaking into the wrong queries | 🟡 | EN |
| [Retargeting Ladder Builder](prompts/paid-ads/retargeting-ladder-builder.md) | Retargeting shows everyone the same message | 🟡 | EN |
| [Campaign Postmortem](prompts/paid-ads/campaign-postmortem.md) | A campaign ended and you want the next one to inherit the lessons | 🟡 | EN |

</details>

<details>
<summary><b>Prompts — SEO and GEO</b> (4)</summary>

| Prompt | Use it when | Level | Lang |
|---|---|:---:|:---:|
| [GEO LLM Visibility Audit](prompts/seo/geo-llm-visibility-audit.md) | You want to know if ChatGPT, Claude and Gemini recommend your brand | 🟢 | EN + AR |
| [llms.txt Generator](prompts/seo/llms-txt-generator.md) | Your site needs an `llms.txt` so AI assistants can cite it | 🟢 | EN |
| [AI Citation Optimizer](prompts/seo/ai-citation-optimizer.md) | You want existing content rewritten so LLMs quote it | 🟡 | EN |
| [Entity Schema Builder](prompts/seo/entity-schema-builder.md) | You need a Person and Organization JSON-LD graph | 🔴 | EN |

</details>

<details>
<summary><b>Prompts — email</b> (3)</summary>

| Prompt | Use it when | Level | Lang |
|---|---|:---:|:---:|
| [Abandoned Cart Recovery Sequence](prompts/email/abandoned-cart-recovery-sequence.md) | You run e-commerce (including COD) and carts go cold | 🟢 | EN + AR |
| [Welcome Sequence Builder](prompts/email/welcome-sequence-builder.md) | New subscribers need 5 emails from signup to first purchase | 🟡 | EN + AR |
| [Win-Back and Reactivation Sequence](prompts/email/winback-reactivation-sequence.md) | Part of your list has gone dormant | 🟡 | EN + AR |

</details>

<details>
<summary><b>Prompts — CRO</b> (3)</summary>

| Prompt | Use it when | Level | Lang |
|---|---|:---:|:---:|
| [Review Mining Copy Bank](prompts/cro/review-mining-copy-bank.md) | You want customer reviews turned into reusable copy | 🟢 | EN + AR |
| [Landing Page CRO Teardown](prompts/cro/landing-page-cro-teardown.md) | A page underperforms and you want the leak found before a redesign | 🟡 | EN |
| [Pricing Page Optimizer](prompts/cro/pricing-page-optimizer.md) | Plans, anchors, decoys or the billing toggle need an audit | 🔴 | EN |

</details>

<details>
<summary><b>Prompts — content and social</b> (6)</summary>

| Prompt | Use it when | Level | Lang |
|---|---|:---:|:---:|
| [Content Repurposing Matrix](prompts/content/content-repurposing-matrix.md) | One flagship piece should feed a month of distribution | 🟢 | EN + AR |
| [Lead Magnet Designer](prompts/content/lead-magnet-designer.md) | You need a freebie that pre-sells the paid product | 🟢 | EN |
| [Case Study Writer](prompts/content/case-study-writer.md) | You have results but no case study people believe | 🟢 | EN + AR |
| [YouTube Script Outline](prompts/content/youtube-script-outline.md) | Educational videos lose viewers in the first minutes | 🟡 | EN + AR |
| [Arabic LinkedIn Content Engine](prompts/social/arabic-linkedin-content-engine.md) | One insight should become a week of Arabic (عامية) posts | 🟡 | EN + AR |
| [UGC Brief Generator](prompts/social/ugc-brief-generator.md) | Creators keep sending footage you can't use | 🟡 | EN + AR |

</details>

<details>
<summary><b>Prompts — growth and offers</b> (3)</summary>

| Prompt | Use it when | Level | Lang |
|---|---|:---:|:---:|
| [Growth Experiment Designer](prompts/growth/growth-experiment-designer.md) | "Let's try stuff" needs to become a ranked testing backlog | 🟡 | EN |
| [Offer Stack Builder](prompts/growth/offer-stack-builder.md) | A good product isn't yet an offer people want | 🟡 | EN |
| [Referral Program Designer](prompts/growth/referral-program-designer.md) | You want referral loops tied to real customer moments | 🔴 | EN |

</details>

<details>
<summary><b>Skills, agents and GPTs</b> (11 original)</summary>

| Asset | What it does | Lang |
|---|---|:---:|
| ⭐ [MENA Ads Command Center](skills/mena-ads/README.md) | Complete paid-ads skill for the Arab world: audits, media plans, creative, tracking, COD ROAS | EN + AR |
| [Funnel Decomposition Analyst](skills/funnel-decomposition/SKILL.md) | Quantified "why did sales drop?" diagnosis from raw numbers | EN |
| [Benchmark Analyst](skills/benchmark-analyst/SKILL.md) | Answers "is this number good?" with matched, sourced benchmarks | EN |
| [COD Operations Analyst](skills/cod-operations-analyst/SKILL.md) | Real revenue, return-to-origin cost and break-even delivery rate for COD stores | EN |
| [Arabic Copy Localizer](skills/arabic-copy-localizer/SKILL.md) | English marketing copy → native عامية with code-switching rules | EN + AR |
| [Conversion Copywriter](skills/conversion-copywriter/SKILL.md) | Direct-response copy in 5 modes: write, rewrite, audit, hook, teach | EN, AR-aware |
| [Performance Media Buyer](skills/performance-media-buyer/SKILL.md) | Paid media in 6 modes: plan, build, optimize, diagnose, audit, report | EN |
| [Growth Strategist Agent](agents/growth-strategist-agent.md) | System prompt for a senior growth advisor | EN |
| [CRO Teardown Agent](agents/cro-teardown-agent.md) | System prompt for a conversion-audit specialist | EN |
| [Growth Strategist GPT](gpts/growth-strategist-gpt.md) | Ready-to-paste Custom GPT configuration for ChatGPT | EN |
| [MENA Ads GPT](gpts/mena-ads-gpt.md) | MENA Ads Command Center as a ChatGPT Project or Gemini Gem | EN + AR |

Plus **11 community skills** (MIT) for A/B testing, churn, onboarding, positioning, ICP research, battlecards and more → [skills/community](skills/community/README.md).

</details>

<details>
<summary><b>Benchmarks</b> (7)</summary>

Every number is cited to a named study with year and URL, including MENA-specific data where it exists.

| Benchmark | Covers |
|---|---|
| [Paid Ads](benchmarks/paid-ads-benchmarks.md) | Meta, Google and TikTok CTR, CPC, CPM and ROAS by industry |
| [CRO and E-commerce](benchmarks/cro-ecommerce-benchmarks.md) | Conversion by funnel stage, AOV, COD markets |
| [Email, SMS and WhatsApp](benchmarks/email-whatsapp-benchmarks.md) | Campaigns, flows, cart recovery, COD markets |
| [SEO and GEO](benchmarks/seo-geo-benchmarks.md) | CTR by position, AI Overview impact, zero-click, LLM citations |
| [Social Media](benchmarks/social-media-benchmarks.md) | Engagement by platform, LinkedIn formats, MENA usage |
| [Content Marketing](benchmarks/content-marketing-benchmarks.md) | Blogs, newsletters, influencers, podcasts, webinars |
| [SaaS and Growth](benchmarks/growth-saas-benchmarks.md) | Trial conversion, activation, churn, NRR, unit economics |

</details>

<details>
<summary><b>Playbooks, frameworks and worked examples</b> (7)</summary>

| Asset | Type | Use it when |
|---|---|---|
| [Lifetime Deal Launch](playbooks/lifetime-deal-launch-playbook.md) | Playbook | Launching a digital product or SaaS at a founding price |
| [Shopify Direct-Checkout Offer](playbooks/shopify-direct-checkout-offer-playbook.md) | Playbook | Building landing pages that skip the cart |
| [COD Profit Funnel](frameworks/cod-profit-funnel.md) | Framework | ROAS looks fine but cash-on-delivery profit doesn't |
| [Bilingual Content System](frameworks/bilingual-content-system.md) | Framework | Running EN + AR marketing without doing everything twice |
| [COD Store ROAS Collapse](worked-examples/cod-store-roas-collapse-turnaround.md) | Worked example | Learning to diagnose a collapsing ad account step by step |
| [SaaS Trial at 2%](worked-examples/saas-trial-conversion-turnaround.md) | Worked example | Seeing why activation comes before persuasion |
| [Monetizing an 8K Newsletter](worked-examples/newsletter-monetization-launch.md) | Worked example | Comparing paid tiers, sponsorships and products with real math |

Worked examples are clearly labeled fictional scenarios built on the benchmark data.

</details>

<details>
<summary><b>Swipe files, MCP and automation</b> (6)</summary>

| Asset | What it is | Lang |
|---|---|:---:|
| [Bilingual Hook Bank](swipe-files/hooks/bilingual-hook-bank.md) | 30 ad and content hooks | EN + AR |
| [Bilingual Subject Line Bank](swipe-files/subject-lines/bilingual-subject-line-bank.md) | 24 email subject-line formulas | EN + AR |
| [Arabic CTA Bank](swipe-files/ctas/arabic-cta-bank.md) | 20 button and closing lines for MENA | EN + AR |
| [COD WhatsApp Script Bank](swipe-files/whatsapp/cod-whatsapp-script-bank.md) | Order confirmation, recovery and upsell messages | EN + AR |
| [Shopify MCP Growth Audits](mcps/shopify-mcp-growth-audits.md) | 5 store-audit recipes for Shopify connected to Claude via MCP | EN |
| [Repo-to-Content Flywheel](workflows/n8n/repo-to-content-flywheel.md) | n8n node map that turns commits into post and email drafts (spec — JSON export not yet published) | EN |

</details>

<details>
<summary><b>Community resources</b> (2)</summary>

| Resource | What it is | Source |
|---|---|---|
| [Awesome AI Marketing](resources/awesome-ai-marketing.md) | Directory of AI marketing tools with when-to-use context | [jmedia65/awesome-ai-marketing](https://github.com/jmedia65/awesome-ai-marketing) (MIT) |
| [Marketing prompts from prompts.chat](resources/marketing-prompts-from-prompts-chat.md) | 38 marketing prompts filtered from the community collection | [f/prompts.chat](https://github.com/f/prompts.chat) (CC0) |

</details>

## Repository map

```
growth-marketing-os/
├── prompts/          paid-ads · seo · email · cro · content · social · growth
├── skills/           Claude / agent skills (SKILL.md) — community/ holds curated MIT skills
├── agents/           full system prompts for marketing agents
├── gpts/             Custom GPT, ChatGPT Project and Gemini Gem configs
├── benchmarks/       sourced market benchmarks
├── playbooks/        step-by-step launches and funnels
├── frameworks/       growth models and mental models
├── swipe-files/      hooks, subject lines, CTAs, WhatsApp scripts (EN + AR)
├── worked-examples/  labeled teaching scenarios
├── mcps/             MCP recipes for marketers
├── workflows/        n8n / Make blueprints
├── case-studies/     real results (template ready, first entries pending)
├── resources/        vendored community resources
├── templates/        asset and case-study templates for contributors
└── llms.txt          machine-readable summary for AI assistants
```

## How every asset is built

- **One format.** Original assets follow the [asset template](templates/ASSET_TEMPLATE.md) and open with YAML frontmatter (`title`, `category`, `type`, `level`, `works_with`, `language`, `last_verified`). The frontmatter is machine-readable, so you can parse the repo into your own tools.
- **A "When I use it" section.** Each original asset says what situation it came from and when to reach for it.
- **Sourced numbers only.** Benchmarks cite a named study, year and link. Worked examples are labeled fictional.
- **Native Arabic, not translation.** Bilingual assets are written in Egyptian/MSA Arabic with natural code-switching for marketing terms.
- **Clear origin.** Anything not written here lives in [`skills/community/`](skills/community/) or [`resources/`](resources/) with its source and license preserved.
- **Links are checked.** A [CI job](.github/workflows/link-check.yml) fails any pull request with a broken relative link.

## What's still missing

Being honest about gaps is part of the format:

- **Case studies** — the [template](templates/CASE_STUDY_TEMPLATE.md) is ready; the first anonymized case studies haven't been published yet. Until then, see the [worked examples](worked-examples/).
- **Importable workflow JSON** — [workflows](workflows/) are published as node maps first; JSON exports are added only after a flow has run live.

Want something specific? [Request an asset](https://github.com/growthack88/growth-marketing-os/issues/new?template=asset-request.md) or [report something outdated](https://github.com/growthack88/growth-marketing-os/issues/new?template=broken-or-outdated.md).

## Contributing

PRs are welcome, and the bar is high: every asset must follow the [master template](templates/ASSET_TEMPLATE.md) and include a real usage scenario. Read [CONTRIBUTING.md](CONTRIBUTING.md) and the [Code of Conduct](CODE_OF_CONDUCT.md) first.

## License and attribution

Original work is [MIT licensed](LICENSE) — free for client work, courses and agencies. Attribution to *Growth Marketing OS by Mahmoud Omar (mahmoudomar.com)* is appreciated; see [CITATION.cff](CITATION.cff).
Community skills and resources keep their original MIT or CC0 licenses, preserved next to each file.

## About the author

**Mahmoud Omar** — Growth Cofounder and Fractional Head of Growth for companies in Egypt, the GCC and MENA. Founder of Read to Lead.

[mahmoudomar.com](https://mahmoudomar.com) · [YouTube — Growth Hack Academy](https://www.youtube.com/@GrowthHackAcademy?sub_confirmation=1) · [Building Growth Machine (ماكينة النمو)](https://buildinggrowthmachine.com) · [Growth OS — 17 growth tools](https://growthduckup.com) · [StartupKit Pro](https://startupkit.pro) · [DuckDoro](https://duckdoro.com)

If this repo saves you time, a ⭐ helps other marketers find it.
