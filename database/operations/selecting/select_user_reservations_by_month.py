from sqlalchemy.orm import Session
from sqlalchemy.sql import extract
from sqlalchemy import select
from database.operations.connecting import connect_to_database
from database.models import ReservationsDates, Reservations, Statuses

def select_user_reservations_by_month(user_id, month):
    with Session(connect_to_database()) as session:
        dates_tab = []
        try:
            stmt = select(ReservationsDates).join(ReservationsDates.reservations).join(ReservationsDates.statuses).where(Reservations.user_id == int(user_id)).where(extract( 'month', ReservationsDates.date_of_reservation) == int(month)).where(Statuses.title != "Cancelled")
            query = session.scalars(stmt).all()
            for i in query:
                dates_tab.append(i.date_of_reservation.day)
            session.close()
            return dates_tab
        except:
            session.close()
            return dates_tab
