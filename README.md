# Religious Vocation Discernment Quiz

A Django web app that helps users explore which religious charism (Capuchin, Carmelite, Dominican, Benedictine, Augustinian) aligns with their spiritual gifts and values through a 20-question quiz.

## Features

-  Modern, responsive UI with gradient design
-  20-question quiz with instant scoring across 5 charisms
-  Mobile-friendly layout
-  Django ORM with SQLite database
-  Production-ready security settings
-  Deployment-ready (Render / Heroku / any WSGI host)

## Local Setup (Windows PowerShell)

### 1. Clone and activate virtual environment

\\\powershell
git clone <your-repo-url>
cd voca
.\\.venv\\Scripts\\Activate.ps1
\\\

### 2. Create .env file (copy from .env.example)

\\\powershell
Copy-Item .env.example .env
\\\

### 3. Install dependencies

\\\powershell
pip install -r requirements.txt
\\\

### 4. Apply migrations

\\\powershell
python manage.py migrate
python manage.py collectstatic --noinput
\\\

### 5. Run development server

\\\powershell
python manage.py runserver
\\\

Visit http://localhost:8000 in your browser.

## Deployment (Render)

### Prerequisites
- GitHub repository with your code pushed
- Render account (render.com)

### Steps

1. Create new Web Service on Render
   - Connect your GitHub repo
   - Choose Python 3.11

2. Set environment variables in Render dashboard:
   \\\
   DJANGO_SECRET_KEY = (generate: python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')
   DEBUG = False
   ALLOWED_HOSTS = voca.onrender.com
   CSRF_TRUSTED_ORIGINS = https://voca.onrender.com
   \\\

3. Build and start commands
   - Build: \pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput\
   - Start: \gunicorn vocation.wsgi\

4. Wait for deployment and visit your Render URL

## Technology Stack

- Django 6.0.2
- WhiteNoise for static files
- Gunicorn WSGI server
- SQLite (dev) / PostgreSQL (production)
- python-dotenv for environment management

## Security

- SECRET_KEY from environment variables
- DEBUG=False in production
- HTTPS redirects enabled
- HSTS headers configured
- CSRF protection

## Status: Ready for production deployment 
