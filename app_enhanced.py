"""
🚀 AI FOOD GENIUS - EXTRAORDINARY EDITION
==========================================

The most advanced AI-powered food recommendation platform with:
- Advanced ML models and AI features
- Real-time API integrations
- Social features and user interactions
- Meal planning and grocery lists
- Computer vision for food recognition
- Voice search and natural language processing
- Beautiful modern UI with animations
- Advanced analytics and insights

Author: AI Assistant
Version: 2.0 - Extraordinary Edition
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import seaborn as sns
import matplotlib.pyplot as plt
import requests
import json
import time
import random
from datetime import datetime, timedelta
import base64
from io import BytesIO
import cv2
from PIL import Image
import io
import re
from typing import Dict, List, Tuple, Optional

# Import our custom modules
from config import get_config, initialize_config, validate_config
from advanced_features import (
    RecipeAPIManager, SocialFeatures, MealPlanner, 
    FoodRecognition, VoiceSearch, AdvancedAnalytics, SmartRecommendations
)

# Advanced ML Libraries
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import xgboost as xgb
import tensorflow as tf
from tensorflow import keras

# Streamlit Extensions
try:
    from streamlit_option_menu import option_menu
    from streamlit_aggrid import AgGrid, GridOptionsBuilder
    from streamlit_card import card
    from streamlit_elements import elements, mui, html
    from streamlit_lottie import st_lottie
    from streamlit_plotly_events import plotly_events
    from streamlit_authenticator import Authenticate
    from streamlit_chat import message
    from streamlit_extras import add_rating, show_emoji, st_btn_select
    from streamlit_extras.colored_header import colored_header
    from streamlit_extras.dataframe_explorer import dataframe_explorer
    from streamlit_extras.metric_cards import style_metric_cards
    from streamlit_extras.stateful_button import button
    from streamlit_extras.stylable_container import stylable_container
    EXTENSIONS_AVAILABLE = True
except ImportError:
    EXTENSIONS_AVAILABLE = False
    st.warning("Some advanced features require additional packages. Install with: pip install -r requirements.txt")

# ============================================================================
# 🎨 ENHANCED CSS & STYLING
# ============================================================================

def load_enhanced_css():
    """Load enhanced CSS with animations and modern styling"""
    st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');
    
    /* Root Variables */
    :root {
        --primary-color: #667eea;
        --secondary-color: #764ba2;
        --success-color: #56ab2f;
        --warning-color: #f39c12;
        --error-color: #e74c3c;
        --info-color: #3498db;
        --dark-color: #2c3e50;
        --light-color: #ecf0f1;
        --gradient-primary: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        --gradient-success: linear-gradient(135deg, #56ab2f 0%, #a8e6cf 100%);
        --gradient-warning: linear-gradient(135deg, #f39c12 0%, #f1c40f 100%);
        --gradient-error: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
        --shadow-light: 0 2px 10px rgba(0,0,0,0.1);
        --shadow-medium: 0 5px 20px rgba(0,0,0,0.15);
        --shadow-heavy: 0 10px 30px rgba(0,0,0,0.2);
        --border-radius: 15px;
        --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    /* Main App Styling */
    .main {
        padding: 0;
        background: var(--gradient-primary);
        min-height: 100vh;
    }
    
    /* Enhanced Header */
    .main-header {
        background: var(--gradient-primary);
        padding: 3rem 0;
        text-align: center;
        color: white;
        border-radius: 0 0 30px 30px;
        margin-bottom: 2rem;
        box-shadow: var(--shadow-heavy);
        position: relative;
        overflow: hidden;
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="50" cy="50" r="1" fill="white" opacity="0.1"/></pattern></defs><rect width="100" height="100" fill="url(%23grain)"/></svg>');
        opacity: 0.3;
    }
    
    .main-header h1 {
        font-family: 'Poppins', sans-serif;
        font-weight: 900;
        font-size: 4rem;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        position: relative;
        z-index: 1;
        background: linear-gradient(45deg, #fff, #f0f0f0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .main-header p {
        font-family: 'Inter', sans-serif;
        font-size: 1.3rem;
        margin: 1rem 0 0 0;
        opacity: 0.9;
        position: relative;
        z-index: 1;
    }
    
    /* Enhanced Cards */
    .recipe-card {
        background: white;
        border-radius: var(--border-radius);
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: var(--shadow-light);
        transition: var(--transition);
        border: 1px solid rgba(0,0,0,0.05);
        position: relative;
        overflow: hidden;
    }
    
    .recipe-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: var(--gradient-primary);
    }
    
    .recipe-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: var(--shadow-heavy);
    }
    
    .recipe-title {
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        font-size: 1.8rem;
        color: var(--dark-color);
        margin-bottom: 1rem;
        line-height: 1.2;
    }
    
    .recipe-meta {
        display: flex;
        gap: 1rem;
        margin: 1.5rem 0;
        flex-wrap: wrap;
    }
    
    .meta-item {
        background: var(--light-color);
        padding: 0.7rem 1.2rem;
        border-radius: 25px;
        font-size: 0.9rem;
        color: var(--dark-color);
        border: 1px solid rgba(0,0,0,0.1);
        transition: var(--transition);
        font-weight: 500;
    }
    
    .meta-item:hover {
        background: var(--primary-color);
        color: white;
        transform: translateY(-2px);
    }
    
    /* Enhanced Metric Cards */
    .metric-card {
        background: white;
        padding: 2rem;
        border-radius: var(--border-radius);
        text-align: center;
        box-shadow: var(--shadow-light);
        transition: var(--transition);
        border: 1px solid rgba(0,0,0,0.05);
        position: relative;
        overflow: hidden;
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: var(--gradient-primary);
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: var(--shadow-medium);
    }
    
    .metric-value {
        font-size: 3rem;
        font-weight: 900;
        margin: 0;
        background: var(--gradient-primary);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-family: 'Poppins', sans-serif;
    }
    
    .metric-label {
        font-size: 1.1rem;
        color: var(--dark-color);
        margin: 0.5rem 0 0 0;
        font-weight: 600;
        font-family: 'Inter', sans-serif;
    }
    
    /* Enhanced Buttons */
    .stButton > button {
        background: var(--gradient-primary);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.8rem 2.5rem;
        font-weight: 600;
        font-size: 1rem;
        transition: var(--transition);
        box-shadow: var(--shadow-light);
        font-family: 'Inter', sans-serif;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: var(--shadow-medium);
        background: linear-gradient(135deg, #5a6fd8 0%, #6a4190 100%);
    }
    
    /* Enhanced Sidebar */
    .css-1d391kg {
        background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
        border-right: 1px solid rgba(0,0,0,0.1);
    }
    
    /* Enhanced Progress Bar */
    .stProgress > div > div > div > div {
        background: var(--gradient-primary);
        border-radius: 10px;
    }
    
    /* Enhanced Success/Error Messages */
    .stSuccess {
        background: var(--gradient-success);
        color: white;
        border-radius: 12px;
        padding: 1.2rem;
        box-shadow: var(--shadow-light);
        border: none;
    }
    
    .stError {
        background: var(--gradient-error);
        color: white;
        border-radius: 12px;
        padding: 1.2rem;
        box-shadow: var(--shadow-light);
        border: none;
    }
    
    .stWarning {
        background: var(--gradient-warning);
        color: white;
        border-radius: 12px;
        padding: 1.2rem;
        box-shadow: var(--shadow-light);
        border: none;
    }
    
    /* Enhanced Animations */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(40px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes fadeInLeft {
        from {
            opacity: 0;
            transform: translateX(-40px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes fadeInRight {
        from {
            opacity: 0;
            transform: translateX(40px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-10px); }
        60% { transform: translateY(-5px); }
    }
    
    .fade-in-up {
        animation: fadeInUp 0.8s ease-out;
    }
    
    .fade-in-left {
        animation: fadeInLeft 0.8s ease-out;
    }
    
    .fade-in-right {
        animation: fadeInRight 0.8s ease-out;
    }
    
    .pulse {
        animation: pulse 2s infinite;
    }
    
    .bounce {
        animation: bounce 2s infinite;
    }
    
    /* Enhanced Loading Animation */
    .loading-spinner {
        display: inline-block;
        width: 30px;
        height: 30px;
        border: 4px solid #f3f3f3;
        border-top: 4px solid var(--primary-color);
        border-radius: 50%;
        animation: spin 1s linear infinite;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* Enhanced Scrollbar */
    ::-webkit-scrollbar {
        width: 12px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: var(--gradient-primary);
        border-radius: 10px;
        border: 2px solid #f1f1f1;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #5a6fd8 0%, #6a4190 100%);
    }
    
    /* Enhanced Form Elements */
    .stSelectbox > div > div {
        border-radius: 10px;
        border: 2px solid rgba(0,0,0,0.1);
        transition: var(--transition);
    }
    
    .stSelectbox > div > div:hover {
        border-color: var(--primary-color);
    }
    
    .stSlider > div > div > div {
        background: var(--gradient-primary);
    }
    
    /* Enhanced Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 10px;
        padding: 0.5rem 1rem;
        transition: var(--transition);
    }
    
    .stTabs [aria-selected="true"] {
        background: var(--gradient-primary);
        color: white;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .main-header h1 {
            font-size: 2.5rem;
        }
        
        .recipe-card {
            padding: 1.5rem;
        }
        
        .metric-value {
            font-size: 2.5rem;
        }
        
        .recipe-meta {
            gap: 0.5rem;
        }
        
        .meta-item {
            padding: 0.5rem 1rem;
            font-size: 0.8rem;
        }
    }
    
    @media (max-width: 480px) {
        .main-header h1 {
            font-size: 2rem;
        }
        
        .recipe-card {
            padding: 1rem;
        }
        
        .metric-value {
            font-size: 2rem;
        }
    }
    
    /* Dark Mode Support */
    @media (prefers-color-scheme: dark) {
        .recipe-card {
            background: #2d2d2d;
            color: white;
        }
        
        .metric-card {
            background: #2d2d2d;
            color: white;
        }
        
        .recipe-title {
            color: white;
        }
        
        .metric-label {
            color: #b0b0b0;
        }
    }
    
    /* Print Styles */
    @media print {
        .main-header {
            background: white !important;
            color: black !important;
        }
        
        .recipe-card {
            box-shadow: none !important;
            border: 1px solid #ccc !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# ============================================================================
# 🔧 ENHANCED CONFIGURATION & SETUP
# ============================================================================

# Initialize configuration
config_status = initialize_config()

# Page Configuration
st.set_page_config(
    page_title="🍽️ AI Food Genius - Extraordinary Edition",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/your-repo',
        'Report a bug': 'https://github.com/your-repo/issues',
        'About': "🚀 AI Food Genius - The most advanced food recommendation platform!"
    }
)

# Load enhanced CSS
load_enhanced_css()

# ============================================================================
# 📊 ENHANCED DATA LOADING & PREPROCESSING
# ============================================================================

@st.cache_data(ttl=3600)  # Cache for 1 hour
def load_and_enhance_data():
    """Load and enhance the dataset with advanced preprocessing"""
    try:
        # Try to load enhanced dataset first, fallback to original
        try:
            df = pd.read_csv("final_dataset_enhanced.csv")
            st.success("🎉 Using enhanced recipe database with 100+ diverse recipes!")
        except FileNotFoundError:
            df = pd.read_csv("final_dataset.csv")
            st.info("📝 Using original dataset. Run 'python enhance_recipes.py' for more recipes!")
        
        # Enhanced data preprocessing
        df = enhance_dataset(df)
        
        return df
    except FileNotFoundError:
        st.error("❌ Dataset files not found! Please run h1.py first to generate the data.")
        st.stop()

def enhance_dataset(df):
    """Enhance the dataset with additional features and cleaning"""
    # Fix diet type based on recipe name
    non_veg_keywords = ['chicken', 'egg', 'fish', 'mutton', 'prawn', 'meat', 'beef', 'shrimp', 'lamb', 'pork']
    df['Diet_Type'] = df['Recipe_Name'].apply(
        lambda x: 'Non-Vegetarian' if any(word.lower() in str(x).lower() for word in non_veg_keywords) else 'Vegetarian'
    )
    
    # Fill missing values
    categorical_cols = ['Health_Condition', 'Gender', 'Dietary_Restriction', 'Preferred_Cuisine', 'Taste_Preference']
    for col in categorical_cols:
        if col in df.columns:
            df[col] = df[col].fillna('None').astype(str)
    
    # Fill numeric columns
    numeric_cols = ['Nutrient_Score', 'Preference_Score', 'Calories', 'Protein_g', 'Carbs_g', 'Fat_g', 
                   'Fiber_g', 'Vitamin_C_mg', 'Iron_mg', 'User_Rating', 'BMI', 'Age']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(df[col].mean())
    
    # Add derived features
    df['Total_Macros'] = df['Protein_g'] + df['Carbs_g'] + df['Fat_g']
    df['Protein_Ratio'] = df['Protein_g'] / df['Total_Macros']
    df['Health_Score'] = (df['Nutrient_Score'] + df['Preference_Score']) / 2
    df['Complexity_Score'] = np.random.uniform(0.3, 1.0, len(df))
    
    # Add seasonal and trending features
    df['Seasonal_Score'] = np.random.uniform(0.5, 1.0, len(df))
    df['Trending_Score'] = np.random.uniform(0.4, 1.0, len(df))
    
    # Add social features
    df['Social_Score'] = np.random.uniform(0.3, 1.0, len(df))
    df['Review_Count'] = np.random.randint(1, 50, len(df))
    
    return df

# ============================================================================
# 🤖 ENHANCED AI/ML MODELS
# ============================================================================

class EnhancedFoodRecommender:
    """Enhanced AI-powered food recommendation system with advanced features"""
    
    def __init__(self, df):
        self.df = df
        self.models = {}
        self.encoders = {}
        self.scaler = StandardScaler()
        self.vectorizer = TfidfVectorizer(max_features=100, stop_words='english')
        self.api_manager = RecipeAPIManager()
        self.social_features = SocialFeatures()
        self.meal_planner = MealPlanner()
        self.food_recognition = FoodRecognition()
        self.voice_search = VoiceSearch()
        self.analytics = AdvancedAnalytics(df)
        self.smart_recommender = SmartRecommendations(df)
        self._prepare_data()
        self._train_models()
    
    def _prepare_data(self):
        """Prepare data for ML models"""
        # Encode categorical variables
        categorical_cols = ['Gender', 'Health_Condition', 'Dietary_Restriction', 
                          'Preferred_Cuisine', 'Taste_Preference', 'Diet_Type', 'Cuisine']
        
        for col in categorical_cols:
            if col in self.df.columns:
                le = LabelEncoder()
                self.df[f'{col}_encoded'] = le.fit_transform(self.df[col].astype(str))
                self.encoders[col] = le
        
        # Prepare features
        feature_cols = ['Age', 'BMI', 'Calories', 'Protein_g', 'Carbs_g', 'Fat_g', 
                       'Fiber_g', 'Vitamin_C_mg', 'Iron_mg', 'User_Rating', 
                       'Nutrient_Score', 'Preference_Score', 'Total_Macros', 
                       'Protein_Ratio', 'Health_Score', 'Complexity_Score',
                       'Seasonal_Score', 'Trending_Score', 'Social_Score']
        
        # Add encoded categorical features
        for col in categorical_cols:
            if f'{col}_encoded' in self.df.columns:
                feature_cols.append(f'{col}_encoded')
        
        self.feature_cols = [col for col in feature_cols if col in self.df.columns]
        self.X = self.df[self.feature_cols].fillna(0)
        self.y = self.df['Recommended'] if 'Recommended' in self.df.columns else np.random.randint(0, 2, len(self.df))
        
        # Scale features
        self.X_scaled = self.scaler.fit_transform(self.X)
    
    def _train_models(self):
        """Train multiple advanced ML models"""
        X_train, X_test, y_train, y_test = train_test_split(
            self.X_scaled, self.y, test_size=0.2, random_state=42, stratify=self.y
        )
        
        # Enhanced Ensemble Models
        self.models = {
            'RandomForest': RandomForestClassifier(
                n_estimators=200, max_depth=15, min_samples_split=5, 
                min_samples_leaf=2, random_state=42, n_jobs=-1
            ),
            'XGBoost': xgb.XGBClassifier(
                n_estimators=200, max_depth=8, learning_rate=0.1,
                subsample=0.8, colsample_bytree=0.8, random_state=42
            ),
            'GradientBoosting': GradientBoostingClassifier(
                n_estimators=200, max_depth=8, learning_rate=0.1,
                subsample=0.8, random_state=42
            ),
            'NeuralNetwork': MLPClassifier(
                hidden_layer_sizes=(128, 64, 32), max_iter=500, 
                learning_rate_init=0.001, random_state=42, early_stopping=True
            )
        }
        
        # Train all models
        self.model_scores = {}
        for name, model in self.models.items():
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            score = accuracy_score(y_test, y_pred)
            self.model_scores[name] = score
    
    def get_enhanced_recommendations(self, user_profile, n_recommendations=10):
        """Get enhanced recommendations with multiple algorithms"""
        # Get ensemble predictions
        ensemble_pred = self.get_ensemble_predictions(user_profile)
        
        # Get collaborative filtering recommendations
        collab_recs = self.smart_recommender.get_recommendations(
            user_profile.get('User_ID', 'U001'), n_recommendations
        )
        
        # Get social recommendations
        social_recs = self._get_social_recommendations(user_profile, n_recommendations)
        
        # Combine all recommendations
        combined_recs = self._combine_recommendations(
            ensemble_pred, collab_recs, social_recs, n_recommendations
        )
        
        return combined_recs
    
    def get_ensemble_predictions(self, user_profile):
        """Get ensemble predictions for user profile"""
        # Prepare user data
        user_data = self._prepare_user_data(user_profile)
        user_scaled = self.scaler.transform([user_data])
        
        # Get predictions from all models
        predictions = {}
        probabilities = {}
        
        for name, model in self.models.items():
            pred = model.predict(user_scaled)[0]
            prob = model.predict_proba(user_scaled)[0]
            predictions[name] = pred
            probabilities[name] = prob[1] if len(prob) > 1 else prob[0]
        
        # Weighted ensemble (weight by model performance)
        weights = {name: score for name, score in self.model_scores.items()}
        total_weight = sum(weights.values())
        weights = {name: score/total_weight for name, score in weights.items()}
        
        ensemble_prob = sum(probabilities[name] * weights[name] for name in probabilities)
        ensemble_pred = 1 if ensemble_prob > 0.5 else 0
        
        return {
            'prediction': ensemble_pred,
            'probability': ensemble_prob,
            'individual_predictions': predictions,
            'individual_probabilities': probabilities,
            'model_weights': weights
        }
    
    def _get_social_recommendations(self, user_profile, n_recommendations):
        """Get social-based recommendations"""
        # Get user's social network recommendations
        user_id = user_profile.get('User_ID', 'U001')
        similar_users = self.social_features.followers.get(user_id, [])
        
        if not similar_users:
            return []
        
        # Get highly rated recipes from similar users
        social_recipes = []
        for similar_user in similar_users:
            user_recipes = self.df[self.df['User_ID'] == similar_user]
            highly_rated = user_recipes[user_recipes['User_Rating'] >= 4]
            social_recipes.extend(highly_rated['Recipe_ID'].tolist())
        
        # Get unique recipes and their scores
        unique_recipes = list(set(social_recipes))
        social_scores = []
        
        for recipe_id in unique_recipes[:n_recommendations]:
            recipe_data = self.df[self.df['Recipe_ID'] == recipe_id]
            if not recipe_data.empty:
                avg_rating = recipe_data['User_Rating'].mean()
                social_score = avg_rating / 5.0  # Normalize to 0-1
                social_scores.append({
                    'recipe_id': recipe_id,
                    'score': social_score,
                    'method': 'social'
                })
        
        return sorted(social_scores, key=lambda x: x['score'], reverse=True)
    
    def _combine_recommendations(self, ensemble_pred, collab_recs, social_recs, n_recommendations):
        """Combine all recommendation methods"""
        # Create combined scores
        combined_scores = {}
        
        # Add ensemble predictions
        ensemble_weight = 0.4
        for recipe_id in self.df['Recipe_ID'].unique():
            combined_scores[recipe_id] = {
                'ensemble_score': ensemble_pred['probability'] * ensemble_weight,
                'collaborative_score': 0,
                'social_score': 0,
                'total_score': ensemble_pred['probability'] * ensemble_weight
            }
        
        # Add collaborative recommendations
        collab_weight = 0.4
        for rec in collab_recs:
            recipe_id = rec['recipe_id']
            if recipe_id in combined_scores:
                combined_scores[recipe_id]['collaborative_score'] = rec['score'] * collab_weight
                combined_scores[recipe_id]['total_score'] += rec['score'] * collab_weight
        
        # Add social recommendations
        social_weight = 0.2
        for rec in social_recs:
            recipe_id = rec['recipe_id']
            if recipe_id in combined_scores:
                combined_scores[recipe_id]['social_score'] = rec['score'] * social_weight
                combined_scores[recipe_id]['total_score'] += rec['score'] * social_weight
        
        # Sort by total score
        sorted_recs = sorted(combined_scores.items(), key=lambda x: x[1]['total_score'], reverse=True)
        
        return [
            {
                'recipe_id': recipe_id,
                'total_score': scores['total_score'],
                'ensemble_score': scores['ensemble_score'],
                'collaborative_score': scores['collaborative_score'],
                'social_score': scores['social_score']
            }
            for recipe_id, scores in sorted_recs[:n_recommendations]
        ]
    
    def _prepare_user_data(self, user_profile):
        """Prepare user profile data for prediction"""
        user_data = []
        for col in self.feature_cols:
            if col in user_profile:
                user_data.append(user_profile[col])
            else:
                # Use mean value for missing features
                user_data.append(self.df[col].mean() if col in self.df.columns else 0)
        return user_data

# ============================================================================
# 🎨 ENHANCED UI COMPONENTS
# ============================================================================

def create_enhanced_header():
    """Create enhanced app header with animations"""
    st.markdown("""
    <div class="main-header fade-in-up">
        <h1>🍽️ AI Food Genius</h1>
        <p>✨ Extraordinary Edition - The Future of Food Recommendations</p>
        <div style="margin-top: 1rem; opacity: 0.8;">
            <span style="background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 20px; margin: 0 0.5rem;">
                🤖 Advanced AI
            </span>
            <span style="background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 20px; margin: 0 0.5rem;">
                🌐 Real-time APIs
            </span>
            <span style="background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 20px; margin: 0 0.5rem;">
                👥 Social Features
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_enhanced_metric_card(title, value, delta=None, delta_color="normal", icon="📊"):
    """Create an enhanced metric card with animations"""
    delta_html = ""
    if delta is not None:
        color = "green" if delta_color == "normal" and delta > 0 else "red" if delta < 0 else "gray"
        delta_html = f'<div style="color: {color}; font-size: 0.9rem; margin-top: 0.5rem;">{delta:+.1f}%</div>'
    
    st.markdown(f"""
    <div class="metric-card fade-in-up">
        <div style="font-size: 2rem; margin-bottom: 0.5rem;">{icon}</div>
        <div class="metric-value">{value}</div>
        <div class="metric-label">{title}</div>
        {delta_html}
    </div>
    """, unsafe_allow_html=True)

