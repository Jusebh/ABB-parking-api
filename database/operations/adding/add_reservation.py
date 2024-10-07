from database.operations.connecting import connect_to_database
from database.models import Reservations, Users, Statuses, ReservationsDates
from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import datetime

def add_reservation(user_id, dates: list):
    with Session(connect_to_database()) as session:
        stmt = select(Users).where(Users.id == user_id)
        user = session.scalars(stmt).one()
        if(user.priority_groups.priority == 1):
            stmt = select(Statuses).where(Statuses.title == "Potwierdzony")
        
        else:
            stmt = select(Statuses).where(Statuses.title == "Oczekujący")
        status = session.scalars(stmt).one()
        status = status.id
        reservation = Reservations(
            user_id = user_id,
            status_id = status,
            created_at = datetime.now()
        )
        session.add(reservation)
        session.flush()
        reservation_id = reservation.id
        for date in dates:
            date_of_reservation = datetime.strptime(date, "%d-%m-%Y").date()
            reservation_date = ReservationsDates(
                reservation_id = reservation_id,
                date_of_reservation = date_of_reservation
            )
            session.add(reservation_date)
        session.commit()
    return True