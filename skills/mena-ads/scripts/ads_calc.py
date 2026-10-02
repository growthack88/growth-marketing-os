#!/usr/bin/env python3
"""MENA Ads calculator — the numbers behind every scale / hold / kill call.

Standard library only. Works anywhere Python 3.8+ runs (Claude Code, Codex,
Gemini CLI, a terminal, or a code-interpreter sandbox in ChatGPT/Claude.ai).

Commands
  breakeven  Break-even ROAS / CPA from unit economics (COD-aware)
  cod        Real ROAS / CPA after confirmation + delivery, RTO tax, break-even delivery rate
  learning   Minimum daily budget to exit the learning phase per platform
  verdict    SCALE / HOLD / REDUCE / PAUSE (+ REFRESH) call for one campaign or ad set
  vat        Ad spend including platform VAT by country
  split      Split a monthly budget across funnel stages and platforms

Examples
  python3 ads_calc.py breakeven --price 499 --cogs 150 --shipping 45 --fees 3 --confirm 0.85 --deliver 0.78 --return-cost 30
  python3 ads_calc.py cod --spend 20000 --orders 400 --aov 499 --confirm 0.85 --deliver 0.78 \
      --cogs 150 --ship-out 45 --return-cost 30
  python3 ads_calc.py learning --platform meta --cpa 120
  python3 ads_calc.py verdict --spend 3000 --conversions 4 --target-cpa 400 --days 5
  python3 ads_calc.py vat --budget 10000 --country SA
  python3 ads_calc.py split --budget 30000 --goal sales --market KSA

Add --json to any command for machine-readable output.
"""
import argparse
import json
import sys

# Learning-phase rules of thumb (events per optimisation unit per 7 days).
# Platforms change these — verify in the platform's help centre.
LEARNING = {
    "meta": {"events": 50, "window_days": 7, "unit": "ad set",
             "note": "~50 optimisation events per ad set within 7 days of the last significant edit"},
    "tiktok": {"events": 50, "window_days": 7, "unit": "ad group",
               "note": "~50 conversions per ad group within 7 days; TikTok also advises budget well above target CPA"},
    "snap": {"events": 50, "window_days": 7, "unit": "ad squad",
             "note": "~50 conversions per ad squad per week for goal-based bidding to stabilise"},
    "google": {"events": 30, "window_days": 30, "unit": "campaign",
               "note": "tCPA works best with ~30+ conversions in 30 days (tROAS ~50); learning lasts ~7 days or ~3 conversion cycles"},
}

# VAT charged on ad spend by country — verify current rates before quoting.
VAT = {"SA": 0.15, "AE": 0.05, "EG": 0.14, "BH": 0.10, "OM": 0.05,
       "QA": 0.0, "KW": 0.0, "JO": 0.16, "MA": 0.20}
COUNTRY_NAMES = {"SA": "Saudi Arabia", "AE": "UAE", "EG": "Egypt", "BH": "Bahrain",
                 "OM": "Oman", "QA": "Qatar", "KW": "Kuwait", "JO": "Jordan", "MA": "Morocco"}

# Starting platform mixes by goal and market (share of the paid budget).
# These are starting hypotheses for a new plan, not benchmarks.
MIX = {
    ("sales", "KSA"): {"Meta": 0.30, "Snapchat": 0.25, "TikTok": 0.20, "Google": 0.25},
    ("sales", "UAE"): {"Meta": 0.40, "Google": 0.35, "TikTok": 0.15, "Snapchat": 0.10},
    ("sales", "EGYPT"): {"Meta": 0.55, "TikTok": 0.25, "Google": 0.20},
    ("sales", "GCC"): {"Meta": 0.35, "Google": 0.30, "Snapchat": 0.20, "TikTok": 0.15},
    ("leads", "KSA"): {"Meta": 0.35, "Google": 0.35, "Snapchat": 0.15, "TikTok": 0.15},
    ("leads", "UAE"): {"Google": 0.45, "Meta": 0.40, "LinkedIn": 0.15},
    ("leads", "EGYPT"): {"Meta": 0.55, "Google": 0.35, "TikTok": 0.10},
    ("leads", "GCC"): {"Google": 0.40, "Meta": 0.40, "Snapchat": 0.10, "TikTok": 0.10},
    ("b2b", "ANY"): {"LinkedIn": 0.45, "Google": 0.40, "Meta": 0.15},
    ("app", "ANY"): {"Meta": 0.35, "Google App Campaigns": 0.30, "TikTok": 0.20, "Snapchat": 0.15},
}
FUNNEL = {"sales": (0.30, 0.25, 0.45), "leads": (0.30, 0.25, 0.45),
          "b2b": (0.35, 0.30, 0.35), "app": (0.50, 0.20, 0.30), "awareness": (0.70, 0.20, 0.10)}


