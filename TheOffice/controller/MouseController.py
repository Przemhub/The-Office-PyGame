import pygame


class MouseController:
    def __init__(self, screen, employee_list, room_board, ground):
        self.screen = screen
        self.emp_list = employee_list
        self.room_board = room_board
        self.ground = ground
        self.speed = 15
        self.threshold = 70

    def scroll_view(self):
        if pygame.mouse.get_pos()[0] >= self.screen.get_width() - self.threshold:
            for emp in self.emp_list:
                emp.rect = emp.rect.move(-self.speed, 0)
            for floor in self.room_board.values():
                for room in floor.values():
                    room.rect = room.rect.move(-self.speed, 0)
                    for a_obj in room.action_objects:
                        a_obj.rect = a_obj.rect.move(-self.speed, 0)

        elif pygame.mouse.get_pos()[0] <= self.threshold:
            for emp in self.emp_list:
                emp.rect = emp.rect.move(self.speed, 0)
            for floor in self.room_board.values():
                for room in floor.values():
                    room.rect = room.rect.move(self.speed, 0)
                    for a_obj in room.action_objects:
                        a_obj.rect = a_obj.rect.move(self.speed, 0)
        elif pygame.mouse.get_pos()[1] <= self.threshold:
            self.ground.move(self.speed)
            for emp in self.emp_list:
                emp.rect = emp.rect.move(0, self.speed)
            for floor in self.room_board.values():
                for room in floor.values():
                    room.rect = room.rect.move(0, self.speed)
                    for a_obj in room.action_objects:
                        a_obj.rect = a_obj.rect.move(0, self.speed)
        elif pygame.mouse.get_pos()[1] >= self.screen.get_height() - self.threshold:
            self.ground.move(-self.speed)
            for emp in self.emp_list:
                emp.rect = emp.rect.move(0, -self.speed)
            for floor in self.room_board.values():
                for room in floor.values():
                    room.rect = room.rect.move(0, -self.speed)
                    for a_obj in room.action_objects:
                        a_obj.rect = a_obj.rect.move(0, -self.speed)
