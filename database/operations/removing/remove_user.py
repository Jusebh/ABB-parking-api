from database.operations.connecting import connect_to_database
from database.models import Users
from sqlalchemy import select
from sqlalchemy.orm import Session

def remove_user(id):
    with Session(connect_to_database()) as session:
        stmt = select(Users).where(Users.id == id)
        result = session.scalars(stmt).one_or_none()
        if result:
            session.delete(result)
            session.commit()
            return True
        return False