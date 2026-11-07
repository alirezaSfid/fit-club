"""Render the plan into: diet-plan-final.md, shopping-list.md and index.html (single file, inline CSS/JS)."""
import json, datetime, pathlib
import markdown
from jinja2 import Environment, FileSystemLoader

from data.plan import W, DAYS
from data.foods import F
from data.recipes import recipe_for, RECIPES
from data.products import P, PANTRY, NOTES, PERSIAN, SPICES, AISLES
from fitclub.calc import meal_tot, day_tot, summary, day_pass, PEOPLE
from fitclub.shop import needs, buy

ROOT = pathlib.Path(__file__).resolve().parents[1]
VERSION = "4.0"
STK = {"Lidl": "Lidl", "AH": "AH", "Jumbo": "Jumbo", "AH Terra": "AH Terra", "": ""}


def grams(food, g):
    if food == "Ei":
        n = round(g / 55)
        return f"{n} egg" + ("" if n == 1 else "s")
    return f"{g:.0f} g"


def fmt(n):
    return f"{n:,.0f}"


def stats():
    out = {}
    for who, key in ((0, "A"), (1, "N")):
        s = summary(who)
        out[key] = dict(kcal=fmt(s["kcal"]), p=f"{s['p']:.0f}", f=f"{s['f']:.0f}", lo=fmt(s["lo"]), hi=fmt(s["hi"]),
                        satp=f"{s['satp']:.0f}", red=f"{s['red']:.0f}", redc=f"{s['redc']:.0f}")
    return out


# ---------- markdown: diet plan ----------
def week_md():
    L = []
    for d in DAYS:
        L.append(f"### {d}\n")
        for m in W[d]:
            ka, pa, _ = meal_tot(m, 0); kn, pn, _ = meal_tot(m, 1)
            L.append(f"**{m['slot']} — {m['name']}**\n")
            rows = [r for r in m["rows"] if r[0] != "BUDGET"]
            if rows:
                L.append("| Item | Alireza | Ana |\n|---|---|---|")
                L += [f"| {f} | {grams(f, a)} | {grams(f, n)} |" for f, a, n in rows]
                L.append("")
            else:
                L.append(f"Budget: Alireza ≤ {fmt(ka)} kcal · Ana ≤ {fmt(kn)} kcal (counted as {pa:.0f} g / {pn:.0f} g protein).\n")
            if m.get("note"):
                L.append(f"_{m['note']}_\n")
            L.append(f"*Alireza {fmt(ka)} kcal / {pa:.0f} g P — Ana {fmt(kn)} kcal / {pn:.0f} g P*\n")
        ta, tn = day_tot(d, 0), day_tot(d, 1)
        L.append(f"**DAY TOTAL — Alireza {fmt(ta[0])} kcal / {ta[1]:.0f} g P / {ta[2]:.0f} g fibre — {'PASS' if day_pass(d, 0) else 'CHECK'} · "
                 f"Ana {fmt(tn[0])} kcal / {tn[1]:.0f} g P / {tn[2]:.0f} g fibre — {'PASS' if day_pass(d, 1) else 'CHECK'}**\n\n---\n")
    return "\n".join(L)


def recipes_md():
    return "## Recipe cards (for two; the grams are in the tables above)\n\n" + "\n".join(
        f"- **{k}.** {v}" for k, v in RECIPES.items()) + "\n"


def diet_plan_md(env):
    st = stats()
    intro = env.from_string((ROOT / "data/plan_intro.md.j2").read_text()).render(**st)
    rules = (ROOT / "data/rules.md").read_text()
    tail = env.from_string((ROOT / "data/plan_tail.md.j2").read_text()).render(**st)
    return f"{intro}\n\n{rules}\n## The week\n\n{week_md()}{recipes_md()}\n{tail}"


# ---------- markdown: shopping list ----------
def shopping_md(env):
    need, weekly = needs()
    st = stats()
    out = [env.from_string((ROOT / "data/shop_intro.md.j2").read_text()).render(**st)]
    for t in ("Saturday", "Tuesday"):
        out.append(f"## {t}\n")
        for a in AISLES:
            items = sorted((f, g) for f, g in need[t].items() if P[f][0] == a)
            if not items:
                continue
            out.append(f"### {a}\n\n| Item | Need (plan) | Buy | Note |\n|---|---|---|---|")
            for f, g in items:
                stk = f" `[{P[f][3]}]`" if P[f][3] else ""
                out.append(f"| {f}{stk} | {fmt(g)} g | {buy(f, g)[0]} | {NOTES.get(f, {}).get(t, '')} |")
            out.append("")
    out.append("## Pantry — buy when it runs out\n\n| Item | Use per week | Pack | Lasts |\n|---|---|---|---|")
    for f, (pk, lab) in PANTRY.items():
        if f == "Berberis (zereshk)" or not weekly.get(f):
            continue
        out.append(f"| {f} | {fmt(weekly[f])} g | {lab} | {pk / weekly[f]:.1f} weeks |")
    out.append(f"| Spices | — | {SPICES} | — |\n")
    out.append("## Persian pantry — once a month\n\n| Item | Use | Buy |\n|---|---|---|")
    out += [f"| {a} | {b} | {c} |" for a, b, c in PERSIAN]
    out.append("\n## Weekly requirement from the plan (both clients summed)\n\n| Ingredient | g/week | Saturday trip | Tuesday trip |\n|---|---|---|---|")
    for f, g in sorted(weekly.items(), key=lambda x: -x[1]):
        s, tt = need["Saturday"].get(f, 0), need["Tuesday"].get(f, 0)
        out.append(f"| {f} | {fmt(g)} | {fmt(s)} | {fmt(tt)} |" if (s or tt) else f"| {f} | {fmt(g)} | pantry | pantry |")
    out.append(env.from_string((ROOT / "data/shop_tail.md.j2").read_text()).render(**st))
    return "\n".join(out) + "\n"


