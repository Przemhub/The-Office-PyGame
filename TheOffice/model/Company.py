class Company:
    def  __init__(self):
        self.employee_num = 0
        self.money = 0
        self.papers_sold = 0
        self.decoration_num = 0

    def update_papers(self,papers):
        self.papers_sold += papers
        self.money += papers * 5

    def update_emp_num(self):
        self.employee_num += 1
