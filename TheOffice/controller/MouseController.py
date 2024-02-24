import pygame


class MouseController:
    def __init__(self, screen, employee_list, room_board, ground, corridors):
        self.screen = screen
        self.emp_list = employee_list
        self.room_board = room_board
        self.ground = ground
        self.speed = 15
        self.threshold = 70
        self.corridors = corridors

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

    def move_objects(self, x, y):
        for emp in self.emp_list:
            emp.rect = emp.rect.move(x, y)
        for floor in self.room_board:
            for room in floor:
                room.rect = room.rect.move(x, y)
                for a_obj in room.action_objects:
                    a_obj.rect = a_obj.rect.move(x, y)
        for corridor in self.corridors:
            corridor.rect = corridor.rect.move(x,y)
