from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees
if __name__ == '__main__':
    current_time=datetime.today() 
    get_employees()
    calculate_salary()
    print(current_time)