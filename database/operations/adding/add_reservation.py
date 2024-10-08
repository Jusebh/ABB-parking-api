from database.operations.connecting import connect_to_database
from database.models import Reservations, Users, Statuses, ReservationsDates
from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import datetime

def add_reservation(user_id: int, day: str, month: str):
    with Session(connect_to_database()) as session:

        reservation = Reservations(
            user_id = user_id,
            created_at = datetime.now()
        )
        session.add(reservation)
        session.flush()
        reservation_id = reservation.id
        year = datetime.now().year
        current_month = datetime.now().month
        current_day = datetime.now().day
        if(current_month == 12 and current_day == 31 and month == "1" and datetime.now().hour >= 21):
            year+=1
        date = f"{day}-{month}-{year}"
        date_of_reservation = datetime.strptime(date, "%d-%m-%Y").date()
        stmt = select(Users).where(Users.id == user_id)
        user = session.scalars(stmt).one()
        if(user.priority_groups.priority == 1):
            stmt2 = select(Statuses).where(Statuses.title == "Potwierdzony")
        else:
            stmt2 = select(Statuses).where(Statuses.title == "Oczekujący")
        status = session.scalars(stmt2).one()
        status = status.id
        reservation_date = ReservationsDates(
            reservation_id = reservation_id,
            date_of_reservation = date_of_reservation,
            status_id = status
        )
        session.add(reservation_date)
        session.commit()
    return True