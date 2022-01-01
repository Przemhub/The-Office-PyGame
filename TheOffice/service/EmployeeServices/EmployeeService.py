import pygame

from model.Employee.Employee import Employee
from service.EmployeeServices.ConsumeService import ConsumeService
from service.EmployeeServices.NeedsService import NeedsService
from service.EmployeeServices.WorkingService import WorkingService


class EmployeeService:
    def __init__(self, room_board):
        self.employee_list = []
        self.init_extras()
        self.room_board = room_board
        self.init_threads()

    def init_threads(self):
        self.hustle_thread = WorkingService()
        self.consumer_thread = ConsumeService()
        self.needs_thread = NeedsService()
        self.hustle_thread.start()
        self.needs_thread.start()
        self.consumer_thread.start()

    def create_employee(self, x, y, name, company):
        emp = Employee(x, y, name, company)
        self.employee_list.append(emp)
        self.needs_thread.insert_emp(emp)

    def init_extras(self):
        self.dragged_emp_i = -1

    def drag_emp_if_selected(self):
        if self.dragged_emp_i != -1:
            self.employee_list[self.dragged_emp_i].rect.centerx = pygame.mouse.get_pos()[0]
            self.employee_list[self.dragged_emp_i].rect.centery = pygame.mouse.get_pos()[1]

    def pick_up_employee(self, index):
        if self.employee_list[index].rect.collidepoint(pygame.mouse.get_pos()):
            self.dragged_emp_i = index
            self.handle_emp_desk_detach_event(self.employee_list[self.dragged_emp_i])

    def put_down_employee(self, index):
        print(index)
        print(self.employee_list[index].rect)
        if self.employee_list[index].rect.collidepoint(pygame.mouse.get_pos()):
            self.handle_emp_desk_collide_event(self.employee_list[self.dragged_emp_i])
        self.dragged_emp_i = -1

    def handle_emp_desk_detach_event(self, emp):
        if emp.desk_observer != None:
            emp.desk_observer.taken = False
            emp.detach_action_object()
            try:
                self.hustle_thread.pop_emp(emp)
            except:
                self.consumer_thread.pop_emp(emp)

    def handle_emp_desk_collide_event(self, emp):
        for floor_i in range(0, len(self.room_board)):
            room_list = list(self.room_board[floor_i].values())
            for room_i in range(0, len(self.room_board[floor_i])):
                for desk_i in range(0, len(room_list[room_i].action_objects)):
                    # print(type(room_list[room_i]).__name__)
                    # print("table rect ", room_list[room_i].action_objects[desk_i].rect)
                    # print("emp rect" ,emp.rect)
                    # print("dolided?",emp.rect.colliderect(room_list[room_i].action_objects[desk_i].rect))
                    if emp.rect.colliderect(room_list[room_i].action_objects[desk_i].rect):
                        # print("Collision detected with:", emp.name)
                        # print("czy taken?", self.action_object_taken(room_list, room_i, desk_i))
                        if self.action_object_taken(room_list, room_i, desk_i) == False:
                            if type(room_list[room_i]).__name__ == "DiningRoom":
                                self.consumer_thread.insert_emp(emp)
                                # print(self.consumer_thread.emp_dict)
                            elif type(room_list[room_i]).__name__ == "OfficeRoom":
                                self.hustle_thread.insert_emp(emp)
                            self.adjust_emp_to_desk(emp, room_list[room_i].action_objects[desk_i], room_list[room_i])
                            self.update_rooms_desk_status(room_list, room_i, desk_i, True)
                            emp.attach_desk(room_list[room_i].action_objects[desk_i])

    def adjust_emp_to_desk(self, emp, desk, room):
        if type(room).__name__ == "DiningRoom":
            emp.sitting_sprite()
            emp.rect.y = desk.rect.y - 30
            emp.rect = emp.rect.move(-20, 0)

    def check_every_employee(self):
        for emp in self.employee_list:
            self.check_needs_and_move(emp)

    def check_needs_and_move(self, emp):
        # only use it once when the needs are below threshold
        if emp.destination_room is None:
            if emp._needs.hunger <= 10:
                for floor_i in range(0, len(self.room_board)):
                    room_list = list(self.room_board[floor_i].values())
                    for room_i in range(0, len(self.room_board[floor_i])):
                        if emp.rect.colliderect(room_list[room_i].rect):
                            room_dist = 1
                            while True:
                                if room_i + room_dist < len(room_list):
                                    if type(room_list[room_i + room_dist]).__name__ == "DiningRoom":
                                        emp.destination_room = room_list[room_i + room_dist]
                                        break
                                if room_i - room_dist >= 0:
                                    if type(room_list[room_i - room_dist]).__name__ == "DiningRoom":
                                        emp.destination_room = room_list[room_i - room_dist]
                                        break
                                if room_i - room_dist < 0 and room_i + room_dist >= len(room_list):
                                    break
                                room_dist += 1
        else:
            self.move_to_destination(emp)

    def move_to_destination(self, emp):
        x = 0
        y = 0
        if emp.destination_room.rect.x > emp.rect.x:
            x = 5
        elif emp.destination_room.rect.x < emp.rect.x:
            x = -5
        else:
            emp.destination_room = None
            return
        emp.rect = emp.rect.move(x, y)

    def action_object_taken(self, room_list, room_i, desk_i):
        action_object = room_list[room_i].action_objects[desk_i]
        # print(type(action_object.taken).__name__)
        # print("tru czynie tru",(action_object.taken == True and action_object.taken == True))
        if type(action_object.taken).__name__ != "list":
            return action_object.taken
        return (action_object.taken[0] == True and action_object.taken[1] == True)

    def update_rooms_desk_status(self, room_list, room_i, desk_i, status):
        room_list[room_i].action_objects[desk_i].taken = status
