from datetime import datetime
from sqlalchemy import update, select
from sqlalchemy.orm import Session
from database.operations.connecting import connect_to_database
from database.models import ReservationsDates, Statuses

def update_reservations_date(reservation_date_id, reservation_date_reservation_id, reservation_date_status, reservation_date_date_of_reservation):
    reservation_date_date_of_reservation = datetime.strptime(reservation_date_date_of_reservation, "%Y-%m-%d").date()
    with Session(connect_to_database()) as session:
        stmt = select(Statuses).where(Statuses.title == reservation_date_status)
        reservation_date_status_id = session.scalars(stmt).one_or_none().id
        stmt = update(ReservationsDates).where(ReservationsDates.id == reservation_date_id).values(reservation_id = reservation_date_reservation_id, date_of_reservation = reservation_date_date_of_reservation, status_id = reservation_date_status_id)
        try: 
            session.execute(stmt)
            session.commit()
            session.close()
            return True
        except:
            session.close()
            return False