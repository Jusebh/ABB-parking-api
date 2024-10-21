from sqlalchemy import select
from sqlalchemy.orm import Session
from database.models import Reservations, ReservationsDates, Users
from database.operations.connecting import connect_to_database

def select_email_by_reservation_id(reservation_id):
    with Session(connect_to_database()) as session:
        stmt = select(Users).join(Users.reservations).join(Reservations.reservations_dates).where(ReservationsDates.id == int(reservation_id))
        result = session.scalars(stmt).one_or_none()
        if result:
            session.close()
            return result.email
        else:
            session.close()
            return None
