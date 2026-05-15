"""
🔧 CONFIGURATION FILE
=====================

Configuration settings for the AI Food Genius platform.
This file contains all the settings, API keys, and configuration options.

Author: AI Assistant
Version: 2.0 - Extraordinary Edition
"""

import os
from typing import Dict, List, Any

# ============================================================================
# 🌐 API CONFIGURATIONS
# ============================================================================

# Try to get API keys from environment or Streamlit secrets
def get_api_key(key_name, default_value):
    """Get API key from environment variable or Streamlit secrets"""
    # First try environment variable
    env_value = os.getenv(key_name)
    if env_value:
        return env_value
    
    # Then try Streamlit secrets
    try:
        import streamlit as st
        return st.secrets.get(key_name, default_value)
    except:
        return default_value

API_CONFIG = {
    # Spoonacular API for recipes
    'SPOONACULAR_API_KEY': get_api_key('SPOONACULAR_API_KEY', 'demo_key'),
    'SPOONACULAR_BASE_URL': 'https://api.spoonacular.com',
    
    # Edamam API for nutrition
    'EDAMAM_APP_ID': get_api_key('EDAMAM_APP_ID', 'demo_id'),
    'EDAMAM_APP_KEY': get_api_key('EDAMAM_APP_KEY', 'demo_key'),
    'EDAMAM_BASE_URL': 'https://api.edamam.com',
    
    # YouTube API for cooking videos
    'YOUTUBE_API_KEY': get_api_key('YOUTUBE_API_KEY', 'demo_key'),
    'YOUTUBE_BASE_URL': 'https://www.googleapis.com/youtube/v3',
    
    # OpenAI API for advanced NLP (optional)
    'OPENAI_API_KEY': get_api_key('OPENAI_API_KEY', 'demo_key'),
    
    # Google Vision API for food recognition (optional)
    'GOOGLE_VISION_API_KEY': get_api_key('GOOGLE_VISION_API_KEY', 'demo_key'),
}

# ============================================================================
# 🎨 UI/UX CONFIGURATIONS
# ============================================================================

UI_CONFIG = {
    # Theme colors
    'PRIMARY_COLOR': '#667eea',
    'SECONDARY_COLOR': '#764ba2',
    'SUCCESS_COLOR': '#56ab2f',
    'WARNING_COLOR': '#f39c12',
    'ERROR_COLOR': '#e74c3c',
    'INFO_COLOR': '#3498db',
    
    # Layout settings
    'SIDEBAR_WIDTH': 300,
    'MAIN_CONTENT_PADDING': 20,
    'CARD_BORDER_RADIUS': 15,
    'ANIMATION_DURATION': 0.3,
    
    # Typography
    'FONT_FAMILY': 'Inter, sans-serif',
    'HEADING_FONT_SIZE': '3rem',
    'SUBHEADING_FONT_SIZE': '1.5rem',
    'BODY_FONT_SIZE': '1rem',
    
    # Spacing
    'SECTION_MARGIN': '2rem',
    'CARD_PADDING': '1.5rem',
    'BUTTON_PADDING': '0.5rem 2rem',
}

# ============================================================================
# 🤖 AI/ML CONFIGURATIONS
# ============================================================================

ML_CONFIG = {
    # Model parameters
    'RANDOM_FOREST_ESTIMATORS': 200,
    'RANDOM_FOREST_MAX_DEPTH': 15,
    'XGBOOST_ESTIMATORS': 200,
    'XGBOOST_MAX_DEPTH': 8,
    'XGBOOST_LEARNING_RATE': 0.1,
    'NEURAL_NETWORK_LAYERS': [128, 64, 32],
    'NEURAL_NETWORK_MAX_ITER': 500,
    
    # Feature engineering
    'MAX_FEATURES_TFIDF': 100,
    'MIN_DF_TFIDF': 2,
    'MAX_DF_TFIDF': 0.95,
    
    # Recommendation weights
    'COLLABORATIVE_WEIGHT': 0.6,
    'CONTENT_WEIGHT': 0.4,
    'NUTRIENT_SCORE_WEIGHT': 0.4,
    'PREFERENCE_SCORE_WEIGHT': 0.3,
    'AI_PREDICTION_WEIGHT': 0.3,
    
    # Clustering
    'N_CLUSTERS': 5,
    'CLUSTERING_RANDOM_STATE': 42,
}

# ============================================================================
# 📊 DATA CONFIGURATIONS
# ============================================================================

