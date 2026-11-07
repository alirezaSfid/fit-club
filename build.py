"""python build.py  →  index.html (GitHub Pages) + plan/diet-plan-final.md + plan/shopping-list.md

Edit data/plan.py (meals and grams) or data/foods.py (values per 100 g), then run:
    pip install -r requirements.txt && pytest -q && python build.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from fitclub.render import build

if __name__ == "__main__":
    build()
    print("built index.html, plan/diet-plan-final.md, plan/shopping-list.md")
