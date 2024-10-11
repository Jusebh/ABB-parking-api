from sqlalchemy import select
from flask import jsonify
from database.models import Reservations, ReservationsDates
from sqlalchemy.orm import Session
from database.operations.connecting import connect_to_database
from datetime import datetime

def select_reservation_by_date(user_id, day, month):
    with Session(connect_to_database()) as session:
        try:
            date = f"{day}-{month}-{str(datetime.now().year)}"
            date = datetime.strptime(date, "%d-%m-%Y").date()
            stmt = select(ReservationsDates).join(ReservationsDates.reservations).where(Reservations.user_id == user_id).where(ReservationsDates.date_of_reservation >= date)
            result = session.scalars(stmt).all()
            reservations_tab = []
            for reservation in result:
                reservations_tab.append({"day": reservation.date_of_reservation.day, "status": reservation.statuses.title})
            return reservations_tab
        except:
            return None