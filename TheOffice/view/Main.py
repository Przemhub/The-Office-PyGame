import pygame

from controller.BuildController import BuildingController
from controller.EmployeeController import EmployeeController
from controller.KeyboardController import KeyboardController
from controller.MouseController import MouseController
from model.Company import Company
from model.Ground import Ground
from model.Interface.StaticElement import StaticElement
from service.Interface.InterfaceService import InterfaceService
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
            # self.mouse_controller.scroll_view()
            self.keyboard_controller.scroll_view()
            self.mouse_controller.move_cursor()
            self.employee_controller.move_employees()
            self.employee_controller.hire_employee(self.first_room.rect.midleft)
            self.interface_service.update_time()
            self.draw()
            self.clock.tick(30)
            pygame.display.flip()

    def update_text(self):
        self.paper_sold = self.font.render(
            "Paper sold: " + str(self.company.papers_sold), True,
            (255, 255, 255))
        self.money = self.font.render("Money: " + str(self.company.money), True, (255, 255, 255))
        self.hunger = self.font.render(
            "Hunger: " + str(self.employee_controller.employee_service.employee_list[0]._needs.hunger), True,
            (255, 255, 255))
        self.stress = self.font.render(
            "Stress: " + str(self.employee_controller.employee_service.employee_list[0]._needs.stress), True,
            (255, 255, 255))

        self.motivation = self.font.render(
            "Motivation: " + str(self.employee_controller.employee_service.employee_list[0]._needs.motivation), True,
            (255, 255, 255))
        self.clock_time = self.font.render("Time: " + self.interface_service.get_clock_progress_str(), True, (255, 255, 255))

    def draw(self):
        for floor in range(0, len(self.building_controller.get_room_board())):
            for room in self.building_controller.get_room_board()[floor]:
                self.screen.blit(room.image, room.rect)
                # for action_obj in room.action_objects:
                #     pygame.draw.rect(self.screen,(0,0,0),action_obj.rect)
        if self.mouse_controller.cursor.drags_room():
            self.screen.blit(self.mouse_controller.cursor.image, self.mouse_controller.cursor.rect.move(-150, -150))
        for emp in self.employee_controller.employee_service.employee_list:
            self.screen.blit(emp.image, emp.rect)

        # draw all elements of interface
        for element in self.interface_service.element_list:
            # icons should always be displayed and elements should only be displayed if user clicked on icon
            if issubclass(element.__class__, StaticElement) or self.interface_service.view_type != self.interface_service.NO_TYPE:
                # draw hover effect
                if element.hover_effect == element.DROP_SHADOW:
                    self.screen.blit(element.hover_surface, element.rect)
                self.screen.blit(element.image, element.rect)

        # draw different views based on which icon user clicked
        if self.interface_service.view_type == self.interface_service.HIRE_EMPLOYEE:
            self.screen.blit(self.interface_service.hire_element.get_emp_image(), self.interface_service.hire_element.rect)
        elif self.interface_service.view_type == self.interface_service.PURCHASE_ROOM:
            self.screen.blit(self.interface_service.building_element.get_room_image(), self.interface_service.building_element.rect)
        elif self.interface_service.view_type == self.interface_service.CALENDAR:
            self.screen.blit(self.interface_service.calendar_element.image, self.interface_service.calendar_element.rect)
            self.screen.blit(self.interface_service.calendar_element.page_images[self.interface_service.calendar_element.current_page],
                             self.interface_service.calendar_element.page_rect)
            pygame.draw.rect(self.screen, (255, 0, 0), self.interface_service.calendar_element.page_marker_rect, 3)

        pygame.draw.line(self.screen, (0, 0, 0), (397, 55), self.interface_service.clock_element.clk_pointer, 5)
        # self.screen.blit(self.hunger, self.text_rect.move(0, 125))
        # self.screen.blit(self.stress, self.text_rect.move(0, 100))
        # self.screen.blit(self.motivation, self.text_rect.move(0, 150))

    def init_objects(self):
        self.ground = Ground(self.screen)
        self.company = Company()

        self.interface_service = InterfaceService()
        self.building_controller = BuildingController()
        self.employee_controller = EmployeeController(self.building_controller.get_room_board(), self.ground, self.company,
                                                      self.interface_service)
        self.mouse_controller = MouseController(self.screen, self.employee_controller.employee_service.employee_list,
                                                self.building_controller, self.ground, self.interface_service)
        self.keyboard_controller = KeyboardController(self.employee_controller, self.mouse_controller, self.company)

        self.employee_controller.create_employee(100, 200)
        self.building_controller.build_room((0, 0), RoomType.CORRIDOR)
        self.building_controller.build_room((1, 0), RoomType.DINING_ROOM)
        self.building_controller.build_room((2, 0), RoomType.OFFICE_ROOM)
        self.building_controller.build_room((3, 0), RoomType.ELEVATOR)
        self.building_controller.build_room((4, 0), RoomType.CORRIDOR)
        self.building_controller.build_room((5, 0), RoomType.CONFERENCE_ROOM)
        self.building_controller.build_room((6, 0), RoomType.CORRIDOR)

        self.first_room = self.building_controller.building_service.room_board[0][0]

        # self.employee_controller.create_employee(120, 280, "Bob2", self._company)
        self.employee_controller.employee_service.employee_list[0]._needs.hunger = 20
        self.employee_controller.employee_service.employee_list[0]._needs.stress = 20

    def init_texts(self):
        self.font = pygame.font.SysFont("Calibri", 24, True)
        self.paper_sold = self.font.render("Paper sold: ", True, (255, 255, 255))
        self.money = self.font.render("Money: ", True, (255, 255, 255))
        self.text_rect = pygame.Rect(0, 0, 1, 1)

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
