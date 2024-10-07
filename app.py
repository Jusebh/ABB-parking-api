from flask import Flask
from database.operations.create_tables import create_tables
from blueprints.admin.get import get_all_priority_groups, get_all_reservations, get_all_reservations_dates, get_all_statuses, get_all_users

app = Flask(__name__)

create_tables()

app.register_blueprint(get_all_users)
app.register_blueprint(get_all_priority_groups)
app.register_blueprint(get_all_reservations)
app.register_blueprint(get_all_reservations_dates)
app.register_blueprint(get_all_statuses)

if __name__ == '__main__':
   app.run(debug=True)