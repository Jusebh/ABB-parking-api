from database.operations.connecting import connect_to_database
from database.models import Reservations
from sqlalchemy import select
from sqlalchemy.orm import Session

def select_all_reservations():
    with Session(connect_to_database()) as session:
        stmt = select(Reservations)
        return session.scalars(stmt).all()