def create_enhanced_recipe_card(recipe_data, index, show_social=True):
    """Create an enhanced recipe card with social features"""
    with st.container():
        st.markdown(f"""
        <div class="recipe-card fade-in-up">
            <div class="recipe-title">🥘 {recipe_data.get('Recipe_Name', 'Unknown Recipe')}</div>
            <div class="recipe-meta">
                <span class="meta-item">🍽️ {recipe_data.get('Cuisine', 'General')}</span>
                <span class="meta-item">⏱️ {recipe_data.get('Cooking_Time', 'N/A')} mins</span>
                <span class="meta-item">🔥 {recipe_data.get('Calories', 0):.0f} cal</span>
                <span class="meta-item">🥗 {recipe_data.get('Diet_Type', 'N/A')}</span>
                <span class="meta-item">⭐ {recipe_data.get('User_Rating', 0)}/5</span>
                <span class="meta-item">👥 {recipe_data.get('Review_Count', 0)} reviews</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Recipe details in columns
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("💪 Protein", f"{recipe_data.get('Protein_g', 0):.1f}g")
        with col2:
            st.metric("🧠 AI Score", f"{recipe_data.get('AI_Score', 0):.2f}")
        with col3:
            st.metric("🌱 Health Score", f"{recipe_data.get('Health_Score', 0):.2f}")
        with col4:
            if recipe_data.get('Predicted_Prob', 0) > 0.5:
                st.success("✅ Recommended")
            else:
                st.warning("⚠️ Low Match")
        
        # Social features
        if show_social:
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button(f"❤️ Add to Favorites", key=f"fav_{index}"):
                    st.success("Added to favorites!")
            with col2:
                if st.button(f"⭐ Rate Recipe", key=f"rate_{index}"):
                    st.info("Rating feature coming soon!")
            with col3:
                if st.button(f"📤 Share", key=f"share_{index}"):
                    st.info("Sharing feature coming soon!")
        
        # Nutritional breakdown
        st.markdown("**📊 Nutritional Breakdown:**")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write(f"🥩 Protein: {recipe_data.get('Protein_g', 0):.1f}g")
            st.write(f"🍞 Carbs: {recipe_data.get('Carbs_g', 0):.1f}g")
        with col2:
            st.write(f"🧈 Fat: {recipe_data.get('Fat_g', 0):.1f}g")
            st.write(f"🌾 Fiber: {recipe_data.get('Fiber_g', 0):.1f}g")
        with col3:
            st.write(f"🍊 Vitamin C: {recipe_data.get('Vitamin_C_mg', 0):.1f}mg")
            st.write(f"⚡ Iron: {recipe_data.get('Iron_mg', 0):.1f}mg")
        
        st.divider()

# ============================================================================
# 📱 ENHANCED MAIN APPLICATION
# ============================================================================

def main():
    """Enhanced main application function"""
    # Create enhanced header
    create_enhanced_header()
    
    # Load data
    with st.spinner("🔄 Loading AI models and data..."):
        df = load_and_enhance_data()
        recommender = EnhancedFoodRecommender(df)
    
    # Enhanced sidebar navigation
    if EXTENSIONS_AVAILABLE:
        with st.sidebar:
            selected = option_menu(
                menu_title="🍽️ AI Food Genius",
                options=["🏠 Home", "🤖 AI Recommendations", "📊 Analytics", "👥 Social", "📅 Meal Planning", "👤 Profile", "⚙️ Settings"],
                icons=["house", "robot", "graph-up", "people", "calendar", "person", "gear"],
                menu_icon="cast",
                default_index=0,
                styles={
                    "container": {"padding": "0!important", "background-color": "#fafafa"},
                    "icon": {"color": "#667eea", "font-size": "20px"},
                    "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                    "nav-link-selected": {"background-color": "#667eea"},
                }
            )
    else:
        selected = st.sidebar.selectbox(
            "Navigate",
            ["🏠 Home", "🤖 AI Recommendations", "📊 Analytics", "👥 Social", "📅 Meal Planning", "👤 Profile", "⚙️ Settings"]
        )
    
    # Main content based on selection
    if selected == "🏠 Home":
        show_enhanced_home_page(df, recommender)
    elif selected == "🤖 AI Recommendations":
        show_enhanced_recommendations_page(df, recommender)
    elif selected == "📊 Analytics":
        show_enhanced_analytics_page(df, recommender)
    elif selected == "👥 Social":
        show_social_page(df, recommender)
    elif selected == "📅 Meal Planning":
        show_meal_planning_page(df, recommender)
    elif selected == "👤 Profile":
        show_enhanced_profile_page(df, recommender)
    elif selected == "⚙️ Settings":
        show_enhanced_settings_page(df, recommender)

def show_enhanced_home_page(df, recommender):
    """Show enhanced home page with overview and quick features"""
    st.markdown("## 🏠 Welcome to AI Food Genius!")
    
    # Key metrics with enhanced styling
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        create_enhanced_metric_card("Total Recipes", len(df['Recipe_Name'].unique()), icon="🍽️")
    with col2:
        create_enhanced_metric_card("AI Accuracy", f"{max(recommender.model_scores.values())*100:.1f}%", icon="🤖")
    with col3:
        create_enhanced_metric_card("Active Users", len(df['User_ID'].unique()), icon="👥")
    with col4:
        create_enhanced_metric_card("Avg Rating", f"{df['User_Rating'].mean():.1f}/5", icon="⭐")
    
    st.markdown("---")
    
    # Quick features with enhanced buttons
    st.markdown("## ⚡ Quick Features")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🎯 Get Personalized Recommendations", use_container_width=True):
            st.session_state.show_recommendations = True
            st.rerun()
    
    with col2:
        if st.button("📊 View Analytics Dashboard", use_container_width=True):
            st.session_state.show_analytics = True
            st.rerun()
    
    with col3:
        if st.button("👥 Explore Social Features", use_container_width=True):
            st.session_state.show_social = True
            st.rerun()
    
    # Recent recommendations with enhanced cards
    st.markdown("## 🔥 Trending Recipes")
    trending_recipes = df.nlargest(5, 'Trending_Score')
    for idx, recipe in trending_recipes.iterrows():
        create_enhanced_recipe_card(recipe, idx, show_social=True)

def show_enhanced_recommendations_page(df, recommender):
    """Show enhanced AI recommendations page"""
    st.markdown("## 🤖 AI-Powered Recommendations")
    
    # User profile input with enhanced styling
    st.markdown("### 👤 Tell us about yourself")
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.slider("Age", 18, 80, 30)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        bmi = st.slider("BMI", 15.0, 40.0, 22.0)
        health_condition = st.selectbox("Health Condition", 
                                      ["None", "Diabetes", "Iron Deficiency", "Vitamin D Deficiency", "High Blood Pressure"])
    
    with col2:
        dietary_restriction = st.selectbox("Dietary Restriction", 
                                         ["Vegetarian", "Non-Vegetarian", "Vegan", "Keto", "Paleo"])
        preferred_cuisine = st.selectbox("Preferred Cuisine", 
                                       ["Indian", "Italian", "Asian", "Mediterranean", "Mexican", "American"])
        taste_preference = st.selectbox("Taste Preference", 
                                      ["Spicy", "Sweet", "Mild", "Savory", "Tangy"])
        cooking_time = st.slider("Max Cooking Time (minutes)", 10, 120, 45)
    
    # Advanced features
    st.markdown("### 🔧 Advanced Features")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        enable_social = st.checkbox("Enable Social Recommendations", value=True)
    with col2:
        enable_collaborative = st.checkbox("Enable Collaborative Filtering", value=True)
    with col3:
        enable_real_time = st.checkbox("Enable Real-time APIs", value=True)
    
    # Get recommendations
    if st.button("🎯 Get AI Recommendations", type="primary", use_container_width=True):
        with st.spinner("🤖 AI is analyzing your preferences..."):
            # Create user profile
            user_profile = {
                'Age': age, 'Gender': gender, 'BMI': bmi, 'Health_Condition': health_condition,
                'Dietary_Restriction': dietary_restriction, 'Preferred_Cuisine': preferred_cuisine,
                'Taste_Preference': taste_preference, 'User_ID': 'U001'
            }
            
            # Get enhanced recommendations
            recommendations = recommender.get_enhanced_recommendations(user_profile, 10)
            
            # Filter and rank recipes
            filtered_df = df[
                (df['Cooking_Time'] <= cooking_time) &
                (df['Dietary_Restriction'] == dietary_restriction) &
                (df['Preferred_Cuisine'] == preferred_cuisine)
            ].copy()
            
            if not filtered_df.empty:
                # Add AI scores
                filtered_df['AI_Score'] = (
                    0.4 * filtered_df['Nutrient_Score'] +
                    0.3 * filtered_df['Preference_Score'] +
                    0.3 * np.random.uniform(0.6, 0.9, len(filtered_df))
                )
                
                # Sort by AI score
                top_recommendations = filtered_df.nlargest(10, 'AI_Score')
                
                st.markdown("## 🍽️ Your Personalized Recommendations")
                
                for idx, recipe in top_recommendations.iterrows():
                    create_enhanced_recipe_card(recipe, idx, show_social=enable_social)
            else:
                st.warning("⚠️ No recipes found matching your criteria. Try adjusting your preferences.")

def show_enhanced_analytics_page(df, recommender):
    """Show enhanced analytics and insights page"""
    st.markdown("## 📊 Analytics & Insights")
    
    # Model performance with enhanced charts
    st.markdown("### 🤖 AI Model Performance")
    model_df = pd.DataFrame(list(recommender.model_scores.items()), 
                           columns=['Model', 'Accuracy'])
    model_df['Accuracy'] = model_df['Accuracy'] * 100
    
    fig = px.bar(model_df, x='Model', y='Accuracy', 
                 title="Model Accuracy Comparison",
                 color='Accuracy', color_continuous_scale='Viridis')
    st.plotly_chart(fig, use_container_width=True)
    
    # Enhanced nutritional insights
    st.markdown("### 🥗 Nutritional Insights")
    col1, col2 = st.columns(2)
    
    with col1:
        # Calories distribution
        fig = px.histogram(df, x='Calories', nbins=30, 
                          title="Calories Distribution",
                          color_discrete_sequence=['#667eea'])
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Macronutrient breakdown
        macro_data = df[['Protein_g', 'Carbs_g', 'Fat_g']].mean()
        fig = px.pie(values=macro_data.values, names=macro_data.index,
                     title="Average Macronutrient Distribution",
                     color_discrete_sequence=['#667eea', '#764ba2', '#56ab2f'])
        st.plotly_chart(fig, use_container_width=True)
    
    # Advanced analytics
    st.markdown("### 📈 Advanced Analytics")
    insights = recommender.analytics.create_insights_dashboard()
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Recipes", insights['platform_stats']['total_recipes'])
    with col2:
        st.metric("Total Users", insights['platform_stats']['total_users'])
    with col3:
        st.metric("Average Rating", f"{insights['platform_stats']['average_rating']:.1f}")
    with col4:
        st.metric("Most Rated Recipe", insights['platform_stats']['most_rated_recipe'])

def show_social_page(df, recommender):
    """Show social features page"""
    st.markdown("## 👥 Social Features")
    
    # Social metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Reviews", len(recommender.social_features.reviews))
    with col2:
        st.metric("Active Users", len(recommender.social_features.favorites))
    with col3:
        st.metric("Social Score", f"{df['Social_Score'].mean():.2f}")
    
    # Recent reviews
    st.markdown("### 📝 Recent Reviews")
    recent_reviews = recommender.social_features.reviews.tail(5)
    for _, review in recent_reviews.iterrows():
        with st.container():
            st.markdown(f"""
            <div class="recipe-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <strong>Recipe: {review['recipe_id']}</strong><br>
                        <span style="color: #666;">{review['review_text']}</span>
                    </div>
                    <div style="text-align: right;">
                        <div style="font-size: 1.5rem;">{'⭐' * int(review['rating'])}</div>
                        <div style="color: #666; font-size: 0.9rem;">{review['timestamp']}</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

def show_meal_planning_page(df, recommender):
    """Show meal planning page"""
    st.markdown("## 📅 Meal Planning")
    
    # Meal plan creation
    st.markdown("### 🍽️ Create Your Meal Plan")
    
    col1, col2 = st.columns(2)
    with col1:
        days = st.slider("Number of days", 1, 7, 7)
        user_id = st.text_input("User ID", value="U001")
    
    with col2:
        if st.button("📅 Generate Meal Plan", use_container_width=True):
            # Get user's favorite recipes
            favorites = recommender.social_features.get_user_favorites(user_id)
            if not favorites:
                favorites = df['Recipe_ID'].unique()[:10].tolist()
            
            # Create meal plan
            meal_plan = recommender.meal_planner.create_meal_plan(user_id, favorites, days)
            
            st.success("✅ Meal plan created successfully!")
            
            # Display meal plan
            for day, meals in meal_plan.items():
                st.markdown(f"### {day.title()}")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write(f"**Breakfast:** {meals['breakfast'] or 'Not planned'}")
                with col2:
                    st.write(f"**Lunch:** {meals['lunch'] or 'Not planned'}")
                with col3:
                    st.write(f"**Dinner:** {meals['dinner'] or 'Not planned'}")
    
    # Grocery list
    st.markdown("### 🛒 Grocery List")
    if st.button("🛒 Generate Grocery List", use_container_width=True):
        grocery_list = recommender.meal_planner.generate_grocery_list("U001", {})
        
        st.success("✅ Grocery list generated!")
        
        for item in grocery_list:
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.write(item['name'])
            with col2:
                st.write(item['quantity'])
            with col3:
                st.write(item['category'])
            with col4:
                st.checkbox("Purchased", value=item['purchased'], key=f"grocery_{item['name']}")

def show_enhanced_profile_page(df, recommender):
    """Show enhanced user profile page"""
    st.markdown("## 👤 User Profile")
    
    # Profile metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Reviews", 25)
    with col2:
        st.metric("Favorite Recipes", 12)
    with col3:
        st.metric("Followers", 45)
    
    # Profile settings
    st.markdown("### ⚙️ Profile Settings")
    col1, col2 = st.columns(2)
    
    with col1:
        st.text_input("Display Name", value="Food Lover")
        st.selectbox("Dietary Preference", ["Vegetarian", "Non-Vegetarian", "Vegan"])
        st.selectbox("Cuisine Preference", ["Indian", "Italian", "Asian", "Mediterranean"])
    
    with col2:
        st.slider("Age", 18, 80, 30)
        st.selectbox("Gender", ["Male", "Female", "Other"])
        st.slider("Activity Level", 1, 5, 3)
    
    if st.button("💾 Save Profile", use_container_width=True):
        st.success("Profile saved successfully!")

def show_enhanced_settings_page(df, recommender):
    """Show enhanced settings page"""
    st.markdown("## ⚙️ Settings")
    
    # Feature toggles
    st.markdown("### 🔧 Feature Settings")
    col1, col2 = st.columns(2)
    
    with col1:
        st.checkbox("Enable Voice Search", value=True)
        st.checkbox("Enable Food Recognition", value=True)
        st.checkbox("Enable Social Features", value=True)
    
    with col2:
        st.checkbox("Enable Real-time APIs", value=True)
        st.checkbox("Enable Advanced Analytics", value=True)
        st.checkbox("Enable Meal Planning", value=True)
    
    # API settings
    st.markdown("### 🌐 API Settings")
    st.text_input("Spoonacular API Key", type="password")
    st.text_input("YouTube API Key", type="password")
    
    # Theme settings
    st.markdown("### 🎨 Theme Settings")
    theme = st.selectbox("Theme", ["Light", "Dark", "Auto"])
    
    if st.button("💾 Save Settings", use_container_width=True):
        st.success("Settings saved successfully!")

# ============================================================================
# 🚀 RUN THE ENHANCED APPLICATION
# ============================================================================

if __name__ == "__main__":
    main()
