"""
AI FOOD GENIUS - IMPROVED VERSION
==================================
Improvements over original simplified edition:
- SQLite persistence: user profiles, favorites, and ratings survive page refresh
- Real user authentication with hashed passwords and session management
- @st.cache_resource on ML models so they are trained once, not on every interaction
- Per-recipe AI scoring: each recipe gets its own score for the user profile
- Real collaborative filtering using user_feedback.csv cosine similarity
- Favorites system: save/unsave recipes, persisted in SQLite
- In-app recipe rating that feeds future recommendations
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.metrics.pairwise import cosine_similarity
import xgboost as xgb
import lightgbm as lgb
from catboost import CatBoostClassifier
import sqlite3
import hashlib
from datetime import datetime

# ============================================================================
# PAGE CONFIG (must be first Streamlit call)
# ============================================================================

st.set_page_config(
    page_title="AI Food Genius",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CUSTOM CSS
# ============================================================================

def load_custom_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');

    .main { padding: 0; }

    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 0;
        text-align: center;
        color: white;
        border-radius: 0 0 30px 30px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    .main-header h1 {
        font-family: 'Poppins', sans-serif;
        font-weight: 900;
        font-size: 3.5rem;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .main-header p {
        font-family: 'Inter', sans-serif;
        font-size: 1.2rem;
        margin: 1rem 0 0 0;
        opacity: 0.9;
    }

    .recipe-card {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
        border: 1px solid rgba(0,0,0,0.05);
    }
    .recipe-card:hover { transform: translateY(-5px); box-shadow: 0 15px 35px rgba(0,0,0,0.15); }
    .recipe-title {
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        font-size: 1.6rem;
        color: #2c3e50;
        margin-bottom: 1rem;
    }
    .recipe-meta { display: flex; gap: 1rem; margin: 1rem 0; flex-wrap: wrap; }
    .meta-item {
        background: #f8f9fa;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        color: #495057;
        border: 1px solid #e9ecef;
    }

    .metric-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        border: 1px solid rgba(0,0,0,0.05);
    }
    .metric-value {
        font-size: 2.8rem;
        font-weight: 900;
        margin: 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-family: 'Poppins', sans-serif;
    }
    .metric-label { font-size: 1rem; color: #2c3e50; margin: 0.5rem 0 0 0; font-weight: 600; }

    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.7rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton > button:hover { transform: translateY(-2px); box-shadow: 0 8px 20px rgba(0,0,0,0.2); }

    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    .fade-in-up { animation: fadeInUp 0.5s ease-out; }
    </style>
    """, unsafe_allow_html=True)

load_custom_css()

# ============================================================================
# DATABASE LAYER
# ============================================================================

