class NeedsService:
    def __init__(self, thread):
        self.thread = thread

    def insert_emp(self, emp):
        self.thread.insert_emp(emp)