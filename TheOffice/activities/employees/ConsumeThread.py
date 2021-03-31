from pygame import time

from activities.employees.EmployeeTaskThread import EmployeeTaskThread


class ConsumeThread(EmployeeTaskThread):
    def __init__(self):
        EmployeeTaskThread.__init__(self)

    def run(self):
        while True:
            if self.empty_dict() == False:
                for employee in  self.emp_dict.values():
                    employee._needs.decrease_needs()
                time.wait(5000)