DATA_CONFIG = {
    # File paths
    'DATASET_PATH': 'final_dataset.csv',
    'USER_PROFILES_PATH': 'user_profiles.csv',
    'RECIPES_PATH': 'recipes.csv',
    'NUTRITION_PATH': 'nutrition.csv',
    'USER_FEEDBACK_PATH': 'user_feedback.csv',
    
    # Data processing
    'CACHE_TTL': 3600,  # 1 hour
    'MAX_RECORDS_DISPLAY': 1000,
    'DEFAULT_PAGE_SIZE': 20,
    
    # Data validation
    'MIN_AGE': 18,
    'MAX_AGE': 80,
    'MIN_BMI': 15.0,
    'MAX_BMI': 40.0,
    'MIN_RATING': 1,
    'MAX_RATING': 5,
    'MIN_COOKING_TIME': 5,
    'MAX_COOKING_TIME': 180,
}

# ============================================================================
# 🍽️ FOOD & NUTRITION CONFIGURATIONS
# ============================================================================

FOOD_CONFIG = {
    # Dietary restrictions
    'DIETARY_RESTRICTIONS': [
        'Vegetarian', 'Non-Vegetarian', 'Vegan', 'Keto', 'Paleo',
        'Gluten-Free', 'Dairy-Free', 'Nut-Free', 'Low-Carb', 'High-Protein'
    ],
    
    # Cuisines
    'CUISINES': [
        'Indian', 'Italian', 'Asian', 'Mediterranean', 'Mexican',
        'American', 'Chinese', 'Japanese', 'Thai', 'French', 'Spanish'
    ],
    
    # Health conditions
    'HEALTH_CONDITIONS': [
        'None', 'Diabetes', 'Iron Deficiency', 'Vitamin D Deficiency',
        'High Blood Pressure', 'Heart Disease', 'Obesity', 'Underweight',
        'Food Allergies', 'Digestive Issues'
    ],
    
    # Taste preferences
    'TASTE_PREFERENCES': [
        'Spicy', 'Sweet', 'Mild', 'Savory', 'Tangy', 'Bitter',
        'Umami', 'Sour', 'Salty', 'Herbal'
    ],
    
    # Cooking methods
    'COOKING_METHODS': [
        'Grilled', 'Baked', 'Fried', 'Steamed', 'Roasted', 'Boiled',
        'Sauteed', 'Stir-fried', 'Slow-cooked', 'Raw'
    ],
    
    # Food categories
    'FOOD_CATEGORIES': [
        'Fruit', 'Vegetable', 'Protein', 'Grain', 'Dairy', 'Legume',
        'Nut', 'Seed', 'Herb', 'Spice', 'Beverage', 'Dessert'
    ],
    
    # Nutritional targets
    'DAILY_NUTRITION_TARGETS': {
        'calories': {'male': 2500, 'female': 2000},
        'protein': {'male': 56, 'female': 46},  # grams
        'carbs': {'male': 300, 'female': 250},  # grams
        'fat': {'male': 83, 'female': 67},      # grams
        'fiber': {'male': 38, 'female': 25},    # grams
        'vitamin_c': {'male': 90, 'female': 75}, # mg
        'iron': {'male': 8, 'female': 18},      # mg
        'calcium': {'male': 1000, 'female': 1000} # mg
    }
}

# ============================================================================
# 🎯 RECOMMENDATION CONFIGURATIONS
# ============================================================================

RECOMMENDATION_CONFIG = {
    # Recommendation limits
    'MAX_RECOMMENDATIONS': 20,
    'DEFAULT_RECOMMENDATIONS': 10,
    'MIN_RECOMMENDATIONS': 5,
    
    # Scoring thresholds
    'MIN_AI_SCORE': 0.3,
    'MIN_USER_RATING': 3.0,
    'MIN_NUTRIENT_SCORE': 0.5,
    'MIN_PREFERENCE_SCORE': 0.4,
    
    # Diversity settings
    'MAX_SAME_CUISINE': 3,
    'MAX_SAME_DIET_TYPE': 2,
    'DIVERSITY_PENALTY': 0.1,
    
    # Personalization
    'PERSONALIZATION_FACTOR': 0.8,
    'COLLABORATIVE_FACTOR': 0.6,
    'CONTENT_FACTOR': 0.4,
    'TRENDING_FACTOR': 0.2,
    'SEASONAL_FACTOR': 0.1,
}

# ============================================================================
# 📱 FEATURE CONFIGURATIONS
# ============================================================================

FEATURE_CONFIG = {
    # Enabled features
    'ENABLE_VOICE_SEARCH': True,
    'ENABLE_FOOD_RECOGNITION': True,
    'ENABLE_SOCIAL_FEATURES': True,
    'ENABLE_MEAL_PLANNING': True,
    'ENABLE_GROCERY_LISTS': True,
    'ENABLE_ANALYTICS': True,
    'ENABLE_REAL_TIME_APIS': True,
    'ENABLE_ADVANCED_ML': True,
    
    # Feature limits
    'MAX_UPLOAD_SIZE_MB': 10,
    'MAX_VOICE_DURATION_SECONDS': 30,
    'MAX_MEAL_PLAN_DAYS': 7,
    'MAX_GROCERY_ITEMS': 50,
    'MAX_SOCIAL_FOLLOWERS': 1000,
    
    # Cache settings
    'CACHE_API_RESPONSES': True,
    'CACHE_DURATION_HOURS': 24,
    'CACHE_MAX_SIZE_MB': 100,
}

