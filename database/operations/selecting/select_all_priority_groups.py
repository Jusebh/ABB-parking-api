from database.operations.connecting import connect_to_database
from database.models import PriorityGroups
from sqlalchemy import select
from sqlalchemy.orm import Session

def select_all_priority_groups():
    with Session(connect_to_database()) as session:
        stmt = select(PriorityGroups)
        return session.scalars(stmt).all()