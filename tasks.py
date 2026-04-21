# from fastapi import APIRouter, Depends, HTTPException -> removing HTTp exception becoz we added not_found import in file
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import crud, schemas
#from ..database import SessionLocal, get_db
from ..database import SessionLocal
from ..exceptions import not_found
from ..logger import logger


# ==================== ROUTER SETUP ====================

router = APIRouter(prefix="/tasks", tags=["Tasks"])

# ==================== DATABASE DEPENDENCY ====================

# Note: If you have get_db in database.py, import it. Otherwise, define it here:
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 3. Depends()

db: Session = Depends(get_db)

# ==================== 1. POST /tasks/ - CREATE TASK ====================

@router.post(
    "/",
    response_model=schemas.TaskResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new task",
    description="Create a task with title and optional description"
)
def create_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new task.
    
    - **title**: Required, 3-100 characters
    - **description**: Optional, max 300 characters
    """
    return crud.create_task(db, task)


# ==================== 2. GET /tasks/ - GET ALL TASKS ====================

@router.get(
    "/",
    response_model=list[schemas.TaskResponse],
    summary="Get all tasks",
    description="""Retrieve all tasks with optional filtering and pagination.
    
    Features:
    - Pagination: Control how many tasks to return
    - Filter by completion status: Get only completed or pending tasks
    - Search: Find tasks by title (case-insensitive partial match)
    """
)
def read_tasks(
    skip: int = 0,
    limit: int = 10,
    completed: bool | None = None,
    search: str | None = None,
    db: Session = Depends(get_db)
):
    """
    Get all tasks with optional filters.
    
    Query Parameters:
    - **skip**: Number of tasks to skip (default: 0)
    - **limit**: Maximum tasks to return (default: 10)
    - **completed**: Filter by status (true/false)
    - **search**: Search term in title (case-insensitive)
    
    Example requests:
    - `GET /tasks/` - Get first 10 tasks
    - `GET /tasks/?skip=10&limit=20` - Get tasks 11-30
    - `GET /tasks/?completed=true` - Get only completed tasks
    - `GET /tasks/?search=fastapi` - Search tasks with "fastapi"
    """
    return crud.get_tasks(
        db=db,
        skip=skip,
        limit=limit,
        completed=completed,
        search=search,
    )


# ==================== 3. GET /tasks/{task_id} - GET SINGLE TASK ====================

@router.get(
    "/{task_id}",
    response_model=schemas.TaskResponse,
    summary="Get a specific task",
    description="Get a single task by its ID"
)
def read_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    """
    Get a task by ID.
    
    - **task_id**: ID of the task to retrieve
    """
    task = crud.get_task(db, task_id)
    if not task:
        raise not_found("Task")
    return task


# ==================== 4. PUT /tasks/{task_id} - UPDATE TASK ====================

@router.put(
    "/{task_id}",
    response_model=schemas.TaskResponse,
    summary="Update a task",
    description="Update a task's completion status"
)
def update_task(
    task_id: int,
    completed: bool,
    db: Session = Depends(get_db)
):
    """
    Update a task's completion status.
    
    - **task_id**: ID of the task to update
    - **completed**: New completion status (true/false)
    """
    task = crud.update_task(db, task_id, completed)
    if not task:
        raise not_found("Task")
    return task


# ==================== 5. DELETE /tasks/{task_id} - DELETE TASK ====================

@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a task",
    description="Delete a task by its ID"
)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete a task by ID.
    
    - **task_id**: ID of the task to delete
    """
    task = crud.delete_task(db, task_id)
    if not task:
        raise not_found("Task")
    return None







# ==================== POST ENDPOINT - CREATE TASK ====================

@router.post(
    "/",                                          # Endpoint URL path: /tasks/
    response_model=schemas.TaskResponse,          # What data format to return
    status_code=status.HTTP_201_CREATED,          # HTTP status code for successful creation
    summary="Create a new task",                  # Short description for API docs
    description="Create a task with title and optional description"  # Long description
)
def create_task(
    task: schemas.TaskCreate,                     # Request body validated by Pydantic
    db: Session = Depends(get_db)                 # Database session (injected by FastAPI)
):
    """
    Create a new task.
    
    This endpoint:
    1. Receives task data from client
    2. Validates it automatically (title length, etc.)
    3. Logs the operation
    4. Saves to database
    5. Returns the created task with its ID
    
    Args:
        task: Validated task data from request body
        db: Database session for database operations
    
    Returns:
        TaskResponse: The created task with auto-generated ID
    """
    
    # -------------------- LOGGING --------------------
    # Log that we're creating a new task
    # INFO level (20) - used for normal application events
    # This helps:
    # - Track user activity
    # - Debug issues
    # - Monitor API usage
    logger.info("Creating a new task")
    
    # Optionally log more details (for debugging)
    # logger.debug(f"Task title: {task.title}")
    # logger.debug(f"Task description: {task.description}")
    
    # -------------------- DATABASE OPERATION --------------------
    # Call the CRUD function to actually save to database
    # crud.create_task does:
    #   1. models.Task(title=task.title, description=task.description)  - Create SQLAlchemy model
    #   2. db.add(db_task)           - Stage for insertion
    #   3. db.commit()               - Save to database
    #   4. db.refresh(db_task)       - Get auto-generated ID
    #   5. return db_task            - Return created task
    return crud.create_task(db, task)