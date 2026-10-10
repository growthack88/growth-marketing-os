---
title: "Pre-Launch Validation Playbook — Get Real Market Feedback Before You Build or Launch"
author: "Mahmoud Omar"
author_url: "https://mahmoudomar.com"
category: "growth"
type: "playbook"
level: "beginner"
works_with: "Any stack — a landing page builder, a form or waitlist tool, a small ad budget, a payment link"
language: "Bilingual"
last_verified: "2026-10-10"
hook: "Compliments aren't data. Ask people to do something that costs them a little: their email, a click, then their money."
email_subject: "Validate before you launch: the 4-step commitment ladder"
short_pitch: "A step-by-step pre-launch playbook: problem interviews → smoke-test landing page → fake door → pre-sale. Each step has a decision rule you write before the test, thresholds derived from your own economics and sourced benchmarks, and an experiment log so every test leaves a lesson."
---

# Pre-Launch Validation Playbook

> Get real market feedback before you launch. Climb a ladder of tests where each step asks people for more commitment, and decide each step's pass/fail number before you look at the results.

## ⚡ What it does

Most pre-launch "feedback" is friends saying "nice idea". It feels like validation and predicts nothing. This playbook replaces opinions with behavior. You move up four steps, from talking to people to taking their money. Each step answers one question, costs more than the one before, and runs only if the previous step passed. Every step has a decision rule written in advance, so you can't talk yourself into a "maybe".

## 🎯 When I use it

<!-- TODO(Mahmoud): replace this paragraph with the real scenario where you ran this ladder (product, which rungs, what the decision rule said, what you decided). The repo promises a real scenario for every original asset; do not merge with this placeholder. -->

Use it before writing code or ordering stock for a new product, a new market, a new price, or a big feature. It's also for when a team is arguing about whether people "will want this" and nobody can settle it. If you already have paying customers and traffic, skip to the [Growth Experiment Designer](../prompts/growth/growth-experiment-designer.md).

## 📋 The Playbook

```
THE RULE THAT MAKES THIS WORK
Before every step, write the decision rule. Fill this in BEFORE the test starts:

  "If [metric] is ≥ [pass line] after [sample] by [date] → we [next step].
   If it's < [fail line] → we [stop / change the offer / change the audience].
   In between → we [one specific change] and rerun once. No third run."

Log it in the Experiment Log (templates/EXPERIMENT_LOG_TEMPLATE.md) before you
look at any results. A rule written after the data comes in is a story.

────────────────────────────────────────────────────────────────────────

STEP 0 — WRITE DOWN THE RISKIEST ASSUMPTION (30 minutes)
List what must be true for this to work: the problem exists, it's painful enough,
these people can be reached, they'll pay this price, you can deliver.
Pick the one that's most likely to be wrong AND kills the plan if it is.
That assumption is what you test first. Everything else waits.

Optional warm-up: synthetic audiences
LLM persona panels, or multi-agent simulators such as MiroFish, can play out how
an imagined audience might react to your message. Use them to sharpen questions
and spot obvious objections. Never count them as validation: the "audience" is
a model talking to itself. Real evidence starts at Step 1.

────────────────────────────────────────────────────────────────────────

STEP 1 — PROBLEM INTERVIEWS (cost: time · proves: the problem is real)
Who:     people who match your target customer. Not friends, not family.
Ask about the past, not the future:
  - "Tell me about the last time [problem] happened."
  - "What did you do about it? What did that cost you (time / money)?"
  - "What have you already tried? Why did you stop?"
Never ask: "Would you use / buy this?" Everyone says yes. (Further reading:
"The Mom Test" by Rob Fitzpatrick.)
Signal:  they already spend time or money on a workaround.
Stop interviewing when three interviews in a row teach you nothing new.
Decision rule example:
  "If most interviewees describe a recent incident AND an existing workaround
   → Step 2. If the problem only shows up when we prompt it → stop or re-target."

────────────────────────────────────────────────────────────────────────

STEP 2 — SMOKE TEST: LANDING PAGE + WAITLIST (cost: small ad budget · proves: strangers want it)
Build:   one page — the promise in the customer's words from Step 1, who it's
         for, what they get, an honest "launching soon" note, one sign-up form.
Traffic: strangers, not your followers. Paid social or search, aimed at the
         audience you will actually sell to.
Metric:  visitor → sign-up rate.

Set the pass line from your economics FIRST, then sanity-check it:
  1. Pilot: spend a small budget to measure YOUR real cost per click.
     (benchmarks/paid-ads-benchmarks.md has US medians; it also notes there are
     no reliable public MENA CPC benchmarks — measure your own.)
  2. Decide the most you can afford per sign-up (from expected price, margin,
     and how many sign-ups you expect to become buyers — a guess you'll
     replace with Step 4 data).
  3. Required sign-up rate = your cost per click ÷ affordable cost per sign-up.
  4. Sanity check: the median landing page converts at 6.6% for campaign/lead
     conversions (Unbounce, Q4 2024 — see benchmarks/cro-ecommerce-benchmarks.md).
     A waitlist for an unbuilt product is a different offer, so treat that as a
     reference point, not a target.

Sample size (so you're not deciding on noise):
  To estimate a rate p within ± m at ~95% confidence:  n ≈ 4 × p × (1 − p) ÷ m²
  e.g. expecting ~5%, wanting ± 2 points: 4 × 0.05 × 0.95 ÷ 0.0004 ≈ 475 visitors.
  Budget ≈ visitors needed × your measured cost per click.

Before you trust the number, check message match: the ad, the page headline and
the form must promise the same thing. A mismatch tests your copy, not demand.
Run the page through the Landing Page CRO Teardown before spending.

────────────────────────────────────────────────────────────────────────

STEP 3 — FAKE DOOR (cost: low · proves: real users choose it in context)
Use when you already have a site, app or audience. Add the new option where a
real decision happens: a plan on the pricing page, a button in the product, a
menu item. Clicking it opens an honest message: "Not live yet. Want early
access?" plus an email field.
Metric:  share of people who saw the option and clicked it, and how many of
         those left an email.
Ethics:  never pretend something exists past the click. Say "coming soon" right
         away, and don't take payment for something you haven't committed to build.
Decision rule: compare to a similar existing option on the same page, not to an
         internet average.

────────────────────────────────────────────────────────────────────────

STEP 4 — PRE-SALE (cost: refunds if you don't ship · proves: willingness to pay)
Offer: a founding price or a refundable deposit, with a clear delivery date and
       a clear refund promise ("full refund if we don't ship by [date]").
Ask:   your waitlist first, then the same paid audience.
Metric: waitlist → paid conversion, and total pre-sales against the number you
        need to justify building (from your own costs).
MENA note: a cash-on-delivery "order" is not a commitment. It's a maybe until
        delivery (see frameworks/cod-profit-funnel.md). For validation, take a
        prepaid deposit through a payment link, card, wallet or bank transfer.
        Use the Lifetime Deal Launch Playbook for founding-price mechanics.
Decision rule example:
  "If pre-sales cover [N]% of the first build cost by [date] → build.
   If fewer than [floor] people pay → go back to Step 1 with the people who
   signed up but didn't pay, and ask why."

────────────────────────────────────────────────────────────────────────

AFTER LAUNCH — SWITCH TO GROWTH EXPERIMENTS
Once real customers and traffic arrive:
  - Turn your idea pile into a ranked backlog: Growth Experiment Designer.
  - Run A/B tests only when traffic can reach a meaningful sample in a few
    weeks: A/B Testing skill (sample-size maths included).
  - Close every test, and every campaign, with the Campaign Postmortem.
  - Keep ONE experiment log for the whole journey, pre-launch included.
```

