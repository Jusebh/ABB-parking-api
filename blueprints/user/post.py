from flask import Blueprint, request, jsonify
from database.operations.adding.add_user import add_user
from database.check_reservation_possibility import check_reservation_possibility
from database.operations.selecting.select_reservation_by_date import select_reservation_by_date
from database.operations.selecting.select_user_email import select_user_email
from database.operations.updating.update_notification_status import update_notification_status

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
        result = check_reservation_possibility(data["day"], data["month"], data["user_id"], data["dates"])
        return jsonify({"result": result})
    else:
        return jsonify({"result": "Wrong content type"})
    
receive_reservation_date = Blueprint("receive_reservation_date", __name__)
@receive_reservation_date.route("/user/post/receiveReservationDate", methods=['POST'])
def reservation_date():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.get_json()
        result = select_reservation_by_date(data["id"], data["day"], data["month"])
        return jsonify({"result": result})
    else:
        return jsonify({"result": "Wrong content type"})
    
receive_user_id = Blueprint("receive_user_id", __name__)
@receive_user_id.route("/user/post/receiveUserId", methods=['POST'])
def user_id():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.get_json()
        result =  select_user_email(data["id"])
        return jsonify({"result": result})
    else:
        return jsonify({"result": "Wrong content type"})
    
change_notification_status = Blueprint("change_notification_status", __name__)
@change_notification_status.route("/user/post/changeNotificationStatus", methods=['POST'])
def notification_status():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.get_json()
        update_notification_status(data["id"], data["status"])
        return jsonify({"result": "changed"})
    else:
        return jsonify({"result": "Wrong content type"})