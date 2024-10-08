from flask import Blueprint, jsonify
from datetime import date
import calendar

current_month = Blueprint("current_month", __name__)
@current_month.route("/user/dates/currentMonth")
def day_of_month():
    months = date.today().month
    return jsonify({"current_month": months})

table_of_days = Blueprint("table_of_days", __name__)
@table_of_days.route("/user/dates/tableOfDates")
def days_table():
    months = date.today().month
    year = date.today().year
    num_days = calendar.monthrange(year, months)
    weekdayTab = []

    for i in range(num_days[1]):
        weekday = date(year, months, i+1).isoweekday()
        if ((weekday) == 6 or (weekday) == 7):
            pass
        else:
            weekdayTab.append([i+1, weekday])
    return jsonify(weekdayTab)