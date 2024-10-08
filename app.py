from flask import Flask
from database.operations.create_tables import create_tables
from blueprints.admin.get import get_all_priority_groups, get_all_reservations, get_all_reservations_dates, get_all_statuses, get_all_users
from blueprints.user.dates import current_month, table_of_days
from blueprints.user.get import get_reservation_by_date

app = Flask(__name__)

create_tables()

app.register_blueprint(get_all_users)
app.register_blueprint(get_all_priority_groups)
app.register_blueprint(get_all_reservations)
app.register_blueprint(get_all_reservations_dates)
app.register_blueprint(get_all_statuses)

app.register_blueprint(current_month)
app.register_blueprint(table_of_days)
app.register_blueprint(get_reservation_by_date)

if __name__ == '__main__':
   app.run(debug=True)