### النسخة العربية

<div dir="rtl">

**القاعدة اللي بتخلّي الطريقة دي تنفع:** قبل كل خطوة، اكتب قاعدة القرار قبل ما تبدأ الاختبار:

> "لو [المؤشر] ≥ [حد النجاح] بعد [حجم العينة] لحد [التاريخ] ← نروح للخطوة اللي بعدها. لو أقل من [حد الفشل] ← نوقف أو نغيّر العرض أو الجمهور. لو في النص ← نعمل تغيير واحد محدد ونعيد مرة واحدة بس."

سجّلها في [سجل التجارب](../templates/EXPERIMENT_LOG_TEMPLATE.md) قبل ما تبص على أي نتيجة. القاعدة اللي بتتكتب بعد النتيجة اسمها قصة، مش قرار.

**الخطوة 0: الافتراض الأخطر.** اكتب كل اللي لازم يكون صح عشان الفكرة تنجح، واختار الافتراض اللي احتمال يطلع غلط أكبر، ولو طلع غلط الخطة كلها تقع. ده اللي يتختبر الأول.
تمهيد اختياري: الجماهير الافتراضية زي محاكيات الوكلاء (MiroFish مثلًا) أو شخصيات بالذكاء الاصطناعي بتساعدك تحسّن أسئلتك وتشوف الاعتراضات الواضحة، لكنها مش دليل، لأن "الجمهور" هنا نموذج بيكلّم نفسه.

**الخطوة 1: مقابلات المشكلة.** الثمن وقتك، والنتيجة إنك تتأكد إن المشكلة حقيقية. اسأل عن الماضي مش المستقبل: "احكيلي آخر مرة حصلت المشكلة دي"، "عملت إيه؟ كلفك كام؟"، "جربت إيه قبل كده وبطّلته ليه؟". متسألش أبدًا "هتستخدمه؟"، لأن الكل هيقول آه. الإشارة القوية إنهم بيصرفوا وقت أو فلوس فعلًا على حل بديل. وقّف المقابلات لما تلات مقابلات ورا بعض ما يضيفوش جديد.

