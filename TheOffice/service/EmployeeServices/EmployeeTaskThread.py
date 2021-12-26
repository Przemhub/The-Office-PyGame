from pygame.threads import Thread


class EmployeeTaskThread(Thread):

    def __init__(self):
        super().__init__()
        self.emp_dict = {}

    def setup_dict(self, employee_dict):
        self.emp_dict = employee_dict

    def insert_emp(self, employee):
        print(employee)
        self.emp_dict[id(employee)] = employee

    def empty_dict(self):
        if len(self.emp_dict) == 0:
            return True
        return False

    def pop_emp(self, employee):
        self.emp_dict.pop(id(employee))

    def get_emp(self, identity):
        return self.emp_dict.get(identity)
