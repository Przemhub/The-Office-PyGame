import pygame

from controller.BuildController import BuildingController
from model.CursorObject import CursorObject


class MouseController:
    def __init__(self, screen, employee_list, building_controller: BuildingController, ground):
        self.screen = screen
        self.emp_list = employee_list
        self.building_controller = building_controller
        self.room_board = building_controller.building_service.room_board
        self.corridors = building_controller.building_service.corridors
        self.ground = ground
        self.speed = 15
        self.threshold = 70
        self.cursor = CursorObject()
        self.board_pos = (-1,-1)

    def scroll_view(self):
        if pygame.mouse.get_pos()[0] >= self.screen.get_width() - self.threshold:
            self.move_objects(-self.speed, 0)
        elif pygame.mouse.get_pos()[0] <= self.threshold:
            self.move_objects(self.speed, 0)
        elif pygame.mouse.get_pos()[1] <= self.threshold:
            self.ground.move(self.speed)
            self.move_objects(0, self.speed)
        elif pygame.mouse.get_pos()[1] >= self.screen.get_height() - self.threshold:
            self.ground.move(-self.speed)
            self.move_objects(0, -self.speed)

    def move_cursor(self):
        self.cursor.relocate(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        if self.cursor.is_active():
            for floor in range (0, len(self.room_board)):
                for room in self.room_board[floor]:
                    if self.cursor.collides_with(room.rect):
                        self.cursor.rect.x = room.rect.x
                        self.cursor.rect.y = room.rect.y
                        self.board_pos = (self.room_board[floor].index(room), floor)

    def place_building(self):
        self.building_controller.build_room(self.board_pos, self.cursor.object_id)
        self.cursor.clear_cursor()

    def move_objects(self, x, y):
        for emp in self.emp_list:
            emp.rect = emp.rect.move(x, y)
        for floor in self.room_board:
            for room in floor:
                room.rect = room.rect.move(x, y)
                for a_obj in room.action_objects:
                    a_obj.rect = a_obj.rect.move(x, y)
        for corridor in self.corridors:
            corridor.rect = corridor.rect.move(x, y)

    def execute_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.cursor.is_active():
            self.place_building()