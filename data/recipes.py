# Recipe cards, keyed by the start of the meal name in plan.py. For two people; grams are in the plan.
RECIPES = {
 "Persian breakfast spread": "Boil the eggs for 8 min. Warm the bread from frozen for 3 min in the air fryer. Put out feta, hüttenkäse, walnuts, herbs, cucumber and tomato. Tea.",
 "Red lentil soup (mercimek)": "Fry the onion and carrot in the oil for 5 min. Add the tomato paste for 1 min, then cumin and paprika. Add the lentils and 1 L of water or stock and simmer 20 min. Blend. Finish with lemon and chili flakes. Serve with skyr mixed with dried mint, and the bread.",
 "Ana's omelet": "Melt the butter, add the eggs, cover and cook on low heat. Top with feta and herbs. Serve with warm bread and tomato and cucumber on the side.",
 "Chickpea bowl": "Season the chicken strips with cumin, paprika and garlic and cook in the air fryer, 12 min at 200 °C. Warm the chickpeas and spinach with garlic in a pan for 3 min. Add tomato and cucumber. Dressing: skyr, tahini, lemon, garlic and a splash of water.",
 "Chelo goosht": "Brown the lamb and onion in the oil with turmeric and pepper. Add the tomato paste for 1 min, then water to cover. Cover and simmer on low for 1.5–2 h; add halved tomatoes for the last 15 min. Serve on rice with a little saffron water.",
 "Ash": "Cook on Sunday. Cook the onion and turmeric in half the oil. Add the barley, red lentils and 1.5 L water; simmer 45 min. Add the beans, chopped herbs and spinach; simmer 20 min more. Top with skyr (in place of kashk) and dried mint warmed in the rest of the oil.",
 "Ghormeh sabzi": "Cook on Sunday. Fry the herbs (or the frozen ghormeh mix) in half the oil for 15 min until dark green; this is where the flavour comes from. In the rest of the oil, brown the onion and beef with turmeric. Add water, 2 pierced limoo amani (or ½ lime) and 1 tbsp dried fenugreek. Cover and simmer 1.5 h. Add the beans and herbs for the last 30 min.",
 "Zereshk polo ba morgh": "Monday: cook double. Put the chicken, onion, turmeric, tomato paste, saffron water and 100 ml water in a pan; cover and cook 25 min. Rinse the barberries and warm them for 1 min in a dry pan with a few drops of saffron water; spoon them over the rice. Mast-o-khiar: skyr, grated cucumber and dried mint.",
 "Sabzi polo ba mahi": "Boil the rice for 10 min and drain. Steam it for 20 min with the chopped dill, parsley, coriander and chives layered in. Season the salmon with turmeric, lemon, garlic and salt and cook in the air fryer, 8 min at 200 °C. Serve with lemon.",
 "Creamy chicken–mushroom pasta": "Brown the mushrooms in a dry pan, then add the onion, garlic, chicken and the oil. In a cold pan, whisk the milk with the maizena; bring to a simmer and stir 2 min until it coats a spoon. Off the heat, stir in the parmesan, then the skyr. Season with pepper and nutmeg. Toss with the pasta, the spinach and a splash of pasta water.",
 "Adasi": "Cook the onion in the oil for 5 min with turmeric and cumin. Add the drained lentils and 200 ml water and simmer 10 min. Mash a third of it. Finish with lemon or golpar. Serve with skyr and cucumber.",
 "Homemade pizza": "Knead the flour and skyr together for 2 min and roll thin. Cook the chicken first (air fryer, 8 min). Sauce: tomato paste with 3 tbsp water, oregano and garlic. Top with mozzarella, chicken, pepper and onion. Bake at 220 °C for about 12 min. Put rocket on top after baking.",
 "Jujeh kabab": "Marinate Thursday night: mix the thighs with half the skyr, grated onion, saffron, lemon and pepper. Cook in the air fryer, 15 min at 200 °C, turning once. Cook the quinoa 15 min. Make mast-o-khiar with the rest of the skyr.",
 "Steak night": "Toss the potato wedges in the oil and cook in the air fryer, 20 min at 200 °C. Dry the steak, salt and pepper it, and cook in a very hot pan 2 min a side; rest 5 min. Steam the broccoli 5 min. Serve with salad.",
 "Frozen saffron skyr": "Soak a pinch of saffron in 1 tbsp hot water for 10 min. Stir it into the skyr with the honey and 1 tsp rose water. Freeze about 2 h, stirring once. Top with pistachio.",
 "Popcorn": "Put the oil and kernels in a pan, cover, and cook on medium heat, shaking the pan. Season with salt or cinnamon.",
}

def recipe_for(name):
    for k, v in RECIPES.items():
        if name.startswith(k):
            return v
    return ""
