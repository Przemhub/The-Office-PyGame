from pygame import transform, image, Surface, font
from pygame.rect import Rect

from model.Interface.InterfaceElement import InterfaceElement


class HireElement(InterfaceElement):
    def __init__(self, rect, img, company):
        super().__init__(rect, img)
        self._company = company
        self._emp_list = [
            {"name": "Bob", "abilities": (5, 5, 5), "images_path": "../resources/employees/male/emp1/", "salary": 3400},
            {"name": "Steve", "abilities": (6, 4, 7), "images_path": "../resources/employees/male/emp2/", "salary": 3400},
            {"name": "Joe", "abilities": (7, 4, 2), "images_path": "../resources/employees/male/emp3/", "salary": 3400},
            {"name": "Marle", "abilities": (3, 8, 8), "images_path": "../resources/employees/female/emp1/", "salary": 3400},
        ]
        self._emp_index = 0
        self.background_surface = Surface((240, 190))
        self.background_surface.set_alpha(150)
        self.background_surface.fill((0, 0, 0))
        self._sysfont = font.SysFont("Calibri", 30, True)
        self.capital_rect = Rect(20, 550, 50, 30)

    def get_current_emp_image(self):
        return transform.scale(image.load(self._emp_list[self._emp_index].get("images_path") + "employee.png"), (60, 140))

    def get_selected_emp(self):
        return self._emp_list[self._emp_index]

    def get_capital_text(self):
        return self._sysfont.render(str(self._company.money), True, (255, 255, 255), (0, 0, 0))

    def next_employee(self):
        self._emp_index += 1
        if self._emp_index == len(self._emp_list):
            self._emp_index = 0

    def previous_employee(self):
        self._emp_index -= 1
        if self._emp_index < 0:
            self._emp_index = len(self._emp_list) - 1
