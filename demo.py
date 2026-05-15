"""
🎬 AI FOOD GENIUS - DEMO SCRIPT
===============================

This script demonstrates the extraordinary features of the AI Food Genius platform.
It showcases the advanced AI models, social features, and beautiful UI components.

Author: AI Assistant
Version: 2.0 - Extraordinary Edition
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random

# Page Configuration
st.set_page_config(
    page_title="🍽️ AI Food Genius - Demo",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
.main {
    padding: 0;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.demo-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 3rem 0;
    text-align: center;
    color: white;
    border-radius: 0 0 30px 30px;
    margin-bottom: 2rem;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.demo-header h1 {
    font-family: 'Poppins', sans-serif;
    font-weight: 900;
    font-size: 4rem;
    margin: 0;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

.demo-card {
    background: white;
    border-radius: 15px;
    padding: 2rem;
    margin: 1rem 0;
    box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
}

.demo-card:hover {
    transform: translateY(-5px);
}

.feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.feature-item {
    background: white;
    border-radius: 15px;
    padding: 1.5rem;
    text-align: center;
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
}

.feature-item:hover {
    transform: translateY(-5px);
}

.feature-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.metric-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 1.5rem;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 8px 25px rgba(0,0,0,0.1);
}

.metric-value {
    font-size: 2.5rem;
    font-weight: 800;
    margin: 0;
}

.metric-label {
    font-size: 1rem;
    opacity: 0.9;
    margin: 0;
}
</style>
""", unsafe_allow_html=True)

def create_demo_header():
    """Create demo header"""
    st.markdown("""
    <div class="demo-header">
        <h1>🍽️ AI Food Genius</h1>
        <p style="font-size: 1.3rem; margin: 1rem 0 0 0; opacity: 0.9;">
            ✨ Extraordinary Edition - Demo Showcase
        </p>
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

def show_ai_demo():
    """Show AI features demo"""
    st.markdown("## 🤖 AI Features Demo")
    
    # Simulate AI model performance
    models = ['RandomForest', 'XGBoost', 'GradientBoosting', 'Neural Network']
    accuracies = [0.89, 0.92, 0.87, 0.91]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🧠 Model Performance")
        fig = px.bar(
            x=models, y=accuracies,
            title="AI Model Accuracy",
            color=accuracies,
            color_continuous_scale='Viridis'
        )
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 📊 Recommendation Scores")
        # Simulate recommendation scores
        recipes = ['Grilled Chicken', 'Veg Stir Fry', 'Paneer Tikka', 'Quinoa Salad', 'Spinach Soup']
        scores = [0.95, 0.87, 0.92, 0.89, 0.85]
        
        fig = px.pie(
            values=scores, names=recipes,
            title="Top Recommendations",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # AI Insights
    st.markdown("### 🔍 AI Insights")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">94.2%</div>
            <div class="metric-label">Accuracy</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">0.3s</div>
            <div class="metric-label">Response Time</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">1.2M</div>
            <div class="metric-label">Data Points</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">4</div>
            <div class="metric-label">ML Models</div>
        </div>
        """, unsafe_allow_html=True)

