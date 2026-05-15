"""
Dataset generator for AI Food Genius.
Generates a rich, realistic dataset with:
  - 250 unique named recipes covering all cuisine x diet x taste combinations
  - 200 user profiles covering every filter option in the app
  - 3000 feedback interactions for collaborative filtering
  - Proper column names so app filters work correctly
"""

import pandas as pd
import numpy as np
import random

random.seed(42)
np.random.seed(42)

# ---------------------------------------------------------------------------
# RECIPE CATALOG
# Each entry: (name, cuisine, recipe_diet, taste, cook_min, cook_max,
#              cal_lo, cal_hi, prot_lo, prot_hi, fat_lo, fat_hi,
#              carb_lo, carb_hi, fiber_lo, fiber_hi)
#
# recipe_diet values MUST match app dropdown:
#   Vegetarian | Non-Vegetarian | Vegan | Keto | Paleo
# ---------------------------------------------------------------------------

CATALOG = [
    # ── INDIAN · VEGETARIAN ──────────────────────────────────────────────────
    ("Dal Makhani",          "Indian","Vegetarian","Savory", 30,50, 250,360, 12,18,  8,14, 30,45, 5,9),
    ("Palak Paneer",         "Indian","Vegetarian","Mild",   25,40, 220,320, 14,20, 12,18, 15,25, 4,8),
    ("Chana Masala",         "Indian","Vegetarian","Spicy",  20,35, 200,300, 10,16,  5,10, 28,40, 7,12),
    ("Aloo Gobi",            "Indian","Vegetarian","Mild",   20,35, 160,250,  5,10,  5,9,  25,38, 5,9),
    ("Rajma Chawal",         "Indian","Vegetarian","Savory", 35,55, 300,420, 14,20,  4,9,  50,65, 8,14),
    ("Paneer Butter Masala", "Indian","Vegetarian","Mild",   25,40, 280,400, 16,22, 14,22, 18,28, 3,6),
    ("Kadhi Pakora",         "Indian","Vegetarian","Tangy",  30,45, 220,320,  8,14, 10,16, 25,35, 3,6),
    ("Matar Paneer",         "Indian","Vegetarian","Mild",   25,40, 240,340, 14,20, 12,18, 18,28, 4,8),
    ("Veg Biryani",          "Indian","Vegetarian","Spicy",  40,60, 320,440, 10,16,  8,14, 55,70, 4,8),
    ("Baingan Bharta",       "Indian","Vegetarian","Savory", 30,45, 150,230,  4,8,   6,12, 20,30, 5,9),
    ("Pav Bhaji",            "Indian","Vegetarian","Spicy",  30,45, 300,420, 10,16, 12,18, 45,60, 5,9),
    ("Dum Aloo",             "Indian","Vegetarian","Spicy",  35,50, 200,300,  5,10,  8,14, 28,40, 4,8),
    ("Khichdi",              "Indian","Vegetarian","Mild",   20,35, 220,320, 10,16,  4,8,  38,52, 5,9),
    ("Poha",                 "Indian","Vegetarian","Mild",   15,25, 180,250,  5,9,   4,8,  35,48, 3,6),
    ("Methi Thepla",         "Indian","Vegetarian","Savory", 20,35, 160,240,  6,10,  5,10, 28,40, 4,8),

    # ── INDIAN · NON-VEGETARIAN ──────────────────────────────────────────────
    ("Butter Chicken",              "Indian","Non-Vegetarian","Mild",   25,40, 320,450, 28,38, 14,22, 12,20, 2,5),
    ("Chicken Biryani",             "Indian","Non-Vegetarian","Spicy",  50,75, 420,560, 30,42, 12,20, 52,68, 3,6),
    ("Mutton Rogan Josh",           "Indian","Non-Vegetarian","Spicy",  50,80, 380,520, 28,40, 18,28, 10,18, 2,5),
    ("Fish Curry",                  "Indian","Non-Vegetarian","Spicy",  25,40, 260,380, 26,36, 10,18, 10,18, 2,5),
    ("Prawn Masala",                "Indian","Non-Vegetarian","Spicy",  25,40, 240,360, 24,34, 10,16, 10,18, 2,4),
    ("Chicken Tikka Masala",        "Indian","Non-Vegetarian","Spicy",  30,45, 300,430, 28,38, 12,20, 14,22, 2,5),
    ("Lamb Korma",                  "Indian","Non-Vegetarian","Mild",   40,60, 380,520, 28,40, 22,32, 12,20, 2,5),
    ("Chicken Saag",                "Indian","Non-Vegetarian","Savory", 30,45, 280,400, 28,38, 14,22, 10,18, 3,7),
    ("Egg Curry",                   "Indian","Non-Vegetarian","Spicy",  20,35, 240,340, 14,20, 14,22, 12,20, 2,5),
    ("Keema Pav",                   "Indian","Non-Vegetarian","Spicy",  25,40, 380,500, 26,36, 18,26, 32,45, 3,6),
    ("Hyderabadi Chicken Biryani",  "Indian","Non-Vegetarian","Spicy",  55,80, 440,580, 32,44, 14,22, 54,70, 3,6),
    ("Fish Fry",                    "Indian","Non-Vegetarian","Savory", 20,30, 240,340, 26,36, 12,20, 10,18, 1,4),

    # ── INDIAN · VEGAN ───────────────────────────────────────────────────────
    ("Vegetable Curry",     "Indian","Vegan","Spicy",  20,35, 160,250,  6,12,  5,10, 22,34, 5,9),
    ("Tofu Tikka",          "Indian","Vegan","Spicy",  20,35, 180,270, 14,20,  8,14, 10,18, 2,5),
    ("Lentil Dal",          "Indian","Vegan","Savory", 25,40, 200,300, 12,18,  3,7,  28,40, 7,12),
    ("Aloo Palak",          "Indian","Vegan","Savory", 20,35, 150,230,  5,10,  5,10, 22,32, 5,9),
    ("Chickpea Curry",      "Indian","Vegan","Spicy",  20,35, 200,300, 10,16,  4,9,  28,40, 7,12),
    ("Mixed Veg Sabzi",     "Indian","Vegan","Mild",   15,30, 120,200,  4,8,   4,8,  18,28, 4,8),
    ("Masoor Dal",          "Indian","Vegan","Savory", 20,35, 180,270, 11,17,  2,6,  26,38, 6,11),
    ("Mushroom Matar",      "Indian","Vegan","Savory", 20,30, 160,240,  6,12,  5,10, 18,28, 4,8),
    ("Veg Korma",           "Indian","Vegan","Mild",   25,40, 200,300,  7,13,  8,14, 22,32, 4,8),

    # ── INDIAN · KETO ────────────────────────────────────────────────────────
    ("Chicken Keto Curry",     "Indian","Keto","Spicy",  25,40, 320,440, 32,44, 20,30,  5,10, 1,3),
    ("Keto Egg Bhurji",        "Indian","Keto","Savory", 10,20, 260,360, 16,24, 20,30,  3,7,  1,3),
    ("Paneer Keto Bowl",       "Indian","Keto","Mild",   15,25, 280,380, 18,26, 22,32,  4,8,  1,3),
    ("Keto Butter Chicken",    "Indian","Keto","Mild",   25,40, 340,460, 32,44, 22,32,  5,10, 1,3),
    ("Tandoori Prawns Keto",   "Indian","Keto","Spicy",  20,35, 220,320, 26,36, 10,18,  3,7,  1,3),

    # ── INDIAN · PALEO ───────────────────────────────────────────────────────
    ("Tandoori Chicken",       "Indian","Paleo","Spicy",  30,50, 280,400, 32,44, 10,18,  4,8,  1,3),
    ("Chicken Seekh Kebab",    "Indian","Paleo","Spicy",  20,35, 260,360, 28,40, 12,20,  3,7,  1,3),
    ("Fish Tikka",             "Indian","Paleo","Spicy",  20,30, 220,320, 28,38, 10,16,  2,6,  1,3),
    ("Lamb Kebab",             "Indian","Paleo","Savory", 25,40, 300,420, 28,40, 16,24,  3,7,  1,3),
    ("Grilled Chicken Tikka",  "Indian","Paleo","Spicy",  20,35, 240,340, 30,42,  8,15,  3,7,  1,3),

    # ── ITALIAN · VEGETARIAN ─────────────────────────────────────────────────
    ("Margherita Pizza",        "Italian","Vegetarian","Savory", 20,35, 320,460, 14,20, 10,16, 48,62, 3,6),
    ("Pasta Primavera",         "Italian","Vegetarian","Mild",   20,35, 280,400, 12,18, 10,16, 45,58, 4,8),
    ("Risotto ai Funghi",       "Italian","Vegetarian","Savory", 30,45, 320,440, 10,16, 10,18, 52,65, 2,5),
    ("Caprese Salad",           "Italian","Vegetarian","Mild",   10,20, 160,250, 10,16, 12,18,  8,14, 2,5),
    ("Vegetable Lasagne",       "Italian","Vegetarian","Savory", 50,75, 340,480, 16,24, 12,18, 45,58, 4,8),
    ("Penne Arrabbiata",        "Italian","Vegetarian","Spicy",  20,30, 280,400, 10,16,  6,12, 50,62, 3,6),
    ("Gnocchi al Pesto",        "Italian","Vegetarian","Savory", 25,40, 320,440, 10,16, 14,22, 48,60, 3,6),
    ("Eggplant Parmigiana",     "Italian","Vegetarian","Savory", 40,60, 280,400, 12,18, 14,22, 28,40, 5,9),
    ("Cacio e Pepe",            "Italian","Vegetarian","Savory", 20,30, 340,460, 14,20, 14,22, 50,62, 2,5),
    ("Bruschetta al Pomodoro",  "Italian","Vegetarian","Tangy",  10,20, 160,240,  6,10,  6,12, 24,34, 2,5),
    ("Ricotta Stuffed Shells",  "Italian","Vegetarian","Mild",   35,50, 320,440, 18,26, 14,22, 38,50, 3,6),
    ("Focaccia Bread",          "Italian","Vegetarian","Savory", 30,50, 240,340,  8,14,  8,14, 38,50, 2,5),

    # ── ITALIAN · NON-VEGETARIAN ─────────────────────────────────────────────
    ("Chicken Parmesan",     "Italian","Non-Vegetarian","Savory", 30,50, 380,520, 36,48, 16,24, 24,36, 2,5),
    ("Spaghetti Bolognese",  "Italian","Non-Vegetarian","Savory", 30,50, 400,540, 28,40, 14,22, 48,62, 3,6),
    ("Grilled Salmon Pasta", "Italian","Non-Vegetarian","Mild",   25,40, 380,500, 32,44, 12,20, 40,52, 2,5),
    ("Chicken Piccata",      "Italian","Non-Vegetarian","Tangy",  25,40, 320,440, 36,48, 14,22, 14,22, 1,4),
    ("Shrimp Scampi",        "Italian","Non-Vegetarian","Savory", 20,30, 320,440, 28,40, 14,22, 28,40, 1,4),
    ("Osso Buco",            "Italian","Non-Vegetarian","Savory", 60,90, 400,560, 34,46, 18,28, 12,20, 1,4),
    ("Seafood Pasta",        "Italian","Non-Vegetarian","Savory", 25,40, 360,480, 28,40, 12,20, 42,55, 2,5),
    ("Chicken Marsala",      "Italian","Non-Vegetarian","Savory", 25,40, 340,460, 36,48, 14,22, 16,24, 1,4),
    ("Beef Meatball Pasta",  "Italian","Non-Vegetarian","Savory", 35,55, 420,560, 30,42, 16,24, 48,62, 3,6),
    ("Pancetta Carbonara",   "Italian","Non-Vegetarian","Savory", 20,30, 400,540, 24,36, 20,30, 48,60, 2,5),
    ("Grilled Swordfish",    "Italian","Non-Vegetarian","Mild",   20,30, 280,380, 34,46, 10,18,  2,6,  1,4),
    ("Veal Saltimbocca",     "Italian","Non-Vegetarian","Savory", 20,30, 320,440, 36,48, 14,22,  4,10, 1,3),

    # ── ITALIAN · VEGAN ──────────────────────────────────────────────────────
    ("Pasta Pomodoro",         "Italian","Vegan","Tangy",  20,30, 280,380, 10,16,  5,10, 50,62, 3,6),
    ("Pasta Aglio e Olio",     "Italian","Vegan","Savory", 15,25, 300,400, 10,16, 12,20, 48,60, 3,6),
    ("Minestrone Soup",        "Italian","Vegan","Savory", 30,45, 180,270,  8,14,  3,7,  28,40, 6,11),
    ("Vegan Pesto Pasta",      "Italian","Vegan","Savory", 20,30, 320,420, 10,16, 14,22, 46,58, 3,6),
    ("Roasted Veg Pasta",      "Italian","Vegan","Mild",   30,45, 280,380,  8,14,  8,14, 44,56, 4,8),
    ("Vegan Risotto",          "Italian","Vegan","Savory", 30,45, 300,400,  7,13,  8,14, 52,65, 2,5),
    ("Bruschetta Classica",    "Italian","Vegan","Mild",   10,20, 140,220,  4,8,   4,8,  22,32, 2,5),
    ("Farinata",               "Italian","Vegan","Savory", 20,35, 200,300,  8,14,  6,12, 28,40, 4,8),

    # ── ITALIAN · KETO ───────────────────────────────────────────────────────
    ("Zucchini Noodles Marinara", "Italian","Keto","Tangy",  20,30, 180,270, 10,16,  8,14,  8,14, 3,6),
    ("Keto Chicken Alfredo",      "Italian","Keto","Savory", 25,40, 380,500, 36,48, 24,34,  4,10, 1,3),
    ("Keto Meatballs",            "Italian","Keto","Savory", 25,40, 340,460, 30,42, 22,32,  4,8,  1,3),
    ("Grilled Chicken Pesto Keto","Italian","Keto","Savory", 20,35, 320,440, 36,48, 20,30,  3,7,  1,3),
    ("Caprese Avocado Bowl",      "Italian","Keto","Mild",   10,20, 260,360, 10,16, 22,32,  6,12, 3,6),

    # ── ITALIAN · PALEO ──────────────────────────────────────────────────────
    ("Chicken Cacciatore",        "Italian","Paleo","Savory", 40,60, 300,420, 32,44, 12,20,  8,14, 2,5),
    ("Grilled Sea Bass Italian",  "Italian","Paleo","Mild",   20,30, 240,340, 30,42,  8,16,  2,6,  1,3),
    ("Paleo Meatballs",           "Italian","Paleo","Savory", 25,40, 300,420, 28,40, 16,24,  4,8,  1,3),
    ("Herb Grilled Chicken",      "Italian","Paleo","Mild",   20,35, 260,360, 32,44, 10,18,  2,6,  1,3),

    # ── ASIAN · VEGETARIAN ───────────────────────────────────────────────────
    ("Vegetable Stir Fry",   "Asian","Vegetarian","Spicy",  15,25, 160,250,  6,12,  6,12, 22,32, 4,8),
    ("Veggie Fried Rice",    "Asian","Vegetarian","Savory", 20,30, 280,380,  8,14,  8,14, 45,58, 3,6),
    ("Spring Rolls",         "Asian","Vegetarian","Mild",   20,35, 200,300,  6,12,  8,14, 28,40, 3,6),
    ("Tofu Ramen",           "Asian","Vegetarian","Savory", 25,40, 280,380, 14,22,  8,14, 38,50, 3,6),
    ("Miso Soup",            "Asian","Vegetarian","Savory", 10,20, 80,160,   6,12,  3,7,  10,18, 2,5),
    ("Vegetable Dumplings",  "Asian","Vegetarian","Savory", 25,40, 200,300,  8,14,  6,12, 30,42, 3,6),
    ("Mapo Tofu",            "Asian","Vegetarian","Spicy",  20,30, 240,340, 12,20, 14,22, 14,22, 2,5),
    ("Vegetarian Pad Thai",  "Asian","Vegetarian","Sweet",  20,30, 300,420,  8,14,  8,14, 48,60, 3,6),
    ("Bibimbap Veg",         "Asian","Vegetarian","Savory", 25,40, 320,440, 10,16, 10,16, 50,62, 4,8),
    ("Japchae",              "Asian","Vegetarian","Sweet",  25,40, 280,380,  6,12,  6,12, 48,60, 3,6),
    ("Agedashi Tofu",        "Asian","Vegetarian","Savory", 20,30, 200,300, 10,16, 10,16, 18,28, 2,5),
    ("Chili Paneer",         "Asian","Vegetarian","Spicy",  20,30, 280,380, 14,22, 12,20, 22,32, 2,5),

    # ── ASIAN · NON-VEGETARIAN ───────────────────────────────────────────────
    ("Chicken Fried Rice",       "Asian","Non-Vegetarian","Savory", 20,35, 360,480, 26,36, 12,20, 48,60, 2,5),
    ("Beef Teriyaki",            "Asian","Non-Vegetarian","Sweet",  20,35, 340,460, 30,42, 12,20, 28,40, 1,4),
    ("Shrimp Pad Thai",          "Asian","Non-Vegetarian","Sweet",  20,35, 320,440, 24,34, 10,18, 42,55, 2,5),
    ("Kung Pao Chicken",         "Asian","Non-Vegetarian","Spicy",  20,35, 320,440, 28,40, 14,22, 22,34, 2,5),
    ("Char Siu Pork",            "Asian","Non-Vegetarian","Sweet",  40,60, 360,480, 28,40, 14,22, 30,42, 1,4),
    ("Salmon Teriyaki",          "Asian","Non-Vegetarian","Sweet",  20,30, 320,440, 32,44, 14,22, 22,32, 1,4),
    ("General Tso Chicken",      "Asian","Non-Vegetarian","Spicy",  20,35, 360,480, 28,40, 14,22, 32,44, 1,4),
    ("Beef Ramen",               "Asian","Non-Vegetarian","Savory", 30,50, 380,500, 28,40, 14,22, 42,55, 2,5),
    ("Thai Green Curry Chicken", "Asian","Non-Vegetarian","Spicy",  25,40, 340,460, 28,40, 18,28, 20,30, 2,5),
    ("Vietnamese Pho",           "Asian","Non-Vegetarian","Mild",   40,60, 300,420, 26,36,  8,14, 32,44, 2,5),
    ("Korean BBQ Beef",          "Asian","Non-Vegetarian","Savory", 30,50, 360,480, 30,42, 16,24, 22,34, 1,4),
    ("Duck Noodles",             "Asian","Non-Vegetarian","Savory", 35,55, 400,540, 28,40, 18,28, 42,55, 2,5),

    # ── ASIAN · VEGAN ────────────────────────────────────────────────────────
    ("Tofu Stir Fry",        "Asian","Vegan","Spicy",  15,25, 200,300, 12,20,  8,14, 18,28, 3,6),
    ("Vegetable Sushi Roll", "Asian","Vegan","Mild",   30,50, 220,320,  6,12,  3,7,  42,54, 2,5),
    ("Edamame Bowl",         "Asian","Vegan","Mild",   10,20, 180,260, 14,20,  6,12, 16,26, 5,9),
    ("Miso Tofu Soup",       "Asian","Vegan","Savory", 15,25, 140,220, 10,16,  4,8,  12,20, 3,6),
    ("Vegan Ramen",          "Asian","Vegan","Savory", 25,40, 280,380, 10,18,  6,12, 40,52, 3,6),
    ("Vegan Pad Thai",       "Asian","Vegan","Sweet",  20,30, 300,400, 10,16,  8,14, 48,60, 3,6),
    ("Buddhist Stir Fry",    "Asian","Vegan","Savory", 15,25, 180,270,  8,14,  6,12, 22,32, 4,8),
    ("Mapo Tofu Vegan",      "Asian","Vegan","Spicy",  15,25, 200,300, 10,18, 10,18, 14,22, 2,5),

    # ── ASIAN · KETO ─────────────────────────────────────────────────────────
    ("Cauliflower Fried Rice",  "Asian","Keto","Savory", 20,30, 200,300, 14,22, 12,20,  8,14, 3,6),
    ("Keto Teriyaki Chicken",   "Asian","Keto","Sweet",  20,35, 300,420, 32,44, 14,22,  5,10, 1,3),
    ("Keto Beef and Broccoli",  "Asian","Keto","Savory", 20,30, 320,440, 30,42, 18,28,  8,14, 3,6),
    ("Keto Shrimp Stir Fry",    "Asian","Keto","Spicy",  15,25, 240,340, 26,36, 12,20,  6,12, 2,5),
    ("Egg Foo Young Keto",      "Asian","Keto","Savory", 15,25, 260,360, 18,28, 18,28,  4,8,  1,3),

    # ── ASIAN · PALEO ────────────────────────────────────────────────────────
    ("Chicken Lettuce Wraps",     "Asian","Paleo","Savory", 20,30, 240,340, 28,40, 10,18,  6,12, 2,5),
    ("Paleo Beef and Broccoli",   "Asian","Paleo","Savory", 20,35, 320,440, 30,42, 16,24,  8,14, 3,6),
    ("Lemongrass Grilled Chicken","Asian","Paleo","Savory", 25,40, 260,360, 30,42, 10,18,  4,8,  1,3),
    ("Thai Basil Ground Meat",    "Asian","Paleo","Spicy",  15,25, 280,380, 26,36, 14,22,  6,12, 1,4),
    ("Coconut Curry Chicken",     "Asian","Paleo","Spicy",  25,40, 320,440, 28,40, 18,28,  8,14, 2,5),

    # ── MEDITERRANEAN · VEGETARIAN ───────────────────────────────────────────
    ("Greek Salad",           "Mediterranean","Vegetarian","Tangy",  10,20, 180,270, 10,16, 14,22,  8,14, 3,6),
    ("Falafel Wrap",          "Mediterranean","Vegetarian","Savory", 20,35, 300,420, 12,18, 10,16, 40,54, 6,11),
    ("Hummus Bowl",           "Mediterranean","Vegetarian","Mild",   10,20, 200,300, 10,16, 10,18, 24,34, 5,9),
    ("Spanakopita",           "Mediterranean","Vegetarian","Savory", 40,60, 280,400, 12,18, 14,22, 28,40, 4,8),
    ("Stuffed Bell Peppers",  "Mediterranean","Vegetarian","Savory", 40,60, 240,360, 10,16,  8,14, 32,44, 5,9),
    ("Shakshuka",             "Mediterranean","Vegetarian","Spicy",  20,35, 200,300, 12,18, 12,20, 14,22, 3,6),
    ("Lentil Soup",           "Mediterranean","Vegetarian","Mild",   30,45, 200,300, 12,18,  4,8,  30,42, 7,12),
    ("Fattoush Salad",        "Mediterranean","Vegetarian","Tangy",  10,20, 160,250,  6,12,  8,14, 20,30, 4,8),
    ("Tabbouleh",             "Mediterranean","Vegetarian","Tangy",  15,25, 140,220,  4,8,   6,12, 20,30, 4,8),
    ("Halloumi Salad",        "Mediterranean","Vegetarian","Savory", 15,25, 240,340, 14,20, 16,24, 10,18, 3,6),
    ("Cheese Borek",          "Mediterranean","Vegetarian","Savory", 30,50, 280,400, 12,18, 14,22, 32,44, 2,5),
    ("Moussaka Veg",          "Mediterranean","Vegetarian","Savory", 50,75, 280,400, 10,16, 12,20, 28,40, 5,9),

    # ── MEDITERRANEAN · NON-VEGETARIAN ───────────────────────────────────────
    ("Grilled Sea Bass",     "Mediterranean","Non-Vegetarian","Mild",   20,30, 240,360, 32,44, 10,18,  2,6,  1,3),
    ("Lamb Kebabs",          "Mediterranean","Non-Vegetarian","Savory", 20,35, 300,420, 28,40, 16,24,  4,8,  1,3),
    ("Chicken Souvlaki",     "Mediterranean","Non-Vegetarian","Savory", 20,35, 280,400, 30,42, 10,18,  6,12, 1,3),
    ("Lamb Moussaka",        "Mediterranean","Non-Vegetarian","Savory", 60,90, 380,520, 26,38, 18,28, 24,36, 3,6),
    ("Shrimp Saganaki",      "Mediterranean","Non-Vegetarian","Spicy",  20,35, 280,400, 26,38, 14,22, 12,20, 1,4),
    ("Grilled Octopus",      "Mediterranean","Non-Vegetarian","Savory", 30,50, 220,320, 26,36,  6,14,  4,8,  1,3),
    ("Beef Shawarma",        "Mediterranean","Non-Vegetarian","Savory", 20,35, 360,480, 28,40, 16,24, 24,36, 2,5),
    ("Chicken Shawarma",     "Mediterranean","Non-Vegetarian","Spicy",  20,35, 320,440, 28,40, 12,20, 24,36, 2,5),
    ("Grilled Branzino",     "Mediterranean","Non-Vegetarian","Mild",   20,30, 220,320, 30,42,  8,16,  2,6,  1,3),
    ("Lamb Chops",           "Mediterranean","Non-Vegetarian","Savory", 20,35, 340,460, 30,42, 18,28,  2,6,  1,3),
    ("Fish Tacos Med",       "Mediterranean","Non-Vegetarian","Spicy",  20,35, 300,420, 24,34, 12,20, 24,36, 2,5),

    # ── MEDITERRANEAN · VEGAN ────────────────────────────────────────────────
    ("Vegan Tabbouleh",          "Mediterranean","Vegan","Tangy",  15,25, 140,220,  4,8,   5,10, 20,30, 4,8),
    ("Roasted Veg Mezze",        "Mediterranean","Vegan","Mild",   25,40, 160,250,  5,10,  6,12, 22,32, 5,9),
    ("Lemon Lentil Soup",        "Mediterranean","Vegan","Tangy",  25,40, 180,280, 10,16,  3,7,  26,38, 6,11),
    ("Vegan Falafel Bowl",       "Mediterranean","Vegan","Savory", 20,35, 280,380, 10,16,  8,14, 36,48, 6,11),
    ("Stuffed Grape Leaves",     "Mediterranean","Vegan","Tangy",  30,50, 200,300,  6,12,  6,12, 28,40, 4,8),
    ("Roasted Eggplant Dip",     "Mediterranean","Vegan","Savory", 20,35, 140,220,  4,8,   8,14, 16,26, 4,8),
    ("Hummus Pita Bowl",         "Mediterranean","Vegan","Mild",   10,20, 220,320,  8,14,  8,14, 32,44, 5,9),

    # ── MEDITERRANEAN · KETO ─────────────────────────────────────────────────
    ("Keto Lamb Chops",           "Mediterranean","Keto","Savory", 20,35, 380,520, 30,42, 26,36,  2,6,  1,3),
    ("Mediterranean Egg Bake",    "Mediterranean","Keto","Savory", 20,30, 260,380, 18,28, 18,28,  4,8,  2,5),
    ("Keto Greek Salad",          "Mediterranean","Keto","Tangy",  10,20, 200,300, 10,16, 16,24,  6,12, 3,6),
    ("Grilled Chicken Tzatziki",  "Mediterranean","Keto","Mild",   20,35, 280,400, 32,44, 10,18,  4,8,  1,3),
    ("Keto Stuffed Peppers",      "Mediterranean","Keto","Savory", 40,60, 300,420, 24,34, 18,28,  8,14, 3,6),

    # ── MEDITERRANEAN · PALEO ────────────────────────────────────────────────
    ("Paleo Chicken Souvlaki",   "Mediterranean","Paleo","Savory", 20,35, 260,380, 30,42,  8,16,  6,12, 1,3),
    ("Mediterranean Beef Bowl",  "Mediterranean","Paleo","Savory", 20,35, 320,440, 28,40, 14,22, 10,18, 2,5),
    ("Paleo Lamb Kebabs",        "Mediterranean","Paleo","Savory", 20,35, 300,420, 28,40, 14,22,  4,8,  1,3),
    ("Grilled Fish Med Paleo",   "Mediterranean","Paleo","Mild",   20,30, 220,320, 30,42,  6,14,  2,6,  1,3),

    # ── MEXICAN · VEGETARIAN ─────────────────────────────────────────────────
    ("Bean Tacos",             "Mexican","Vegetarian","Spicy",  15,25, 280,400, 12,18,  8,14, 40,54, 8,14),
    ("Veggie Burrito",         "Mexican","Vegetarian","Savory", 15,25, 360,480, 12,18, 10,16, 54,68, 7,12),
    ("Cheese Quesadilla",      "Mexican","Vegetarian","Savory", 10,20, 320,440, 16,24, 16,24, 36,48, 2,5),
    ("Guacamole Bowl",         "Mexican","Vegetarian","Mild",   10,20, 200,300,  4,8,  16,24, 18,28, 6,11),
    ("Cheese Enchiladas",      "Mexican","Vegetarian","Spicy",  25,40, 360,500, 16,24, 18,28, 36,48, 3,6),
    ("Mexican Corn Salad",     "Mexican","Vegetarian","Sweet",  10,20, 200,300,  6,12,  8,14, 30,42, 4,8),
    ("Bean Nachos",            "Mexican","Vegetarian","Spicy",  15,25, 380,520, 14,20, 18,28, 46,58, 6,11),
    ("Veggie Burrito Bowl",    "Mexican","Vegetarian","Savory", 15,25, 320,440, 12,18,  8,14, 48,62, 7,12),
    ("Cheese Tamales",         "Mexican","Vegetarian","Savory", 45,70, 320,440, 12,18, 14,22, 42,55, 4,8),
    ("Papas con Rajas",        "Mexican","Vegetarian","Mild",   25,40, 240,360,  6,12, 10,16, 36,48, 4,8),
    ("Chiles Rellenos",        "Mexican","Vegetarian","Spicy",  30,50, 280,400, 12,18, 16,24, 26,38, 4,8),

    # ── MEXICAN · NON-VEGETARIAN ─────────────────────────────────────────────
    ("Chicken Tacos",       "Mexican","Non-Vegetarian","Spicy",  15,30, 320,440, 28,40, 10,18, 28,40, 2,5),
    ("Beef Burrito",        "Mexican","Non-Vegetarian","Savory", 15,30, 420,560, 30,42, 16,24, 48,62, 4,8),
    ("Carnitas",            "Mexican","Non-Vegetarian","Savory", 90,120,380,520, 30,42, 20,30, 10,18, 1,3),
    ("Shrimp Fajitas",      "Mexican","Non-Vegetarian","Spicy",  20,30, 300,420, 26,38, 10,18, 24,36, 3,6),
    ("Chicken Enchiladas",  "Mexican","Non-Vegetarian","Spicy",  30,50, 380,520, 30,42, 16,24, 32,44, 3,6),
    ("Al Pastor Tacos",     "Mexican","Non-Vegetarian","Spicy",  25,40, 320,440, 26,38, 14,22, 26,38, 2,5),
    ("Carne Asada",         "Mexican","Non-Vegetarian","Savory", 20,35, 340,460, 34,46, 14,22,  4,8,  1,3),
    ("Fish Tacos",          "Mexican","Non-Vegetarian","Mild",   15,30, 300,420, 24,34, 10,18, 28,40, 2,5),
    ("Chicken Quesadilla",  "Mexican","Non-Vegetarian","Savory", 15,25, 360,480, 28,40, 16,24, 30,42, 2,5),
    ("Birria Tacos",        "Mexican","Non-Vegetarian","Spicy",  60,90, 380,520, 30,42, 16,24, 26,38, 2,5),
    ("Chicken Fajitas",     "Mexican","Non-Vegetarian","Savory", 20,30, 320,440, 30,42, 10,18, 22,34, 3,6),
    ("Beef Tostadas",       "Mexican","Non-Vegetarian","Savory", 20,35, 360,480, 28,40, 16,24, 28,40, 3,6),

    # ── MEXICAN · VEGAN ──────────────────────────────────────────────────────
    ("Black Bean Taco Bowl",  "Mexican","Vegan","Spicy",  15,25, 280,380, 12,18,  6,12, 42,56, 8,14),
    ("Veggie Fajita Bowl",    "Mexican","Vegan","Savory", 15,25, 260,360,  8,14,  6,12, 38,52, 5,9),
    ("Mexican Avocado Toast", "Mexican","Vegan","Mild",   10,20, 220,320,  5,9,  14,22, 22,32, 4,8),
    ("Salsa Bowl",            "Mexican","Vegan","Spicy",  10,20, 180,270,  5,9,   4,9,  28,40, 5,9),
    ("Vegan Burrito",         "Mexican","Vegan","Savory", 15,25, 320,420, 10,16,  8,14, 50,64, 8,14),
    ("Roasted Veggie Tacos",  "Mexican","Vegan","Mild",   20,35, 240,340,  7,13,  8,14, 34,46, 5,9),
    ("Mushroom Tacos",        "Mexican","Vegan","Savory", 15,25, 220,320,  6,12,  6,12, 30,42, 4,8),

    # ── MEXICAN · KETO ───────────────────────────────────────────────────────
    ("Keto Beef Taco Bowl",      "Mexican","Keto","Spicy",  15,25, 340,460, 30,42, 22,32,  5,10, 2,5),
    ("Keto Chicken Fajita Bowl", "Mexican","Keto","Savory", 15,25, 300,420, 32,44, 14,22,  6,12, 2,5),
    ("Cauliflower Burrito Bowl", "Mexican","Keto","Savory", 25,40, 280,400, 24,34, 14,22,  8,14, 3,6),
    ("Keto Carnitas Bowl",       "Mexican","Keto","Savory", 20,35, 360,500, 30,42, 22,32,  4,8,  1,3),
    ("Keto Lettuce Tacos",       "Mexican","Keto","Spicy",  15,25, 260,380, 26,38, 14,22,  4,8,  2,5),

    # ── MEXICAN · PALEO ──────────────────────────────────────────────────────
    ("Chicken Taco Lettuce Wrap","Mexican","Paleo","Spicy",  15,25, 260,380, 28,40, 10,18,  6,12, 2,5),
    ("Paleo Beef Fajita Bowl",   "Mexican","Paleo","Savory", 20,35, 320,440, 30,42, 14,22,  8,14, 2,5),
    ("Grilled Mexican Chicken",  "Mexican","Paleo","Savory", 20,35, 260,360, 30,42,  8,16,  4,8,  1,3),
    ("Paleo Carne Asada",        "Mexican","Paleo","Savory", 20,35, 320,440, 32,44, 14,22,  4,8,  1,3),

    # ── AMERICAN · VEGETARIAN ────────────────────────────────────────────────
    ("Mac and Cheese",           "American","Vegetarian","Savory", 20,35, 380,520, 16,24, 16,24, 48,62, 2,5),
    ("Veggie Burger",            "American","Vegetarian","Savory", 15,25, 320,440, 16,24, 14,22, 38,50, 5,9),
    ("Grilled Cheese Sandwich",  "American","Vegetarian","Savory", 10,20, 320,440, 14,20, 18,28, 36,48, 2,5),
    ("Caesar Salad",             "American","Vegetarian","Savory", 10,20, 200,300, 10,16, 14,22, 14,22, 3,6),
    ("Vegetarian Chili",         "American","Vegetarian","Spicy",  30,50, 260,380, 14,22,  6,12, 36,50, 8,14),
    ("Avocado Toast",            "American","Vegetarian","Mild",   10,20, 220,320,  7,13, 14,22, 26,36, 5,9),
    ("Garden Salad",             "American","Vegetarian","Mild",   10,20, 120,200,  4,8,   6,12, 16,24, 4,8),
    ("Cheese Pizza",             "American","Vegetarian","Savory", 20,35, 340,480, 16,24, 12,20, 46,60, 2,5),
    ("Loaded Baked Potato",      "American","Vegetarian","Savory", 50,70, 340,480, 12,18, 14,22, 48,62, 5,9),
    ("French Onion Soup",        "American","Vegetarian","Savory", 40,60, 280,400, 14,22, 12,20, 28,40, 3,6),
    ("Veggie Wrap",              "American","Vegetarian","Mild",   10,20, 280,400, 10,16,  8,14, 40,54, 4,8),
    ("Caprese Sandwich",         "American","Vegetarian","Mild",   10,20, 280,380, 12,18, 12,20, 34,46, 2,5),

    # ── AMERICAN · NON-VEGETARIAN ────────────────────────────────────────────
    ("BBQ Chicken",           "American","Non-Vegetarian","Sweet",  30,50, 340,480, 36,48, 12,20, 18,30, 1,3),
    ("Classic Beef Burger",   "American","Non-Vegetarian","Savory", 15,30, 420,580, 30,42, 22,32, 36,48, 2,5),
    ("Grilled Ribeye Steak",  "American","Non-Vegetarian","Savory", 20,35, 400,560, 40,54, 22,32,  2,6,  1,3),
    ("Chicken Wings",         "American","Non-Vegetarian","Spicy",  25,40, 360,500, 32,44, 22,32,  6,12, 1,3),
    ("Turkey Club Sandwich",  "American","Non-Vegetarian","Savory", 10,20, 340,480, 28,40, 14,22, 30,42, 2,5),
    ("Pulled Pork Sandwich",  "American","Non-Vegetarian","Sweet",  90,120,400,560, 28,40, 16,24, 38,52, 2,5),
    ("Chicken Caesar Wrap",   "American","Non-Vegetarian","Savory", 10,20, 340,460, 32,44, 14,22, 24,36, 2,5),
    ("Fish and Chips",        "American","Non-Vegetarian","Savory", 25,40, 420,580, 28,40, 20,30, 42,56, 2,5),
    ("BLT Sandwich",          "American","Non-Vegetarian","Savory", 10,20, 320,440, 20,30, 16,24, 30,42, 2,5),
    ("Shrimp Po Boy",         "American","Non-Vegetarian","Spicy",  20,30, 360,500, 24,34, 16,24, 38,52, 2,5),
    ("Chicken Pot Pie",       "American","Non-Vegetarian","Savory", 50,75, 420,580, 26,38, 22,32, 38,52, 2,5),
    ("Lobster Bisque",        "American","Non-Vegetarian","Savory", 30,50, 320,440, 20,30, 16,24, 22,32, 1,3),

    # ── AMERICAN · VEGAN ─────────────────────────────────────────────────────
    ("Vegan Burger",        "American","Vegan","Savory", 15,25, 300,420, 18,26, 12,20, 36,50, 5,9),
    ("Acai Bowl",           "American","Vegan","Sweet",  10,20, 280,400,  6,12, 10,18, 48,62, 6,11),
    ("Vegan Mac",           "American","Vegan","Savory", 25,40, 340,460, 10,16, 12,20, 54,68, 3,6),
    ("Lentil Chili Bowl",   "American","Vegan","Spicy",  30,50, 260,380, 14,22,  4,9,  38,52, 8,14),
    ("Tofu Scramble",       "American","Vegan","Savory", 10,20, 220,320, 14,22, 10,18, 10,18, 3,6),
    ("Vegan Buffalo Wings", "American","Vegan","Spicy",  25,40, 240,360, 12,20, 10,18, 22,34, 4,8),
    ("Smoothie Bowl",       "American","Vegan","Sweet",  10,20, 300,420,  8,14, 10,18, 52,66, 6,11),
    ("Vegan BLT",           "American","Vegan","Savory", 10,20, 260,380,  8,14,  8,14, 34,48, 4,8),

    # ── AMERICAN · KETO ──────────────────────────────────────────────────────
    ("Keto Burger Bowl",       "American","Keto","Savory", 15,25, 380,520, 34,46, 26,36,  4,8,  1,3),
    ("Bacon and Eggs",         "American","Keto","Savory", 10,20, 320,440, 24,34, 26,36,  2,6,  1,3),
    ("Keto Steak Asparagus",   "American","Keto","Savory", 20,35, 420,580, 40,54, 28,38,  4,8,  2,5),
    ("Keto Chicken Salad",     "American","Keto","Mild",   10,20, 280,400, 30,42, 18,28,  4,8,  2,5),
    ("Keto BLT Salad",         "American","Keto","Savory", 10,20, 300,420, 22,32, 22,32,  4,8,  2,5),
    ("Keto Chili",             "American","Keto","Spicy",  30,50, 340,480, 30,42, 20,30,  6,12, 3,6),

    # ── AMERICAN · PALEO ─────────────────────────────────────────────────────
    ("Paleo Chicken Bowl",    "American","Paleo","Savory", 20,35, 280,400, 32,44, 10,18,  8,14, 2,5),
    ("Grass-fed Beef Steak",  "American","Paleo","Savory", 20,35, 380,520, 40,54, 20,30,  2,6,  1,3),
    ("Turkey Lettuce Wrap",   "American","Paleo","Mild",   10,20, 240,340, 28,40,  8,16,  6,12, 2,5),
    ("Paleo Chicken Wings",   "American","Paleo","Spicy",  25,40, 300,420, 32,44, 14,22,  4,8,  1,3),
    ("Grilled Salmon American","American","Paleo","Mild",  20,30, 300,420, 34,46, 14,22,  2,6,  1,3),
]

