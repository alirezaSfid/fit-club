"""Shopping list: every gram the plan needs is bought, in whole packs, and nothing is lost between plan and list."""
from data.products import P, PANTRY
from fitclub.shop import needs, buy

def test_every_planned_food_is_on_a_list():
    need, weekly = needs()
    for f, g in weekly.items():
        on_trips = need["Saturday"].get(f, 0) + need["Tuesday"].get(f, 0)
        assert f in PANTRY or abs(on_trips - g) < 1e-6, f
        assert f in P or f in PANTRY, f

def test_packs_cover_need_with_less_than_one_pack_left():
    need, _ = needs()
    for t in need:
        for f, g in need[t].items():
            _text, bought = buy(f, g)
            if bought is not None:
                pack = P[f][1]
                assert bought >= g, (t, f)
                assert bought - g < pack, (t, f, bought, g)

def test_tins_are_used_whole():
    need, _ = needs()
    for t in need:
        for f, g in need[t].items():
            if P[f][0] == "Voorraad — tins":
                assert g % P[f][1] == 0, (t, f, g)
