from database.operations.connecting import connect_to_database
from database.models import ReservationsDates
from sqlalchemy import select
from sqlalchemy.orm import Session

def select_all_reservations_dates():
    with Session(connect_to_database()) as session:
        stmt = select(ReservationsDates)
        return session.scalars(stmt).all()