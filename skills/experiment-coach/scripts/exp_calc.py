#!/usr/bin/env python3
"""Experiment Coach calculator — pre-launch and A/B maths, standard library only.

Every command prints the formula it used, so a chat-only assistant can show the
same working by hand. Rates accept 0.07 or 7 (anything > 1 is read as a percent).

  passline      required visitor→sign-up rate from your own unit economics
  precision     visitors needed to estimate one rate within ± a margin
  ab            sample size per arm (and duration) for a two-variant test
  significance  read out an A/B or before/after result (two-proportion z-test)
  srm           check the traffic split (sample ratio mismatch)
  budget        paid-traffic cost for a sample
  presale       pre-sales needed to cover a build or stock cost
  selftest      run the built-in checks

Examples:
  python3 exp_calc.py passline --price 150 --payback-months 3 --signup-to-paid 0.10 --cpc 3
  python3 exp_calc.py precision --p 0.07 --margin 0.02
  python3 exp_calc.py ab --baseline 0.05 --mde 20 --relative --daily-visitors 800
  python3 exp_calc.py significance --a-conv 29 --a-n 700 --b-conv 54 --b-n 720
  python3 exp_calc.py presale --cost 30000 --price 900 --fees 0.03
"""
import argparse
import math
import sys
from statistics import NormalDist

Z = NormalDist()


def rate(x):
    x = float(x)
    if x < 0:
        raise argparse.ArgumentTypeError("rates can't be negative")
    return x / 100 if x > 1 else x


def pct(x, digits=2):
    return f"{x * 100:.{digits}f}%"


# ── calculations ────────────────────────────────────────────────────────────

def max_cac(price=None, payback_months=None, margin=None, cac=None):
    """Most you can spend to acquire one paying customer."""
    if cac is not None:
        return cac
    if price is None:
        raise ValueError("give --max-cac, or --price with --payback-months (subscription) or --margin (one-off)")
    if payback_months is not None:
        return price * payback_months * (margin if margin is not None else 1.0)
    if margin is not None:
        return price * margin
    raise ValueError("with --price, also give --payback-months or --margin")


def passline(cac, signup_to_paid, cpc=None):
    """Affordable cost per sign-up, and the sign-up rate that makes paid traffic work.

    >>> round(passline(450, 0.10, 3)[1], 4)
    0.0667
    """
    cost_per_signup = cac * signup_to_paid
    required = cpc / cost_per_signup if cpc is not None else None
    return cost_per_signup, required


def precision_n(p, margin, confidence=0.95):
    """Visitors to estimate a rate within ± margin: exact z, and the conservative ×4 rule.

    >>> precision_n(0.07, 0.02)
    (626, 651)
    """
    z = Z.inv_cdf(1 - (1 - confidence) / 2)
    exact = math.ceil(z * z * p * (1 - p) / margin ** 2)
    rule = math.ceil(4 * p * (1 - p) / margin ** 2)
    return exact, rule


