"""
🍽️ RECIPE DATABASE ENHANCEMENT
==============================

This script enhances the recipe database with a comprehensive collection of
diverse recipes covering different dietary preferences, cuisines, and meal types.

Author: AI Assistant
Version: 2.0 - Enhanced Recipe Collection
"""

import pandas as pd
import numpy as np
import random
from datetime import datetime

def create_enhanced_recipes():
    """Create a comprehensive recipe database with diverse options"""
    
    # Comprehensive recipe collection
    recipes_data = []
    
    # ============================================================================
    # 🥗 VEGETARIAN RECIPES
    # ============================================================================
    
    vegetarian_recipes = [
        # Indian Vegetarian
        {"name": "Dal Makhani", "cuisine": "Indian", "diet": "Vegetarian", "time": 45, "calories": 320, "protein": 18, "carbs": 45, "fat": 8, "fiber": 12, "vitamin_c": 15, "iron": 4.2, "calcium": 120},
        {"name": "Palak Paneer", "cuisine": "Indian", "diet": "Vegetarian", "time": 30, "calories": 280, "protein": 22, "carbs": 12, "fat": 16, "fiber": 4, "vitamin_c": 45, "iron": 3.8, "calcium": 350},
        {"name": "Chana Masala", "cuisine": "Indian", "diet": "Vegetarian", "time": 35, "calories": 250, "protein": 15, "carbs": 38, "fat": 6, "fiber": 10, "vitamin_c": 25, "iron": 3.5, "calcium": 80},
        {"name": "Aloo Gobi", "cuisine": "Indian", "diet": "Vegetarian", "time": 25, "calories": 180, "protein": 6, "carbs": 28, "fat": 5, "fiber": 6, "vitamin_c": 60, "iron": 2.1, "calcium": 45},
        {"name": "Rajma Curry", "cuisine": "Indian", "diet": "Vegetarian", "time": 40, "calories": 290, "protein": 16, "carbs": 42, "fat": 7, "fiber": 14, "vitamin_c": 20, "iron": 4.8, "calcium": 95},
        {"name": "Biryani Rice", "cuisine": "Indian", "diet": "Vegetarian", "time": 50, "calories": 350, "protein": 8, "carbs": 65, "fat": 8, "fiber": 3, "vitamin_c": 12, "iron": 1.8, "calcium": 25},
        {"name": "Samosa", "cuisine": "Indian", "diet": "Vegetarian", "time": 30, "calories": 220, "protein": 5, "carbs": 28, "fat": 10, "fiber": 3, "vitamin_c": 8, "iron": 1.2, "calcium": 30},
        {"name": "Pakora", "cuisine": "Indian", "diet": "Vegetarian", "time": 20, "calories": 180, "protein": 4, "carbs": 22, "fat": 8, "fiber": 2, "vitamin_c": 15, "iron": 1.5, "calcium": 40},
        
        # Italian Vegetarian
        {"name": "Margherita Pizza", "cuisine": "Italian", "diet": "Vegetarian", "time": 25, "calories": 280, "protein": 12, "carbs": 35, "fat": 10, "fiber": 2, "vitamin_c": 8, "iron": 1.8, "calcium": 200},
        {"name": "Pasta Primavera", "cuisine": "Italian", "diet": "Vegetarian", "time": 20, "calories": 320, "protein": 14, "carbs": 45, "fat": 8, "fiber": 4, "vitamin_c": 35, "iron": 2.2, "calcium": 120},
        {"name": "Risotto", "cuisine": "Italian", "diet": "Vegetarian", "time": 35, "calories": 380, "protein": 10, "carbs": 55, "fat": 12, "fiber": 2, "vitamin_c": 5, "iron": 1.5, "calcium": 80},
        {"name": "Caprese Salad", "cuisine": "Italian", "diet": "Vegetarian", "time": 10, "calories": 150, "protein": 8, "carbs": 8, "fat": 10, "fiber": 1, "vitamin_c": 25, "iron": 0.8, "calcium": 150},
        {"name": "Eggplant Parmesan", "cuisine": "Italian", "diet": "Vegetarian", "time": 45, "calories": 320, "protein": 16, "carbs": 25, "fat": 18, "fiber": 6, "vitamin_c": 12, "iron": 2.5, "calcium": 280},
        {"name": "Minestrone Soup", "cuisine": "Italian", "diet": "Vegetarian", "time": 30, "calories": 180, "protein": 8, "carbs": 28, "fat": 4, "fiber": 8, "vitamin_c": 40, "iron": 2.8, "calcium": 60},
        
        # Asian Vegetarian
        {"name": "Vegetable Stir Fry", "cuisine": "Asian", "diet": "Vegetarian", "time": 15, "calories": 120, "protein": 4, "carbs": 18, "fat": 3, "fiber": 5, "vitamin_c": 55, "iron": 1.8, "calcium": 45},
        {"name": "Tofu Curry", "cuisine": "Asian", "diet": "Vegetarian", "time": 25, "calories": 200, "protein": 16, "carbs": 12, "fat": 10, "fiber": 3, "vitamin_c": 20, "iron": 3.2, "calcium": 180},
        {"name": "Vegetable Spring Rolls", "cuisine": "Asian", "diet": "Vegetarian", "time": 20, "calories": 80, "protein": 3, "carbs": 12, "fat": 2, "fiber": 2, "vitamin_c": 25, "iron": 1.2, "calcium": 30},
        {"name": "Miso Soup", "cuisine": "Asian", "diet": "Vegetarian", "time": 10, "calories": 35, "protein": 2, "carbs": 4, "fat": 1, "fiber": 1, "vitamin_c": 5, "iron": 0.8, "calcium": 20},
        {"name": "Vegetable Ramen", "cuisine": "Asian", "diet": "Vegetarian", "time": 20, "calories": 280, "protein": 12, "carbs": 45, "fat": 6, "fiber": 4, "vitamin_c": 30, "iron": 2.5, "calcium": 80},
        
        # Mediterranean Vegetarian
        {"name": "Greek Salad", "cuisine": "Mediterranean", "diet": "Vegetarian", "time": 10, "calories": 200, "protein": 8, "carbs": 12, "fat": 14, "fiber": 3, "vitamin_c": 35, "iron": 1.5, "calcium": 120},
        {"name": "Hummus", "cuisine": "Mediterranean", "diet": "Vegetarian", "time": 15, "calories": 180, "protein": 8, "carbs": 18, "fat": 8, "fiber": 6, "vitamin_c": 8, "iron": 2.8, "calcium": 60},
        {"name": "Falafel", "cuisine": "Mediterranean", "diet": "Vegetarian", "time": 30, "calories": 220, "protein": 10, "carbs": 25, "fat": 8, "fiber": 6, "vitamin_c": 12, "iron": 3.5, "calcium": 80},
        {"name": "Ratatouille", "cuisine": "Mediterranean", "diet": "Vegetarian", "time": 40, "calories": 120, "protein": 4, "carbs": 18, "fat": 4, "fiber": 6, "vitamin_c": 45, "iron": 1.8, "calcium": 40},
        {"name": "Stuffed Bell Peppers", "cuisine": "Mediterranean", "diet": "Vegetarian", "time": 35, "calories": 180, "protein": 8, "carbs": 22, "fat": 6, "fiber": 5, "vitamin_c": 80, "iron": 2.2, "calcium": 60},
        
        # Mexican Vegetarian
        {"name": "Bean Burrito", "cuisine": "Mexican", "diet": "Vegetarian", "time": 15, "calories": 320, "protein": 14, "carbs": 45, "fat": 8, "fiber": 12, "vitamin_c": 15, "iron": 3.8, "calcium": 120},
        {"name": "Vegetable Quesadilla", "cuisine": "Mexican", "diet": "Vegetarian", "time": 20, "calories": 280, "protein": 12, "carbs": 28, "fat": 12, "fiber": 4, "vitamin_c": 25, "iron": 2.5, "calcium": 200},
        {"name": "Guacamole", "cuisine": "Mexican", "diet": "Vegetarian", "time": 10, "calories": 160, "protein": 2, "carbs": 8, "fat": 14, "fiber": 6, "vitamin_c": 20, "iron": 0.8, "calcium": 20},
        {"name": "Vegetable Enchiladas", "cuisine": "Mexican", "diet": "Vegetarian", "time": 30, "calories": 250, "protein": 10, "carbs": 32, "fat": 8, "fiber": 6, "vitamin_c": 30, "iron": 2.8, "calcium": 150},
    ]
    
    # ============================================================================
    # 🥩 NON-VEGETARIAN RECIPES
    # ============================================================================
    
    non_vegetarian_recipes = [
        # Indian Non-Vegetarian
        {"name": "Chicken Curry", "cuisine": "Indian", "diet": "Non-Vegetarian", "time": 40, "calories": 350, "protein": 28, "carbs": 15, "fat": 18, "fiber": 3, "vitamin_c": 20, "iron": 3.2, "calcium": 60},
        {"name": "Mutton Biryani", "cuisine": "Indian", "diet": "Non-Vegetarian", "time": 60, "calories": 480, "protein": 32, "carbs": 45, "fat": 20, "fiber": 2, "vitamin_c": 15, "iron": 4.5, "calcium": 40},
        {"name": "Fish Curry", "cuisine": "Indian", "diet": "Non-Vegetarian", "time": 30, "calories": 280, "protein": 35, "carbs": 8, "fat": 12, "fiber": 2, "vitamin_c": 25, "iron": 2.8, "calcium": 80},
        {"name": "Chicken Tikka", "cuisine": "Indian", "diet": "Non-Vegetarian", "time": 35, "calories": 220, "protein": 25, "carbs": 5, "fat": 10, "fiber": 1, "vitamin_c": 8, "iron": 2.2, "calcium": 30},
        {"name": "Lamb Rogan Josh", "cuisine": "Indian", "diet": "Non-Vegetarian", "time": 50, "calories": 420, "protein": 30, "carbs": 12, "fat": 25, "fiber": 2, "vitamin_c": 18, "iron": 4.8, "calcium": 50},
        {"name": "Prawn Curry", "cuisine": "Indian", "diet": "Non-Vegetarian", "time": 25, "calories": 200, "protein": 22, "carbs": 8, "fat": 8, "fiber": 2, "vitamin_c": 15, "iron": 2.5, "calcium": 60},
        {"name": "Chicken Biryani", "cuisine": "Indian", "diet": "Non-Vegetarian", "time": 55, "calories": 450, "protein": 30, "carbs": 42, "fat": 18, "fiber": 2, "vitamin_c": 12, "iron": 3.8, "calcium": 35},
        {"name": "Egg Curry", "cuisine": "Indian", "diet": "Non-Vegetarian", "time": 20, "calories": 180, "protein": 14, "carbs": 8, "fat": 10, "fiber": 2, "vitamin_c": 12, "iron": 2.8, "calcium": 80},
        
        # Italian Non-Vegetarian
        {"name": "Chicken Parmesan", "cuisine": "Italian", "diet": "Non-Vegetarian", "time": 35, "calories": 420, "protein": 35, "carbs": 25, "fat": 18, "fiber": 2, "vitamin_c": 8, "iron": 2.5, "calcium": 200},
        {"name": "Spaghetti Carbonara", "cuisine": "Italian", "diet": "Non-Vegetarian", "time": 20, "calories": 480, "protein": 20, "carbs": 45, "fat": 22, "fiber": 2, "vitamin_c": 5, "iron": 2.2, "calcium": 120},
        {"name": "Chicken Alfredo", "cuisine": "Italian", "diet": "Non-Vegetarian", "time": 25, "calories": 520, "protein": 28, "carbs": 35, "fat": 28, "fiber": 2, "vitamin_c": 8, "iron": 2.8, "calcium": 150},
        {"name": "Seafood Risotto", "cuisine": "Italian", "diet": "Non-Vegetarian", "time": 40, "calories": 380, "protein": 25, "carbs": 42, "fat": 12, "fiber": 2, "vitamin_c": 12, "iron": 3.2, "calcium": 80},
        {"name": "Pepperoni Pizza", "cuisine": "Italian", "diet": "Non-Vegetarian", "time": 25, "calories": 320, "protein": 18, "carbs": 32, "fat": 14, "fiber": 2, "vitamin_c": 8, "iron": 2.8, "calcium": 180},
        {"name": "Chicken Marsala", "cuisine": "Italian", "diet": "Non-Vegetarian", "time": 30, "calories": 350, "protein": 32, "carbs": 15, "fat": 16, "fiber": 1, "vitamin_c": 5, "iron": 2.2, "calcium": 40},
        
        # Asian Non-Vegetarian
        {"name": "Chicken Stir Fry", "cuisine": "Asian", "diet": "Non-Vegetarian", "time": 20, "calories": 250, "protein": 28, "carbs": 15, "fat": 8, "fiber": 3, "vitamin_c": 35, "iron": 2.8, "calcium": 40},
        {"name": "Beef Teriyaki", "cuisine": "Asian", "diet": "Non-Vegetarian", "time": 25, "calories": 320, "protein": 35, "carbs": 18, "fat": 12, "fiber": 2, "vitamin_c": 15, "iron": 4.2, "calcium": 30},
        {"name": "Sweet and Sour Chicken", "cuisine": "Asian", "diet": "Non-Vegetarian", "time": 30, "calories": 380, "protein": 25, "carbs": 35, "fat": 15, "fiber": 2, "vitamin_c": 25, "iron": 2.5, "calcium": 35},
        {"name": "Pork Dumplings", "cuisine": "Asian", "diet": "Non-Vegetarian", "time": 35, "calories": 280, "protein": 18, "carbs": 25, "fat": 12, "fiber": 2, "vitamin_c": 8, "iron": 2.8, "calcium": 40},
        {"name": "Chicken Ramen", "cuisine": "Asian", "diet": "Non-Vegetarian", "time": 25, "calories": 420, "protein": 32, "carbs": 45, "fat": 12, "fiber": 3, "vitamin_c": 20, "iron": 3.5, "calcium": 60},
        {"name": "Beef Noodles", "cuisine": "Asian", "diet": "Non-Vegetarian", "time": 20, "calories": 450, "protein": 35, "carbs": 38, "fat": 18, "fiber": 3, "vitamin_c": 15, "iron": 4.8, "calcium": 45},
        
        # Mediterranean Non-Vegetarian
        {"name": "Grilled Salmon", "cuisine": "Mediterranean", "diet": "Non-Vegetarian", "time": 20, "calories": 280, "protein": 35, "carbs": 2, "fat": 14, "fiber": 0, "vitamin_c": 5, "iron": 1.8, "calcium": 20},
        {"name": "Chicken Souvlaki", "cuisine": "Mediterranean", "diet": "Non-Vegetarian", "time": 30, "calories": 320, "protein": 32, "carbs": 8, "fat": 16, "fiber": 1, "vitamin_c": 12, "iron": 2.5, "calcium": 40},
        {"name": "Lamb Kebab", "cuisine": "Mediterranean", "diet": "Non-Vegetarian", "time": 35, "calories": 380, "protein": 35, "carbs": 5, "fat": 22, "fiber": 1, "vitamin_c": 8, "iron": 4.2, "calcium": 30},
        {"name": "Fish Tacos", "cuisine": "Mediterranean", "diet": "Non-Vegetarian", "time": 25, "calories": 280, "protein": 25, "carbs": 22, "fat": 10, "fiber": 3, "vitamin_c": 20, "iron": 2.8, "calcium": 80},
        
        # Mexican Non-Vegetarian
        {"name": "Chicken Enchiladas", "cuisine": "Mexican", "diet": "Non-Vegetarian", "time": 35, "calories": 380, "protein": 28, "carbs": 32, "fat": 15, "fiber": 4, "vitamin_c": 25, "iron": 3.2, "calcium": 180},
        {"name": "Beef Tacos", "cuisine": "Mexican", "diet": "Non-Vegetarian", "time": 20, "calories": 320, "protein": 22, "carbs": 25, "fat": 14, "fiber": 3, "vitamin_c": 15, "iron": 3.8, "calcium": 120},
        {"name": "Chicken Quesadilla", "cuisine": "Mexican", "diet": "Non-Vegetarian", "time": 15, "calories": 420, "protein": 32, "carbs": 28, "fat": 18, "fiber": 2, "vitamin_c": 8, "iron": 2.8, "calcium": 250},
        {"name": "Pork Carnitas", "cuisine": "Mexican", "diet": "Non-Vegetarian", "time": 45, "calories": 350, "protein": 35, "carbs": 8, "fat": 18, "fiber": 1, "vitamin_c": 5, "iron": 3.5, "calcium": 25},
    ]
    
    # ============================================================================
    # 🌱 VEGAN RECIPES
    # ============================================================================
    
    vegan_recipes = [
        # Indian Vegan
        {"name": "Vegan Dal", "cuisine": "Indian", "diet": "Vegan", "time": 35, "calories": 250, "protein": 15, "carbs": 38, "fat": 6, "fiber": 12, "vitamin_c": 18, "iron": 4.5, "calcium": 80},
        {"name": "Vegan Curry", "cuisine": "Indian", "diet": "Vegan", "time": 30, "calories": 200, "protein": 8, "carbs": 28, "fat": 8, "fiber": 6, "vitamin_c": 35, "iron": 3.2, "calcium": 60},
        {"name": "Vegan Biryani", "cuisine": "Indian", "diet": "Vegan", "time": 45, "calories": 320, "protein": 8, "carbs": 58, "fat": 8, "fiber": 4, "vitamin_c": 20, "iron": 2.8, "calcium": 40},
        {"name": "Vegan Samosa", "cuisine": "Indian", "diet": "Vegan", "time": 25, "calories": 180, "protein": 4, "carbs": 25, "fat": 8, "fiber": 3, "vitamin_c": 12, "iron": 1.8, "calcium": 25},
        
        # Italian Vegan
        {"name": "Vegan Pasta", "cuisine": "Italian", "diet": "Vegan", "time": 20, "calories": 280, "protein": 10, "carbs": 45, "fat": 6, "fiber": 4, "vitamin_c": 25, "iron": 2.5, "calcium": 60},
        {"name": "Vegan Pizza", "cuisine": "Italian", "diet": "Vegan", "time": 25, "calories": 250, "protein": 8, "carbs": 35, "fat": 8, "fiber": 3, "vitamin_c": 15, "iron": 2.2, "calcium": 80},
        {"name": "Vegan Risotto", "cuisine": "Italian", "diet": "Vegan", "time": 30, "calories": 320, "protein": 8, "carbs": 55, "fat": 8, "fiber": 3, "vitamin_c": 8, "iron": 2.8, "calcium": 40},
        
        # Asian Vegan
        {"name": "Vegan Stir Fry", "cuisine": "Asian", "diet": "Vegan", "time": 15, "calories": 120, "protein": 4, "carbs": 18, "fat": 3, "fiber": 5, "vitamin_c": 55, "iron": 2.2, "calcium": 50},
        {"name": "Vegan Ramen", "cuisine": "Asian", "diet": "Vegan", "time": 20, "calories": 250, "protein": 8, "carbs": 42, "fat": 6, "fiber": 4, "vitamin_c": 35, "iron": 3.5, "calcium": 60},
        {"name": "Vegan Sushi", "cuisine": "Asian", "diet": "Vegan", "time": 30, "calories": 180, "protein": 6, "carbs": 32, "fat": 2, "fiber": 2, "vitamin_c": 20, "iron": 2.8, "calcium": 40},
        
        # Mediterranean Vegan
        {"name": "Vegan Hummus Bowl", "cuisine": "Mediterranean", "diet": "Vegan", "time": 15, "calories": 220, "protein": 10, "carbs": 25, "fat": 8, "fiber": 8, "vitamin_c": 30, "iron": 3.8, "calcium": 80},
        {"name": "Vegan Falafel", "cuisine": "Mediterranean", "diet": "Vegan", "time": 30, "calories": 200, "protein": 8, "carbs": 22, "fat": 8, "fiber": 6, "vitamin_c": 15, "iron": 3.2, "calcium": 60},
        {"name": "Vegan Ratatouille", "cuisine": "Mediterranean", "diet": "Vegan", "time": 35, "calories": 100, "protein": 3, "carbs": 15, "fat": 3, "fiber": 5, "vitamin_c": 50, "iron": 1.8, "calcium": 35},
        
        # Mexican Vegan
        {"name": "Vegan Burrito", "cuisine": "Mexican", "diet": "Vegan", "time": 15, "calories": 280, "protein": 12, "carbs": 42, "fat": 6, "fiber": 10, "vitamin_c": 20, "iron": 4.2, "calcium": 80},
        {"name": "Vegan Tacos", "cuisine": "Mexican", "diet": "Vegan", "time": 20, "calories": 200, "protein": 8, "carbs": 28, "fat": 6, "fiber": 6, "vitamin_c": 25, "iron": 3.5, "calcium": 60},
    ]
    
    # ============================================================================
    # 🥓 KETO RECIPES
    # ============================================================================
    
    keto_recipes = [
        # Keto Meat
        {"name": "Keto Chicken", "cuisine": "American", "diet": "Keto", "time": 25, "calories": 320, "protein": 35, "carbs": 2, "fat": 18, "fiber": 1, "vitamin_c": 5, "iron": 2.8, "calcium": 30},
        {"name": "Keto Steak", "cuisine": "American", "diet": "Keto", "time": 20, "calories": 450, "protein": 42, "carbs": 1, "fat": 28, "fiber": 0, "vitamin_c": 2, "iron": 5.2, "calcium": 20},
        {"name": "Keto Salmon", "cuisine": "American", "diet": "Keto", "time": 15, "calories": 380, "protein": 38, "carbs": 1, "fat": 22, "fiber": 0, "vitamin_c": 3, "iron": 1.5, "calcium": 15},
        {"name": "Keto Bacon", "cuisine": "American", "diet": "Keto", "time": 10, "calories": 280, "protein": 18, "carbs": 1, "fat": 22, "fiber": 0, "vitamin_c": 0, "iron": 1.2, "calcium": 10},
        
        # Keto Vegetarian
        {"name": "Keto Avocado", "cuisine": "American", "diet": "Keto", "time": 5, "calories": 160, "protein": 2, "carbs": 8, "fat": 14, "fiber": 6, "vitamin_c": 10, "iron": 0.6, "calcium": 12},
        {"name": "Keto Cauliflower", "cuisine": "American", "diet": "Keto", "time": 20, "calories": 80, "protein": 3, "carbs": 8, "fat": 4, "fiber": 3, "vitamin_c": 60, "iron": 0.8, "calcium": 25},
        {"name": "Keto Zucchini", "cuisine": "American", "diet": "Keto", "time": 15, "calories": 60, "protein": 2, "carbs": 6, "fat": 3, "fiber": 2, "vitamin_c": 25, "iron": 0.5, "calcium": 20},
        {"name": "Keto Spinach", "cuisine": "American", "diet": "Keto", "time": 10, "calories": 40, "protein": 3, "carbs": 4, "fat": 2, "fiber": 2, "vitamin_c": 35, "iron": 2.8, "calcium": 60},
    ]
    
    # ============================================================================
    # 🥗 HEALTHY/LOW-CALORIE RECIPES
    # ============================================================================
    
    healthy_recipes = [
        # Low Calorie
        {"name": "Grilled Chicken Salad", "cuisine": "American", "diet": "Healthy", "time": 20, "calories": 180, "protein": 25, "carbs": 8, "fat": 6, "fiber": 3, "vitamin_c": 45, "iron": 2.2, "calcium": 80},
        {"name": "Quinoa Bowl", "cuisine": "American", "diet": "Healthy", "time": 25, "calories": 220, "protein": 12, "carbs": 35, "fat": 6, "fiber": 5, "vitamin_c": 30, "iron": 3.8, "calcium": 60},
        {"name": "Green Smoothie", "cuisine": "American", "diet": "Healthy", "time": 5, "calories": 120, "protein": 4, "carbs": 22, "fat": 2, "fiber": 4, "vitamin_c": 80, "iron": 2.5, "calcium": 100},
        {"name": "Oatmeal", "cuisine": "American", "diet": "Healthy", "time": 10, "calories": 150, "protein": 6, "carbs": 25, "fat": 3, "fiber": 4, "vitamin_c": 5, "iron": 2.8, "calcium": 40},
        {"name": "Greek Yogurt", "cuisine": "American", "diet": "Healthy", "time": 2, "calories": 100, "protein": 15, "carbs": 8, "fat": 2, "fiber": 0, "vitamin_c": 2, "iron": 0.5, "calcium": 150},
    ]
    
    # ============================================================================
    # 🍰 DESSERTS
    # ============================================================================
    
    dessert_recipes = [
        # Traditional Desserts
        {"name": "Chocolate Cake", "cuisine": "American", "diet": "Dessert", "time": 45, "calories": 350, "protein": 6, "carbs": 45, "fat": 16, "fiber": 3, "vitamin_c": 2, "iron": 2.8, "calcium": 80},
        {"name": "Apple Pie", "cuisine": "American", "diet": "Dessert", "time": 60, "calories": 320, "protein": 4, "carbs": 42, "fat": 16, "fiber": 4, "vitamin_c": 8, "iron": 1.8, "calcium": 25},
        {"name": "Ice Cream", "cuisine": "American", "diet": "Dessert", "time": 5, "calories": 200, "protein": 4, "carbs": 22, "fat": 10, "fiber": 0, "vitamin_c": 2, "iron": 0.8, "calcium": 120},
        {"name": "Cheesecake", "cuisine": "American", "diet": "Dessert", "time": 90, "calories": 400, "protein": 8, "carbs": 35, "fat": 25, "fiber": 1, "vitamin_c": 1, "iron": 1.2, "calcium": 100},
        
        # Healthy Desserts
        {"name": "Fruit Salad", "cuisine": "American", "diet": "Healthy Dessert", "time": 10, "calories": 80, "protein": 1, "carbs": 18, "fat": 0, "fiber": 3, "vitamin_c": 60, "iron": 0.8, "calcium": 20},
        {"name": "Yogurt Parfait", "cuisine": "American", "diet": "Healthy Dessert", "time": 5, "calories": 120, "protein": 8, "carbs": 18, "fat": 2, "fiber": 2, "vitamin_c": 25, "iron": 1.2, "calcium": 120},
    ]
    
    # ============================================================================
    # 🍳 BREAKFAST RECIPES
    # ============================================================================
    
    breakfast_recipes = [
        # Traditional Breakfast
        {"name": "Pancakes", "cuisine": "American", "diet": "Breakfast", "time": 20, "calories": 250, "protein": 8, "carbs": 35, "fat": 8, "fiber": 2, "vitamin_c": 2, "iron": 2.2, "calcium": 120},
        {"name": "French Toast", "cuisine": "American", "diet": "Breakfast", "time": 15, "calories": 220, "protein": 10, "carbs": 28, "fat": 8, "fiber": 1, "vitamin_c": 1, "iron": 2.8, "calcium": 100},
        {"name": "Scrambled Eggs", "cuisine": "American", "diet": "Breakfast", "time": 10, "calories": 180, "protein": 14, "carbs": 2, "fat": 12, "fiber": 0, "vitamin_c": 0, "iron": 1.8, "calcium": 60},
        {"name": "Omelette", "cuisine": "American", "diet": "Breakfast", "time": 15, "calories": 200, "protein": 16, "carbs": 3, "fat": 14, "fiber": 1, "vitamin_c": 8, "iron": 2.2, "calcium": 80},
        
        # Healthy Breakfast
        {"name": "Smoothie Bowl", "cuisine": "American", "diet": "Healthy Breakfast", "time": 10, "calories": 180, "protein": 6, "carbs": 32, "fat": 4, "fiber": 6, "vitamin_c": 70, "iron": 2.5, "calcium": 80},
        {"name": "Avocado Toast", "cuisine": "American", "diet": "Healthy Breakfast", "time": 5, "calories": 220, "protein": 8, "carbs": 22, "fat": 12, "fiber": 8, "vitamin_c": 15, "iron": 2.8, "calcium": 60},
    ]
    
    # ============================================================================
    # 🍲 SOUPS AND STEWS
    # ============================================================================
    
    soup_recipes = [
        # Traditional Soups
        {"name": "Tomato Soup", "cuisine": "American", "diet": "Soup", "time": 25, "calories": 120, "protein": 4, "carbs": 18, "fat": 4, "fiber": 3, "vitamin_c": 25, "iron": 1.8, "calcium": 40},
        {"name": "Chicken Noodle Soup", "cuisine": "American", "diet": "Soup", "time": 30, "calories": 150, "protein": 12, "carbs": 18, "fat": 4, "fiber": 2, "vitamin_c": 15, "iron": 2.2, "calcium": 30},
        {"name": "Vegetable Soup", "cuisine": "American", "diet": "Soup", "time": 20, "calories": 80, "protein": 3, "carbs": 12, "fat": 2, "fiber": 4, "vitamin_c": 40, "iron": 1.5, "calcium": 25},
        {"name": "Lentil Soup", "cuisine": "American", "diet": "Soup", "time": 35, "calories": 180, "protein": 12, "carbs": 28, "fat": 4, "fiber": 8, "vitamin_c": 20, "iron": 3.8, "calcium": 40},
        
        # International Soups
        {"name": "Miso Soup", "cuisine": "Asian", "diet": "Soup", "time": 10, "calories": 35, "protein": 2, "carbs": 4, "fat": 1, "fiber": 1, "vitamin_c": 5, "iron": 0.8, "calcium": 20},
        {"name": "Pho", "cuisine": "Asian", "diet": "Soup", "time": 45, "calories": 300, "protein": 25, "carbs": 35, "fat": 8, "fiber": 2, "vitamin_c": 15, "iron": 3.2, "calcium": 60},
        {"name": "Gazpacho", "cuisine": "Mediterranean", "diet": "Soup", "time": 15, "calories": 60, "protein": 2, "carbs": 12, "fat": 1, "fiber": 2, "vitamin_c": 45, "iron": 1.2, "calcium": 20},
    ]
    
    # Combine all recipes
    all_recipes = (
        vegetarian_recipes + 
        non_vegetarian_recipes + 
        vegan_recipes + 
        keto_recipes + 
        healthy_recipes + 
        dessert_recipes + 
        breakfast_recipes + 
        soup_recipes
    )
    
    # Create DataFrame
    recipes_df = pd.DataFrame(all_recipes)
    
    # Add recipe IDs
    recipes_df['Recipe_ID'] = [f'R{i+1:03d}' for i in range(len(recipes_df))]
    
    # Reorder columns
    column_order = [
        'Recipe_ID', 'name', 'cuisine', 'diet', 'time', 'calories', 
        'protein', 'carbs', 'fat', 'fiber', 'vitamin_c', 'iron', 'calcium'
    ]
    
    recipes_df = recipes_df[column_order]
    
    # Rename columns to match original format
    recipes_df.columns = [
        'Recipe_ID', 'Recipe_Name', 'Cuisine', 'Diet_Type', 'Cooking_Time', 
        'Calories', 'Protein_g', 'Carbs_g', 'Fat_g', 'Fiber_g', 
        'Vitamin_C_mg', 'Iron_mg', 'Calcium_mg'
    ]
    
    return recipes_df

