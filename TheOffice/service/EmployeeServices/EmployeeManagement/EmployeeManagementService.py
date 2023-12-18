from pygame import time, mouse

from model.Employee.Employee import Employee
from model.Ground import Ground
from service.EmployeeServices.EmployeeManagement.AnimationService import AnimationService
from service.EmployeeServices.EmployeeManagement.CollisionService import CollisionService
from service.EmployeeServices.EmployeeManagement.DestinationSearchService import DestinationSearchService
from service.EmployeeServices.Needs.NeedsService import NeedsService
from service.EmployeeServices.Needs.TaskService import TaskService
from service.EmployeeThreads.EmployeeNeedThread import EmployeeNeedThread
from service.EmployeeThreads.EmployeeTaskThread import EmployeeTaskThread


class EmployeeManagementService:
    def __init__(self, room_board, ground: Ground):
        self.employee_list = []
        self.init_extras()
        self.room_board = room_board
        self.ground = ground
        self.initial_ticks = time.get_ticks()
        self.init_threads()
        self.init_services()

    def check_employees_needs_and_move(self):
        for emp in self.employee_list:
            self.check_emp_needs_and_move(emp)
            if not emp.is_sitting_down():
                self.gravity_employee(emp)

    def check_emp_needs_and_move(self, emp: Employee):
        if emp.destination is None:
            # the moment when employee starts feeling hungry
            if emp.is_hungry():
                self.task_service_t.pop_emp(emp, "work")
                self.task_service_t.pop_emp(emp, "stress")
                self.dest_service.search_for_room(emp, "DiningRoom")
            elif emp.is_stressed():
                if not emp.is_eating():
                    self.task_service_t.pop_emp(emp, "hunger")
                    self.task_service_t.pop_emp(emp, "work")
                    self.dest_service.search_for_room(emp, "GameRoom")
            # when employee just stands on ground
            elif emp.is_idle():
                self.task_service_t.pop_emp(emp, "hunger")
                self.task_service_t.pop_emp(emp, "stress")
                self.dest_service.search_for_room(emp, "OfficeRoom")
        # movement logic towards destination
        if emp.destination is not None and not emp.is_dragged() and self.ground.is_touching_adjusted(emp):
            if emp.is_sitting_down():
                emp.remove_from_desk()
            self.move_emp_towards_destination(emp)
            if self.dest_service.emp_arrived_at_destination(emp):
                self.dest_service.change_destination(emp, self.dest_service.search_destination(emp))

    def create_employee(self, x, y, name, company):
        emp = Employee(x, y, name, company)
        self.employee_list.append(emp)
        self.needs_service_t.insert_emp(emp)

    def init_extras(self):
        self.dragged_emp_i = -1

    def init_threads(self):
        self.emp_task_thread = EmployeeTaskThread()
        self.emp_need_thread = EmployeeNeedThread()
        self.task_service_t = TaskService(self.emp_task_thread)
        self.needs_service_t = NeedsService(self.emp_need_thread)
        self.emp_task_thread.start()
        self.emp_need_thread.start()

    def init_services(self):
        self.dest_service = DestinationSearchService(self.room_board, self.task_service_t)
        self.collision_service = CollisionService(self.room_board, self.task_service_t)
        self.animation_service = AnimationService()

    def drag_emp_if_selected(self):
        if self.dragged_emp_i != -1:
            self.employee_list[self.dragged_emp_i].rect.centerx = mouse.get_pos()[0]
            self.employee_list[self.dragged_emp_i].rect.centery = mouse.get_pos()[1]

    def pick_up_employee(self, index):
        if self.employee_list[index].rect.collidepoint(mouse.get_pos()):
            self.dragged_emp_i = index
            self.collision_service.handle_emp_desk_detach_event(self.employee_list[self.dragged_emp_i])

    def put_down_employee(self, index):
        if self.employee_list[index].rect.collidepoint(mouse.get_pos()):
            self.collision_service.handle_emp_desk_collide(self.employee_list[self.dragged_emp_i])
        self.dragged_emp_i = -1

    def move_emp_towards_destination(self, emp):
        x = 0
        emp.direction = ''
        if emp.destination.rect.x > emp.rect.x + 5:
            x = 5
            emp.direction = 'R'
        elif emp.destination.rect.x < emp.rect.x - 5:
            x = -5
            emp.direction = 'L'
        emp.rect = emp.rect.move(x, 0)
        self.animation_service.animate_employee(emp)

    def gravity_employee(self, emp: Employee):
        if not self.ground.is_touching(emp):
            emp.rect = emp.rect.move(0, 12)

    def delay_by_frames(self, frames):
        delay = time.get_ticks() - self.initial_ticks
        if delay > frames:
            self.initial_ticks = time.get_ticks()
        return delay <= frames
