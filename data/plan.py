# Diet plan v4 as data. rows: (food, Alireza g, Ana g). Budget meals: ("BUDGET", (kA,pA,fA),(kN,pN,fN))
W = {}
def M(slot, name, rows, note=""): return dict(slot=slot, name=name, rows=rows, note=note)

skyr_bowl = lambda: M("Breakfast 07:30","Skyr bowl",[
 ("Skyr 0%",330,210),("Havermout",45,25),("Bosvruchten (diepvries)",125,100),("Walnoten",10,6),("Chiazaad",10,5)])
oats = lambda: M("Breakfast 07:30","Overnight oats",[
 ("Havermout",55,35),("Whey (ON Gold Standard)",30,18),("Halfvolle melk",150,100),("Bosvruchten (diepvries)",125,100),("Chiazaad",10,5)],
 "Mix the night before in a jar; packable for office days.")
dates = lambda choc=True: M("Tea 16:30","Dates & walnuts with tea",[("Dadels",30,20),("Walnoten",12,8)]+([("Pure chocolade 70%+",10,6)] if choc else []))
fruitpb = lambda choc=True: M("Tea 16:30","Apple & peanut butter with tea",[("Appel",180,150 if choc else 120),("Pindakaas 100%",20,12 if choc else 10)]+([("Pure chocolade 70%+",10,6)] if choc else []))
saffron = lambda: M("TV 21:30","Frozen saffron skyr (bastani-style)",[("Skyr 0%",250,150),("Honing",10,6),("Pistache",5,3)],
 "Saffron + 1 tsp rose water stirred in; freezer ~2 h before, stir once.")
popcorn = lambda: M("TV 21:30","Popcorn",[("Popcornmais",40,30),("Olijfolie",4,3)],"Pan with lid, or paper bag in the microwave.")
fruitbowl = lambda: M("TV 21:30","Fruit bowl & tea",[("Sinaasappel",150,120),("Granaatappelpitjes",100,80)])

