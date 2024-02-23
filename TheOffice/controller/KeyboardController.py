import pygame


class KeyboardController:
    def __init__(self, employee_controller, building_controller, company):
        self.employee_controller = employee_controller
        self.building_controller = building_controller
        self._company = company

    def execute_event(self, e):
        if e.type is pygame.QUIT:
            self.employee_controller.employee_service.emp_need_thread.destroy()
            self.employee_controller.employee_service.emp_task_thread.destroy()
            pygame.sys.exit(0)
        if e.type == pygame.KEYDOWN:
            if e.key is pygame.K_q:
                print("pressed")
                self.employee_controller.create_employee(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], self._company)
            elif e.key is pygame.K_1:
                self.building_controller.build_office((5, 0))
            elif e.key is pygame.K_2:
                self.building_controller.build_dining_room((5, 0))
            elif e.key is pygame.K_3:
                self.building_controller.build_game_room((5, 0))