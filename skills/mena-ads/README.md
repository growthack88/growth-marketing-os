# MENA Ads Command Center · مركز قيادة الإعلانات

> A complete paid-ads skill for the Arab world: audits with a 0-100 health score, media plans, scale/kill decisions, creative and Arabic ad copy, tracking fixes, COD real-ROAS maths, seasonal planning and client reports, across Meta, Google, TikTok, Snapchat, LinkedIn, X, YouTube and Click-to-WhatsApp. It works in Claude, ChatGPT, Gemini, Cursor, Codex or any AI.

**By [Mahmoud Omar](https://mahmoudomar.com)** · part of [Growth Marketing OS](../../README.md) · MIT

---

## العربي — في دقيقة

**ده إيه؟** سكيل كاملة لإدارة الإعلانات المدفوعة، معمولة مخصوص للسوق العربي: مصر والسعودية والإمارات والخليج والشام والمغرب العربي. بتشتغل زي ميديا باير سينيور: بتسألك الأسئلة الصح، تحسب الأرقام، تدي حسابك درجة من 100، وتطلعلك قرارات واضحة (كبّر / ثبّت / قلّل / وقّف) مع الخطوات الجاية.

**إيه اللي يميزها عن أي سكيل إعلانات تانية؟**
- **الـ COD:** بتحسب الروآس الحقيقي على الطلبات اللي اتسلمت فعلًا، مش الطلبات اللي اتعملت بس.
- **اللهجات:** مصري للسوق المصري، وخليجي/سعودي للخليج، والفصحى بس في الأماكن اللي محتاجاها.
- **سناب شات والواتساب:** فيها بلاي بوك كامل لسناب شات (أساسي في السعودية) ولإعلانات Click-to-WhatsApp.
- **المواسم:** رمضان والعيد والجمعة البيضاء والأيام الوطنية.
- **القوانين والضرائب:** ترخيص موثوق، تصاريح المؤثرين في الإمارات، الـ VAT على الإعلانات، وقوانين حماية البيانات.

**تستخدمها إزاي؟** اكتب الأمر أو اسأل عادي بالعربي:

| اكتب | أو قول | هتاخد |
|---|---|---|
| `/mena-ads audit` | "راجع حساب الإعلانات بتاعي" | تقييم من 100 + أهم الإصلاحات + خطة 30 يوم |
| `/mena-ads plan` | "عندي 50 ألف ريال، وزعهم إزاي؟" | خطة منصات وميزانية وأهداف |
| `/mena-ads optimize` | "أكبّر الحملة دي ولا أوقفها؟" | قرار لكل حملة بالأرقام |
| `/mena-ads diagnose` | "الروآس وقع فجأة ليه؟" | السبب الأساسي + الحلول بالترتيب |
| `/mena-ads creative` | "عايز أفكار إعلانات وهوكات" | زوايا + هوكات + بريف UGC + خطة تست |
| `/mena-ads copy` | "اكتبلي إعلان سناب باللهجة السعودية" | كوبي جاهز لكل منصة |
| `/mena-ads calc` | "احسبلي نقطة التعادل" | Break-even ROAS / CPA والروآس الحقيقي للـ COD |
| `/mena-ads season` | "خطة رمضان" | خطة موسمية وتقويم كريتيف |
| `/mena-ads report` | "اعملي تقرير للعميل" | تقرير أسبوعي أو شهري بالعربي أو الإنجليزي |
| `/mena-ads tracking` · `compliance` · `competitors` · `connect` | | البيكسل والـ CAPI · السياسات · المنافسين · ربط الحساب لايف |

**أسرع طريقة تبدأ بيها:** ثبّتها بأي طريقة من اللي تحت، وابعتلها screenshot أو ملف export من Ads Manager، واكتب: "راجع حسابي".

---

## Install: pick your AI

### 1 · Claude Code (recommended): plugin, two commands

```bash
/plugin marketplace add growthack88/growth-marketing-os
```

```bash
/plugin install mena-ads@growth-marketing-os
```

This installs the skill plus its companions (COD Operations Analyst, Arabic Copy Localizer, Performance Media Buyer, Benchmark Analyst). Call it with `/mena-ads:mena-ads audit`, or just ask in plain Arabic or English ("audit my Meta account", "راجع حملاتي"); the skill triggers by itself.

**Manual install** (personal skills folder, gives the short `/mena-ads` command):

```bash
git clone https://github.com/growthack88/growth-marketing-os.git
```

```bash
./growth-marketing-os/skills/mena-ads/install.sh
```

Use `--project` to install into the current project's `.claude/skills` instead.

### 2 · Claude.ai and Claude Desktop

1. Build the zip: `./skills/mena-ads/install.sh --zip` (or download this folder and zip `mena-ads/`).
2. Claude → **Settings → Capabilities → Skills → Upload skill** → choose `mena-ads.zip`. Keep code execution on so Claude can run the calculator.
3. Ask: "audit my ads" and attach screenshots or CSV exports.

No skill upload on your plan? Create a **Project**, paste [SKILL.md](SKILL.md) into the project instructions, and upload the `references/` files as project knowledge.

### 3 · ChatGPT (Custom GPT or Project)

Follow [gpts/mena-ads-gpt.md](../../gpts/mena-ads-gpt.md): paste the instructions, upload `references/*.md` as Knowledge, upload `scripts/ads_calc.py`, and turn on Code Interpreter. Open the GPT and type `audit` or `خطة رمضان`.

### 4 · Gemini (Gems), Copilot, Perplexity Spaces, any chat AI

Create a Gem / custom assistant / space with the same instructions from [gpts/mena-ads-gpt.md](../../gpts/mena-ads-gpt.md) and attach the `references/` files. The skill is plain Markdown, so any assistant that accepts instructions and files can run it.

### 5 · Codex, Gemini CLI, Cursor, OpenCode, and other coding agents

Any agent that reads the Agent Skills (`SKILL.md`) format: copy the folder into that tool's skills directory:

```bash
./skills/mena-ads/install.sh --dir /path/to/your/agent/skills
```

Agents that use `AGENTS.md` instead: add this line to your project's `AGENTS.md`:

```
For any paid-advertising task (ads, campaigns, ROAS, CPA, media plans, ad creative, اعلانات), read and follow skills/mena-ads/SKILL.md and only the reference files it routes to.
```

### 6 · Live ad-account data (optional)

Connect Google Ads / Meta / GA4 / Shopify through an MCP server and the skill reads live numbers instead of screenshots. It reads freely but never changes anything without your explicit yes for each change. See [references/data-connections.md](references/data-connections.md).

---

## What's inside

```
mena-ads/
├── SKILL.md                      router: commands, intake, core rules, output contract
├── references/
│   ├── audit-checklist.md        0-100 scoring, cross-platform + 12 MENA checks, report format
│   ├── meta.md                   diagnostic ladder, structure, signal tiers, fatigue, CTWA, 22 checks
│   ├── google.md                 search-term classes, IS matrix, PMax, Shopping, Arabic search, 20 checks
│   ├── tiktok.md                 Smart+, Spark Ads, creator rules, 12 checks
│   ├── snapchat.md               the GCC channel: structure, formats, creative, 9 checks
│   ├── other-platforms.md        LinkedIn, YouTube, X, Microsoft, Apple Search Ads, Amazon/noon retail media
│   ├── mena-market-playbook.md   markets, dialects, calendar, COD, payments, VAT, compliance
│   ├── tracking-measurement.md   Pixel/CAPI/EC, COD confirmed/delivered events, WhatsApp, attribution
│   ├── budget-scaling.md         economics → allocation → scale/hold/reduce/pause → diagnosis
│   ├── creative-system.md        angles, hooks (AR examples), testing, briefs, copy limits, ad libraries
│   ├── reporting.md              weekly + monthly templates (AR/EN)
│   └── data-connections.md       exports, MCP options, safety gate, API data hygiene
├── scripts/ads_calc.py           break-even, COD real ROAS, learning budget, verdict, VAT, split
├── install.sh                    Claude Code / any skills folder / zip for Claude.ai
├── CREDITS.md + licenses/        sources and their MIT notices
└── README.md
```

## Calculator examples

```bash
python3 scripts/ads_calc.py breakeven --price 499 --cogs 150 --shipping 45 --fees 3 --confirm 0.85 --deliver 0.78 --return-cost 30
python3 scripts/ads_calc.py cod --spend 20000 --orders 400 --aov 499 --confirm 0.85 --deliver 0.78 --cogs 150 --ship-out 45 --return-cost 30
python3 scripts/ads_calc.py verdict --spend 12000 --conversions 40 --target-cpa 400 --days 14 --frequency 3.4 --ctr-drop 25
python3 scripts/ads_calc.py split --budget 50000 --goal sales --market KSA
```

Add `--json` for machine-readable output.

## Honest limits

- Thresholds are practitioner heuristics, not platform law. Recalibrate them to your account after ~90 days.
- Platform features, attribution windows, tax rates, Islamic calendar dates and regulations change; the files mark those with **verify**.
- Not legal or tax advice. Check compliance questions with a local advisor.

## Credits

Builds on ideas from five open-source projects. See [CREDITS.md](CREDITS.md).

---

Maintained by [Mahmoud Omar](https://mahmoudomar.com) · [Growth Hack Academy on YouTube](https://www.youtube.com/@GrowthHackAcademy?sub_confirmation=1) · ⭐ [Star the repo](https://github.com/growthack88/growth-marketing-os)
