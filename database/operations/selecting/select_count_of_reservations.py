from database.operations.connecting import connect_to_database
from database.models import ReservationsDates
from sqlalchemy import select
from sqlalchemy.orm import Session
from datetime import datetime

def select_count_of_reservations(day: str, month: str):
    date = f"{day}-{month}-{str(datetime.now().year)}"
    date = datetime.strptime(date, "%d-%m-%Y").date()
    with Session(connect_to_database()) as session:
        stmt = select(ReservationsDates).where(ReservationsDates.date_of_reservation == date)
        return session.scalars(stmt).all().count()