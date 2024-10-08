from flask import Blueprint
from database.operations.selecting.select_all_users import select_all_users
from database.operations.selecting.select_all_priority_groups import select_all_priority_groups
from database.operations.selecting.select_all_reservations import select_all_reservations
from database.operations.selecting.select_all_reservations_dates import select_all_reservations_dates
from database.operations.selecting.select_all_statuses import select_all_statuses

get_all_users = Blueprint("get_all_users", __name__)
@get_all_users.route("/admin/get/allUsers")
def all_users():
    users = select_all_users()
    users_tab = []
    for user in users:
        users_tab.append({"id": user.id, "email": user.email, "priority_group_id": user.priority_group_id})
    return users_tab

get_all_priority_groups = Blueprint("get_all_priority_groups", __name__)
@get_all_priority_groups.route("/admin/get/allPriorityGroups")
def all_priority_groups():
    priority_groups = select_all_priority_groups()
    priority_groups_tab = []
    for priority_group in priority_groups:
        priority_groups_tab.append({"id": priority_group.id, "priority": priority_group.priority})
    return priority_groups_tab

get_all_reservations = Blueprint("get_all_reseravtions", __name__)
@get_all_reservations.route("/admin/get/allReservations")
def all_reservations():
    reservations = select_all_reservations()
    reservations_tab = []
    for reservation in reservations:
        reservations_tab.append({"id": reservation.id, "user_id": reservation.user_id, "status_id": reservation.status_id, "created_at": reservation.created_at})
    return reservations_tab

get_all_reservations_dates = Blueprint("get_all_reservations_dates", __name__)
@get_all_reservations_dates.route("/admin/get/allReservationsDates")
def all_reservations_dates():
    reservations_dates = select_all_reservations_dates()
    reservations_dates_tab = []
    for reservations_date in reservations_dates:
        reservations_dates_tab.append[{"id": reservations_date.id, "reservation_id": reservations_date.reservation_id, "date_of_reservation": reservations_date.date_of_reservation}]
    return reservations_dates_tab

get_all_statuses = Blueprint("get_all_statuses", __name__)
@get_all_statuses.route("/admin/get/allStatuses")
def all_statuses():
    statuses = select_all_statuses()
    statuses_tab = []
    for status in statuses:
        statuses_tab.append({"id": status.id, "title": status.title})
    return statuses_tab