# Tracking & Measurement — fix the signal before you touch the bids

Most accounts that "stopped working" are fine. What broke is the signal the algorithm optimises on. Check this file **first** in every audit and before every scale decision. If tracking scores Poor, every other recommendation is provisional.

---

## 1 · Signal checklist per platform

| Platform | Browser | Server-side | Match-quality target | Dedup |
|---|---|---|---|---|
| **Meta** | Pixel | Conversions API (CAPI), via Shopify/WooCommerce/Salla/Zid integration, GTM server, or a CAPI gateway | Event Match Quality ≥ 6 for Purchase (≥ 8 is strong) | Same `event_id` on Pixel + CAPI |
| **Google** | Google tag / GTM | Enhanced Conversions (web + leads), offline conversion import (GCLID / hashed email/phone), Consent Mode v2 where required | Enhanced conversions "Excellent/Good" diagnostics | Transaction ID |
| **TikTok** | TikTok Pixel | Events API | Hashed email/phone + `ttclid` | `event_id` |
| **Snapchat** | Snap Pixel | Conversions API (CAPI) | Hashed email/phone, `click_id` | `event_id` / `client_dedup_id` |
| **LinkedIn** | Insight Tag | Conversions API | Hashed email + `li_fat_id` | event ID |

Must-pass checks:
1. **Purchase/lead fires once per real conversion** (compare platform count vs backend count for the same 7 days; > ±20% gap = broken).
2. **Value + currency are passed** and in the account's currency (EGP vs USD mismatches inflate ROAS 50×).
3. **Server events are deduplicated** against browser events.
4. **The optimisation event is the one that matters** — not a page view, not "Lead" when 70% of leads are junk.
5. **Domain verified (Meta) and Aggregated Event Measurement priorities set** where relevant.
6. **Consent:** in markets with consent requirements, Consent Mode / consent banners are wired so modelled conversions still flow.
7. **UTMs on every ad** (`utm_source / utm_medium / utm_campaign / utm_content={{ad.name}}`) so GA4 and the store backend can see what the platforms claim.

Score this section in the audit as: Pass (all 7) · Partial (Purchase works, server-side missing or value wrong) · Fail (purchase count off by > 20%, or optimising on a vanity event).

## 2 · COD and MENA-specific measurement

Platform "Purchase" in a COD store is a **placed order**. The account then optimises toward people who order, not people who pay. Fix it in this order:

1. **Measure the chain** — Orders → Confirmed → Delivered, by campaign (UTMs + order IDs). Without this the account is managed on fiction. Minimum viable version: a sheet or WhatsApp Business labels by stage.
2. **Confirmation event (fast, high-volume):** when the call centre / WhatsApp confirms an order (usually within hours), send a server-side event (`Purchase` with value, or a custom `ConfirmedOrder`) to Meta CAPI / TikTok Events API / Snap CAPI. When it reaches ~50/week per ad set, make it the optimisation event.
3. **Delivered event (slow, highest quality):** send delivered orders with real value as offline / CAPI events (Meta accepts offline events up to 62 days old; web events must be within 7 days — verify current windows) and as Google offline conversion adjustments. Use them for value optimisation and reporting even if volume is too low to optimise on directly.
4. **Audiences from reality:** seed lookalikes from delivered buyers, exclude repeat refusers (customer-list upload), retarget confirmed-but-undelivered with reassurance creative.
5. **Report three ROAS numbers side by side:** platform (placed), confirmed, delivered (real). Run `python3 scripts/ads_calc.py cod ...` for the maths.

## 3 · Click-to-WhatsApp (CTWA) and messaging ads

- Optimise CTWA campaigns for **conversations** only while learning; graduate to **purchases/leads via the Conversions API for Business Messaging** (send `LeadSubmitted` / `Purchase` events from your WhatsApp Business Platform/CRM back to Meta with the conversation's ctwa_clid).
- Without that loop, CTWA "cost per conversation" is a vanity metric: 1,000 cheap conversations can mean 10 sales.
- Track per campaign: conversations → qualified (replied to first question) → quoted → sold, with time to first reply. Replies after 5 minutes kill conversion rates, so staffing is part of the funnel.
- Use quick replies and a qualifying first message ("Which size/city?") so the sales team can sort intent fast.

## 4 · Lead-gen quality loop

- Raw "Lead" is a vanity event in the region (fake numbers, accidental instant-form submits, wrong country codes).
- Fixes: Higher Intent form type / review step on Meta Instant Forms, phone validation, one qualifying question, WhatsApp/phone verification.
- Send CRM stages back (Meta CAPI for CRM / conversion leads optimisation; Google offline conversion import; LinkedIn CAPI). Optimise to **qualified lead** as soon as volume allows.

## 5 · Attribution: what to trust

- Platform attribution over-claims (each platform counts its own touch); GA4 last-click under-claims social and video. The truth is in between. Use **blended MER** (total revenue ÷ total ad spend, from the backend) as the business-level check, and platform data for within-platform decisions.
- In WhatsApp-heavy and COD markets, click-based attribution understates social: people see the ad, then message or come back via search. Expect brand search and direct traffic to rise when social works. Say so instead of chasing false precision.
- When a client has the budget and the volume, run a **holdout / geo test** (e.g., pause a channel in one city or country for 2-3 weeks) before believing any channel's ROAS claims.
- Attribution windows: compare like with like (Meta 7-day click / 1-day view default vs Google data-driven); state the window in every report.

## 6 · Quick tracking audit prompt (works in any AI)

Paste with the user's data:

```
Audit my ad tracking. For each platform I run [list], tell me:
1) Is the optimisation event the right one for my business ([COD e-com / prepaid e-com / lead-gen / app])?
2) Platform conversions vs backend for the same 7 days: [numbers] — is the gap acceptable (±20%)?
3) Is server-side tracking (CAPI / Events API / Enhanced Conversions) live and deduplicated?
4) What should I send back as offline conversions (confirmed / delivered / qualified)?
Output: Pass / Partial / Fail per platform, and the 3 fixes in priority order.
```
