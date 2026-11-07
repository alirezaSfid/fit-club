"""Meal, day and week totals computed from data/foods.py and data/plan.py. Nothing is typed by hand."""
from data.foods import F
from data.plan import W, DAYS

PEOPLE = ("Alireza", "Ana")
LEGUMES = {"Rode linzen (dry)", "Linzen (tin, drained)", "Witte bonen (tin, drained)",
           "Kidneybonen (tin, drained)", "Kikkererwten (tin, drained)"}
RED_MEAT = {"Lamsbout mager", "Runderpoulet mager", "Kogelbiefstuk"}

# Targets: daily kcal band, weekly-average target, protein floor (not on Saturday), fibre weekly-average floor, red meat raw cap
TARGETS = {
    0: dict(lo=2130, hi=2250, avg=2200, p=165, f=30, red=500),
    1: dict(lo=1370, hi=1480, avg=1400, p=100, f=25, red=300),
}
AVG_TOL = 15
NO_PROTEIN_FLOOR_DAYS = {"Saturday"}   # social dinner is a budget, not a recipe


def meal_tot(m, who):
    k = p = f = 0.0
    for r in m["rows"]:
        if r[0] == "BUDGET":
            b = r[1] if who == 0 else r[2]
            k += b[0]; p += b[1]; f += b[2]
            continue
        food, a, n = r
        g = a if who == 0 else n
        v = F[food]
        k += v[0] * g / 100; p += v[1] * g / 100; f += v[2] * g / 100
    return k, p, f


def day_tot(day, who):
    t = [0.0, 0.0, 0.0]
    for m in W[day]:
        mt = meal_tot(m, who)
        t = [t[i] + mt[i] for i in range(3)]
    return tuple(t)


def legume_meals(day):
    return [m["name"] for m in W[day] if any(r[0] in LEGUMES for r in m["rows"])]


def red_meat_raw(who):
    return sum((r[1] if who == 0 else r[2]) for d in DAYS for m in W[d] for r in m["rows"] if r[0] in RED_MEAT)


def summary(who):
    days = [day_tot(d, who) for d in DAYS]
    red = red_meat_raw(who)
    return dict(
        kcal=sum(x[0] for x in days) / 7, p=sum(x[1] for x in days) / 7, f=sum(x[2] for x in days) / 7,
        lo=min(x[0] for x in days), hi=max(x[0] for x in days),
        satp=day_tot("Saturday", who)[1], red=red, redc=red * 0.7,
    )


def day_pass(day, who):
    t, (k, p, _f) = TARGETS[who], day_tot(day, who)
    return t["lo"] <= k <= t["hi"] and (p >= t["p"] or day in NO_PROTEIN_FLOOR_DAYS)
