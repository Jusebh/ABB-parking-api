from sqlalchemy import select
from sqlalchemy.orm import Session
from database.operations.connecting import connect_to_database
from database.models import OAuth, Users

def add_oauth(provider, provider_user_id, token, mail):
  with Session(connect_to_database()) as session:
    stmt = select(Users).where(Users.email == mail)
    user = session.scalars(stmt).one_or_none()
    if not user:
      user = Users(
        email = mail,
        priority_group_id = 1,
        notifications = True,
      )
      session.add(user)
      session.flush()
    oauth = OAuth(
      provider = provider,
      provider_user_id = provider_user_id,
      token = token,
      user_id = user.id
    )
    session.add(oauth)
    result = oauth.users
    session.commit()
    session.close()
    return result