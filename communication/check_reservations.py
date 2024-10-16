from database.operations.selecting.select_reservation_to_notify import select_reservation_to_notify
from communication.notify_mail import notify_mail

def check_reservations():
    users_to_notify = select_reservation_to_notify()
    for user in users_to_notify:
        notify_mail(user["email"], user["date"])