def enhance_user_profiles():
    """Enhance user profiles with more diverse data"""
    num_users = 100  # Increased from 50
    
    users = pd.DataFrame({
        'User_ID': [f'U{i+1:03d}' for i in range(num_users)],
        'Age': [random.randint(18, 70) for _ in range(num_users)],
        'Gender': [random.choice(['Male', 'Female', 'Other']) for _ in range(num_users)],
        'BMI': [round(random.uniform(16.0, 35.0), 1) for _ in range(num_users)],
        'Health_Condition': [random.choice([
            'None', 'Diabetes', 'Iron Deficiency', 'Vitamin D Deficiency', 
            'High Blood Pressure', 'Heart Disease', 'Obesity', 'Underweight',
            'Food Allergies', 'Digestive Issues', 'High Cholesterol'
        ]) for _ in range(num_users)],
        'Dietary_Restriction': [random.choice([
            'Vegetarian', 'Non-Vegetarian', 'Vegan', 'Keto', 'Paleo',
            'Gluten-Free', 'Dairy-Free', 'Nut-Free', 'Low-Carb', 'High-Protein'
        ]) for _ in range(num_users)],
        'Preferred_Cuisine': [random.choice([
            'Indian', 'Italian', 'Asian', 'Mediterranean', 'Mexican',
            'American', 'Chinese', 'Japanese', 'Thai', 'French', 'Spanish'
        ]) for _ in range(num_users)],
        'Taste_Preference': [random.choice([
            'Spicy', 'Sweet', 'Mild', 'Savory', 'Tangy', 'Bitter',
            'Umami', 'Sour', 'Salty', 'Herbal'
        ]) for _ in range(num_users)]
    })
    
    return users

