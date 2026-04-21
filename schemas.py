# Schemas (Pydantic)

'''
🔧 What are Pydantic Models?
- Pydantic models are data validation and serialization classes that:
    - Validate incoming data
    - Define data structure
    - Convert data to/from JSON
    - Provide type hints and auto-completion
    - Analogy: Like a bouncer at a club - checks if data meets requirements before letting it in!
'''

from pydantic import BaseModel, Field


# 📊 TaskCreate Model (Input Schema)

class TaskCreate(BaseModel):
    title: str
    description: str | None = None

'''
Purpose: Validates data when creating a new task

Field	         Type	           Required?	      Explanation
title	         str	           ✅ Required	      Task name - must be provided
description	     str | None	       ❌ Optional	      Task details - can be None/omitted

'''

# 📊 TaskResponse Model (Output Schema)

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    completed: bool

    # Config Class: from_attributes
    class Config:
        from_attributes = True

'''
Purpose: Defines how tasks are returned to the client

Field	                   Type	               Explanation
id	                        int	                 Auto-generated database ID
title	                    str	                 Task name
description	                str | None	         Task details (can be None)
completed	                bool	             Task completion status
'''


# Config Class: from_attributes
'''
Purpose: Allows Pydantic to work with SQLAlchemy models
'''    
    

# Better Validation


# LINE 3: Define a class named TaskCreate that inherits from BaseModel
# This class will be used to validate incoming data when creating a task
class TaskCreate(BaseModel):
    
    # LINE 5-6: Define the 'title' field with validation rules
    # This is a REQUIRED field (because of ...)
    title: str = Field(
        ...,                    # ... (ellipsis) means this field is REQUIRED
                                # No default value - user MUST provide it
        min_length=3,           # Title must be at least 3 characters long
        max_length=100,         # Title cannot exceed 100 characters
    )
    
    # LINE 7-8: Define the 'description' field with validation rules
    # This is an OPTIONAL field (because of = None)
    description: str | None = Field(
        None,                   # Default value is None, making this field optional
                                # If user doesn't provide it, it will be None
        max_length=300,         # If provided, cannot exceed 300 characters
    )