import identity.web, requests
import app_config
from flask import Blueprint, jsonify, render_template, request, session, url_for

auth = identity.web.Auth(
    session = session,
    authority = app_config.AUTHORITY,
    client_id = app_config.CLIENT_ID,
    client_credential = app_config.CLIENT_SECRET
)

get_login_link = Blueprint("get_login_link", __name__)
@get_login_link.route("/user/oauth/getLoginLink")
def login():
    log_in = auth.log_in(
        scopes = app_config.SCOPE,
        redirect_uri = url_for("auth_response.response", _external=True),
        prompt = "select_account"
    )
    return jsonify({ "link": log_in['auth_uri'] })

get_logout_link = Blueprint("get_logout_link", __name__)
@get_logout_link.route("/user/oauth/getLogoutLink")
def logout():
    log_out_link = auth.log_out(url_for("logout_success_msg.logout_success", _external=True))
    print(log_out_link)
    return jsonify({ "link": log_out_link })

logout_success_msg = Blueprint("logout_success_msg", __name__, template_folder="templates")
@logout_success_msg.route("/user/oauth/logoutSuccess")
def logout_success():
    return render_template("logout_success.html")

auth_response = Blueprint("auth_response", __name__, template_folder="templates")
@auth_response.route(app_config.REDIRECT_PATH)
def response():
    result = auth.complete_log_in(request.args)
    if "error" in result:
        return render_template("login_error.html")
    return render_template("login_success.html")

find_user = Blueprint("find_user", __name__)
@find_user.route("/user/oauth/findUser")
def user():
    if not auth.get_user():
        return jsonify({ "isLoggedIn": False })
    return jsonify({ "isLoggedIn": True })

get_user_data = Blueprint("get_user_data", __name__)
@get_user_data.route("/user/oauth/getUserData")
def user_data():
    token = auth.get_token_for_user(app_config.SCOPE)
    if "error" in token:
        return jsonify({ "result": None })
    api_result = requests.get(
        app_config.ENDPOINT,
        headers = {'Authorization': 'Bearer ' + token['access_token']},
        timeout = 30
    ).json()
    return jsonify({ "result": api_result })