**الخطوة 2: اختبار الدخان (صفحة هبوط + قائمة انتظار).** الثمن ميزانية إعلانات صغيرة، والنتيجة إنك تعرف هل ناس غريبة عايزاه. صفحة واحدة بالوعد بكلام العميل نفسه، وفورم تسجيل، وزيارات مدفوعة من الجمهور اللي هتبيع له فعلًا، مش من متابعينك. المؤشر نسبة الزوار اللي سجلوا.
حدّد حد النجاح من حساباتك أنت: قِس تكلفة النقرة الحقيقية بميزانية تجريبية صغيرة (مفيش أرقام عامة موثوقة لتكلفة النقرة في MENA). حدد أقصى تكلفة تقدر تتحملها لكل تسجيل. النسبة المطلوبة = تكلفة النقرة ÷ أقصى تكلفة للتسجيل. وللمقارنة بس: متوسط صفحات الهبوط 6.6% لتحويلات الحملات (Unbounce، الربع الرابع 2024)، وقائمة انتظار لمنتج لسه مش موجود عرض مختلف.
حجم العينة: n ≈ 4 × p × (1 − p) ÷ m². مثال: لو متوقع حوالي 5% وعايز دقة ± نقطتين، محتاج حوالي 475 زائر.

**الخطوة 3: الباب الوهمي (Fake Door).** الثمن قليل، والنتيجة إنك تعرف هل المستخدمين الحقيقيين بيختاروه وهم في موقف قرار. حط الاختيار الجديد مكان القرار الحقيقي (باقة في صفحة الأسعار، أو زرار في المنتج)، ولما حد يضغط تظهر رسالة صريحة: "لسه مش متاح، تحب توصلك أول ما ينزل؟". متدّعيش أبدًا إن الحاجة موجودة، ومتاخدش فلوس على حاجة مش ملتزم تبنيها. قارن بنسبة اختيار متاح جنبه في نفس الصفحة، مش بمتوسط من الإنترنت.

**الخطوة 4: البيع المسبق.** الثمن استرجاع الفلوس لو ما سلمتش، والنتيجة إنك تتأكد إن فيه استعداد للدفع. سعر مؤسسين أو عربون قابل للاسترجاع، بتاريخ تسليم واضح ووعد استرجاع كامل. ابدأ بقائمة الانتظار.
ملحوظة لأسواقنا: طلب الدفع عند الاستلام مش التزام، ده "يمكن" لحد ما يتسلم. في التحقق خُد عربون مدفوع مقدمًا بلينك دفع أو محفظة أو تحويل.

**بعد الإطلاق:** حوّل أفكارك لقائمة تجارب مرتبة بـ [Growth Experiment Designer](../prompts/growth/growth-experiment-designer.md)، واستخدم [A/B Testing](../skills/community/ab-testing/SKILL.md) بس لما الزيارات تكفي، واقفل كل تجربة بـ [Campaign Postmortem](../prompts/paid-ads/campaign-postmortem.md).

</div>

## 🧠 Pro tips

- **Climb in order.** Pre-selling before interviews just tells you that *something* didn't sell, not why.
- **One change per rerun.** If the smoke test lands between the pass and fail lines, change one thing (the audience, the promise, or the price), not all three. Otherwise the rerun teaches nothing.
- **Your waitlist is also your first research panel.** Email the people who signed up and didn't pay. Their "why not" is your next Step 1.
- **Write down the losers too.** A stopped idea with a logged reason is worth more than a vague memory of "we tried that once".
- **Small budgets go further in Egypt.** The paid-ads benchmarks show Meta CPMs in Egypt far below US levels, so smoke tests there are cheap. The limit is usually price and margin, not media cost.

## 🔗 Related assets

- [Experiment Log template](../templates/EXPERIMENT_LOG_TEMPLATE.md): record every step's hypothesis, rule and result
- [Worked example: validating a product before launch](../worked-examples/pre-launch-validation-walkthrough.md): this ladder end to end
- [Growth Experiment Designer](../prompts/growth/growth-experiment-designer.md): the post-launch backlog
- [A/B Testing skill](../skills/community/ab-testing/SKILL.md): when traffic allows
- [ICP Research](../skills/community/icp-research/SKILL.md) and [Voice of Customer Synthesis](../skills/community/voice-of-customer-synthesis/SKILL.md): turn interview notes into usable inputs
- [Landing Page CRO Teardown](../prompts/cro/landing-page-cro-teardown.md): check the smoke-test page before you spend
- [Offer Stack Builder](../prompts/growth/offer-stack-builder.md) and [Lifetime Deal Launch Playbook](lifetime-deal-launch-playbook.md): shape the pre-sale offer
- [Paid Ads](../benchmarks/paid-ads-benchmarks.md) and [CRO & E-commerce](../benchmarks/cro-ecommerce-benchmarks.md) benchmarks: the sourced reference points used above

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
