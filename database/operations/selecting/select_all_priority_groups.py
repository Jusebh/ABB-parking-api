from sqlalchemy import select
from sqlalchemy.orm import Session
from database.operations.connecting import connect_to_database
from database.models import PriorityGroups

def select_all_priority_groups():
    with Session(connect_to_database()) as session:
        stmt = select(PriorityGroups)
        result = session.scalars(stmt).all()
        priority_groups_tab = []
        for priority_group in result:
            priority_groups_tab.append({"id": priority_group.id, "priority": priority_group.priority, "title": priority_group.title})
        session.close()
        return priority_groups_tab