#!/usr/bin/env python3
"""
🚀 AI FOOD GENIUS - ENHANCED LAUNCHER
=====================================

This script launches the extraordinary AI Food Genius platform with all advanced features.
It handles setup, configuration, and provides a beautiful startup experience.

Author: AI Assistant
Version: 2.0 - Extraordinary Edition
"""

import os
import sys
import subprocess
import time
import webbrowser
from pathlib import Path
import streamlit as st

def print_banner():
    """Print the beautiful startup banner"""
    banner = """
    ╔══════════════════════════════════════════════════════════════════════════════╗
    ║                                                                              ║
    ║  🍽️  AI FOOD GENIUS - EXTRAORDINARY EDITION  🍽️                            ║
    ║                                                                              ║
    ║  🚀 The most advanced AI-powered food recommendation platform               ║
    ║  ✨ Featuring cutting-edge ML, real-time APIs, and stunning UI             ║
    ║  🤖 Powered by ensemble AI models and advanced analytics                   ║
    ║  👥 Social features, meal planning, and computer vision                    ║
    ║                                                                              ║
    ║  Version: 2.0 - Extraordinary Edition                                       ║
    ║  Author: AI Assistant                                                       ║
    ║                                                                              ║
    ╚══════════════════════════════════════════════════════════════════════════════╝
    """
    print(banner)

def check_requirements():
    """Check if all requirements are installed"""
    print("🔍 Checking requirements...")
    
    required_packages = [
        'streamlit', 'pandas', 'numpy', 'scikit-learn', 'xgboost',
        'plotly', 'seaborn', 'matplotlib', 'requests', 'pillow'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"  ✅ {package}")
        except ImportError:
            missing_packages.append(package)
            print(f"  ❌ {package}")
    
    if missing_packages:
        print(f"\n⚠️  Missing packages: {', '.join(missing_packages)}")
        print("📦 Installing missing packages...")
        
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + missing_packages)
            print("✅ All packages installed successfully!")
        except subprocess.CalledProcessError:
            print("❌ Failed to install packages. Please run: pip install -r requirements.txt")
            return False
    
    return True

def check_data_files():
    """Check if data files exist"""
    print("\n📊 Checking data files...")
    
    required_files = [
        'final_dataset.csv',
        'user_profiles.csv',
        'recipes.csv',
        'nutrition.csv',
        'user_feedback.csv'
    ]
    
    missing_files = []
    
    for file in required_files:
        if os.path.exists(file):
            print(f"  ✅ {file}")
        else:
            missing_files.append(file)
            print(f"  ❌ {file}")
    
    if missing_files:
        print(f"\n⚠️  Missing data files: {', '.join(missing_files)}")
        print("🔄 Generating sample data...")
        
        try:
            subprocess.check_call([sys.executable, 'h1.py'])
            print("✅ Sample data generated successfully!")
        except subprocess.CalledProcessError:
            print("❌ Failed to generate data. Please run: python h1.py")
            return False
    
    return True

def check_configuration():
    """Check configuration and setup"""
    print("\n⚙️  Checking configuration...")
    
    # Check if config.py exists
    if os.path.exists('config.py'):
        print("  ✅ Configuration file found")
    else:
        print("  ❌ Configuration file missing")
        return False
    
    # Check if advanced_features.py exists
    if os.path.exists('advanced_features.py'):
        print("  ✅ Advanced features module found")
    else:
        print("  ❌ Advanced features module missing")
        return False
    
    # Check if app_enhanced.py exists
    if os.path.exists('app_enhanced.py'):
        print("  ✅ Enhanced application found")
    else:
        print("  ❌ Enhanced application missing")
        return False
    
    return True

