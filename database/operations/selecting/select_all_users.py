from database.operations.connecting import connect_to_database
from database.models import Users
from sqlalchemy import select
from sqlalchemy.orm import Session

def select_all_users():
    with Session(connect_to_database()) as session:
        stmt = select(Users)
        return session.scalars(stmt).all()