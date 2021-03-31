import random

from numpy.matlib import rand

from data.employee.Abilities import Abilities
from data.employee.Needs import Needs
from data.employee.SaleCalculator import SaleCalculator
from data.employee.Statistics import Statistics


class EmployeeData:
    def __init__(self,name,company) -> object:
        self.name = name
        self.company_observer = company
        self.init_data()
        self._calculator = SaleCalculator(self._needs, self._stats)
        self.company_observer.update_emp_num()
        self.desk_observer = None

    def attach_desk(self, desk):
        print(desk.taken)
        self.desk_observer = desk

    def detach_desk(self):
        self.desk_observer = None

    def init_data(self):
        self._stats = Statistics()
        self._needs = Needs()
        self._abilities = Abilities()



    def make_sale(self):
        sale = self._calculator.calculate_sale()
        self._stats.papers_sold += sale
        self.update_company(sale)

    def can_work(self):
        if self._needs.is_hungry():
            return False
        elif self._needs.is_motivated():
            return False
        elif self._needs.is_stressed():
            return False
        return True

    def update_company(self,papers):
        self.company_observer.update_papers(papers)