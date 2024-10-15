import calendar
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import select
from database.operations.connecting import connect_to_database
from database.models import Reservations, Statuses, ReservationsDates

def add_reservation(user_id, day, month, dates: list, priority):
    result = []
    hour = datetime.now().hour + 1
    current_day = datetime.now().day
    current_month = datetime.now().month
    current_year = datetime.now().year

    last_day = calendar.monthrange(current_year, int(month))[1]
    if int(day) == last_day and hour >= 20:
        if current_month == 12:
            current_year += 1
            current_month = 1
        else:
            current_month += 1
    
    with Session(connect_to_database()) as session:
        reservation = Reservations(
            user_id = int(user_id),
            created_at = datetime.now()
        )
        session.add(reservation)
        session.commit()
        reservation_id = reservation.id
        
        for i in dates:
            if int(i) > last_day:
                continue
            elif int(i) <= current_day or current_month < int(month):
                result.append(f"Rezerwacja na dzień {i} nie powiodła się z powodu wybrania przeszłej daty.")
            elif int(i) == (current_day + 1) and current_month == int(month):
                if hour >= 16:
                    result.append(f"Rezerwacje na dzień {i} są już zamknięte, przepraszamy.")
                elif hour < 16:
                    date = f"{i}-{month}-{current_year}"
                    date = datetime.strptime(date, "%d-%m-%Y").date()
                    if priority == 1:
                        stmt = select(Statuses).where(Statuses.title == "Approved")
                    else:
                        stmt = select(Statuses).where(Statuses.title == "Pending")
                    status = session.scalars(stmt).one()
                    reservation_date = ReservationsDates(
                        reservation_id = reservation_id,
                        date_of_reservation = date,
                        status_id = status.id
                    )
                    session.add(reservation_date)
                    session.commit()
                    result.append(f"Rezerwacja na dzień {i} powiodła się, i jej aktualny status to \"{status.title}\".")
            elif int(i) > current_day and current_month == int(month):
                date = f"{i}-{month}-{current_year}"
                date = datetime.strptime(date, "%d-%m-%Y").date()
                if priority == 1:
                    stmt = select(Statuses).where(Statuses.title == "Approved")
                else:
                    stmt = select(Statuses).where(Statuses.title == "Pending")
                status = session.scalars(stmt).one()
                reservation_date = ReservationsDates(
                    reservation_id = reservation_id,
                    date_of_reservation = date,
                    status_id = status.id
                )
                session.add(reservation_date)
                session.commit()
                result.append(f"Rezerwacja na dzień {i} powiodła się, i jej aktualny status to \"{status.title}\".")
            else:
                result.append(f"Przy rezerwacji na dzień {i},  coś poszło nie tak.")
    return result