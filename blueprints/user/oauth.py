import app_config
from flask import Blueprint, flash, render_template, url_for
from flask_dance.consumer import oauth_authorized, oauth_error
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage
from flask_dance.contrib.azure import make_azure_blueprint
from flask_login import current_user, login_required, login_user, logout_user
from sqlalchemy.orm import Session
from database.models import OAuth
from database.operations.adding.add_oauth import add_oauth
from database.operations.adding.add_user import add_user
from database.operations.connecting import connect_to_database
from database.operations.selecting.select_oauth import select_oauth

blueprint = make_azure_blueprint(
    client_id = app_config.CLIENT_ID,
    client_secret = app_config.CLIENT_SECRET,
    scope = app_config.SCOPE,
    storage = SQLAlchemyStorage(OAuth, Session(connect_to_database()), user=current_user),
    tenant = app_config.TENANT_ID,
)

@oauth_authorized.connect_via(blueprint)
def azure_logged_in(blueprint, token):
    if not token:
        return False
    resp = blueprint.session.get("/v1.0/me")
    if not resp.ok:
        return False
    info = resp.json()
    user_id = info["id"]
    oauth = select_oauth(provider=blueprint.name, provider_user_id=user_id)
    if not oauth:
        oauth = add_oauth(blueprint.name, user_id, token)
    if oauth.users:
        login_user(oauth.users)
    else:
        user = add_user(info["mail"], "Basic")
        oauth.users = user
        login_user(user)
    return False

@oauth_error.connect_via(blueprint)
def azure_error(blueprint, message, response):
    msg = ("OAuth error from {name}." "message={message}" "response={response}").format(
        name = blueprint.name, message = message, response = response
    )
    flash(msg, category="error")

logout = Blueprint("logout", __name__, template_folder="templates")
@logout.route("/user/oauth/logout")
@login_required
def logout_function():
    logout_user()
    return render_template("logout_success")