def ab_n(p1, p2, alpha=0.05, power=0.80):
    """Per-arm sample size for a two-sided two-proportion test.

    >>> 8100 < ab_n(0.05, 0.06) < 8250
    True
    """
    za = Z.inv_cdf(1 - alpha / 2)
    zb = Z.inv_cdf(power)
    pbar = (p1 + p2) / 2
    num = (za * math.sqrt(2 * pbar * (1 - pbar)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    return math.ceil(num / (p2 - p1) ** 2)


def two_prop(a_conv, a_n, b_conv, b_n, confidence=0.95):
    """Pooled z-test p-value, plus an unpooled CI for the difference B − A.

    >>> r = two_prop(29, 700, 54, 720)
    >>> round(r["p_value"], 3) < 0.05
    True
    """
    pa, pb = a_conv / a_n, b_conv / b_n
    pooled = (a_conv + b_conv) / (a_n + b_n)
    se0 = math.sqrt(pooled * (1 - pooled) * (1 / a_n + 1 / b_n))
    zstat = (pb - pa) / se0 if se0 else 0.0
    p_value = 2 * (1 - Z.cdf(abs(zstat)))
    se = math.sqrt(pa * (1 - pa) / a_n + pb * (1 - pb) / b_n)
    zc = Z.inv_cdf(1 - (1 - confidence) / 2)
    diff = pb - pa
    return {"pa": pa, "pb": pb, "diff": diff, "ci": (diff - zc * se, diff + zc * se),
            "rel": (diff / pa) if pa else float("nan"), "z": zstat, "p_value": p_value}


def srm(a_n, b_n, expected_a=0.5):
    """Chi-square (1 df) test that the observed split matches the planned split.

    >>> srm(5000, 5000)[1] > 0.99
    True
    >>> srm(5000, 5400)[1] < 0.001
    True
    """
    total = a_n + b_n
    ea, eb = total * expected_a, total * (1 - expected_a)
    chi2 = (a_n - ea) ** 2 / ea + (b_n - eb) ** 2 / eb
    p_value = 2 * (1 - Z.cdf(math.sqrt(chi2)))
    return chi2, p_value


def presale_needed(cost, price, fees=0.0):
    """Paid pre-sales needed to cover a cost, after payment fees.

    >>> presale_needed(30000, 900, 0.03)
    35
    """
    return math.ceil(cost / (price * (1 - fees)))


# ── CLI ─────────────────────────────────────────────────────────────────────

def cmd_passline(a):
    cac = max_cac(a.price, a.payback_months, a.margin, a.max_cac)
    cps, req = passline(cac, a.signup_to_paid, a.cpc)
    print("PASS LINE FROM UNIT ECONOMICS")
    if a.max_cac is None:
        if a.payback_months is not None:
            m = a.margin if a.margin is not None else 1.0
            print(f"  max CAC = price × payback months × margin = {a.price:g} × {a.payback_months:g} × {m:g} = {cac:,.2f}")
        else:
            print(f"  max CAC = price × margin = {a.price:g} × {a.margin:g} = {cac:,.2f}")
    else:
        print(f"  max CAC (given) = {cac:,.2f}")
    print(f"  affordable cost per sign-up = max CAC × sign-up→paid = {cac:,.2f} × {a.signup_to_paid:g} = {cps:,.2f}")
    if req is not None:
        print(f"  required sign-up rate = CPC ÷ cost per sign-up = {a.cpc:g} ÷ {cps:,.2f} = {pct(req)}")
        print("  Write it into the decision rule BEFORE the test. The sign-up→paid rate is a guess until a pre-sale measures it.")
    else:
        print("  Add --cpc (measure it with a small pilot) to get the required sign-up rate.")


def cmd_precision(a):
    exact, rule = precision_n(a.p, a.margin, a.confidence)
    print("VISITORS TO ESTIMATE ONE RATE")
    print(f"  n = z² × p × (1 − p) ÷ m²  with p = {pct(a.p)}, m = ±{pct(a.margin)}, confidence = {a.confidence:g}")
    print(f"  exact: {exact:,} visitors  ·  conservative rule (z² ≈ 4): {rule:,} visitors")
    if a.cpc:
        print(f"  budget at CPC {a.cpc:g}: {exact * a.cpc:,.0f} – {rule * a.cpc:,.0f}")


def cmd_ab(a):
    p1 = a.baseline
    p2 = p1 * (1 + a.mde) if a.relative else p1 + a.mde
    if not 0 < p2 < 1:
        sys.exit("the variant rate falls outside 0–100%; check --mde / --relative")
    n = ab_n(p1, p2, a.alpha, a.power)
    print("A/B SAMPLE SIZE (two-sided, two arms, equal split)")
    print(f"  baseline {pct(p1)} → variant {pct(p2)} (detecting a {abs(p2 - p1) * 100:.2f}-point absolute change)")
    print(f"  alpha {a.alpha:g}, power {a.power:g} → {n:,} visitors PER ARM, {2 * n:,} total")
    if a.daily_visitors:
        days = math.ceil(2 * n / a.daily_visitors)
        weeks = math.ceil(days / 7)
        print(f"  at {a.daily_visitors:,.0f} eligible visitors/day: {days} days → run {weeks} full week(s) to cover weekday cycles")
        if days > 42:
            print("  ⚠ Longer than ~6 weeks: test a bigger change, a higher-traffic step, or use a pre-launch method instead.")


def cmd_significance(a):
    r = two_prop(a.a_conv, a.a_n, a.b_conv, a.b_n, a.confidence)
    lo, hi = r["ci"]
    print("READOUT (B vs A)")
    print(f"  A: {a.a_conv}/{a.a_n} = {pct(r['pa'])}   B: {a.b_conv}/{a.b_n} = {pct(r['pb'])}")
    print(f"  difference: {r['diff'] * 100:+.2f} percentage points (relative {r['rel'] * 100:+.1f}%)")
    print(f"  {a.confidence * 100:.0f}% CI for the difference: {lo * 100:+.2f} to {hi * 100:+.2f} points")
    print(f"  z = {r['z']:.2f}, two-sided p = {r['p_value']:.4f}")
    if lo > 0 or hi < 0:
        print("  The interval excludes zero. Now check: was this the pre-registered metric and sample, and does the guardrail hold?")
    else:
        print("  The interval includes zero: no reliable difference at this sample. Don't call a winner.")


def cmd_srm(a):
    chi2, p = srm(a.a_n, a.b_n, a.expected)
    print("SAMPLE RATIO CHECK")
    print(f"  planned split {a.expected:g}/{1 - a.expected:g}, observed {a.a_n:,} / {a.b_n:,}")
    print(f"  chi² = {chi2:.2f}, p = {p:.4f}")
    print("  ⚠ p < 0.01: the split is broken (tracking, redirects, bots). Fix it before reading results." if p < 0.01
          else "  Split looks fine.")


def cmd_budget(a):
    print("TRAFFIC BUDGET")
    print(f"  {a.visitors:,} visitors × CPC {a.cpc:g} = {a.visitors * a.cpc:,.0f}")


def cmd_presale(a):
    n = presale_needed(a.cost, a.price, a.fees)
    print("PRE-SALE BREAK-EVEN")
    print(f"  pre-sales = cost ÷ (price × (1 − fees)) = {a.cost:,.0f} ÷ ({a.price:g} × {1 - a.fees:g}) = {n} paid customers")
    if a.waitlist:
        print(f"  from a waitlist of {a.waitlist:,}: needs {pct(n / a.waitlist, 1)} of it to pay")


def cmd_selftest(_):
    import doctest
    failures, tests = doctest.testmod(verbose=False)
    # Worked-example numbers (worked-examples/pre-launch-validation-walkthrough.md)
    assert precision_n(0.07, 0.02)[1] == 651
    assert abs(passline(450, 0.10, 3)[1] - 0.0667) < 1e-3
    assert round(29 / 700, 3) == 0.041 and round(54 / 720, 3) == 0.075
    print(f"selftest: {tests} doctests, {failures} failures; worked-example checks passed")
    sys.exit(1 if failures else 0)


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("passline", help="required sign-up rate from unit economics")
    s.add_argument("--max-cac", type=float, help="most you can spend per paying customer (skip price/margin)")
    s.add_argument("--price", type=float, help="price per month (subscription) or per order (one-off)")
    s.add_argument("--payback-months", type=float, help="months of revenue you'll spend to acquire a customer")
    s.add_argument("--margin", type=rate, help="gross margin share, e.g. 0.4 (one-off products)")
    s.add_argument("--signup-to-paid", type=rate, required=True, help="share of sign-ups expected to pay (a guess until a pre-sale)")
    s.add_argument("--cpc", type=float, help="your measured cost per click")
    s.set_defaults(fn=cmd_passline)

    s = sub.add_parser("precision", help="visitors to estimate one rate within ± margin")
    s.add_argument("--p", type=rate, required=True, help="expected rate")
    s.add_argument("--margin", type=rate, required=True, help="± margin, e.g. 0.02 for two points")
    s.add_argument("--confidence", type=float, default=0.95)
    s.add_argument("--cpc", type=float)
    s.set_defaults(fn=cmd_precision)

    s = sub.add_parser("ab", help="per-arm sample size and duration")
    s.add_argument("--baseline", type=rate, required=True)
    s.add_argument("--mde", type=float, required=True, help="minimum detectable effect: absolute (0.01) or with --relative (20 = +20%%)")
    s.add_argument("--relative", action="store_true")
    s.add_argument("--alpha", type=float, default=0.05)
    s.add_argument("--power", type=float, default=0.80)
    s.add_argument("--daily-visitors", type=float)
    s.set_defaults(fn=cmd_ab)

    s = sub.add_parser("significance", help="two-proportion readout")
    for k in ("a-conv", "a-n", "b-conv", "b-n"):
        s.add_argument(f"--{k}", type=int, required=True)
    s.add_argument("--confidence", type=float, default=0.95)
    s.set_defaults(fn=cmd_significance)

    s = sub.add_parser("srm", help="sample ratio mismatch check")
    s.add_argument("--a-n", type=int, required=True)
    s.add_argument("--b-n", type=int, required=True)
    s.add_argument("--expected", type=float, default=0.5, help="planned share for A")
    s.set_defaults(fn=cmd_srm)

    s = sub.add_parser("budget", help="paid-traffic cost for a sample")
    s.add_argument("--visitors", type=int, required=True)
    s.add_argument("--cpc", type=float, required=True)
    s.set_defaults(fn=cmd_budget)

    s = sub.add_parser("presale", help="pre-sales needed to cover a cost")
    s.add_argument("--cost", type=float, required=True, help="build, stock or launch cost to cover")
    s.add_argument("--price", type=float, required=True)
    s.add_argument("--fees", type=rate, default=0.0, help="payment fees share")
    s.add_argument("--waitlist", type=int)
    s.set_defaults(fn=cmd_presale)

    s = sub.add_parser("selftest", help="run built-in checks")
    s.set_defaults(fn=cmd_selftest)

    a = p.parse_args(argv)
    if a.cmd == "ab" and a.relative:
        a.mde = a.mde / 100 if a.mde > 1 else a.mde
    elif a.cmd == "ab":
        a.mde = rate(a.mde)
    try:
        a.fn(a)
    except ValueError as e:
        sys.exit(f"error: {e}")


if __name__ == "__main__":
    main()