def pct(x):
    return f"{x * 100:.1f}%"


def money(x):
    return f"{x:,.2f}"


def out(args, data, lines):
    if args.json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        print("\n".join(lines))


def rate(value, name, small=False):
    """Accept 0.78 or 78 for 78%.

    small=True is for parameters that are normally a few percent (fees, margins,
    CTR drops): there, 1 means 1%, not 100%.
    """
    if value is None:
        return None
    if value > 1 or (small and value == 1):
        value = value / 100.0
    if not 0 < value <= 1:
        sys.exit(f"{name} must be between 0 and 1 (or 0-100 as a percentage)")
    return value


def cmd_breakeven(a):
    fees = rate(a.fees, "fees", small=True) if a.fees else 0.0
    c = rate(a.confirm, "confirm") if a.confirm else 1.0
    d = rate(a.deliver, "deliver") if a.deliver else 1.0
    cash_rate = c * d  # share of PLACED orders that become cash
    margin_per_delivered = a.price - a.cogs - a.shipping - a.other - a.price * fees
    if margin_per_delivered <= 0:
        sys.exit("Unit margin is zero or negative before ads: fix price/costs first; no ROAS can save it.")
    # Unconfirmed orders are never shipped (no cost). Confirmed-but-failed ones cost shipping out + return.
    rto_cost_per_placed = c * (1 - d) * (a.shipping + a.return_cost)
    profit_per_placed = cash_rate * margin_per_delivered - rto_cost_per_placed
    if profit_per_placed <= 0:
        sys.exit(f"At {pct(c)} confirmation x {pct(d)} delivery, each placed order loses money before ads: fix ops first.")
    be_cpa_placed = profit_per_placed
    be_cpa_delivered = profit_per_placed / cash_rate
    be_roas_platform = a.price / be_cpa_placed  # platforms count placed orders at full price
    be_roas_real = (a.price * cash_rate) / be_cpa_placed
    target_cpa = be_cpa_placed / 1.2  # 20% safety buffer: the default working target
    data = {
        "cash_rate_of_placed_orders": round(cash_rate, 4),
        "margin_per_delivered_order": round(margin_per_delivered, 2),
        "profit_per_placed_order_before_ads": round(profit_per_placed, 2),
        "breakeven_cpa_per_placed_order": round(be_cpa_placed, 2),
        "breakeven_cpa_per_delivered_order": round(be_cpa_delivered, 2),
        "breakeven_platform_roas": round(be_roas_platform, 2),
        "breakeven_real_roas": round(be_roas_real, 2),
        "suggested_target_cpa_placed": round(target_cpa, 2),
        "suggested_target_platform_roas": round(a.price / target_cpa, 2),
    }
    lines = [
        "BREAK-EVEN",
        f"  Margin per delivered order ........ {money(margin_per_delivered)}",
        f"  Placed orders that become cash .... {pct(cash_rate)}  (confirm {pct(c)} x deliver {pct(d)})",
        f"  Profit per PLACED order before ads  {money(profit_per_placed)}",
        f"  Break-even CPA (placed order) ..... {money(be_cpa_placed)}",
        f"  Break-even CPA (delivered order) .. {money(be_cpa_delivered)}",
        f"  Break-even ROAS as platforms show it (placed revenue) ... {be_roas_platform:.2f}",
        f"  Break-even REAL ROAS (delivered revenue) ............... {be_roas_real:.2f}",
        f"  Suggested working target (break-even / 1.2): CPA <= {money(target_cpa)} "
        f"-> platform ROAS >= {a.price / target_cpa:.2f}",
    ]
    target_margin = rate(a.target_margin, "target-margin", small=True) if a.target_margin else None
    if target_margin:
        tm_cpa = be_cpa_placed - a.price * cash_rate * target_margin
        if tm_cpa <= 0:
            lines.append(f"  A {pct(target_margin)} net margin on delivered revenue is not reachable with paid traffic.")
            data["target_cpa_placed"] = None
        else:
            data["target_cpa_placed"] = round(tm_cpa, 2)
            data["target_platform_roas"] = round(a.price / tm_cpa, 2)
            lines.append(f"  For {pct(target_margin)} net margin on delivered revenue: CPA <= {money(tm_cpa)} "
                         f"-> platform ROAS >= {a.price / tm_cpa:.2f}")
    lines.append("  Use the suggested target as --target-cpa in `verdict`. Below break-even, every sale loses money.")
    out(a, data, lines)


