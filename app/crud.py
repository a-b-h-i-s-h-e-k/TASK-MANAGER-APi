# # CRUD Logic

from sqlalchemy.orm import Session
from . import models, schemas

def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(
        title=task.title,
        description=task.description
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Task).offset(skip).limit(limit).all()


# Filtering + Search

def get_tasks(
    db: Session,                    # Database session - the connection to database
    skip: int = 0,                  # Number of records to skip (for pagination)
    limit: int = 10,                # Maximum records to return (for pagination)
    completed: bool | None = None,  # Filter by completion status (True/False/None)
    search: str | None = None,      # Search term to look for in task titles
):
    """
    Get tasks with optional filtering and search.
    
    Args:
        db: Database session
        skip: Number of tasks to skip (pagination)
        limit: Maximum number of tasks to return
        completed: Filter by completion status (True=completed, False=pending, None=all)
        search: Search term to look for in task titles (case-insensitive)
    
    Returns:
        List of Task objects matching the criteria
    """
    
    # Start with base query - select ALL tasks
    query = db.query(models.Task)
    
    # FILTER 1: Filter by completion status if specified
    # If completed is NOT None (meaning user provided True or False)
    if completed is not None:
        # Add WHERE clause: WHERE tasks.completed = ? 
        # Example: if completed=True -> WHERE completed = 1
        query = query.filter(models.Task.completed == completed)
    
    # FILTER 2: Search in title if search term is provided
    # If search is NOT None and NOT empty string
    if search:
        # Add WHERE clause: WHERE title LIKE '%search_term%' (case-insensitive)
        # ilike = case-insensitive LIKE
        # f"%{search}%" = search term with wildcards before and after
        # Example: search="fast" will match "FastAPI", "fast", "breakfast"
        query = query.filter(models.Task.title.ilike(f"%{search}%"))
    
    # Apply pagination and execute query
    # .offset(skip) = Skip first 'skip' number of records
    # .limit(limit) = Only return 'limit' number of records
    # .all() = Execute query and return all results as a list
    return query.offset(skip).limit(limit).all()





def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def delete_task(db: Session, task_id: int):
    task = get_task(db, task_id)
    if task:
        db.delete(task)
        db.commit()
    return task

def update_task(db: Session, task_id: int, completed: bool):
    task = get_task(db, task_id)
    if task:
        task.completed = completed
        db.commit()
        db.refresh(task)
    return task




























# from sqlalchemy.orm import Session
# from . import models, schemas


# # 1. CREATE Task

# def create_task(db: Session, task: schemas.TaskCreate):
#     db_task = models.Task(
#         title = task.title,
#         title = task.title,
#         description = task.description
#     )
#     db.add(db_task)    # Stage the task
#     db.commit()        # Save to database
#     db.refresh(db_task)  # Get auto-generated ID
#     return db_task 

# # 2. READ All Tasks (with Pagination)

# def get_tasks(db: Session, skip: int = 0, limit: int = 10):
#     return db.query(models.Task).offset(skip).limit(limit).all()


# # 3. READ Single Task by ID

# def get_task(db: Session, task_id: int):
#     return db.query(models.Task).filter(models.Task.id == task_id).first()


# # 4. UPDATE Task

# def update_task(db: Session, task_id: int, completed: bool):
#     task = get_task(db, task_id)  # Find the task
#     if task:                       # If found
#         task.completed = completed # Update field
#         db.commit()                # Save changes
#         db.refresh(task)           # Get updated version
#     return task                    # Return updated task or None

# # 5. DELETE Task

# def delete_task(db: Session, task_id: int):
#     task = get_task(db, task_id)  # Find the task
#     if task:                       # If found
#         db.delete(task)            # Stage deletion
#         db.commit()                # Actually delete
#     return task                    # Return deleted task or None


