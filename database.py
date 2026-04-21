# 🗄️ STEP 3 — Database Setup
# - We start with SQLite (simple, fast).


from sqlalchemy import create_engine  
# Creates database connection

from sqlalchemy.orm import sessionmaker, declarative_base
# sessionmaker: Creates database sessions
# declarative_base: Base class for database models

import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# DATABASE_URL = "sqlite:///./tasks.db"

'''
-> sqlite:/// = Database type (SQLite)
-> ./tasks.db = File path where database is stored


=> Other database examples:
   =======================

# PostgreSQL
"postgresql://user:pass@localhost/dbname"

# MySQL
"mysql://user:pass@localhost/dbname"

# SQLite memory (temporary)
"sqlite:///:memory:"
'''

# 3. Engine (The Connection)

engine = create_engine(
    DATABASE_URL, connect_args = {"check_same_thread": False}
)

'''
Engine = Core interface to database
check_same_thread: False = Allows multiple threads to access SQLite (needed for FastAPI)
Without this, you'd get threading errors
'''

#  4. SessionLocal (The Conversation)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

'''
- Session = Like a conversation with database
- bind=engine = Connect session to our engine
- autoflush=False = Don't auto-save changes
- autocommit=False = Manual transaction control

-> You'll use this to create sessions:

db = SessionLocal()  # Start conversation
try:
    # Do database operations
    db.commit()  # Save changes
finally:
    db.close()  # End conversation

'''

# 5. Base (The Blueprint)

Base = declarative_base()

'''
- Base = Template for creating database tables

- Your models will inherit from this:

class Task(Base):  # Inherit from Base
    __tablename__ = "tasks"  # Table name
    id = Column(Integer, primary_key=True)
    title = Column(String)

'''



'''
📊 Database Components Analogy

Component	         Role	                   Analogy
Engine	        Connection to database	   Phone line to call center
Session	        Active conversation	       Customer service call
Base	        Model template	           Blueprint for tables
DATABASE_URL	Database address	       Phone number

'''