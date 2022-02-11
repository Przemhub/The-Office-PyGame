from pygame import time

from service.EmployeeServices.EmployeeTaskThread import EmployeeTaskThread


class WorkingService(EmployeeTaskThread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            if self.empty_dict() == False:
                i = 0
                for employee in self.emp_dict.values():
                    if employee.can_work():
                        employee.make_sale()
                        if i >= 3:
                            employee._needs.increase_stress()
                            employee._needs.decrease_motivation()
                            i=0
                        else:
                            i+=1
                time.wait(1000)
