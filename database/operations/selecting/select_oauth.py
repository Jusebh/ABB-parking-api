from sqlalchemy import select
from sqlalchemy.orm import Session
from database.models import OAuth
from database.operations.connecting import connect_to_database

def select_oauth(provider, provider_user_id):
  with Session(connect_to_database()) as session:
    stmt = select(OAuth).where(OAuth.provider == provider).where(OAuth.provider_user_id == provider_user_id)
    result = session.scalars(stmt).one_or_none()
    if result:
      result = result.users
    session.close()
    return result