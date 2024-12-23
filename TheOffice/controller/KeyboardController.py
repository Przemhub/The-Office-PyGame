import pygame
from pygame import K_LEFT, K_a

from controller.MouseController import MouseController
from service.RoomType import RoomType


class KeyboardController:
    def __init__(self, employee_controller, mouse_controller: MouseController, company):
        self.employee_controller = employee_controller
        self.cursor = mouse_controller.cursor
        self.building_controller = mouse_controller.building_controller
        self.mouse_controller = mouse_controller
        self.company = company
        self._speed = 15

    def execute_event(self, e):
        if e.type == pygame.KEYDOWN:
            if e.key is pygame.K_q:
                self.employee_controller.create_employee(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            elif e.key is pygame.K_1:
                self.cursor.set_cursor_object(RoomType.OFFICE_ROOM)
            elif e.key is pygame.K_2:
                self.cursor.set_cursor_object(RoomType.DINING_ROOM)
            elif e.key is pygame.K_3:
                self.cursor.set_cursor_object(RoomType.GAME_ROOM)
            elif e.key is pygame.K_f:
                self.building_controller.build_floor()

    def scroll_view(self):
        keys = pygame.key.get_pressed()
        if keys[K_a]:
            self.mouse_controller.move_objects(self._speed, 0)
        if keys[pygame.K_d]:
            self.mouse_controller.move_objects(-self._speed, 0)
        if keys[pygame.K_w]:
            self.mouse_controller.move_objects(0, self._speed)
        if keys[pygame.K_s]:
            self.mouse_controller.move_objects(0, -self._speed)

