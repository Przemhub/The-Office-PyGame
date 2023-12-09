from pygame import time
from pygame.threads import Thread


class EmployeeTaskThread(Thread):

    def __init__(self):
        self.work_dict = {}
        self.hunger_dict = {}
        self.stress_dict = {}
        self.stop = False
        super().__init__()

    def empty_dict(self):
        return len(self.work_dict) == 0 and len(self.hunger_dict) == 0 and len(self.stress_dict) == 0

    def insert_emp_work(self, emp):
        self.work_dict[id(emp)] = emp

    def insert_emp_hunger(self, emp):
        self.hunger_dict[id(emp)] = emp

    def insert_emp_stress(self, emp):
        self.stress_dict[id(emp)] = emp

    def pop_emp_work(self, emp):
        if self.work_dict.__contains__(id(emp)):
            self.work_dict.pop(id(emp))

    def pop_emp_hunger(self, emp):
        if self.hunger_dict.__contains__(id(emp)):
            self.hunger_dict.pop(id(emp))

    def pop_emp_stress(self, emp):
        self.stress_dict.pop(id(emp))

    def run(self):
        while not self.stop:
            if self.empty_dict() == False:
                i = 0
                for employee in self.work_dict.values():
                    if employee.can_work():
                        employee.make_sale()
                        if i >= 3:
                            employee._needs.increase_stress()
                            employee._needs.decrease_motivation()
                            i = 0
                        else:
                            i += 1
                for employee in self.hunger_dict.values():
                    employee._needs.eat()
                time.wait(3000)

    def destroy(self):
        self.stop = True
