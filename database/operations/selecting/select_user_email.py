from sqlalchemy import select
from database.models import Users
from sqlalchemy.orm import Session
from database.operations.connecting import connect_to_database
from datetime import datetime

def select_user_email(user_id):
    with Session(connect_to_database()) as session:
        stmt = select(Users).where(Users.id == user_id)
        result = session.scalars(stmt).one_or_none()
        if result:
            return {"email": result.email}
        else:
            return {"email": None}