from database.operations.connecting import connect_to_database
from sqlalchemy import select
from database.models import ReservationsDates, Reservations
from sqlalchemy.orm import Session
from sqlalchemy.sql import extract

def select_user_reservations_by_month(user_id, month):
    with Session(connect_to_database()) as session:
        dates_tab = []
        try:
            stmt = select(ReservationsDates).join(ReservationsDates.reservations).where(Reservations.user_id == int(user_id)).where(extract( 'month', ReservationsDates.date_of_reservation) == int(month))
            query = session.scalars(stmt).all()
            for i in query:
                dates_tab.append(i.date_of_reservation.day)
            return dates_tab
        except:
            return dates_tab