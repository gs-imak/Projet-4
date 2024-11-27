from flask_sqlalchemy import SQLAlchemy #this will need to be changed later on 

# Initialize the database object
db = SQLAlchemy()

# Import models here to register them with SQLAlchemy
from .user import User  # Example model

__all__ = ["db", "User"]
