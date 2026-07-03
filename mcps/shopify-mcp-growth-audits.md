---
title: "Shopify MCP Growth Audit Recipes — Run Store Audits by Talking to Your Store"
author: "Mahmoud Omar"
author_url: "https://mahmoudomar.com"
category: "growth"
type: "mcp"
level: "intermediate"
works_with: "Claude (Desktop/Code) + Shopify MCP connector"
language: "EN"
last_verified: "2026-07-02"
hook: "Your Shopify dashboard answers 'what happened'. Your store connected to an LLM answers 'so what do I do'."
email_subject: "5 store audits I now run by talking to my Shopify store"
short_pitch: "Connect Shopify to Claude via MCP and run these 5 growth-audit recipes conversationally: funnel decomposition from live data, dead-inventory sweep, offer setup, collection hygiene, and a weekly analytics ritual — no CSV exports."
---

# Shopify MCP Growth Audit Recipes

> Five copy-paste audit recipes for a Shopify store connected to Claude via MCP — live funnel diagnosis, dead-inventory sweeps, offer creation, and a weekly analytics ritual, all conversational, no CSV exports.

## ⚡ What it does

MCP (Model Context Protocol) lets Claude talk to your Shopify store directly — read products, orders, analytics; create collections and offers. That turns audits from "export CSV → clean → paste → analyze" into a single conversation. These five recipes are the growth-relevant ones: each is a prompt you paste after connecting, engineered to make the model pull the right data before it opines.

## 🎯 When I use it (real scenario)

I run my own Shopify stores through this setup — the MCP connection is how offers get created, collections get built, and weekly numbers get pulled without opening the admin. The recipes formalize what stuck: the funnel-decomposition pull replaced my manual Monday exports, and the offer-setup recipe is how new campaign products go live (it pairs with the [Direct-Checkout Playbook](../playbooks/shopify-direct-checkout-offer-playbook.md) — the model creates the product, you grab the variant permalink).

## 📋 The Recipes

```
SETUP (once): connect the official Shopify MCP connector to Claude
(claude.ai → Settings → Connectors, or Claude Desktop config). Authenticate
the store. Multi-store: note which store the connector is pinned to —
switching stores usually means reconnecting, so verify with a "what store
is this?" question BEFORE running anything that writes.

RECIPE 1 — WEEKLY FUNNEL PULL (read-only)
"Pull my store analytics for the last 7 days vs the 7 days before:
sessions, conversion rate, AOV, total sales, top 5 products by revenue.
Then decompose the change: which lever (traffic / conversion / AOV)
explains most of the delta? Verdict first, table second."

RECIPE 2 — DEAD INVENTORY SWEEP (read-only)
"List products with zero sales in the last 60 days that still have
inventory. For each: current stock, price, and whether it appears in any
collection. Recommend: discount-and-clear, bundle-into-offer, or delist —
with one-line reasoning each."

RECIPE 3 — CAMPAIGN OFFER SETUP (writes — review before confirming)
"Create a new product for a campaign offer: [name], price [X], compare-at
price [anchor], one variant, DON'T publish to the online store catalog yet.
Then give me the variant ID for a /cart/VARIANT_ID:1 checkout permalink."

RECIPE 4 — COLLECTION HYGIENE (read, then optional writes)
"Audit my collections: which are empty, which overlap >80% in products,
which bestsellers (top 20 by 90-day revenue) are missing from their
obvious collection? Propose fixes; apply only the ones I approve."

RECIPE 5 — PRE-CAMPAIGN STOCK CHECK (read-only)
"I'm about to run ads to [product/offer]. Check: inventory level vs my
last 30 days' sales velocity — how many days of stock is that? Flag if
under 14 days at 2x current velocity (ads work = velocity jumps)."
```

## 🧠 Pro tips

- Read-recipes are safe to run freely; treat every write-recipe as a two-step — let the model propose, you approve, then it executes. Never one-shot bulk writes on a live store.
- ShopifyQL analytics via MCP beats screenshot-pasting your dashboard: the model gets exact numbers, and you can ask follow-ups without new exports.
- Feed Recipe 1's output into the [Funnel Decomposition Skill](../skills/funnel-decomposition/SKILL.md) rules for a sharper verdict format — they compose.
- If a number looks off, ask the model to state the exact query/tool call it used. MCP answers are auditable; use that.
- COD stores: platform "sales" ≠ collected cash. Pair the weekly pull with your delivery-rate sheet ([COD Profit Funnel](../frameworks/cod-profit-funnel.md)) before celebrating.

## 🔗 Related assets

- [Shopify Direct-Checkout Offer Playbook](../playbooks/shopify-direct-checkout-offer-playbook.md)
- [Funnel Decomposition Skill](../skills/funnel-decomposition/SKILL.md)
- [The COD Profit Funnel](../frameworks/cod-profit-funnel.md)
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