W["Saturday"] = [
 M("Breakfast 08:30","Persian breakfast spread",[("Iraans/Turks brood",50,30),("Feta",30,25),("Ei",110,55),("Hüttenkäse",110,90),("Walnoten",5,5),
   ("Komkommer",100,100),("Tomaat",100,100),("Verse kruiden",20,20)]),
 M("Lunch 12:30","Red lentil soup (mercimek) + mint skyr",[("Rode linzen (dry)",70,45),("Ui",50,40),("Wortel",80,60),("Olijfolie",6,4),
   ("Tomatenpuree",15,10),("Skyr 0%",200,130),("Iraans/Turks brood",30,15)],"Lemon + chili flakes on top."),
 fruitpb(choc=False),
 M("Dinner","SOCIAL DINNER — out, friends or takeaway",[("BUDGET",(900,40,6),(550,28,4))],
   "One plate + one dessert or drink. Every other week drinks count inside this budget (Alireza 2, Ana 1)."),
]
W["Sunday"] = [
 M("Breakfast 09:00","Ana's omelet with Iranian bread",[("Ei",165,110),("Roomboter",5,4),("Iraans/Turks brood",70,45),("Feta",20,15),
   ("Tomaat",100,100),("Komkommer",100,50),("Verse kruiden",20,20)],"Alireza 3 eggs, Ana 2."),
 M("Lunch 13:00","Chickpea bowl with chicken & tahini-yoghurt",[("Kipfilet",150,90),("Kikkererwten (tin, drained)",160,105),("Spinazie",165,135),
   ("Tomaat",150,120),("Komkommer",100,100),("Skyr 0%",60,40),("Tahin",10,5),("Olijfolie",5,3)]),
 M("Tea 16:30","Weekend dessert — Ana's baking or bastani",[("BUDGET",(250,5,1),(180,4,1))],"One portion with tea."),
 M("Dinner 19:30","Chelo goosht",[("Lamsbout mager",150,90),("Zilvervliesrijst (dry)",60,30),("Ui",60,40),("Tomaat",150,120),
   ("Tomatenpuree",15,10),("Olijfolie",6,4),("Komkommer",100,100),("Sla",100,100)]),
 saffron(),
]
W["Monday"] = [
 skyr_bowl(),
 M("Lunch 12:30","Ash (cooked Sunday)",[("Gort (dry)",40,25),("Rode linzen (dry)",40,25),("Witte bonen (tin, drained)",160,105),
   ("Verse kruiden",80,60),("Spinazie (diepvries)",70,60),("Ui",60,40),("Olijfolie",7,4),("Skyr 0%",170,110)],"Skyr instead of kashk; mint + fried onion on top from the day's oil."),
 dates(),
 M("Dinner 19:30","Zereshk polo ba morgh — cook double for Tuesday lunch",[("Kipfilet",200,115),("Zilvervliesrijst (dry)",60,35),("Berberis (zereshk)",8,5),
   ("Ui",60,40),("Tomatenpuree",15,10),("Olijfolie",7,4),("Sla",150,150),("Skyr 0%",100,60),("Komkommer",80,80)],"Mast-o-khiar: skyr + cucumber + dried mint."),
 popcorn(),
]
W["Tuesday"] = [
 oats(),
 M("Lunch 12:30","Zereshk polo ba morgh (Monday's second portion)",[("Kipfilet",200,115),("Zilvervliesrijst (dry)",60,30),("Berberis (zereshk)",8,5),
   ("Ui",60,40),("Tomatenpuree",15,10),("Olijfolie",7,4),("Sla",150,150),("Skyr 0%",100,60),("Komkommer",80,80)]),
 fruitpb(),
 M("Dinner 19:30","Sabzi polo ba mahi",[("Zalmfilet ASC",150,100),("Zilvervliesrijst (dry)",55,35),("Verse kruiden",60,50),
   ("Olijfolie",3,2),("Sla",150,150),("Tomaat",100,100)],"Salmon: turmeric, lemon, garlic, 8 min air fryer 200 °C."),
 saffron(),
]
W["Wednesday"] = [
 skyr_bowl(),
 M("Lunch 12:30","Creamy chicken–mushroom pasta (new sauce)",[("Volkoren pasta (dry)",65,35),("Kipfilet",130,80),("Champignons",150,100),
   ("Ui",40,40),("Halfvolle melk",150,100),("Maizena",7,5),("Parmezaan",15,8),("Skyr 0%",80,40),("Olijfolie",3,2),
   ("Spinazie (diepvries)",50,50),("Sla",150,150)]),
 dates(),
 M("Dinner 19:30","Ghormeh sabzi",[("Runderpoulet mager",140,85),("Kidneybonen (tin, drained)",150,100),("Sabzi (ghormeh-kruiden)",150,120),
   ("Ui",50,40),("Olijfolie",6,5),("Zilvervliesrijst (dry)",45,20),("Sla",150,150)],"Cooked on Sunday with the ash; fridge until Wednesday (or freeze, thaw Tuesday night)."),
 fruitbowl(),
]
W["Thursday"] = [
 oats(),
 M("Lunch 12:30","Adasi + yoghurt",[("Linzen (tin, drained)",320,210),("Ui",50,40),("Olijfolie",6,4),("Skyr 0%",200,120),("Komkommer",150,150)],
   "Cumin, turmeric, lemon; 15 minutes from the tin."),
 fruitpb(),
 M("Dinner 19:30","Homemade pizza — yoghurt dough",[("Zelfrijzend bakmeel",90,55),("Skyr 0%",100,60),("Tomatenpuree",25,15),("Mozzarella light",75,50),
   ("Kipfilet",100,60),("Paprika",100,70),("Ui",30,20),("Olijfolie",3,2),("Sla",150,150)],
   "Dough: flour + skyr 1:1, knead 2 min, roll thin. Sauce: tomato paste + 3 tbsp water + oregano + garlic. 220 °C ~12 min; rocket on top after baking."),
 saffron(),
]
W["Friday"] = [
 skyr_bowl(),
 M("Lunch 12:30","Jujeh kabab + quinoa + mast-o-khiar",[("Kipdijfilet",200,120),("Quinoa (dry)",50,30),("Ui",50,40),("Skyr 0%",130,80),("Olijfolie",4,3),
   ("Komkommer",80,80),("Sla",150,150),("Tomaat",100,100)],"Thigh in the saffron-yoghurt marinade (made Thursday night), air fryer 15 min 200 °C."),
 dates(),
 M("Dinner 19:30","Steak night",[("Kogelbiefstuk",200,110),("Aardappel",220,120),("Olijfolie",6,4),("Broccoli",250,200),
   ("Sla",150,150),("Tomaat",100,100)],"Potatoes in the air fryer; steak 2 min a side, rest 5."),
 popcorn(),
]
DAYS = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
