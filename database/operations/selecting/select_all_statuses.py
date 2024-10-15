from sqlalchemy import select
from sqlalchemy.orm import Session
from database.operations.connecting import connect_to_database
from database.models import Statuses

def select_all_statuses():
    with Session(connect_to_database()) as session:
        stmt = select(Statuses)
        result = session.scalars(stmt).all()
        statuses_tab = []
        for stasus in result:
            statuses_tab.append({"id": stasus.id, "title": stasus.title})
        return statuses_tab