from flask import Flask, render_template
from flask_apscheduler import APScheduler
from flask_login import LoginManager
from flask_session import Session
from blueprints.admin.get import get_all_priority_groups, get_all_reservations_dates, get_all_statuses, get_all_users
from blueprints.admin.post import receive_new_user_data, receive_new_reservation_data, receive_remove_data, receive_update_data, receive_email_data
from blueprints.user.oauth import blueprint, logout
from blueprints.user.post import receive_reservation_data, receive_user_data, receive_reservation_date, receive_user_id, change_notification_status, cancel_reservation, free_spaces_count, display_notification_status
from communication.check_reservations import check_reservations
from database.operations.create_tables import create_tables
from database.operations.selecting.select_user_by_id import select_user_by_id
import app_config
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.config.from_object(app_config)
Session(app)

create_tables()
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto="https")

app.register_blueprint(get_all_users)
app.register_blueprint(get_all_priority_groups)
app.register_blueprint(get_all_reservations_dates)
app.register_blueprint(get_all_statuses)

app.register_blueprint(receive_new_user_data)
app.register_blueprint(receive_new_reservation_data)
app.register_blueprint(receive_remove_data)
app.register_blueprint(receive_update_data)
app.register_blueprint(receive_email_data)

app.register_blueprint(blueprint, url_pefix="/login")
app.register_blueprint(logout)

app.register_blueprint(receive_reservation_data)
app.register_blueprint(receive_user_data)
app.register_blueprint(receive_reservation_date)
app.register_blueprint(receive_user_id)
app.register_blueprint(change_notification_status)
app.register_blueprint(cancel_reservation)
app.register_blueprint(free_spaces_count)
app.register_blueprint(display_notification_status)

@app.route("/")
def index():
   return render_template("home.html")

login_manager = LoginManager()
login_manager.login_view = "azure.login"

@login_manager.user_loader
def load_user(user_id):
   return select_user_by_id(user_id)

login_manager.init_app(app)

scheduler = APScheduler()

@scheduler.task('interval', id="1", hours = 1)
def check_user_reservations():
   check_reservations()
   
scheduler.init_app(app)

scheduler.start()

if __name__ == '__main__':
   app.run()