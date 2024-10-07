from database.operations.connecting import connect_to_database
from sqlalchemy import update
from sqlalchemy.orm import Session
from database.models import Users

def update_user(user_id, user_email):
    with Session(connect_to_database()) as session:
        stmt = update(Users).where(Users.id == user_id).values(email = user_email)
        try: 
            session.execute(stmt)
            session.commit()
        except:
            return False
        return True