def enhance_nutrition_data():
    """Enhance nutrition database with more food items"""
    num_foods = 500  # Increased from 300
    
    food_names = [
        # Fruits
        'Apple', 'Banana', 'Orange', 'Grape', 'Strawberry', 'Blueberry', 'Mango', 'Pineapple',
        'Watermelon', 'Kiwi', 'Peach', 'Pear', 'Cherry', 'Plum', 'Apricot', 'Papaya',
        
        # Vegetables
        'Broccoli', 'Spinach', 'Carrot', 'Tomato', 'Cucumber', 'Bell Pepper', 'Onion', 'Garlic',
        'Potato', 'Sweet Potato', 'Cauliflower', 'Cabbage', 'Lettuce', 'Celery', 'Zucchini',
        'Eggplant', 'Asparagus', 'Green Beans', 'Peas', 'Corn', 'Mushroom', 'Radish',
        
        # Proteins
        'Chicken Breast', 'Chicken Thigh', 'Beef', 'Pork', 'Lamb', 'Fish', 'Salmon', 'Tuna',
        'Shrimp', 'Crab', 'Lobster', 'Egg', 'Egg White', 'Tofu', 'Tempeh', 'Paneer',
        'Greek Yogurt', 'Cottage Cheese', 'Milk', 'Cheese', 'Almonds', 'Walnuts', 'Peanuts',
        
        # Grains
        'Rice', 'Brown Rice', 'Quinoa', 'Oats', 'Wheat', 'Barley', 'Bread', 'Pasta',
        'Noodles', 'Couscous', 'Bulgur', 'Millet', 'Buckwheat', 'Rye', 'Cornmeal',
        
        # Legumes
        'Lentils', 'Chickpeas', 'Black Beans', 'Kidney Beans', 'Pinto Beans', 'Soybeans',
        'Green Lentils', 'Red Lentils', 'Split Peas', 'Black-eyed Peas', 'Navy Beans',
        
        # Nuts and Seeds
        'Almonds', 'Walnuts', 'Cashews', 'Pistachios', 'Hazelnuts', 'Pecans', 'Macadamia',
        'Chia Seeds', 'Flax Seeds', 'Sunflower Seeds', 'Pumpkin Seeds', 'Sesame Seeds',
        
        # Dairy and Alternatives
        'Milk', 'Almond Milk', 'Soy Milk', 'Coconut Milk', 'Oat Milk', 'Yogurt',
        'Greek Yogurt', 'Cottage Cheese', 'Ricotta', 'Mozzarella', 'Cheddar', 'Parmesan',
        
        # Oils and Fats
        'Olive Oil', 'Coconut Oil', 'Avocado Oil', 'Butter', 'Ghee', 'Avocado',
        'Olives', 'Coconut', 'Dark Chocolate', 'Cocoa Powder',
        
        # Herbs and Spices
        'Basil', 'Oregano', 'Thyme', 'Rosemary', 'Cilantro', 'Parsley', 'Mint',
        'Ginger', 'Turmeric', 'Cumin', 'Coriander', 'Paprika', 'Chili Powder',
        'Cinnamon', 'Nutmeg', 'Cardamom', 'Cloves', 'Bay Leaves', 'Sage'
    ]
    
    nutrition = pd.DataFrame({
        'Food_ID': [f'F{i+1:03d}' for i in range(num_foods)],
        'Food_Name': [random.choice(food_names) for _ in range(num_foods)],
        'Calories': [random.randint(20, 800) for _ in range(num_foods)],
        'Protein_g': [round(random.uniform(0.1, 50.0), 1) for _ in range(num_foods)],
        'Fat_g': [round(random.uniform(0.1, 40.0), 1) for _ in range(num_foods)],
        'Carbs_g': [round(random.uniform(0.1, 80.0), 1) for _ in range(num_foods)],
        'Fiber_g': [round(random.uniform(0.1, 15.0), 1) for _ in range(num_foods)],
        'Vitamin_C_mg': [round(random.uniform(0.1, 120.0), 1) for _ in range(num_foods)],
        'Iron_mg': [round(random.uniform(0.1, 8.0), 1) for _ in range(num_foods)],
        'Calcium_mg': [round(random.uniform(5.0, 500.0), 1) for _ in range(num_foods)]
    })
    
    return nutrition

