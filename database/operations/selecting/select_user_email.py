from sqlalchemy import select
from sqlalchemy.orm import Session
from database.models import Users
from database.operations.connecting import connect_to_database

def select_user_email(user_id):
    with Session(connect_to_database()) as session:
        stmt = select(Users).where(Users.id == int(user_id))
        result = session.scalars(stmt).one_or_none()
        if result:
            session.close()
            return {"email": result.email}
        else:
            session.close()
            return {"email": None}