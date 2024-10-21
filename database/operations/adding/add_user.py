from sqlalchemy import select
from sqlalchemy.orm import Session
from database.operations.connecting import connect_to_database
from database.models import Users, PriorityGroups

def add_user(email, priority_group, notifications = True, role = "user"):
    with Session(connect_to_database()) as session:
        try:
            stmt = select(PriorityGroups).where(PriorityGroups.title == priority_group)
            priority = session.scalars(stmt).one_or_none().id
            user = Users(
                email = email,
                priority_group_id = priority,
                notifications = True,
                role = role,
                notifications = notifications
            )
            session.add(user)
            session.commit()
            session.close()
            return True
        except:
            return False