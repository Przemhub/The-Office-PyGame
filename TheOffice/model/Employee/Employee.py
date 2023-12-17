from pygame import sprite, image, mask, mouse, Rect

from model.Employee.Abilities import Abilities
from model.Employee.Needs import Needs
from model.Employee.SaleCalculator import SaleCalculator
from model.Employee.Statistics import Statistics
from model.Furniture import Furniture


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
        self.assigned_furniture = None

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

    def set_desk(self, action_object : Furniture):
        self.assigned_furniture = action_object

    def is_sitting_down(self):
        return self.assigned_furniture is not None

    def remove_from_desk(self):
        if self.assigned_furniture is not None:
            self.assigned_furniture.taken = False
        self.assigned_furniture = None
        self.image = image.load("../resources/employees/employee.png")

    def init_data(self):
        self._stats = Statistics()
        self._needs = Needs()
        self._abilities = Abilities()
        self.direction = ''
        self.destination = None

    def make_sale(self):
        sale = self._calculator.calculate_sale()
        print("sale", sale)
        self._stats.papers_sold += sale
        self.update_company(sale)

    def can_work(self):
        if self.is_hungry():
            return False
        elif self.is_unmotivated():
            return False
        elif self.is_stressed():
            return False
        return True

    def update_company(self, papers):
        self.company_observer.update_papers(papers)

    def is_idle(self):
        return self.destination is None and not (self.is_working() or self.is_eating() or self.is_playing())

    def is_working(self):
        return type(self.assigned_furniture).__name__ == "OfficeDesk" and not (self.is_hungry() or self.is_stressed())

    def is_playing(self):
        return type(self.assigned_furniture).__name__ == "GameSpot" and not (self.is_hungry() or self.is_relaxed())

    def is_eating(self):
        return type(self.assigned_furniture).__name__ == "DiningChair" and not self.is_satiated()

    def is_satiated(self):
        return self._needs.hunger > 99

    def is_relaxed(self):
        return self._needs.stress > 99

    def is_hungry(self):
        return self._needs.hunger <= self._abilities.stomach

    def is_stressed(self):
        return self._needs.stress <= self._abilities.anxiety

    def is_unmotivated(self):
        return self._needs.motivation <= 0

    def is_dragged(self):
        return self.rect.collidepoint(mouse.get_pos())

    def is_sitting_on(self, furniture):
        return type(self.assigned_furniture).__name__ == furniture

    def change_walking_sprite(self, walking_sprite):
        self.image = self.walk_images[walking_sprite]
        self.current_position = walking_sprite

    def sitting_sprite_right(self):
        self.image = image.load("../resources/employees/employee_sit.png")

    def sitting_sprite_left(self):
        self.image = image.load("../resources/employees/employee_sit2.png")

    def sitting_sprite_back(self):
        self.image = image.load("../resources/employees/employee_sit3.png")

    def sitting_sprite_back_game(self):
        self.image = image.load("../resources/employees/employee_sit4.png")
