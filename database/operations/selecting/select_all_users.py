from sqlalchemy import select
from sqlalchemy.orm import Session
from database.operations.connecting import connect_to_database
from database.models import Users

def select_all_users():
    with Session(connect_to_database()) as session:
        stmt = select(Users)
        result = session.scalars(stmt).all()
        users_tab = []
        for user in result:
            users_tab.append({"id": user.id, "email": user.email, "priority_group": user.priority_groups.priority, "notification": user.notifications, "role": user.role})
        session.close()
        return users_tab