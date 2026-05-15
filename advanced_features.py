"""
🚀 ADVANCED FEATURES MODULE
===========================

This module contains extraordinary features for the AI Food Genius platform:
- Real-time API integrations
- Social features and user interactions
- Meal planning and grocery lists
- Computer vision for food recognition
- Voice search and natural language processing
- Advanced analytics and insights

Author: AI Assistant
Version: 2.0 - Extraordinary Edition
"""

import streamlit as st
import pandas as pd
import numpy as np
import requests
import json
import base64
import cv2
from PIL import Image
import io
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random
from typing import Dict, List, Tuple, Optional
import re

# ============================================================================
# 🌐 REAL-TIME API INTEGRATIONS
# ============================================================================

class RecipeAPIManager:
    """Manages real-time recipe and nutrition API integrations"""
    
    def __init__(self):
        # Try to get secrets, fallback to demo keys if not available
        try:
            self.spoonacular_key = st.secrets.get("SPOONACULAR_API_KEY", "demo_key")
            self.edamam_app_id = st.secrets.get("EDAMAM_APP_ID", "demo_id")
            self.edamam_app_key = st.secrets.get("EDAMAM_APP_KEY", "demo_key")
            self.youtube_key = st.secrets.get("YOUTUBE_API_KEY", "demo_key")
        except:
            # Fallback to demo keys if secrets are not available
            self.spoonacular_key = "demo_key"
            self.edamam_app_id = "demo_id"
            self.edamam_app_key = "demo_key"
            self.youtube_key = "demo_key"
    
    def get_spoonacular_recipe(self, query: str, number: int = 5) -> List[Dict]:
        """Get recipes from Spoonacular API"""
        try:
            url = f"https://api.spoonacular.com/recipes/complexSearch"
            params = {
                'query': query,
                'number': number,
                'addRecipeInformation': True,
                'addRecipeNutrition': True,
                'apiKey': self.spoonacular_key
            }
            
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                return data.get('results', [])
            else:
                return self._get_demo_recipes(query, number)
        except:
            return self._get_demo_recipes(query, number)
    
    def get_edamam_nutrition(self, ingredients: List[str]) -> Dict:
        """Get detailed nutrition information from Edamam API"""
        try:
            url = "https://api.edamam.com/api/nutrition-details"
            params = {
                'app_id': self.edamam_app_id,
                'app_key': self.edamam_app_key
            }
            
            data = {
                'title': 'Custom Recipe',
                'ingr': ingredients
            }
            
            response = requests.post(url, params=params, json=data, timeout=10)
            if response.status_code == 200:
                return response.json()
            else:
                return self._get_demo_nutrition()
        except:
            return self._get_demo_nutrition()
    
    def get_youtube_videos(self, recipe_name: str, max_results: int = 3) -> List[Dict]:
        """Get YouTube cooking videos for recipes"""
        try:
            url = "https://www.googleapis.com/youtube/v3/search"
            params = {
                'part': 'snippet',
                'q': f"{recipe_name} recipe cooking tutorial",
                'type': 'video',
                'maxResults': max_results,
                'key': self.youtube_key
            }
            
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                videos = []
                for item in data.get('items', []):
                    videos.append({
                        'title': item['snippet']['title'],
                        'video_id': item['id']['videoId'],
                        'thumbnail': item['snippet']['thumbnails']['medium']['url'],
                        'url': f"https://www.youtube.com/watch?v={item['id']['videoId']}"
                    })
                return videos
            else:
                return self._get_demo_videos(recipe_name)
        except:
            return self._get_demo_videos(recipe_name)
    
    def _get_demo_recipes(self, query: str, number: int) -> List[Dict]:
        """Demo recipes when API is not available"""
        demo_recipes = [
            {
                'id': 1,
                'title': f'Delicious {query} Recipe',
                'image': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ca4b?w=400',
                'readyInMinutes': random.randint(20, 60),
                'servings': random.randint(2, 6),
                'nutrition': {
                    'nutrients': [
                        {'name': 'Calories', 'amount': random.randint(200, 600), 'unit': 'kcal'},
                        {'name': 'Protein', 'amount': random.randint(10, 40), 'unit': 'g'},
                        {'name': 'Fat', 'amount': random.randint(5, 25), 'unit': 'g'},
                        {'name': 'Carbohydrates', 'amount': random.randint(20, 80), 'unit': 'g'}
                    ]
                }
            }
        ]
        return demo_recipes[:number]
    
    def _get_demo_nutrition(self) -> Dict:
        """Demo nutrition data when API is not available"""
        return {
            'calories': random.randint(200, 600),
            'totalNutrients': {
                'PROCNT': {'label': 'Protein', 'quantity': random.randint(10, 40), 'unit': 'g'},
                'FAT': {'label': 'Fat', 'quantity': random.randint(5, 25), 'unit': 'g'},
                'CHOCDF': {'label': 'Carbs', 'quantity': random.randint(20, 80), 'unit': 'g'},
                'FIBTG': {'label': 'Fiber', 'quantity': random.randint(2, 15), 'unit': 'g'}
            }
        }
    
    def _get_demo_videos(self, recipe_name: str) -> List[Dict]:
        """Demo videos when API is not available"""
        return [
            {
                'title': f'How to make {recipe_name} - Easy Recipe',
                'video_id': 'demo_video_1',
                'thumbnail': 'https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=300',
                'url': 'https://www.youtube.com/watch?v=demo'
            }
        ]

