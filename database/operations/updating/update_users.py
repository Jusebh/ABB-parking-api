from sqlalchemy import update, select
from sqlalchemy.orm import Session
from database.operations.connecting import connect_to_database
from database.models import Users, PriorityGroups


def update_user(user_id, user_email, priority_group, notifications, role):
    with Session(connect_to_database()) as session:
        stmt = select(PriorityGroups).where(PriorityGroups.title == priority_group)
        priority_group_id = session.scalars(stmt).one_or_none().id
        if notifications == "True":
            notifications = True
        elif notifications == "False":
            notifications = False
        stmt = (
            update(Users)
            .where(Users.id == user_id)
            .values(
                email=user_email,
                priority_group_id=int(priority_group_id),
                notifications=notifications,
                role=role,
            )
        )
        try:
            session.execute(stmt)
            session.commit()
            session.close()
            return True
        except:
            session.close()
            return False