def cmd_cod(a):
    c = rate(a.confirm, "confirm")
    d = rate(a.deliver, "deliver")
    confirmed = a.orders * c
    delivered = confirmed * d
    failed = confirmed - delivered
    placed_rev = a.orders * a.aov
    real_rev = delivered * a.aov
    platform_roas = placed_rev / a.spend if a.spend else 0
    real_roas = real_rev / a.spend if a.spend else 0
    platform_cpa = a.spend / a.orders if a.orders else 0
    real_cpa = a.spend / delivered if delivered else float("inf")
    rto_tax = failed * (a.ship_out + a.return_cost)
    data = {"confirmed": round(confirmed, 1), "delivered": round(delivered, 1), "failed": round(failed, 1),
            "platform_roas": round(platform_roas, 2), "real_roas": round(real_roas, 2),
            "platform_cpa": round(platform_cpa, 2), "real_cpa": round(real_cpa, 2),
            "rto_tax": round(rto_tax, 2), "end_to_end_rate": round(c * d, 4)}
    lines = [
        "COD REAL ECONOMICS",
        f"  Orders placed {a.orders:,.0f} → confirmed {confirmed:,.0f} ({pct(c)}) → delivered {delivered:,.0f} ({pct(d)})",
        f"  End-to-end: {pct(c * d)} of placed orders become cash",
        f"  ROAS   platform {platform_roas:.2f}  →  REAL {real_roas:.2f}",
        f"  CPA    platform {money(platform_cpa)}  →  REAL {money(real_cpa)} per delivered order",
        f"  RTO tax (shipping out + return on {failed:,.0f} failed) ........ {money(rto_tax)}",
    ]
    if a.cogs is not None:
        fees = rate(a.fees, "fees", small=True) if a.fees else 0.0
        margin = a.aov - a.cogs - a.ship_out - a.other - a.aov * fees
        profit = delivered * margin - rto_tax - a.spend
        data["net_profit"] = round(profit, 2)
        lines.append(f"  Net profit after ads + RTO ......... {money(profit)}")
        # Break-even delivery rate: delivered margin covers failed-order cost and ad spend per confirmed order.
        spend_per_confirmed = a.spend / confirmed if confirmed else 0
        denom = margin + a.ship_out + a.return_cost
        be_dr = (a.ship_out + a.return_cost + spend_per_confirmed) / denom if denom > 0 else None
        if be_dr is not None:
            data["breakeven_delivery_rate"] = round(be_dr, 4)
            verdict = ("delivery economics allow scaling (now run `verdict` per campaign and check tracking)"
                       if d > be_dr + 0.05 else
                       ("HOLD: delivery barely covers costs, fix delivery first" if d >= be_dr
                        else "STOP SCALING: losing money per order"))
            data["delivery_verdict"] = verdict
            lines.append(f"  Break-even delivery rate at this spend: {pct(min(be_dr, 1))}  (now {pct(d)}) → {verdict}")
    lines.append("  Optimise and report on delivered orders. Placed-order ROAS is a forecast, not revenue.")
    out(a, data, lines)


def cmd_learning(a):
    rule = LEARNING[a.platform]
    events_per_day = rule["events"] / rule["window_days"]
    daily = events_per_day * a.cpa
    data = {"platform": a.platform, "unit": rule["unit"], "min_daily_budget": round(daily, 2),
            "comfortable_daily_budget": round(daily * 1.3, 2), "rule": rule["note"]}
    lines = [
        f"LEARNING PHASE — {a.platform}",
        f"  Rule: {rule['note']} (verify — platforms change this)",
        f"  At CPA {money(a.cpa)}: minimum ≈ {money(daily)}/day per {rule['unit']}",
        f"  Comfortable (+30% buffer) ≈ {money(daily * 1.3)}/day",
        "  If the budget can't reach this: optimise for a higher-volume event (AddToCart / InitiateCheckout /",
        "  confirmed lead), consolidate ad sets, or widen the audience — don't fragment.",
    ]
    out(a, data, lines)


