# MENA Market Playbook — what changes when the account runs in the Arab world

Load this file for any account that targets Egypt, the GCC (KSA, UAE, Kuwait, Qatar, Bahrain, Oman), the Levant, Iraq, or North Africa. It is the layer generic ad playbooks don't have. Facts that move (calendar dates, tax rates, platform reach, regulation) are marked **verify** — check them before quoting them to a client.

---

## 1 · Market map: one region, several different ad markets

| Market | Typical shape | Platforms that usually carry volume | Payment reality | Creative register |
|---|---|---|---|---|
| **Egypt** | Huge reach, very low CPMs, low AOV, price-sensitive | Facebook + Instagram, TikTok, YouTube, Google Search | COD dominant; InstaPay, Fawry, wallets, BNPL (valU, Sympl) growing | Egyptian عامية, humour, price/value framing |
| **KSA** | High AOV, high CPMs, young population | Snapchat (often #1 for reach), TikTok, Instagram, X, Google, YouTube | Mada, Apple Pay, BNPL (Tabby, Tamara), COD still present | Saudi/Gulf dialect, family, status, national pride |
| **UAE** | Most international, majority expat | Instagram, Google, YouTube, Meta, LinkedIn (B2B), Snapchat, TikTok | Cards + Apple Pay, BNPL; COD low | English first for most categories, Arabic for nationals; Hindi/Urdu/Malayalam/Tagalog for expat segments |
| **Kuwait / Qatar / Bahrain / Oman** | Small, wealthy, saturates fast | Instagram, Snapchat, TikTok, Google | Cards, KNET (Kuwait), BNPL | Gulf dialect; frequency caps matter (small pools) |
| **Iraq / Jordan / Levant** | Mid CPMs, Facebook-heavy | Facebook, Instagram, TikTok, YouTube | COD common | Local dialects; Levantine for Jordan/Lebanon |
| **Morocco / Algeria / Tunisia** | Low CPMs, French + Darija | Facebook, Instagram, TikTok, YouTube | COD dominant | Darija + French code-switching, not Gulf Arabic |

Rules:
- **Never run one "MENA" campaign.** Split at least by country (often by country × language). CPMs, AOVs, delivery rates, and creative register differ by an order of magnitude between Egypt and Qatar; a blended campaign spends where it's cheapest, not where it's profitable.
- **Small GCC pools saturate.** Kuwait, Bahrain, Qatar, Oman: watch frequency weekly and rotate creative faster than in Egypt or KSA.
- **Egypt's cheap reach is a testing lab.** With Egyptian CPMs a fraction of GCC CPMs (see the [paid-ads benchmarks](https://github.com/growthack88/growth-marketing-os/blob/main/benchmarks/paid-ads-benchmarks.md) MENA table), test hooks and angles cheaply in Egypt, then port winners to the GCC in the right dialect. Margin and AOV, not media cost, are Egypt's constraint.

## 2 · Language, dialect, and audience targeting

- **Pick the dialect per market** — Egyptian عامية for Egypt, Gulf/Saudi (خليجي/سعودي) for the GCC, Darija + French for the Maghreb. MSA (فصحى) reads like a government notice in a performance ad; use it only for formal B2B, government, finance, or legal categories where it signals trust. For copy itself, hand off to the [Arabic Copy Localizer](../../arabic-copy-localizer/SKILL.md) when it is installed.
- **Code-switching is native, not lazy:** product, tech and business words often stay in English ("offer", "delivery", "app", "cashback") inside Arabic sentences. Mirror how the audience writes in comments.
- **Device language ≠ audience language.** Many Arab users run their phones and Google in English. In Google Ads, target **Arabic + English** for Arabic campaigns; on Meta and TikTok, don't restrict Arabic creative to Arabic-language users unless you have tested it.
- **Expat segments in the GCC** (UAE especially, also KSA, Qatar, Kuwait) are separate audiences with separate languages, price sensitivity, and calendars (Diwali, Onam, Christmas, Chinese New Year). Build them as separate ad sets with their own creative, not as a translation of the Arabic ad.
- **Arabic search behaviour (Google, Snapchat search, TikTok search):** cover spelling variants: ة/ه, ى/ي, أ/إ/ا, with and without "ال", Arabizi/Franco ("se3r", "3ard"), English transliterations, and common misspellings. Use them in keyword lists, negatives, and Shopping titles.
- **RTL creative QA:** check that Arabic text renders right-to-left, numbers and Latin brand names don't flip, line breaks don't orphan one word, and Arabic copy is ~20-30% longer than English, so compress headlines before they get truncated.

## 3 · The calendar (plan 4-6 weeks ahead)

Islamic dates move about 11 days earlier each year and depend on moon sighting. **Verify every date** before you lock a flight plan.

| Moment | Approx. timing | What happens to ads |
|---|---|---|
| **Ramadan** | ~8 Feb – 9 Mar 2027 (verify); ~28 Jan – 26 Feb 2028 (verify) | Usage moves to after iftar and late night (roughly 9 pm – 2 am) and suhoor. CPMs rise through the month, peaking in the last 10 days. Content tone: family, generosity, reflection. Food/F&B, fashion, gifting, telecom, and charity spike. |
| **Eid al-Fitr** | Right after Ramadan (~9-10 Mar 2027, verify) | Pre-Eid shopping peak (clothes, gifts, sweets, electronics) in the 7-10 days before. Delivery cut-off dates matter more than bids. |
| **Eid al-Adha** | ~16-17 May 2027 (verify) | Travel + gifting + livestock/F&B; many GCC residents travel, so local reach drops. |
| **Hijri New Year / Mawlid** | Varies | Low commercial weight; mind tone. |
| **Saudi Founding Day** | 22 Feb | National pride creative (KSA). |
| **Mother's Day (Arab world)** | 21 Mar | Big gifting moment in Egypt and much of the region. |
| **Summer** | Jul – Aug | GCC residents travel; KSA/UAE local reach drops and travel/tourism spikes. Egypt's North Coast (الساحل) season. |
| **Back to school** | Late Aug – Sep (GCC), Sep – Oct (Egypt) | Electronics, stationery, uniforms, education. |
| **Saudi National Day** | 23 Sep | Heavy retail discounting in KSA. |
| **11.11** | 11 Nov | Strong in GCC marketplaces. |
| **White Friday / Yellow Friday / Black Friday** | Late Nov | The region's biggest discount window; marketplaces (Amazon, noon) set the pricing tone. CPMs spike. |
| **UAE National Day (Eid Al Etihad)** | 2 Dec | UAE pride and retail campaigns. |
| **Qatar National Day** | 18 Dec | Qatar. |
| **Dubai Shopping Festival** | ~Dec – Jan (verify) | UAE retail + tourism. |
| **Kuwait National & Liberation Days** | 25-26 Feb | Kuwait. |

Seasonal rules:
- **Load creative before the season, not during it.** New ads launched in the first Ramadan week sit in learning while CPMs climb. Launch and exit learning 7-14 days before.
- **Ramadan dayparting:** shift budget weight to post-iftar and late-night windows only after checking your own hour-of-day data; don't blindly cut daytime (Google intent stays).
- **Expect CPM inflation in Ramadan, White Friday, and pre-Eid.** Judge efficiency on CPA/real ROAS, not CPM. Raise bid caps or cost caps ahead of time or delivery stalls.
- **Impulse seasons hurt COD quality.** Ramadan and sale seasons inflate placed orders and lower confirmation/delivery rates. Budget on delivered economics (see section 5).
- **Weekends differ by country:** KSA, Egypt, Kuwait, Qatar, Bahrain, Oman, Jordan: Friday–Saturday. UAE: Saturday–Sunday (Friday is a half working day). Morocco: Saturday–Sunday. Don't import "weekend = Sat/Sun" dayparting rules.
- **Friday midday prayer** dips engagement briefly in most markets — not worth a schedule rule, but don't read a Friday 12-2 pm dip as a creative problem.

## 4 · Platform reality in the region

- **Snapchat** is a top-tier channel in KSA and strong across the GCC (Snap's own audience figures claim very high reach among Saudi 13-34s — verify current numbers in Snap's audience insights). Never skip it for a Saudi consumer brand. See [snapchat.md](snapchat.md).
- **TikTok** is strong in KSA, Egypt, Iraq, and the UAE. Native creator-style Arabic content wins; polished TV ads lose.
- **Meta** (Facebook + Instagram) is the backbone almost everywhere; Facebook skews older and dominates Egypt/Iraq/Levant, Instagram dominates the GCC.
- **Click-to-WhatsApp (CTWA)** is a primary conversion path in the region, not a niche one. Many buyers would rather message a seller than fill a checkout. Run CTWA for high-consideration, high-ticket, or trust-sensitive offers, and measure it properly (see [tracking-measurement.md](tracking-measurement.md)).
- **X (Twitter)** has unusual weight in KSA for news, sports, and public conversation; it's a viable awareness channel there when most other markets would skip it.
- **Google Search + YouTube** capture intent everywhere; YouTube is the largest long-form video channel across the region.
- **LinkedIn** is the B2B channel for UAE/KSA, but CPCs are high; tighten targeting and use lead forms.
- **Marketplaces and retail media** (Amazon.sa/.ae/.eg, noon, Talabat, Careem, Namshi) are fast-growing ad channels; if the client sells on them, retail media budget belongs in the plan.

## 5 · Payments, COD, and what "conversion" means here

- **COD changes the conversion event.** A placed COD order is a promise, not revenue. Measure the full chain: Orders → Confirmed → Delivered (paid). Use the [COD Profit Funnel](https://github.com/growthack88/growth-marketing-os/blob/main/frameworks/cod-profit-funnel.md) math: `Real ROAS = delivered revenue ÷ spend`, `Real CPA = spend ÷ delivered orders`. Use `scripts/ads_calc.py cod` for the numbers, and hand deep COD ops questions to the [COD Operations Analyst](../../cod-operations-analyst/SKILL.md).
- **Feed better signals back to the algorithm:**
  1. Fire a server-side `Purchase` (or a custom `ConfirmedOrder`) event after the confirmation call/WhatsApp, normally within hours. Optimize toward it once it reaches ~50 events per week per ad set.
  2. Send delivered orders back as offline/CAPI events with the real value (Meta, TikTok, Snap, and Google offline/enhanced conversions all accept this), so value optimization learns from people who actually pay.
  3. Upload repeat refusers (RTO customers) as an exclusion list; upload delivered buyers as the seed for lookalikes.
- **BNPL (Tabby, Tamara, valU, Sympl) lifts AOV and conversion rate** in KSA/UAE/Egypt; it's an offer lever. "Split into 4 payments" in the ad is a legitimate hook — check the provider's brand rules.
- **Prepaid nudges** (small discount or free shipping for paying online) move good customers off COD and raise delivery rate.
- **Ad-account billing:** Egyptian advertisers paying in USD often hit bank limits on foreign card spend, so payments fail and delivery stops. Use a local-currency ad account, a backup payment method, or an authorized reseller. A failed payment pauses delivery and can hurt learning.
- **VAT on ad spend (verify current rates):** KSA 15%, UAE 5%, Egypt 14%, Bahrain 10%, Oman 5%; Qatar and Kuwait have no VAT. Platforms may add VAT to the invoice; budgets and CPA targets should state whether they include it.

## 6 · Compliance and cultural guardrails (checklist — not legal advice)

- **Prohibited or heavily restricted almost everywhere in the region:** alcohol, pork products, gambling/betting, dating, adult content, and certain financial products (crypto, forex, unlicensed lending). Platform policies vary by country — check per market.
- **Influencer and creator ads:** KSA requires creators doing paid ads to hold a Mawthooq licence (GCAM); the UAE requires an advertiser permit from the UAE Media Council for creators paid to promote. **Verify current rules** before signing creators, and keep the licence numbers on file.
- **Health, supplement, cosmetic and medical claims** need local regulator approvals (e.g., SFDA in KSA, EDA in Egypt, MOHAP/DHA in the UAE). "Clinically proven", "cures", or before/after claims without approval get ads rejected and accounts restricted.
- **Pricing:** show prices in local currency; KSA requires VAT-inclusive consumer prices. Discounts must be real (a reference price that actually existed). The big sale seasons get regulator attention.
- **Data protection:** KSA PDPL (SDAIA), UAE PDPL, Egypt Data Protection Law 151/2020. Customer-list uploads, lead forms, and WhatsApp messaging need a lawful basis and an opt-out. Don't upload lists you can't account for.
- **Cultural fit:** modest styling by default for GCC; no mocking of religion, the national leadership, or national symbols; careful with maps (disputed borders get ads pulled and brands boycotted); mind Ramadan daytime sensitivities (food/drink close-ups are fine for F&B brands, but timing and tone matter); gender mixing norms differ by market and category: test, don't assume.
- **Special ad categories** (housing, employment, credit, social issues) restrict targeting on Meta and Google; real estate, a huge category in UAE/KSA/Egypt, usually falls under the housing category. Plan audiences accordingly.

## 7 · MENA defaults to apply when the user gives nothing else

- Split by country; Arabic creative in the market's dialect plus English for UAE.
- Conversion event: confirmed/delivered orders for COD; purchase for prepaid; qualified lead (not raw lead) for lead-gen. Lead-gen in the region suffers from junk leads, so add a qualifying question to forms or use higher-intent form types, and send CRM-qualified leads back as conversions.
- Include Snapchat for any KSA consumer offer; include CTWA for any offer above the market's impulse price point.
- Prices in local currency, VAT stated, delivery time stated in the ad (it's a top objection).
- Check the calendar for the next 60 days before planning anything.
