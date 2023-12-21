from pygame import Surface

from model.Employee.Employee import Employee


class Ground:
    def __init__(self, screen: Surface):
        self.screen = screen
        self.y = screen.get_height() * 6 / 7

    def is_touching(self, emp: Employee):
        return emp.rect.y >= self.y

    def is_touching_adjusted(self, emp: Employee):
        return emp.rect.y + 30 >= self.y

    def move(self, y):
        self.y += y