DB_PATH = "food_genius.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password_hash TEXT NOT NULL,
            age INTEGER DEFAULT 25,
            gender TEXT DEFAULT 'Other',
            bmi REAL DEFAULT 22.0,
            health_condition TEXT DEFAULT 'None',
            dietary_restriction TEXT DEFAULT 'Vegetarian',
            preferred_cuisine TEXT DEFAULT 'Indian',
            taste_preference TEXT DEFAULT 'Mild'
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS favorites (
            username TEXT,
            recipe_name TEXT,
            added_at TEXT,
            PRIMARY KEY (username, recipe_name)
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS ratings (
            username TEXT,
            recipe_name TEXT,
            rating INTEGER,
            rated_at TEXT,
            PRIMARY KEY (username, recipe_name)
        )
    """)
    conn.commit()
    conn.close()

init_db()

def _hash(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username: str, password: str, profile: dict) -> bool:
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.execute(
            "INSERT INTO users VALUES (?,?,?,?,?,?,?,?,?)",
            (username, _hash(password),
             profile.get('age', 25), profile.get('gender', 'Other'),
             profile.get('bmi', 22.0), profile.get('health_condition', 'None'),
             profile.get('dietary_restriction', 'Vegetarian'),
             profile.get('preferred_cuisine', 'Indian'),
             profile.get('taste_preference', 'Mild'))
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def authenticate_user(username: str, password: str):
    conn = sqlite3.connect(DB_PATH)
    row = conn.execute(
        "SELECT age, gender, bmi, health_condition, dietary_restriction, preferred_cuisine, taste_preference "
        "FROM users WHERE username=? AND password_hash=?",
        (username, _hash(password))
    ).fetchone()
    conn.close()
    if row:
        keys = ['age', 'gender', 'bmi', 'health_condition', 'dietary_restriction', 'preferred_cuisine', 'taste_preference']
        return {'username': username, **dict(zip(keys, row))}
    return None

def update_profile(username: str, profile: dict):
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "UPDATE users SET age=?, gender=?, bmi=?, health_condition=?, dietary_restriction=?, preferred_cuisine=?, taste_preference=? WHERE username=?",
        (profile['age'], profile['gender'], profile['bmi'],
         profile['health_condition'], profile['dietary_restriction'],
         profile['preferred_cuisine'], profile['taste_preference'], username)
    )
    conn.commit()
    conn.close()
    st.session_state.user.update(profile)

def add_favorite(username: str, recipe_name: str):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("INSERT OR IGNORE INTO favorites VALUES (?,?,?)",
                 (username, recipe_name, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def remove_favorite(username: str, recipe_name: str):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("DELETE FROM favorites WHERE username=? AND recipe_name=?", (username, recipe_name))
    conn.commit()
    conn.close()

def get_favorites(username: str) -> set:
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute("SELECT recipe_name FROM favorites WHERE username=?", (username,)).fetchall()
    conn.close()
    return {r[0] for r in rows}

def save_rating(username: str, recipe_name: str, rating: int):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("INSERT OR REPLACE INTO ratings VALUES (?,?,?,?)",
                 (username, recipe_name, rating, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def get_user_ratings(username: str) -> dict:
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute("SELECT recipe_name, rating FROM ratings WHERE username=?", (username,)).fetchall()
    conn.close()
    return {r[0]: r[1] for r in rows}

# ============================================================================
# DATA LOADING
# ============================================================================

@st.cache_data(ttl=3600)
def load_data() -> pd.DataFrame:
    try:
        df = pd.read_csv("final_dataset.csv")
        return _enhance(df)
    except FileNotFoundError:
        st.error("Dataset not found. Run h1.py first.")
        st.stop()

@st.cache_data(ttl=3600)
def load_feedback_pivot():
    """Build user-item rating matrix from user_feedback.csv for collaborative filtering."""
    try:
        fb = pd.read_csv("user_feedback.csv")
        return fb.pivot_table(index='User_ID', columns='Recipe_ID', values='User_Rating', fill_value=0)
    except FileNotFoundError:
        return None

def _enhance(df: pd.DataFrame) -> pd.DataFrame:
    # Preserve Recipe_Diet if the CSV already has it (generated by new h1.py).
    # Only fall back to keyword detection if the column is missing (old datasets).
    if 'Recipe_Diet' not in df.columns:
        non_veg = ['chicken', 'egg', 'fish', 'mutton', 'prawn', 'meat', 'beef', 'shrimp', 'lamb', 'pork']
        df['Recipe_Diet'] = df['Recipe_Name'].apply(
            lambda x: 'Non-Vegetarian' if any(w in str(x).lower() for w in non_veg) else 'Vegetarian'
        )
    else:
        df['Recipe_Diet'] = df['Recipe_Diet'].fillna('Vegetarian').astype(str)

    # Keep Diet_Type as an alias for backward-compat display
    df['Diet_Type'] = df['Recipe_Diet']

    # Preserve Taste column from new dataset; fall back to Taste_Preference
    if 'Taste' not in df.columns and 'Taste_Preference' in df.columns:
        df['Taste'] = df['Taste_Preference']
    elif 'Taste' in df.columns:
        df['Taste'] = df['Taste'].fillna('Savory').astype(str)

    for col in ['Health_Condition', 'Gender', 'Dietary_Restriction', 'Preferred_Cuisine', 'Taste_Preference']:
        if col in df.columns:
            df[col] = df[col].fillna('None').astype(str)
    for col in ['Nutrient_Score', 'Preference_Score', 'Calories', 'Protein_g', 'Carbs_g', 'Fat_g',
                'Fiber_g', 'Vitamin_C_mg', 'Iron_mg', 'User_Rating', 'BMI', 'Age']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(df[col].median())
    df['Total_Macros'] = df['Protein_g'] + df['Carbs_g'] + df['Fat_g']
    df['Protein_Ratio'] = df['Protein_g'] / df['Total_Macros'].replace(0, 1)
    df['Health_Score'] = (df['Nutrient_Score'] + df['Preference_Score']) / 2
    # use deterministic seeds so scores don't shuffle on every cache miss
    rng = np.random.default_rng(42)
    df['Complexity_Score'] = rng.uniform(0.3, 1.0, len(df))
    df['Seasonal_Score']   = rng.uniform(0.5, 1.0, len(df))
    df['Trending_Score']   = rng.uniform(0.4, 1.0, len(df))
    return df

# ============================================================================
# ML RECOMMENDER — cached so models train once per session
# ============================================================================

class FoodRecommender:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        self.encoders: dict = {}
        self.scaler = StandardScaler()
        self._prepare()
        self._train()

    def _prepare(self):
        cat_cols = ['Gender', 'Health_Condition', 'Dietary_Restriction',
                    'Preferred_Cuisine', 'Taste_Preference', 'Diet_Type', 'Cuisine']
        for col in cat_cols:
            if col in self.df.columns:
                le = LabelEncoder()
                self.df[f'{col}_enc'] = le.fit_transform(self.df[col].astype(str))
                self.encoders[col] = le

        base_feats = ['Age', 'BMI', 'Calories', 'Protein_g', 'Carbs_g', 'Fat_g',
                      'Fiber_g', 'Vitamin_C_mg', 'Iron_mg', 'User_Rating',
                      'Nutrient_Score', 'Preference_Score', 'Total_Macros',
                      'Protein_Ratio', 'Health_Score', 'Complexity_Score',
                      'Seasonal_Score', 'Trending_Score']
        enc_feats = [f'{c}_enc' for c in cat_cols if f'{c}_enc' in self.df.columns]
        self.feature_cols = [c for c in base_feats + enc_feats if c in self.df.columns]

        self.X = self.df[self.feature_cols].fillna(0)
        # Target: recommended if rated >= 4, else not
        if 'Recommended' in self.df.columns:
            self.y = self.df['Recommended']
        else:
            self.y = (self.df['User_Rating'] >= 4).astype(int)

        self.X_scaled = self.scaler.fit_transform(self.X)

    def _train(self):
        X_tr, X_te, y_tr, y_te = train_test_split(
            self.X_scaled, self.y, test_size=0.2, random_state=42, stratify=self.y
        )
        self.models = {
            'RandomForest': RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42, n_jobs=-1),
            'XGBoost':      xgb.XGBClassifier(n_estimators=100, max_depth=6, random_state=42, eval_metric='logloss', verbosity=0),
            'NeuralNet':    MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=300, random_state=42),
            'LightGBM':     lgb.LGBMClassifier(n_estimators=200, max_depth=6, learning_rate=0.05,
                                                num_leaves=31, random_state=42, verbose=-1),
            'CatBoost':     CatBoostClassifier(iterations=200, depth=6, learning_rate=0.05,
                                               random_seed=42, verbose=0),
        }
        self.model_scores: dict = {}
        for name, m in self.models.items():
            m.fit(X_tr, y_tr)
            self.model_scores[name] = accuracy_score(y_te, m.predict(X_te))

    def score_recipes(self, user_profile: dict, recipes: pd.DataFrame) -> pd.Series:
        """
        Score each recipe individually.
        Recipe-level categoricals (Cuisine, Diet_Type) come from the recipe row.
        User-level categoricals (Dietary_Restriction, Gender, etc.) come from the user profile.
        """
        if recipes.empty:
            return pd.Series(dtype=float)

        # Which categoricals belong to the recipe vs the user
        RECIPE_CATS = {'Diet_Type', 'Cuisine', 'Recipe_Diet'}
        USER_CATS   = {'Gender', 'Health_Condition', 'Dietary_Restriction',
                       'Preferred_Cuisine', 'Taste_Preference'}

        rows = []
        for _, recipe in recipes.iterrows():
            row = {}
            # 1. Numeric features — take from recipe if present, else user profile, else mean
            for col in self.feature_cols:
                if col.endswith('_enc'):
                    continue
                if col in recipe.index:
                    row[col] = recipe[col]
                elif col in user_profile:
                    row[col] = user_profile[col]
                else:
                    row[col] = self.df[col].mean() if col in self.df.columns else 0

            # 2. Encoded categoricals — recipe-level from recipe, user-level from profile
            for orig, le in self.encoders.items():
                enc_col = f'{orig}_enc'
                if enc_col not in self.feature_cols:
                    continue
                if orig in RECIPE_CATS and orig in recipe.index:
                    val = str(recipe[orig])
                elif orig in USER_CATS and orig in user_profile:
                    val = str(user_profile[orig])
                else:
                    val = ''
                row[enc_col] = le.transform([val])[0] if val in le.classes_ else 0

            rows.append(row)

        X = pd.DataFrame(rows)[self.feature_cols].fillna(0)
        X_scaled = self.scaler.transform(X)

        total_w = sum(self.model_scores.values())
        probs = np.zeros(len(rows))
        for name, m in self.models.items():
            w = self.model_scores[name] / total_w
            probs += w * m.predict_proba(X_scaled)[:, 1]

        return pd.Series(probs, index=recipes.index)


@st.cache_resource
def get_recommender():
    """Train once and cache for the entire session."""
    df = load_data()
    return FoodRecommender(df)

# ============================================================================
# COLLABORATIVE FILTERING
# ============================================================================

def collaborative_recommendations(user_ratings: dict, pivot, df: pd.DataFrame, n: int = 8) -> pd.DataFrame:
    """
    Find users in the feedback matrix similar to this user (by cosine similarity
    on their shared recipe ratings), then recommend their top-rated recipes.
    """
    if pivot is None or not user_ratings:
        return pd.DataFrame()

    if 'Recipe_ID' not in df.columns or 'Recipe_Name' not in df.columns:
        return pd.DataFrame()

    name_to_id = df.drop_duplicates('Recipe_Name').set_index('Recipe_Name')['Recipe_ID']

    # Build a vector for the current user aligned to pivot columns
    user_vec = np.zeros(len(pivot.columns))
    for recipe_name, rating in user_ratings.items():
        if recipe_name in name_to_id.index:
            rid = name_to_id[recipe_name]
            if rid in pivot.columns:
                user_vec[pivot.columns.get_loc(rid)] = rating

    if user_vec.sum() == 0:
        return pd.DataFrame()

    sims = cosine_similarity([user_vec], pivot.values)[0]
    top_idx = np.argsort(sims)[::-1][:5]  # 5 most similar users

    already_rated = {name_to_id[r] for r in user_ratings if r in name_to_id.index}
    candidate_scores: dict = {}
    for idx in top_idx:
        sim = sims[idx]
        for rid, rating in pivot.iloc[idx].items():
            if rating >= 4 and rid not in already_rated:
                candidate_scores[rid] = candidate_scores.get(rid, 0) + sim * rating

    if not candidate_scores:
        return pd.DataFrame()

    top_ids = sorted(candidate_scores, key=candidate_scores.get, reverse=True)[:n]
    result = df[df['Recipe_ID'].isin(top_ids)].drop_duplicates('Recipe_Name').copy()
    result['Collab_Score'] = result['Recipe_ID'].map(candidate_scores)
    return result.sort_values('Collab_Score', ascending=False)

# ============================================================================
# AUTH SIDEBAR
# ============================================================================

def auth_sidebar() -> dict | None:
    """Render login/register in sidebar. Returns logged-in user dict or None."""
    if st.session_state.get('user'):
        user = st.session_state.user
        st.sidebar.success(f"Logged in as **{user['username']}**")
        if st.sidebar.button("Logout"):
            st.session_state.user = None
            st.rerun()
        return user

    st.sidebar.markdown("### Account")
    tab = st.sidebar.radio("", ["Login", "Register"], horizontal=True, label_visibility="collapsed")

    if tab == "Login":
        uname = st.sidebar.text_input("Username", key="li_u")
        pwd   = st.sidebar.text_input("Password", type="password", key="li_p")
        if st.sidebar.button("Login", use_container_width=True):
            user = authenticate_user(uname, pwd)
            if user:
                st.session_state.user = user
                st.rerun()
            else:
                st.sidebar.error("Invalid username or password")
    else:
        uname   = st.sidebar.text_input("Username", key="rg_u")
        pwd     = st.sidebar.text_input("Password", type="password", key="rg_p")
        age     = st.sidebar.slider("Age", 18, 80, 25, key="rg_age")
        gender  = st.sidebar.selectbox("Gender", ["Male", "Female", "Other"], key="rg_g")
        dietary = st.sidebar.selectbox("Diet", ["Vegetarian", "Non-Vegetarian", "Vegan", "Keto"], key="rg_d")
        cuisine = st.sidebar.selectbox("Cuisine", ["Indian", "Italian", "Asian", "Mediterranean", "Mexican", "American"], key="rg_c")
        if st.sidebar.button("Register", use_container_width=True):
            if uname and pwd:
                ok = register_user(uname, pwd, {
                    'age': age, 'gender': gender, 'bmi': 22.0,
                    'health_condition': 'None', 'dietary_restriction': dietary,
                    'preferred_cuisine': cuisine, 'taste_preference': 'Mild'
                })
                if ok:
                    st.session_state.user = authenticate_user(uname, pwd)
                    st.rerun()
                else:
                    st.sidebar.error("Username already taken")
            else:
                st.sidebar.warning("Fill in all fields")
    return None

# ============================================================================
# UI COMPONENTS
# ============================================================================

def create_header():
    st.markdown("""
    <div class="main-header fade-in-up">
        <h1>🍽️ AI Food Genius</h1>
        <p>Personalized AI-powered food recommendations</p>
    </div>
    """, unsafe_allow_html=True)

def metric_card(title: str, value, icon: str = "📊"):
    st.markdown(f"""
    <div class="metric-card fade-in-up">
        <div style="font-size:2rem;margin-bottom:.5rem">{icon}</div>
        <div class="metric-value">{value}</div>
        <div class="metric-label">{title}</div>
    </div>
    """, unsafe_allow_html=True)

def recipe_card(recipe, index: int, user: dict | None, favorites: set):
    name = recipe.get('Recipe_Name', 'Unknown')
    diet_label  = recipe.get('Recipe_Diet') or recipe.get('Diet_Type') or 'N/A'
    taste_label = recipe.get('Taste') or recipe.get('Taste_Preference') or 'N/A'
    st.markdown(f"""
    <div class="recipe-card fade-in-up">
        <div class="recipe-title">🥘 {name}</div>
        <div class="recipe-meta">
            <span class="meta-item">🍽️ {recipe.get('Cuisine','General')}</span>
            <span class="meta-item">⏱️ {recipe.get('Cooking_Time','N/A')} mins</span>
            <span class="meta-item">🔥 {recipe.get('Calories',0):.0f} cal</span>
            <span class="meta-item">🥗 {diet_label}</span>
            <span class="meta-item">😋 {taste_label}</span>
            <span class="meta-item">⭐ {recipe.get('User_Rating',0):.1f}/5</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("💪 Protein",     f"{recipe.get('Protein_g',0):.1f}g")
    with c2: st.metric("🧠 AI Score",    f"{recipe.get('AI_Score',0):.2f}")
    with c3: st.metric("🌱 Health Score",f"{recipe.get('Health_Score',0):.2f}")
    with c4:
        if user:
            is_fav = name in favorites
            label  = "❤️ Saved" if is_fav else "🤍 Save"
            if st.button(label, key=f"fav_{index}"):
                if is_fav:
                    remove_favorite(user['username'], name)
                else:
                    add_favorite(user['username'], name)
                st.rerun()
        else:
            st.info("Login to save")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.write(f"🥩 Protein: {recipe.get('Protein_g',0):.1f}g")
        st.write(f"🍞 Carbs:   {recipe.get('Carbs_g',0):.1f}g")
    with c2:
        st.write(f"🧈 Fat:     {recipe.get('Fat_g',0):.1f}g")
        st.write(f"🌾 Fiber:   {recipe.get('Fiber_g',0):.1f}g")
    with c3:
        st.write(f"🍊 Vit C:  {recipe.get('Vitamin_C_mg',0):.1f}mg")
        st.write(f"⚡ Iron:   {recipe.get('Iron_mg',0):.1f}mg")

    if user:
        with st.expander("Rate this recipe"):
            rating = st.slider("Your rating", 1, 5, 3, key=f"rate_{index}")
            if st.button("Submit", key=f"submit_{index}"):
                save_rating(user['username'], name, rating)
                st.success("Rating saved — it will improve your future recommendations!")

    st.divider()

# ============================================================================
# PAGES
# ============================================================================

def page_home(df: pd.DataFrame, rec: FoodRecommender):
    c1, c2, c3, c4 = st.columns(4)
    with c1: metric_card("Total Recipes", len(df['Recipe_Name'].unique()), "🍽️")
    with c2: metric_card("AI Accuracy",   f"{max(rec.model_scores.values())*100:.1f}%", "🤖")
    with c3: metric_card("Active Users",  len(df['User_ID'].unique()), "👥")
    with c4: metric_card("Avg Rating",    f"{df['User_Rating'].mean():.1f}/5", "⭐")

    st.markdown("---")
    st.markdown("## 🔥 Trending Recipes")
    user = st.session_state.get('user')
    favs = get_favorites(user['username']) if user else set()
    for i, (_, row) in enumerate(df.nlargest(5, 'Trending_Score').iterrows()):
        recipe_card(row, i, user, favs)


def page_recommendations(df: pd.DataFrame, rec: FoodRecommender):
    st.markdown("## 🤖 AI Recommendations")

    user = st.session_state.get('user')

    # Pre-fill from saved profile if logged in
    defaults = user if user else {}

    c1, c2 = st.columns(2)
    with c1:
        age     = st.slider("Age", 18, 80, int(defaults.get('age', 30)))
        gender  = st.selectbox("Gender", ["Male","Female","Other"],
                               index=["Male","Female","Other"].index(defaults.get('gender','Male')) if defaults.get('gender') in ["Male","Female","Other"] else 0)
        bmi     = st.slider("BMI", 15.0, 40.0, float(defaults.get('bmi', 22.0)))
        health  = st.selectbox("Health Condition",
                               ["None","Diabetes","Iron Deficiency","Vitamin D Deficiency","High Blood Pressure"],
                               index=["None","Diabetes","Iron Deficiency","Vitamin D Deficiency","High Blood Pressure"].index(defaults.get('health_condition','None')) if defaults.get('health_condition') in ["None","Diabetes","Iron Deficiency","Vitamin D Deficiency","High Blood Pressure"] else 0)
    with c2:
        dietary = st.selectbox("Dietary Restriction",
                               ["Vegetarian","Non-Vegetarian","Vegan","Keto","Paleo"],
                               index=["Vegetarian","Non-Vegetarian","Vegan","Keto","Paleo"].index(defaults.get('dietary_restriction','Vegetarian')) if defaults.get('dietary_restriction') in ["Vegetarian","Non-Vegetarian","Vegan","Keto","Paleo"] else 0)
        cuisine = st.selectbox("Preferred Cuisine",
                               ["Indian","Italian","Asian","Mediterranean","Mexican","American"],
                               index=["Indian","Italian","Asian","Mediterranean","Mexican","American"].index(defaults.get('preferred_cuisine','Indian')) if defaults.get('preferred_cuisine') in ["Indian","Italian","Asian","Mediterranean","Mexican","American"] else 0)
        taste   = st.selectbox("Taste Preference", ["Spicy","Sweet","Mild","Savory","Tangy"],
                               index=["Spicy","Sweet","Mild","Savory","Tangy"].index(defaults.get('taste_preference','Mild')) if defaults.get('taste_preference') in ["Spicy","Sweet","Mild","Savory","Tangy"] else 2)
        max_time = st.slider("Max Cooking Time (min)", 10, 120, 45)

    if st.button("🎯 Get Recommendations", type="primary", use_container_width=True):
        user_profile = {
            'Age': age, 'BMI': bmi, 'Gender': gender,
            'Health_Condition': health, 'Dietary_Restriction': dietary,
            'Preferred_Cuisine': cuisine, 'Taste_Preference': taste,
        }

        with st.spinner("AI is scoring recipes for you..."):
            filtered = df[df['Cooking_Time'] <= max_time].copy()

            # Hard-filter on recipe's own diet type (Recipe_Diet comes from h1.py, not the user column)
            diet_col = 'Recipe_Diet' if 'Recipe_Diet' in filtered.columns else 'Diet_Type'
            exact = filtered[
                (filtered[diet_col]  == dietary) &
                (filtered['Cuisine'] == cuisine)
            ].drop_duplicates('Recipe_Name')

            # Fall back: diet-only → unrestricted, so we always show something
            if len(exact) < 5:
                exact = filtered[filtered[diet_col] == dietary].drop_duplicates('Recipe_Name')
            subset = (exact if len(exact) >= 5 else filtered.drop_duplicates('Recipe_Name')).copy()

            # ── Multi-component scoring ──────────────────────────────────────
            # ML model gives a base probability per recipe
            ml_prob = rec.score_recipes(user_profile, subset)

            # Taste match: exact match gets +0.25 bonus
            taste_col = 'Taste' if 'Taste' in subset.columns else 'Taste_Preference'
            taste_match = (subset[taste_col] == taste).astype(float) * 0.25 if taste_col in subset.columns else 0.0

            # Health-condition bonus — nudge nutritionally relevant recipes higher
            def health_bonus(row):
                h = health
                if h == 'Diabetes':
                    # Low carb + high fiber is best for diabetes
                    return 0.1 * (1 - row['Carbs_g'] / 70) + 0.1 * (row['Fiber_g'] / 15)
                elif h == 'Iron Deficiency':
                    return 0.2 * min(row['Iron_mg'] / 8, 1.0)
                elif h == 'Vitamin D Deficiency':
                    # Non-veg foods (fish, egg) have more Vit D — approximate via protein
                    return 0.15 * min(row['Protein_g'] / 40, 1.0)
                elif h == 'High Blood Pressure':
                    # Low fat + high fiber
                    return 0.1 * (1 - row['Fat_g'] / 35) + 0.1 * (row['Fiber_g'] / 15)
                return 0.0

            health_scores = subset.apply(health_bonus, axis=1)

            # Nutrition quality: normalised nutrient score
            nutr = subset['Nutrient_Score'] if 'Nutrient_Score' in subset.columns else pd.Series(0.7, index=subset.index)

            # Combine: 40% ML + 25% taste + 20% health + 15% nutrition
            raw_score = 0.40 * ml_prob + 0.25 * taste_match + 0.20 * health_scores + 0.15 * nutr

            # Rescale within subset so top/bottom are clearly differentiated
            s_min, s_max = raw_score.min(), raw_score.max()
            if s_max - s_min > 0.001:
                subset['AI_Score'] = (raw_score - s_min) / (s_max - s_min)
            else:
                subset['AI_Score'] = raw_score

            top = subset.nlargest(10, 'AI_Score')

        st.markdown("### Your Personalized Recommendations")
        favs = get_favorites(user['username']) if user else set()
        for i, (_, row) in enumerate(top.iterrows()):
            recipe_card(row, 100 + i, user, favs)

        # Collaborative filtering section (only if user has rated recipes)
        if user:
            user_ratings = get_user_ratings(user['username'])
            if user_ratings:
                pivot = load_feedback_pivot()
                collab = collaborative_recommendations(user_ratings, pivot, df)
                if not collab.empty:
                    st.markdown("### 🤝 Based on Users Like You")
                    collab['AI_Score'] = collab.get('Collab_Score', 0) / 25.0
                    for i, (_, row) in enumerate(collab.iterrows()):
                        recipe_card(row, 200 + i, user, favs)
            else:
                st.info("Rate some recipes to unlock collaborative recommendations from similar users.")


def page_analytics(df: pd.DataFrame, rec: FoodRecommender):
    st.markdown("## 📊 Analytics & Insights")

    st.markdown("### 🤖 Model Performance")
    model_df = pd.DataFrame(rec.model_scores.items(), columns=['Model', 'Accuracy'])
    model_df['Accuracy'] *= 100
    fig = px.bar(model_df, x='Model', y='Accuracy', color='Accuracy',
                 color_continuous_scale='Viridis', title="Model Accuracy (%)")
    st.plotly_chart(fig, use_container_width=True)

    c1, c2 = st.columns(2)
    with c1:
        fig = px.histogram(df, x='Calories', nbins=30, title="Calorie Distribution")
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        macro = df[['Protein_g','Carbs_g','Fat_g']].mean()
        fig = px.pie(values=macro.values, names=macro.index, title="Avg Macronutrient Split")
        st.plotly_chart(fig, use_container_width=True)

    c1, c2 = st.columns(2)
    with c1:
        cuisine_counts = df['Cuisine'].value_counts()
        fig = px.pie(values=cuisine_counts.values, names=cuisine_counts.index, title="Recipes by Cuisine")
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        diet_counts = df['Diet_Type'].value_counts()
        fig = px.bar(x=diet_counts.index, y=diet_counts.values, title="Veg vs Non-Veg")
        st.plotly_chart(fig, use_container_width=True)


def page_profile(df: pd.DataFrame):
    st.markdown("## 👤 Profile")
    user = st.session_state.get('user')

    if not user:
        st.warning("Please log in to view and edit your profile.")
        return

    st.markdown(f"### Welcome, **{user['username']}**")

    with st.form("profile_form"):
        c1, c2 = st.columns(2)
        with c1:
            age     = st.slider("Age", 18, 80, int(user.get('age', 25)))
            gender  = st.selectbox("Gender", ["Male","Female","Other"],
                                   index=["Male","Female","Other"].index(user.get('gender','Other')) if user.get('gender') in ["Male","Female","Other"] else 2)
            bmi     = st.slider("BMI", 15.0, 40.0, float(user.get('bmi', 22.0)))
            health  = st.selectbox("Health Condition",
                                   ["None","Diabetes","Iron Deficiency","Vitamin D Deficiency","High Blood Pressure"],
                                   index=["None","Diabetes","Iron Deficiency","Vitamin D Deficiency","High Blood Pressure"].index(user.get('health_condition','None')) if user.get('health_condition') in ["None","Diabetes","Iron Deficiency","Vitamin D Deficiency","High Blood Pressure"] else 0)
        with c2:
            dietary = st.selectbox("Dietary Restriction",
                                   ["Vegetarian","Non-Vegetarian","Vegan","Keto","Paleo"],
                                   index=["Vegetarian","Non-Vegetarian","Vegan","Keto","Paleo"].index(user.get('dietary_restriction','Vegetarian')) if user.get('dietary_restriction') in ["Vegetarian","Non-Vegetarian","Vegan","Keto","Paleo"] else 0)
            cuisine = st.selectbox("Preferred Cuisine",
                                   ["Indian","Italian","Asian","Mediterranean","Mexican","American"],
                                   index=["Indian","Italian","Asian","Mediterranean","Mexican","American"].index(user.get('preferred_cuisine','Indian')) if user.get('preferred_cuisine') in ["Indian","Italian","Asian","Mediterranean","Mexican","American"] else 0)
            taste   = st.selectbox("Taste Preference", ["Spicy","Sweet","Mild","Savory","Tangy"],
                                   index=["Spicy","Sweet","Mild","Savory","Tangy"].index(user.get('taste_preference','Mild')) if user.get('taste_preference') in ["Spicy","Sweet","Mild","Savory","Tangy"] else 2)

        if st.form_submit_button("Save Profile", use_container_width=True):
            update_profile(user['username'], {
                'age': age, 'gender': gender, 'bmi': bmi,
                'health_condition': health, 'dietary_restriction': dietary,
                'preferred_cuisine': cuisine, 'taste_preference': taste
            })
            st.success("Profile saved!")

    # Favorites
    st.markdown("### ❤️ Saved Recipes")
    favs = get_favorites(user['username'])
    if favs:
        fav_df = df[df['Recipe_Name'].isin(favs)].drop_duplicates('Recipe_Name')
        if not fav_df.empty:
            for i, (_, row) in enumerate(fav_df.iterrows()):
                recipe_card(row, 300 + i, user, favs)
        else:
            st.info("Your saved recipes aren't in the current dataset.")
    else:
        st.info("No saved recipes yet. Hit the 🤍 Save button on any recipe!")

    # Ratings history
    st.markdown("### ⭐ Your Ratings")
    ratings = get_user_ratings(user['username'])
    if ratings:
        ratings_df = pd.DataFrame(ratings.items(), columns=['Recipe', 'Rating'])
        st.dataframe(ratings_df, use_container_width=True)
    else:
        st.info("You haven't rated any recipes yet.")


def page_favorites(df: pd.DataFrame):
    st.markdown("## ❤️ Favourites")
    user = st.session_state.get('user')
    if not user:
        st.warning("Log in to see your saved recipes.")
        return
    favs = get_favorites(user['username'])
    if not favs:
        st.info("No saved recipes yet.")
        return
    fav_df = df[df['Recipe_Name'].isin(favs)].drop_duplicates('Recipe_Name')
    for i, (_, row) in enumerate(fav_df.iterrows()):
        recipe_card(row, 400 + i, user, favs)

# ============================================================================
# MAIN
# ============================================================================

def main():
    create_header()

    user = auth_sidebar()

    with st.spinner("Loading AI models..."):
        df  = load_data()
        rec = get_recommender()

    page = st.sidebar.selectbox(
        "Navigate",
        ["🏠 Home", "🤖 AI Recommendations", "📊 Analytics", "👤 Profile", "❤️ Favourites"]
    )

    if   page == "🏠 Home":               page_home(df, rec)
    elif page == "🤖 AI Recommendations": page_recommendations(df, rec)
    elif page == "📊 Analytics":          page_analytics(df, rec)
    elif page == "👤 Profile":            page_profile(df)
    elif page == "❤️ Favourites":         page_favorites(df)


if __name__ == "__main__":
    main()
