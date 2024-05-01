import pygame

from controller.BuildController import BuildingController
from controller.EmployeeController import EmployeeController
from controller.KeyboardController import KeyboardController
from controller.MouseController import MouseController
from model.Company import Company
from model.Ground import Ground
from model.Time.Clock import Clock
from service.RoomType import RoomType


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
                if event.type is pygame.QUIT:
                    self.employee_controller.employee_service.emp_need_thread.destroy()
                    self.employee_controller.employee_service.emp_task_thread.destroy()
                    pygame.sys.exit(0)
                self.keyboard_controller.execute_event(event)
                self.mouse_controller.execute_event(event)
                self.employee_controller.grab_employee_event(event)
            self.screen.fill((155, 232, 255))
            self.employee_controller.drag_employee()
            self.update_text()
            self.mouse_controller.scroll_view()
            self.mouse_controller.move_cursor()
            self.employee_controller.move_employees()
            self.ingame_clock.tick()
            self.draw()
            self.clock.tick(30)
            pygame.display.flip()

    def update_text(self):
        self.paper_sold = self.font.render(
            "Paper sold: " + str(self.employee_controller.employee_service.employee_list[0]._stats.papers_sold), True,
            (255, 255, 255))
        self.money = self.font.render("Money: " + str(self._company.money), True, (255, 255, 255))
        self.hunger = self.font.render(
            "Hunger: " + str(self.employee_controller.employee_service.employee_list[0]._needs.hunger), True,
            (255, 255, 255))
        self.stress = self.font.render(
            "Stress: " + str(self.employee_controller.employee_service.employee_list[0]._needs.stress), True,
            (255, 255, 255))

        self.motivation = self.font.render(
            "Motivation: " + str(self.employee_controller.employee_service.employee_list[0]._needs.motivation), True,
            (255, 255, 255))
        self.clock_time = self.font.render("Time: " + self.ingame_clock.get_progress_str(), True, (255, 255, 255))


    def draw(self):
        for floor in range(0, len(self.building_controller.get_room_board())):
            for room in self.building_controller.get_room_board()[floor]:
                self.screen.blit(room.image, room.rect)
                # for action_obj in room.action_objects:
                #     pygame.draw.rect(self.screen,(0,0,0),action_obj.rect)
        if self.mouse_controller.cursor.is_active():
            self.screen.blit(self.mouse_controller.cursor.image, self.mouse_controller.cursor.rect)
        for emp in self.employee_controller.employee_service.employee_list:
            self.screen.blit(emp.image, emp.rect)

        self.screen.blit(self.paper_sold, self.text_rect)
        self.screen.blit(self.money, self.text_rect.move(0, 25))
        self.screen.blit(self.clock_time, self.text_rect.move(0, 50))
        self.screen.blit(self.hunger, self.text_rect.move(0, 125))
        self.screen.blit(self.stress, self.text_rect.move(0, 100))
        self.screen.blit(self.motivation, self.text_rect.move(0, 150))


    def init_objects(self):
        self.ground = Ground(self.screen)
        self._company = Company()
        self.ingame_clock = Clock()
        self.building_controller = BuildingController()
        self.employee_controller = EmployeeController(self.building_controller.get_room_board(), self.ground)
        self.mouse_controller = MouseController(self.screen, self.employee_controller.employee_service.employee_list,
                                                self.building_controller, self.ground)
        self.keyboard_controller = KeyboardController(self.employee_controller, self.mouse_controller, self._company)

        self.employee_controller.create_employee(100, 200, self._company)
        self.building_controller.build_room((0,0), RoomType.CORRIDOR)
        self.building_controller.build_room((1,0), RoomType.DINING_ROOM)
        self.building_controller.build_room((2,0), RoomType.OFFICE_ROOM)
        self.building_controller.build_room((3,0), RoomType.ELEVATOR)
        self.building_controller.build_room((4,0), RoomType.CORRIDOR)
        self.building_controller.build_room((5,0), RoomType.CONFERENCE_ROOM)
        self.building_controller.build_room((6,0), RoomType.CORRIDOR)


        # self.employee_controller.create_employee(120, 280, "Bob2", self._company)
        self.employee_controller.employee_service.employee_list[0]._needs.hunger = 20
        self.employee_controller.employee_service.employee_list[0]._needs.stress = 20

    def init_texts(self):
        self.font = pygame.font.SysFont("Calibri", 24, True)
        self.paper_sold = self.font.render("Paper sold: ", True, (255, 255, 255))
        self.money = self.font.render("Money: ", True, (255, 255, 255))
        self.clock_time = self.font.render("Time: ", True, (255, 255, 255))
        self.text_rect = pygame.Rect(300, 100, 1, 1)

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


if __name__ == "__main__":
    Game()
