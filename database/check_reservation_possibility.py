from database.operations.adding.add_reservation import add_reservation
from database.operations.selecting.select_count_of_reservations import select_count_of_reservations
from database.operations.selecting.select_priority_group import select_priority_group
from database.operations.selecting.select_reservations_by_priority import select_reservation_by_priority
from database.operations.updating.update_reservation_status import update_reservation_status
from datetime import datetime

def check_reservation_possibility(day: str, month: str, user_id, dates: list):
    date = f"{day}-{month}-{str(datetime.now().year)}"
    datetime.strptime(date, "%d-%m-%Y").date()
    number_of_reservations = int(select_count_of_reservations(day, month))
    priority = int(select_priority_group(int(user_id)))
    if priority == 1:
        for i in dates:
            number_of_reservations = select_count_of_reservations(i, month)
            if number_of_reservations == 25:
                reservation_to_replace = select_reservation_by_priority(i, month, priority)
                update_reservation_status(reservation_to_replace, "Odrzucony")
        result = add_reservation(int(user_id), day, month, dates, priority)
    elif priority == 2:
        new_dates = dates.copy()
        for i in dates:
            number_of_reservations = int(select_count_of_reservations(i, month))
            if number_of_reservations == 25:
                reservation_to_replace = select_reservation_by_priority(i, month, priority)
                if reservation_to_replace:
                    update_reservation_status(reservation_to_replace, "Odrzucony")
                else:
                    new_dates.remove(i)
        result = add_reservation(int(user_id), day, month, new_dates, priority)
    elif priority == 3:
        new_dates = dates.copy()
        for i in dates:
            number_of_reservations = int(select_count_of_reservations(i, month))
            if number_of_reservations == 25:
                new_dates.remove(i)
        result = add_reservation(int(user_id), day, month, new_dates, priority)
    return result            