# ---------- app data ----------
PREP = [
    ("sun1", "Sunday", "Chelo goosht — start first, 1.5–2 h (tonight's dinner)"),
    ("sun2", "Sunday", "Ash — Monday's lunch → fridge"),
    ("sun3", "Sunday", "Ghormeh sabzi — Wednesday's dinner → fridge (or freeze, thaw Tuesday night)"),
    ("sun4", "Sunday", "Portion the chicken for Monday's zereshk polo (Monday dinner + Tuesday lunch)"),
    ("mon", "Monday night", "Overnight oats for Tuesday"),
    ("tue", "Tuesday", "Steak: freeze it if the use-by date is before Friday"),
    ("wed", "Wednesday night", "Overnight oats for Thursday"),
    ("thu", "Thursday night", "Marinate Friday's jujeh (thighs, half the skyr, onion, saffron, lemon)"),
]


def app_data():
    need, weekly = needs()
    days = []
    for d in DAYS:
        meals = []
        for i, m in enumerate(W[d]):
            ka, pa, _ = meal_tot(m, 0); kn, pn, _ = meal_tot(m, 1)
            rows = [[f, grams(f, a), grams(f, n)] for f, a, n in [r for r in m["rows"] if r[0] != "BUDGET"]]
            meals.append(dict(id=f"{d[:3]}{i}", slot=m["slot"], name=m["name"], note=m.get("note", ""),
                              recipe=recipe_for(m["name"]), rows=rows, budget=not rows,
                              ka=round(ka), pa=round(pa), kn=round(kn), pn=round(pn)))
        ta, tn = day_tot(d, 0), day_tot(d, 1)
        days.append(dict(name=d, meals=meals,
                         a=[round(ta[0]), round(ta[1]), round(ta[2]), day_pass(d, 0)],
                         n=[round(tn[0]), round(tn[1]), round(tn[2]), day_pass(d, 1)]))
    shop = {}
    for t in ("Saturday", "Tuesday"):
        secs = []
        for a in AISLES:
            items = sorted((f, g) for f, g in need[t].items() if P[f][0] == a)
            if items:
                secs.append(dict(aisle=a, items=[dict(id=f"{t[:3]}:{f}", name=f, st=STK[P[f][3]], need=f"{fmt(g)} g",
                                                      buy=buy(f, g)[0], note=NOTES.get(f, {}).get(t, "")) for f, g in items]))
        shop[t] = secs
    pantry = [dict(id=f"pan:{f}", name=f, week=f"{fmt(weekly[f])} g/wk", pack=lab, lasts=f"{pk / weekly[f]:.1f} wk")
              for f, (pk, lab) in PANTRY.items() if f != "Berberis (zereshk)" and weekly.get(f)]
    persian = [dict(id=f"per:{a}", name=a, use=b, buy=c) for a, b, c in PERSIAN]
    md = lambda p: markdown.markdown((ROOT / p).read_text(), extensions=["tables"])
    return dict(version=VERSION, built=datetime.date.today().isoformat(), days=days, shop=shop, pantry=pantry,
                persian=persian, spices=SPICES, prep=[dict(id=i, when=w, text=t) for i, w, t in PREP],
                rules=md("data/rules.md"), train=md("data/training.md"),
                firstWeek=markdown.markdown((ROOT / "data/first_week.md").read_text()), firstWeekUntil="2026-11-14",
                stats=stats())


def build():
    env = Environment(loader=FileSystemLoader(str(ROOT / "templates")), autoescape=False, keep_trailing_newline=True)
    (ROOT / "plan").mkdir(exist_ok=True)
    (ROOT / "plan/diet-plan-final.md").write_text(diet_plan_md(env))
    (ROOT / "plan/shopping-list.md").write_text(shopping_md(env))
    css = (ROOT / "templates/base.css").read_text() + (ROOT / "templates/app.css").read_text()
    html = env.get_template("index.html.j2").render(css=css, data=json.dumps(app_data(), ensure_ascii=False),
                                                     js=(ROOT / "templates/app.js").read_text(), version=VERSION)
    (ROOT / "index.html").write_text(html)
    return html
