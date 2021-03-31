from pygame.threads import Thread


class EmployeeTaskThread(Thread):
    def __init__(self):
        self.emp_dict = {}
        Thread.__init__(self)

    def setup_dict(self, employee_dict):
        self.emp_dict = employee_dict

    def insert_emp(self, employee):
        self.emp_dict[id(employee)] = employee

    def empty_dict(self):
        if len(self.emp_dict) == 0:
            return True
        return False

    def pop_emp(self, employee):
        self.emp_dict.pop(id(employee))

    def get_emp(self, id):
        return self.emp_dict.get(id)