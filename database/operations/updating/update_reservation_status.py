import threading
from sqlalchemy import update, select
from sqlalchemy.orm import Session
from database.operations.connecting import connect_to_database
from database.models import ReservationsDates, Statuses
from database.operations.selecting.select_email_by_reservation_id import select_email_by_reservation_id
from database.operations.selecting.select_user_id import select_user_id
from database.operations.selecting.select_user_notification_status import select_user_notification_status
from communication.status_changed_mail import status_changed_mail

def update_reservation_status(reservation_date_id, status):
    with Session(connect_to_database()) as session:
        stmt = select(Statuses).where(Statuses.title == status)
        status_id = session.scalars(stmt).one()
        stmt = update(ReservationsDates).where(ReservationsDates.id == reservation_date_id).values(status_id = status_id.id)
        try: 
            session.execute(stmt)
            session.commit()
            stmt = select(ReservationsDates).where(ReservationsDates.id == reservation_date_id)
            result = session.scalars(stmt).one_or_none()
            date = result.date_of_reservation
            email = select_email_by_reservation_id(reservation_date_id)
            id = select_user_id(email)
            notification_status = select_user_notification_status(id)
            if notification_status:
                thread = threading.Thread(target = status_changed_mail, args=(email, date, status))
                thread.start()
        except:
            return False
        return True