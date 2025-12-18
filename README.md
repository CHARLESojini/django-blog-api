# Django Blog API
## Live Demo

- **API Base URL:** https://django-blog-api-0q1s.onrender.com/api/
- **Swagger Documentation:** https://django-blog-api-0q1s.onrender.com/swagger/
- **ReDoc:** https://django-blog-api-0q1s.onrender.com/redoc/
- **Posts Endpoint:** https://django-blog-api-0q1s.onrender.com/api/posts/
## Authentication

This API uses JWT (JSON Web Token) authentication.

### How to Authenticate:

1. **Register** a new user:
```bash
   POST /api/users/register/
   {
     "username": "yourname",
     "email": "your@email.com",
     "password": "yourpassword",
     "password_confirm": "yourpassword"
   }
```

2. **Login** to get tokens:
```bash
   POST /api/users/login/
   {
     "username": "yourname",
     "password": "yourpassword"
   }
```
   Response:
```json
   {
     "access": "eyJhbGciOiJIUzI1NiIs...",
     "refresh": "eyJhbGciOiJIUzI1NiIs..."
   }
```

3. **Use the access token** in protected requests:
```
   Authorization: Bearer <your_access_token>
```

### Protected Endpoints (Require Authentication):
- Create, update, delete posts
- Like/unlike posts
- Create, update, delete comments

### Public Endpoints (No Authentication):
- View all posts
- View single post
- View comments

A RESTful Blog Application API built with Django REST Framework and PostgreSQL.

## Features

- User authentication (JWT-based signup/login)
- Create, read, update, delete blog posts
- Like/unlike blog posts
- Comment on blog posts
- Image upload for cover photos
- Paginated responses
- Swagger API documentation

## Tech Stack

- Python 3.13
- Django 6.0
- Django REST Framework
- PostgreSQL
- JWT Authentication (SimpleJWT)
- drf-yasg (Swagger documentation)

## Installation

### Prerequisites

- Python 3.10+
- PostgreSQL

### Setup

1. Clone the repository:
```bash
   git clone https://github.com/YOUR_USERNAME/django-blog-api.git
   cd django-blog-api
```

2. Create virtual environment:
```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

4. Create `.env` file:
```
   DEBUG=True
   SECRET_KEY=your-secret-key
   DATABASE_NAME=blog_db
   DATABASE_USER=postgres
   DATABASE_PASSWORD=your_password
   DATABASE_HOST=localhost
   DATABASE_PORT=5432
```

5. Create database:
```bash
   psql -U postgres
   CREATE DATABASE blog_db;
   \q
```

6. Run migrations:
```bash
   python manage.py migrate
```

7. Start the server:
```bash
   python manage.py runserver
```
## Docker Setup (Alternative)

1. Make sure Docker is installed and running

2. Build and start containers:
```bash
   docker-compose up --build
```

3. Run migrations (in a new terminal):
```bash
   docker-compose exec web python manage.py migrate
```

4. Access the API at `http://localhost:8000`

5. Stop containers:
```bash
   docker-compose down
```

## API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/users/register/` | Register new user |
| POST | `/api/users/login/` | Login and get JWT token |
| POST | `/api/users/token/refresh/` | Refresh JWT token |
| GET | `/api/users/profile/` | Get user profile |

### Blog Posts
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/posts/` | List all posts |
| POST | `/api/posts/` | Create new post |
| GET | `/api/posts/{id}/` | Get single post |
| PUT | `/api/posts/{id}/` | Update post |
| DELETE | `/api/posts/{id}/` | Delete post |
| POST | `/api/posts/{id}/like/` | Like/unlike post |

### Comments
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/comments/post/{post_id}/` | List comments for a post |
| POST | `/api/comments/post/{post_id}/` | Add comment to post |
| GET | `/api/comments/{id}/` | Get single comment |
| PUT | `/api/comments/{id}/` | Update comment |
| DELETE | `/api/comments/{id}/` | Delete comment |

## API Documentation

- Swagger UI: `http://127.0.0.1:8000/swagger/`
- ReDoc: `http://127.0.0.1:8000/redoc/`

## Author

Chima Charles Ojini