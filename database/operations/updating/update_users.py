from sqlalchemy import update
from sqlalchemy.orm import Session
from database.operations.connecting import connect_to_database
from database.models import Users

def update_user(user_id, user_email, priority_group_id, notifications, role):
    with Session(connect_to_database()) as session:
        stmt = update(Users).where(Users.id == user_id).values(email = user_email, priority_group_id = int(priority_group_id), notifications = notifications, role = role)
        try: 
            session.execute(stmt)
            session.commit()
            session.close()
            return True
        except:
            session.close()
            return False