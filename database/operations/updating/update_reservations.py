from database.operations.connecting import connect_to_database
from sqlalchemy import update
from sqlalchemy.orm import Session
from database.models import Reservations

def update_reservation(reservation_id, reservation_user_id):
    with Session(connect_to_database()) as session:
        stmt = update(Reservations).where(Reservations.id == reservation_id).values(user_id = reservation_user_id)
        try: 
            session.execute(stmt)
            session.commit()
        except:
            return False
        return True