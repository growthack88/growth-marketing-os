# Creative System — angles, hooks, Arabic copy, briefs, testing

Load for `creative`, `copy`, and `competitors`, and for any "creative fatigue" diagnosis. On Meta, TikTok and Snapchat, creative is the main targeting lever: the algorithm finds buyers through what the ad says and shows. So a new creative batch has to test a **new reason to buy**, not a new font.

---

## 1 · Angle-first: the research → angle → hook → brief pipeline

1. **Research (inputs):** reviews, comments, DMs, WhatsApp chats, call-centre notes, competitor ads (§6). Mine comments into categories: confusion, trust, price, product, delivery, support, competitor, praise. A theme counts only with ≥ 3 different people; < 30 real comments = directional only. Themes ≥ 20% of comments → fix in the ad or landing page; 5-20% → FAQ/objection ad; < 5% → log.
2. **Decompose each existing ad** into: audience · pain · promise · proof · mechanism · offer · CTA · objection handled. This shows which angles you've already tested (usually one: "best price").
3. **Build the angle matrix:** at least one angle per driver:

| Driver | Example angle (skincare, KSA) |
|---|---|
| Pain | "بشرتك تتعب من الحر والمكيف" |
| Desired outcome | Glow before an occasion / wedding season |
| Proof | Real Saudi customer reviews, numbers sold |
| Mechanism | Why this ingredient works in humid/dry climates |
| Objection-kill | "Is it original?": authenticity, SFDA registration, return policy |
| Identity/status | What women in her circle use |
| Enemy / alternative | Expensive clinic sessions vs a 3-minute routine |
| Occasion/season | Ramadan nights, Eid looks, National Day, summer travel |
| Offer | Bundle, gift with purchase, free delivery, Tabby split |
| Founder/brand story | Saudi-made, family business |

   Full 12-angle prompt: [Ad Angle Matrix](https://github.com/growthack88/growth-marketing-os/blob/main/prompts/paid-ads/ad-angle-matrix.md).
4. **Hooks per angle** (§2), **brief per hook** (§4), **test plan** (§3).

**Angle verdicts:** an angle "wins" only after ≥ 3× target CPA spent and ≥ 10 conversions, beating the blended result by ≥ 20%. An angle that wins on CTR only = "attention winner, conversion unproven". If an angle ran in only one audience/country, its result is confounded.

## 2 · Hooks

Write hooks in batches of 8-10, spread across mechanisms:

| Mechanism | Pattern | Arabic example (Egyptian / Gulf) |
|---|---|---|
| Pattern interrupt | Unexpected visual/sound/statement | "متشتريش ده قبل ما تشوف الفيديو ده" / "لا تشتري هذا قبل ما تشوف" |
| Open loop / curiosity | Withhold the answer | "الغلطة اللي بتبوّظ ٩٠٪ من..." |
| Direct claim | Specific, provable promise | "توصيل في الرياض خلال ٢٤ ساعة، والدفع عند الاستلام" |
| Identity call-out | Name the viewer | "لو انتي أم شغالة وما عندك وقت..." |
| Social-proof lead | Lead with numbers or a review | "+١٢ ألف طلب في مصر الشهر ده" |
| Confession / relatability | First-person admission | "كنت فاكر إن... لحد ما جربت" |
| Contrast / before-after | Old way vs new way (where allowed) | "قبل: ساعة كوي. بعد: ٥ دقايق" |
| Imperative | Command + reason | "وقّف اشتراكك في... وجرّب ده" |
| Question | A question in the viewer's words | "ليه ريحة العود ما تثبت؟" |

Arabic hook rules: the first 3-5 words carry the hook (Arabic runs ~20-30% longer than English); dialect matches the market; numbers in Western digits unless the brand uses Arabic-Indic digits consistently; no فصحى for consumer performance ads; avoid wordplay that only works in one dialect when the ad runs in several markets.

## 3 · Testing system

- **Two kinds of tests:** *concept* tests (big swings: UGC vs studio, testimonial vs demo, new angle) and *iteration* tests (one element: hook, first frame, headline, CTA, format). Run concepts first; iterate on winners.
- **Order:** concept → hook → visual/first frame → body → CTA/offer.
- **Ratio:** for every 3-5 iterations on a winning theme, launch 2-3 genuinely new concepts. Without exploration, the account runs out of angles.
- **Readable test:** set the success metric and minimum data before launching (e.g. ≥ 3× target CPA spent or ≥ 10 conversions per variant for a directional call; ~50+ conversions per variant for a confident A/B call). Low budgets: judge on a leading metric (hook rate, CTR, cost per add-to-cart) and say so.
- **Setup:** Meta: test new concepts inside the live Advantage+ campaign or a dedicated ABO test campaign with equal budgets; promote winners. TikTok/Snap: 3-6 creatives per ad group; replace losers weekly.
- **Egypt as a lab:** low Egyptian CPMs make angle tests cheap; port winning angles to the GCC, re-shot in Gulf dialect with Gulf talent.
- **Log every test:** hypothesis · variable · audience · dates · spend · result · decision. The log is the account's memory.

## 4 · Briefs

**Video / UGC brief (one per hook):**

```
Angle: [driver + one-sentence reason to buy]
Audience: [country · dialect · who exactly]
Hook (0-3 s): [line + first frame]
Beats: 3-8 s problem/desire · 8-15 s product/demo/mechanism · 15-22 s proof · last 3 s CTA
CTA + offer: [price in local currency · delivery time · payment options: COD/Tabby/Tamara/Apple Pay]
On-screen text: [Arabic captions, max 6-8 words per card]
Talent: [age, styling (modest by default in GCC), dialect]
Format: 9:16 master + 4:5 and 1:1 cut-downs; 15-30 s (TikTok/Snap 9-21 s)
Variations: 3 alternative hooks · 1 alternative angle · 1 alternative CTA
Compliance: claims allowed? licences (Mawthooq / UAE Media Council)? music licensed?
```

**Static brief:** one claim, one visual, one proof element, price/offer badge, CTA. Arabic headline ≤ 6 words, RTL layout (logo and reading flow right-to-left), 1:1 + 4:5 + 9:16.

**Production spec per monthly batch (mid-size account):** ~12 new creatives per platform family: 6 video + 6 static/carousel, across ≥ 4 angles, in 9:16 + 4:5 (+ 1:1 for some placements). Detailed UGC brief prompt: [UGC Brief Generator](https://github.com/growthack88/growth-marketing-os/blob/main/prompts/social/ugc-brief-generator.md).

## 5 · Copy by platform

**Frameworks:** PAS (pain → agitate → solve), AIDA, BAB (before → after → bridge), 4P (promise → picture → proof → push), FAB (feature → advantage → benefit). Pick by awareness: unaware → story/pain; problem-aware → PAS; solution-aware → mechanism + proof; product-aware → offer + objection-kill + urgency (only real urgency).

**Character limits** (verify; platforms change them):

| Platform | Limits |
|---|---|
| Meta | Primary text: first ~125 characters visible · headline ~40 · description ~30. Write 4 primary texts + 3 headlines per ad (Flexible format) |
| Google RSA | 15 headlines × 30 chars · 4 descriptions × 90 chars · paths 15 chars |
| TikTok | Ad text ~100 characters (keep short; the video carries the message) |
| Snapchat | Brand name ~25 · headline ~34 characters |
| LinkedIn | Intro ~150 visible · headline ~70 |
| X | 280 characters per post; card headline ~70 |

Arabic counts characters the same way, but Arabic words are longer: write to ~80% of the limit.

**Arabic copy rules:**
- Dialect per market: Egyptian (مصري) for Egypt, Gulf/Saudi (خليجي/سعودي) for the GCC, Levantine for Jordan/Lebanon, Darija/French for the Maghreb. MSA only for formal B2B, government, finance, healthcare.
- Keep English where the audience does: product/tech/business words, brand names, "offer", "delivery", "cashback".
- Always answer the region's top three objections somewhere in the copy: **Is it original? When does it arrive? How do I pay?**
- Prices in local currency (ر.س / د.إ / ج.م or SAR/AED/EGP), VAT-inclusive where required.
- CTA words that work: اطلب الآن · اطلبه دلوقتي · احجز · كلّمنا واتساب · تسوّق الآن. Match the CTA button language to the ad language.
- Deep localisation from English: [Arabic Copy Localizer](../../arabic-copy-localizer/SKILL.md) (when installed).

**Copy QA before launch:** dialect consistent · RTL renders correctly (numbers, Latin brand names, punctuation) · no truncated headline · claims allowed for the category · offer matches the landing page · CTA matches the objective.

## 6 · Competitor research (ad libraries)

Sources: **Meta Ad Library** (filter by country: SA, AE, EG…), **TikTok Creative Center** (top ads by country and industry) and **TikTok Ad Library**, **Google Ads Transparency Center**, **Snapchat Ads Gallery / political ads library** where available, **LinkedIn Ad Library**.

Read ads as signals, not results; you can't see their performance. Proxies:
- **Evergreen:** running ≥ 30 days (≥ 60 = strong signal they're profitable).
- **Breakout:** launched in the last 30 days with ≥ 4 variants = they're scaling an angle (2-3 variants = medium signal).
- Note: angle, hook, format, offer, dialect, talent, landing page, price, and payment/delivery claims.

Synthesis: rank angles as (a) used by several competitors **and** working for you → double down, (b) competitor-proven, untested by you → test next, (c) only you → potential whitespace, (d) nobody → low priority. Output the top 5-7 test ideas. Full prompt: [Competitor Ads Teardown](https://github.com/growthack88/growth-marketing-os/blob/main/prompts/paid-ads/competitor-ads-teardown.md). Never copy a competitor's creative or claims; adapt the insight.

## 7 · Seasonal creative (MENA)

- **Ramadan:** warm, family, generosity, night-time settings, lanterns/crescents used tastefully; launch 7-14 days before day 1 so ads exit learning before CPMs climb. Separate creative for the last 10 days (Eid prep: gifts, outfits, sweets, delivery cut-offs).
- **Eid:** gifting, new clothes, family gatherings, "arrives before Eid" guarantees.
- **National days** (KSA 23 Sep, Founding Day 22 Feb, UAE 2 Dec, Qatar 18 Dec, Kuwait 25-26 Feb): national colours and pride, respectful use of flags and symbols, no political content.
- **White/Yellow Friday & 11.11:** price + countdown + bundle; real reference prices only.
- **Summer (GCC):** travel, staying cool, delivery to holiday homes; Egypt: الساحل season.