def cmd_verdict(a):
    t = a.target_cpa
    n = a.conversions
    cpa = a.spend / n if n else None
    reasons = []
    if n == 0 and a.spend >= 3 * t:
        call = "PAUSE"
        reasons.append(f"Spent {a.spend / t:.1f}x target CPA with zero conversions (rule: 0 conv after 3x target CPA -> pause).")
    elif cpa is not None and n >= 20 and cpa > 2 * t:
        call = "PAUSE"
        reasons.append(f"CPA {money(cpa)} is {cpa / t:.2f}x target on {n:.0f} conversions (rule: >2x target with 20+ conv -> pause).")
    elif cpa is not None and a.spend >= 3 * t and cpa > 2 * t:
        call = "PAUSE"
        reasons.append(f"Spent {a.spend / t:.1f}x target CPA and CPA is {cpa / t:.2f}x target "
                       "(rule: 3x target spent without getting near target -> pause, unless still inside the conversion-lag window).")
    elif cpa is not None and a.spend >= 3 * t and cpa > 1.5 * t:
        call = "REDUCE"
        reasons.append(f"Spent {a.spend / t:.1f}x target CPA at {cpa / t:.2f}x target. Cut ~20% and fix the weakest layer; "
                       "pause if it doesn't recover within 3-5 days.")
    elif a.spend < 3 * t and n < 10:
        call = "NOT ENOUGH DATA"
        reasons.append(f"Only {a.spend / t:.1f}x target CPA spent and {n:.0f} conversions (need 3x spend or 10 conv). "
                       "Don't edit; edits reset learning.")
    elif a.days < 7 or n < 30:
        call = "HOLD"
        reasons.append(f"{a.days} days / {n:.0f} conversions: below the 7-day / 30-conversion bar for scale or cut decisions. "
                       f"Current CPA {money(cpa) if cpa else 'n/a'} vs target {money(t)}.")
    elif cpa <= 0.85 * t:
        call = "SCALE"
        reasons.append(f"CPA {money(cpa)} is {pct(1 - cpa / t)} better than target on {n:.0f} conversions.")
        reasons.append("+15-20% budget per step, one step per 72h (vertical), or duplicate into a new campaign/geo "
                       "(horizontal). Roll back if CPA runs >20% over target for 3 days.")
    elif cpa <= 1.15 * t:
        call = "HOLD"
        reasons.append(f"CPA {money(cpa)} is within +/-15% of target. Keep spending; add new creative angles.")
    elif cpa <= 1.25 * t:
        call = "HOLD + FIX"
        reasons.append(f"CPA {money(cpa)} is {pct(cpa / t - 1)} over target: keep the budget, fix the weakest layer "
                       "(creative/landing page/offer), re-check in 3-5 days.")
    elif cpa <= 2 * t:
        call = "REDUCE"
        reasons.append(f"CPA {money(cpa)} is {pct(cpa / t - 1)} over target on {n:.0f} conversions. Cut budget ~20% and "
                       "diagnose the broken layer (signal -> auction -> hook/CTR -> landing page -> post-conversion).")
    else:
        call = "PAUSE"
        reasons.append(f"CPA {money(cpa)} is {cpa / t:.2f}x target. Pause (don't delete) and rebuild the angle/offer.")
    if a.frequency and a.ctr_drop is not None:
        drop = rate(a.ctr_drop, "ctr-drop") if a.ctr_drop else 0
        if a.frequency >= 3 and drop >= 0.2:
            reasons.append(f"Fatigue: frequency {a.frequency:.1f} with CTR down {pct(drop)} → REFRESH creative "
                           "(new angle, not a new font).")
            if call in ("HOLD", "SCALE", "NOT ENOUGH DATA"):
                call += " + REFRESH"
    data = {"verdict": call, "cpa": round(cpa, 2) if cpa else None, "target_cpa": t, "reasons": reasons}
    lines = [f"VERDICT: {call}"] + [f"  - {r}" for r in reasons]
    out(a, data, lines)


def cmd_vat(a):
    code = a.country.upper()
    if code not in VAT:
        sys.exit(f"Unknown country {code}. Known: {', '.join(sorted(VAT))}")
    v = VAT[code]
    total = a.budget * (1 + v)
    data = {"country": COUNTRY_NAMES[code], "vat_rate": v, "budget_ex_vat": a.budget, "total_inc_vat": round(total, 2)}
    lines = [f"VAT — {COUNTRY_NAMES[code]} ({pct(v)}, verify current rate)",
             f"  Media budget {money(a.budget)} → invoice ≈ {money(total)} incl. VAT",
             "  State in every plan whether CPA/ROAS targets are ex- or incl. VAT."]
    out(a, data, lines)