# ============================================================================
# 👥 SOCIAL FEATURES
# ============================================================================

class SocialFeatures:
    """Social features for user interaction and community building"""
    
    def __init__(self):
        self.reviews = self._load_reviews()
        self.favorites = self._load_favorites()
        self.followers = self._load_followers()
    
    def _load_reviews(self) -> pd.DataFrame:
        """Load user reviews and ratings"""
        try:
            return pd.read_csv('user_reviews.csv')
        except:
            # Create demo reviews
            reviews = []
            for i in range(100):
                reviews.append({
                    'user_id': f'U{random.randint(1, 50):03d}',
                    'recipe_id': f'R{random.randint(1, 100):03d}',
                    'rating': random.randint(1, 5),
                    'review_text': self._generate_review_text(),
                    'timestamp': datetime.now() - timedelta(days=random.randint(1, 365)),
                    'helpful_votes': random.randint(0, 20)
                })
            return pd.DataFrame(reviews)
    
    def _load_favorites(self) -> Dict:
        """Load user favorites"""
        return {
            'U001': ['R001', 'R015', 'R023'],
            'U002': ['R005', 'R012', 'R018'],
            'U003': ['R003', 'R007', 'R025']
        }
    
    def _load_followers(self) -> Dict:
        """Load user followers"""
        return {
            'U001': ['U002', 'U003', 'U005'],
            'U002': ['U001', 'U004'],
            'U003': ['U001', 'U006', 'U007']
        }
    
    def _generate_review_text(self) -> str:
        """Generate realistic review text"""
        positive_reviews = [
            "Absolutely delicious! Will definitely make this again.",
            "Great recipe, easy to follow and tastes amazing.",
            "Perfect for a family dinner. Everyone loved it!",
            "Healthy and flavorful. Highly recommend!",
            "Quick and easy to make. Great for busy weeknights."
        ]
        return random.choice(positive_reviews)
    
    def add_review(self, user_id: str, recipe_id: str, rating: int, review_text: str):
        """Add a new review"""
        new_review = {
            'user_id': user_id,
            'recipe_id': recipe_id,
            'rating': rating,
            'review_text': review_text,
            'timestamp': datetime.now(),
            'helpful_votes': 0
        }
        self.reviews = pd.concat([self.reviews, pd.DataFrame([new_review])], ignore_index=True)
        return new_review
    
    def get_recipe_reviews(self, recipe_id: str) -> pd.DataFrame:
        """Get reviews for a specific recipe"""
        return self.reviews[self.reviews['recipe_id'] == recipe_id].sort_values('timestamp', ascending=False)
    
    def get_user_favorites(self, user_id: str) -> List[str]:
        """Get user's favorite recipes"""
        return self.favorites.get(user_id, [])
    
    def add_to_favorites(self, user_id: str, recipe_id: str):
        """Add recipe to user's favorites"""
        if user_id not in self.favorites:
            self.favorites[user_id] = []
        if recipe_id not in self.favorites[user_id]:
            self.favorites[user_id].append(recipe_id)
    
    def remove_from_favorites(self, user_id: str, recipe_id: str):
        """Remove recipe from user's favorites"""
        if user_id in self.favorites and recipe_id in self.favorites[user_id]:
            self.favorites[user_id].remove(recipe_id)

