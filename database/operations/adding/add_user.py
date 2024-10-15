from sqlalchemy import select
from sqlalchemy.orm import Session
from database.operations.connecting import connect_to_database
from database.models import Users, PriorityGroups

def add_user(email, priority_group_id=1):
    with Session(connect_to_database()) as session:
        stmt = select(PriorityGroups).where(PriorityGroups.priority == priority_group_id)
        priority_group = session.scalars(stmt).one()
        priority_group = priority_group.id
        user = Users(
            email = email,
            priority_group_id = priority_group,
            notifications = True
        )
        session.add(user)
        session.commit()
