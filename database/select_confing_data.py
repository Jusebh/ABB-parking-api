from sqlalchemy import select
from sqlalchemy.orm import Session
from database.operations.connecting import connect_to_database
from database.models import Config


def select_config_data(name):
    with Session(connect_to_database()) as session:
        stmt = select(Config).where(Config.name == name)
        result = session.scalars(stmt).one_or_none()
        if result:
            result = result.value
            session.close()
            return result
        else:
            session.close()
            return None