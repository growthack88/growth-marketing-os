---
name: icp-research
version: "4.2"
author: genesys-growth
last_updated: 2026-03-15
description: >
  Scrapes case studies, testimonials, and solutions pages from a target
  website to build structured ICP documentation. Produces TAM analysis,
  firmographic segments, champion and economic buyer personas, use case
  mapping, customer proof points, and voice-of-customer synthesis with
  normalized attributes. Requires website URL as primary input.
  Upstream: recommended company-context. Downstream: feeds positioning,
  product-messaging, landing-page-copy, content-strategy, and outreach-emails.
---

<!--
COMMUNITY SKILL — included under its original MIT license.
Source: https://github.com/matteotitta/genesys-skills by Matteo Titta (MIT).
License text: ../LICENSE-genesys-skills.txt
Curated into Growth Marketing OS by Mahmoud Omar (mahmoudomar.com) — this file
is NOT original work by the repo author; see /skills/community/README.md.
-->


# ICP research skill

Generate ideal customer profiles for B2B SaaS clients through systematic research and structured output.

## Report structure

The final ICP report follows this numbered section order:

| Section | Purpose |
|---------|---------|
| Header | Research date, website, category, confidence score (1-5) |
| 1. Executive summary | High-level synthesis of findings and strategic recommendations |
| 2. TAM analysis | Market sizing with targeting strategy per layer (TAM/SAM/SOM/ICP) |
| 3. Firmographics analysis | Geographic, industry, company segment patterns, and technographics |
| 4. Roles and personas | Core use case, Champion deep-dive, Economic Buyer deep-dive, buying journey |
| 5. Negative ICP | Who is NOT a fit, disqualification criteria, and red flags |
| 6. Customer proof points | Named customers, outcomes, and evidence with URLs |
| 7. Voice of customer synthesis | Language patterns, pain points, and outcome terminology |
| 8. ICP segment definitions | Scoring matrix, in-market signals, segment deep-dives |
| 9. Intent signals and buying triggers | Observable signals indicating purchase readiness |
| 10. Recommendations | Prioritization and messaging by segment |
| 11. Data gaps | Missing information and follow-up suggestions |
| 12. Source appendix | All sources with access dates, URLs, and confidence levels |

**Confidence score calculation**: Count High/Medium/Low data points. Score 5 if >70% High, Score 4 if >50% High, Score 3 if mixed, Score 2 if >50% Low, Score 1 if >70% Low.

---

## Output dimensions

Research produces structured outputs across multiple dimensions. See `references/dimension-schemas.md` for complete field definitions.

### TAM analysis

Market opportunity sizing with explicit methodology, assumptions, and targeting strategy.

| Field | Description |
|-------|-------------|
| TAM summary | Rich paragraph explaining total addressable market with methodology |
| TAM calculation table | Metric, value, source/basis, and **targeting strategy** for each layer |
| ICP row | Below SOM: highest priority segment based on research findings |
| Assumptions | Documented assumptions underlying each estimate |

**TAM table structure:**

| Metric | Value | Source/Basis | Targeting strategy |
|--------|-------|--------------|-------------------|
| TAM | $XB | [Methodology] | Long-term market awareness and category leadership |
| SAM | $XM | [Qualification] | Segment-specific campaigns and channel strategy |
| SOM | $XM | [Capture estimate] | Direct sales and targeted ABM |
| **ICP** | $XM | [Research findings] | Highest-priority accounts for immediate focus |

### Firmographics

Company attributes that define ideal customers with segment deep-dives.

| Field | Description |
|-------|-------------|
| Geography summary | Paragraph with regional patterns and evidence |
| Geography table | Regions sorted by concentration, with URL + date evidence |
| Industry summary | Paragraph explaining vertical patterns |
| Industry table | Industries sorted by presence, with URL + date evidence |
| Company segments summary | Paragraph describing size/stage patterns |
| Segments table | Enterprise → Mid-market → SMB → Startup |
| **Segment deep-dives** | For each segment: Priorities, ICP-fit, Budget & sales cycle, Unique approach, Proof points |
| **Technographics** | Required tools, integrations, and tech stack indicators |
| Adjacent stack | Common tools and integrations |

