import os
from sqlalchemy import create_engine

def connect_to_database():
    # connection_string = os.getenv("DB")
    return create_engine("sqlite:///test.db", echo = True)