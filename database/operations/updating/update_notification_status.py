from sqlalchemy import update
from sqlalchemy.orm import Session
from database.operations.connecting import connect_to_database
from database.models import Users


def update_notification_status(user_id, notification_status):
    with Session(connect_to_database()) as session:
        if notification_status == "True":
            notification_status = True
        elif notification_status == "False":
            notification_status = False
        print(notification_status)
        stmt = update(Users).where(Users.id == user_id).values(notifications=notification_status)
        session.execute(stmt)
        session.commit()
        session.close()
