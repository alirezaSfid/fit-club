# fit-club — Alireza & Ana week plan (v4)

The phone app for the weight-loss plan, served by GitHub Pages from `index.html`.
`index.html` is **generated**: do not edit it by hand.

## How it works

```
data/foods.py     kcal, protein, fibre per 100 g (source: L = label, N = NEVO, E = estimate)
data/plan.py      the week: days → meals → (food, Alireza g, Ana g)
data/recipes.py   recipe cards
data/products.py  packs, aisles, store stickers, pantry, Persian pantry
data/*.md         rules, training, plan intro/tail, shopping intro/tail
fitclub/          calc.py (totals, targets) · shop.py (trips, packs) · render.py (markdown + html)
tests/            calorie assurance and shopping checks — the build must pass them
build.py          → index.html, plan/diet-plan-final.md, plan/shopping-list.md
```

## Change the plan

```
pip install -r requirements.txt
# edit data/plan.py or data/foods.py
pytest -q          # every day inside its kcal band, protein floors, fibre, legumes, red meat, whole packs
python build.py    # regenerate the page and the two markdown files
```

The tests are the calorie assurance. If a change pushes a day outside 2,130–2,250 kcal (Alireza) or 1,370–1,480 kcal (Ana), the build fails.

## In the app

- **Plan:** the five moments of each day, with portions per person, the recipe, and a one-tap check per meal (as planned / swapped / extra). The header shows this week's "as planned" score.
- **Prep:** the Sunday cook-up and the weekly prep checklist.
- **Shop:** Saturday and Tuesday lists in aisle order, the pantry, and the monthly Persian pantry.
- **Train**, **Rules:** generated from `data/training.md` and `data/rules.md`.

Ticks are stored on each phone (localStorage) and reset every Saturday. Shared ticks between both phones (Supabase) are the next step.