**Company segment deep-dive structure:**

For each segment (Enterprise, Mid-market, SMB), include:
- **Priorities:** Key priorities within today's market trends and dynamics
- **ICP-fit:** Why this segment is a good fit for our product
- **Budget & sales cycle:** Spending power and typical cycle length
- **Unique approach:** How we target this segment uniquely
- **Proof points:** Stats of impact from representatives with URLs and dates

### Technographics

Required technology prerequisites and common stack patterns. This section identifies tools that indicate fit or readiness.

| Category | Purpose |
|----------|---------|
| CRM | Customer relationship management (Salesforce, HubSpot, Pipedrive) |
| E-commerce | Commerce platforms (Shopify, BigCommerce, WooCommerce) |
| Marketing automation | Email and automation (Klaviyo, Mailchimp, Braze, Marketo) |
| CDP | Customer data platforms (Segment, mParticle, Rudderstack) |
| Analytics | Product and web analytics (Amplitude, Mixpanel, Google Analytics, Posthog) |
| Cloud | Infrastructure providers (AWS, Azure, GCP, Vercel) |
| Data warehouse | Data storage (Snowflake, BigQuery, Redshift, Databricks) |
| ERP | Enterprise resource planning (SAP, NetSuite, Oracle) |
| Communication | Team communication (Slack, Microsoft Teams) |
| Project management | Work management (Jira, Asana, Monday, Linear) |

**Technographics table structure:**

| Category | Required/Preferred | Common tools | Why it matters | Evidence |
|----------|-------------------|--------------|----------------|----------|
| [Category] | Required | [Tool names] | [Product dependency or integration] | [Source] ([URL], [Date]) |
| [Category] | Preferred | [Tool names] | [Better fit or faster time-to-value] | [Source] ([URL], [Date]) |

### Personas

Who buys and uses the product, with explicit Champion and Economic Buyer deep-dives.

| Field | Description |
|-------|-------------|
| Persona overview | Rich paragraph summarizing buying committee structure |
| Personas table | Sorted: **Champion → Economic Buyer → User → Influencer** |
| **Core use case** | Business process definition with steps, scenarios, alternatives, drivers, outcomes |
| **Champion deep-dive** | Explicit template for the person who drives evaluation |
| **Economic Buyer deep-dive** | Explicit template for the person who controls budget |
| User deep-dive(s) | Additional personas who use the product daily |
| Use cases by role | Champion first, then by seniority |
| Alternatives mentioned | Competitors and substitutes with URLs |
| Buying journey | Champion → Economic Buyer → User columns |

**Core use case structure:**

- **Use case statement:** 1-2 sentences defining the business process
- **Key steps:** Numbered steps in the process
- **Core scenarios:** 3-4 typical scenarios
- **Current alternatives:** Competitors, Manual, DIY approaches
- **Business drivers:** What drives the need
- **Desired outcomes:** What success looks like

**Champion deep-dive structure (12 fields):**

The Champion is the person who feels the pain daily, drives the evaluation, and advocates internally for the solution.

1. **Titles:** Title variations with context (e.g., "Manager of X, Senior Y, Lead Z")
2. **Department & team size:** Where they sit and typical team structure
3. **Responsibilities:** Key responsibilities in paragraph form (2-3 sentences)
4. **Jobs to be done:** 3-5 product-agnostic jobs they're trying to accomplish
5. **Success metrics / KPIs:** How they're measured and what success looks like
6. **Challenges:** Things that make their job harder (obstacles they struggle with)
7. **Pain points:** Problems that hurt them directly (negative impact they feel)
8. **Current alternatives:** How they currently achieve goals without this product
9. **Problems with alternatives:** Specific issues with current approach
10. **Buying behavior:** How they typically discover and evaluate solutions
11. **Channels & influences:** Communities, content, events, and influencers they trust
12. **Testimonial:** Verbatim quote from case study with name, title, company, and description of product usage

**Economic Buyer deep-dive structure (13 fields):**

The Economic Buyer is the person who controls budget and makes the final purchasing decision.

