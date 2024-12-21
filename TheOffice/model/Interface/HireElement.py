from pygame import transform, image

from model.Interface.InterfaceElement import InterfaceElement


class HireElement(InterfaceElement):
    def __init__(self, rect, img):
        super().__init__(rect, img)
        self.emp_list = [
            {"name": "Bob", "abilities": (6, 4, 5), "images_path": "../resources/employees/male/emp1/"},
            {"name": "Bob", "abilities": (6, 4, 5), "images_path": "../resources/employees/male/emp2/"},
            {"name": "Bob", "abilities": (6, 4, 5), "images_path": "../resources/employees/male/emp3/"},
            {"name": "Bob", "abilities": (6, 4, 5), "images_path": "../resources/employees/female/emp1/"},
        ]
        self.emp_index = 0

    def get_emp_image(self):
        return transform.scale(image.load(self.emp_list[self.emp_index].get("images_path") + "employee.png"), (60,140))