# ============================================================================
# 🔒 SECURITY CONFIGURATIONS
# ============================================================================

SECURITY_CONFIG = {
    # Authentication
    'ENABLE_AUTHENTICATION': False,  # Set to True for production
    'SESSION_TIMEOUT_MINUTES': 60,
    'MAX_LOGIN_ATTEMPTS': 5,
    'PASSWORD_MIN_LENGTH': 8,
    
    # Data privacy
    'ENABLE_DATA_ENCRYPTION': True,
    'ENABLE_ANONYMOUS_MODE': True,
    'DATA_RETENTION_DAYS': 365,
    'ENABLE_GDPR_COMPLIANCE': True,
    
    # API security
    'ENABLE_RATE_LIMITING': True,
    'MAX_REQUESTS_PER_MINUTE': 60,
    'ENABLE_API_KEY_VALIDATION': True,
}

# ============================================================================
# 📊 ANALYTICS CONFIGURATIONS
# ============================================================================

ANALYTICS_CONFIG = {
    # Tracking
    'ENABLE_USER_ANALYTICS': True,
    'ENABLE_PERFORMANCE_METRICS': True,
    'ENABLE_ERROR_TRACKING': True,
    'ENABLE_USAGE_STATISTICS': True,
    
    # Metrics
    'TRACK_PAGE_VIEWS': True,
    'TRACK_USER_INTERACTIONS': True,
    'TRACK_RECOMMENDATION_CLICKS': True,
    'TRACK_SEARCH_QUERIES': True,
    
    # Reporting
    'GENERATE_DAILY_REPORTS': True,
    'GENERATE_WEEKLY_REPORTS': True,
    'GENERATE_MONTHLY_REPORTS': True,
    'REPORT_RETENTION_DAYS': 90,
}

# ============================================================================
# 🌍 LOCALIZATION CONFIGURATIONS
# ============================================================================

LOCALIZATION_CONFIG = {
    # Supported languages
    'SUPPORTED_LANGUAGES': ['en', 'es', 'fr', 'de', 'it', 'pt', 'zh', 'ja', 'ko', 'hi'],
    'DEFAULT_LANGUAGE': 'en',
    
    # Regional settings
    'SUPPORTED_CURRENCIES': ['USD', 'EUR', 'GBP', 'INR', 'JPY', 'CNY'],
    'DEFAULT_CURRENCY': 'USD',
    
    # Units
    'SUPPORTED_UNITS': ['metric', 'imperial'],
    'DEFAULT_UNITS': 'metric',
    
    # Date formats
    'DATE_FORMAT': '%Y-%m-%d',
    'TIME_FORMAT': '%H:%M:%S',
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',
}

# ============================================================================
# 🚀 PERFORMANCE CONFIGURATIONS
# ============================================================================

PERFORMANCE_CONFIG = {
    # Caching
    'ENABLE_REDIS_CACHE': False,  # Set to True if Redis is available
    'CACHE_TTL_SECONDS': 3600,
    'MAX_CACHE_SIZE_MB': 500,
    
    # Database
    'ENABLE_DATABASE_OPTIMIZATION': True,
    'QUERY_TIMEOUT_SECONDS': 30,
    'MAX_CONNECTIONS': 100,
    
    # API
    'API_TIMEOUT_SECONDS': 10,
    'MAX_RETRIES': 3,
    'RETRY_DELAY_SECONDS': 1,
    
    # UI
    'ENABLE_LAZY_LOADING': True,
    'PAGINATION_SIZE': 20,
    'MAX_CONCURRENT_REQUESTS': 5,
}

# ============================================================================
# 🎨 THEME CONFIGURATIONS
# ============================================================================

THEME_CONFIG = {
    # Light theme
    'LIGHT_THEME': {
        'background': '#ffffff',
        'primary': '#667eea',
        'secondary': '#764ba2',
        'text': '#2c3e50',
        'text_secondary': '#7f8c8d',
        'border': '#e0e0e0',
        'card_background': '#ffffff',
        'sidebar_background': '#f8f9fa',
    },
    
    # Dark theme
    'DARK_THEME': {
        'background': '#1a1a1a',
        'primary': '#667eea',
        'secondary': '#764ba2',
        'text': '#ffffff',
        'text_secondary': '#b0b0b0',
        'border': '#333333',
        'card_background': '#2d2d2d',
        'sidebar_background': '#1e1e1e',
    },
    
    # Current theme
    'CURRENT_THEME': 'LIGHT_THEME',
}