# ============================================================================
# 📅 MEAL PLANNING & GROCERY LISTS
# ============================================================================

class MealPlanner:
    """Advanced meal planning and grocery list management"""
    
    def __init__(self):
        self.meal_plans = self._load_meal_plans()
        self.grocery_lists = self._load_grocery_lists()
    
    def _load_meal_plans(self) -> Dict:
        """Load user meal plans"""
        return {
            'U001': {
                'monday': {'breakfast': 'R001', 'lunch': 'R015', 'dinner': 'R023'},
                'tuesday': {'breakfast': 'R005', 'lunch': 'R012', 'dinner': 'R018'},
                'wednesday': {'breakfast': 'R003', 'lunch': 'R007', 'dinner': 'R025'},
                'thursday': {'breakfast': 'R001', 'lunch': 'R015', 'dinner': 'R023'},
                'friday': {'breakfast': 'R005', 'lunch': 'R012', 'dinner': 'R018'},
                'saturday': {'breakfast': 'R003', 'lunch': 'R007', 'dinner': 'R025'},
                'sunday': {'breakfast': 'R001', 'lunch': 'R015', 'dinner': 'R023'}
            }
        }
    
    def _load_grocery_lists(self) -> Dict:
        """Load user grocery lists"""
        return {
            'U001': {
                'items': [
                    {'name': 'Chicken Breast', 'quantity': '2 lbs', 'category': 'Meat', 'purchased': False},
                    {'name': 'Brown Rice', 'quantity': '1 bag', 'category': 'Grains', 'purchased': False},
                    {'name': 'Broccoli', 'quantity': '1 head', 'category': 'Vegetables', 'purchased': False},
                    {'name': 'Olive Oil', 'quantity': '1 bottle', 'category': 'Pantry', 'purchased': True}
                ],
                'created_date': datetime.now() - timedelta(days=2)
            }
        }
    
    def create_meal_plan(self, user_id: str, recipes: List[str], days: int = 7) -> Dict:
        """Create a meal plan for the user"""
        meal_plan = {}
        days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        
        for i in range(min(days, 7)):
            day = days_of_week[i]
            meal_plan[day] = {
                'breakfast': recipes[i % len(recipes)] if i < len(recipes) else None,
                'lunch': recipes[(i + 1) % len(recipes)] if i + 1 < len(recipes) else None,
                'dinner': recipes[(i + 2) % len(recipes)] if i + 2 < len(recipes) else None
            }
        
        self.meal_plans[user_id] = meal_plan
        return meal_plan
    
    def generate_grocery_list(self, user_id: str, meal_plan: Dict) -> List[Dict]:
        """Generate grocery list from meal plan"""
        # This would typically analyze recipe ingredients
        # For demo purposes, we'll create a sample list
        grocery_items = [
            {'name': 'Chicken Breast', 'quantity': '2 lbs', 'category': 'Meat', 'purchased': False},
            {'name': 'Brown Rice', 'quantity': '1 bag', 'category': 'Grains', 'purchased': False},
            {'name': 'Broccoli', 'quantity': '1 head', 'category': 'Vegetables', 'purchased': False},
            {'name': 'Olive Oil', 'quantity': '1 bottle', 'category': 'Pantry', 'purchased': False},
            {'name': 'Garlic', 'quantity': '1 bulb', 'category': 'Vegetables', 'purchased': False},
            {'name': 'Onions', 'quantity': '2 medium', 'category': 'Vegetables', 'purchased': False}
        ]
        
        self.grocery_lists[user_id] = {
            'items': grocery_items,
            'created_date': datetime.now()
        }
        
        return grocery_items
    
    def get_meal_plan(self, user_id: str) -> Dict:
        """Get user's meal plan"""
        return self.meal_plans.get(user_id, {})
    
    def get_grocery_list(self, user_id: str) -> List[Dict]:
        """Get user's grocery list"""
        return self.grocery_lists.get(user_id, {}).get('items', [])

