from flask import Blueprint, request, jsonify
from database.operations.adding.add_user import add_user

receive_data_of_reservation = Blueprint("receive_data_of_reservation", __name__)
@receive_data_of_reservation.route("/user/post/receiveDataOfReservation", methods=['POST'])
def data_of_reservation():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.get_json()
        try:
            add_user(data["email"])
            return jsonify({"succeed" : True})
        except Exception as e:
            return jsonify({"error" : str(e)})
    else:
        return jsonify("Wrong content type")