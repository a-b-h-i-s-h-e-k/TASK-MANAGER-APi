# 📝 Task Manager API

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

A production-ready REST API for managing tasks with full CRUD operations, search, filtering, and pagination. Built with FastAPI, SQLAlchemy, and SQLite.

## ✨ Features

- ✅ **CRUD Operations** - Create, Read, Update, Delete tasks
- 🔍 **Search & Filter** - Search by title and filter by completion status
- 📄 **Pagination** - Built-in pagination for large datasets
- 📚 **Auto Documentation** - Interactive Swagger UI and ReDoc
- 🏥 **Health Check** - Endpoint for monitoring API status
- 📝 **Logging** - Comprehensive request/response logging
- 🔐 **Input Validation** - Pydantic models with field validation
- 🚀 **High Performance** - Built on FastAPI (as fast as NodeJS and Go)

## 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| **FastAPI** | Modern web framework for building APIs |
| **SQLAlchemy** | SQL toolkit and ORM |
| **Pydantic** | Data validation using Python type hints |
| **SQLite** | Lightweight disk-based database |
| **Uvicorn** | Lightning-fast ASGI server |

## 📋 API Endpoints

| Method | Endpoint | Description | Request Body | Response |
|--------|----------|-------------|--------------|----------|
| `POST` | `/tasks/` | Create a new task | Task data | Created task |
| `GET` | `/tasks/` | Get all tasks (with filters) | - | List of tasks |
| `GET` | `/tasks/{id}` | Get a specific task | - | Single task |
| `PUT` | `/tasks/{id}` | Update task status | Status | Updated task |
| `DELETE` | `/tasks/{id}` | Delete a task | - | 204 No Content |
| `GET` | `/health` | Health check | - | Status OK |

## 📁 Project Structure

task-manager-api/
├── app/
│ ├── init.py
│ ├── main.py # Application entry point
│ ├── database.py # Database configuration
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic schemas
│ ├── services.py # Business logic layer
│ ├── exceptions.py # Custom exceptions
│ └── routes/
│ ├── init.py
│ └── tasks.py # API endpoints
├── requirements.txt # Project dependencies
├── tasks.db # SQLite database
├── Dockerfile # Docker configuration
├── docker-compose.yml # Docker Compose setup
└── README.md # Project documentation



## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- virtualenv (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/task-manager-api.git
   cd task-manager-api


2. **Create and activate virtual environment**

# Linux/Mac
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate

3. **Install dependencies**
 pip install -r requirements.txt

4. **Run the application**

uvicorn app.main:app --reload


5. **Access the API**

- API: http://localhost:8000
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc


### 📖 API Documentation

1. Create a Task

POST /tasks/
Content-Type: application/json

{
    "title": "Learn FastAPI",
    "description": "Complete the FastAPI tutorial"
}


### Response (201 Created)

json
{
    "id": 1,
    "title": "Learn FastAPI",
    "description": "Complete the FastAPI tutorial",
    "completed": false
}

### Get All Tasks

GET /tasks/?skip=0&limit=10&completed=false&search=fastapi


## Query Parameters


Parameter	        Type	         Default	           Description
skip	            int	               0	           Number of tasks to skip (pagination)
limit	            int	               10	           Maximum tasks to return
completed	        bool	          null	           Filter by completion status
search	            string	          null	           Search in task titles (case-insensitive)


### Get a Single Task

GET /tasks/{id}

### Response (200 OK)

json
{
    "id": 1,
    "title": "Learn FastAPI",
    "description": "Complete the FastAPI tutorial",
    "completed": false
}


### Update a Task

PUT /tasks/{id}?completed=true

### Response (200 OK)

json
{
    "id": 1,
    "title": "Learn FastAPI",
    "description": "Complete the FastAPI tutorial",
    "completed": true
}


### Delete a Task

DELETE /tasks/{id}

### Response (204 No Content) - No response body

### Health Check

GET /health


### Response (200 OK)

json
{
    "status": "ok"
}









