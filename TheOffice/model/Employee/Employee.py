import random

from numpy.matlib import rand
from pygame import sprite, image, mask
from pygame.rect import Rect
from pygame.sprite import AbstractGroup

from model.Employee.Abilities import Abilities
from model.Employee.Needs import Needs
from model.Employee.SaleCalculator import SaleCalculator
from model.Employee.Statistics import Statistics


class Employee(sprite.Sprite):

    def __init__(self, x, y, name, company):
        sprite.Sprite.__init__(self)
        self.name = name
        self.company_observer = company
        self.init_sprite(x, y)
        self.init_data()
        self._calculator = SaleCalculator(self._needs, self._stats)
        self.company_observer.update_emp_num()
        self.desk_observer = None

    def init_sprite(self, x, y):

        self.image = image.load("../resources/employees/employee.png")
        self.mask = mask.from_surface(self.image)
        self.rect = Rect(x, y, self.image.get_width(), self.image.get_height())

    def attach_desk(self, action_objects):
        print(action_objects.taken)
        self.desk_observer = action_objects

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

    def update_company(self, papers):
        self.company_observer.update_papers(papers)
