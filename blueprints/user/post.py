from flask import Blueprint, request, jsonify
from database.operations.adding.add_user import add_user
from database.operations.adding.add_reservation import add_reservation
from datetime import datetime

receive_user_data = Blueprint("receive_user_data", __name__)
@receive_user_data.route("/user/post/receiveUserData", methods=['POST'])
def user_data():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.get_json()
        try:
            add_user(data["email"])
            return jsonify({"result" : "Succed"})
        except Exception as e:
            return jsonify({"result" : f"Error: {str(e)}"})
    else:
        return jsonify({"result":"Wrong content type"})
    
receive_reservation_data = Blueprint("receive_reservation_data", __name__)
@receive_reservation_data.route("/user/post/receiveReservationData", methods=['POST'])
def reservation_data():
    content_type = request.headers.get('Content-Type')
    current_hour = datetime.now().hour
    current_day = datetime.now().day
    current_month = datetime.now().month
    result = []
    if (content_type == 'application/json'):
        data = request.get_json()
        dates = data["dates"]
        for i in dates:
            if int(i) <= current_day and int(data["month"] == current_month):
                if i == current_day and current_hour >= 16:
                    result.append(f"Reservation on {i} can't be completed (it's too late).\n")
                else:
                    result.append(f"Reservation on past date can't be made.\n")
            else:
                try:
                    add_reservation(data["id"], i, data["month"])
                    result.append(f"Reservation on day {i} was made.")
                except Exception as e:
                    result.append(f"Reservation on day {i} can't be made, because of {e} error.")
        return jsonify({"result": result})
    else:
        return jsonify("Wrong content type")