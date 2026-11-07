"""Calorie assurance as a test: the build is blocked if the plan leaves its targets."""
import pytest
from data.plan import W, DAYS
from data.foods import F
from fitclub.calc import day_tot, summary, legume_meals, red_meat_raw, TARGETS, AVG_TOL, NO_PROTEIN_FLOOR_DAYS

WHO = [(0, "Alireza"), (1, "Ana")]

@pytest.mark.parametrize("who,name", WHO)
@pytest.mark.parametrize("day", DAYS)
def test_daily_kcal_band(who, name, day):
    t, k = TARGETS[who], day_tot(day, who)[0]
    assert t["lo"] <= k <= t["hi"], f"{name} {day}: {k:.0f} kcal outside {t['lo']}–{t['hi']}"

@pytest.mark.parametrize("who,name", WHO)
@pytest.mark.parametrize("day", [d for d in DAYS if d not in NO_PROTEIN_FLOOR_DAYS])
def test_daily_protein_floor(who, name, day):
    p = day_tot(day, who)[1]
    assert p >= TARGETS[who]["p"], f"{name} {day}: {p:.0f} g protein"

@pytest.mark.parametrize("who,name", WHO)
def test_weekly_averages(who, name):
    s, t = summary(who), TARGETS[who]
    assert abs(s["kcal"] - t["avg"]) <= AVG_TOL, f"{name} avg {s['kcal']:.0f}"
    assert s["p"] >= t["p"], f"{name} avg protein {s['p']:.0f}"
    assert s["f"] >= t["f"], f"{name} avg fibre {s['f']:.0f}"

def test_ana_never_below_floor():
    assert all(day_tot(d, 1)[0] >= 1300 for d in DAYS)

def test_legumes_once_a_day_and_four_a_week():
    per_day = {d: legume_meals(d) for d in DAYS}
    assert all(len(v) <= 1 for v in per_day.values()), per_day
    assert sum(len(v) for v in per_day.values()) >= 4

@pytest.mark.parametrize("who,name", WHO)
def test_red_meat_cap(who, name):
    assert red_meat_raw(who) <= TARGETS[who]["red"]

def test_every_food_has_values_and_source():
    used = {r[0] for d in DAYS for m in W[d] for r in m["rows"] if r[0] != "BUDGET"}
    missing = used - set(F)
    assert not missing, missing
    assert all(len(F[f]) == 4 and F[f][3] for f in used)

def test_eggs_are_whole():
    for d in DAYS:
        for m in W[d]:
            for r in m["rows"]:
                if r[0] == "Ei":
                    assert r[1] % 55 == 0 and r[2] % 55 == 0, (d, m["name"])
