from pygame import time

from activities.employees.EmployeeTaskThread import EmployeeTaskThread


class HustleThread(EmployeeTaskThread):
    def __init__(self):
        EmployeeTaskThread.__init__(self)

    def run(self):
        while True:
            if self.empty_dict() == False:
                for employee in self.emp_dict.values():
                    if employee._data.can_work():
                        employee._data.make_sale()
                    else:
                        self.pop_emp(employee)
                time.wait(1000)
