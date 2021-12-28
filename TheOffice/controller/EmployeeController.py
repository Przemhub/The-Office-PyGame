import pygame

from service.EmployeeServices.EmployeeService import EmployeeService


class EmployeeController:
    def __init__(self, room_singleton, hustle_thread, consumer_thread, needs_thread):
        self.employee_service = EmployeeService(room_singleton.room_board, hustle_thread, consumer_thread,needs_thread)

    def grab_employee_event(self, event):
        for i in range(0, len(self.employee_service.employee_list)):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.employee_service.pick_up_employee(i)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.employee_service.put_down_employee(i)