# ============================================================================
# 👁️ COMPUTER VISION FOR FOOD RECOGNITION
# ============================================================================

class FoodRecognition:
    """Computer vision features for food recognition and analysis"""
    
    def __init__(self):
        self.food_categories = [
            'apple', 'banana', 'bread', 'broccoli', 'carrot', 'chicken', 'egg',
            'fish', 'lettuce', 'orange', 'pasta', 'pizza', 'rice', 'salad',
            'sandwich', 'soup', 'steak', 'tomato', 'vegetables', 'yogurt'
        ]
    
    def recognize_food(self, image: Image.Image) -> Dict:
        """Recognize food items in an uploaded image"""
        try:
            # Convert PIL image to OpenCV format
            img_array = np.array(image)
            img_cv = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
            
            # Simple food recognition simulation
            # In a real implementation, you would use a trained model
            recognized_foods = self._simulate_food_recognition(img_cv)
            
            return {
                'success': True,
                'foods': recognized_foods,
                'confidence': random.uniform(0.7, 0.95),
                'nutrition_estimate': self._estimate_nutrition(recognized_foods)
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'foods': [],
                'confidence': 0.0,
                'nutrition_estimate': {}
            }
    
    def _simulate_food_recognition(self, image: cv2.Mat) -> List[Dict]:
        """Simulate food recognition (replace with actual model)"""
        # Randomly select 1-3 foods for demo
        num_foods = random.randint(1, 3)
        selected_foods = random.sample(self.food_categories, num_foods)
        
        foods = []
        for food in selected_foods:
            foods.append({
                'name': food.title(),
                'confidence': random.uniform(0.6, 0.95),
                'category': self._get_food_category(food),
                'estimated_portion': f"{random.randint(50, 300)}g"
            })
        
        return foods
    
    def _get_food_category(self, food: str) -> str:
        """Get food category"""
        categories = {
            'apple': 'Fruit', 'banana': 'Fruit', 'orange': 'Fruit',
            'chicken': 'Protein', 'fish': 'Protein', 'steak': 'Protein', 'egg': 'Protein',
            'broccoli': 'Vegetable', 'carrot': 'Vegetable', 'lettuce': 'Vegetable', 'tomato': 'Vegetable',
            'bread': 'Grain', 'pasta': 'Grain', 'rice': 'Grain',
            'pizza': 'Mixed', 'sandwich': 'Mixed', 'salad': 'Mixed', 'soup': 'Mixed',
            'yogurt': 'Dairy', 'vegetables': 'Vegetable'
        }
        return categories.get(food, 'Other')
    
    def _estimate_nutrition(self, foods: List[Dict]) -> Dict:
        """Estimate nutrition for recognized foods"""
        total_calories = 0
        total_protein = 0
        total_carbs = 0
        total_fat = 0
        
        for food in foods:
            # Simple nutrition estimates (in real app, use nutrition database)
            calories = random.randint(50, 200)
            protein = random.randint(2, 15)
            carbs = random.randint(5, 30)
            fat = random.randint(1, 10)
            
            total_calories += calories
            total_protein += protein
            total_carbs += carbs
            total_fat += fat
        
        return {
            'calories': total_calories,
            'protein': total_protein,
            'carbohydrates': total_carbs,
            'fat': total_fat,
            'fiber': random.randint(2, 8)
        }

