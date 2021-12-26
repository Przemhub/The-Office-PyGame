from pygame import time

from service.EmployeeServices.EmployeeTaskThread import EmployeeTaskThread


class WorkingService(EmployeeTaskThread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            if self.empty_dict() == False:
                for employee in self.emp_dict.values():
                    if employee.can_work():
                        employee.make_sale()
                    else:
                        self.pop_emp(employee)
                time.wait(1000)
