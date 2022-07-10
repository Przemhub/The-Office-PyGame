from pygame import time

from service.EmployeeThreads.EmployeeTaskThread import EmployeeTaskThread


class WorkingService:
    def __init__(self,thread):
        self.thread = thread

    def start(self):
        self.thread.start()

    def insert_emp(self, emp):
        self.thread.insert_emp_work(emp)

    def pop_emp(self, emp):
        self.thread.pop_emp_work(emp)
