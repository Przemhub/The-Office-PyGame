from service.EmployeeThreads.EmployeeTaskThread import EmployeeTaskThread


class WorkingService:
    def __init__(self,thread : EmployeeTaskThread):
        self.thread = thread

    def insert_emp(self, emp):
        self.thread.insert_emp_work(emp)

    def pop_emp(self, emp):
        self.thread.pop_emp_work(emp)
