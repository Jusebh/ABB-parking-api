from datetime import datetime
from flask import Blueprint, request, jsonify
from database.operations.adding.add_user import add_user
from database.operations.adding.add_reservation import add_reservation
from communication.admin_mail import admin_mail
from database.operations.removing.remove_priority_group import remove_priority_group
from database.operations.removing.remove_reservation import remove_reservation
from database.operations.removing.remove_reservations_date import remove_reservations_date
from database.operations.removing.remove_status import remove_status
from database.operations.removing.remove_user import remove_user
from database.operations.updating.update_priority_groups import update_priority_group
from database.operations.updating.update_reservations import update_reservation
from database.operations.updating.update_reservations_dates import update_reservations_date
from database.operations.updating.update_statuses import update_status
from database.operations.updating.update_users import update_user

receive_new_user_data = Blueprint("receive_new_user_data", __name__)
@receive_new_user_data.route("/admin/post/receiveNewUserData", methods=['POST'])
def new_user_data():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
        try:
            add_user(data["email"], data["priority_group_id"])
            return jsonify({"result": "Successfully added user"})
        except:
            return jsonify({"result": "Couldn't add user"})
    else:
        return jsonify({"result": "Wrong content type"})

receive_new_reservation_data = Blueprint("receive_new_reservation_data", __name__)
@receive_new_reservation_data.route("/admin/post/receiveNewReservationData", methods=['POST'])
def new_reservation_data():
    content_type = request.headers.get('Content-Type')
    current_hour = datetime.now().hour
    current_day = datetime.now().day
    current_month = datetime.now().month
    result = []
    if (content_type == 'application/json'):
        data = request.get_json()
        dates = data["dates"]
        for i in dates:
            if int(i) <= current_day and data["month"] == current_month:
                if i == current_day and current_hour >= 16:
                    result.append(f"Reservation on {i} can't be completed (it's too late).")
                else:
                    result.append(f"Reservation on past date can't be made.")
            else:
                try:
                    add_reservation(data["id"], i, data["month"])
                    result.append(f"Reservation on day {i} was made.")
                except Exception as e:
                    result.append(f"Reservation on day {i} can't be made, because of {e} error.")
        return jsonify({"result": result})
    else:
        return jsonify({"result": "Wrong content type"})

receive_remove_data = Blueprint("receive_remove_data", __name__)
@receive_remove_data.route("/admin/post/receiveRemoveData", methods=['POST'])
def remove_data():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
        try:
            if data["table"] == "users":
                remove_user(int(data["id"]))
            elif data["table"] == "reservations":
                remove_reservation(int(data["id"]))
            elif data["table"] == "reservations_dates":
                remove_reservations_date(int(data["id"]))
            elif data["table"] == "priority_groups":
                remove_priority_group(int(data["id"]))
            elif data["table"] == "statuses":
                remove_status(int(data["id"]))
            else:
                return jsonify({"result": "An error occured"})
            return jsonify({"result": "Successfully added user"})
        except:
            return jsonify({"result": "Couldn't add user"})
    else:
        return jsonify({"result": "Wrong content type"})

receive_update_data = Blueprint("receive_update_data", __name__)
@receive_update_data.route("/admin/post/receiveUpdateData", methods=['POST'])
def update_data():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
        try:
            if data["table"] == "users":
                update_user(int(data["user_id"]), data["user_email"])
            elif data["table"] == "reservations":
                update_reservation(int(data["reservation_id"]), int(data["reservation_user_id"]))
            elif data["table"] == "reservations_dates":
                update_reservations_date(int(data["reservation_date_id"]), int(data["reservation_date_reservation_id"]), int(data["reservation_date_status_id"]), data["reservation_date_date_of_reservation"])
            elif data["table"] == "priority_groups":
                update_priority_group(int(data["group_id"]), data["priority_number"])
            elif data["table"] == "statuses":
                update_status(int(data["status_id"]), data["status_title"])
            else:
                return jsonify({"result": "An error occured"})
            return jsonify({"result": "Successfully added user"})
        except:
            return jsonify({"result": "Couldn't add user"})
    else:
        return jsonify({"result": "Wrong content type"})
    
receive_email_data = Blueprint("receive_email_data", __name__)
@receive_email_data.route("/admin/post/receiveEmailData", methods=['POST'])
def email_data():
    content_type = request.headers.get("Content-Type")
    if content_type == 'application/json':
        data = request.get_json()
        try:
            admin_mail(data["email_list"], data["content"], data["subject"])
            return jsonify({"result": "Email has been sent."})
        except:
            return jsonify({"result": "Something went wrong."})
    else:
        return jsonify("Wrong content type")