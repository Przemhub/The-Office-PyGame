import sys

import pygame

from controller.EmployeeController import EmployeeController
from model.Company import CompanyData
from service.BuildingService import BuildingService


class Game:
    def __init__(self):
        pygame.init()
        self.init_screen()
        self.init_texts()
        self.init_objects()
        self.main_loop()

    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                self.employee_controller.grab_employee_event(event)
            self.screen.fill((136, 205, 235))
            self.employee_controller.employee_service.drag_emp_if_selected()
            self.update_text()
            self.draw()
            pygame.display.flip()

    def update_text(self):
        self.paper_sold = self.font.render(
            "Paper sold: " + str(self.employee_controller.employee_service.employee_list[0]._stats.papers_sold), True,
            (255, 255, 255))
        self.money = self.font.render("Money: " + str(self._company.money), True, (255, 255, 255))
        self.needs = self.font.render(
            "Hunger: " + str(self.employee_controller.employee_service.employee_list[0]._needs.hunger), True,
            (255, 255, 255))

    def init_objects(self):
        self.build_service = BuildingService()
        self.build_service.build_dining_room((0, 0))
        self.build_service.build_office((1, 0))
        self.employee_controller = EmployeeController(self.build_service)
        self._company = CompanyData()
        self.employee_controller.employee_service.create_employee(100, 10, "Bob", self._company)
        self.employee_controller.employee_service.create_employee(120, 10, "Bob2", self._company)

    def draw(self):
        for floor in range(0, len(self.build_service.room_board)):
            for room in self.build_service.room_board[floor].values():
                self.screen.blit(room.image, room.rect)
        for emp in self.employee_controller.employee_service.employee_list:
            self.screen.blit(emp.image, emp.rect)

        self.screen.blit(self.paper_sold, pygame.Rect(300, 100, 1, 1))
        self.screen.blit(self.money, pygame.Rect(300, 200, 1, 1))
        self.screen.blit(self.needs, pygame.Rect(300, 250, 1, 1))

    def init_texts(self):
        self.font = pygame.font.SysFont("Calibri", 24, True)
        self.paper_sold = self.font.render("Paper sold: ", True, (255, 255, 255))
        self.money = self.font.render("Money: ", True, (255, 255, 255))

    def init_screen(self):
        pygame.display.init()
        self.res_list = [
            (1600, 900),
            (1440, 900),
            (1360, 768),
            (1280, 720),
            (800, 600)
        ]
        self.res_option = 4
        self.full_screen = False
        self.current_res = self.res_list[4]
        self.screen = pygame.display.set_mode(self.current_res)

    def init_map(self):
        room_singleton = BuildingService()
        room_singleton.build_office((0, 0))


if __name__ == "__main__":
    Game()
