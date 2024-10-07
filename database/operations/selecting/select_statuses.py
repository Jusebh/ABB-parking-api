from database.operations.connecting import connect_to_database
from database.models import Statuses
from sqlalchemy import select
from sqlalchemy.orm import Session

def select_user():
    with Session(connect_to_database()) as session:
        stmt = select(Statuses)
        return session.scalars(stmt).all()