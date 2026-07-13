# Django Portfolio Website

A full-featured portfolio website built with **Django**, **Django REST Framework**, and **PostgreSQL**.

## Features

✅ **Portfolio Management** - Showcase your projects with categories, images, and links  
✅ **Blog System** - Write and publish blog posts with categories and tags  
✅ **Contact Form** - Receive and manage contact messages with email notifications  
✅ **Admin Dashboard** - Comprehensive Django admin interface for content management  
✅ **REST API** - Full REST API for frontend integration  
✅ **JWT Authentication** - Secure API endpoints with JWT tokens  
✅ **PostgreSQL Database** - Robust and scalable database backend  
✅ **Responsive Design** - Mobile-friendly admin interface  

## Project Structure

```
portfolio-django/
├── config/                    # Django configuration
│   ├── settings.py           # Settings
│   ├── urls.py               # URL routing
│   └── wsgi.py               # WSGI application
├── apps/
│   ├── core/                 # Core utilities (Skills, Social Links)
│   ├── portfolio/            # Portfolio projects
│   ├── blog/                 # Blog system
│   └── contact/              # Contact form
├── media/                     # User uploaded files
├── staticfiles/               # Static files
├── manage.py                  # Django management
├── requirements.txt           # Python dependencies
├── .env.example               # Environment variables template
├── nginx/                     # Nginx Configuration
├── Dockerfile                 # Docker Image Configureation
├── comopose.yaml              # Container Configuration
└── README.md                  # This file
```

## Installation

### Prerequisites

- Python 3.8+
- PostgreSQL 12+
- pip and virtualenv

### Setup Steps

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd portfolio-django
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create PostgreSQL database**:
   ```bash
   createdb portfolio_db
   createuser portfolio_user
   ```

5. **Configure environment**:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

6. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

7. **Create superuser**:
   ```bash
   python manage.py createsuperuser
   ```

8. **Run development server**:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

- **Admin**: `http://localhost:8000/admin/`
- **API**: `http://localhost:8000/api/`
- **Portfolio**: `/api/portfolio/projects/`
- **Blog**: `/api/blog/posts/`
- **Contact**: `/api/contact/messages/`
- **Skills**: `/api/core/skills/`

## Technologies

- Django 4.2
- Django REST Framework 3.14
- PostgreSQL
- JWT Authentication
- Pillow (Image processing)

## License

MIT
