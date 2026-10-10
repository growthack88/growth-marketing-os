# Experiment Log Template · قالب سجل التجارب

One entry per test, pre-launch or post-launch. Fill in **Before** before the test starts. Fill in **After** only when the sample or the date in your decision rule is reached. Keep every entry, including stopped ideas. The log is how a team stops repeating old tests.

Used by the [Pre-Launch Validation Playbook](../playbooks/pre-launch-validation-playbook.md), the [Growth Experiment Designer](../prompts/growth/growth-experiment-designer.md) and the [Campaign Postmortem](../prompts/paid-ads/campaign-postmortem.md).

## Copy this block for each test

```markdown
### EXP-[number] · [short name]

**Before** (fill in before launch — don't edit after the test starts)
- Date started:
- Owner:
- Stage: pre-launch step [0 / 1 / 2 / 3 / 4] · or post-launch
- Riskiest assumption this tests:
- Hypothesis: We believe [audience] will [behavior] because [reason].
- Test: [interviews / smoke test / fake door / pre-sale / A/B test / other] — what exactly runs where
- Primary metric (one only):
- Guardrail metric (must not get worse):
- Sample needed: [n] — how you calculated it
- Budget / time cap:
- Decision rule:
  - Pass: if [metric] ≥ [line] after [sample] by [date] → [action]
  - Fail: if [metric] < [line] → [action]
  - In between: [the ONE change], rerun once
- Where the pass/fail lines came from: [your economics / benchmark file + section / previous test]

**After** (fill in at the sample size or date above)
- Date ended:
- Result: [metric value, sample reached, cost]
- Decision: pass / fail / rerun → what we did next
- What surprised us:
- Learning in one sentence (what the next test inherits):
- Links: [dashboard, page, ad set, postmortem]
```

## النسخة العربية

<div dir="rtl">

سجل واحد لكل تجربة، قبل الإطلاق أو بعده. املأ جزء **قبل** قبل ما الاختبار يبدأ، واملأ جزء **بعد** لما توصل لحجم العينة أو التاريخ المكتوب في قاعدة القرار. احتفظ بكل التجارب، حتى الأفكار اللي وقفتها، لأن السجل هو اللي بيمنع الفريق إنه يعيد نفس التجربة.


```markdown
### تجربة-[رقم] · [اسم مختصر]

**قبل** (يتملأ قبل الإطلاق، وميتعدلش بعد ما الاختبار يبدأ)
- تاريخ البداية:
- المسؤول:
- المرحلة: قبل الإطلاق خطوة [0 / 1 / 2 / 3 / 4] · أو بعد الإطلاق
- الافتراض الأخطر اللي بنختبره:
- الفرضية: نعتقد إن [الجمهور] هيعمل [السلوك] لأن [السبب].
- الاختبار: [مقابلات / اختبار دخان / باب وهمي / بيع مسبق / A/B / غيره] وبالظبط هيشتغل فين
- المؤشر الأساسي (واحد بس):
- مؤشر الحماية (لازم ميسوءش):
- حجم العينة المطلوب: [n] وإزاي حسبته
- حد الميزانية أو الوقت:
- قاعدة القرار:
  - نجاح: لو [المؤشر] ≥ [الحد] بعد [العينة] لحد [التاريخ] ← [الإجراء]
  - فشل: لو [المؤشر] < [الحد] ← [الإجراء]
  - في النص: [التغيير الواحد] ونعيد مرة واحدة
- الحدود جت منين: [حساباتنا / ملف benchmarks والقسم / تجربة سابقة]

**بعد** (يتملأ عند حجم العينة أو التاريخ)
- تاريخ النهاية:
- النتيجة: [قيمة المؤشر، العينة اللي وصلناها، التكلفة]
- القرار: نجاح / فشل / إعادة ← عملنا إيه بعدها
- إيه اللي فاجأنا:
- الدرس في جملة (اللي التجربة الجاية هتورثه):
- روابط: [الداشبورد، الصفحة، الإعلان، الـ postmortem]
```

</div>
