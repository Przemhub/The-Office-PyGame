from pygame import time

from service.EmployeeServices.EmployeeTaskThread import EmployeeTaskThread


class ConsumeService(EmployeeTaskThread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            if self.empty_dict() == False:
                for employee in  self.emp_dict.values():
                    employee._needs.decrease_needs()
                time.wait(5000)
