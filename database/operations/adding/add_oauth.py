from sqlalchemy import select
from sqlalchemy.orm import Session
from database.operations.connecting import connect_to_database
from database.models import OAuth

def add_oauth(provider, provider_user_id, token):
  with Session(connect_to_database()) as session:
    oauth = OAuth(
      provider = provider,
      provider_user_id = provider_user_id,
      token = token
    )
    session.add(oauth)
    session.commit()
    session.close()
    return oauth