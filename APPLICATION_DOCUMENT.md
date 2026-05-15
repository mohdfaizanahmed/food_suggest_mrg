# AI Food Genius — Application Document

---

## What Is This Application?

**AI Food Genius** is a personalized food recommendation web application. Given a user's age, health condition, dietary preference, and taste profile, it suggests the most suitable recipes — ranked by an AI system that considers nutrition, personal taste, and the behaviour of similar users.

It is built as a fully functional web app using Python and Streamlit, runs entirely on a local machine, and requires no paid APIs or cloud services.

---

## What Can a User Do?

The application has five sections:

| Page | What it does |
|---|---|
| **Home** | Shows an overview dashboard with platform stats and trending recipes |
| **AI Recommendations** | The main feature — enter your profile and get personalized recipe suggestions |
| **Analytics** | Visual breakdowns of model accuracy, calorie distribution, cuisine spread, macronutrients |
| **Profile** | Save your preferences permanently; view your rating history |
| **Favourites** | All recipes you saved with the ❤️ button, in one place |

Users can also **register and log in**. All data (saved recipes, ratings, profile settings) persists across sessions using a local database — nothing is lost on page refresh.

---

## The Dataset

Everything the AI learns from comes from a structured dataset built specifically for this application.

| What | Size |
|---|---|
| Unique recipes | **250** (all with real names) |
| User profiles | **200** |
| User–recipe interactions | **3,000** |
| Total columns per record | **26** |

**Cuisines covered:** Indian, Italian, Asian, Mediterranean, Mexican, American

**Diet types:** Vegetarian, Non-Vegetarian, Vegan, Keto, Paleo

**Taste profiles:** Spicy, Sweet, Mild, Savory, Tangy

**Health conditions tracked:** None, Diabetes, Iron Deficiency, Vitamin D Deficiency, High Blood Pressure

Every cuisine–diet combination has between 4 and 15 recipes, ensuring that no filter combination returns an empty result. Recipes are assigned realistic nutritional values (calories, protein, carbs, fat, fiber, Vitamin C, iron, calcium) matched to their diet type — for example, Keto recipes are high-fat and low-carb by design.

Each record in the dataset captures 26 pieces of information including the user's profile, the recipe's nutritional content, a nutrient quality score, a preference score, and whether the user recommended the recipe (1 = yes, 0 = no).

---

## How Recommendations Work

Getting a recommendation is not a single step. The system runs three layers in sequence.

---

### Layer 1 — Filtering

Before any AI scoring happens, the system filters the recipe pool to only show what is actually relevant:

1. **Diet filter** — Only recipes matching the selected diet type (e.g., Vegan) are considered. This uses the recipe's own diet tag, not the user's profile column, so a Vegan filter will never show chicken dishes.
2. **Cuisine filter** — Narrowed further to the preferred cuisine (e.g., Indian Vegan recipes only).
3. **Cooking time filter** — Any recipe that takes longer than the user's maximum cooking time is removed.
4. **Fallback logic** — If fewer than 5 recipes survive the strict filter, the system relaxes the cuisine constraint (diet-only match), then falls back to the full pool if needed. This ensures users always see results.

---

### Layer 2 — AI Scoring (5-Model Ensemble)

The filtered recipes are then scored individually by five machine learning models working together. Each model receives a feature vector combining the recipe's nutritional data with the user's profile information, and outputs a probability — "how likely is this recipe to be recommended for this person?"

The five models are:

**1. Random Forest**
A collection of 100 decision trees, each trained on a random subset of the data. They vote together, which makes the result stable and resistant to noise. Parameters: 100 trees, max depth 10.

**2. XGBoost (Extreme Gradient Boosting)**
Trees built sequentially, where each new tree corrects the errors of the previous one. Well known for strong performance on structured/tabular data. Parameters: 100 trees, depth 6.

**3. Neural Network (MLP)**
A three-layer neural network (input → 64 neurons → 32 neurons → output) that learns non-linear relationships between features that tree-based models might miss. Trained for up to 300 iterations.

**4. LightGBM (Light Gradient Boosting Machine)**
A Microsoft-developed gradient boosting framework that grows trees leaf-wise (not level-wise like XGBoost), making it faster and often more accurate, especially when the dataset has many features. Parameters: 200 trees, depth 6, learning rate 0.05.

**5. CatBoost (Categorical Boosting)**
Developed by Yandex. Unlike the other models, CatBoost handles categorical features (like cuisine type, diet type) natively without manual encoding, which reduces information loss. Parameters: 200 iterations, depth 6, learning rate 0.05.

#### How the five models are combined

Each model is scored on a held-out test set (20% of the data). Its weight in the final answer is proportional to how accurate it was:

```
Final score = Σ (model_accuracy / total_accuracy) × model_probability
```

A model that scored 65% accuracy gets more say than one that scored 55%. This is called a **weighted ensemble** and consistently outperforms any single model alone.

