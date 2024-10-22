import os
from sqlalchemy import create_engine


def connect_to_database():
    # connection_string = os.getenv("CONN_STRING")
    connection_string = "sqlite:///test.db"
    return create_engine(connection_string, echo=True)