# ---------------------------------------------------------------------------
# BUILD RECIPES DATAFRAME
# ---------------------------------------------------------------------------

def rand_range(lo, hi, decimal=1):
    return round(random.uniform(lo, hi), decimal)

def build_recipes():
    rows = []
    for i, entry in enumerate(CATALOG):
        (name, cuisine, diet, taste,
         ck_lo, ck_hi,
         cal_lo, cal_hi,
         prot_lo, prot_hi,
         fat_lo, fat_hi,
         carb_lo, carb_hi,
         fib_lo, fib_hi) = entry

        # Micronutrients vary by diet type
        vit_c = rand_range(5, 40) if diet in ("Vegan","Vegetarian","Paleo") else rand_range(2, 20)
        iron  = rand_range(2, 8)  if diet in ("Vegan","Vegetarian") else rand_range(1, 5)
        calcium = rand_range(30, 200) if diet in ("Vegetarian",) else rand_range(10, 100)

        rows.append({
            "Recipe_ID":       f"R{i+1:03d}",
            "Recipe_Name":     name,
            "Cuisine":         cuisine,
            "Recipe_Diet":     diet,          # matches app filter values
            "Taste":           taste,
            "Cooking_Time":    random.randint(ck_lo, ck_hi),
            "Calories":        random.randint(cal_lo, cal_hi),
            "Protein_g":       rand_range(prot_lo, prot_hi),
            "Fat_g":           rand_range(fat_lo, fat_hi),
            "Carbs_g":         rand_range(carb_lo, carb_hi),
            "Fiber_g":         rand_range(fib_lo, fib_hi),
            "Vitamin_C_mg":    vit_c,
            "Iron_mg":         iron,
            "Calcium_mg":      calcium,
        })
    return pd.DataFrame(rows)