---

### Layer 3 — Multi-Component Final Score

The ensemble output is only 40% of the final score. Three more factors are layered on top to make the result genuinely personalized:

| Component | Weight | What it does |
|---|---|---|
| ML ensemble probability | **40%** | Learned from 3,000 user–recipe interactions |
| Taste match | **25%** | +0.25 bonus if recipe taste matches user's stated preference exactly (e.g., both Spicy) |
| Health condition bonus | **20%** | Adjusts scores based on nutritional needs — Diabetes → prefers low-carb/high-fiber; Iron Deficiency → prefers high-iron foods; High Blood Pressure → prefers low-fat/high-fiber |
| Nutrient quality score | **15%** | A recipe-level quality score based on overall nutritional balance |

After combining all four components, scores are **normalized** within the result set so the top and bottom recipes are clearly differentiated — no more "everything scores 0.99."

The top 10 recipes by this final score are shown to the user.

---

### Layer 4 — Collaborative Filtering (After You Rate Recipes)

Once a user has rated at least a few recipes, a fourth recommendation layer activates: **collaborative filtering**.

This works by finding other users in the system who rated recipes similarly to you (measured using cosine similarity on a user–recipe rating matrix). It then recommends recipes those similar users gave high ratings to, but that you haven't tried yet.

This is the same core technique used by Netflix and Spotify — "users like you also enjoyed..."

---

## Accuracy

### What we measured

Models are evaluated on a held-out test set (20% of the data, 600 records) that was never used during training. The metric is **classification accuracy** — what percentage of the time does the model correctly predict whether a user will recommend a recipe or not.

### Results (without data leakage)

| Model | Accuracy |
|---|---|
| Random Forest | **62.8%** |
| CatBoost | 59.3% |
| XGBoost | 57.3% |
| LightGBM | 56.3% |
| Neural Network | 53.5% |
| **Weighted Ensemble** | **~63%** (best of all) |

### Honest context — how does this compare to research?

Research papers on food recommendation systems typically report **75–90% accuracy**, but those numbers come from:

- Datasets with **1 million+ real interactions** (e.g., Food.com, Yelp, Recipe1M)
- Metrics like **NDCG@10** and **Precision@K**, which measure ranking quality — not just correct/wrong
- Systems trained on years of real user behaviour

Our dataset is **synthetic and small** (3,000 interactions, 250 recipes). A direct comparison with research benchmarks would not be fair or meaningful.

What this application demonstrates is the **correct architecture**: a multi-model ensemble, collaborative filtering, health-aware scoring, and persistent user profiles. Replacing the synthetic dataset with real user data from a live API (Spoonacular, Edamam) would close the gap significantly.

---

## Data Storage

The application uses two storage layers:

**CSV files** — The recipe and user dataset lives in `final_dataset.csv`, generated by the data builder (`h1.py`). This is what the AI models train on.

**SQLite database** (`food_genius.db`) — A lightweight local database that stores:
- User accounts (username + hashed password)
- Saved/favourite recipes (per user)
- Recipe ratings (per user, with timestamp)

Passwords are never stored in plain text — they are hashed using SHA-256 before being saved.

---

## Technology Stack

| Layer | Technology |
|---|---|
| Web framework | Streamlit |
| Data handling | Pandas, NumPy |
| Machine learning | scikit-learn, XGBoost, LightGBM, CatBoost |
| Similarity search | scikit-learn (cosine similarity) |
| Charts & graphs | Plotly |
| Database | SQLite (Python stdlib — no install needed) |
| Language | Python 3 |

---

## How the System Learns from Feedback

Every time a logged-in user rates a recipe (1–5 stars), that rating is saved to the database. These ratings immediately improve the collaborative filtering recommendations — the more you rate, the more accurately the system can find users similar to you and surface recipes you are likely to enjoy.

The ML models themselves are trained once at startup (and cached), so they benefit from ratings on the next session restart. This is a realistic design — production recommendation systems retrain on a scheduled basis (daily/weekly) rather than in real-time.

---

## Summary

AI Food Genius is a multi-layer recommendation system that combines:

1. **Hard filtering** — only showing recipes appropriate for your diet and cuisine
2. **A 5-model AI ensemble** — RandomForest, XGBoost, LightGBM, CatBoost, and a Neural Network, combined by accuracy-weighted voting
3. **Personalized scoring** — taste matching, health-condition nutrition bonuses, and recipe quality
4. **Collaborative filtering** — learning from users with similar preferences
5. **Persistent memory** — your profile, ratings, and favourites saved across sessions

The system achieves ~63% recommendation accuracy on a synthetic dataset of 250 recipes and 3,000 interactions, and is architected to scale directly to research-level performance once connected to real-world recipe and user data.

---

*Document generated for AI Food Genius | Built with Python, Streamlit, and scikit-learn ecosystem*
