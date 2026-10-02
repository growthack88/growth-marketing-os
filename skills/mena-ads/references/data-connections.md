# Data Connections — exports, screenshots, or live accounts via MCP

The skill works at three levels. Start at the lowest one that answers the question.

| Level | How | Best for |
|---|---|---|
| **1 · Paste** | Screenshots or copied tables from Ads Manager / Google Ads | Quick diagnosis in any chat AI |
| **2 · Export** | CSV/XLSX exports (campaign, ad set/ad group, ad, search terms, breakdowns) | Audits and reports; works in ChatGPT, Claude.ai, Gemini, any agent |
| **3 · Live (MCP)** | An MCP server connected to the ad account | Daily optimisation, monitoring, agency workflows |

## 1 · What to export (minimum useful set)

**Meta Ads Manager** (last 30 days + previous 30, daily breakdown if possible): campaign / ad set / ad level with Amount spent, Impressions, Reach, Frequency, CPM, Link clicks, CTR (link), CPC (link), Results + Cost per result, Purchases + Purchase value (or Leads), ROAS, 3-second video plays, ThruPlays, Video plays at 25/50/75/95%. Add Breakdown → Age, Gender, Placement, Country, and Time of day if diagnosing.

**Google Ads:** Campaigns, Ad groups, Keywords, **Search terms** (essential), Assets, Auction insights; columns Cost, Impr., Clicks, CTR, Avg. CPC, Conversions, Conv. value, Cost/conv., Conv. value/cost, Search impr. share, Search lost IS (budget), Search lost IS (rank), Quality Score.

**TikTok / Snapchat:** campaign / ad group (ad squad) / ad with Spend, Impressions, CPM, Clicks, CTR, Conversions, CPA, Value, 2-second and 6-second views, average watch time, frequency.

**Backend (always):** orders by day and source/UTM; for COD add confirmed and delivered counts and delivered value. The backend is the truth platforms are checked against.

## 2 · Live connections (MCP)

MCP lets Claude, ChatGPT (where MCP connectors are enabled), Cursor, Codex and other agents read ad accounts directly. Options change fast; check each project's README before installing.

| Platform | Options (verify current status) |
|---|---|
| **Google Ads** | Google's official open-source Google Ads MCP server (`googleads/google-ads-mcp`, read-oriented, GAQL queries); hosted connectors such as GoMarble; community servers |
| **Meta Ads** | Hosted connectors (GoMarble, Pipeboard and others); community Meta Marketing API MCP servers; Meta's own tooling as it ships |
| **TikTok / Microsoft / Amazon** | Official or beta MCP servers announced by the platforms; check their developer docs |
| **GA4** | Google's Analytics MCP server (read-only reporting) |
| **Shopify** | Shopify's MCP / Admin API connectors (see this repo's [Shopify MCP recipes](https://github.com/growthack88/growth-marketing-os/blob/main/mcps/shopify-mcp-growth-audits.md)) |

Credentials: use OAuth or the platform's developer token flow inside the MCP client. **Never paste access tokens, passwords, or API keys into the chat.**

## 3 · Safety gate for live accounts (non-negotiable)

Reading is free. Every **write** (pause, enable, budget, bid, targeting, new campaign/ad, negative keywords) must pass all six:

1. **Exact change shown:** account ID, object IDs, current value → new value.
2. **Blast radius stated:** spend affected, learning-phase reset risk, policy risk.
3. **Explicit "yes" from the user for that specific change.** Approval for one change doesn't cover the next.
4. **Smallest reversible step:** budget changes ≤ 20% per step; new campaigns/ads created **paused** for the user to review; no deletions (pause instead; deletion is never done by the agent).
5. **Rollback noted:** what to revert and when to check (usually 3-7 days).
6. **Verify after:** re-read the object to confirm the change took effect.

Also:
- Skip anything edited in the last 48 hours to 7 days unless the user insists; it hasn't settled.
- Never pause the top-converting ad in an ad set, even if a rule says so; flag it instead.
- Never raise budget > 100% or cut > 50% in one step.

## 4 · API data hygiene (when reading via MCP/API)

- Google costs are in **micros** (÷ 1,000,000); Meta budgets are in **cents/minor units**.
- Meta purchases: use `omni_purchase` if present, else `purchase`, **never add the two** (double counting).
- Paginate: Meta returns 25 rows per page by default; fetch all pages before totalling.
- Don't sum conversions across platforms or attribution windows (Meta 7-day click / 1-day view ≠ Google data-driven ≠ GA4 last click).
- GA4: `conversions` ≠ `transactions`; intraday data lags 24-72 hours; never add channel subsets to make a total.
- Currency: never assume USD. Read the account currency (EGP, SAR, AED, KWD…) and convert only when comparing across accounts, stating the rate and date.
- Shopify/Salla/Zid orders: decide gross vs net (refunds, cancellations, COD returns) and `created_at` vs `processed_at` before reconciling with platform numbers.
