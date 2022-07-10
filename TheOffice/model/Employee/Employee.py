from pygame import sprite, image, mask
from pygame.rect import Rect

from model.Employee.Abilities import Abilities
from model.Employee.Needs import Needs
from model.Employee.SaleCalculator import SaleCalculator
from model.Employee.Statistics import Statistics


class Employee(sprite.Sprite):

    def __init__(self, x, y, name, company):
        sprite.Sprite.__init__(self)
        self.name = name
        self.current_position = -1
        self.company_observer = company
        self.init_sprite(x, y)
        self.init_data()
        self._calculator = SaleCalculator(self._needs, self._stats)
        self.company_observer.update_emp_num()
        self.desk_observer = None

    def init_sprite(self, x, y):

        self.WALK_LEFT = 0
        self.WALK_LEFT2 = 1
        self.WALK_LEFT3 = 2
        self.WALK_LEFT4 = 3
        self.WALK_RIGHT = 4
        self.WALK_RIGHT2 = 5
        self.WALK_RIGHT3 = 6
        self.WALK_RIGHT4 = 7
        img_names = [
            "employee_walk_left.png",
            "employee_walk_left2.png",
            "employee_walk_left3.png",
            "employee_walk_left2.png",
            "employee_walk_right.png",
            "employee_walk_right2.png",
            "employee_walk_right3.png",
            "employee_walk_right2.png",
        ]
        self.image = image.load("../resources/employees/employee.png")
        self.walk_images = [image.load("../resources/employees/" + img_name) for img_name in img_names]
        self.mask = mask.from_surface(self.image)
        self.rect = Rect(x, y, self.image.get_width(), self.image.get_height())

    def set_desk(self, action_objects):
        self.desk_observer = action_objects

    def is_sitting_down(self):
        return self.desk_observer != None

    def remove_from_desk(self):
        self.desk_observer.taken = False
        self.desk_observer = None
        self.image = image.load("../resources/employees/employee.png")

    def init_data(self):
        self._stats = Statistics()
        self._needs = Needs()
        self._abilities = Abilities()
        self.destination = None

    def make_sale(self):
        sale = self._calculator.calculate_sale()
        print("sale",sale)
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

    def change_walking_sprite(self, walking_sprite):
        self.image = self.walk_images[walking_sprite]
        self.current_position = walking_sprite

    def sitting_sprite_right(self):
        self.image = image.load("../resources/employees/employee_sit.png")
    def sitting_sprite_left(self):
        self.image = image.load("../resources/employees/employee_sit2.png")
    def sitting_sprite_back(self):
        self.image = image.load("../resources/employees/employee_sit3.png")
    def is_satiated(self):
        return self._needs.hunger >= 99
    def is_hungry(self):
        return self._needs.hunger <= 10