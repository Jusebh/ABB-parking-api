from database.operations.connecting import connect_to_database
from database.models import Users, PriorityGroups
from sqlalchemy.orm import Session
from sqlalchemy import select

def add_user(email):
    with Session(connect_to_database()) as session:
        stmt = select(PriorityGroups).where(PriorityGroups.priority == None)
        priority_group = session.scalars(stmt).one()
        priority_group = priority_group.id
        user = Users(
            email = email,
            priority_group_id = priority_group
        )
        session.add(user)
        session.commit()