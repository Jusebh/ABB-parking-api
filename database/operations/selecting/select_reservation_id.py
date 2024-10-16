import calendar
from datetime import datetime
from sqlalchemy import select
from sqlalchemy.orm import Session
from database.models import Reservations, ReservationsDates, Statuses
from database.operations.connecting import connect_to_database
from database.select_confing_data import select_config_data


def select_reservation_id(user_id, day, month):
    next_month_open_hour = int(select_config_data("next_month_opening_hour"))
    current_hour = datetime.now().hour
    current_day = datetime.now().day
    current_year = datetime.now().year
    current_month = datetime.now().month
    last_day = calendar.monthrange(current_year, int(month))[1]
    
    if int(current_day) == last_day and current_hour >= next_month_open_hour and current_month == 12:
        current_year += 1
    
    date = f"{day}-{month}-{current_year}"
    date = datetime.strptime(date, "%d-%m-%Y").date()
    with Session(connect_to_database) as session:
        stmt = select(ReservationsDates).join(ReservationsDates.reservations).join(ReservationsDates.statuses).where(Reservations.user_id == user_id).where(ReservationsDates.date_of_reservation == date).where(Statuses.title != "Canceled")
        result = session.scalars(stmt).one_or_none()
        if result:
            return result.id
        else:
            return None
    
    