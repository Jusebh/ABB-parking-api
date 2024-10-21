from sqlalchemy import select
from sqlalchemy.orm import Session
from database.models import Users
from database.operations.connecting import connect_to_database

def select_user_id(email):
    with Session(connect_to_database()) as session:
        stmt = select(Users).where(Users.email == email)
        result = session.scalars(stmt).one_or_none()
        if result:
            session.close()
            return {"id": result.id}
        else:
            session.close()
            return {"id": None}