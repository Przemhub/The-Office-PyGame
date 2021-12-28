import sys

import pygame

from controller.EmployeeController import EmployeeController
from model.Company import CompanyData
from model.Employee.Employee import Employee
from model.RoomSingleton import RoomSingleton
from service.EmployeeServices.ConsumeService import ConsumeService
from service.EmployeeServices.NeedsService import NeedsService
from service.EmployeeServices.WorkingService import WorkingService


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
        hustle_thread = WorkingService()
        consumer_thread = ConsumeService()
        needs_thread = NeedsService()
        hustle_thread.start()
        needs_thread.start()
        consumer_thread.start()
        self.building = RoomSingleton()


        self.building.build_dining_room((0, 0))
        self.building.build_office((1, 0))
        
        self.employee_controller = EmployeeController(self.building, hustle_thread, consumer_thread, needs_thread)

        self._company = CompanyData()
        emp = Employee(100, 10, "Bob", self._company)
        emp2 = Employee(120, 10, "Bob2", self._company)
        self.employee_controller.employee_service.add_employee(emp)
        self.employee_controller.employee_service.add_employee(emp2)


    def draw(self):
        for floor in range(0, len(self.building.room_board)):
            for room in self.building.room_board[floor].values():
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
        room_singleton = RoomSingleton()
        room_singleton.build_office((0, 0))


if __name__ == "__main__":
    Game()
