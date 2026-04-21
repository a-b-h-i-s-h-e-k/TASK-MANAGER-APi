# LINE 1: Import HTTPException from FastAPI
# HTTPException is the class that creates HTTP error responses
from fastapi import HTTPException

# LINE 3: Define a helper function to create "not found" errors
# This function returns an HTTPException object that FastAPI can raise
def not_found(entity: str = "Item"):
    # LINE 4: Create and return an HTTP 404 error response
    # status_code=404 means "Not Found" (resource doesn't exist)
    # detail=... is the error message that will be sent to the client
    return HTTPException(
        status_code=404,                    # HTTP 404 Not Found status
        detail=f"{entity} not found"        # Dynamic error message
    )