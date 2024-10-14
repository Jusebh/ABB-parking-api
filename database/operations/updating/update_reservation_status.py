from database.operations.connecting import connect_to_database
from sqlalchemy import update, select
from sqlalchemy.orm import Session
from database.models import ReservationsDates, Statuses
from datetime import datetime

def update_reservation_status(reservation_date_id, status):
    with Session(connect_to_database()) as session:
        stmt = select(Statuses).where(Statuses.title == status)
        status_id = session.scalars(stmt).one()
        stmt = update(ReservationsDates).where(ReservationsDates.id == reservation_date_id).values(status_id = status_id.id)
        try: 
            session.execute(stmt)
            session.commit()
        except:
            return False
        return True