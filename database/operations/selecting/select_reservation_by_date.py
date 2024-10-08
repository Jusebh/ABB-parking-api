from sqlalchemy import select
from database.models import Reservations, ReservationsDates
from sqlalchemy.orm import Session
from database.operations.connecting import connect_to_database
from datetime import datetime

def select_reservation_by_date(user_id, date):
    with Session(connect_to_database()) as session:
        date += f"-{str(datetime.year)}"
        date = datetime.strptime(date, "%d-%m-%Y").date()
        stmt = select(Reservations).join(Reservations.reservations_dates).where(Reservations.user_id == user_id).where(ReservationsDates.date_of_reservation == date)
        result = session.scalars(stmt).one_or_none()
        if result:
            return {"status": result.statuses, "date": date}
        else:
            return {"status": None, "date": None}