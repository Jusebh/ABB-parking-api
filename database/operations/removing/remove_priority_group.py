from sqlalchemy import select
from sqlalchemy.orm import Session
from database.operations.connecting import connect_to_database
from database.models import PriorityGroups

def remove_priority_group(id):
    with Session(connect_to_database()) as session:
        stmt = select(PriorityGroups).where(PriorityGroups.id == id)
        result = session.scalars(stmt).one_or_none()
        if result:
            session.delete(result)
            session.commit()
            return True
        return False