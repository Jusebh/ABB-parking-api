from database.operations.connecting import connect_to_database
from sqlalchemy import update
from sqlalchemy.orm import Session
from database.models import Statuses

def update_user(status_id, status_title):
    with Session(connect_to_database()) as session:
        stmt = update(Statuses).where(Statuses.id == status_id).values(title = status_title)
        try: 
            session.execute(stmt)
            session.commit()
        except:
            return False
        return True