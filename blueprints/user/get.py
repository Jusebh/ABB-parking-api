from flask import Blueprint, jsonify
from database.operations.selecting.select_reservation_by_date import select_reservation_by_date

get_reservation_by_date = Blueprint("get_reservation_by_date", __name__)
@get_reservation_by_date.route("/user/get/reservation_by_date")
def reservation_by_date():
    return jsonify(select_reservation_by_date())