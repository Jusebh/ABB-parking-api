from database.operations.connecting import connect_to_database
from sqlalchemy import update
from sqlalchemy.orm import Session
from database.models import PriorityGroups

def update_user(group_id, priority_number):
    with Session(connect_to_database()) as session:
        stmt = update(PriorityGroups).where(PriorityGroups.id == group_id).values(priority = priority_number)
        try: 
            session.execute(stmt)
            session.commit()
        except:
            return False
        return True