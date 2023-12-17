from service.EmployeeThreads.EmployeeTaskThread import EmployeeTaskThread


class ConsumeService:
    def __init__(self,thread : EmployeeTaskThread):
        self.task_thread = thread

    def insert_emp(self,emp):
        self.task_thread.insert_emp_hunger(emp)

    def pop_emp(self,emp):
        self.task_thread.pop_emp_hunger(emp)


