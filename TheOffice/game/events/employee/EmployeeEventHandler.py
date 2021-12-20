import pygame

from game.events.employee.EmpDeskEvent import EmpDeskEvent


class EmployeeEventHandler:
    def __init__(self, room_singleton, hustle_thread, consumer_thread):
        self.employee_list = []
        self.init_extras()
        self.building_observer = room_singleton
        self.init_threads(hustle_thread,consumer_thread)
        self.emp_desk_event = EmpDeskEvent(self.building_observer.room_board, self.hustle_thread, self.consumer_thread)

    def init_threads(self,hustle_thread,consumer_thread):
        self.hustle_thread = hustle_thread
        self.consumer_thread = consumer_thread

    def init_extras(self):
        self.dragged_emp_i = -1

    def add_employee(self,emp):
        self.employee_list.append(emp)

    def drag_emp_if_selected(self):
        if self.dragged_emp_i != -1:
            self.employee_list[self.dragged_emp_i].rect.x = pygame.mouse.get_pos()[0]
            self.employee_list[self.dragged_emp_i].rect.y = pygame.mouse.get_pos()[1]


    def handle_drag_event(self,event):
        for i in range (0, len(self.employee_list)):
            if event.type == pygame.MOUSEBUTTONDOWN and self.employee_list[i].rect.collidepoint(pygame.mouse.get_pos()):
                self.dragged_emp_i = i
                self.handle_emp_desk_detach_event(self.employee_list[self.dragged_emp_i])
            if event.type == pygame.MOUSEBUTTONUP and self.employee_list[i].rect.collidepoint(pygame.mouse.get_pos()):
                self.handle_emp_desk_collide_event(self.employee_list[self.dragged_emp_i])
                self.dragged_emp_i = -1
                break

    def handle_emp_desk_detach_event(self,emp):
        self.emp_desk_event.handle_detach_event(emp)

    def handle_emp_desk_collide_event(self,emp):
        self.emp_desk_event.handle_collide_event(emp)
