from pygame import time
from pygame.threads import Thread


class EmployeeNeedThread(Thread):
    def __init__(self):
        super().__init__()
        self.emp_dict = {}



    def insert_emp(self, employee):
        self.emp_dict[id(employee)] = employee

    def empty_dict(self):
        if len(self.emp_dict) == 0:
            return True
        return False

    def pop_emp(self, employee):
        self.emp_dict.pop(id(employee))

    def get_emp(self, identity):
        return self.emp_dict.get(identity)

    def run(self):
        while True:
            if self.empty_dict() == False:
                for employee in self.emp_dict.values():
                    if employee.can_work():
                        employee._needs.increase_hunger()
                time.wait(10000)
