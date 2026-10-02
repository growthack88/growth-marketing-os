# Credits & Licenses

The MENA Ads Command Center is original work by [Mahmoud Omar](https://mahmoudomar.com), released under the MIT license as part of [Growth Marketing OS](https://github.com/growthack88/growth-marketing-os).

While designing it, we studied five open-source paid-ads projects. Parts of their structure, checklists and decision thresholds were **adapted and rewritten** (not copied verbatim) from the four MIT-licensed projects below. Their copyright and permission notices are preserved in [`licenses/`](licenses/), as the MIT license requires. Please star the originals.

| Project | Author | License | What we adapted |
|---|---|---|---|
| [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | agricidaniel | MIT ([notice](licenses/LICENSE-claude-ads.txt)) | Weighted audit scoring (severity × category weights, A-F grades, coverage rule), multi-platform check structure, the live-account mutation gate, evidence discipline |
| [gomarble-ai/marketing-agent](https://github.com/gomarble-ai/marketing-agent) | GoMarble | MIT ([notice](licenses/LICENSE-gomarble-marketing-agent.txt)) | Google search-term classes (Q1-Q5), impression-share pressure matrix, PMax and Shopping kill/scale gates, Meta copy archetypes, competitor-ad proxies (evergreen/breakout), API data-hygiene rules |
| [thatrebeccarae/claude-marketing](https://github.com/thatrebeccarae/claude-marketing) (mirrored at [wearehyperai/claude-paid-media-marketing](https://github.com/wearehyperai/claude-paid-media-marketing)) | Rebecca Rae Barton | MIT ([notice](licenses/LICENSE-claude-marketing-rebecca-rae-barton.txt)) | Google/Meta audit check thresholds, budget-share-weighted cross-platform score, structure minimums, waste thresholds |
| [mardab96/meta-ads-skills](https://github.com/mardab96/meta-ads-skills) | Marek Dabrowski / AdLume | MIT ([notice](licenses/LICENSE-meta-ads-skills.txt)) | Meta diagnostic ladder, volume gates and "not enough data" verdicts, fatigue statuses, budget reallocation and rollback rules, signal-readiness tiers, attribution/lag/click-to-session checks, comment and angle mining |
| [borghei/Claude-Skills](https://github.com/borghei/Claude-Skills) | Amin Borghei | MIT + Commons Clause | **Reviewed only. No text or code copied.** The Commons Clause restricts commercial use, and this skill is meant for commercial client work. Only general, widely known industry practice overlaps |

**Original to this skill:** the MENA layer (market map, dialects, calendar, COD real-ROAS logic and server-side confirmed/delivered events, Click-to-WhatsApp measurement, Snapchat playbook, regional compliance and VAT notes), the command router, the `ads_calc.py` calculator, the reporting templates, and the cross-AI install paths.

Benchmarks cited in the skill come from their named original publishers (WordStream/LocaliQ, Triple Whale, Optmyzr, IAB MENA, and others) via this repo's [paid-ads benchmarks](https://github.com/growthack88/growth-marketing-os/blob/main/benchmarks/paid-ads-benchmarks.md).

Platform names (Meta, Google, TikTok, Snapchat, LinkedIn, X, Microsoft, Apple, Amazon, noon) are trademarks of their owners. This skill is independent and not endorsed by any of them.
