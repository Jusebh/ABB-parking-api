from flask import Blueprint, request, jsonify
from database.operations.adding.add_user import add_user
from database.check_reservation_possibility import check_reservation_possibility
from database.select_confing_data import select_config_data
from database.operations.selecting.select_count_of_reservations import select_count_of_reservations
from database.operations.selecting.select_reservation_by_date import select_reservation_by_date
from database.operations.selecting.select_reservation_id import select_reservation_id
from database.operations.selecting.select_user_email import select_user_email
from database.operations.selecting.select_user_notification_status import select_user_notification_status
from database.operations.updating.update_notification_status import update_notification_status
from database.operations.updating.update_reservation_status import update_reservation_status

receive_user_data = Blueprint("receive_user_data", __name__)
@receive_user_data.route("/user/post/receiveUserData", methods=['POST'])
def user_data():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.get_json()
        try:
            add_user(data["email"])
            return jsonify({"result" : "Succeed"})
        except Exception as e:
            return jsonify({"result" : f"Error: {str(e)}"})
    else:
        return jsonify({"result":"Wrong content type"})
    
receive_reservation_data = Blueprint("receive_reservation_data", __name__)
@receive_reservation_data.route("/user/post/receiveReservationData", methods=['POST'])
def reservation_data():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.get_json()
        result = check_reservation_possibility(data["day"], data["month"], int(data["user_id"]), data["dates"])
        return jsonify({"result": result})
    else:
        return jsonify({"result": "Wrong content type"})
    
receive_reservation_date = Blueprint("receive_reservation_date", __name__)
@receive_reservation_date.route("/user/post/receiveReservationDate", methods=['POST'])
def reservation_date():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.get_json()
        result = select_reservation_by_date(int(data["id"]), data["day"], data["month"])
        return jsonify({"result": result})
    else:
        return jsonify({"result": "Wrong content type"})
    
receive_user_id = Blueprint("receive_user_id", __name__)
@receive_user_id.route("/user/post/receiveUserId", methods=['POST'])
def user_id():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.get_json()
        result =  select_user_email(int(data["id"]))
        return jsonify({"result": result})
    else:
        return jsonify({"result": "Wrong content type"})
    
change_notification_status = Blueprint("change_notification_status", __name__)
@change_notification_status.route("/user/post/changeNotificationStatus", methods=['POST'])
def notification_status():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.get_json()
        update_notification_status(int(data["id"]), data["status"])
        return jsonify({"result": "changed"})
    else:
        return jsonify({"result": "Wrong content type"})
    
cancel_reservation = Blueprint("cancel_reservation", __name__)
@cancel_reservation.route("/user/post/cancelReservation", methods=['POST'])
def cancel():
    content_type = request.headers.get('Content-Type')
    if(content_type == 'application/json'):
        data = request.get_json()
        reservation_id = select_reservation_id(data["user_id"], data["day"], data["month"])
        if reservation_id:
            update_reservation_status(reservation_id, "Cancelled")
            return jsonify({"result": True})
        else:
            return jsonify({"result": False})
    else:
        return jsonify({"result": "Wrong content type"})
        
free_spaces_count = Blueprint("free_spaces_count", __name__)
@free_spaces_count.route("/user/post/freeSpacesCount", methods=['POST'])
def free_spaces():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.get_json()
        total_spaces_count = select_config_data("parking_spots_number")
        occupied_spaces_count = select_count_of_reservations(data["day"], data["month"])
        free_spaces = int(total_spaces_count) - int(occupied_spaces_count)
        return jsonify({"result": {"total_spaces": total_spaces_count, "free_spaces": free_spaces}})
    else:
        return jsonify({"result": "Wrong content type"})
    
display_notification_status = Blueprint("display_notification_status", __name__)
@display_notification_status.route("/user/post/displayNotificationStatus", methods=['POST'])
def display_status():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.get_json()
        status = select_user_notification_status(int(data["user_id"]))
        if status != None:
            return jsonify({"result": {"status": status}})
        else:
            return jsonify({"result": {"stauts": None}})
    else:
        return jsonify({"result": "Wrong content type"})