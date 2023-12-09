import pygame

from service.EmployeeServices.EmployeeService import EmployeeService


class EmployeeController:
    def __init__(self, room_board, ground):
        self.employee_service = EmployeeService(room_board, ground)

    def create_employee(self, x, y, name, company):
        self.employee_service.create_employee(x, y, name, company)

    def grab_employee_event(self, event):
        for i in range(0, len(self.employee_service.employee_list)):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.employee_service.pick_up_employee(i)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.employee_service.put_down_employee(i)

    def drag_employee(self):
        self.employee_service.drag_emp_if_selected()

    def move_employees(self):
        self.employee_service.check_employees_needs_and_move()