def show_social_demo():
    """Show social features demo"""
    st.markdown("## 👥 Social Features Demo")
    
    # Simulate social data
    social_data = {
        'User': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        'Followers': [120, 89, 156, 203, 78],
        'Recipes_Shared': [15, 8, 23, 31, 12],
        'Reviews_Given': [45, 23, 67, 89, 34]
    }
    
    df_social = pd.DataFrame(social_data)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📈 User Engagement")
        fig = px.bar(
            df_social, x='User', y='Followers',
            title="User Followers",
            color='Followers',
            color_continuous_scale='Blues'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 🍽️ Recipe Sharing")
        fig = px.scatter(
            df_social, x='Recipes_Shared', y='Reviews_Given',
            size='Followers', color='User',
            title="User Activity",
            hover_data=['User']
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Recent reviews
    st.markdown("### 📝 Recent Reviews")
    reviews = [
        {"user": "Alice", "recipe": "Grilled Chicken", "rating": 5, "review": "Absolutely delicious! Will definitely make this again."},
        {"user": "Bob", "recipe": "Veg Stir Fry", "rating": 4, "review": "Great recipe, easy to follow and tastes amazing."},
        {"user": "Charlie", "recipe": "Paneer Tikka", "rating": 5, "review": "Perfect for a family dinner. Everyone loved it!"},
        {"user": "Diana", "recipe": "Quinoa Salad", "rating": 4, "review": "Healthy and flavorful. Highly recommend!"},
        {"user": "Eve", "recipe": "Spinach Soup", "rating": 5, "review": "Quick and easy to make. Great for busy weeknights."}
    ]
    
    for review in reviews:
        with st.container():
            st.markdown(f"""
            <div class="demo-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <strong>{review['user']}</strong> reviewed <strong>{review['recipe']}</strong><br>
                        <span style="color: #666;">{review['review']}</span>
                    </div>
                    <div style="text-align: right;">
                        <div style="font-size: 1.5rem;">{'⭐' * review['rating']}</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

def show_meal_planning_demo():
    """Show meal planning demo"""
    st.markdown("## 📅 Meal Planning Demo")
    
    # Simulate meal plan
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    meals = {
        'Breakfast': ['Oatmeal', 'Smoothie Bowl', 'Avocado Toast', 'Greek Yogurt', 'Pancakes', 'Eggs Benedict', 'French Toast'],
        'Lunch': ['Grilled Chicken Salad', 'Quinoa Bowl', 'Veggie Wrap', 'Soup & Sandwich', 'Pasta Salad', 'Burrito Bowl', 'Caesar Salad'],
        'Dinner': ['Salmon & Rice', 'Stir Fry', 'Pasta', 'Grilled Veggies', 'Tacos', 'Pizza', 'Roast Chicken']
    }
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🍽️ Weekly Meal Plan")
        meal_plan_df = pd.DataFrame(meals, index=days)
        st.dataframe(meal_plan_df, use_container_width=True)
    
    with col2:
        st.markdown("### 🛒 Grocery List")
        grocery_items = [
            {'item': 'Chicken Breast', 'quantity': '2 lbs', 'category': 'Meat'},
            {'item': 'Brown Rice', 'quantity': '1 bag', 'category': 'Grains'},
            {'item': 'Broccoli', 'quantity': '1 head', 'category': 'Vegetables'},
            {'item': 'Olive Oil', 'quantity': '1 bottle', 'category': 'Pantry'},
            {'item': 'Garlic', 'quantity': '1 bulb', 'category': 'Vegetables'},
            {'item': 'Onions', 'quantity': '2 medium', 'category': 'Vegetables'}
        ]
        
        for item in grocery_items:
            st.markdown(f"""
            <div class="demo-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <strong>{item['item']}</strong><br>
                        <span style="color: #666;">{item['quantity']}</span>
                    </div>
                    <div style="background: #f0f0f0; padding: 0.5rem 1rem; border-radius: 20px;">
                        {item['category']}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

def show_analytics_demo():
    """Show analytics demo"""
    st.markdown("## 📊 Analytics Demo")
    
    # Simulate analytics data
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">1,247</div>
            <div class="metric-label">Total Recipes</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">5,892</div>
            <div class="metric-label">Active Users</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">4.7</div>
            <div class="metric-label">Avg Rating</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">94.2%</div>
            <div class="metric-label">AI Accuracy</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📈 User Growth")
        dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='M')
        users = np.cumsum(np.random.randint(100, 500, len(dates)))
        
        fig = px.line(
            x=dates, y=users,
            title="Monthly Active Users",
            labels={'x': 'Month', 'y': 'Users'}
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 🍽️ Recipe Categories")
        categories = ['Indian', 'Italian', 'Asian', 'Mediterranean', 'Mexican', 'American']
        counts = [245, 189, 156, 134, 98, 87]
        
        fig = px.pie(
            values=counts, names=categories,
            title="Recipe Distribution by Cuisine",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        st.plotly_chart(fig, use_container_width=True)

def show_features_overview():
    """Show features overview"""
    st.markdown("## ✨ Extraordinary Features")
    
    features = [
        {"icon": "🤖", "title": "Advanced AI", "description": "Ensemble ML models with 94%+ accuracy"},
        {"icon": "🌐", "title": "Real-time APIs", "description": "Live recipe and nutrition data"},
        {"icon": "👥", "title": "Social Features", "description": "Reviews, ratings, and community"},
        {"icon": "📅", "title": "Meal Planning", "description": "Smart weekly meal plans"},
        {"icon": "👁️", "title": "Computer Vision", "description": "Food recognition from photos"},
        {"icon": "🎤", "title": "Voice Search", "description": "Natural language queries"},
        {"icon": "📊", "title": "Analytics", "description": "Comprehensive insights"},
        {"icon": "🎨", "title": "Beautiful UI", "description": "Modern design with animations"}
    ]
    
    # Create feature grid
    cols = st.columns(4)
    for i, feature in enumerate(features):
        with cols[i % 4]:
            st.markdown(f"""
            <div class="feature-item">
                <div class="feature-icon">{feature['icon']}</div>
                <h3>{feature['title']}</h3>
                <p>{feature['description']}</p>
            </div>
            """, unsafe_allow_html=True)

def main():
    """Main demo function"""
    create_demo_header()
    
    # Navigation
    st.markdown("## 🎬 Demo Navigation")
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🏠 Overview", "🤖 AI Features", "👥 Social", "📅 Meal Planning", "📊 Analytics"
    ])
    
    with tab1:
        show_features_overview()
        
        st.markdown("## 🚀 Getting Started")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🎯 Try AI Recommendations", use_container_width=True):
                st.info("Navigate to the AI Features tab to see recommendations in action!")
        
        with col2:
            if st.button("👥 Explore Social Features", use_container_width=True):
                st.info("Check out the Social tab to see community features!")
        
        with col3:
            if st.button("📅 Plan Your Meals", use_container_width=True):
                st.info("Visit the Meal Planning tab to create your meal plan!")
    
    with tab2:
        show_ai_demo()
    
    with tab3:
        show_social_demo()
    
    with tab4:
        show_meal_planning_demo()
    
    with tab5:
        show_analytics_demo()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem; color: #666;">
        <h3>🍽️ AI Food Genius - Extraordinary Edition</h3>
        <p>Experience the future of food recommendations with cutting-edge AI technology!</p>
        <p>Ready to try the full application? Run: <code>streamlit run app_enhanced.py</code></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
