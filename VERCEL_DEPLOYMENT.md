# 🚀 Vercel Deployment Guide - SK Hostel Management System

## Prerequisites

Before deploying to Vercel, ensure you have:
- A [Vercel account](https://vercel.com) (free)
- A [GitHub account](https://github.com) 
- Git installed on your machine
- The Vercel CLI (optional but recommended)

---

## Step 1: Prepare Your Code for Deployment

### 1.1 Collect Static Files
Run this command to collect all static files:
```bash
python manage.py collectstatic --noinput
```

### 1.2 Update Django Settings
✅ Already done! Your `settings.py` has been configured for Vercel with:
- WhiteNoise middleware for static file serving
- Vercel domain support in ALLOWED_HOSTS
- Security settings for production

### 1.3 Generate a Strong SECRET_KEY
Run this in Python to generate a secure key:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```
Save this key - you'll need it for Vercel environment variables.

---

## Step 2: Push Your Code to GitHub

### 2.1 Initialize Git Repository (if not already done)
```bash
cd c:\Users\saroj\OneDrive\Desktop\scoder\hostel_pg_system
git init
```

### 2.2 Add All Files
```bash
git add .
```

### 2.3 Create Initial Commit
```bash
git commit -m "Initial commit: SK Hostel Management System ready for Vercel"
```

### 2.4 Add Remote Repository
Replace `your-username` and `your-repo` with your GitHub username and repository name:
```bash
git remote add origin https://github.com/your-username/your-repo.git
git branch -M main
git push -u origin main
```

---

## Step 3: Deploy to Vercel

### Option A: Using Vercel Web Dashboard (Easiest)

1. **Go to [Vercel Dashboard](https://vercel.com/dashboard)**
2. **Click "New Project"**
3. **Select "Import Git Repository"**
4. **Connect your GitHub account** and select your repository
5. **Configure Project:**
   - Framework Preset: **Other** (since it's Django)
   - Root Directory: `.` (current directory)
   - Build Command: Leave blank or enter `python manage.py collectstatic --noinput`
   - Output Directory: `staticfiles`

6. **Add Environment Variables** (⚠️ Critical Step):
   Click "Environment Variables" and add:
   
   | Variable | Value |
   |----------|-------|
   | `SECRET_KEY` | Paste the key you generated earlier |
   | `DEBUG` | `False` |
   | `PYTHON_VERSION` | `3.11` |
   | `SITE_URL` | Will be provided by Vercel after deployment |
   
7. **Click "Deploy"**

### Option B: Using Vercel CLI

1. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel:**
   ```bash
   vercel login
   ```

3. **Deploy:**
   ```bash
   cd c:\Users\saroj\OneDrive\Desktop\scoder\hostel_pg_system
   vercel
   ```

4. **Follow the prompts** to configure your project

5. **Add Environment Variables:**
   ```bash
   vercel env add SECRET_KEY
   vercel env add DEBUG
   vercel env add PYTHON_VERSION
   ```

---

## Step 4: Configure Database (Important!)

⚠️ **Current Issue:** Your project uses SQLite, which won't persist on Vercel (serverless environment).

### Solution: Migrate to PostgreSQL

1. **Create a free PostgreSQL database:**
   - Use [ElephantSQL](https://www.elephantsql.com/) (free tier available)
   - Or [Railway](https://railway.app/)
   - Or [Supabase](https://supabase.com/)

2. **Update requirements.txt:**
   ```bash
   pip install psycopg2-binary
   ```

3. **Update settings.py DATABASE section:**
   ```python
   import dj_database_url
   
   if 'DATABASE_URL' in os.environ:
       DATABASES = {
           'default': dj_database_url.config(
               default=os.environ.get('DATABASE_URL'),
               conn_max_age=600
           )
       }
   else:
       DATABASES = {
           'default': {
               'ENGINE': 'django.db.backends.sqlite3',
               'NAME': BASE_DIR / 'db.sqlite3',
           }
       }
   ```

4. **Add DATABASE_URL to Vercel environment variables:**
   - Set it to your PostgreSQL connection string

5. **Run migrations on Vercel:**
   ```bash
   vercel env pull  # Pull environment variables
   python manage.py migrate
   ```

---

## Step 5: Verify Your Deployment

After deployment:

1. **Visit your Vercel URL** (e.g., `https://your-app.vercel.app`)
2. **Check these pages:**
   - Homepage: `https://your-app.vercel.app/`
   - Login: `https://your-app.vercel.app/login/`
   - Register: `https://your-app.vercel.app/register/`

3. **If you see static files not loading:**
   - Run: `python manage.py collectstatic --noinput`
   - Commit and push to GitHub
   - Vercel will auto-redeploy

---

## Troubleshooting

### Issue: Static files not loading (CSS/JS broken)
**Solution:**
```bash
python manage.py collectstatic --noinput
git add .
git commit -m "Update static files"
git push
```

### Issue: 500 Error or Import Errors
1. Check Vercel Logs: Go to your Vercel project → Deployments → click the deployment → View Logs
2. Verify all requirements are in `requirements.txt`
3. Check environment variables are set correctly

### Issue: Database connection error
1. Verify DATABASE_URL is set in Vercel env vars
2. Ensure database user has correct permissions
3. Run migrations: `vercel env pull && python manage.py migrate`

### Issue: ALLOWED_HOSTS error
The `vercel.json` and `settings.py` are already configured. If you get this error:
1. Get your Vercel URL from the deployment
2. Add it to ALLOWED_HOSTS in settings.py
3. Redeploy

---

## Important Security Notes

⚠️ **For Production:**
1. Set `DEBUG = False` (already set in env var)
2. Use a strong `SECRET_KEY` (not the insecure default)
3. Use PostgreSQL instead of SQLite
4. Enable HTTPS (Vercel does this automatically)
5. Set `SECURE_SSL_REDIRECT = True` (already in settings.py)

---

## Next Steps

1. ✅ Confirm Git is initialized and remote added
2. ✅ Push code to GitHub
3. ✅ Create Vercel account and connect GitHub
4. ✅ Deploy through Vercel dashboard
5. ✅ Set environment variables
6. 🔄 Migrate to PostgreSQL (optional but recommended)
7. ✅ Test your deployed site

---

## Useful Links

- [Vercel Django Docs](https://vercel.com/docs/solutions/python)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/)
- [ElephantSQL (Free PostgreSQL)](https://www.elephantsql.com/)
- [Vercel Environment Variables](https://vercel.com/docs/projects/environment-variables)

---

Need help? Check the error message in Vercel Logs or GitHub Issues!
