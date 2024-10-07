from database.operations.connecting import connect_to_database
from sqlalchemy import delete, select
from sqlalchemy.orm import Session

def remove_record(table: str, id):
    table = table.lower()
    if table == "users":
        from database.models import Users as model
    elif table == "reservations":
        from database.models import Reservations as model
    elif table == "prioritygroups":
        from database.models import PriorityGroups as model
    elif table == "reservationdates":
        from database.models import ReservationsDates as model
    elif table == "statuses":
        from database.models import Statuses as model
    else:
        return False
    with Session(connect_to_database()) as session:
        stmt = select(model).where(model.id == id)
        result = session.scalars(stmt).one_or_none()
        if result:
            session.delete(result)
            session.commit()
            return True
        return False