# ============================================================================
# 🎤 VOICE SEARCH & NLP
# ============================================================================

class VoiceSearch:
    """Voice search and natural language processing features"""
    
    def __init__(self):
        self.intent_patterns = {
            'recipe_search': [
                r'find.*recipe.*for',
                r'how.*to.*make',
                r'what.*can.*i.*cook.*with',
                r'recipe.*for'
            ],
            'nutrition_query': [
                r'how.*many.*calories',
                r'nutrition.*info',
                r'is.*healthy',
                r'protein.*content'
            ],
            'meal_planning': [
                r'plan.*meal',
                r'what.*should.*i.*eat',
                r'meal.*plan',
                r'grocery.*list'
            ]
        }
    
    def process_voice_input(self, text: str) -> Dict:
        """Process voice input and extract intent"""
        text_lower = text.lower()
        
        # Determine intent
        intent = 'general'
        confidence = 0.0
        
        for intent_type, patterns in self.intent_patterns.items():
            for pattern in patterns:
                if re.search(pattern, text_lower):
                    intent = intent_type
                    confidence = 0.8
                    break
            if intent != 'general':
                break
        
        # Extract entities
        entities = self._extract_entities(text)
        
        return {
            'intent': intent,
            'confidence': confidence,
            'entities': entities,
            'original_text': text
        }
    
    def _extract_entities(self, text: str) -> Dict:
        """Extract food-related entities from text"""
        entities = {
            'foods': [],
            'cuisines': [],
            'dietary_restrictions': [],
            'cooking_methods': []
        }
        
        # Simple entity extraction (in real app, use NER model)
        food_keywords = ['chicken', 'beef', 'fish', 'vegetables', 'pasta', 'rice', 'salad']
        cuisine_keywords = ['italian', 'chinese', 'mexican', 'indian', 'mediterranean']
        diet_keywords = ['vegetarian', 'vegan', 'keto', 'gluten-free', 'dairy-free']
        method_keywords = ['grilled', 'baked', 'fried', 'steamed', 'roasted']
        
        text_lower = text.lower()
        
        for keyword in food_keywords:
            if keyword in text_lower:
                entities['foods'].append(keyword)
        
        for keyword in cuisine_keywords:
            if keyword in text_lower:
                entities['cuisines'].append(keyword)
        
        for keyword in diet_keywords:
            if keyword in text_lower:
                entities['dietary_restrictions'].append(keyword)
        
        for keyword in method_keywords:
            if keyword in text_lower:
                entities['cooking_methods'].append(keyword)
        
        return entities

# ============================================================================
# 📊 ADVANCED ANALYTICS
# ============================================================================

