from database.models import Base
from database.operations.connecting import connect_to_database


def create_tables():
    Base.metadata.create_all(connect_to_database())
