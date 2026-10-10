# Experiment Coach · مدرب التجارب

> A growth-experiment lead inside your chat. Validate an idea before you build it, then keep running experiments after launch. It does the maths, writes the decision rule before the data, and tells you plainly: continue, change one thing, or stop.

**By [Mahmoud Omar](https://mahmoudomar.com)** · part of [Growth Marketing OS](../../README.md) · MIT

---

## العربي — في دقيقة

<div dir="rtl">

**ده إيه؟** سكيل بتركّبها مرة واحدة في الشات اللي بتستخدمه (Claude أو ChatGPT أو Gemini)، وبعدها تكلّمها عادي. بتشتغل معاك زي مسؤول تجارب نمو: تساعدك تتأكد من فكرتك قبل ما تبني أو تطلق، وبعد الإطلاق تمشي معاك في تجارب منظمة.

**بتعمل إيه؟**
- **تطلّع الافتراض الأخطر** في فكرتك، وتختار أرخص اختبار يجاوب عليه.
- **تكتبلك سكريبت مقابلات** بالعامية أو بالفصحى، ولما ترجعلها بالإجابات تلخّصها.
- **تحسبلك حد النجاح** من أرقامك أنت (السعر وتكلفة النقرة)، وكمان حجم العينة والميزانية.
- **تكتبلك أدوات الاختبار:** صفحة الهبوط، والإعلانات، ورسالة الباب الوهمي، وعرض البيع المسبق.
- **تكتب قاعدة القرار قبل الاختبار**، ولما ترجعلها بالأرقام تقولك: كمّل، أو غيّر حاجة واحدة، أو وقّف.
- **بعد الإطلاق:** 32 كارت تجارب جاهزة، وحساب اختبارات A/B، وسجل تجارب، ومراجعة بعد كل تجربة.

**مفيش أرقام مخترعة:** مش هتقولك "التجربة دي بتزوّد المبيعات 30%". أي رقم مرجعي بمصدره، وغير كده بتقولك تقيس رقمك إزاي.

</div>

| Type a command | …or just say | You get |
|---|---|---|
| `/experiment-coach validate` | "عايز أختبر فكرتي قبل ما أبنيها" | Riskiest assumption + the first test with its decision rule |
| `/experiment-coach interview` | "اكتبلي أسئلة مقابلات للعملاء" | Recruiting plan + interview script in your dialect |
| `/experiment-coach smoke-test` | "عايز أعمل صفحة وقائمة انتظار" | Pass line, sample, budget, page copy, test ads |
| `/experiment-coach presale` | "عايز أبيع قبل ما أبني" | Offer, refund terms, break-even pre-sales |
| `/experiment-coach readout` | "دي نتيجة الاختبار، أعمل إيه؟" | Verdict against your rule: continue / change one thing / stop |
| `/experiment-coach backlog` | "عندي أفكار كتير، أبدأ بأنهي؟" | A ranked backlog against your bottleneck, with kill lines |
| `/experiment-coach calc` | "النتيجة دي معنوية؟" | The calculation, with the formula shown |

All 15 commands are in [SKILL.md](SKILL.md).

## Install: pick your AI

### 1 · Claude Code (recommended): plugin, two commands

```bash
/plugin marketplace add growthack88/growth-marketing-os
```

```bash
/plugin install experiment-coach@growth-marketing-os
```

This installs the skill plus its companions (Benchmark Analyst, Funnel Decomposition, and the community A/B Testing skill). Call it with `/experiment-coach:experiment-coach validate`, or just ask in plain Arabic or English; the skill triggers by itself.

**Manual install** (personal skills folder, gives the short `/experiment-coach` command):

```bash
git clone https://github.com/growthack88/growth-marketing-os.git
```

```bash
./growth-marketing-os/skills/experiment-coach/install.sh
```

Use `--project` to install into the current project's `.claude/skills` instead.

### 2 · Claude app (claude.ai, Desktop)

1. Build the upload file: `./skills/experiment-coach/install.sh --zip`. It makes `experiment-coach.zip` with a description short enough for the app, which accepts up to 200 characters.
2. Turn on **Settings → Capabilities → Code execution and file creation**. On Team/Enterprise, an owner enables skills under **Organization settings**.
3. **Customize → Skills → + → Create skill → Upload a skill**, choose `experiment-coach.zip`, then switch the skill on.
4. Ask: "help me validate my idea" or "عايز أختبر فكرتي قبل الإطلاق".

No skills on your plan? Create a **Project**, paste [SKILL.md](SKILL.md) into the project instructions, and upload the `references/` files as project knowledge.

### 3 · ChatGPT

- **Business / Enterprise / Edu workspaces:** **Plugins → Skills → Create → Upload from your computer**, and upload the same `experiment-coach.zip`.
- **Personal accounts:** create a **Project**. Paste the instructions from [gpts/experiment-coach-gpt.md](../../gpts/experiment-coach-gpt.md) into Project settings, and add the `references/` files and `scripts/exp_calc.py` as project files.

### 4 · Gemini and any other chat AI

- **Gemini app:** Gems → **New Gem**, paste the same instructions, and add the `references/` files under **Knowledge**.
- **Gemini CLI:** `./skills/experiment-coach/install.sh --dir ~/.gemini/skills`.
- Any assistant that accepts instructions plus files can run it; it's plain Markdown. Without code execution it does the maths step by step from [references/calculations.md](references/calculations.md).

### 5 · Codex, Cursor, OpenCode and other coding agents

```bash
./skills/experiment-coach/install.sh --dir /path/to/your/agent/skills
```

Agents that use `AGENTS.md` instead: add this line to your project's `AGENTS.md`:

```
For idea validation, pre-launch tests, growth experiments, A/B sample sizes or test readouts (تجارب، اختبر فكرتي), read and follow skills/experiment-coach/SKILL.md and only the reference files it routes to.
```

## What's inside

```
experiment-coach/
├── SKILL.md                    router: 15 commands, intake, core rules, output contract
├── references/
│   ├── validation-ladder.md    interviews → smoke test → fake door → pre-sale, with rule templates
│   ├── calculations.md         pass line, sample sizes, A/B size and duration, readout, SRM, pre-sale break-even
│   ├── interviews.md           recruiting, EN + Egyptian Arabic scripts, synthesis grid
│   ├── test-assets.md          landing page, test ads, fake door, pre-sale offer, waitlist follow-up
│   ├── experiment-cards.md     32 cards by funnel stage and business type (no invented lifts)
│   ├── readout.md              verdict rules, A/B readouts, postmortem
│   ├── experiment-log.md       log entry, plan JSON (GrowthLab format v1.0), importing GrowthLab exports
│   ├── mena-notes.md           COD ≠ commitment, payment rails, channels, Ramadan, weekends, consent
│   └── benchmarks-used.md      the only reference numbers it may quote, each with source and caveat
├── scripts/exp_calc.py         stdlib calculator; `selftest` runs the checks
└── install.sh                  Claude Code / any skills folder / zip for upload
```

## Calculator examples

```bash
python3 scripts/exp_calc.py passline --price 150 --payback-months 3 --signup-to-paid 0.10 --cpc 3
python3 scripts/exp_calc.py precision --p 0.07 --margin 0.02 --cpc 3
python3 scripts/exp_calc.py ab --baseline 0.05 --mde 20 --relative --daily-visitors 800
python3 scripts/exp_calc.py significance --a-conv 29 --a-n 700 --b-conv 54 --b-n 720
python3 scripts/exp_calc.py presale --cost 30000 --price 900 --fees 0.03 --waitlist 83
python3 scripts/exp_calc.py selftest
```

## Works with GrowthLab

GrowthLab is a separate simulation app that rehearses launches and messages on synthetic personas. Experiment Coach reads GrowthLab exports, labels them as synthetic, and turns them into real-market tests with pass lines, samples and dates. It can also write plans in the same JSON format. A simulation never passes a ladder step; real interviews, smoke tests and pre-sales decide.

## Honest limits

- It can't see your ad accounts or analytics unless you paste or connect the data.
- Pass lines depend on your economics; when you don't know a number, it marks it as an assumption for a test to replace.
- Small pre-launch samples give directional answers with wide ranges. The skill shows the range instead of hiding it.
- It won't predict conversion rates or lifts. No one can do that honestly before a test.
