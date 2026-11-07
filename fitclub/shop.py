"""Shopping needs per trip, rounded to whole packs, computed from the plan."""
import math
from data.plan import W, DAYS
from data.products import P, PANTRY


def trip(day, slot, name, food=None):
    """Saturday trip = Sat, Sun, Mon, Tue breakfast+lunch, and Wednesday's ghormeh (cooked Sunday). Milk all on Saturday."""
    if food == "Halfvolle melk":
        return "Saturday"
    if day in ("Saturday", "Sunday", "Monday"):
        return "Saturday"
    if day == "Tuesday" and (slot.startswith("Breakfast") or slot.startswith("Lunch")):
        return "Saturday"
    if day == "Wednesday" and name.startswith("Ghormeh"):
        return "Saturday"
    return "Tuesday"


def needs():
    need = {"Saturday": {}, "Tuesday": {}}
    weekly = {}
    for d in DAYS:
        for m in W[d]:
            for r in m["rows"]:
                if r[0] == "BUDGET":
                    continue
                f, a, n = r
                g = a + n
                weekly[f] = weekly.get(f, 0) + g
                if f in PANTRY:
                    continue
                t = trip(d, m["slot"], m["name"], f)
                need[t][f] = need[t].get(f, 0) + g
    return need, weekly


def buy(f, g):
    """Return (text, grams bought or None when bought by weight/pieces)."""
    _aisle, pack, label, _st, piece = P[f]
    if pack:
        k = math.ceil(g / pack - 1e-9)
        return f"{k} × {label}", k * pack
    if piece:
        k = math.ceil(g / piece - 0.05)
        return (f"{k} eggs" if f == "Ei" else f"≈ {k} pc / {g:,.0f} g"), None
    return f"{g:,.0f} g", None
