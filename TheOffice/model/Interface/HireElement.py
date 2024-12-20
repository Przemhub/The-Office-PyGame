from pygame import transform, image

from model.Interface.InterfaceElement import InterfaceElement


class HireElement(InterfaceElement):
    def __init__(self, rect, img):
        super().__init__(rect, img)
        self.emp_list = [
            {"name": "Bob", "abilities": (6, 4, 5), "image": transform.scale(image.load("../resources/employees/employee.png"), (60, 140))},
        ]
        self.emp_index = 0

    def get_emp_image(self):
        return self.emp_list[self.emp_index].get("image")
