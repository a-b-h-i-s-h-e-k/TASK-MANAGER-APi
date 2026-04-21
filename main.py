## Step 2 - Running a Basic FastAPI APP

from fastapi import FastAPI  # Import the FastAPI class
from .database import Base, engine
from .routers import tasks

app = FastAPI()  # Create an application instance

Base.metadata.create_all(bind=engine)

#  Include the router
app.include_router(tasks.router)

@app.get("/")  # Decorator - maps this function to GET requests at "/"
def root():    # Function that runs when someone visits "/"
    return {"message": "Task Manager API is running 🚀"}  # Response sent backss

@app.get("/health")
def health():
    return {"status": "ok"}