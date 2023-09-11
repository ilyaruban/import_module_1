from datetime import date
from application import salary
from application.db import people

if __name__ == '__main__':
    print(salary.calculate_salary(1, 2))
    people.get_employees('Data')
    print(date.today())
