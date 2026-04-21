# 🚀 Hostel Management System - PythonAnywhere Deployment Guide

## Step 1: Prepare Your Code

### Collect Static Files
```bash
cd c:\Users\saroj\OneDrive\Desktop\scoder\hostel_pg_system
python manage.py collectstatic --noinput
```

### Create a .gitignore file
```bash
# Create .gitignore
*.pyc
__pycache__/
*.sqlite3
.env
venv/
staticfiles/
.DS_Store
```

## Step 2: Create PythonAnywhere Account

1. Go to https://www.pythonanywhere.com/
2. Sign up for a free account (Free tier available)
3. Verify your email
4. Log in to your PythonAnywhere dashboard

## Step 3: Upload Code to PythonAnywhere

### Option A: Using Git (Recommended)
1. Push your code to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/hostel-management.git
   git push -u origin main
   ```

2. In PythonAnywhere console:
   ```bash
   git clone https://github.com/yourusername/hostel-management.git
   ```

### Option B: Upload Zip File
1. Zip your project folder
2. Upload via PythonAnywhere web interface
3. Extract in your home directory

## Step 4: Create Virtual Environment on PythonAnywhere

In PythonAnywhere Bash Console:
```bash
mkvirtualenv --python=/usr/bin/python3.11 hostel_env
pip install Django==6.0.4
pip install -r hostel-management/requirements.txt
```

## Step 5: Configure Web App

1. Go to **Web** tab in PythonAnywhere dashboard
2. Click "Add a new web app"
3. Choose **Manual configuration** → Python 3.11
4. After creation, update settings:

### WSGI Configuration
Click on WSGI configuration file and replace with:

```python
# /var/www/yourusername_pythonanywhere_com_wsgi.py
import os
import sys

# Add your project directory to the sys.path
project_home = '/home/yourusername/hostel-management'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'hostel_pg_system.settings'

# Import Django application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### Virtualenv Path
Set to: `/home/yourusername/.virtualenvs/hostel_env`

## Step 6: Configure Static Files

In PythonAnywhere Web tab, add URL mapping:
- URL: `/static/`
- Directory: `/home/yourusername/hostel-management/staticfiles`

## Step 7: Update Django Settings

Update ALLOWED_HOSTS in settings.py:
```python
ALLOWED_HOSTS = ['yourusername.pythonanywhere.com', 'localhost']
```

## Step 8: Create Database on PythonAnywhere

In PythonAnywhere Bash Console:
```bash
cd /home/yourusername/hostel-management
python manage.py migrate
python manage.py createsuperuser
```

## Step 9: Reload Web App

Click "Reload" button in Web tab to restart your web app.

## Step 10: Test Your Deployment

Visit: `https://yourusername.pythonanywhere.com`

You should see your hostel management system running!

---

## Common Issues & Solutions

### Issue: Static files not showing
**Solution**: Run `python manage.py collectstatic --noinput` and update STATIC_ROOT path

### Issue: Database errors
**Solution**: Re-run migrations: `python manage.py migrate`

### Issue: Permission denied errors
**Solution**: Check file permissions: `chmod -R 755 hostel-management/`

### Issue: "ModuleNotFoundError"
**Solution**: Ensure virtualenv path is correct and all packages are installed

---

## Management Commands

Once deployed, you can use PythonAnywhere Bash Console:

```bash
# Create backup
python manage.py dumpdata > backup.json

# Restore backup
python manage.py loaddata backup.json

# Create new admin user
python manage.py createsuperuser

# Check system
python manage.py check

# Clear cache
python manage.py clear_cache
```

---

## Monitoring & Updates

### View error logs
In PythonAnywhere Web tab, check:
- Server log
- Error log  
- Access log

### Update code
```bash
cd hostel-management
git pull origin main
python manage.py migrate
python manage.py collectstatic --noinput
# Then reload web app
```

---

## Production Checklist

- ✅ Set `DEBUG = False` (Already configured via settings.py)
- ✅ Set `ALLOWED_HOSTS` properly
- ✅ Collect static files
- ✅ Set up SSL/HTTPS (PythonAnywhere provides free SSL)
- ✅ Create superuser account
- ✅ Run database migrations
- ✅ Test all features
- ✅ Set up backup system
- ✅ Configure email (optional)

---

## Quick Reference

| Item | Value |
|------|-------|
| Django Version | 6.0.4 |
| Python Version | 3.11+ |
| Database | SQLite3 |
| Web Framework | Django 6 |
| Server | PythonAnywhere |

---

## Support

For more help:
- PythonAnywhere Docs: https://help.pythonanywhere.com/
- Django Docs: https://docs.djangoproject.com/en/6.0/
- GitHub Issues: Create an issue in your repository

---

**Deployment completed! 🎉**

Your hostel management system is now live on the internet!