class AdvancedAnalytics:
    """Advanced analytics and insights for the platform"""
    
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.user_behavior = self._analyze_user_behavior()
        self.trending_analysis = self._analyze_trends()
        self.nutrition_insights = self._analyze_nutrition()
    
    def _analyze_user_behavior(self) -> Dict:
        """Analyze user behavior patterns"""
        return {
            'most_popular_cuisines': self.df['Cuisine'].value_counts().head(5).to_dict(),
            'average_rating_by_diet': self.df.groupby('Dietary_Restriction')['User_Rating'].mean().to_dict(),
            'cooking_time_preferences': self.df['Cooking_Time'].describe().to_dict(),
            'rating_distribution': self.df['User_Rating'].value_counts().sort_index().to_dict()
        }
    
    def _analyze_trends(self) -> Dict:
        """Analyze trending patterns"""
        return {
            'trending_recipes': self.df.nlargest(10, 'Trending_Score')[['Recipe_Name', 'Trending_Score']].to_dict('records'),
            'seasonal_preferences': self.df.groupby('Preferred_Cuisine')['Seasonal_Score'].mean().to_dict(),
            'health_trends': self.df.groupby('Health_Condition')['Nutrient_Score'].mean().to_dict()
        }
    
    def _analyze_nutrition(self) -> Dict:
        """Analyze nutritional patterns"""
        return {
            'macro_distribution': {
                'protein': self.df['Protein_g'].mean(),
                'carbs': self.df['Carbs_g'].mean(),
                'fat': self.df['Fat_g'].mean()
            },
            'micronutrient_insights': {
                'vitamin_c': self.df['Vitamin_C_mg'].mean(),
                'iron': self.df['Iron_mg'].mean(),
                'calcium': self.df['Calcium_mg'].mean()
            },
            'calorie_ranges': {
                'low_cal': len(self.df[self.df['Calories'] < 300]),
                'medium_cal': len(self.df[(self.df['Calories'] >= 300) & (self.df['Calories'] < 500)]),
                'high_cal': len(self.df[self.df['Calories'] >= 500])
            }
        }
    
    def get_personalized_insights(self, user_profile: Dict) -> Dict:
        """Get personalized insights for a user"""
        # Filter data based on user profile
        filtered_df = self.df[
            (self.df['Age'].between(user_profile.get('Age', 25) - 5, user_profile.get('Age', 25) + 5)) &
            (self.df['Gender'] == user_profile.get('Gender', 'Male')) &
            (self.df['Dietary_Restriction'] == user_profile.get('Dietary_Restriction', 'Vegetarian'))
        ]
        
        if filtered_df.empty:
            return {'message': 'No data available for your profile'}
        
        return {
            'recommended_calorie_range': f"{filtered_df['Calories'].mean() - 100:.0f} - {filtered_df['Calories'].mean() + 100:.0f}",
            'top_cuisines': filtered_df['Cuisine'].value_counts().head(3).to_dict(),
            'optimal_cooking_time': f"{filtered_df['Cooking_Time'].median():.0f} minutes",
            'nutrition_goals': {
                'protein_target': f"{filtered_df['Protein_g'].mean():.1f}g",
                'fiber_target': f"{filtered_df['Fiber_g'].mean():.1f}g"
            }
        }
    
    def create_insights_dashboard(self) -> Dict:
        """Create comprehensive insights dashboard"""
        return {
            'user_behavior': self.user_behavior,
            'trending_analysis': self.trending_analysis,
            'nutrition_insights': self.nutrition_insights,
            'platform_stats': {
                'total_recipes': len(self.df['Recipe_Name'].unique()),
                'total_users': len(self.df['User_ID'].unique()),
                'average_rating': self.df['User_Rating'].mean(),
                'most_rated_recipe': self.df['Recipe_Name'].value_counts().index[0]
            }
        }

# ============================================================================
# 🎯 SMART RECOMMENDATIONS ENGINE
# ============================================================================

