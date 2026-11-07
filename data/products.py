# Product data for the shopping list. Pack sizes and drained weights verified on AH product pages where marked.
# P: food -> (aisle, pack grams or None (by weight), pack label, store sticker, piece weight for counting)
P = {
 "Skyr 0%":("Zuivel & eieren",500,"500 g tub","Lidl",None),
 "Magere kwark":("Zuivel & eieren",500,"500 g tub","Lidl",None),
 "Hüttenkäse":("Zuivel & eieren",200,"200 g tub","",None),
 "Halfvolle melk":("Zuivel & eieren",1000,"1 L","",None),
 "Ei":("Zuivel & eieren",None,"","",55),
 "Feta":("Zuivel & eieren",200,"200 g (AH Griekse feta)","AH",None),
 "Parmezaan":("Zuivel & eieren",150,"150 g block","",None),
 "Mozzarella light":("Zuivel & eieren",125,"125 g drained ball","AH",None),
 "Roomboter":("Zuivel & eieren",250,"250 g","",None),
 "Kipfilet":("Vlees & vis",None,"","Lidl",None),
 "Kipdijfilet":("Vlees & vis",None,"","",None),
 "Lamsbout mager":("Vlees & vis",None,"","Jumbo",None),
 "Runderpoulet mager":("Vlees & vis",None,"","Jumbo",None),
 "Kogelbiefstuk":("Vlees & vis",None,"","AH",None),
 "Zalmfilet ASC":("Vlees & vis",None,"","AH",None),
 "Tomaat":("Groente & fruit",None,"","",100), "Komkommer":("Groente & fruit",None,"","",400),
 "Sla":("Groente & fruit",None,"","",400), "Ui":("Groente & fruit",None,"","",150),
 "Paprika":("Groente & fruit",None,"","",160), "Champignons":("Groente & fruit",250,"250 g box","",None),
 "Broccoli":("Groente & fruit",None,"","",450), "Spinazie":("Groente & fruit",300,"300 g bag","",None),
 "Verse kruiden":("Groente & fruit",None,"","",None), "Wortel":("Groente & fruit",None,"","",100),
 "Aardappel":("Groente & fruit",None,"","",None), "Appel":("Groente & fruit",None,"","",180),
 "Sinaasappel":("Groente & fruit",None,"","",150), "Granaatappelpitjes":("Groente & fruit",None,"","",250),
 "Sabzi (ghormeh-kruiden)":("Groente & fruit",None,"","",None),
 "Iraans/Turks brood":("Brood",None,"","",None),
 "Bosvruchten (diepvries)":("Diepvries",500,"500 g bag","Lidl",None),
 "Kikkererwten (tin, drained)":("Voorraad — tins",265,"400 g tin (265 g drained)","AH Terra",None),
 "Witte bonen (tin, drained)":("Voorraad — tins",265,"400 g tin (265 g drained)","AH Terra",None),
 "Kidneybonen (tin, drained)":("Voorraad — tins",250,"400 g tin (250 g drained)","AH Terra",None),
 "Linzen (tin, drained)":("Voorraad — tins",265,"400 g tin (265 g drained)","AH Terra",None),
 "Passata":("Voorraad — tins",500,"500 g","",None), "Tomatenpuree":("Voorraad — tins",70,"70 g tin","",None),
}

# Pantry: food -> (pack grams, label). Bought when it runs out.
PANTRY = {  # weekly use -> pack; bought when it runs out
 "Havermout":(1000,"1 kg"),"Zilvervliesrijst (dry)":(1000,"1 kg"),"Quinoa (dry)":(500,"500 g"),"Volkoren pasta (dry)":(500,"500 g"),
 "Zelfrijzend bakmeel":(1000,"1 kg"),"Rode linzen (dry)":(500,"500 g"),"Gort (dry)":(500,"500 g"),"Maizena":(400,"400 g"),
 "Popcornmais":(350,"350 g (AH Valle del Sole)"),"Chiazaad":(250,"250 g"),"Walnoten":(200,"200 g (Lidl)"),"Pindakaas 100%":(350,"350 g, 100% pinda"),
 "Tahin":(300,"300 g jar"),"Pistache":(150,"150 g, shelled, unsalted"),"Dadels":(500,"500 g"),"Honing":(350,"350 g"),
 "Pure chocolade 70%+":(100,"100 g bar"),"Olijfolie":(460,"500 ml"),"Whey (ON Gold Standard)":(899,"899 g (AH)"),
 "Berberis (zereshk)":(100,"100 g — Persian pantry"),
 "Spinazie (diepvries)":(450,"450 g bag"),"Tomatenpuree":(70,"70 g tin — 2 a week"),
 "Feta":(200,"200 g (AH Griekse feta)"),"Parmezaan":(150,"150 g block"),"Roomboter":(250,"250 g"),
}

# Per-trip notes shown next to an item.
NOTES = {
 "Kipfilet":{"Saturday":"Sun bowl 240 · Mon zereshk ×2 630 — portion Sunday; Monday's in the fridge","Tuesday":"Wed pasta 210 · Thu pizza 160"},
 "Lamsbout mager":{"Saturday":"Sun chelo goosht"}, "Runderpoulet mager":{"Saturday":"ghormeh sabzi, cooked Sunday for Wednesday"},
 "Kipdijfilet":{"Tuesday":"Fri jujeh — marinate Thursday night"}, "Kogelbiefstuk":{"Tuesday":"Fri steak — freeze if the date is before Friday"},
 "Zalmfilet ASC":{"Tuesday":"Tue sabzi polo — cook today"}, "Verse kruiden":{"Saturday":"parsley, coriander, dill (ash, spread, omelet)","Tuesday":"dill, parsley, coriander, chives (sabzi polo)"},
 "Sabzi (ghormeh-kruiden)":{"Saturday":"fresh parsley + coriander + leek + spinach, or 1 frozen ghormeh mix (Persian pantry)"},
 "Iraans/Turks brood":{"Saturday":"sangak/barbari from the freezer; Turks brood as stand-in"},
 "Skyr 0%":{"Saturday":"","Tuesday":"~300 g is left over each week; when a full tub is still in the fridge, buy 5"},
 "Halfvolle melk":{"Saturday":"Tue + Thu oats, Wed sauce"},
}

PERSIAN = [
 ("Berberis (zereshk)", "Mon dinner + Tue lunch, 26 g/week", "100 g bag (lasts ~4 weeks)"),
 ("Dried fenugreek (shanbalileh)", "ghormeh sabzi, 1 tbsp/week", "1 bag (months)"),
 ("Limoo amani", "ghormeh sabzi, 2/week", "1 bag (months)"),
 ("Saffron", "zereshk polo, chelo, jujeh, frozen skyr", "1 g (≈ a month)"),
 ("Frozen ghormeh-sabzi herb mix (optional)", "instead of fresh herbs", "1 bag ≈ 1.5 weeks"),
 ("Sangak or barbari", "weekend breakfasts, Sat lunch: 240 g/week", "1 large bread, portioned into the freezer (≈ 2–3 weeks)"),
]
SPICES = "turmeric, cumin, paprika, cinnamon, oregano, dried mint, black pepper, nutmeg, iodised salt"
AISLES = ["Groente & fruit","Vlees & vis","Zuivel & eieren","Brood","Diepvries","Voorraad — tins"]
