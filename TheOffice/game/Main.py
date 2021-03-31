import sys

import pygame

from activities.employees.HustleThread import HustleThread
from activities.employees.ConsumeThread import ConsumeThread
from data.Company import CompanyData
from game.events.employee.EmployeeEventHandler import EmployeeEventHandler
from objects.Employee import EmployeeObject
from objects.rooms.RoomSingleton import RoomSingleton


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
                self.emp_event_handler.handle_drag_event(event)
            self.screen.fill((136,205,235))
            self.emp_event_handler.drag_emp_if_selected()
            self.update_text()
            self.draw()
            pygame.display.flip()

    def update_text(self):
        self.paper_sold = self.font.render("Paper sold: "+str(self.emp_event_handler.employee_list[0]._data._stats.papers_sold),True,(255,255,255))
        self.money = self.font.render("Money: " + str(self._company.money),True,(255,255,255))

    def init_objects(self):
        hustle_thread = HustleThread()
        consumer_thread = ConsumeThread()
        hustle_thread.start()
        self.building = RoomSingleton()
        self.building.build_office((0, 0))
        self.building.build_dining_room((1,0))
        self.emp_event_handler = EmployeeEventHandler(self.building, hustle_thread, consumer_thread)

        self._company = CompanyData()
        emp = EmployeeObject(100, 10, "Bob", self._company)
        emp2 = EmployeeObject(120,10,"Bob2",self._company)
        self.emp_event_handler.add_employee(emp)
        self.emp_event_handler.add_employee(emp2)


    def draw(self):
        for floor in range(0,len(self.building.room_board)):
            for room in self.building.room_board[floor]:
                self.screen.blit(room.image, room.rect)
        for emp in self.emp_event_handler.employee_list:
            self.screen.blit(emp.image, emp.rect)
        self.screen.blit(self.paper_sold,pygame.Rect(300,100,1,1))
        self.screen.blit(self.money, pygame.Rect(300, 200,1,1))

    def init_texts(self):
        self.font = pygame.font.SysFont("Calibri",24,True)
        self.paper_sold = self.font.render("Paper sold: ",True,(255,255,255))
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
        room_singleton.build_office((0,0))
if __name__=="__main__":
    Game()