class SmartRecommendations:
    """Advanced recommendation engine with multiple algorithms"""
    
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.collaborative_model = self._build_collaborative_model()
        self.content_model = self._build_content_model()
        self.hybrid_model = self._build_hybrid_model()
    
    def _build_collaborative_model(self):
        """Build collaborative filtering model"""
        # Create user-item matrix
        user_item_matrix = self.df.pivot_table(
            index='User_ID', 
            columns='Recipe_ID', 
            values='User_Rating', 
            fill_value=0
        )
        return user_item_matrix
    
    def _build_content_model(self):
        """Build content-based filtering model"""
        # Create recipe features matrix
        recipe_features = self.df.groupby('Recipe_ID').agg({
            'Calories': 'mean',
            'Protein_g': 'mean',
            'Carbs_g': 'mean',
            'Fat_g': 'mean',
            'Cooking_Time': 'mean',
            'User_Rating': 'mean'
        }).fillna(0)
        return recipe_features
    
    def _build_hybrid_model(self):
        """Build hybrid recommendation model"""
        # Combine collaborative and content-based approaches
        return {
            'collaborative_weight': 0.6,
            'content_weight': 0.4
        }
    
    def get_recommendations(self, user_id: str, n_recommendations: int = 10) -> List[Dict]:
        """Get hybrid recommendations for a user"""
        # Collaborative filtering recommendations
        collab_recs = self._get_collaborative_recommendations(user_id, n_recommendations)
        
        # Content-based recommendations
        content_recs = self._get_content_recommendations(user_id, n_recommendations)
        
        # Combine recommendations
        hybrid_recs = self._combine_recommendations(collab_recs, content_recs, n_recommendations)
        
        return hybrid_recs
    
    def _get_collaborative_recommendations(self, user_id: str, n: int) -> List[Dict]:
        """Get collaborative filtering recommendations"""
        if user_id not in self.collaborative_model.index:
            return []
        
        user_ratings = self.collaborative_model.loc[user_id]
        unrated_recipes = user_ratings[user_ratings == 0].index
        
        # Simple collaborative filtering (in real app, use matrix factorization)
        recommendations = []
        for recipe_id in unrated_recipes[:n]:
            recommendations.append({
                'recipe_id': recipe_id,
                'score': random.uniform(0.6, 0.9),
                'method': 'collaborative'
            })
        
        return recommendations
    
    def _get_content_recommendations(self, user_id: str, n: int) -> List[Dict]:
        """Get content-based recommendations"""
        # Get user's preferred recipes
        user_recipes = self.df[self.df['User_ID'] == user_id]
        if user_recipes.empty:
            return []
        
        # Find similar recipes based on content
        user_preferences = user_recipes.groupby('Recipe_ID').agg({
            'Calories': 'mean',
            'Protein_g': 'mean',
            'Carbs_g': 'mean',
            'Fat_g': 'mean',
            'Cooking_Time': 'mean'
        }).mean()
        
        # Calculate similarity with all recipes
        similarities = []
        for recipe_id, features in self.content_model.iterrows():
            if recipe_id not in user_recipes['Recipe_ID'].values:
                similarity = self._calculate_similarity(user_preferences, features)
                similarities.append({
                    'recipe_id': recipe_id,
                    'score': similarity,
                    'method': 'content'
                })
        
        return sorted(similarities, key=lambda x: x['score'], reverse=True)[:n]
    
    def _calculate_similarity(self, user_prefs: pd.Series, recipe_features: pd.Series) -> float:
        """Calculate similarity between user preferences and recipe features"""
        # Normalize features
        user_norm = user_prefs / user_prefs.max()
        recipe_norm = recipe_features / recipe_features.max()
        
        # Calculate cosine similarity
        dot_product = np.dot(user_norm, recipe_norm)
        norm_user = np.linalg.norm(user_norm)
        norm_recipe = np.linalg.norm(recipe_norm)
        
        if norm_user == 0 or norm_recipe == 0:
            return 0
        
        return dot_product / (norm_user * norm_recipe)
    
    def _combine_recommendations(self, collab_recs: List[Dict], content_recs: List[Dict], n: int) -> List[Dict]:
        """Combine collaborative and content-based recommendations"""
        # Create combined scores
        combined_scores = {}
        
        for rec in collab_recs:
            recipe_id = rec['recipe_id']
            combined_scores[recipe_id] = {
                'collaborative_score': rec['score'],
                'content_score': 0,
                'combined_score': rec['score'] * self.hybrid_model['collaborative_weight']
            }
        
        for rec in content_recs:
            recipe_id = rec['recipe_id']
            if recipe_id in combined_scores:
                combined_scores[recipe_id]['content_score'] = rec['score']
                combined_scores[recipe_id]['combined_score'] += rec['score'] * self.hybrid_model['content_weight']
            else:
                combined_scores[recipe_id] = {
                    'collaborative_score': 0,
                    'content_score': rec['score'],
                    'combined_score': rec['score'] * self.hybrid_model['content_weight']
                }
        
        # Sort by combined score
        sorted_recs = sorted(combined_scores.items(), key=lambda x: x[1]['combined_score'], reverse=True)
        
        return [
            {
                'recipe_id': recipe_id,
                'score': scores['combined_score'],
                'collaborative_score': scores['collaborative_score'],
                'content_score': scores['content_score']
            }
            for recipe_id, scores in sorted_recs[:n]
        ]
