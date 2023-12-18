from service.EmployeeThreads.EmployeeNeedThread import EmployeeNeedThread


class NeedsService:
    def __init__(self, thread : EmployeeNeedThread):
        self.need_thread = thread

    def insert_emp(self, emp):
        self.need_thread.insert_emp(emp)