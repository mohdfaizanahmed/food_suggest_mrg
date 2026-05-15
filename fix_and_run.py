#!/usr/bin/env python3
"""
🔧 AI FOOD GENIUS - FIX AND RUN SCRIPT
======================================

This script fixes the configuration issues and runs the appropriate version
of the AI Food Genius platform based on available dependencies.

Author: AI Assistant
Version: 2.0 - Fix Edition
"""

import os
import sys
import subprocess
import importlib.util

def check_dependencies():
    """Check which dependencies are available"""
    dependencies = {
        'streamlit': False,
        'pandas': False,
        'numpy': False,
        'scikit-learn': False,
        'xgboost': False,
        'plotly': False,
        'tensorflow': False,
        'torch': False,
        'transformers': False
    }
    
    for dep in dependencies:
        try:
            importlib.import_module(dep)
            dependencies[dep] = True
        except ImportError:
            dependencies[dep] = False
    
    return dependencies

def create_streamlit_config():
    """Create Streamlit configuration files"""
    # Create .streamlit directory if it doesn't exist
    if not os.path.exists('.streamlit'):
        os.makedirs('.streamlit')
        print("✅ Created .streamlit directory")
    
    # Create secrets.toml if it doesn't exist
    secrets_path = '.streamlit/secrets.toml'
    if not os.path.exists(secrets_path):
        with open(secrets_path, 'w') as f:
            f.write("""# AI Food Genius - Streamlit Secrets Configuration
# Demo configuration - replace with real API keys for production

SPOONACULAR_API_KEY = "demo_key"
EDAMAM_APP_ID = "demo_id"
EDAMAM_APP_KEY = "demo_key"
YOUTUBE_API_KEY = "demo_key"
OPENAI_API_KEY = "demo_key"
GOOGLE_VISION_API_KEY = "demo_key"
DATABASE_URL = "sqlite:///food_genius.db"
SECRET_KEY = "demo_secret_key"
""")
        print("✅ Created secrets.toml file")
    
    # Create config.toml if it doesn't exist
    config_path = '.streamlit/config.toml'
    if not os.path.exists(config_path):
        with open(config_path, 'w') as f:
            f.write("""[global]
developmentMode = false

[server]
headless = false
port = 8501
enableCORS = false
enableXsrfProtection = true

[browser]
gatherUsageStats = false
serverAddress = "localhost"

[theme]
primaryColor = "#667eea"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "Inter"

[client]
showErrorDetails = true
toolbarMode = "minimal"

[runner]
magicEnabled = true
installTracer = false
fixMatplotlib = true
""")
        print("✅ Created config.toml file")

def check_data_files():
    """Check if data files exist"""
    required_files = [
        'final_dataset.csv',
        'user_profiles.csv',
        'recipes.csv',
        'nutrition.csv',
        'user_feedback.csv'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"⚠️ Missing data files: {', '.join(missing_files)}")
        print("🔄 Generating sample data...")
        try:
            subprocess.run([sys.executable, 'h1.py'], check=True)
            print("✅ Sample data generated successfully!")
        except subprocess.CalledProcessError:
            print("❌ Failed to generate data. Please run: python h1.py")
            return False
    else:
        print("✅ All data files found")
    
    return True

def determine_app_version():
    """Determine which app version to run based on available dependencies"""
    deps = check_dependencies()
    
    # Check for advanced dependencies
    advanced_deps = ['tensorflow', 'torch', 'transformers']
    has_advanced = all(deps[dep] for dep in advanced_deps)
    
    # Check for basic dependencies
    basic_deps = ['streamlit', 'pandas', 'numpy', 'scikit-learn', 'xgboost', 'plotly']
    has_basic = all(deps[dep] for dep in basic_deps)
    
    if has_advanced and has_basic:
        return 'enhanced'
    elif has_basic:
        return 'simple'
    else:
        return 'basic'

def install_missing_dependencies():
    """Install missing basic dependencies"""
    basic_deps = ['streamlit', 'pandas', 'numpy', 'scikit-learn', 'xgboost', 'plotly']
    missing = []
    
    for dep in basic_deps:
        try:
            importlib.import_module(dep)
        except ImportError:
            missing.append(dep)
    
    if missing:
        print(f"📦 Installing missing dependencies: {', '.join(missing)}")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + missing)
            print("✅ Dependencies installed successfully!")
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to install dependencies")
            return False
    
    return True

def run_application(app_version):
    """Run the appropriate application version"""
    print(f"🚀 Running AI Food Genius - {app_version.title()} Edition")
    
    if app_version == 'enhanced':
        app_file = 'app_enhanced.py'
        port = 8501
    elif app_version == 'simple':
        app_file = 'app_simple.py'
        port = 8502
    else:
        app_file = 'h2.py'  # Original basic version
        port = 8503
    
    print(f"📱 Application will be available at: http://localhost:{port}")
    print("⏹️ Press Ctrl+C to stop the application")
    print("="*60)
    
    try:
        subprocess.run([
            sys.executable, '-m', 'streamlit', 'run', app_file,
            '--server.port', str(port),
            '--server.address', 'localhost',
            '--browser.gatherUsageStats', 'false'
        ])
    except KeyboardInterrupt:
        print("\n👋 AI Food Genius stopped. Thank you for using our platform!")
    except Exception as e:
        print(f"\n❌ Error running application: {e}")

def main():
    """Main function"""
    print("🔧 AI Food Genius - Fix and Run Script")
    print("="*50)
    
    # Create Streamlit configuration
    create_streamlit_config()
    
    # Check data files
    if not check_data_files():
        print("❌ Data setup failed. Please check the errors above.")
        return
    
    # Check dependencies
    deps = check_dependencies()
    print("\n📋 Dependency Status:")
    for dep, available in deps.items():
        status = "✅" if available else "❌"
        print(f"  {status} {dep}")
    
    # Determine app version
    app_version = determine_app_version()
    print(f"\n🎯 Recommended app version: {app_version.title()}")
    
    # Install missing basic dependencies if needed
    if app_version == 'basic':
        if not install_missing_dependencies():
            print("❌ Failed to install dependencies. Please install manually.")
            return
        app_version = 'simple'  # Upgrade to simple after installing deps
    
    # Ask user which version to run
    print(f"\n🚀 Available versions:")
    print("1. Enhanced Edition (requires advanced ML libraries)")
    print("2. Simple Edition (beautiful UI with basic ML)")
    print("3. Basic Edition (original version)")
    
    try:
        choice = input(f"\nWhich version would you like to run? (1/2/3) [default: {app_version}]: ").strip()
        
        if choice == '1':
            app_version = 'enhanced'
        elif choice == '2':
            app_version = 'simple'
        elif choice == '3':
            app_version = 'basic'
        elif choice == '':
            pass  # Use default
        else:
            print("Invalid choice, using default")
    
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
        return
    
    # Run the application
    run_application(app_version)

if __name__ == "__main__":
    main()
