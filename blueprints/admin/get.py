from flask import Blueprint, jsonify
from database.operations.selecting.select_all_users import select_all_users
from database.operations.selecting.select_all_priority_groups import select_all_priority_groups
from database.operations.selecting.select_all_reservations_dates import select_all_reservations_dates
from database.operations.selecting.select_all_statuses import select_all_statuses

get_all_users = Blueprint("get_all_users", __name__)
@get_all_users.route("/admin/get/allUsers")
def all_users():
    users = select_all_users()
    return jsonify({"result": users})

get_all_priority_groups = Blueprint("get_all_priority_groups", __name__)
@get_all_priority_groups.route("/admin/get/allPriorityGroups")
def all_priority_groups():
    priority_groups = select_all_priority_groups()
    return jsonify({"result": priority_groups})

get_all_reservations_dates = Blueprint("get_all_reservations_dates", __name__)
@get_all_reservations_dates.route("/admin/get/allReservationsDates")
def all_reservations_dates():
    reservations_dates = select_all_reservations_dates()
    return jsonify({"result": reservations_dates})

get_all_statuses = Blueprint("get_all_statuses", __name__)
@get_all_statuses.route("/admin/get/allStatuses")
def all_statuses():
    statuses = select_all_statuses()
    return jsonify({"result": statuses})