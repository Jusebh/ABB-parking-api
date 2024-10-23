from datetime import date
from sqlalchemy import select
from sqlalchemy.orm import Session
from database.operations.connecting import connect_to_database
from database.models import ReservationsDates, Reservations


def select_reservation_to_notify():
    with Session(connect_to_database()) as session:
        stmt = select(ReservationsDates).join(ReservationsDates.reservations).join(Reservations.users).join(ReservationsDates.statuses)
        result = session.scalars(stmt).all()
        today = date.today()
        email_tab = []
        for i in result:
            if i.reservations.users.notifications:
                if i.statuses.title == "Potwierdzony":
                    if (i.date_of_reservation - today).days <= 1:
                        email_tab.append(
                            {
                                "email": i.reservations.users.email,
                                "date": i.date_of_reservation,
                            }
                        )
        session.close()
        return email_tab
