from database.operations.connecting import connect_to_database
from sqlalchemy import update
from sqlalchemy.orm import Session
from database.models import ReservationsDates

def update_reservations_date(reservation_date_id, reservation_date_reservation_id, reservation_date_date_of_reservation):
    with Session(connect_to_database()) as session:
        stmt = update(ReservationsDates).where(ReservationsDates.id == reservation_date_id).values(reservation_id = reservation_date_reservation_id, date_of_reservation = reservation_date_date_of_reservation)
        try: 
            session.execute(stmt)
            session.commit()
        except:
            return False
        return True