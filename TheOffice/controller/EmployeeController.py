import random

import pygame

from service.EmployeeServices.EmployeeManagement.EmployeeManagementService import EmployeeManagementService


class EmployeeController:
    def __init__(self, room_board, ground):
        self.employee_names = [
            "George",
            "Michael",
            "Bob",
            "Kayle",
            "John",
            "Mark",
            "Dane",
            "Tom",
            "Bill",
            "Howard",
            "Harry"
        ]
        self.employee_service = EmployeeManagementService(room_board, ground)

    def create_employee(self, x, y, company):
        self.employee_service.create_employee(x, y, self.employee_names[random.randint(0, len(self.employee_names)-1)], company)

    def grab_employee_event(self, event):
        for i in range(0, len(self.employee_service.employee_list)):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.employee_service.pick_up_employee(i)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.employee_service.put_down_employee()

    def drag_employee(self):
        self.employee_service.drag_emp_if_selected()

    def move_employees(self):
        self.employee_service.check_employees_needs_and_move()