# ============================================================================
# 🔧 DEVELOPMENT CONFIGURATIONS
# ============================================================================

DEVELOPMENT_CONFIG = {
    # Debug settings
    'DEBUG_MODE': True,
    'VERBOSE_LOGGING': True,
    'ENABLE_PROFILING': False,
    
    # Testing
    'ENABLE_MOCK_DATA': True,
    'MOCK_API_RESPONSES': True,
    'ENABLE_UNIT_TESTS': False,
    
    # Development tools
    'ENABLE_HOT_RELOAD': True,
    'ENABLE_DEBUG_TOOLBAR': True,
    'ENABLE_PERFORMANCE_MONITORING': True,
}

# ============================================================================
# 📋 CONFIGURATION VALIDATION
# ============================================================================

def validate_config() -> Dict[str, Any]:
    """Validate configuration settings and return status"""
    validation_results = {
        'valid': True,
        'errors': [],
        'warnings': [],
        'recommendations': []
    }
    
    # Validate API keys
    if API_CONFIG['SPOONACULAR_API_KEY'] == 'demo_key':
        validation_results['warnings'].append('Using demo Spoonacular API key')
        validation_results['recommendations'].append('Set SPOONACULAR_API_KEY environment variable for real API access')
    
    if API_CONFIG['YOUTUBE_API_KEY'] == 'demo_key':
        validation_results['warnings'].append('Using demo YouTube API key')
        validation_results['recommendations'].append('Set YOUTUBE_API_KEY environment variable for real API access')
    
    # Validate data files
    import os
    required_files = [
        DATA_CONFIG['DATASET_PATH'],
        DATA_CONFIG['USER_PROFILES_PATH'],
        DATA_CONFIG['RECIPES_PATH'],
        DATA_CONFIG['NUTRITION_PATH'],
        DATA_CONFIG['USER_FEEDBACK_PATH']
    ]
    
    for file_path in required_files:
        if not os.path.exists(file_path):
            validation_results['errors'].append(f'Required data file not found: {file_path}')
            validation_results['valid'] = False
    
    # Validate ML parameters
    if ML_CONFIG['RANDOM_FOREST_ESTIMATORS'] < 10:
        validation_results['errors'].append('Random Forest estimators should be at least 10')
        validation_results['valid'] = False
    
    if ML_CONFIG['XGBOOST_LEARNING_RATE'] <= 0 or ML_CONFIG['XGBOOST_LEARNING_RATE'] > 1:
        validation_results['errors'].append('XGBoost learning rate should be between 0 and 1')
        validation_results['valid'] = False
    
    return validation_results

# ============================================================================
# 🎯 CONFIGURATION GETTERS
# ============================================================================

def get_config(section: str) -> Dict[str, Any]:
    """Get configuration for a specific section"""
    configs = {
        'api': API_CONFIG,
        'ui': UI_CONFIG,
        'ml': ML_CONFIG,
        'data': DATA_CONFIG,
        'food': FOOD_CONFIG,
        'recommendation': RECOMMENDATION_CONFIG,
        'feature': FEATURE_CONFIG,
        'security': SECURITY_CONFIG,
        'analytics': ANALYTICS_CONFIG,
        'localization': LOCALIZATION_CONFIG,
        'performance': PERFORMANCE_CONFIG,
        'theme': THEME_CONFIG,
        'development': DEVELOPMENT_CONFIG
    }
    
    return configs.get(section, {})

def get_all_configs() -> Dict[str, Dict[str, Any]]:
    """Get all configuration sections"""
    return {
        'api': API_CONFIG,
        'ui': UI_CONFIG,
        'ml': ML_CONFIG,
        'data': DATA_CONFIG,
        'food': FOOD_CONFIG,
        'recommendation': RECOMMENDATION_CONFIG,
        'feature': FEATURE_CONFIG,
        'security': SECURITY_CONFIG,
        'analytics': ANALYTICS_CONFIG,
        'localization': LOCALIZATION_CONFIG,
        'performance': PERFORMANCE_CONFIG,
        'theme': THEME_CONFIG,
        'development': DEVELOPMENT_CONFIG
    }

# ============================================================================
# 🚀 INITIALIZATION
# ============================================================================

def initialize_config():
    """Initialize configuration and validate settings"""
    validation = validate_config()
    
    if not validation['valid']:
        print("❌ Configuration validation failed:")
        for error in validation['errors']:
            print(f"  - {error}")
        return False
    
    if validation['warnings']:
        print("⚠️ Configuration warnings:")
        for warning in validation['warnings']:
            print(f"  - {warning}")
    
    if validation['recommendations']:
        print("💡 Configuration recommendations:")
        for recommendation in validation['recommendations']:
            print(f"  - {recommendation}")
    
    print("✅ Configuration initialized successfully!")
    return True

if __name__ == "__main__":
    initialize_config()
