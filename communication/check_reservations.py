from database.operations.selecting.select_reservation_to_notify import select_reservation_to_notify
from communication.mail import mail

def check_reservations():
    users_to_notify = select_reservation_to_notify()
    for user in users_to_notify:
        mail(user["email"], user["date"])