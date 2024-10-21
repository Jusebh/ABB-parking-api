import calendar
from datetime import datetime
from sqlalchemy import select, desc
from sqlalchemy.orm import Session
from database.models import Reservations, ReservationsDates, Users, PriorityGroups
from database.operations.connecting import connect_to_database
from database.select_confing_data import select_config_data

def select_reservation_by_priority(day, month, priority):
    with Session(connect_to_database()) as session:
        try:
            next_month_open_hour = int(select_config_data("next_month_opening_hour"))
            current_hour = datetime.now().hour
            current_day = datetime.now().day
            current_year = datetime.now().year
            current_month = datetime.now().month
            last_day = calendar.monthrange(current_year, int(month))[1]
            
            if int(current_day) == last_day and current_hour >= next_month_open_hour and current_month == 12:
                current_year += 1
            
            date = f"{day}-{month}-{current_year}"
            stmt = select(ReservationsDates).join(ReservationsDates.reservations).join(Reservations.users).join(Users.priority_groups).where(ReservationsDates.date_of_reservation == date).where(PriorityGroups.priority > int(priority)).order_by(desc(PriorityGroups.priority)).order_by(desc(Reservations.created_at))
            try:
                result = session.scalars(stmt).first()  
                session.close()         
                return result.reservation_id
            except:
                session.close()
                return None
        except:
            session.close()
            return None
        
        
        
        
        
        