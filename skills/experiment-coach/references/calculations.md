# Calculations (do these by hand when code can't run)

Show every step to the user. Round sample sizes **up**. Write rates as decimals inside formulas (7% = 0.07). `scripts/exp_calc.py` runs the same formulas.

## 1 · Pass line from unit economics (`passline`)

1. **Max CAC**, the most you can spend to win one paying customer:
   - subscription: price per month × payback months (× gross margin if costs per user are high)
   - one-off product: price × gross margin
2. **Affordable cost per sign-up** = max CAC × expected sign-up→paid rate. That rate is an *assumption* until a pre-sale measures it, so label it.
3. **Required sign-up rate** = measured CPC ÷ affordable cost per sign-up.

Example: EGP 150/month, 3-month payback → max CAC 450. Guess 10% of sign-ups pay → EGP 45 per sign-up. CPC EGP 3 → 3 ÷ 45 = **6.7%**.

CPC must be **measured** with a small pilot spend. There are no reliable public MENA CPC benchmarks ([benchmarks-used](benchmarks-used.md)).

## 2 · Sample to estimate one rate (`precision`)

n = z² × p × (1 − p) ÷ m², where p is the expected rate and m is the ± margin. At 95% confidence z ≈ 1.96 (z² ≈ 3.84). The conservative shortcut uses 4.

Example: p = 0.07, m = 0.02 → 3.84 × 0.07 × 0.93 ÷ 0.0004 ≈ **626** (shortcut: **651**).

If p is unknown, use 0.5 (the worst case), or run a small pilot first.

## 3 · Budget (`budget`)

Budget = visitors needed × CPC. Not every click becomes a page view, so measure the click → landing-page-view ratio in the pilot and divide by it: budget = visitors ÷ landing ratio × CPC.

## 4 · A/B sample size and duration (`ab`)

Per arm, two-sided, equal split:

n = [ z₁₋α/₂ × √(2 p̄ (1 − p̄)) + z₁₋β × √(p₁(1 − p₁) + p₂(1 − p₂)) ]² ÷ (p₂ − p₁)²

with p̄ = (p₁ + p₂) ÷ 2. For α = 0.05 and power 0.8: z₁₋α/₂ = 1.96 and z₁₋β = 0.84.

Example: 5% → 6% needs about **8,158 per arm** (16,316 total). Duration = total ÷ eligible daily visitors, rounded **up to full weeks**. If it's longer than ~6 weeks, test a bigger change, a higher-traffic step, or go back to a pre-launch method.

Quick feel without a formula: smaller baselines and smaller effects need far more traffic. Halving the effect roughly quadruples the sample.

## 5 · Readout: two-proportion test (`significance`)

- p_A = conv_A ÷ n_A, p_B = conv_B ÷ n_B, pooled p = (conv_A + conv_B) ÷ (n_A + n_B)
- z = (p_B − p_A) ÷ √( p(1 − p)(1/n_A + 1/n_B) ), and the two-sided p-value comes from z (|z| ≥ 1.96 ↔ p ≤ 0.05)
- 95% CI for the difference: (p_B − p_A) ± 1.96 × √( p_A(1 − p_A)/n_A + p_B(1 − p_B)/n_B )

Report the difference in **percentage points** and relative %, the CI, and p. If the CI includes 0, there's no reliable difference at this sample. Don't call a winner.

Example: 29/700 (4.14%) vs 54/720 (7.50%) → +3.36 points, CI +0.93 to +5.78, z ≈ 2.70, p ≈ 0.007.

**Caveat:** two runs at different times are not a randomized A/B. Seasonality, ads and audience can differ. Present that kind of comparison as directional unless traffic was split at the same time.

## 6 · Pre-sale break-even (`presale`)

Pre-sales needed = cost to cover ÷ (price × (1 − payment fees)). Also show it as a share of the waitlist.

Example: EGP 30,000 ÷ (900 × 0.97) → **35** pre-sales. From an 83-person waitlist, that's 42%. A number like that says "cover part of the cost, or lower the build scope", not "fail".

## 7 · Traffic split check (`srm`)

chi² = Σ (observed − expected)² ÷ expected over both arms. With 1 degree of freedom, p < 0.01 means the split is broken (redirects, tracking, bots). Fix it before reading the test.

Example: 5,000 vs 5,400 on a planned 50/50 → chi² ≈ 15.4, p ≈ 0.0001 → broken.
