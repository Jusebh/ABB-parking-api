from flask import Flask
from database.operations.create_tables import create_tables
from database.operations.selecting.select_all_users import select_all_users
from database.operations.selecting.select_all_priority_groups import select_all_priority_groups
from database.operations.selecting.select_all_reservations import select_all_reservations
from database.operations.selecting.select_all_reservations_dates import select_all_reservations_dates
from database.operations.selecting.select_all_statuses import select_all_statuses

app = Flask(__name__) 
create_tables()

@app.route("/admin/get/allUsers")
def get_all_users():
    users = select_all_users()
    users_tab = []
    for user in users:
        users_tab.append({"id": user.id, "email": user.email, "priority_group_id": user.priority_group_id})
    return users_tab

@app.route("/admin/get/allPriorityGroups")
def get_all_priority_groups():
    priority_groups = select_all_priority_groups()
    priority_groups_tab = []
    for priority_group in priority_groups:
        priority_groups_tab.append({"id": priority_group.id, "priority": priority_group.priority})
    return priority_groups_tab

@app.route("/admin/get/allReservations")
def get_all_reservations():
    reservations = select_all_reservations()
    reservations_tab = []
    for reservation in reservations:
        reservations_tab.append({"id": reservation.id, "user_id": reservation.user_id, "status_id": reservation.status_id, "created_at": reservation.created_at})
    return reservations_tab

@app.route("/admin/get/allReservationsDates")
def get_all_reservations_dates():
    reservations_dates = select_all_reservations_dates()
    reservations_dates_tab = []
    for reservations_date in reservations_dates:
        reservations_dates_tab.append[{"id": reservations_date.id, "reservation_id": reservations_date.reservation_id, "date_of_reservation": reservations_date.date_of_reservation}]
    return reservations_dates_tab

@app.route("/admin/get/allStatuses")
def get_all_statuses():
    statuses = select_all_statuses()
    statuses_tab = []
    for status in statuses:
        statuses_tab.append({"id": status.id, "title": status.title})
    return statuses_tab

if __name__ == '__main__':
   app.run(debug=True)