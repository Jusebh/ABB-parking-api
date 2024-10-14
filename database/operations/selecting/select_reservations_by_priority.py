from sqlalchemy import select, desc
from flask import jsonify
from database.models import Reservations, ReservationsDates, Users, PriorityGroups
from sqlalchemy.orm import Session
from database.operations.connecting import connect_to_database
from datetime import datetime

def select_reservation_by_priority(day, month, priority):
    with Session(connect_to_database()) as session:
        try:
            date = f"{day}-{month}-{str(datetime.now().year)}"
            date = datetime.strptime(date, "%d-%m-%Y").date()
            stmt = select(ReservationsDates).join(ReservationsDates.reservations).join(Reservations.users).join(Users.priority_groups).where(ReservationsDates.date_of_reservation == date).where(PriorityGroups.priority > priority).order_by(desc(PriorityGroups.priority)).order_by(desc(Reservations.created_at))
            try:
                result = session.scalars(stmt).first()           
                return result.reservation_id
            except:
                return None
        except:
            return None