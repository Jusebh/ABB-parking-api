from sqlalchemy import select
from sqlalchemy.orm import Session
from database.operations.connecting import connect_to_database
from database.models import Users

def select_user_notification_status(user_id):
    with Session(connect_to_database()) as session:
        stmt = select(Users).where(Users.id == int(user_id))
        result = session.scalars(stmt).one_or_none()
        if result:
            result = result.notifications
            session.close()
            return result
        else:
            session.close()
            return None