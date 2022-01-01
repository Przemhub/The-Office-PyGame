from pygame import time

from service.EmployeeServices.EmployeeTaskThread import EmployeeTaskThread


class NeedsService(EmployeeTaskThread):
    def __init__(self):
        super().__init__()
        self.emp_dict = {}
    def run(self):
        while True:
            if self.empty_dict() == False:
                for employee in self.emp_dict.values():
                    if employee.can_work():
                        employee._needs.increase_hunger()
                time.wait(6000)