def cmd_split(a):
    goal = a.goal.lower()
    market = a.market.upper()
    mix = MIX.get((goal, market)) or MIX.get((goal, "ANY")) or MIX.get((goal, "GCC")) or MIX[("sales", "GCC")]
    top, mid, bottom = FUNNEL.get(goal, FUNNEL["sales"])
    test = a.budget * 0.10
    core = a.budget - test
    data = {"goal": goal, "market": market, "test_budget": round(test, 2),
            "platforms": {p: round(core * s, 2) for p, s in mix.items()},
            "funnel": {"prospecting": round(core * top, 2), "consideration": round(core * mid, 2),
                       "conversion_retargeting": round(core * bottom, 2)}}
    lines = [f"BUDGET SPLIT — {goal} / {market} — {money(a.budget)} per month (starting hypothesis, not a benchmark)",
             f"  10% test budget (new platform / angle) ... {money(test)}"]
    for p, s in mix.items():
        lines.append(f"  {p:<24} {pct(s):>6}  {money(core * s)}")
    lines += [f"  Funnel: prospecting {pct(top)} · consideration {pct(mid)} · conversion/retargeting {pct(bottom)}",
              "  Re-weight after 2-4 weeks toward the platform with the best REAL CPA, never by CPM."]
    out(a, data, lines)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--json", action="store_true", help="machine-readable output")
    sub = p.add_subparsers(dest="cmd", required=True)

    b = sub.add_parser("breakeven", parents=[common], help="break-even ROAS/CPA from unit economics")
    b.add_argument("--price", type=float, required=True, help="selling price / AOV")
    b.add_argument("--cogs", type=float, required=True, help="product cost")
    b.add_argument("--shipping", type=float, default=0, help="outbound shipping per order")
    b.add_argument("--fees", type=float, default=0, help="payment/COD/platform fee as %% of price (3 or 0.03)")
    b.add_argument("--other", type=float, default=0, help="other per-order cost (packaging, call centre)")
    b.add_argument("--confirm", type=float, help="COD confirmation rate of placed orders (default 100%%)")
    b.add_argument("--deliver", type=float, help="COD delivery rate of CONFIRMED orders (default 100%%)")
    b.add_argument("--return-cost", type=float, default=0, help="extra cost per failed delivery (return leg)")
    b.add_argument("--target-margin", type=float, help="desired net margin %% after ads")

    c = sub.add_parser("cod", parents=[common], help="real ROAS/CPA after confirmation and delivery")
    c.add_argument("--spend", type=float, required=True)
    c.add_argument("--orders", type=float, required=True, help="placed orders")
    c.add_argument("--aov", type=float, required=True)
    c.add_argument("--confirm", type=float, required=True, help="confirmation rate")
    c.add_argument("--deliver", type=float, required=True, help="delivery rate of confirmed orders")
    c.add_argument("--cogs", type=float, help="product cost per order (enables profit + break-even DR)")
    c.add_argument("--ship-out", type=float, default=0, help="outbound shipping per order")
    c.add_argument("--return-cost", type=float, default=0, help="return leg + repack per failed delivery")
    c.add_argument("--fees", type=float, default=0, help="payment/COD fee as %% of AOV")
    c.add_argument("--other", type=float, default=0, help="other per-order cost (packaging, call centre)")

    l = sub.add_parser("learning", parents=[common], help="min daily budget to exit learning")
    l.add_argument("--platform", choices=sorted(LEARNING), required=True)
    l.add_argument("--cpa", type=float, required=True, help="expected CPA of the optimisation event")

    v = sub.add_parser("verdict", parents=[common], help="scale / hold / kill call")
    v.add_argument("--spend", type=float, required=True)
    v.add_argument("--conversions", type=float, required=True)
    v.add_argument("--target-cpa", type=float, required=True)
    v.add_argument("--days", type=int, default=7, help="days since launch or last significant edit")
    v.add_argument("--platform", choices=sorted(LEARNING), default="meta")
    v.add_argument("--frequency", type=float, help="7-day frequency")
    v.add_argument("--ctr-drop", type=float, help="CTR drop vs first week (20 or 0.2)")

    t = sub.add_parser("vat", parents=[common], help="spend including VAT")
    t.add_argument("--budget", type=float, required=True)
    t.add_argument("--country", required=True, help="SA, AE, EG, BH, OM, QA, KW, JO, MA")

    s = sub.add_parser("split", parents=[common], help="monthly budget split by platform and funnel")
    s.add_argument("--budget", type=float, required=True)
    s.add_argument("--goal", default="sales", choices=sorted(FUNNEL))
    s.add_argument("--market", default="GCC", help="KSA, UAE, EGYPT, GCC, ANY")

    a = p.parse_args()
    {"breakeven": cmd_breakeven, "cod": cmd_cod, "learning": cmd_learning,
     "verdict": cmd_verdict, "vat": cmd_vat, "split": cmd_split}[a.cmd](a)


if __name__ == "__main__":
    main()
