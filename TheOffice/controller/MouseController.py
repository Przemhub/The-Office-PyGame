import pygame


class MouseController:
    def __init__(self, screen, employee_list, room_board, ground):
        self.screen = screen
        self.emp_list = employee_list
        self.room_board = room_board
        self.ground = ground

    def scroll_view(self):
        if pygame.mouse.get_pos()[0] >= self.screen.get_width() - 10:
            for emp in self.emp_list:
                emp.rect = emp.rect.move(-10, 0)
            for floor in self.room_board.values():
                for room in floor.values():
                    room.rect = room.rect.move(-10, 0)
                    for a_obj in room.action_objects:
                        a_obj.rect = a_obj.rect.move(-10, 0)

        elif pygame.mouse.get_pos()[0] <= 10:
            for emp in self.emp_list:
                emp.rect = emp.rect.move(10, 0)
            for floor in self.room_board.values():
                for room in floor.values():
                    room.rect = room.rect.move(10, 0)
                    for a_obj in room.action_objects:
                        a_obj.rect = a_obj.rect.move(10, 0)
        elif pygame.mouse.get_pos()[1] <= 10:
            self.ground.move(10)
            for emp in self.emp_list:
                emp.rect = emp.rect.move(0, 10)
            for floor in self.room_board.values():
                for room in floor.values():
                    room.rect = room.rect.move(0, 10)
                    for a_obj in room.action_objects:
                        a_obj.rect = a_obj.rect.move(0, 10)
        elif pygame.mouse.get_pos()[1] >= self.screen.get_height() - 10:
            self.ground.move(-10)
            for emp in self.emp_list:
                emp.rect = emp.rect.move(0, -10)
            for floor in self.room_board.values():
                for room in floor.values():
                    room.rect = room.rect.move(0, -10)
                    for a_obj in room.action_objects:
                        a_obj.rect = a_obj.rect.move(0, -10)