def create_enhanced_feedback(users_df, recipes_df):
    """Create enhanced user feedback with more interactions"""
    interactions = []
    
    # Create more diverse interactions
    for _ in range(1000):  # Increased from 500
        user = random.choice(users_df['User_ID'])
        recipe = random.choice(recipes_df['Recipe_ID'])
        
        # More realistic rating distribution
        rating_weights = [0.05, 0.1, 0.15, 0.35, 0.35]  # Fewer 1-2 stars, more 4-5 stars
        rating = random.choices([1, 2, 3, 4, 5], weights=rating_weights)[0]
        
        interactions.append((user, recipe, rating))
    
    feedback = pd.DataFrame(interactions, columns=['User_ID', 'Recipe_ID', 'User_Rating'])
    
    # Remove duplicates
    feedback = feedback.drop_duplicates()
    
    return feedback

def main():
    """Main function to enhance all datasets"""
    print("🍽️ Enhancing AI Food Genius Recipe Database...")
    print("="*60)
    
    # Create enhanced datasets
    print("📝 Creating enhanced recipes...")
    recipes_df = create_enhanced_recipes()
    print(f"✅ Created {len(recipes_df)} diverse recipes")
    
    print("👥 Creating enhanced user profiles...")
    users_df = enhance_user_profiles()
    print(f"✅ Created {len(users_df)} user profiles")
    
    print("🥗 Creating enhanced nutrition data...")
    nutrition_df = enhance_nutrition_data()
    print(f"✅ Created {len(nutrition_df)} food items")
    
    print("💬 Creating enhanced user feedback...")
    feedback_df = create_enhanced_feedback(users_df, recipes_df)
    print(f"✅ Created {len(feedback_df)} user interactions")
    
    # Save enhanced datasets
    print("\n💾 Saving enhanced datasets...")
    recipes_df.to_csv('recipes_enhanced.csv', index=False)
    users_df.to_csv('user_profiles_enhanced.csv', index=False)
    nutrition_df.to_csv('nutrition_enhanced.csv', index=False)
    feedback_df.to_csv('user_feedback_enhanced.csv', index=False)
    
    # Create final merged dataset
    print("🔄 Creating final merged dataset...")
    merged = feedback_df.merge(users_df, on='User_ID', how='left').merge(recipes_df, on='Recipe_ID', how='left')
    
    # Add synthetic scores
    merged['Nutrient_Score'] = np.random.uniform(0.6, 1.0, len(merged))
    merged['Preference_Score'] = np.random.uniform(0.5, 1.0, len(merged))
    merged['Recommended'] = (merged['User_Rating'] > 3).astype(int)
    
    # Save final dataset
    merged.to_csv('final_dataset_enhanced.csv', index=False)
    
    print("✅ Enhanced datasets saved successfully!")
    print(f"📊 Final dataset contains {len(merged)} records")
    
    # Display summary statistics
    print("\n📈 Dataset Summary:")
    print(f"  🍽️ Total Recipes: {len(recipes_df)}")
    print(f"  👥 Total Users: {len(users_df)}")
    print(f"  🥗 Total Food Items: {len(nutrition_df)}")
    print(f"  💬 Total Interactions: {len(feedback_df)}")
    
    print("\n🍽️ Recipe Categories:")
    diet_counts = recipes_df['Diet_Type'].value_counts()
    for diet, count in diet_counts.items():
        print(f"  {diet}: {count} recipes")
    
    print("\n🌍 Cuisine Distribution:")
    cuisine_counts = recipes_df['Cuisine'].value_counts()
    for cuisine, count in cuisine_counts.items():
        print(f"  {cuisine}: {count} recipes")
    
    print("\n🎉 Recipe database enhancement completed!")
    print("🚀 Your AI Food Genius now has a comprehensive recipe collection!")

if __name__ == "__main__":
    main()
