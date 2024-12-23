from pygame import transform, image, Surface

from model.Interface.InterfaceElement import InterfaceElement


class HireElement(InterfaceElement):
    def __init__(self, rect, img):
        super().__init__(rect, img)
        self._emp_list = [
            {"name": "Bob", "abilities": (6, 6, 6), "images_path": "../resources/employees/male/emp1/", "salary" : 2500},
            {"name": "Steve", "abilities": (6, 4, 7), "images_path": "../resources/employees/male/emp2/", "salary" : 2450},
            {"name": "Joe", "abilities": (4, 6, 8), "images_path": "../resources/employees/male/emp3/", "salary": 2400},
            {"name": "Marle", "abilities": (8, 7, 4), "images_path": "../resources/employees/female/emp1/", "salary" : 2550},
        ]
        self._emp_index = 0
        self.background_surface = Surface((240,190))
        self.background_surface.set_alpha(150)
        self.background_surface.fill((0,0,0))

    def get_current_emp_image(self):
        return transform.scale(image.load(self._emp_list[self._emp_index].get("images_path") + "employee.png"), (60, 140))

    def get_selected_emp(self):
        return self._emp_list[self._emp_index]

    def next_employee(self):
        self._emp_index += 1
        if self._emp_index == len(self._emp_list):
            self._emp_index = 0

    def previous_employee(self):
        self._emp_index -= 1
        if self._emp_index < 0:
            self._emp_index = len(self._emp_list) - 1
