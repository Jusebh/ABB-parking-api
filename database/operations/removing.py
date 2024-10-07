import database.operations.connecting as conn
from sqlalchemy import delete
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
    with Session(conn) as session:
        delete(table).where(model.id == id)
        session.commit()
    return True