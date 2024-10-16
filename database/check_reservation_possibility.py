import calendar
from datetime import datetime
from database.operations.adding.add_reservation import add_reservation
from communication.new_reservation_mail import new_reservation_mail
from database.select_confing_data import select_config_data
from database.operations.selecting.select_count_of_reservations import select_count_of_reservations
from database.operations.selecting.select_priority_group import select_priority_group
from database.operations.selecting.select_reservations_by_priority import select_reservation_by_priority
from database.operations.selecting.select_user_email import select_user_email
from database.operations.selecting.select_user_reservations_by_month import select_user_reservations_by_month
from database.operations.updating.update_reservation_status import update_reservation_status

def check_reservation_possibility(day: str, month: str, user_id, dates: list):
    email = select_user_email(int(user_id))
    number_of_parking_spots = int(select_config_data("parking_spots_number"))
    result = []
    current_year = datetime.now().year  
    last_day = calendar.monthrange(current_year, int(month))[1]  
    date = f"{day}-{month}-{str(datetime.now().year)}"
    datetime.strptime(date, "%d-%m-%Y").date()
    number_of_reservations = int(select_count_of_reservations(day, month))
    priority = int(select_priority_group(int(user_id)))
    reservations_on_current_month = select_user_reservations_by_month(user_id, month)
    for x in reservations_on_current_month:
        print(x)
        if x in dates:
            print("xd")
            result.append(f"You already have reservation on day {x}.")
            dates.remove(x)
    if priority == 1:
        for i in dates:
            if i <= last_day:
                number_of_reservations = select_count_of_reservations(i, month)
                if number_of_reservations == number_of_parking_spots:
                    reservation_to_replace = select_reservation_by_priority(i, month, priority)
                    update_reservation_status(reservation_to_replace, "Rejected")
        result += add_reservation(int(user_id), day, month, dates, priority)
        new_reservation_mail(email, dates)
    elif priority == 2:
        new_dates = dates.copy()
        for i in dates:
            if i <= last_day:
                number_of_reservations = int(select_count_of_reservations(i, month))
                if number_of_reservations == number_of_parking_spots:
                    reservation_to_replace = select_reservation_by_priority(i, month, priority)
                    if reservation_to_replace:
                        update_reservation_status(reservation_to_replace, "Rejected")
                    else:
                        new_dates.remove(i)
        result += add_reservation(int(user_id), day, month, new_dates, priority)
        new_reservation_mail(email, new_dates)
    elif priority == 3:
        new_dates = dates.copy()
        for i in dates:
            if i <= last_day:
                number_of_reservations = int(select_count_of_reservations(i, month))
                if number_of_reservations == number_of_parking_spots:
                    new_dates.remove(i)
        result += add_reservation(int(user_id), day, month, new_dates, priority)
        new_reservation_mail(email, new_dates)
    return result            