1. **Titles:** Title variations with context (e.g., "VP of X, Director of Y, Head of Z")
2. **Department & team size:** Where they sit, reporting structure, direct reports
3. **Responsibilities:** Key responsibilities in paragraph form (2-3 sentences)
4. **Jobs to be done:** 3-5 business-level jobs they're trying to accomplish
5. **Success metrics / KPIs:** Business metrics they're accountable for
6. **Challenges:** Business-level obstacles they face
7. **Pain points:** Business impacts that create urgency
8. **What they actually care about:** Beyond stated concerns — what drives decisions
9. **Common objections:** Typical pushback during sales process
10. **What a "no-brainer" looks like:** Conditions that make approval easy
11. **Buying behavior:** How they evaluate and approve purchases
12. **Channels & influences:** Where they get information and who they trust
13. **Testimonial:** Verbatim quote from case study with name, title, company

### Negative ICP

Identifying who is NOT a fit helps sales disqualify quickly and avoid bad-fit deals.

| Field | Description |
|-------|-------------|
| Disqualification criteria | Table of attributes that indicate poor fit |
| Red flags | Warning signs from churned or unsuccessful customers |
| Objection patterns | Objections that signal poor fit vs. legitimate concerns |

### Intent signals and buying triggers

Observable events or behaviors indicating a company or persona is more likely to buy now.

| Field | Description |
|-------|-------------|
| Overview | Paragraph explaining signal detection strategy |
| Company-level signals | Events at the organization level |
| Persona-level signals | Behaviors from individual buyers |
| Signal sources | Where to detect each signal |

---

## Sorting rules

Apply consistent sorting across all tables:

| Dimension | Sort order |
|-----------|------------|
| Decision role | **Champion → Economic Buyer → User → Influencer** |
| Company size | Enterprise → Mid-market → SMB → Startup |
| Frequency | Very high → High → Medium → Low |
| Confidence | High → Medium → Low |
| Customer concentration | High → Medium → Low |
| Priority | 1 → 2 → 3 → 4 |
| Industry presence | Strong → Moderate → Emerging |

---

## Rich description requirements

Every section must include contextual paragraphs, not just tables. All evidence must include URL and access date.

### Minimum requirements

| Section | Required prose |
|---------|----------------|
| Each macro section (1-12) | Opening paragraph (3-5 sentences) summarizing findings |
| Each industry vertical | 2-3 sentences explaining why this industry fits and evidence |
| Each company segment | Deep-dive with Priorities, ICP-fit, Budget & sales cycle, Unique approach, Proof points |
| Champion persona | Full deep-dive with all 12 fields including Channels & influences |
| Economic Buyer persona | Full deep-dive with all 13 fields including Channels & influences |
| Core use case | Full definition with steps, scenarios, alternatives, drivers, outcomes |
| Each ICP segment | Deep-dive with Priorities, ICP-fit, Budget & sales cycle, Unique approach, Proof points |
| Negative ICP | Disqualification criteria, red flags, and objection patterns |
| Intent signals | Company-level and persona-level signals with detection sources |
| Data gaps | Paragraph explaining impact of missing data and mitigation |

### Paragraph quality checklist

- [ ] Opens with the key insight, not setup
- [ ] Includes specific evidence (names, numbers, sources)
- [ ] Includes URL and date for all evidence
- [ ] Explains the "so what" — why this matters
- [ ] Avoids generic language that could apply to any company

---

## Workflow

### Phase 1: Data extraction

1. **Discover key pages**
   ```
   Fetch: [domain]/customers OR /case-studies OR /success-stories
   Fetch: [domain]/solutions OR /use-cases OR /industries
   Fetch: [domain]/pricing
   Fetch: [domain]/integrations OR /partners
   Search: site:[domain] case study testimonial
   Search: site:g2.com "[company]" reviews
   Search: site:linkedin.com "[company]" hiring [relevant role]
   ```

2. **Extract raw data** per source (record URL and date for each):
   - Customer names and logos
   - Job titles and roles mentioned
   - Industry and company size indicators
   - Quantified outcomes and stats
   - Verbatim quotes and pain point language
   - Use case descriptions and workflows
   - Tech stack and integrations
   - Community and content references