def setup_environment():
    """Set up environment variables and configuration"""
    print("\n🌍 Setting up environment...")
    
    # Create .env file if it doesn't exist
    if not os.path.exists('.env'):
        print("  📝 Creating .env file...")
        with open('.env', 'w') as f:
            f.write("""# AI Food Genius - Environment Variables
# API Keys (optional - demo mode works without them)
SPOONACULAR_API_KEY=demo_key
EDAMAM_APP_ID=demo_id
EDAMAM_APP_KEY=demo_key
YOUTUBE_API_KEY=demo_key
OPENAI_API_KEY=demo_key
GOOGLE_VISION_API_KEY=demo_key

# Database (optional)
DATABASE_URL=sqlite:///food_genius.db

# Security
SECRET_KEY=your_secret_key_here
""")
        print("  ✅ .env file created")
    else:
        print("  ✅ .env file exists")
    
    # Create logs directory
    if not os.path.exists('logs'):
        os.makedirs('logs')
        print("  ✅ Logs directory created")
    else:
        print("  ✅ Logs directory exists")

def launch_application():
    """Launch the Streamlit application"""
    print("\n🚀 Launching AI Food Genius...")
    print("  🌐 Opening browser...")
    print("  📱 Application will be available at: http://localhost:8501")
    print("  ⏹️  Press Ctrl+C to stop the application")
    print("\n" + "="*80)
    
    try:
        # Launch Streamlit
        subprocess.run([
            sys.executable, '-m', 'streamlit', 'run', 'app_enhanced.py',
            '--server.port', '8501',
            '--server.address', 'localhost',
            '--browser.gatherUsageStats', 'false',
            '--server.headless', 'false'
        ])
    except KeyboardInterrupt:
        print("\n\n👋 AI Food Genius stopped. Thank you for using our platform!")
    except Exception as e:
        print(f"\n❌ Error launching application: {e}")
        print("💡 Try running: streamlit run app_enhanced.py")

def show_features():
    """Show available features"""
    features = """
    🎯 AVAILABLE FEATURES:
    
    🤖 AI Recommendations
    ├── Ensemble ML Models (RandomForest, XGBoost, Neural Networks)
    ├── Collaborative Filtering
    ├── Content-Based Filtering
    ├── Real-time Personalization
    └── Hybrid Recommendation Engine
    
    🌐 Real-time APIs
    ├── Spoonacular Recipe API
    ├── Edamam Nutrition API
    ├── YouTube Cooking Videos
    ├── OpenAI Natural Language Processing
    └── Google Vision Food Recognition
    
    👥 Social Features
    ├── User Reviews & Ratings
    ├── Social Following
    ├── Recipe Sharing
    ├── Community Insights
    └── Social Recommendations
    
    📅 Meal Planning
    ├── Smart Meal Planning
    ├── Grocery List Generation
    ├── Nutritional Goal Tracking
    ├── Dietary Restriction Management
    └── Seasonal Recommendations
    
    👁️ Computer Vision
    ├── Food Recognition from Photos
    ├── Nutritional Analysis
    ├── Barcode Scanning
    ├── Smart Substitutions
    └── Voice Search
    
    📊 Advanced Analytics
    ├── User Behavior Analysis
    ├── Nutritional Insights
    ├── Trending Analysis
    ├── Performance Metrics
    └── Personalized Reports
    
    🎨 Beautiful UI/UX
    ├── Modern Design with Animations
    ├── Responsive Layout
    ├── Dark/Light Themes
    ├── Interactive Charts
    └── Real-time Updates
    """
    print(features)

def main():
    """Main function"""
    print_banner()
    
    print("🔧 Initializing AI Food Genius...")
    
    # Check requirements
    if not check_requirements():
        print("❌ Requirements check failed. Please install missing packages.")
        return
    
    # Check data files
    if not check_data_files():
        print("❌ Data files check failed. Please generate sample data.")
        return
    
    # Check configuration
    if not check_configuration():
        print("❌ Configuration check failed. Please ensure all files are present.")
        return
    
    # Setup environment
    setup_environment()
    
    # Show features
    show_features()
    
    print("\n✅ All checks passed! AI Food Genius is ready to launch.")
    
    # Ask user if they want to launch
    try:
        response = input("\n🚀 Launch AI Food Genius now? (y/n): ").lower().strip()
        if response in ['y', 'yes', '']:
            launch_application()
        else:
            print("👋 AI Food Genius is ready. Run 'streamlit run app_enhanced.py' when you're ready!")
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")

if __name__ == "__main__":
    main()
