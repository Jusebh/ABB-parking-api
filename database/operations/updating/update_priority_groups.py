from sqlalchemy import update
from sqlalchemy.orm import Session
from database.operations.connecting import connect_to_database
from database.models import PriorityGroups


def update_priority_group(group_id, title, priority):
    with Session(connect_to_database()) as session:
        stmt = update(PriorityGroups).where(PriorityGroups.id == group_id).values(priority=priority, title=title)
        try:
            session.execute(stmt)
            session.commit()
            session.close()
            return True
        except:
            session.close()
            return False
