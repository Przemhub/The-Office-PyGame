import pygame

from controller.MouseController import MouseController
from service.RoomType import RoomType


class KeyboardController:
    def __init__(self, employee_controller, mouse_controller: MouseController, company):
        self.employee_controller = employee_controller
        self.cursor = mouse_controller.cursor
        self._company = company

    def execute_event(self, e):
        if e.type == pygame.KEYDOWN:
            if e.key is pygame.K_q:
                print("pressed")
                self.employee_controller.create_employee(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], self._company)
            elif e.key is pygame.K_1:
                self.cursor.set_cursor_object(RoomType.OFFICE_ROOM)
            elif e.key is pygame.K_2:
                self.cursor.set_cursor_object(RoomType.DINING_ROOM)
            elif e.key is pygame.K_3:
                self.cursor.set_cursor_object(RoomType.GAME_ROOM)