3. **Normalize attributes**

   | Attribute | Normalization rules |
   |-----------|---------------------|
   | Geography | Map to: US, North America, EMEA, APAC, LATAM, Global |
   | Industry | Use standard verticals: SaaS, E-commerce, Finance, Healthcare, etc. |
   | Company size | Revenue bands: <$1M, $1-10M, $10-50M, $50-100M, $100M+ |
   | Team size | Employee bands: 1-10, 11-50, 51-200, 201-500, 501-1000, 1000+ |
   | Tech stack | Category + tool name: CRM (Salesforce), CDP (Segment) |

### Phase 2: Analysis and synthesis

For each segment (by industry x company size):

1. **Identify patterns** across extracted data
2. **Define core use case** with steps, scenarios, alternatives, drivers, outcomes
3. **Build Champion deep-dive** with all 12 fields including Channels & influences
4. **Build Economic Buyer deep-dive** with all 13 fields including Channels & influences
5. **Map use cases** to segment-specific needs
6. **Identify negative ICP** criteria and red flags
7. **Identify intent signals** at company and persona level
8. **Collect proof points** with testimonials for personas and segments
9. **Document technographics** with required and preferred tools
10. **Calculate TAM estimate** with targeting strategy per layer
11. **Identify ICP** as highest-priority segment below SOM

### Phase 3: Structured output

Generate numbered sections following the report structure above.

Apply sorting rules to all tables (Champion first for personas).

Include rich descriptions with URLs and dates for all evidence.

Include deep-dives for company segments, personas (Champion and Economic Buyer explicitly), and ICP segments.

---

## Input requirements

### Required
- **Website URL**: Primary company website

### Optional (improves quality)

| Input | Purpose |
|-------|---------|
| Case studies URL | Direct link to case studies page |
| Testimonials URL | Direct link to testimonials |
| Market context | Category, competitors, GTM approach |
| Sales call notes | Win/loss context, objections |
| Existing ICP docs | Validate or expand current understanding |

---

## Anti-hallucination guardrails

1. **Never invent customer names.** Only cite publicly referenced customers.
2. **Quote verbatim.** Use exact customer language in quotes.
3. **Mark confidence levels.** Tag data as High/Medium/Low confidence.
4. **Cite sources with URLs and dates.** Include URL and access date for every claim.
5. **Acknowledge gaps.** Explicit "Not available" for missing data.

| Confidence | Definition |
|------------|------------|
| High | Direct from official source, verifiable |
| Medium | Third-party source, multiple signals |
| Low | Single indirect source, inferred |

---

## Reference files

| File | Purpose |
|------|---------|
| `references/dimension-schemas.md` | Complete field definitions for all dimensions |
| `references/icp-output-template.md` | Full report template with numbered sections |
| `references/search-patterns.md` | Detailed search queries per data type |
| `references/examples/example-strapi.md` | Worked example: Strapi (headless CMS) |

---

## Quality checklist

- [ ] All 12 numbered sections present
- [ ] Every section has opening synthesis paragraph
- [ ] All tables sorted per sorting rules (Champion first for personas)
- [ ] TAM table includes ICP row with targeting strategy
- [ ] Technographics section included with Required/Preferred tools
- [ ] Core use case defined with steps, scenarios, alternatives, drivers, outcomes
- [ ] Champion deep-dive includes all 12 fields with Channels & influences
- [ ] Economic Buyer deep-dive includes all 13 fields with Channels & influences
- [ ] Persona deep-dives include testimonials with quotes
- [ ] Company segment deep-dives include Priorities, ICP-fit, Budget & sales cycle, Unique approach, Proof points
- [ ] Negative ICP documented with disqualification criteria and red flags
- [ ] Intent signals documented with company-level and persona-level signals
- [ ] ICP segment deep-dives include Priorities, ICP-fit, Budget & sales cycle, Unique approach, Proof points
- [ ] Customer names sourced from public references only
- [ ] Firmographics normalized to standard attributes
- [ ] VOC quotes are verbatim with source URLs and dates
- [ ] All evidence includes URL and access date
- [ ] Confidence levels assigned to all key data
- [ ] Data gaps documented with follow-up suggestions
