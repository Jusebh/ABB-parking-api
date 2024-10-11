from database.operations.connecting import connect_to_database
from database.models import ReservationsDates
from sqlalchemy import select
from sqlalchemy.orm import Session

def select_all_reservations_dates():
    with Session(connect_to_database()) as session:
        stmt = select(ReservationsDates)
        result = session.scalars(stmt).all()
        reservations_tab = []
        for reservation_date in result:
            reservations_tab.append({"id": reservation_date.id, "user": reservation_date.reservations.users.email, "date_of_reservation": reservation_date.date_of_reservation, "status": reservation_date.statuses.title})
        return reservations_tab