# ---------------------------------------------------------------------------
# BUILD USERS DATAFRAME (200 users, all filter combos represented)
# ---------------------------------------------------------------------------

DIETS    = ["Vegetarian","Non-Vegetarian","Vegan","Keto","Paleo"]
CUISINES = ["Indian","Italian","Asian","Mediterranean","Mexican","American"]
TASTES   = ["Spicy","Sweet","Mild","Savory","Tangy"]
HEALTH   = ["None","Diabetes","Iron Deficiency","Vitamin D Deficiency","High Blood Pressure"]
GENDERS  = ["Male","Female","Other"]

def build_users(n=200):
    # Seed one user for every diet × cuisine combo (30 combinations) so all filters have data
    rows = []
    uid = 1
    for diet in DIETS:
        for cuisine in CUISINES:
            rows.append({
                "User_ID":              f"U{uid:03d}",
                "Age":                  random.randint(18, 60),
                "Gender":               random.choice(GENDERS),
                "BMI":                  round(random.uniform(18.0, 32.0), 1),
                "Health_Condition":     random.choice(HEALTH),
                "Dietary_Restriction":  diet,
                "Preferred_Cuisine":    cuisine,
                "Taste_Preference":     random.choice(TASTES),
            })
            uid += 1

    # Fill rest randomly
    while uid <= n:
        rows.append({
            "User_ID":              f"U{uid:03d}",
            "Age":                  random.randint(18, 65),
            "Gender":               random.choice(GENDERS),
            "BMI":                  round(random.uniform(18.0, 35.0), 1),
            "Health_Condition":     random.choice(HEALTH),
            "Dietary_Restriction":  random.choice(DIETS),
            "Preferred_Cuisine":    random.choice(CUISINES),
            "Taste_Preference":     random.choice(TASTES),
        })
        uid += 1

    return pd.DataFrame(rows)

