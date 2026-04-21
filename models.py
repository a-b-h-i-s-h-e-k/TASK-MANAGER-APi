### Model (DB Table)


from sqlalchemy import Column, Integer, String, Boolean

'''
Column = Defines a database column, Integer = Integer data type
String = Text data type, Boolean = True/False data type
'''

from .database import Base

'''
- Base = The blueprint creator 
- . = Current directory (import from local database.py file)
'''

# 2. Class Definition

class Task(Base):
    '''
       - Creates a database table called "Task"
       - (Base) = Inherits from Base, making it a database model
       - SQLAlchemy knows: "This is a database table!"
    '''

    # 3. Table Name
    __tablename__ = "tasks"
    '''
      - Sets the actual database table name to "tasks"
      - Without this, table would be named "Task" (class name)
      - Convention: lowercase, plural name
    '''

    # 4. ID Column (Primary Key)
    id = Column(Integer, primary_key = True, index = True)
    '''
    Integer	   -         Stores whole numbers (1, 2, 3...)
    primary_key=True -	 Unique identifier for each row
    index=True	     -   Creates index for faster searching
    Analogy: Like student ID number - unique for each student
    '''

    # 5. Title Column
    title = Column(String, nullable = False)
    '''
    String - Stores text
    nullable=False - Cannot be empty/null
    Analogy: Task name - every task must have a title
    '''

    # 6. Description Column
    description = Column(String, nullable = True)
    '''
    nullable=True - Can be empty/null (optional)
    Analogy: Task details - optional, can leave blank
    '''

    # 7. Completed Column
    completed = Column(Boolean, default = False)
    '''
    default=False - Default value is False (not completed)
    Analogy: Task status - starts as incomplete
    '''
