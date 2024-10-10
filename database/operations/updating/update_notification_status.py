from database.operations.connecting import connect_to_database
from sqlalchemy import update
from sqlalchemy.orm import Session
from database.models import Users

def update_notification_status(user_id, notification_status):
    with Session(connect_to_database()) as session:
        stmt = update(Users).where(Users.id == user_id).values(notification = notification_status)
        try: 
            session.execute(stmt)
            session.commit()
        except:
            return False
        return True