# ---------------------------------------------------------------------------
# BUILD FEEDBACK (3000 interactions, biased toward matching user preferences)
# ---------------------------------------------------------------------------

def build_feedback(users: pd.DataFrame, recipes: pd.DataFrame, n=3000):
    """
    Generate realistic, balanced feedback.
    - Matching diet + cuisine: ratings skewed toward 4-5
    - Matching diet only: ratings around 3-4
    - Mismatched diet: ratings skewed toward 1-2
    This gives the ML model a real signal to learn from (roughly 50/50 recommend split).
    """
    rows = []
    seen = set()

    for _, u in users.iterrows():
        uid   = u["User_ID"]
        u_diet    = u["Dietary_Restriction"]
        u_cuisine = u["Preferred_Cuisine"]
        u_taste   = u["Taste_Preference"]

        # Classify each recipe into match tiers for this user
        full_match  = recipes[(recipes["Recipe_Diet"] == u_diet) & (recipes["Cuisine"] == u_cuisine)]
        diet_match  = recipes[(recipes["Recipe_Diet"] == u_diet) & (recipes["Cuisine"] != u_cuisine)]
        no_match    = recipes[recipes["Recipe_Diet"]  != u_diet]

        def sample_tier(pool, k, base_mean, base_std):
            k = min(k, len(pool))
            if k == 0:
                return
            for _, r in pool.sample(k).iterrows():
                key = (uid, r["Recipe_ID"])
                if key in seen:
                    continue
                seen.add(key)
                # Taste match adds +0.5 to mean
                taste_bonus = 0.5 if r.get("Taste") == u_taste else 0.0
                rating = int(np.clip(np.random.normal(base_mean + taste_bonus, base_std), 1, 5))
                rows.append({"User_ID": uid, "Recipe_ID": r["Recipe_ID"], "User_Rating": rating})

        sample_tier(full_match, 6, base_mean=4.0, base_std=0.8)   # good match → high ratings
        sample_tier(diet_match, 3, base_mean=3.0, base_std=1.0)   # partial match → neutral
        sample_tier(no_match,   2, base_mean=1.8, base_std=0.8)   # diet mismatch → low ratings

    # Random interactions to reach n
    user_ids   = users["User_ID"].tolist()
    recipe_ids = recipes["Recipe_ID"].tolist()
    while len(rows) < n:
        uid = random.choice(user_ids)
        rid = random.choice(recipe_ids)
        key = (uid, rid)
        if key not in seen:
            seen.add(key)
            rows.append({"User_ID": uid, "Recipe_ID": rid, "User_Rating": random.randint(1, 5)})

    return pd.DataFrame(rows[:n])

# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

print("Generating recipes...")
recipes = build_recipes()
recipes.to_csv("recipes.csv", index=False)
print(f"  {len(recipes)} unique recipes across {recipes['Cuisine'].nunique()} cuisines")

print("Generating users...")
users = build_users(200)
users.to_csv("user_profiles.csv", index=False)
print(f"  {len(users)} users")

print("Generating feedback...")
feedback = build_feedback(users, recipes, n=3000)
feedback.to_csv("user_feedback.csv", index=False)
print(f"  {len(feedback)} interactions")

# ── Nutrition sidecar (kept for compatibility) ───────────────────────────────
nutrition = pd.DataFrame({
    "Food_ID":    [f"F{i+1:03d}" for i in range(300)],
    "Food_Name":  [random.choice(["Apple","Chicken","Rice","Broccoli","Spinach","Fish","Tofu","Paneer","Oats","Banana"]) for _ in range(300)],
    "Calories":   [random.randint(30, 600) for _ in range(300)],
    "Protein_g":  [round(random.uniform(0.1, 35.0), 1) for _ in range(300)],
    "Fat_g":      [round(random.uniform(0.1, 25.0), 1) for _ in range(300)],
    "Carbs_g":    [round(random.uniform(5.0, 60.0), 1) for _ in range(300)],
    "Fiber_g":    [round(random.uniform(0.1, 10.0), 1) for _ in range(300)],
    "Vitamin_C_mg":[round(random.uniform(1.0, 90.0), 1) for _ in range(300)],
    "Iron_mg":    [round(random.uniform(0.1, 5.0), 1) for _ in range(300)],
    "Calcium_mg": [round(random.uniform(5.0, 300.0), 1) for _ in range(300)],
})
nutrition.to_csv("nutrition.csv", index=False)

# ── Merge into final_dataset.csv ─────────────────────────────────────────────
print("Merging into final_dataset.csv...")
merged = (feedback
          .merge(users,   on="User_ID",   how="left")
          .merge(recipes, on="Recipe_ID", how="left"))

merged["Nutrient_Score"]   = np.random.uniform(0.6, 1.0, len(merged))
merged["Preference_Score"] = np.random.uniform(0.5, 1.0, len(merged))
merged["Recommended"]      = (merged["User_Rating"] >= 4).astype(int)

merged.to_csv("final_dataset.csv", index=False)
print(f"  final_dataset.csv: {len(merged)} rows, {merged['Recipe_Name'].nunique()} unique recipes")
print("\nAll datasets generated successfully.")

# Coverage report
print("\nRecipes per Cuisine x Diet:")
print(recipes.groupby(["Cuisine","Recipe_Diet"]).size().to_string())
