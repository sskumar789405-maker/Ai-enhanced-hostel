#!/usr/bin/env python
"""
Hostel Management System - Deployment Helper
Prepares the project for PythonAnywhere deployment
"""

import os
import sys
import subprocess
from pathlib import Path

def print_header(text):
    """Print formatted header"""
    print("\n" + "="*70)
    print(f"  {text}")
    print("="*70 + "\n")

def print_step(number, text):
    """Print step number"""
    print(f"[{number}] {text}")

def run_command(cmd, description):
    """Run shell command with error handling"""
    print(f"  → {description}...")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"  ✅ {description}")
            return True
        else:
            print(f"  ❌ {description}")
            print(f"  Error: {result.stderr}")
            return False
    except Exception as e:
        print(f"  ❌ {description}")
        print(f"  Exception: {e}")
        return False

def main():
    """Main deployment preparation"""
    print_header("🚀 HOSTEL MANAGEMENT SYSTEM - DEPLOYMENT PREPARATION")
    
    # Get project root
    project_root = Path.cwd()
    print(f"Project root: {project_root}\n")
    
    # Step 1: System checks
    print_step(1, "Running Django System Checks")
    run_command("python manage.py check", "System checks")
    
    # Step 2: Collect static files
    print_step(2, "Collecting Static Files")
    run_command(
        "python manage.py collectstatic --noinput",
        "Static file collection"
    )
    
    # Step 3: Generate requirements
    print_step(3, "Generating Requirements File")
    print("  → Creating requirements.txt...")
    try:
        with open("requirements.txt", "w") as f:
            f.write("""Django==6.0.4
asgiref==3.11.1
sqlparse==0.5.2
tzdata==2024.2
gunicorn==21.2.0
psycopg2-binary==2.9.9
whitenoise==6.6.0
python-dotenv==1.0.0
""")
        print("  ✅ requirements.txt created")
    except Exception as e:
        print(f"  ❌ Error creating requirements.txt: {e}")
    
    # Step 4: Check for necessary files
    print_step(4, "Verifying Deployment Files")
    necessary_files = [
        "README.md",
        "DEPLOYMENT_GUIDE.md",
        "QUICK_DEPLOY.md",
        ".gitignore",
        "requirements.txt",
        "runtime.txt"
    ]
    
    for file in necessary_files:
        if Path(file).exists():
            print(f"  ✅ {file} present")
        else:
            print(f"  ⚠️  {file} missing")
    
    # Step 5: Test database
    print_step(5, "Testing Database")
    run_command("python manage.py migrate --check", "Database check")
    
    # Step 6: Summary
    print_header("✨ DEPLOYMENT PREPARATION COMPLETE")
    
    print("""
Your project is ready for deployment! 🎉

Next steps:

1. Create a GitHub repository:
   git init
   git add .
   git commit -m "Ready for deployment"
   git remote add origin https://github.com/yourusername/hostel-management.git
   git push -u origin main

2. Follow QUICK_DEPLOY.md for PythonAnywhere setup

3. Or read DEPLOYMENT_GUIDE.md for detailed instructions

For questions, check README.md or DEPLOYMENT_GUIDE.md

Happy deploying! 🚀
    """)

if __name__ == "__main__":
    main()
