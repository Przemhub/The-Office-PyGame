import sys

import pygame

from controller.BuildController import BuildingController
from controller.EmployeeController import EmployeeController
from controller.MouseController import MouseController
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
            self.screen.fill((155, 232, 255))
            self.employee_controller.drag_employee()
            self.update_text()
            self.mouse_controller.scroll_view()
            self.employee_controller.check_employees_needs()
            self.draw()
            self.clock.tick(30)
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
        self.building_controller = BuildingController()
        self.building_controller.build_office((0, 0))
        self.building_controller.build_office((1, 0))
        self.building_controller.build_dining_room((2, 0))
        self.employee_controller = EmployeeController(self.building_controller.get_room_board())
        self.mouse_controller = MouseController(self.screen, self.employee_controller.employee_service.employee_list,
                                                self.building_controller.get_room_board())
        self._company = CompanyData()
        self.employee_controller.create_employee(100, 10, "Bob", self._company)
        self.employee_controller.create_employee(120, 280, "Bob2", self._company)
        self.employee_controller.employee_service.employee_list[0]._needs.hunger = 60

    def draw(self):
        for floor in range(0, len(self.building_controller.get_room_board())):
            for room in self.building_controller.get_room_board()[floor].values():
                self.screen.blit(room.image, room.rect)
        for emp in self.employee_controller.employee_service.employee_list:
            self.screen.blit(emp.image, emp.rect)

        self.screen.blit(self.paper_sold, pygame.Rect(300, 100, 1, 1))
        self.screen.blit(self.money, pygame.Rect(300, 200, 1, 1))
        self.screen.blit(self.needs, pygame.Rect(300, 250, 1, 1))
        # for floor in range(0, len(self.build_service.room_board)):
        #     for room in self.build_service.room_board[floor].values():
        #         for table in room.action_objects:
        #             pygame.draw.rect(self.screen, (0,0,0),table.rect)

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
        self.clock = pygame.time.Clock()

    def init_map(self):
        room_singleton = BuildingService()
        room_singleton.build_office((0, 0))


if __name__ == "__main__":
    Game()
