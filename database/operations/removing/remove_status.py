from database.operations.connecting import connect_to_database
from database.models import Statuses
from sqlalchemy import select
from sqlalchemy.orm import Session

def remove_status(id):
    with Session(connect_to_database()) as session:
        stmt = select(Statuses).where(Statuses.id == id)
        result = session.scalars(stmt).one_or_none()
        if result:
            session.delete(result)
            session.commit()
            return True
        return False